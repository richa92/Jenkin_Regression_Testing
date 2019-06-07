""" datavarable  for ovf6853."""
import os

cwd = os.getcwd()
download_to_path = cwd


def make_range_list(start, end, prefix='net_', suffix=''):
    """ function for rangelist."""
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist


SSH_PASS = 'hpvse1'

LIG = 'LIG1'
EG = 'EG'
ENC1 = 'enc1'
LI = ENC1 + '-' + LIG

# change Applaince ip
APPLIANCE_IP = '15.186.22.215'

appliance_cred = ['root', 'hpvse1']

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

serveradmin = {'userName': 'Serveradmin', 'password': 'Serveradmin'}

network_admin = {'userName': 'Networkadmin', 'password': 'Networkadmin'}

backup_admin = {'userName': 'Backupadmin', 'password': 'Backupadmin'}

readonly_user = {'userName': 'readonly', 'password': 'readonly'}

vcenter = {'server': '15.199.230.130', 'user': 'GopalK', 'password': 'hpvse1'}

network_sets = [{"name": "set1", "networkUris": ["eth_10"], "connectionTemplateUri":None, "type":"network-setV5", "nativeNetworkUri":None},
                {"name": "set2", "networkUris": ["eth_20", "eth_30"], "connectionTemplateUri":None, "type":"network-setV5", "nativeNetworkUri":None},
                {"name": "set3", "networkUris": ["eth_40"], "connectionTemplateUri":None, "type":"network-setV5", "nativeNetworkUri":None},
                {"name": "set4", "networkUris": ["eth_40"], "connectionTemplateUri":None, "type":"network-setV5", "nativeNetworkUri":None},
                {"name": "set5", "networkUris": ["eth_50"], "connectionTemplateUri":None, "type":"network-setV5", "nativeNetworkUri":None},
                {"name": "set6", "networkUris": ["eth_50"], "connectionTemplateUri":None, "type":"network-setV5", "nativeNetworkUri":None},
                {"name": "set7", "networkUris": ["eth_10"], "connectionTemplateUri":None, "type":"network-setV5", "nativeNetworkUri":None}]

network_sets1 = [{"name": "set5", "networkUris": ["eth_50"], "connectionTemplateUri":None, "type":"network-setV4", "nativeNetworkUri":None},
                 {"name": "set6", "networkUris": ["eth_50"], "connectionTemplateUri":None, "type":"network-setV4", "nativeNetworkUri":None}]


# users = [{'userName': 'Serveradmin', 'password': 'Serveradmin', 'fullName': 'Serveradmin', 'roles': ['Server administrator','Backup administrator'], 'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'}]
users = [{"type": "UserAndPermissions", "userName": "Networkadmin", "fullName": "", "password": "Networkadmin",
          "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True, "permissions": [{"roleName": "Network administrator", "scopeUri": None}]},
         {"type": "UserAndPermissions", "userName": "Storageadmin", "fullName": "", "password": "Storageadmin",
          "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True, "permissions": [{"roleName": "Storage administrator", "scopeUri": None}]},
         {"type": "UserAndPermissions", "userName": "Backupadmin", "fullName": "", "password": "Backupadmin",
          "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True, "permissions": [{"roleName": "Backup administrator", "scopeUri": None}]},
         {"type": "UserAndPermissions", "userName": "Serveradmin", "fullName": "", "password": "Serveradmin",
          "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True, "permissions": [{"roleName": "Server administrator", "scopeUri": None}]},
         {"type": "UserAndPermissions", "userName": "FullRole", "fullName": "", "password": "Serveradmin",
          "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True, "permissions": [{"roleName": "Infrastructure administrator", "scopeUri": None}]},
         {"type": "UserAndPermissions", "userName": "Software", "fullName": "", "password": "Serveradmin",
          "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True, "permissions": [{"roleName": "Software administrator", "scopeUri": None}]},
         {"type": "UserAndPermissions", "userName": "Readonly", "fullName": "", "password": "Serveradmin",
          "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True, "permissions": [{"roleName": "Read only", "scopeUri": None}]}
         ]


usercred = [{'userName': 'Networkadmin', 'password': 'Networkadmin'},
            {'userName': 'Serveradmin', 'password': 'Serveradmin'},
            {'userName': 'Storageadmin', 'password': 'Storageadmin'},
            {'userName': 'Backupadmin', 'password': 'Backupadmin'},
            {'userName': 'FullRole', 'password': 'Serveradmin'},
            {'userName': 'Software', 'password': 'Serveradmin'},
            {'userName': 'Readonly', 'password': 'Serveradmin'}, ]

LI_dto = {'name': LI}
LE = 'LE'
loggerlevel = r'INFO'   # use INFO|DEBUG

enclosureCount = 1
REDUNDANCY = 'HighlyAvailable'
fcnets = [{"type": "fc-networkV4",
           "name": "FC_1",
           "fabricType": "FabricAttach",
           "linkStabilityTime": 30,
           "autoLoginRedistribution": True
           }]
frame = 2

UPS = {'us': {'name': 'set2',
              'ethernetNetworkType': 'Tagged',
              'networkType': 'Ethernet',
              'networkUris': ['Network2'],
              'networkSetsUri': ['Netset1'],
              'nativeNetworkUri': None,
              'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '1', 'port': 'X5', 'speed': 'Auto'},
                                         ]}}

ethnets = [
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth_10",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 10
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth_20",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 20
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth_30",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 30
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth_40",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 40
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth_50",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 50
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth_60",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 60
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth_70",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 70
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth_80",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 80
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth_90",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 90
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth_100",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 100
    }

]
# us1:Create UplinkSet consisting of Network set
# us2:Create Uplinkset consisting of multiple NetworkSet
# us3:Same uplinkset to multiple Networks
# us4:Same Network to multiple uplinkset
# us5:Uplinkset with non-existent NetworkSet

Same_Network_Different_UplinkSet = {'ups1': {'name': 'set1',
                                             'ethernetNetworkType': 'Tagged',
                                             'networkType': 'Ethernet',
                                             'networkUris': ['Network1'],
                                             'networkSetsUri': ['Netset1'],
                                             'nativeNetworkUri': None,
                                             'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '1', 'port': 'X5', 'speed': 'Auto'}]},
                                    'ups2': {'name': 'set2',
                                             'ethernetNetworkType': 'Tagged',
                                             'networkType': 'Ethernet',
                                             'networkUris': ['Network1'],
                                             'networkSetsUri': ['Netset1'],
                                             'nativeNetworkUri': None,
                                             'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '1', 'port': 'X5', 'speed': 'Auto'},
                                                                        ]}
                                    }

Same_Networkset_Multiple_UplinkSet = {'ups1': {'name': 'set1',
                                               'ethernetNetworkType': 'Tagged',
                                               'networkType': 'Ethernet',
                                               'networkUris': ['Network1', 'Network2'],
                                               'networkSetsUri': ['Netset1'],
                                               'nativeNetworkUri': None,
                                               'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '1', 'port': 'X5', 'speed': 'Auto'}]},
                                      'ups2': {'name': 'set2',
                                               'ethernetNetworkType': 'Tagged',
                                               'networkType': 'Ethernet',
                                               'networkUris': ['Network1'],
                                               'networkSetsUri': ['Netset1'],
                                               'nativeNetworkUri': None,
                                               'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '1', 'port': 'X5', 'speed': 'Auto'},
                                                                          ]}
                                      }
# UplinksetName to get URI
UplinkSet_Name = "set1"
Networks_to_be_removed = ["Network3", "Network4"]

# 'us2': {'name': 'us2',
#                       'ethernetNetworkType': 'Tagged',
#                       'networkType': 'Ethernet',
#                       'networkUris': [],
#                       'nativeNetworkUri': None,
#                       'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': '1', 'speed': 'Auto'},
#                                                  {'enclosure': '1', 'bay': '3', 'port': '2', 'speed': 'Auto'}
#                                                  ]}
icmap_1 = \
    [
        {'bay': 1, 'enclosure': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module', 'enclosureIndex': 1},
        {'bay': 2, 'enclosure': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module', 'enclosureIndex': 2}
    ]

Netset = [{"name": "Netset1", "networkUris": ["Network1", "Network2", "Network3"], "connectionTemplateUri":None, "type": "network-setV4", "nativeNetworkUri": None, "networkSetType":"Regular", "initialScopeUris":[]},
          {"name": "Netset2", "networkUris": " ", "connectionTemplateUri": None, "type": "network-setV4", "nativeNetworkUri": None, "networkSetType": "Regular", "initialScopeUris": []},
          {"name": "Netset3", "networkUris": " ", "connectionTemplateUri": None, "type": "network-setV4", "nativeNetworkUri": None, "networkSetType": "Regular", "initialScopeUris": []}]

NetSet1_asso_Net = [{"name": "Netset1_asso_1", "networkUris": ["Network1_asso_1", "Network2_asso_2"], "connectionTemplateUri":None, "type":"network-setV4", "nativeNetworkUri": None, "networkSetType":"Regular", "initialScopeUris":[]},
                    {"name": "NetSet2_asso_1", "networkUris": ["Network1_asso_1", "Network2_notasso_2"], "connectionTemplateUri":None, "type":"network-setV4", "nativeNetworkUri": None, "networkSetType":"Regular", "initialScopeUris":[]}]

update_network_sets1 = [{"name": ["Netsetsame1", "Netsetsame2"], "networkUris": ["Network1", "Network2", "Network3"], "delete_networkUris":["Network1"], "connectionTemplateUri":None, "type":"network-setV5", "nativeNetworkUri":None}]

update_network_sets2 = [{"name": ["Netsetsame1"], "networkUris": ["Network2", "Network3"], "delete_networkUris":["Network2"], "connectionTemplateUri":None, "type":"network-setV5", "nativeNetworkUri":None}]

Networkset_Name_SameNetworks_Uplinkset = [{"name": "Netsetsame1", "networkUris": ["Network1", "Network2", "Network3"], "connectionTemplateUri":None, "type":"network-setV4", "nativeNetworkUri": None, "networkSetType":"Regular", "initialScopeUris":[]},
                                          {"name": "Netsetsame2", "networkUris": ["Network1", "Network2", "Network3"], "connectionTemplateUri":None, "type":"network-setV4", "nativeNetworkUri": None, "networkSetType":"Regular", "initialScopeUris":[]}]

Networkset_Name_SameNetworks_Uplinkset = [{"name": "Netsetsame1", "networkUris": ["Network1", "Network2", "Network3"], "connectionTemplateUri":None, "type":"network-setV4", "nativeNetworkUri": None, "networkSetType":"Regular", "initialScopeUris":[]},
                                          {"name": "Netsetsame2", "networkUris": ["Network1", "Network2", "Network3"], "connectionTemplateUri":None, "type":"network-setV4", "nativeNetworkUri": None, "networkSetType":"Regular", "initialScopeUris":[]}]

Networkset_Same_Uplinkset = {'us5': {'name': 'set5',
                                     'ethernetNetworkType': 'Tagged',
                                     'networkType': 'Ethernet',
                                     'networkUris': ['Network3', 'Network4'],
                                     'networkSetsUri': [''],
                                     'nativeNetworkUri': None,
                                     'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '1', 'port': 'X6', 'speed': 'Auto'},
                                                                ]}}


Network_to_NetworkSet_check_Uplinkset = [{"name": "Netsetsame1", "networkUris": ["Network1", "Network2", "Network3"]}]
ethernet_network2 = [{"vlanId": "401",
                      "purpose": "Management",
                      "name": "network1",
                      "smartLink": False,
                      "privateNetwork": False,
                      "connectionTemplateUri": None,
                      "NetworkSet": "",
                      "ethernetNetworkType": "Tagged",
                      "type": "ethernet-networkV4"},
                     {"vlanId": "402",
                      "purpose": "Management",
                      "name": "network2",
                      "smartLink": False,
                      "privateNetwork": False,
                      "connectionTemplateUri": None,
                      "NetworkSet": "NetworkSetdoesntexist",
                      "ethernetNetworkType": "Tagged",
                      "type": "ethernet-networkV4"},
                     {"vlanId": "403",
                      "purpose": "Management",
                      "name": "fvt4network3",
                      "smartLink": False,
                      "privateNetwork": False,
                      "connectionTemplateUri": None,
                      "NetworkSet": "NetSet1",
                      "ethernetNetworkType": "Tagged",
                      "type": "ethernet-networkV4"},
                     {"vlanId": "404",
                      "purpose": "Management",
                      "name": "network4",
                      "smartLink": False,
                      "privateNetwork": False,
                      "NetworkSet": "NetSet2",
                      "connectionTemplateUri": None,
                      "ethernetNetworkType": "Tagged",
                      "type": "ethernet-networkV4"},
                     {"vlanId": "405",
                      "purpose": "Management",
                      "name": "network5",
                      "smartLink": False,
                      "privateNetwork": False,
                      "connectionTemplateUri": None,
                      "ethernetNetworkType": "Tagged",
                      "type": "ethernet-networkV4"},
                     {"vlanId": "406",
                      "purpose": "Management",
                      "name": "network6",
                      "smartLink": False,
                      "privateNetwork": False,
                      "connectionTemplateUri": None,
                      "ethernetNetworkType": "Tagged",
                      "type": "ethernet-networkV4"},
                     {"vlanId": "407",
                      "purpose": "Management",
                      "name": "network7",
                      "smartLink": False,
                      "privateNetwork": False,
                      "connectionTemplateUri": None,
                      "ethernetNetworkType": "Tagged",
                      "type": "ethernet-networkV4"}]

ethernet_network3 = [{"vlanId": "401",
                      "purpose": "Management",
                      "name": "network_1",
                      "smartLink": False,
                      "privateNetwork": False,
                      "connectionTemplateUri": None,
                      "NetworkSet": "Network_set_1",
                      "ethernetNetworkType": "Tagged",
                      "type": "ethernet-networkV4"},
                     {"vlanId": "402",
                      "purpose": "Management",
                      "name": "network_1",
                      "smartLink": False,
                      "privateNetwork": False,
                      "connectionTemplateUri": None,
                      "NetworkSet": "Network_set_1",
                      "ethernetNetworkType": "Tagged",
                      "type": "ethernet-networkV4"}]

NetworkSet = ["NetworkSet1"]

server_profiles_edit = [{'type': 'ServerProfileV10',
                         'serverHardwareUri': 'enc1' + ', bay 8',
                         'serverHardwareTypeUri': '',
                         'enclosureUri': 'ENC:' + 'enc1',
                         'enclosureGroupUri': 'EG:config1-group',
                         'serialNumberType': 'Virtual',
                         'macType': 'Virtual',
                         'wwnType': 'Virtual',
                         'name': 'Profile_server1',
                         'description': '',
                         'affinity': 'Bay',
                         'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                         'boot': {'manageBoot': True, 'order': ['HardDisk']},
                         'connectionSettings': {'connections': [{'id': 1,
                                                                 'name': 'conn-net1',
                                                                 'functionType': 'Ethernet',
                                                                 'portId': 'Flb 1:1-a',
                                                                 'requestedMbps': 2500,
                                                                 'networkUri': 'ETH:network1',
                                                                 # 'networksetUri': multiple_network_set,
                                                                 'mac': None,
                                                                 'wwpn': None,
                                                                 'wwnn': None}]}},
                        {'type': 'ServerProfileV10',
                         'serverHardwareUri': 'enc1' + ', bay 8',
                         'serverHardwareTypeUri': '',
                                                  'enclosureUri': 'ENC:' + 'enc1',
                                                  'enclosureGroupUri': 'EG:config1-group',
                                                  'serialNumberType': 'Virtual',
                                                  'macType': 'Virtual',
                                                  'wwnType': 'Virtual',
                                                  'name': 'Profile_server2',
                                                  'description': '',
                                                  'affinity': 'Bay',
                                                  'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                         'boot': {'manageBoot': True, 'order': ['HardDisk']},
                         'connectionSettings': {'connections': [{'id': 1,
                                                                 'name': 'conn-net1',
                                                                 'functionType': 'Ethernet',
                                                                 'portId': 'Flb 1:1-a',
                                                                 'requestedMbps': 2500,
                                                                 'networkUri': 'ETH:network1',

                                                                 'mac': None,
                                                                 'wwpn': None,
                                                                 'wwnn': None}]}}
                        ]

ilo_details_enc2_bay6 = {'ilo_ip': '15.245.132.58', 'username': 'Administrator', 'password': 'hpvse123'}

ping_file = ['ping_serverip0.txt', 'ping_serverip1.txt', 'ping_serverip2.txt', 'ping_serverip3.txt', 'ping_serverip4.txt', 'ping_serverip5.txt', 'ping_serverip6.txt', 'ping_serverip7.txt']

multiple_network_set = ["netset1", "netset2", "netset3"]

Networks_removed = ['Network2']
Networks_removed_1 = ['Network2', 'Network3']

NS = [{"name": "NS1", "networkUris": ["N1", "N2", "N3"], "connectionTemplateUri":None, "type": "network-setV4", "nativeNetworkUri": None, "networkSetType":"Regular", "initialScopeUris":[]},
      {"name": "NS2", "networkUris": ["N1"], "connectionTemplateUri":None, "type":"network-setV4", "nativeNetworkUri": None, "networkSetType":"Regular", "initialScopeUris":[]}]

uplink_sets_Int_network = {'us': {'name': 'set_int',
                                  'ethernetNetworkType': 'Tagged',
                                  'networkType': 'Ethernet',
                                  'networkUris': ['fvt-Network1_Int'],
                                  'networkSetsUri': ['Netset1'],
                                  'nativeNetworkUri': None,
                                  'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '1', 'port': 'X5', 'speed': 'Auto'},
                                                             ]}}

uplink_sets_Delete_networkset = {'us': {'name': 'set2',
                                        'ethernetNetworkType': 'Tagged',
                                        'networkType': 'Ethernet',
                                        'networkUris': [],
                                        'networkSetsUri': ['Netset1'],
                                        'nativeNetworkUri': None,
                                        'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '1', 'port': 'X5', 'speed': 'Auto'},
                                                                   ]}}
# Add port information based on which enlosure you are using


uplink_set1 = {'US2': {
    'type': 'uplink-setV5',
    'name': 'US_Unsplitter',
    'portConfigInfos': [],
    'networkType': 'Ethernet',
    'manualLoginRedistributionState': 'NotSupported',
    'logicalInterconnectUri': "",  # user should defined logical interconnect name
    'connectionMode': 'Auto',
    'networkUris': ['eth_500', 'non-existing'],
    'fcNetworkUris': [],  # user should defined fabric channel name
    'fcoeNetworkUris': []
}}

uplinkset2 = {
    'type': 'uplink-setV5',
    'name': 'US1',
    'portConfigInfos': [],
    'networkType': 'Ethernet',
    'manualLoginRedistributionState': 'NotSupported',
    'logicalInterconnectUri': "",  # user should defined logical interconnect name
    'connectionMode': 'Auto',
    'networkUris': ['eth_10'],
    'fcNetworkUris': [],  # user should defined fabric channel name
    'fcoeNetworkUris': []}

uplinkset31 = {
    'type': 'uplink-setV5',
    'name': 'US_PF',
    'portConfigInfos': [],
    'networkType': 'Ethernet',
    'manualLoginRedistributionState': 'NotSupported',
    'logicalInterconnectUri': "",  # user should defined logical interconnect name
    'connectionMode': 'Auto',
    'networkUris': ['eth_10'],
    'fcNetworkUris': [],  # user should defined fabric channel name
    'fcoeNetworkUris': []}

US_duplicate_NS1 = {
    'type': 'uplink-setV5',
    'name': 'US_duplicate_NS',
    'portConfigInfos': [],
    'networkType': 'Ethernet',
    'manualLoginRedistributionState': 'NotSupported',
    'logicalInterconnectUri': "",  # user should defined logical interconnect name
    'connectionMode': 'Auto',
    'networkUris': ['set6'],
    'fcNetworkUris': [],  # user should defined fabric channel name
    'fcoeNetworkUris': []}


SP_NS = [{'type': 'ServerProfileV11', 'serverHardwareUri': ENC1 + ', bay 6',
          'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + EG,
          'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
          'name': 'profile_bay3', 'description': '', 'affinity': 'Bay',
          "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
          'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Auto',
                                                  'requestedMbps': '2500', 'networkUri': 'NS:set1', 'mac': None, 'wwpn': None, 'wwnn': None},

                                                 ]}}]
lig_uplink_sets1 = {'US1': {'name': 'US1', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['eth_10'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                    'logicalPortConfigInfos': [],
                            },
                    'US2': {'name': 'US2', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['eth_30'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                            'logicalPortConfigInfos': [],
                            'US5': {'name': 'US5', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['eth_40'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                    'logicalPortConfigInfos': [],
                                    },
                            'US6': {'name': 'US6', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['eth_50'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                    'logicalPortConfigInfos': [],
                                    }}}

# Add net30 and net40 in internal networks
ligs = {'lig1':
        {'name': 'LIG1',
         'type': 'logical-interconnect-groupV4',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC 16Gb 24-Port FC Module'}],
         'interconnectBaySet': 3,
         'redundancyType': 'Redundant',
         "internalNetworkUris": ["eth_50"],
         'uplinkSets': [],
         'ethernetSettings': None,
         'state': None,
         'telemetryConfiguration': None,
         'snmpConfiguration': None}
        }

eg_body1 = {'name': 'EG',
            'interconnectBayMappings':
                [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:' + 'LIG1'},
                 {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:' + 'LIG1'},
                 {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:' + 'LIG1'},
                 {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:' + 'LIG1'}],
            'ipRangeUris': [],
            'enclosureCount': 1,
            'osDeploymentSettings': None,
            'configurationScript': None,
            'powerMode': None,
            'ambientTemperatureMode': 'Standard'}

encs = [{'hostname': '15.186.18.129', 'username': 'Administrator', 'password': 'compaq', 'enclosureGroupUri': 'EG:EG', 'force': False, 'licensingIntent': 'OneViewNoiLO'}]

# change this based on the connections given
port = ['LOM 1:1-a']

server_details = {'windows_ip': '', 'username': 'Administrator', 'password': 'hpvse@1'}
# change the ilo ip as required
ilo_details = {'ilo_ip': '15.245.133.62', 'username': 'Administrator', 'password': 'hpvse123'}
ping_cmd1 = ["cmd /c ping -n 10 -l 1024 gateway_ip>sample.txt"]
server_credentials = {'userName': 'Administrator', 'password': 'password@123'}
pingfile = 'sample.txt'
Ping_Lost = 'Lost'
number = 5
flag = 'Windows'
Powershell_get_mac = "Get-NetAdapter | where MacAddress -eq 'pppppppp' | Select Name"
Powershell_get_mac1 = "New-netlbfoteam -name 'Team1' -TeamMembers 'pppp','qqq' -TeamingMode 'LACP'"
detlete_team_cmd0 = "Remove-NetLbfoTeam 'Team1'"
team_status_cmd0 = "Get-NetLbfoTeam -Name 'Team1' | fl Name,Status"
tagging_cmd = "Set-NetAdapter -Name 'adapter_name' -VlanId 'vlan_id'"

uplinkset3 = {
    'type': 'uplink-setV6',
    'name': 'US_PF',
    'portConfigInfos': [{"desiredSpeed": "Auto", "location": {"locationEntries": [{"value": "X1", "type": "Port"}, {"value": 1, "type": "Bay"},
                                                                                  {"value": ENC1, "type": "Enclosure"}]}}],
    'networkType': 'Ethernet',
    'manualLoginRedistributionState': 'NotSupported',
    'logicalInterconnectUri': "",  # user should defined logical interconnect name
    'connectionMode': 'Auto',
    'networkUris': [],
    'fcNetworkUris': [],  # user should defined fabric channel name
    'fcoeNetworkUris': [],
    'networkSetUris': []
}

uplinkset4 = {
    'type': 'uplink-setV6',
    'name': 'US_PF1',
    'portConfigInfos': [{"desiredSpeed": "Auto", "location": {"locationEntries": [{"value": "X2", "type": "Port"}, {"value": 1, "type": "Bay"},
                                                                                  {"value": ENC1, "type": "Enclosure"}]}}],
    'networkType': 'Ethernet',
    'manualLoginRedistributionState': 'NotSupported',
    'logicalInterconnectUri': "",  # user should defined logical interconnect name
    'connectionMode': 'Auto',
    'networkUris': [],
    'fcNetworkUris': [],  # user should defined fabric channel name
    'fcoeNetworkUris': [],
    'networkSetUris': []
}

uplinkset5 = {
    'type': 'uplink-setV6',
    'name': 'US_PF1',
    'portConfigInfos': [{"desiredSpeed": "Auto", "location": {"locationEntries": [{"value": "X5", "type": "Port"}, {"value": 1, "type": "Bay"},
                                                                                  {"value": ENC1, "type": "Enclosure"}]}}],
    'networkType': 'Ethernet',
    'manualLoginRedistributionState': 'NotSupported',
    'logicalInterconnectUri': "",  # user should defined logical interconnect name
    'connectionMode': 'Auto',
    'networkUris': [],
    'fcNetworkUris': [],  # user should defined fabric channel name
    'fcoeNetworkUris': [],
    'networkSetUris': []
}

uplink_set_non_existing_network_set = {
    'type': 'uplink-setV6',
    'name': 'US_Unsplitter',
    'portConfigInfos': [],
    'networkType': 'Ethernet',
    'manualLoginRedistributionState': 'NotSupported',
    'logicalInterconnectUri': "",  # user should defined logical interconnect name
    'connectionMode': 'Auto',
    'networkUris': [],
    'fcNetworkUris': [],  # user should defined fabric channel name
    'fcoeNetworkUris': [],
    'networkSetUris': ['Netset10']
}

uplinkset6 = {
    'type': 'uplink-setV6',
    'name': 'US_PF1',
    'portConfigInfos': [{"desiredSpeed": "Auto", "location": {"locationEntries": [{"value": "X4", "type": "Port"}, {"value": 1, "type": "Bay"},
                                                                                  {"value": ENC1, "type": "Enclosure"}]}}],
    'networkType': 'Ethernet',
    'manualLoginRedistributionState': 'NotSupported',
    'logicalInterconnectUri': "",  # user should defined logical interconnect name
    'connectionMode': 'Auto',
    'networkUris': ['eth_10'],
    'fcNetworkUris': [],  # user should defined fabric channel name
    'fcoeNetworkUris': [],
    'networkSetUris': ['set7']
}

US_duplicate_NS = {
    'type': 'uplink-setV6',
    'name': 'US_Duplicate',
    'portConfigInfos': [{"desiredSpeed": "Auto", "location": {"locationEntries": [{"value": "X6", "type": "Port"}, {"value": 1, "type": "Bay"},
                                                                                  {"value": ENC1, "type": "Enclosure"}]}}],
    'networkType': 'Ethernet',
    'manualLoginRedistributionState': 'NotSupported',
    'logicalInterconnectUri': "",  # user should defined logical interconnect name
    'connectionMode': 'Auto',
    'networkUris': ['eth_50', 'eth_40'],
    'fcNetworkUris': [],  # user should defined fabric channel name
    'fcoeNetworkUris': [],
    'networkSetUris': ['set6']
}

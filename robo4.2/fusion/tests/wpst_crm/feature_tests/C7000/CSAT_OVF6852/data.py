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

APPLIANCE_IP = '15.186.22.215'

appliance_cred = ['root', 'hpvse1']

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

serveradmin = {'userName': 'Serveradmin', 'password': 'Serveradmin'}

network_admin = {'userName': 'Networkadmin', 'password': 'Networkadmin'}

backup_admin = {'userName': 'Backupadmin', 'password': 'Backupadmin'}

readonly_user = {'userName': 'readonly', 'password': 'readonly'}

vcenter = {'server': '15.199.230.130', 'user': 'GopalK', 'password': 'hpvse1'}

users = [{'userName': 'Serveradmin', 'password': 'Serveradmin', 'fullName': 'Serveradmin', 'roles': ['Server administrator', 'Backup administrator'], 'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'}]

LIG = 'LIG1'
EG = 'EG'
ENC1 = 'enc1'
LI = ENC1 + '-' + LIG
LI_dto = {'name': LI}
LE = 'LE'
IC_bay_set = 1
IC_bay_set_pair = IC_bay_set + 3
loggerlevel = r'INFO'

enclosureCount = 1
IBS = 3
REDUNDANCY = 'HighlyAvailable'
fcnets = [{"type": "fc-networkV4",
           "name": "FC_1",
           "fabricType": "FabricAttach",
           "linkStabilityTime": 30,
           "autoLoginRedistribution": True
           }]
frame = 2
ethernet_network1 = [{"vlanId": "401",
                      "purpose": "Management",
                      "name": "fvt4network1",
                      "smartLink": False,
                      "privateNetwork": False,
                      "connectionTemplateUri": None,
                      "ethernetNetworkType": "Tagged",
                      "type": "ethernet-networkV4"},
                     {"vlanId": "403",
                      "purpose": "Management",
                      "name": "en1",
                      "smartLink": False,
                      "privateNetwork": False,
                      "connectionTemplateUri": None,
                      "ethernetNetworkType": "Tagged",
                      "type": "ethernet-networkV4"},
                     {"vlanId": "404",
                      "purpose": "Management",
                      "name": "fvt4network4",
                      "smartLink": False,
                      "privateNetwork": False,
                      "connectionTemplateUri": None,
                      "ethernetNetworkType": "Tagged",
                      "type": "ethernet-networkV4"},
                     {"vlanId": "405",
                      "purpose": "Management",
                      "name": "fvt4network5",
                      "smartLink": False,
                      "privateNetwork": False,
                      "connectionTemplateUri": None,
                      "ethernetNetworkType": "Tagged",
                      "type": "ethernet-networkV4"}]

ethernet_network = [{"vlanId": "401",
                     "purpose": "Management",
                     "name": "network1",
                     "smartLink": False,
                     "privateNetwork": False,
                     "connectionTemplateUri": None,
                     "ethernetNetworkType": "Tagged",
                     "type": "ethernet-networkV4"},
                    {"vlanId": "402",
                     "purpose": "Management",
                     "name": "network2",
                     "smartLink": False,
                     "privateNetwork": False,
                     "connectionTemplateUri": None,
                     "ethernetNetworkType": "Tagged",
                     "type": "ethernet-networkV4"},
                    {"vlanId": "403",
                     "purpose": "Management",
                     "name": "fvt4network3",
                     "smartLink": False,
                     "privateNetwork": False,
                     "connectionTemplateUri": None,
                     "ethernetNetworkType": "Tagged",
                     "type": "ethernet-networkV4"},
                    {"vlanId": "404",
                     "purpose": "Management",
                     "name": "network4",
                     "smartLink": False,
                     "privateNetwork": False,
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

uplink_sets = {'us1': {'name': 'set1',
                       'ethernetNetworkType': 'Tagged',
                       'networkType': 'Ethernet',
                       'networkUris': ['Network1'],
                       'nativeNetworkUri': None,
                       'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '1', 'port': 'X5', 'speed': 'Auto'},
                                                  ]},
               }

icmap_1 = \
    [
        {'bay': 1, 'enclosure': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module', 'enclosureIndex': 1},
        {'bay': 2, 'enclosure': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module', 'enclosureIndex': 2}
    ]

Netset = [{"name": "Netset1", "networkUris": "Network1", "connectionTemplateUri": None, "type": "network-setV4", "nativeNetworkUri": None, "networkSetType": "Regular", "initialScopeUris": []},
          {"name": "Netset2", "networkUris": " ", "connectionTemplateUri": None, "type": "network-setV4", "nativeNetworkUri": None, "networkSetType": "Regular", "initialScopeUris": []},
          {"name": "Netset3", "networkUris": " ", "connectionTemplateUri": None, "type": "network-setV4", "nativeNetworkUri": None, "networkSetType": "Regular", "initialScopeUris": []}]

Netset1 = [{"name": "Netset1", "networkUris": [], "connectionTemplateUri":None, "type":"network-setV5", "nativeNetworkUri": None, "networkSetType":"Regular", "initialScopeUris":[]},
           {"name": "Netset2", "networkUris": " ", "connectionTemplateUri": None, "type": "network-setV5", "nativeNetworkUri": None, "networkSetType": "Regular", "initialScopeUris": []},
           {"name": "Netset3", "networkUris": " ", "connectionTemplateUri": None, "type": "network-setV5", "nativeNetworkUri": None, "networkSetType": "Regular", "initialScopeUris": []},
           {"name": "Netset4", "networkUris": " ", "connectionTemplateUri": None, "type": "network-setV5", "nativeNetworkUri": None, "networkSetType": "Regular", "initialScopeUris": []},
           {"name": "Netset5", "networkUris": " ", "connectionTemplateUri": None, "type": "network-setV5", "nativeNetworkUri": None, "networkSetType": "Regular", "initialScopeUris": []},
           {"name": "Netset6", "networkUris": " ", "connectionTemplateUri": None, "type": "network-setV5", "nativeNetworkUri": None, "networkSetType": "Regular", "initialScopeUris": []},
           {"name": "Netset7", "networkUris": " ", "connectionTemplateUri": None, "type": "network-setV5", "nativeNetworkUri": None, "networkSetType": "Regular", "initialScopeUris": []},
           ]

encs = [{'hostname': '15.186.18.129', 'username': 'Administrator', 'password': 'compaq', 'enclosureGroupUri': 'EG:EG', 'force': False, 'licensingIntent': 'OneViewNoiLO'}]

# Empty NetworkSet
ethernet_network1 = [{"vlanId": "401",
                      "purpose": "Management",
                      "name": "network1",
                      "smartLink": False,
                      "privateNetwork": False,
                      "connectionTemplateUri": None,
                      "networkSetUris": [],
                      "ethernetNetworkType": "Tagged",
                      "type": "ethernet-networkV5"}]

ethernet_network2 = [{"vlanId": "402",
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
                      "name": " ",
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

SP_NS = [{'type': 'ServerProfileV11', 'serverHardwareUri': ENC1 + ', bay 6',
          'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + EG,
          'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
          'name': 'profile_bay3', 'description': '', 'affinity': 'Bay',
          "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
          'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Auto',
                                                  'requestedMbps': '2500', 'networkUri': 'NS:Netset7', 'mac': None, 'wwpn': None, 'wwnn': None},

                                                 ]}}]

multiple_network_set = ["netset1", "netset2", "netset3"]

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
         'uplinkSets': [uplink_sets['us1'].copy()],
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

LE = {'name': LE,
      'enclosureUris': [],
      'enclosureGroupUri': 'EG:' + EG,
      'firmwareBaselineUri': None,
      'forceInstallFirmware': False
      }

bulk_ethernet_network = [{"vlanIdRange": "401", "purpose": "General", "namePrefix": "Net1", "smartLink": False, "privateNetwork": False, "bandwidth": {"maximumBandwidth": 10000, "typicalBandwidth": 2000}, "type": "bulk-ethernet-networkV2", "networkSetUris": []}]

bulk_ethernet_network2 = [{"vlanIdRange": "402", "purpose": "General", "namePrefix": "Net2", "smartLink": False, "privateNetwork": False, "bandwidth": {"maximumBandwidth": 10000, "typicalBandwidth": 2000}, "type": "bulk-ethernet-networkV2", "networkSetUris": ['Netset1']}]

bulk_ethernet_network1 = [{"vlanIdRange": "402", "purpose": "General", "namePrefix": "Net21", "smartLink": False, "privateNetwork": False, "bandwidth": {"maximumBandwidth": 10000, "typicalBandwidth": 2000}, "type": "bulk-ethernet-networkV2", "networkSetUris": ['Netset211']}]

bulk_ethernet_network3 = [{"vlanIdRange": "403", "purpose": "General", "namePrefix": "Net4", "smartLink": False, "privateNetwork": False, "bandwidth": {"maximumBandwidth": 10000, "typicalBandwidth": 2000}, "type": "bulk-ethernet-networkV2"}]

bulk_ethernet_network4 = [{"vlanIdRange": "404", "purpose": "General", "namePrefix": "Net_multiple_NS", "smartLink": False, "privateNetwork": False, "bandwidth": {"maximumBandwidth": 10000, "typicalBandwidth": 2000}, "type": "bulk-ethernet-networkV2", "networkSetUris": ['Netset1', 'Netset2']}]

bulk_ethernet_network5 = [{"vlanIdRange": "404", "purpose": "General", "namePrefix": "Eth", "smartLink": False, "privateNetwork": False, "bandwidth": {"maximumBandwidth": 10000, "typicalBandwidth": 2000}, "type": "bulk-ethernet-networkV2", "networkSetUris": ['Netset7']}]

uplinkset3 = {
    'type': 'uplink-setV6',
    'name': 'US_PF',
    'portConfigInfos': [{"desiredSpeed": "Auto", "location": {"locationEntries": [{"value": "X1", "type": "Port"}, {"value": 1, "type": "Bay"},
                                                                                  {"value": ENC1, "type": "Enclosure"}]}}],
    'networkType': 'Ethernet',
    'manualLoginRedistributionState': 'NotSupported',
    'logicalInterconnectUri': "",  # user should defined logical interconnect name
    'connectionMode': 'Auto',
    'networkUris': ['Eth'],
    'fcNetworkUris': [],  # user should defined fabric channel name
    'fcoeNetworkUris': [],
    'networkSetUris': []
}

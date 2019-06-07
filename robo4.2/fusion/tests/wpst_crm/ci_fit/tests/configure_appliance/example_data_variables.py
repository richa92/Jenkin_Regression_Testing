"""
This is an example CI-fIT data variable file.  It can be used as a reference for creating test rig data var files.
"""


def make_range_list(vrange):
    """
    Create a range of networks using the range and prefix defined in the other methods
    """
    rlist = []
    for x in xrange(vrange['start'], (vrange['end'] + 1)):
        rlist.append(vrange['prefix'] + str(x) + vrange['suffix'])
    return rlist


def range_list(start, end, prefix='net_', suffix=''):
    """
    Create a range of networks using the range and prefix defined in the other methods
    """
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist


"""
These are the credentials for the Administrator account.  The password specified here is used during FTS
as you are forced to change the password
"""
admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

"""
This is the vCenter server IP\FQDN, username and password  where your appliance is hosted. This is used
to be able to specify a VM name instead of IP during SETUP\TEARDOWN.  You can use ${APPLIANCE_IP} instead to force a specific host.
"""
vcenter = {'server': '15.186.4.110', 'user': 'Administrator', 'password': 'Compaq123'}

"""
This is the Appliance Network Configuration Data used during FTS for a non-clustered config (valid for C7000 and Tbird).  You can specify STATIC or DHCP as needed
"""
appliance = {'type': 'ApplianceNetworkConfiguration',
             'applianceNetworks':
             [{'device': 'eth0',
               'macAddress': None,
               'interfaceName': 'hpqcorpnet',
               'activeNode': '1',
               'unconfigure': False,
               'ipv4Type': 'STATIC',
               'ipv4Subnet': '255.255.224.0',
               'ipv4Gateway': '15.186.0.1',
               'ipv4NameServers': ['16.110.135.51', '16.110.135.52'],
               'app1Ipv4Addr': '15.186.7.254',
               'ipv6Type': 'UNCONFIGURE',
               'hostname': 'ci-fit-i13.austin.hp.com',
               'confOneNode': True,
               'domainName': 'usa.hp.com',
               'aliasDisabled': True,
               }],
             }

"""
This is the Appliance Network Configuration Data used during FTS for a clustered config (valid for Tbird).  You can specify STATIC or DHCP as needed
NOTE: there are some different attributes that must be used for clustered.
    virtIpv4Addr: this is the cluster IP, used for UI and API
    app1Ipv4Addr: Node1 IPv4 address in a two node cluster
    app2Ipv4Addr: Node2 IPv4 address in a two node cluster
"""
appliance = {'type': 'ApplianceNetworkConfiguration',
             'applianceNetworks':
             [{'device': 'eth0',
               'macAddress': None,
               'interfaceName': 'vLAN101',
               'activeNode': '1',
               'unconfigure': False,
               'ipv4Type': 'STATIC',
               'ipv4Subnet': '255.255.0.0',
               'ipv4Gateway': '192.168.0.1',
               'ipv4NameServers': ['192.168.0.2'],
               'virtIpv4Addr': '192.168.0.100',
               'app1Ipv4Addr': '192.168.0.101',
               'app2Ipv4Addr': '192.168.0.102',
               'ipv6Type': 'UNCONFIGURE',
               'hostname': 'f105.usa.hp.com',
               'confOneNode': True,
               'domainName': 'usa.hp.com',
               'aliasDisabled': True,
               }],
             }


"""
This is the time and locale settings used during FTS.
"""
timeandlocale = {'type': 'TimeAndLocale', 'dateTime': None, 'timezone': 'UTC', 'ntpServers': ['ntp.hp.net'], 'locale': 'en_US.UTF-8'}

"""
These are the virtual address ranges for MAC, WWN and SERIAL numbers
"""
ranges = [{'name': 'CI-FIT-01-MAC', 'type': 'Range', 'category': 'id-range-VMAC', 'rangeCategory': 'CUSTOM', 'startAddress': 'A2:11:11:00:00:00', 'endAddress': 'A2:11:11:0F:FF:FF', 'enabled': True},
          {'name': 'CI-FIT-01-WWN', 'type': 'Range', 'category': 'id-range-VWWN', 'rangeCategory': 'CUSTOM', 'startAddress': '21:11:11:11:00:00:00:00', 'endAddress': '21:11:11:11:00:0F:FF:FF', 'enabled': True},
          {'name': 'CI-FIT-01-SN', 'type': 'Range', 'category': 'id-range-VSN', 'rangeCategory': 'CUSTOM', 'startAddress': 'VCUBBB0000', 'endAddress': 'VCUBBB0ZZZ', 'enabled': True}]

"""
These are the users you want to create on the appliance
"""
users = [{'userName': 'Serveradmin', 'password': 'Serveradmin', 'fullName': 'Serveradmin', 'roles': ['Server administrator'], 'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'Networkadmin', 'password': 'Networkadmin', 'fullName': 'Networkadmin', 'roles': ['Network administrator'], 'emailAddress': 'nat@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'Backupadmin', 'password': 'Backupadmin', 'fullName': 'Backupadmin', 'roles': ['Backup administrator'], 'emailAddress': 'backup@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'Noprivledge', 'password': 'Noprivledge', 'fullName': 'Noprivledge', 'roles': ['Read only'], 'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'}
         ]

"""
These are the Licenses you want to add to the appliance
"""
licenses = [{'key': 'YCDE D9MA H9P9 8HUZ U7B5 HWW5 Y9JL KMPL MHND 7AJ9 DXAU 2CSM GHTG L762 LFH6 F4R4 KJVT D5KM EFVW DT5J 83HJ 8VC6 AK2P 3EW2 L9YE HUNJ TZZ7 MB5X 82Z5 WHEF GE4C LUE3 BKT8 WXDG NK6Y C4GA HZL4 XBE7 3VJ6 2MSU 4ZU9 9WGG CZU7 WE4X YN44 CH55 KZLG 2F4N A8RJ UKEG 3F9V JQY5 "423207356 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR H3TCJHCGAYAY"'},
            {'key': 'QC3C A9MA H9PQ GHVZ U7B5 HWW5 Y9JL KMPL 2HVF 4FZ9 DXAU 2CSM GHTG L762 7JX5 V5FU KJVT D5KM EFVW DV5J 43LL PSS6 AK2P 3EW2 T9YE XUNJ TZZ7 MB5X 82Z5 WHEF GE4C LUE3 BKT8 WXDG NK6Y C4GA HZL4 XBE7 3VJ6 2MSU 4ZU9 9WGG CZU7 WE4X YN44 CH55 KZLG 2F4N A8RJ UKEG 3F9V JQY5 "423207566 HPOV-NFR2 HP_OneView_w/o_iLO_48_Seat_NFR 6H72JHCGY5AU"'}
            ]
"""
These are the ETHERNET networks you want to add to the appliance
"""
ethernet_networks = [{'name': 'IC',
                      'type': 'ethernet-networkV3',
                      'vlanId': None,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Untagged'},
                     {'name': 'Tunnel1',
                      'type': 'ethernet-networkV3',
                      'vlanId': None,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tunnel'},
                     {'name': 'Tunnel2',
                      'type': 'ethernet-networkV3',
                      'vlanId': None,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tunnel'},
                     ]


"""
These are the ethernet networks you want to create in bulk.
You can use this to set network ranges with different prefixes
You can also set the max bandwidth and typical bandwidth.
"""
bulk_ethernet_network = [{"vlanIdRange": "1-100", "description": "General networking", "purpose": "General", "namePrefix": "Net", "smartLink": True, "privateNetwork": False, "bandwidth": {"maximumBandwidth": 10000, "typicalBandwidth": 2500}, "type": "bulk-ethernet-networkV2"},
                         {"vlanIdRange": "500-505", "description": "General networking", "purpose": "General", "namePrefix": "Net", "smartLink": True, "privateNetwork": False, "bandwidth": {"maximumBandwidth": 10000, "typicalBandwidth": 2500}, "type": "bulk-ethernet-networkV2"}, ]


"""
These are the RANGES of ETHERNET networks you want to add to the appliance.
"""
ethernet_ranges = [{'prefix': 'net_', 'suffix': '', 'start': 2, 'end': 50, 'name': None, 'type': 'ethernet-networkV3',
                    'vlanId': None, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False, 'connectionTemplateUri': None,
                    'ethernetNetworkType': 'Tagged'},
                   {'prefix': 'net_', 'suffix': '', 'start': 51, 'end': 102, 'name': None, 'type': 'ethernet-networkV3',
                    'vlanId': None, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False, 'connectionTemplateUri': None,
                    'ethernetNetworkType': 'Tagged'}]

"""
These are the network sets you want to add to the appliance.
NOTE: There are 2 fields that use data that MUST have also been defined in either 'ethernet_networks' or 'ethernet_ranges' above:
 networkUris = a list of network names that you want to include in the set.  Example ['net1', 'net2']
 nativeNetworkUri = a string with only 1 network name to use as the native network
"""
network_sets = [{'name': 'NS_23', 'type': 'network-set', 'networkUris': ['net_23'], 'nativeNetworkUri': 'net_23'},
                {'name': 'NS_24', 'type': 'network-set', 'networkUris': ['net_24'], 'nativeNetworkUri': 'net_24'},
                {'name': 'NS_46', 'type': 'network-set', 'networkUris': ['net_46'], 'nativeNetworkUri': 'net_46'},
                {'name': 'NS_47', 'type': 'network-set', 'networkUris': ['net_47'], 'nativeNetworkUri': 'net_47'},
                {'name': 'NS_96', 'type': 'network-set', 'networkUris': ['net_96'], 'nativeNetworkUri': 'net_96'},
                {'name': 'NS_97', 'type': 'network-set', 'networkUris': ['net_97'], 'nativeNetworkUri': 'net_97'},
                {'name': 'NS_98', 'type': 'network-set', 'networkUris': ['net_98'], 'nativeNetworkUri': 'net_98'},
                {'name': 'NS_99', 'type': 'network-set', 'networkUris': ['net_99'], 'nativeNetworkUri': 'net_99'}]

"""
These are the network set ranges you want to add to the appliance.
NOTE: referenced ethernet network data that MUST have also been defined in either 'ethernet_networks' or 'ethernet_ranges' above:
 networkUris = This becomes populated with all the networks in the range you specify
 nativeNetworkUri = a string with only 1 network name to use as the native network
"""
network_set_ranges = [{'prefix': 'net_', 'suffix': '', 'start': 2, 'end': 22, 'name': 'VlanTrunk1', 'type': 'network-set', 'networkUris': None, 'nativeNetworkUri': 'net_2'},
                      {'prefix': 'net_', 'suffix': '', 'start': 25, 'end': 45, 'name': 'VlanTrunk2', 'type': 'network-set', 'networkUris': None, 'nativeNetworkUri': 'net_25'},
                      {'prefix': 'net_', 'suffix': '', 'start': 50, 'end': 70, 'name': 'VlanTrunk3', 'type': 'network-set', 'networkUris': None, 'nativeNetworkUri': 'net_50'},
                      {'prefix': 'net_', 'suffix': '', 'start': 75, 'end': 95, 'name': 'VlanTrunk4', 'type': 'network-set', 'networkUris': None, 'nativeNetworkUri': 'net_75'}
                      ]

"""
These are the FibreChannel networks you want to add to the appliance
"""
fc_networks = [{'name': 'SAN-1-A', 'type': 'fc-networkV2', 'linkStabilityTime': 30, 'autoLoginRedistribution': True, 'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'},
               {'name': 'SAN-2-B', 'type': 'fc-networkV2', 'linkStabilityTime': 30, 'autoLoginRedistribution': True, 'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'},
               {'name': 'SAN-3-A', 'type': 'fc-networkV2', 'linkStabilityTime': 30, 'autoLoginRedistribution': True, 'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'},
               {'name': 'SAN-4-B', 'type': 'fc-networkV2', 'linkStabilityTime': 30, 'autoLoginRedistribution': True, 'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'},
               {'name': 'SAN-5-A', 'type': 'fc-networkV2', 'linkStabilityTime': 30, 'autoLoginRedistribution': True, 'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'},
               {'name': 'SAN-6-B', 'type': 'fc-networkV2', 'linkStabilityTime': 30, 'autoLoginRedistribution': True, 'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'},
               ]

"""
These are the FCoE networks you want to add to the appliance
"""
fcoe_networks = [{'name': 'fcoe-100', 'type': 'fcoe-networkV300', 'vlanId': 100},
                 {'name': 'fcoe-2000', 'type': 'fcoe-networkV300', 'vlanId': 2000},
                 {'name': 'fcoe-100b', 'type': 'fcoe-networkV300', 'vlanId': 100},
                 ]

"""
These are the RANGES of FCoE networks you want to add to the appliance.
"""
fcoe_ranges = [{'prefix': 'fcoe-', 'suffix': 'a', 'start': 1001, 'end': 1032},
               {'prefix': 'fcoe-', 'suffix': 'b', 'start': 1001, 'end': 1032},
               {'prefix': 'fcoe-', 'suffix': 'c', 'start': 1001, 'end': 1032},
               {'prefix': 'fcoe-', 'suffix': 'd', 'start': 1001, 'end': 1032},
               ]

"""
# C7000
These are the enclosure group(s) you want to add to the appliance
NOTE:  There are some special fields:
 enclosureTypeUri = /rest/enclosure-types/c7000
 logicalInterconnectGroupUri = for each ic bay, you must specify 'LIG:' + the name of the LIG for that bay
                               The LIG you choose MUST be defined in your datafile (or exist on the appliance)
"""
enc_groups = [{'name': 'FFF8-8FC20-8FC24',
               'type': 'EnclosureGroupV300',
               'enclosureTypeUri': '/rest/enclosure-types/c7000',
               'stackingMode': 'Enclosure',
               'interconnectBayMappingCount': 8,
               'configurationScript': None,
               'interconnectBayMappings':
               [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:LIG-FFF8-8FC20-8FC24'},
                {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:LIG-FFF8-8FC20-8FC24'},
                {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG-FFF8-8FC20-8FC24'},
                {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:LIG-FFF8-8FC20-8FC24'},
                {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:LIG-FFF8-8FC20-8FC24'},
                {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG-FFF8-8FC20-8FC24'},
                {'interconnectBay': 7, 'logicalInterconnectGroupUri': 'LIG:LIG-FFF8-8FC20-8FC24'},
                {'interconnectBay': 8, 'logicalInterconnectGroupUri': 'LIG:LIG-FFF8-8FC20-8FC24'}]},
              ]

"""
# Synergy
These are the enclosure group(s) you want to add to the appliance.
NOTE:  There are some special fields:
 enclosureTypeUri = /rest/enclosure-types/SY12000
 logicalInterconnectGroupUri = for each ic bay, you must specify 'LIG:' + the name of the LIG for that bay
                               The LIG you choose MUST be defined in your datafile (or exist on the appliance)
 enclosureCount = The number of enclosures in the group
"""

enc_groups = [{'name': 'Tbird-EG',
               'type': 'EnclosureGroupV300',
               'enclosureCount': 2,
               'enclosureTypeUri': '/rest/enclosure-types/SY12000',
               'stackingMode': 'Enclosure',
               'interconnectBayMappingCount': 6,
               'configurationScript': None,
               'interconnectBayMappings':
               [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
                {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG1'}],
               'ipAddressingMode': "Externally",
               'ipRangeUris': [],
               'powerMode': "RedundantPowerFeed"
               }
              ]


"""
These are the C7000 enclosure(s) you want to add to the appliance
NOTE: There is a special field:
 enclosureGroupUri = You must specify EG: + the name of the enclosure group to associate the enclosure with
                     The EG you choose MUST be defined in your datafile (or exist on the appliance)

"""
encs = [{'hostname': '15.186.2.184', 'username': 'Administrator', 'password': 'compaq', 'enclosureGroupUri': 'EG:FFF8-8FC20-8FC24', 'force': False, 'licensingIntent': 'OneViewNoiLO'}
        ]

"""
The uplinkset(s) you want to use in your LIG(s)
NOTE:  There are some special fields
 networkUris = a list of network names to include in the uplinkset
 networkSetUris = a list of network set names to include in the uplinkset. Example - 'networkSetUris': ['NWS1','NWS2']
 nativeNetworkUri = a string containing the name of the network you want to be the native network
"""
uplink_sets = {'IC': {'name': 'IC',
                      'ethernetNetworkType': 'Untagged',
                      'networkType': 'Ethernet',
                      'networkUris': ['IC'],
                      'nativeNetworkUri': None,
                      'mode': 'Auto',
                      'logicalPortConfigInfos': [{'bay': '1', 'port': 'X4', 'speed': 'Auto'}]},
               'Tunnel1': {'name': 'Tunnel1',
                           'ethernetNetworkType': 'Tunnel',
                           'networkType': 'Ethernet',
                           'networkUris': ['Tunnel1'],
                           'nativeNetworkUri': None,
                           'mode': 'Auto',
                           'lacpTimer': 'Long',
                           'logicalPortConfigInfos': [{'bay': '1', 'port': 'X3', 'speed': 'Auto'}]},
               'Tunnel2': {'name': 'Tunnel2',
                           'ethernetNetworkType': 'Tunnel',
                           'networkType': 'Ethernet',
                           'networkUris': ['Tunnel2'],
                           'nativeNetworkUri': None,
                           'mode': 'Auto',
                           'lacpTimer': 'Long',
                           'logicalPortConfigInfos': [{'bay': '2', 'port': 'X3', 'speed': 'Auto'}]},
               'SAN-1-A': {'name': 'SAN-1-A',
                           'ethernetNetworkType': 'NotApplicable',
                           'networkType': 'FibreChannel',
                           'networkUris': ['SAN-1-A'],
                           'nativeNetworkUri': None,
                           'mode': 'Auto',
                           'logicalPortConfigInfos': [{'bay': '1', 'port': 'X7', 'speed': 'Auto'}]},
               'SAN-2-B': {'name': 'SAN-2-B',
                           'ethernetNetworkType': 'NotApplicable',
                           'networkType': 'FibreChannel',
                           'networkUris': ['SAN-2-B'],
                           'nativeNetworkUri': None,
                           'mode': 'Auto',
                           'logicalPortConfigInfos': [{'bay': '2', 'port': 'X7', 'speed': 'Auto'}]},
               'SAN-3-A': {'name': 'SAN-3-A',
                           'ethernetNetworkType': 'NotApplicable',
                           'networkType': 'FibreChannel',
                           'networkUris': ['SAN-3-A'],
                           'nativeNetworkUri': None,
                           'mode': 'Auto',
                           'logicalPortConfigInfos': [{'bay': '3', 'port': '1', 'speed': 'Auto'},
                                                      {'bay': '3', 'port': '2', 'speed': 'Auto'}]},
               'SAN-4-B': {'name': 'SAN-4-B',
                           'ethernetNetworkType': 'NotApplicable',
                           'networkType': 'FibreChannel',
                           'networkUris': ['SAN-4-B'],
                           'nativeNetworkUri': None,
                           'mode': 'Auto',
                           'logicalPortConfigInfos': [{'bay': '4', 'port': '1', 'speed': 'Auto'},
                                                      {'bay': '4', 'port': '2', 'speed': 'Auto'}]},
               'SAN-5-A': {'name': 'SAN-5-A',
                           'ethernetNetworkType': 'NotApplicable',
                           'networkType': 'FibreChannel',
                           'networkUris': ['SAN-5-A'],
                           'nativeNetworkUri': None,
                           'mode': 'Auto',
                           'logicalPortConfigInfos': [{'bay': '5', 'port': '1', 'speed': 'Auto'},
                                                      {'bay': '5', 'port': '2', 'speed': 'Auto'}]},
               'SAN-6-B': {'name': 'SAN-6-B',
                           'ethernetNetworkType': 'NotApplicable',
                           'networkType': 'FibreChannel',
                           'networkUris': ['SAN-6-B'],
                           'nativeNetworkUri': None,
                           'mode': 'Auto',
                           'logicalPortConfigInfos': [{'bay': '6', 'port': '1', 'speed': 'Auto'},
                                                      {'bay': '6', 'port': '2', 'speed': 'Auto'}]},
               'BigPipe1': {'name': 'BigPipe1',
                            'ethernetNetworkType': 'Tagged',
                            'networkType': 'Ethernet',
                            'networkUris': make_range_list(ethernet_ranges[0]),
                            'nativeNetworkUri': None,
                            'mode': 'Auto',
                            'logicalPortConfigInfos': [{'bay': '1', 'port': 'X1', 'speed': 'Auto'},
                                                       {'bay': '1', 'port': 'X2', 'speed': 'Auto'}]},
               'BigPipe2': {'name': 'BigPipe2',
                            'ethernetNetworkType': 'Tagged',
                            'networkType': 'Ethernet',
                            'networkUris': make_range_list(ethernet_ranges[1]),
                            'nativeNetworkUri': None,
                            'mode': 'Auto',
                            'logicalPortConfigInfos': [{'bay': '2', 'port': 'X1', 'speed': 'Auto'},
                                                       {'bay': '2', 'port': 'X2', 'speed': 'Auto'}]},
               }

"""
The LIG(s) you want to add to the appliance
NOTE:  There are some special fields
[for C7000 LIG]
 enclosureType = C7000
 interconnectMapTemplate: an list of ICMs and their position - you must specify all 8. If a bay is empty, type = None
    enclosure = 1
    enclosureIndex = 1
    bay = the physical bay the ICM should be in
    type = the name of the ICM type
 uplinkSets: an list of uplinksets to create. These are references to the dictionary keys defined previously in the uplink_set variable.
"""
# c7000
ligs = [{'name': 'LIG-FFF8-8FC20-8FC24',
         'type': 'logical-interconnect-groupV3',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC 8Gb 20-Port FC Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC 8Gb 20-Port FC Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC 8Gb 24-Port FC Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC 8Gb 24-Port FC Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 7, 'type': 'HP VC 8Gb 24-Port FC Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 8, 'type': 'HP VC 8Gb 24-Port FC Module'},
                                     ],
         'uplinkSets': [uplink_sets['IC'],
                        uplink_sets['Tunnel1'],
                        uplink_sets['Tunnel2'],
                        uplink_sets['SAN-1-A'],
                        uplink_sets['SAN-2-B'],
                        uplink_sets['SAN-3-A'],
                        uplink_sets['SAN-4-B'],
                        uplink_sets['SAN-5-A'],
                        uplink_sets['SAN-6-B'],
                        uplink_sets['BigPipe1'],
                        uplink_sets['BigPipe2']],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None}
        ]
"""
The LIG(s) you want to add to the appliance
NOTE:  There are some special fields
[for TClass LIG]
 enclosureType = TClass
 enclosureIndexes = a list of integers representing the ids of each enclosure
 fcoeSettings =
    fcoeMode = either 'FcfNpv' , 'Transit', or 'NotApplicable'
 interconnectMapTemplate: an list of ICMs and their position.
    enclosure = The physical enclosure the ICM is located in
    enclosureIndex = The enclosure index of the ICM is located in (usually matches the setting in 'enclosure'
    bay = the physical bay the ICM should be in
    type = the name of the ICM type
 interconnectBaySet = an integer representing the IBS\Fabric (1 = Bay 1&4, 2 = Bay 2&5, 3 = Bay 3&6)
 redundancyType = 'Redundant', 'HighlyAvailable', 'NonRedundantASide', 'NonRedundantBSide'
 uplinkSets: an list of uplinksets to create. These are references to the dictionary keys defined previously in the uplink_set variable.
"""
ligs = [{'name': 'LIG1',
         'type': 'logical-interconnect-groupV3',
         'enclosureType': 'TClass',
         'interconnectMapTemplate': [{'bay': 3, 'enclosure': 1, 'type': 'HP FlexFabric 40GbE Module - EdgeSafe/Virtual Connect version', 'enclosureIndex': 1},
                                     {'bay': 6, 'enclosure': 2, 'type': 'HP FlexFabric 40GbE Module - EdgeSafe/Virtual Connect version', 'enclosureIndex': 2},
                                     {'bay': 6, 'enclosure': 1, 'type': 'HP FlexFabric 20GbE Expansion Module', 'enclosureIndex': 1},
                                     {'bay': 3, 'enclosure': 2, 'type': 'HP FlexFabric 20GbE Expansion Module', 'enclosureIndex': 2}],
         'enclosureIndexes': [1, 2],
         'interconnectBaySet': 3,
         'redundancyType': 'HighlyAvailable',
         'fcoeSettings': {'fcoeMode': 'FcfNpv'},
         'uplinkSets': [uplink_sets['us1'].copy(), uplink_sets['us2'].copy(), uplink_sets['us3'].copy()],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None}
        ]

"""
Optional LIG variables
These variables can be used in the LIG variables above.  They are only broken out to help simplify looking at them.
"""
telemetry = {'enableTelemetry': True, 'sampleInterval': 400, 'sampleCount': 20}

trapDestinations = [{'trapSeverities': ['Major'],
                     'enetTrapCategories': ['Other'],
                     'fcTrapCategories': ['Other'],
                     'vcmTrapCategories': ['Legacy'],
                     'trapFormat': 'SNMPv1',
                     'trapDestination': '192.168.99.99',
                     'communityString': 'public'}]

snmp = {'snmpAccess': ['192.168.1.0/24'],
        'trapDestinations': trapDestinations}

enet = {'enableFastMacCacheFailover': False}


"""
The LE(s) you want to add to the appliance TCLASS ONLY
NOTE:  There are some special fields
[TClass LE]
 enclosureUris = a list of enclosures to add to this LE - 'ENC:' + the name of the enclosure (by default the serial number of the enclosure)
 enclosureGroupUri = You must specify EG: + the name of the enclosure group to associate the enclosure with
                     The EG you choose MUST be defined in your datafile (or exist on the appliance)
"""
les = [{'name': 'LE',
        'enclosureUris': ['ENC:0000A66101', 'ENC:0000A66103'],
        'enclosureGroupUri': 'EG:EG',
        'firmwareBaselineUri': None,
        'forceInstallFirmware': False
        }]


server_profiles = [{'type': 'ServerProfileV5', 'serverHardwareUri': 'CI-FIT-11, bay 1',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:CI-FIT-11', 'enclosureGroupUri': 'EG:FFF8-8FC20-8FC24', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                    'name': 'CI-FIT-11_Bay1-BL465cGen8', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
                    'connections': [{'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:IC', 'boot': {'priority': 'Primary'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:net_96', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 4, 'name': '4', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-b', 'requestedMbps': '2500', 'networkUri': 'ETH:net_96', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 5, 'name': '5', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-c', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk1', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 6, 'name': '6', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-c', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk1', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 7, 'name': '7', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS_23', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 8, 'name': '8', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS_23', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 9, 'name': '9', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1', 'requestedMbps': '8000', 'networkUri': 'FC:SAN-3-A', 'boot': {'priority': 'Primary', 'targets': [{'arrayWwpn': '21110002ac00364c', 'lun': '0'}]}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 10, 'name': '10', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:2', 'requestedMbps': '8000', 'networkUri': 'FC:SAN-4-B', 'boot': {'priority': 'Secondary', 'targets': [{'arrayWwpn': '20110002ac00364c', 'lun': '0'}]}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 11, 'name': '11', 'functionType': 'FibreChannel', 'portId': 'Mezz 2:1', 'requestedMbps': '8000', 'networkUri': 'FC:SAN-5-A', 'boot': {'priority': 'NotBootable'}},
                                    {'id': 12, 'name': '12', 'functionType': 'FibreChannel', 'portId': 'Mezz 2:2', 'requestedMbps': '8000', 'networkUri': 'FC:SAN-6-B', 'boot': {'priority': 'NotBootable'}},
                                    ]},
                   {'type': 'ServerProfileV5', 'serverHardwareUri': 'CI-FIT-11, bay 2',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:CI-FIT-11', 'enclosureGroupUri': 'EG:FFF8-8FC20-8FC24', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                    'name': 'CI-FIT-11_Bay2-BL465cGen8', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
                    'connections': [{'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:IC', 'boot': {'priority': 'Primary'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:net_97', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 4, 'name': '4', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-b', 'requestedMbps': '2500', 'networkUri': 'ETH:net_97', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 5, 'name': '5', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-c', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk2', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 6, 'name': '6', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-c', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk2', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 7, 'name': '7', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS_24', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 8, 'name': '8', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS_24', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 9, 'name': '9', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1', 'requestedMbps': '8000', 'networkUri': 'FC:SAN-3-A', 'boot': {'priority': 'NotBootable'}},
                                    {'id': 10, 'name': '10', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:2', 'requestedMbps': '8000', 'networkUri': 'FC:SAN-4-B', 'boot': {'priority': 'NotBootable'}},
                                    {'id': 11, 'name': '11', 'functionType': 'FibreChannel', 'portId': 'Mezz 2:1', 'requestedMbps': '8000', 'networkUri': 'FC:SAN-5-A', 'boot': {'priority': 'NotBootable'}},
                                    {'id': 12, 'name': '12', 'functionType': 'FibreChannel', 'portId': 'Mezz 2:2', 'requestedMbps': '8000', 'networkUri': 'FC:SAN-6-B', 'boot': {'priority': 'NotBootable'}},
                                    ]},
                   {'type': 'ServerProfileV5', 'serverHardwareUri': 'CI-FIT-11, bay 3',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:CI-FIT-11', 'enclosureGroupUri': 'EG:FFF8-8FC20-8FC24', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                    'name': 'CI-FIT-11_Bay3-BL465cGen8', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
                    'connections': [{'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:IC', 'boot': {'priority': 'Primary'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:net_98', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 4, 'name': '4', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-b', 'requestedMbps': '2500', 'networkUri': 'ETH:net_98', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 5, 'name': '5', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-c', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 6, 'name': '6', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-c', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 7, 'name': '7', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS_46', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 8, 'name': '8', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS_46', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 9, 'name': '9', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1', 'requestedMbps': '8000', 'networkUri': 'FC:SAN-3-A', 'boot': {'priority': 'NotBootable'}},
                                    {'id': 10, 'name': '10', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:2', 'requestedMbps': '8000', 'networkUri': 'FC:SAN-4-B', 'boot': {'priority': 'NotBootable'}},
                                    {'id': 11, 'name': '11', 'functionType': 'FibreChannel', 'portId': 'Mezz 2:1', 'requestedMbps': '8000', 'networkUri': 'FC:SAN-5-A', 'boot': {'priority': 'NotBootable'}},
                                    {'id': 12, 'name': '12', 'functionType': 'FibreChannel', 'portId': 'Mezz 2:2', 'requestedMbps': '8000', 'networkUri': 'FC:SAN-6-B', 'boot': {'priority': 'NotBootable'}},
                                    ]},
                   {'type': 'ServerProfileV5', 'serverHardwareUri': 'CI-FIT-11, bay 4',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:CI-FIT-11', 'enclosureGroupUri': 'EG:FFF8-8FC20-8FC24', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                    'name': 'CI-FIT-11_Bay4-BL465cGen8', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
                    'connections': [{'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:IC', 'boot': {'priority': 'Primary'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 3, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Flb 1:1-b', 'requestedMbps': '2000', 'networkUri': 'FC:SAN-1-A', 'boot': {'priority': 'NotBootable'}},
                                    {'id': 4, 'name': '4', 'functionType': 'FibreChannel', 'portId': 'Flb 1:2-b', 'requestedMbps': '2000', 'networkUri': 'FC:SAN-2-B', 'boot': {'priority': 'NotBootable'}},
                                    {'id': 5, 'name': '5', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-c', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk4', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 6, 'name': '6', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-c', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk4', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 7, 'name': '7', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-d', 'requestedMbps': '2500', 'networkUri': 'ETH:net_99', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 8, 'name': '8', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-d', 'requestedMbps': '2500', 'networkUri': 'ETH:net_99', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 9, 'name': '9', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1', 'requestedMbps': '8000', 'networkUri': 'FC:SAN-3-A', 'boot': {'priority': 'NotBootable'}},
                                    {'id': 10, 'name': '10', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:2', 'requestedMbps': '8000', 'networkUri': 'FC:SAN-4-B', 'boot': {'priority': 'NotBootable'}},
                                    {'id': 11, 'name': '11', 'functionType': 'FibreChannel', 'portId': 'Mezz 2:1', 'requestedMbps': '8000', 'networkUri': 'FC:SAN-5-A', 'boot': {'priority': 'NotBootable'}},
                                    {'id': 12, 'name': '12', 'functionType': 'FibreChannel', 'portId': 'Mezz 2:2', 'requestedMbps': '8000', 'networkUri': 'FC:SAN-6-B', 'boot': {'priority': 'NotBootable'}},
                                    ]},
                   {'type': 'ServerProfileV5', 'serverHardwareUri': 'CI-FIT-11, bay 5',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:CI-FIT-11', 'enclosureGroupUri': 'EG:FFF8-8FC20-8FC24', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                    'name': 'CI-FIT-11_Bay5-BL460cGen8', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
                    'connections': [{'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:IC', 'boot': {'priority': 'Primary'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:net_96', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 4, 'name': '4', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-b', 'requestedMbps': '2500', 'networkUri': 'ETH:net_96', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 5, 'name': '5', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-c', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk1', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 6, 'name': '6', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-c', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk1', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 7, 'name': '7', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS_23', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 8, 'name': '8', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS_23', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 9, 'name': '9', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1', 'requestedMbps': '8000', 'networkUri': 'FC:SAN-3-A', 'boot': {'priority': 'NotBootable'}},
                                    {'id': 10, 'name': '10', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:2', 'requestedMbps': '8000', 'networkUri': 'FC:SAN-4-B', 'boot': {'priority': 'NotBootable'}},
                                    {'id': 11, 'name': '11', 'functionType': 'FibreChannel', 'portId': 'Mezz 2:1', 'requestedMbps': '8000', 'networkUri': 'FC:SAN-5-A', 'boot': {'priority': 'Primary', 'targets': [{'arrayWwpn': '21110002ac00364c', 'lun': '0'}]}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 12, 'name': '12', 'functionType': 'FibreChannel', 'portId': 'Mezz 2:2', 'requestedMbps': '8000', 'networkUri': 'FC:SAN-6-B', 'boot': {'priority': 'Secondary', 'targets': [{'arrayWwpn': '20110002ac00364c', 'lun': '0'}]}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    ]},
                   {'type': 'ServerProfileV5', 'serverHardwareUri': 'CI-FIT-11, bay 6',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:CI-FIT-11', 'enclosureGroupUri': 'EG:FFF8-8FC20-8FC24', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                    'name': 'CI-FIT-11_Bay6-BL460cGen8', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
                    'connections': [{'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:IC', 'boot': {'priority': 'Primary'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:net_97', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 4, 'name': '4', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-b', 'requestedMbps': '2500', 'networkUri': 'ETH:net_97', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 5, 'name': '5', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-c', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk2', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 6, 'name': '6', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-c', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk2', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 7, 'name': '7', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS_24', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 8, 'name': '8', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS_24', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 9, 'name': '9', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1', 'requestedMbps': '8000', 'networkUri': 'FC:SAN-3-A', 'boot': {'priority': 'NotBootable'}},
                                    {'id': 10, 'name': '10', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:2', 'requestedMbps': '8000', 'networkUri': 'FC:SAN-4-B', 'boot': {'priority': 'NotBootable'}},
                                    {'id': 11, 'name': '11', 'functionType': 'FibreChannel', 'portId': 'Mezz 2:1', 'requestedMbps': '8000', 'networkUri': 'FC:SAN-5-A', 'boot': {'priority': 'NotBootable'}},
                                    {'id': 12, 'name': '12', 'functionType': 'FibreChannel', 'portId': 'Mezz 2:2', 'requestedMbps': '8000', 'networkUri': 'FC:SAN-6-B', 'boot': {'priority': 'NotBootable'}},
                                    ]},
                   {'type': 'ServerProfileV5', 'serverHardwareUri': 'CI-FIT-11, bay 7',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:CI-FIT-11', 'enclosureGroupUri': 'EG:FFF8-8FC20-8FC24', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                    'name': 'CI-FIT-11_Bay7-BL460cGen8', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
                    'connections': [{'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:IC', 'boot': {'priority': 'Primary'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:net_98', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 4, 'name': '4', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-b', 'requestedMbps': '2500', 'networkUri': 'ETH:net_98', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 5, 'name': '5', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-c', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 6, 'name': '6', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-c', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 7, 'name': '7', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS_46', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 8, 'name': '8', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS_46', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 9, 'name': '9', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1', 'requestedMbps': '8000', 'networkUri': 'FC:SAN-3-A', 'boot': {'priority': 'NotBootable'}},
                                    {'id': 10, 'name': '10', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:2', 'requestedMbps': '8000', 'networkUri': 'FC:SAN-4-B', 'boot': {'priority': 'NotBootable'}},
                                    {'id': 11, 'name': '11', 'functionType': 'FibreChannel', 'portId': 'Mezz 2:1', 'requestedMbps': '8000', 'networkUri': 'FC:SAN-5-A', 'boot': {'priority': 'NotBootable'}},
                                    {'id': 12, 'name': '12', 'functionType': 'FibreChannel', 'portId': 'Mezz 2:2', 'requestedMbps': '8000', 'networkUri': 'FC:SAN-6-B', 'boot': {'priority': 'NotBootable'}},
                                    ]},
                   {'type': 'ServerProfileV5', 'serverHardwareUri': 'CI-FIT-11, bay 8',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:CI-FIT-11', 'enclosureGroupUri': 'EG:FFF8-8FC20-8FC24', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                    'name': 'CI-FIT-11_Bay8-BL460cGen8', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
                    'connections': [{'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:IC', 'boot': {'priority': 'Primary'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 3, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Flb 1:1-b', 'requestedMbps': '2000', 'networkUri': 'FC:SAN-1-A', 'boot': {'priority': 'NotBootable'}},
                                    {'id': 4, 'name': '4', 'functionType': 'FibreChannel', 'portId': 'Flb 1:2-b', 'requestedMbps': '2000', 'networkUri': 'FC:SAN-2-B', 'boot': {'priority': 'NotBootable'}},
                                    {'id': 5, 'name': '5', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-c', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk4', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 6, 'name': '6', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-c', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk4', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 7, 'name': '7', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-d', 'requestedMbps': '2500', 'networkUri': 'ETH:net_99', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 8, 'name': '8', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-d', 'requestedMbps': '2500', 'networkUri': 'ETH:net_99', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 9, 'name': '9', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1', 'requestedMbps': '8000', 'networkUri': 'FC:SAN-3-A', 'boot': {'priority': 'NotBootable'}},
                                    {'id': 10, 'name': '10', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:2', 'requestedMbps': '8000', 'networkUri': 'FC:SAN-4-B', 'boot': {'priority': 'NotBootable'}},
                                    {'id': 11, 'name': '11', 'functionType': 'FibreChannel', 'portId': 'Mezz 2:1', 'requestedMbps': '8000', 'networkUri': 'FC:SAN-5-A', 'boot': {'priority': 'NotBootable'}},
                                    {'id': 12, 'name': '12', 'functionType': 'FibreChannel', 'portId': 'Mezz 2:2', 'requestedMbps': '8000', 'networkUri': 'FC:SAN-6-B', 'boot': {'priority': 'NotBootable'}},
                                    ]},
                   {'type': 'ServerProfileV5', 'serverHardwareUri': 'CI-FIT-11, bay 9',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:CI-FIT-11', 'enclosureGroupUri': 'EG:FFF8-8FC20-8FC24', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                    'name': 'CI-FIT-11_Bay9-BL420cGen8', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
                    'connections': [{'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:IC', 'boot': {'priority': 'Primary'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:net_96', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 4, 'name': '4', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-b', 'requestedMbps': '2500', 'networkUri': 'ETH:net_96', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 5, 'name': '5', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-c', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk1', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 6, 'name': '6', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-c', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk1', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 7, 'name': '7', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS_23', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 8, 'name': '8', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS_23', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 9, 'name': '9', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1', 'requestedMbps': '8000', 'networkUri': 'FC:SAN-3-A', 'boot': {'priority': 'NotBootable'}},
                                    {'id': 10, 'name': '10', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:2', 'requestedMbps': '8000', 'networkUri': 'FC:SAN-4-B', 'boot': {'priority': 'NotBootable'}},
                                    {'id': 11, 'name': '11', 'functionType': 'FibreChannel', 'portId': 'Mezz 2:1', 'requestedMbps': '8000', 'networkUri': 'FC:SAN-5-A', 'boot': {'priority': 'Primary', 'targets': [{'arrayWwpn': '21110002ac00364c', 'lun': '0'}]}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 12, 'name': '12', 'functionType': 'FibreChannel', 'portId': 'Mezz 2:2', 'requestedMbps': '8000', 'networkUri': 'FC:SAN-6-B', 'boot': {'priority': 'Secondary', 'targets': [{'arrayWwpn': '20110002ac00364c', 'lun': '0'}]}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    ]},
                   {'type': 'ServerProfileV5', 'serverHardwareUri': 'CI-FIT-11, bay 10',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:CI-FIT-11', 'enclosureGroupUri': 'EG:FFF8-8FC20-8FC24', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                    'name': 'CI-FIT-11_Bay10-BL420cGen8', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
                    'connections': [{'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:IC', 'boot': {'priority': 'Primary'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:net_97', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 4, 'name': '4', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-b', 'requestedMbps': '2500', 'networkUri': 'ETH:net_97', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 5, 'name': '5', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-c', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk2', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 6, 'name': '6', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-c', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk2', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 7, 'name': '7', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS_24', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 8, 'name': '8', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS_24', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 9, 'name': '9', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1', 'requestedMbps': '8000', 'networkUri': 'FC:SAN-3-A', 'boot': {'priority': 'NotBootable'}},
                                    {'id': 10, 'name': '10', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:2', 'requestedMbps': '8000', 'networkUri': 'FC:SAN-4-B', 'boot': {'priority': 'NotBootable'}},
                                    {'id': 11, 'name': '11', 'functionType': 'FibreChannel', 'portId': 'Mezz 2:1', 'requestedMbps': '8000', 'networkUri': 'FC:SAN-5-A', 'boot': {'priority': 'NotBootable'}},
                                    {'id': 12, 'name': '12', 'functionType': 'FibreChannel', 'portId': 'Mezz 2:2', 'requestedMbps': '8000', 'networkUri': 'FC:SAN-6-B', 'boot': {'priority': 'NotBootable'}},
                                    ]},
                   {'type': 'ServerProfileV5', 'serverHardwareUri': 'CI-FIT-11, bay 11',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:CI-FIT-11', 'enclosureGroupUri': 'EG:FFF8-8FC20-8FC24', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                    'name': 'CI-FIT-11_Bay11-BL42065cGen8', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
                    'connections': [{'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:IC', 'boot': {'priority': 'Primary'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:net_98', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 4, 'name': '4', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-b', 'requestedMbps': '2500', 'networkUri': 'ETH:net_98', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 5, 'name': '5', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-c', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 6, 'name': '6', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-c', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 7, 'name': '7', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS_46', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 8, 'name': '8', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS_46', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 9, 'name': '9', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1', 'requestedMbps': '8000', 'networkUri': 'FC:SAN-3-A', 'boot': {'priority': 'NotBootable'}},
                                    {'id': 10, 'name': '10', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:2', 'requestedMbps': '8000', 'networkUri': 'FC:SAN-4-B', 'boot': {'priority': 'NotBootable'}},
                                    {'id': 11, 'name': '11', 'functionType': 'FibreChannel', 'portId': 'Mezz 2:1', 'requestedMbps': '8000', 'networkUri': 'FC:SAN-5-A', 'boot': {'priority': 'NotBootable'}},
                                    {'id': 12, 'name': '12', 'functionType': 'FibreChannel', 'portId': 'Mezz 2:2', 'requestedMbps': '8000', 'networkUri': 'FC:SAN-6-B', 'boot': {'priority': 'NotBootable'}},
                                    ]},
                   {'type': 'ServerProfileV5', 'serverHardwareUri': 'CI-FIT-11, bay 12',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:CI-FIT-11', 'enclosureGroupUri': 'EG:FFF8-8FC20-8FC24', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                    'name': 'CI-FIT-11_Bay12-BL420cGen8', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
                    'connections': [{'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:IC', 'boot': {'priority': 'Primary'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 3, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Flb 1:1-b', 'requestedMbps': '2000', 'networkUri': 'FC:SAN-1-A', 'boot': {'priority': 'NotBootable'}},
                                    {'id': 4, 'name': '4', 'functionType': 'FibreChannel', 'portId': 'Flb 1:2-b', 'requestedMbps': '2000', 'networkUri': 'FC:SAN-2-B', 'boot': {'priority': 'NotBootable'}},
                                    {'id': 5, 'name': '5', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-c', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk4', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 6, 'name': '6', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-c', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk4', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 7, 'name': '7', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-d', 'requestedMbps': '2500', 'networkUri': 'ETH:net_99', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 8, 'name': '8', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-d', 'requestedMbps': '2500', 'networkUri': 'ETH:net_99', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 9, 'name': '9', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1', 'requestedMbps': '8000', 'networkUri': 'FC:SAN-3-A', 'boot': {'priority': 'NotBootable'}},
                                    {'id': 10, 'name': '10', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:2', 'requestedMbps': '8000', 'networkUri': 'FC:SAN-4-B', 'boot': {'priority': 'NotBootable'}},
                                    {'id': 11, 'name': '11', 'functionType': 'FibreChannel', 'portId': 'Mezz 2:1', 'requestedMbps': '8000', 'networkUri': 'FC:SAN-5-A', 'boot': {'priority': 'NotBootable'}},
                                    {'id': 12, 'name': '12', 'functionType': 'FibreChannel', 'portId': 'Mezz 2:2', 'requestedMbps': '8000', 'networkUri': 'FC:SAN-6-B', 'boot': {'priority': 'NotBootable'}},
                                    ]},
                   {'type': 'ServerProfileV5', 'serverHardwareUri': 'CI-FIT-11, bay 13',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:CI-FIT-11', 'enclosureGroupUri': 'EG:FFF8-8FC20-8FC24', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                    'name': 'CI-FIT-11_Bay13-BL460cG7', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
                    'connections': [{'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Lom 1:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:IC', 'boot': {'priority': 'Primary'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Lom 1:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:Tunnel1', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 4, 'name': '4', 'functionType': 'Ethernet', 'portId': 'Lom 1:2-b', 'requestedMbps': '2500', 'networkUri': 'ETH:Tunnel2', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    ]},
                   {'type': 'ServerProfileV5', 'serverHardwareUri': 'CI-FIT-11, bay 14',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:CI-FIT-11', 'enclosureGroupUri': 'EG:FFF8-8FC20-8FC24', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                    'name': 'CI-FIT-11_Bay14-BL460cG7', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
                    'connections': [{'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Lom 1:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:IC', 'boot': {'priority': 'Primary'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Lom 1:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:Tunnel1', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 4, 'name': '4', 'functionType': 'Ethernet', 'portId': 'Lom 1:2-b', 'requestedMbps': '2500', 'networkUri': 'ETH:Tunnel2', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    ]},
                   {'type': 'ServerProfileV5', 'serverHardwareUri': 'CI-FIT-11, bay 15',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:CI-FIT-11', 'enclosureGroupUri': 'EG:FFF8-8FC20-8FC24', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                    'name': 'CI-FIT-11_Bay15-BL460cG7', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
                    'connections': [{'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Lom 1:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:IC', 'boot': {'priority': 'Primary'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Lom 1:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:Tunnel1', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 4, 'name': '4', 'functionType': 'Ethernet', 'portId': 'Lom 1:2-b', 'requestedMbps': '2500', 'networkUri': 'ETH:Tunnel2', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    ]},
                   {'type': 'ServerProfileV5', 'serverHardwareUri': 'CI-FIT-11, bay 16',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:CI-FIT-11', 'enclosureGroupUri': 'EG:FFF8-8FC20-8FC24', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                    'name': 'CI-FIT-11_Bay16-BL460cG7', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
                    'connections': [{'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Lom 1:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:IC', 'boot': {'priority': 'Primary'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Lom 1:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:Tunnel1', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 4, 'name': '4', 'functionType': 'Ethernet', 'portId': 'Lom 1:2-b', 'requestedMbps': '2500', 'networkUri': 'ETH:Tunnel2', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    ]},
                   ]

server_profile_templates = [{'type': 'ServerProfileTemplateV1', 'serverHardwareTypeUri': 'SHT:BL465c Gen8 1', 'enclosureGroupUri': 'EG:EG',
                             'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical', 'name': 'Profile1', 'description': '', 'affinity': 'Bay',
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
                             'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a',
                                              'requestedMbps': '2000', 'networkUri': 'ETH:net_101',
                                              'boot': {'priority': 'NotBootable'}},
                                             {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Flb 1:2-b',
                                              'requestedMbps': '2000', 'networkUri': 'FCOE:fcoe_102',
                                              'boot': {'priority': 'NotBootable'}},
                                             {'id': 3, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Flb 1:1-b',
                                              'requestedMbps': '2000', 'networkUri': 'FC:SAN-A',
                                              'boot': {'priority': 'NotBootable'}}]}, ]

"""
These are the network ranges you want to change the bandwidth.
"""
NETWORK_RANGE_TO_EDIT_BANDWIDTH = [{'prefix': 'fc', 'suffix': '',
                                    'start': 1, 'end': 3, 'type': 'fc',
                                    'name': None, 'User_typical_bandwidth': 2500,
                                    'User_max_bandwidth': 50000},
                                   {'prefix': 'net', 'suffix': '',
                                    'start': 3, 'end': 32, 'name': None,
                                    'type': 'ethernet', 'User_typical_bandwidth': None,
                                    'User_max_bandwidth': None},
                                   {'prefix': 'FCOE-', 'suffix': '-A',
                                    'start': 3776, 'end': 3807, 'name': None,
                                    'type': 'fcoe', 'User_typical_bandwidth': 3000,
                                    'User_max_bandwidth': None}]

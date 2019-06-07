"""
This is an example CI-fIT Tbird data variable file.
It can be used as a reference for creating test rig data var files.
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
This is the root user password for ssh access to OV.
"""
SSH_PASS = 'hpvse1'

"""
These are the credentials for the Administrator account.  The password specified here is used during FTS
as you are forced to change the password
"""
admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

"""
These are the credentials for the root account.  The password specified here is used during Tbird
hardware setup via ssh.
"""
ssh_credentials = {'userName': 'root', 'password': 'hponeview'}

"""
These are the credentials for the vCenter server.
"""
vcenter = {'server': '15.186.1.3', 'user': 'wpstuser', 'password': 'HPvse123'}

"""
This is the Appliance Network Configuration Data used during FTS for a non-clustered config (valid for C7000 and Tbird).
STATIC
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
               'app1Ipv4Addr': '15.186.7.135',
               'app2Ipv4Addr': '15.186.7.123',
               'virtIpv4Addr': '15.186.20.128',
               'ipv6Type': 'UNCONFIGURE',
               'hostname': 'cifit-30-pb53-dcs.austin.hpecorp.net',
               'confOneNode': True,
               'domainName': 'usa.hp.com',
               'aliasDisabled': True,
               }],
             }

"""
This is the Appliance Network Configuration Data used during FTS for a non-clustered config (valid for C7000 and Tbird).
DHCP
"""
# appliance = {'type': 'ApplianceNetworkConfiguration',
#              'applianceNetworks':
#              [{'device': 'eth0',
#                'macAddress': None,
#                'interfaceName': 'hpqcorpnet',
#                'activeNode': '1',
#                'unconfigure': False,
#                'ipv4Type': 'STATIC',
#                'ipv4Subnet': '255.255.224.0',
#                'ipv4Gateway': '15.186.0.1',
#                'ipv4NameServers': ['16.110.135.51', '16.110.135.52'],
#                'app1Ipv4Addr': '15.186.21.59',
#                'ipv6Type': 'UNCONFIGURE',
#                'hostname': 'Tbird30-PB45.austin.hpecorp.net',
#                'confOneNode': True,
#                'domainName': 'usa.hp.com',
#                'aliasDisabled': True,
#                }],
#              }


"""
This is the Appliance Network Configuration Data used during FTS for a clustered config (valid for Tbird).  You can specify STATIC or DHCP as needed
NOTE: there are some different attributes that must be used for clustered.
    virtIpv4Addr: this is the cluster IP, used for UI and API
    app1Ipv4Addr: Node1 IPv4 address in a two node cluster
    app2Ipv4Addr: Node2 IPv4 address in a two node cluster
"""
# appliance = {'type': 'ApplianceNetworkConfiguration',
#              'applianceNetworks':
#              [{'activeNode': '1',
#                'unconfigure': False,
#                'app1Ipv4Addr': '15.186.7.178',
#                'app1Ipv6Addr': '',
#                'app2Ipv4Addr': '15.186.7.129',
#                'app2Ipv6Addr': '',
#                'virtIpv4Addr': '15.186.22.191',
#                'virtIpv6Addr': None,
#                'app1Ipv4Alias': None,
#                'app1Ipv6Alias': None,
#                'app2Ipv4Alias': None,
#                'app2Ipv6Alias': None,
#                'hostname': 'Tbird30-dcs-pb45.austin.hpecorp.net',
#                'confOneNode': True,
#                'interfaceName': 'hpqcorpnet',
#                'macAddress': None,
#                'ipv4Type': 'STATIC',
#                'ipv6Type': 'UNCONFIGURED',
#                'overrideIpv4DhcpDnsServers': False
#                'ipv4Subnet': '255.255.224.0',
#                'ipv4Gateway': '15.186.0.1',
#                'ipv6Subnet': None,
#                'ipv6Gateway': None,
#                'domainName': 'usa.hp.com',
#                'searchDomains': [],
#                'ipv4NameServers': ['16.110.135.51', '16.110.135.52'],
#                'ipv6NameServers': ['16.110.135.51', '16.110.135.52'],
#                'bondedTo': None,
#                'aliasDisabled': True,
#                'configureRabbitMqSslListener': False,
#                'configurePostgresSslListener': False,
#                'webServerCertificate': None,
#                'webServerCertificateChain': None,
#                'webServerCertificateKey': None}],
#                'serverCertificater':{'rabbitMQCertificate':None,'rabbitMQRootCACertificate':None,
#                                      'rabbitMQCertificateKey':None,'postgresCertificate':None,
#                                      'postgresRootCACertificate':None,'postgresCertificateKey':None}
#              }
#


"""
This is the time and locale settings used during FTS.
"""
timeandlocale = {'type': 'TimeAndLocale', 'dateTime': None, 'timezone': 'UTC', 'ntpServers': ['ntp.hp.net'], 'locale': 'en_US.UTF-8'}

"""
These are the virtual address ranges for MAC, WWN and SERIAL numbers
"""
ranges = [{'name': 'CI-FIT-02-MAC', 'type': 'Range', 'category': 'id-range-VMAC', 'rangeCategory': 'CUSTOM', 'startAddress': 'C2:33:33:00:00:00', 'endAddress': 'C2:33:33:0F:FF:FF', 'enabled': True},
          {'name': 'CI-FIT-02-WWN', 'type': 'Range', 'category': 'id-range-VWWN', 'rangeCategory': 'CUSTOM', 'startAddress': '54:44:4C:44:00:00:00:00', 'endAddress': '54:44:4C:44:00:0F:FF:FF', 'enabled': True},
          {'name': 'CI-FIT-02-SN', 'type': 'Range', 'category': 'id-range-VSN', 'rangeCategory': 'CUSTOM', 'startAddress': 'VCUNNN0000', 'endAddress': 'VCUNNN0ZZZ', 'enabled': True}]

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
licenses = [{'key': 'YCDC D9MA H9PQ KHX2 V7B5 HWWB Y9JL KMPL TA2E PDRA DXAU 2CSM GHTG L762 HUK7 GB5M KJVT D5KM EFRW DS5R TXXK 6Q22 AK2P 3EW2 AJQ4 HU5V TZZH AB6X 82Z5 WHEF GE4C LUE3 BKT8 WXDG NK6Y C4GA HZL4 XBE7 3VJ6 2MSU 4ZU9 9WGG CZU7 WE4X YN44 CH55 KZLG 2F4N A8RJ UKEC 3F9V JQY5 "423542007 HPOV-NFR1 HP_OneView_16_Seat_NFR 75YYJJECU46C"_3DWNY-6B2KD-D8Z6S-6YR4B-K8GDW'},
            {'key': '9B3C A99A H9P9 GHUZ U7B5 HWW5 Y9JL KMPL 5AWA 8CBE DXAU 2CSM GHTG L762 7NGZ GDV4 KJVT D5KM EFRW DS5R 5XP8 4XK2 GNSL 9F82 7JKT QVXB XZKH ABB4 NV2C LHXU KN7U 5NA6 BKRK 35QB D8UW R42A X3BN LQ6M 5V9A PM6Q 4MN9 9GGS EZU7 GEMX VUJW CDB5 JVRX 8HEN 2J98 ACPB "TKOPREN HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR ATJUJJEDAT2Y"'}
            ]
"""
These are the ETHERNET networks you want to add to the appliance
"""
ethernet_networks = [{'name': 'IC',
                      'type': 'ethernet-networkV4',
                      'vlanId': None,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Untagged'},
                     {'name': 'Tunnel1',
                      'type': 'ethernet-networkV4',
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
bulk_ethernet_network = [{
    "vlanIdRange": "1-100", "description": "General networking", "purpose": "General", "namePrefix": "Net", "smartLink": True, "privateNetwork": False, "bandwidth": {"maximumBandwidth": 10000, "typicalBandwidth": 2500}, "type": "bulk-ethernet-networkV2"},
    {"vlanIdRange": "500-505", "description": "General networking", "purpose": "General", "namePrefix": "Net", "smartLink": True, "privateNetwork": False, "bandwidth": {"maximumBandwidth": 10000, "typicalBandwidth": 2500}, "type": "bulk-ethernet-networkV2"},
]


"""
These are the RANGES of ETHERNET networks you want to add to the appliance.
"""
ethernet_ranges = [{'prefix': 'net_', 'suffix': '', 'start': 2, 'end': 50, 'name': None, 'type': 'ethernet-networkV4',
                    'vlanId': None, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False, 'connectionTemplateUri': None,
                    'ethernetNetworkType': 'Tagged'},
                   {'prefix': 'net_', 'suffix': '', 'start': 51, 'end': 102, 'name': None, 'type': 'ethernet-networkV4',
                    'vlanId': None, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False, 'connectionTemplateUri': None,
                    'ethernetNetworkType': 'Tagged'}]

"""
These are the network sets you want to add to the appliance.
NOTE: There are 2 fields that use data that MUST have also been defined in either 'ethernet_networks' or 'ethernet_ranges' above:
 networkUris = a list of network names that you want to include in the set.  Example ['net1', 'net2']
 nativeNetworkUri = a string with only 1 network name to use as the native network
"""
network_sets = [{'name': 'NS_23', 'type': 'network-setV5', 'networkUris': ['net_23'], 'nativeNetworkUri': 'net_23'},
                {'name': 'NS_24', 'type': 'network-setV5', 'networkUris': ['net_24'], 'nativeNetworkUri': 'net_24'},
                {'name': 'NS_46', 'type': 'network-setV5', 'networkUris': ['net_46'], 'nativeNetworkUri': 'net_46'},
                {'name': 'NS_47', 'type': 'network-setV5', 'networkUris': ['net_47'], 'nativeNetworkUri': 'net_47'},
                {'name': 'NS_96', 'type': 'network-setV5', 'networkUris': ['net_96'], 'nativeNetworkUri': 'net_96'},
                {'name': 'NS_97', 'type': 'network-setV5', 'networkUris': ['net_97'], 'nativeNetworkUri': 'net_97'},
                {'name': 'NS_98', 'type': 'network-setV5', 'networkUris': ['net_98'], 'nativeNetworkUri': 'net_98'},
                {'name': 'NS_99', 'type': 'network-setV5', 'networkUris': ['net_99'], 'nativeNetworkUri': 'net_99'}]

"""
These are the network set ranges you want to add to the appliance.
NOTE: referenced ethernet network data that MUST have also been defined in either 'ethernet_networks' or 'ethernet_ranges' above:
 networkUris = This becomes populated with all the networks in the range you specify
 nativeNetworkUri = a string with only 1 network name to use as the native network
"""
network_set_ranges = [{'prefix': 'net_', 'suffix': '', 'start': 2, 'end': 22, 'name': 'VlanTrunk1', 'type': 'network-setV5', 'networkUris': None, 'nativeNetworkUri': 'net_2'},
                      {'prefix': 'net_', 'suffix': '', 'start': 25, 'end': 45, 'name': 'VlanTrunk2', 'type': 'network-setV5', 'networkUris': None, 'nativeNetworkUri': 'net_25'},
                      {'prefix': 'net_', 'suffix': '', 'start': 50, 'end': 70, 'name': 'VlanTrunk3', 'type': 'network-setV5', 'networkUris': None, 'nativeNetworkUri': 'net_50'},
                      {'prefix': 'net_', 'suffix': '', 'start': 75, 'end': 95, 'name': 'VlanTrunk4', 'type': 'network-setV5', 'networkUris': None, 'nativeNetworkUri': 'net_75'}
                      ]

"""
These are the FibreChannel networks you want to add to the appliance
"""
fc_networks = [{'name': 'SAN-1-A', 'type': 'fc-networkV4', 'linkStabilityTime': 30, 'autoLoginRedistribution': True, 'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'},
               {'name': 'SAN-2-B', 'type': 'fc-networkV4', 'linkStabilityTime': 30, 'autoLoginRedistribution': True, 'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'},
               {'name': 'SAN-3-A', 'type': 'fc-networkV4', 'linkStabilityTime': 30, 'autoLoginRedistribution': True, 'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'},
               {'name': 'SAN-4-B', 'type': 'fc-networkV4', 'linkStabilityTime': 30, 'autoLoginRedistribution': True, 'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'},
               {'name': 'SAN-5-A', 'type': 'fc-networkV4', 'linkStabilityTime': 30, 'autoLoginRedistribution': True, 'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'},
               {'name': 'SAN-6-B', 'type': 'fc-networkV4', 'linkStabilityTime': 30, 'autoLoginRedistribution': True, 'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'},
               ]

"""
These are the FCoE networks you want to add to the appliance
"""
fcoe_networks = [{'name': 'fcoe-100', 'type': 'fcoe-networkV4', 'vlanId': 100},
                 {'name': 'fcoe-2000', 'type': 'fcoe-networkV4', 'vlanId': 2000},
                 {'name': 'fcoe-100b', 'type': 'fcoe-networkV4', 'vlanId': 100},
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
# Synergy
These are the enclosure group(s) you want to add to the appliance.
NOTE:  There are some special fields:
 enclosureTypeUri = /rest/enclosure-types/SY12000
 logicalInterconnectGroupUri = for each ic bay, you must specify 'LIG:' + the name of the LIG for that bay
                               The LIG you choose MUST be defined in your datafile (or exist on the appliance)
 enclosureCount = The number of enclosures in the group
"""

enc_groups = [{'name': 'Tbird-EG',
               'type': 'EnclosureGroupV8',
               'enclosureCount': 1,
               'enclosureTypeUri': '/rest/enclosure-types/SY12000',
               'stackingMode': 'Enclosure',
               'interconnectBayMappingCount': 2,
               'configurationScript': None,
               'interconnectBayMappings':
               [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
                {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG1'}],
               'ipAddressingMode': "External",
               'ipRangeUris': [],
               'powerMode': "RedundantPowerFeed"
               }
              ]


"""
These are the TBird enclosure(s) you want to add to the appliance
NOTE: There is a special field:
 enclosureGroupUri = You must specify EG: + the name of the enclosure group to associate the enclosure with
                     The EG you choose MUST be defined in your datafile (or exist on the appliance)

"""
encs = [
    {'hostname': '15.186.22.181', 'username': 'Administrator', 'password': 'compaq', 'enclosureGroupUri': 'EG:Tbird-EG', 'force': False, 'licensingIntent': 'OneViewNoiLO'},
]

"""
The uplinkset(s) you want to use in your LIG(s)
NOTE:  There are some special fields
 networkUris = a list of network names to include in the uplinkset
 nativeNetworkUri = a string containing the name of the network you want to be the native network
"""
uplink_sets = {'IC': {
    'name': 'IC',
    'ethernetNetworkType': 'Untagged',
    'networkType': 'Ethernet',
    'networkUris': ['IC'],
    'mode': 'Auto',
    'lacpTimer': 'Short',
    'logicalPortConfigInfos': [{'bay': '3', 'port': 'Q1.1', 'speed': 'Auto'}]},
    'pvlan_us': {'name': 'pvlan_us',
                 'ethernetNetworkType': 'Tagged',
                 'networkType': 'Ethernet',
                 'networkUris': ['Net_10', 'Net_8'],
                 'nativeNetworkUri': None,
                 'mode': 'Auto',
                 # -> PVLAN
                 'privateVlanDomains': [{'isolatedNetwork': {'uri': 'Net_10'}, 'primaryNetwork': {'uri': 'Net_8'}}],  # PV Lan
                 # -> PVLAN
                 'logicalPortConfigInfos': [{'bay': '3', 'port': 'Q6', 'speed': 'Speed25G'}, ]},
    'Tunnel1': {'name': 'Tunnel1',
                'ethernetNetworkType': 'Tunnel',
                'networkType': 'Ethernet',
                'networkUris': ['Tunnel1'],
                'nativeNetworkUri': None,
                'mode': 'Auto',
                'lacpTimer': 'Long',
                'logicalPortConfigInfos': [{'bay': '3', 'port': 'Q2.3', 'speed': 'Auto'}]},
    'BigPipe1': {'name': 'BigPipe1',
                 'ethernetNetworkType': 'Tagged',
                 'networkType': 'Ethernet',
                 'networkUris': make_range_list(ethernet_ranges[0]) + make_range_list(ethernet_ranges[1]),
                 'nativeNetworkUri': None,
                 'mode': 'Auto',
                 'logicalPortConfigInfos': [{'bay': '3', 'port': 'Q4.1', 'speed': 'Auto'},
                                            {'bay': '3', 'port': 'Q4.2', 'speed': 'Auto'}]},
    #               'SAN-1-A': {'name': 'SAN-1-A',
    #                           'ethernetNetworkType': 'NotApplicable',
    #                           'networkType': 'FibreChannel',
    #                           'networkUris': ['SAN-1-A'],
    #                           'nativeNetworkUri': None,
    #                           'mode': 'Auto',
    #                           'logicalPortConfigInfos': [{'bay': '3', 'port': 'Q3.4', 'speed': 'Auto'}]},
}

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
         'type': 'logical-interconnect-groupV7',
         'enclosureType': 'SY12000',
         'ethernetSettings': None,
         'interconnectMapTemplate': [
             {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
             {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
         ],
         'enclosureIndexes': [1],
         'interconnectBaySet': 3,
         'redundancyType': 'Redundant',
         'uplinkSets': [uplink_sets['IC'],
                        uplink_sets['pvlan_us'],
                        uplink_sets['Tunnel1'],
                        uplink_sets['BigPipe1'],
                        #                        uplink_sets['SAN-1-A'],
                        ],
         'stackingMode': 'Enclosure',
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None},
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
        'enclosureUris': ['ENC:0000A66101', ],
        'enclosureGroupUri': 'EG:Tbird-EG',
        'firmwareBaselineUri': None,
        'forceInstallFirmware': False
        }]

"""
Server Profile boot 'order' options are 'PXE' or 'HardDisk'.

"""
server_profiles = [{'type': 'ServerProfileV11', 'serverHardwareUri': '0000A66101, bay 1',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:0000A66101', 'enclosureGroupUri': 'EG:Tbird-EG', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'Tbird-1Enc_Bay1-SY660cGen9', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                    'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                    'bios': {'manageBios': False, 'overriddenSettings': []},
                    'hideUnusedFlexNics':True,
                    'iscsiInitiatorName':'',
                    'osDeploymentSettings':None,
                    'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:IC', 'boot': {'priority': 'Primary'}, 'mac': None, 'wwpn': '', 'wwnn': '', "requiestedVFS": "Auto"},
                                    {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:net_10', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500', 'networkUri': 'ETH:net_11', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 4, 'name': '4', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 5, 'name': '5', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk4', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 6, 'name': '6', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS_23', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 7, 'name': '7', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS_24', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    #                                    {'id': 9, 'name': '9', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-e', 'requestedMbps': '8000', 'networkUri': 'FC:SAN-3-A', 'boot': {'priority': 'Primary', 'targets': [{'arrayWwpn': '21110002ac00364c', 'lun': '0'}]}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    #                                    {'id': 10, 'name': '10', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:2-e', 'requestedMbps': '8000', 'networkUri': 'FC:SAN-4-B', 'boot': {'priority': 'Secondary', 'targets': [{'arrayWwpn': '20110002ac00364c', 'lun': '0'}]}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    ]},
                   ]

server_profile_templates = [
    {'type': 'ServerProfileTemplateV2',
     'serverHardwareTypeUri': 'SHT:SY 660 Gen9 1', 'enclosureGroupUri': 'EG:Tbird-EG',
     'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
     'name': 'Profile1', 'description': '', 'affinity': 'Bay',
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
     'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                      'requestedMbps': '2000', 'networkUri': 'ETH:IC',
                      'boot': {'priority': 'Primary'}},
                     {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b',
                      'requestedMbps': '2000', 'networkUri': 'NS:VlanTrunk3',
                      'boot': {'priority': 'NotBootable'}},
                     ]},
    {'type': 'ServerProfileTemplateV2',
     'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1', 'enclosureGroupUri': 'EG:Tbird-EG',
     'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
     'name': 'Profile2', 'description': '', 'affinity': 'Bay',
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
     'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                      'requestedMbps': '2000', 'networkUri': 'ETH:IC',
                      'boot': {'priority': 'Primary'}},
                     {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b',
                      'requestedMbps': '2000', 'networkUri': 'NS:VlanTrunk3',
                      'boot': {'priority': 'NotBootable'}},
                     ]},
]

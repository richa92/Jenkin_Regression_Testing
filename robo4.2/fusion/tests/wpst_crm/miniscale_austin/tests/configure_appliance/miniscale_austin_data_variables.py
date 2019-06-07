def make_range_list(vrange):
    rlist = []
    for x in xrange(vrange['start'], (vrange['end'] + 1)):
        rlist.append(vrange['prefix'] + str(x) + vrange['suffix'])
    return rlist


def rlist(start, end, prefix='ENet', suffix=''):
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
ssh_credentials = {'userName': 'root', 'password': 'hpvse1'}

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
               'app1Ipv4Addr': '15.186.10.xx',
               'app2Ipv4Addr': '15.186.11.xx',
               'virtIpv4Addr': '15.186.9.xx',
               'ipv6Type': 'UNCONFIGURE',
               'hostname': 'ci-manager-eagle3.us.rdlabs.hpecorp.net',
               'confOneNode': True,
               'domainName': 'usa.hp.com',
               'aliasDisabled': True,
               }]
             }


"""
This is the time and locale settings used during FTS.
"""
timeandlocale = {'type': 'TimeAndLocale', 'dateTime': None, 'timezone': 'UTC', 'ntpServers': ['ntp.hp.net'], 'locale': 'en_US.UTF-8'}

"""
These are the virtual address ranges for MAC, WWN and SERIAL numbers
"""
ranges = [{'name': 'MiniScaleAustin-MAC', 'type': 'Range', 'category': 'id-range-VMAC', 'rangeCategory': 'CUSTOM', 'startAddress': '9A:DC:8C:60:00:00', 'endAddress': '9A:DC:8C:6F:FF:FF', 'enabled': True},
          {'name': 'MiniScaleAustin-WWN', 'type': 'Range', 'category': 'id-range-VWWN', 'rangeCategory': 'CUSTOM', 'startAddress': '10:00:B2:0D:B0:C0:00:00', 'endAddress': '10:00:B2:0D:B0:CF:FF:FF', 'enabled': True},
          {'name': 'MiniScaleAustin-SN', 'type': 'Range', 'category': 'id-range-VSN', 'rangeCategory': 'CUSTOM', 'startAddress': 'VCGFMGP000', 'endAddress': 'VCGFMGPZZZ', 'enabled': True}]

"""
These are the users you want to create on the appliance
"""
users = [{'userName': 'Serveradmin', 'password': 'Serveradmin', 'fullName': 'Serveradmin', 'roles': ['Server administrator'], 'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'Networkadmin', 'password': 'Networkadmin', 'fullName': 'Networkadmin', 'roles': ['Network administrator'], 'emailAddress': 'nat@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'Backupadmin', 'password': 'Backupadmin', 'fullName': 'Backupadmin', 'roles': ['Backup administrator'], 'emailAddress': 'backup@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'Noprivledge', 'password': 'Noprivledge', 'fullName': 'Noprivledge', 'roles': ['Read only'], 'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'}
         ]

"""
These are the ETHERNET networks you want to add to the appliance
"""
ethernet_networks = [{'name': 'Eth_Untagged',
                      'type': 'ethernet-networkV4',
                      'vlanId': None,
                      'purpose': 'General',
                      'smartLink': False,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Untagged'},
                     {'name': 'Eth_Tunnel',
                      'type': 'ethernet-networkV4',
                      'vlanId': None,
                      'purpose': 'General',
                      'smartLink': False,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tunnel'},
                     ]
bulk_ethernet_network = {"vlanIdRange": "4-1203", "purpose": "General", "namePrefix": "Net", "smartLink": False, "privateNetwork": False, "bandwidth": {"maximumBandwidth": 10000, "typicalBandwidth": 2000}, "type": "bulk-ethernet-networkV1"}
"""
These are the RANGES of ETHERNET networks you want to add to the appliance.
"""
ethernet_ranges = [
    {'prefix': 'Net_', 'suffix': '', 'start': 4, 'end': 1203, 'name': None, 'type': 'ethernet-networkV4',
     'vlanId': None, 'purpose': 'General', 'smartLink': False, 'privateNetwork': False, 'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged'},
]

"""
These are the network sets you want to add to the appliance.
NOTE: There are 2 fields that use data that MUST have also been defined in either 'ethernet_networks' or 'ethernet_ranges' above:
 networkUris = a list of network names that you want to include in the set.  Example ['net1', 'net2']
 nativeNetworkUri = a string with only 1 network name to use as the native network
"""
network_sets = [
    {'name': 'VlanTrunk1', 'type': 'network-setV4', 'networkUris': rlist(4, 113, 'Net_', ''), 'nativeNetworkUri': 'Net_4'},
    {'name': 'VlanTrunk2', 'type': 'network-setV4', 'networkUris': rlist(114, 253, 'Net_', ''), 'nativeNetworkUri': 'Net_114'},
    {'name': 'VlanTrunk3', 'type': 'network-setV4', 'networkUris': rlist(254, 413, 'Net_', ''), 'nativeNetworkUri': 'Net_254'},
    {'name': 'VlanTrunk4', 'type': 'network-setV4', 'networkUris': rlist(414, 563, 'Net_', ''), 'nativeNetworkUri': 'Net_414'},
    {'name': 'VlanTrunk5', 'type': 'network-setV4', 'networkUris': rlist(564, 723, 'Net_', ''), 'nativeNetworkUri': 'Net_564'},
    {'name': 'VlanTrunk6', 'type': 'network-setV4', 'networkUris': rlist(724, 883, 'Net_', ''), 'nativeNetworkUri': 'Net_724'},
    {'name': 'VlanTrunk7', 'type': 'network-setV4', 'networkUris': rlist(884, 1003, 'Net_', ''), 'nativeNetworkUri': 'Net_884'},
    {'name': 'VlanTrunk8', 'type': 'network-setV4', 'networkUris': rlist(1004, 1203, 'Net_', ''), 'nativeNetworkUri': 'Net_1004'}
]

"""
These are the FibreChannel networks you want to add to the appliance
"""
fc_networks = [{'name': 'FC_A_1', 'type': 'fc-networkV4', 'linkStabilityTime': 30, 'autoLoginRedistribution': True, 'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'},
               {'name': 'FC_B_4', 'type': 'fc-networkV4', 'linkStabilityTime': 30, 'autoLoginRedistribution': True, 'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'}
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
enc_groups = [{'name': 'EG',
               'enclosureCount': 3,
               'configurationScript': None,
               'interconnectBayMappings':
               [{'enclosureIndex': 1, 'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:LIG_CARBON'},
                {'enclosureIndex': 2, 'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:LIG_CARBON'},
                {'enclosureIndex': 3, 'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:LIG_CARBON'},
                {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG_POTASH'},
                {'enclosureIndex': 1, 'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:LIG_CARBON'},
                {'enclosureIndex': 2, 'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:LIG_CARBON'},
                {'enclosureIndex': 3, 'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:LIG_CARBON'},
                {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG_POTASH'}],
               'ipAddressingMode': "DHCP",
               'ipRangeUris': [],
               'powerMode': "RedundantPowerFeed"
               }
              ]

"""
The uplinkset(s) you want to use in your LIG(s)
NOTE:  There are some special fields
 networkUris = a list of network names to include in the uplinkset
 nativeNetworkUri = a string containing the name of the network you want to be the native network
"""
uplink_sets = {
    'FC_A_1': {'name': 'US_FC_A_1',
               'ethernetNetworkType': 'NotApplicable',
               'networkType': 'FibreChannel',
               'networkUris': ['FC_A_1'],
               'nativeNetworkUri': None,
               'mode': 'Auto',
               'lacpTimer': 'Short',
               'logicalPortConfigInfos': [{'enclosure': '-1', 'bay': '1', 'port': '1', 'speed': 'Auto'},
                                          {'enclosure': '-1', 'bay': '1', 'port': '2', 'speed': 'Auto'}]},
    'FC_B_4': {'name': 'US_FC_B_4',
               'ethernetNetworkType': 'NotApplicable',
               'networkType': 'FibreChannel',
               'networkUris': ['FC_B_4'],
               'nativeNetworkUri': None,
               'mode': 'Auto',
               'lacpTimer': 'Short',
               'logicalPortConfigInfos': [{'enclosure': '-1', 'bay': '4', 'port': '1', 'speed': 'Auto'}]},
    'BIG_PIPE_ENET': {'name': 'US_BIG_PIPE_ENET',
                      'ethernetNetworkType': 'Tagged',
                      'networkType': 'Ethernet',
                      'networkUris': ['Net_1'] + make_range_list({'prefix': 'Net_', 'suffix': '', 'start': 4, 'end': 1203}),
                      'nativeNetworkUri': None,
                      'mode': 'Auto',
                      'lacpTimer': 'Short',
                      'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q1.1', 'speed': 'Auto'},
                                                 {'enclosure': '2', 'bay': '6', 'port': 'Q1.1', 'speed': 'Auto'}]},
    'Untagged': {'name': 'US_Untagged',
                 'ethernetNetworkType': 'Untagged',
                 'networkType': 'Ethernet',
                 'networkUris': ['Eth_Untagged'],
                 'nativeNetworkUri': None,
                 'mode': 'Auto',
                 'lacpTimer': 'Short',
                 'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q1.3', 'speed': 'Auto'},
                                            {'enclosure': '2', 'bay': '6', 'port': 'Q1.3', 'speed': 'Auto'}]},
    'Tunnel': {'name': 'US_Tunnel',
               'ethernetNetworkType': 'Tunnel',
               'networkType': 'Ethernet',
               'networkUris': ['Eth_Tunnel'],
               'nativeNetworkUri': None,
               'mode': 'Auto',
               'lacpTimer': 'Short',
               'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q1.4', 'speed': 'Auto'},
                                          {'enclosure': '2', 'bay': '6', 'port': 'Q1.4', 'speed': 'Auto'}]}
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
ligs = [
    {'name': 'LIG_POTASH',
     'type': 'logical-interconnect-groupV6',
     'enclosureType': 'SY12000',
     'ethernetSettings': None,
     'interconnectMapTemplate': [{'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
                                 {'bay': 6, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
                                 {'bay': 3, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
                                 {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
                                 {'bay': 3, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3},
                                 {'bay': 6, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3},
                                 ],
     'enclosureIndexes': [1, 2, 3],
     'interconnectBaySet':3,
     'redundancyType': 'HighlyAvailable',
     'uplinkSets': [
             uplink_sets['BIG_PIPE_ENET'],
             uplink_sets['Untagged'],
             uplink_sets['Tunnel']
     ],
     'stackingMode': 'Enclosure',
     'state': 'Active',
     'telemetryConfiguration': None,
     'snmpConfiguration': None},
    {'name': 'LIG_CARBON',
     'type': 'logical-interconnect-groupV400',
     'enclosureType': 'SY12000',
     'ethernetSettings': None,
     'interconnectMapTemplate': [{'bay': 1, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1},
                                 {'bay': 4, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1},
                                 ],
     'enclosureIndexes': [-1],
     'interconnectBaySet': 1,
     'redundancyType': 'Redundant',
     'uplinkSets': [uplink_sets['FC_A_1'],
                    uplink_sets['FC_B_4'],
                    ],
     'stackingMode': 'Enclosure',
     'state': 'Active',
     'telemetryConfiguration': None,
     'snmpConfiguration': None}
]

"""
Rename enclosure to more easier names
"""
enc_names = {
    'CN744502F2': 'Encl1', 'CN744502FB': 'Encl2', 'CN754408RS': 'Encl3'
}

"""
The LE(s) you want to add to the appliance TCLASS ONLY
NOTE:  There are some special fields
[TClass LE]
 enclosureUris = a list of enclosures to add to this LE - 'ENC:' + the name of the enclosure (by default the serial number of the enclosure)
 enclosureGroupUri = You must specify EG: + the name of the enclosure group to associate the enclosure with
                     The EG you choose MUST be defined in your datafile (or exist on the appliance)
"""
les = [{'name': 'LE',
        'enclosureUris': ['ENC:Encl1', 'ENC:Encl2', 'ENC:Encl3'],
        'enclosureGroupUri': 'EG:EG',
        'firmwareBaselineUri': None,
        'forceInstallFirmware': False
        }]


"""
Server Profile no hardware assigned.
Boot 'order' options are 'PXE' or 'HardDisk'.
"""
server_profiles_nohw = [
    {'type': 'ServerProfileV10', 'serverHardwareUri': None,
     'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'UserDefined', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'ServerProfile_Encl1_Bay1', 'description': 'Server Profile for server in Enclosure 1, Bay 1', 'affinity': 'Bay',
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'hideUnusedFlexNics':True,
     'serialNumber':'VCGFMGP000',
     'uuid':'bee869fe-0af6-4342-8779-743a9612f75f',
     'iscsiInitiatorName':'',
     'osDeploymentSettings':None,
     'connectionSettings':{
         'connections': [
             {'id': 1, 'name': 'conn_FC_A_1', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_A_1', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:00', 'wwpn': '10:00:b2:0d:b0:c0:00:00', 'wwnn': '10:00:b2:0d:b0:c0:00:01'},
             {'id': 2, 'name': 'conn_FC_B_4', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:2', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_B_4', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:01', 'wwpn': '10:00:b2:0d:b0:c0:00:02', 'wwnn': '10:00:b2:0d:b0:c0:00:03'},
             {'id': 3, 'name': 'conn_VlanTrunk1_A', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk1', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:02', 'wwpn': '', 'wwnn': ''},
             {'id': 4, 'name': 'conn_VlanTrunk1_B', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk1', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:03', 'wwpn': '', 'wwnn': ''},
             {'id': 5, 'name': 'conn_Eth_Untagged_A', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:Eth_Untagged', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:06', 'wwpn': '', 'wwnn': ''},
             {'id': 6, 'name': 'conn_Eth_Untagged_B', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '2500', 'networkUri': 'ETH:Eth_Untagged', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:07', 'wwpn': '', 'wwnn': ''}
         ]}
     },
    {'type': 'ServerProfileV10', 'serverHardwareUri': None,
     'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'UserDefined', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'ServerProfile_Encl1_Bay2', 'description': 'Server Profile for server in Enclosure 1, Bay 2', 'affinity': 'Bay',
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'hideUnusedFlexNics':True,
     'serialNumber':'VCGFMGP00I',
     'uuid':'7a9bcb5a-8756-4bc6-a62b-627f241199c7',
     'iscsiInitiatorName':'',
     'osDeploymentSettings':None,
     'connectionSettings':{
         'connections': [
             {'id': 1, 'name': 'conn_FC_A_1', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_A_1', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:B0', 'wwpn': '10:00:b2:0d:b0:c0:00:04', 'wwnn': '10:00:b2:0d:b0:c0:00:05'},
             {'id': 2, 'name': 'conn_FC_B_4', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:2', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_B_4', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:B1', 'wwpn': '10:00:b2:0d:b0:c0:00:06', 'wwnn': '10:00:b2:0d:b0:c0:00:07'},
             {'id': 3, 'name': 'conn_VlanTrunk2_A', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk2', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:B2', 'wwpn': '', 'wwnn': ''},
             {'id': 4, 'name': 'conn_VlanTrunk2_B', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk2', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:B3', 'wwpn': '', 'wwnn': ''},
             {'id': 5, 'name': 'conn_Eth_Tunnel_A', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:Eth_Tunnel', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:B6', 'wwpn': '', 'wwnn': ''},
             {'id': 6, 'name': 'conn_Eth_Tunnel_B', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '2500', 'networkUri': 'ETH:Eth_Tunnel', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:B7', 'wwpn': '', 'wwnn': ''}
         ]}
     },
    {'type': 'ServerProfileV10', 'serverHardwareUri': None,
     'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'UserDefined', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'ServerProfile_Encl1_Bay3', 'description': 'Server Profile for server in Enclosure 1, Bay 3', 'affinity': 'Bay',
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'hideUnusedFlexNics':True,
     'serialNumber':'VCGFMGP003',
     'uuid':'e85108e8-baad-4a08-9bc8-c17c961d4b47',
     'iscsiInitiatorName':'',
     'osDeploymentSettings':None,
     'connectionSettings':{
         'connections': [
             {'id': 1, 'name': 'conn_FC_A_1', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_A_1', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:04', 'wwpn': '10:00:b2:0d:b0:c0:00:08', 'wwnn': '10:00:b2:0d:b0:c0:00:09'},
             {'id': 2, 'name': 'conn_FC_B_4', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:2', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_B_4', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:05', 'wwpn': '10:00:b2:0d:b0:c0:00:0a', 'wwnn': '10:00:b2:0d:b0:c0:00:0b'},
             {'id': 3, 'name': 'conn_VlanTrunk3_A', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk3', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:08', 'wwpn': '', 'wwnn': ''},
             {'id': 4, 'name': 'conn_VlanTrunk3_B', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk3', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:09', 'wwpn': '', 'wwnn': ''},
             {'id': 5, 'name': 'conn_Eth_Untagged_A', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:Eth_Untagged', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:0A', 'wwpn': '', 'wwnn': ''},
             {'id': 6, 'name': 'conn_Eth_Untagged_B', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '2500', 'networkUri': 'ETH:Eth_Untagged', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:0B', 'wwpn': '', 'wwnn': ''}
         ]}
     },
    {'type': 'ServerProfileV10', 'serverHardwareUri': None,
     'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'UserDefined', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'ServerProfile_Encl1_Bay4', 'description': 'Server Profile for server in Enclosure 1, Bay 4', 'affinity': 'Bay',
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'hideUnusedFlexNics':True,
     'serialNumber':'VCGFMGP004',
     'uuid':'77af5aaa-f677-4a7f-a21f-a2ed28904502',
     'iscsiInitiatorName':'',
     'osDeploymentSettings':None,
     'connectionSettings':{
         'connections': [
             {'id': 1, 'name': 'conn_FC_A_1', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_A_1', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:0C', 'wwpn': '10:00:b2:0d:b0:c0:00:0c', 'wwnn': '10:00:b2:0d:b0:c0:00:0d'},
             {'id': 2, 'name': 'conn_FC_B_4', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:2', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_B_4', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:0D', 'wwpn': '10:00:b2:0d:b0:c0:00:0e', 'wwnn': '10:00:b2:0d:b0:c0:00:0f'},
             {'id': 3, 'name': 'conn_VlanTrunk4_A', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk4', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:0E', 'wwpn': '', 'wwnn': ''},
             {'id': 4, 'name': 'conn_VlanTrunk4_B', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk4', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:0F', 'wwpn': '', 'wwnn': ''},
             {'id': 5, 'name': 'conn_Eth_Tunnel_A', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:Eth_Tunnel', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:10', 'wwpn': '', 'wwnn': ''},
             {'id': 6, 'name': 'conn_Eth_Tunnel_B', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '2500', 'networkUri': 'ETH:Eth_Tunnel', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:11', 'wwpn': '', 'wwnn': ''}
         ]}
     },
    {'type': 'ServerProfileV10', 'serverHardwareUri': None,
     'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'UserDefined', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'ServerProfile_Encl1_Bay6', 'description': 'Server Profile for server in Enclosure 1, Bay 6', 'affinity': 'Bay',
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'hideUnusedFlexNics':True,
     'serialNumber':'VCGFMGP005',
     'uuid':'6aaf0d42-9a47-4146-8d3a-1458acf35f60',
     'iscsiInitiatorName':'',
     'osDeploymentSettings':None,
     'connectionSettings':{
         'connections': [
             {'id': 1, 'name': 'conn_FC_A_1', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_A_1', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:12', 'wwpn': '10:00:b2:0d:b0:c0:00:10', 'wwnn': '10:00:b2:0d:b0:c0:00:11'},
             {'id': 2, 'name': 'conn_FC_B_4', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:2', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_B_4', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:13', 'wwpn': '10:00:b2:0d:b0:c0:00:12', 'wwnn': '10:00:b2:0d:b0:c0:00:13'},
             {'id': 3, 'name': 'conn_VlanTrunk5_A', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk5', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:14', 'wwpn': '', 'wwnn': ''},
             {'id': 4, 'name': 'conn_VlanTrunk5_B', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk5', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:15', 'wwpn': '', 'wwnn': ''},
             {'id': 5, 'name': 'conn_Eth_Untagged_A', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:Eth_Untagged', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:16', 'wwpn': '', 'wwnn': ''},
             {'id': 6, 'name': 'conn_Eth_Untagged_B', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '2500', 'networkUri': 'ETH:Eth_Untagged', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:17', 'wwpn': '', 'wwnn': ''}
         ]}
     },
    {'type': 'ServerProfileV10', 'serverHardwareUri': None,
     'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'UserDefined', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'ServerProfile_Encl1_Bay7', 'description': 'Server Profile for server in Enclosure 1, Bay 7', 'affinity': 'Bay',
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'hideUnusedFlexNics':True,
     'serialNumber':'VCGFMGP006',
     'uuid':'d7524b47-459f-4ae2-a26d-09ad44154ac7',
     'iscsiInitiatorName':'',
     'osDeploymentSettings':None,
     'connectionSettings':{
         'connections': [
             {'id': 1, 'name': 'conn_FC_A_1', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_A_1', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:18', 'wwpn': '10:00:b2:0d:b0:c0:00:14', 'wwnn': '10:00:b2:0d:b0:c0:00:15'},
             {'id': 2, 'name': 'conn_FC_B_4', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:2', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_B_4', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:19', 'wwpn': '10:00:b2:0d:b0:c0:00:16', 'wwnn': '10:00:b2:0d:b0:c0:00:17'},
             {'id': 3, 'name': 'conn_VlanTrunk6_A', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk6', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:1A', 'wwpn': '', 'wwnn': ''},
             {'id': 4, 'name': 'conn_VlanTrunk6_B', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk6', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:1B', 'wwpn': '', 'wwnn': ''},
             {'id': 5, 'name': 'conn_Eth_Tunnel_A', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:Eth_Tunnel', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:1C', 'wwpn': '', 'wwnn': ''},
             {'id': 6, 'name': 'conn_Eth_Tunnel_B', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '2500', 'networkUri': 'ETH:Eth_Tunnel', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:1D', 'wwpn': '', 'wwnn': ''}
         ]}
     },
    {'type': 'ServerProfileV10', 'serverHardwareUri': None,
     'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'UserDefined', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'ServerProfile_Encl1_Bay8', 'description': 'Server Profile for server in Enclosure 1, Bay 8', 'affinity': 'Bay',
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'hideUnusedFlexNics':True,
     'serialNumber':'VCGFMGP007',
     'uuid':'f52e7ddf-3b21-40fa-bdd7-ec5e61ea005a',
     'iscsiInitiatorName':'',
     'osDeploymentSettings':None,
     'connectionSettings':{
         'connections': [
             {'id': 1, 'name': 'conn_FC_A_1', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_A_1', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:1E', 'wwpn': '10:00:b2:0d:b0:c0:00:18', 'wwnn': '10:00:b2:0d:b0:c0:00:19'},
             {'id': 2, 'name': 'conn_FC_B_4', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:2', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_B_4', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:1F', 'wwpn': '10:00:b2:0d:b0:c0:00:1a', 'wwnn': '10:00:b2:0d:b0:c0:00:1b'},
             {'id': 3, 'name': 'conn_VlanTrunk7_A', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk7', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:20', 'wwpn': '', 'wwnn': ''},
             {'id': 4, 'name': 'conn_VlanTrunk7_B', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk7', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:21', 'wwpn': '', 'wwnn': ''},
             {'id': 5, 'name': 'conn_Eth_Untagged_A', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:Eth_Untagged', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:22', 'wwpn': '', 'wwnn': ''},
             {'id': 6, 'name': 'conn_Eth_Untagged_B', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '2500', 'networkUri': 'ETH:Eth_Untagged', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:23', 'wwpn': '', 'wwnn': ''}
         ]}
     },
    {'type': 'ServerProfileV10', 'serverHardwareUri': None,
     'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'UserDefined', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'ServerProfile_Encl1_Bay9', 'description': 'Server Profile for server in Enclosure 1, Bay 9', 'affinity': 'Bay',
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'hideUnusedFlexNics':True,
     'serialNumber':'VCGFMGP009',
     'uuid':'277fa7f5-ddff-4eb6-9b54-25dab8be94e4',
     'iscsiInitiatorName':'',
     'osDeploymentSettings':None,
     'connectionSettings':{
         'connections': [
             {'id': 1, 'name': 'conn_FC_A_1', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_A_1', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:24', 'wwpn': '10:00:b2:0d:b0:c0:00:1c', 'wwnn': '10:00:b2:0d:b0:c0:00:1d'},
             {'id': 2, 'name': 'conn_FC_B_4', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:2', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_B_4', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:25', 'wwpn': '10:00:b2:0d:b0:c0:00:1e', 'wwnn': '10:00:b2:0d:b0:c0:00:1f'},
             {'id': 3, 'name': 'conn_VlanTrunk8_A', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk8', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:26', 'wwpn': '', 'wwnn': ''},
             {'id': 4, 'name': 'conn_VlanTrunk8_B', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk8', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:27', 'wwpn': '', 'wwnn': ''},
             {'id': 5, 'name': 'conn_Eth_Tunnel_A', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:Eth_Tunnel', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:28', 'wwpn': '', 'wwnn': ''},
             {'id': 6, 'name': 'conn_Eth_Tunnel_B', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '2500', 'networkUri': 'ETH:Eth_Tunnel', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:29', 'wwpn': '', 'wwnn': ''}
         ]}
     },
    {'type': 'ServerProfileV10', 'serverHardwareUri': None,
     'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'UserDefined', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'ServerProfile_Encl2_Bay1', 'description': 'Server Profile for server in Enclosure 2, Bay 1', 'affinity': 'Bay',
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'hideUnusedFlexNics':True,
     'serialNumber':'VCGFMGP00A',
     'uuid':'5f5d6198-ed00-4a7a-9486-18c8ac81f3cb',
     'iscsiInitiatorName':'',
     'osDeploymentSettings':None,
     'connectionSettings':{
         'connections': [
             {'id': 1, 'name': 'conn_FC_A_1', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_A_1', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:2A', 'wwpn': '10:00:b2:0d:b0:c0:00:20', 'wwnn': '10:00:b2:0d:b0:c0:00:21'},
             {'id': 2, 'name': 'conn_FC_B_4', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:2', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_B_4', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:2B', 'wwpn': '10:00:b2:0d:b0:c0:00:22', 'wwnn': '10:00:b2:0d:b0:c0:00:23'},
             {'id': 3, 'name': 'conn_VlanTrunk1_A', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk1', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:2C', 'wwpn': '', 'wwnn': ''},
             {'id': 4, 'name': 'conn_VlanTrunk1_B', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk1', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:2D', 'wwpn': '', 'wwnn': ''},
             {'id': 5, 'name': 'conn_Eth_Untagged_A', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:Eth_Untagged', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:2E', 'wwpn': '', 'wwnn': ''},
             {'id': 6, 'name': 'conn_Eth_Untagged_B', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '2500', 'networkUri': 'ETH:Eth_Untagged', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:2F', 'wwpn': '', 'wwnn': ''}
         ]}
     },
    {'type': 'ServerProfileV10', 'serverHardwareUri': None,
     'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'UserDefined', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'ServerProfile_Encl2_Bay2', 'description': 'Server Profile for server in Enclosure 2, Bay 2', 'affinity': 'Bay',
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'hideUnusedFlexNics':True,
     'serialNumber':'VCGFMGP00B',
     'uuid':'b6db1c86-47fd-4a72-b110-db21d7d82114',
     'iscsiInitiatorName':'',
     'osDeploymentSettings':None,
     'connectionSettings':{
         'connections': [
             {'id': 1, 'name': 'conn_FC_A_1', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_A_1', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:30', 'wwpn': '10:00:b2:0d:b0:c0:00:24', 'wwnn': '10:00:b2:0d:b0:c0:00:25'},
             {'id': 2, 'name': 'conn_FC_B_4', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:2', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_B_4', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:31', 'wwpn': '10:00:b2:0d:b0:c0:00:26', 'wwnn': '10:00:b2:0d:b0:c0:00:27'},
             {'id': 3, 'name': 'conn_VlanTrunk2_A', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk2', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:32', 'wwpn': '', 'wwnn': ''},
             {'id': 4, 'name': 'conn_VlanTrunk2_B', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk2', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:33', 'wwpn': '', 'wwnn': ''},
             {'id': 5, 'name': 'conn_Eth_Tunnel_A', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:Eth_Tunnel', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:34', 'wwpn': '', 'wwnn': ''},
             {'id': 6, 'name': 'conn_Eth_Tunnel_B', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '2500', 'networkUri': 'ETH:Eth_Tunnel', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:35', 'wwpn': '', 'wwnn': ''}
         ]}
     },
    {'type': 'ServerProfileV10', 'serverHardwareUri': None,
     'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'UserDefined', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'ServerProfile_Encl2_Bay3', 'description': 'Server Profile for server in Enclosure 2, Bay 3', 'affinity': 'Bay',
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'hideUnusedFlexNics':True,
     'serialNumber':'VCGFMGP00C',
     'uuid':'72f87947-855d-491b-90e4-0962ebc8bdb0',
     'iscsiInitiatorName':'',
     'osDeploymentSettings':None,
     'connectionSettings':{
         'connections': [
             {'id': 1, 'name': 'conn_FC_A_1', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_A_1', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:36', 'wwpn': '10:00:b2:0d:b0:c0:00:28', 'wwnn': '10:00:b2:0d:b0:c0:00:29'},
             {'id': 2, 'name': 'conn_FC_B_4', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:2', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_B_4', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:37', 'wwpn': '10:00:b2:0d:b0:c0:00:2a', 'wwnn': '10:00:b2:0d:b0:c0:00:2b'},
             {'id': 3, 'name': 'conn_VlanTrunk3_A', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk3', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:38', 'wwpn': '', 'wwnn': ''},
             {'id': 4, 'name': 'conn_VlanTrunk3_B', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk3', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:39', 'wwpn': '', 'wwnn': ''},
             {'id': 5, 'name': 'conn_Eth_Untagged_A', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:Eth_Untagged', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:3A', 'wwpn': '', 'wwnn': ''},
             {'id': 6, 'name': 'conn_Eth_Untagged_B', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '2500', 'networkUri': 'ETH:Eth_Untagged', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:3B', 'wwpn': '', 'wwnn': ''}
         ]}
     },
    {'type': 'ServerProfileV10', 'serverHardwareUri': None,
     'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'UserDefined', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'ServerProfile_Encl2_Bay4', 'description': 'Server Profile for server in Enclosure 2, Bay 4', 'affinity': 'Bay',
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'hideUnusedFlexNics':True,
     'serialNumber':'VCGFMGP00F',
     'uuid':'a3622e39-d9ff-4047-9e0f-bfbd59c52abd',
     'iscsiInitiatorName':'',
     'osDeploymentSettings':None,
     'connectionSettings':{
         'connections': [
             {'id': 1, 'name': 'conn_FC_A_1', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_A_1', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:3C', 'wwpn': '10:00:b2:0d:b0:c0:00:2c', 'wwnn': '10:00:b2:0d:b0:c0:00:2d'},
             {'id': 2, 'name': 'conn_FC_B_4', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:2', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_B_4', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:3D', 'wwpn': '10:00:b2:0d:b0:c0:00:2e', 'wwnn': '10:00:b2:0d:b0:c0:00:2f'},
             {'id': 3, 'name': 'conn_VlanTrunk4_A', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk4', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:3E', 'wwpn': '', 'wwnn': ''},
             {'id': 4, 'name': 'conn_VlanTrunk4_B', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk4', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:3F', 'wwpn': '', 'wwnn': ''},
             {'id': 5, 'name': 'conn_Eth_Tunnel_A', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:Eth_Tunnel', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:40', 'wwpn': '', 'wwnn': ''},
             {'id': 6, 'name': 'conn_Eth_Tunnel_B', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '2500', 'networkUri': 'ETH:Eth_Tunnel', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:41', 'wwpn': '', 'wwnn': ''}
         ]}
     },
    {'type': 'ServerProfileV10', 'serverHardwareUri': None,
     'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'UserDefined', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'ServerProfile_Encl2_Bay6', 'description': 'Server Profile for server in Enclosure 2, Bay 6', 'affinity': 'Bay',
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'hideUnusedFlexNics':True,
     'serialNumber':'VCGFMGP00G',
     'uuid':'00cbaf4b-d3c6-4d3e-a674-b9849d118adc',
     'iscsiInitiatorName':'',
     'osDeploymentSettings':None,
     'connectionSettings':{
         'connections': [
             {'id': 1, 'name': 'conn_FC_A_1', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_A_1', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:42', 'wwpn': '10:00:b2:0d:b0:c0:00:30', 'wwnn': '10:00:b2:0d:b0:c0:00:31'},
             {'id': 2, 'name': 'conn_FC_B_4', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:2', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_B_4', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:43', 'wwpn': '10:00:b2:0d:b0:c0:00:32', 'wwnn': '10:00:b2:0d:b0:c0:00:33'},
             {'id': 3, 'name': 'conn_VlanTrunk5_A', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk5', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:44', 'wwpn': '', 'wwnn': ''},
             {'id': 4, 'name': 'conn_VlanTrunk5_B', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk5', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:45', 'wwpn': '', 'wwnn': ''},
             {'id': 5, 'name': 'conn_Eth_Untagged_A', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:Eth_Untagged', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:46', 'wwpn': '', 'wwnn': ''},
             {'id': 6, 'name': 'conn_Eth_Untagged_B', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '2500', 'networkUri': 'ETH:Eth_Untagged', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:47', 'wwpn': '', 'wwnn': ''}
         ]}
     },
    {'type': 'ServerProfileV10', 'serverHardwareUri': None,
     'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'UserDefined', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'ServerProfile_Encl2_Bay7', 'description': 'Server Profile for server in Enclosure 2, Bay 7', 'affinity': 'Bay',
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'hideUnusedFlexNics':True,
     'serialNumber':'VCGFMGP00H',
     'uuid':'655e9061-6815-40ef-9f7d-3977e08655f7',
     'iscsiInitiatorName':'',
     'osDeploymentSettings':None,
     'connectionSettings':{
         'connections': [
             {'id': 1, 'name': 'conn_FC_A_1', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_A_1', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:48', 'wwpn': '10:00:b2:0d:b0:c0:00:34', 'wwnn': '10:00:b2:0d:b0:c0:00:35'},
             {'id': 2, 'name': 'conn_FC_B_4', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:2', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_B_4', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:49', 'wwpn': '10:00:b2:0d:b0:c0:00:36', 'wwnn': '10:00:b2:0d:b0:c0:00:37'},
             {'id': 3, 'name': 'conn_VlanTrunk6_A', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk6', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:4A', 'wwpn': '', 'wwnn': ''},
             {'id': 4, 'name': 'conn_VlanTrunk6_B', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk6', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:4B', 'wwpn': '', 'wwnn': ''},
             {'id': 5, 'name': 'conn_Eth_Tunnel_A', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:Eth_Tunnel', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:4C', 'wwpn': '', 'wwnn': ''},
             {'id': 6, 'name': 'conn_Eth_Tunnel_B', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '2500', 'networkUri': 'ETH:Eth_Tunnel', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:4D', 'wwpn': '', 'wwnn': ''}
         ]}
     },
    {'type': 'ServerProfileV10', 'serverHardwareUri': None,
     'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'UserDefined', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'ServerProfile_Encl2_Bay8', 'description': 'Server Profile for server in Enclosure 2, Bay 8', 'affinity': 'Bay',
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'hideUnusedFlexNics':True,
     'serialNumber':'VCGFMGP00J',
     'uuid':'c263676c-745a-4b86-a029-8d8bdd58c178',
     'iscsiInitiatorName':'',
     'osDeploymentSettings':None,
     'connectionSettings':{
         'connections': [
             {'id': 1, 'name': 'conn_FC_A_1', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_A_1', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:4E', 'wwpn': '10:00:b2:0d:b0:c0:00:38', 'wwnn': '10:00:b2:0d:b0:c0:00:39'},
             {'id': 2, 'name': 'conn_FC_B_4', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:2', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_B_4', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:4F', 'wwpn': '10:00:b2:0d:b0:c0:00:3a', 'wwnn': '10:00:b2:0d:b0:c0:00:3b'},
             {'id': 3, 'name': 'conn_VlanTrunk7_A', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk7', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:50', 'wwpn': '', 'wwnn': ''},
             {'id': 4, 'name': 'conn_VlanTrunk7_B', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk7', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:51', 'wwpn': '', 'wwnn': ''},
             {'id': 5, 'name': 'conn_Eth_Untagged_A', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:Eth_Untagged', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:52', 'wwpn': '', 'wwnn': ''},
             {'id': 6, 'name': 'conn_Eth_Untagged_B', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '2500', 'networkUri': 'ETH:Eth_Untagged', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:53', 'wwpn': '', 'wwnn': ''}
         ]}
     },
    {'type': 'ServerProfileV10', 'serverHardwareUri': None,
     'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'UserDefined', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'ServerProfile_Encl2_Bay9', 'description': 'Server Profile for server in Enclosure 2, Bay 9', 'affinity': 'Bay',
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'hideUnusedFlexNics':True,
     'serialNumber':'VCGFMGP00K',
     'uuid':'bb475302-ed4f-4d14-a29d-a210eba79295',
     'iscsiInitiatorName':'',
     'osDeploymentSettings':None,
     'connectionSettings':{
         'connections': [
             {'id': 1, 'name': 'conn_FC_A_1', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_A_1', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:54', 'wwpn': '10:00:b2:0d:b0:c0:00:3c', 'wwnn': '10:00:b2:0d:b0:c0:00:3d'},
             {'id': 2, 'name': 'conn_FC_B_4', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:2', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_B_4', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:55', 'wwpn': '10:00:b2:0d:b0:c0:00:3e', 'wwnn': '10:00:b2:0d:b0:c0:00:3f'},
             {'id': 3, 'name': 'conn_VlanTrunk8_A', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk8', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:56', 'wwpn': '', 'wwnn': ''},
             {'id': 4, 'name': 'conn_VlanTrunk8_B', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk8', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:57', 'wwpn': '', 'wwnn': ''},
             {'id': 5, 'name': 'conn_Eth_Tunnel_A', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:Eth_Tunnel', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:58', 'wwpn': '', 'wwnn': ''},
             {'id': 6, 'name': 'conn_Eth_Tunnel_B', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '2500', 'networkUri': 'ETH:Eth_Tunnel', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:59', 'wwpn': '', 'wwnn': ''}
         ]}
     },
    {'type': 'ServerProfileV10', 'serverHardwareUri': None,
     'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'UserDefined', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'ServerProfile_Encl3_Bay3', 'description': 'Server Profile for server in Enclosure 3, Bay 3', 'affinity': 'Bay',
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'hideUnusedFlexNics':True,
     'serialNumber':'VCGFMGP00L',
     'uuid':'dbf4c85c-6817-4c3b-adb6-68c14d3dd0d9',
     'iscsiInitiatorName':'',
     'osDeploymentSettings':None,
     'connectionSettings':{
         'connections': [
             {'id': 1, 'name': 'conn_FC_A_1', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_A_1', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:5A', 'wwpn': '10:00:b2:0d:b0:c0:00:40', 'wwnn': '10:00:b2:0d:b0:c0:00:41'},
             {'id': 2, 'name': 'conn_FC_B_4', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:2', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_B_4', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:5B', 'wwpn': '10:00:b2:0d:b0:c0:00:42', 'wwnn': '10:00:b2:0d:b0:c0:00:43'},
             {'id': 3, 'name': 'conn_VlanTrunk3_A', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk3', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:5C', 'wwpn': '', 'wwnn': ''},
             {'id': 4, 'name': 'conn_VlanTrunk3_B', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk3', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:5D', 'wwpn': '', 'wwnn': ''},
             {'id': 5, 'name': 'conn_Eth_Untagged_A', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:Eth_Untagged', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:5E', 'wwpn': '', 'wwnn': ''},
             {'id': 6, 'name': 'conn_Eth_Untagged_B', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '2500', 'networkUri': 'ETH:Eth_Untagged', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:5F', 'wwpn': '', 'wwnn': ''}
         ]}
     },
    {'type': 'ServerProfileV10', 'serverHardwareUri': None,
     'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'UserDefined', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'ServerProfile_Encl3_Bay4', 'description': 'Server Profile for server in Enclosure 3, Bay 4', 'affinity': 'Bay',
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'hideUnusedFlexNics':True,
     'serialNumber':'VCGFMGP00M',
     'uuid':'30728299-49c9-4ef0-addf-09e96b052669',
     'iscsiInitiatorName':'',
     'osDeploymentSettings':None,
     'connectionSettings':{
         'connections': [
             {'id': 1, 'name': 'conn_FC_A_1', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_A_1', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:60', 'wwpn': '10:00:b2:0d:b0:c0:00:44', 'wwnn': '10:00:b2:0d:b0:c0:00:45'},
             {'id': 2, 'name': 'conn_FC_B_4', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:2', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_B_4', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:61', 'wwpn': '10:00:b2:0d:b0:c0:00:46', 'wwnn': '10:00:b2:0d:b0:c0:00:47'},
             {'id': 3, 'name': 'conn_VlanTrunk4_A', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk4', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:62', 'wwpn': '', 'wwnn': ''},
             {'id': 4, 'name': 'conn_VlanTrunk4_B', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk4', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:63', 'wwpn': '', 'wwnn': ''},
             {'id': 5, 'name': 'conn_Eth_Tunnel_A', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:Eth_Tunnel', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:64', 'wwpn': '', 'wwnn': ''},
             {'id': 6, 'name': 'conn_Eth_Tunnel_B', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '2500', 'networkUri': 'ETH:Eth_Tunnel', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:65', 'wwpn': '', 'wwnn': ''}
         ]}
     },
    {'type': 'ServerProfileV10', 'serverHardwareUri': None,
     'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'UserDefined', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'ServerProfile_Encl3_Bay6', 'description': 'Server Profile for server in Enclosure 3, Bay 6', 'affinity': 'Bay',
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'hideUnusedFlexNics':True,
     'serialNumber':'VCGFMGP00N',
     'uuid':'e1d752ee-a6a1-4b65-9241-f029f1daa833',
     'iscsiInitiatorName':'',
     'osDeploymentSettings':None,
     'connectionSettings':{
         'connections': [
             {'id': 1, 'name': 'conn_FC_A_1', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_A_1', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:66', 'wwpn': '10:00:b2:0d:b0:c0:00:48', 'wwnn': '10:00:b2:0d:b0:c0:00:49'},
             {'id': 2, 'name': 'conn_FC_B_4', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:2', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_B_4', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:67', 'wwpn': '10:00:b2:0d:b0:c0:00:4a', 'wwnn': '10:00:b2:0d:b0:c0:00:4b'},
             {'id': 3, 'name': 'conn_VlanTrunk5_A', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk5', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:68', 'wwpn': '', 'wwnn': ''},
             {'id': 4, 'name': 'conn_VlanTrunk5_B', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk5', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:69', 'wwpn': '', 'wwnn': ''},
             {'id': 5, 'name': 'conn_Eth_Untagged_A', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:Eth_Untagged', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:6A', 'wwpn': '', 'wwnn': ''},
             {'id': 6, 'name': 'conn_Eth_Untagged_B', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '2500', 'networkUri': 'ETH:Eth_Untagged', 'boot': {'priority': 'NotBootable'}, 'mac': '9A:DC:8C:60:00:6B', 'wwpn': '', 'wwnn': ''}
         ]}
     }
]

"""
Maps sever profile to encl, bay.  First column: server profile name. Second column: Enclosure, bay #
"""
# 4.10
server_profile_to_bay_map = {
    'ServerProfile_Encl1_Bay1': 'Encl1, bay 1',
    'ServerProfile_Encl1_Bay2': 'Encl1, bay 2',
    'ServerProfile_Encl1_Bay3': 'Encl1, bay 3',
    'ServerProfile_Encl1_Bay4': 'Encl1, bay 4',
    'ServerProfile_Encl1_Bay6': 'Encl1, bay 6',
    'ServerProfile_Encl1_Bay7': 'Encl1, bay 7',
    'ServerProfile_Encl1_Bay8': 'Encl1, bay 8',
    'ServerProfile_Encl1_Bay9': 'Encl1, bay 9',
    'ServerProfile_Encl2_Bay1': 'Encl2, bay 1',
    'ServerProfile_Encl2_Bay2': 'Encl2, bay 2',
    'ServerProfile_Encl2_Bay3': 'Encl2, bay 3',
    'ServerProfile_Encl2_Bay4': 'Encl2, bay 4',
    'ServerProfile_Encl2_Bay6': 'Encl2, bay 6',
    'ServerProfile_Encl2_Bay7': 'Encl2, bay 7',
    'ServerProfile_Encl2_Bay8': 'Encl2, bay 8',
    'ServerProfile_Encl2_Bay9': 'Encl2, bay 9',
    'ServerProfile_Encl3_Bay3': 'Encl3, bay 3',
    'ServerProfile_Encl3_Bay4': 'Encl3, bay 4',
    'ServerProfile_Encl3_Bay6': 'Encl3, bay 6'
}

"""
REQUEST BODY FOR OV SUPPORT DUMP
"""
SUPPORT_DUMP = {
    "errorCode": "CI",
    "encrypt": True
}
"""
REQUEST BODY FOR LE SUPPORT DUMP    165
"""
LE_SUPPORTDUMP_PAYLOAD = {"encrypt": True, "errorCode": "MyDump16", "excludeApplianceDump": False}

"""
    Data File for Nitro Ping & Traceroute feature
"""
admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

ssh_credentials = {'userName': 'root', 'password': 'hpvse1'}

ethernet_networks = [
    {"vlanIdRange": "21-25",
     "namePrefix": "Eth_network",
     "privateNetwork": False,
     "smartLink": True,
     "purpose": "General",
     "type": "bulk-ethernet-networkV1",
     "bandwidth": {"maximumBandwidth": 20000, "typicalBandwidth": 2500},
     }
]


li_name = {'name': 'LE-LIG1'}
IC2_nitro = 'SGH734VBEB, interconnect 2'
IC5_nitro = 'SGH734VBE6, interconnect 5'
ping_call = {"diagnosticUtilityType": "Ping", "address": ""}
trace_call = {"diagnosticUtilityType": "Traceroute", "address": ""}
Valid_Ipv4 = ['192.168.144.142', '192.168.144.171']
Valid_inactive_IPv4 = '192.168.145.201'
Invalid_ipv4 = '192.168.144.a'
Invalid_ipv4_format = 'a.b.144.'
Gateway = '192.168.144.1'
blank_ip = ''
gateway_ip = '192.168.144.1'
localhost_name = 'localhost'
localhost_ip = '127.0.0.1'
Valid_Ipv6 = ['fe80::9edc:71ff:fe9b:9674', 'fe80::9edc:71ff:fe9a:a05c']
Valid_inactive_IPv6 = 'fe80::9edc:71ff:fe9a:a05a'
Invalid_ipv6 = 'fe80::9edc:71ff:fe9a:H3R4'
Invalid_ipv6_format = 'fe80::9edc:71ff:fe9a.9'
Ipv6_192_168_144_142 = 'fe80::9eb6:54ff:fe98:e098'
Ipv4_192_168_144_142 = '192.166.144.142'
netmask = '255.255.255.0'
Invalid_ip_err_msg = 'CRM_INVALID_DESTINATION_ADDRESS_OR_HOSTNAME'
ongoing_opr_err_msg = 'CRM_ONGOING_SESSION_ON_INTERCONNECT_FOR_DIAGNOSTIC_UTILITY'
Invalid_destination_address_msg = 'CRM_INVALID_DESTINATION_ADDRESS_FOR_DIAGNOSTIC_UTILITY'
Netmask_Invalid = 'sendto: Network is unreachable'
Max_hops = '15 hops max'
Trace_15_hop = '15  *  *  *'
Trace_invalid = '!H'
Trace_precedence = '!C'
ms = 'ms'
Nitro_LI_ibs2 = {'name': 'LE-LIG-LACP'}

ENC1 = 'SGH734VBEB'
ENC2 = 'SGH734VBE6'
POTASH = 'Virtual Connect SE 40Gb F8 Module for Synergy'
NITRO = 'Virtual Connect SE 100Gb F32 Module for Synergy'
METHANE = 'Synergy 50Gb Interconnect Link Module'

LIG_Version = 'logical-interconnect-groupV7'
LIG_ethernet_version = 'EthernetInterconnectSettingsV6'
eth_network_Version = 'ethernet-networkV4'
fcoe_network_version = 'fcoe-networkV4'
fc_network_version = 'fc-networkV4'
UPLINK_TYPE = 'uplink-setV5'
SERVER_PROFILE = 'ServerProfileV10'

LE_NAME = "LE"
LIG_NAME = "LIG_Nitro"
LI_NAME = LE_NAME + '-' + LIG_NAME
US_NAME = 'US1'


uplink_sets = {'US1': {
    'name': 'US1', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged',
    'networkUris': ['Eth_network_21'],
    'mode': 'Auto',
    'loadBalancingMode': 'SourceAndDestinationIp',
    'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '2', 'port': 'Q1:1', 'speed': 'Speed10G'},
                               {'enclosure': '1', 'bay': '2', 'port': 'Q1:2', 'speed': 'Speed10G'},
                               {'enclosure': '2', 'bay': '5', 'port': 'Q2:1', 'speed': 'Speed10G'},
                               {'enclosure': '2', 'bay': '5', 'port': 'Q2:2', 'speed': 'Speed10G'}],
}
}

lig_nitro = {"name": "LIG_Nitro",
             "type": LIG_Version,
             "downlinkSpeedMode": "SPEED_10GB",
             "enclosureType": "SY12000",
             "ethernetSettings": {'type': LIG_ethernet_version, 'interconnectType': 'Ethernet', 'enableIgmpSnooping': False, 'igmpIdleTimeoutInterval': 260, 'enableFastMacCacheFailover': True, 'macRefreshInterval': 5,
                                  'enableNetworkLoopProtection': True, 'enablePauseFloodProtection': True},
             "description": None,
             "status": None,
             "state": None,
             "category": None,
             "created": None,
             "modified": None,
             "eTag": None,
             "uri": None,
             "uplinkSets": [],
             'interconnectMapTemplate': [{'bay': 2, 'enclosure': 1, 'type': NITRO, 'enclosureIndex': 1},
                                         {'bay': 5, 'enclosure': 1, 'type': METHANE, 'enclosureIndex': 1},
                                         {'bay': 2, 'enclosure': 2, 'type': METHANE, 'enclosureIndex': 2},
                                         {'bay': 5, 'enclosure': 2, 'type': NITRO, 'enclosureIndex': 2}],
             "internalNetworkUris": [],
             'interconnectBaySet': 2,
             'redundancyType': 'HighlyAvailable',
             'enclosureIndexes': [1, 2],
             "qosConfiguration": {"activeQosConfig": {"type": "QosConfiguration", "configType": "Passthrough", "downlinkClassificationType": None, "uplinkClassificationType": None, "qosTrafficClassifiers": None, "description": None, "status": None, "name": None, "state": None, "category": "qos-aggregated-configuration", "created": None, "modified": None, "eTag": None, "uri": None}, "inactiveFCoEQosConfig": None, "inactiveNonFCoEQosConfig": None, "type": "qos-aggregated-configuration", "name": None, "state": None, "status": None, "eTag": None, "modified": None, "created": None, "category": "qos-aggregated-configuration", "uri": None}
             }

Logical_Enclosure_HA = [{"name": "LE",
                         "enclosureUris": ['ENC:SGH734VBEB', 'ENC:SGH734VBE6'],
                         "enclosureGroupUri": "EG:EG_HA",
                         "firmwareBaselineUri": None,
                         "forceInstallFirmware": False}]

enc_group_nitro = [{"name": "EG_HA",
                    "interconnectBayMappings": [{'interconnectBay': 1, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': None},
                                                {'interconnectBay': 2, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': "LIG:LIG_Nitro"},
                                                {'interconnectBay': 3, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': None},
                                                {'interconnectBay': 4, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': None},
                                                {'interconnectBay': 5, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': "LIG:LIG_Nitro"},
                                                {'interconnectBay': 6, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': None},
                                                {'interconnectBay': 2, 'enclosureIndex': 2, 'logicalInterconnectGroupUri': "LIG:LIG_Nitro"},
                                                {'interconnectBay': 5, 'enclosureIndex': 2, 'logicalInterconnectGroupUri': "LIG:LIG_Nitro"}
                                                ],
                    "configurationScript": "",
                    "powerMode": "RedundantPowerFeed",
                    "ipAddressingMode": "DHCP",
                    "ipRangeUris": [],
                    "enclosureCount": 2}]

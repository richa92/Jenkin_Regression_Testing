import os
import sys

sys.path.append(os.path.dirname(__file__))
FUSION_USERNAME = 'Administrator'
FUSION_PASSWORD = 'hpvse123'
FUSION_SSH_USERNAME = 'root'
FUSION_SSH_PASSWORD = 'hpvse1'

FUSION_PROMPT = '#'  # Fusion Appliance Prompt
FUSION_TIMEOUT = 180  # Timeout.  Move this out???
FUSION_NIC = 'bond0'  # Fusion Appliance Primary NIC
FUSION_NIC_SUFFIX = '%' + FUSION_NIC

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

appliance = {'type': 'ApplianceNetworkConfiguration',
             'applianceNetworks':
                 [{'device': 'eth0',
                   'macAddress': None,
                   'interfaceName': 'hpcorp',
                   'activeNode': '1',
                   'unconfigure': False,
                   'ipv4Type': 'STATIC',
                   'ipv4Subnet': '255.255.248.0',
                   'ipv4Gateway': '15.245.128.1',
                   'ipv4NameServers': ['16.110.135.52'],
                   'virtIpv4Addr': '15.245.131.152',
                   'app1Ipv4Addr': '15.245.131.153',
                   'app2Ipv4Addr': '15.245.131.154',
                   'ipv6Type': 'UNCONFIGURE',
                   'hostname': 'feature.usa.hpe.com',
                   'confOneNode': True,
                   'domainName': 'usa.hpe.com',
                   'aliasDisabled': True,
                   }],
             }

ENC1 = 'CN754406W6'

ethernet_networks = [{'name': 'wpstDefaultnetwork',
                      'type': 'ethernet-networkV4',
                      'vlanId': '100',
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'ethernetNetworkType': 'Tagged'},
                     {'name': 'wpstnetwork1',
                      'type': 'ethernet-networkV4',
                      'vlanId': '101',
                      'purpose': 'Management',
                      'smartLink': True,
                      'privateNetwork': False,
                      'ethernetNetworkType': 'Tagged'},
                     {'name': 'wpstnetwork2',
                      'type': 'ethernet-networkV4',
                      'vlanId': '102',
                      'purpose': 'Management',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'},
                     {'name': 'wpstnetwork3',
                      'type': 'ethernet-networkV4',
                      'vlanId': '103',
                      'purpose': 'Management',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'},
                     {'name': 'wpstnetwork4',
                      'type': 'ethernet-networkV4',
                      'vlanId': '104',
                      'purpose': 'Management',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'},
                     {'name': 'wpstnetwork5',
                      'type': 'ethernet-networkV4',
                      'vlanId': '105',
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'},
                     {'name': 'wpstnetwork6',
                      'type': 'ethernet-networkV4',
                      'vlanId': '106',
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'},
                     {'name': 'wpstnetwork7',
                      'type': 'ethernet-networkV4',
                      'vlanId': '107',
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'},
                     {'name': 'wpstnetwork8',
                      'type': 'ethernet-networkV4',
                      'vlanId': '108',
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'},
                     {'name': 'wpstnetwork9',
                      'type': 'ethernet-networkV4',
                      'vlanId': '109',
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'},
                     {'name': 'wpstnetwork10',
                      'type': 'ethernet-networkV4',
                      'vlanId': '110',
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'}
                     ]

Enc1InterconnectMap1 = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
    ]

Enc1InterconnectMap2 = \
    [{'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
     {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
     ]

uplink_sets = {
    'uplink_set_1':
        {'name': 'uplink_set',
         'ethernetNetworkType': 'Tagged',
         'networkType': 'Ethernet',
         'networkUris': ['wpstnetwork1', 'wpstnetwork2', 'wpstnetwork3'],
         'lacpTimer': 'Short',
         'mode': 'Auto',
         'nativeNetworkUri': None,
         'logicalPortConfigInfos': [
             {'enclosure': '1', 'bay': '3', 'port': 'Q3', 'speed': 'Auto'},
         ]
         },
    'uplink_set_2':
        {'name': 'uplink_set',
         'ethernetNetworkType': 'Tagged',
         'networkType': 'Ethernet',
         'networkUris': ['wpstnetwork1', 'wpstnetwork2', 'wpstnetwork3'],
         'lacpTimer': 'Short',
         'mode': 'Auto',
         'nativeNetworkUri': None,
         'logicalPortConfigInfos': [
             {'enclosure': '1', 'bay': '3', 'port': 'Q3', 'speed': 'Auto'},
             {'enclosure': '1', 'bay': '3', 'port': 'Q4', 'speed': 'Auto'},
         ]
         },
    'uplink_set_3':
        {'name': 'uplink_set',
         'ethernetNetworkType': 'Tagged',
         'networkType': 'Ethernet',
         'networkUris': ['wpstnetwork1', 'wpstnetwork2', 'wpstnetwork4'],
         'lacpTimer': 'Short',
         'mode': 'Auto',
         'nativeNetworkUri': None,
         'logicalPortConfigInfos': [
             {'enclosure': '1', 'bay': '1', 'port': 'Q3', 'speed': 'Auto'},
         ]
         },
    'uplink_set_5':
        {'name': 'uplink_set',
         'ethernetNetworkType': 'Tagged',
         'networkType': 'Ethernet',
         'networkUris': ['wpstnetwork1', 'wpstnetwork2', 'wpstnetwork6'],
         'lacpTimer': 'Short',
         'mode': 'Auto',
         'nativeNetworkUri': None,
         'logicalPortConfigInfos': [
             {'enclosure': '1', 'bay': '3', 'port': 'Q3', 'speed': 'Auto'},
         ]
         }
}

ligs = {
    'Enc-LIG':
        {'name': 'Enc-LIG',
         'type': 'logical-interconnect-groupV4',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': Enc1InterconnectMap1,
         'enclosureIndexes': [1],
         'interconnectBaySet': 3,
         'redundancyType': 'NonRedundantASide',
         'fcoeSettings': {'fcoeMode': 'FcfNpv'},
         'uplinkSets': [uplink_sets['uplink_set_1'].copy()],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None
         },
    'Enc-LIG2':
        {'name': 'Enc-LIG',
         'type': 'logical-interconnect-groupV4',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': Enc1InterconnectMap1,
         'enclosureIndexes': [1],
         'interconnectBaySet': 3,
         'redundancyType': 'NonRedundantASide',
         'fcoeSettings': {'fcoeMode': 'FcfNpv'},
         'uplinkSets': [uplink_sets['uplink_set_2'].copy()],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None
         }
}

enc_group = {
    'Enc-EG':
        {'name': 'Enc-EG',
         'enclosureCount': 1,
         'interconnectBayMappings':
             [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Enc-LIG'},
              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': None}],
         'ipAddressingMode': 'External',
         'ipRangeUris': [],
         'ambientTemperatureMode': 'Standard',
         'powerMode': 'RedundantPowerFeed'
         },
}

updated_internal_network_list = []

LI_uplink_sets = {
    'uplinkset_2':
        {'name': 'uplink_set',
         'ethernetNetworkType': 'Tagged',
         'networkType': 'Ethernet',
         'networkUris': ['wpstnetwork2', 'wpstnetwork3', 'wpstnetwork4'],
         'fcNetworkUris': [],
         'fcoeNetworkUris': [],
         'nativeNetworkUri': None,
         'manualLoginRedistributionState': 'NotSupported',
         'lacpTimer': 'Short',
         'connectionMode': 'Auto',
         'portConfigInfos': [
             {'enclosure': ENC1, 'bay': '3', 'port': 'Q3', 'desiredSpeed': 'Auto'}
         ]
         },
    'uplinkset_3':
        {'name': 'uplink_set',
         'ethernetNetworkType': 'Tagged',
         'networkType': 'Ethernet',
         'networkUris': ['wpstnetwork1', 'wpstnetwork2', 'wpstnetwork4'],
         'fcNetworkUris': [],
         'fcoeNetworkUris': [],
         'nativeNetworkUri': None,
         'manualLoginRedistributionState': 'NotSupported',
         'lacpTimer': 'Short',
         'connectionMode': 'Auto',
         'portConfigInfos': [
             {'enclosure': ENC1, 'bay': '3', 'port': 'Q3', 'desiredSpeed': 'Auto'}
         ]
         },
    'uplinkset_4':
        {'name': 'uplink_set',
         'ethernetNetworkType': 'Tagged',
         'networkType': 'Ethernet',
         'networkUris': ['wpstnetwork1', 'wpstnetwork2', 'wpstnetwork4'],
         'fcNetworkUris': [],
         'fcoeNetworkUris': [],
         'nativeNetworkUri': None,
         'manualLoginRedistributionState': 'NotSupported',
         'lacpTimer': 'Short',
         'connectionMode': 'Auto',
         'portConfigInfos': [
             {'enclosure': ENC1, 'bay': '3', 'port': 'Q3', 'desiredSpeed': 'Auto'}
         ]
         },
    'uplinkset_5':
        {'name': 'uplink_set',
         'ethernetNetworkType': 'Tagged',
         'networkType': 'Ethernet',
         'networkUris': ['wpstnetwork1', 'wpstnetwork2', 'wpstnetwork6'],
         'fcNetworkUris': [],
         'fcoeNetworkUris': [],
         'nativeNetworkUri': None,
         'manualLoginRedistributionState': 'NotSupported',
         'lacpTimer': 'Short',
         'connectionMode': 'Auto',
         'portConfigInfos': [
             {'enclosure': ENC1, 'bay': '3', 'port': 'Q3', 'desiredSpeed': 'Auto'}
         ]
         }
}

les = {
    'Enc-LE':
        {'name': 'Enc-LE',
         'enclosureUris': ['ENC:CN754406W6'],
         'enclosureGroupUri': 'Enc:Enc-EG',
         'firmwareBaselineUri': None,
         'forceInstallFirmware': False
         },
}
les_updates = [{'enclosureUris': ['CN754406W6']}]

profiles = [{'type': 'ServerProfileV8',
             'serverHardwareUri': 'CN754406W6, bay 6',
             'serverHardwareTypeUri': None,
             'enclosureUri': 'CN754406W6',
             'enclosureGroupUri': 'Enc-EG',
             "iscsiInitiatorNameType": "AutoGenerated",
             'serialNumberType': 'Virtual',
             'macType': 'Virtual',
             'wwnType': 'Virtual',
             'name': 'profile1',
             "iscsiInitiatorName": "",
             'description': 'Profile',
             'affinity': 'Bay',
             'connections': [{'id': 1,
                              'name': 'conn1',
                              'functionType': 'Ethernet',
                              'portId': 'Auto',
                              'requestedMbps': '2500',
                              'networkUri': 'wpstnetwork1',
                              },
                             ]
             },
            {'type': 'ServerProfileV8',
             'serverHardwareUri': 'CN754406W6, bay 7',
             'serverHardwareTypeUri': None,
             'enclosureUri': 'CN754406W6',
             'enclosureGroupUri': 'Enc-EG',
             "iscsiInitiatorNameType": "AutoGenerated",
             'serialNumberType': 'Virtual',
             'macType': 'Virtual',
             'wwnType': 'Virtual',
             'name': 'profile2',
             "iscsiInitiatorName": "",
             'description': 'Profile',
             'affinity': 'Bay',
             'connections': [{'id': 1,
                              'name': 'conn1',
                              'functionType': 'Ethernet',
                              'portId': 'Auto',
                              'requestedMbps': '2500',
                              'networkUri': 'wpstnetwork1',
                              },
                             ]
             },
            ]

SLC_Enc_map_Good = \
    [{'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
     {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
     ]

SLC_Enc_map_Bad = \
    [{'bay': 1, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
     ]

SLC_Enc_map_Carbon = \
    [{'bay': 1, 'enclosure': 1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1},
     ]
# LIGs
# LIG1 - LIG matching with the h/w; bay 3 - Potash; bay 6 - CL20
# LIG2 - LIG NOT matching with the h/w; bay 3 - Potash; bay 6 - Potash

#
# Switch Life Cycle
# 1. Begin in Monitored state; Use LIG1 to create LE; Monitored --> Configured; done
# 2. Delete LE; Configured --> Monitored; done
# 3. Begin in Monitored state; Use LIG2 to create LE; Monitored --> Unmanaged; done
# 4. Edit LIG using LIG1; Unmanaged --> Configured
# 5. Edit LIG using LIG2; Configured --> Unmanaged
# 6. Edit LIG using LIG2; Unmanaged --> Monitored; done
# 7. Delete LE; Create LE using LIG1;efuse CL20 off; Monitored --> Configured --> Absent; efuse CL20 on; done
# 8. Delete LE; Create LE using LIG2; Unmamaged; efuse CL20 off; Unmanaged --> Absent; done
# 9. Edit LIG with LIG1; efuse CL20 on; Absent --> Configured; done
# 10. Delete LE; efuse CL20 off; Create LIG with LIG2; Absent; efuse on; Absent --> Unmanaged; done

slc_ligs = {
    'LIG1':
        {'name': 'LIG',
         'type': 'logical-interconnect-groupV4',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': SLC_Enc_map_Good,
         'enclosureIndexes': [1],
         'interconnectBaySet': 3,
         'redundancyType': 'Redundant',
         'fcoeSettings': {'fcoeMode': 'FcfNpv'},
         'uplinkSets': [uplink_sets['uplink_set_1'].copy()],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None
         },
    'LIG2':
        {'name': 'LIG',
         'type': 'logical-interconnect-groupV4',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': SLC_Enc_map_Good,
         'enclosureIndexes': [1],
         'interconnectBaySet': 3,
         'redundancyType': 'Redundant',
         'fcoeSettings': {'fcoeMode': 'FcfNpv'},
         'uplinkSets': [],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None
         },
    'LIG3':
        {'name': 'LIG',
         'type': 'logical-interconnect-groupV4',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': SLC_Enc_map_Good,
         'enclosureIndexes': [1],
         'interconnectBaySet': 3,
         'redundancyType': 'Redundant',
         'fcoeSettings': {'fcoeMode': 'FcfNpv'},
         'uplinkSets': [uplink_sets['uplink_set_5'].copy()],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None
         }
}

slc_egs = {
    'EG1':
        {'name': 'EG',
         'enclosureCount': 1,
         'interconnectBayMappings':
             [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG'},
              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG'}],
         'ipAddressingMode': "External",
         'ipRangeUris': [],
         'ambientTemperatureMode': 'Standard',
         'powerMode': "RedundantPowerFeed"
         },
    'EG2':
        {'name': 'EG',
         'enclosureCount': 1,
         'interconnectBayMappings':
             [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG'},
              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG'}],
         'ipAddressingMode': "External",
         'ipRangeUris': [],
         'ambientTemperatureMode': 'Standard',
         'powerMode': "RedundantPowerFeed"
         },
    'EG3':
        {'name': 'EG',
         'enclosureCount': 1,
         'interconnectBayMappings':
             [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG'},
              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG'}],
         'ipAddressingMode': "External",
         'ipRangeUris': [],
         'ambientTemperatureMode': 'Standard',
         'powerMode': "RedundantPowerFeed"
         },
}

slc_les = {
    'LE1':
        {'name': 'LE',
         'enclosureUris': ['ENC:CN754406W6'],
         'enclosureGroupUri': 'Enc:EG',
         'firmwareBaselineUri': None,
         'forceInstallFirmware': False
         },
    'LE2':
        {'name': 'LE',
         'enclosureUris': ['ENC:CN754406W6'],
         'enclosureGroupUri': 'Enc:EG',
         'firmwareBaselineUri': None,
         'forceInstallFirmware': False
         },
    'LE3':
        {'name': 'LE',
         'enclosureUris': ['ENC:CN754406W6'],
         'enclosureGroupUri': 'Enc:EG',
         'firmwareBaselineUri': None,
         'forceInstallFirmware': False
         }
}

import os
import sys


def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist


APPLIANCE_IP = '15.186.14.17'
Enclosure_Ip = '15.186.2.227'
ENC1 = 'aus-c7000-188'
ENCLOSURE_NAME = 'aus-c7000-188'
admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}
# Enclosure details
enclosure_credentials = {'userName': 'Administrator', 'Password': 'Compaq123'}
Uplinkset_List1 = ['ss-comp-add', 'ss-comp-ug1', 'ss-comp-ug2']
Uplinkset_name = ['ss-comp-ug2', 'ss-comp-ug1', 'ss-comp-add']
Uplinkset_List = ['ss-comp-ug1', 'ss-comp-ug2']
Uplinkset_List2 = ['ss-comp-ug1', 'ss-comp-ug2']
up_List = ['ss-comp-ug2']
bay_no = 5
LI_name = ['aus-c7000-188-LIG-COMP-SS']
users = [{'userName': 'Networkadmin', 'password': 'Networkadmin', 'fullName': 'Networkadmin', 'emailAddress': 'nat@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions', 'enabled': True, 'permissions': [{'roleName': 'Network administrator', 'scopeUri': None}]},
         {'userName': 'Serveradmin', 'password': 'Serveradmin', 'fullName': 'Serveradmin', 'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions', 'enabled': True, 'permissions': [{'roleName': 'Server administrator', 'scopeUri': None}]}]

Serveradmin_credentials = {'userName': 'Serveradmin', 'password': 'Serveradmin'}
Networkadmin_credentials = {'userName': 'Networkadmin', 'password': 'Networkadmin'}

IC_Configured = 'Configured'
Consistency_Alert_Status = 'CLEARED'
LIG = 'SHAW_Lig'
enet_body = [{
    'type': 'ethernet-networkV4',
    'ethernetNetworkType': 'Tagged',
    'name': 'wpstnetwork9',
    'privateNetwork': False,
    'purpose': 'General',
    'smartLink': True,
    'connectionTemplateUri': None,
    'vlanId': 10
},
    {
    'type': 'ethernet-networkV4',
    'ethernetNetworkType': 'Tagged',
    'name': 'wpstnetwork3',
    'privateNetwork': False,
    'purpose': 'General',
    'smartLink': True,
    'connectionTemplateUri': None,
    'vlanId': 10
},
    {
    'type': 'ethernet-networkV4',
    'ethernetNetworkType': 'Tagged',
    'name': 'wpstnetwork1',
    'privateNetwork': False,
    'purpose': 'General',
    'smartLink': True,
    'connectionTemplateUri': None,
    'vlanId': 20
},
    {
    'type': 'ethernet-networkV4',
    'ethernetNetworkType': 'Tagged',
    'name': 'wpstnetwork8',
    'privateNetwork': False,
    'purpose': 'General',
    'smartLink': True,
    'connectionTemplateUri': None,
    'vlanId': 20
},
    {
    'type': 'ethernet-networkV4',
    'ethernetNetworkType': 'Tagged',
    'name': 'wpstnetwork7',
    'privateNetwork': False,
    'purpose': 'General',
    'smartLink': True,
    'connectionTemplateUri': None,
    'vlanId': 30
},
    {
    'type': 'ethernet-networkV4',
    'ethernetNetworkType': 'Tagged',
    'name': 'wpstnetwork2',
    'privateNetwork': False,
    'purpose': 'General',
    'smartLink': True,
    'connectionTemplateUri': None,
    'vlanId': 30
}]

Fc_body = [{'type': 'fc-networkV4',
            'name': 'DATAAUTOMATED',
            'fabricType': 'FabricAttach',
            'linkStabilityTime': 30,
            'autoLoginRedistribution': True
            },
           {'type': 'fc-networkV4',
            'name': 'DATAAUTOMATED1',
            'fabricType': 'FabricAttach',
            'linkStabilityTime': 30,
            'autoLoginRedistribution': True
            },
           {'type': 'fc-networkV4',
            'name': 'DATAAUTOMATED2',
            'fabricType': 'FabricAttach',
            'linkStabilityTime': 30,
            'autoLoginRedistribution': True
            },
           {'type': 'fc-networkV4',
            'name': 'DATAAUTOMATED3',
            'fabricType': 'FabricAttach',
            'linkStabilityTime': 30,
            'autoLoginRedistribution': True
            },
           {'type': 'fc-networkV4',
            'name': 'DATAAUTOMATED4',
            'fabricType': 'FabricAttach',
            'linkStabilityTime': 30,
            'autoLoginRedistribution': True
            },
           {'type': 'fc-networkV4',
            'name': 'DATAAUTOMATED5',
            'fabricType': 'FabricAttach',
            'linkStabilityTime': 30,
            'autoLoginRedistribution': True
            },
           {'type': 'fc-networkV4',
            'name': 'DATAAUTOMATED6',
            'fabricType': 'FabricAttach',
            'linkStabilityTime': 30,
            'autoLoginRedistribution': True
            }]


ligs = [{'name': 'LIG-COMP-SS',
         'type': 'logical-interconnect-groupV6',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC Flex-10/10D Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC Flex-10/10D Module'}],
         'uplinkSets': [{'name': 'ss-comp-ug1',
                         'lacpTimer': 'Short',
                         'ethernetNetworkType': 'Tagged',
                         'networkType': 'Ethernet',
                         'networkUris': ['wpstnetwork1', 'wpstnetwork3'],
                         'nativeNetworkUri': None,
                         'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '1', 'port': 'X2', 'speed': 'Auto'},
                                                    {'bay': '2', 'enclosure': '1', 'port': 'X3', 'speed': 'Auto'}]},
                        {'name': 'ss-comp-ug2',
                         'lacpTimer': 'Short',
                         'ethernetNetworkType': 'Tagged',
                         'networkType': 'Ethernet',
                         'networkUris': ['wpstnetwork2'],
                         'nativeNetworkUri': None,
                         'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': 'X1', 'speed': 'Auto'},
                                                    {'bay': '4', 'enclosure': '1', 'port': 'X1', 'speed': 'Auto'}]}],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None
         }]
Edit_Lig = [{'name': 'LIG-COMP-SS',
             'type': 'logical-interconnect-groupV6',
             'enclosureType': 'C7000',
             'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                         {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                         {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC Flex-10 Enet Module'},
                                         {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC Flex-10 Enet Module'}],
             'uplinkSets': [],
             'stackingMode': 'Enclosure',
             'ethernetSettings':{"Fast MAC cache failover": "true", "MAC refresh interval": "20", "IGMP snooping": "true", "IGMP idle timeout interval": "300", "Loop protection": "false"},
             'state': 'Active',
             'telemetryConfiguration': {"type": "telemetry-configuration", "sampleCount": 15, "sampleInterval": 260, "enableTelemetry": 'true'},
             'snmpConfiguration': {'type': 'snmp-configuration', 'readCommunity': 'public', 'systemContact': '', "SNMPv1, v2": 'false'}
             }]
Edit_Ligtype = [{'name': 'LIG-COMP-SS',
                 'type': 'logical-interconnect-groupV6',
                 'enclosureType': 'C7000',
                 'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC Flex-10 Enet Module'},
                                             {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC Flex-10 Enet Module'}],
                 'uplinkSets': [],
                 'stackingMode': 'Enclosure',
                 'ethernetSettings':{"Fast MAC cache failover": "true", "MAC refresh interval": "20", "IGMP snooping": "true", "IGMP idle timeout interval": "300", "Loop protection": "false"},
                 'state': 'Active',
                 'telemetryConfiguration': {"type": "telemetry-configuration", "sampleCount": 15, "sampleInterval": 260, "enableTelemetry": 'true'},
                 'snmpConfiguration': {'type': 'snmp-configuration', 'readCommunity': 'public', 'systemContact': '', "SNMPv1, v2": 'false'}
                 }]
Add_Ligtype = [{'name': 'LIG-COMP-SS',
                'type': 'logical-interconnect-groupV6',
                'enclosureType': 'C7000',
                'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                                            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                                            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC Flex-10/10D Module'},
                                            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC Flex-10/10D Module'}],
                'uplinkSets': [],
                'stackingMode': 'Enclosure',
                'ethernetSettings':{"Fast MAC cache failover": "true", "MAC refresh interval": "20", "IGMP snooping": "true", "IGMP idle timeout interval": "300", "Loop protection": "false"},
                'state': 'Active',
                'telemetryConfiguration': {"type": "telemetry-configuration", "sampleCount": 15, "sampleInterval": 260, "enableTelemetry": 'true'},
                'snmpConfiguration': {'type': 'snmp-configuration', 'readCommunity': 'public', 'systemContact': '', "SNMPv1, v2": 'false'}
                }]
uplinkSets_Add = [{'name': 'ss-comp-ug1',
                   'lacpTimer': 'Short',
                   'ethernetNetworkType': 'Tagged',
                   'networkType': 'Ethernet',
                   'networkUris': ['wpstnetwork1'],
                   'nativeNetworkUri': None,
                   'mode': 'Auto',
                   'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '1', 'port': 'X2', 'speed': 'Auto'},
                                              {'bay': '2', 'enclosure': '1', 'port': 'X3', 'speed': 'Auto'}]},

                  {'name': 'ss-comp-ug',
                   'lacpTimer': 'Short',
                   'ethernetNetworkType': 'Tagged',
                   'networkType': 'Ethernet',
                   'networkUris': ['wpstnetwork2'],
                   'nativeNetworkUri': None,
                   'mode': 'Auto',
                   'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '1', 'port': 'X3', 'speed': 'Auto'},
                                              {'bay': '2', 'enclosure': '1', 'port': 'X5', 'speed': 'Auto'}]
                   },
                  {'name': 'ss-comp-add',
                   'lacpTimer': 'Short',
                           'ethernetNetworkType': 'Tagged',
                           'networkType': 'Ethernet',
                           'networkUris': ['wpstnetwork9'],
                           'nativeNetworkUri': None,
                           'mode': 'Auto',
                           'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '1', 'port': 'X4', 'speed': 'Auto'},
                                                      {'bay': '2', 'enclosure': '1', 'port': 'X7', 'speed': 'Auto'}]
                   }]
Edit_uplinkset = [{'name': 'ss-comp-ug1',
                   'lacpTimer': 'Short',
                   'ethernetNetworkType': 'Tagged',
                   'networkType': 'Ethernet',
                   'networkUris': ['wpstnetwork1', 'wpstnetwork7'],
                   'nativeNetworkUri': None,
                   'mode': 'Auto',
                   'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '1', 'port': 'X2', 'speed': 'Auto'},
                                              {'bay': '2', 'enclosure': '1', 'port': 'X3', 'speed': 'Auto'}]},

                  {'name': 'ss-comp-ug2',
                   'lacpTimer': 'Short',
                   'ethernetNetworkType': 'Tagged',
                   'networkType': 'Ethernet',
                   'networkUris': ['wpstnetwork2', 'wpstnetwork8'],
                   'nativeNetworkUri': None,
                   'mode': 'Auto',
                   'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': 'X1', 'speed': 'Auto'},
                                              {'bay': '4', 'enclosure': '1', 'port': 'X1', 'speed': 'Auto'}]
                   }]
uplinkSets_Edit = [{'name': 'ss-comp-ug2',
                    'lacpTimer': 'Short',
                    'ethernetNetworkType': 'Tagged',
                    'networkType': 'Ethernet',
                    'networkUris': ['wpstnetwork2'],
                    'nativeNetworkUri': None,
                    'mode': 'Auto',
                    'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '1', 'port': 'X2', 'speed': 'Auto'},
                                               {'bay': '2', 'enclosure': '1', 'port': 'X3', 'speed': 'Auto'}]
                    }]
ethernetSettings_edit = {"Fast MAC cache failover": "false", "MAC refresh interval": "10", "IGMP snooping": "true", "IGMP idle timeout interval": "300", "Loop protection": "false"}

telemetryConfiguration_edit = {"type": "telemetry-configuration", "sampleCount": 15, "sampleInterval": 260, "enableTelemetry": 'true'}
snmpConfiguration_edit = {'type': 'snmp-configuration', 'readCommunity': 'public', 'systemContact': '', "SNMPv1, v2": 'false'}

eg_body1 = [{'name': 'config1-group',
             'interconnectBayMappings': [
                 {'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:LIG-COMP-SS'},
                 {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:LIG-COMP-SS'},
                 {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG-COMP-SS'},
                 {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:LIG-COMP-SS'},
                 {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                 {'interconnectBay': 6, 'logicalInterconnectGroupUri': None},
                 {'interconnectBay': 7, 'logicalInterconnectGroupUri': None},
                 {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}],
             'ipRangeUris': [],
             'enclosureCount':1,
             'osDeploymentSettings': None,
             'configurationScript': None,
             'powerMode': None,
             'ambientTemperatureMode':'Standard'}]

encs = [{'hostname': '15.186.2.227', 'username': 'Administrator', 'password': 'Compaq123', 'enclosureGroupUri': 'EG:config1-group', 'force': False, 'licensingIntent': 'OneViewNoiLO'}]


server_profile1 = [{'type': 'ServerProfileV10', 'serverHardwareUri': ENC1 + ', bay 5',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:config1-group', 'serialNumberType': 'Virtual', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'Profile1', 'description': '', 'affinity': 'Bay',
                    'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '1000', 'networkUri': 'ETH:wpstnetwork1',
                                                            'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                           {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2000', 'networkUri': 'ETH:wpstnetwork3',
                                                            'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                           ]},

                    'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']}, 'bios':{'manageBios': False, 'overriddenSettings': []}, 'sanStorage': None}]

interconnects_inventory = ['aus-c7000-188, interconnect 3', 'aus-c7000-188, interconnect 4']
interconnects_unmanaged = ['aus-c7000-188, interconnect 1', 'aus-c7000-188, interconnect 2']

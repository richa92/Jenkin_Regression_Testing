import os
import sys


def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist

APPLIANCE_IP = '15.186.30.57'
Enclosure_Ip = '15.186.17.26'
ENC1 = 'USE0515652'
ENCLOSURE_NAME = 'USE0515652'
admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}
# Enclosure details
enclosure_credentials = {'userName': 'Administrator', 'Password': 'hpvse123'}
Uplinkset_List1 = ['fc-comp-ug1', 'fc-comp-ug2', 'fc-comp-add']
Uplinkset_name = ['fc-comp-add', 'fc-comp-ug1', 'fc-comp-ug2']
Uplinkset_List = ['fc-comp-ug1', 'fc-comp-ug2']
up_List = ['ss-comp-ug2']
bay_no = 2
LI_name = ['USE0515652-LIG-COMP-OU']
users = [{'userName': 'Networkadmin', 'password': 'Networkadmin', 'fullName': 'Networkadmin', 'emailAddress': 'nat@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions', 'enabled': True, 'permissions': [{'roleName': 'Network administrator', 'scopeUri': None}]},
         {'userName': 'Serveradmin', 'password': 'Serveradmin', 'fullName': 'Serveradmin', 'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions', 'enabled': True, 'permissions': [{'roleName': 'Server administrator', 'scopeUri': None}]}]

Serveradmin_credentials = {'userName': 'Serveradmin', 'password': 'Serveradmin'}
Networkadmin_credentials = {'userName': 'Networkadmin', 'password': 'Networkadmin'}

interconnects_inventory = ['USE0515652, interconnect 5', 'USE0515652, interconnect 6', 'USE0515652, interconnect 7', 'USE0515652, interconnect 8']
interconnects_unmanaged = ['USE0515652, interconnect 1', 'USE0515652, interconnect 2', 'USE0515652, interconnect 3', 'USE0515652, interconnect 4']
IC_Configured = 'Configured'
Consistency_Alert_Status = 'CLEARED'
LIG = 'SHAW_Lig'
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

ligs = [{'name': 'LIG-COMP-OU',
         'type': 'logical-interconnect-groupV6',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC 8Gb 24-Port FC Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC 8Gb 24-Port FC Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC 8Gb 20-Port FC Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC 8Gb 20-Port FC Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 7, 'type': 'HP VC Flex-10 Enet Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 8, 'type': 'HP VC Flex-10 Enet Module'}],
         'uplinkSets': [{'name': 'fc-comp-ug1',
                         'lacpTimer': 'Short',
                         'ethernetNetworkType': None,
                         'networkType': 'FibreChannel',
                         'networkUris': ['DATAAUTOMATED'],
                         'nativeNetworkUri': None,
                         'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '5', 'enclosure': '1', 'port': '2', 'speed': 'Auto'}]},

                        {'name': 'fc-comp-ug2',
                         'lacpTimer': 'Short',
                         'ethernetNetworkType': None,
                         'networkType': 'FibreChannel',
                         'networkUris': ['DATAAUTOMATED2'],
                         'nativeNetworkUri': None,
                         'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '6', 'enclosure': '1', 'port': '1', 'speed': 'Auto'}]}],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None
         }]
Edit_Lig = [{'name': 'LIG-COMP-OU',
             'type': 'logical-interconnect-groupV6',
             'enclosureType': 'C7000',
             'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC Flex-10 Enet Module'},
                                         {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC Flex-10 Enet Module'},
                                         {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC Flex-10 Enet Module'},
                                         {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC Flex-10 Enet Module'},
                                         {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                         {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                         {'enclosure': 1, 'enclosureIndex': 1, 'bay': 7, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                         {'enclosure': 1, 'enclosureIndex': 1, 'bay': 8, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'}],
             'uplinkSets': [],
             'stackingMode': 'Enclosure',
             'ethernetSettings':{"Fast MAC cache failover": "true", "MAC refresh interval": "20", "IGMP snooping": "true", "IGMP idle timeout interval": "300", "Loop protection": "false"},
             'state': 'Active',
             'telemetryConfiguration': {"type": "telemetry-configuration", "sampleCount": 15, "sampleInterval": 260, "enableTelemetry": 'true'},
             'snmpConfiguration': {'type': 'snmp-configuration', 'readCommunity': 'public', 'systemContact': '', "SNMPv1, v2": 'false'}
             }]
Edit_Ligtype = [{'name': 'LIG-COMP-OU',
                 'type': 'logical-interconnect-groupV6',
                 'enclosureType': 'C7000',
                 'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC Flex-10 Enet Module'},
                                             {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC Flex-10 Enet Module'},
                                             {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC Flex-10 Enet Module'},
                                             {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC Flex-10 Enet Module'}],
                 'uplinkSets': [],
                 'stackingMode': 'Enclosure',
                 'ethernetSettings':{"Fast MAC cache failover": "true", "MAC refresh interval": "20", "IGMP snooping": "true", "IGMP idle timeout interval": "300", "Loop protection": "false"},
                 'state': 'Active',
                 'telemetryConfiguration': {"type": "telemetry-configuration", "sampleCount": 15, "sampleInterval": 260, "enableTelemetry": 'true'},
                 'snmpConfiguration': {'type': 'snmp-configuration', 'readCommunity': 'public', 'systemContact': '', "SNMPv1, v2": 'false'}
                 }]
Add_Ligtype = [{'name': 'LIG-COMP-OU',
                'type': 'logical-interconnect-groupV6',
                'enclosureType': 'C7000',
                'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC 8Gb 24-Port FC Module'},
                                            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC 8Gb 24-Port FC Module'},
                                            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC 8Gb 20-Port FC Module'},
                                            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC 8Gb 20-Port FC Module'},
                                            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 7, 'type': 'HP VC Flex-10 Enet Module'},
                                            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 8, 'type': 'HP VC Flex-10 Enet Module'}],
                'uplinkSets': [],
                'stackingMode': 'Enclosure',
                'ethernetSettings':{"Fast MAC cache failover": "true", "MAC refresh interval": "20", "IGMP snooping": "true", "IGMP idle timeout interval": "300", "Loop protection": "false"},
                'state': 'Active',
                'telemetryConfiguration': {"type": "telemetry-configuration", "sampleCount": 15, "sampleInterval": 260, "enableTelemetry": 'true'},
                'snmpConfiguration': {'type': 'snmp-configuration', 'readCommunity': 'public', 'systemContact': '', "SNMPv1, v2": 'false'}
                }]
uplinkSets_Add = [{'name': 'fc-comp-ug1',
                   'lacpTimer': 'Short',
                   'ethernetNetworkType': None,
                   'networkType': 'FibreChannel',
                   'networkUris': ['DATAAUTOMATED'],
                   'nativeNetworkUri': None,
                   'mode': 'Auto',
                   'logicalPortConfigInfos': [{'bay': '5', 'enclosure': '1', 'port': '2', 'speed': 'Auto'}]},

                  {'name': 'fc-comp-ug2',
                   'lacpTimer': 'Short',
                   'ethernetNetworkType': None,
                   'networkType': 'FibreChannel',
                   'networkUris': ['DATAAUTOMATED2'],
                   'nativeNetworkUri': None,
                   'mode': 'Auto',
                   'logicalPortConfigInfos': [{'bay': '6', 'enclosure': '1', 'port': '1', 'speed': 'Auto'}]},
                  {'name': 'fc-comp-add',
                   'lacpTimer': 'Short',
                           'ethernetNetworkType': 'Tagged',
                           'networkType': 'FibreChannel',
                           'networkUris': ['DATAAUTOMATED4'],
                           'nativeNetworkUri': None,
                           'mode': 'Auto',
                           'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '1', 'port': '1', 'speed': 'Auto'},
                                                      {'bay': '4', 'enclosure': '1', 'port': '2', 'speed': 'Auto'}]
                   }]

Edit_uplinkset = [{'name': 'fc-comp-ug1',
                   'lacpTimer': 'Short',
                   'ethernetNetworkType': None,
                   'networkType': 'FibreChannel',
                   'networkUris': ['DATAAUTOMATED2'],
                   'nativeNetworkUri': None,
                   'mode': 'Auto',
                   'logicalPortConfigInfos': [{'bay': '5', 'enclosure': '1', 'port': '1', 'speed': 'Auto'}]},

                  {'name': 'fc-comp-ug2',
                   'lacpTimer': 'Short',
                   'ethernetNetworkType': None,
                   'networkType': 'FibreChannel',
                   'networkUris': ['DATAAUTOMATED1'],
                   'nativeNetworkUri': None,
                   'mode': 'Auto',
                   'logicalPortConfigInfos': [{'bay': '6', 'enclosure': '1', 'port': '1', 'speed': 'Auto'}]}]
uplinkSets_Edit = [{'name': 'ss-comp-ug2',
                    'lacpTimer': 'Short',
                    'ethernetNetworkType': None,
                    'networkType': 'FibreChannel',
                    'networkUris': ['DATAAUTOMATED3'],
                    'nativeNetworkUri': None,
                    'mode': 'Auto',
                    'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': '1', 'speed': 'Auto'}]}]
ethernetSettings_edit = {"Fast MAC cache failover": "false", "MAC refresh interval": "10", "IGMP snooping": "true", "IGMP idle timeout interval": "300", "Loop protection": "false"}

telemetryConfiguration_edit = {"type": "telemetry-configuration", "sampleCount": 15, "sampleInterval": 260, "enableTelemetry": 'true'}
snmpConfiguration_edit = {'type': 'snmp-configuration', 'readCommunity': 'public', 'systemContact': '', "SNMPv1, v2": 'false'}

eg_body1 = [{'name': 'config1-group',
             'interconnectBayMappings': [
                 {'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:LIG-COMP-OU'},
                 {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:LIG-COMP-OU'},
                 {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG-COMP-OU'},
                 {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:LIG-COMP-OU'},
                 {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:LIG-COMP-OU'},
                 {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG-COMP-OU'},
                 {'interconnectBay': 7, 'logicalInterconnectGroupUri': 'LIG:LIG-COMP-OU'},
                 {'interconnectBay': 8, 'logicalInterconnectGroupUri': 'LIG:LIG-COMP-OU'}],
             'ipRangeUris': [],
             'enclosureCount':1,
             'osDeploymentSettings': None,
             'configurationScript': None,
             'powerMode': None,
             'ambientTemperatureMode':'Standard'}]

encs = [{'hostname': '15.186.17.26', 'username': 'Administrator', 'password': 'compaq', 'enclosureGroupUri': 'EG:config1-group', 'force': False, 'licensingIntent': 'OneViewNoiLO'}]


server_profile1 = [{'type': 'ServerProfileV10', 'serverHardwareUri': ENC1 + ', bay 2',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:config1-group', 'serialNumberType': 'Virtual', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'Profile1', 'description': '', 'affinity': 'Bay',
                    'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '4000', 'networkUri': 'FC:DATAAUTOMATED',
                                                            'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                           {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '4000', 'networkUri': 'FC:DATAAUTOMATED2',
                                                            'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                           ]},

                    'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']}, 'bios':{'manageBios': False, 'overriddenSettings': []}, 'sanStorage': None}]

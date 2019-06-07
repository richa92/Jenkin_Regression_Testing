import os
import sys

cwd = os.getcwd()
download_to_path = cwd


def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist
# Hint:
# Check for linked uplink ports in var up_ports_5 and up_ports_6
# Check for linked uplink ports in var dw_ports
# Uplinkset should be created to hill modules with corresponding linked port even when hardware setup has been changed in var uplink_sets
# Creating separate LIG for each modules so create separate uplinkset for each hill module with corresponding linked port in var uplink_sets_separateLIG
# Check the hill module bay set when hardware setup is changed in var ligs1
# Check whether the supported and unsupported transceiver connected to any port of hill module before running connector suite
# Supported transceiver can be find in OV by expanding the port deatis in interconnect page for corresponding uplink port you can able to see the connector and digital diagnostics info
# Check whether the given analyzer and monitored port is linked before configuring port mirroring
# Analyzer port is linked port from hill not the port given in the uplink set
# Monitored port is linked downlink port
# Check whether the given password for interconnect is correct even when tthe hardware setup is changed
# Check for LUN drives after giving FC connection to servers
# Eg:Hill in bay 3 and bay4, D drive for IC3 and E drive for IC4..So change accordingly in var diskspd_cmd
# Check for server details,linux and ilo credentials
SSH_PASS = 'hpvse1'

APPLIANCE_IP = "15.186.16.227"
ENCLOSURE_IP = "15.186.20.255"
interconnect_bay5 = "3"
interconnect_bay6 = "4"
OA_USER = "Administrator"
OA_PASS = "compaq"
FUSION_IP = APPLIANCE_IP
FUSION_SSH_USERNAME = "root"
FUSION_SSH_PASSWORD = "hpvse1"
FUSION_PROMPT = '#'               # Fusion Appliance Prompt
FUSION_TIMEOUT = 180
IC_SSH_USERNAME = "root"
IC_TIMEOUT = 100
IC_PROMPT = '>'
pm_timer = 3000

appliance_cred = ['root', 'hpvse1']
up_ports_5 = ['2', '3', '4']  # Linked uplink ports of that Hill module
up_ports_6 = ['1', '2', '3']  # Linked uplink ports of that Hill module
dw_ports = ['d6', 'd3']  # Linked downlink ports (Servers in configured state should be given here)
admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

serveradmin = {'userName': 'Serveradmin', 'password': 'Serveradmin'}

network_admin = {'userName': 'Networkadmin', 'password': 'Networkadmin'}

backup_admin = {'userName': 'Backupadmin', 'password': 'Backupadmin'}

readonly_user = {'userName': 'readonly', 'password': 'readonly'}

vcenter = {'server': '15.199.230.130', 'user': 'GopalK', 'password': 'hpvse1'}


#users = [{'type':'UserAndPermissions','userName':'Serveradmin','fullName':'Serveradmin','password': 'Serveradmin','emailAddress': '', 'officePhone': '', 'mobilePhone': '','enabled':True,'permissions':[{'roleName':'Serveradministrator','scopeUri':None}]}]

users = [{'type': 'UserAndPermissions', 'userName': 'Serveradmin', 'fullName': '', 'password': 'Serveradmin', 'emailAddress': '', 'officePhone': '', 'mobilePhone': '', 'enabled': True, 'permissions': [{'roleName': 'Server administrator', 'scopeUri': None}]}]


# Uplinkset should be created to hill modules with corresponding linked port even when hardware setup has been changed
uplink_sets = {'UplinkSet_1': {'name': 'UplinkSet_1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_1'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                               'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': '2', 'speed': 'Auto'}
                                                          ]},
               'UplinkSet_2': {'name': 'UplinkSet_2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_2'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                               'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '1', 'port': '3', 'speed': 'Auto'}]},
               'UplinkSet_3': {'name': 'UplinkSet_3', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_3'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                               'logicalPortConfigInfos': [{'bay': '5', 'enclosure': '1', 'port': '1', 'speed': 'Auto'}]},
               'UplinkSet_4': {'name': 'UplinkSet_4', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_4'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                               'logicalPortConfigInfos': [{'bay': '6', 'enclosure': '1', 'port': '1', 'speed': 'Auto'}]},
               'UplinkSet_5': {'name': 'us_eth', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Untagged', 'networkUris': ['enet_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                               'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '1', 'port': 'X5', 'speed': 'Auto'}]}}

uplink_sets_enc1 = {'UplinkSet_1': {'name': 'UplinkSet_1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_1'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                    'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': '2', 'speed': 'Auto'}
                                                               ]},
                    'UplinkSet_2': {'name': 'UplinkSet_2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_2'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                    'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '1', 'port': '3', 'speed': 'Auto'}]},
                    'UplinkSet_3': {'name': 'UplinkSet_3', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_3'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                    'logicalPortConfigInfos': [{'bay': '5', 'enclosure': '1', 'port': '1', 'speed': 'Auto'}
                                                               ]},
                    'UplinkSet_4': {'name': 'UplinkSet_4', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_4'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                    'logicalPortConfigInfos': [{'bay': '6', 'enclosure': '1', 'port': '1', 'speed': 'Auto'}
                                                               ]},
                    'UplinkSet_5': {'name': 'UplinkSet_5', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_3'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                    'logicalPortConfigInfos': [{'bay': '5', 'enclosure': '1', 'port': '4', 'speed': 'Auto'}
                                                               ]}}
# Creating separate LIG for each modules so create separate uplinkset for each hill module with corresponding linked port
uplink_sets_separateLIG = {'UplinkSet_1': {'name': 'UplinkSet_1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_1'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                           'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': '2', 'speed': 'Auto'}
                                                                      ]},
                           'UplinkSet_2': {'name': 'UplinkSet_2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_2'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                           'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '1', 'port': '1', 'speed': 'Auto'}]}
                           }
enet_hill = {"purpose": "General",
             "name": "enet_hill",
             "smartLink": False,
             "privateNetwork": False,
             "connectionTemplateUri": None,
             "ethernetNetworkType": "Untagged",
             "type": "ethernet-networkV4"
             }


fcnets1 = [{"type": "fc-networkV4",
            "name": "FC_1",
            "fabricType": "FabricAttach",
            "linkStabilityTime": 30,
            "autoLoginRedistribution": True
            },
           {"type": "fc-networkV4",
            "name": "FC_2",
            "fabricType": "FabricAttach",
            "linkStabilityTime": 30,
            "autoLoginRedistribution": True
            },
           {"type": "fc-networkV4",
            "name": "FC_3",
            "fabricType": "FabricAttach",
            "linkStabilityTime": 30,
            "autoLoginRedistribution": True
            },
           {"type": "fc-networkV4",
            "name": "FC_4",
            "fabricType": "FabricAttach",
            "linkStabilityTime": 30,
            "autoLoginRedistribution": True
            }]
# Check the hill module bay set when hardware setup is changed
ligs1 = {'lig1':
         {'name': 'LIG1',
          'type': 'logical-interconnect-groupV4',
          'enclosureType': 'C7000',
          'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                      {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                      {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                      {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                      {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC 8Gb 24-Port FC Module'},
                                      {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC 8Gb 24-Port FC Module'}],
          'uplinkSets': [uplink_sets['UplinkSet_1'].copy(), uplink_sets['UplinkSet_2'].copy(), uplink_sets['UplinkSet_3'].copy(), uplink_sets['UplinkSet_4'].copy()],
          'internalNetworkUris': [],
          'stackingMode': 'Enclosure',
          'eTag': None,
          'ethernetSettings': None,
          'state': 'Active',
          'telemetryConfiguration': None,
          'snmpConfiguration': {'type': 'snmp-configuration',
                                'readCommunity': 'public',
                                'systemContact': '',
                                'enabled': 'true',
                                'category': 'snmp-configuration'
                                }
          },
         'lig2':
         {'name': 'LIG2',
          'type': 'logical-interconnect-groupV5',
          'enclosureType': 'C7000',
          'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                      {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                      {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                      {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                      {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC 8Gb 24-Port FC Module'},
                                      {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC 8Gb 24-Port FC Module'}],
          'uplinkSets': [uplink_sets['UplinkSet_5'].copy(), uplink_sets_enc1['UplinkSet_1'].copy(), uplink_sets_enc1['UplinkSet_2'].copy(), uplink_sets_enc1['UplinkSet_3'].copy(), uplink_sets_enc1['UplinkSet_4'].copy()],
          'internalNetworkUris': [],
          'stackingMode': 'Enclosure',
          'eTag': None,
          'ethernetSettings': None,
          'state': 'Active',
          'telemetryConfiguration': None,
          'snmpConfiguration': {'type': 'snmp-configuration',
                                'readCommunity': 'public',
                                'systemContact': '',
                                'enabled': 'true',
                                'category': 'snmp-configuration'
                                }
          },

         'lig3':
         {'name': 'LIG3',
          'type': 'logical-interconnect-groupV5',
          'enclosureType': 'C7000',
          'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                      {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC 16Gb 24-Port FC Module'}
                                      ],
          'uplinkSets': [uplink_sets['UplinkSet_5'].copy(), uplink_sets_separateLIG['UplinkSet_1'].copy()],
          'internalNetworkUris': [],
          'stackingMode': 'Enclosure',
          'eTag': None,
          'ethernetSettings': None,
          'state': 'Active',
          'telemetryConfiguration': None,
          'snmpConfiguration': {'type': 'snmp-configuration',
                                'readCommunity': 'public',
                                'systemContact': '',
                                'enabled': 'true',
                                'category': 'snmp-configuration'
                                }
          },
         'lig4':
         {'name': 'LIG4',
          'type': 'logical-interconnect-groupV5',
          'enclosureType': 'C7000',
          'interconnectMapTemplate': [
              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC 16Gb 24-Port FC Module'}],
          'uplinkSets': [uplink_sets_separateLIG['UplinkSet_2'].copy()],
          'internalNetworkUris': [],
          'stackingMode': 'Enclosure',
          'eTag': None,
          'ethernetSettings': None,
          'state': 'Active',
          'telemetryConfiguration': None,
          'snmpConfiguration': {'type': 'snmp-configuration',
                                'readCommunity': 'public',
                                'systemContact': '',
                                'enabled': 'true',
                                'category': 'snmp-configuration'
                                }
          }}
enc_group_hill = {'name': 'EG_Hill',
                  'enclosureCount': '1',
                  'osDeploymentSettings': None,
                  'powerMode': None,
                  'ambientTemperatureMode': 'Standard',
                  'configurationScript': None,
                  'interconnectBayMappings':
                  [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
                   {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
                   {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
                   {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
                   {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
                   {'interconnectBay': 7, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
                   {'interconnectBay': 8, 'logicalInterconnectGroupUri': 'LIG:LIG1'}]}

enc_group_1 = {'name': 'EG_1',
               'enclosureCount': '1',
               'osDeploymentSettings': None,
               'configurationScript': None,
               'powerMode': None,
               'ambientTemperatureMode': 'Standard',
               'configurationScript': None,
               'interconnectBayMappings':
               [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:LIG2'},
                {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:LIG2'},
                {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG2'},
                {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:LIG2'},
                {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:LIG2'},
                {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG2'}
                ]}

enc_group_separateLIG = {'name': 'EG_2',
                         'enclosureCount': '1',
                         'osDeploymentSettings': None,
                         'configurationScript': None,
                         'powerMode': None,
                         'ambientTemperatureMode': 'Standard',
                         'configurationScript': None,
                         'interconnectBayMappings':
                         [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:LIG3'},
                          {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG3'},
                             {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:LIG4'}
                          ]}
# Check the enclosure ip when it is changed
encs = [{'hostname': '15.186.28.6', 'username': 'Administrator', 'password': 'compaq', 'enclosureGroupUri': 'EG:EG_Hill', 'licensingIntent': 'OneViewNoiLO'}]
encs1 = [{'hostname': '15.186.20.255', 'username': 'Administrator', 'password': 'compaq', 'enclosureGroupUri': 'EG:EG_1', 'licensingIntent': 'OneViewNoiLO'}]
encs_separateLIG = [{'hostname': '15.186.20.255', 'username': 'Administrator', 'password': 'compaq', 'enclosureGroupUri': 'EG:EG_2', 'licensingIntent': 'OneViewNoiLO'}]
ENC1 = 'enc1'
ENC2 = 'enc2'
# Check the hill bay number when the hardware setup is changed
INTERCONNECTS_enc1 = [ENC1 + ', interconnect 3', ENC1 + ', interconnect 4']
INTERCONNECTS_enc2 = [ENC2 + ', interconnect 5', ENC2 + ', interconnect 6']
ic_bay1 = INTERCONNECTS_enc1[0].split()[-1]
ic_bay2 = INTERCONNECTS_enc1[1].split()[-1]
LI = ENC2 + '-' + "EG1 logical interconnect group"
LI1 = ENC1 + '-' + "LIG2"
LI3 = ENC1 + '-' + "LIG3"
LI4 = ENC1 + '-' + "LIG4"
# Check whether the unsupported transceiver connected to any port before running connector suite
unsupported_port = "5"
unsupported_port_status = "ModuleIncompatible"
Invalid_wwn = "00:00:00:00:00:00:00:00"
# Check whether the given analyzer and monitored port is linked before configuring port mirroring
# Analyzer port is linked port from hill not the port given in the uplink set
# Monitored port is linked downlink port
uplink_ports = "2"
analyzer_aport = "4"
analyzer_aport1 = "3"
analyzer_mport = "d6"
analyzer_mport1 = "d3"
used_uplink_port = "2"
FUSION_IP = APPLIANCE_IP
# Chek whether the given password is correct even when tthe hardware setup is changed
Password_IC5 = "8SBNYSQ3"
Password_IC6 = "6KWDJF7J"
FUSION_SSH_USERNAME = "root"
FUSION_SSH_PASSWORD = "hpvse1"
FUSION_PROMPT = '#'               # Fusion Appliance Prompt
FUSION_TIMEOUT = 180
port_map = {
    '1': '17', '2': '18', '3': '19', '4': '20', '5': '29', '6': '30', '7': '31', '8': '0'}
# Check whether the unsupported port is given here
unsupported_transreceiver = {"portName": "5",
                             "speed": "null",
                             "vendorName": "null",
                             "vendorPartNumber": "null",
                             "vendorRevision": "null",
                             "vendorOui": "null",
                             "extIdentifier": "null",
                             "digitalDiagnostics":
                             {
                                 "temperature": "null",
                                 "voltage": "null",
                                 "laneInformation":
                                 [
                                 ]
                             },
                             "serialNumber": "null",
                             "identifier": "UNKNOWN",
                             "connector": "UNKNOWN_OR_UNSPECIFIED"
                             }
# Before triggering the connector suite,Verify the given serial number is correct or not if not change it.
Supported_transreceiver_SFP = {
    "portName": "1",
    "speed": "null",
    "vendorName": "HP-A     BROCADE",
    "vendorPartNumber": "QK724A",
    "vendorRevision": "A",
    "extIdentifier": "null",
    "vendorOui": "00:05:1e",
    "digitalDiagnostics":
    {
        "voltage": "",
        "temperature": "",
        "laneInformation":
        [
            {
                "laneId": "",
                "rxPowermW": "",
                "rxPowerdBm": "",
                "txPowermW": "",
                "txPowerdBm": "",
                "current": ""
            }
        ]
    },
    "identifier": "SFP",
    "serialNumber": "HAA115086051LY2",
    "connector": "LC"
}

Supported_transreceiver_SFP_5 = {
    "portName": "2",
    "speed": "null",
    "vendorName": "HP-F     BROCADE",
    "vendorPartNumber": "QK724A",
    "vendorRevision": "A",
    "extIdentifier": "null",
    "vendorOui": "00:05:1e",
    "digitalDiagnostics":
                                {
                                    "voltage": "3334.000",
                                    "temperature": "38",
                                    "laneInformation":
                                    [
                                        {
                                            "laneId": "1",
                                            "rxPowermW": "0.6260",
                                            "rxPowerdBm": "-2.0340",
                                            "txPowermW": "0.5270",
                                            "txPowerdBm": "-2.7820",
                                            "current": "7.710"
                                        }
                                    ]
                                },
    "identifier": "SFP",
    "serialNumber": "HAF313480000963",
    "connector": "LC"
}
# Check the port given below should be the port which we haven given in the uplinkset for hill module
neg_uplink_sets = {'name': 'UplinkSet_2_1',
                   'ethernetNetworkType': 'NotApplicable',
                   'networkType': 'FibreChannel',
                   'networkUris': [],
                   'fcNetworkUris': ['FC_3'],
                   'fcoeNetworkUris': [],
                   'lacpTimer': 'Short',
                   'logicalInterconnectUri': None,
                   'primaryPortLocation': None,
                   'manualLoginRedistributionState': 'Supported',
                   'connectionMode': 'Auto',
                   'nativeNetworkUri': None,
                   'portConfigInfos': [{'bay': '3', 'port': '4', 'desiredSpeed': 'Auto', 'enclosure': ENC1}
                                       ]}

neg_uplink_sets1 = {'name': 'UplinkSet_2_1',
                    'ethernetNetworkType': 'NotApplicable',
                    'networkType': 'FibreChannel',
                    'networkUris': [],
                    'fcNetworkUris': ['FC_2'],
                    'fcoeNetworkUris': [],
                    'lacpTimer': 'Short',
                    'logicalInterconnectUri': None,
                    'primaryPortLocation': None,
                    'manualLoginRedistributionState': 'Supported',
                    'connectionMode': 'Auto',
                    'nativeNetworkUri': None,
                    'portConfigInfos': [{'bay': '4', 'port': '2', 'desiredSpeed': 'Speed8G', 'enclosure': ENC1}
                                        ]}
# Check whether the server bay given below is in configured state
server_profiles_bay1 = [{'type': 'ServerProfileV9', 'serverHardwareUri': ENC1 + ', bay 3',
                         'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_1', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Physical',
                         'name': 'Profile_server1', 'description': '', 'affinity': 'Bay',
                         'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:enet_hill',
                                                                 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                                {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Auto',
                                                                 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_2',
                                                                 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}]},
                         'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']}, 'bios':{'manageBios': False, 'overriddenSettings': []}, 'sanStorage': None}]

server_profiles_bay10 = [{'type': 'ServerProfileV9', 'serverHardwareUri': ENC1 + ', bay 6',
                          'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_1', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Physical',
                          'name': 'Profile_server10', 'description': '', 'affinity': 'Bay',
                          'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:enet_hill',
                                                                  'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                                 {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Auto',
                                                                  'requestedMbps': 'Auto', 'networkUri': 'FC:FC_1',
                                                                  'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}]},
                          'boot': {'manageBoot': True, 'order': ["HardDisk"]}, 'bootMode':{'manageMode': True, 'mode': 'UEFI', 'secureBoot': 'Disabled', 'pxeBootPolicy': 'Auto'}, 'bios': {'manageBios': False, 'overriddenSettings': []}, 'sanStorage': None}]

server_profiles_separateLIG1 = [{'type': 'ServerProfileV9', 'serverHardwareUri': ENC1 + ', bay 6',
                                 'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_2', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Physical',
                                 'name': 'Profile_server1', 'description': '', 'affinity': 'Bay',
                                 'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:enet_hill',
                                                                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                                        {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Auto',
                                                                         'requestedMbps': 'Auto', 'networkUri': 'FC:FC_1',
                                                                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                                        {'id': 3, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Auto',
                                                                         'requestedMbps': 'Auto', 'networkUri': 'FC:FC_2',
                                                                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}]},
                                 'boot': {'manageBoot': True, 'order': ["HardDisk"]}, 'bootMode':{'manageMode': True, 'mode': 'UEFI', 'secureBoot': 'Disabled', 'pxeBootPolicy': 'Auto'}, 'bios': {'manageBios': False, 'overriddenSettings': []}, 'sanStorage': None}]

server_profiles_separateLIG2 = [{'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 3',
                                 'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_2', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Physical',
                                 'name': 'Profile_server2', 'description': '', 'affinity': 'Bay',
                                 'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:enet_hill',
                                                                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                                        {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Auto',
                                                                         'requestedMbps': 'Auto', 'networkUri': 'FC:FC_2',
                                                                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}]},
                                 'boot': {'manageBoot': True, 'order': ['HardDisk']}, 'bios':{'manageBios': False, 'overriddenSettings': []}, 'sanStorage': None}]

# Check the server bay given here is same as the bay created in server profile
oa_details_1 = {'oa_ip': encs1[0]['hostname'], "username": encs1[0]["username"], "password": encs1[0]["password"], "server_bay": server_profiles_bay10[0]['serverHardwareUri'].split(' ')[-1]}
# Check for LUN drives after giving FC connection to servers
# Eg:Hill in bay 3 and bay4, D drive for IC3 and E drive for IC4
diskspd_cmd = "C:\\Users\\Administrator\\Desktop\\diskspd.exe -c50M -d120 -r -w70 -t19 -o12 -b40k -h -L D:\\multi5.dat >C:\\Ov_restartbefore1.dat"
diskspd_cmd1 = "C:\\Users\\Administrator\\Desktop\\diskspd.exe -c50M -d120 -r -w70 -t19 -o12 -b40k -h -L E:\\multi5.dat >C:\\Ov_restartbefore1.dat"


# Change the module file path before triggering script as current directory path
module_file_path = "C:\\RC_Nov_30\\fusion\\tests\\wpst_crm\\feature_tests\\C7000\\OVF648_Hill_Digital_diagnostics_Port_mirroring_Connector_information\\GetServerIPs.py"
# If the hardware setup check for the server username and password
windows_server_cred = ["Administrator", 'password@123']

server_details = {'username': 'Administrator', 'password': 'password@123'}
# If the hardware setup check for the linux details and ilo username and password
linux_details = {"hostip": "15.186.21.149", "username": "root", "password": "password", "dir_location": "/root/pexpect/pexpect-u-2.5.1/",
                 "python_cmd": "python2.7"}
ilo_details = {'ilo_ip': '', 'username': 'Administrator', 'password': 'hpvse123'}

server_bay_1 = "6"
server_bay_10 = "3"
interconnect_state = ["Maintenance", "Configured"]

li_portmonitor = {
    "analyzerPort": {
        "portUri": "",
        "portMonitorConfigInfo": "AnalyzerPort"
    },
    "enablePortMonitor": "true",
    "type": "port-monitor",
    "monitoredPorts": [
        {
            "portUri": "",
            "portMonitorConfigInfo": "MonitoredBoth"
        }
    ]
}

li_portmonitor_from_server = {
    "analyzerPort": {
        "portUri": "",
        "portMonitorConfigInfo": "AnalyzerPort"
    },
    "enablePortMonitor": "true",
    "type": "port-monitor",
    "monitoredPorts": [
        {
            "portUri": "",
            "portMonitorConfigInfo": "MonitoredFromServer"
        }
    ]
}

li_portmonitor_to_server = {
    "analyzerPort": {
        "portUri": "",
        "portMonitorConfigInfo": "AnalyzerPort"
    },
    "enablePortMonitor": "true",
    "type": "port-monitor",
    "monitoredPorts": [
        {
            "portUri": "",
            "portMonitorConfigInfo": "MonitoredToServer"
        }
    ]
}

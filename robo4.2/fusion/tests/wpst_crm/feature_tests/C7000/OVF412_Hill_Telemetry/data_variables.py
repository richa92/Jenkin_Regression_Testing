import os
import sys

cwd = os.getcwd()
download_to_path = cwd


def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist

APPLIANCE_IP = '15.186.17.191'
ENCLOSURE_IP = '15.186.20.255'
OA_USER = "Administrator"
OA_PASS = "compaq"
DEVICE = "IOM"
ACTION = ["ON", "OFF"]
interconnect_bay3 = "3"
interconnect_bay4 = "4"
admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

network_admin = {'userName': 'Networkadmin', 'password': 'Networkadmin'}

serveradmin = {'userName': 'Serveradmin', 'password': 'Serveradmin'}

up_ports_3 = ['2', '3', '4']
up_ports_4 = ['1', '2', '3']
dw_ports_3 = ['d3', 'd6', 'd8']

users = [{'type': 'UserAndPermissions', 'userName': 'Serveradmin', 'fullName': 'Serveradmin', 'password': 'Serveradmin', 'emailAddress': '', 'officePhone': '', 'mobilePhone': '', 'enabled': True, 'permissions': [{'roleName': 'Server administrator', 'scopeUri': None}]}, {'type': 'UserAndPermissions', 'userName': 'Networkadmin', 'fullName': 'Networkadmin', 'password': 'Networkadmin', 'emailAddress': '', 'officePhone': '', 'mobilePhone': '', 'enabled': True, 'permissions': [{'roleName': 'Network administrator', 'scopeUri': None}]}]

enet_hill = {"purpose": "General",
             "name": "enet_hill",
             "smartLink": False,
             "privateNetwork": False,
             "connectionTemplateUri": None,
             "ethernetNetworkType": "Untagged",
             "type": "ethernet-networkV4"
             }

fcnets1 = [{"type": "fc-networkV4",
            "name": "FC3",
            "fabricType": "FabricAttach",
            "linkStabilityTime": 30,
            "autoLoginRedistribution": True
            },
           {"type": "fc-networkV4",
            "name": "FC4",
            "fabricType": "FabricAttach",
            "linkStabilityTime": 30,
            "autoLoginRedistribution": True
            },
           {"type": "fc-networkV4",
            "name": "FC5",
            "fabricType": "FabricAttach",
            "linkStabilityTime": 30,
            "autoLoginRedistribution": True
            },
           {"type": "fc-networkV4",
            "name": "FC6",
            "fabricType": "FabricAttach",
            "linkStabilityTime": 30,
            "autoLoginRedistribution": True
            }]

uplink_sets1 = {'UplinkSet_1': {'name': 'UplinkSet_1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_1'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                'logicalPortConfigInfos': [{'bay': '5', 'enclosure': '1', 'port': '2', 'speed': 'Auto'}
                                                           ]},
                'UplinkSet_2': {'name': 'UplinkSet_2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_2'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                'logicalPortConfigInfos': [{'bay': '6', 'enclosure': '1', 'port': '1', 'speed': 'Auto'}]}
                }
uplink_sets = {'UplinkSet_1': {'name': 'UplinkSet_1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_1'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                               'logicalPortConfigInfos': [{'bay': '5', 'enclosure': '1', 'port': '1', 'speed': 'Auto'}
                                                          ]},
               'UplinkSet_2': {'name': 'UplinkSet_2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_2'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                               'logicalPortConfigInfos': [{'bay': '6', 'enclosure': '1', 'port': '1', 'speed': 'Auto'}]},
               'UplinkSet_3': {'name': 'UplinkSet_3', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_3'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                               'logicalPortConfigInfos': [{'bay': '7', 'enclosure': '1', 'port': '1', 'speed': 'Auto'}]},
               'UplinkSet_4': {'name': 'UplinkSet_4', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_4'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                               'logicalPortConfigInfos': [{'bay': '8', 'enclosure': '1', 'port': '1', 'speed': 'Auto'}]},
               'UplinkSet_5': {'name': 'us_eth', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Untagged', 'networkUris': ['enet_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                               'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '1', 'port': 'X5', 'speed': 'Auto'}]}}

uplink_sets_enc1 = {'UplinkSet_1': {'name': 'UplinkSet_1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC3'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                    'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': '2', 'speed': 'Auto'}
                                                               ]},
                    'UplinkSet_2': {'name': 'UplinkSet_2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC4'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                    'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '1', 'port': '1', 'speed': 'Auto'}]},
                    'UplinkSet_3': {'name': 'UplinkSet_3', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC5'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                    'logicalPortConfigInfos': [{'bay': '5', 'enclosure': '1', 'port': '1', 'speed': 'Auto'}
                                                               ]},
                    'UplinkSet_4': {'name': 'UplinkSet_4', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC6'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                    'logicalPortConfigInfos': [{'bay': '6', 'enclosure': '1', 'port': '1', 'speed': 'Auto'}
                                                               ]}
                    }

Lig_name = 'LIG1'
Lig_name1 = 'LIG2'
LI = 'enc1-LIG1'

telemetry_0 = {"type": "telemetry-configuration", "enableTelemetry": "true", "sampleCount": 0, "sampleInterval": 60}
telemetry_interval_0 = {"type": "telemetry-configuration", "enableTelemetry": "true", "sampleCount": 60, "sampleInterval": 0}
telemetry_enable = {"type": "telemetry-configuration", "enableTelemetry": "false", "sampleCount": 60, "sampleInterval": 60}
true_flag = True
Invalid_vcfcsampleIntervals = [-1, -60, '$@#', 'ONE_SAMPLE_PER_ONE_SECONDS', 'ONE_SAMPLE_PER_FIVE_SECONDS', 'ONE_SAMPLE_PER_TWO_HOUR']
Invalid_vcfcsampleIntervals1 = [15, 300, 3800]
ligs1 = {'lig2':
         {'name': Lig_name,
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
          'snmpConfiguration': None
          },
         'lig3':
         {'name': Lig_name1,
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
          'telemetryConfiguration': {"type": "telemetry-configuration", "enableTelemetry": 'true', "sampleInterval": 300, "sampleCount": 12, "category": "telemetry-configurations", "vcfcsampleIntervals": ''},
          'snmpConfiguration': None
          },
         'lig4':
         {'name': Lig_name,
          'type': 'logical-interconnect-groupV5',
          'enclosureType': 'C7000',
          'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                      {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                      {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC 16Gb 24-Port FC Module'}
                                      ],
          'uplinkSets': [uplink_sets['UplinkSet_5'].copy(), uplink_sets_enc1['UplinkSet_1'].copy(), uplink_sets_enc1['UplinkSet_2'].copy()],
          'internalNetworkUris': [],
          'stackingMode': 'Enclosure',
          'eTag': None,
          'ethernetSettings': None,
          'state': 'Active',
          'telemetryConfiguration': None,
          'snmpConfiguration': None
          },
         'lig_neg': {'name': Lig_name,
                     'type': 'logical-interconnect-groupV5',

                     'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                                 {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                                 {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                                 {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                                 {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC 8Gb 24-Port FC Module'},
                                                 {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC 8Gb 24-Port FC Module'}],
                     'uplinkSets': [uplink_sets['UplinkSet_5'].copy(), uplink_sets_enc1['UplinkSet_1'].copy(), uplink_sets_enc1['UplinkSet_2'].copy()],
                     'internalNetworkUris': [],
                     'stackingMode': 'Enclosure',
                     'eTag': None,
                     'ethernetSettings': None,
                     'state': 'Active',
                     'telemetryConfiguration': {"type": "telemetry-configuration", "enableTelemetry": 'true', "sampleInterval": 300, "sampleCount": 12, "category": "telemetry-configurations", "vcfcsampleIntervals": ''},
                              'snmpConfiguration': None
                     },
         'lig_neg1': {'name': Lig_name,
                      'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                                  {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},

                                                  {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC 8Gb 24-Port FC Module'},
                                                  {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC 8Gb 24-Port FC Module'}],
                      'uplinkSets': [uplink_sets['UplinkSet_5'].copy(), uplink_sets_enc1['UplinkSet_3'].copy(), uplink_sets_enc1['UplinkSet_4'].copy()],
                      'internalNetworkUris': [],
                      'stackingMode': 'Enclosure',
                      'eTag': None,
                      'ethernetSettings': None,
                      'state': 'Active',
                      'telemetryConfiguration': None,
                      'snmpConfiguration': None
                      },
         'lig_neg2': {'name': Lig_name,
                      'type': 'logical-interconnect-groupV400',

                      'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                                  {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                                  {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                                  {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                                  {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC 8Gb 24-Port FC Module'},
                                                  {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC 8Gb 24-Port FC Module'}],
                      'uplinkSets': [uplink_sets['UplinkSet_1'].copy(), uplink_sets['UplinkSet_2'].copy()],
                      'internalNetworkUris': [],
                      'stackingMode': 'Enclosure',
                      'eTag': None,
                      'ethernetSettings': None,
                      'state': 'Active',
                      'telemetryConfiguration': {"type": "telemetry-configuration", "enableTelemetry": 'false', "sampleCount": 60, "sampleInterval": 60},
                              'snmpConfiguration': None
                      }}

enc_group_1 = {'name': 'EG',
               'enclosureCount': '1',
               'osDeploymentSettings': None,
               'configurationScript': None,
               'powerMode': None,
               'ambientTemperatureMode': 'Standard',
               'configurationScript': None,
               'interconnectBayMappings':
               [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
                {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
                {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
                {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
                {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
                {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG1'}
                ]}

enc_group_2 = {'name': 'EG',
               'enclosureCount': '1',
               'osDeploymentSettings': None,
               'configurationScript': None,
               'powerMode': None,
               'ambientTemperatureMode': 'Standard',
               'configurationScript': None,
               'interconnectBayMappings':
               [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
                {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
                {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
                ]}

encs1 = [{'hostname': ENCLOSURE_IP, 'username': 'Administrator', 'password': 'compaq', 'enclosureGroupUri': 'EG:EG', 'licensingIntent': 'OneViewNoiLO'}]
ENC1 = 'enc1'
les = {'le1':
       {'name': 'enc1',
        }}
INTERCONNECTS_enc1 = [ENC1 + ', interconnect 3', ENC1 + ', interconnect 4']
Edit_Uplink_Port = {'associatedUplinkSetUri': '',
                    'interconnectName': INTERCONNECTS_enc1[0],
                    'portType': 'Uplink',
                    'portId': '',
                    'portHealthStatus': '',
                    'capability': ['FibreChannel'],
                    'configPortTypes': ['FibreChannel'],
                    'enabled': '',
                    'portName': '',
                    'portStatus': '',
                    'type': 'port'}
interconnect_state = ["Maintenance", "Configured", "Absent"]
server_profiles1 = [{'type': 'ServerProfileV9', 'serverHardwareUri': ENC1 + ', bay 3',
                     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Physical',
                     'name': 'Profile_server2', 'description': '', 'affinity': 'Bay',
                     'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:enet_hill',
                                                             'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                            {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Auto',
                                                             'requestedMbps': 'Auto', 'networkUri': 'FC:FC3',
                                                             'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                            {'id': 3, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Auto',
                                                             'requestedMbps': 'Auto', 'networkUri': 'FC:FC4',
                                                             'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}]},
                     'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']}, 'bios':{'manageBios': False, 'overriddenSettings': []}, 'sanStorage': None}]

server_profile6 = [{'type': 'ServerProfileV9', 'serverHardwareUri': ENC1 + ', bay 6',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'Profile_server1', 'description': '', 'affinity': 'Bay',
                    'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:enet_hill',
                                                                           'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                           {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Auto',
                                                            'requestedMbps': 'Auto', 'networkUri': 'FC:FC3',
                                                            'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                           {'id': 3, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Auto',
                                                            'requestedMbps': 'Auto', 'networkUri': 'FC:FC4',
                                                            'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                           ]},
                    'boot': {'manageBoot': True, 'order': ['CD', 'USB', 'HardDisk', 'PXE']}, 'bios':{'manageBios': True, 'overriddenSettings': []}, 'sanStorage': None}]
oa_details_1 = {'oa_ip': encs1[0]['hostname'], "username": encs1[0]["username"], "password": encs1[0]["password"], "server_bay": server_profile6[0]['serverHardwareUri'].split(' ')[-1]}
oa_details_2 = {'oa_ip': encs1[0]['hostname'], "username": encs1[0]["username"], "password": encs1[0]["password"], "server_bay": server_profiles1[0]['serverHardwareUri'].split(' ')[-1]}

diskspd_cmd = "C:\\Users\\Administrator\\Desktop\\diskspd.exe -c50M -d120 -r -w70 -t9 -o9 -b20K -h -L D:\\multi5.dat >C:\\Ov_restartbefore1.dat"
diskspd_cmd4 = "C:\\Users\\Administrator\\Desktop\\diskspd.exe -c50M -d60 -r -w70 -t9 -o9 -b20K -h -L E:\\multi5.dat >C:\\Ov_restartbefore1.dat"
diskspd_cmd1 = "C:\\Users\\Administrator\\Desktop\\diskspd.exe -c50M -d300 -r -w70 -t9 -o9 -b20K -h -L D:\\multi5.dat >C:\\Ov_restartbefore1.dat"
diskspd_cmd3 = "C:\\Users\\Administrator\\Desktop\\diskspd.exe -c50M -d120 -r -w70 -t9 -o9 -b20K -h -L D:\\multi5.dat >C:\\Ov_restartbefore1.dat"
diskspd_cmd2 = "C:\\Users\\Administrator\\Desktop\\diskspd.exe -c50M -d3600 -r -w70 -t9 -o9 -b20K -h -L D:\\multi5.dat >C:\\Ov_restartbefore1.dat"
module_file_path = "C:\\DB_4.10\\fusion\\tests\\wpst_crm\\feature_tests\\C7000\\OVF412\\GetServerIPs.py"
SPP_bundle_308 = 'SPPGen10Snap1FF.2017_0807.40.iso'
SPP_bundle_400 = 'bp-2017-09-29-01.iso'
fw_uri_308 = '/rest/firmware-drivers/SPPGen10Snap1FF_2017_0807_40'
fw_uri_400 = '/rest/firmware-drivers/bp-2017-09-29-01'
kill_diskspd = "TASKKILL /F /IM diskspd.exe"
windows_server_cred = ["Administrator", 'password@123']

server_details = {'username': 'Administrator', 'password': 'password@123'}

linux_details = {"hostip": "15.186.21.149", "username": "root", "password": "password", "dir_location": "/root/pexpect/pexpect-u-2.5.1/",
                 "python_cmd": "python2.7"}

server_bay_1 = "1"
server_bay_10 = "10"

fc_bay_num_3 = uplink_sets_enc1['UplinkSet_1']['logicalPortConfigInfos'][0]['bay']
fc_bay_num_4 = "4"
portno_for_statistics_3_2 = uplink_sets_enc1['UplinkSet_1']['logicalPortConfigInfos'][0]['port']
portno_for_statistics_3_d6 = "d6"
portno_for_statistics_3_d3 = "d3"
portno_for_statistics_3_3 = "3"
portno_for_statistics_3_4 = "4"
portno_for_statistics_4_1 = "1"
portno_for_statistics_4_d6 = "d6"
portno_for_statistics_4_d3 = "d3"
portno_for_statistics_4_2 = "2"
portno_for_statistics_4_3 = "3"


fc_bay_num_6 = uplink_sets['UplinkSet_1']['logicalPortConfigInfos'][0]['bay']
portno_for_statistics_6_1 = "1"


Edit_telemetry = {'name': Lig_name,
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
                  'telemetryConfiguration': '',
                  'snmpConfiguration': None
                  }

Edit_telemetry_24 = {'name': Lig_name,

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
                     'telemetryConfiguration': {"type": "telemetry-configuration", "enableTelemetry": 'true', "sampleCount": 24, "sampleInterval": 3600},
                     'snmpConfiguration': None
                     }
restart_mode = 'REBOOT'

total_samples_60 = 59
total_samples_10 = 9
total_samples_24 = 23
expected_samples = 5
sample_interval = ['ONE_SAMPLE_PER_SIX_SECONDS', 'ONE_SAMPLE_PER_MINUTE', 'ONE_SAMPLE_PER_HOUR']
telemetry_default_enabled = {'enableTelemetry': True}
telemetry_default = "ONE_SAMPLE_PER_MINUTE"
telemetry_10 = {"type": "telemetry-configuration", "enableTelemetry": "true", "sampleInterval": 300, "sampleCount": 12, "category": "telemetry-configurations", "vcfcsampleIntervals": "ONE_SAMPLE_PER_SIX_SECONDS"}
telemetry_60 = {"type": "telemetry-configuration", "enableTelemetry": "true", "sampleInterval": 300, "sampleCount": 12, "category": "telemetry-configurations", "vcfcsampleIntervals": "ONE_SAMPLE_PER_MINUTE"}
telemetry_24 = {"type": "telemetry-configuration", "enableTelemetry": "true", "sampleInterval": 300, "sampleCount": 12, "category": "telemetry-configurations", "vcfcsampleIntervals": "ONE_SAMPLE_PER_HOUR"}
neg_telemetry_li = {"type": "telemetry-configuration", "enableTelemetry": "true", "sampleInterval": 300, "sampleCount": 12, "category": "telemetry-configurations", "vcfcsampleIntervals": Invalid_vcfcsampleIntervals}
UNSUPPORTED_API = ['300', '400', '500', '600']
telemetry_enable_errorcode = 'CRM_INVALID_ARGUMENT_FC_ENABLE_TELEMETRY'
liupdate_body = {"sppUri": ' ', "command": "UPDATE", "force": True, "ethernetActivationType": "Serial", "ethernetActivationDelay": "0", "fcActivationType": "Serial", "fcActivationDelay": "0", "validationType": "None"}

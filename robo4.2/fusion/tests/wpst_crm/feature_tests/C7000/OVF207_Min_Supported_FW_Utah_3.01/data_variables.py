import os
import sys

cwd = os.getcwd()
download_to_path = cwd


def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist

SSH_PASS = 'hpvse1'
APPLIANCE_IP_3_10 = '15.186.12.237'
APPLIANCE_IP_3_00 = '15.186.25.22'

appliance_cred = ['root', 'hpvse1']

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

network_user = {'enabled': True, 'password': 'wpsthpvse1', 'roles': ['Network administrator'], 'type': 'UserAndRoles', 'userName': 'NetworkUser'}

users = [{'enabled': True, 'password': 'wpsthpvse1', 'roles': ['Backup administrator'], 'type': 'UserAndRoles', 'userName': 'BackupUser'},
         {'enabled': True, 'password': 'wpsthpvse1', 'roles': ['Server administrator'], 'type': 'UserAndRoles', 'userName': 'ServerUser'},
         {'enabled': True, 'password': 'wpsthpvse1', 'roles': ['Storage administrator'], 'type': 'UserAndRoles', 'userName': 'Storageuser'},
         {'enabled': True, 'password': 'wpsthpvse1', 'roles': ['Server firmware operator'], 'type': 'UserAndRoles', 'userName': 'Operator'},
         {'enabled': True, 'password': 'wpsthpvse1', 'roles': ['Software administrator'], 'type': 'UserAndRoles', 'userName': 'Softwareuser'}]

ENC2 = 'enc2'
ENC1 = 'enc1'
LE = 'enc1'
LI = 'enc2-LIG_Utah'
EG1 = 'EG_Utah'
server_bay_2 = '2'
key = 'If-Match'
value = '*'


SPP_bundle_301 = 'SPP2015100.2015_0921.6.iso'
SPP_bundle_308 = 'SPP2017070.2017_0528.144.iso'
SPP_bundle_111 = 'SPP2014090.2014_0827.10.iso'
SPP_bundle_300 = 'SPPGen9Snap2.2014_1022.39.iso'

encs = [{'hostname': '15.186.28.6', 'username': 'Administrator', 'password': 'compaq', 'enclosureGroupUri': 'EG:EG_Utah', 'force': False, 'licensingIntent': 'OneViewNoiLO'}]

ilo_details = {'ilo_ip': '', 'username': 'Administrator', 'password': 'password@123'}

server_details = {'username': 'Administrator', 'password': 'hpvse1'}

diskspd_cmd_60s = "PowerShell.exe -ExecutionPolicy Bypass -File .\\test-60s.ps1"

linux_details = {"hostip": "15.186.21.149", "username": "root", "password": "password", "dir_location": "/root/pexpect/pexpect-u-2.5.1/",
                 "python_cmd": "python2.7"}

oa_details_1 = {'oa_ip': encs[0]['hostname'], "username": encs[0]["username"], "password": encs[0]["password"], "server_bay": '1'}

module_file_path = "C:\\TBird_regression_SPRINT_97\\fusion\\tests\\wpst_crm\\feature_tests\\C7000\\OVF207_Min_Supported_FW_Utah_3.01\\GetServerIPs.py"

diskspd_cmd1 = "C:\\disk\\Diskspd-v2.0.17\\amd64fre\\diskspd.exe -c50M -d10 -r -w70 -t9 -o9 -b20K -h -L D:\\multi5.dat >C:\\Ov_restartbefore1.dat"

windows_server_cred = ["Administrator", 'password@123']

INTERCONNECTS_UTAH = ['enc2, interconnect 7', 'enc2, interconnect 8']

fc_firmwareVersion_latest = '3.08'
fc_firmwareVersion_301 = '3.01'
fc_firmwareVersion_old = '1.11'

fw_uri_111 = '/rest/firmware-drivers/SPP2014090_2014_0827_10'
fw_uri_301 = '/rest/firmware-drivers/SPP2015100_2015_0921_6'
fw_uri_305 = '/rest/firmware-drivers/SPP2016100_2016_1015_191'
fw_uri_308 = '/rest/firmware-drivers/SPP2017070_2017_0528_144'
fw_uri_300 = '/rest/firmware-drivers/SPPGen9Snap2_2014_1022_39'


bay1 = '1'
bin_310 = 'HPEOneView-fullupdate-3.10.02-SNAPSHOT-0298391.bin'

Upload_Sleep_Time = '4200'
Upload_Sleep_Time1 = '1800'
version_Check = '3.10.02-0298391'
version_300 = '3.00.08-0298859'

fcNet_utah = [{'type': 'fc-networkV300',
               'linkStabilityTime': 30,
               'autoLoginRedistribution': True,
               'name': 'fc1_utah',
               'connectionTemplateUri': None,
               'managedSanUri': None,
               'fabricType': 'FabricAttach'},
              {'type': 'fc-networkV300',
               'linkStabilityTime': 30,
               'autoLoginRedistribution': True,
               'name': 'fc2_utah',
               'connectionTemplateUri': None,
               'managedSanUri': None,
               'fabricType': 'FabricAttach'},
              {'type': 'fc-networkV300',
               'linkStabilityTime': 30,
               'autoLoginRedistribution': True,
               'name': 'fc3_utah',
               'connectionTemplateUri': None,
               'managedSanUri': None,
               'fabricType': 'FabricAttach'},
              {'type': 'fc-networkV300',
               'linkStabilityTime': 30,
               'autoLoginRedistribution': True,
               'name': 'fc4_utah',
               'connectionTemplateUri': None,
               'managedSanUri': None,
               'fabricType': 'FabricAttach'}]

enet_hill = {"purpose": "General",
             "name": "enet_hill",
             "smartLink": False,
             "privateNetwork": False,
             "connectionTemplateUri": None,
             "ethernetNetworkType": "Untagged",
             "type": "ethernet-networkV300"
             }

lig_uplink_config = {'UplinkSet_1': {'name': 'us_1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc1_utah'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                     'logicalPortConfigInfos': [{'bay': '7', 'enclosure': '1', 'port': '1', 'speed': 'Auto'}]},
                     'UplinkSet_2': {'name': 'us_2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc2_utah'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                     'logicalPortConfigInfos': [{'bay': '8', 'enclosure': '1', 'port': '1', 'speed': 'Auto'}]},
                     'UplinkSet_3': {'name': 'us_3', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc3_utah'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                     'logicalPortConfigInfos': [{'bay': '5', 'enclosure': '1', 'port': '1', 'speed': 'Auto'}]},
                     'UplinkSet_4': {'name': 'us_4', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc4_utah'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                     'logicalPortConfigInfos': [{'bay': '6', 'enclosure': '1', 'port': '1', 'speed': 'Auto'}]},
                     'UplinkSet_5': {'name': 'us_5', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc1_utah'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                     'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '1', 'port': '1', 'speed': 'Auto'}]},
                     'UplinkSet_6': {'name': 'us_6', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc2_utah'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                     'logicalPortConfigInfos': [{'bay': '5', 'enclosure': '1', 'port': '1', 'speed': 'Auto'}]}
                     }

lig_uplink_sets = {'UplinkSet_1': {'name': 'us_eth', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Untagged', 'networkUris': ['enet_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                   'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '1', 'port': 'X5', 'speed': 'Auto'}]}}

lig_utah = {'name': 'LIG_Utah',
            'type': 'logical-interconnect-groupV4',
            'enclosureType': 'C7000',
            'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                        {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                        {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                                        {'enclosure': 1, 'enclosureIndex': 1, 'bay': 7, 'type': 'HP VC 8Gb 24-Port FC Module'},
                                        {'enclosure': 1, 'enclosureIndex': 1, 'bay': 8, 'type': 'HP VC 8Gb 24-Port FC Module'}],
            'uplinkSets': [lig_uplink_config['UplinkSet_1'].copy(), lig_uplink_config['UplinkSet_2'].copy()],
            'stackingMode': 'Enclosure',
            'ethernetSettings': None,
            'state': 'Active',
            'telemetryConfiguration': None,
            'snmpConfiguration': {'type': 'snmp-configuration', 'readCommunity': 'public', 'systemContact': '', 'trapDestinations': [{'trapDestination': '15.186.21.149', 'communityString': 'public', 'trapFormat': 'SNMPv1', 'trapSeverities': ['Critical', 'Major', 'Minor', 'Warning', 'Normal', 'Info', 'Unknown'], 'vcmTrapCategories': ['Legacy'], 'enetTrapCategories': ['PortStatus', 'PortThresholds', 'Other'], 'fcTrapCategories': ['PortStatus', 'Other']}], 'snmpAccess': [], 'enabled': False, 'description': None, 'name': None, 'state': None, 'status': None, 'eTag': None, 'category': 'snmp-configuration', 'uri': None},
            'qosConfiguration': None}

lig_utah_111 = {'name': 'LIG_Utah',
                'type': 'logical-interconnect-groupV300',
                'enclosureType': 'C7000',
                'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                                            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 7, 'type': 'HP VC 8Gb 24-Port FC Module'},
                                            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 8, 'type': 'HP VC 8Gb 24-Port FC Module'}
                                            ],
                'uplinkSets': [lig_uplink_config['UplinkSet_1'].copy(), lig_uplink_config['UplinkSet_2'].copy(), lig_uplink_sets['UplinkSet_1'].copy()],
                'stackingMode': 'Enclosure',
                'ethernetSettings': None,
                'state': 'Active',
                'telemetryConfiguration': None,
                'snmpConfiguration': {'type': 'snmp-configuration', 'readCommunity': 'public', 'systemContact': '', 'trapDestinations': [{'trapDestination': '15.186.21.149', 'communityString': 'public', 'trapFormat': 'SNMPv1', 'trapSeverities': ['Critical', 'Major', 'Minor', 'Warning', 'Normal', 'Info', 'Unknown'], 'vcmTrapCategories': ['Legacy'], 'enetTrapCategories': ['PortStatus', 'PortThresholds', 'Other'], 'fcTrapCategories': ['PortStatus', 'Other']}], 'snmpAccess': [], 'enabled': False, 'description': None, 'name': None, 'state': None, 'status': None, 'eTag': None, 'category': 'snmp-configuration', 'uri': None},
                'qosConfiguration': None}

lig_utah_111_310 = {'name': 'LIG_Utah',
                    'type': 'logical-interconnect-groupV4',
                    'enclosureType': 'C7000',
                    'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                                {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                                {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                                                {'enclosure': 1, 'enclosureIndex': 1, 'bay': 7, 'type': 'HP VC 8Gb 24-Port FC Module'},
                                                {'enclosure': 1, 'enclosureIndex': 1, 'bay': 8, 'type': 'HP VC 8Gb 24-Port FC Module'}],
                    'uplinkSets': [lig_uplink_config['UplinkSet_1'].copy(), lig_uplink_config['UplinkSet_2'].copy()],
                    'stackingMode': 'Enclosure',
                    'ethernetSettings': None,
                    'state': 'Active',
                    'telemetryConfiguration': None,
                    'snmpConfiguration': {'type': 'snmp-configuration', 'readCommunity': 'public', 'systemContact': '', 'trapDestinations': [{'trapDestination': '15.186.21.149', 'communityString': 'public', 'trapFormat': 'SNMPv1', 'trapSeverities': ['Critical', 'Major', 'Minor', 'Warning', 'Normal', 'Info', 'Unknown'], 'vcmTrapCategories': ['Legacy'], 'enetTrapCategories': ['PortStatus', 'PortThresholds', 'Other'], 'fcTrapCategories': ['PortStatus', 'Other']}], 'snmpAccess': [], 'enabled': False, 'description': None, 'name': None, 'state': None, 'status': None, 'eTag': None, 'category': 'snmp-configuration', 'uri': None},
                    'qosConfiguration': None}

enc_group_utah = {'name': 'EG_Utah',
                  'ipRangeUris': [],
                  'enclosureCount': 1,
                  'osDeploymentSettings': None,
                  'configurationScript': None,
                  'powerMode': None,
                  'ambientTemperatureMode': 'Standard',
                  'interconnectBayMappings': [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:LIG_Utah'},
                                              {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:LIG_Utah'},
                                              {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:LIG_Utah'},
                                              {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
                                              {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                                              {'interconnectBay': 6, 'logicalInterconnectGroupUri': None},
                                              {'interconnectBay': 7, 'logicalInterconnectGroupUri': 'LIG:LIG_Utah'},
                                              {'interconnectBay': 8, 'logicalInterconnectGroupUri': 'LIG:LIG_Utah'}]}

enc_group_utah_111 = {'name': 'EG_Utah',
                      'type': 'EnclosureGroupV300',
                      'enclosureTypeUri': '/rest/enclosure-types/c7000',
                      'stackingMode': 'Enclosure',
                      'interconnectBayMappingCount': 8,
                      'configurationScript': None,
                      'interconnectBayMappings': [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:LIG_Utah'},
                                                  {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:LIG_Utah'},
                                                  {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
                                                  {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:LIG_Utah'},
                                                  {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                                                  {'interconnectBay': 6, 'logicalInterconnectGroupUri': None},
                                                  {'interconnectBay': 7, 'logicalInterconnectGroupUri': 'LIG:LIG_Utah'},
                                                  {'interconnectBay': 8, 'logicalInterconnectGroupUri': 'LIG:LIG_Utah'}]}

enc_group_utah_111_310 = {'name': 'EG_Utah', 'interconnectBayMappings': [
    {'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:LIG_Utah'},
    {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:LIG_Utah'},
    {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
    {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:LIG_Utah'},
    {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
    {'interconnectBay': 6, 'logicalInterconnectGroupUri': None},
    {'interconnectBay': 7, 'logicalInterconnectGroupUri': 'LIG:LIG_Utah'},
    {'interconnectBay': 8, 'logicalInterconnectGroupUri': 'LIG:LIG_Utah'}],
    'ipRangeUris': [],
    'enclosureCount': 1,
    'osDeploymentSettings': None,
    'configurationScript': None,
    'powerMode': None,
    'ambientTemperatureMode': 'Standard'}


encs_m = {'hostname': '15.186.27.232', 'username': 'Administrator', 'password': 'compaq', 'enclosureGroupUri': None, 'licensingIntent': 'OneViewStandard', 'state': 'Monitored'}

enc_body1 = {'hostname': '15.186.28.6', 'username': 'Administrator', 'password': 'compaq', 'enclosureGroupUri': 'EG:EG_Utah', 'force': False, 'licensingIntent': 'OneViewNoiLO'}

# encs_fwupdate variable added only for Suite3
encs_fwupdate = {'hostname': '15.186.28.6', 'username': 'Administrator', 'password': 'compaq', 'enclosureGroupUri': '', 'force': False, 'licensingIntent': 'OneView', 'firmwareBaselineUri': fw_uri_111, 'forceInstallFirmware': True, 'updateFirmwareOn': 'EnclosureOnly'}

leupdate_body = [{"op": "replace", "path": "/firmware", "value": {"firmwareBaselineUri": '', "forceInstallFirmware": True, "firmwareUpdateOn": "SharedInfrastructureOnly", "logicalInterconnectUpdateMode": "Parallel", "validateIfLIFirmwareUpdateIsNonDisruptive": False, "updateFirmwareOnUnmanagedInterconnect": False}}]

liupdate_body = {"sppUri": ' ', "command": "UPDATE", "force": True, "ethernetActivationType": "Parallel", "ethernetActivationDelay": "0", "fcActivationType": "Parallel", "fcActivationDelay": "0", "validationType": "None"}

server_profiles = [{'type': 'ServerProfileV7', 'serverHardwareUri': ENC2 + ', bay 2',
                            'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC2, 'enclosureGroupUri': 'EG:EG_Utah', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                            'name': 'PROFILE1', 'description': '', 'affinity': 'Bay',
                            'boot': {'manageBoot': False},
                            'bootMode': None,
                            'connections': [{'id': 1, 'name': 'Downlink_1', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'FC:fc1_utah',
                                             'wwnn': '20:00:7E:9B:F9:0B:00:7F', 'wwpn': '10:00:7E:9B:F9:0B:00:7F', 'wwpnType': 'UserDefined'}
                                            ]}
                   ]

server_profiles_gen9 = [{'type': 'ServerProfileV6', 'serverHardwareUri': ENC2 + ', bay 3',
                         'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC2, 'enclosureGroupUri': 'EG:EG_Utah', 'serialNumberType': 'Virtual', 'macType': 'Physical', 'wwnType': 'Physical',
                         'name': 'Profile_server3', 'description': '', 'affinity': 'Bay',
                         'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:enet_hill', 'mac': None, 'wwpn': '', 'wwnn': ''},
                                         {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': 'Auto', 'networkUri': 'FC:fc1_utah', 'mac': None, 'wwpn': '', 'wwnn': ''}],
                         'boot': None, 'bootMode': {'manageMode': False}, 'bios': {'manageBios': False, 'overriddenSettings': []}, 'sanStorage': None}]

server_profiles_bay1 = [{'type': 'ServerProfileV7', 'serverHardwareUri': ENC2 + ', bay 1',
                         'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC2, 'enclosureGroupUri': 'EG:EG_Utah', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Physical',
                         'name': 'Profile_server1', 'description': '', 'affinity': 'Bay',
                         'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:enet_hill', 'mac': None, 'wwpn': '', 'wwnn': ''},
                                         {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': 'Auto', 'networkUri': 'FC:fc1_utah', 'mac': None, 'wwpn': '', 'wwnn': ''}],
                         'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']}, 'bios':{'manageBios': False, 'overriddenSettings': []}, 'sanStorage': None}]

valDict_1 = {'recommendedActions': 'Retry the downgrade operation for the constituent interconnects with an SPP containing the supported firmware version or higher.'}


valDict_user = {'status_code': 401,
                'errorCode': 'AUTHORIZATION',
                'message': 'Authorization error: User not authorized for this operation.'}

valDict_Action = {'recommendedActions': [u'Update logical interconnect firmware with SPP containing either Virtual Connect firmware version 4.41, 4.45, or 4.50 prior to upgrading to firmware version 4.60 or higher.']}

valDict_msg = '"Virtual Connect 8Gb 24-port Fibre Channel" modules require minimum firmware version 3.01 or 3.05 before upgrading to 3.08 or higher.'

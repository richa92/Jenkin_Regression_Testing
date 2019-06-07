from copy import deepcopy
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

appliance_cred = ['root', 'hpvse1']

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

users = [{"type": "UserAndPermissions", "userName": "Networkadmin", "fullName": "", "password": "Networkadmin",
          "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True, "permissions": [{"roleName": "Network administrator", "scopeUri": None}]},
         {"type": "UserAndPermissions", "userName": "Storageadmin", "fullName": "", "password": "Storageadmin",
          "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True, "permissions": [{"roleName": "Storage administrator", "scopeUri": None}]},
         {"type": "UserAndPermissions", "userName": "Backupadmin", "fullName": "", "password": "Backupadmin",
          "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True, "permissions": [{"roleName": "Backup administrator", "scopeUri": None}]},
         {"type": "UserAndPermissions", "userName": "Serveradmin", "fullName": "", "password": "Serveradmin",
          "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True, "permissions": [{"roleName": "Server administrator", "scopeUri": None}]},
         ]
usercred = [{'userName': 'Serveradmin', 'password': 'Serveradmin'},
            {'userName': 'Storageadmin', 'password': 'Storageadmin'},
            {'userName': 'Backupadmin', 'password': 'Backupadmin'}]

network_user = [{'userName': 'Networkadmin', 'password': 'Networkadmin'}]


ENC1 = 'enc2'
LE = 'enc2'
LI = 'enc2-LIG-COMP-OU'
server_bay_2 = '1'
key = 'If-Match'
value = '*'

CURDIR = "C:\checkout420\fusion\tests\wpst_crm\feature_tests\C7000\4692_Downgrade"

ilo_details = {'ilo_ip': '15.186.22.175', 'username': 'Administrator', 'password': 'password@123'}

SPP_bundle_111 = 'SPP2014090.2014_0827.10.iso'
SPP_bundle_301 = 'SPP2015100.2015_0921.6.iso'
SPP_bundle_305 = 'SPPgen9snap6_2016_0825_153.iso'
SPP_bundle_308 = 'SPP2017070.2017_0608.153.iso'
SPP_bundle_400 = 'Custom_SPP_4_0.iso'
SPP_bundle_410 = 'bp-2018-03-29-01.iso'
SPP_bundle_500 = 'Custom_5_x.iso'

fc_firmwareVersion_500 = '5.00'
fc_firmwareVersion_410 = '4.10'
fc_firmwareVersion_400 = '4.00'
fc_firmwareVersion_308 = '3.08'
fc_firmwareVersion_305 = '3.05'
fc_firmwareVersion_301 = '3.01'

fw_uri_301 = '/rest/firmware-drivers/SPP2015100_2015_0921_6'
fw_uri_305 = '/rest/firmware-drivers/SPPgen9snap6_2016_0825_153'
fw_uri_308 = '/rest/firmware-drivers/SPP2017070_2017_0608_153'
fw_uri_400 = '/rest/firmware-drivers/Custom_SPP_4_x'
fw_uri_410 = '/rest/firmware-drivers/bp-2018-03-29-01'
fw_uri_500 = '/rest/firmware-drivers/Custom_5_x'

FC_Hill = [{'type': 'fc-networkV4',
            'linkStabilityTime': 30,
            'autoLoginRedistribution': True,
            'name': 'fc1_Hill',
            'connectionTemplateUri': None,
            'managedSanUri': None,
            'fabricType': 'FabricAttach'},
           {'type': 'fc-networkV4',
               'linkStabilityTime': 30,
               'autoLoginRedistribution': True,
               'name': 'fc2_Hill',
               'connectionTemplateUri': None,
               'managedSanUri': None,
               'fabricType': 'FabricAttach'},
           {'type': 'fc-networkV4',
               'linkStabilityTime': 30,
               'autoLoginRedistribution': True,
               'name': 'fc3_Hill',
               'connectionTemplateUri': None,
               'managedSanUri': None,
               'fabricType': 'FabricAttach'},
           {'type': 'fc-networkV4',
               'linkStabilityTime': 30,
               'autoLoginRedistribution': True,
               'name': 'fc4_Hill',
               'connectionTemplateUri': None,
               'managedSanUri': None,
               'fabricType': 'FabricAttach'}]

Enet_Hill = {"purpose": "General",
             "name": "enet_hill",
             "smartLink": False,
             "privateNetwork": False,
             "connectionTemplateUri": None,
             "ethernetNetworkType": "Untagged",
             "type": "ethernet-networkV4"
             }

lig_uplink_config = {'UplinkSet_1': {'name': 'us_1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc1_Hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None, 'fcMode': 'TRUNK',
                                     'logicalPortConfigInfos': [{'bay': '5', 'enclosure': '1', 'port': '1', 'speed': 'Auto'},
                                                                {'bay': '5', 'enclosure': '1', 'port': '2', 'speed': 'Auto'},
                                                                {'bay': '5', 'enclosure': '1', 'port': '3', 'speed': 'Auto'},
                                                                {'bay': '5', 'enclosure': '1', 'port': '4', 'speed': 'Auto'},
                                                                {'bay': '5', 'enclosure': '1', 'port': '5', 'speed': 'Auto'},
                                                                {'bay': '5', 'enclosure': '1', 'port': '6', 'speed': 'Auto'},
                                                                {'bay': '5', 'enclosure': '1', 'port': '7', 'speed': 'Auto'},
                                                                {'bay': '5', 'enclosure': '1', 'port': '8', 'speed': 'Auto'}]},
                     'UplinkSet_2': {'name': 'us_2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc2_Hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None, 'fcMode': 'TRUNK',
                                     'logicalPortConfigInfos': [{'bay': '6', 'enclosure': '1', 'port': '1', 'speed': 'Auto'},
                                                                {'bay': '6', 'enclosure': '1', 'port': '2', 'speed': 'Auto'},
                                                                {'bay': '6', 'enclosure': '1', 'port': '3', 'speed': 'Auto'}]}}

lig_uplink_sets = {'UplinkSet_1': {'name': 'us_eth', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Untagged', 'networkUris': ['enet_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                   'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '1', 'port': 'X5', 'speed': 'Auto'}]}}

ligs = {'LIG_Hill':
        {'name': 'LIG-COMP-OU',
            'type': 'logical-interconnect-groupV6',
            'enclosureType': 'C7000',
            'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                        {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC 8Gb 24-Port FC Module'},
                                        {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC 8Gb 24-Port FC Module'},
                                        {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                        {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                        {'enclosure': 1, 'enclosureIndex': 1, 'bay': 8, 'type': 'HP VC FlexFabric-20/40 F8 Module'}],
            'uplinkSets': [lig_uplink_config['UplinkSet_1'].copy(), lig_uplink_config['UplinkSet_2'].copy(), lig_uplink_sets['UplinkSet_1'].copy()],
            'stackingMode': 'Enclosure',
            'ethernetSettings': None,
            'state': 'Active',
            'telemetryConfiguration': None,
            'snmpConfiguration': None,
            'qosConfiguration': None}
        }

enc_group = {
    'EG':
        {'name': 'EG',
         'ipRangeUris': [],
         'enclosureCount': 1,
         'powerMode': None,
         'ambientTemperatureMode': 'Standard',
         'interconnectBayMappings':
         [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:LIG_Hill'},
          {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG_Hill'},
          {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:LIG_Hill'},
          {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:LIG_Hill'},
          {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG_Hill'},
          {'interconnectBay': 8, 'logicalInterconnectGroupUri': 'LIG:LIG_Hill'}]}
}

encs = [{'hostname': '15.186.23.18', 'username': 'Administrator', 'password': 'compaq', 'enclosureGroupUri': 'EG:EG', 'force': 'true', 'licensingIntent': 'OneViewNoiLO'}]

encs_fwupdate = [{'hostname': '15.186.23.18', 'username': 'Administrator', 'password': 'compaq', 'enclosureGroupUri': 'EG:EG', 'force': False, 'licensingIntent': 'OneView', 'firmwareBaselineUri': fw_uri_500, 'forceInstallFirmware': True, 'updateFirmwareOn': 'EnclosureOnly'}]

leupdate_body = [{"op": "replace", "path": "/firmware", "value": {"firmwareBaselineUri": '', "forceInstallFirmware": True, "firmwareUpdateOn": "SharedInfrastructureOnly", "logicalInterconnectUpdateMode": "Parallel", "validateIfLIFirmwareUpdateIsNonDisruptive": False, "updateFirmwareOnUnmanagedInterconnect": False}}]

liupdate_body = {"sppUri": ' ', "command": "UPDATE", "force": True, "ethernetActivationType": "Parallel", "ethernetActivationDelay": "0", "fcActivationType": "Parallel", "fcActivationDelay": "0", "validationType": "None"}

liupdate_body1 = {"sppUri": ' ', "command": "UPDATE", "force": True, "ethernetActivationType": "Serial", "ethernetActivationDelay": "0", "fcActivationType": "Serial", "fcActivationDelay": "0", "validationType": "None"}

liupdate_body2 = {"sppUri": ' ', "command": "UPDATE", "force": True, "ethernetActivationType": "OddEven", "ethernetActivationDelay": "0", "fcActivationType": "Serial", "fcActivationDelay": "0", "validationType": "None"}

server_details = {'username': 'Administrator', 'password': 'hpvse1'}

diskspd_cmd_60s = "PowerShell.exe -ExecutionPolicy Bypass -File .\\test-60s.ps1"

linux_details = {"hostip": "15.186.25.25", "username": "root", "password": "password@123", "dir_location": "/root/pexpect/pexpect-u-2.5.1/",
                 "python_cmd": "python2.7"}

oa_details_1 = {'oa_ip': encs[0]['hostname'], "username": encs[0]["username"], "password": encs[0]["password"], "server_bay": '1'}

module_file_path = "C:\\checkout420\\fusion\\tests\\wpst_crm\\feature_tests\\C7000\\4692_Downgrade\\GetServerIPs.py"

diskspd_cmd1 = "C:\\Diskspd-v2.0.17\\amd64fre\\diskspd.exe -c50M -d10 -r -w70 -t9 -o9 -b20K -h -L D:\\multi5.dat >C:\\Ov_restartbefore1.dat"

diskspd_cmd = ['cmd /c "C:\Users\Administrator\Desktop\Diskspd\diskspd.exe -c50M -d60 -r -w70 -t9 -o9 -b10K -h -L D:\sample.dat >C:\sample1.dat"', 'cmd /c "C:\Users\Administrator\Desktop\Diskspd\diskspd.exe -c50M -d60 -r -w70 -t9 -o9 -b10K -h -L D:\sample.dat >C:\sample1.dat"']

windows_server_cred = {'userName': 'Administrator', 'password': 'password@123'}

INTERCONNECTS_HILL = ['enc2, interconnect 5', 'enc2, interconnect 6']

valDict_1 = {'recommendedActions': 'Update interconnect firmware using SPP containing Virtual Connect firmware version 3.08 or higher prior to downgrading the firmware version to 3.05 or lower.'}

valDict_user = {'status_code': 403,
                'errorCode': 'ACTION_FORBIDDEN_BY_ROLE'}

valDict_Action = {'recommendedActions': [u'Update logical interconnect firmware with SPP containing either Virtual Connect firmware version 4.41, 4.45, or 4.50 prior to upgrading to firmware version 4.60 or higher.']}

server_profiles = [{'type': 'ServerProfileV10', 'serverHardwareUri': ENC1 + ', bay 1',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'config1-group', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'Profile_server1', 'description': '', 'affinity': 'Bay',
                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'connectionSettings': {
                        'connections': [{'id': 1, 'name': '1', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': 'Auto', 'networkUri': 'FC:fc1_Hill', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpnType': 'UserDefined', 'wwpn': '10:00:a0:b9:cc:1c:08:51', 'wwnn': '20:00:a0:b9:cc:1c:08:51'},
                                        {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': 'Auto', 'networkUri': 'FC:fc2_Hill', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpnType': 'UserDefined', 'wwpn': '10:00:a0:b9:cc:1c:08:52', 'wwnn': '20:00:a0:b9:cc:1c:08:52'},
                                        {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:enet_hill', 'mac': None, 'wwpn': '', 'wwnn': ''},
                                        ]}}]

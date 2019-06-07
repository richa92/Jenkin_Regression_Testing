def make_range_list(vrange):
    rlist = []
    for x in xrange(vrange['start'], (vrange['end'] + 1)):
        rlist.append(vrange['prefix'] + str(x) + vrange['suffix'])
    return rlist

SSH_PASS = 'hpvse1'

FUSION_USERNAME = 'Administrator'    # Fusion Appliance Username
FUSION_PASSWORD = 'hpvse123'         # Fusion Appliance Password
FUSION_SSH_USERNAME = 'root'             # Fusion SSH Username
FUSION_SSH_PASSWORD = 'hpvse1'        # Fusion SSH Password


FUSION_PROMPT = '#'               # Fusion Appliance Prompt
FUSION_TIMEOUT = 180              # Timeout.  Move this out???
FUSION_NIC = 'bond0'            # Fusion Appliance Primary NIC
FUSION_NIC_SUFFIX = '%' + FUSION_NIC

SWITCH_USERNAME = 'admin'
SWITCH_PASSWORD = 'password'
SWITCH_PROMPT = '>'
SWITCH_TIMEOUT = 300

IC_SSH_USERNAME = 'root'
IC_TIMEOUT = 100
IC_PROMPT = '>'

Enclosure = 'CN750160YS'

APPLIANCE_IP = '15.186.9.20'
FUSION_IP = '15.186.9.20'

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

vcenter = {'server': '15.199.230.130', 'user': 'rbriggs', 'password': 'hpvse1'}

appliance = {'type': 'ApplianceNetworkConfiguration',
             'applianceNetworks':
                 [{'device': 'eth0',
                   'macAddress': None,
                   'interfaceName': 'VLAN 106',
                   'activeNode': '1',
                   'unconfigure': False,
                   'ipv4Type': 'DHCP',
                   'ipv6Type': 'UNCONFIGURE',
                   'hostname': 'portmon.usa.hp.com',
                   'confOneNode': True,
                   'domainName': 'usa.hp.com',
                   'aliasDisabled': True}]}

diskspd_cmd_60s = "PowerShell.exe -ExecutionPolicy Bypass -File .\\test-60s.ps1"

server_details = {'username': 'Administrator', 'password': 'password@123'}

linux_details = {"hostip": "15.186.21.149", "username": "root", "password": "password", "dir_location": "/root/pexpect/pexpect-u-2.5.1/",
                 "python_cmd": "python2.7"}

ilo_details = {'ilo_ip': '', 'username': 'Administrator', 'password': 'hpvse123'}
server_bay_3 = "3"


diskspd_cmd_5m = "PowerShell.exe -ExecutionPolicy Bypass -File .\\test-5m.ps1"
diskspd_cmd_10m = "PowerShell.exe -ExecutionPolicy Bypass -File .\\test-10m.ps1"
diskspd_cmd_20m = "PowerShell.exe -ExecutionPolicy Bypass -File .\\test-20m.ps1"
diskspd_cmd_1hr = "PowerShell.exe -ExecutionPolicy Bypass -File .\\test-1hr.ps1"
diskspd_cmd_2hr = "PowerShell.exe -ExecutionPolicy Bypass -File .\\test-2hr.ps1"
diskspd_cmd_4hr = "PowerShell.exe -ExecutionPolicy Bypass -File .\\test-4hr.ps1"
diskspd_cmd_6hr = "PowerShell.exe -ExecutionPolicy Bypass -File .\\test-6hr.ps1"

bay_electron = '3'
bay_quartz = '2'

ic_firmwareVersion_old = '1.03.01'
ic_firmwareVersion_new = '1.05.24'


old_SPP_bundle = 'SPP2016100.2016.1015.191.iso'

latest_SPP_bundle = 'SPP2017070.2017.0602.148.iso'


fw_uri_301 = '/rest/firmware-drivers/SPP2015100_2015_0921_6'

ambientTemperatureMode = 'Standard'


leupdate_body = [{"op": "replace",
                  "path": "/firmware",
                  "value": {"firmwareBaselineUri": ' ',
                            "forceInstallFirmware": False,
                            "firmwareUpdateOn": "SharedInfrastructureOnly",
                            "logicalInterconnectUpdateMode": "Parallel",
                            "validateIfLIFirmwareUpdateIsNonDisruptive": False,
                            "updateFirmwareOnUnmanagedInterconnect": False}
                  }]

liupdate_body = {"sppUri": ' ',
                 "command": "UPDATE",
                 "force": True,
                 "ethernetActivationType": "Parallel",
                 "ethernetActivationDelay": "0",
                 "fcActivationType": "Parallel",
                 "fcActivationDelay": "0",
                 "validationType": "None"}

eg_type = 'EnclosureGroupV7'

subnet = {'type': 'Subnet',
          'name': 'snet_20561',
          'gateway': '15.245.128.1',
          'networkId': '15.245.128.0',
          'subnetmask': '255.255.248.0',
          'dnsServers': [],
          'domain': 'testdom.com'}

ipv4range = {'type': 'Range',
             'startAddress': '15.245.132.121',
             'endAddress': '15.245.132.124',
             'name': 'test',
             'subnetUri': ' '}

timeandlocale = {'type': 'TimeAndLocale', 'dateTime': None, 'timezone': 'UTC', 'ntpServers': ['192.173.0.23'], 'locale': 'en_US.UTF-8'}

ranges = [{'name': 'FC-WWN', 'type': 'Range', 'category': 'id-range-VWWN', 'rangeCategory': 'CUSTOM', 'startAddress': '10:00:7E:9B:F9:0B:00:00', 'endAddress': '10:00:7E:9B:F9:0B:00:7F', 'enabled': True}]

ICM_MODEL = 'Virtual Connect SE 16Gb FC Module for Synergy'
ICM_MODEL_TAA = 'Virtual Connect SE 16Gb FC TAA Module for Synergy'

INTERCONNECTS = ['CN750160YS, interconnect 1', 'CN750160YS, interconnect 4']

LI_NAME = 'LE_1-LIG_1-1'

intervals = ['5', '15', '30', '60', '120']
portno = ['8', '9']

traffic_bays = ['1', '2']
ANALYZER_PORT = 3

Cmds = {'portshow 8', 'portshow 1'}
LE_SupportDump_Payload = {"encrypt": True, "errorCode": "MyDump16", "excludeApplianceDump": False}
icbays = ['1', '4']

del_uplinkset_20504 = 'UplinkSet_1'
ip_pool_static = ['15.245.132.121', '15.245.132.122', '15.245.132.123', '15.245.132.124']

Mode = 'PRESERVE_NETWORK'
admin_default_paswd = "admin"

US_name = ['UplinkSet_1', 'UplinkSet_2']


Linked_Uplink_port = ['Q1:1', '1', '3']
Linked_Uplink_port_id = ['21', '13', '15']
Linked_Downlink_port = ['d1', 'd2', 'd3']

users = []

fcnets = [{"type": "fc-networkV4",
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
           }
          ]

fc_20635 = [{"type": "fc-networkV4",
             "name": "FC_20635",
             "fabricType": "FabricAttach",
             "linkStabilityTime": 30,
             "autoLoginRedistribution": True
             }
            ]

fcnets_add = [{"type": "fc-networkV4",
               "name": "FC_5",
               "fabricType": "FabricAttach",
               "linkStabilityTime": 30,
               "autoLoginRedistribution": True
               },
              {"type": "fc-networkV4",
               "name": "FC_6",
               "fabricType": "FabricAttach",
               "linkStabilityTime": 30,
               "autoLoginRedistribution": True
               },
              {"type": "fc-networkV4",
               "name": "FC_7",
               "fabricType": "FabricAttach",
               "linkStabilityTime": 30,
               "autoLoginRedistribution": True
               },
              {"type": "fc-networkV4",
               "name": "FC_8",
               "fabricType": "FabricAttach",
               "linkStabilityTime": 30,
               "autoLoginRedistribution": True
               },
              {"type": "fc-networkV4",
               "name": "FC_9",
               "fabricType": "FabricAttach",
               "linkStabilityTime": 30,
               "autoLoginRedistribution": True
               },
              {"type": "fc-networkV4",
               "name": "FC_10",
               "fabricType": "FabricAttach",
               "linkStabilityTime": 30,
               "autoLoginRedistribution": True
               },
              {"type": "fc-networkV4",
               "name": "FC_11",
               "fabricType": "FabricAttach",
               "linkStabilityTime": 30,
               "autoLoginRedistribution": True
               },
              {"type": "fc-networkV4",
               "name": "FC_12",
               "fabricType": "FabricAttach",
               "linkStabilityTime": 30,
               "autoLoginRedistribution": True
               },
              {"type": "fc-networkV4",
               "name": "FC_13",
               "fabricType": "FabricAttach",
               "linkStabilityTime": 30,
               "autoLoginRedistribution": True
               }
              ]


uplink_sets = {'UplinkSet_1': {'name': 'UplinkSet_1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_1'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                               'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': 'Q1:1', 'speed': 'Auto'}]},
               'UplinkSet_2': {'name': 'UplinkSet_2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_2'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                               'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '-1', 'port': '1', 'speed': 'Speed16G'}]},
               'UplinkSet_3': {'name': 'UplinkSet_3', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_3'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                               'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': '2', 'speed': 'Speed8G'}]},
               'UplinkSet_4': {'name': 'UplinkSet_4', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_4'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                               'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '-1', 'port': '2', 'speed': 'Speed4G'}]},
               'UplinkSet_20464': {'name': 'UplinkSet_4', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_2'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                   'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '-1', 'port': '1', 'speed': 'Speed4G'}]},
               'UplinkSet1_20580': {'name': 'UplinkSet_1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_1'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                    'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': 'Q1:1', 'speed': 'Speed4G'}]},
               'UplinkSet2_20580': {'name': 'UplinkSet_2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_2'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                    'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '-1', 'port': '1', 'speed': 'Speed4G'}]},
               'UplinkSet1_20581': {'name': 'UplinkSet_1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_1'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                    'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': 'Q1:1', 'speed': 'Speed8G'}]},
               'UplinkSet2_20581': {'name': 'UplinkSet_2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_2'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                    'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '-1', 'port': '1', 'speed': 'Speed8G'}]},
               'UplinkSet_20970_1': {'name': 'UplinkSet_20970_1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_1'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                     'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': 'Q1:1', 'speed': 'Speed8G'}]},
               'UplinkSet_20970_2': {'name': 'UplinkSet_20970_2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_2'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                     'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '-1', 'port': '1', 'speed': 'Speed4G'}]},
               'UplinkSet_20635': {'name': 'UplinkSet_1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_20635'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                   'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': 'Q1:1', 'speed': 'Speed4G'}]},
               'UplinkSet_failover': {'name': 'UplinkSet_1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_1'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                      'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': 'Q1:1', 'speed': 'Auto'},
                                                                 {'bay': '1', 'enclosure': '-1', 'port': 'Q1:2', 'speed': 'Auto'}]}
               }

uplink_sets_full = {'UplinkSet_1': {'name': 'UplinkSet_1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_1'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                    'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': '1', 'speed': 'Auto'}]},
                    'UplinkSet_2': {'name': 'UplinkSet_2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_2'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                    'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': '2', 'speed': 'Speed4G'}]},
                    'UplinkSet_3': {'name': 'UplinkSet_3', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_3'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                    'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': '3', 'speed': 'Speed8G'}]},
                    'UplinkSet_4': {'name': 'UplinkSet_4', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_4'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                    'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': '4', 'speed': 'Speed16G'}]},
                    'UplinkSet_5': {'name': 'UplinkSet_5', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_5'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                    'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': '5', 'speed': 'Auto'}]},
                    'UplinkSet_6': {'name': 'UplinkSet_6', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_6'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                    'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': '6', 'speed': 'Speed4G'}]},
                    'UplinkSet_7': {'name': 'UplinkSet_7', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_7'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                    'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': '7', 'speed': 'Speed8G'}]},
                    'UplinkSet_8': {'name': 'UplinkSet_8', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_8'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                    'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': '8', 'speed': 'Speed16G'}]},
                    'UplinkSet_9': {'name': 'UplinkSet_9', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_9'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                    'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': 'Q1.1', 'speed': 'Auto'}]},
                    'UplinkSet_10': {'name': 'UplinkSet_10', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_10'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                     'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': 'Q2.1', 'speed': 'Speed4G'}]},
                    'UplinkSet_11': {'name': 'UplinkSet_11', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_11'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                     'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': 'Q3.1', 'speed': 'Speed8G'}]},
                    'UplinkSet_12': {'name': 'UplinkSet_12', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_12'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                     'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': 'Q4.1', 'speed': 'Speed16G'}]},
                    'UplinkSet_13': {'name': 'UplinkSet_13', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_13'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                     'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': 'Q1.2', 'speed': 'Auto'}]}
                    }
lig_US_20532 = {'UplinkSet_1': {'name': 'UplinkSet_1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_1'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': '1', 'speed': 'Auto'},
                                                           {'bay': '1', 'enclosure': '-1', 'port': '2', 'speed': 'Auto'},
                                                           {'bay': '1', 'enclosure': '-1', 'port': '3', 'speed': 'Auto'},
                                                           {'bay': '1', 'enclosure': '-1', 'port': '4', 'speed': 'Auto'},
                                                           {'bay': '1', 'enclosure': '-1', 'port': '5', 'speed': 'Auto'},
                                                           {'bay': '1', 'enclosure': '-1', 'port': '6', 'speed': 'Auto'},
                                                           {'bay': '1', 'enclosure': '-1', 'port': '7', 'speed': 'Auto'},
                                                           {'bay': '1', 'enclosure': '-1', 'port': '8', 'speed': 'Auto'},
                                                           {'bay': '1', 'enclosure': '-1', 'port': 'Q1.1', 'speed': 'Auto'},
                                                           {'bay': '1', 'enclosure': '-1', 'port': 'Q2.1', 'speed': 'Auto'},
                                                           {'bay': '1', 'enclosure': '-1', 'port': 'Q3.1', 'speed': 'Auto'},
                                                           {'bay': '1', 'enclosure': '-1', 'port': 'Q4.1', 'speed': 'Auto'}]},
                'UplinkSet_2': {'name': 'UplinkSet_1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_1'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '-1', 'port': '1', 'speed': 'Auto'},
                                                           {'bay': '4', 'enclosure': '-1', 'port': '2', 'speed': 'Auto'},
                                                           {'bay': '4', 'enclosure': '-1', 'port': '3', 'speed': 'Auto'},
                                                           {'bay': '4', 'enclosure': '-1', 'port': '4', 'speed': 'Auto'},
                                                           {'bay': '4', 'enclosure': '-1', 'port': '5', 'speed': 'Auto'},
                                                           {'bay': '4', 'enclosure': '-1', 'port': '6', 'speed': 'Auto'},
                                                           {'bay': '4', 'enclosure': '-1', 'port': '7', 'speed': 'Auto'},
                                                           {'bay': '4', 'enclosure': '-1', 'port': '8', 'speed': 'Auto'},
                                                           {'bay': '4', 'enclosure': '-1', 'port': 'Q1.1', 'speed': 'Auto'},
                                                           {'bay': '4', 'enclosure': '-1', 'port': 'Q2.1', 'speed': 'Auto'},
                                                           {'bay': '4', 'enclosure': '-1', 'port': 'Q3.1', 'speed': 'Auto'},
                                                           {'bay': '4', 'enclosure': '-1', 'port': 'Q4.1', 'speed': 'Auto'}]}
                }

lig_US1_20532 = {'UplinkSet_1': {'name': 'UplinkSet_1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_1'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                 'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': '1', 'speed': 'Auto'},
                                                            {'bay': '1', 'enclosure': '-1', 'port': '2', 'speed': 'Auto'},
                                                            {'bay': '1', 'enclosure': '-1', 'port': '3', 'speed': 'Auto'},
                                                            {'bay': '1', 'enclosure': '-1', 'port': '4', 'speed': 'Auto'},
                                                            {'bay': '1', 'enclosure': '-1', 'port': '5', 'speed': 'Auto'},
                                                            {'bay': '1', 'enclosure': '-1', 'port': '6', 'speed': 'Auto'},
                                                            {'bay': '1', 'enclosure': '-1', 'port': '7', 'speed': 'Auto'},
                                                            {'bay': '1', 'enclosure': '-1', 'port': '8', 'speed': 'Auto'},
                                                            {'bay': '1', 'enclosure': '-1', 'port': 'Q1.1', 'speed': 'Auto'},
                                                            {'bay': '1', 'enclosure': '-1', 'port': 'Q2.1', 'speed': 'Auto'},
                                                            {'bay': '1', 'enclosure': '-1', 'port': 'Q3.1', 'speed': 'Auto'},
                                                            {'bay': '1', 'enclosure': '-1', 'port': 'Q4.1', 'speed': 'Auto'},
                                                            {'bay': '1', 'enclosure': '-1', 'port': 'Q1.2', 'speed': 'Auto'}]},
                 'UplinkSet_2': {'name': 'UplinkSet_1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_1'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                 'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '-1', 'port': '1', 'speed': 'Auto'},
                                                            {'bay': '4', 'enclosure': '-1', 'port': '2', 'speed': 'Auto'},
                                                            {'bay': '4', 'enclosure': '-1', 'port': '3', 'speed': 'Auto'},
                                                            {'bay': '4', 'enclosure': '-1', 'port': '4', 'speed': 'Auto'},
                                                            {'bay': '4', 'enclosure': '-1', 'port': '5', 'speed': 'Auto'},
                                                            {'bay': '4', 'enclosure': '-1', 'port': '6', 'speed': 'Auto'},
                                                            {'bay': '4', 'enclosure': '-1', 'port': '7', 'speed': 'Auto'},
                                                            {'bay': '4', 'enclosure': '-1', 'port': '8', 'speed': 'Auto'},
                                                            {'bay': '4', 'enclosure': '-1', 'port': 'Q1.1', 'speed': 'Auto'},
                                                            {'bay': '4', 'enclosure': '-1', 'port': 'Q2.1', 'speed': 'Auto'},
                                                            {'bay': '4', 'enclosure': '-1', 'port': 'Q3.1', 'speed': 'Auto'},
                                                            {'bay': '4', 'enclosure': '-1', 'port': 'Q4.1', 'speed': 'Auto'},
                                                            {'bay': '4', 'enclosure': '-1', 'port': 'Q1.2', 'speed': 'Auto'}]}
                 }
lig_US_20575 = {'UplinkSet_1': {'name': 'UplinkSet_1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_1'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': '1', 'speed': 'Auto'}]},
                'UplinkSet_2': {'name': 'UplinkSet_2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_2'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': '2', 'speed': 'Auto'}]},
                'UplinkSet_3': {'name': 'UplinkSet_3', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_3'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': '3', 'speed': 'Auto'}]},
                'UplinkSet_4': {'name': 'UplinkSet_4', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_4'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': '4', 'speed': 'Auto'}]},
                'UplinkSet_5': {'name': 'UplinkSet_5', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_5'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': '5', 'speed': 'Auto'}]},
                'UplinkSet_6': {'name': 'UplinkSet_6', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_6'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': '6', 'speed': 'Auto'}]},
                'UplinkSet_7': {'name': 'UplinkSet_7', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_7'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': '7', 'speed': 'Auto'}]},
                'UplinkSet_8': {'name': 'UplinkSet_8', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_8'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': '8', 'speed': 'Auto'}]},
                'UplinkSet_9': {'name': 'UplinkSet_9', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_9'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': 'Q1.1', 'speed': 'Auto'}]},
                'UplinkSet_10': {'name': 'UplinkSet_10', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_10'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                 'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': 'Q2.1', 'speed': 'Auto'}]},
                'UplinkSet_11': {'name': 'UplinkSet_11', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_11'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                 'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': 'Q3.1', 'speed': 'Auto'}]},
                'UplinkSet_12': {'name': 'UplinkSet_12', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_12'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                 'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': 'Q4.1', 'speed': 'Auto'}]},
                'UplinkSet_13': {'name': 'UplinkSet_13', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_13'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                 'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': 'Q1.2', 'speed': 'Auto'}]},
                'UplinkSet_14': {'name': 'UplinkSet_1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_1'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                 'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '-1', 'port': '1', 'speed': 'Auto'}]},
                'UplinkSet_15': {'name': 'UplinkSet_2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_2'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                 'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '-1', 'port': '2', 'speed': 'Auto'}]},
                'UplinkSet_16': {'name': 'UplinkSet_3', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_3'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                 'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '-1', 'port': '3', 'speed': 'Auto'}]},
                'UplinkSet_17': {'name': 'UplinkSet_4', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_4'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                 'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '-1', 'port': '4', 'speed': 'Auto'}]},
                'UplinkSet_18': {'name': 'UplinkSet_5', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_5'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                 'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '-1', 'port': '5', 'speed': 'Auto'}]},
                'UplinkSet_19': {'name': 'UplinkSet_6', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_6'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                 'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '-1', 'port': '6', 'speed': 'Auto'}]},
                'UplinkSet_20': {'name': 'UplinkSet_7', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_7'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                 'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '-1', 'port': '7', 'speed': 'Auto'}]},
                'UplinkSet_21': {'name': 'UplinkSet_8', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_8'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                 'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '-1', 'port': '8', 'speed': 'Auto'}]},
                'UplinkSet_22': {'name': 'UplinkSet_9', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_9'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                 'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '-1', 'port': 'Q1.1', 'speed': 'Auto'}]},
                'UplinkSet_23': {'name': 'UplinkSet_10', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_10'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                 'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '-1', 'port': 'Q2.1', 'speed': 'Auto'}]},
                'UplinkSet_24': {'name': 'UplinkSet_11', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_11'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                 'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '-1', 'port': 'Q3.1', 'speed': 'Auto'}]},
                'UplinkSet_25': {'name': 'UplinkSet_12', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_12'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                 'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '-1', 'port': 'Q4.1', 'speed': 'Auto'}]},
                'UplinkSet_26': {'name': 'UplinkSet_13', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_13'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                 'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '-1', 'port': 'Q1.2', 'speed': 'Auto'}]}
                }

LIG1 = 'LIG_1'

ligs = {'lig1':
        {'name': 'LIG_1',
         'type': 'logical-interconnect-groupV400',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': [{'bay': 1, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1},
                                     {'bay': 4, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1}
                                     ],
         'enclosureIndexes': [-1],
         'interconnectBaySet': 1,
         'redundancyType': 'Redundant',
         'uplinkSets': [uplink_sets['UplinkSet_1'].copy(), uplink_sets['UplinkSet_2'].copy()],
         'internalNetworkUris': [],
         'stackingMode': 'Enclosure',
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
        'lig20968':
        {'name': 'LIG_1',
         'type': 'logical-interconnect-groupV400',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': [{'bay': 1, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1},
                                     {'bay': 4, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1}
                                     ],
         'enclosureIndexes': [-1],
         'interconnectBaySet': 1,
         'redundancyType': 'Redundant',
         'uplinkSets': [uplink_sets['UplinkSet_1'].copy(), uplink_sets['UplinkSet_2'].copy(), uplink_sets['UplinkSet_3'].copy()],
         'internalNetworkUris': [],
         'stackingMode': 'Enclosure',
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
        'lig20464':
        {'name': 'LIG_1',
         'type': 'logical-interconnect-groupV400',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': [{'bay': 1, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1},
                                     {'bay': 4, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1}
                                     ],
         'enclosureIndexes': [-1],
         'interconnectBaySet': 1,
         'redundancyType': 'Redundant',
         'uplinkSets': [uplink_sets['UplinkSet_1'].copy(), uplink_sets['UplinkSet_20464'].copy()],
         'internalNetworkUris': [],
         'stackingMode': 'Enclosure',
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
        'lig20467':
        {'name': 'LIG_1',
         'type': 'logical-interconnect-groupV400',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': [{'bay': 1, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1},
                                     {'bay': 4, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1}
                                     ],
         'enclosureIndexes': [-1],
         'interconnectBaySet': 1,
         'redundancyType': 'Redundant',
         'uplinkSets': [uplink_sets['UplinkSet_1'].copy(), uplink_sets['UplinkSet_2'].copy()],
         'internalNetworkUris': [],
         'stackingMode': 'Enclosure',
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
        'lig20563':
        {'name': 'LIG_1',
         'type': 'logical-interconnect-groupV400',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': [{'bay': 1, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1},
                                     {'bay': 4, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1}
                                     ],
         'enclosureIndexes': [-1],
         'interconnectBaySet': 1,
         'redundancyType': 'Redundant',
         'uplinkSets': [uplink_sets['UplinkSet_1'].copy(), uplink_sets['UplinkSet_2'].copy(), uplink_sets['UplinkSet_3'].copy()],
         'internalNetworkUris': [],
         'stackingMode': 'Enclosure',
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
        'lig20580':
        {'name': 'LIG_1',
         'type': 'logical-interconnect-groupV400',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': [{'bay': 1, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1},
                                     {'bay': 4, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1}
                                     ],
         'enclosureIndexes': [-1],
         'interconnectBaySet': 1,
         'redundancyType': 'Redundant',
         'uplinkSets': [uplink_sets['UplinkSet1_20580'].copy(), uplink_sets['UplinkSet2_20580'].copy()],
         'internalNetworkUris': [],
         'stackingMode': 'Enclosure',
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
        'lig20581':
        {'name': 'LIG_1',
         'type': 'logical-interconnect-groupV400',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': [{'bay': 1, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1},
                                     {'bay': 4, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1}
                                     ],
         'enclosureIndexes': [-1],
         'interconnectBaySet': 1,
         'redundancyType': 'Redundant',
         'uplinkSets': [uplink_sets['UplinkSet1_20581'].copy(), uplink_sets['UplinkSet2_20581'].copy()],
         'internalNetworkUris': [],
         'stackingMode': 'Enclosure',
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
        'lig20540_12':
        {'name': 'LIG_20540',
         'type': 'logical-interconnect-groupV400',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': [{'bay': 1, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1},
                                     {'bay': 4, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1}
                                     ],
         'enclosureIndexes': [-1],
         'interconnectBaySet': 1,
         'redundancyType': 'Redundant',
         'uplinkSets': [uplink_sets_full['UplinkSet_1'].copy(), uplink_sets_full['UplinkSet_2'].copy(), uplink_sets_full['UplinkSet_3'].copy(),
                        uplink_sets_full['UplinkSet_4'].copy(), uplink_sets_full['UplinkSet_5'].copy(), uplink_sets_full['UplinkSet_6'].copy(),
                        uplink_sets_full['UplinkSet_7'].copy(), uplink_sets_full['UplinkSet_8'].copy(), uplink_sets_full['UplinkSet_9'].copy(),
                        uplink_sets_full['UplinkSet_10'].copy(), uplink_sets_full['UplinkSet_11'].copy(), uplink_sets_full['UplinkSet_12'].copy()],
         'internalNetworkUris': [],
         'stackingMode': 'Enclosure',
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
        'lig20540_13':
        {'name': 'LIG_20540',
         'type': 'logical-interconnect-groupV400',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': [{'bay': 1, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1},
                                     {'bay': 4, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1}
                                     ],
         'enclosureIndexes': [-1],
         'interconnectBaySet': 1,
         'redundancyType': 'Redundant',
         'uplinkSets': [uplink_sets_full['UplinkSet_1'].copy(), uplink_sets_full['UplinkSet_2'].copy(), uplink_sets_full['UplinkSet_3'].copy(),
                        uplink_sets_full['UplinkSet_4'].copy(), uplink_sets_full['UplinkSet_5'].copy(), uplink_sets_full['UplinkSet_6'].copy(),
                        uplink_sets_full['UplinkSet_7'].copy(), uplink_sets_full['UplinkSet_8'].copy(), uplink_sets_full['UplinkSet_9'].copy(),
                        uplink_sets_full['UplinkSet_10'].copy(), uplink_sets_full['UplinkSet_11'].copy(), uplink_sets_full['UplinkSet_12'].copy(),
                        uplink_sets_full['UplinkSet_13'].copy()],
         'internalNetworkUris': [],
         'stackingMode': 'Enclosure',
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
        'lig20983_2':
        {'name': 'LIG_A_side',
         'type': 'logical-interconnect-groupV400',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': [{'bay': 1, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1}],
         'enclosureIndexes': [-1],
         'interconnectBaySet': 1,
         'redundancyType': 'NonRedundantASide',
         'uplinkSets': [uplink_sets['UplinkSet_1'].copy(), uplink_sets['UplinkSet_3'].copy()],
         'internalNetworkUris': [],
         'stackingMode': 'Enclosure',
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
        'lig20983_3':
        {'name': 'LIG_B_side',
         'type': 'logical-interconnect-groupV400',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': [{'bay': 4, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1}],
         'enclosureIndexes': [-1],
         'interconnectBaySet': 1,
         'redundancyType': 'NonRedundantBSide',
         'uplinkSets': [uplink_sets['UplinkSet_2'].copy(), uplink_sets['UplinkSet_4'].copy()],
         'internalNetworkUris': [],
         'stackingMode': 'Enclosure',
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
        'lig20970':
        {'name': 'LIG_1',
         'type': 'logical-interconnect-groupV400',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': [{'bay': 1, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1},
                                     {'bay': 4, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1}
                                     ],
         'enclosureIndexes': [-1],
         'interconnectBaySet': 1,
         'redundancyType': 'Redundant',
         'uplinkSets': [uplink_sets['UplinkSet_20970_1'].copy(), uplink_sets['UplinkSet_20970_2'].copy()],
         'internalNetworkUris': [],
         'stackingMode': 'Enclosure',
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
        'lig20635':
        {'name': 'LIG_1',
         'type': 'logical-interconnect-groupV400',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': [{'bay': 1, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1},
                                     {'bay': 4, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1}
                                     ],
         'enclosureIndexes': [-1],
         'interconnectBaySet': 1,
         'redundancyType': 'Redundant',
         'uplinkSets': [uplink_sets['UplinkSet_20635'].copy(), uplink_sets['UplinkSet_2'].copy()],
         'internalNetworkUris': [],
         'stackingMode': 'Enclosure',
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
        'lig_failover':
        {'name': 'LIG_1',
         'type': 'logical-interconnect-groupV400',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': [{'bay': 1, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1},
                                     {'bay': 4, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1}
                                     ],
         'enclosureIndexes': [-1],
         'interconnectBaySet': 1,
         'redundancyType': 'Redundant',
         'uplinkSets': [uplink_sets['UplinkSet_failover'].copy(), uplink_sets['UplinkSet_2'].copy()],
         'internalNetworkUris': [],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': {'type': 'snmp-configuration',
                               'readCommunity': 'public',
                               'systemContact': '',
                               'enabled': 'true',
                               'category': 'snmp-configuration'
                               }
         }
        }

lig_20532_12 = {'lig20532':
                {'name': 'LIG_20532',
                 'type': 'logical-interconnect-groupV400',
                 'enclosureType': 'SY12000',
                 'interconnectMapTemplate': [{'bay': 1, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1},
                                             {'bay': 4, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1}
                                             ],
                 'enclosureIndexes': [-1],
                 'interconnectBaySet': 1,
                 'redundancyType': 'Redundant',
                 'uplinkSets': [lig_US_20532['UplinkSet_1'].copy()],
                 'internalNetworkUris': [],
                 'stackingMode': 'Enclosure',
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
                'lig1_20532':
                {'name': 'LIG1_20532',
                 'type': 'logical-interconnect-groupV400',
                 'enclosureType': 'SY12000',
                 'interconnectMapTemplate': [{'bay': 1, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1},
                                             {'bay': 4, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1}
                                             ],
                 'enclosureIndexes': [-1],
                 'interconnectBaySet': 1,
                 'redundancyType': 'Redundant',
                 'uplinkSets': [lig_US_20532['UplinkSet_2'].copy()],
                 'internalNetworkUris': [],
                 'stackingMode': 'Enclosure',
                 'ethernetSettings': None,
                 'state': 'Active',
                 'telemetryConfiguration': None,
                 'snmpConfiguration': {'type': 'snmp-configuration',
                                       'readCommunity': 'public',
                                       'systemContact': '',
                                       'enabled': 'true',
                                       'category': 'snmp-configuration'
                                       }
                 }
                }

lig_20532_13 = {'lig20532':
                {'name': 'LIG_20532',
                 'type': 'logical-interconnect-groupV400',
                 'enclosureType': 'SY12000',
                 'interconnectMapTemplate': [{'bay': 1, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1},
                                             {'bay': 4, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1}
                                             ],
                 'enclosureIndexes': [-1],
                 'interconnectBaySet': 1,
                 'redundancyType': 'Redundant',
                 'uplinkSets': [lig_US1_20532['UplinkSet_1'].copy()],
                 'internalNetworkUris': [],
                 'stackingMode': 'Enclosure',
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
                'lig1_20532':
                {'name': 'LIG1_20532',
                 'type': 'logical-interconnect-groupV400',
                 'enclosureType': 'SY12000',
                 'interconnectMapTemplate': [{'bay': 1, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1},
                                             {'bay': 4, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1}
                                             ],
                 'enclosureIndexes': [-1],
                 'interconnectBaySet': 1,
                 'redundancyType': 'Redundant',
                 'uplinkSets': [lig_US1_20532['UplinkSet_2'].copy()],
                 'internalNetworkUris': [],
                 'stackingMode': 'Enclosure',
                 'ethernetSettings': None,
                 'state': 'Active',
                 'telemetryConfiguration': None,
                 'snmpConfiguration': {'type': 'snmp-configuration',
                                       'readCommunity': 'public',
                                       'systemContact': '',
                                       'enabled': 'true',
                                       'category': 'snmp-configuration'
                                       }
                 }
                }

lig_20575_12 = {'lig20575':
                {'name': 'LIG_20575',
                 'type': 'logical-interconnect-groupV400',
                 'enclosureType': 'SY12000',
                 'interconnectMapTemplate': [{'bay': 1, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1}],
                 'enclosureIndexes': [-1],
                 'interconnectBaySet': 1,
                 'redundancyType': 'NonRedundantASide',
                 'uplinkSets': [lig_US_20575['UplinkSet_1'].copy(), lig_US_20575['UplinkSet_2'].copy(), lig_US_20575['UplinkSet_3'].copy(),
                                lig_US_20575['UplinkSet_4'].copy(), lig_US_20575['UplinkSet_5'].copy(), lig_US_20575['UplinkSet_6'].copy(),
                                lig_US_20575['UplinkSet_7'].copy(), lig_US_20575['UplinkSet_8'].copy(), lig_US_20575['UplinkSet_9'].copy(),
                                lig_US_20575['UplinkSet_10'].copy(), lig_US_20575['UplinkSet_11'].copy(), lig_US_20575['UplinkSet_12'].copy()],
                 'internalNetworkUris': [],
                 'stackingMode': 'Enclosure',
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
                'lig1_20575':
                {'name': 'LIG1_20575',
                 'type': 'logical-interconnect-groupV400',
                 'enclosureType': 'SY12000',
                 'interconnectMapTemplate': [{'bay': 4, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1}],
                 'enclosureIndexes': [-1],
                 'interconnectBaySet': 1,
                 'redundancyType': 'NonRedundantBSide',
                 'uplinkSets': [lig_US_20575['UplinkSet_14'].copy(), lig_US_20575['UplinkSet_15'].copy(), lig_US_20575['UplinkSet_16'].copy(),
                                lig_US_20575['UplinkSet_17'].copy(), lig_US_20575['UplinkSet_18'].copy(), lig_US_20575['UplinkSet_19'].copy(),
                                lig_US_20575['UplinkSet_20'].copy(), lig_US_20575['UplinkSet_21'].copy(), lig_US_20575['UplinkSet_22'].copy(),
                                lig_US_20575['UplinkSet_23'].copy(), lig_US_20575['UplinkSet_24'].copy(), lig_US_20575['UplinkSet_25'].copy()],
                 'internalNetworkUris': [],
                 'stackingMode': 'Enclosure',
                 'ethernetSettings': None,
                 'state': 'Active',
                 'telemetryConfiguration': None,
                 'snmpConfiguration': {'type': 'snmp-configuration',
                                       'readCommunity': 'public',
                                       'systemContact': '',
                                       'enabled': 'true',
                                       'category': 'snmp-configuration'
                                       }
                 }
                }

lig_20575_13 = {'lig20575':
                {'name': 'LIG_20575',
                 'type': 'logical-interconnect-groupV400',
                 'enclosureType': 'SY12000',
                 'interconnectMapTemplate': [{'bay': 1, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1}],
                 'enclosureIndexes': [-1],
                 'interconnectBaySet': 1,
                 'redundancyType': 'NonRedundantASide',
                 'uplinkSets': [lig_US_20575['UplinkSet_1'].copy(), lig_US_20575['UplinkSet_2'].copy(), lig_US_20575['UplinkSet_3'].copy(),
                                lig_US_20575['UplinkSet_4'].copy(), lig_US_20575['UplinkSet_5'].copy(), lig_US_20575['UplinkSet_6'].copy(),
                                lig_US_20575['UplinkSet_7'].copy(), lig_US_20575['UplinkSet_8'].copy(), lig_US_20575['UplinkSet_9'].copy(),
                                lig_US_20575['UplinkSet_10'].copy(), lig_US_20575['UplinkSet_11'].copy(), lig_US_20575['UplinkSet_12'].copy(),
                                lig_US_20575['UplinkSet_13'].copy()],
                 'internalNetworkUris': [],
                 'stackingMode': 'Enclosure',
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
                'lig1_20575':
                {'name': 'LIG1_20575',
                 'type': 'logical-interconnect-groupV400',
                 'enclosureType': 'SY12000',
                 'interconnectMapTemplate': [{'bay': 4, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1}],
                 'enclosureIndexes': [-1],
                 'interconnectBaySet': 1,
                 'redundancyType': 'NonRedundantBSide',
                 'uplinkSets': [lig_US_20575['UplinkSet_14'].copy(), lig_US_20575['UplinkSet_15'].copy(), lig_US_20575['UplinkSet_16'].copy(),
                                lig_US_20575['UplinkSet_17'].copy(), lig_US_20575['UplinkSet_18'].copy(), lig_US_20575['UplinkSet_19'].copy(),
                                lig_US_20575['UplinkSet_20'].copy(), lig_US_20575['UplinkSet_21'].copy(), lig_US_20575['UplinkSet_22'].copy(),
                                lig_US_20575['UplinkSet_23'].copy(), lig_US_20575['UplinkSet_24'].copy(), lig_US_20575['UplinkSet_25'].copy(),
                                lig_US_20575['UplinkSet_26'].copy()],
                 'internalNetworkUris': [],
                 'stackingMode': 'Enclosure',
                 'ethernetSettings': None,
                 'state': 'Active',
                 'telemetryConfiguration': None,
                 'snmpConfiguration': {'type': 'snmp-configuration',
                                       'readCommunity': 'public',
                                       'systemContact': '',
                                       'enabled': 'true',
                                       'category': 'snmp-configuration'
                                       }
                 }
                }


ENC1 = 'CN750160YS'

LI = 'LE_1-LIG_1-1'

EG1 = 'EG_1'

interconnectBayMappingCount = 1
stackingMode = 'Enclosure'
enclosureTypeUri = '/rest/enclosure-types/SY12000'

enc_groups = {'enc_group1':
              {'name': 'EG_1',
               'enclosureCount': 1,
               'interconnectBayMappings':
               [{'interconnectBay': 1, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': 'LIG:LIG_1'},
                {'interconnectBay': 4, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': 'LIG:LIG_1'}
                ],
               'ipAddressingMode': 'External',
               'ipRangeUris': [],
               'powerMode': 'RedundantPowerFeed'
               },
              'enc_group_20983_1':
              {'name': 'EG_1',
               'enclosureCount': 1,
               'interconnectBayMappings':
               [{'interconnectBay': 1, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': 'LIG:LIG_A_side'},
                {'interconnectBay': 4, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': 'LIG:LIG_B_side'}
                ],
               'ipAddressingMode': 'External',
               'ipRangeUris': [],
               'powerMode': 'RedundantPowerFeed'
               },
              'enc_group_20983':
              {'name': 'EG_1',
               'enclosureCount': 1,
               'interconnectBayMappings':
               [{'interconnectBay': 1, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': 'LIG:LIG_1'},
                {'interconnectBay': 4, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': 'LIG:LIG_1'}
                ],
               'ipAddressingMode': 'External',
               'ipRangeUris': [],
               'powerMode': 'RedundantPowerFeed'
               },
              'enc_group_20968':
              {'name': 'EG_1',
               'enclosureCount': 1,
               'interconnectBayMappings':
               [{'interconnectBay': 1, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': 'LIG:LIG_1'},
                {'interconnectBay': 4, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': 'LIG:LIG_1'}
                ],
               'ipAddressingMode': 'External',
               'ipRangeUris': [],
               'powerMode': 'RedundantPowerFeed'
               },
              'enc_group_20561_dhcp':
              {'name': 'EG_1',
               'enclosureCount': 1,
               'interconnectBayMappings':
               [{'interconnectBay': 1, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': 'LIG:LIG_1'},
                {'interconnectBay': 4, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': 'LIG:LIG_1'}
                ],
               'ipAddressingMode': 'DHCP',
               'ipRangeUris': [],
               'powerMode': 'RedundantPowerFeed'
               }
              }

enc_group_20561_static = [{'name': 'EG_1',
                           'enclosureCount': 1,
                           'interconnectBayMappings':
                           [{'interconnectBay': 1, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': 'LIG:LIG_1'},
                            {'interconnectBay': 4, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': 'LIG:LIG_1'}
                            ],
                           'ipAddressingMode': 'IpPool',
                           'ipRangeUris': [],
                           'powerMode': 'RedundantPowerFeed'
                           }]


LE1 = 'LE_1'

les = {'le1':
       {'name': 'LE_1',
        'enclosureUris': ['ENC:' + ENC1],
        'enclosureGroupUri': 'EG:EG_1',
        'firmwareBaselineUri': None,
        'forceInstallFirmware': False
        },
       'le2':
       {'name': 'LE_1',
        'enclosureUris': ['ENC:' + ENC1],
        'enclosureGroupUri': 'EG:EG_1',
        'firmwareBaselineUri': None,
        'forceInstallFirmware': False
        },
       'le3':
       {'name': 'LE_1',
        'enclosureUris': ['ENC:' + ENC1],
        'enclosureGroupUri': 'EG:EG_1',
        'firmwareBaselineUri': None,
        'forceInstallFirmware': False
        }
       }

li_uplink_set_20504 = {'name': 'UplinkSet_20504',
                       'ethernetNetworkType': 'NotApplicable',
                       'networkType': 'FibreChannel',
                       'networkUris': [],
                       'fcNetworkUris': ['FC_1'],
                       'fcoeNetworkUris': [],
                       'lacpTimer': 'Short',
                       'logicalInterconnectUri': None,
                       'primaryPortLocation': None,
                       'manualLoginRedistributionState': 'Supported',
                       'connectionMode': 'Auto',
                       'nativeNetworkUri': None,
                       'portConfigInfos': [{'bay': '1', 'port': '2', 'desiredSpeed': 'Speed4G', 'enclosure': ENC1}]}


li_portmonitor = {"type": "port-monitor",
                  "enablePortMonitor": 'true',
                  "analyzerPort": {"portMonitorConfigInfo": "AnalyzerPort",
                                   "portUri": "UplinkportUri"},
                  "monitoredPorts": [{"portMonitorConfigInfo": "MonitoredBoth",
                                      "portUri": "DownlinkportUri"}]
                  }

add_mirrorport = {"type": "port-monitor",
                  "enablePortMonitor": 'true',
                  "analyzerPort": {"portMonitorConfigInfo": "AnalyzerPort",
                                   "portUri": "UplinkportUri"},
                  "monitoredPorts": [{"portMonitorConfigInfo": "MonitoredBoth",
                                      "portUri": "DownlinkportUri"},
                                     {"portMonitorConfigInfo": "MonitoredBoth",
                                      "portUri": "DownlinkportUri"}]
                  }


Edit_Uplink_Port = {'associatedUplinkSetUri': '',
                    'interconnectName': INTERCONNECTS[0],
                    'portType': 'Uplink',
                    'portId': '',
                    'portHealthStatus': '',
                    'capability': ['FibreChannel'],
                    'configPortTypes': ['FibreChannel'],
                    'enabled': '',
                    'portName': '',
                    'portStatus': '',
                    'type': 'port'}

PROFILE1 = 'CN750160YS_Bay1-Carbon'
PROFILE2 = 'CN750160YS_Bay2-Carbon'

PROFILES = ['CN750160YS_Bay1-Carbon', 'CN750160YS_Bay2-Carbon']

server_profile1 = [{'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 1',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_1', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': PROFILE1, 'description': '', 'affinity': 'Bay',
                    'bootMode': {"manageMode": True, "mode": "BIOS"},
                    'boot': {"manageBoot": True, "order": ["CD", "USB", "HardDisk"]},
                    'connections': [{'id': 1, 'name': 'BAY4', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '16000', 'networkUri': 'FC:FC_1', "wwpnType": "UserDefined", "wwpn": "10:00:00:90:fa:5d:34:53", "wwnn": "20:00:00:90:fa:5d:34:53", "ipv4": {}, "boot": {"priority": "Primary", "bootVolumeSource": "UserDefined", "targets": [{"arrayWwpn": "10:00:00:90:fa:5d:34:53", "lun": "0"}], "iscsi": {}}}]}]


server_profile2 = [{'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 2',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_1', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                    'name': 'PROFILE2', 'description': '', 'affinity': 'Bay',
                    'bootMode': {"manageMode": True, "mode": "BIOS"},
                    'boot': {"manageBoot": True, "order": ["CD", "USB", "HardDisk"]},
                    'connections': [{'id': 1, 'name': 'Downlink_1', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_1', "wwpnType": "UserDefined", "wwpn": "10:00:9a:69:37:00:00:10", "wwnn": "20:00:9a:69:37:00:00:10", "ipv4": {}, "boot": {"priority": "Primary", "bootVolumeSource": "UserDefined", "targets": [{"arrayWwpn": "20:00:9a:69:37:00:00:10", "lun": "0"}], "iscsi": {}}},
                                    {'id': 2, 'name': 'Downlink_2', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '16000', 'networkUri': 'FC:FC_2', "wwpnType": "UserDefined", "wwpn": "10:00:9a:69:37:00:00:11", "wwnn": "20:00:9a:69:37:00:00:11", "ipv4": {}, "boot": {"priority": "Secondary", "bootVolumeSource": "UserDefined", "targets": [{"arrayWwpn": "20:00:9a:69:37:00:00:10", "lun": "0"}], "iscsi": {}}}]}]


server_profiles3 = [{'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 3',
                     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + EG1, 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                     'name': 'LUNS_ELX_LGCY', 'description': '', 'affinity': 'Bay',
                     'bootMode': {"manageMode": True, "mode": "BIOS"},
                     'boot': {"manageBoot": True, "order": ["CD", "USB", "HardDisk"]},
                     'connections': [{'id': 1, 'name': 'BAY1', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_1', "wwpnType": "UserDefined", "wwpn": "10:00:00:90:fa:5d:34:56", "wwnn": "20:00:00:90:fa:5d:34:56", "boot": {"priority": "NotBootable", "iscsi": {}}},
                                     {'id': 2, 'name': 'BAY4', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '16000', 'networkUri': 'FC:FC_2', "wwpnType": "UserDefined", "wwpn": "10:00:00:90:fa:5d:34:57", "wwnn": "20:00:00:90:fa:5d:34:57", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
                                     ]}]

server_profiles = [[{'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 1',
                     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_1', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                     'name': PROFILE1, 'description': '', 'affinity': 'Bay',
                     'bootMode': {"manageMode": True, "mode": "BIOS"},
                     'boot': {"manageBoot": True, "order": ["CD", "USB", "HardDisk"]},
                     'connections': [{'id': 1, 'name': 'Downlink_1', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '16000', 'networkUri': 'FC:FC_1', "wwpnType": "UserDefined", "wwpn": "10:00:00:90:fa:5d:34:52", "wwnn": "20:00:00:90:fa:5d:34:52", "boot": {"priority": "Primary", "bootVolumeSource": "UserDefined", "targets": [{"arrayWwpn": "10:00:00:90:fa:5d:34:52", "lun": "0"}], "iscsi": {}}},
                                     {'id': 2, 'name': 'Downlink_2', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '16000', 'networkUri': 'FC:FC_2', "wwpnType": "UserDefined", "wwpn": "10:00:00:90:fa:5d:34:53", "wwnn": "20:00:00:90:fa:5d:34:53", "ipv4": {}, "boot": {"priority": "Secondary", "bootVolumeSource": "UserDefined", "targets": [{"arrayWwpn": "10:00:00:90:fa:5d:34:53", "lun": "0"}], "iscsi": {}}},
                                     ]

                     }],
                   [{'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 2',
                       'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_1', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                       'name': PROFILE2, 'description': '', 'affinity': 'Bay',
                     'bootMode': {"manageMode": True, "mode": "BIOS"},
                     'boot': {"manageBoot": True, "order": ["CD", "USB", "HardDisk"]},
                     'connections': [{'id': 1, 'name': 'Downlink_1', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '16000', 'networkUri': 'FC:FC_1', "wwpnType": "UserDefined", "wwpn": "10:00:9a:69:37:00:00:08", "wwnn": "20:00:9a:69:37:00:00:08", "boot": {"priority": "Primary", "bootVolumeSource": "UserDefined", "targets": [{"arrayWwpn": "10:00:9a:69:37:00:00:08", "lun": "1"}], "iscsi": {}}},
                                     {'id': 2, 'name': 'Downlink_2', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '16000', 'networkUri': 'FC:FC_2', "wwpnType": "UserDefined", "wwpn": "10:00:9a:69:37:00:00:10", "wwnn": "20:00:9a:69:37:00:00:10", "ipv4": {}, "boot": {"priority": "Secondary", "bootVolumeSource": "UserDefined", "targets": [{"arrayWwpn": "20:00:9a:69:37:00:00:10", "lun": "0"}], "iscsi": {}}},
                                     ]

                     }
                    ]
                   ]

server_profile_20502 = [[{'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 1',
                          'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_1', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                          'name': PROFILE1, 'description': 'Server using Carbon', 'affinity': 'Bay',
                          'boot': {'manageBoot': False},
                          'bootMode': None,
                          'connections': [{'id': 1, 'name': 'Downlink_1', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_1', "wwpnType": "UserDefined", "wwpn": "10:00:00:90:fa:5d:34:52", "wwnn": "20:00:00:90:fa:5d:34:52", "boot": {"priority": "Primary", "bootVolumeSource": "UserDefined", "targets": [{"arrayWwpn": "10:00:00:90:fa:5d:34:52", "lun": "0"}], "iscsi": {}}},
                                          {'id': 2, 'name': 'Downlink_2', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '16000', 'networkUri': 'FC:FC_2', "wwpnType": "UserDefined", "wwpn": "10:00:00:90:fa:5d:34:53", "wwnn": "20:00:00:90:fa:5d:34:53", "ipv4": {}, "boot": {"priority": "Secondary", "bootVolumeSource": "UserDefined", "targets": [{"arrayWwpn": "10:00:00:90:fa:5d:34:53", "lun": "0"}], "iscsi": {}}}
                                          ]}],
                        [{'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 2',
                          'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_1', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                          'name': PROFILE2, 'description': 'Server using Carbon', 'affinity': 'Bay',
                          'boot': {'manageBoot': False},
                          'bootMode': None,
                          'connections': [{'id': 1, 'name': 'Downlink_1', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_1', "wwpnType": "UserDefined", "wwpn": "10:00:9a:69:37:00:00:08", "wwnn": "20:00:9a:69:37:00:00:08", "boot": {"priority": "Primary", "bootVolumeSource": "UserDefined", "targets": [{"arrayWwpn": "10:00:9a:69:37:00:00:08", "lun": "1"}], "iscsi": {}}},
                                          {'id': 2, 'name': 'Downlink_2', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '16000', 'networkUri': 'FC:FC_2', "wwpnType": "UserDefined", "wwpn": "10:00:9a:69:37:00:00:10", "wwnn": "20:00:9a:69:37:00:00:10", "ipv4": {}, "boot": {"priority": "Secondary", "bootVolumeSource": "UserDefined", "targets": [{"arrayWwpn": "20:00:9a:69:37:00:00:10", "lun": "0"}], "iscsi": {}}},
                                          ]}]
                        ]

server_profile_20634 = [[{'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 1',
                          'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_1', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                          'name': PROFILE1, 'description': '', 'affinity': 'Bay',
                          'bootMode': {"manageMode": True, "mode": "BIOS"},
                          'boot': {"manageBoot": True, "order": ["CD", "USB", "HardDisk"]},
                          'connections': [{'id': 1, 'name': 'Downlink_1', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_1', "wwpnType": "UserDefined", "wwpn": "10:00:00:90:fa:5d:34:52", "wwnn": "20:00:00:90:fa:5d:34:52", "boot": {"priority": "Primary", "bootVolumeSource": "UserDefined", "targets": [{"arrayWwpn": "10:00:00:90:fa:5d:34:52", "lun": "0"}], "iscsi": {}}},
                                          {'id': 2, 'name': 'Downlink_2', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_2', "wwpnType": "UserDefined", "wwpn": "10:00:00:90:fa:5d:34:53", "wwnn": "20:00:00:90:fa:5d:34:53", "ipv4": {}, "boot": {"priority": "Secondary", "bootVolumeSource": "UserDefined", "targets": [{"arrayWwpn": "10:00:00:90:fa:5d:34:53", "lun": "0"}], "iscsi": {}}},
                                          ]}],
                        [{'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 2',
                          'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_1', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                          'name': PROFILE2, 'description': '', 'affinity': 'Bay',
                          'bootMode': {"manageMode": True, "mode": "BIOS"},
                          'boot': {"manageBoot": True, "order": ["CD", "USB", "HardDisk"]},
                          'connections': [{'id': 1, 'name': 'Downlink_1', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_1', "wwpnType": "UserDefined", "wwpn": "10:00:9a:69:37:00:00:08", "wwnn": "20:00:9a:69:37:00:00:08", "boot": {"priority": "Primary", "bootVolumeSource": "UserDefined", "targets": [{"arrayWwpn": "10:00:9a:69:37:00:00:08", "lun": "1"}], "iscsi": {}}},
                                          {'id': 2, 'name': 'Downlink_2', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_2', "wwpnType": "UserDefined", "wwpn": "10:00:9a:69:37:00:00:10", "wwnn": "20:00:9a:69:37:00:00:10", "ipv4": {}, "boot": {"priority": "Secondary", "bootVolumeSource": "UserDefined", "targets": [{"arrayWwpn": "20:00:9a:69:37:00:00:10", "lun": "0"}], "iscsi": {}}},
                                          ]}
                         ]
                        ]

server_profile_20503 = [[{'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 1',
                          'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_1', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                          'name': PROFILE1, 'description': '', 'affinity': 'Bay',
                          'bootMode': {"manageMode": True, "mode": "BIOS"},
                          'boot': {"manageBoot": True, "order": ["CD", "USB", "HardDisk"]},
                          'connections': [{'id': 1, 'name': 'Downlink_1', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '16000', 'networkUri': 'FC:FC_1', "wwpnType": "UserDefined", "wwpn": "10:00:00:90:fa:5d:34:52", "wwnn": "20:00:00:90:fa:5d:34:52", "boot": {"priority": "Primary", "bootVolumeSource": "UserDefined", "targets": [{"arrayWwpn": "10:00:00:90:fa:5d:34:52", "lun": "0"}], "iscsi": {}}},
                                          {'id': 2, 'name': 'Downlink_2', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '16000', 'networkUri': 'FC:FC_2', "wwpnType": "UserDefined", "wwpn": "10:00:00:90:fa:5d:34:53", "wwnn": "20:00:00:90:fa:5d:34:53", "ipv4": {}, "boot": {"priority": "Secondary", "bootVolumeSource": "UserDefined", "targets": [{"arrayWwpn": "10:00:00:90:fa:5d:34:53", "lun": "0"}], "iscsi": {}}},
                                          ]

                          }],
                        [{'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 2',
                          'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_1', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                          'name': PROFILE2, 'description': '', 'affinity': 'Bay',
                          'bootMode': {"manageMode": True, "mode": "BIOS"},
                          'boot': {"manageBoot": True, "order": ["CD", "USB", "HardDisk"]},
                          'connections': [{'id': 1, 'name': 'Downlink_1', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '16000', 'networkUri': 'FC:FC_1', "wwpnType": "UserDefined", "wwpn": "10:00:9a:69:37:00:00:08", "wwnn": "20:00:9a:69:37:00:00:08", "boot": {"priority": "Primary", "bootVolumeSource": "UserDefined", "targets": [{"arrayWwpn": "10:00:9a:69:37:00:00:08", "lun": "1"}], "iscsi": {}}},
                                          {'id': 2, 'name': 'Downlink_2', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '16000', 'networkUri': 'FC:FC_2', "wwpnType": "UserDefined", "wwpn": "10:00:9a:69:37:00:00:10", "wwnn": "20:00:9a:69:37:00:00:10", "ipv4": {}, "boot": {"priority": "Secondary", "bootVolumeSource": "UserDefined", "targets": [{"arrayWwpn": "20:00:9a:69:37:00:00:10", "lun": "0"}], "iscsi": {}}},
                                          ]

                          }
                         ]
                        ]

multi_profile = [[{'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 1',
                   'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_1', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                   'name': PROFILE1, 'description': '', 'affinity': 'Bay',
                   'bootMode': {"manageMode": True, "mode": "BIOS"},
                   'boot': {"manageBoot": True, "order": ["CD", "USB", "HardDisk"]},
                   'connections': [{'id': 1, 'name': 'Downlink_1', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '16000', 'networkUri': 'FC:FC_1', "wwpnType": "UserDefined", "wwpn": "10:00:00:90:fa:5d:34:52", "wwnn": "20:00:00:90:fa:5d:34:52", "boot": {"priority": "Primary", "bootVolumeSource": "UserDefined", "targets": [{"arrayWwpn": "10:00:00:90:fa:5d:34:52", "lun": "0"}], "iscsi": {}}},
                                   {'id': 2, 'name': 'Downlink_2', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '16000', 'networkUri': 'FC:FC_2', "wwpnType": "UserDefined", "wwpn": "10:00:00:90:fa:5d:34:53", "wwnn": "20:00:00:90:fa:5d:34:53", "ipv4": {}, "boot": {"priority": "Secondary", "bootVolumeSource": "UserDefined", "targets": [{"arrayWwpn": "10:00:00:90:fa:5d:34:53", "lun": "0"}], "iscsi": {}}},
                                   ]

                   }],
                 [{'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 2',
                   'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_1', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                   'name': PROFILE2, 'description': '', 'affinity': 'Bay',
                   'bootMode': {"manageMode": True, "mode": "BIOS"},
                   'boot': {"manageBoot": True, "order": ["CD", "USB", "HardDisk"]},
                   'connections': [{'id': 1, 'name': 'Downlink_1', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '16000', 'networkUri': 'FC:FC_1', "wwpnType": "UserDefined", "wwpn": "10:00:9a:69:37:00:00:08", "wwnn": "20:00:9a:69:37:00:00:08", "boot": {"priority": "Primary", "bootVolumeSource": "UserDefined", "targets": [{"arrayWwpn": "10:00:9a:69:37:00:00:08", "lun": "1"}], "iscsi": {}}},
                                   {'id': 2, 'name': 'Downlink_2', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '16000', 'networkUri': 'FC:FC_2', "wwpnType": "UserDefined", "wwpn": "10:00:9a:69:37:00:00:10", "wwnn": "20:00:9a:69:37:00:00:10", "ipv4": {}, "boot": {"priority": "Secondary", "bootVolumeSource": "UserDefined", "targets": [{"arrayWwpn": "20:00:9a:69:37:00:00:10", "lun": "0"}], "iscsi": {}}},
                                   ]

                   }
                  ]
                 ]

multi_profile_dummy = [[{'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 1',
                         'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_1', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                         'name': PROFILE1, 'description': 'Server using Carbon', 'affinity': 'Bay',
                         'boot': {'manageBoot': False},
                         'bootMode': None,
                         'connections': [{'id': 1, 'name': 'Downlink_1', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_1', "wwpnType": "UserDefined", "wwpn": "10:00:00:90:fa:5d:34:52", "wwnn": "20:00:00:90:fa:5d:34:52", "boot": {"priority": "Primary", "bootVolumeSource": "UserDefined", "targets": [{"arrayWwpn": "10:00:00:90:fa:5d:34:52", "lun": "0"}], "iscsi": {}}},
                                         {'id': 2, 'name': 'Downlink_2', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '16000', 'networkUri': 'FC:FC_2', "wwpnType": "UserDefined", "wwpn": "10:00:00:90:fa:5d:34:53", "wwnn": "20:00:00:90:fa:5d:34:53", "ipv4": {}, "boot": {"priority": "Secondary", "bootVolumeSource": "UserDefined", "targets": [{"arrayWwpn": "10:00:00:90:fa:5d:34:53", "lun": "0"}], "iscsi": {}}}
                                         ]}],
                       [{'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 2',
                         'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_1', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                         'name': PROFILE2, 'description': 'Server using Carbon', 'affinity': 'Bay',
                         'boot': {'manageBoot': False},
                         'bootMode': None,
                         'connections': [{'id': 1, 'name': 'Downlink_1', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_1', "wwpnType": "UserDefined", "wwpn": "10:00:9a:69:37:00:00:08", "wwnn": "20:00:9a:69:37:00:00:08", "boot": {"priority": "Primary", "bootVolumeSource": "UserDefined", "targets": [{"arrayWwpn": "10:00:9a:69:37:00:00:08", "lun": "1"}], "iscsi": {}}},
                                         {'id': 2, 'name': 'Downlink_2', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '16000', 'networkUri': 'FC:FC_2', "wwpnType": "UserDefined", "wwpn": "10:00:9a:69:37:00:00:10", "wwnn": "20:00:9a:69:37:00:00:10", "ipv4": {}, "boot": {"priority": "Secondary", "bootVolumeSource": "UserDefined", "targets": [{"arrayWwpn": "20:00:9a:69:37:00:00:10", "lun": "0"}], "iscsi": {}}},
                                         ]}]
                       ]

profile_20994 = [[{'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 1',
                   'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_1', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                   'name': PROFILE1, 'description': 'Server using Carbon', 'affinity': 'Bay',
                   'bootMode': {"manageMode": True, "mode": "BIOS"},
                   'boot': {"manageBoot": True, "order": ["CD", "USB", "HardDisk"]},
                   'connections': [{'id': 1, 'name': 'Downlink_1', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_1', "wwpnType": "UserDefined", "wwpn": "10:00:00:90:fa:5d:34:53", "wwnn": "20:00:00:90:fa:5d:34:53", "ipv4": {}, "boot": {"priority": "Primary", "bootVolumeSource": "UserDefined", "targets": [{"arrayWwpn": "10:00:00:90:fa:5d:34:53", "lun": "0"}], "iscsi": {}}}]}],
                 [{'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 2',
                   'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_1', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                   'name': PROFILE2, 'description': 'Server using Carbon', 'affinity': 'Bay',
                   'bootMode': {"manageMode": True, "mode": "BIOS"},
                   'boot': {"manageBoot": True, "order": ["CD", "USB", "HardDisk"]},
                   'connections': [{'id': 1, 'name': 'Downlink_2', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_2', "wwpnType": "UserDefined", "wwpn": "10:00:9a:69:37:00:00:10", "wwnn": "20:00:9a:69:37:00:00:10", "ipv4": {}, "boot": {"priority": "Primary", "bootVolumeSource": "UserDefined", "targets": [{"arrayWwpn": "20:00:9a:69:37:00:00:10", "lun": "0"}], "iscsi": {}}}]}]
                 ]


server_profiles_20635 = [[{'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 1',
                           'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_1', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                           'name': PROFILE1, 'description': '', 'affinity': 'Bay',
                           'bootMode': {"manageMode": True, "mode": "BIOS"},
                           'boot': {"manageBoot": True, "order": ["CD", "USB", "HardDisk"]},
                           'connections': [{'id': 1, 'name': 'Downlink_1', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_20635', "wwpnType": "UserDefined", "wwpn": "10:00:00:90:fa:5d:34:52", "wwnn": "20:00:00:90:fa:5d:34:52", "boot": {"priority": "Primary", "bootVolumeSource": "UserDefined", "targets": [{"arrayWwpn": "10:00:00:90:fa:5d:34:52", "lun": "0"}], "iscsi": {}}},
                                           {'id': 2, 'name': 'Downlink_2', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '16000', 'networkUri': 'FC:FC_2', "wwpnType": "UserDefined", "wwpn": "10:00:00:90:fa:5d:34:53", "wwnn": "20:00:00:90:fa:5d:34:53", "ipv4": {}, "boot": {"priority": "Secondary", "bootVolumeSource": "UserDefined", "targets": [{"arrayWwpn": "10:00:00:90:fa:5d:34:53", "lun": "0"}], "iscsi": {}}}]}],
                         [{'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 2',
                           'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_1', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                           'name': PROFILE2, 'description': '', 'affinity': 'Bay',
                           'bootMode': {"manageMode": True, "mode": "BIOS"},
                           'boot': {"manageBoot": True, "order": ["CD", "USB", "HardDisk"]},
                           'connections': [{'id': 1, 'name': 'Downlink_1', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_20635', "wwpnType": "UserDefined", "wwpn": "10:00:9a:69:37:00:00:08", "wwnn": "20:00:9a:69:37:00:00:08", "boot": {"priority": "Primary", "bootVolumeSource": "UserDefined", "targets": [{"arrayWwpn": "10:00:9a:69:37:00:00:08", "lun": "1"}], "iscsi": {}}},
                                           {'id': 2, 'name': 'Downlink_2', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '16000', 'networkUri': 'FC:FC_2', "wwpnType": "UserDefined", "wwpn": "10:00:9a:69:37:00:00:10", "wwnn": "20:00:9a:69:37:00:00:10", "ipv4": {}, "boot": {"priority": "Secondary", "bootVolumeSource": "UserDefined", "targets": [{"arrayWwpn": "20:00:9a:69:37:00:00:10", "lun": "0"}], "iscsi": {}}}]}]
                         ]

server_profile_20563 = [[{'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 1',
                          'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_1', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                          'name': PROFILE1, 'description': '', 'affinity': 'Bay',
                          'bootMode': {"manageMode": True, "mode": "BIOS"},
                          'boot': {"manageBoot": True, "order": ["CD", "USB", "HardDisk"]},
                          'connections': [{'id': 1, 'name': 'Downlink_1', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_1', "wwpnType": "UserDefined", "wwpn": "10:00:00:90:fa:5d:34:52", "wwnn": "20:00:00:90:fa:5d:34:52", "boot": {"priority": "Primary", "bootVolumeSource": "UserDefined", "targets": [{"arrayWwpn": "10:00:00:90:fa:5d:34:52", "lun": "0"}], "iscsi": {}}},
                                          {'id': 2, 'name': 'Downlink_2', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '16000', 'networkUri': 'FC:FC_2', "wwpnType": "UserDefined", "wwpn": "10:00:00:90:fa:5d:34:53", "wwnn": "20:00:00:90:fa:5d:34:53", "ipv4": {}, "boot": {"priority": "Secondary", "bootVolumeSource": "UserDefined", "targets": [{"arrayWwpn": "10:00:00:90:fa:5d:34:53", "lun": "0"}], "iscsi": {}}}]}],

                        [{'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 2',
                          'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_1', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                          'name': PROFILE2, 'description': '', 'affinity': 'Bay',
                          'bootMode': {"manageMode": True, "mode": "BIOS"},
                          'boot': {"manageBoot": True, "order": ["CD", "USB", "HardDisk"]},
                          'connections': [{'id': 1, 'name': 'Downlink_3', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_1', "wwpnType": "UserDefined", "wwpn": "10:00:9a:69:37:00:00:08", "wwnn": "20:00:9a:69:37:00:00:08", "boot": {"priority": "Primary", "bootVolumeSource": "UserDefined", "targets": [{"arrayWwpn": "10:00:9a:69:37:00:00:08", "lun": "1"}], "iscsi": {}}},
                                          {'id': 2, 'name': 'Downlink_4', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '16000', 'networkUri': 'FC:FC_2', "wwpnType": "UserDefined", "wwpn": "10:00:9a:69:37:00:00:10", "wwnn": "20:00:9a:69:37:00:00:10", "ipv4": {}, "boot": {"priority": "Secondary", "bootVolumeSource": "UserDefined", "targets": [{"arrayWwpn": "20:00:9a:69:37:00:00:10", "lun": "0"}], "iscsi": {}}}]}]]


server_profile_quartz = [{'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 2',
                          'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_1', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                          'name': PROFILE2, 'description': '', 'affinity': 'Bay',
                          'bootMode': {"manageMode": True, "mode": "BIOS"},
                          'boot': {"manageBoot": True, "order": ["CD", "USB", "HardDisk"]},
                          'connections': [{'id': 1, 'name': 'Downlink_3', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_1', "wwpnType": "UserDefined", "wwpn": "10:00:9a:69:37:00:00:08", "wwnn": "20:00:9a:69:37:00:00:08", "boot": {"priority": "Primary", "bootVolumeSource": "UserDefined", "targets": [{"arrayWwpn": "10:00:9a:69:37:00:00:08", "lun": "1"}], "iscsi": {}}}]}
                         ]

server_profile_electron = [{'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 1',
                            'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_1', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                            'name': PROFILE1, 'description': '', 'affinity': 'Bay',
                            'bootMode': {"manageMode": True, "mode": "BIOS"},
                            'boot': {"manageBoot": True, "order": ["CD", "USB", "HardDisk"]},
                            'connections': [{'id': 1, 'name': 'Downlink_1', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_1', "wwpnType": "UserDefined", "wwpn": "10:00:00:90:fa:5d:34:52", "wwnn": "20:00:00:90:fa:5d:34:52", "boot": {"priority": "Primary", "bootVolumeSource": "UserDefined", "targets": [{"arrayWwpn": "10:00:00:90:fa:5d:34:52", "lun": "0"}], "iscsi": {}}}]}
                           ]

profile_redundant_electron = [{'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 1',
                               'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_1', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                               'name': PROFILE1, 'description': '', 'affinity': 'Bay',
                               'bootMode': {"manageMode": True, "mode": "BIOS"},
                               'boot': {"manageBoot": True, "order": ["CD", "USB", "HardDisk"]},
                               'connections': [{'id': 1, 'name': 'Downlink_1', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_1', "wwpnType": "UserDefined", "wwpn": "10:00:00:90:fa:5d:34:52", "wwnn": "20:00:00:90:fa:5d:34:52", "boot": {"priority": "Primary", "bootVolumeSource": "UserDefined", "targets": [{"arrayWwpn": "10:00:00:90:fa:5d:34:52", "lun": "0"}], "iscsi": {}}},
                                               {'id': 2, 'name': 'Downlink_2', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '16000', 'networkUri': 'FC:FC_2', "wwpnType": "UserDefined", "wwpn": "10:00:00:90:fa:5d:34:53", "wwnn": "20:00:00:90:fa:5d:34:53", "ipv4": {}, "boot": {"priority": "Secondary", "bootVolumeSource": "UserDefined", "targets": [{"arrayWwpn": "10:00:00:90:fa:5d:34:53", "lun": "0"}], "iscsi": {}}}]}]


profile_redundant_quartz = [{'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 2',
                             'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_1', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                             'name': PROFILE2, 'description': '', 'affinity': 'Bay',
                             'bootMode': {"manageMode": True, "mode": "BIOS"},
                             'boot': {"manageBoot": True, "order": ["CD", "USB", "HardDisk"]},
                             'connections': [{'id': 1, 'name': 'Downlink_3', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_1', "wwpnType": "UserDefined", "wwpn": "10:00:9a:69:37:00:00:08", "wwnn": "20:00:9a:69:37:00:00:08", "boot": {"priority": "Primary", "bootVolumeSource": "UserDefined", "targets": [{"arrayWwpn": "10:00:9a:69:37:00:00:08", "lun": "1"}], "iscsi": {}}},
                                             {'id': 2, 'name': 'Downlink_4', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '16000', 'networkUri': 'FC:FC_2', "wwpnType": "UserDefined", "wwpn": "10:00:9a:69:37:00:00:10", "wwnn": "20:00:9a:69:37:00:00:10", "ipv4": {}, "boot": {"priority": "Secondary", "bootVolumeSource": "UserDefined", "targets": [{"arrayWwpn": "20:00:9a:69:37:00:00:10", "lun": "0"}], "iscsi": {}}}]}]


server_profiles_20640 = [[{'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 1',
                           'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_1', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                           'name': PROFILE1, 'description': '', 'affinity': 'Bay',
                           'bootMode': {"manageMode": True, "mode": "BIOS"},
                           'boot': {"manageBoot": True, "order": ["CD", "USB", "HardDisk"]},
                           'connections': [{'id': 1, 'name': 'Downlink_1', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_1', "wwpnType": "UserDefined", "wwpn": "10:00:00:90:fa:5d:34:52", "wwnn": "20:00:00:90:fa:5d:34:52", "boot": {"priority": "Primary", "bootVolumeSource": "UserDefined", "targets": [{"arrayWwpn": "10:00:00:90:fa:5d:34:52", "lun": "0"}], "iscsi": {}}}]}
                          ],
                         [{'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 2',
                           'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_1', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                           'name': PROFILE2, 'description': '', 'affinity': 'Bay',
                           'bootMode': {"manageMode": True, "mode": "BIOS"},
                           'boot': {"manageBoot": True, "order": ["CD", "USB", "HardDisk"]},
                           'connections': [{'id': 1, 'name': 'Downlink_3', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_1', "wwpnType": "UserDefined", "wwpn": "10:00:9a:69:37:00:00:08", "wwnn": "20:00:9a:69:37:00:00:08", "boot": {"priority": "Primary", "bootVolumeSource": "UserDefined", "targets": [{"arrayWwpn": "10:00:9a:69:37:00:00:08", "lun": "1"}], "iscsi": {}}}]}]
                         ]

valDict = {'status_code': 200, 'taskState': 'Completed'}

valDict_20489 = {'macType': 'Physical', 'wwnType': 'Physical', 'serialNumberType': 'Physical'}
valDict_20502 = {'macType': 'Physical', 'wwnType': 'Physical', 'serialNumberType': 'Physical'}

val_sp1_20503 = {'serialNumberType': 'Physical', 'serialNumber': 'HD53NP0397', 'uuid': '36343537-3338-4448-3533-4E5030333937'}

val_sp2_20503 = {'serialNumberType': 'Physical', 'serialNumber': 'HD53NP0766', 'uuid': '36343537-3338-4448-3533-4E5030373636'}

valDict_20540 = {'errorCode': 'CRM_EXCEEDS_MAX_LICENSED_UPLINKPORTS_FC_MODULE',
                 'message': 'The interconnect module in bay 1 has exceeded the limit of 12 uplink ports included in uplink sets within the same interconnect.',
                 'recommendedActions': ['Reduce the number of uplink ports defined in the uplink sets.']
                 }

valDict_error = [{'errorCode': 'CRM_EXCEEDS_MAX_LICENSED_UPLINKPORTS_FC_MODULE',
                  'message': 'The interconnect module in bay 1 has exceeded the limit of 12 uplink ports included in uplink sets within the same interconnect.',
                  'recommendedActions': ['Reduce the number of uplink ports defined in the uplink sets.']
                  },
                 {'errorCode': 'CRM_EXCEEDS_MAX_LICENSED_UPLINKPORTS_FC_MODULE',
                  'message': 'The interconnect module in bay 4 has exceeded the limit of 12 uplink ports included in uplink sets within the same interconnect.',
                  'recommendedActions': ['Reduce the number of uplink ports defined in the uplink sets.']
                  }
                 ]

error_msg_20994 = 'The number of monitored ports exceeds the limit of 1 for Virtual Connect SE 16Gb FC Module.'

########################################

true = True
false = False

########################################
"""
default_variables = {'admin_credentials': admin_credentials,
                     'appliance': appliance,
                     'encs': encs,
                     'enc_groups': enc_groups,
                     'ethernet_networks': ethernet_networks,
                     'ethernet_ranges': ethernet_ranges,
                     'fc_networks': fc_networks,
                     'fcoe_networks': fcoe_networks,
                     'fcoe_ranges': fcoe_ranges,
                     'les': les,
                     'licenses': licenses,
                     'ligs': ligs,
                     'network_sets': network_sets,
                     'network_set_ranges': network_set_ranges,
                     'ranges': ranges,
                     'rc': rc,
                     'server_profiles': server_profiles,
                     'uplink_sets': uplink_sets,
                     'users': users,
                     'timeandlocale': timeandlocale,
                     'true': true, 'false': false,
                     'vcenter': vcenter}


def get_variables():

    variables = default_variables
    return variables
"""

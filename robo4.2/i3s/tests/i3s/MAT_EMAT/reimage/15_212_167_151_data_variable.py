''' Data variable file of 167.151 '''
# pylint: disable=invalid-name
# from winnt import NULL
# from requests.api import patch

admin_credentials = {'userName': 'Administrator', 'password': 'admin123'}
ov_appliances = ['fe80::32e1:71ff:fe68:f8a0', 'fe80::9eb6:54ff:fe98:d2e0']
MAC = '30:e1:71:68:f8:a0'
i3s_appliances = ['fe80::1602:ecff:fe46:a758', 'fe80::1602:ecff:fe46:e160']
i3s_enclosure = ['SGH736WTHW', 'SGH736WTHV']
enclosures_count = '3'
DEFAULT_USER = 'Administrator'
status = '200'
NEW_PASSWORD = 'admin123'
# SUBNET_1 = '255.255.252.0'
# IPV4GATEWAY = '15.212.164.1'
# DOMAINNAME = 'hpecorp.net'
# HOSTNAME = 'EB2405.test.local'
# DNS1 = '16.110.135.51'
# DNS2 = '16.110.135.52'
# MAINTENANCEIP1 = '15.212.167.152'
# MAINTENANCEIP2 = '15.212.167.153'
CLUSTERIP = '15.212.167.151'
OV_ACTIVE = 'fe80::32e1:71ff:fe68:f8a0'
# Ov_Build_sha = '/ov/4.10/ddimage/HPEOneView-SSH-4.20.00-0367037-withsig_PASS141.zip.sha256'
# OV_Build = '/ov/4.10/ddimage/HPEOneView-SSH-4.20.00-0367037-withsig_PASS141.zip'
# I3S_Build_sha = '/i3s/4.10/ddimage/HPEImageStreamer-SSH-4.20.00-0366675-withsig.zip.sha256'
# I3S_Build = '/i3s/4.10/ddimage/HPEImageStreamer-SSH-4.20.00-0366675-withsig.zip'
# i3s_version= '4.00.00-0319447'
# ov_version= '4.00.00-0319900'
build_server = 'fe80::9932:1c50:6353:7a9'
# build_version = '4.10'
blade_IP = '15.212.164.253'
support_dump_loc = r'C:\support_dump\sd'
fusion_IP = '15.212.167.151'

network = {"type": "ApplianceNetworkConfiguration",
           "applianceNetworks": [{"activeNode": 1,
                                  "unconfigure": False,
                                  "app1Ipv4Addr": "15.212.167.152", "app1Ipv6Addr": "",
                                  "app2Ipv4Addr": "15.212.167.153", "app2Ipv6Addr": "",
                                  "virtIpv4Addr": "15.212.167.151", "virtIpv6Addr": None,
                                  "app1Ipv4Alias": None, "app1Ipv6Alias": None,
                                  "app2Ipv4Alias": None, "app2Ipv6Alias": None,
                                  "hostname": "EB2405.test.local",
                                  "confOneNode": True, "interfaceName": "",
                                  "macAddress": "30:e1:71:68:f8:a0",
                                  "ipv4Type": "STATIC", "ipv6Type": "UNCONFIGURE",
                                  "overrideIpv4DhcpDnsServers": False,
                                  "ipv4Subnet": "255.255.252.0",
                                  "ipv4Gateway": "15.212.164.1",
                                  "ipv6Subnet": None, "ipv6Gateway": None,
                                  "domainName": "test.local",
                                  "searchDomains": [],
                                  "ipv4NameServers": [],
                                  "ipv6NameServers": [","],
                                  "bondedTo": None, "aliasDisabled": True}]}

servers = [{'serverHardwareUri': 'SGH736WTHV, bay 1', 'serverHardwareTypeUri': 'SY 480 Gen9 2'},
           {'serverHardwareUri': 'SGH736WTHW, bay 4', 'serverHardwareTypeUri': 'SY 480 Gen9 1'}]

iscsi_subnet = {'type': 'Subnet', 'gateway': '192.168.0.1',
                'networkId': '192.168.0.0', 'subnetmask': '255.255.0.0',
                'dnsServers': [], 'domain': 'deploy.local'}

mgmt_subnet = {'type': 'Subnet', 'gateway': '15.212.164.1',
               'networkId': '15.212.164.0', 'subnetmask': '255.255.252.0',
               'dnsServers': ['16.110.135.51', '16.110.135.52'], 'domain': 'test.local'}

iscsi_ipv4ranges = {'type': 'Range', 'networkId': '192.168.0.0',
                    'startAddress': '192.168.20.10', 'endAddress': '192.168.20.50',
                    'name': 'iscsi_nw', 'subnetUri': ' '}

mgmt_ipv4ranges = {'type': 'Range', 'networkId': '15.212.164.0',
                   'startAddress': '15.212.167.154', 'endAddress': '15.212.167.164',
                   'name': 'mgmt_nw', 'subnetUri': ' '}

sd_body = [{"encrypt": False, "errorCode": "CI", "userName": "administrator", "password": "admin123"}, {
    "encrypt": True, "errorCode": "CI", "userName": "backup", "password": "admin123"}, {"encrypt": False, "errorCode": "CI"}]

bin_file_loc = 'C:\\bin file\\'
ov_bin = 'HPEOneView-fullupdate-4.10.00-SNAPSHOT-0340528.bin'
ov_version_Check = '4.10.00-0340528'
i3s_bin = 'i3s-fullupdate-4.10.00-SNAPSHOT-0340283.bin'
i3s_version_Check = '4.10.00-0340283'
SPP_LOCATION = 'C:\\Builds\\terfs\\bp-2018-04-27-02.iso'
leupdate_body = [{"op": "replace",
                  "path": "/firmware",
                  "value": {"firmwareBaselineUri": ' ',
                            "forceInstallFirmware": True,
                            "firmwareUpdateOn": "SharedInfrastructureAndServerProfiles",
                            "logicalInterconnectUpdateMode": "Orchestrated",
                            "validateIfLIFirmwareUpdateIsNonDisruptive": False,
                            "updateFirmwareOnUnmanagedInterconnect": False}
                  }]

iscsi_network = {'vlanId': '1022', 'networkId': '192.168.0.0',
                 'ethernetNetworkType': 'Tagged', 'subnetUri': '',
                 'purpose': 'ISCSI', 'name': 'iscsi_nw',
                 'smartLink': False, 'privateNetwork': False,
                 'connectionTemplateUri': None, 'type': 'ethernet-networkV4'}

mgmt_network = {'vlanId': '0', 'networkId': '15.212.164.0',
                'ethernetNetworkType': 'Untagged', 'subnetUri': '',
                'purpose': 'Management', 'name': 'mgmt_nw',
                'smartLink': False, 'privateNetwork': False,
                'connectionTemplateUri': None, 'type': 'ethernet-networkV4'}

lig_tbird_3enc = {'type': 'logical-interconnect-groupV4',
                  'ethernetSettings': {'type': 'EthernetInterconnectSettingsV4', 'enableIgmpSnooping': False,
                                       'igmpIdleTimeoutInterval': 260, 'enableFastMacCacheFailover': True, 'macRefreshInterval': 5,
                                       'enableNetworkLoopProtection': True, 'enablePauseFloodProtection': True,
                                       'enableRichTLV': False, 'interconnectType': 'Ethernet', 'dependentResourceUri': None,
                                       'name': 'defaultEthernetSwitchSettings', 'category': None, 'uri': '/ethernetSettings'},
                  'description': None,
                  'name': 'LIG-3enc',
                  'interconnectMapTemplate': [{'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
                                              {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
                                              {'bay': 6, 'enclosure': 1, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 1},
                                              {'bay': 3, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
                                              {'bay': 6, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
                                              {'bay': 3, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3}],
                  'enclosureType': 'SY12000',
                  'enclosureIndexes': [1, 2, 3],
                  'interconnectBaySet': '3',
                  'redundancyType': 'HighlyAvailable',
                  'internalNetworkUris': [],
                  'snmpConfiguration': {'type': 'snmp-configuration', 'v3Enabled': True, 'readCommunity': 'public', 'systemContact': '',
                                        'snmpAccess': None, 'enabled': True, 'description': None, 'name': None,
                                        'state': None, 'category': 'snmp-configuration'},
                  'qosConfiguration': None,
                  'uplinkSets': [
                      {'networkUris': ['iscsi_nw'], 'mode':'Auto', 'lacpTimer':'Short', 'primaryPort':None,
                       'logicalPortConfigInfos':[{'enclosure': '1', 'bay': '3', 'port': 'Q1:1', 'speed': 'Auto'},
                                                 {'enclosure': '1', 'bay': '3', 'port': 'Q2:1', 'speed': 'Auto'},
                                                 {'enclosure': '2', 'bay': '6', 'port': 'Q1:1', 'speed': 'Auto'},
                                                 {'enclosure': '2', 'bay': '6', 'port': 'Q2:1', 'speed': 'Auto'}],

                       'name': 'uplink_3encl', 'networkType': 'Ethernet',
                       'ethernetNetworkType': 'ImageStreamer'},
                      {'networkUris': ['mgmt_nw'], 'mode':'Auto',
                       'lacpTimer':'Short', 'primaryPort':None,
                       'nativeNetworkUri': None,
                          'logicalPortConfigInfos':[{'enclosure': '1', 'bay': '3', 'port': 'Q4:1', 'speed': 'Auto'}],
                          'networkType': 'Ethernet', 'ethernetNetworkType': 'Untagged', 'name': 'uplink_2'}]}

enc_groups_tbird_3enc = {'name': 'EG-3enc', 'powerMode': 'RedundantPowerFeed',
                         'ambientTemperatureMode': 'Standard', 'ipAddressingMode': 'External',
                         'ipRangeUris': [], 'enclosureCount': 3,
                         'configurationScript': None,
                         'osDeploymentSettings': {'manageOSDeployment': True,
                                                  'deploymentModeSettings': {'deploymentMode': 'Internal', 'deploymentNetworkUri': None}},
                         'interconnectBayMappings': [{'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG-3enc'},
                                                     {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG-3enc'}]}

les_3enc = {'name': 'LE-3enc',
            'enclosureUris': ['ENC:SGH736WTHX', 'ENC:SGH736WTHV', 'ENC:SGH736WTHW', ],
            'enclosureGroupUri': 'EG:EG-3enc', 'firmwareBaselineUri': None,
            'forceInstallFirmware': False}

osdeploymentserver = {'name': 'OSDS-3enc', 'description': 'os deployment server',
                      'applianceUri': 'SGH736WTHW, appliance 2', 'mgmtNetworkUri': ['mgmt_nw'],
                      'deplManagersType': 'Image Streamer'}

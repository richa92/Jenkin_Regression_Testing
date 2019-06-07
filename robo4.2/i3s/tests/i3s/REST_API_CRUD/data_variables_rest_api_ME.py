# from winnt import NULL
# from requests.api import patch
"""
REST_API_CRUD_DataFile
"""
admin_credentials = {'userName': 'Administrator', 'password': 'admin123'}

# used for SPT creation
networks = {'iscsi': 'iscsi_nw', 'mgmt': 'mgmt_nw'}
# used for SPT creation
egs = [{'enclosureGroupUri': 'EG'}]
# used for SPT creation
servers = [{'serverHardwareUri': 'SGH750SF2K, bay 2', 'serverHardwareTypeUri': 'SY 660 Gen9 2'},
           {'serverHardwareUri': 'SGH750SF2H, bay 1', 'serverHardwareTypeUri': 'SY 660 Gen9 2'},
           {'serverHardwareUri': 'SGH750SF2H, bay 2', 'serverHardwareTypeUri': 'SY 660 Gen9 2'}]

serverHardwareUri = "SGH750SF2J, bay 6"
serverHardwareTypeUri = "SY 480 Gen10 1"
enclosureGroupUri = "EG"
enclosureUri = "SGH750SF2J"
networkUri_iscsi = "iscsi_nw"
networkUri_mgmt = "mgmt_nw"

mgmt_subnet = '15.212.164.0'                                                                  # mgmt n/wk subnet
deploy_subnet = '192.168.0.0'                                                                 # deploy n/wk subnet

mgmt_ip_range = 'mgmt_nw'                                                                     # mgmt ip range name
deploy_ip_range = 'iscsi_nw'                                                                  # deployment ip range name

mgmt_network_name = 'mgmt_nw'                                                                 # mgmt n/wk name
deploy_network_name = 'iscsi_nw'                                                              # deployment n/wk name

subnet = [{'type': 'Subnet',
           'gateway': '192.168.0.1',
           'networkId': '192.168.0.0',
           'subnetmask': '255.255.0.0',
           'dnsServers': [],
           'domain': 'vse.rdlabs.hpecorp.net'},
          {'type': 'Subnet',
           'gateway': '15.212.164.1',
           'networkId': '15.212.164.0',
           'subnetmask': '255.255.252.0',
           'dnsServers': [
               '16.110.135.51',
               '16.110.135.52'],
           'domain': 'vse.rdlabs.hpecorp.net'}]

range_enable = [{'type': 'Range',
                 'enabled': 'true'}]
range_disable = [{'type': 'Range',
                  'enabled': 'false'}]

ipv4ranges = [{'type': 'Range',
               'startAddress': '192.168.20.10',
               'endAddress': '192.168.20.50',
               'name': 'iscsi_nw',
               'subnetUri': ' '},
              {'type': 'Range',
               'startAddress': '15.212.167.154',
               'endAddress': '15.212.167.164',
               'name': 'mgmt_nw',
               'subnetUri': ' '}]

Ethernet_network = [{'vlanId': '149',
                     'ethernetNetworkType': 'Tagged',
                     'subnetUri': '',
                     'purpose': 'ISCSI',
                     'name': 'iscsi_nw',
                     'smartLink': False,
                     'privateNetwork': False,
                     'connectionTemplateUri': None,
                     'type': 'ethernet-networkV4'},
                    {'vlanId': '0',
                     'ethernetNetworkType': 'Untagged',
                     'subnetUri': '',
                     'purpose': 'Management',
                     'name': 'mgmt_nw',
                     'smartLink': False,
                     'privateNetwork': False,
                     'connectionTemplateUri': None,
                     'type': 'ethernet-networkV4'}]

osdeploymentserver = {'name': 'OSDS',
                      'description': 'OS Deployment Server',
                      'applianceUri': 'SGH750SF2K, appliance 2',
                      'mgmtNetworkUri': ['mgmt_nw'],
                      'deplManagersType': 'Image Streamer'}

osdeploymentserver_update = [{
    'type': 'DeploymentManager',
    'primaryActiveAppliance': '',
    'deplManagersType': 'Image Streamer',
    'description': 'os deployment server update',
    'category': 'deployment-managers',
    'name': 'OSDS',
    'id': '',
    'uri': ''}]

logical_interconnect_group = [{'type': 'logical-interconnect-groupV7',
                               'ethernetSettings': {'type': 'EthernetInterconnectSettingsV6', 'enableIgmpSnooping': False, 'igmpIdleTimeoutInterval': 260, 'enableFastMacCacheFailover': True, 'macRefreshInterval': 5, 'enableNetworkLoopProtection': True, 'enablePauseFloodProtection': True, 'enableRichTLV': False, 'interconnectType': 'Ethernet', 'dependentResourceUri': None, 'name': 'defaultEthernetSwitchSettings', 'category': None, 'uri': '/ethernetSettings'},
                               'description': None,
                               'name': 'LIG',
                               'interconnectMapTemplate':
                               {'interconnectMapEntryTemplates': [
                                   {'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Enclosure', 'relativeValue': 1}]}, 'permittedInterconnectTypeUri': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
                                   {'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 6}, {'type': 'Enclosure', 'relativeValue': 2}]}, 'permittedInterconnectTypeUri': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
                                   {'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 6}, {'type': 'Enclosure', 'relativeValue': 1}]}, 'permittedInterconnectTypeUri': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 1},
                                   {'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Enclosure', 'relativeValue': 2}]}, 'permittedInterconnectTypeUri': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
                                   {'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 6}, {'type': 'Enclosure', 'relativeValue': 3}]}, 'permittedInterconnectTypeUri': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
                                   {'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Enclosure', 'relativeValue': 3}]}, 'permittedInterconnectTypeUri': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3}]},
                               'enclosureType': 'SY12000',
                               'enclosureIndexes': [1, 2, 3],
                               'interconnectBaySet': '3',
                               'redundancyType': 'HighlyAvailable',
                               'internalNetworkUris': [],
                               'snmpConfiguration': {'type': 'snmp-configuration', 'readCommunity': '', 'systemContact': '', 'trapDestinations': None, 'snmpAccess': None, 'enabled': False, 'description': None, 'name': None, 'state': None, 'v3Enabled': True, 'category': 'snmp-configuration'},
                               'qosConfiguration': None,
                               'uplinkSets': [
                                   {'networkUris': networkUri_iscsi, 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                    'logicalPortConfigInfos': [{'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 62}, {'type': 'Enclosure', 'relativeValue': 1}]}},
                                                               {'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 6}, {'type': 'Port', 'relativeValue': 62}, {'type': 'Enclosure', 'relativeValue': 2}]}},
                                                               {'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 63}, {'type': 'Enclosure', 'relativeValue': 1}]}},
                                                               {'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 6}, {'type': 'Port', 'relativeValue': 63}, {'type': 'Enclosure', 'relativeValue': 2}]}}],
                                    'networkType': 'Ethernet', 'ethernetNetworkType': 'ImageStreamer', 'name': 'uplink_3encl'},
                                   {'networkUris': networkUri_mgmt, 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                    'logicalPortConfigInfos': [
                                        {'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 77}, {'type': 'Enclosure', 'relativeValue': 1}]}}],
                                    'networkType': 'Ethernet', 'ethernetNetworkType': 'Untagged', 'name': 'mgmt_3encl'}]},
                              {'type': 'logical-interconnect-groupV7',
                               'ethernetSettings': {'type': 'EthernetInterconnectSettingsV6', 'enableIgmpSnooping': False, 'igmpIdleTimeoutInterval': 260, 'enableFastMacCacheFailover': True, 'macRefreshInterval': 5, 'enableNetworkLoopProtection': True, 'enablePauseFloodProtection': True, 'enableRichTLV': False, 'interconnectType': 'Ethernet', 'dependentResourceUri': None, 'name': 'defaultEthernetSwitchSettings', 'category': None, 'uri': '/ethernetSettings'},
                               'description': None,
                               'name': 'LIG-for-EG-update',
                               'interconnectMapTemplate':
                               {'interconnectMapEntryTemplates': [
                                   {'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Enclosure', 'relativeValue': 1}]}, 'permittedInterconnectTypeUri': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
                                   {'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 6}, {'type': 'Enclosure', 'relativeValue': 2}]}, 'permittedInterconnectTypeUri': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
                                   {'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 6}, {'type': 'Enclosure', 'relativeValue': 1}]}, 'permittedInterconnectTypeUri': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 1},
                                   {'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Enclosure', 'relativeValue': 2}]}, 'permittedInterconnectTypeUri': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
                                   {'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 6}, {'type': 'Enclosure', 'relativeValue': 3}]}, 'permittedInterconnectTypeUri': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
                                   {'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Enclosure', 'relativeValue': 3}]}, 'permittedInterconnectTypeUri': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3}]},
                               'enclosureType': 'SY12000',
                               'enclosureIndexes': [1, 2, 3],
                               'interconnectBaySet': '3',
                               'redundancyType': 'HighlyAvailable',
                               'internalNetworkUris': [],
                               'snmpConfiguration': {'type': 'snmp-configuration', 'readCommunity': '', 'systemContact': '', 'trapDestinations': None, 'snmpAccess': None, 'enabled': False, 'description': None, 'name': None, 'state': None, 'v3Enabled': True, 'category': 'snmp-configuration'},
                               'qosConfiguration': None,
                               'uplinkSets': [
                                   {'networkUris': networkUri_iscsi, 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                    'logicalPortConfigInfos': [{'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 62}, {'type': 'Enclosure', 'relativeValue': 1}]}},
                                                               {'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 6}, {'type': 'Port', 'relativeValue': 62}, {'type': 'Enclosure', 'relativeValue': 2}]}},
                                                               {'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 63}, {'type': 'Enclosure', 'relativeValue': 1}]}},
                                                               {'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 6}, {'type': 'Port', 'relativeValue': 63}, {'type': 'Enclosure', 'relativeValue': 2}]}}],
                                    'networkType': 'Ethernet', 'ethernetNetworkType': 'ImageStreamer', 'name': 'uplink_3enc'},
                                   {'networkUris': networkUri_mgmt, 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                    'logicalPortConfigInfos': [{'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 77}, {'type': 'Enclosure', 'relativeValue': 1}]}}],
                                    'networkType': 'Ethernet', 'ethernetNetworkType': 'Untagged', 'name': 'mgmt_3enc'}]},
                              {'type': 'logical-interconnect-groupV7',
                               'ethernetSettings': {'type': 'EthernetInterconnectSettingsV6', 'enableIgmpSnooping': False, 'igmpIdleTimeoutInterval': 260, 'enableFastMacCacheFailover': True, 'macRefreshInterval': 5, 'enableNetworkLoopProtection': True, 'enablePauseFloodProtection': True, 'enableRichTLV': False, 'interconnectType': 'Ethernet', 'dependentResourceUri': None, 'name': 'defaultEthernetSwitchSettings', 'category': None, 'uri': '/ethernetSettings'},
                               'description': None,
                               'name': 'LIG-new',
                               'interconnectMapTemplate':
                               {'interconnectMapEntryTemplates': [
                                   {'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Enclosure', 'relativeValue': 1}]}, 'permittedInterconnectTypeUri': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
                                   {'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 6}, {'type': 'Enclosure', 'relativeValue': 2}]}, 'permittedInterconnectTypeUri': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
                                   {'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 6}, {'type': 'Enclosure', 'relativeValue': 1}]}, 'permittedInterconnectTypeUri': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 1},
                                   {'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Enclosure', 'relativeValue': 2}]}, 'permittedInterconnectTypeUri': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
                                   {'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 6}, {'type': 'Enclosure', 'relativeValue': 3}]}, 'permittedInterconnectTypeUri': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
                                   {'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Enclosure', 'relativeValue': 3}]}, 'permittedInterconnectTypeUri': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3}]},
                               'enclosureType': 'SY12000',
                               'enclosureIndexes': [1, 2, 3],
                               'interconnectBaySet': '3',
                               'redundancyType': 'HighlyAvailable',
                               'internalNetworkUris': [],
                               'snmpConfiguration': {'type': 'snmp-configuration', 'readCommunity': 'public', 'systemContact': '', 'trapDestinations': None, 'snmpAccess': None, 'enabled': False, 'description': None, 'name': None, 'state': None, 'v3Enabled': True, 'category': 'snmp-configuration'},
                               'qosConfiguration': None,
                               'uplinkSets': [
                                   {'networkUris': networkUri_mgmt, 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                    'logicalPortConfigInfos': [
                                        {'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 66}, {'type': 'Enclosure', 'relativeValue': 1}]}},
                                        {'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 6}, {'type': 'Port', 'relativeValue': 66}, {'type': 'Enclosure', 'relativeValue': 2}]}}],
                                    'networkType': 'Ethernet', 'ethernetNetworkType': 'Untagged', 'name': 'mgmt_3encl'}]}]

logical_interconnect_group_update_uplink = {'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 6}, {'type': 'Port', 'relativeValue': 77}, {'type': 'Enclosure', 'relativeValue': 2}]}}

enclosure_group = [{
    'name': 'EG',
    'ambientTemperatureMode': 'Standard',
    'enclosureCount': 3,
    'ipAddressingMode': 'External',
    'ipRangeUris': [],
    'powerMode': 'RedundantPowerFeed',
    'osDeploymentSettings':{'manageOSDeployment': True, 'deploymentModeSettings': {'deploymentMode': 'Internal', 'deploymentNetworkUri': ''}},
    'interconnectBayMappings': [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                                {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                                {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG'},
                                {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                                {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                                {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG'}]}]

enclosure_group_update = [
    {'name': 'EG-update'},
    {'name': 'EG',
     'ambientTemperatureMode': 'Standard',
     'enclosureCount': 3,
     'ipAddressingMode': 'External',
     'ipRangeUris': [],
     'powerMode': 'RedundantPowerFeed',
     'enclosureCount': 3,
     'osDeploymentSettings':{'manageOSDeployment': True, 'deploymentModeSettings': {'deploymentMode': 'Internal', 'deploymentNetworkUri': ''}},
     'interconnectBayMappings': [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                                 {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                                 {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG-for-EG-update'},
                                 {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                                 {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                                 {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG-for-EG-update'}]}]

logical_enclosure = {'name': 'LE',
                     'enclosureUris': ['ENC:SGH750SF2J', 'ENC:SGH750SF2K', 'ENC:SGH750SF2H'],
                     'enclosureGroupUri': 'EG:EG',
                     'firmwareBaselineUri': None,
                     'forceInstallFirmware': False}

logical_enclosure_update = [{'name': 'LE',
                             'enclosureUris': ['ENC:SGH708YL3F', 'ENC:SGH708YL3C', 'ENC:SGH708YL3H'],
                             'enclosureGroupUri': 'EG:EG',
                             'firmwareBaselineUri': None,
                             'forceInstallFirmware': False}]

goldenimage_add = [{'name': 'Goldenimage',
                    'description': '',
                    'file': "valid_file"}]

goldenimage_update = [{'name': 'Goldenimage_RESTAPI',
                       'description': 'Golden_Image_update',
                       'file': "valid_file"}]

goldenimage_delete = [{'name': 'Goldenimage_RESTAPI'}]

goldenimage_create = [{
    'type': 'GoldenImage',
    'name': 'Captured GoldenImage',
    'description': 'GI Capture',
    'imageCapture': 'true',
    'osVolumeURI': 'serverprofile_RESTAPI_update',
    'buildPlanUri': 'HPE - ESXi - generalize full state - 2018-07-31'}]

artifactbundle_create = [{
    'name': 'Artifact_Bundle from create call for RESTAPI',
    'description': 'ab from Deploymentplans',
    'deploymentPlans': [{'resourceUri': 'Deploymentplan for MGMT NIC attributes'}]}]

artifactbundle_add = [{
    'name': 'C:/Goldenimage/HPE-ESXi-2018-12-02-v5.0.zip'}]

artifactbundle_extract = [{
    'name': 'HPE-ESXi-2018-12-02-v5.0'}]

artifactbundle_update = [{
    'name': 'Artifact_Bundle from create call name update'}]

artifactbundle_delete = [{'name': 'HPE-ESXi-2018-12-02-v5.0'}]

planscript_create = [
    {"type": "PlanScript",
     "description": "Planscript for deploy",
     "name": "Planscript_for_deploy",
     "hpProvided": 'false',
     "planType": "deploy",
     "content": "echo \"Network values\"\necho \"ManagementNIC1\"\necho @ManagementNIC1.mac@\necho @ManagementNIC1.vlanid@\necho @ManagementNIC1.ipaddress@\necho @ManagementNIC1.netmask@\necho @ManagementNIC1.gateway@\necho @ManagementNIC1.dns1@\necho @ManagementNIC1.dns2@\n\necho \"########################################\"\necho \"Configure ESXi host management network-NIC1\"\necho \"########################################\"\n\necho \"Check Image Streamer capture details\"\n-download /ImageStreamerCapture ./ImageStreamerCapture\n\nupload -<<END /ImageStreamer/check_capture\n#!/bin/bash\nif [ -f ./ImageStreamerCapture ]; then\n    echo \"Capture details:\"\n    cat ./ImageStreamerCapture\nelse\n    echo\n    echo \"WARNING: ESXi Golden Image was not captured by Image Streamer.\"\n    echo \"Golden Image may not be prepared for correct personalization.\"\n    echo \"Recommend deploying Golden Image as is and capturing a new\"\n    echo \"Golden Image using Image Streamer via correct capture Build Plan\"\n    echo\nfi\necho\nEND\ndownload /ImageStreamer/check_capture ./check_capture\n!source ./check_capture\n\n-rm-f /ImageStreamerCapture\n\nupload -<<END /ImageStreamer/esxi_mgmt_net\n#! /bin/bash\n\ncat <<\"EOF\" >>local.sh\n# HPE Image Streamer ESXi host configuration\nesxcli system syslog mark --message \"HPE Image Streamer ESXi host configuration for @Hostname1@\"\n\n# Image Streamer management network configuration\nesxcli system hostname set --host \"@Hostname1@\"\nesxcli system hostname set --domain \"@DomainName1@\"\n\nVMK1=vmk2\nUPLINK1=`esxcli network nic list | grep -i \"@ManagementNIC1.mac@\" | awk \'{ print $1 }\'`\n\nesxcli network vswitch standard add --vswitch-name=vSwitch1\n\nesxcli network vswitch standard portgroup add --portgroup-name=ManagementNetwork1 --vswitch-name=vSwitch1\n\nesxcfg-vswitch vSwitch1 -v @ManagementNIC1.vlanid:0@ -p ManagementNetwork1\n\nesxcli network vswitch standard uplink add --uplink-name=$UPLINK1 --vswitch-name=vSwitch1\n\nesxcli network ip interface add --interface-name=$VMK1 --portgroup-name=ManagementNetwork1\n\nEOF\n\nif [[ \"@ManagementNIC1.mac@\" != \"none\" ]]; then\n\nif [[ \"@ManagementNIC1.ipaddress@\" =~ [0-9]*\\.[0-9]*\\.[0-9]*\\.[0-9]* ]]; then\n\necho \"Configure ESXi host management network for static IP\"\ncat <<\"EOF\" >>local.sh\nesxcli network ip interface ipv4 set --interface-name=$VMK1 --ipv4=@ManagementNIC1.ipaddress@ --netmask=@ManagementNIC1.netmask@ --type=static\n\nesxcli network ip route ipv4 add --gateway \"@ManagementNIC1.gateway@\" --network default\nesxcli network ip dns server add --server=@ManagementNIC1.dns1@\nesxcli network ip dns server add --server=@ManagementNIC1.dns2@\n\nEOF\n\nelse\n\necho \"Configure ESXi host management network for DHCP\"\ncat <<\"EOF\" >>local.sh\nesxcli network ip  interface ipv4 set --interface-name=$VMK1 --type=dhcp   \n\nEOF\nfi\n\nelse\necho \"mac address of management nic1 : @ManagementNIC1.mac@\"\n\nfi\n\nexit 0\nEND\n\ndownload /ImageStreamer/esxi_mgmt_net ./esxi_mgmt_net\necho \"Run esxi_mgmt_net\"\n!source ./esxi_mgmt_net\necho \"Configure host management complete\""},
    {"type": "PlanScript",
     "description": "Planscript_for_capture",
     "name": "ps_type_capture",
     "hpProvided": "false",
     "planType": "capture",
     "content": "# (C) Copyright 2015-2015 Hewlett-Packard Development Company, L.P.\r\n# Script to mount disk in libguesfs virtual appliance for personalizaiton or generalization\r\nmount /dev/sda5 /\r\n\r\n\r\n# creating tmp dir at local filesystem\r\n!mkdir -p ./onetime\r\n!mkdir -p ./state/local\r\n\r\n# copying required files for personalization/generalization to local filesysystem\r\n-copy-out /onetime.tgz .\r\n-copy-out /state.tgz .\r\n-copy-out /boot.cfg .\r\n\r\n# trying to findout whether onetime.tgz will be picked up during booting or state.tgz will be picked\r\n# based on that we can process either onetime.tgz or state.tgz for personalization/generalization\r\n\r\n-!grep \"onetime.tgz\"  ./boot.cfg >./onetime_found\r\n-!grep \"state.tgz\" ./boot.cfg > ./state_found\r\necho \"########################################\"\r\necho \"Generalize host configuration\"\r\necho \"########################################\"\r\n\r\necho \"Empty jumpstrt.tgz archive to remove any configuration left over from install\"\r\nrm /jumpstrt.gz\r\ntouch /jumpstrt\r\ncompress-out gzip /jumpstrt ./jumpstrt.gz\r\nrm /jumpstrt\r\nupload ./jumpstrt.gz /jumpstrt.gz\r\n!rm ./jumpstrt.gz\r\necho\r\n\r\necho \"Empty useropts.gz archive to remove special user configuration\"\r\nrm /useropts.gz\r\ntouch /useropts\r\ncompress-out gzip /useropts ./useropts.gz\r\nrm /useropts\r\nupload ./useropts.gz /useropts.gz\r\n!rm ./useropts.gz\r\necho \r\n\r\necho \"Remove state.tgz archive which holds host configuration\"\r\nrm-f /state.tgz\r\necho \r\n\r\necho \"Download boot.cfg\"\r\ndownload /boot.cfg ./boot.cfg\r\necho\r\n\r\necho \"Construct boot.cfg configuration script\"\r\nupload -<<END /boot_cfg_configure\r\n#!/bin/bash\r\n\r\necho\r\necho \"Original boot.cfg:\"\r\ncat boot.cfg\r\necho\r\n\r\ncp boot.cfg boot.cfg.bak\r\n\r\nsed '/^kernelopt=.*installerDiskDumpSlotSize=/ {\r\n         s/\\(kernelopt=\\).*\\(installerDiskDumpSlotSize=[0-9]*\\).*/\\1 \\2/; n }\r\n     /^kernelopt=/ {\r\n         s/.*/kernelopt=/ }\r\n     /^modules=/ {\r\n         s/--- state.tgz/--- onetime.tgz/ }\r\n    ' < boot.cfg.bak > boot.cfg\r\n\r\nrm boot.cfg.bak\r\n\r\necho \"New boot.cfg:\"\r\ncat boot.cfg\r\necho\r\n\r\necho \"Construct ImageStreamerCapture details file\"\r\necho \"HPE Image Streamer Capture for ESXi 5\" > ./ImageStreamerCapture\r\necho \"Complete generalization by host state removal\" >> ./ImageStreamerCapture\r\ndate >> ./ImageStreamerCapture\r\n\r\nexit 0\r\nEND\r\necho \r\n\r\necho \"Run boot.cfg configuration script\"\r\ndownload /boot_cfg_configure ./boot_cfg_configure\r\n!source ./boot_cfg_configure\r\nrm-f /boot_cfg_configure\r\necho\r\n\r\necho \"Replace boot.cfg\"\r\nupload ./boot.cfg /boot.cfg\r\necho\r\n\r\necho \"Save capture details in Golden Image\"\r\nupload  ./ImageStreamerCapture  /ImageStreamerCapture\r\necho\r\n# (C) Copyright 2015-2015 Hewlett-Packard Development Company, L.P.\r\n# Script to Unmount\r\n\r\n-copy-in onetime.tgz /\r\n-copy-in state.tgz /\r\numount /"}]

planscript_update = [{
    "type": "PlanScript",
    "description": "Planscript update description",
    "name": "Planscript_for_deploy_update",
    "hpProvided": 'false',
    "planType": "deploy",
    "content": "echo \"Network values\"\necho \"ManagementNIC1\"\necho @ManagementNIC1.mac@\necho @ManagementNIC1.vlanid@\necho @ManagementNIC1.ipaddress@\necho @ManagementNIC1.netmask@\necho @ManagementNIC1.gateway@\necho @ManagementNIC1.dns1@\necho @ManagementNIC1.dns2@\n\necho \"########################################\"\necho \"Configure ESXi host management network-NIC1\"\necho \"########################################\"\n\necho \"Check Image Streamer capture details\"\n-download /ImageStreamerCapture ./ImageStreamerCapture\n\nupload -<<END /ImageStreamer/check_capture\n#!/bin/bash\nif [ -f ./ImageStreamerCapture ]; then\n    echo \"Capture details:\"\n    cat ./ImageStreamerCapture\nelse\n    echo\n    echo \"WARNING: ESXi Golden Image was not captured by Image Streamer.\"\n    echo \"Golden Image may not be prepared for correct personalization.\"\n    echo \"Recommend deploying Golden Image as is and capturing a new\"\n    echo \"Golden Image using Image Streamer via correct capture Build Plan\"\n    echo\nfi\necho\nEND\ndownload /ImageStreamer/check_capture ./check_capture\n!source ./check_capture\n\n-rm-f /ImageStreamerCapture\n\nupload -<<END /ImageStreamer/esxi_mgmt_net\n#! /bin/bash\n\ncat <<\"EOF\" >>local.sh\n# HPE Image Streamer ESXi host configuration\nesxcli system syslog mark --message \"HPE Image Streamer ESXi host configuration for @Hostname1@\"\n\n# Image Streamer management network configuration\nesxcli system hostname set --host \"@Hostname1@\"\nesxcli system hostname set --domain \"@DomainName1@\"\n\nVMK1=vmk2\nUPLINK1=`esxcli network nic list | grep -i \"@ManagementNIC1.mac@\" | awk \'{ print $1 }\'`\n\nesxcli network vswitch standard add --vswitch-name=vSwitch1\n\nesxcli network vswitch standard portgroup add --portgroup-name=ManagementNetwork1 --vswitch-name=vSwitch1\n\nesxcfg-vswitch vSwitch1 -v @ManagementNIC1.vlanid:0@ -p ManagementNetwork1\n\nesxcli network vswitch standard uplink add --uplink-name=$UPLINK1 --vswitch-name=vSwitch1\n\nesxcli network ip interface add --interface-name=$VMK1 --portgroup-name=ManagementNetwork1\n\nEOF\n\nif [[ \"@ManagementNIC1.mac@\" != \"none\" ]]; then\n\nif [[ \"@ManagementNIC1.ipaddress@\" =~ [0-9]*\\.[0-9]*\\.[0-9]*\\.[0-9]* ]]; then\n\necho \"Configure ESXi host management network for static IP\"\ncat <<\"EOF\" >>local.sh\nesxcli network ip interface ipv4 set --interface-name=$VMK1 --ipv4=@ManagementNIC1.ipaddress@ --netmask=@ManagementNIC1.netmask@ --type=static\n\nesxcli network ip route ipv4 add --gateway \"@ManagementNIC1.gateway@\" --network default\nesxcli network ip dns server add --server=@ManagementNIC1.dns1@\nesxcli network ip dns server add --server=@ManagementNIC1.dns2@\n\nEOF\n\nelse\n\necho \"Configure ESXi host management network for DHCP\"\ncat <<\"EOF\" >>local.sh\nesxcli network ip  interface ipv4 set --interface-name=$VMK1 --type=dhcp   \n\nEOF\nfi\n\nelse\necho \"mac address of management nic1 : @ManagementNIC1.mac@\"\n\nfi\n\nexit 0\nEND\n\ndownload /ImageStreamer/esxi_mgmt_net ./esxi_mgmt_net\necho \"Run esxi_mgmt_net\"\n!source ./esxi_mgmt_net\necho \"Configure host management complete\""}]

buildplan_create = [
    {  # 1 BP having CA as SSH
        'type': 'OeBuildPlanV5',
        'customAttributes': [{
            'constraints': '{"options":["enabled"]}',
            'description': 'ssh is enabled',
            'name': 'SSH',
            'value': 'enabled',
            'type': 'option'}],
        'buildStep': [{'planScriptUri': 'HPE - ESXi - mount - 2018-07-31', 'parameters': None, 'serialNumber': '1'},
                      {'planScriptUri': 'HPE - ESXi - unpack state - 2017-07-07', 'parameters': None, 'serialNumber': '2'},
                      {'planScriptUri': 'HPE - ESXi - configure ssh - 2017-12-15', 'parameters': None, 'serialNumber': '3'},
                      {'planScriptUri': 'HPE - ESXi - repack state - 2017-03-15', 'parameters': None, 'serialNumber': '4'},
                      {'planScriptUri': 'HPE - ESXi - umount - 2017-03-15', 'parameters': None, 'serialNumber': '5'}],
        'hpProvided': False,
        'oeBuildPlanType': 'deploy',
        'description': 'Create BP',
        'name': 'Buildplan for SSH'},
    {  # 2 BP having CA as password
        'type': 'OeBuildPlanV5',
        'customAttributes': [{
            'constraints': '{}',
            'description': 'passwd',
            'name': 'Password',
            'value': "",
            'type': 'password'}],
        'buildStep': [{'planScriptUri': 'HPE - ESXi - mount - 2018-07-31', 'parameters': None, 'serialNumber': '1'},
                      {'planScriptUri': 'HPE - ESXi - unpack state - 2017-07-07', 'parameters': None, 'serialNumber': '2'},
                      {'planScriptUri': 'HPE - ESXi - set password - 2017-03-15', 'parameters': None, 'serialNumber': '3'},
                      {'planScriptUri': 'HPE - ESXi - repack state - 2017-03-15', 'parameters': None, 'serialNumber': '4'},
                      {'planScriptUri': 'HPE - ESXi - umount - 2017-03-15', 'parameters': None, 'serialNumber': '5'}],
        'hpProvided': False,
        'oeBuildPlanType': 'deploy',
        'description': 'Create BP',
        'name': 'Buildplan for Password'},
    {  # 3 BP for capture
        'type': 'OeBuildPlanV5',
        'dependentArtifacts': None,
        'customAttributes': [],
        'buildStep': [{'planScriptUri': 'HPE - ESXi - mount - 2018-07-31', 'parameters': None, 'serialNumber': '1'},
                      {'planScriptUri': 'ps_type_capture', 'parameters': None, 'serialNumber': '2'},
                      {'planScriptUri': 'HPE - ESXi - umount - 2017-03-15', 'parameters': None, 'serialNumber': '3'}],
        'hpProvided': False,
        'oeBuildPlanType': 'capture',
        'description': 'Create Build Plan with type capture',
        'name': 'Buildplan for capture'}]

buildplan_update = [{  # Update name and Description
    'description': 'Update BP',
    'name': 'Update Buildplan name'}]

deploymentplan_create = [{  # 1 Valid DP having CA as SSH
    'type': 'OEDeploymentPlanV5',
    'hpProvided': False,
    'customAttributes': [{
        'visible': True,
        'constraints': '{"options":["enabled"]}',
        'editable': True,
        'description': 'ssh',
        'name': 'SSH',
        'value': 'enabled',
        'type': 'option'
    }],
    'goldenImageURI': 'Goldenimage_RESTAPI',
    'oeBuildPlanURI': 'Buildplan for SSH',
    'category': 'oe-deployment-plans',
    'description': 'Deployment Plan with ssh as custom attribute',
    'name': 'Deploymentplan for SSH'
}, {  # 2 Valid DP having CA as Passwd
    'type': 'OEDeploymentPlanV5',
    'hpProvided': False,
    'customAttributes': [{
        'visible': True,
        'constraints': '{}',
        'editable': True,
        'description': 'passwd',
        'name': 'Password',
        'value': 'Welcome123',
        'type': 'password'
    }],
    'goldenImageURI': 'Goldenimage_RESTAPI',
    'oeBuildPlanURI': 'Buildplan for Password',
    'category': 'oe-deployment-plans',
    'description': 'Deployment Plan with Passwd as custom attribute',
    'name': 'Deploymentplan for Password'
}, {  # 3 Valid DP having MGMG NIC attributes
    'type': 'OEDeploymentPlanV5',
    'hpProvided': False,
    'customAttributes': [{
        'visible': True,
        'constraints': '{"helpText":""}',
        'editable': True,
        'description': 'domain name',
        'name': 'DomainName',
        'value': 'hpe.com',
        'type': 'fqdn'
    }, {
        'visible': True,
        'constraints': '{"helpText":""}',
        'editable': True,
        'description': 'host name',
        'name': 'Hostname',
        'value': 'myhost',
        'type': 'hostname'
    }, {
        'visible': True,
        'constraints': '{"options":["enabled"]}',
        'editable': True,
        'description': 'Configure ssh',
        'name': 'SSH',
        'value': 'enabled',
        'type': 'option'
    }, {
        'visible': True,
        'constraints': '{}',
        'editable': True,
        'description': 'Passwd',
        'name': 'Password',
        'value': 'Welcome123',
        'type': 'password'
    }, {
        'visible': True,
        'constraints': '{"ipv4static":true,"ipv4dhcp":true,"ipv4disable":false,"parameters":["dns1","dns2","gateway","ipaddress","mac","netmask","vlanid"]}',
        'editable': True,
        'description': 'MGMT',
        'name': 'ManagementNIC',
        'value': '',
        'type': 'nic'
    }],
    'goldenImageURI': 'Goldenimage_RESTAPI',
    'oeBuildPlanURI': 'HPE- ESXi - deploy in single frame non-HA config- 2018-07-31',
    'category': 'oe-deployment-plans',
    'description': 'Deployment Plan having multiple custom attributes',
    'name': 'Deploymentplan for MGMT NIC attributes'
}]

deploymentplan_update = [{  # Update name and description
    'description': 'Deployment Plan update',
    'name': 'Deploymentplan name update'
}]

serverprofile_template_create = [{
    "type": "ServerProfileTemplateV7",
    "description": "server profile template for RESTAPI",
    "name": "Serverprofile_template having NIC attributes_RESTAPI",
    "serverProfileDescription": "server profile template",
    # "serverHardwareTypeUri": "SHT:" + servers[0]['serverHardwareTypeUri'],
    "serverHardwareTypeUri": 'SY 480 Gen10 1',
    # "enclosureGroupUri": "EG:" + egs[0]['enclosureGroupUri'],
    "enclosureGroupUri": 'EG',
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "connectionSettings": {"connections": [{"id": 1, "name": "Deployment Network A", "functionType": "Ethernet", "portId": "Mezz 3:1-a", "requestedMbps": "2500",
                                            "networkUri": 'ETH:' + networks['iscsi'], "requestedVFs": "Auto",
                                            "ipv4": {"ipAddressSource": "SubnetPool"},
                                            "boot": {"priority": "Primary", "ethernetBootType": "iSCSI",
                                                     "iscsi": {"initiatorNameSource": "ProfileInitiatorName", "firstBootTargetIp": None,
                                                               "secondBootTargetIp": "", "secondBootTargetPort": ""},
                                                     "bootVolumeSource": "UserDefined"}},
                                           {"id": 2, "name": "Deployment Network B", "functionType": "Ethernet", "portId": "Mezz 3:2-a", "requestedMbps": "2500",
                                            "networkUri": 'ETH:' + networks['iscsi'], "requestedVFs": "Auto",
                                            "ipv4": {"ipAddressSource": "SubnetPool"},
                                            "boot": {"priority": "Secondary", "ethernetBootType": "iSCSI",
                                                     "iscsi": {"initiatorNameSource": "ProfileInitiatorName", "firstBootTargetIp": None,
                                                               "secondBootTargetIp": "", "secondBootTargetPort": ""},
                                                     "bootVolumeSource": "UserDefined"}},
                                           {"id": 3, "name": "", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                            "networkUri": 'ETH:' + networks['mgmt'], "lagName": None, "isolatedTrunk": False, "requestedVFs": "0",
                                            "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}}],
                           "manageConnections": True,
                           "complianceControl": "Checked"},
    "osDeploymentSettings": {"osDeploymentPlanUri": "Deploymentplan for MGMT NIC attributes",
                             "osCustomAttributes": [{"name": "DomainName",
                                                     "value": "hpe.com",
                                                     "constraints": "{\"helpText\":\"\"}",
                                                     "type": "fqdn"},
                                                    {"name": "Hostname",
                                                     "value": "myhost",
                                                     "constraints": "{\"helpText\":\"\"}",
                                                     "type": "hostname"},
                                                    {"name": "ManagementNIC.connectionid",
                                                     "value": "3"},
                                                    {"name": "ManagementNIC.networkuri",
                                                     "value": 'ETH:' + networks['mgmt']},
                                                    {"name": "ManagementNIC.constraint",
                                                     "value": "auto"},
                                                    {"name": "ManagementNIC.vlanid",
                                                     "value": "0"},
                                                    {"name": "Password",
                                                     "value": "RESTAPI@321"},
                                                    {"name": "SSH",
                                                     "value": "enabled",
                                                     "constraints": "{\"options\":[\"enabled\"]}",
                                                     "type": "option"}],
                             "complianceControl": "Checked"},
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": "",
        "forceInstallFirmware": False,
        "complianceControl": "Checked"},
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"],
        "complianceControl": "Checked"},
    "bootMode": {
        "manageMode": True,
        "mode": "UEFIOptimized",
        "secureBoot": "Unmanaged",
        "pxeBootPolicy": "Auto",
        "complianceControl": "Checked"},
    "bios": {
        "manageBios": False,
        "overriddenSettings": [],
        "complianceControl": "Checked"},
    "managementProcessor": {
        "manageMp": False,
        "mpSettings": [],
        "complianceControl": "Checked"},
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [],
        "complianceControl": "CheckedMinimum"},
    "sanStorage": {'volumeAttachments': [], 'manageSanStorage':False}}]

serverprofile_from_spt = [{  # Create Server profile from SPT, having NIC attributes
    'type': 'ServerProfileV11',
    'name': 'serverprofile from spt',
    'description': 'sp',
    'iscsiInitiatorNameType': 'AutoGenerated',
    'serverProfileTemplateUri': 'Serverprofile_template having NIC attributes_RESTAPI',
    'serverHardwareUri': serverHardwareUri,
    'serverHardwareTypeUri': 'SY 480 Gen10 1',
    'enclosureGroupUri': 'EG',
    'enclosureUri': enclosureUri,
    'affinity': 'Bay',
    'hideUnusedFlexNics': True,
    'firmware': {'firmwareInstallType': None, 'forceInstallFirmware': False, 'manageFirmware': False, 'firmwareBaselineUri': None},
    'macType': 'Virtual',
    'wwnType': 'Virtual',
    'category': 'server-profiles',
    'connectionSettings': {
        'connections': [{'id': 1, 'name': 'Deployment Network A', 'functionType': 'Ethernet', 'networkUri': 'iscsi_nw',
                         'portId': 'Mezz 3:1-a', 'requestedVFs': 'Auto', 'requestedMbps': '2500',
                         'ipv4': {'ipAddressSource': 'SubnetPool'},
                         'boot': {'bootVolumeSource': 'UserDefined', 'priority': 'Primary', 'ethernetBootType': "iSCSI", 'iscsi': {'initiatorNameSource': 'ProfileInitiatorName'}}},
                        {'id': 2, 'name': 'Deployment Network B', 'functionType': 'Ethernet', 'networkUri': 'iscsi_nw',
                         'portId': 'Mezz 3:2-a', 'requestedVFs': 'Auto', 'requestedMbps': '2500',
                         'ipv4': {'ipAddressSource': 'SubnetPool'},
                         'boot': {'bootVolumeSource': 'UserDefined', 'priority': 'Secondary', 'ethernetBootType': "iSCSI", 'iscsi': {'initiatorNameSource': 'ProfileInitiatorName'}}},
                        {'id': 3, 'name': 'Blade_boot_mgmt', 'functionType': 'Ethernet', 'networkUri': 'mgmt_nw',
                         'portId': 'Mezz 3:1-c', 'requestedVFs': 0, 'requestedMbps': '2500',
                         'boot': {'priority': 'NotBootable', 'iscsi': {}}}]},
    'bootMode': {'manageMode': True, 'pxeBootPolicy': 'Auto', 'mode': 'UEFIOptimized'},
    'boot': {'manageBoot': True, 'order': ['HardDisk']},
    'bios':{'manageBios': False, 'overriddenSettings': []},
    'localStorage':{},
    'sanStorage': {'volumeAttachments': [], 'manageSanStorage':False},
    'osDeploymentSettings':{'osDeploymentPlanUri': 'Deploymentplan for MGMT NIC attributes',
                            'osCustomAttributes': [{'name': "DomainName", 'value': "hpe.com"},
                                                   {'name': "Hostname", 'value': "esxihost"},
                                                   {'name': "ManagementNIC.connectionid", 'value': "3"},
                                                   {'name': "ManagementNIC.dhcp", 'value': "false"},
                                                   {'name': "ManagementNIC.ipv4disable", 'value': "false"},
                                                   {'name': "ManagementNIC.networkuri", 'value': 'mgmt_nw'},
                                                   {'name': "ManagementNIC.constraint", 'value': "auto"},
                                                   {'name': "Password", 'value': 'RESTAPI@321'},
                                                   {'name': "SSH", 'value': "enabled"}], 'osVolumeUri': None}}]

Serverprofile_template_copy = [{
    'name': 'Copy_Serverprofile_template having NIC attributes_RESTAPI',
    'description': 'SPT Copy',
    'osDeploymentSettings': {'osDeploymentPlanUri': 'Deploymentplan name update',
                             'osCustomAttributes': [{'name': "SSH", 'value': "enabled"}]}}]

Serverprofile_template_edit = [{
    'name': 'Copy_Serverprofile_template having NIC attributes_RESTAPI_update',
    'description': 'SPT Update',
    'osDeploymentSettings': {'osDeploymentPlanUri': 'Deploymentplan for Password',
                             'osCustomAttributes': [{'name': "Password", 'value': 'RESTAPI@321'}]}}]

serverprofile_create = [{
    'type': 'ServerProfileV11',
    'name': 'serverprofile_RESTAPI',
    'description': 'sp',
    'iscsiInitiatorNameType': 'AutoGenerated',
    'serverProfileTemplateUri': None,
    'serverHardwareUri': serverHardwareUri,
    'serverHardwareTypeUri': 'SY 480 Gen10 1',
    'enclosureGroupUri': 'EG',
    'enclosureUri': enclosureUri,
    'affinity': 'Bay',
    'hideUnusedFlexNics': True,
    'firmware': {'firmwareInstallType': None, 'forceInstallFirmware': False, 'manageFirmware': False, 'firmwareBaselineUri': None},
    'macType': 'Virtual',
    'wwnType': 'Virtual',
    'category': 'server-profiles',
    'connectionSettings': {'reapplyState': 'NotApplying',
                           'connections': [{'id': 1, 'name': 'Deployment Network A', 'functionType': 'Ethernet', 'networkUri': 'iscsi_nw',
                                            'portId': 'Mezz 3:1-a', 'requestedVFs': 'Auto', 'requestedMbps': '2500', 'allocatedVFs': 64, 'macType': 'Virtual', 'wwpnType': 'Virtual', 'mac': '',
                                            'allocatedMbps': 2500, 'maximumMbps': 10000,
                                            'boot': {'bootVolumeSource': 'UserDefined', 'priority': 'Primary', 'ethernetBootType': "iSCSI", 'iscsi': {'initiatorNameSource': 'ProfileInitiatorName'}}},
                                           {'id': 2, 'name': 'Deployment Network B', 'functionType': 'Ethernet', 'networkUri': 'iscsi_nw',
                                            'portId': 'Mezz 3:2-a', 'requestedVFs': 'Auto', 'requestedMbps': '2500', 'allocatedVFs': 64, 'macType': 'Virtual', 'wwpnType': 'Virtual', 'mac': '',
                                            'allocatedMbps': 2500, 'maximumMbps': 10000,
                                            'boot': {'bootVolumeSource': 'UserDefined', 'priority': 'Secondary', 'ethernetBootType': "iSCSI", 'iscsi': {'initiatorNameSource': 'ProfileInitiatorName'}}},
                                           {'id': 3, 'name': 'Blade_boot_mgmt', 'functionType': 'Ethernet', 'networkUri': 'mgmt_nw',
                                            'portId': 'Mezz 3:1-c', 'requestedVFs': 0, 'requestedMbps': '2500', 'allocatedVFs': 0, 'macType': 'Virtual', 'wwpnType': 'Virtual', 'mac': '',
                                            'allocatedMbps': 2500, 'maximumMbps': 10000,
                                            'boot': {'priority': 'NotBootable', 'iscsi': {}}}]},
    'bootMode': {'manageMode': True, 'pxeBootPolicy': 'Auto', 'mode': 'UEFIOptimized'},
    'boot': {'manageBoot': True, 'order': ['HardDisk']},
    'bios':{'reapplyState': 'NotApplying', 'manageBios': False, 'overriddenSettings': []},
    'localStorage':{},
    'sanStorage': {'volumeAttachments': [], 'manageSanStorage':False},
    'osDeploymentSettings':{'osDeploymentPlanUri': 'Deploymentplan for MGMT NIC attributes',
                            'osCustomAttributes': [{'name': "DomainName", 'value': "hpe.com"},
                                                   {'name': "Hostname", 'value': "esxihost"},
                                                   {'name': "ManagementNIC.connectionid", 'value': "3"},
                                                   {'name': "ManagementNIC.dhcp", 'value': "false"},
                                                   {'name': "ManagementNIC.ipv4disable", 'value': "false"},
                                                   {'name': "ManagementNIC.networkuri", 'value': 'mgmt_nw'},
                                                   {'name': "ManagementNIC.constraint", 'value': "auto"},
                                                   {'name': "Password", 'value': 'RESTAPI@321'},
                                                   {'name': "SSH", 'value': "enabled"}],
                            'osVolumeUri': None}}]

SPT_from_SP = [{  # 0 Create SPT from Server profile
    'name': 'SPT_from_Serverprofile'}]

serverprofile_edit = [{  # 0 Edit CA values in Server profile for name and description
    'name': 'serverprofile_RESTAPI_update',
    'description': 'sp update'}]

backup_bundle_add = [{'name': 'C:/Goldenimage/ci-30e171681800_backup_2019-02-11_100239_v5.00.00-0379798.zip'}]

deploymentplan_delete = [{'name': 'Deploymentplan name update'},
                         {'name': 'Deploymentplan for Password'},
                         {'name': 'Deploymentplan for MGMT NIC attributes'}]

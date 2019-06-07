''' Data variable file of 164.6 '''
# pylint: disable=invalid-name
# from winnt import NULL
# from requests.api import patch

admin_credentials = {'userName': 'Administrator', 'password': 'admin123'}
ov_appliances = ['fe80::1602:ecff:fe46:6538', 'fe80::1602:ecff:fe46:a368']
MAC = "14:02:ec:46:65:38"
i3s_appliances = ['fe80::1602:ecff:fe45:3d48', 'fe80::1602:ecff:fe46:f7d0', 'fe80::1602:ecff:fe45:4d68', 'fe80::32e1:71ff:fe68:cb80']
i3s_enclosure = ['SGH725TX6F', 'SGH736WTHS', 'SGH736WTHP', 'SGH724SLP4']
enclosures_count = '5'
DEFAULT_USER = 'Administrator'
status = '200'
NEW_PASSWORD = 'admin123'
# SUBNET_1 = '255.255.252.0'
# IPV4GATEWAY = '15.212.164.1'
# DOMAINNAME = 'hpecorp.net'
# HOSTNAME = 'EB2409.test.local'
# DNS1 = '16.110.135.51'
# DNS2 = '16.110.135.52'
# MAINTENANCEIP1 = '15.212.164.7'
# MAINTENANCEIP2 = '15.212.164.8'
CLUSTERIP = '15.212.164.6'
OV_ACTIVE = 'fe80::1602:ecff:fe46:6538'
Ov_Build_sha = '/OneView/4.10/ddimage/HPEOneView-SSH-4.10.04-0370820-withsig.zip.sha256'
OV_Build = '/OneView/4.10/ddimage/HPEOneView-SSH-4.10.04-0370820-withsig.zip'
I3S_Build_sha = '/I3S/4.10/ddimage/HPEImageStreamer-SSH-4.10.04-0363343-withsig.zip.sha256'
I3S_Build = '/I3S/4.10/ddimage/HPEImageStreamer-SSH-4.10.04-0363343-withsig.zip'
# i3s_version= '4.00.00-0319447'
# ov_version= '4.00.00-0319900'
build_server = 'fe80::9932:1c50:6353:7a9'
build_version = '4.10'
blade_IP = '15.212.164.254'
support_dump_loc = r'C:\support_dump\sd'
fusion_IP = '15.212.164.6'

network = {"type": "ApplianceNetworkConfiguration",
           "applianceNetworks": [{"activeNode": 1,
                                  "unconfigure": False,
                                  "app1Ipv4Addr": "15.212.164.7", "app1Ipv6Addr": "",
                                  "app2Ipv4Addr": "15.212.164.8", "app2Ipv6Addr": "",
                                  "virtIpv4Addr": "15.212.164.6", "virtIpv6Addr": None,
                                  "app1Ipv4Alias": None, "app1Ipv6Alias": None,
                                  "app2Ipv4Alias": None, "app2Ipv6Alias": None,
                                  "hostname": "EB2405.test.local",
                                  "confOneNode": True, "interfaceName": "",
                                  "macAddress": "14:02:ec:46:65:38",
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

servers = [{'serverHardwareUri': 'SGH736WTHR, bay 8', 'serverHardwareTypeUri': 'SY 480 Gen9 1'},
           {'serverHardwareUri': 'SGH736WTHR, bay 5', 'serverHardwareTypeUri': 'SY 480 Gen9 1'}]

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
                   'startAddress': '15.212.164.9', 'endAddress': '15.212.164.21',
                   'name': 'mgmt_nw', 'subnetUri': ' '}

sd_body = [{"encrypt": False, "errorCode": "CI", "userName": "administrator", "password": "admin123"}, {
    "encrypt": True, "errorCode": "CI", "userName": "backup", "password": "admin123"}, {"encrypt": False, "errorCode": "CI"}]

bin_file_loc = 'C:\\bin file\\ov\\HPEOneView-fullupdate-4.10.00-SNAPSHOT-0338466.bin'
ov_bin = 'HPEOneView-fullupdate-4.10.00-SNAPSHOT-0338466.bin'
ov_version_Check = '4.10.00-0338466'

iscsi_network = {'vlanId': '149', 'networkId': '192.168.0.0',
                 'ethernetNetworkType': 'Tagged', 'subnetUri': '',
                 'purpose': 'ISCSI', 'name': 'iscsi_nw',
                 'smartLink': False, 'privateNetwork': False,
                 'connectionTemplateUri': None, 'type': 'ethernet-networkV4'}

mgmt_network = {'vlanId': '0', 'networkId': '15.212.164.0',
                'ethernetNetworkType': 'Untagged', 'subnetUri': '',
                'purpose': 'Management', 'name': 'mgmt_nw',
                'smartLink': False, 'privateNetwork': False,
                'connectionTemplateUri': None, 'type': 'ethernet-networkV4'}

lig_tbird_3enc1 = {'type': 'logical-interconnect-groupV4',
                   'ethernetSettings': {'type': 'EthernetInterconnectSettingsV4', 'enableIgmpSnooping': False,
                                        'igmpIdleTimeoutInterval': 260, 'enableFastMacCacheFailover': True, 'macRefreshInterval': 5,
                                        'enableNetworkLoopProtection': True, 'enablePauseFloodProtection': True,
                                        'enableRichTLV': False, 'interconnectType': 'Ethernet', 'dependentResourceUri': None,
                                        'name': 'defaultEthernetSwitchSettings', 'category': None, 'uri': '/ethernetSettings'},
                   'description': None,
                   'name': 'LIG-3encprimay',
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
                                                  {'enclosure': '1', 'bay': '3', 'port': 'Q1:2', 'speed': 'Auto'},
                                                  {'enclosure': '2', 'bay': '6', 'port': 'Q1:1', 'speed': 'Auto'},
                                                  {'enclosure': '2', 'bay': '6', 'port': 'Q1:2', 'speed': 'Auto'}],

                        'name': 'uplink_3encl', 'networkType': 'Ethernet',
                        'ethernetNetworkType': 'ImageStreamer'},
                       {'networkUris': ['mgmt_nw'], 'mode':'Auto',
                        'lacpTimer':'Short', 'primaryPort':None,
                        'nativeNetworkUri': None,
                        'logicalPortConfigInfos':[{'enclosure': '1', 'bay': '3', 'port': 'Q4:1', 'speed': 'Auto'}],
                        'networkType': 'Ethernet', 'ethernetNetworkType': 'Untagged', 'name': 'uplink_2'}]}
lig_tbird_3enc2 = {'type': 'logical-interconnect-groupV4',
                   'ethernetSettings': {'type': 'EthernetInterconnectSettingsV4', 'enableIgmpSnooping': False,
                                        'igmpIdleTimeoutInterval': 260, 'enableFastMacCacheFailover': True, 'macRefreshInterval': 5,
                                        'enableNetworkLoopProtection': True, 'enablePauseFloodProtection': True,
                                        'enableRichTLV': False, 'interconnectType': 'Ethernet', 'dependentResourceUri': None,
                                        'name': 'defaultEthernetSwitchSettings', 'category': None, 'uri': '/ethernetSettings'},
                   'description': None,
                   'name': 'LIG-3encsecondary',
                   'interconnectMapTemplate': [{'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
                                               {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
                                               {'bay': 6, 'enclosure': 1, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 1},
                                               {'bay': 3, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2}],
                   'enclosureType': 'SY12000',
                   'enclosureIndexes': [1, 2],
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
                                                  {'enclosure': '1', 'bay': '3', 'port': 'Q1:2', 'speed': 'Auto'},
                                                  {'enclosure': '2', 'bay': '6', 'port': 'Q1:1', 'speed': 'Auto'},
                                                  {'enclosure': '2', 'bay': '6', 'port': 'Q1:2', 'speed': 'Auto'}],

                        'name': 'uplink_3encl', 'networkType': 'Ethernet',
                        'ethernetNetworkType': 'ImageStreamer'},
                       {'networkUris': ['mgmt_nw'], 'mode':'Auto',
                        'lacpTimer':'Short', 'primaryPort':None,
                        'nativeNetworkUri': None,
                        'logicalPortConfigInfos':[{'enclosure': '1', 'bay': '3', 'port': 'Q4:1', 'speed': 'Auto'}],
                        'networkType': 'Ethernet', 'ethernetNetworkType': 'Untagged', 'name': 'uplink_2'}]}
enc_groups_tbird_3enc1 = {'name': 'EG-3encprimay', 'powerMode': 'RedundantPowerFeed',
                          'ambientTemperatureMode': 'Standard', 'ipAddressingMode': 'External',
                          'ipRangeUris': [], 'enclosureCount': 3,
                          'configurationScript': None,
                          'osDeploymentSettings': {'manageOSDeployment': True,
                                                   'deploymentModeSettings': {'deploymentMode': 'Internal', 'deploymentNetworkUri': None}},
                          'interconnectBayMappings': [{'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG-3encprimay'},
                                                      {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG-3encprimay'}]}
enc_groups_tbird_3enc2 = {'name': 'EG-3encsecondary', 'powerMode': 'RedundantPowerFeed',
                          'ambientTemperatureMode': 'Standard', 'ipAddressingMode': 'External',
                          'ipRangeUris': [], 'enclosureCount': 2,
                          'configurationScript': None,
                          'osDeploymentSettings': {'manageOSDeployment': True,
                                                   'deploymentModeSettings': {'deploymentMode': 'Internal', 'deploymentNetworkUri': None}},
                          'interconnectBayMappings': [{'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG-3encsecondary'},
                                                      {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG-3encsecondary'}]}
les_3enc1 = {'name': 'LE-3encprimay',
             'enclosureUris': ['ENC:SGH736WTHR', 'ENC:SGH736WTHP', 'ENC:SGH736WTHS'],
             'enclosureGroupUri': 'EG:EG-3encprimay', 'firmwareBaselineUri': None,
             'forceInstallFirmware': False}
les_3enc2 = {'name': 'LE-3encsecondary',
             'enclosureUris': ['ENC:SGH725TX6F', 'ENC:SGH724SLP4', ],
             'enclosureGroupUri': 'EG:EG-3encsecondary', 'firmwareBaselineUri': None,
             'forceInstallFirmware': False}
osdeploymentserver = {'name': 'OSDS-3enc', 'description': 'os deployment server',
                      'applianceUri': 'SGH736WTHP, appliance 2', 'mgmtNetworkUri': ['mgmt_nw'],
                      'deplManagersType': 'Image Streamer'}

goldenimage = [{'name': 'GoldenImage_e2e_1', 'description': 'valid_goldenimage', 'file': "valid_file"},
               {'name': 'GoldenImage_e2e', 'description': 'valid_goldenimage', 'file': "valid_file"}]

planscript = {"type": "PlanScript", "description": "valid deploy planscript",
              "name": "ps_deploy_for_e2e_test", "hpProvided": "false", "planType": "deploy",
              "content": "# Mount /bootbank area for ESXi 5.5+ \r\n#\r\n# Typical partition layout is:\r\n# 1 - UEFI ESP\r\n# 5 - /bootbank  <= holds ESXi host state to be configured\r\n# 6 - /altbootbank\r\n\r\necho \"########################################\"\r\necho \"Mount ESXi /bootbank\"\r\necho \"########################################\"\r\n\r\n# List structure storage layout found in ESXi Golden Image / OS Volume\r\necho \"Devices:\"\r\n-list-devices\r\necho\r\necho \"Partitions:\"\r\n-list-partitions\r\necho\r\necho \"File systems:\"\r\n-list-filesystems\r\necho\r\n\r\necho \"Mount file systems:\"\r\necho \"/dev/sda5 is assumed to hold ESXi host state configuration\"\r\necho \"mount /dev/sda5\"\r\nmount /dev/sda5 /\r\necho \"File system details for /dev/sda5:\"\r\n-statvfs /\r\necho\r\necho \"########################################\"\r\necho \"Copy out and unpack ESXi host state\"\r\necho \"########################################\"\r\n\r\necho \"Create ImageStreamer temp directory\"\r\n-mkdir /ImageStreamer\r\necho\r\n\r\necho \"Extract ESXi host configuration from Golden Image\"\r\necho \"Copy out boot.cfg\"\r\ndownload /boot.cfg boot.cfg\r\necho \"Copy out state.tgz if present\"\r\n-download /state.tgz state.tgz\r\necho \"Copy out onetime.tgz if present\"\r\n-download /onetime.tgz onetime.tgz\r\necho\r\n\r\necho \"Build esxi_unpack ESXi host state unpack script\"\r\nupload -<<END /ImageStreamer/esxi_unpack\r\n#! /bin/bash\r\nDIR=`pwd`\r\n\r\necho \"Finding ESXi host state configuration archive in Golden Image\"\r\nSTATE=`grep -c onetime.tgz $DIR/boot.cfg`\r\nif [ \"$STATE\" -eq \"0\" ]; then\r\n    echo\r\n    echo \"Unpack state.tgz\"\r\n    mkdir $DIR/esxi_state\r\n    cd $DIR/esxi_state\r\n    tar xvpzf $DIR/state.tgz\r\n    echo\r\n    echo \"Unpack local.tgz\"\r\n    mkdir $DIR/esxi_local\r\n    cd $DIR/esxi_local\r\n    tar xvpzf $DIR/esxi_state/local.tgz\r\n    echo\r\nelse\r\n    echo\r\n    echo \"Unpack onetime.tgz\"\r\n    mkdir $DIR/esxi_onetime\r\n    cd $DIR/esxi_onetime\r\n    tar xvpzf $DIR/onetime.tgz\r\n    echo\r\nfi\r\n\r\nif [ -e etc/rc.local.d/local.sh ]; then\r\n    cp etc/rc.local.d/local.sh $DIR/local.sh\r\nfi\r\n\r\necho \"Unpacking ESXi host state complete.\"\r\nexit 0\r\nEND\r\ndownload /ImageStreamer/esxi_unpack ./esxi_unpack\r\necho\r\n\r\necho \"Build esxi_repack ESXi host state repack script\"\r\nupload -<<END /ImageStreamer/esxi_repack\r\n#! /bin/bash\r\nDIR=`pwd`\r\n\r\necho \"---------------------------------------------------------------\"\r\necho \"Final ESXi host local.sh content for configuration at first boot:\"\r\ncat $DIR/local.sh\r\necho \"---------------------------------------------------------------\"\r\necho\r\n\r\necho \"Finding ESXi host state configuration archive\"\r\nSTATE=`grep -c onetime.tgz $DIR/boot.cfg`\r\nif [ \"$STATE\" -eq \"0\" ]; then\r\n    echo\r\n    echo \"Repack local.tgz\"\r\n    cd $DIR/esxi_local\r\n    mkdir -p etc/rc.local.d\r\n    cp $DIR/local.sh etc/rc.local.d/local.sh\r\n    chmod 777 etc/rc.local.d/local.sh\r\n    tar cvpzf $DIR/esxi_state/local.tgz *\r\n    echo\r\n    echo \"Repack state.tgz\"\r\n    cd $DIR/esxi_state\r\n    tar cvpzf $DIR/state.tgz *\r\n    echo\r\nelse\r\n    echo\r\n    echo \"Repack onetime.tgz\"\r\n    cd $DIR/esxi_onetime\r\n    mkdir -p etc/rc.local.d\r\n    cp $DIR/local.sh etc/rc.local.d/local.sh\r\n    chmod 777 etc/rc.local.d/local.sh\r\n    tar cvpzf $DIR/onetime.tgz *\r\n    touch $DIR/state.tgz\r\n    echo\r\nfi\r\necho \"Repacking ESXi host state complete.\"\r\nexit 0\r\nEND\r\ndownload /ImageStreamer/esxi_repack ./esxi_repack\r\necho\r\n\r\necho \"Run  esxi_repack ESXi host state unpack script\"\r\n!source ./esxi_unpack\r\necho\r\necho \"########################################\"\r\necho \"Configure ssh\"\r\necho \"########################################\"\r\n\r\nupload -<<END /ImageStreamer/esxi_ssh\r\n#!/bin/bash\r\nif [ \"@SSH:enabled@\" = \"enabled\" ]; then\r\ncat <<\"EOF\" >>local.sh\r\nvim-cmd hostsvc/enable_esx_shell\r\nvim-cmd hostsvc/start_esx_shell\r\nvim-cmd hostsvc/enable_ssh\r\nvim-cmd hostsvc/start_ssh\r\nservices.sh restart\r\n\r\nEOF\r\nfi\r\n\r\nexit 0\r\nEND\r\n\r\ndownload /ImageStreamer/esxi_ssh esxi_ssh\r\necho \"Run esxi_ssh\"\r\n!source ./esxi_ssh\r\necho \"########################################\"\r\necho \"Pack and replace ESXi host state into ESXi host OS Volume\"\r\necho \"########################################\"\r\n\r\necho \"Run  esxi_repack ESXi host state repack script\"\r\n!source ./esxi_repack\r\n\r\necho \"Copy in state.tgz if present\"\r\n-upload state.tgz /state.tgz \r\necho \"Copy in onetime.tgz if present\"\r\n-upload onetime.tgz /onetime.tgz\r\n\r\necho \"Remove Image Streamer temp directory\"\r\nrm-rf /tmp/ImageStreamer\r\necho \"########################################\"\r\necho \"Cleanup and unmount file systems \"\r\necho \"########################################\"\r\n\r\necho \"Remove ImageStreamer temp directory\"\r\nrm-rf /ImageStreamer\r\n\r\necho \"Unmount file systems\"\r\numount /\r\necho"}

buildplan = {"type": "OeBuildPlanV5",
             "customAttributes": [{"constraints": "{}",
                                   "description": "To enable ssh", "name": "SSH",
                                   "value": "enabled", "type": "string"}],
             "buildStep": [{"planScriptUri": "ps_deploy_for_e2e_test",
                            "serialNumber": "1", "parameters": "1"}],
             "hpProvided": False, "oeBuildPlanType": "deploy",
             "description": "Buildplan", "name": "oebp_deploy_for_e2e_test"}

deploymentplan = [
    {"type": "OEDeploymentPlanV5",
     "hpProvided": "false",
     "customAttributes": [{"visible": True, "constraints": "{}",
                           "editable": True, "description": "ssh enabled",
                           "name": "SSH", "value": "enabled", "type": "string"}],
     "goldenImageURI": "GoldenImage_e2e",
     "oeBuildPlanURI": "oebp_deploy_for_e2e_test",
     "category": "oe-deployment-plans",
     "description": "Deployment Plan",
     "name": "oedp_deploy_for_e2e_test"},

    {"type": "OEDeploymentPlanV5",
     "name": "oedp_deploy_esxi6.5",
     "description": "",
     "goldenImageURI": "GoldenImage_e2e",
     "oeBuildPlanURI": "HPE - ESXi - deploy in single frame non-HA config- 2017-03-24",
     "ostype": "ESXi",
     "hpProvided": "false",
     "customAttributes": [
         {"name": "SSH", "value": "enabled",
          "type": "option", "description": "",
          "editable": True, "visible": True,
          "constraints": "{\"options\":[\"enabled\"]}"},
         {"name": "ManagementNIC",
          "value": None, "type": "nic",
          "description": "", "editable": True,
          "visible": True,
          "constraints": "{\"ipv4static\":true,\"ipv4dhcp\":true,\"ipv4disable\":false,\"parameters\":[\"dns1\",\"dns2\",\"gateway\",\"ipaddress\",\"mac\",\"netmask\",\"vlanid\"]}"},
         {"name": "Password",
          "value": "", "type": "password",
          "description": "Password value must meet password complexity and minimum length requirements defined for ESXi 5.x, ESXi 6.x appropriately.",
          "editable": True, "visible": True,
          "constraints": "{}"},
         {"name": "DomainName",
          "value": "", "type": "fqdn",
          "description": "", "editable": True,
          "visible": True, "constraints": "{\"helpText\":\"\"}"},
         {"name": "Hostname", "value": "",
          "type": "hostname", "description": "",
          "editable": True, "visible": True,
          "constraints": "{\"helpText\":\"\"}"}]}]

buildplan_delete = [{'name': 'HPE - ESXi - generalize full state - 2017-03-24'},
                    {'name': 'HPE - ESXi - deploy with multiple management NIC HA config- 2017-03-24'},
                    {'name': 'HPE - ESXi - deploy in single frame non-HA config- 2017-03-24'}]

planscript_delete = [{'name': 'HPE - ESXi - configure management 1st NIC - 2017-03-16'},
                     {'name': 'HPE - ESXi - set password - 2017-03-15'},
                     {'name': 'HPE - ESXi - umount - 2017-03-15'},
                     {'name': 'HPE - ESXi - configure ssh - 2017-03-15'},
                     {'name': 'HPE - ESXi - repack state - 2017-03-15'},
                     {'name': 'HPE - ESXi - configure management 2nd NIC HA - 2017-03-15'},
                     {'name': 'HPE - ESXi - generalize host configuration - 2017-03-15'},
                     {'name': 'HPE - ESXi - mount - 2017-03-15'},
                     {'name': 'HPE - ESXi - unpack state - 2017-03-15'},
                     {'name': 'HPE - ESXi - configure iSCSI boot HA - 2017-03-15'}]

artifactbundle_delete = {'name': 'HPE-ESX-4.1'}

artifactbundle = {'name': 'ab_automate_1',
                  'description': 'ab with deploymentplan only',
                  'deploymentPlans': [{'resourceUri': 'oedp_deploy_for_e2e_test', 'readOnly': False}]}

artifactbundle_update = {'name': 'ab_automate_update', 'type': 'ArtifactsBundle'}

artifactbundle_add = {'name': 'esx_6.X'}

artifactbundle_extract = {'name': 'HPE-ESX-4.1'}

OSDP = [{'name': 'oedp_deploy_esxi6.5'},
        {'name': 'oedp_deploy_for_e2e_test'}]

CREATEGOLDENIMAGE = [
    {
        'type': 'GoldenImage',
        'name': 'Test',
        'description': 'Test',
        'imageCapture': 'true',
        'osVolumeURI': 'i3s_serverprofile_for_SE',
        'buildPlanUri': 'HPE - ESXi - generalize full state - 2017-03-24',
    },
    {
        'type': 'GoldenImage',
        'name': 'Test',
        'description': 'Duplicate Name',
        'imageCapture': 'true',
        'osVolumeURI': 'i3s_serverprofile_for_SE',
        'buildPlanUri': 'HPE - ESXi - generalize full state - 2017-03-24',
    },
    {
        'type': 'GoldenImage',
        'name': '',
        'description': 'Name field null',
        'imageCapture': 'true',
        'osVolumeURI': 'i3s_serverprofile_for_SE',
        'buildPlanUri': 'HPE - ESXi - generalize full state - 2017-03-24',
    },
]

serverprofile_3enc = {"type": "ServerProfileV9", "serverHardwareUri": "SH:SGH736WTHS, bay 1",
                      "serverHardwareTypeUri": "SHT:SY 480 Gen9 1", "enclosureGroupUri": "EG:EG-3encprimay",
                      'enclosureUri': 'ENC:SGH736WTHS', "serialNumberType": "Virtual",
                      "iscsiInitiatorNameType": "AutoGenerated", "macType": "Virtual",
                      "wwnType": "Virtual", "name": "i3s_serverprofile_for_SE",
                      "description": "", "affinity": "Bay",
                      "connectionSettings": {
                          "connections": [{"id": 1, "name": "Deployment Network A",
                                           "functionType": "Ethernet", "portId": "Mezz 3:1-a",
                                           "requestedMbps": "2500", "networkUri": "ETH:iscsi_nw",
                                           "mac": None, "wwpn": "",
                                           "wwnn": "", "requestedVFs": "Auto",
                                           "ipv4": {"ipAddress": None},
                                           "boot": {"priority": "Primary",
                                                    "ethernetBootType": "iSCSI",
                                                    "iscsi": {"initiatorNameSource": "ProfileInitiatorName",
                                                              "firstBootTargetIp": None, "secondBootTargetIp": "",
                                                              "secondBootTargetPort": "", "initiatorName": None,
                                                              "bootTargetName": None, "bootTargetLun": None}}},
                                          {"id": 2, "name": "Deployment Network B",
                                           "functionType": "Ethernet", "portId": "Mezz 3:2-a",
                                           "requestedMbps": "2500", "networkUri": "ETH:iscsi_nw",
                                           "mac": None, "wwpn": "",
                                           "wwnn": "", "requestedVFs": "Auto",
                                           "ipv4": {"ipAddress": None},
                                           "boot": {"priority": "Secondary",
                                                    "ethernetBootType": "iSCSI",
                                                    "iscsi": {"initiatorNameSource": "ProfileInitiatorName",
                                                              "firstBootTargetIp": None, "secondBootTargetIp": "",
                                                              "secondBootTargetPort": "", "initiatorName": None,
                                                              "bootTargetName": None, "bootTargetLun": None}}},
                                          {"id": 3, "name": "con1",
                                           "functionType": "Ethernet", "portId": "Auto",
                                           "requestedMbps": "2500", "networkUri": "ETH:mgmt_nw",
                                           "lagName": None, "mac": None,
                                           "wwpn": None, "wwnn": None,
                                           "requestedVFs": "0", "ipv4": {},
                                           "boot": {"priority": "NotBootable", "iscsi": {}}}]},
                      "boot": {"manageBoot": True, "order": ["HardDisk"]},
                      "bootMode": {"manageMode": True, "mode": "UEFIOptimized",
                                   "secureBoot": "Unmanaged", "pxeBootPolicy": "Auto"},
                      "firmware": {"manageFirmware": False, "firmwareBaselineUri": "",
                                   "forceInstallFirmware": False, "firmwareInstallType": None,
                                   "firmwareScheduleDateTime": "", "firmwareActivationType": "Immediate"},
                      "bios": {"manageBios": False, "overriddenSettings": []},
                      "hideUnusedFlexNics": True, "iscsiInitiatorName": "",
                      "osDeploymentSettings": {"osDeploymentPlanUri": "oedp_deploy_esxi6.5",
                                               "osCustomAttributes": [{"name": "DomainName", "value": "hpe.com", "constraints": "{\"helpText\":\"\"}", "type": "fqdn"},
                                                                      {"name": "Hostname", "value": "hpe", "constraints": "{\"helpText\":\"\"}", "type": "hostname"},
                                                                      {"name": "ManagementNIC.dns1", "value": "16.110.135.51"},
                                                                      {"name": "ManagementNIC.dns2", "value": "16.110.135.52"},
                                                                      {"name": "ManagementNIC.gateway", "value": "15.212.164.1"},
                                                                      {"name": "ManagementNIC.ipaddress", "value": "15.212.164.255"},
                                                                      {"name": "ManagementNIC.netmask", "value": "255.255.252.0"},
                                                                      {"name": "ManagementNIC.connectionid", "value": "3"},
                                                                      {"name": "ManagementNIC.dhcp", "value": "False"},
                                                                      {"name": "ManagementNIC.ipv4disable", "value": "False"},
                                                                      {"name": "ManagementNIC.networkuri", "value": "ETH:mgmt_nw"},
                                                                      {"name": "ManagementNIC.constraint", "value": "userspecified"},
                                                                      {"name": "ManagementNIC.vlanid", "value": "0"},
                                                                      {"name": "Password", "value": "hpVSE123#"},
                                                                      {"name": "SSH", "value": "enabled", "constraints": "{\"options\":[\"enabled\"]}", "type": "option"}],
                                               "osVolumeUri": None, "forceOsDeployment": False},
                      "localStorage": {"sasLogicalJBODs": [], "controllers": []},
                      "sanStorage": None,
                      "initialScopeUris": []}

sp_templates = [
    {'type': 'ServerProfileTemplateV5', 'serverProfileDescription': '',
     'serverHardwareTypeUri': 'SHT:' + servers[0]['serverHardwareTypeUri'],
     'enclosureGroupUri': 'EG:EG-3enc', 'serialNumberType': 'Virtual',
     'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'MAT_SPT1',
     'description': '', 'affinity': 'Bay',
     'connectionSettings': {'connections': [{'id': 1, 'name': 'Deployment Network A',
                                             'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                             'requestedMbps': '2500', 'networkUri': 'ETH:iscsi_nw',
                                             'requestedVFs': 'Auto',
                                             'ipv4': {'ipAddressSource': 'SubnetPool'},
                                             'boot': {'priority': 'Primary', 'ethernetBootType': 'iSCSI',
                                                      'iscsi': {'initiatorNameSource': 'ProfileInitiatorName', 'firstBootTargetIp': None,
                                                                'secondBootTargetIp': '', 'secondBootTargetPort': ''},
                                                      'bootVolumeSource': 'UserDefined'}},
                                            {'id': 2, 'name': 'Deployment Network B',
                                             'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                             'requestedMbps': '2500', 'networkUri': 'ETH:iscsi_nw',
                                             'requestedVFs': 'Auto',
                                             'ipv4': {'ipAddressSource': 'SubnetPool'},
                                             'boot': {'priority': 'Secondary', 'ethernetBootType': 'iSCSI',
                                                      'iscsi': {'initiatorNameSource': 'ProfileInitiatorName', 'firstBootTargetIp': None,
                                                                'secondBootTargetIp': '', 'secondBootTargetPort': ''},
                                                      'bootVolumeSource': 'UserDefined'}},
                                            {'id': 3, 'name': 'Management Network A',
                                             'functionType': 'Ethernet', 'portId': 'Auto',
                                             'requestedMbps': '2500', 'networkUri': 'ETH:mgmt_nw',
                                             'lagName': None, 'requestedVFs': '0',
                                             'ipv4': {},
                                             'boot': {'priority': 'NotBootable', 'iscsi': {}}}],
                            'manageConnections': True},
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'bootMode': {'manageMode': True, 'mode': 'UEFIOptimized',
                  'secureBoot': 'Unmanaged', 'pxeBootPolicy': 'Auto'},
     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '',
                  'forceInstallFirmware': False, 'firmwareInstallType': None,
                  'firmwareActivationType': 'Immediate'},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
     'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
     'sanStorage': None,
     'osDeploymentSettings': {
         'osDeploymentPlanUri': 'oedp_deploy_esxi6.5',
         'osCustomAttributes': [{'name': 'DomainName', 'value': 'lab.local', 'constraints': '{\'helpText\':\'\'}', 'type': 'fqdn'},
                                {'name': 'Hostname', 'value': '{enclosure}', 'constraints': '{\'helpText\':\'\'}', 'type': 'hostname'},
                                {'name': 'ManagementNIC.connectionid', 'value': '3'},
                                {'name': 'ManagementNIC.dhcp', 'value': 'False'},
                                {'name': 'ManagementNIC.ipv4disable', 'value': 'False'},
                                {'name': 'ManagementNIC.networkuri', 'value': 'ETH:mgmt_nw'},
                                {'name': 'ManagementNIC.constraint', 'value': 'auto'},
                                {'name': 'ManagementNIC.vlanid', 'value': '0'},
                                {'name': 'Password', 'value': None},
                                {'name': 'SSH', 'value': 'enabled', 'constraints': '{\'options\':[\'enabled\']}', 'type': 'option'}]},
     'initialScopeUris': []},
    {'type': 'ServerProfileTemplateV5', 'serverProfileDescription': '',
     'serverHardwareTypeUri': 'SHT:' + servers[1]['serverHardwareTypeUri'],
     'enclosureGroupUri': 'EG:EG-3enc', 'serialNumberType': 'Virtual',
     'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'MAT_SPT2',
     'description': '', 'affinity': 'Bay',
     'connectionSettings': {'connections': [{'id': 1, 'name': 'Deployment Network A', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                             'requestedMbps': '2500', 'networkUri': 'ETH:iscsi_nw', 'requestedVFs': 'Auto',
                                             'ipv4': {'ipAddressSource': 'SubnetPool'},
                                             'boot': {'priority': 'Primary', 'ethernetBootType': 'iSCSI',
                                                      'iscsi': {'initiatorNameSource': 'ProfileInitiatorName', 'firstBootTargetIp': None,
                                                                'secondBootTargetIp': '', 'secondBootTargetPort': ''},
                                                      'bootVolumeSource': 'UserDefined'}},
                                            {'id': 2, 'name': 'Deployment Network B',
                                             'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                             'requestedMbps': '2500', 'networkUri': 'ETH:iscsi_nw',
                                             'requestedVFs': 'Auto',
                                             'ipv4': {'ipAddressSource': 'SubnetPool'},
                                             'boot': {'priority': 'Secondary', 'ethernetBootType': 'iSCSI',
                                                      'iscsi': {'initiatorNameSource': 'ProfileInitiatorName', 'firstBootTargetIp': None,
                                                                'secondBootTargetIp': '', 'secondBootTargetPort': ''},
                                                      'bootVolumeSource': 'UserDefined'}},
                                            {'id': 3, 'name': 'Management Network A',
                                             'functionType': 'Ethernet', 'portId': 'Auto',
                                             'requestedMbps': '2500', 'networkUri': 'ETH:mgmt_nw',
                                             'lagName': None, 'requestedVFs': '0',
                                             'ipv4': {},
                                             'boot': {'priority': 'NotBootable', 'iscsi': {}}}],
                            'manageConnections': True},
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'bootMode': {'manageMode': True, 'mode': 'UEFIOptimized',
                  'secureBoot': 'Unmanaged', 'pxeBootPolicy': 'Auto'},
     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '',
                  'forceInstallFirmware': False, 'firmwareInstallType': None,
                  'firmwareActivationType': 'Immediate'},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
     'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
     'sanStorage': None,
     'osDeploymentSettings': {
         'osDeploymentPlanUri': 'oedp_deploy_esxi6.5',
         'osCustomAttributes': [{'name': 'DomainName', 'value': 'lab.local', 'constraints': '{\'helpText\':\'\'}', 'type': 'fqdn'},
                                {'name': 'Hostname', 'value': '{enclosure}', 'constraints': '{\'helpText\':\'\'}', 'type': 'hostname'},
                                {'name': 'ManagementNIC.connectionid', 'value': '3'},
                                {'name': 'ManagementNIC.dhcp', 'value': 'False'},
                                {'name': 'ManagementNIC.ipv4disable', 'value': 'False'},
                                {'name': 'ManagementNIC.networkuri', 'value': 'ETH:mgmt_nw'},
                                {'name': 'ManagementNIC.constraint', 'value': 'auto'},
                                {'name': 'ManagementNIC.vlanid', 'value': '0'},
                                {'name': 'Password', 'value': None},
                                {'name': 'SSH', 'value': 'enabled', 'constraints': '{\'options\':[\'enabled\']}', 'type': 'option'}]},
     'initialScopeUris': []}]

sp_from_spt = [{'type': 'ServerProfileV8', 'name': 'sp1_from_spt1',
                'serverHardwareUri': 'SH:' + servers[0]['serverHardwareUri'],
                'serverProfileTemplateUri': 'SPT:' + sp_templates[0]['name']},
               {'type': 'ServerProfileV8', 'name': 'sp2_from_spt2',
                'serverHardwareUri': 'SH:' + servers[1]['serverHardwareUri'],
                'serverProfileTemplateUri': 'SPT:' + sp_templates[1]['name']}]

connSettings = {
    "connections": [{"id": 1,
                     "name": "Deployment Network A", "functionType": "Ethernet",
                     "portId": "Mezz 3:1-a", "requestedMbps": "2500",
                     "networkUri": 'ETH:iscsi_nw',
                     "mac": None, "wwpn": "",
                     "wwnn": "", "requestedVFs": "Auto",
                     "ipv4": {"ipAddress": None},
                     "boot": {"priority": "Primary",
                              "ethernetBootType": "iSCSI",
                              "iscsi": {"initiatorNameSource": "ProfileInitiatorName",
                                        "firstBootTargetIp": None, "secondBootTargetIp": "",
                                        "secondBootTargetPort": "", "initiatorName": None,
                                        "bootTargetName": None, "bootTargetLun": None}}},
                    {"id": 2,
                     "name": "Deployment Network B", "functionType": "Ethernet",
                     "portId": "Mezz 3:2-a", "requestedMbps": "2500",
                     "networkUri": 'ETH:iscsi_nw',
                     "mac": None, "wwpn": "",
                     "wwnn": "", "requestedVFs": "Auto",
                     "ipv4": {"ipAddress": None},
                     "boot": {"priority": "Secondary",
                              "ethernetBootType": "iSCSI",
                              "iscsi": {"initiatorNameSource": "ProfileInitiatorName",
                                        "firstBootTargetIp": None, "secondBootTargetIp": "",
                                        "secondBootTargetPort": "", "initiatorName": None,
                                        "bootTargetName": None, "bootTargetLun": None}}},
                    {"id": 3,
                     "name": "", "functionType": "Ethernet",
                     "portId": "Auto", "requestedMbps": "2500",
                     "networkUri": 'ETH:mgmt_nw',
                     "lagName": None, "mac": None,
                     "wwpn": None, "wwnn": None,
                     "requestedVFs": "0", "ipv4": {},
                     "boot": {"priority": "NotBootable", "iscsi": {}}}]}

spt_profile = {
    "type": "ServerProfileV9",
    "serverHardwareUri": 'SH:' + servers[0]['serverHardwareUri'],
    "serverHardwareTypeUri": 'SHT:' + servers[0]['serverHardwareTypeUri'],
    "enclosureGroupUri": 'EG:EG-3enc',
    "serialNumberType": "Virtual", "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual", "wwnType": "Virtual",
    "name": "sp1_from_spt1",
    "description": "", "affinity": "Bay",
    "connectionSettings": connSettings,
    "boot": {"manageBoot": True, "order": ["HardDisk"]},
    "bootMode": {"manageMode": True, "mode": "UEFIOptimized",
                 "secureBoot": "Unmanaged", "pxeBootPolicy": "Auto"},
    "firmware": {"manageFirmware": False, "firmwareBaselineUri": "",
                 "forceInstallFirmware": False, "firmwareInstallType": None,
                 "firmwareScheduleDateTime": "", "firmwareActivationType": "Immediate"},
    "bios": {"manageBios": False, "overriddenSettings": []},
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": {
        "osDeploymentPlanUri": "oedp_deploy_esxi6.5",
        "osCustomAttributes": [{"name": "DomainName", "value": "lab.local", "constraints": "{\"helpText\":\"\"}", "type": "fqdn"},
                               {"name": "Hostname", "value": "{enclosure}", "constraints": "{\"helpText\":\"\"}", "type": "hostname"},
                               {"name": "ManagementNIC.connectionid", "value": "3"},
                               {"name": "ManagementNIC.dhcp", "value": "False"},
                               {"name": "ManagementNIC.ipv4disable", "value": "False"},
                               {"name": "ManagementNIC.networkuri", "value": 'ETH:mgmt_nw'},
                               {"name": "ManagementNIC.constraint", "value": "auto"},
                               {"name": "ManagementNIC.vlanid", "value": "0"},
                               {"name": "Password", "value": None},
                               {"name": "SSH", "value": "enabled", "constraints": "{\"options\":[\"enabled\"]}", "type": "option"}],
        "osVolumeUri": None,
        "forceOsDeployment": False},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": None,
    "initialScopeUris": []}

i3s_hosts = [{"encl_serial_number": "SGH708YL3H", "bay": 1},
             {"encl_serial_number": "SGH708YL3C", "bay": 1}]

BLADES = {'Blade1': 'SGH708YL3H, bay 2'}


# CLRM Inputs

admin_credentials = {'userName': 'Administrator', 'password': 'admin123'}
OV_IP = '15.212.164.238'
OV_credentials = {'userName': 'Administrator', 'password': 'admin123'}
APPLIANCE_IP = OV_IP
fusion_ip = OV_IP

golden_images = [
    {'name': 'CLRM_GI', 'description': 'valid_goldenimage', 'file': "valid_file"}
]

headers = {"Accept": "application/json, */*", "Accept-language": "en_US", "Content-Type": "application/json", "X-Api-Version": "800"}


deploymentplans = [
    {"type": "OEDeploymentPlanV5",
     "name": "CLRM_MAT_OSDP",
     "description": "",
     "goldenImageURI": "CLRM_GI",
     "oeBuildPlanURI": "HPE- ESXi - deploy in single frame non-HA config- 2017-11-29",
     "ostype": "ESXi",
     "hpProvided": "false",
     "customAttributes": [
         {"name": "SSH", "value": "enabled",
          "type": "option", "description": "",
          "editable": True, "visible": True,
          "constraints": "{\"options\":[\"enabled\"]}"},
         {"name": "ManagementNIC",
          "value": None, "type": "nic",
          "description": "", "editable": True,
          "visible": True,
          "constraints": "{\"ipv4static\":true,\"ipv4dhcp\":true,\"ipv4disable\":false,\"parameters\":[\"dns1\",\"dns2\",\"gateway\",\"ipaddress\",\"mac\",\"netmask\",\"vlanid\"]}"},
         {"name": "Password",
          "value": "", "type": "password",
          "description": "Password value must meet password complexity and minimum length requirements defined for ESXi 5.x, ESXi 6.x appropriately.",
          "editable": True, "visible": True,
          "constraints": "{}"},
         {"name": "DomainName",
          "value": "", "type": "fqdn",
          "description": "", "editable": True,
          "visible": True, "constraints": "{\"helpText\":\"\"}"},
         {"name": "Hostname", "value": "",
          "type": "hostname", "description": "",
          "editable": True, "visible": True,
          "constraints": "{\"helpText\":\"\"}"}]}]


clrm_mat_spt_var = [{'type': 'ServerProfileTemplateV5', 'name': 'CLRM_MAT_SPT',
                     'serverProfileDescription': 'Server Profile Template',
                     'iscsiInitiatorNameType': 'AutoGenerated',
                     'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1',
                     'enclosureGroupUri': 'EG:EG-3enc',
                     'affinity': 'Bay', 'hideUnusedFlexNics': True,
                     'firmware': {'forceInstallFirmware': False, 'manageFirmware': False},
                     'macType': 'Virtual', 'wwnType': 'Virtual',
                     'osDeploymentSettings': {
                         'osDeploymentPlanUri': 'oedp_deploy_esxi6.5',
                         'osCustomAttributes': [{"name": "DomainName", "value": "lab.local", "constraints": "{\"helpText\":\"\"}", "type": "fqdn"},
                                                {"name": "Hostname", "value": "{enclosure}", "constraints": "{\"helpText\":\"\"}", "type": "hostname"},
                                                {"name": "ManagementNIC.connectionid", "value": "3"},
                                                {"name": "ManagementNIC.dhcp", "value": "False"},
                                                {"name": "ManagementNIC.ipv4disable", "value": "False"},
                                                {"name": "ManagementNIC.networkuri", "value": 'ETH:mgmt_nw'},
                                                {"name": "ManagementNIC.constraint", "value": "auto"},
                                                {"name": "ManagementNIC.vlanid", "value": "0"},
                                                {"name": "Password", "value": None},
                                                {"name": "SSH", "value": "enabled", "constraints": "{\"options\":[\"enabled\"]}", "type": "option"}]},
                     'connectionSettings': {
                         'manageConnections': True,
                         'connections': [{'id': 1, 'name': 'Deployment Network A',
                                          'functionType': 'Ethernet', 'networkUri': 'ETH:iscsi_nw',
                                          'portId': 'Mezz 3:1-a', 'requestedVFs': 'Auto', 'requestedMbps': '2500',
                                          'ipv4': {'ipAddressSource': 'SubnetPool'},
                                          'boot': {'bootVolumeSource': 'UserDefined',
                                                   'priority': 'Primary', 'ethernetBootType': 'iSCSI',
                                                   'iscsi': {'initiatorNameSource': 'ProfileInitiatorName'}}},
                                         {'id': 2, 'name': 'Deployment Network B',
                                          'functionType': 'Ethernet', 'networkUri': 'ETH:iscsi_nw',
                                          'portId': 'Auto', 'requestedVFs': 'Auto', 'requestedMbps': '2500',
                                          'ipv4': {'ipAddressSource': 'SubnetPool'},
                                          'boot': {'bootVolumeSource': 'UserDefined',
                                                   'priority': 'Secondary', 'ethernetBootType': 'iSCSI',
                                                   'iscsi': {'initiatorNameSource': 'ProfileInitiatorName'}}},
                                         {'id': 3, 'name': 'Blade_boot_mgmt',
                                          'functionType': 'Ethernet', 'networkUri': 'ETH:mgmt_nw',
                                          'portId': 'Auto', 'requestedVFs': 0, 'requestedMbps': '2500',
                                          'boot': {'priority': 'NotBootable', 'iscsi': {}}}]},
                     'bootMode': {'manageMode': True, 'pxeBootPolicy': 'Auto', 'mode': 'UEFIOptimized', 'secureBoot': 'Unmanaged'},
                     'boot': {'manageBoot': True, 'order': []},
                     'bios': {'manageBios': False, 'overriddenSettings': []},
                     'localStorage': {},
                     'sanStorage': None}]

vCenter_password = 'Orion!@#123'

Hypervisor_manager = [{'username': 'administrator@vsphere.local', 'password': vCenter_password, 'type': 'HypervisorManagerV2', 'name': '15.146.41.128', 'port': '443'}]

CERTIFICATE = {
    "certificateDetails": [{
        "aliasName": "Vcenter",
        "base64Data": "",
        "type": "CertificateDetailV2"
    }],
    "type": "CertificateInfoV2"
}

Cluster_payload = [{'type': 'HypervisorClusterProfileV3', 'name': 'CLRM_MAT_CLUSTER', 'path': 'Hybd', 'vcenter': '15.146.41.128',
                    'profile_name': 'CLRM_MAT_SPT', 'hypervisor_type': 'Vmware',
                    'server_password': 'hpVSE123#',
                    'server_hardware': [servers[0]['serverHardwareUri'], servers[1]['serverHardwareUri']],
                    'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

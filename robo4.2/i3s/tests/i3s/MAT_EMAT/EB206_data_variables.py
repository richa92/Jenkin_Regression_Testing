#from winnt import NULL
from requests.api import patch

linux = '1'
temp_OV_ip = '15.212.164.234'
netmask = '255.255.252.0'
gateway = '15.212.164.1'
vm_username = 'root'
vm_password = '1iso*help'
interface      = 'eno16780032'   #Local interface
interface_id  =  '252'
i3_interface   = 'bond1'    #i3s appliance mgmt interface
ov_interface	   = 'bond0'
admin_credentials = {'userName': 'Administrator', 'password': 'admin123'}
ov_appliances = ['fe80::1602:ecff:fe46:9450']
MAC = '14:02:ec:46:94:50'
i3s_appliances = ['fe80::9eb6:54ff:fe98:c108']
i3s_enclosure = ['CN75450628']
enclosures_count = '1'
DEFAULT_USER = 'Administrator'
status = '200'
NEW_PASSWORD = 'admin123'
#SUBNET_1 = '255.255.252.0'
#IPV4GATEWAY = '15.212.164.1'
#DOMAINNAME = 'hpecorp.net'
#HOSTNAME = 'EB2402.test.local'
#DNS1 = '16.110.135.51'
#DNS2 = '16.110.135.52'
#MAINTENANCEIP1 = '15.212.164.207'
#MAINTENANCEIP2 = '15.212.164.208'
CLUSTERIP = '15.212.164.206'
OV_ACTIVE = 'fe80::1602:ecff:fe46:9450'                             
#i3s_version= '4.00.00-0319447'
#ov_version= '4.00.00-0319900'
build_server = 'fe80::250:56ff:fe97:325f'
build_version = '5.00'
blade_IP= '15.212.164.250'
support_dump_loc= 'C:\support_dump\sd'
fusion_IP = '15.212.164.206'


network = {"type": "ApplianceNetworkConfiguration",
           "applianceNetworks": [{"activeNode": 1,
                                  "unconfigure": False,
                                  "app1Ipv4Addr": "15.212.164.207", "app1Ipv6Addr": "",
                                  "app2Ipv4Addr": "15.212.164.208", "app2Ipv6Addr": "",
                                  "virtIpv4Addr": "15.212.164.206", "virtIpv6Addr": None,
                                  "app1Ipv4Alias": None, "app1Ipv6Alias": None,
                                  "app2Ipv4Alias": None, "app2Ipv6Alias": None,
                                  "hostname": "EB2405.test.local",
                                  "confOneNode": True, "interfaceName": "",
                                  "macAddress": "14:02:ec:46:94:50",
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

servers = [{'serverHardwareUri': 'SGH724SLP1, bay 3', 'serverHardwareTypeUri': 'SY 480 Gen9 1'},
           {'serverHardwareUri': 'SGH724SLP1, bay 5', 'serverHardwareTypeUri': 'SY 480 Gen9 1'}]

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
                    'startAddress': '15.212.164.209', 'endAddress': '15.212.164.213',
                    'name': 'mgmt_nw', 'subnetUri': ' '}

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
				

				
sd_body = [{"encrypt": False, "errorCode": "CI", "userName": "administrator", "password": "admin123"}, {
    "encrypt": True, "errorCode": "CI", "userName": "backup", "password": "admin123"}, {"encrypt": False, "errorCode": "CI"}]

lig_tbird_1enc = {'type': 'logical-interconnect-groupV4',
                 'ethernetSettings': {'type': 'EthernetInterconnectSettingsV4', 'enableIgmpSnooping': False, 'igmpIdleTimeoutInterval': 260, 'enableFastMacCacheFailover': True, 'macRefreshInterval': 5, 'enableNetworkLoopProtection': True, 'enablePauseFloodProtection': True, 'enableRichTLV': False, 'interconnectType': 'Ethernet', 'dependentResourceUri': None, 'name': 'defaultEthernetSwitchSettings', 'category': None, 'uri': '/ethernetSettings'},
                 'description': None,
                 'name': 'LIG-1enc',
                 'interconnectMapTemplate':
                 {'interconnectMapEntryTemplates': [
                     {'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Enclosure', 'relativeValue': 1}]}, 'permittedInterconnectTypeUri': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1}]},

                 'enclosureType': 'SY12000',
                 'enclosureIndexes': [1],
                 'interconnectBaySet': '3',
                 'redundancyType': 'NonRedundantASide',
                 'internalNetworkUris': [],
                 'snmpConfiguration': {'type': 'snmp-configuration', 'readCommunity': 'public', 'systemContact': '', 'trapDestinations': None, 'snmpAccess': None, 'enabled': False, 'v3Enabled': True,'description': None, 'name': None, 'state': None, 'category': 'snmp-configuration'},
                 'qosConfiguration': None,
                 'uplinkSets':[
                    {'networkUris':['iscsi_nw'],'mode':'Auto','lacpTimer':'Short','primaryPort':None,
                    'logicalPortConfigInfos':[{'desiredSpeed':'Auto','logicalLocation':{'locationEntries':[{'type':'Bay','relativeValue':3},{'type':'Port','relativeValue':62},{'type':'Enclosure','relativeValue':1}]}}],
                    'networkType':'Ethernet','ethernetNetworkType':'Tagged','name':'uplink_1'},
					
					{'networkUris':['mgmt_nw'],'mode':'Auto','lacpTimer':'Short','primaryPort':None,
                    'logicalPortConfigInfos':[{'desiredSpeed':'Auto','logicalLocation':{'locationEntries':[{'type':'Bay','relativeValue':3},{'type':'Port','relativeValue':77},{'type':'Enclosure','relativeValue':1}]}}],
					'networkType':'Ethernet','ethernetNetworkType':'Untagged','name':'uplink_2'}
                    ]
                 }
				 
enc_groups_tbird_1enc = {'name': 'EG-1enc',
'powerMode': 'RedundantPowerFeed',
'ambientTemperatureMode': 'Standard',
'ipAddressingMode': 'External',
'ipRangeUris': [],
'enclosureCount': 1,
'osDeploymentSettings':{'manageOSDeployment':True,'deploymentModeSettings':{'deploymentMode':'External','deploymentNetworkUri': ['iscsi_nw']}},
'interconnectBayMappings': [
                                {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG-1enc'},
                           ]
}

les_1enc = {'name': 'LE-1enc',
            'enclosureUris': ['ENC:CN75450628'],
            'enclosureGroupUri': 'EG:EG-1enc',
            'firmwareBaselineUri': None,
            'forceInstallFirmware': False
            }

osdeploymentserver = {'name': 'OSDS-1enc', 'description': 'os deployment server',
                      'applianceUri': 'CN75450628, appliance 2', 'mgmtNetworkUri': ['mgmt_nw'],
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
deploymentplan_update = [
    {"type": "OEDeploymentPlanV5",
     "hpProvided": "false",
     "customAttributes": [{"visible": True, "constraints": "{}",
                           "editable": True, "description": "ssh enabled",
                           "name": "SSH", "value": "enabled", "type": "string"}],
     "goldenImageURI": "Test",
     "oeBuildPlanURI": "oebp_deploy_for_e2e_test",
     "category": "oe-deployment-plans",
     "description": "Deployment Plan",
     "name": "oedp_deploy_for_e2e_test"},
    {"type": "OEDeploymentPlanV5",
     "name": "oedp_deploy_esxi6.5",
     "description": "",
     "goldenImageURI": "Test",
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

artifactbundle_delete = {'name': 'HPE-ESXi-2017-03-24'}

artifactbundle = {'name': 'ab_automate_1',
                  'description': 'ab with deploymentplan only',
                  'deploymentPlans': [{'resourceUri': 'oedp_deploy_for_e2e_test', 'readOnly': False}]}

artifactbundle_update = {'name': 'ab_automate_update', 'type': 'ArtifactsBundle'}

artifactbundle_add = {'name': 'c:/Users/Administrator/GoldenImage_download/HPE-ESXi-2017-03-24.zip'}

artifactbundle_extract = {'name': 'HPE-ESXi-2017-03-24'}

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

serverprofile_3enc = {"type": "ServerProfileV6", "serverHardwareUri": "SH:SGH724SLP1, bay 4",
     "serverHardwareTypeUri": "SHT:SY 480 Gen9 1", "enclosureGroupUri": "EG:EG-3enc",
     'enclosureUri': 'ENC:SGH724SLP1', "serialNumberType": "Virtual",
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
     'connectionSettings': {'connections': [
         {'id': 1, 'name': 'Deployment Network A',
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
     'connectionSettings': {'connections': [
         {'id': 1, 'name': 'Deployment Network A',
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
    "type": "ServerProfileV6",
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

i3s_hosts = [{"encl_serial_number": "SGH724SLP1", "bay": 2}]

BLADES = {'Blade1': 'SGH724SLP1, bay 4'}

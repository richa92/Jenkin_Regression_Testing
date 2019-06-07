from winnt import NULL
from requests.api import patch

CHLORIDEX = 'CHLORIDE20'                                                                     # Chloride hardware available in test rack

POTASH = 'Virtual Connect SE 40Gb F8 Module for Synergy'
CHLORIDE10  = 'Synergy 10Gb Interconnect Link Module'
CHLORIDE20 = 'Synergy 20Gb Interconnect Link Module'

fusion_IP = '15.212.164.150'
fusion_IPv6= 'fe80::1602:ecff:fe45:af78'

ov_appliances = ['fe80::1602:ecff:fe45:af78', 'fe80::9eb6:54ff:fe98:c2f0']                    # list of ov appliance ipv6 addresses
OV_ACTIVE = 'fe80::1602:ecff:fe45:af78'                                                       # Ov ipv6 which is to be set as Active, incase there are more than 1 OV
i3s_appliances = ['fe80::1602:ecff:fe45:1de8', 'fe80::9eb6:54ff:fe98:6668']                   # list of i3s appliance ipv6 addresses
i3s_enclosure = ['SGH708YL3J', 'SGH724SLP0']
enclosures_count = '3'                                                                        # count of enclosures in test setup


DEFAULT_USER = 'Administrator'                                                                # default OV UI login username
DEFAULT_PASSWORD= 'admin123'                                                                  # new password user wishes to set for OV after first time login
status = '200'


Ov_Build_sha = 'HPEOneView-SSH-4.00.00-0320990_signed-withsig.zip.sha256'                     # OV build sha256 filename
OV_Build = 'HPEOneView-SSH-4.00.00-0320990_signed-withsig.zip'                                # OV build filename

I3S_Build_sha = 'HPEImageStreamer-SSH-4.00.00-0321181-withsig.zip.sha256'                     # I3s build sha256 filename
I3S_Build = 'HPEImageStreamer-SSH-4.00.00-0321181-withsig.zip'                                # I3s build filename
build_server = 'fe80::94c7:b59:8878:e979'                                                     # Windows IIS to download the builds from

mgmt_subnet = '15.212.164.0'                                                                  # mgmt n/wk subnet
deploy_subnet = '192.168.0.0'                                                                 # deploy n/wk subnet

mgmt_ip_range = 'mgmt_nw'                                                                     # mgmt ip range name
deploy_ip_range = 'iscsi_nw'                                                                  # deployment ip range name

mgmt_network_name = 'mgmt_nw'                                                                 # mgmt n/wk name
deploy_network_name = 'iscsi_nw'                                                              # deployment n/wk name

osdeploymentserver_name = 'OSDS-3enc'                                                         # osdeployment server name

#-------------------------------------------------------------------------------------------------------------------------------------------------------
network = {
	"type": "ApplianceNetworkConfigurationV2",
	"applianceNetworks": [{
		"activeNode": 1,
		"unconfigure": False,
		"app1Ipv4Addr": "15.212.164.152",                                                     # OV maintenance1 ipv4 
		"app1Ipv6Addr": "",
		"app2Ipv4Addr": "15.212.164.151",                                                     # OV maintenance2 ipv4
		"app2Ipv6Addr": "",
		"virtIpv4Addr": "15.212.164.150",                                                     # OV cluster ipv4
		"virtIpv6Addr": None,
		"app1Ipv4Alias": None,
		"app1Ipv6Alias": None,
		"app2Ipv4Alias": None,
		"app2Ipv6Alias": None,
		"hostname": "eb2512",                                                                # OV hostname as displayed in OV Settings->Networking UI
		"confOneNode": True,
		"interfaceName": "",
		"macAddress": "14:02:ec:45:af:78",                                                   # OV mac address, can be got from ssh session to ov, have the mac in all small letters
		"ipv4Type": "STATIC",
		"ipv6Type": "UNCONFIGURE",
		"overrideIpv4DhcpDnsServers": False,
		"ipv4Subnet": "255.255.252.0",                                                       # ov ipv4 netmask
		"ipv4Gateway": "15.212.164.1",                                                       # ov ipv4 gateway
		"ipv6Subnet": None,
		"ipv6Gateway": None,
		"domainName": None,
		"searchDomains": [],
		"ipv4NameServers": ["", ""],
		"ipv6NameServers": ["", ""],
		"bondedTo": None,
		"aliasDisabled": True
	}]
}


subnet = [{'type': 'Subnet',
           'gateway': '192.168.0.1',                                                         # deployment n/wk gateway
           'networkId': '192.168.0.0',                                                       # deployment n/wk subnet
           'subnetmask': '255.255.0.0',                                                      # deployment n/wk netmask
           'dnsServers': [                          
                    ],
            'domain': 'vse.rdlabs.hpecorp.net'},                                             # deployment n/wk domain name
          
          {'type': 'Subnet',
           'gateway': '15.212.164.1',                                                        # mgmt n/wk gateway
           'networkId': '15.212.164.0',                                                      # mgmt n/wk subnet
           'subnetmask': '255.255.252.0',                                                    # mgmt n/wk netmask
           'dnsServers': [
                    '16.110.135.51',                                                         # mgmt n/wk dns1 server
					'16.110.135.52'                                                          # mgmt n/wk dns2 server
                        ],
            'domain': 'vse.rdlabs.hpecorp.net'}                                              # mgmt n/wk domain name
]
range_enable = [{'type': 'Range',
                 'enabled': 'true'}
                ]
range_disable = [{'type': 'Range',
                  'enabled': 'false'}
                 ]

ipv4ranges = [{'type': 'Range',
               'startAddress': '192.168.20.10',                                             # deployment n/wk start ip address
               'endAddress': '192.168.20.50',                                               # deployment n/wk end ip address
               'name': 'iscsi_nw',                                                          # deployment n/wk address range name
               'subnetUri': ' '},          
              {'type': 'Range',
               'startAddress': '15.212.164.153',                                            # mgmt n/wk start ip address
               'endAddress': '15.212.164.165',                                              # mgmt n/wk end ip address
               'name': 'mgmt_nw',                                                           # mgmt n/wk address range name
               'subnetUri': ' '}
              ]

Ethernet_network_1 = [
    {'vlanId': '2512',                                                                      # deployment n/wk vland id
     'ethernetNetworkType': 'Tagged',
     'subnetUri': '',
     'purpose':'ISCSI',
     'name':'iscsi_nw',                                                                     # deployment n/wk name
     'smartLink': False,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV4'},

	 

    {'vlanId': '0',
     'ethernetNetworkType': 'Untagged',
     'subnetUri': '',
     'purpose': 'Management',
     'name': 'mgmt_nw',                                                                    # mgmt n/wk name
     'smartLink': False,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV4'}
]

lig_tbird_3enc = {'type': 'logical-interconnect-groupV4',
                 'ethernetSettings': {'type': 'EthernetInterconnectSettingsV4', 'enableIgmpSnooping': False, 'igmpIdleTimeoutInterval': 260, 'enableFastMacCacheFailover': True, 'macRefreshInterval': 5, 'enableNetworkLoopProtection': True, 'enablePauseFloodProtection': True, 'enableRichTLV': False, 'interconnectType': 'Ethernet', 'dependentResourceUri': None, 'name': 'defaultEthernetSwitchSettings', 'category': None, 'uri': '/ethernetSettings'},
                 'description': None,
                 'name': 'LIG-3enc',                                                                                                                                                                                                                           # lig name
                 'interconnectMapTemplate':
                 {'interconnectMapEntryTemplates': [
                     {'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Enclosure', 'relativeValue': 1}]}, 'permittedInterconnectTypeUri': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},         # permittedInterconnectTypeUri should have the interconnect available in bay3 of Enclosure1 which is Potash always
                     {'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 6}, {'type': 'Enclosure', 'relativeValue': 2}]}, 'permittedInterconnectTypeUri': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},         # permittedInterconnectTypeUri should have the interconnect available in bay6 of Enclosure2 which is Potash always
                     {'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 6}, {'type': 'Enclosure', 'relativeValue': 1}]}, 'permittedInterconnectTypeUri': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},                 # permittedInterconnectTypeUri should have the interconnect available in bay6 of Enclosure1 which is Chloride , can be 'Synergy 20Gb Interconnect Link Module'/'Synergy 10Gb Interconnect Link Module'
                     {'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Enclosure', 'relativeValue': 2}]}, 'permittedInterconnectTypeUri': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},                 # permittedInterconnectTypeUri should have the interconnect available in bay3 of Enclosure2 which is Chloride , can be 'Synergy 20Gb Interconnect Link Module'/'Synergy 10Gb Interconnect Link Module'
                     {'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 6}, {'type': 'Enclosure', 'relativeValue': 3}]}, 'permittedInterconnectTypeUri': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3},                 # permittedInterconnectTypeUri should have the interconnect available in bay3 of Enclosure6 which is Chloride , can be 'Synergy 20Gb Interconnect Link Module'/'Synergy 10Gb Interconnect Link Module'   
                     {'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Enclosure', 'relativeValue': 3}]}, 'permittedInterconnectTypeUri': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3}]},               # permittedInterconnectTypeUri should have the interconnect available in bay6 of Enclosure2 which is Chloride , can be 'Synergy 20Gb Interconnect Link Module'/'Synergy 10Gb Interconnect Link Module'

                 'enclosureType': 'SY12000',
                 'enclosureIndexes': [1, 2, 3],
                 'interconnectBaySet': '3',
                 'redundancyType': 'HighlyAvailable',
                 'internalNetworkUris': [],
                 'snmpConfiguration': {'type': 'snmp-configuration','v3Enabled': True, 'readCommunity': 'public', 'systemContact': '', 'trapDestinations': None, 'snmpAccess': None, 'enabled': True, 'description': None, 'name': None, 'state': None, 'category': 'snmp-configuration'},
                 'qosConfiguration': None,
                 'uplinkSets':[
                    {'networkUris':['iscsi_nw'],'mode':'Auto','lacpTimer':'Short','primaryPort':None,                                                                                                                              # networkUris should have the deployment n/wk name
                    'logicalPortConfigInfos':[{'desiredSpeed':'Auto','logicalLocation':{'locationEntries':[{'type':'Bay','relativeValue':3},{'type':'Port','relativeValue':62},{'type':'Enclosure','relativeValue':1}]}},          # Modify the 'relative value' in this block {relative value'{'type':'Port','relativeValue':62}} to have bay3 Potash port which is connected to EM Mgmt port (here the Potash port no is Q1:1), the relative value in this block specifies the enclosure where the potash is available {'type':'Enclosure','relativeValue':1}
											  {'desiredSpeed':'Auto','logicalLocation':{'locationEntries':[{'type':'Bay','relativeValue':3},{'type':'Port','relativeValue':63},{'type':'Enclosure','relativeValue':1}]}},          # Modify the 'relative value' in this block {relative value'{'type':'Port','relativeValue':63}} to have bay3 Potash port which is connected to EM Mgmt port (here the Potash port no is Q1:2)
                                              {'desiredSpeed':'Auto','logicalLocation':{'locationEntries':[{'type':'Bay','relativeValue':6},{'type':'Port','relativeValue':63},{'type':'Enclosure','relativeValue':2}]}}, 	       # Modify the 'relative value' in this block {relative value'{'type':'Port','relativeValue':63}} to have bay6 Potash port which is connected to EM Mgmt port (here the Potash port no is Q1:2)
                                              {'desiredSpeed':'Auto','logicalLocation':{'locationEntries':[{'type':'Bay','relativeValue':6},{'type':'Port','relativeValue':62},{'type':'Enclosure','relativeValue':2}]}}],         # Modify the 'relative value' in this block {relative value'{'type':'Port','relativeValue':63}} to have bay6 Potash port which is connected to EM Mgmt port (here the Potash port no is Q1:1)
                     'networkType':'Ethernet','ethernetNetworkType':'ImageStreamer','name':'uplink_3encl'},                                                                                                                        # deployment uplink name to be given for name
                    
                    ]
                 }
				 
enc_groups_tbird_3enc = {'name': 'EG-2512',                                                                                              # EG name
'powerMode': 'RedundantPowerFeed',
'ambientTemperatureMode': 'Standard',
'ipAddressingMode': 'External',
'ipRangeUris': [],
'enclosureCount': 3,
'configurationScript': None,
'osDeploymentSettings':{'manageOSDeployment':True,'deploymentModeSettings':{'deploymentMode':'Internal','deploymentNetworkUri': None}},
'interconnectBayMappings': [
                                {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG-3enc'},                                  # Lig name, my lig name is 'LIG-3enc'
                                {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG-3enc'}                                   # Lig name, my lig name is 'LIG-3enc'
                             ]      
}
 
les_3enc = {'name': 'LE-2512',                                                                                                           # LE name
            'enclosureUris': ['ENC:SGH708YL3D','ENC:SGH708YL3J','ENC:SGH724SLP0'],                                                       # give enclosure names in same positional order in the rack
            'enclosureGroupUri': 'EG:EG-2512',                                                                                           # give EG name for 'enclosureGroupUri', my EG name here is 'EG-3enc'
            'firmwareBaselineUri': None,
            'forceInstallFirmware': False
            }
			
osdeploymentserver = { 'name' : 'OSDS-3enc',                                                                                              # osds name
'description': 'os deployment server',
'applianceUri':'SGH724SLP0, appliance 2',                                                                                                 # Give i3s appliance available enclosure, bay no, which is to be made active appliance
'mgmtNetworkUri':['mgmt_nw'],
'deplManagersType':'Image Streamer'
}

goldenimage = {'name': 'GoldenImage_e2e',
               'description': 'valid_goldenimage',
               'file': "valid_file"
              }
              
planscript = {
                "type": "PlanScript",
                "description": "valid deploy planscript",
                "name": "ps_deploy_for_e2e_test",
                "hpProvided": "false",
                "planType": "deploy",
                "content": "# Mount /bootbank area for ESXi 5.5+ \r\n#\r\n# Typical partition layout is:\r\n# 1 - UEFI ESP\r\n# 5 - /bootbank  <= holds ESXi host state to be configured\r\n# 6 - /altbootbank\r\n\r\necho \"########################################\"\r\necho \"Mount ESXi /bootbank\"\r\necho \"########################################\"\r\n\r\n# List structure storage layout found in ESXi Golden Image / OS Volume\r\necho \"Devices:\"\r\n-list-devices\r\necho\r\necho \"Partitions:\"\r\n-list-partitions\r\necho\r\necho \"File systems:\"\r\n-list-filesystems\r\necho\r\n\r\necho \"Mount file systems:\"\r\necho \"/dev/sda5 is assumed to hold ESXi host state configuration\"\r\necho \"mount /dev/sda5\"\r\nmount /dev/sda5 /\r\necho \"File system details for /dev/sda5:\"\r\n-statvfs /\r\necho\r\necho \"########################################\"\r\necho \"Copy out and unpack ESXi host state\"\r\necho \"########################################\"\r\n\r\necho \"Create ImageStreamer temp directory\"\r\n-mkdir /ImageStreamer\r\necho\r\n\r\necho \"Extract ESXi host configuration from Golden Image\"\r\necho \"Copy out boot.cfg\"\r\ndownload /boot.cfg boot.cfg\r\necho \"Copy out state.tgz if present\"\r\n-download /state.tgz state.tgz\r\necho \"Copy out onetime.tgz if present\"\r\n-download /onetime.tgz onetime.tgz\r\necho\r\n\r\necho \"Build esxi_unpack ESXi host state unpack script\"\r\nupload -<<END /ImageStreamer/esxi_unpack\r\n#! /bin/bash\r\nDIR=`pwd`\r\n\r\necho \"Finding ESXi host state configuration archive in Golden Image\"\r\nSTATE=`grep -c onetime.tgz $DIR/boot.cfg`\r\nif [ \"$STATE\" -eq \"0\" ]; then\r\n    echo\r\n    echo \"Unpack state.tgz\"\r\n    mkdir $DIR/esxi_state\r\n    cd $DIR/esxi_state\r\n    tar xvpzf $DIR/state.tgz\r\n    echo\r\n    echo \"Unpack local.tgz\"\r\n    mkdir $DIR/esxi_local\r\n    cd $DIR/esxi_local\r\n    tar xvpzf $DIR/esxi_state/local.tgz\r\n    echo\r\nelse\r\n    echo\r\n    echo \"Unpack onetime.tgz\"\r\n    mkdir $DIR/esxi_onetime\r\n    cd $DIR/esxi_onetime\r\n    tar xvpzf $DIR/onetime.tgz\r\n    echo\r\nfi\r\n\r\nif [ -e etc/rc.local.d/local.sh ]; then\r\n    cp etc/rc.local.d/local.sh $DIR/local.sh\r\nfi\r\n\r\necho \"Unpacking ESXi host state complete.\"\r\nexit 0\r\nEND\r\ndownload /ImageStreamer/esxi_unpack ./esxi_unpack\r\necho\r\n\r\necho \"Build esxi_repack ESXi host state repack script\"\r\nupload -<<END /ImageStreamer/esxi_repack\r\n#! /bin/bash\r\nDIR=`pwd`\r\n\r\necho \"---------------------------------------------------------------\"\r\necho \"Final ESXi host local.sh content for configuration at first boot:\"\r\ncat $DIR/local.sh\r\necho \"---------------------------------------------------------------\"\r\necho\r\n\r\necho \"Finding ESXi host state configuration archive\"\r\nSTATE=`grep -c onetime.tgz $DIR/boot.cfg`\r\nif [ \"$STATE\" -eq \"0\" ]; then\r\n    echo\r\n    echo \"Repack local.tgz\"\r\n    cd $DIR/esxi_local\r\n    mkdir -p etc/rc.local.d\r\n    cp $DIR/local.sh etc/rc.local.d/local.sh\r\n    chmod 777 etc/rc.local.d/local.sh\r\n    tar cvpzf $DIR/esxi_state/local.tgz *\r\n    echo\r\n    echo \"Repack state.tgz\"\r\n    cd $DIR/esxi_state\r\n    tar cvpzf $DIR/state.tgz *\r\n    echo\r\nelse\r\n    echo\r\n    echo \"Repack onetime.tgz\"\r\n    cd $DIR/esxi_onetime\r\n    mkdir -p etc/rc.local.d\r\n    cp $DIR/local.sh etc/rc.local.d/local.sh\r\n    chmod 777 etc/rc.local.d/local.sh\r\n    tar cvpzf $DIR/onetime.tgz *\r\n    touch $DIR/state.tgz\r\n    echo\r\nfi\r\necho \"Repacking ESXi host state complete.\"\r\nexit 0\r\nEND\r\ndownload /ImageStreamer/esxi_repack ./esxi_repack\r\necho\r\n\r\necho \"Run  esxi_repack ESXi host state unpack script\"\r\n!source ./esxi_unpack\r\necho\r\necho \"########################################\"\r\necho \"Configure ssh\"\r\necho \"########################################\"\r\n\r\nupload -<<END /ImageStreamer/esxi_ssh\r\n#!/bin/bash\r\nif [ \"@SSH:enabled@\" = \"enabled\" ]; then\r\ncat <<\"EOF\" >>local.sh\r\nvim-cmd hostsvc/enable_esx_shell\r\nvim-cmd hostsvc/start_esx_shell\r\nvim-cmd hostsvc/enable_ssh\r\nvim-cmd hostsvc/start_ssh\r\nservices.sh restart\r\n\r\nEOF\r\nfi\r\n\r\nexit 0\r\nEND\r\n\r\ndownload /ImageStreamer/esxi_ssh esxi_ssh\r\necho \"Run esxi_ssh\"\r\n!source ./esxi_ssh\r\necho \"########################################\"\r\necho \"Pack and replace ESXi host state into ESXi host OS Volume\"\r\necho \"########################################\"\r\n\r\necho \"Run  esxi_repack ESXi host state repack script\"\r\n!source ./esxi_repack\r\n\r\necho \"Copy in state.tgz if present\"\r\n-upload state.tgz /state.tgz \r\necho \"Copy in onetime.tgz if present\"\r\n-upload onetime.tgz /onetime.tgz\r\n\r\necho \"Remove Image Streamer temp directory\"\r\nrm-rf /tmp/ImageStreamer\r\necho \"########################################\"\r\necho \"Cleanup and unmount file systems \"\r\necho \"########################################\"\r\n\r\necho \"Remove ImageStreamer temp directory\"\r\nrm-rf /ImageStreamer\r\n\r\necho \"Unmount file systems\"\r\numount /\r\necho"
}

buildplan = {
              "type": "OeBuildPlanV5",
              "customAttributes": [
                {
                  "constraints": "{}",
                  "description": "To enable ssh",
                  "name": "SSH",
                  "value": "enabled",
                  "type": "string"
                }
              ],
              "buildStep": [
                {
                  "planScriptUri": "ps_deploy_for_e2e_test",
                  "serialNumber": "1",
                  "parameters" : "1"
                }
              ],
              "hpProvided": False,
   			  "oeBuildPlanType":"deploy",
              "description": "Buildplan",
              "name": "oebp_deploy_for_e2e_test"
}

deploymentplan = [{  
            "type": "OEDeploymentPlanV5",
            "hpProvided": "false",
            "customAttributes": [{
                "visible": True, 
                "constraints": "{}",
                "editable": True,
                "description": "ssh enabled",
                "name": "SSH",
                "value": "enabled",
                "type": "string"
            }],
            "goldenImageURI": "GoldenImage_e2e",
            "oeBuildPlanURI": "oebp_deploy_for_e2e_test",
            "category": "oe-deployment-plans",
            "description": "Deployment Plan",
            "name": "oedp_deploy_for_e2e_test"
},
{
	"type": "OEDeploymentPlanV5",
	"name": "oedp_deploy_esxi6.5",
	"description": "",
	"goldenImageURI": "GoldenImage_e2e",
	"oeBuildPlanURI": "HPE - ESXi - deploy in single frame non-HA config- 2017-03-24",
	"ostype": "ESXi",
	"hpProvided": "false",
	"customAttributes": [{
		"name": "SSH",
		"value": "enabled",
		"type": "option",
		"description": "",
		"editable": True,
		"visible": True,
		"constraints": "{\"options\":[\"enabled\"]}"
	}, {
		"name": "ManagementNIC",
		"value": None,
		"type": "nic",
		"description": "",
		"editable": True,
		"visible": True,
		"constraints": "{\"ipv4static\":true,\"ipv4dhcp\":true,\"ipv4disable\":false,\"parameters\":[\"dns1\",\"dns2\",\"gateway\",\"ipaddress\",\"mac\",\"netmask\",\"vlanid\"]}"
	}, {
		"name": "Password",
		"value": "",
		"type": "password",
		"description": "Password value must meet password complexity and minimum length requirements defined for ESXi 5.x, ESXi 6.x appropriately.",
		"editable": True,
		"visible": True,
		"constraints": "{}"
	}, {
		"name": "DomainName",
		"value": "",
		"type": "fqdn",
		"description": "",
		"editable": True,
		"visible": True,
		"constraints": "{\"helpText\":\"\"}"
	}, {
		"name": "Hostname",
		"value": "",
		"type": "hostname",
		"description": "",
		"editable": True,
		"visible": True,
		"constraints": "{\"helpText\":\"\"}"
	}]
}
]


buildplan_delete=[{'name': 'HPE - ESXi - generalize full state - 2017-03-24'},
                  {'name': 'HPE - ESXi - deploy with multiple management NIC HA config- 2017-03-24'},
				  {'name': 'HPE - ESXi - deploy in single frame non-HA config- 2017-03-24'}
				  ]
				  
planscript_delete=[{'name': 'HPE - ESXi - configure management 1st NIC - 2017-03-16'},
                   {'name': 'HPE - ESXi - set password - 2017-03-15'},
				   {'name': 'HPE - ESXi - umount - 2017-03-15'},
				   {'name': 'HPE - ESXi - configure ssh - 2017-03-15'},
				   {'name': 'HPE - ESXi - repack state - 2017-03-15'},
				   {'name': 'HPE - ESXi - configure management 2nd NIC HA - 2017-03-15'},
				   {'name': 'HPE - ESXi - generalize host configuration - 2017-03-15'},
				   {'name': 'HPE - ESXi - mount - 2017-03-15'},
				   {'name': 'HPE - ESXi - unpack state - 2017-03-15'},
				   {'name': 'HPE - ESXi - configure iSCSI boot HA - 2017-03-15'}
                   ]
				   
artifactbundle_delete= {'name': 'HPE-ESXi-2017-03-24'}

artifactbundle = {
        'name':'ab_automate_1',
        'description':'ab with deploymentplan only',
        'deploymentPlans':[
        {
        'resourceUri':'oedp_deploy_for_e2e_test',
        'readOnly':False
        }  
        ]         
}
                   
artifactbundle_update = {
        'name':'ab_automate_update',
        'type':'ArtifactsBundle'       
}

artifactbundle_add = {
        'name':'c:/Users/Administrator/GoldenImage_download/HPE-ESXi-2017-03-24.zip'
}

artifactbundle_extract = {
        'name':'HPE-ESXi-2017-03-24' 
}


serverprofile_3enc = {'type':'ServerProfileV8',
'name':'i3s_serverprofile_for_ME',
'iscsiInitiatorNameType':'AutoGenerated',
'serverHardwareUri' : 'SGH708YL3D, bay 4',
'serverHardwareTypeUri' : 'SY 480 Gen9 1',
'enclosureGroupUri': 'EG-2512',
'enclosureUri':'SGH708YL3D',
'affinity':'Bay',
'hideUnusedFlexNics':True,
'firmware':{'firmwareInstallType': None,'forceInstallFirmware':False,'manageFirmware':False,'firmwareBaselineUri':None},
'macType':'Virtual',
'wwnType':'Virtual',
'connections':[
{'id':1,'name':'Deployment Network A','functionType':'Ethernet','networkUri':'iscsi_nw',
'portId':'Mezz 3:1-a','requestedVFs':'Auto','macType':'Virtual', 'wwpn': '', 'wwnn': '', 'mac':None,'requestedMbps':'2500',
'allocatedMbps':2500,'maximumMbps':20000,
'ipv4': {'ipAddress': None}, 
'boot': { 'priority': 'Primary','ethernetBootType': 'iSCSI',
		  'iscsi': {'initiatorNameSource': 'ProfileInitiatorName',
			 	    'firstBootTargetIp': None,'secondBootTargetIp': '','secondBootTargetPort': '', 
		            'initiatorName': None, 'bootTargetName': None, 'bootTargetLun': None
                    }
		}
}, {'id':2,'name':'Deployment Network B','functionType':'Ethernet','networkUri':'iscsi_nw',
'portId':'Mezz 3:2-a','requestedVFs':'Auto','macType':'Virtual', 'wwpn': '', 'wwnn': '', 'mac':None,'requestedMbps':'2500',
'allocatedMbps':2500,'maximumMbps':20000,
'ipv4': {'ipAddress': None}, 
'boot': { 'priority': 'Secondary','ethernetBootType': 'iSCSI',
		  'iscsi': {'initiatorNameSource': 'ProfileInitiatorName',
			 	    'firstBootTargetIp': None,'secondBootTargetIp': '','secondBootTargetPort': '', 
		            'initiatorName': None, 'bootTargetName': None, 'bootTargetLun': None
                    }
		}
}, {'id': 3,'name': 'tor-con','functionType': 'Ethernet','portId': 'Auto','requestedMbps': '2500',
	'networkUri': 'mgmt_nw','mac': None,'wwpn': None,'wwnn': None,'requestedVFs': '0','ipv4': {},
'boot': { 'priority': 'NotBootable','iscsi': {} 
        }
   }           ],		
'bootMode':{'manageMode':True,'pxeBootPolicy':'Auto','mode':'UEFIOptimized', 'secureBoot': 'Unmanaged'},
'boot':{'manageBoot':True,'order':['HardDisk']},
'bios':{'manageBios':False,'overriddenSettings':[]},
'localStorage':{'sasLogicalJBODs': [],
		'controllers': []},
'osDeploymentSettings':{'osDeploymentPlanUri':'oedp_deploy_esxi6.5',
                      'forceOsDeployment': False,
                      'osVolumeUri':None, 
'osCustomAttributes': [{'name': 'DomainName','value': 'hpe.com'}, 
                       {'name': 'Hostname','value': 'host1'}, 
					   {'name': 'ManagementNIC.dns1','value': '16.110.135.51'},
		               {'name': 'ManagementNIC.dns2','value': '16.110.135.52'},
		               {'name': 'ManagementNIC.gateway','value': '15.212.168.1'}, 
			           {'name': 'ManagementNIC.ipaddress','value': '15.212.168.96'},
                       {'name': 'ManagementNIC.netmask','value': '255.255.252.0'},
	                   {'name': 'ManagementNIC.connectionid','value': '3'},
		               {'name': 'ManagementNIC.dhcp','value': 'false'},
		               {'name': 'ManagementNIC.ipv4disable','value': 'false'},
                       {'name': 'ManagementNIC.vlanid','value': '0'},
		               {'name': 'ManagementNIC.networkuri','value': 'mgmt_nw'},
                       {'name': 'ManagementNIC.constraint','value': 'userspecified'},
			           {'name': 'Password','value': None},
					   {'name': 'SSH','value': 'enabled'}
					   ]
		             },  					  
'sanStorage': None
}



BLADES = {'Blade1'    :    ':SGH708YL3D, bay 4'}
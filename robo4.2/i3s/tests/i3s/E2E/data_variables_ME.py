from winnt import NULL
from requests.api import patch

admin_credentials = {'userName': 'Administrator', 'password': 'admin123'}

subnet = [{'type': 'Subnet',
           'gateway': '192.168.0.1',
           'networkId': '192.168.0.0',
           'subnetmask': '255.255.0.0',
           'dnsServers': [                          
                    ],
            'domain': 'vse.rdlabs.hpecorp.net'},   
          
          {'type': 'Subnet',
           'gateway': '15.212.168.1',
           'networkId': '15.212.168.0',
           'subnetmask': '255.255.252.0',
           'dnsServers': [
                    '16.110.135.51'
                        ],
            'domain': 'vse.rdlabs.hpecorp.net'}     
]
range_enable = [{'type': 'Range',
                 'enabled': 'true'}
                ]
range_disable = [{'type': 'Range',
                  'enabled': 'false'}
                 ]

ipv4ranges = [{'type': 'Range',
               'startAddress': '192.168.100.10',
               'endAddress': '192.168.100.50',
               'name': 'iscsi_nw',
               'subnetUri': ' '},              
              {'type': 'Range',
               'startAddress': '15.212.170.79',
               'endAddress': '15.212.170.83',
               'name': 'mgmt_nw',
               'subnetUri': ' '}
              ]

Ethernet_network_1 = [
    {'vlanId': '189',
     'ethernetNetworkType': 'Tagged',
     'subnetUri': '',
     'purpose':'ISCSI',
     'name':'iscsi_nw',
     'smartLink': False,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'vlanId': '0',
     'ethernetNetworkType': 'Untagged',
     'subnetUri': '',
     'purpose': 'Management',
     'name': 'mgmt_nw',
     'smartLink': False,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'}
]

lig_tbird_3enc = {'type': 'logical-interconnect-groupV300',
                 'ethernetSettings': {'type': 'EthernetInterconnectSettingsV201', 'enableIgmpSnooping': False, 'igmpIdleTimeoutInterval': 260, 'enableFastMacCacheFailover': True, 'macRefreshInterval': 5, 'enableNetworkLoopProtection': True, 'enablePauseFloodProtection': True, 'enableRichTLV': False, 'interconnectType': 'Ethernet', 'dependentResourceUri': None, 'name': 'defaultEthernetSwitchSettings', 'category': None, 'uri': '/ethernetSettings'},
                 'description': None,
                 'name': 'LIG-3enc',
                 'interconnectMapTemplate':
                 {'interconnectMapEntryTemplates': [
                     {'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Enclosure', 'relativeValue': 1}]}, 'permittedInterconnectTypeUri': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
                     {'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 6}, {'type': 'Enclosure', 'relativeValue': 2}]}, 'permittedInterconnectTypeUri': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
                     {'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 6}, {'type': 'Enclosure', 'relativeValue': 1}]}, 'permittedInterconnectTypeUri': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
                     {'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Enclosure', 'relativeValue': 2}]}, 'permittedInterconnectTypeUri': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
                     {'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 6}, {'type': 'Enclosure', 'relativeValue': 3}]}, 'permittedInterconnectTypeUri': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3},
                     {'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Enclosure', 'relativeValue': 3}]}, 'permittedInterconnectTypeUri': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3}]},

                 'enclosureType': 'SY12000',
                 'enclosureIndexes': [1, 2, 3],
                 'interconnectBaySet': '3',
                 'redundancyType': 'HighlyAvailable',
                 'internalNetworkUris': [],
                 'snmpConfiguration': {'type': 'snmp-configuration', 'readCommunity': 'public', 'systemContact': '', 'trapDestinations': None, 'snmpAccess': None, 'enabled': True, 'description': None, 'name': None, 'state': None, 'category': 'snmp-configuration'},
                 'qosConfiguration': None,
                 'uplinkSets':[
                    {'networkUris':['iscsi_nw'],'mode':'Auto','lacpTimer':'Short','primaryPort':None,
                    'logicalPortConfigInfos':[{'desiredSpeed':'Auto','logicalLocation':{'locationEntries':[{'type':'Bay','relativeValue':6},{'type':'Port','relativeValue':67},{'type':'Enclosure','relativeValue':2}]}},
                                              {'desiredSpeed':'Auto','logicalLocation':{'locationEntries':[{'type':'Bay','relativeValue':3},{'type':'Port','relativeValue':67},{'type':'Enclosure','relativeValue':1}]}},
                                              {'desiredSpeed':'Auto','logicalLocation':{'locationEntries':[{'type':'Bay','relativeValue':3},{'type':'Port','relativeValue':62},{'type':'Enclosure','relativeValue':1}]}},
                                              {'desiredSpeed':'Auto','logicalLocation':{'locationEntries':[{'type':'Bay','relativeValue':6},{'type':'Port','relativeValue':62},{'type':'Enclosure','relativeValue':2}]}}],
                    'networkType':'Ethernet','ethernetNetworkType':'ImageStreamer','name':'uplink_3encl'}
                    ]
                 }

enc_groups_tbird_3enc = {'name': 'EG-3enc',
'type': 'EnclosureGroupV300',
'enclosureTypeUri': '/rest/enclosure-types/SY12000',
'stackingMode': 'Enclosure',
'ipAddressingMode': 'External',
'ipRangeUris': [],
'interconnectBayMappingCount': 2,
'enclosureCount': 3,
'configurationScript': None,
'osDeploymentSettings':{'manageOSDeployment':True,'deploymentModeSettings':{'deploymentMode':'Internal','deploymentNetworkUri': None}},
'interconnectBayMappings': [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                             {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                                {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG-3enc'},
                                {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                                {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                                {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG-3enc'}
                             ]
}

les_3enc = {'name': 'LE-3enc',
            'enclosureUris': ['ENC:CN754408RY','ENC:CN7544043S','ENC:CN7545061L'],
            'enclosureGroupUri': 'EG:EG-3enc',
            'firmwareBaselineUri': None,
            'forceInstallFirmware': False
            }

osdeploymentserver = { 'name' : 'OSDS-3enc',
'description': 'os deployment server',
'applianceUri':'CN7544043S,CIM bay1',
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
              "type": "OeBuildPlan",
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
              "oeBuildPlanType": "deploy",
              "description": "Buildplan",
              "name": "oebp_deploy_for_e2e_test"
}

deploymentplan = {  
            "type": "OEDeploymentPlan",
            "hpProvided": False,
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
            "description": "Deployment Plan ",
            "name": "oep_deploy_for_e2e_test"
}

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
        'name':'c:/Goldenimage/ab_download.zip'
}

artifactbundle_extract = {
        'name':'ab_download'
}

serverprofile_1enc_nic = {'type':'ServerProfileV6',
'name':'i3s_serverprofile_automat1',
'iscsiInitiatorNameType':'AutoGenerated',
'serverHardwareUri' : '7U86XMVH6T, bay 7',
'serverHardwareTypeUri' : 'SY 480 Gen9 1',
'enclosureGroupUri': 'EG-3enc',
'enclosureUri':'7U86XMVH6T',
'affinity':'Bay',
'hideUnusedFlexNics':True,
'firmware':{'firmwareInstallType': None,'forceInstallFirmware':False,'manageFirmware':False,'firmwareBaselineUri':None},
'macType':'Virtual',
'wwnType':'Virtual',
'osDeploymentSettings':{'osDeploymentPlanUri':'oedp_deploy_for_e2e_test',
'osCustomAttributes':[{'name': 'hostname', 'value': 'bay7'},{'name': 'MACMGMT.dns1', 'value':'16.110.135.51'},{'name': 'MACMGMT.connectionid', 'value': 2},{'name': 'MACMGMT.constraint', 'value': 'userspecified'},{'name': 'MACMGMT.gateway', 'value': '15.212.168.1'},{'name': 'MACMGMT.ipaddress', 'value': '15.212.170.110'},{'name': 'MACMGMT.netmask', 'value': '255.255.252.0'}],'osVolumeUri':None},                                 
'connections':[
{'id':1,'name':'Deployment Network A','functionType':'Ethernet','networkUri':['iscsi_nw'],
'portId':'Mezz 3:1-a','requestedVFs':'Auto','allocatedVFs':24,'macType':'Virtual','wwpnType':'Virtual','mac':'','requestedMbps':'2500',
'allocatedMbps':2500,'maximumMbps':20000,
'boot':{'priority':'Primary','initiatorNameSource':'ProfileInitiatorName','chapLevel':'None'}
},
{'id':2,'name':'Blade_boot','functionType':'Ethernet','networkUri':['mgmt_nw'],
'portId':'Mezz 3:2-a','requestedVFs':0,'allocatedVFs':24,'macType':'Virtual','wwpnType':'Virtual','mac':'','requestedMbps':'2500',
'allocatedMbps':2500,'maximumMbps':10000,
'boot':{'priority':'NotBootable','initiatorNameSource':'ProfileInitiatorName','chapLevel':'None'}
}
],
'bootMode':{'manageMode':True,'pxeBootPolicy':'Auto','mode':'UEFIOptimized'},
'boot':{'manageBoot':True,'order':[]},
'bios':{'manageBios':False,'overriddenSettings':[]},
'localStorage':{},
'sanStorage':{'volumeAttachments':[],'manageSanStorage':False}
}

serverprofile_3enc = {'type':'ServerProfileV6',
'name':'i3s_serverprofile_for_ME',
'iscsiInitiatorNameType':'AutoGenerated',
'serverHardwareUri' : 'CN754408RY, bay 1',
'serverHardwareTypeUri' : 'SY 480 Gen9 1',
'enclosureGroupUri': 'EG-3enc',
'enclosureUri':'CN754408RY',
'affinity':'Bay',
'hideUnusedFlexNics':True,
'firmware':{'firmwareInstallType': None,'forceInstallFirmware':False,'manageFirmware':False,'firmwareBaselineUri':None},
'macType':'Virtual',
'wwnType':'Virtual',
'osDeploymentSettings':{'osDeploymentPlanUri':'oedp_deploy_for_e2e_test',
'osCustomAttributes':[{'name': 'SSH', 'value': 'enabled'}],
                      'osVolumeUri':None},              
'connections':[
{'id':1,'name':'Deployment Network A','functionType':'Ethernet','networkUri':['iscsi_nw'],
'portId':'Mezz 3:1-a','requestedVFs':'Auto','allocatedVFs':64,'macType':'Virtual','wwpnType':'Virtual','mac':'','requestedMbps':'2500',
'allocatedMbps':2500,'maximumMbps':10000,
'boot':{'priority':'Primary','initiatorNameSource':'ProfileInitiatorName','chapLevel':'None'}
},
{'id':2,'name':'Deployment Network B','functionType':'Ethernet','networkUri':['iscsi_nw'],
'portId':'Mezz 3:2-a','requestedVFs':'Auto','allocatedVFs':64,'macType':'Virtual','wwpnType':'Virtual','mac':'','requestedMbps':'2500',
'allocatedMbps':2500,'maximumMbps':10000,
'boot':{'priority':'Secondary','initiatorNameSource':'ProfileInitiatorName','chapLevel':'None'}
}],
'bootMode':{'manageMode':True,'pxeBootPolicy':'Auto','mode':'UEFIOptimized'},
'boot':{'manageBoot':True,'order':['HardDisk']},
'bios':{'manageBios':False,'overriddenSettings':[]},
'localStorage':{},
'sanStorage':{'volumeAttachments':[],'manageSanStorage':False}
}

BLADES = {'Blade1'    :    'CN754408RY, bay 1'}
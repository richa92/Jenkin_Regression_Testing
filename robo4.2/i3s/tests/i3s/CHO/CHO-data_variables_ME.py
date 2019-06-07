from winnt import NULL
from requests.api import patch

admin_credentials = {'userName': 'Administrator', 'password': 'admin123'}


les_3enc = {'name': 'LE',
            'enclosureUris': ['ENC:SGH708YL3F', 'ENC:SGH708YL3C', 'ENC:SGH708YL3H'],
            'enclosureGroupUri': 'EG:EG',
            'firmwareBaselineUri': None,
            'forceInstallFirmware': False
            }

osdeploymentserver = {'name': 'OSDS-3enc',
                      'description': 'os deployment server',
                      'applianceUri': 'CN7544043S,CIM bay1',
                      'mgmtNetworkUri': ['mgmt_nw'],
                      'deplManagersType': 'Image Streamer'
                      }

goldenimage = {'name': 'CHO GI',
               'description': 'ESXi 6.5',
               'file': "valid_file"
               }


planscript = [{
    "type": "PlanScript",
    "description": "Mount Script",
    "name": "PS_MOUNT",
    "hpProvided": "false",
    "planType": "general",
    "content": "# Mount /bootbank area for ESXi 5.x, 6.x \n#\n# Typical partition layout is:\n# 1 - UEFI ESP\n# 5 - /bootbank  <= holds ESXi host state to be configured\n# 6 - /altbootbank\n\necho \"########################################\"\necho \"Mount ESXi /bootbank\"\necho \"########################################\"\n\n# List structure storage layout found in ESXi Golden Image / OS Volume\necho \"Devices:\"\n-list-devices\necho\necho \"Partitions:\"\n-list-partitions\necho\necho \"File systems:\"\n-list-filesystems\necho\n\necho \"Mount file systems:\"\necho \"/dev/sda5 is assumed to hold ESXi host state configuration\"\necho \"mount /dev/sda5\"\nmount /dev/sda5 /\necho \"File system details for /dev/sda5:\"\n-statvfs /\necho"
}, {
    "type": "PlanScript",
    "description": 'Unpack Script',
    "name": "PS_UNPACK",
    "hpProvided": "false",
    "planType": "general",
    "content": "echo \"########################################\"\necho \"Copy out and unpack ESXi host state\"\necho \"########################################\"\n\necho \"Create ImageStreamer temp directory\"\n-mkdir /ImageStreamer\necho\n\necho \"Extract ESXi host configuration from Golden Image\"\necho \"Copy out boot.cfg\"\ndownload /boot.cfg boot.cfg\necho \"Copy out state.tgz if present\"\n-download /state.tgz state.tgz\necho \"Copy out onetime.tgz if present\"\n-download /onetime.tgz onetime.tgz\necho\n\necho \"Build esxi_unpack ESXi host state unpack script\"\nupload -<<END /ImageStreamer/esxi_unpack\n#! /bin/bash\nDIR=`pwd`\n\necho \"Finding ESXi host state configuration archive in Golden Image\"\nSTATE=`grep -c onetime.tgz $DIR/boot.cfg`\nif [ \"$STATE\" -eq \"0\" ]; then\n    echo\n    echo \"Unpack state.tgz\"\n    mkdir $DIR/esxi_state\n    cd $DIR/esxi_state\n    tar xvpzf $DIR/state.tgz\n    echo\n    echo \"Unpack local.tgz\"\n    mkdir $DIR/esxi_local\n    cd $DIR/esxi_local\n    tar xvpzf $DIR/esxi_state/local.tgz\n    echo\nelse\n    echo\n    echo \"Unpack onetime.tgz\"\n    mkdir $DIR/esxi_onetime\n    cd $DIR/esxi_onetime\n    tar xvpzf $DIR/onetime.tgz\n    echo\nfi\n\nif [ -e etc/rc.local.d/local.sh ]; then\n    cp etc/rc.local.d/local.sh $DIR/local.sh\nfi\n\necho \"Unpacking ESXi host state complete.\"\nexit 0\nEND\ndownload /ImageStreamer/esxi_unpack ./esxi_unpack\necho\n\necho \"Build esxi_repack ESXi host state repack script\"\nupload -<<END /ImageStreamer/esxi_repack\n#! /bin/bash\nDIR=`pwd`\n\necho \"---------------------------------------------------------------\"\necho \"Final ESXi host local.sh content for configuration at first boot:\"\ncat $DIR/local.sh\necho \"---------------------------------------------------------------\"\necho\n\necho \"Finding ESXi host state configuration archive\"\nSTATE=`grep -c onetime.tgz $DIR/boot.cfg`\nif [ \"$STATE\" -eq \"0\" ]; then\n    echo\n    echo \"Repack local.tgz\"\n    cd $DIR/esxi_local\n    mkdir -p etc/rc.local.d\n    cp $DIR/local.sh etc/rc.local.d/local.sh\n    chmod 777 etc/rc.local.d/local.sh\n    tar cvpzf $DIR/esxi_state/local.tgz *\n    echo\n    echo \"Repack state.tgz\"\n    cd $DIR/esxi_state\n    tar cvpzf $DIR/state.tgz *\n    echo\nelse\n    echo\n    echo \"Repack onetime.tgz\"\n    cd $DIR/esxi_onetime\n    mkdir -p etc/rc.local.d\n    cp $DIR/local.sh etc/rc.local.d/local.sh\n    chmod 777 etc/rc.local.d/local.sh\n    tar cvpzf $DIR/onetime.tgz *\n    touch $DIR/state.tgz\n    echo\nfi\necho \"Repacking ESXi host state complete.\"\nexit 0\nEND\ndownload /ImageStreamer/esxi_repack ./esxi_repack\necho\n\necho \"Run  esxi_repack ESXi host state unpack script\"\n!source ./esxi_unpack\necho"
}, {
    "type": "PlanScript",
    "description": "Single Nic With VLAN Script",
    "name": "PS_SINGLE_NIC_WITH_VLAN",
    "hpProvided": 'false',
    "planType": "deploy",
    "content": "echo \"Network values\"\necho \"ManagementNIC1\"\necho @ManagementNIC1.mac@\necho @ManagementNIC1.vlanid@\necho @ManagementNIC1.ipaddress@\necho @ManagementNIC1.netmask@\necho @ManagementNIC1.gateway@\necho @ManagementNIC1.dns1@\necho @ManagementNIC1.dns2@\n\necho \"########################################\"\necho \"Configure ESXi host management network-NIC1\"\necho \"########################################\"\n\necho \"Check Image Streamer capture details\"\n-download /ImageStreamerCapture ./ImageStreamerCapture\n\nupload -<<END /ImageStreamer/check_capture\n#!/bin/bash\nif [ -f ./ImageStreamerCapture ]; then\n    echo \"Capture details:\"\n    cat ./ImageStreamerCapture\nelse\n    echo\n    echo \"WARNING: ESXi Golden Image was not captured by Image Streamer.\"\n    echo \"Golden Image may not be prepared for correct personalization.\"\n    echo \"Recommend deploying Golden Image as is and capturing a new\"\n    echo \"Golden Image using Image Streamer via correct capture Build Plan\"\n    echo\nfi\necho\nEND\ndownload /ImageStreamer/check_capture ./check_capture\n!source ./check_capture\n\n-rm-f /ImageStreamerCapture\n\nupload -<<END /ImageStreamer/esxi_mgmt_net\n#! /bin/bash\n\ncat <<\"EOF\" >>local.sh\n# HPE Image Streamer ESXi host configuration\nesxcli system syslog mark --message \"HPE Image Streamer ESXi host configuration for @Hostname1@\"\n\n# Image Streamer management network configuration\nesxcli system hostname set --host \"@Hostname1@\"\nesxcli system hostname set --domain \"@DomainName1@\"\n\nVMK1=vmk2\nUPLINK1=`esxcli network nic list | grep -i \"@ManagementNIC1.mac@\" | awk \'{ print $1 }\'`\n\nesxcli network vswitch standard add --vswitch-name=vSwitch1\n\nesxcli network vswitch standard portgroup add --portgroup-name=ManagementNetwork1 --vswitch-name=vSwitch1\n\nesxcfg-vswitch vSwitch1 -v @ManagementNIC1.vlanid:0@ -p ManagementNetwork1\n\nesxcli network vswitch standard uplink add --uplink-name=$UPLINK1 --vswitch-name=vSwitch1\n\nesxcli network ip interface add --interface-name=$VMK1 --portgroup-name=ManagementNetwork1\n\nEOF\n\nif [[ \"@ManagementNIC1.mac@\" != \"none\" ]]; then\n\nif [[ \"@ManagementNIC1.ipaddress@\" =~ [0-9]*\\.[0-9]*\\.[0-9]*\\.[0-9]* ]]; then\n\necho \"Configure ESXi host management network for static IP\"\ncat <<\"EOF\" >>local.sh\nesxcli network ip interface ipv4 set --interface-name=$VMK1 --ipv4=@ManagementNIC1.ipaddress@ --netmask=@ManagementNIC1.netmask@ --type=static\n\nesxcli network ip route ipv4 add --gateway \"@ManagementNIC1.gateway@\" --network default\nesxcli network ip dns server add --server=@ManagementNIC1.dns1@\nesxcli network ip dns server add --server=@ManagementNIC1.dns2@\n\nEOF\n\nelse\n\necho \"Configure ESXi host management network for DHCP\"\ncat <<\"EOF\" >>local.sh\nesxcli network ip  interface ipv4 set --interface-name=$VMK1 --type=dhcp   \n\nEOF\nfi\n\nelse\necho \"mac address of management nic1 : @ManagementNIC1.mac@\"\n\nfi\n\nexit 0\nEND\n\ndownload /ImageStreamer/esxi_mgmt_net ./esxi_mgmt_net\necho \"Run esxi_mgmt_net\"\n!source ./esxi_mgmt_net\necho \"Configure host management complete\""
}, {
    "type": "PlanScript",
    "description": "Plan script for Set Password",
    "name": "PS_SET_PASSWORD",
    "hpProvided": 'false',
    "planType": "deploy",
    "content": "#Please note that password value should meet password complexity and \n#minimum length requirements defined for ESXi 5.x, ESXi 6.x appropriately. \n\necho \"########################################\"\necho \"Configure host password\"\necho \"########################################\"\n\nupload -<<END /ImageStreamer/esxi_password\n#! /bin/bash\n\ncat <<\"EOF\" >>local.sh\n# Image Streamer password configuration\necho \"@Password@\" | passwd root --stdin\n\nEOF\n\nexit 0\nEND\n\ndownload /ImageStreamer/esxi_password esxi_password\necho \"Run esxi_password\"\n!source ./esxi_password\necho"
}, {
    "type": "PlanScript",
    "description": "Plan script to Configure SSH",
    "name": "PS_CONFIGURE_SSH",
    "hpProvided": 'false',
    "planType": "deploy",
    "content": "echo \"########################################\"\necho \"Configure ssh\"\necho \"########################################\"\n\nupload -<<END /ImageStreamer/esxi_ssh\n#!/bin/bash\nif [ \"@SSH:enabled@\" = \"enabled\" ]; then\ncat <<\"EOF\" >>local.sh\nvim-cmd hostsvc/enable_esx_shell\nvim-cmd hostsvc/start_esx_shell\nvim-cmd hostsvc/enable_ssh\nvim-cmd hostsvc/start_ssh\n\nEOF\nfi\n\nexit 0\nEND\n\ndownload /ImageStreamer/esxi_ssh esxi_ssh\necho \"Run esxi_ssh\"\n!source ./esxi_ssh"
}, {
    "type": "PlanScript",
    "description": 'Re-pack Script',
    "name": "PS_REPACK",
    "hpProvided": "false",
    "planType": "general",
    "content": "echo \"########################################\"\necho \"Pack and replace ESXi host state into ESXi host OS Volume\"\necho \"########################################\"\n\necho \"Run  esxi_repack ESXi host state repack script\"\n!source ./esxi_repack\n\necho \"Copy in state.tgz if present\"\n-upload state.tgz /state.tgz \necho \"Copy in onetime.tgz if present\"\n-upload onetime.tgz /onetime.tgz"
}, {
    "type": "PlanScript",
    "description": "Unmount Script",
    "name": "PS_UNMOUNT",
    "hpProvided": 'false',
    "planType": "general",
    "content": "echo \"########################################\"\necho \"Cleanup and unmount file systems \"\necho \"########################################\"\n\necho \"Remove ImageStreamer temp directory\"\nrm-rf /ImageStreamer\n\necho \"Unmount file systems\"\numount /\necho"
}]


buildplan = {
    'type': 'OeBuildPlanV5',
    "customAttributes": [
            {
                "constraints": "{\"options\":[\"enabled\"]}",
                "description": "",
                "name": "SSH",
                "value": "enabled",
                "type": "option"
            },
        {
                "constraints": "{\"ipv4static\":true,\"ipv4dhcp\":false,\"ipv4disable\":false,\"parameters\":[\"dns1\",\"dns2\",\"gateway\",\"ipaddress\",\"mac\",\"netmask\"]}",
                "description": "",
                "name": "ManagementNIC1",
                "value": "",
                "type": "nic"
            },
        {
                "constraints": "{\"maxlen\":\"15\"}",
                "description": "",
                "name": "Password",
                "value": "Synergy@123",
                "type": "password"
            },
        {
                "constraints": "{\"helpText\":\"\"}",
                "description": "",
                "name": "DomainName1",
                "value": "vse.rdlabs.hpe.com",
                "type": "fqdn"
            },
        {
                "constraints": "{\"helpText\":\"\"}",
                "description": "",
                "name": "Hostname1",
                "value": "CHO-setup",
                "type": "hostname"
            }
    ],
    'buildStep': [{'planScriptUri': 'PS_MOUNT', 'parameters': None, 'serialNumber': '1'},
                  {'planScriptUri': 'PS_UNPACK',
                      'parameters': None, 'serialNumber': '2'},
                  {'planScriptUri': 'PS_SINGLE_NIC_WITH_VLAN',
                      'parameters': None, 'serialNumber': '3'},
                  {'planScriptUri': 'PS_SET_PASSWORD',
                      'parameters': None, 'serialNumber': '4'},
                  {'planScriptUri': 'PS_CONFIGURE_SSH',
                      'parameters': None, 'serialNumber': '5'},
                  {'planScriptUri': 'PS_REPACK',
                      'parameters': None, 'serialNumber': '6'},
                  {'planScriptUri': 'PS_UNMOUNT', 'parameters': None, 'serialNumber': '7'}],
    'hpProvided': False,
    'oeBuildPlanType': 'deploy',
    'description': 'Build plan having custom attributes to set host name, domain name, single NIC, password and to enable SSH',
    'name': 'CHO BP'}


deploymentplan = {
    "type": "OEDeploymentPlanV5",
    "hpProvided": False,
    "customAttributes":  [
            {
                "name": "Hostname1",
                "visible": True,
                "value": "CHO-setup",
                "description": "",
                "type": "hostname",
                "constraints": "{\"helpText\":\"\"}",
                "editable": True,
            },
        {
                "name": "SSH",
                "visible": True,
                "value": "enabled",
                "description": "",
                "type": "option",
                "constraints": "{\"options\":[\"enabled\"]}",
                "editable": True,
        },
        {
                "name": "DomainName1",
                "visible": True,
                "value": "vse.rdlabs.hpe.com",
                "description": "",
                "type": "fqdn",
                "constraints": "{\"helpText\":\"\"}",
                "editable": True,
        },
        {
                "name": "Password",
                "visible": True,
                "value": "**********",
                "description": "",
                "type": "password",
                "constraints": "{\"maxlen\":\"15\"}",
                "editable": True,
        },
        {
                "name": "ManagementNIC1",
                "visible": True,
                "value": "",
                "description": "",
                "type": "nic",
                "constraints": "{\"ipv4static\":true,\"ipv4dhcp\":false,\"ipv4disable\":false,\"parameters\":[\"dns1\",\"dns2\",\"gateway\",\"ipaddress\",\"mac\",\"netmask\",\"vlanid\"]}",
                "editable": True,
        }
    ],
    "goldenImageURI": "CHO GI",
    "oeBuildPlanURI": "CHO BP",
    "category": "oe-deployment-plans",
    "description": "Deployment plan having custom attributes to set host name, domain name, single NIC, password and to enable SSH",
    "name": "CHO DP",
}


deploymentplan_delete = {'name': 'CHO DP'}

buildplan_delelte = {'name': 'CHO BP'}

goldenimage_delete = {'name': 'CHO GI'}

planscript_delete = [{'name': 'PS_MOUNT'},
                     {'name': 'PS_UNPACK'},
                     {'name': 'PS_SINGLE_NIC_WITH_VLAN'},
                     {'name': 'PS_SET_PASSWORD'},
                     {'name': 'PS_CONFIGURE_SSH'},
                     {'name': 'PS_REPACK'},
                     {'name': 'PS_UNMOUNT'}
                     ]


artifactbundle = {
    'name': 'ab_automate_1',
    'description': 'ab with deploymentplan only',
    'deploymentPlans': [
            {
                'resourceUri': 'CHO DP',
                'readOnly': False
            }
    ]
}

artifactbundle_update = {
    'name': 'ab_automate_update',
    'type': 'ArtifactsBundle'
}

artifactbundle_add = {
    'name': 'c:/Goldenimage/ab_download.zip'
}

artifactbundle_extract = {
    'name': 'ab_download'
}


serverprofile_3enc = [
    {'type': 'ServerProfileV8',
     'name': 'CHO-SP1-SGH708YL3C-bay 1',
     'iscsiInitiatorNameType': 'AutoGenerated',
     'serverHardwareUri': 'SGH708YL3C, bay 1',
     'serverHardwareTypeUri': 'SY 480 Gen10 1',
     'enclosureGroupUri': 'EG',
     'enclosureUri': 'SGH708YL3C',
     'affinity': 'Bay',
     'hideUnusedFlexNics': True,
     'firmware': {'firmwareInstallType': None, 'forceInstallFirmware': False, 'manageFirmware': False, 'firmwareBaselineUri': None},
     'macType': 'Virtual',
     'wwnType': 'Virtual',
     'osDeploymentSettings': {'osDeploymentPlanUri': 'CHO DP',
                              'osCustomAttributes': [{'name': "DomainName1", 'value': "hpe.com"},
                                                     {'name': "Hostname1",
                                                      'value': "Host1"},
                                                     {'name': "ManagementNIC1.connectionid",
                                                         'value': "3"},
                                                     {'name': "ManagementNIC1.dhcp",
                                                      'value': "false"},
                                                     {'name': "ManagementNIC1.ipv4disable",
                                                      'value': "false"},
                                                     {'name': "ManagementNIC1.networkuri",
                                                      'value': ['mgmt']},
                                                     {'name': "ManagementNIC1.constraint",
                                                      'value': "auto"},
                                                     {'name': "Password",
                                                         'value': 'Changed@321'},
                                                     {'name': "SSH", 'value': "enabled"}],
                              'osVolumeUri': None},
        "connectionSettings": {
         'connections': [
             {'id': 1, 'name': 'Deployment Network A', 'functionType': 'Ethernet', 'networkUri': ['deploy'],
              'portId':'Mezz 3:1-a', 'requestedVFs':'Auto', 'allocatedVFs':64, 'macType':'Virtual', 'wwpnType':'Virtual', 'mac':'', 'requestedMbps':'2500',
              'allocatedMbps':2500, 'maximumMbps':20000,
              'boot':{'priority': 'Primary', 'ethernetBootType': "iSCSI", 'iscsi': {'initiatorNameSource': 'ProfileInitiatorName'}}
              },

             {'id': 2, 'name': 'Deployment Network B', 'functionType': 'Ethernet', 'networkUri': ['deploy'],
              'portId':'Mezz 3:2-a', 'requestedVFs':'Auto', 'allocatedVFs':64, 'macType':'Virtual', 'wwpnType':'Virtual', 'mac':'', 'requestedMbps':'2500',
              'allocatedMbps':2500, 'maximumMbps':10000,
              'boot':{'priority': 'Secondary', 'ethernetBootType': "iSCSI", 'iscsi': {'initiatorNameSource': 'ProfileInitiatorName'}}
              },

             {'id': 3, 'name': 'Blade_boot_mgmt', 'functionType': 'Ethernet', 'networkUri': ['mgmt'],
              'portId':'Mezz 3:1-c', 'requestedVFs':0, 'allocatedVFs':24, 'macType':'Virtual', 'wwpnType':'Virtual', 'mac':'', 'requestedMbps':'2500',
              'allocatedMbps':2500, 'maximumMbps':10000,
              'boot':{'priority': 'NotBootable', 'iscsi': {}}
              }
         ]
     },
        'bootMode': {'manageMode': True, 'pxeBootPolicy': 'Auto', 'mode': 'UEFIOptimized'},
        'boot': {'manageBoot': True, 'order': []},
        'bios':{'manageBios': False, 'overriddenSettings': []},
        'localStorage':{},
        'sanStorage': {'volumeAttachments': [], 'manageSanStorage':False}
     },



    {'type': 'ServerProfileV8',
     'name': 'CHO-SP2-SGH708YL3C-bay 2',
     'iscsiInitiatorNameType': 'AutoGenerated',
     'serverHardwareUri': 'SGH708YL3C, bay 2',
     'serverHardwareTypeUri': 'SY 480 Gen9 2',
     'enclosureGroupUri': 'EG',
     'enclosureUri': 'SGH708YL3C',
     'affinity': 'Bay',
     'hideUnusedFlexNics': True,
     'firmware': {'firmwareInstallType': None, 'forceInstallFirmware': False, 'manageFirmware': False, 'firmwareBaselineUri': None},
     'macType': 'Virtual',
     'wwnType': 'Virtual',
     'osDeploymentSettings': {'osDeploymentPlanUri': 'CHO DP',
                              'osCustomAttributes': [{'name': "DomainName1", 'value': "hpe.com"},
                                                     {'name': "Hostname1",
                                                      'value': "Host3"},
                                                     {'name': "ManagementNIC1.connectionid",
                                                         'value': "3"},
                                                     {'name': "ManagementNIC1.dhcp",
                                                      'value': "false"},
                                                     {'name': "ManagementNIC1.ipv4disable",
                                                      'value': "false"},
                                                     {'name': "ManagementNIC1.networkuri",
                                                      'value': ['mgmt']},
                                                     {'name': "ManagementNIC1.constraint",
                                                      'value': "auto"},
                                                     {'name': "Password",
                                                         'value': 'Changed@321'},
                                                     {'name': "SSH", 'value': "enabled"}],
                              'osVolumeUri': None},
        "connectionSettings": {
         'connections': [
             {'id': 1, 'name': 'Deployment Network A', 'functionType': 'Ethernet', 'networkUri': ['deploy'],
              'portId':'Mezz 3:1-a', 'requestedVFs':'Auto', 'allocatedVFs':64, 'macType':'Virtual', 'wwpnType':'Virtual', 'mac':'', 'requestedMbps':'2500',
              'allocatedMbps':2500, 'maximumMbps':20000,
              'boot':{'priority': 'Primary', 'ethernetBootType': "iSCSI", 'iscsi': {'initiatorNameSource': 'ProfileInitiatorName'}}
              },

             {'id': 2, 'name': 'Deployment Network B', 'functionType': 'Ethernet', 'networkUri': ['deploy'],
              'portId':'Mezz 3:2-a', 'requestedVFs':'Auto', 'allocatedVFs':64, 'macType':'Virtual', 'wwpnType':'Virtual', 'mac':'', 'requestedMbps':'2500',
              'allocatedMbps':2500, 'maximumMbps':10000,
              'boot':{'priority': 'Secondary', 'ethernetBootType': "iSCSI", 'iscsi': {'initiatorNameSource': 'ProfileInitiatorName'}}
              },

             {'id': 3, 'name': 'Blade_boot_mgmt', 'functionType': 'Ethernet', 'networkUri': ['mgmt'],
              'portId':'Mezz 3:1-c', 'requestedVFs':0, 'allocatedVFs':24, 'macType':'Virtual', 'wwpnType':'Virtual', 'mac':'', 'requestedMbps':'2500',
              'allocatedMbps':2500, 'maximumMbps':10000,
              'boot':{'priority': 'NotBootable', 'iscsi': {}}
              }
         ]
     },
        'bootMode': {'manageMode': True, 'pxeBootPolicy': 'Auto', 'mode': 'UEFIOptimized'},
        'boot': {'manageBoot': True, 'order': []},
        'bios':{'manageBios': False, 'overriddenSettings': []},
        'localStorage':{},
        'sanStorage': {'volumeAttachments': [], 'manageSanStorage':False}
     },

    {'type': 'ServerProfileV8',
     'name': 'CHO-SP3-SGH708YL3F-bay 4',
     'iscsiInitiatorNameType': 'AutoGenerated',
     'serverHardwareUri': 'SGH708YL3F, bay 4',
     'serverHardwareTypeUri': 'SY 480 Gen10 2',
     'enclosureGroupUri': 'EG',
     'enclosureUri': 'SGH708YL3F',
     'affinity': 'Bay',
     'hideUnusedFlexNics': True,
     'firmware': {'firmwareInstallType': None, 'forceInstallFirmware': False, 'manageFirmware': False, 'firmwareBaselineUri': None},
     'macType': 'Virtual',
     'wwnType': 'Virtual',
     'osDeploymentSettings': {'osDeploymentPlanUri': 'CHO DP',
                              'osCustomAttributes': [{'name': "DomainName1", 'value': "hpe.com"},
                                                     {'name': "Hostname1",
                                                      'value': "Host4"},
                                                     {'name': "ManagementNIC1.connectionid",
                                                         'value': "3"},
                                                     {'name': "ManagementNIC1.dhcp",
                                                      'value': "false"},
                                                     {'name': "ManagementNIC1.ipv4disable",
                                                      'value': "false"},
                                                     {'name': "ManagementNIC1.networkuri",
                                                      'value': ['mgmt']},
                                                     {'name': "ManagementNIC1.constraint",
                                                      'value': "auto"},
                                                     {'name': "Password",
                                                         'value': 'Changed@321'},
                                                     {'name': "SSH", 'value': "enabled"}],
                              'osVolumeUri': None},
        "connectionSettings": {
         'connections': [
             {'id': 1, 'name': 'Deployment Network A', 'functionType': 'Ethernet', 'networkUri': ['deploy'],
              'portId':'Mezz 3:1-a', 'requestedVFs':'Auto', 'allocatedVFs':64, 'macType':'Virtual', 'wwpnType':'Virtual', 'mac':'', 'requestedMbps':'2500',
              'allocatedMbps':2500, 'maximumMbps':20000,
              'boot':{'priority': 'Primary', 'ethernetBootType': "iSCSI", 'iscsi': {'initiatorNameSource': 'ProfileInitiatorName'}}
              },

             {'id': 2, 'name': 'Deployment Network B', 'functionType': 'Ethernet', 'networkUri': ['deploy'],
              'portId':'Mezz 3:2-a', 'requestedVFs':'Auto', 'allocatedVFs':64, 'macType':'Virtual', 'wwpnType':'Virtual', 'mac':'', 'requestedMbps':'2500',
              'allocatedMbps':2500, 'maximumMbps':10000,
              'boot':{'priority': 'Secondary', 'ethernetBootType': "iSCSI", 'iscsi': {'initiatorNameSource': 'ProfileInitiatorName'}}
              },

             {'id': 3, 'name': 'Blade_boot_mgmt', 'functionType': 'Ethernet', 'networkUri': ['mgmt'],
              'portId':'Mezz 3:1-c', 'requestedVFs':0, 'allocatedVFs':24, 'macType':'Virtual', 'wwpnType':'Virtual', 'mac':'', 'requestedMbps':'2500',
              'allocatedMbps':2500, 'maximumMbps':10000,
              'boot':{'priority': 'NotBootable', 'iscsi': {}}
              }
         ]
     },
        'bootMode': {'manageMode': True, 'pxeBootPolicy': 'Auto', 'mode': 'UEFIOptimized'},
        'boot': {'manageBoot': True, 'order': []},
        'bios':{'manageBios': False, 'overriddenSettings': []},
        'localStorage':{},
        'sanStorage': {'volumeAttachments': [], 'manageSanStorage':False}
     },

    {'type': 'ServerProfileV8',
     'name': 'CHO-SP4-SGH708YL3H-bay 4',
     'iscsiInitiatorNameType': 'AutoGenerated',
     'serverHardwareUri': 'SGH708YL3H, bay 4',
     'serverHardwareTypeUri': 'SY 480 Gen9 1',
     'enclosureGroupUri': 'EG',
     'enclosureUri': 'SGH708YL3H',
     'affinity': 'Bay',
     'hideUnusedFlexNics': True,
     'firmware': {'firmwareInstallType': None, 'forceInstallFirmware': False, 'manageFirmware': False, 'firmwareBaselineUri': None},
     'macType': 'Virtual',
     'wwnType': 'Virtual',
     'osDeploymentSettings': {'osDeploymentPlanUri': 'CHO DP',
                              'osCustomAttributes': [{'name': "DomainName1", 'value': "hpe.com"},
                                                     {'name': "Hostname1",
                                                      'value': "Host5"},
                                                     {'name': "ManagementNIC1.connectionid",
                                                         'value': "3"},
                                                     {'name': "ManagementNIC1.dhcp",
                                                      'value': "false"},
                                                     {'name': "ManagementNIC1.ipv4disable",
                                                      'value': "false"},
                                                     {'name': "ManagementNIC1.networkuri",
                                                      'value': ['mgmt']},
                                                     {'name': "ManagementNIC1.constraint",
                                                      'value': "auto"},
                                                     {'name': "Password",
                                                         'value': 'Changed@321'},
                                                     {'name': "SSH", 'value': "enabled"}],
                              'osVolumeUri': None},
        "connectionSettings": {
         'connections': [
             {'id': 1, 'name': 'Deployment Network A', 'functionType': 'Ethernet', 'networkUri': ['deploy'],
              'portId':'Mezz 3:1-a', 'requestedVFs':'Auto', 'allocatedVFs':64, 'macType':'Virtual', 'wwpnType':'Virtual', 'mac':'', 'requestedMbps':'2500',
              'allocatedMbps':2500, 'maximumMbps':20000,
              'boot':{'priority': 'Primary', 'ethernetBootType': "iSCSI", 'iscsi': {'initiatorNameSource': 'ProfileInitiatorName'}}
              },

             {'id': 2, 'name': 'Deployment Network B', 'functionType': 'Ethernet', 'networkUri': ['deploy'],
              'portId':'Mezz 3:2-a', 'requestedVFs':'Auto', 'allocatedVFs':64, 'macType':'Virtual', 'wwpnType':'Virtual', 'mac':'', 'requestedMbps':'2500',
              'allocatedMbps':2500, 'maximumMbps':10000,
              'boot':{'priority': 'Secondary', 'ethernetBootType': "iSCSI", 'iscsi': {'initiatorNameSource': 'ProfileInitiatorName'}}
              },

             {'id': 3, 'name': 'Blade_boot_mgmt', 'functionType': 'Ethernet', 'networkUri': ['mgmt'],
              'portId':'Mezz 3:1-c', 'requestedVFs':0, 'allocatedVFs':24, 'macType':'Virtual', 'wwpnType':'Virtual', 'mac':'', 'requestedMbps':'2500',
              'allocatedMbps':2500, 'maximumMbps':10000,
              'boot':{'priority': 'NotBootable', 'iscsi': {}}
              }
         ]
     },
        'bootMode': {'manageMode': True, 'pxeBootPolicy': 'Auto', 'mode': 'UEFIOptimized'},
        'boot': {'manageBoot': True, 'order': []},
        'bios':{'manageBios': False, 'overriddenSettings': []},
        'localStorage':{},
        'sanStorage': {'volumeAttachments': [], 'manageSanStorage':False}
     }]


BLADES = [{'Blade1': '00HPMP13F8, bay 1'}, {'Blade2': '00HPMP13F8, bay 8'}, {
    'Blade3': '0AXRH8G10J, bay 9'}, {'Blade4': '935OZCVY40, bay 5'}]

#from winnt import NULL
#from requests.api import patch

admin_credentials = {
    'userName': 'Administrator',
    'password': 'admin123'
}

serverHardwareUri  = ["CN7545061G, bay 5",
                      "CN7545061G, bay 6"]
serverHardwareTypeUri ="SY 480 Gen9 1"
enclosureGroupUri= "EG"
enclosureUri =["CN7545061G","CN7545061G"]
networkUri_iscsi = "deploy"
networkUri_mgmt = "mgmt"


goldenimage = [{'name': 'ESXi_6.5',
                    'description': 'Golden Image for ESXi 6.5',
                    'file': "valid_file"},
               {'name': 'ESXi_6.5 (1)',
                    'description': 'Golden Image for ESXi 6.5',
                    'file': "valid_file",
                    "readOnly": "true"}
                   ]

goldenimage_update = [{'name': 'Updated ESXi_6.5',
                       'description': 'Updated ESXi_6.5',
                        'type': 'GoldenImage'},
                    {'name': 'Updated-1 ESXi_6.5',
                     'description': 'Updated-1 ESXi_6.5',
                     'type': 'GoldenImage'},
                      {'name': 'Updated-2 ESXi_6.5',
                       'description': 'Updated-2 ESXi_6.5',
                       'type': 'GoldenImage'}
                      ]

artifactbundle = [{'name': 'AB for GI-yes',
                   'description': 'GI With Read only Yes',
                   'goldenImages': [{'resourceUri': 'ESXi_6.5',
                                     'readOnly': True}]}]

planscript = [ {
    "type": "PlanScript",
    "description": "Planscript having multiple CA",
    "name": "PS1-Multi-CA-Read only No",
    "hpProvided": 'false',
    "planType": "deploy",
    "content": "# (C) Copyright 2015-2015 Hewlett-Packard Development Company, L.P.\n# Script to mount disk in libguesfs virtual appliance for personalizaiton or generalization\nmount /dev/sda5 /\n\n\n# creating tmp dir at local filesystem\n!mkdir -p ./onetime\n!mkdir -p ./state/local\n\n# copying required files for personalization/generalization to local filesysystem\n-copy-out /onetime.tgz .\n-copy-out /state.tgz .\n-copy-out /boot.cfg .\n\n# trying to findout whether onetime.tgz will be picked up during booting or state.tgz will be picked\n# based on that we can process either onetime.tgz or state.tgz for personalization/generalization\n\n-!grep \"onetime.tgz\"  ./boot.cfg >./onetime_found\n-!grep \"state.tgz\" ./boot.cfg > ./state_found\n\n\n# (C) Copyright 2015-2015 Hewlett-Packard Development Company, L.P.\n# Script to PERSONALIZE\n\n!if [ -s  \"state_found\" ]; \\\nthen \\\ncd state; \\\ntar xvpzf ../state.tgz; \\\ncd local; \\\ntar xvpzf ../local.tgz; \\\nmkdir -p etc/rc.local.d; \\\necho esxcli system hostname set -H \"@hostname:Bay8@\">>   etc/rc.local.d/local.sh; \\\necho esxcli system hostname set -d \"@DomainName:Linuxhost@\">>  etc/rc.local.d/local.sh; \\\necho esxcli system settings keyboard layout set -l \"@KeyboardLayout:English@\">>  etc/rc.local.d/local.sh; \\\nchmod 777  etc/rc.local.d/local.sh; \\\ntar cvpzf ../local.tgz *; \\\ncd ../; \\\ntar cvpzf ../state.tgz local.tgz; \\\ntouch  ../state.tgz; \\\nelse \\\ncd  onetime; \\\ntar xvpzf ../onetime.tgz; \\\necho esxcli system hostname set -H \"@hostname:Bay8@\">>   etc/rc.local.d/local.sh; \\\necho esxcli system hostname set -d \"@DomainName:Linuxhost@\">>  etc/rc.local.d/local.sh; \\\necho esxcli system settings keyboard layout set -l \"@KeyboardLayout:English@\">>  etc/rc.local.d/local.sh; \\\nchmod 777   etc/rc.local.d/local.sh; \\\ntar cvpzf ../onetime.tgz *; \\\nfi\n\n\n\n# (C) Copyright 2015-2015 Hewlett-Packard Development Company, L.P.\n# Script to Unmount\n\n-copy-in onetime.tgz /\n-copy-in state.tgz /\numount /"
}, {
    "type": "PlanScript",
    "description": "Planscript having single CA",
    "name": "PS1-Single-CA-Read only No",
    "hpProvided": 'false',
    "planType": "deploy",
    "content": "# (C) Copyright 2015-2015 Hewlett-Packard Development Company, L.P.\n# Script to PERSONALIZE\n\n!if [ -s  \"state_found\" ]; \\\nthen \\\ncd state; \\\ntar xvpzf ../state.tgz; \\\ncd local; \\\ntar xvpzf ../local.tgz; \\\nmkdir -p etc/rc.local.d; \\\necho esxcli system hostname set -H \"@hostname:Bay8@\">>   etc/rc.local.d/local.sh; \\\nchmod 777  etc/rc.local.d/local.sh; \\\ntar cvpzf ../local.tgz *; \\\ncd ../; \\\ntar cvpzf ../state.tgz local.tgz; \\\ntouch  ../state.tgz; \\\nelse \\\ncd  onetime; \\\ntar xvpzf ../onetime.tgz; \\\necho esxcli system hostname set -H \"@hostname:Bay8@\">>   etc/rc.local.d/local.sh; \\\nchmod 777   etc/rc.local.d/local.sh; \\\ntar cvpzf ../onetime.tgz *; \\\nfi"
},
    {
    "type": "PlanScript",
    "description": "Planscript having multiple CA",
    "name": "PS-Multi-CA-Read only Yes",
    "hpProvided": 'true',
    "planType": "deploy",
    "content": "# (C) Copyright 2015-2015 Hewlett-Packard Development Company, L.P.\n# Script to mount disk in libguesfs virtual appliance for personalizaiton or generalization\nmount /dev/sda5 /\n\n\n# creating tmp dir at local filesystem\n!mkdir -p ./onetime\n!mkdir -p ./state/local\n\n# copying required files for personalization/generalization to local filesysystem\n-copy-out /onetime.tgz .\n-copy-out /state.tgz .\n-copy-out /boot.cfg .\n\n# trying to findout whether onetime.tgz will be picked up during booting or state.tgz will be picked\n# based on that we can process either onetime.tgz or state.tgz for personalization/generalization\n\n-!grep \"onetime.tgz\"  ./boot.cfg >./onetime_found\n-!grep \"state.tgz\" ./boot.cfg > ./state_found\n\n\n# (C) Copyright 2015-2015 Hewlett-Packard Development Company, L.P.\n# Script to PERSONALIZE\n\n!if [ -s  \"state_found\" ]; \\\nthen \\\ncd state; \\\ntar xvpzf ../state.tgz; \\\ncd local; \\\ntar xvpzf ../local.tgz; \\\nmkdir -p etc/rc.local.d; \\\necho esxcli system hostname set -H \"@hostname:Bay8@\">>   etc/rc.local.d/local.sh; \\\necho esxcli system hostname set -d \"@DomainName:Linuxhost@\">>  etc/rc.local.d/local.sh; \\\necho esxcli system settings keyboard layout set -l \"@KeyboardLayout:English@\">>  etc/rc.local.d/local.sh; \\\nchmod 777  etc/rc.local.d/local.sh; \\\ntar cvpzf ../local.tgz *; \\\ncd ../; \\\ntar cvpzf ../state.tgz local.tgz; \\\ntouch  ../state.tgz; \\\nelse \\\ncd  onetime; \\\ntar xvpzf ../onetime.tgz; \\\necho esxcli system hostname set -H \"@hostname:Bay8@\">>   etc/rc.local.d/local.sh; \\\necho esxcli system hostname set -d \"@DomainName:Linuxhost@\">>  etc/rc.local.d/local.sh; \\\necho esxcli system settings keyboard layout set -l \"@KeyboardLayout:English@\">>  etc/rc.local.d/local.sh; \\\nchmod 777   etc/rc.local.d/local.sh; \\\ntar cvpzf ../onetime.tgz *; \\\nfi\n\n\n\n# (C) Copyright 2015-2015 Hewlett-Packard Development Company, L.P.\n# Script to Unmount\n\n-copy-in onetime.tgz /\n-copy-in state.tgz /\numount /"
}, {
    "type": "PlanScript",
    "description": "Planscript having single CA",
    "name": "PS-Single-CA-Read only Yes",
    "hpProvided": 'true',
    "planType": "deploy",
    "content": "# (C) Copyright 2015-2015 Hewlett-Packard Development Company, L.P.\n# Script to PERSONALIZE\n\n!if [ -s  \"state_found\" ]; \\\nthen \\\ncd state; \\\ntar xvpzf ../state.tgz; \\\ncd local; \\\ntar xvpzf ../local.tgz; \\\nmkdir -p etc/rc.local.d; \\\necho esxcli system hostname set -H \"@hostname:Bay8@\">>   etc/rc.local.d/local.sh; \\\nchmod 777  etc/rc.local.d/local.sh; \\\ntar cvpzf ../local.tgz *; \\\ncd ../; \\\ntar cvpzf ../state.tgz local.tgz; \\\ntouch  ../state.tgz; \\\nelse \\\ncd  onetime; \\\ntar xvpzf ../onetime.tgz; \\\necho esxcli system hostname set -H \"@hostname:Bay8@\">>   etc/rc.local.d/local.sh; \\\nchmod 777   etc/rc.local.d/local.sh; \\\ntar cvpzf ../onetime.tgz *; \\\nfi"
}, {
    "type": "PlanScript",
    "description": "Planscript having multiple CA",
    "name": "Inuse Planscript in BP",
    "hpProvided": 'false',
    "planType": "deploy",
    "content": "@Password@\n@Hostname@\n@NIC.ipaddress@\n@NIC.mac@\n#Added new comments\nAdded"
}
]

planscript_update = [{
    "type": "PlanScript",
    "description": "Planscript having multiple CA",
    "name": "Updated-PS1-Multi-CA",
    "hpProvided": 'false',
    "planType": "deploy",
    "content": "# (C) Copyright 2015-2015 Hewlett-Packard Development Company, L.P.\n# Script to mount disk in libguesfs virtual appliance for personalizaiton or generalization\nmount /dev/sda5 /\n\n\n# creating tmp dir at local filesystem\n!mkdir -p ./onetime\n!mkdir -p ./state/local\n\n# copying required files for personalization/generalization to local filesysystem\n-copy-out /onetime.tgz .\n-copy-out /state.tgz .\n-copy-out /boot.cfg .\n\n# trying to findout whether onetime.tgz will be picked up during booting or state.tgz will be picked\n# based on that we can process either onetime.tgz or state.tgz for personalization/generalization\n\n-!grep \"onetime.tgz\"  ./boot.cfg >./onetime_found\n-!grep \"state.tgz\" ./boot.cfg > ./state_found\n\n\n# (C) Copyright 2015-2015 Hewlett-Packard Development Company, L.P.\n# Script to PERSONALIZE\n\n!if [ -s  \"state_found\" ]; \\\nthen \\\ncd state; \\\ntar xvpzf ../state.tgz; \\\ncd local; \\\ntar xvpzf ../local.tgz; \\\nmkdir -p etc/rc.local.d; \\\necho esxcli system hostname set -H \"@hostname:Bay8@\">>   etc/rc.local.d/local.sh; \\\necho esxcli system hostname set -d \"@DomainName:Linuxhost@\">>  etc/rc.local.d/local.sh; \\\necho esxcli system settings keyboard layout set -l \"@KeyboardLayout:English@\">>  etc/rc.local.d/local.sh; \\\nchmod 777  etc/rc.local.d/local.sh; \\\ntar cvpzf ../local.tgz *; \\\ncd ../; \\\ntar cvpzf ../state.tgz local.tgz; \\\ntouch  ../state.tgz; \\\nelse \\\ncd  onetime; \\\ntar xvpzf ../onetime.tgz; \\\necho esxcli system hostname set -H \"@hostname:Bay8@\">>   etc/rc.local.d/local.sh; \\\necho esxcli system hostname set -d \"@DomainName:Linuxhost@\">>  etc/rc.local.d/local.sh; \\\necho esxcli system settings keyboard layout set -l \"@KeyboardLayout:English@\">>  etc/rc.local.d/local.sh; \\\nchmod 777   etc/rc.local.d/local.sh; \\\ntar cvpzf ../onetime.tgz *; \\\nfi\n\n\n\n# (C) Copyright 2015-2015 Hewlett-Packard Development Company, L.P.\n# Script to Unmount\n\n-copy-in onetime.tgz /\n-copy-in state.tgz /\numount /"
}, {
    "type": "PlanScript",
    "description": "Planscript having single CA",
    "name": "Updated-PS1-Single-CA",
    "hpProvided": 'false',
    "planType": "deploy",
    "content": "# (C) Copyright 2015-2015 Hewlett-Packard Development Company, L.P.\n# Script to PERSONALIZE\n\n!if [ -s  \"state_found\" ]; \\\nthen \\\ncd state; \\\ntar xvpzf ../state.tgz; \\\ncd local; \\\ntar xvpzf ../local.tgz; \\\nmkdir -p etc/rc.local.d; \\\necho esxcli system hostname set -H \"@hostname:Bay8@\">>   etc/rc.local.d/local.sh; \\\nchmod 777  etc/rc.local.d/local.sh; \\\ntar cvpzf ../local.tgz *; \\\ncd ../; \\\ntar cvpzf ../state.tgz local.tgz; \\\ntouch  ../state.tgz; \\\nelse \\\ncd  onetime; \\\ntar xvpzf ../onetime.tgz; \\\necho esxcli system hostname set -H \"@hostname:Bay8@\">>   etc/rc.local.d/local.sh; \\\nchmod 777   etc/rc.local.d/local.sh; \\\ntar cvpzf ../onetime.tgz *; \\\nfi"
}, {
    "type": "PlanScript",
    "description": "PS content is changed",
    "name": "PS content changed",
    "hpProvided": 'false',
    "planType": "deploy",
    "content": "@Password@\n@Hostname@\n@NIC.ipaddress@\n@NIC.mac@\n#Added new comments\nChanging the script"
}, {
    "type": "PlanScript",
    "description": "PS content is changed",
    "name": "PS content changed",
    "hpProvided": 'false',
    "planType": "deploy",
    "content": "@Password:hpvse1@\n@Hostname:Linuxhost@\n@NIC.ipaddress@\n@NIC.mac@\n#Added new comments\nChanging the script"
}, {
    "type": "PlanScript",
    "description": "PS content is changed",
    "name": "PS content changed",
    "hpProvided": 'false',
    "planType": "deploy",
    "content": "@Password:hpvse1@\n@Hostname:Linuxhost@\n@String@\n@NIC.ipaddress@\n@NIC.mac@\n#Added new comments\nChanging the script" #  @String@ CA is added
}, {
    "type": "PlanScript",
    "description": "PS content is changed",
    "name": "PS content changed",
    "hpProvided": 'false',
    "planType": "deploy",
    "content": "@Password:hpvse1@\n@Password:Compaq123@\n@Hostname:Linuxhost@\n@String@\n@NIC.ipaddress@\n@NIC.mac@\n#Added new comments\nChanging the script"
}, {
    "type": "PlanScript",
    "description": "PS content is changed",
    "name": "PS content changed",
    "hpProvided": 'false',
    "planType": "deploy",
    "content": "@Password:hpvse1@\n@Password@\n@Hostname:Linuxhost@\n@String@\n@NIC.ipaddress@\n@NIC.mac@\n#Added new comments\nChanging the script"
}, {
    "type": "PlanScript",
    "description": "PS content is changed",
    "name": "PS content changed",
    "hpProvided": 'false',
    "planType": "deploy",
    "content": "@Password:hpvse1@\n@Number:24@\n@Hostname:Linuxhost@\n@String@\n@NIC.ipaddress@\n@NIC.mac@\n#Added new comments\nChanging the script"
}, {
    "type": "PlanScript",
    "description": "PS content is changed",
    "name": "PS content changed",
    "hpProvided": 'false',
    "planType": "deploy",
    "content": "@Number:24@\n@Hostname:Linuxhost@\n@String@\n@NIC.ipaddress@\n@NIC.mac@\n#Added new comments\nChanging the script" # @Password@ CA is deleted
}, {
    "type": "PlanScript",
    "description": "PS content is changed",
    "name": "PS content changed",
    "hpProvided": 'false',
    "planType": "deploy",
    "content": "@Number:24@\n@Hostname:Linuxhost@\n@String@\n@NIC.ipaddress@\n@NIC.gateway@\n@NIC.mac@\n#Added new comments\nChanging the script"
}, {
    "type": "PlanScript",
    "description": "PS content is changed",
    "name": "PS content changed",
    "hpProvided": 'false',
    "planType": "deploy",
    "content": "@Number:24@\n@Hostname:Linuxhost@\n@String@\n@NIC.ipaddress\n@NIC.dns1@\n@NIC.mac@\n#Added new comments\nChanging the script"
}, {
    "type": "PlanScript",
    "description": "PS content is changed",
    "name": "PS content changed",
    "hpProvided": 'false',
    "planType": "deploy",
    "content": "@Number:24@\n@Hostname:Linuxhost@\n@String@\n@NIC.ipv6address\n@NIC.dns1@\n@NIC.mac@\n#Added new comments\nChanging the script"
}, {
    "type": "PlanScript",
    "description": "PS content is changed",
    "name": "PS content changed",
    "hpProvided": 'false',
    "planType": "deploy",
    "content": "@Number:24@\n@Hostname:Linuxhost@\n@String@\n@NIC.ipaddress:15.154.101.22\n@NIC.dns1@\n@NIC.mac@\n#Added new comments\nChanging the script"
}, {
    "type": "PlanScript",
    "description": "PS content is changed",
    "name": "PS content changed",
    "hpProvided": 'false',
    "planType": "deploy",
    "content": "@Number:25@\n@Hostname:Linuxhost@\n@String@\n@NIC.ipaddress:15.154.101.22\n@NIC.dns1@\n@NIC.mac@\n#Added new comments\nChanging the script"
}, {
    "type": "PlanScript",
    "description": "PS content is changed",
    "name": "PS content changed",
    "hpProvided": 'false',
    "planType": "deploy",
    "content": "@Number:25@\n@Hostname:Linuxhost@\n@String@\n@NIC.ipaddress:15.154.101.22\n@NIC.dns1@\n#Added new comments\nChanging the script"  # @NIC.mac@ is deleted
}, {
    "type": "PlanScript",
    "description": "PS description is changed",
    "name": "PS name changed",
    "hpProvided": 'false',
    "planType": "deploy",
    "content": "@Number:25@\n@Hostname:Linuxhost@\n@String@\n@NIC.ipaddress:15.154.101.22\n@NIC.dns1@\n#Added new comments\nChanging the script"
}, {
    "type": "PlanScript",
    "description": "PS content is changed",
    "name": "PS content changed",
    "hpProvided": False,
    "planType": "capture",
    "content": "@Number:25@\n@Hostname:Linuxhost@\n@String@\n@NIC.ipaddress:15.154.101.22\n@NIC.dns1@\n#Added new comments\nChanging the script"
}, {
    "type": "PlanScript",
    "description": "Edit in-use PS",
    "name": "Edited In-use PS ",
    "hpProvided": False,
    "planType": "deploy",
    "content": "@Number:25@\n@Hostname:Linuxhost@\n@String@\n@NIC.ipaddress:15.154.101.22\n@NIC.dns1@\n#Added new comments\nChanging the script"

}
]



buildplan = [{
    "type": "OeBuildPlanV5",
    "customAttributes": [
        {
            "constraints": "{}",
            "description": "desciption",
            "name": "KeyboardLayout",
            "value": "English",
            "type": "string"
        },
        {
            "constraints": "{}",
            "description": "desciption",
            "name": "hostname",
            "value": "Bay8",
            "type": "string"
        },
        {
            "constraints": "{}",
            "description": "desciption",
            "name": "DomainName",
            "value": "vse.rdlabs.hpecorp.net",
            "type": "string"
        }
    ],
    "buildStep": [
        {
            "planScriptUri": "PS1-Multi-CA-Read only No",
            "serialNumber": "1"
        }
    ],
    "hpProvided": False,
    "oeBuildPlanType": "deploy",
    "description": "BP1-Single-buildStep-Multi-CA",
    "category": "oe-build-plans",
    "name": "BP1-Single-buildStep-Multi-CA-Read only No"
},
{
    "type": "OeBuildPlanV5",
    "customAttributes": [
        {
            "constraints": "{}",
            "description": "desciption",
            "name": "hostname",
            "value": "Bay8",
            "type": "string"
        }
    ],
    "buildStep": [
        {
            "planScriptUri": "PS1-Single-CA-Read only No",
            "serialNumber": "1"
        }
    ],
    "hpProvided": False,
    "oeBuildPlanType": "deploy",
    "description": "BP-Single-buildStep-Single-CA",
    "category": "oe-build-plans",
    "name": "BP1-Single-buildStep-Single-CA-Read only No"
}, {
    "type": "OeBuildPlanV5",
    "customAttributes": [
        {
            "constraints": "{}",
            "description": "desciption",
            "name": "KeyboardLayout",
            "value": "English",
            "type": "string"
        },
        {
            "constraints": "{}",
            "description": "desciption",
            "name": "hostname",
            "value": "Bay8",
            "type": "string"
        },
        {
            "constraints": "{}",
            "description": "desciption",
            "name": "DomainName",
            "value": "vse.rdlabs.hpecorp.net",
            "type": "string"
        }
    ],
    "buildStep": [
        {
            "planScriptUri": "PS-Multi-CA-Read only Yes",
            "serialNumber": "1"
        }
    ],
    "hpProvided": "true",
    "oeBuildPlanType": "deploy",
    "description": "BP-Single-buildStep-Multi-CA",
    "category": "oe-build-plans",
    "name": "BP-Single-buildStep-Multi-CA-Read only Yes"
}, {
    "type": "OeBuildPlanV5",
    "customAttributes": [
        {
            "constraints": "{}",
            "description": "desciption",
            "name": "hostname",
            "value": "Bay8",
            "type": "string"
        }
    ],
    "buildStep": [
        {
            "planScriptUri": "PS-Single-CA-Read only Yes",
            "serialNumber": "1"
        }
    ],
    "hpProvided": "true",
    "oeBuildPlanType": "deploy",
    "description": "BP-Single-buildStep-Single-CA",
    "category": "oe-build-plans",
    "name": "BP-Single-buildStep-Single-CA-Read only Yes"
}, {
    "type": "OeBuildPlanV5",
    "customAttributes": [
        {
            "name": "Hostname",
            "description": "",
            "value": "",
            "constraints": "{}",
            "type": "string"
        },
        {
            "name": "NIC",
            "description": "",
            "value": "",
            "constraints": "{\"ipv4static\":true,\"ipv4dhcp\":false,\"ipv4disable\":false,\"parameters\":[\"ipaddress\",\"mac\"]}",
            "type": "nic"
        },
        {
            "name": "Password",
            "description": "",
            "value": "",
            "constraints": "{}",
            "type": "string"
        }
    ],
    "buildStep": [
        {
            "planScriptUri": "Inuse Planscript in BP",
            "serialNumber": "1"
        }
    ],
    "hpProvided": False,
    "oeBuildPlanType": "deploy",
    "description": "Inuse BP",
    "category": "oe-build-plans",
    "name": "Inuse BP"
}
]


buildplan_update = [{
    "type": "OeBuildPlanV5",
    "customAttributes": [
        {
            "constraints": "{}",
            "description": "desciption",
            "name": "KeyboardLayout",
            "value": "English",
            "type": "string"
        },
        {
            "constraints": "{}",
            "description": "desciption",
            "name": "hostname",
            "value": "",
            "type": "string"
        },
        {
            "constraints": "{}",
            "description": "desciption",
            "name": "DomainName",
            "value": "vse.rdlabs.hpecorp.net",
            "type": "string"
        }
    ],
    "buildStep": [
        {
            "planScriptUri": "PS1-Multi-CA-Read only No",
            "serialNumber": "1"
        }
    ],
    "hpProvided": False,
    "oeBuildPlanType": "deploy",
    "description": "Updated Description BP1-Single-buildStep-Multi-CA",
    "category": "oe-build-plans",
    "name": "Updated BP1-Single-buildStep-Multi-CA"
}, {
    "type": "OeBuildPlanV5",
    "customAttributes": [
        {
            "constraints": "{}",
            "description": "desciption",
            "name": "hostname",
            "value": ":Linuxhost",
            "type": "string"
        }
    ],
    "buildStep": [
        {
            "planScriptUri": "Updated-PS1-Single-CA",
            "serialNumber": "1"
        }
    ],
    "hpProvided": False,
    "oeBuildPlanType": "deploy",
    "description": "Updated BP1-Single-buildStep-Single-CA",
    "category": "oe-build-plans",
    "name": "Updated BP1-Single-buildStep-Single-CA"
}]

deploymentplan = [{  # 1 Valid DP having Multiple CA
    "type": "OEDeploymentPlanV5",
    "hpProvided": False,
    "customAttributes": [{
        "visible": False,
        "constraints": "{}",
        "editable": True,
        "description": "desc domain name",
        "name": "DomainName",
        "value": "domain.net",
        "type": "string"
    },{
        "visible": False,
        "constraints": "{}",
        "editable": True,
        "description": "desc host name",
        "name": "hostname",
        "value": "myhost",
        "type": "string"
    },{
        "visible": True,
        "constraints": "{}",
        "editable": True,
        "description": "desc keyboard layout type",
        "name": "KeyboardLayout",
        "value": "English",
        "type": "string"
    }],
    "goldenImageURI": "ESXi_6.5",
    "oeBuildPlanURI": "BP1-Single-buildStep-Multi-CA-Read only No",
    "category": "oe-deployment-plans",
    "description": "Deployment Plan with all the valid fields and having multiple custom attributes",
    "name": "Valid DP1 with Multiple CA-Read only No"
},{# 2 Valid DP having single CA
    "type": "OEDeploymentPlanV5",
    "hpProvided": False,
    "customAttributes": [{
        "visible": False,
        "constraints": "{}",
        "editable": True,
        "description": "desc host name",
        "name": "hostname",
        "value": "myhost",
        "type": "string"
    }],
    "goldenImageURI": "ESXi_6.5",
    "oeBuildPlanURI": "BP1-Single-buildStep-Single-CA-Read only No",
    "category": "oe-deployment-plans",
    "description": "Deployment Plan with all the valid fields and having only one custom attribute",
    "name": "Valid DP1 with Single CA-Read only No"
},
{  # 1 Valid DP having Multiple CA
    "type": "OEDeploymentPlanV5",
    "hpProvided": "true",
    "customAttributes": [{
        "visible": False,
        "constraints": "{}",
        "editable": True,
        "description": "desc domain name",
        "name": "DomainName",
        "value": "domain.net",
        "type": "string"
    },{
        "visible": False,
        "constraints": "{}",
        "editable": True,
        "description": "desc host name",
        "name": "hostname",
        "value": "myhost",
        "type": "string"
    }, {
        "visible": True,
        "constraints": "{}",
        "editable": True,
        "description": "desc keyboard layout type",
        "name": "KeyboardLayout",
        "value": "English",
        "type": "string"
    }],
    "goldenImageURI": "ESXi_6.5 (1)",
    "oeBuildPlanURI": "BP-Single-buildStep-Multi-CA-Read only Yes",
    "category": "oe-deployment-plans",
    "description": "Deployment Plan with all the valid fields and having multiple custom attributes",
    "name": "Valid DP with Multiple CA-Read only Yes"
}, {  # 2 Valid DP having single CA
    "type": "OEDeploymentPlanV5",
    "hpProvided": "true",
    "customAttributes": [{
        "visible": False,
        "constraints": "{}",
        "editable": True,
        "description": "desc host name",
        "name": "hostname",
        "value": "myhost",
        "type": "string"
    }],
    "goldenImageURI": "",
    "oeBuildPlanURI": "BP-Single-buildStep-Single-CA-Read only Yes",
    "category": "oe-deployment-plans",
    "description": "Deployment Plan with all the valid fields and having only one custom attribute",
    "name": "Valid DP with Single CA-Read only Yes"
}, {
        "type": "OEDeploymentPlanV5",
        "hpProvided": False,
        "customAttributes": [
        {
            "name": "Number",
            "visible": True,
            "value": "24",
            "description": "",
            "type": "string",
            "constraints": "{}",
            "editable": True,
        },
        {
            "name": "String",
            "visible": True,
            "value": "String",
            "description": "",
            "type": "string",
            "constraints": "{}",
            "editable": True,
        },
        {
            "name": "Hostname",
            "visible": True,
            "value": "Linuxhost",
            "description": "",
            "type": "string",
            "constraints": "{}",
            "editable": True,
        },
        {
            "name": "NIC",
            "visible": True,
            "value": "",
            "description": "",
            "type": "nic",
            "constraints": "{\"ipv4static\":true,\"ipv4dhcp\":false,\"ipv4disable\":false,\"parameters\":[\"dns1\"]}",
            "editable": True,
        }
    ],
        "goldenImageURI": "",
        "oeBuildPlanURI": "Inuse BP",
        "category": "oe-deployment-plans",
        "description": "Unassigned DP1",
        "name": "Unassigned DP1"
    }, {
"type": "OEDeploymentPlanV5",
        "hpProvided": False,
        "customAttributes": [
        {
            "name": "Number",
            "visible": True,
            "value": "24",
            "description": "",
            "type": "string",
            "constraints": "{}",
            "editable": True,
        },
        {
            "name": "String",
            "visible": True,
            "value": "String",
            "description": "",
            "type": "string",
            "constraints": "{}",
            "editable": True,
        },
        {
            "name": "Hostname",
            "visible": True,
            "value": "Linuxhost",
            "description": "",
            "type": "string",
            "constraints": "{}",
            "editable": True,
        },
        {
            "name": "NIC",
            "visible": True,
            "value": "",
            "description": "",
            "type": "nic",
            "constraints": "{\"ipv4static\":true,\"ipv4dhcp\":false,\"ipv4disable\":false,\"parameters\":[\"dns1\"]}",
            "editable": True,
        }
    ],
        "goldenImageURI": "",
        "oeBuildPlanURI": "Inuse BP",
        "category": "oe-deployment-plans",
        "description": "Edited Unassigned DP1",
        "name": "Edited Unassigned DP1"
    }]


serverprofile = [{
    "type": "ServerProfileV11",
    "name": "SP_RESTAPI-Read only No",
    "iscsiInitiatorNameType": "AutoGenerated",
    "serverProfileTemplateUri": None,
    "serverHardwareUri": serverHardwareUri[0],
    "serverHardwareTypeUri": "SY 480 Gen9 1",
    "enclosureGroupUri": "EG",
    "enclosureUri": enclosureUri[0],
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "firmware": {"firmwareInstallType": None, "forceInstallFirmware": False, "manageFirmware": False,
                 "firmwareBaselineUri": None},
    "macType": "Virtual",
    "wwnType": "Virtual",
    "category": "server-profiles",
    "connectionSettings": {"reapplyState": "NotApplying",
                           "connections": [
                               {"id": 1, "name": "Deployment Network A", "functionType": "Ethernet",
                                "networkUri": "deploy",
                                "portId": "Mezz 3:1-a", "requestedVFs": "Auto", "requestedMbps": "2500",
                                "allocatedVFs": 64, "macType": "Virtual", "wwpnType": "Virtual", "mac": '',
                                "allocatedMbps": 2500, "maximumMbps": 10000,
                                "boot": {"bootVolumeSource": "UserDefined", "priority": "Primary",
                                         "ethernetBootType": "iSCSI",
                                         "iscsi": {"initiatorNameSource": "ProfileInitiatorName"}}
                                },
								
                               {"id": 3, "name": "Blade_boot_mgmt", "functionType": "Ethernet", "networkUri": "mgmt",
                                "portId": "Mezz 3:1-c", "requestedVFs": 0, "requestedMbps": "2500", "allocatedVFs": 0,
                                "macType": "Virtual", "wwpnType": "Virtual", "mac": '',
                                "allocatedMbps": 2500, "maximumMbps": 10000,
                                "boot": {"priority": "NotBootable", "iscsi": {}}
                                }
                           ]},
    "bootMode": {"manageMode": True, "pxeBootPolicy": "Auto", "mode": "UEFIOptimized"},
    "boot": {"manageBoot": True, "order": ["HardDisk"]},
    "bios": {"reapplyState": "NotApplying", "manageBios": False, "overriddenSettings": []},
    "localStorage": {},
    "sanStorage": {"volumeAttachments": [], "manageSanStorage": False},
    "osDeploymentSettings":{"osDeploymentPlanUri": "Valid DP1 with Multiple CA-Read only No",
                            "osCustomAttributes": [{"name": "KeyboardLayout", "value": "English"}],
                            "osVolumeUri": None}
}, {
    'type':'ServerProfileV11',
    'name':'SP_RESTAPI-Read only Yes',
    'description': 'sp',
    'iscsiInitiatorNameType': 'AutoGenerated',
    'serverProfileTemplateUri': None,
    'serverHardwareUri': serverHardwareUri[1],
    'serverHardwareTypeUri': 'SY 480 Gen9 1',
    'enclosureGroupUri': 'EG',
    'enclosureUri': enclosureUri[1],
    'affinity': 'Bay',
    'hideUnusedFlexNics': True,
    'firmware':{'firmwareInstallType': None,'forceInstallFirmware':False,'manageFirmware':False,'firmwareBaselineUri':None},
    'macType':'Virtual',
    'wwnType':'Virtual',
    'category': 'server-profiles',
    'connectionSettings': {'connections':[
    {'id':1,'name':'Deployment Network A','functionType':'Ethernet','networkUri':'deploy',
                        'portId':'Mezz 3:1-a','requestedVFs':'Auto','requestedMbps':'2500','allocatedVFs':64,'macType':'Virtual','wwpnType':'Virtual','mac':'',
                        'allocatedMbps':2500,'maximumMbps':10000,
                        'boot':{'bootVolumeSource': 'UserDefined','priority':'Primary','ethernetBootType':"iSCSI",'iscsi':{'initiatorNameSource':'ProfileInitiatorName'}}
                        },

                        
                        {'id':3,'name':'Blade_boot_mgmt','functionType':'Ethernet','networkUri':'mgmt',
                        'portId':'Mezz 3:1-c','requestedVFs':0,'requestedMbps':'2500','allocatedVFs':0,'macType':'Virtual','wwpnType':'Virtual','mac':'',
                        'allocatedMbps':2500,'maximumMbps':10000,
                        'boot':{'priority':'NotBootable','iscsi':{}}
                        }

]},
'bootMode':{'manageMode':True,'pxeBootPolicy':'Auto','mode':'UEFIOptimized'},
'boot':{'manageBoot':True,'order':['HardDisk']},
'bios':{'reapplyState':'NotApplying','manageBios':False,'overriddenSettings':[]},
'localStorage':{},
'sanStorage':{'volumeAttachments':[],'manageSanStorage':False},
'osDeploymentSettings':{'osDeploymentPlanUri':'Valid DP with Multiple CA-Read only Yes',
'osCustomAttributes':[
                      {'name': "KeyboardLayout", 'value': "English"},
                      ],'osVolumeUri':None}
}, {

    "type": "ServerProfileV11",
    "name": "Unassigned SP",
    "iscsiInitiatorNameType": "AutoGenerated",
    "serverProfileTemplateUri": None,
    "serverHardwareUri": None,
    "serverHardwareTypeUri": "SY 480 Gen9 1",
    "enclosureGroupUri": "EG",
    "enclosureUri": None,
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "firmware": {"firmwareInstallType": None, "forceInstallFirmware": False, "manageFirmware": False,
                 "firmwareBaselineUri": None},
    "macType": "Virtual",
    "wwnType": "Virtual",
    "category": "server-profiles",
    "connectionSettings": {"reapplyState": "NotApplying",
                           "connections": [
                               {"id": 1, "name": "Deployment Network A", "functionType": "Ethernet",
                                "networkUri": "deploy",
                                "portId": "Mezz 3:1-a", "requestedVFs": "Auto", "requestedMbps": "2500",
                                "allocatedVFs": 64, "macType": "Virtual", "wwpnType": "Virtual", "mac": '',
                                "allocatedMbps": 2500, "maximumMbps": 10000,
                                "boot": {"bootVolumeSource": "UserDefined", "priority": "Primary",
                                         "ethernetBootType": "iSCSI",
                                         "iscsi": {"initiatorNameSource": "ProfileInitiatorName"}}
                                },


                               {"id": 3, "name": "Blade_boot_mgmt", "functionType": "Ethernet", "networkUri": "mgmt",
                                "portId": "Mezz 3:1-c", "requestedVFs": 0, "requestedMbps": "2500", "allocatedVFs": 0,
                                "macType": "Virtual", "wwpnType": "Virtual", "mac": '',
                                "allocatedMbps": 2500, "maximumMbps": 10000,
                                "boot": {"priority": "NotBootable", "iscsi": {}}
                                }
                           ]},
    "bootMode": {"manageMode": True, "pxeBootPolicy": "Auto", "mode": "UEFIOptimized"},
    "boot": {"manageBoot": True, "order": ["HardDisk"]},
    "bios": {"reapplyState": "NotApplying", "manageBios": False, "overriddenSettings": []},
    "localStorage": {},
    "sanStorage": {"volumeAttachments": [], "manageSanStorage": False},
    "osDeploymentSettings":{"osDeploymentPlanUri": "Unassigned DP1",
                            "osCustomAttributes": [{
                "name": "NIC.dhcp",
                "value": False,
                "constraints": None,
                "type": None
            }, {
                "name": "NIC.ipv4disable",
                "value": False,
                "constraints": None,
                "type": None
            },
            {
                "name": "Number",
                "value": "24",
                "constraints": "{}",
                "type": "string"
            },
            {
                "name": "Hostname",
                "value": "Linuxhost",
                "constraints": "{}",
                "type": "string"
            },
            {
                "name": "NIC.constraint",
                "value": "auto",
                "constraints": None,
                "type": None
            },
            {
                "name": "String",
                "value": "String",
                "constraints": "{}",
                "type": "string"
            },
            {
                "name": "NIC.networkuri",
                "value": "mgmt",
                "constraints": None,
                "type": None
            },
            {
                "name": "NIC.connectionid",
                "value": "3",
                "constraints": None,
                "type": None
            }
        ],
        "osVolumeUri": None}
}]

deploymentplan_update = [{
    "type": "OEDeploymentPlanV5",
    "hpProvided": False,
    "customAttributes": [{
        "visible": False,
        "constraints": "{}",
        "editable": True,
        "description": "desc domain name",
        "name": "DomainName",
        "value": "domain.net",
        "type": "string"
    }, {
        "visible": False,
        "constraints": "{}",
        "editable": True,
        "description": "desc host name",
        "name": "hostname",
        "value": "myhost",
        "type": "string"
    }, {
        "visible": True,
        "constraints": "{}",
        "editable": True,
        "description": "desc keyboard layout type",
        "name": "KeyboardLayout",
        "value": "English",
        "type": "string"
    }],
    "goldenImageURI": "Updated ESXi_6.5",
    "oeBuildPlanURI": "BP1-Single-buildStep-Multi-CA-Read only No",
    "category": "oe-deployment-plans",
    "description": "Deployment plan name and description got updated",
    "name": "Updated Valid DP1 with multi CA- Change in Name and Description"
},
    {
        "type": "OEDeploymentPlanV5",
        "hpProvided": False,
        "customAttributes": [{
            "visible": False,
            "constraints": "{}",
            "editable": True,
            "description": "desc domain name",
            "name": "DomainName",
            "value": "domain.net",
            "type": "string"
        }, {
            "visible": False,
            "constraints": "{}",
            "editable": True,
            "description": "desc host name",
            "name": "hostname",
            "value": "myhost",
            "type": "string"
        }, {
            "visible": True,
            "constraints": "{}",
            "editable": True,
            "description": "desc keyboard layout type",
            "name": "KeyboardLayout",
            "value": "English",
            "type": "string"
        }],
        "goldenImageURI": "Updated-1 ESXi_6.5",
        "oeBuildPlanURI": "BP1-Single-buildStep-Multi-CA-Read only No",
        "category": "oe-deployment-plans",
        "description": "Deployment plan name and description got updated",
        "name": "Updated-1 Valid DP1 with multi CA- Change in Name and Description"
    },
    {
        "type": "OEDeploymentPlanV5",
        "hpProvided": False,
        "customAttributes": [{
            "visible": False,
            "constraints": "{}",
            "editable": True,
            "description": "desc domain name",
            "name": "DomainName",
            "value": "domain.net",
            "type": "string"
        }, {
            "visible": False,
            "constraints": "{}",
            "editable": True,
            "description": "desc host name",
            "name": "hostname",
            "value": "myhost",
            "type": "string"
        }, {
            "visible": True,
            "constraints": "{}",
            "editable": True,
            "description": "desc keyboard layout type",
            "name": "KeyboardLayout",
            "value": "English",
            "type": "string"
        }],
        "goldenImageURI": "Updated-2 ESXi_6.5",
        "oeBuildPlanURI": "BP1-Single-buildStep-Multi-CA-Read only No",
        "category": "oe-deployment-plans",
        "description": "Deployment plan name and description got updated",
        "name": "Updated-2 Valid DP1 with multi CA- Change in Name and Description"
    }
]

SPT_from_SP = [{#0 Create SPT from Server profile
'name':'SPT_from_Serverprofile'
},{ #2, Serverprofile_template_create
'name': 'SPT_from_SP'
}]

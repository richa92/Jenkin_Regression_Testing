#from winnt import NULL
from requests.api import patch

admin_credentials = {
    'userName': 'Administrator',
    'password': 'admin123'
}


goldenimage_add = [{'name': 'ESXi_60',
                    'description': 'Golden Image for ESXi 6.0',
                    'file': "valid_file"},
                   {'name': 'ESXi_60_1',
                    'description': 'Golden Image for ESXi 6.0',
                    'file': "valid_file"}
                   ]


goldenimage_delete = [{'name': 'ESXi_60'},
                      {'name': 'ESXi_60_1'}
                      ]


planscript = [{
    "type": "PlanScript",
    "description": "Mount Script",
    "name": "PS for MOUNT",
    "hpProvided": "false",
    "planType": "deploy",
    "content": "# (C) Copyright 2015-2015 Hewlett-Packard Development Company, L.P.\n# Script to mount disk in libguesfs virtual appliance for personalizaiton or generalization\nmount /dev/sda5 /\n\n\n# creating tmp dir at local filesystem\n!mkdir -p ./onetime\n!mkdir -p ./state/local\n\n# copying required files for personalization/generalization to local filesysystem\n-copy-out /onetime.tgz .\n-copy-out /state.tgz .\n-copy-out /boot.cfg .\n\n# trying to findout whether onetime.tgz will be picked up during booting or state.tgz will be picked\n# based on that we can process either onetime.tgz or state.tgz for personalization/generalization\n\n-!grep \"onetime.tgz\"  ./boot.cfg >./onetime_found\n-!grep \"state.tgz\" ./boot.cfg > ./state_found"
}, {
    "type": "PlanScript",
    "description": 'Deploy Script',
    "name": "PS for  DEPLOY",
    "hpProvided": "false",
    "planType": "deploy",
    "content": "# (C) Copyright 2015-2015 Hewlett-Packard Development Company, L.P.\n# Script to PERSONALIZE\n\n!if [ -s  \"state_found\" ]; \\\nthen \\\ncd state; \\\ntar xvpzf ../state.tgz; \\\ncd local; \\\ntar xvpzf ../local.tgz; \\\nmkdir -p etc/rc.local.d; \\\necho esxcli system hostname set -H \"@hostname:Bay8@\">>   etc/rc.local.d/local.sh; \\\necho esxcli system hostname set -d \"@DomainName:vse.rdlabs.hpecorp.net@\">>  etc/rc.local.d/local.sh; \\\necho esxcli system settings keyboard layout set -l \"@KeyboardLayout:English@\">>  etc/rc.local.d/local.sh; \\\nchmod 777  etc/rc.local.d/local.sh; \\\ntar cvpzf ../local.tgz *; \\\ncd ../; \\\ntar cvpzf ../state.tgz local.tgz; \\\ntouch  ../state.tgz; \\\nelse \\\ncd  onetime; \\\ntar xvpzf ../onetime.tgz; \\\necho esxcli system hostname set -H \"@hostname:Bay8@\">>   etc/rc.local.d/local.sh; \\\necho esxcli system hostname set -d \"@DomainName:vse.rdlabs.hpecorp.net@\">>  etc/rc.local.d/local.sh; \\\necho esxcli system settings keyboard layout set -l \"@KeyboardLayout:English@\">>  etc/rc.local.d/local.sh; \\\nchmod 777   etc/rc.local.d/local.sh; \\\ntar cvpzf ../onetime.tgz *; \\\nfi"
}, {
    "type": "PlanScript",
    "description": "Umount Script",
    "name": "PS for UMOUNT",
    "hpProvided": 'false',
    "planType": "deploy",
    "content": "# (C) Copyright 2015-2015 Hewlett-Packard Development Company, L.P.\n# Script to Unmount\n\n-copy-in onetime.tgz /\n-copy-in state.tgz /\numount /"
}, {
    "type": "PlanScript",
    "description": "Planscript having multiple CA",
    "name": "PS-Multi-CA",
    "hpProvided": 'false',
    "planType": "deploy",
    "content": "# (C) Copyright 2015-2015 Hewlett-Packard Development Company, L.P.\n# Script to mount disk in libguesfs virtual appliance for personalizaiton or generalization\nmount /dev/sda5 /\n\n\n# creating tmp dir at local filesystem\n!mkdir -p ./onetime\n!mkdir -p ./state/local\n\n# copying required files for personalization/generalization to local filesysystem\n-copy-out /onetime.tgz .\n-copy-out /state.tgz .\n-copy-out /boot.cfg .\n\n# trying to findout whether onetime.tgz will be picked up during booting or state.tgz will be picked\n# based on that we can process either onetime.tgz or state.tgz for personalization/generalization\n\n-!grep \"onetime.tgz\"  ./boot.cfg >./onetime_found\n-!grep \"state.tgz\" ./boot.cfg > ./state_found\n\n\n# (C) Copyright 2015-2015 Hewlett-Packard Development Company, L.P.\n# Script to PERSONALIZE\n\n!if [ -s  \"state_found\" ]; \\\nthen \\\ncd state; \\\ntar xvpzf ../state.tgz; \\\ncd local; \\\ntar xvpzf ../local.tgz; \\\nmkdir -p etc/rc.local.d; \\\necho esxcli system hostname set -H \"@hostname:Bay8@\">>   etc/rc.local.d/local.sh; \\\necho esxcli system hostname set -d \"@DomainName:vse.rdlabs.hpecorp.net@\">>  etc/rc.local.d/local.sh; \\\necho esxcli system settings keyboard layout set -l \"@KeyboardLayout:English@\">>  etc/rc.local.d/local.sh; \\\nchmod 777  etc/rc.local.d/local.sh; \\\ntar cvpzf ../local.tgz *; \\\ncd ../; \\\ntar cvpzf ../state.tgz local.tgz; \\\ntouch  ../state.tgz; \\\nelse \\\ncd  onetime; \\\ntar xvpzf ../onetime.tgz; \\\necho esxcli system hostname set -H \"@hostname:Bay8@\">>   etc/rc.local.d/local.sh; \\\necho esxcli system hostname set -d \"@DomainName:vse.rdlabs.hpecorp.net@\">>  etc/rc.local.d/local.sh; \\\necho esxcli system settings keyboard layout set -l \"@KeyboardLayout:English@\">>  etc/rc.local.d/local.sh; \\\nchmod 777   etc/rc.local.d/local.sh; \\\ntar cvpzf ../onetime.tgz *; \\\nfi\n\n\n\n# (C) Copyright 2015-2015 Hewlett-Packard Development Company, L.P.\n# Script to Unmount\n\n-copy-in onetime.tgz /\n-copy-in state.tgz /\numount /"
}, {
    "type": "PlanScript",
    "description": "Planscript having single CA",
    "name": "PS-Single-CA",
    "hpProvided": 'false',
    "planType": "deploy",
    "content": "# (C) Copyright 2015-2015 Hewlett-Packard Development Company, L.P.\n# Script to PERSONALIZE\n\n!if [ -s  \"state_found\" ]; \\\nthen \\\ncd state; \\\ntar xvpzf ../state.tgz; \\\ncd local; \\\ntar xvpzf ../local.tgz; \\\nmkdir -p etc/rc.local.d; \\\necho esxcli system hostname set -H \"@hostname:Bay8@\">>   etc/rc.local.d/local.sh; \\\nchmod 777  etc/rc.local.d/local.sh; \\\ntar cvpzf ../local.tgz *; \\\ncd ../; \\\ntar cvpzf ../state.tgz local.tgz; \\\ntouch  ../state.tgz; \\\nelse \\\ncd  onetime; \\\ntar xvpzf ../onetime.tgz; \\\necho esxcli system hostname set -H \"@hostname:Bay8@\">>   etc/rc.local.d/local.sh; \\\nchmod 777   etc/rc.local.d/local.sh; \\\ntar cvpzf ../onetime.tgz *; \\\nfi"
}]


planscript_delete = [{
    "name": "PS for MOUNT"
}, {
    "name": "PS for  DEPLOY"
}, {
    "name": "PS for UMOUNT"
}, {
    "name": "PS-Multi-CA"
}, {
    "name": "PS-Single-CA"
}]


buildplan_create = [{
    "type": "OeBuildPlanV5",
    "customAttributes": [
        {
            "constraints": "",
            "description": "desciption",
            "name": "KeyboardLayout",
            "value": "English",
            "type": "string"
        },
        {
            "constraints": "",
            "description": "desciption",
            "name": "hostname",
            "value": "Bay8",
            "type": "string"
        },
        {
            "constraints": "",
            "description": "desciption",
            "name": "DomainName",
            "value": "vse.rdlabs.hpecorp.net",
            "type": "string"
        }
    ],
    "buildStep": [
        {
            "planScriptUri": "PS-Multi-CA",
            "serialNumber": "1"
        }
    ],
    "hpProvided": False,
    "oeBuildPlanType": "deploy",
    "description": "BP-Single-buildStep-Multi-CA",
    "category": "oe-build-plans",
    "name": "BP-Single-buildStep-Multi-CA"
}, {
    "type": "OeBuildPlanV5",
    "customAttributes": [
        {
            "constraints": "",
            "description": "desciption",
            "name": "hostname",
            "value": "Bay8",
            "type": "string"
        }
    ],
    "buildStep": [
        {
            "planScriptUri": "PS-Single-CA",
            "serialNumber": "1"
        }
    ],
    "hpProvided": False,
    "oeBuildPlanType": "deploy",
    "description": "BP-Single-buildStep-Single-CA",
    "category": "oe-build-plans",
    "name": "BP-Single-buildStep-Single-CA"
}, {
    "type": "OeBuildPlanV5",
    "customAttributes": [
        {
            "constraints": "",
            "description": "desciption",
            "name": "KeyboardLayout",
            "value": "English",
            "type": "string"
        },
        {
            "constraints": "",
            "description": "desciption",
            "name": "hostname",
            "value": "Bay8",
            "type": "string"
        },
        {
            "constraints": "",
            "description": "desciption",
            "name": "DomainName",
            "value": "vse.rdlabs.hpecorp.net",
            "type": "string"
        }
    ],
    "buildStep": [
        {
            "planScriptUri": "PS-Multi-CA",
            "serialNumber": "1"
        }
    ],
    "hpProvided": False,
    "oeBuildPlanType": "deploy",
    "description": "BP-Single-buildStep-Multi-CA",
    "category": "oe-build-plans",
    "name": "BP-Single-buildStep-Multi-CA-1"
}]


buildplan_del = [{
    'name': 'BP-Single-buildStep-Multi-CA'
}, {
    'name': 'BP-Single-buildStep-Single-CA'
}, {
    'name': 'BP-Single-buildStep-Multi-CA-1'
}]


deploymentplan_create = [{  # 1 Valid DP having Multiple CA
    "type": "OEDeploymentPlanV5",
    "hpProvided": False,
    "customAttributes": [{
        "visible": False,
        "constraints": "",
        "editable": True,
        "description": "desc domain name",
        "name": "DomainName",
        "value": "domain.net",
        "type": "string"
    }, {
        "visible": False,
        "constraints": "",
        "editable": True,
        "description": "desc host name",
        "name": "hostname",
        "value": "myhost",
        "type": "string"
    }, {
        "visible": True,
        "constraints": "",
        "editable": True,
        "description": "desc keyboard layout type",
        "name": "KeyboardLayout",
        "value": "English",
        "type": "string"
    }],
    "goldenImageURI": "ESXi_60",
    "oeBuildPlanURI": "BP-Single-buildStep-Multi-CA",
    "category": "oe-deployment-plans",
    "description": "Deployment Plan with all the valid fields and having multiple custom attributes",
    "name": "Valid DP with Multiple CA"
}, {  # 2 Valid DP having single CA
    "type": "OEDeploymentPlanV5",
    "hpProvided": False,
    "customAttributes": [{
        "visible": False,
        "constraints": "",
        "editable": True,
        "description": "desc host name",
        "name": "hostname",
        "value": "myhost",
        "type": "string"
    }],
    "goldenImageURI": "ESXi_60",
    "oeBuildPlanURI": "BP-Single-buildStep-Single-CA",
    "category": "oe-deployment-plans",
    "description": "Deployment Plan with all the valid fields and having only one custom attribute",
    "name": "Valid DP with Single CA"
}, {  # 3 Valid DP with name containing 255 characters
    "type": "OEDeploymentPlanV5",
    "hpProvided": False,
    "customAttributes": [{
        "visible": False,
        "constraints": "",
        "editable": True,
        "description": "desc domain name",
        "name": "DomainName",
        "value": "domain.net",
        "type": "string"
    }, {
        "visible": False,
        "constraints": "",
        "editable": True,
        "description": "desc host name",
        "name": "hostname",
        "value": "myhost",
        "type": "string"
    }, {
        "visible": True,
        "constraints": "",
        "editable": True,
        "description": "desc keyboard layout type",
        "name": "KeyboardLayout",
        "value": "English",
        "type": "string"
    }],
    "goldenImageURI": "ESXi_60",
    "oeBuildPlanURI": "BP-Single-buildStep-Multi-CA",
    "category": "oe-deployment-plans",
    "description": "Deployment Plan with all the valid fields and name containing 255 characters",
    "name": "Valid DP having name containing 255 characters thnamelengnamenamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthname"
}, {  # 4 Name_Having_More_Than_255_Char
    "type": "OEDeploymentPlanV5",
    "hpProvided": False,
    "customAttributes": [{
        "visible": False,
        "constraints": "",
        "editable": True,
        "description": "desc domain name",
        "name": "DomainName",
        "value": "domain.net",
        "type": "string"
    }, {
        "visible": False,
        "constraints": "",
        "editable": True,
        "description": "desc host name",
        "name": "hostname",
        "value": "myhost",
        "type": "string"
    }, {
        "visible": True,
        "constraints": "",
        "editable": True,
        "description": "desc keyboard layout type",
        "name": "KeyboardLayout",
        "value": "English",
        "type": "string"
    }],
    "goldenImageURI": "ESXi_60",
    "oeBuildPlanURI": "BP-Single-buildStep-Multi-CA",
    "category": "oe-deployment-plans",
    "description": "Deployment Plan with all the valid fields and name containing more than 255 characters",
    "name": "Valid DP having name containing more than 255 characters thnamelengnamenamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelength-255"
}, {  # 5 Desc_Having_1000_Char
    "type": "OEDeploymentPlanV5",
    "hpProvided": False,
    "customAttributes": [{
        "visible": False,
        "constraints": "",
        "editable": True,
        "description": "desc domain name",
        "name": "DomainName",
        "value": "domain.net",
        "type": "string"
    }, {
        "visible": False,
        "constraints": "",
        "editable": True,
        "description": "desc host name",
        "name": "hostname",
        "value": "myhost",
        "type": "string"
    }, {
        "visible": True,
        "constraints": "",
        "editable": True,
        "description": "desc keyboard layout type",
        "name": "KeyboardLayout",
        "value": "English",
        "type": "string"
    }],
    "goldenImageURI": "ESXi_60",
    "oeBuildPlanURI": "BP-Single-buildStep-Multi-CA",
    "category": "oe-deployment-plans",
    "description": "Deployment Plan with all the valid fields and description field having 1000 characters Deployment Plan with all the valid fields and description field having 1000 characters Deployment Plan with all the valid fields and description field having 1000 characters Deployment Plan with all the valid fields and description field having 1000 characters Deployment Plan with all the valid fields and description field having 1000 characters Deployment Plan with all the valid fields and description field having 1000 characters Deployment Plan with all the valid fields and description field having 1000 characters Deployment Plan with all the valid fields and description field having 1000 characters Deployment Plan with all the valid fields and description field having 1000 characters Deployment Plan with all the valid fields and description field having 1000 characters Deployment Plan with all the valid fields and description field having 1000 characters Deployment Plan with all the valid fiel END",
    "name": "Valid DP having description field containing 1000 characters"
}, {  # 6 Desc_Having_More_Than_1000_Char
    "type": "OEDeploymentPlanV5",
    "hpProvided": False,
    "customAttributes": [{
        "visible": False,
        "constraints": "",
        "editable": True,
        "description": "desc domain name",
        "name": "DomainName",
        "value": "domain.net",
        "type": "string"
    }, {
        "visible": False,
        "constraints": "",
        "editable": True,
        "description": "desc host name",
        "name": "hostname",
        "value": "myhost",
        "type": "string"
    }, {
        "visible": True,
        "constraints": "",
        "editable": True,
        "description": "desc keyboard layout type",
        "name": "KeyboardLayout",
        "value": "English",
        "type": "string"
    }],
    "goldenImageURI": "ESXi_60",
    "oeBuildPlanURI": "BP-Single-buildStep-Multi-CA",
    "category": "oe-deployment-plans",
    "description": "Deployment Plan with all the valid fields and description field having more 1000 characters Deployment Plan with all the valid fields and description field having 1000 characters Deployment Plan with all the valid fields and description field having 1000 characters Deployment Plan with all the valid fields and description field having 1000 characters Deployment Plan with all the valid fields and description field having 1000 characters Deployment Plan with all the valid fields and description field having 1000 characters Deployment Plan with all the valid fields and description field having 1000 characters Deployment Plan with all the valid fields and description field having 1000 characters Deployment Plan with all the valid fields and description field having 1000 characters Deployment Plan with all the valid fields and description field having 1000 characters Deployment Plan with all the valid fields and description field having 1000 characters Deployment Plan with all the valid fiel END",
    "name": "Valid DP having description field containing more than 1000 characters"
}, {  # 7 DP having no Name, Desc, GI, BP and CA
    "type": "OEDeploymentPlanV5",
    "hpProvided": False,
    "customAttributes": [],
    "goldenImageURI": "",
    "oeBuildPlanURI": "",
    "category": "oe-deployment-plans",
    "description": "",
    "name": ""
}, {  # 8 Valid_DP_Multi_CA for Update test 1- Change in Name
    "type": "OEDeploymentPlanV5",
    "hpProvided": False,
    "customAttributes": [{
        "visible": False,
        "constraints": "",
        "editable": True,
        "description": "desc domain name",
        "name": "DomainName",
        "value": "domain.net",
        "type": "string"
    }, {
        "visible": False,
        "constraints": "",
        "editable": True,
        "description": "desc host name",
        "name": "hostname",
        "value": "myhost",
        "type": "string"
    }, {
        "visible": True,
        "constraints": "",
        "editable": True,
        "description": "desc keyboard layout type",
        "name": "KeyboardLayout",
        "value": "English",
        "type": "string"
    }],
    "goldenImageURI": "ESXi_60",
    "oeBuildPlanURI": "BP-Single-buildStep-Multi-CA",
    "category": "oe-deployment-plans",
    "description": "Deployment Plan with all the valid fields and having multiple custom attributes",
    "name": "Valid DP with multiple CA for Update test- Change in Name"
}, {  # 9 Valid_DP_Multi_CA for Update test- Change in Name and Description
    "type": "OEDeploymentPlanV5",
    "hpProvided": False,
    "customAttributes": [{
            "visible": False,
            "constraints": "",
            "editable": True,
            "description": "desc domain name",
            "name": "DomainName",
            "value": "domain.net",
            "type": "string"
    }, {
        "visible": False,
        "constraints": "",
        "editable": True,
        "description": "desc host name",
        "name": "hostname",
        "value": "myhost",
        "type": "string"
    }, {
        "visible": True,
        "constraints": "",
        "editable": True,
        "description": "desc keyboard layout type",
        "name": "KeyboardLayout",
        "value": "English",
        "type": "string"
    }],
    "goldenImageURI": "ESXi_60",
    "oeBuildPlanURI": "BP-Single-buildStep-Multi-CA",
    "category": "oe-deployment-plans",
    "description": "Deployment Plan with all the valid fields and having multiple custom attributes",
    "name": "Valid DP with multiple CA for Update test- Change in Name and Description"
}, {  # 10 DP without Name, Desc, GI, BP, but having valid CA
    "type": "OEDeploymentPlanV5",
    "hpProvided": False,
    "customAttributes": [{
        "visible": False,
        "constraints": "",
        "editable": True,
        "description": "desc domain name",
        "name": "DomainName",
        "value": "domain.net",
        "type": "string"
    }, {
        "visible": False,
        "constraints": "",
        "editable": True,
        "description": "desc host name",
        "name": "hostname",
        "value": "myhost",
        "type": "string"
    }, {
        "visible": True,
        "constraints": "",
        "editable": True,
        "description": "desc keyboard layout type",
        "name": "KeyboardLayout",
        "value": "English",
        "type": "string"
    }],
    "goldenImageURI": "",
    "oeBuildPlanURI": "",
    "category": "oe-deployment-plans",
    "description": "",
    "name": ""
}, {  # 11 DP having valid Name, Desc, GI and BP, but without any CA
    "type": "OEDeploymentPlanV5",
    "hpProvided": False,
    "customAttributes": [{
        "visible": False,
        "constraints": "",
        "editable": True,
        "description": "desc domain name",
        "name": "DomainName",
        "value": "",
        "type": "string"
    }, {
        "visible": False,
        "constraints": "",
        "editable": True,
        "description": "desc host name",
        "name": "hostname",
        "value": "",
        "type": "string"
    }, {
        "visible": True,
        "constraints": "",
        "editable": True,
        "description": "desc keyboard layout type",
        "name": "KeyboardLayout",
        "value": "",
        "type": "string"
    }],
    "goldenImageURI": "ESXi_60",
    "oeBuildPlanURI": "BP-Single-buildStep-Multi-CA",
    "category": "oe-deployment-plans",
    "description": "Valid GI, BP, Name, Desc but blank CA value",
    "name": "Valid GI BP Name Desc but blank CA value"
}, {  # 12 Valid GI, BP, Name, Desc, but NO CA
    "type": "OEDeploymentPlanV5",
    "hpProvided": False,
    "goldenImageURI": "ESXi_60",
    "oeBuildPlanURI": "BP-Single-buildStep-Multi-CA",
    "category": "oe-deployment-plans",
    "description": "Valid GI, BP, Name, Desc, but without CA",
    "name": "Valid GI BP Name Desc but NO CA"
}, {  # 13 Valid Name, Desc, GI, CA but blank BP
    "type": "OEDeploymentPlanV5",
    "hpProvided": False,
    "customAttributes": [{
        "visible": False,
        "constraints": "",
        "editable": True,
        "description": "desc domain name",
        "name": "DomainName",
        "value": "domain.net",
        "type": "string"
    }, {
        "visible": False,
        "constraints": "",
        "editable": True,
        "description": "desc host name",
        "name": "hostname",
        "value": "myhost",
        "type": "string"
    }, {
        "visible": True,
        "constraints": "",
        "editable": True,
        "description": "desc keyboard layout type",
        "name": "KeyboardLayout",
        "value": "English",
        "type": "string"
    }],
    "goldenImageURI": "ESXi_60",
    "oeBuildPlanURI": "",
    "category": "oe-deployment-plans",
    "description": "Valid GI, Name, Desc, CA but blank BP",
    "name": "Valid Name Desc GI CA but blank BP"
}, {  # 14 DP having BP, Name, Desc, CA but blank GI
    "type": "OEDeploymentPlanV5",
    "hpProvided": False,
    "customAttributes": [{
        "visible": False,
        "constraints": "",
        "editable": True,
        "description": "desc domain name",
        "name": "DomainName",
        "value": "domain.net",
        "type": "string"
    }, {
        "visible": False,
        "constraints": "",
        "editable": True,
        "description": "desc host name",
        "name": "hostname",
        "value": "myhost",
        "type": "string"
    }, {
        "visible": True,
        "constraints": "",
        "editable": True,
        "description": "desc keyboard layout type",
        "name": "KeyboardLayout",
        "value": "English",
        "type": "string"
    }],
    "goldenImageURI": "",
    "oeBuildPlanURI": "BP-Single-buildStep-Multi-CA",
    "category": "oe-deployment-plans",
    "description": "Valid Name, Desc, CA and BP, but blank GI",
    "name": "Valid Name Desc CA and BP but blank GI"
}, {  # 15 GI, BP, Name, Desc, CA but duplicate name
    "type": "OEDeploymentPlanV5",
    "hpProvided": False,
    "customAttributes": [{
        "visible": False,
        "constraints": "",
        "editable": True,
        "description": "desc domain name",
        "name": "DomainName",
        "value": "domain.net",
        "type": "string"
    }, {
        "visible": False,
        "constraints": "",
        "editable": True,
        "description": "desc host name",
        "name": "hostname",
        "value": "myhost",
        "type": "string"
    }, {
        "visible": True,
        "constraints": "",
        "editable": True,
        "description": "desc keyboard layout type",
        "name": "KeyboardLayout",
        "value": "English",
        "type": "string"
    }],
    "goldenImageURI": "ESXi_60",
    "oeBuildPlanURI": "BP-Single-buildStep-Multi-CA",
    "category": "oe-deployment-plans",
    "description": "Valid GI, BP, Name, Desc, CA but duplicate name",
    "name": "Valid DP with multiple CA"
}, {  # 16 DP having GI, BP, Name, Desc, CA but Invalid name
    "type": "OEDeploymentPlanV5",
    "hpProvided": False,
    "customAttributes": [{
        "visible": False,
        "constraints": "",
        "editable": True,
        "description": "desc domain name",
        "name": "DomainName",
        "value": "domain.net",
        "type": "string"
    }, {
        "visible": False,
        "constraints": "",
        "editable": True,
        "description": "desc host name",
        "name": "hostname",
        "value": "myhost",
        "type": "string"
    }, {
        "visible": True,
        "constraints": "",
        "editable": True,
        "description": "desc keyboard layout type",
        "name": "KeyboardLayout",
        "value": "English",
        "type": "string"
    }],
    "goldenImageURI": "ESXi_60",
    "oeBuildPlanURI": "BP-Single-buildStep-Multi-CA",
    "category": "oe-deployment-plans",
    "description": "DP having GI, BP, Name, Desc, CA but Name containing special characters",
    "name": "#@^& DP containg special charaters (($% --##"
}, {  # 17 DP having only CA (It does not have any Name, Desc, GI and BP)
    "type": "OEDeploymentPlanV5",
    "hpProvided": False,
    "customAttributes": [{
        "visible": False,
        "constraints": "",
        "editable": True,
        "description": "desc domain name",
        "name": "DomainName",
        "value": "domain.net",
        "type": "string"
    }, {
        "visible": False,
        "constraints": "",
        "editable": True,
        "description": "desc host name",
        "name": "hostname",
        "value": "myhost",
        "type": "string"
    }, {
        "visible": True,
        "constraints": "",
        "editable": True,
        "description": "desc keyboard layout type",
        "name": "KeyboardLayout",
        "value": "English",
        "type": "string"
    }],
    "goldenImageURI": "",
    "oeBuildPlanURI": "",
    "category": "oe-deployment-plans",
    "description": "",
    "name": ""
}, {  # 18 Valid DP having Multiple CA but hpProvided set to True
    "type": "OEDeploymentPlanV5",
    "hpProvided": True,
    "customAttributes": [{
        "visible": False,
        "constraints": "",
        "editable": True,
        "description": "desc domain name",
        "name": "DomainName",
        "value": "domain.net",
        "type": "string"
    }, {
        "visible": False,
        "constraints": "",
        "editable": True,
        "description": "desc host name",
        "name": "hostname",
        "value": "myhost",
        "type": "string"
    }, {
        "visible": False,
        "constraints": "",
        "editable": True,
        "description": "desc keyboard layout type",
        "name": "KeyboardLayout",
        "value": "English",
        "type": "string"
    }],
    "goldenImageURI": "ESXi_60",
    "oeBuildPlanURI": "BP-Single-buildStep-Multi-CA",
    "category": "oe-deployment-plans",
    "description": "Deployment Plan with all the valid fields and having multiple custom attributes",
    "name": "DP having multiple CA and hpProvided set to True"
}, {  # 19 Valid DP having Multiple CA and all CA visible set to True
    "type": "OEDeploymentPlanV5",
    "hpProvided": False,
    "customAttributes": [{
        "visible": True,
        "constraints": "",
        "editable": True,
        "description": "desc domain name",
        "name": "DomainName",
        "value": "domain.net",
        "type": "string"
    }, {
        "visible": True,
        "constraints": "",
        "editable": True,
        "description": "desc host name",
        "name": "hostname",
        "value": "myhost",
        "type": "string"
    }, {
        "visible": True,
        "constraints": "",
        "editable": True,
        "description": "desc keyboard layout type",
        "name": "KeyboardLayout",
        "value": "English",
        "type": "string"
    }],
    "goldenImageURI": "ESXi_60",
    "oeBuildPlanURI": "BP-Single-buildStep-Multi-CA",
    "category": "oe-deployment-plans",
    "description": "Deployment Plan with all the valid fields and having multiple custom attributes",
    "name": "DP having multiple CA and all CA visible set to True"
}, {  # 20 Valid DP having Multiple CA and some of the CA visible set to True
    "type": "OEDeploymentPlanV5",
    "hpProvided": False,
    "customAttributes": [{
        "visible": False,
        "constraints": "",
        "editable": False,
        "description": "desc domain name",
        "name": "DomainName",
        "value": "domain.net",
        "type": "string"
    }, {
        "visible": True,
        "constraints": "",
        "editable": True,
        "description": "desc host name",
        "name": "hostname",
        "value": "myhost",
        "type": "string"
    }, {
        "visible": True,
        "constraints": "",
        "editable": True,
        "description": "desc keyboard layout type",
        "name": "KeyboardLayout",
        "value": "English",
        "type": "string"
    }],
    "goldenImageURI": "ESXi_60",
    "oeBuildPlanURI": "BP-Single-buildStep-Multi-CA",
    "category": "oe-deployment-plans",
    "description": "Deployment Plan with all the valid fields and having multiple custom attributes",
    "name": "DP having multiple CA and some of the CA visible set to True"
}, {  # 21 Valid DP having Multiple CA and and all CA are not editable
    "type": "OEDeploymentPlanV5",
    "hpProvided": False,
    "customAttributes": [{
        "visible": False,
        "constraints": "",
        "editable": False,
        "description": "desc domain name",
        "name": "DomainName",
        "value": "domain.net",
        "type": "string"
    }, {
        "visible": False,
        "constraints": "",
        "editable": False,
        "description": "desc host name",
        "name": "hostname",
        "value": "myhost",
        "type": "string"
    }, {
        "visible": True,
        "constraints": "",
        "editable": False,
        "description": "desc keyboard layout type",
        "name": "KeyboardLayout",
        "value": "English",
        "type": "string"
    }],
    "goldenImageURI": "ESXi_60",
    "oeBuildPlanURI": "BP-Single-buildStep-Multi-CA",
    "category": "oe-deployment-plans",
    "description": "Deployment Plan with all the valid fields and having multiple custom attributes",
    "name": "DP having multiple CA and all CA are not editable"
}, {  # 22 Valid DP to test GET Public API call
    "type": "OEDeploymentPlanV5",
    "hpProvided": False,
    "customAttributes": [{
        "visible": False,
        "constraints": "",
        "editable": True,
        "description": "desc host name",
        "name": "hostname",
        "value": "myhost",
        "type": "string"
    }],
    "goldenImageURI": "ESXi_60",
    "oeBuildPlanURI": "BP-Single-buildStep-Single-CA",
    "category": "oe-deployment-plans",
    "description": "Deployment Plan with all the valid fields and having only one custom attribute",
    "name": "CL RHEL API_GET"
}, {  # 23 Valid DP to test GET Public API call
    "type": "OEDeploymentPlanV5",
    "hpProvided": False,
    "customAttributes": [{
        "visible": False,
        "constraints": "",
        "editable": True,
        "description": "desc host name",
        "name": "hostname",
        "value": "myhost",
        "type": "string"
    }],
    "goldenImageURI": "ESXi_60",
    "oeBuildPlanURI": "BP-Single-buildStep-Single-CA",
    "category": "oe-deployment-plans",
    "description": "Deployment Plan with all the valid fields and having only one custom attribute",
    "name": "cl artifact_for_GET"
}, {  # 24 Valid DP to test GET Public API call
    "type": "OEDeploymentPlanV5",
    "hpProvided": False,
    "customAttributes": [{
        "visible": False,
        "constraints": "",
        "editable": True,
        "description": "desc host name",
        "name": "hostname",
        "value": "myhost",
        "type": "string"
    }],
    "goldenImageURI": "ESXi_60",
    "oeBuildPlanURI": "BP-Single-buildStep-Single-CA",
    "category": "oe-deployment-plans",
    "description": "Deployment Plan with all the valid fields and having only one custom attribute",
    "name": "RHEL-7.2-deploymentplan"
}, {  # 25 Valid DP to test GET Public API call
    "type": "OEDeploymentPlanV5",
    "hpProvided": False,
    "customAttributes": [{
        "visible": False,
        "constraints": "",
        "editable": True,
        "description": "desc host name",
        "name": "hostname",
        "value": "myhost",
        "type": "string"
    }],
    "goldenImageURI": "ESXi_60",
    "oeBuildPlanURI": "BP-Single-buildStep-Single-CA",
    "category": "oe-deployment-plans",
    "description": "Deployment Plan with all the valid fields and having only one custom attribute",
    "name": "123_deploymentplan"
}, {  # 26 Valid DP to test GET Public API call
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
    "goldenImageURI": "ESXi_60",
    "oeBuildPlanURI": "BP-Single-buildStep-Single-CA",
    "category": "oe-deployment-plans",
    "description": "Deployment Plan with all the valid fields and having only one custom attribute",
    "name": "deploymentplan_456"
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
    "goldenImageURI": "ESXi_60",
    "oeBuildPlanURI": "BP-Single-buildStep-Multi-CA",
    "category": "oe-deployment-plans",
    "description": "Deployment plan name and description got updated",
    "name": "Update DP- Change in Name and Description"
}, {
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
    "goldenImageURI": "ESXi_60",
    "oeBuildPlanURI": "BP-Single-buildStep-Multi-CA",
    "category": "oe-deployment-plans",
    "description": "Deployment plan got changed",
    "name": "Update DP- Change in Name"
}, {
    "type": "OEDeploymentPlanV5",
    "hpProvided": False,
    "customAttributes": [{
        "visible": False,
        "constraints": "{}",
        "editable": True,
        "description": "Update desc domain name",
        "name": "DomainName",
        "value": "update.domain.net",
        "type": "string"
    }, {
        "visible": False,
        "constraints": "{}",
        "editable": True,
        "description": "Update desc host name",
        "name": "hostname",
        "value": "Update myhost",
        "type": "string"
    }, {
        "visible": True,
        "constraints": "{}",
        "editable": True,
        "description": "Update desc keyboard layout type",
        "name": "KeyboardLayout",
        "value": "Spanish",
        "type": "string"
    }],
    "goldenImageURI": "ESXi_60",
    "oeBuildPlanURI": "BP-Single-buildStep-Multi-CA",
    "category": "oe-deployment-plans",
    "description": "Update Deploymentplan- Change In CA",
    "name": "Update DP- Change In CA"
}, {
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
    "goldenImageURI": "ESXi_60_1",
    "oeBuildPlanURI": "BP-Single-buildStep-Multi-CA",
    "category": "oe-deployment-plans",
    "description": "Update Deploymentplan- Change In GI",
    "name": "Update DP- Change In GI"
}, {
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
    "goldenImageURI": "ESXi_60",
    "oeBuildPlanURI": "BP-Single-buildStep-Multi-CA-1",
    "category": "oe-deployment-plans",
    "description": "Update Deploymentplan- Change In BP",
    "name": "Update DP- Change In BP"
}]


deploymentplan_delete = [{
    'name': 'Valid DP having name containing 255 characters thnamelengnamenamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthname'
}, {
    'name': 'Valid Name Desc CA and BP but blank GI'
}, {
    'name': 'Update DP- Change in Name'
}, {
    'name': 'Update DP- Change in Name and Description'
}, {
    'name': 'Update DP- Change In CA'
}, {
    'name': 'Update DP- Change In GI'
}, {
    'name': 'Update DP- Change In BP'
}, {
    'name': 'DP having multiple CA and all CA are not editable'
}, {
    'name': 'DP having multiple CA and some of the CA visible set to True'
}, {
    'name': 'DP having multiple CA and all CA visible set to True'
}, {
    'name': 'DP having multiple CA and hpProvided set to True'
}, {
    'name': 'CL RHEL API_GET'
}, {
    'name': 'cl artifact_for_GET'
}, {
    'name': 'RHEL-7.2-deploymentplan'
}, {
    'name': '123_deploymentplan'
}, {
    'name': 'deploymentplan_456'
}]


deploymentplan_get = [{
    'name': 'Valid DP with Multiple CA'
}, {
    'goldenImageURI': 'ESXi_60'
}, {
    'oeBuildPlanURI': 'BP-Single-buildStep-Multi-CA'
}, {
    'description': 'Deployment Plan with all the valid fields and having only one custom attribute'
}, {
    'name': 'Valid DP with multiple CA for Update test- Change in Name'
}, {
    'name': 'Valid DP with multiple CA for Update test- Change in Name and Description'
}, {
    'name': 'Valid DP with Single CA'
}, {
    'name': 'Valid DP having description field containing 1000 characters'
}, {
    'name': 'DP having multiple CA and hpProvided set to True'
}, {
    'name': 'Non-existing DP'
}]

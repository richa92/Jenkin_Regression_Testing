
from requests.api import patch

admin_credentials = {'userName': 'Administrator',
                     'password': 'admin123'}

buildplan_get = [{'name': 'BP2-Create'},
                 {'name': 'bpp2create'}]

buildplan_update = [
    {
        'type': 'OeBuildPlan',
        'customAttributes': [{
            "constraints": "{\"ipv4static\":true,\"ipv4dhcp\":false,\"parameters\":[\"dns1\",\"dns2\",\"gateway\",\"ipaddress\",\"mac\",\"netmask\"]}",
            "description": "",
            "name": "MgmtNIC",
            "value": "",
            "type": "nic"
        }, 
            {
            'constraints': '{}',
            'description': '',
            'name': 'hostname',
            'value': 'Update',
            'type': 'string'},
            {
            'constraints': '{}',
            'description': '',
            'name': 'DomainName',
            'value': 'vse.rdlabs.com',
            'type': 'string'}],
        'buildStep': [{'planScriptUri': 'PS1', 'parameters': None, 'serialNumber': '1'},
                      {'planScriptUri': 'PS-Deploy',
                          'parameters': None, 'serialNumber': '2'},
                      {'planScriptUri': 'PS3', 'parameters': None, 'serialNumber': '3'}],
        'description': 'Deploy update test-Create BP with type Deploy-edited',
        'name': 'BP2-Create-edited'},
    {
        'type': 'OeBuildPlan',
        'dependentArtifacts': None,
        'customAttributes': [],
        'buildStep': [{'planScriptUri': 'PS1', 'parameters': None, 'serialNumber': '1'},
                      {'planScriptUri': 'PS-Deploy',
                          'parameters': None, 'serialNumber': '2'},
                      {'planScriptUri': 'PS3', 'parameters': None, 'serialNumber': '3'}],
        'hpProvided': False,
        'oeBuildPlanType': 'capture',
        'description': 'Deploy update test-Create BP with type Deploy-edited',
        'name': 'BP28-Create'}]

buildplan_create = [
    # 0
    {
        'type': 'OeBuildPlan',
        'customAttributes': [{
            "constraints": "{\"ipv4static\":true,\"ipv4dhcp\":false,\"parameters\":[\"dns1\",\"dns2\",\"gateway\",\"ipaddress\",\"mac\",\"netmask\"]}",
            "description": "",
            "name": "MgmtNIC",
            "value": "",
            "type": "nic"
        }, {
            'constraints': '{}',
            'description': '',
            'name': 'hostname',
            'value': 'BP2-Create',
            'type': 'integer'
        }, {
            'constraints': '{}',
            'description': '',
            'name': 'DomainName',
            'value': 'vse.rdlabs.hpecorp.net',
            'type': 'string'
        }],
        'buildStep': [{'planScriptUri': 'PS1', 'parameters': None, 'serialNumber': '1'},
                      {'planScriptUri': 'PS1A',
                          'parameters': None, 'serialNumber': '2'},
                      {'planScriptUri': 'PS-Deploy',
                          'parameters': None, 'serialNumber': '3'},
                      {'planScriptUri': 'PS3A',
                          'parameters': None, 'serialNumber': '4'},
                      {'planScriptUri': 'PS3', 'parameters': None, 'serialNumber': '5'}],
        'hpProvided': False,
        'oeBuildPlanType': 'deploy',
        'description': 'Create BP with BLANK Name',
        'name': ''},
    # 1
    {
        'type': 'OeBuildPlan',
        'customAttributes': [{
            "constraints": "{\"ipv4static\":true,\"ipv4dhcp\":false,\"parameters\":[\"dns1\",\"dns2\",\"gateway\",\"ipaddress\",\"mac\",\"netmask\"]}",
            "description": "",
            "name": "ManagementNIC3",
            "value": "",
            "type": "nic"
        }, {
            'constraints': '{}',
            'description': '',
            'name': 'hostname',
            'value': 'BP1-Create',
            'type': 'string'
        }, {
            'constraints': '{}',
            'description': '',
            'name': 'DomainName',
            'value': 'vse.rdlabs.hpecorp.net',
            'type': 'string'
        }],
        'buildStep': [{'planScriptUri': 'PS-Deploy', 'parameters': None, 'serialNumber': '1'},
                      {'planScriptUri': 'PS-Deploy',
                          'parameters': None, 'serialNumber': '2'},
                      {'planScriptUri': 'PS-Deploy', 'parameters': None, 'serialNumber': '3'}],
        'hpProvided': False,
        'oeBuildPlanType': 'deploy',
        'description': 'Build Plan of type Deploy having multiple Plan Scripts. Contents of all the PS are the same',
        'name': 'BP1-Create'},
    # 2
    {
        'type': 'OeBuildPlanV5',
	'dependentArtifacts': None,
        'customAttributes': [{
			"constraints": "{\"ipv4static\":true,\"ipv4dhcp\":false,\"ipv4disable\":false,\"parameters\":[\"dns1\",\"dns2\",\"gateway\",\"ipaddress\",\"mac\",\"netmask\",\"vlanid\"]}",
            "description": "",
            "name": "MgmtNIC",
            "value": "",
            "type": "nic"
        },{
            'constraints': '{}',
            'description': '',
            'name': 'Hostname',
            'value': 'Update',
            'type': 'string'
        }, {
            'constraints': '{}',
            'description': '',
            'name': 'DomainName',
            'value': 'vse.rdlabs.com',
            'type': 'string'
        }],
        'buildStep': [{'planScriptUri': 'PS1', 'parameters': None, 'serialNumber': '1'},
                      {'planScriptUri': 'PS1A',
                          'parameters': None, 'serialNumber': '2'},
                      {'planScriptUri': 'PS-Deploy',
                          'parameters': None, 'serialNumber': '3'},
                      {'planScriptUri': 'PS3A',
                          'parameters': None, 'serialNumber': '4'},
                      {'planScriptUri': 'PS3', 'parameters': None, 'serialNumber': '5'}],
        'hpProvided': False,
        'oeBuildPlanType': 'deploy',
        'description': 'Create BP with type Deploy',
	'category': 'oe-build-plans',
        'name': 'BP2-Create'},
    # 3
    {
        'type': 'OeBuildPlan',
        'customAttributes': [{
            "constraints": "{\"ipv4static\":true,\"ipv4dhcp\":false,\"parameters\":[\"dns1\",\"dns2\",\"gateway\",\"ipaddress\",\"mac\",\"netmask\"]}",
            "description": "",
            "name": "MgmtNIC",
            "value": "",
            "type": "nic"
        }, {
            'constraints': '{}',
            'description': '',
            'name': 'hostname',
            'value': 'BP2-Create',
            'type': 'integer'
        }, {
            'constraints': '{}',
            'description': '',
            'name': 'DomainName',
            'value': 'vse.rdlabs.hpecorp.net',
            'type': 'string'
        }],
        'buildStep': [{'planScriptUri': 'PS1', 'parameters': None, 'serialNumber': '1'},
                      {'planScriptUri': 'PS1A',
                          'parameters': None, 'serialNumber': '2'},
                      {'planScriptUri': 'PS-Deploy',
                          'parameters': None, 'serialNumber': '3'},
                      {'planScriptUri': 'PS3A',
                          'parameters': None, 'serialNumber': '4'},
                      {'planScriptUri': 'PS3', 'parameters': None, 'serialNumber': '5'}],
        'hpProvided': False,
        'oeBuildPlanType': 'capture',
        'description': 'Create BP with type capture using deploy scripts',
        'name': 'BP3-Create'},
    # 4
    {
        'type': 'OeBuildPlanV5',
        'dependentArtifacts': None,
        'customAttributes': [],
        'buildStep': [{'planScriptUri': 'PS1', 'parameters': None, 'serialNumber': '1'},
                      {'planScriptUri': 'PS-Capture',
                          'parameters': None, 'serialNumber': '2'},
                      {'planScriptUri': 'PS3', 'parameters': None, 'serialNumber': '3'}],
        'hpProvided': False,
        'oeBuildPlanType': 'capture',
        'description': 'Create Build Plan with type capture',
        'name': 'BP4-Create'},
    # 5
    {
        'type': 'OeBuildPlan',
        'customAttributes': [{
            "constraints": "{\"ipv4static\":true,\"ipv4dhcp\":false,\"parameters\":[\"dns1\",\"dns2\",\"gateway\",\"ipaddress\",\"mac\",\"netmask\"]}",
            "description": "",
            "name": "MgmtNIC",
            "value": "",
            "type": "nic"
        }, {
            'constraints': '{}',
            'description': '',
            'name': 'hostname',
            'value': 'BP2-Create',
            'type': 'integer'
        }, {
            'constraints': '{}',
            'description': '',
            'name': 'DomainName',
            'value': 'vse.rdlabs.hpecorp.net',
            'type': 'string'
        }],
        'buildStep': [{'planScriptUri': 'PS1', 'parameters': None, 'serialNumber': '1'},
                      {'planScriptUri': 'PS1A',
                          'parameters': None, 'serialNumber': '2'},
                      {'planScriptUri': 'PS-Deploy',
                          'parameters': None, 'serialNumber': '3'},
                      {'planScriptUri': 'PS3A',
                          'parameters': None, 'serialNumber': '4'},
                      {'planScriptUri': 'PS3', 'parameters': None, 'serialNumber': '5'}],
        'hpProvided': False,
        'oeBuildPlanType': 'deploy',
        'description': 'Create BP with DUPLICATE Name',
        'name': 'BP2-Create'},
    # 6
    {
        'type': 'OeBuildPlan',
        'customAttributes': [{
            "constraints": "{\"ipv4static\":true,\"ipv4dhcp\":false,\"parameters\":[\"dns1\",\"dns2\",\"gateway\",\"ipaddress\",\"mac\",\"netmask\"]}",
            "description": "",
            "name": "MgmtNIC",
            "value": "",
            "type": "nic"
        }, {
            'constraints': '{}',
            'description': '',
            'name': 'hostname',
            'value': 'BP2-Create',
            'type': 'integer'
        }, {
            'constraints': '{}',
            'description': '',
            'name': 'DomainName',
            'value': 'vse.rdlabs.hpecorp.net',
            'type': 'string'
        }],
        'buildStep': [{'planScriptUri': 'PS1', 'parameters': None, 'serialNumber': '1'},
                      {'planScriptUri': 'PS1A',
                          'parameters': None, 'serialNumber': '2'},
                      {'planScriptUri': 'PS-Deploy',
                          'parameters': None, 'serialNumber': '3'},
                      {'planScriptUri': 'PS3A',
                          'parameters': None, 'serialNumber': '4'},
                      {'planScriptUri': 'PS3', 'parameters': None, 'serialNumber': '5'}],
        'hpProvided': False,
        'oeBuildPlanType': 'deploy',
        'description': 'Create BP with INVALID Name',
        'name': 'BP6-Create-=&#!@%'},
    # 7
    {
        'type': 'OeBuildPlanV5',
        'customAttributes': [],
        'buildStep': [{'planScriptUri': 'PS1', 'parameters': None, 'serialNumber': '1'},
                      {'planScriptUri': 'PS3', 'parameters': None, 'serialNumber': '3'}],
        'hpProvided': False,
        'oeBuildPlanType': 'deploy',
        'description': 'Create BP without CA',
        'name': 'BP7-Create'},
    # 8
    {
        'type': 'OeBuildPlan',
        'customAttributes': [{
            'constraints': '{}',
            'description': '',
            'name': 'hostname',
            'value': 'BP5-Create',
            'type': 'string'
        }],
        'buildStep': [],
        'hpProvided': False,
        'oeBuildPlanType': 'deploy',
        'description': 'Create BP without Build Steps',
        'name': 'BP8-Create'},
    # 9
    {
        'type': 'OeBuildPlan',
        'dependentArtifacts': None,
        'customAttributes': [{
            "constraints": "{\"ipv4static\":true,\"ipv4dhcp\":false,\"parameters\":[\"dns1\",\"dns2\",\"gateway\",\"ipaddress\",\"mac\",\"netmask\"]}",
            "description": "",
            "name": "MgmtNIC",
            "value": "",
            "type": "nic"
        }, {
            'constraints': '{}',
            'description': '',
            'name': 'hostname',
            'value': 'BP2-Create',
            'type': 'integer'
        }, {
            'constraints': '{}',
            'description': '',
            'name': 'DomainName',
            'value': 'vse.rdlabs.hpecorp.net',
            'type': 'string'
        }],
        'buildStep': [{'planScriptUri': 'PS1', 'parameters': None, 'serialNumber': '1'},
                      {'planScriptUri': 'PS1A',
                          'parameters': None, 'serialNumber': '2'},
                      {'planScriptUri': 'PS-Deploy',
                          'parameters': None, 'serialNumber': '3'},
                      {'planScriptUri': 'PS3A',
                          'parameters': None, 'serialNumber': '4'},
                      {'planScriptUri': 'PS3', 'parameters': None, 'serialNumber': '5'}],
        'hpProvided': False,
        'oeBuildPlanType': 'Capture',
        'description': 'Create Capture Build Plan using Deploy script',
        'name': 'BP9-Create'},
    # 10
    {
        'type': 'OeBuildPlanV5',
        'dependentArtifacts': None,
        'customAttributes': [],
        'buildStep': [{'planScriptUri': 'PS1', 'parameters': None, 'serialNumber': '1'},
                      {'planScriptUri': 'PS-Capture',
                          'parameters': None, 'serialNumber': '2'},
                      {'planScriptUri': 'PS3', 'parameters': None, 'serialNumber': '3'}],
        'hpProvided': False,
        'oeBuildPlanType': 'capture',
        'description': 'Create Build Plan with type capture without CA',
        'name': 'BP10-Create'},
    # 11
    {
        'type': 'OeBuildPlan',
        'dependentArtifacts': None,
        'customAttributes': [{
            'constraints': '{}',
            'description': '',
            'name': 'hostname',
            'value': 'BP5-Create',
            'type': 'string'
        }],
        'buildStep': [],
        'hpProvided': False,
        'oeBuildPlanType': 'capture',
        'description': 'Create Build Plan without build step with type capture',
        'name': 'BP11-Create'},
    # 12
    {
        'type': 'OeBuildPlan',
        'customAttributes': [{
            "constraints": "{\"ipv4static\":true,\"ipv4dhcp\":false,\"parameters\":[\"dns1\",\"dns2\",\"gateway\",\"ipaddress\",\"mac\",\"netmask\"]}",
            "description": "",
            "name": "MgmtNIC",
            "value": "",
            "type": "nic"
        }, {
            'constraints': '{}',
            'description': '',
            'name': 'hostname',
            'value': 'BP2-Create',
            'type': 'integer'
        }, {
            'constraints': '{}',
            'description': '',
            'name': 'DomainName',
            'value': 'vse.rdlabs.hpecorp.net',
            'type': 'string'
        }],
        'buildStep': [{'planScriptUri': 'PS1', 'parameters': None, 'serialNumber': '1'},
                      {'planScriptUri': 'PS1A',
                          'parameters': None, 'serialNumber': '2'},
                      {'planScriptUri': 'PS-Deploy',
                          'parameters': None, 'serialNumber': '3'},
                      {'planScriptUri': 'PS3A',
                          'parameters': None, 'serialNumber': '4'},
                      {'planScriptUri': 'PS3', 'parameters': None, 'serialNumber': '5'}],
        'hpProvided': 'xyz',
        'oeBuildPlanType': 'deploy',
        'description': 'Create BP with type Deploy and Invalid HP-Provided',
        'name': 'BP12-Create'},
    # 13
    {
        'type': 'OeBuildPlan',
        'osType': 'esxi',
        'customAttributes': [{
            "constraints": "{\"ipv4static\":true,\"ipv4dhcp\":false,\"parameters\":[\"dns1\",\"dns2\",\"gateway\",\"ipaddress\",\"mac\",\"netmask\"]}",
            "description": "",
            "name": "MgmtNIC",
            "value": "",
            "type": "nic"
        }, {
            'constraints': '{}',
            'description': '',
            'name': 'hostname',
            'value': 'BP2-Create',
            'type': 'integer'
        }, {
            'constraints': '{}',
            'description': '',
            'name': 'DomainName',
            'value': 'vse.rdlabs.hpecorp.net',
            'type': 'string'
        }],
        'buildStep': [{'planScriptUri': 'PS1', 'parameters': None, 'serialNumber': '1'},
                      {'planScriptUri': 'PS1A',
                          'parameters': None, 'serialNumber': '2'},
                      {'planScriptUri': 'PS-Deploy',
                          'parameters': None, 'serialNumber': '3'},
                      {'planScriptUri': 'PS3A',
                          'parameters': None, 'serialNumber': '4'},
                      {'planScriptUri': 'PS3', 'parameters': None, 'serialNumber': '5'}],
        'hpProvided': False,
        'oeBuildPlanType': 'deploy',
        'description': 'Create BP with type Deploy and with invalid data osType',
        'name': 'BP13-Create'},
    # 14
    {
        'type': 'OeBuildPlan',
        'customAttributes': [{
            "constraints": "{\"ipv4static\":true,\"ipv4dhcp\":false,\"parameters\":[\"dns1\",\"dns2\",\"gateway\",\"ipaddress\",\"mac\",\"netmask\"]}",
            "description": "",
            "name": "MgmtNIC",
            "value": "",
            "type": "nic"
        }, {
            'constraints': '{}',
            'description': '',
            'name': 'hostname',
            'value': 'BP2-Create',
            'type': 'integer'
        }, {
            'constraints': '{}',
            'description': '',
            'name': 'DomainName',
            'value': 'vse.rdlabs.hpecorp.net',
            'type': 'string'
        }],
        'buildStep': [{'planScriptUri': 'PS1', 'parameters': None, 'serialNumber': '1'},
                      {'planScriptUri': 'PS1A',
                          'parameters': None, 'serialNumber': '2'},
                      {'planScriptUri': 'PS-Deploy',
                          'parameters': None, 'serialNumber': '3'},
                      {'planScriptUri': 'PS3A',
                          'parameters': None, 'serialNumber': '4'},
                      {'planScriptUri': 'PS3', 'parameters': None, 'serialNumber': '5'}],
        'hpProvided': False,
        'oeBuildPlanType': 'xyz',
        'description': 'Create BP with with invalid data for oeBuildPlanType type field',
        'name': 'BP14-Create'},
    # 15
    {
        'type': 'OeBuildPlan',
        'customAttributes': [{
            "constraints": "{\"ipv4static\":true,\"ipv4dhcp\":false,\"parameters\":[\"dns1\",\"dns2\",\"gateway\",\"ipaddress\",\"mac\",\"netmask\"]}",
            "description": "",
            "name": "MgmtNIC",
            "value": "",
            "type": "nic"
        }, {
            'constraints': '{}',
            'description': '',
            'name': 'hostname',
            'value': 'BP2-Create',
            'type': 'integer'
        }, {
            'constraints': '{}',
            'description': '',
            'name': 'DomainName',
            'value': 'vse.rdlabs.hpecorp.net',
            'type': 'string'
        }],
        'buildStep': [{'planScriptUri': 'PS1', 'parameters': None, 'serialNumber': '1'},
                      {'planScriptUri': 'PS1A',
                          'parameters': None, 'serialNumber': '2'},
                      {'planScriptUri': 'PS-Deploy',
                          'parameters': None, 'serialNumber': '3'},
                      {'planScriptUri': 'PS3A',
                          'parameters': None, 'serialNumber': '4'},
                      {'planScriptUri': 'PS3', 'parameters': None, 'serialNumber': '5'}],
        'description': 'Create BP with some missing fields',
        'name': 'BP15-Create'},
    # 16
    {
        'type': 'OeBuildPlanV5',
        'customAttributes': [],
        'buildStep': [],
        'hpProvided': False,
        'oeBuildPlanType': 'deploy',
        'description': 'Create BP with type Deploy and with name field of length 255 characters',
        'name': 'Createnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengt'
    },
    # 17
    {
        'type': 'OeBuildPlan',
        'customAttributes': [],
        'buildStep': [],
        'hpProvided': False,
        'oeBuildPlanType': 'deploy',
        'description': 'Create BP with type Deploy and with name field of length more than 255 characters',
        'name': 'BP-Create-Createnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamel'},
    # 18
    {
        'type': 'OeBuildPlanV5',
        'customAttributes': [],
        'buildStep': [],
        'hpProvided': False,
        'oeBuildPlanType': 'deploy',
        'description': 'namelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelength',
        'name': 'BP18-Create'},
    # 19
    {
        'type': 'OeBuildPlan',
        'customAttributes': [{
            "constraints": "{\"ipv4static\":true,\"ipv4dhcp\":false,\"parameters\":[\"dns1\",\"dns2\",\"gateway\",\"ipaddress\",\"mac\",\"netmask\"]}",
            "description": "",
            "name": "MgmtNIC",
            "value": "",
            "type": "nic"
        }, {
            'constraints': '{}',
            'description': '',
            'name': 'hostname',
            'value': 'BP2-Create',
            'type': 'integer'
        }, {
            'constraints': '{}',
            'description': '',
            'name': 'DomainName',
            'value': 'vse.rdlabs.hpecorp.net',
            'type': 'string'
        }],
        'buildStep': [{'planScriptUri': 'PS1', 'parameters': None, 'serialNumber': '1'},
                      {'planScriptUri': 'PS1A',
                          'parameters': None, 'serialNumber': '2'},
                      {'planScriptUri': 'PS-Deploy',
                          'parameters': None, 'serialNumber': '3'},
                      {'planScriptUri': 'PS3A',
                          'parameters': None, 'serialNumber': '4'},
                      {'planScriptUri': 'PS3', 'parameters': None, 'serialNumber': '5'}],
        'hpProvided': False,
        'oeBuildPlanType': 'deploy',
        'description': 'BP-Create-namelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelength',
        'name': 'BP19-Create'},
    # 20
    {
        'type': 'OeBuildPlanV5',
        'customAttributes': [{
            "constraints": "{\"ipv4static\":true,\"ipv4dhcp\":false,\"parameters\":[\"dns1\",\"dns2\",\"gateway\",\"ipaddress\",\"mac\",\"netmask\"]}",
            "description": "",
            "name": "MgmtNIC",
            "value": "",
            "type": "nic"
        },
            {
            "constraints": "{}",
            "description": "",
            "name": "DomainName",
            "value": "vse.rdlabs.hpecorp.net",
            "type": "string"
        },
            {
            "constraints": "{}",
            "description": "",
            "name": "Hostname",
            "value": "BP2-Create",
            "type": "string"
        }],
        'buildStep': [{'planScriptUri': 'PS-Deploy', 'parameters': None, 'serialNumber': '3'}],
        'hpProvided': False,
        'oeBuildPlanType': 'deploy',
        'description': 'Create Build Plan with single Build step of OSBP type Deploy',
        'name': 'BP20-Create'},
    # 21
    {
        'type': 'OeBuildPlanV5',
        'dependentArtifacts': None,
        'customAttributes': [],
        'buildStep': [{'planScriptUri': 'PS-Capture', 'parameters': None, 'serialNumber': '1'}],
        'hpProvided': False,
        'oeBuildPlanType': 'capture',
        'description': 'Create BP with type Capture and with only single build step',
        'name': 'BP21-Create'},
    # 22
    {
        'type': 'OeBuildPlanV5',
        'customAttributes': [{
            "constraints": "{\"ipv4static\":true,\"ipv4dhcp\":false,\"parameters\":[\"dns1\",\"dns2\",\"gateway\",\"ipaddress\",\"mac\",\"netmask\"]}",
            "description": "",
            "name": "MgmtNIC",
            "value": "",
            "type": "nic"
        }, {
            'constraints': '{}',
            'description': '',
            'name': 'hostname',
            'value': 'BP2-Create',
            'type': 'string'
        }, {
            'constraints': '{}',
            'description': '',
            'name': 'DomainName',
            'value': 'vse.rdlabs.hpecorp.net',
            'type': 'string'
        }],
        'buildStep': [{'planScriptUri': 'PS-Capture', 'parameters': None, 'serialNumber': '1'},
                      {'planScriptUri': 'PS-Deploy', 'parameters': None, 'serialNumber': '2'}],
        'hpProvided': False,
        'oeBuildPlanType': 'deploy',
        'description': 'Create BP with multiple Build Steps with different PS type',
        'name': 'BP22-Create'},
    # 23
    {
        'type': 'OeBuildPlan',
        'customAttributes': [{
            "constraints": "{\"ipv4static\":true,\"ipv4dhcp\":false,\"parameters\":[\"dns1\",\"dns2\",\"gateway\",\"ipaddress\",\"mac\",\"netmask\"]}",
            "description": "",
            "name": "MgmtNIC",
            "value": "",
            "type": "nic"
        }, {
            'constraints': '{}',
            'description': '',
            'name': 'hostname',
            'value': 'BP2-Create',
            'type': 'integer'
        }, {
            'constraints': '{}',
            'description': '',
            'name': 'DomainName',
            'value': 'vse.rdlabs.hpecorp.net',
            'type': 'string'
        }],
        'buildStep': [{'planScriptUri': 'PS1', 'parameters': None, 'serialNumber': '1'},
                      {'planScriptUri': 'PS1A',
                          'parameters': None, 'serialNumber': '1'},
                      {'planScriptUri': 'PS-Deploy',
                          'parameters': None, 'serialNumber': '1'},
                      {'planScriptUri': 'PS3A',
                          'parameters': None, 'serialNumber': '1'},
                      {'planScriptUri': 'PS3', 'parameters': None, 'serialNumber': '1'}],
        'hpProvided': False,
        'oeBuildPlanType': 'deploy',
        'description': 'Create BP with multiple Build Steps having same serial number in Build Step',
        'name': 'BP23-Create'},
    # 24
    {
        'type': 'OeBuildPlan',
        'customAttributes': [{
            "constraints": "{\"ipv4static\":true,\"ipv4dhcp\":false,\"parameters\":[\"dns1\",\"dns2\",\"gateway\",\"ipaddress\",\"mac\",\"netmask\"]}",
            "description": "",
            "name": "MgmtNIC",
            "value": "",
            "type": "nic"
        }, {
            'constraints': '{}',
            'description': '',
            'name': 'hostname',
            'value': 'BP2-Create',
            'type': 'integer'
        }, {
            'constraints': '{}',
            'description': '',
            'name': 'DomainName',
            'value': 'vse.rdlabs.hpecorp.net',
            'type': 'string'
        }],
        'buildStep': [{'planScriptUri': 'PS1', 'parameters': None, 'serialNumber': '-1'},
                      {'planScriptUri': 'PS1A', 'parameters': None,
                          'serialNumber': '-2'},
                      {'planScriptUri': 'PS-Deploy',
                          'parameters': None, 'serialNumber': '-3'},
                      {'planScriptUri': 'PS3A', 'parameters': None,
                          'serialNumber': '-4'},
                      {'planScriptUri': 'PS3', 'parameters': None, 'serialNumber': '-5'}],
        'hpProvided': False,
        'oeBuildPlanType': 'deploy',
        'description': 'Create BP with multiple Build Steps having negative serial number in Build Step',
        'name': 'BP24-Create'},
    # 25
    {
        'type': 'OeBuildPlan',
        'customAttributes': [{
            'constraints': '{}',
            'description': '',
            'name': 'KeyboardLayout',
            'value': 'English',
            'type': 'string'
        }, {
            'constraints': '{}',
            'description': '',
            'name': 'hostname',
            'value': 'BP2-Create',
            'type': 'string'
        }, {
            'constraints': '{}',
            'description': '',
            'name': 'DomainName',
            'value': 'vse.rdlabs.hpecorp.net',
            'type': 'string'
        }, {
            'constraints': '{}',
            'description': '',
            'name': 'Gateway',
            'value': '192.168.0.1',
            'type': 'string'}],
        'buildStep': [{'planScriptUri': 'PS1', 'parameters': None, 'serialNumber': '1'},
                      {'planScriptUri': 'PS1A',
                          'parameters': None, 'serialNumber': '2'},
                      {'planScriptUri': 'PS-Deploy',
                          'parameters': None, 'serialNumber': '3'},
                      {'planScriptUri': 'PS3A',
                          'parameters': None, 'serialNumber': '4'},
                      {'planScriptUri': 'PS3', 'parameters': None, 'serialNumber': '5'}],
        'hpProvided': False,
        'oeBuildPlanType': 'deploy',
        'description': 'Create BP with type Deploy where one of the Custom Attributes not in Plan Script',
        'name': 'BP25-Create'},
    # 26
    {
        'type': 'OeBuildPlan',
        'customAttributes': [{
            'constraints': '{}',
            'description': '',
            'name': 'hostname',
            'value': 'BP26-Create',
            'type': 'string'
        }, {
            'constraints': '{}',
            'description': '',
            'name': 'hostname',
            'value': 'BP26-Create',
            'type': 'string'
        }, {
            'constraints': '{}',
            'description': '',
            'name': 'hostname',
            'value': 'BP26-Create',
            'type': 'string'
        }],
        'buildStep': [{'planScriptUri': 'PS1', 'parameters': None, 'serialNumber': '1'},
                      {'planScriptUri': 'PS1A',
                          'parameters': None, 'serialNumber': '2'},
                      {'planScriptUri': 'PS-Deploy',
                          'parameters': None, 'serialNumber': '3'},
                      {'planScriptUri': 'PS3A',
                          'parameters': None, 'serialNumber': '4'},
                      {'planScriptUri': 'PS3', 'parameters': None, 'serialNumber': '5'}],
        'hpProvided': False,
        'oeBuildPlanType': 'deploy',
        'description': 'Create BP with Custom Attributes and all with same data',
        'name': 'BP26-Create'},
    # 27
    {
        'type': 'OeBuildPlan',
        'customAttributes': [{
            "constraints": "{\"ipv4static\":true,\"ipv4dhcp\":false,\"parameters\":[\"dns1\",\"dns2\",\"gateway\",\"ipaddress\",\"mac\",\"netmask\"]}",
            "description": "",
            "name": "MgmtNIC",
            "value": "",
            "type": "nic"
        }, {
            'constraints': '{}',
            'description': '',
            'name': 'hostname',
            'value': 'BP2-Create',
            'type': 'integer'
        }, {
            'constraints': '{}',
            'description': '',
            'name': 'DomainName',
            'value': 'vse.rdlabs.hpecorp.net',
            'type': 'string'
        }],
        'buildStep': [{'planScriptUri': 'PS1', 'parameters': None, 'serialNumber': '1'},
                      {'planScriptUri': 'PS1A',
                          'parameters': None, 'serialNumber': '2'},
                      {'planScriptUri': 'PS-Deploy',
                          'parameters': None, 'serialNumber': '3'},
                      {'planScriptUri': 'PS3A',
                          'parameters': None, 'serialNumber': '4'},
                      {'planScriptUri': 'PS3', 'parameters': None, 'serialNumber': '5'}],
        'hpProvided': False,
        'oeBuildPlanType': 'deploy',
        'description': 'Create BP with invalid CA type',
        'name': 'BP27-Create'},
    # 28
    {
        'type': 'OeBuildPlanV5',
        'customAttributes': [{
            "constraints": "{\"ipv4static\":true,\"ipv4dhcp\":false,\"parameters\":[\"dns1\",\"dns2\",\"gateway\",\"ipaddress\",\"mac\",\"netmask\"]}",
            "description": "",
            "name": "MgmtNIC",
            "value": "",
            "type": "nic"
        },
            {
            "constraints": "{}",
            "description": "",
            "name": "DomainName",
            "value": "vse.rdlabs.hpecorp.net",
            "type": "string"
        },
            {
            "constraints": "{}",
            "description": "",
            "name": "Hostname",
            "value": "BP2-Create",
            "type": "string"
        }],
        'buildStep': [{'planScriptUri': 'PS1', 'parameters': None, 'serialNumber': '1'},
                      {'planScriptUri': 'PS1A',
                          'parameters': None, 'serialNumber': '2'},
                      {'planScriptUri': 'PS-Deploy',
                          'parameters': None, 'serialNumber': '3'},
                      {'planScriptUri': 'PS3A',
                          'parameters': None, 'serialNumber': '4'},
                      {'planScriptUri': 'PS3', 'parameters': None, 'serialNumber': '5'}],
        'hpProvided': False,
        'oeBuildPlanType': 'deploy',
        'description': 'Create BP with type Deploy for update test',
        'name': 'BP28-Create'},
    # 29
    {
        'type': 'OeBuildPlanV5',
        'customAttributes': [],
        'buildStep': [],
        'hpProvided': False,
        'oeBuildPlanType': 'deploy',
        'description': 'valid buildplan1 for get call',
        'name': 'CL RHEL API_GET'},
    # 30
    {
        'type': 'OeBuildPlanV5',
        'customAttributes': [],
        'buildStep': [],
        'hpProvided': False,
        'oeBuildPlanType': 'deploy',
        'description': 'valid buildplan2 for get call',
        'name': 'cl artifact_for_GET'},
    # 31
    {
        'type': 'OeBuildPlanV5',
        'customAttributes': [],
        'buildStep': [],
        'hpProvided': False,
        'oeBuildPlanType': 'deploy',
        'description': 'valid buildplan3 for get call',
        'name': 'RHEL-7.2-buildplan'},
    # 32
    {
        'type': 'OeBuildPlanV5',
        'customAttributes': [],
        'buildStep': [],
        'hpProvided': False,
        'oeBuildPlanType': 'deploy',
        'description': 'valid buildplan4 for get call',
        'name': '123_buildplan'},
    # 33
    {
        'type': 'OeBuildPlanV5',
        'customAttributes': [],
        'buildStep': [],
        'hpProvided': False,
        'oeBuildPlanType': 'deploy',
        'description': 'valid buildplan5 for get call',
        'name': 'buildplan_456'}
]

buildplan_del = [{'name': 'BP2-Create'},
                 {'name': 'BP10-Create'},
                 {'name': 'BP4-Create'},
                 {'name': 'BP7-Create'},
                 {'name': 'Createnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengt'},                
                 {'name': 'BP21-Create'},
                 {'name': 'CL RHEL API_GET'},
                 {'name': 'cl artifact_for_GET'},
                 {'name': 'RHEL-7.2-buildplan'},
                 {'name': '123_buildplan'},
                 {'name': 'buildplan_456'},
                 {'name': 'BP20-Create'},
                 {'name': 'BP28-Create'},
                 {'name': 'BP18-Create'},
                 ]
planscript = [{
    "type": "PlanScript",
    "description": "Mount Plan Script for General- for BP automation",
    "name": "PS1",
    "hpProvided": "true",
    "planType": "general",
    "content": "# (C) Copyright 2015-2015 Hewlett-Packard Development Company, L.P.\r\n# Script to mount disk in libguesfs virtual appliance for personalizaiton or generalization\r\nmount /dev/sda5 /\r\n\r\n\r\n# creating tmp dir at local filesystem\r\n!mkdir -p ./onetime\r\n!mkdir -p ./state/local\r\n\r\n# copying required files for personalization/generalization to local filesysystem\r\n-copy-out /onetime.tgz .\r\n-copy-out /state.tgz .\r\n-copy-out /boot.cfg .\r\n\r\n# trying to findout whether onetime.tgz will be picked up during booting or state.tgz will be picked\r\n# based on that we can process either onetime.tgz or state.tgz for personalization/generalization\r\n\r\n-!grep \"onetime.tgz\"  ./boot.cfg >./onetime_found\r\n-!grep \"state.tgz\" ./boot.cfg > ./state_found"
}, {
    "type": "PlanScript",
    "description": "UnPack Plan Script for General- for BP automation",
    "name": "PS1A",
    "hpProvided": "true",
    "planType": "general",
    "content": "echo \"########################################\"\r\necho \"Copy out and unpack ESXi host state\"\r\necho \"########################################\"\r\n\r\necho \"Create ImageStreamer temp directory\"\r\n-mkdir /ImageStreamer\r\necho\r\n\r\necho \"Extract ESXi host configuration from Golden Image\"\r\necho \"Copy out boot.cfg\"\r\ndownload /boot.cfg boot.cfg\r\necho \"Copy out state.tgz if present\"\r\n-download /state.tgz state.tgz\r\necho \"Copy out onetime.tgz if present\"\r\n-download /onetime.tgz onetime.tgz\r\necho\r\n\r\necho \"Build esxi_unpack ESXi host state unpack script\"\r\nupload -<<END /ImageStreamer/esxi_unpack\r\n#! /bin/bash\r\nDIR=`pwd`\r\n\r\necho \"Finding ESXi host state configuration archive in Golden Image\"\r\nSTATE=`grep -c onetime.tgz $DIR/boot.cfg`\r\nif [ \"$STATE\" -eq \"0\" ]; then\r\n    echo\r\n    echo \"Unpack state.tgz\"\r\n    mkdir $DIR/esxi_state\r\n    cd $DIR/esxi_state\r\n    tar xvpzf $DIR/state.tgz\r\n    echo\r\n    echo \"Unpack local.tgz\"\r\n    mkdir $DIR/esxi_local\r\n    cd $DIR/esxi_local\r\n    tar xvpzf $DIR/esxi_state/local.tgz\r\n    echo\r\nelse\r\n    echo\r\n    echo \"Unpack onetime.tgz\"\r\n    mkdir $DIR/esxi_onetime\r\n    cd $DIR/esxi_onetime\r\n    tar xvpzf $DIR/onetime.tgz\r\n    echo\r\nfi\r\n\r\nif [ -e etc/rc.local.d/local.sh ]; then\r\n    cp etc/rc.local.d/local.sh $DIR/local.sh\r\nfi\r\n\r\necho \"Unpacking ESXi host state complete.\"\r\nexit 0\r\nEND\r\ndownload /ImageStreamer/esxi_unpack ./esxi_unpack\r\necho\r\n\r\necho \"Build esxi_repack ESXi host state repack script\"\r\nupload -<<END /ImageStreamer/esxi_repack\r\n#! /bin/bash\r\nDIR=`pwd`\r\n\r\necho \"---------------------------------------------------------------\"\r\necho \"Final ESXi host local.sh content for configuration at first boot:\"\r\ncat $DIR/local.sh\r\necho \"---------------------------------------------------------------\"\r\necho\r\n\r\necho \"Finding ESXi host state configuration archive\"\r\nSTATE=`grep -c onetime.tgz $DIR/boot.cfg`\r\nif [ \"$STATE\" -eq \"0\" ]; then\r\n    echo\r\n    echo \"Repack local.tgz\"\r\n    cd $DIR/esxi_local\r\n    mkdir -p etc/rc.local.d\r\n    cp $DIR/local.sh etc/rc.local.d/local.sh\r\n    chmod 777 etc/rc.local.d/local.sh\r\n    tar cvpzf $DIR/esxi_state/local.tgz *\r\n    echo\r\n    echo \"Repack state.tgz\"\r\n    cd $DIR/esxi_state\r\n    tar cvpzf $DIR/state.tgz *\r\n    echo\r\nelse\r\n    echo\r\n    echo \"Repack onetime.tgz\"\r\n    cd $DIR/esxi_onetime\r\n    mkdir -p etc/rc.local.d\r\n    cp $DIR/local.sh etc/rc.local.d/local.sh\r\n    chmod 777 etc/rc.local.d/local.sh\r\n    tar cvpzf $DIR/onetime.tgz *\r\n    touch $DIR/state.tgz\r\n    echo\r\nfi\r\necho \"Repacking ESXi host state complete.\"\r\nexit 0\r\nEND\r\ndownload /ImageStreamer/esxi_repack ./esxi_repack\r\necho\r\n\r\necho \"Run  esxi_repack ESXi host state unpack script\"\r\n!source ./esxi_unpack\r\necho"
}, {
    "type": "PlanScript",
    "description": "Plan Script for Deploy- for BP automation",
    "name": "PS-Deploy",
    "hpProvided": "true",
    "planType": "deploy",
    "content": "echo \"########################################\"\r\necho \"Configure ESXi host management network\"\r\necho \"########################################\"\r\n\r\necho \"Check Image Streamer capture details\"\r\n-download /ImageStreamerCapture ./ImageStreamerCapture\r\n\r\nupload -<<END /ImageStreamer/check_capture\r\n#!/bin/bash\r\nif [ -f ./ImageStreamerCapture ]; then\r\n    echo \"Capture details:\"\r\n    cat ./ImageStreamerCapture\r\nelse\r\n    echo\r\n    echo \"WARNING: ESXi Golden Image was not captured by Image Streamer.\"\r\n    echo \"Golden Image may not be prepared for correct personalization.\"\r\n    echo \"Recommend deploying Golden Image as is and capturing a new\"\r\n    echo \"Golden Image using Image Streamer via correct capture Build Plan\"\r\n    echo\r\nfi\r\necho\r\nEND\r\ndownload /ImageStreamer/check_capture ./check_capture\r\n!source ./check_capture\r\n\r\n-rm-f /ImageStreamerCapture\r\n\r\nupload -<<END /ImageStreamer/esxi_mgmt_net\r\n#! /bin/bash\r\n\r\ncat <<\"EOF\" >>local.sh\r\n# HPE Image Streamer ESXi host configuration\r\nesxcli system syslog mark --message \"HPE Image Streamer ESXi host configuration for @Hostname@\"\r\n\r\n# Image Streamer management network configuration\r\nesxcli system hostname set --host \"@Hostname@\"\r\nesxcli system hostname set --domain \"@DomainName@\"\r\n\r\nVMK1=vmk2\r\nUPLINK1=`esxcli network nic list | grep -i \"@MgmtNIC.mac@\" | awk '{ print $1 }'`\r\n\r\nesxcli network vswitch standard add --vswitch-name=vSwitch1\r\n\r\nesxcli network vswitch standard portgroup add --portgroup-name=ManangementNetwork1 --vswitch-name=vSwitch1\r\n\r\nesxcli network vswitch standard uplink add --uplink-name=$UPLINK1 --vswitch-name=vSwitch1\r\n\r\nesxcli network ip interface add --interface-name=$VMK1 --portgroup-name=ManangementNetwork1\r\n\r\nEOF\r\n\r\nif [[ \"@MgmtNIC.ipaddress@\" =~ [0-9]*\\.[0-9]*\\.[0-9]*\\.[0-9]* ]]; then\r\n\r\necho \"Configure ESXi host management network for static IP\"\r\ncat <<\"EOF\" >>local.sh\r\nesxcli network ip interface ipv4 set --interface-name=$VMK1 --ipv4=@MgmtNIC.ipaddress@ --netmask=@MgmtNIC.netmask@ --type=static\r\n\r\nesxcli network ip route ipv4 add --gateway \"@MgmtNIC.gateway@\" --network default\r\nesxcli network ip dns server add --server=@MgmtNIC.dns1@\r\nesxcli network ip dns server add --server=@MgmtNIC.dns2@\r\n\r\nEOF\r\n\r\nelse\r\n\r\necho \"Configure ESXi host management network for DHCP\"\r\ncat <<\"EOF\" >>local.sh\r\nesxcli network ip  interface ipv4 set --interface-name=$VMK1 --type=dhcp   \r\n\r\nEOF\r\nfi\r\n\r\nexit 0\r\nEND\r\n\r\ndownload /ImageStreamer/esxi_mgmt_net ./esxi_mgmt_net\r\necho \"Run esxi_mgmt_net\"\r\n!source ./esxi_mgmt_net\r\necho \"Configure host management complete\""
}, {
    "type": "PlanScript",
    "description": "RePack Plan Script for General- for BP automation",
    "name": "PS3A",
    "hpProvided": "true",
    "planType": "general",
    "content": "echo \"########################################\"\r\necho \"Pack and replace ESXi host state into ESXi host OS Volume\"\r\necho \"########################################\"\r\n\r\necho \"Run  esxi_repack ESXi host state repack script\"\r\n!source /esxi_repack\r\n\r\necho \"Copy in state.tgz if present\"\r\n-upload state.tgz /state.tgz \r\necho \"Copy in onetime.tgz if present\"\r\n-upload onetime.tgz /onetime.tgz\r\n\r\necho \"Remove Image Streamer temp directory\"\r\nrm-rf /tmp/ImageStreamer"
}, {
    "type": "PlanScript",
    "description": "UnMount Plan Script for General- for BP automation",
    "name": "PS3",
    "hpProvided": "true",
    "planType": "general",
    "content": "echo \"########################################\"\r\necho \"Cleanup and unmount file systems \"\r\necho \"########################################\"\r\n\r\necho \"Remove ImageStreamer temp directory\"\r\nrm-rf /ImageStreamer\r\n\r\necho \"Unmount file systems\"\r\numount /\r\necho"
}, {
    "type": "PlanScript",
    "type": "PlanScript",
    "description": "Plan Script for Capture- for BP automation",
    "name": "PS-Capture",
    "hpProvided": "true",
    "planType": "capture",
    "state": "active",
    "content": "echo \"########################################\"\r\necho \"Generalize host configuration\"\r\necho \"########################################\"\r\n\r\necho \"Empty jumpstrt.tgz archive to remove any configuration left over from install\"\r\nrm /jumpstrt.gz\r\ntouch /jumpstrt\r\ncompress-out gzip /jumpstrt /jumpstrt.gz\r\nrm /jumpstrt\r\nupload /jumpstrt.gz /jumpstrt.gz\r\n!rm /jumpstrt.gz\r\necho\r\n\r\necho \"Empty useropts.gz archive to remove special user configuration\"\r\nrm /useropts.gz\r\ntouch /useropts\r\ncompress-out gzip /useropts /useropts.gz\r\nrm /useropts\r\nupload /useropts.gz /useropts.gz\r\n!rm /useropts.gz\r\necho \r\n\r\necho \"Remove state.tgz archive which holds host configuration\"\r\nrm-f /state.tgz\r\necho \r\n\r\necho \"Download boot.cfg\"\r\ndownload /boot.cfg /boot.cfg\r\necho\r\n\r\necho \"Construct boot.cfg configuration script\"\r\nupload -<<END /boot_cfg_configure\r\n#!/bin/bash\r\n\r\necho\r\necho \"Original boot.cfg:\"\r\ncat boot.cfg\r\necho\r\n\r\ncp boot.cfg boot.cfg.bak\r\n\r\nsed '/^kernelopt=.*installerDiskDumpSlotSize=/ {\r\n         s/\\(kernelopt=\\).*\\(installerDiskDumpSlotSize=[0-9]*\\).*/\\1 \\2/; n }\r\n     /^kernelopt=/ {\r\n         s/.*/kernelopt=/ }\r\n     /^modules=/ {\r\n         s/--- state.tgz/--- onetime.tgz/ }\r\n    ' < boot.cfg.bak > boot.cfg\r\n\r\nrm boot.cfg.bak\r\n\r\necho \"New boot.cfg:\"\r\ncat boot.cfg\r\necho\r\n\r\necho \"Construct ImageStreamerCapture details file\"\r\necho \"HPE Image Streamer Capture for ESXi 5\" > /ImageStreamerCapture\r\necho \"Complete generalization by host state removal\" >> /ImageStreamerCapture\r\ndate >> /ImageStreamerCapture\r\n\r\nexit 0\r\nEND\r\necho \r\n\r\necho \"Run boot.cfg configuration script\"\r\ndownload /boot_cfg_configure /boot_cfg_configure\r\n!source /boot_cfg_configure\r\nrm-f /boot_cfg_configure\r\necho\r\n\r\necho \"Replace boot.cfg\"\r\nupload /boot.cfg /boot.cfg\r\necho\r\n\r\necho \"Save capture details in Golden Image\"\r\nupload  /ImageStreamerCapture  /ImageStreamerCapture\r\necho"
}]

planscript_delete = [{'name': 'PS1'},
                     {'name': 'PS1A'},
                     {'name': 'PS-Deploy'},
                     {'name': 'PS3'},
                     {'name': 'PS3A'},
                     {'name': 'PS-Capture'}]

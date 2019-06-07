from FusionLibrary.api.security.login_domains import LoginDomain
def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist

admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}

vcenter = {'server': 'wpstwork.vse.adapps.hp.com', 'user': 'wpst-srm', 'password': 'wpstsrm1'}

users = [{'userName': 'sarah', 'password': 'serveradmin', 'fullName': 'Sarah', 'roles': ['Server administrator'], 'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'nat', 'password': 'networkadmin', 'fullName': 'Nat', 'roles': ['Network administrator'], 'emailAddress': 'nat@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'backup', 'password': 'backupadmin', 'fullName': 'Backup', 'roles': ['Backup administrator'], 'emailAddress': 'backup@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'rheid', 'password': 'readonly', 'fullName': 'Rheid', 'roles': ['Read only'], 'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'}
         ]

ethernet_networks = [{'name': 'net_10', 'type': 'ethernet-networkV3', 'vlanId': 101, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tagged'},
                     {'name': 'net_11', 'type': 'ethernet-networkV3', 'vlanId': 101, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tagged'},
                     {'name': 'net_12', 'type': 'ethernet-networkV3', 'vlanId': 101, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tagged'}
                     ]

fcoe_networks = [{'name': 'fcoe_102', 'type': 'fcoe-network', 'vlanId': 102}]

fc_networks = [{'type': 'fc-networkV2',
                'linkStabilityTime': 30,
                'autoLoginRedistribution': True,
                'name': 'SAN-A',
                'connectionTemplateUri': None,
                'managedSanUri': None,
                'fabricType': 'FabricAttach'}]

LoginDomains = [{'name': 'wpstAD', 'newname': 'wpstAD-new',  'authProtocol': 'AD', 'directoryServerIpAddress': '16.125.77.30', 'userNamefield': 'CN', 'org':'cn=users+ou=storageUsers+ou=nwUsers,ou=networkUsers+OU=networkUsers+OU=serverUsers+ou=sUsers,ou=serverUsers', 'top':'DC=wpstAD,DC=com',  'useSsl': 'false', 'userName': 'adserver', 'password': 'Appliance@dmin123', 'directoryServerCertificateBase64Data': '-----BEGIN CERTIFICATE-----\nMIIDrjCCApagAwIBAgIQZDhBBW/8SpNHBvVM9AsnvTANBgkqhkiG9w0BAQUFADBJMRMwEQYKCZImiZPyLGQBGRYDY29tMRYwFAYKCZImiZPyLGQBGRYGd3BzdEFEMRowGAYDVQQDExF3cHN0QUQtV1BTVC1BRC1DQTAeFw0xNDAzMjAxNzA1MjRaFw0xOTAzMjAxNzE1MjNaMEkxEzARBgoJkiaJk/IsZAEZFgNjb20xFjAUBgoJkiaJk/IsZAEZFgZ3cHN0QUQxGjAYBgNVBAMTEXdwc3RBRC1XUFNULUFELUNBMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxnQCjTZuDhuYXYsXyCVZZ0Q06PODw6B/ktN2GVyFqG2fkFFJJtj0UUrythnxQoUrYm8xWN3+KrqRBqFOVvx4VcYCLPhc7Q6kxLRB9FbjVbyYISkZXoRfwpBCFzHDSSKmSymXJQwmsZ/dzsBzRQ44q8cTc3JR6yqpbJIfhpPdeWYBUUjLbxm9o4rV0xzPlkYjMQ7MLmNZir7RRuE5GrW2/6MUYvgabN9qrsbZxG/8TvMeG8AbuHv8jNFRdFv2SkUTmo0UjwRqciK2cBtlQGPoVVDy+7dMiP+VY0jmeceB8IvLP6U2+hm9BreLlcgcSlLuV+AggvQ8hmXBheHM+BH2ewIDAQABo4GRMIGOMBMGCSsGAQQBgjcUAgQGHgQAQwBBMA4GA1UdDwEB/wQEAwIBhjAPBgNVHRMBAf8EBTADAQH/MB0GA1UdDgQWBBRIO04qEVeUVikGs4nLlXBT/1HohDASBgkrBgEEAYI3FQEEBQIDAQABMCMGCSsGAQQBgjcVAgQWBBSIWKTbCPR2OQDf86oNCk1x8jPiVjANBgkqhkiG9w0BAQUFAAOCAQEAq+HyTyJMe/uQVznfyxXMIUX/RYnhkmHyanHPskfso2R3bYwqnjQi/UckyM2nr8sMpTxpvM8Gu25pjNFB4kUBt38TCZ9staiUZaGB2fKdBrK/5wrmvy9VTL7j5qUSiR7bmzy80dXvbLMZDO1+GPqdAIRj12LlUkWE8wIzK7/nxIgPlUVJgPsJgoFfv0p8N4r0v2ySWzap2arIQuVD8TBvUO4cDMzz8sO5uAiM/V2fiCj3C6V57KhapjqirbwwSVztdALJ4loca8eU1vVP7ks2zfvg78v9VV8V8OX4oHDZX7pI6eD30sqRA2dWVQShmrz3oZdOmdnyyIgvjx4NnONvBw==\n-----END CERTIFICATE-----'}
    ]

sans = [{'connectionInfo': [{'name': 'Host', 'value': '16.125.71.184'}, {'name': 'Port', 'value': '5989'}, {'name': 'Username', 'value': 'Administrator'}, {'name': 'Password', 'value':'password'},  {'name': 'useSsl', 'value': 'true'}]},
        {'connectionInfo': [{'name': 'Host', 'value': '16.125.65.2'}, {'name': 'Port', 'value': '5989'}, {'name': 'Username', 'value': 'Administrator'}, {'name': 'Password', 'value': 'password'}, {'name': 'useSsl', 'value': 'true'}]}]

storage_systems = [{'ip_hostname': 'wpst3par-7200-4-srv.vse.rdlabs.hpecorp.net', 'username': 'fusionadm', 'password': 'hpvse1'},
                   {'ip_hostname': 'wpst3par-7200-6-srv.vse.rdlabs.hpecorp.net', 'username': 'fusionadm', 'password': 'hpvse1'}]
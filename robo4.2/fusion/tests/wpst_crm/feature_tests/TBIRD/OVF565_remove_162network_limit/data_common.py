# Rack AT51 & AS51 Enclosures
ENC_1 = 'CN754406W4'
ENC_2 = 'CN7545084F'
ENC_3 = 'CN754XXXXX'
ENC_4 = 'CN754XXXXX'
ENC_5 = 'CN754XXXXX'

# DTO Types
icm_settings_type = 'EthernetInterconnectSettingsV4'

appliance_ip = '15.245.131.xxx'
admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}


def make_range_list(start, end, prefix='net_', suffix=''):
    tlist = []
    for x in xrange(start, end + 1):
        tlist.append(prefix + str(x) + suffix)
    return tlist


def rlist(start, end, prefix='net_', suffix=''):
    tlist = []
    for x in xrange(start, end + 1):
        tlist.append(prefix + str(x) + suffix)
    return tlist


users = [
    {'userName': 'Serveradmin', 'password': 'Serveradmin', 'fullName': 'Serveradmin',
     'permissions': [{'roleName': 'Server administrator'}],
     'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
     'type': 'UserAndPermissions'},
    {'userName': 'Networkadmin', 'password': 'Networkadmin', 'fullName': 'Networkadmin',
     'permissions': [{'roleName': 'Network administrator'}], 'emailAddress': 'nat@hp.com',
     'officePhone': '970-555-0003',
     'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions'},
    {'userName': 'Backupadmin', 'password': 'Backupadmin', 'fullName': 'Backupadmin',
     'permissions': [{'roleName': 'Backup administrator'}],
     'emailAddress': 'backup@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
     'type': 'UserAndPermissions'},
    {'userName': 'Noprivledge', 'password': 'Noprivledge', 'fullName': 'Noprivledge',
     'permissions': [{'roleName': 'Read only'}],
     'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
     'type': 'UserAndPermissions'}
]

ethernet_networks = [{'name': 'net_401',
                      'type': 'ethernet-networkV4',
                      'vlanId': 401,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'},
                     {'name': 'net_402',
                      'type': 'ethernet-networkV4',
                      'vlanId': 402,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'},
                     {'name': 'net_403',
                      'type': 'ethernet-networkV4',
                      'vlanId': 403,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'},
                     {'name': 'net_404',
                      'type': 'ethernet-networkV4',
                      'vlanId': 404,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'},
                     {'name': 'net_405',
                      'type': 'ethernet-networkV4',
                      'vlanId': 405,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'},
                     {'name': 'net_406',
                      'type': 'ethernet-networkV4',
                      'vlanId': 406,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'},
                     {'name': 'net_407',
                      'type': 'ethernet-networkV4',
                      'vlanId': 407,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'},
                     {'name': 'net_408',
                      'type': 'ethernet-networkV4',
                      'vlanId': 408,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'},
                     {'name': 'net_409',
                      'type': 'ethernet-networkV4',
                      'vlanId': 409,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'},
                     {'name': 'net_410',
                      'type': 'ethernet-networkV4',
                      'vlanId': 410,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'},
                     {'name': 'tunnelnetwork1',
                      'type': 'ethernet-networkV4',
                      'vlanId': None,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tunnel'},
                     {'name': 'tunnelnetwork2',
                      'type': 'ethernet-networkV4',
                      'vlanId': None,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tunnel'},
                     {'name': 'untaggednetwork1',
                      'type': 'ethernet-networkV4',
                      'vlanId': None,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Untagged'},
                     {'name': 'untaggednetwork2',
                      'type': 'ethernet-networkV4',
                      'vlanId': None,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Untagged'}
                     ]

ethernet_ranges = [
    {'prefix': 'net_', 'suffix': '', 'start': 1, 'end': 400, 'name': None, 'type': 'ethernet-networkV4',
     'vlanId': None, 'purpose': 'General', 'smartLink': False, 'privateNetwork': False, 'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged'},
    # {'prefix': 'net_', 'suffix': '', 'start': 411, 'end': 4094, 'name': None, 'type': 'ethernet-networkV4',
    #  'vlanId': None, 'purpose': 'General', 'smartLink': False, 'privateNetwork': False, 'connectionTemplateUri': None,
    #  'ethernetNetworkType': 'Tagged'}
]

# The VLAN ID must be between 1 and 4094, excluding internally reserved VLAN IDs 3967-4094.
bulk_networks_dict = {
    'vlanIdRange': '411-2000',
    'namePrefix': 'net',
    'privateNetwork': False,
    'smartLink': True,
    'purpose': 'General',
    'type': 'bulk-ethernet-networkV1',
    'bandwidth': {
        'maximumBandwidth': 20000,
        'typicalBandwidth': 2500}
}

network_sets = [
    {'name': 'netset162', 'type': 'network-setV4', 'networkUris': rlist(1301, 1462, prefix='net_'),
     'nativeNetworkUri': None},
    {'name': 'netset1K', 'type': 'network-setV4', 'networkUris': rlist(1, 1000, prefix='net_'),
     'nativeNetworkUri': 'net_401'},
    {'name': 'netset501', 'type': 'network-setV4', 'networkUris': rlist(301, 801, prefix='net_'),
     'nativeNetworkUri': None},
    {'name': 'netset334', 'type': 'network-setV4', 'networkUris': rlist(301, 634, prefix='net_'),
     'nativeNetworkUri': None},
    {'name': 'netset251', 'type': 'network-setV4', 'networkUris': rlist(301, 551, prefix='net_'),
     'nativeNetworkUri': None},
    {'name': 'netset201', 'type': 'network-setV4', 'networkUris': rlist(301, 501, prefix='net_'),
     'nativeNetworkUri': None}
]

grow_network_sets = {
    "Enc1_netset": {
        'name': 'netset1K',
        'type': 'network-setV4',
        'networkUris': rlist(1, 1000, prefix='net_'),
        'nativeNetworkUri': 'net_401'
    },
    "Enc2_netset": {
        'name': 'netset1K',
        'type': 'network-setV4',
        'networkUris': rlist(301, 800, prefix='net_'),
        'nativeNetworkUri': 'net_401'
    },
    "Enc3_netset": {
        'name': 'netset1K',
        'type': 'network-setV4',
        'networkUris': rlist(301, 633, prefix='net_'),
        'nativeNetworkUri': 'net_401'
    },
    "Enc4_netset": {
        'name': 'netset1K',
        'type': 'network-setV4',
        'networkUris': rlist(301, 550, prefix='net_'),
        'nativeNetworkUri': 'net_401'
    },
    "Enc5_netset": {
        'name': 'netset1K',
        'type': 'network-setV4',
        'networkUris': rlist(301, 500, prefix='net_'),
        'nativeNetworkUri': 'net_401'
    }
}

neg_grow_network_sets = {

    "Enc1_netset": {
        'name': 'netset1K',
        'type': 'network-setV4',
        'networkUris': rlist(1, 1001, prefix='net_'),
        'nativeNetworkUri': None
    },
    "Enc2_netset": {
        'name': 'netset1K',
        'type': 'network-setV4',
        'networkUris': rlist(301, 801, prefix='net_'),
        'nativeNetworkUri': None
    },
    "Enc3_netset": {
        'name': 'netset1K',
        'type': 'network-setV4',
        'networkUris': rlist(301, 634, prefix='net_'),
        'nativeNetworkUri': None
    },
    "Enc4_netset": {
        'name': 'netset1K',
        'type': 'network-setV4',
        'networkUris': rlist(301, 551, prefix='net_'),
        'nativeNetworkUri': None
    },
    "Enc5_netset": {
        'name': 'netset1K',
        'type': 'network-setV4',
        'networkUris': rlist(301, 501, prefix='net_'),
        'nativeNetworkUri': None
    }
}

neg_network_sets = [
    {'name': 'netset1001', 'type': 'network-setV4', 'networkUris': rlist(1, 1001, prefix='net_'),
     'nativeNetworkUri': None},
]

fcoe_networks = [{'name': 'fcoenetwork1002', 'type': 'fcoe-networkV4', 'vlanId': 1002},
                 {'name': 'fcoenetwork1003', 'type': 'fcoe-networkV4', 'vlanId': 1003}]

###
# logical enclosure template
###
les = {
    'name': 'Grow-LE',
    'enclosureUris': None,
    'enclosureGroupUri': None,
    'firmwareBaselineUri': None,
    'forceInstallFirmware': False
}

telemetry = {
    'type': 'telemetry-configuration',
    'enableTelemetry': False,
    'sampleInterval': 200,
    'sampleCount': 20
}

ethernet_setting = {
    'type': icm_settings_type,
    'enableFastMacCacheFailover': False,
    'enableIgmpSnooping': False,
    'enableNetworkLoopProtection': False,
    'igmpIdleTimeoutInterval': 130,
    'macRefreshInterval': 10
}

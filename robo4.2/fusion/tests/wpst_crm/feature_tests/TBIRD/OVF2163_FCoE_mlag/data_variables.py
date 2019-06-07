# This file will define any comware related settings


def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist


def rlist(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist


SSH_PASS = 'hpvse1'
interface = 'bond0'

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

vcenter = {'server': '15.199.230.130', 'user': 'rbriggs', 'password': 'hpvse1'}

ranges = [{'name': 'FCOE-MAC', 'type': 'Range', 'category': 'id-range-VMAC',
           'rangeCategory': 'CUSTOM', 'startAddress': '00:BA:51:00:00:00',
           'endAddress': '00:BA:51:00:00:7F', 'enabled': True},
          {'name': 'FCOE-WWN', 'type': 'Range', 'category': 'id-range-VWWN',
           'rangeCategory': 'CUSTOM', 'startAddress': '21:11:BA:51:00:00:00:00',
           'endAddress': '21:11:BA:51:00:00:00:7F', 'enabled': True},
          {'name': 'FCOE-SN', 'type': 'Range', 'category': 'id-range-VSN',
           'rangeCategory': 'CUSTOM', 'startAddress': 'VCUAAAAAAA',
           'endAddress': 'VCUAAAAADT', 'enabled': True}]

appliance = {'type': 'ApplianceNetworkConfigurationV2',
             'applianceNetworks':
                 [{'device': 'eth0',
                   'macAddress': None,
                   'interfaceName': 'hpecorp',
                   'activeNode': '1',
                   'unconfigure': False,
                   'ipv4Type': 'STATIC',
                   'ipv4Subnet': '255.255.248.0',
                   'ipv4Gateway': '15.245.128.1',
                   'ipv4NameServers': ['16.110.135.51', '16.110.135.52'],
                   'virtIpv4Addr': '15.245.131.72',
                   'app1Ipv4Addr': '15.245.131.73',
                   'app2Ipv4Addr': '15.245.131.74',
                   'ipv6Type': 'UNCONFIGURE',
                   'hostname': 'BA51-2ENCS.us.rdlabs.hpecorp.net',
                   'confOneNode': True,
                   'domainName': 'us.rdlabs.hpecorp.net',
                   'aliasDisabled': True,
                   }],
             }

timeandlocale = {'type': 'TimeAndLocale',
                 'dateTime': None,
                 'timezone': 'UTC',
                 'ntpServers': ['ntp.hp.net'],
                 'locale': 'en_US.UTF-8'}

EG = 'EG'
EG2 = 'EG2'
EG3 = 'EG3'
DCS_ENC1 = '0000A66101'
DCS_ENC2 = '0000A66102'
ENC1 = 'MXQ734024M'
ENC2 = 'CN7545084B'

ENC1_BAY1_IP_A = '10.11.1.15'
ENC1_BAY1_IP_B = '10.11.1.15'
ENC1_BAY1 = '%s, bay 1' % ENC1
ENC2_BAY4_IP = '10.11.1.13'
ENC2_BAY4 = '%s, bay 4' % ENC2

US_edit = 'us1-comware'

GW_IP = '10.11.0.1'

PING_LIST_1 = [ENC1_BAY1_IP_A, ENC2_BAY4_IP]
PING_LIST_2 = [ENC1_BAY1_IP_B, ENC2_BAY4_IP]
PING_LIST_3 = [ENC1_BAY1_IP_A, GW_IP]

SERVERS = [ENC1_BAY1, ENC2_BAY4]

LE = 'LE'
LE2 = 'LE2'
LE3 = 'LE3'

LIG1 = 'LIG1'
BothLIG1 = 'IBS3-HA-Both'
ComwareLIG1 = 'ComwareLIG1'
ComwareLIG2 = 'IBS3-HA-Comware'
CiscoLIG1 = 'CiscoLIG1'
CiscoLIG2 = 'IBS3-HA-Cisco'
CLIG1 = 'CLIG1'
CLIG2 = 'CLIG2'
CLIG3 = 'CLIG3'
CLIG4 = 'CLIG4'
CLIG5 = 'CLIG5'

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

licenses = [
    {
        'key': 'YCDC D9MA H9PQ KHX2 V7B5 HWWB Y9JL KMPL TA2E PDRA DXAU 2CSM GHTG L762 HUK7 GB5M KJVT D5KM EFRW DS5R TXXK 6Q22 AK2P 3EW2 AJQ4 HU5V TZZH AB6X 82Z5 WHEF GE4C LUE3 BKT8 WXDG NK6Y C4GA HZL4 XBE7 3VJ6 2MSU 4ZU9 9WGG CZU7 WE4X YN44 CH55 KZLG 2F4N A8RJ UKEC 3F9V JQY5 "423542007 HPOV-NFR1 HP_OneView_16_Seat_NFR 75YYJJECU46C"_3DWNY-6B2KD-D8Z6S-6YR4B-K8GDW'},
    {
        'key': '9CTC B9MA H9PA GHWY V7B5 HWWB Y9JL KMPL 3ASE NGRE DXAU 2CSM GHTG L762 FN83 EARE KJVT D5KM EFRW DS5R 3XPK 4T22 AK2P 3EW2 AJA6 XUNV TZZX MB5X 82Z5 WHEF GE4C LUE3 BKT8 WXDG NK6Y C4GA HZL4 XBE7 3VJ6 2MSU 4ZU9 9WGG CZU7 WE4X YN44 CH55 KZLG 2F4N A8RJ UKEC 3F9V JQY5 "423542185 HPOV-NFR1 HP_OneView_16_Seat_NFR JJT5JJEC9DC5"_3JNBT-28349-3DJ6L-TBRPP-PDLNR'},
    {
        'key': '9B3C A99A H9P9 GHUZ U7B5 HWW5 Y9JL KMPL 5AWA 8CBE DXAU 2CSM GHTG L762 7NGZ GDV4 KJVT D5KM EFRW DS5R 5XP8 4XK2 GNSL 9F82 7JKT QVXB XZKH ABB4 NV2C LHXU KN7U 5NA6 BKRK 35QB D8UW R42A X3BN LQ6M 5V9A PM6Q 4MN9 9GGS EZU7 GEMX VUJW CDB5 JVRX 8HEN 2J98 ACPB "TKOPREN HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR ATJUJJEDAT2Y"'}
]

ethernet_ranges = [{'prefix': 'net_', 'suffix': '', 'start': 1, 'end': 2999,
                    'name': None, 'type': 'ethernet-networkV4',
                    'vlanId': None, 'purpose': 'General', 'smartLink': False,
                    'privateNetwork': False,
                    'connectionTemplateUri': None,
                    'ethernetNetworkType': 'Tagged'},
                   ]

network_sets = [{'name': 'netset1', 'type': 'network-setV4',
                 'networkUris': rlist(1, 499), 'nativeNetworkUri': None},
                {'name': 'netset2', 'type': 'network-setV4',
                 'networkUris': rlist(500, 999), 'nativeNetworkUri': None},
                {'name': 'netset3', 'type': 'network-setV4',
                 'networkUris': rlist(1000, 1499), 'nativeNetworkUri': None},
                {'name': 'netset4', 'type': 'network-setV4',
                 'networkUris': rlist(1500, 1999), 'nativeNetworkUri': None},
                {'name': 'netset5', 'type': 'network-setV4',
                 'networkUris': rlist(2000, 2499), 'nativeNetworkUri': None},
                {'name': 'netset6', 'type': 'network-setV4',
                 'networkUris': rlist(2500, 2999), 'nativeNetworkUri': None},
                ]

fcoe_networks = {'fcoe-1': {'name': 'fcoe-1', 'type': 'fcoe-networkV4',
                            'vlanId': 1},
                 'fcoe-100': {'name': 'fcoe-100', 'type': 'fcoe-networkV4',
                              'vlanId': 100},
                 'fcoe-258': {'name': 'fcoe-258', 'type': 'fcoe-networkV4',
                              'vlanId': 258},
                 'fcoe-2000': {'name': 'fcoe-2000', 'type': 'fcoe-networkV4',
                               'vlanId': 2000},
                 'fcoe-100b': {'name': 'fcoe-100b', 'type': 'fcoe-networkV4',
                               'vlanId': 100},
                 'fcnetwork-a': {'name': 'fcnetwork-a',
                                 'type': 'fcoe-networkV4',
                                 'vlanId': 209},
                 'network-a': {'name': 'network-a',
                               'type': 'fcoe-networkV4', 'vlanId': 210},
                 'network-b': {'name': 'network-b',
                               'type': 'fcoe-networkV4', 'vlanId': 211},
                 'no-vlanId': {'name': 'no-vlanId', 'type': 'fcoe-networkV4'},
                 'fcoe-4095': {'name': 'fcoe-4095', 'type': 'fcoe-networkV4',
                               'vlanId': 4095}}

fcoe_ranges = {'fcoe-range32a': {'prefix': 'fcoe-', 'suffix': 'a',
                                 'start': 1001, 'end': 1032},
               'fcoe-range32b': {'prefix': 'fcoe-', 'suffix': 'b',
                                 'start': 1001, 'end': 1032},
               'fcoe-range32c': {'prefix': 'fcoe-', 'suffix': 'c',
                                 'start': 1001, 'end': 1032},
               'fcoe-range32d': {'prefix': 'fcoe-', 'suffix': 'd',
                                 'start': 1001, 'end': 1032},
               'fcoe-range33': {'prefix': 'fcoe-', 'suffix': '',
                                'start': 1001, 'end': 1033},
               'fcoe-range30a': {'prefix': 'fcoe-', 'suffix': 'a',
                                 'start': 1001, 'end': 1030},
               'fcoe-range128': {'prefix': 'fcoe-', 'suffix': '',
                                 'start': 1001, 'end': 1128},
               'fcoe-range-delete-20': {'prefix': 'fcoe-', 'suffix': '',
                                        'start': 1109, 'end': 1128},
               'fcoe-range-256': {'prefix': 'fcoe-', 'suffix': '',
                                  'start': 2, 'end': 257}
               }

fc_networks = [{'type': 'fc-networkV4',
                'linkStabilityTime': 30,
                'autoLoginRedistribution': True,
                'name': 'fcnetwork-a',
                'connectionTemplateUri': None,
                'managedSanUri': None,
                'fabricType': 'FabricAttach'}]

enc_groups = [
    {'name': EG,
     'enclosureCount': 1,
     'interconnectBayMappings': [
         {'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
         {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
         {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:' + ComwareLIG1},
         {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
         {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
         {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:' + ComwareLIG1}],
     'ipAddressingMode': "External",
     },
]
enc_groups_me = [
    {'name': EG2,
     'enclosureCount': 2,
     'interconnectBayMappings': [
         {'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
         {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
         {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:' + BothLIG1},
         {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
         {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
         {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:' + BothLIG1}],
     'ipAddressingMode': "External",
     },
]

les = [{'name': LE,
        'enclosureUris': ['ENC:' + ENC1],
        'enclosureGroupUri': 'EG:EG',
        'firmwareBaselineUri': None,
        'forceInstallFirmware': False
        },
       {'name': LE2,
        'enclosureUris': ['ENC:' + ENC1, 'END:' + ENC2],
        'enclosureGroupUri': 'EG:%s' % EG2,
        'firmwareBaselineUri': None,
        'forceInstallFirmware': False
        },
       {'name': LE3,
        'enclosureUris': ['ENC:' + ENC1, 'ENC:' + ENC2],
        'enclosureGroupUri': 'EG:%s' % EG3,
        'firmwareBaselineUri': None,
        'forceInstallFirmware': False
        },
       ]

# Cisco Nets:
cisco_nets = make_range_list(2000, 2010, 'net_')
cisco_nets.append('fcoe-50')
cisco_nets.append('fcoe-60')

cisco_nets_mlag_bay3 = []
cisco_nets_mlag_bay3.append('fcoe-50')
cisco_nets_mlag_bay6 = []
cisco_nets_mlag_bay6.append('fcoe-60')

# Comware nets:
comware_nets = make_range_list(1000, 1020, 'net_')
comware_nets_less_one = make_range_list(1000, 1020, 'net_')
comware_nets.append('fcoe-30')
comware_nets.append('fcoe-40')
comware_nets_less_one.append('fcoe-30')
comware_nets_less_one.append('fcoe-40')

comware_nets_mlag_bay3 = []
comware_nets_mlag_bay3.append('fcoe-30')
comware_nets_mlag_bay6 = []
comware_nets_mlag_bay6.append('fcoe-40')

# add fcoenetwork fcoe-2. It will be assigned to bay 3:
comware_fcoe_nets_add_one = []
comware_fcoe_nets_add_one.append('fcoe-30')
comware_fcoe_nets_add_one.append('fcoe-40')
comware_fcoe_nets_add_one.append('fcoe-2')

# add fcoenetwork fcoe-2.
comware_nets_mlag_add_one_bay3 = []
comware_nets_mlag_add_one_bay3.append('fcoe-30')
comware_nets_mlag_add_one_bay3.append('fcoe-2')

# remove fcoenetwork fcoe-2.
comware_nets_mlag_minus_one_bay3 = []
comware_nets_mlag_minus_one_bay3.append('fcoe-30')
comware_fcoe_nets_less_one = []
comware_fcoe_nets_less_one.append('fcoe-30')
comware_fcoe_nets_less_one.append('fcoe-40')

comware_fcoe_nets = []
comware_fcoe_nets.append('fcoe-30')
comware_fcoe_nets.append('fcoe-40')

uplink_sets = {
    'us1': {
        'name': 'us1',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': make_range_list(200, 216, 'fcoe-'),
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Long',
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q1',
             'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q2',
             'speed': 'Auto'}]
    },
    'us2': {
        'name': 'us2',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': make_range_list(217, 224, 'fcoe-'),
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Long',
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '6', 'port': 'Q3',
             'speed': 'Auto'},
            {'enclosure': '1', 'bay': '6', 'port': 'Q4',
             'speed': 'Auto'}, ]
    },
    'us1-comware': {
        'name': 'us1-comware',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': comware_nets,
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Long',
        'fcoeMlagMode': 'InterfaceAndMacBinding',
        'fcoeNetworkMlagBays': [
            {'networkUris': comware_nets_mlag_bay3,
             'bay': '3'},
            {'networkUris': comware_nets_mlag_bay6,
             'bay': '6'}],
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q1',
             'speed': 'Auto',
             'mlagFcoePort': 'vFcMacAndInterfaceBinding'},
            {'enclosure': '1', 'bay': '6', 'port': 'Q3',
             'speed': 'Auto',
             'mlagFcoePort': 'vFcMacAndInterfaceBinding'}, ]
    },
    'us2-comware': {
        'name': 'us2-comware',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': comware_nets_less_one,
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Long',
        'fcoeMlagMode': 'InterfaceAndMacBinding',
        'fcoeNetworkMlagBays': [
            {'networkUris': comware_nets_mlag_minus_one_bay3,
             'bay': '3'},
            {'networkUris': comware_nets_mlag_bay6,
             'bay': '6'}],
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q1',
             'speed': 'Auto',
             'mlagFcoePort': 'vFcMacAndInterfaceBinding'},
            {'enclosure': '1', 'bay': '6', 'port': 'Q3',
             'speed': 'Auto',
             'mlagFcoePort': 'vFcMacAndInterfaceBinding'}, ]
    },
    'us1-comware-33': {
        'name': 'us1-comware-33',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': make_range_list(2, 35, 'fcoe-'),
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Long',
        'fcoeMlagMode': 'InterfaceAndMacBinding',
        'fcoeNetworkMlagBays': [
            {'networkUris': make_range_list(2, 17, 'fcoe-'),
             'bay': '3'},
            {'networkUris': make_range_list(18, 35, 'fcoe-'),
             'bay': '6'}],
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q1',
             'speed': 'Auto',
             'mlagFcoePort': 'vFcMacAndInterfaceBinding'},
            {'enclosure': '1', 'bay': '6', 'port': 'Q3',
             'speed': 'Auto',
             'mlagFcoePort': 'vFcMacAndInterfaceBinding'}, ]
    },
    'us1-cisco-33': {
        'name': 'us1-cisco-33',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': make_range_list(2, 35, 'fcoe-'),
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Long',
        'fcoeMlagMode': 'MacBinding',
        'fcoeNetworkMlagBays': [
            {'networkUris': make_range_list(2, 17, 'fcoe-'),
             'bay': '3'},
            {'networkUris': make_range_list(18, 35, 'fcoe-'),
             'bay': '6'}],
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q1',
             'speed': 'Auto',
             'mlagFcoePort': 'NA'},
            {'enclosure': '1', 'bay': '6', 'port': 'Q3',
             'speed': 'Auto',
             'mlagFcoePort': 'NA'}, ]
    },
    'us1-comware-32': {
        'name': 'us1-comware-32',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': make_range_list(2, 33, 'fcoe-'),
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Long',
        'fcoeMlagMode': 'InterfaceAndMacBinding',
        'fcoeNetworkMlagBays': [
            {'networkUris': make_range_list(2, 17, 'fcoe-'),
             'bay': '3'},
            {'networkUris': make_range_list(18, 33, 'fcoe-'),
             'bay': '6'}],
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q1',
             'speed': 'Auto',
             'mlagFcoePort': 'vFcMacAndInterfaceBinding'},
            {'enclosure': '1', 'bay': '6', 'port': 'Q3',
             'speed': 'Auto',
             'mlagFcoePort': 'vFcMacAndInterfaceBinding'}, ]
    },
    'us1-comware-17p': {
        'name': 'us1-comware-17p',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': make_range_list(2, 9, 'fcoe-'),
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Long',
        'fcoeMlagMode': 'InterfaceAndMacBinding',
        'fcoeNetworkMlagBays': [
            {'networkUris': make_range_list(2, 5, 'fcoe-'), 'bay': '3'},
            {'networkUris': make_range_list(6, 9, 'fcoe-'), 'bay': '6'}],
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q1:1', 'speed': 'Auto',
             'mlagFcoePort': 'vFcMacAndInterfaceBinding'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q1:2', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q1:3', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q1:4', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q2:1', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q2:2', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q2:3', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q2:4', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q3:4', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '6', 'port': 'Q3:1', 'speed': 'Auto',
             'mlagFcoePort': 'vFcMacAndInterfaceBinding'},
            {'enclosure': '1', 'bay': '6', 'port': 'Q3:2', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '6', 'port': 'Q3:3', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '6', 'port': 'Q3:4', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '6', 'port': 'Q4:1', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '6', 'port': 'Q4:2', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '6', 'port': 'Q4:3', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '6', 'port': 'Q4:4', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '6', 'port': 'Q5:4', 'speed': 'Auto'}, ]
    },
    'us3': {
        'name': 'us3',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': make_range_list(1025, 1032, 'fcoe-'),
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Long',
        'logicalPortConfigInfos': [
            {'enclosure': '2', 'bay': '6', 'port': 'Q5', 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': 'Q6', 'speed': 'Auto'}]
    },
    'us1a': {
        'name': 'us1',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': make_range_list(1002, 1004, 'fcoe-') + ['network-a'],
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Long',
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q1', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q2', 'speed': 'Auto'}, ]
    },
    'us2a': {
        'name': 'us2',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': make_range_list(1005, 1008, 'fcoe-') + ['network-b'],
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Long',
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q3', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q4', 'speed': 'Auto'}, ]
    },
    'us3a': {
        'name': 'us3',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': make_range_list(1009, 1015, 'fcoe-') + ['network-c'],
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Long',
        'logicalPortConfigInfos': [
            {'enclosure': '2', 'bay': '6', 'port': 'Q5', 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': 'Q6', 'speed': 'Auto'}]
    },
    'us-eth': {
        'name': 'us-eth',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['network-d'],
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Long',
        'logicalPortConfigInfos': [
            {'enclosure': '2', 'bay': '6', 'port': 'Q4', 'speed': 'Auto'},
        ]
    },
    'us3-8fcoe': {
        'name': 'us3',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': make_range_list(1009, 1015, 'fcoe-'),
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Long',
        'logicalPortConfigInfos': [
            {'enclosure': '2', 'bay': '6', 'port': 'Q5', 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': 'Q6', 'speed': 'Auto'}]
    },
    'us1-fcoe': {
        'name': 'us1-fcoe',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['fcoe-1032c'],
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Long',
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q3', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q4', 'speed': 'Auto'}]
    },
    'us-32fcoe-a': {
        'name': 'us-32fcoe-a',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': make_range_list(1040, 1071, 'fcoe-', ''),
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Long',
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q5', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q6', 'speed': 'Auto'}]
    },
    'us-32fcoe-b': {
        'name': 'us-32fcoe-b',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': make_range_list(1072, 1103, 'fcoe-', ''),
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Long',
        'logicalPortConfigInfos': [
            {'enclosure': '2', 'bay': '6', 'port': 'Q5', 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': 'Q6', 'speed': 'Auto'}]
    },
    'Q1.1-Q6.4': {
        'name': 'Q1.1-Q6.4',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': make_range_list(**fcoe_ranges['fcoe-range32b']),
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Long',
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q1:1', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q1:2', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q1:3', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q1:4', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q2:1', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q2:2', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q2:3', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q2:4', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q3:1', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q3:2', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q3:3', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q3:4', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q4:1', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q4:2', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q4:3', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q4:4', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q5:1', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q5:2', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q5:3', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q5:4', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q6:1', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q6:2', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q6:3', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q6:4', 'speed': 'Auto'}, ]
    },
    'Q1-Q8': {
        'name': 'Q1-Q8',
        'ethernetNetworkType': 'Tunnel',
        'networkType': 'Ethernet',
        'networkUris': ['Tunnel1'],
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Long',
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q1', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q2', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q3', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q4', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q5', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q6', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q7', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q8', 'speed': 'Auto'}]
    },
    'us33a': {
        'name': 'us-33-exceeds-32max',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': make_range_list(1001, 1034, 'fcoe-'),
        'primaryPort': None,
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q5', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q6', 'speed': 'Auto'}, ]
    },
    'us33': {
        'name': 'us-33-exceeds-32max',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': make_range_list(1001, 1034, 'fcoe-'),
        'primaryPort': None,
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'logicalPortConfigInfos': [
            {'enclosure': '2', 'bay': '6', 'port': 'Q1', 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': 'Q2', 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': 'Q3', 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': 'Q4', 'speed': 'Auto'}, ]
    },
    'us10': {
        'name': 'us-spans-multiple-ICMs',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': make_range_list(1027, 1028, 'fcoe-'),
        'primaryPort': None,
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q5', 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': 'Q1', 'speed': 'Auto'}, ]
    },
    'unsupported-ics2': {
        'name': 'unsupported-ics2',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['fcoe-100'],
        'primaryPort': None,
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'logicalPortConfigInfos': [{'bay': '1', 'port': '1', 'speed': 'Auto'}]
    },
    'duplicate-vlan': {
        'name': 'duplicate-vlan',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['fcoe-1032', 'fcoe-1032a'],
        'primaryPort': None,
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'logicalPortConfigInfos': [
            {'enclosure': '2', 'bay': '6', 'port': 'Q1', 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': 'Q2', 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': 'Q3', 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': 'Q4', 'speed': 'Auto'}, ]
    },
    'duplicate-vlan-eth': {
        'name': 'duplicate-vlan',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['eth-100', 'fcoe-100'],
        'primaryPort': None,
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'logicalPortConfigInfos': [
            {'enclosure': '2', 'bay': '6', 'port': 'Q1', 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': 'Q2', 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': 'Q3', 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': 'Q4', 'speed': 'Auto'}, ]
    },
    'AsideIBS3': {
        'name': 'IBS3-Aside-Q6-40gb',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': comware_nets,
        'primaryPort': None,
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'fcoeMlagMode': 'InterfaceAndMacBinding',
        'fcoeNetworkMlagBays': [
            {'networkUris': comware_nets_mlag_bay3, 'bay': '3'},
            {'networkUris': comware_nets_mlag_bay6, 'bay': '6'}
        ],
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q4:1', 'speed': 'Auto',
             'mlagFcoePort': 'vFcMacAndInterfaceBinding'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q4:2', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q4:3', 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': 'Q4:1', 'speed': 'Auto',
             'mlagFcoePort': 'vFcMacAndInterfaceBinding'},
            {'enclosure': '2', 'bay': '6', 'port': 'Q4:2', 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': 'Q4:3', 'speed': 'Auto'},
        ]
    },
    'BsideIBS3': {
        'name': 'IBS3-Bside-Q6-40gb',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': cisco_nets,
        'primaryPort': None,
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'fcoeMlagMode': 'MacBinding',
        'fcoeNetworkMlagBays': [
            {'networkUris': cisco_nets_mlag_bay3, 'bay': '3'},
            {'networkUris': cisco_nets_mlag_bay6, 'bay': '6'}
        ],
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q1:1', 'speed': 'Auto',
             'mlagFcoePort': 'NA'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q1:2', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q1:3', 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': 'Q1:1', 'speed': 'Auto',
             'mlagFcoePort': 'NA'},
            {'enclosure': '2', 'bay': '6', 'port': 'Q1:2', 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': 'Q1:3', 'speed': 'Auto'},
        ]
    }

}

li_uplink_sets = {
    'us1': {
        'name': 'us1-1',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': [],
        'fcNetworkUris': [],
        'fcoeNetworkUris': make_range_list(2, 9, 'fcoe-'),
        'lacpTimer': 'Short',
        'fcoeMlagMode': 'InterfaceAndMacBinding',
        'fcoeNetworkMlagBays': [
            {'networkUris': make_range_list(2, 5, 'fcoe-'), 'bay': '3'},
            {'networkUris': make_range_list(6, 9, 'fcoe-'), 'bay': '6'}],
        'logicalInterconnectUri': None,
        'primaryPortLocation': None,
        'manualLoginRedistributionState': 'NotSupported',
        'connectionMode': 'Auto',
        'nativeNetworkUri': None,
        'portConfigInfos': [
            {'enclosure': ENC1, 'bay': '3', 'port': 'Q3',
             'desiredSpeed': 'Auto',
             'mlagFcoePort': 'vFcMacAndInterfaceBinding'},
            {'enclosure': ENC1, 'bay': '6', 'port': 'Q2',
             'desiredSpeed': 'Auto',
             'mlagFcoePort': 'vFcMacAndInterfaceBinding'}]
    },
    'IBS3-Aside-add-fcoe-2': {
        'name': 'IBS3-Aside-Q6-40gb',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': comware_nets,
        'fcNetworkUris': [],
        'fcoeNetworkUris': comware_fcoe_nets_add_one,
        'lacpTimer': 'Long',
        'fcoeMlagMode': 'InterfaceAndMacBinding',
        'fcoeNetworkMlagBays': [
            {'networkUris': comware_nets_mlag_add_one_bay3, 'bay': '3'},
            {'networkUris': comware_nets_mlag_bay6, 'bay': '6'}],
        'logicalInterconnectUri': None,
        'primaryPortLocation': None,
        'manualLoginRedistributionState': 'NotSupported',
        'connectionMode': 'Auto',
        'nativeNetworkUri': None,
        'portConfigInfos': [
            {'enclosure': ENC1, 'bay': '3', 'port': 'Q4:1',
             'desiredSpeed': 'Auto',
             'mlagFcoePort': 'vFcMacAndInterfaceBinding'},
            {'enclosure': ENC1, 'bay': '3', 'port': 'Q4:2',
             'desiredSpeed': 'Auto'},
            {'enclosure': ENC1, 'bay': '3', 'port': 'Q4:3',
             'desiredSpeed': 'Auto'},
            {'enclosure': ENC2, 'bay': '6', 'port': 'Q4:1',
             'desiredSpeed': 'Auto',
             'mlagFcoePort': 'vFcMacAndInterfaceBinding'},
            {'enclosure': ENC2, 'bay': '6', 'port': 'Q4:2',
             'desiredSpeed': 'Auto'},
            {'enclosure': ENC2, 'bay': '6', 'port': 'Q4:3',
             'desiredSpeed': 'Auto'}]
    },
    'IBS3-Aside-minus-fcoe-2': {
        'name': 'IBS3-Aside-Q6-40gb',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': comware_nets,
        'fcNetworkUris': [],
        'fcoeNetworkUris': comware_fcoe_nets_less_one,
        'lacpTimer': 'Long',
        'fcoeMlagMode': 'InterfaceAndMacBinding',
        'fcoeNetworkMlagBays': [
            {'networkUris': comware_nets_mlag_minus_one_bay3, 'bay': '3'},
            {'networkUris': comware_nets_mlag_bay6, 'bay': '6'}],
        'logicalInterconnectUri': None,
        'primaryPortLocation': None,
        'manualLoginRedistributionState': 'NotSupported',
        'connectionMode': 'Auto',
        'nativeNetworkUri': None,
        'portConfigInfos': [
            {'enclosure': ENC1, 'bay': '3', 'port': 'Q4:1',
             'desiredSpeed': 'Auto',
             'mlagFcoePort': 'vFcMacAndInterfaceBinding'},
            {'enclosure': ENC1, 'bay': '3', 'port': 'Q4:2',
             'desiredSpeed': 'Auto'},
            {'enclosure': ENC1, 'bay': '3', 'port': 'Q4:3',
             'desiredSpeed': 'Auto'},
            {'enclosure': ENC2, 'bay': '6', 'port': 'Q4:1',
             'desiredSpeed': 'Auto',
             'mlagFcoePort': 'vFcMacAndInterfaceBinding'},
            {'enclosure': ENC2, 'bay': '6', 'port': 'Q4:2',
             'desiredSpeed': 'Auto'},
            {'enclosure': ENC2, 'bay': '6', 'port': 'Q4:3',
             'desiredSpeed': 'Auto'}]
    },
    'us2-comware-add-fcoe-2': {
        'name': 'us1-comware',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': comware_nets,
        'fcNetworkUris': [],
        'fcoeNetworkUris': comware_fcoe_nets_add_one,
        'lacpTimer': 'Long',
        'fcoeMlagMode': 'InterfaceAndMacBinding',
        'fcoeNetworkMlagBays': [
            {'networkUris': comware_nets_mlag_add_one_bay3, 'bay': '3'},
            {'networkUris': comware_nets_mlag_bay6, 'bay': '6'}],
        'logicalInterconnectUri': None,
        'primaryPortLocation': None,
        'manualLoginRedistributionState': 'NotSupported',
        'connectionMode': 'Auto',
        'nativeNetworkUri': None,
        'portConfigInfos': [
            {'enclosure': ENC1, 'bay': '3', 'port': 'Q1',
             'desiredSpeed': 'Auto',
             'mlagFcoePort': 'vFcMacAndInterfaceBinding'},
            {'enclosure': ENC1, 'bay': '6', 'port': 'Q3',
             'desiredSpeed': 'Auto',
             'mlagFcoePort': 'vFcMacAndInterfaceBinding'}, ]
    },
    'us2-comware-minus-fcoe-2': {
        'name': 'us1-comware',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': comware_nets,
        'fcNetworkUris': [],
        'fcoeNetworkUris': comware_fcoe_nets_less_one,
        'lacpTimer': 'Long',
        'fcoeMlagMode': 'InterfaceAndMacBinding',
        'fcoeNetworkMlagBays': [
            {'networkUris': comware_nets_mlag_minus_one_bay3, 'bay': '3'},
            {'networkUris': comware_nets_mlag_bay6, 'bay': '6'}],
        'logicalInterconnectUri': None,
        'primaryPortLocation': None,
        'manualLoginRedistributionState': 'NotSupported',
        'connectionMode': 'Auto',
        'nativeNetworkUri': None,
        'portConfigInfos': [
            {'enclosure': ENC1, 'bay': '3', 'port': 'Q1',
             'desiredSpeed': 'Auto',
             'mlagFcoePort': 'vFcMacAndInterfaceBinding'},
            {'enclosure': ENC1, 'bay': '6', 'port': 'Q3',
             'desiredSpeed': 'Auto',
             'mlagFcoePort': 'vFcMacAndInterfaceBinding'}, ]
    },
    'IBS3-Aside-add-port': {
        'name': 'IBS3-Aside-Q6-40gb',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': comware_nets,
        'fcNetworkUris': [],
        'fcoeNetworkUris': comware_fcoe_nets,
        'lacpTimer': 'Long',
        'fcoeMlagMode': 'InterfaceAndMacBinding',
        'fcoeNetworkMlagBays': [
            {'networkUris': comware_nets_mlag_bay3, 'bay': '3'},
            {'networkUris': comware_nets_mlag_bay6, 'bay': '6'}],
        'logicalInterconnectUri': None,
        'primaryPortLocation': None,
        'manualLoginRedistributionState': 'NotSupported',
        'connectionMode': 'Auto',
        'nativeNetworkUri': None,
        'portConfigInfos': [
            {'enclosure': ENC1, 'bay': '3', 'port': 'Q4:1',
             'desiredSpeed': 'Auto',
             'mlagFcoePort': 'vFcMacAndInterfaceBinding'},
            {'enclosure': ENC1, 'bay': '3', 'port': 'Q4:2',
             'desiredSpeed': 'Auto'},
            {'enclosure': ENC1, 'bay': '3', 'port': 'Q4:3',
             'desiredSpeed': 'Auto'},
            {'enclosure': ENC1, 'bay': '3', 'port': 'Q4:4',
             'desiredSpeed': 'Auto'},
            {'enclosure': ENC2, 'bay': '6', 'port': 'Q4:1',
             'desiredSpeed': 'Auto',
             'mlagFcoePort': 'vFcMacAndInterfaceBinding'},
            {'enclosure': ENC2, 'bay': '6', 'port': 'Q4:2',
             'desiredSpeed': 'Auto'},
            {'enclosure': ENC2, 'bay': '6', 'port': 'Q4:3',
             'desiredSpeed': 'Auto'},
            {'enclosure': ENC2, 'bay': '6', 'port': 'Q4:4',
             'desiredSpeed': 'Auto'},
        ]
    },
    'IBS3-Aside-minus-port': {
        'name': 'IBS3-Aside-Q6-40gb',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': comware_nets,
        'fcNetworkUris': [],
        'fcoeNetworkUris': comware_fcoe_nets,
        'lacpTimer': 'Long',
        'fcoeMlagMode': 'InterfaceAndMacBinding',
        'fcoeNetworkMlagBays': [
            {'networkUris': comware_nets_mlag_bay3, 'bay': '3'},
            {'networkUris': comware_nets_mlag_bay6, 'bay': '6'}],
        'logicalInterconnectUri': None,
        'primaryPortLocation': None,
        'manualLoginRedistributionState': 'NotSupported',
        'connectionMode': 'Auto',
        'nativeNetworkUri': None,
        'portConfigInfos': [
            {'enclosure': ENC1, 'bay': '3', 'port': 'Q4:1',
             'desiredSpeed': 'Auto',
             'mlagFcoePort': 'vFcMacAndInterfaceBinding'},
            {'enclosure': ENC1, 'bay': '3', 'port': 'Q4:2',
             'desiredSpeed': 'Auto'},
            {'enclosure': ENC1, 'bay': '3', 'port': 'Q4:3',
             'desiredSpeed': 'Auto'},
            {'enclosure': ENC2, 'bay': '6', 'port': 'Q4:1',
             'desiredSpeed': 'Auto',
             'mlagFcoePort': 'vFcMacAndInterfaceBinding'},
            {'enclosure': ENC2, 'bay': '6', 'port': 'Q4:2',
             'desiredSpeed': 'Auto'},
            {'enclosure': ENC2, 'bay': '6', 'port': 'Q4:3',
             'desiredSpeed': 'Auto'}, ]
    },
    'us2-comware-add-port': {
        'name': 'us1-comware',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': comware_nets,
        'fcNetworkUris': [],
        'fcoeNetworkUris': comware_fcoe_nets,
        'lacpTimer': 'Long',
        'fcoeMlagMode': 'InterfaceAndMacBinding',
        'fcoeNetworkMlagBays': [
            {'networkUris': comware_nets_mlag_bay3, 'bay': '3'},
            {'networkUris': comware_nets_mlag_bay6, 'bay': '6'}],
        'logicalInterconnectUri': None,
        'primaryPortLocation': None,
        'manualLoginRedistributionState': 'NotSupported',
        'connectionMode': 'Auto',
        'nativeNetworkUri': None,
        'portConfigInfos': [
            {'enclosure': ENC1, 'bay': '3', 'port': 'Q1',
             'desiredSpeed': 'Auto',
             'mlagFcoePort': 'vFcMacAndInterfaceBinding'},
            {'enclosure': ENC1, 'bay': '3', 'port': 'Q3',
             'desiredSpeed': 'Auto'},
            {'enclosure': ENC1, 'bay': '6', 'port': 'Q3',
             'desiredSpeed': 'Auto',
             'mlagFcoePort': 'vFcMacAndInterfaceBinding'}, ]
    },
    'us2-comware-minus-port': {
        'name': 'us1-comware',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': comware_nets,
        'fcNetworkUris': [],
        'fcoeNetworkUris': comware_fcoe_nets,
        'lacpTimer': 'Long',
        'fcoeMlagMode': 'InterfaceAndMacBinding',
        'fcoeNetworkMlagBays': [
            {'networkUris': comware_nets_mlag_bay3, 'bay': '3'},
            {'networkUris': comware_nets_mlag_bay6, 'bay': '6'}],
        'logicalInterconnectUri': None,
        'primaryPortLocation': None,
        'manualLoginRedistributionState': 'NotSupported',
        'connectionMode': 'Auto',
        'nativeNetworkUri': None,
        'portConfigInfos': [
            {'enclosure': ENC1, 'bay': '3', 'port': 'Q1',
             'desiredSpeed': 'Auto',
             'mlagFcoePort': 'vFcMacAndInterfaceBinding'},
            {'enclosure': ENC1, 'bay': '6', 'port': 'Q3',
             'desiredSpeed': 'Auto',
             'mlagFcoePort': 'vFcMacAndInterfaceBinding'}, ]
    },
    'us1-1icm': {
        'name': 'us1-1icm',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': [],
        'fcNetworkUris': [],
        'fcoeNetworkUris': make_range_list(2, 9, 'fcoe-'),
        'lacpTimer': 'Short',
        'fcoeMlagMode': 'InterfaceAndMacBinding',
        'fcoeNetworkMlagBays': [
            {'networkUris': make_range_list(2, 5, 'fcoe-'), 'bay': '3'}, ],
        'logicalInterconnectUri': None,
        'primaryPortLocation': None,
        'manualLoginRedistributionState': 'NotSupported',
        'connectionMode': 'Auto',
        'nativeNetworkUri': None,
        'portConfigInfos': [
            {'enclosure': ENC1, 'bay': '3', 'port': 'Q5',
             'desiredSpeed': 'Auto',
             'mlagFcoePort': 'vFcMacAndInterfaceBinding'}, ]
    },
    'us1-2icm': {
        'name': 'us1-2icm',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': [],
        'fcNetworkUris': [],
        'fcoeNetworkUris': make_range_list(2, 3, 'fcoe-'),
        'lacpTimer': 'Short',
        'fcoeMlagMode': 'InterfaceAndMacBinding',
        'fcoeNetworkMlagBays': [
            {'networkUris': ['fcoe-2'], 'bay': '3'},
            {'networkUris': ['fcoe-3'], 'bay': '6'}],
        'logicalInterconnectUri': None,
        'primaryPortLocation': None,
        'manualLoginRedistributionState': 'NotSupported',
        'connectionMode': 'Auto',
        'nativeNetworkUri': None,
        'portConfigInfos': [
            {'enclosure': ENC1, 'bay': '3', 'port': 'Q3',
             'desiredSpeed': 'Auto',
             'mlagFcoePort': 'vFcMacAndInterfaceBinding'},
            {'enclosure': ENC2, 'bay': '6', 'port': 'Q2',
             'desiredSpeed': 'Auto',
             'mlagFcoePort': 'vFcMacAndInterfaceBinding'}]
    },
    'us1-32fcoea': {
        'name': 'us1-1',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': [],
        'fcNetworkUris': [],
        'fcoeNetworkUris': make_range_list(101, 109, 'fcoe-'),
        'lacpTimer': 'Short',
        'logicalInterconnectUri': None,
        'primaryPortLocation': None,
        'manualLoginRedistributionState': 'NotSupported',
        'connectionMode': 'Auto',
        'nativeNetworkUri': None,
        'portConfigInfos': [
            {'enclosure': ENC1, 'bay': '3', 'port': 'Q3',
             'desiredSpeed': 'Auto'},
            {'enclosure': ENC1, 'bay': '3', 'port': 'Q4',
             'desiredSpeed': 'Auto'}]
    },
    'us3': {
        'name': 'us3',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': [],
        'fcNetworkUris': [],
        'fcoeNetworkUris': make_range_list(109, 115, 'fcoe-'),
        'lacpTimer': 'Short',
        'logicalInterconnectUri': None,
        'primaryPortLocation': None,
        'manualLoginRedistributionState': 'NotSupported',
        'connectionMode': 'Auto',
        'nativeNetworkUri': None,
        'portConfigInfos': [
            {'enclosure': ENC1, 'bay': '3', 'port': 'Q3',
             'desiredSpeed': 'Auto'},
            {'enclosure': ENC1, 'bay': '3', 'port': 'Q2',
             'desiredSpeed': 'Auto'}]
    },
    'us1-remove-uplink-port': {
        'name': 'us1',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': [],
        'fcNetworkUris': [],
        'fcoeNetworkUris': make_range_list(1001, 1032, 'fcoe-'),
        'lacpTimer': 'Short',
        'logicalInterconnectUri': None,
        'primaryPortLocation': None,
        'manualLoginRedistributionState': 'NotSupported',
        'connectionMode': 'Auto',
        'nativeNetworkUri': None,
        'portConfigInfos': [
            {'enclosure': ENC1, 'bay': '3', 'port': 'Q1',
             'desiredSpeed': 'Auto'}]
    },
    'us-1-fcoe': {
        'name': 'us-1-fcoe',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': [],
        'fcNetworkUris': [],
        'fcoeNetworkUris': ['fcoe-100'],
        'lacpTimer': 'Short',
        'logicalInterconnectUri': None,
        'primaryPortLocation': None,
        'manualLoginRedistributionState': 'NotSupported',
        'connectionMode': 'Auto',
        'nativeNetworkUri': None,
        'portConfigInfos': [
            {'enclosure': ENC1, 'bay': '3', 'port': 'Q5',
             'desiredSpeed': 'Auto'}]
    },
    'us-16-fcoe': {
        'name': 'us-16-fcoe',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': [],
        'fcNetworkUris': [],
        'fcoeNetworkUris': make_range_list(1017, 1032, 'fcoe-'),
        'lacpTimer': 'Short',
        'logicalInterconnectUri': None,
        'primaryPortLocation': None,
        'manualLoginRedistributionState': 'NotSupported',
        'connectionMode': 'Auto',
        'nativeNetworkUri': None,
        'portConfigInfos': [
            {'enclosure': ENC2, 'bay': '6', 'port': 'Q4',
             'desiredSpeed': 'Auto'}]
    },
    'us-33-fcoe': {
        'name': 'us-33-fcoe',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': [],
        'fcNetworkUris': [],
        'fcoeNetworkUris': make_range_list(1031, 1063, 'fcoe-'),
        'lacpTimer': 'Short',
        'logicalInterconnectUri': None,
        'primaryPortLocation': None,
        'manualLoginRedistributionState': 'NotSupported',
        'connectionMode': 'Auto',
        'nativeNetworkUri': None,
        'portConfigInfos': [
            {'enclosure': ENC2, 'bay': '6', 'port': 'Q4',
             'desiredSpeed': 'Auto'}]
    },
    'us-eth': {
        'name': 'us-eth',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['network-d'],
        'fcNetworkUris': [],
        'fcoeNetworkUris': [],
        'lacpTimer': 'Short',
        'logicalInterconnectUri': None,
        'primaryPortLocation': None,
        'manualLoginRedistributionState': 'NotSupported',
        'connectionMode': 'Auto',
        'nativeNetworkUri': None,
        'portConfigInfos': [
            {'enclosure': ENC1, 'bay': '3', 'port': 'Q5',
             'desiredSpeed': 'Auto'},
            {'enclosure': ENC1, 'bay': '3', 'port': 'Q6',
             'desiredSpeed': 'Auto'}]
    },
    'us-spans-2-ics': {
        'name': 'us-spans-2-ics',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': [],
        'fcNetworkUris': [],
        'fcoeNetworkUris': ['fcoe-1108'],
        'lacpTimer': 'Short',
        'logicalInterconnectUri': None,
        'primaryPortLocation': None,
        'manualLoginRedistributionState': 'NotSupported',
        'connectionMode': 'Auto',
        'nativeNetworkUri': None,
        'portConfigInfos': [
            {'enclosure': ENC1, 'bay': '3', 'port': 'Q5',
             'desiredSpeed': 'Auto'},
            {'enclosure': ENC2, 'bay': '6', 'port': 'Q1',
             'desiredSpeed': 'Auto'}]
    },
    'us-dup-vlanId': {
        'name': 'us-dup-vlanId',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['eth-100'],
        'fcNetworkUris': [],
        'fcoeNetworkUris': ['fcoe-100'],
        'lacpTimer': 'Short',
        'logicalInterconnectUri': None,
        'primaryPortLocation': None,
        'manualLoginRedistributionState': 'NotSupported',
        'connectionMode': 'Auto',
        'nativeNetworkUri': None,
        'portConfigInfos': [
            {'enclosure': ENC2, 'bay': '6', 'port': 'Q1',
             'desiredSpeed': 'Auto'}]
    },
    'BFS': {
        'name': 'Bside-Q6-40gb',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['eth-401'],
        'fcNetworkUris': [],
        'fcoeNetworkUris': ['fcoe-1003'],
        'lacpTimer': 'Short',
        'logicalInterconnectUri': None,
        'primaryPortLocation': None,
        'manualLoginRedistributionState': 'NotSupported',
        'connectionMode': 'Auto',
        'nativeNetworkUri': None,
        'portConfigInfos': [
            {'enclosure': ENC2, 'bay': '6', 'port': 'Q6',
             'desiredSpeed': 'Auto'}]
    },
}

icmap = [
    {'bay': 3, 'enclosure': 1,
     'type': 'Virtual Connect SE 40Gb F8 Module for Synergy',
     'enclosureIndex': 1},
    {'bay': 6, 'enclosure': 1,
     'type': 'Virtual Connect SE 40Gb F8 Module for Synergy',
     'enclosureIndex': 1},
]

ligs = {
    'LIG1': {
        'name': 'LIG1',
        'type': 'logical-interconnect-groupV4',
        'enclosureType': 'SY12000',
        'interconnectMapTemplate': icmap,
        'enclosureIndexes': [1],
        'interconnectBaySet': 3,
        'uplinkSets': [uplink_sets['us1'].copy(), uplink_sets['us2'].copy()],
        'redundancyType': 'Redundant',
        'fcoeSettings': {'fcoeMode': 'FcfNpv'},
        'stackingMode': 'Enclosure',
        'ethernetSettings': None,
        'state': 'Active',
        'telemetryConfiguration': None,
        'snmpConfiguration': None
    },
    'CLIG1': {
        'name': 'ComwareLIG1',
        'type': 'logical-interconnect-groupV4',
        'enclosureType': 'SY12000',
        'interconnectMapTemplate': icmap,
        'enclosureIndexes': [1],
        'interconnectBaySet': 3,
        'redundancyType': 'Redundant',
        'fcoeSettings': {'fcoeMode': 'FcfNpv'},
        'uplinkSets': [uplink_sets['us1-comware'].copy()],
        'stackingMode': 'Enclosure',
        'ethernetSettings': None,
        'state': 'Active',
        'telemetryConfiguration': None,
        'snmpConfiguration': None
    },
    'CLIG2': {
        'name': 'ComwareLIG2-33',
        'type': 'logical-interconnect-groupV4',
        'enclosureType': 'SY12000',
        'interconnectMapTemplate': icmap,
        'enclosureIndexes': [1],
        'interconnectBaySet': 3,
        'redundancyType': 'Redundant',
        'fcoeSettings': {'fcoeMode': 'FcfNpv'},
        'uplinkSets': [uplink_sets['us1-comware-33'].copy()],
        'stackingMode': 'Enclosure',
        'ethernetSettings': None,
        'state': 'Active',
        'telemetryConfiguration': None,
        'snmpConfiguration': None
    },
    'CLIG3': {
        'name': 'ComwareLIG2-32',
        'type': 'logical-interconnect-groupV4',
        'enclosureType': 'SY12000',
        'interconnectMapTemplate': icmap,
        'enclosureIndexes': [1],
        'interconnectBaySet': 3,
        'redundancyType': 'Redundant',
        'fcoeSettings': {'fcoeMode': 'FcfNpv'},
        'uplinkSets': [uplink_sets['us1-comware-32'].copy()],
        'stackingMode': 'Enclosure',
        'ethernetSettings': None,
        'state': 'Active',
        'telemetryConfiguration': None,
        'snmpConfiguration': None
    },
    'CLIG4': {
        'name': 'ComwareLIG-17p',
        'type': 'logical-interconnect-groupV4',
        'enclosureType': 'SY12000',
        'interconnectMapTemplate': icmap,
        'enclosureIndexes': [1],
        'interconnectBaySet': 3,
        'redundancyType': 'Redundant',
        'fcoeSettings': {'fcoeMode': 'FcfNpv'},
        'uplinkSets': [uplink_sets['us1-comware-17p'].copy()],
        'stackingMode': 'Enclosure',
        'ethernetSettings': None,
        'state': 'Active',
        'telemetryConfiguration': None,
        'snmpConfiguration': None
    },
    'CLIG5': {
        'name': 'CiscoLIG1',
        'type': 'logical-interconnect-groupV4',
        'enclosureType': 'SY12000',
        'interconnectMapTemplate': icmap,
        'enclosureIndexes': [1],
        'interconnectBaySet': 3,
        'redundancyType': 'Redundant',
        'fcoeSettings': {'fcoeMode': 'FcfNpv'},
        'uplinkSets': [uplink_sets['us1-cisco-33'].copy()],
        'stackingMode': 'Enclosure',
        'ethernetSettings': None,
        'state': 'Active',
        'telemetryConfiguration': None,
        'snmpConfiguration': None
    },
    'lig3': {
        'name': 'duplicate-vlans',
        'type': 'logical-interconnect-groupV4',
        'enclosureType': 'SY12000',
        'interconnectMapTemplate': icmap,
        'enclosureIndexes': [1, 2],
        'interconnectBaySet': 3,
        'redundancyType': 'HighlyAvailable',
        'fcoeSettings': {'fcoeMode': 'FcfNpv'},
        'uplinkSets': [uplink_sets['duplicate-vlan'].copy()],
        'stackingMode': 'Enclosure',
        'ethernetSettings': None,
        'state': 'Active',
        'telemetryConfiguration': None,
        'snmpConfiguration': None
    },
    'lig4': {
        'name': 'LIG-with-more-than-64-fcoe',
        'type': 'logical-interconnect-groupV4',
        'enclosureType': 'SY12000',
        'interconnectMapTemplate': icmap,
        'enclosureIndexes': [1, 2],
        'interconnectBaySet': 3,
        'redundancyType': 'HighlyAvailable',
        'fcoeSettings': {'fcoeMode': 'FcfNpv'},
        'uplinkSets': [uplink_sets['us-32fcoe-a'].copy(),
                       uplink_sets['us-32fcoe-b'].copy(),
                       uplink_sets['us1-fcoe'].copy()],
        'stackingMode': 'Enclosure',
        'ethernetSettings': None,
        'state': 'Active',
        'telemetryConfiguration': None,
        'snmpConfiguration': None
    },
    'lig5': {
        'name': 'LIG-with-US-with-more-than-32-fcoe',
        'type': 'logical-interconnect-groupV4',
        'enclosureType': 'SY12000',
        'interconnectMapTemplate': icmap,
        'enclosureIndexes': [1, 2],
        'interconnectBaySet': 3,
        'redundancyType': 'HighlyAvailable',
        'fcoeSettings': {'fcoeMode': 'FcfNpv'},
        'uplinkSets': [uplink_sets['us33a'].copy()],
        'stackingMode': 'Enclosure',
        'ethernetSettings': None,
        'state': 'Active',
        'telemetryConfiguration': None,
        'snmpConfiguration': None
    },
    'lig6': {
        'name': 'LIG1',
        'type': 'logical-interconnect-groupV4',
        'enclosureType': 'SY12000',
        'interconnectMapTemplate': icmap,
        'enclosureIndexes': [1, 2],
        'interconnectBaySet': 3,
        'redundancyType': 'HighlyAvailable',
        'fcoeSettings': {'fcoeMode': 'FcfNpv'},
        'uplinkSets': [uplink_sets['us1a'].copy(),
                       uplink_sets['us2a'].copy(),
                       uplink_sets['us3a'].copy(),
                       uplink_sets['us-eth'].copy()],
        'stackingMode': 'Enclosure',
        'ethernetSettings': None,
        'state': 'Active',
        'telemetryConfiguration': None,
        'snmpConfiguration': None
    },
    'lig7': {
        'name': 'Invalid-LIG',
        'type': 'logical-interconnect-groupV4',
        'enclosureType': 'SY12000',
        'interconnectMapTemplate': icmap,
        'enclosureIndexes': [1, 2],
        'interconnectBaySet': 3,
        'redundancyType': 'HighlyAvailable',
        'fcoeSettings': {'fcoeMode': 'FcfNpv'},
        'uplinkSets': [uplink_sets['us10'].copy()],
        'stackingMode': 'Enclosure',
        'ethernetSettings': None,
        'state': 'Active',
        'telemetryConfiguration': None,
        'snmpConfiguration': None
    },
    'lig8': {
        'name': 'Invalid-LIG',
        'type': 'logical-interconnect-groupV4',
        'enclosureType': 'SY12000',
        'interconnectMapTemplate': icmap,
        'enclosureIndexes': [1, 2],
        'interconnectBaySet': 3,
        'redundancyType': 'HighlyAvailable',
        'fcoeSettings': {'fcoeMode': 'FcfNpv'},
        'uplinkSets': [uplink_sets['duplicate-vlan-eth'].copy()],
        'stackingMode': 'Enclosure',
        'ethernetSettings': None,
        'state': 'Active',
        'telemetryConfiguration': None,
        'snmpConfiguration': None
    },
    'lig9': {
        'name': 'LIG1',
        'type': 'logical-interconnect-groupV4',
        'enclosureType': 'SY12000',
        'interconnectMapTemplate': icmap,
        'enclosureIndexes': [1, 2],
        'interconnectBaySet': 3,
        'redundancyType': 'HighlyAvailable',
        'fcoeSettings': {'fcoeMode': 'FcfNpv'},
        'uplinkSets': [uplink_sets['us-32fcoe-a'].copy()],
        'stackingMode': 'Enclosure',
        'ethernetSettings': None,
        'state': 'Active',
        'telemetryConfiguration': None,
        'snmpConfiguration': None
    },
    'q1-q8': {
        'name': 'Invalid-LIG-Q1-Q8',
        'type': 'logical-interconnect-groupV4',
        'enclosureType': 'SY12000',
        'interconnectMapTemplate': icmap,
        'enclosureIndexes': [1, 2],
        'interconnectBaySet': 3,
        'redundancyType': 'HighlyAvailable',
        'fcoeSettings': {'fcoeMode': 'FcfNpv'},
        'uplinkSets': [uplink_sets['Q1-Q8'].copy()],
        'stackingMode': 'Enclosure',
        'ethernetSettings': None,
        'state': 'Active',
        'telemetryConfiguration': None,
        'snmpConfiguration': None
    },
    'IBS3-HA-Both': {
        'name': 'IBS3-HA-Both',
        'type': 'logical-interconnect-groupV4',
        'enclosureType': 'SY12000',
        'interconnectMapTemplate': [
            {'bay': 3, 'enclosure': 1,
             'type': 'Virtual Connect SE 40Gb F8 Module for Synergy',
             'enclosureIndex': 1},
            {'bay': 6, 'enclosure': 2,
             'type': 'Virtual Connect SE 40Gb F8 Module for Synergy',
             'enclosureIndex': 2},
            {'bay': 6, 'enclosure': 1,
             'type': 'Synergy 20Gb Interconnect Link Module',
             'enclosureIndex': 1},
            {'bay': 3, 'enclosure': 2,
             'type': 'Synergy 20Gb Interconnect Link Module',
             'enclosureIndex': 2}],
        'enclosureIndexes': [1, 2],
        'interconnectBaySet': 3,
        'redundancyType': 'HighlyAvailable',
        'fcoeSettings': {'fcoeMode': 'FcfNpv'},
        'uplinkSets': [uplink_sets['AsideIBS3'].copy(),
                       uplink_sets['BsideIBS3'].copy()],
        'stackingMode': 'Enclosure',
        'ethernetSettings': None,
        'state': 'Active',
        'telemetryConfiguration': None,
        'snmpConfiguration': None
    },
    'IBS3-HA-Comware': {
        'name': 'IBS3-HA-Comware',
        'type': 'logical-interconnect-groupV4',
        'enclosureType': 'SY12000',
        'interconnectMapTemplate': [
            {'bay': 3, 'enclosure': 1,
             'type': 'Virtual Connect SE 40Gb F8 Module for Synergy',
             'enclosureIndex': 1},
            {'bay': 6, 'enclosure': 2,
             'type': 'Virtual Connect SE 40Gb F8 Module for Synergy',
             'enclosureIndex': 2},
            {'bay': 6, 'enclosure': 1,
             'type': 'Synergy 20Gb Interconnect Link Module',
             'enclosureIndex': 1},
            {'bay': 3, 'enclosure': 2,
             'type': 'Synergy 20Gb Interconnect Link Module',
             'enclosureIndex': 2}],
        'enclosureIndexes': [1, 2],
        'interconnectBaySet': 3,
        'redundancyType': 'HighlyAvailable',
        'fcoeSettings': {'fcoeMode': 'FcfNpv'},
        'uplinkSets': [uplink_sets['AsideIBS3'].copy()],
        'stackingMode': 'Enclosure',
        'ethernetSettings': None,
        'state': 'Active',
        'telemetryConfiguration': None,
        'snmpConfiguration': None
    },
    'IBS3-HA-Cisco': {
        'name': 'IBS3-HA-Cisco',
        'type': 'logical-interconnect-groupV4',
        'enclosureType': 'SY12000',
        'interconnectMapTemplate': [
            {'bay': 3, 'enclosure': 1,
             'type': 'Virtual Connect SE 40Gb F8 Module for Synergy',
             'enclosureIndex': 1},
            {'bay': 6, 'enclosure': 2,
             'type': 'Virtual Connect SE 40Gb F8 Module for Synergy',
             'enclosureIndex': 2},
            {'bay': 6, 'enclosure': 1,
             'type': 'Synergy 20Gb Interconnect Link Module',
             'enclosureIndex': 1},
            {'bay': 3, 'enclosure': 2,
             'type': 'Synergy 20Gb Interconnect Link Module',
             'enclosureIndex': 2}],
        'enclosureIndexes': [1, 2],
        'interconnectBaySet': 3,
        'redundancyType': 'HighlyAvailable',
        'fcoeSettings': {'fcoeMode': 'FcfNpv'},
        'uplinkSets': [uplink_sets['BsideIBS3'].copy()],
        'stackingMode': 'Enclosure',
        'ethernetSettings': None,
        'state': 'Active',
        'telemetryConfiguration': None,
        'snmpConfiguration': None
    },
    'BFS': {
        'name': 'LIG1',
        'type': 'logical-interconnect-groupV4',
        'enclosureType': 'SY12000',
        'interconnectMapTemplate': [
            {'bay': 3, 'enclosure': 1,
             'type': 'Virtual Connect SE 40Gb F8 Module for Synergy',
             'enclosureIndex': 1},
            {'bay': 6, 'enclosure': 2,
             'type': 'Virtual Connect SE 40Gb F8 Module for Synergy',
             'enclosureIndex': 2},
            {'bay': 6, 'enclosure': 1,
             'type': 'Synergy 10Gb Interconnect Link Module',
             'enclosureIndex': 1},
            {'bay': 3, 'enclosure': 2,
             'type': 'Synergy 10Gb Interconnect Link Module',
             'enclosureIndex': 2}],
        'enclosureIndexes': [1, 2],
        'interconnectBaySet': 3,
        'redundancyType': 'HighlyAvailable',
        'fcoeSettings': {'fcoeMode': 'FcfNpv'},
        'uplinkSets': [uplink_sets['BsideIBS3'].copy()],
        'stackingMode': 'Enclosure',
        'ethernetSettings': None,
        'state': 'Active',
        'telemetryConfiguration': None,
        'snmpConfiguration': None
    },
}

telemetry = {'enableTelemetry': True, 'sampleInterval': 400, 'sampleCount': 20}

trapDestinations = [{'trapSeverities': ['Major'],
                     'enetTrapCategories': ['Other'],
                     'fcTrapCategories': ['Other'],
                     'vcmTrapCategories': ['Legacy'],
                     'trapFormat': 'SNMPv1',
                     'trapDestination': '192.168.99.99',
                     'communityString': 'public'}]

snmp = {'snmpAccess': ['192.168.1.0/24'],
        'trapDestinations': trapDestinations}

enet = {'enableFastMacCacheFailover': False}

"""
0 = Windows
1 = Esxi 6
2 = RHEL 6.7
"""
aside_connections = [
    {'id': 1, 'name': '1a', 'functionType': 'Ethernet',
     'portId': 'Mezz 3:1-a',
     'requestedMbps': '2500',
     'networkUri': 'ETH:net_1010',
     'boot': {'priority': 'NotBootable'}},
    {'id': 2, 'name': '2a', 'functionType': 'FibreChannel',
     'portId': 'Mezz 3:1-b',
     'requestedMbps': '2500',
     'networkUri': 'FCOE:fcoe-30',
     'wwpnType': 'UserDefined',
     'wwpn': '10:00:aa:33:7f:f0:00:00',
     'wwnn': '10:00:aa:33:7f:f0:00:01',
     'mac': 'DE:59:B8:A0:00:03',
     'boot': {'priority': 'Primary',
              'bootVolumeSource': 'UserDefined',
              'targets': [{
                          'arrayWwpn': '20:23:00:02:ac:01:d4:db',
                          'lun': '0'}]}},
    {'id': 3, 'name': '3a', 'functionType': 'Ethernet',
     'portId': 'Mezz 3:1-c',
     'requestedMbps': '2500',
     'networkUri': 'ETH:net_1011',
     'boot': {'priority': 'NotBootable'}},
    {'id': 4, 'name': '4a', 'functionType': 'Ethernet',
     'portId': 'Mezz 3:1-d',
     'requestedMbps': '2500',
     'networkUri': 'ETH:net_1012',
     'boot': {'priority': 'NotBootable'}},
    {'id': 5, 'name': '1b', 'functionType': 'Ethernet',
     'portId': 'Mezz 3:2-a',
     'requestedMbps': '2500',
     'networkUri': 'ETH:net_1010',
     'boot': {'priority': 'NotBootable'}},
    {'id': 6, 'name': '2b', 'functionType': 'FibreChannel',
     'portId': 'Mezz 3:2-b',
     'requestedMbps': '2500',
     'networkUri': 'FCOE:fcoe-40',
     'wwpnType': 'UserDefined',
     'wwpn': '10:00:aa:33:7f:f0:00:06',
     'wwnn': '10:00:aa:33:7f:f0:00:07',
     'mac': 'DE:59:B8:A0:00:0e',
     'boot': {'priority': 'Secondary',
              'bootVolumeSource': 'UserDefined',
              'targets': [{
                          'arrayWwpn': '20:23:00:02:ac:01:d4:db',
                          'lun': '0'}]}},
    {'id': 7, 'name': '3b', 'functionType': 'Ethernet',
     'portId': 'Mezz 3:2-c',
     'requestedMbps': '2500',
     'networkUri': 'ETH:net_1011',
     'boot': {'priority': 'NotBootable'}},
    {'id': 8, 'name': '4b', 'functionType': 'Ethernet',
     'portId': 'Mezz 3:2-d',
     'requestedMbps': '2500',
     'networkUri': 'ETH:net_1012',
     'boot': {'priority': 'NotBootable'}},
]

aside_connections_2 = [
    {'id': 1, 'name': '1a', 'functionType': 'Ethernet',
     'portId': 'Mezz 3:1-a',
     'requestedMbps': '2500',
     'networkUri': 'ETH:net_1010',
     'boot': {'priority': 'NotBootable'}},
    {'id': 2, 'name': '2a', 'functionType': 'FibreChannel',
     'portId': 'Mezz 3:1-b',
     'requestedMbps': '2500',
     'networkUri': 'FCOE:fcoe-30',
     'wwpnType': 'UserDefined',
     'wwpn': '10:00:aa:33:7f:f0:00:02',
     'wwnn': '10:00:aa:33:7f:f0:00:03',
     'mac': 'DE:59:B8:A0:00:06',
     'boot': {'priority': 'Primary',
              'bootVolumeSource': 'UserDefined',
              'targets': [{
                          'arrayWwpn': '20:23:00:02:ac:01:d4:db',
                          'lun': '0'}]}},
    {'id': 3, 'name': '3a', 'functionType': 'Ethernet',
     'portId': 'Mezz 3:1-c',
     'requestedMbps': '2500',
     'networkUri': 'ETH:net_1011',
     'boot': {'priority': 'NotBootable'}},
    {'id': 4, 'name': '4a', 'functionType': 'Ethernet',
     'portId': 'Mezz 3:1-d',
     'requestedMbps': '2500',
     'networkUri': 'ETH:net_1012',
     'boot': {'priority': 'NotBootable'}},
    {'id': 5, 'name': '1b', 'functionType': 'Ethernet',
     'portId': 'Mezz 3:2-a',
     'requestedMbps': '2500',
     'networkUri': 'ETH:net_1010',
     'boot': {'priority': 'NotBootable'}},
    {'id': 6, 'name': '2b', 'functionType': 'FibreChannel',
     'portId': 'Mezz 3:2-b',
     'requestedMbps': '2500',
     'networkUri': 'FCOE:fcoe-40',
     'wwpnType': 'UserDefined',
     'wwpn': '10:00:aa:33:7f:f0:00:04',
     'wwnn': '10:00:aa:33:7f:f0:00:05',
     'mac': 'DE:59:B8:A0:00:0A',
     'boot': {'priority': 'Secondary',
              'bootVolumeSource': 'UserDefined',
              'targets': [{
                          'arrayWwpn': '20:23:00:02:ac:01:d4:db',
                          'lun': '0'}]}},
    {'id': 7, 'name': '3b', 'functionType': 'Ethernet',
     'portId': 'Mezz 3:2-c',
     'requestedMbps': '2500',
     'networkUri': 'ETH:net_1011',
     'boot': {'priority': 'NotBootable'}},
    {'id': 8, 'name': '4b', 'functionType': 'Ethernet',
     'portId': 'Mezz 3:2-d',
     'requestedMbps': '2500',
     'networkUri': 'ETH:net_1012',
     'boot': {'priority': 'NotBootable'}},
]
bside_connections = [
    {'id': 1, 'name': '1', 'functionType': 'Ethernet',
     'portId': 'Mezz 3:2-a',
     'requestedMbps': '2500',
     'networkUri': 'ETH:net_1010',
     'boot': {'priority': 'NotBootable'}},
    {'id': 2, 'name': '2', 'functionType': 'FibreChannel',
     'portId': 'Mezz 3:2-b',
     'requestedMbps': '2500',
     'networkUri': 'FCOE:fcoe-40',
     'boot': {'priority': 'NotBootable'}},
    {'id': 3, 'name': '3', 'functionType': 'Ethernet',
     'portId': 'Mezz 3:2-c',
     'requestedMbps': '2500',
     'networkUri': 'ETH:net_1011',
     'boot': {'priority': 'NotBootable'}},
    {'id': 4, 'name': '4', 'functionType': 'Ethernet',
     'portId': 'Mezz 3:2-d',
     'requestedMbps': '2500',
     'networkUri': 'ETH:net_1012',
     'boot': {'priority': 'NotBootable'}},
]
server_profiles = [
    {'type': 'ServerProfileV10',
     'serverHardwareUri': ENC1 + ', bay 1',
     'serverHardwareTypeUri': '',
     'enclosureUri': 'ENC:' + ENC1,
     'enclosureGroupUri': 'EG:%s' % EG2,
     'serialNumberType': 'Virtual',
     'macType': 'Virtual', 'wwnType': 'Virtual',
     'name': ENC1 + '_Bay1-BFS',
     'description': 'Blackbird - Aside',
     'affinity': 'Bay',
     'bootMode':
         {'manageMode': True, 'mode': 'UEFI',
          'pxeBootPolicy': 'Auto'},
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'connectionSettings': {'connections': aside_connections},
     },
    {'type': 'ServerProfileV10',
     'serverHardwareUri': ENC2 + ', bay 1',
     'serverHardwareTypeUri': '',
     'enclosureUri': 'ENC:' + ENC2,
     'enclosureGroupUri': 'EG:%s' % EG2,
     'serialNumberType': 'Virtual',
     'macType': 'Virtual', 'wwnType': 'Virtual',
     'name': ENC2 + '_Bay1-BFS',
     'description': 'Blackbird - Aside',
     'affinity': 'Bay',
     'bootMode':
         {'manageMode': True, 'mode': 'UEFI',
          'pxeBootPolicy': 'Auto'},
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'connectionSettings': {'connections': aside_connections_2},
     },
]

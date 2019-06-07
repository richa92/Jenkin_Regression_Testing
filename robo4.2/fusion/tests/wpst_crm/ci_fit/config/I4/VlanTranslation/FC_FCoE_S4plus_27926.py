"""
Fusion 3.0 Vlan Tranlation configuration on 2 frame ME (Eagle 47 and 48) with fully load 24 servers
Test ID: 27926: Scenario 4 Plus - Unique Network Set for each of 4 PFs per port Eth  + FC + FCoE
"""

def make_range_list(vrange):
    rlist = []
    for x in xrange(vrange['start'], (vrange['end'] + 1)):
        rlist.append(vrange['prefix'] + str(x) + vrange['suffix'])
    return rlist


def rlist(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist

"""
This is the root user password for ssh access to OV.
"""
SSH_PASS = 'hpvse1'

"""
These are the credentials for the Administrator account.  The password specified here is used during FTS
as you are forced to change the password
"""
admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

"""
These are the credentials for the root account.  The password specified here is used during Tbird
hardware setup via ssh.
"""
ssh_credentials = {'userName': 'root', 'password': 'hpvse1'}
#DCS ssh_credentials = {'userName': 'root', 'password': 'hponeview'}

"""
This is the Appliance Network Configuration Data used during FTS for a non-clustered config (valid for C7000 and Tbird).
STATIC
"""

appliance = {'type': 'ApplianceNetworkConfiguration',
             'applianceNetworks':
             [{'device': 'eth0',
               'macAddress': None,
               'interfaceName': 'hpqcorpnet',
               'activeNode': '1',
               'unconfigure': False,
               'ipv4Type': 'STATIC',
               'ipv4Subnet': '255.255.224.0',
               'ipv4Gateway': '15.186.0.1',
               'ipv4NameServers': ['16.110.135.51', '16.110.135.52'],
               'app1Ipv4Addr': '15.186.10.47',
               'app2Ipv4Addr': '15.186.11.47',
               'virtIpv4Addr': '15.186.9.47',
               'ipv6Type': 'UNCONFIGURE',
               'hostname': 'ci-manager-eagle47.us.rdlabs.hpecorp.net',
               'confOneNode': True,
               'domainName': 'usa.hp.com',
               'aliasDisabled': True,
               }],
             }

"""
This is the Appliance Network Configuration Data used during FTS for a non-clustered config (valid for C7000 and Tbird).  
DHCP
"""

"""
This is the time and locale settings used during FTS.
"""
timeandlocale = {'type': 'TimeAndLocale', 'dateTime': None, 'timezone': 'UTC', 'ntpServers': ['ntp.hp.net'], 'locale': 'en_US.UTF-8'}

"""
These are the virtual address ranges for MAC, WWN and SERIAL numbers
"""
ranges = [{'name': 'Eagle47-MAC', 'type': 'Range', 'category': 'id-range-VMAC', 'rangeCategory': 'CUSTOM', 'startAddress': 'B2:66:66:00:00:29', 'endAddress': 'B2:66:66:0F:FF:FF', 'enabled': True},
#mle          {'name': 'Eagle47-WWN', 'type': 'Range', 'category': 'id-range-VWWN', 'rangeCategory': 'CUSTOM', 'startAddress': '53:33:3C:33:00:00:00:00', 'endAddress': '53:33:3C:33:00:0F:FF:FF', 'enabled': True},
          {'name': 'Eagle47-WWN', 'type': 'Range', 'category': 'id-range-VWWN', 'rangeCategory': 'CUSTOM', 'startAddress': '59:99:9C:99:00:00:00:00', 'endAddress': '59:99:9C:99:00:0F:FF:FF', 'enabled': True},
          {'name': 'Eagle47-SN', 'type': 'Range', 'category': 'id-range-VSN', 'rangeCategory': 'CUSTOM', 'startAddress': 'VCUQQQ0005', 'endAddress': 'VCUQQQ0ZZZ', 'enabled': True}]

"""
These are the users you want to create on the appliance
"""
users = [{'userName': 'Serveradmin', 'password': 'Serveradmin', 'fullName': 'Serveradmin', 'roles': ['Server administrator'], 'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'Networkadmin', 'password': 'Networkadmin', 'fullName': 'Networkadmin', 'roles': ['Network administrator'], 'emailAddress': 'nat@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'Backupadmin', 'password': 'Backupadmin', 'fullName': 'Backupadmin', 'roles': ['Backup administrator'], 'emailAddress': 'backup@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'Noprivledge', 'password': 'Noprivledge', 'fullName': 'Noprivledge', 'roles': ['Read only'], 'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'}
        ]

"""
These are the Licenses you want to add to the appliance
"""
licenses = [{'key': 'YCDC D9MA H9PQ KHX2 V7B5 HWWB Y9JL KMPL TA2E PDRA DXAU 2CSM GHTG L762 HUK7 GB5M KJVT D5KM EFRW DS5R TXXK 6Q22 AK2P 3EW2 AJQ4 HU5V TZZH AB6X 82Z5 WHEF GE4C LUE3 BKT8 WXDG NK6Y C4GA HZL4 XBE7 3VJ6 2MSU 4ZU9 9WGG CZU7 WE4X YN44 CH55 KZLG 2F4N A8RJ UKEC 3F9V JQY5 "423542007 HPOV-NFR1 HP_OneView_16_Seat_NFR 75YYJJECU46C"_3DWNY-6B2KD-D8Z6S-6YR4B-K8GDW'},
            {'key': '9B3C A99A H9P9 GHUZ U7B5 HWW5 Y9JL KMPL 5AWA 8CBE DXAU 2CSM GHTG L762 7NGZ GDV4 KJVT D5KM EFRW DS5R 5XP8 4XK2 GNSL 9F82 7JKT QVXB XZKH ABB4 NV2C LHXU KN7U 5NA6 BKRK 35QB D8UW R42A X3BN LQ6M 5V9A PM6Q 4MN9 9GGS EZU7 GEMX VUJW CDB5 JVRX 8HEN 2J98 ACPB "TKOPREN HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR ATJUJJEDAT2Y"'},
            {'key': 'YBKA D9MA H9P9 8HX3 V2B4 HWWV Y9JL KMPL B89H MZVU GR4S JHWE J2SP XNZ8 CMRG HPMR UFVU A5K9 MWHC 9K4K HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'},
            {'key': '9B2G D9MA H9PA CHVZ V2B4 HWWV Y9JL KMPL B89H MZVU 6RMS 9HWE 92R6 3FZ3 CMRG HPMR MFVU A5K9 MHGK EKX9 HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'}
           ]

"""
These are the ETHERNET networks you want to add to the appliance
"""


ethernet_networks = [
    {
        "type": "ethernet-networkV300",
        "ethernetNetworkType": "Untagged",
        "name": "IC",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": False,
        "vlanId": 0
    },
    {
        "type": "ethernet-networkV300",
        "ethernetNetworkType": "Untagged",
        "name": "1-Untagged",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": False,
        "vlanId": 0
    },
    {
        "type": "ethernet-networkV300",
        "ethernetNetworkType": "Tunnel",
        "name": "1-Tunnel",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": False,
        "vlanId": 0
    },
    {
        "type": "ethernet-networkV300",
        "ethernetNetworkType": "Tunnel",
        "name": "2-Tunnel",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": False,
        "vlanId": 0
    },
    {
        "type": "ethernet-networkV300",
        "ethernetNetworkType": "Untagged",
        "name": "2-Untagged",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": False,
        "vlanId": 0
    }
]

"""
These are the RANGES of ETHERNET networks you want to add to the appliance.
"""
ethernet_ranges = [
                   {'prefix': 'net_', 'suffix': '', 'start': 2, 'end': 3966, 'name': None, 'type': 'ethernet-networkV300',
                    'vlanId': None, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False, 'connectionTemplateUri': None,
                    'ethernetNetworkType': 'Tagged'},
                  ]

"""
These are the network sets you want to add to the appliance.
NOTE: There are 2 fields that use data that MUST have also been defined in either 'ethernet_networks' or 'ethernet_ranges' above:
 networkUris = a list of network names that you want to include in the set.  Example ['net1', 'net2']
 nativeNetworkUri = a string with only 1 network name to use as the native network
"""
network_sets = [
                {'name': 'NW-1', 'type': 'network-setV300', 'networkUris': rlist(2,163,'net_',''), 'nativeNetworkUri': 'None'},
                {'name': 'NW-2', 'type': 'network-setV300', 'networkUris': rlist(164,325,'net_',''), 'nativeNetworkUri': 'None'},
                {'name': 'NW-3', 'type': 'network-setV300', 'networkUris': rlist(326,487,'net_',''), 'nativeNetworkUri': 'None'},
                {'name': 'NW-4', 'type': 'network-setV300', 'networkUris': rlist(488,649,'net_',''), 'nativeNetworkUri': 'None'},
                {'name': 'NW-5', 'type': 'network-setV300', 'networkUris': rlist(650,811,'net_',''), 'nativeNetworkUri': 'None'},
                {'name': 'NW-6', 'type': 'network-setV300', 'networkUris': rlist(812,973,'net_',''), 'nativeNetworkUri': 'None'},
                {'name': 'NW-7', 'type': 'network-setV300', 'networkUris': rlist(974,1135,'net_',''), 'nativeNetworkUri': 'None'},
                {'name': 'NW-8', 'type': 'network-setV300', 'networkUris': rlist(1136,1297,'net_',''), 'nativeNetworkUri': 'None'},
                {'name': 'NW-9', 'type': 'network-setV300', 'networkUris': rlist(1298,1459,'net_',''), 'nativeNetworkUri': 'None'},
                {'name': 'NW-10', 'type': 'network-setV300', 'networkUris': rlist(1460,1621,'net_',''), 'nativeNetworkUri': 'None'},
                {'name': 'NW-11', 'type': 'network-setV300', 'networkUris': rlist(1622,1783,'net_',''), 'nativeNetworkUri': 'None'},
                {'name': 'NW-12', 'type': 'network-setV300', 'networkUris': rlist(1784,1945,'net_',''), 'nativeNetworkUri': 'None'},
                {'name': 'NW-13', 'type': 'network-setV300', 'networkUris': rlist(1946,2107,'net_',''), 'nativeNetworkUri': 'None'},
                {'name': 'NW-14', 'type': 'network-setV300', 'networkUris': rlist(2108,2269,'net_',''), 'nativeNetworkUri': 'None'},
                {'name': 'NW-15', 'type': 'network-setV300', 'networkUris': rlist(2270,2431,'net_',''), 'nativeNetworkUri': 'None'},
                {'name': 'NW-16', 'type': 'network-setV300', 'networkUris': rlist(2432,2593,'net_',''), 'nativeNetworkUri': 'None'},
                {'name': 'NW-17', 'type': 'network-setV300', 'networkUris': rlist(2594,2755,'net_',''), 'nativeNetworkUri': 'None'},
                {'name': 'NW-18', 'type': 'network-setV300', 'networkUris': rlist(2756,2917,'net_',''), 'nativeNetworkUri': 'None'},
                {'name': 'NW-19', 'type': 'network-setV300', 'networkUris': rlist(2918,3063,'net_','') + rlist(3066,3079,'net_',''), 'nativeNetworkUri': 'None'},
                {'name': 'NW-20', 'type': 'network-setV300', 'networkUris': rlist(3080,3241,'net_',''), 'nativeNetworkUri': 'None'},
                {'name': 'NW-21', 'type': 'network-setV300', 'networkUris': rlist(3242,3403,'net_',''), 'nativeNetworkUri': 'None'},
                {'name': 'NW-22', 'type': 'network-setV300', 'networkUris': rlist(3404,3565,'net_',''), 'nativeNetworkUri': 'None'},
                {'name': 'NW-23', 'type': 'network-setV300', 'networkUris': rlist(3566,3727,'net_',''), 'nativeNetworkUri': 'None'},
                {'name': 'NW-24', 'type': 'network-setV300', 'networkUris': rlist(3728,3889,'net_',''), 'nativeNetworkUri': 'None'},
#                {'name': 'NW-25', 'type': 'network-setV300', 'networkUris': rlist(2,88,'net_','') + rlist(3890,3902,'net_',''), 'nativeNetworkUri': 'None'},
                {'name': 'NW-25', 'type': 'network-setV300', 'networkUris': rlist(2,88,'net_','') + rlist(3890,3964,'net_',''), 'nativeNetworkUri': 'None'},
                {'name': 'NW-26', 'type': 'network-setV300', 'networkUris': rlist(2,2,'net_','') + rlist(3965,3965,'net_',''), 'nativeNetworkUri': 'None'},
                {'name': 'NW-27-14', 'type': 'network-setV300', 'networkUris': rlist(992,1005,'net_',''), 'nativeNetworkUri': 'None'},
                {'name': 'NW-28-14', 'type': 'network-setV300', 'networkUris': rlist(1001,1014,'net_',''), 'nativeNetworkUri': 'None'},
                {'name': 'NW-29-14', 'type': 'network-setV300', 'networkUris': rlist(1006,1019,'net_',''), 'nativeNetworkUri': 'None'},
                {'name': 'NW-30-14', 'type': 'network-setV300', 'networkUris': rlist(3952,3965,'net_',''), 'nativeNetworkUri': 'None'},
#                {'name': 'NW-30-15', 'type': 'network-setV300', 'networkUris': rlist(3951,3965,'net_',''), 'nativeNetworkUri': 'None'},
                ]

"""
These are the FibreChannel networks you want to add to the appliance
"""
fc_networks = [{'name': 'FC_FCoE-A', 'type': 'fc-networkV300', 'linkStabilityTime': 30, 'autoLoginRedistribution': True, 'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'},
               {'name': 'FC_FCoE-B', 'type': 'fc-networkV300', 'linkStabilityTime': 30, 'autoLoginRedistribution': True, 'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'},
               {'name': 'FC-A', 'type': 'fc-networkV300', 'linkStabilityTime': 30, 'autoLoginRedistribution': True, 'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'},
               {'name': 'FC-B', 'type': 'fc-networkV300', 'linkStabilityTime': 30, 'autoLoginRedistribution': True, 'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'}
              ]

"""
These are the FCoE networks you want to add to the appliance
"""
fcoe_networks = [{'name': 'FCoE-A-3064', 'type': 'fcoe-networkV300', 'vlanId': 3064},
                 {'name': 'FCoE-B-3065', 'type': 'fcoe-networkV300', 'vlanId': 3065},
                ]

"""
These are the RANGES of FCoE networks you want to add to the appliance.
"""
#fcoe_ranges = [{'prefix': 'FCOE-', 'suffix': 'A', 'start': 1001, 'end': 1032},
#               {'prefix': 'FCOE-', 'suffix': 'B', 'start': 1001, 'end': 1032},
#              ]
#                                      ]


"""
# Synergy
These are the enclosure group(s) you want to add to the appliance.
NOTE:  There are some special fields:
 enclosureTypeUri = /rest/enclosure-types/SY12000
 logicalInterconnectGroupUri = for each ic bay, you must specify 'LIG:' + the name of the LIG for that bay
                               The LIG you choose MUST be defined in your datafile (or exist on the appliance)
 enclosureCount = The number of enclosures in the group
"""

enc_groups = [{'name': 'EG-2ME',
               'type': 'EnclosureGroupV300',
               'enclosureCount': 2,
               'enclosureTypeUri': '/rest/enclosure-types/SY12000',
               'stackingMode': 'Enclosure',
               'interconnectBayMappingCount': 6,
               'configurationScript': None,
               'interconnectBayMappings':
               [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG-2ME'},
                {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG-2ME'}],
               'ipAddressingMode': "DHCP",
               'ipRangeUris': [],
               'powerMode': "RedundantPowerFeed"
               }
              ]




"""OLD
enc_groups = [{'name': 'EG-2ME',
               'type': 'EnclosureGroupV300',
               'enclosureCount': 2,
               'enclosureTypeUri': '/rest/enclosure-types/SY12000',
               'stackingMode': 'Enclosure',
               'interconnectBayMappingCount': 6,
               'configurationScript': None,
               'interconnectBayMappings':
               [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG-2ME'},
                {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG-2ME'}],
               'ipAddressingMode': "External",
               'ipRangeUris': [],
               'powerMode': "RedundantPowerFeed"
               }
              ]
"""

"""
These are the TBird enclosure(s) you want to add to the appliance
NOTE: There is a special field:
 enclosureGroupUri = You must specify EG: + the name of the enclosure group to associate the enclosure with
                     The EG you choose MUST be defined in your datafile (or exist on the appliance)
"""

encs = [
        {'hostname': '15.186.9.47', 'username': 'Administrator', 'password': 'compaq', 'enclosureGroupUri': 'EG-2ME', 'force': False, 'licensingIntent': 'OneViewNoiLO'},
       ]


"""
The uplinkset(s) you want to use in your LIG(s)
NOTE:  There are some special fields
 networkUris = a list of network names to include in the uplinkset
 nativeNetworkUri = a string containing the name of the network you want to be the native network
"""

uplink_sets = {
            'IC': {'name': 'IC',
                        'ethernetNetworkType': 'Untagged',
                        'networkType': 'Ethernet',
                        'networkUris': ['IC'],
                        'nativeNetworkUri': None,
                        'mode': 'Auto',
                        'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q1', 'speed': 'Auto'},]},
             'FCoE-A-3064': {'name': 'FCoE-A-3064',
                           'ethernetNetworkType': 'Tagged',
                           'networkType': 'Ethernet',
                           'networkUris': ['FCoE-A-3064'],
                           'nativeNetworkUri': None,
                           'mode': 'Auto',
                           'lacpTimer': 'Short',
                           'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q5', 'speed': 'Auto'},]},					   
             'FCoE-B-3065': {'name': 'FCoE-B-3065',
                           'ethernetNetworkType': 'Tagged',
                           'networkType': 'Ethernet',
                           'networkUris': ['FCoE-B-3065'],
                           'nativeNetworkUri': None,
                           'mode': 'Auto',
                           'lacpTimer': 'Short',
                           'logicalPortConfigInfos': [{'enclosure': '2', 'bay': '6', 'port': 'Q5', 'speed': 'Auto'},]},					   
             'FC-A': {'name': 'FC-A',
                           'ethernetNetworkType': 'NotApplicable',
                           'networkType': 'FibreChannel',
                           'networkUris': ['FC-A'],
                           'nativeNetworkUri': None,
                           'mode': 'Auto',
                           'lacpTimer': None,
                           'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q6.1', 'speed': 'Auto'},]},
             'FC-B': {'name': 'FC-B',
                           'ethernetNetworkType': 'NotApplicable',
                           'networkType': 'FibreChannel',
                           'networkUris': ['FC-B'],
                           'nativeNetworkUri': None,
                           'mode': 'Auto',
                           'lacpTimer': None,
                           'logicalPortConfigInfos': [{'enclosure': '2', 'bay': '6', 'port': 'Q6.1', 'speed': 'Auto'},]},
			'UplinkSet-Q2': {'name': 'UplinkSet-Q2',
                              'ethernetNetworkType': 'Tagged',
                              'networkType': 'Ethernet',
                              'networkUris': make_range_list({'start': 2, 'end': 1000, 'prefix':'net_', 'suffix':''}),
                              'mode': 'Auto',
                              'lacpTimer': 'Long',
                              'logicalPortConfigInfos': [{'enclosure': '1','bay': '3', 'port': 'Q2', 'speed': 'Auto'},
                                                         {'enclosure': '2','bay': '6', 'port': 'Q2', 'speed': 'Auto'}]},
			'UplinkSet-Q3Q4-BigPipe': {'name': 'UplinkSet-Q3Q4-BigPipe',
                              'ethernetNetworkType': 'Tagged',
                              'networkType': 'Ethernet',
#                             'networkUris': make_range_list({'start': 1001, 'end': 3966, 'prefix':'net_', 'suffix':''}),
                              'networkUris': make_range_list({'start': 1001, 'end': 3063, 'prefix': 'net_', 'suffix': ''}) + make_range_list({'start': 3066, 'end': 3966, 'prefix': 'net_', 'suffix': ''}),
                              'mode': 'Auto',
                              'lacpTimer': 'Long',
                              'logicalPortConfigInfos': [{'enclosure': '1','bay': '3', 'port': 'Q3', 'speed': 'Auto'},
                                                         {'enclosure': '1','bay': '3', 'port': 'Q4', 'speed': 'Auto'},
                                                         {'enclosure': '2','bay': '6', 'port': 'Q3', 'speed': 'Auto'},
                                                         {'enclosure': '2','bay': '6', 'port': 'Q4', 'speed': 'Auto'}]},
			}										 

"""
The LIG(s) you want to add to the appliance
NOTE:  There are some special fields
[for TClass LIG]
 enclosureType = TClass
 enclosureIndexes = a list of integers representing the ids of each enclosure
 fcoeSettings =
    fcoeMode = either 'FcfNpv' , 'Transit', or 'NotApplicable'
 interconnectMapTemplate: an list of ICMs and their position.
    enclosure = The physical enclosure the ICM is located in
    enclosureIndex = The enclosure index of the ICM is located in (usually matches the setting in 'enclosure'
    bay = the physical bay the ICM should be in
    type = the name of the ICM type
 interconnectBaySet = an integer representing the IBS\Fabric (1 = Bay 1&4, 2 = Bay 2&5, 3 = Bay 3&6)
 redundancyType = 'Redundant', 'HighlyAvailable', 'NonRedundantASide', 'NonRedundantBSide'
 uplinkSets: an list of uplinksets to create. These are references to the dictionary keys defined previously in the uplink_set variable.
"""
ligs = [{'name': 'LIG-2ME',
         'type': 'logical-interconnect-groupV300',
         'enclosureType': 'SY12000',
         'ethernetSettings': None,
         'interconnectMapTemplate': [
                                     {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
                                     {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
                                     {'bay': 6, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
                                     {'bay': 3, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
                                    ],
         'enclosureIndexes': [1,2],
         'interconnectBaySet': 3,
         'redundancyType': 'HighlyAvailable',
         'uplinkSets': [
                       uplink_sets['IC'],
                       uplink_sets['FCoE-A-3064'],
                       uplink_sets['FCoE-B-3065'],				
                       uplink_sets['FC-A'],
                       uplink_sets['FC-B'],
                       uplink_sets['UplinkSet-Q2'],
                       uplink_sets['UplinkSet-Q3Q4-BigPipe'],
                       ],
         'stackingMode': 'Enclosure',
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None},
        ]


"""
Optional LIG variables
These variables can be used in the LIG variables above.  They are only broken out to help simplify looking at them.
"""
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
The LE(s) you want to add to the appliance TCLASS ONLY
NOTE:  There are some special fields
[TClass LE]
 enclosureUris = a list of enclosures to add to this LE - 'ENC:' + the name of the enclosure (by default the serial number of the enclosure)
 enclosureGroupUri = You must specify EG: + the name of the enclosure group to associate the enclosure with
                     The EG you choose MUST be defined in your datafile (or exist on the appliance)
"""
les = [{'name': 'LE',
		'enclosureUris': ['ENC:CN75450498','ENC:CN7545049J',],
        'enclosureGroupUri': 'EG:EG-2ME',
        'firmwareBaselineUri': None,
        'forceInstallFirmware': False
        }]

"""
Server Profile boot 'order' options are 'PXE' or 'HardDisk'.
"""
#server_profiles = [	
#                   {'type': 'ServerProfileV6', 'serverHardwareUri': 'CN75450498, bay 1',
#                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:CN75450498', 'enclosureGroupUri': 'EG:EG-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'E47-Bay1-1', 'description': '', 'affinity': 'Bay',
#                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
#                    'bootMode': {'manageMode':True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
#                    'firmware':{'manageFirmware':False,'firmwareBaselineUri':'','forceInstallFirmware':False,'firmwareInstallType':None},
#                    'bios':{'manageBios':False,'overriddenSettings':[]},
#                    'hideUnusedFlexNics':True,
#                    'iscsiInitiatorName':'',
#                    'osDeploymentSettings':None,
#                    'connections': [
#  								    {'id': 1, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 2, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 3, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '7500', 'networkUri': 'NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 4, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 5, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 6, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500', 'networkUri': 'NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 7, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '7500', 'networkUri': 'NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 8, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#                                    ]},
#                   {'type': 'ServerProfileV6', 'serverHardwareUri': 'CN75450498, bay 2',
#                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:CN75450498', 'enclosureGroupUri': 'EG:EG-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'E47-Bay2-2', 'description': '', 'affinity': 'Bay',
#                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
#                    'bootMode': {'manageMode':True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
#                    'firmware':{'manageFirmware':False,'firmwareBaselineUri':'','forceInstallFirmware':False,'firmwareInstallType':None},
#                    'bios':{'manageBios':False,'overriddenSettings':[]},
#                    'hideUnusedFlexNics':True,
#                    'iscsiInitiatorName':'',
#                    'osDeploymentSettings':None,
#                    'connections': [
#  								    {'id': 1, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 2, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 3, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '7500', 'networkUri': 'NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 4, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 5, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 6, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500', 'networkUri': 'NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 7, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '7500', 'networkUri': 'NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 8, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#                                    ]},
#                   {'type': 'ServerProfileV6', 'serverHardwareUri': 'CN75450498, bay 3',
#                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:CN75450498', 'enclosureGroupUri': 'EG:EG-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'E47-Bay3-3', 'description': '', 'affinity': 'Bay',
#                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
#                    'bootMode': {'manageMode':True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
#                    'firmware':{'manageFirmware':False,'firmwareBaselineUri':'','forceInstallFirmware':False,'firmwareInstallType':None},
#                    'bios':{'manageBios':False,'overriddenSettings':[]},
#                    'hideUnusedFlexNics':True,
#                    'iscsiInitiatorName':'',
#                    'osDeploymentSettings':None,
#                    'connections': [
#  								    {'id': 1, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 2, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 3, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '7500', 'networkUri': 'NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 4, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 5, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 6, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500', 'networkUri': 'NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 7, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '7500', 'networkUri': 'NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 8, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#                                    ]},
#                   {'type': 'ServerProfileV6', 'serverHardwareUri': 'CN75450498, bay 4',
#                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:CN75450498', 'enclosureGroupUri': 'EG:EG-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'E47-Bay4-4', 'description': '', 'affinity': 'Bay',
#                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
#                    'bootMode': {'manageMode':True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
#                    'firmware':{'manageFirmware':False,'firmwareBaselineUri':'','forceInstallFirmware':False,'firmwareInstallType':None},
#                    'bios':{'manageBios':False,'overriddenSettings':[]},
#                    'hideUnusedFlexNics':True,
#                    'iscsiInitiatorName':'',
#                    'osDeploymentSettings':None,
#                    'connections': [
#  								    {'id': 1, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 2, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 3, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '7500', 'networkUri': 'NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 4, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 5, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 6, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500', 'networkUri': 'NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 7, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '7500', 'networkUri': 'NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 8, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#                                    ]},
#                   {'type': 'ServerProfileV6', 'serverHardwareUri': 'CN75450498, bay 5',
#                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:CN75450498', 'enclosureGroupUri': 'EG:EG-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'E47-Bay5-5', 'description': '', 'affinity': 'Bay',
#                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
#                    'bootMode': {'manageMode':True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
#                    'firmware':{'manageFirmware':False,'firmwareBaselineUri':'','forceInstallFirmware':False,'firmwareInstallType':None},
#                    'bios':{'manageBios':False,'overriddenSettings':[]},
#                    'hideUnusedFlexNics':True,
#                    'iscsiInitiatorName':'',
#                    'osDeploymentSettings':None,
#                    'connections': [
#  								    {'id': 1, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 2, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 3, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '7500', 'networkUri': 'NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 4, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 5, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 6, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500', 'networkUri': 'NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 7, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '7500', 'networkUri': 'NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 8, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#                                    ]},
#                   {'type': 'ServerProfileV6', 'serverHardwareUri': 'CN75450498, bay 6',
#                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:CN75450498', 'enclosureGroupUri': 'EG:EG-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'E47-Bay6-6', 'description': '', 'affinity': 'Bay',
#                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
#                    'bootMode': {'manageMode':True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
#                    'firmware':{'manageFirmware':False,'firmwareBaselineUri':'','forceInstallFirmware':False,'firmwareInstallType':None},
#                    'bios':{'manageBios':False,'overriddenSettings':[]},
#                    'hideUnusedFlexNics':True,
#                    'iscsiInitiatorName':'',
#                    'osDeploymentSettings':None,
#                    'connections': [
#  								    {'id': 1, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 2, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 3, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '7500', 'networkUri': 'NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 4, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 5, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 6, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500', 'networkUri': 'NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 7, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '7500', 'networkUri': 'NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 8, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#                                    ]},
#                   {'type': 'ServerProfileV6', 'serverHardwareUri': 'CN75450498, bay 7',
#                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:CN75450498', 'enclosureGroupUri': 'EG:EG-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'E47-Bay7-7', 'description': '', 'affinity': 'Bay',
#                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
#                    'bootMode': {'manageMode':True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
#                    'firmware':{'manageFirmware':False,'firmwareBaselineUri':'','forceInstallFirmware':False,'firmwareInstallType':None},
#                    'bios':{'manageBios':False,'overriddenSettings':[]},
#                    'hideUnusedFlexNics':True,
#                    'iscsiInitiatorName':'',
#                    'osDeploymentSettings':None,
#                    'connections': [
#  								    {'id': 1, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 2, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 3, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '7500', 'networkUri': 'NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 4, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 5, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 6, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500', 'networkUri': 'NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 7, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '7500', 'networkUri': 'NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 8, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#                                    ]},
#                   {'type': 'ServerProfileV6', 'serverHardwareUri': 'CN75450498, bay 8',
#                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:CN75450498', 'enclosureGroupUri': 'EG:EG-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'E47-Bay8-8', 'description': '', 'affinity': 'Bay',
#                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
#                    'bootMode': {'manageMode':True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
#                    'firmware':{'manageFirmware':False,'firmwareBaselineUri':'','forceInstallFirmware':False,'firmwareInstallType':None},
#                    'bios':{'manageBios':False,'overriddenSettings':[]},
#                    'hideUnusedFlexNics':True,
#                    'iscsiInitiatorName':'',
#                    'osDeploymentSettings':None,
#                    'connections': [
#  								    {'id': 1, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 2, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 3, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '7500', 'networkUri': 'NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 4, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 5, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 6, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500', 'networkUri': 'NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 7, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '7500', 'networkUri': 'NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 8, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#                                    ]},
#                   {'type': 'ServerProfileV6', 'serverHardwareUri': 'CN75450498, bay 9',
#                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:CN75450498', 'enclosureGroupUri': 'EG:EG-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'E47-Bay9-9', 'description': '', 'affinity': 'Bay',
#                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
#                    'bootMode': {'manageMode':True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
#                    'firmware':{'manageFirmware':False,'firmwareBaselineUri':'','forceInstallFirmware':False,'firmwareInstallType':None},
#                    'bios':{'manageBios':False,'overriddenSettings':[]},
#                    'hideUnusedFlexNics':True,
#                    'iscsiInitiatorName':'',
#                    'osDeploymentSettings':None,
#                    'connections': [
#  								    {'id': 1, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 2, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 3, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '7500', 'networkUri': 'NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 4, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 5, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 6, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500', 'networkUri': 'NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 7, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '7500', 'networkUri': 'NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 8, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#                                    ]},
#                   {'type': 'ServerProfileV6', 'serverHardwareUri': 'CN75450498, bay 10',
#                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:CN75450498', 'enclosureGroupUri': 'EG:EG-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'E47-Bay10-10', 'description': '', 'affinity': 'Bay',
#                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
#                    'bootMode': {'manageMode':True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
#                    'firmware':{'manageFirmware':False,'firmwareBaselineUri':'','forceInstallFirmware':False,'firmwareInstallType':None},
#                    'bios':{'manageBios':False,'overriddenSettings':[]},
#                    'hideUnusedFlexNics':True,
#                    'iscsiInitiatorName':'',
#                    'osDeploymentSettings':None,
#                    'connections': [
#  								    {'id': 1, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 2, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 3, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '7500', 'networkUri': 'NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 4, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 5, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 6, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500', 'networkUri': 'NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 7, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '7500', 'networkUri': 'NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 8, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#                                    ]},
#                   {'type': 'ServerProfileV6', 'serverHardwareUri': 'CN75450498, bay 11',
#                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:CN75450498', 'enclosureGroupUri': 'EG:EG-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'E47-Bay11-11', 'description': '', 'affinity': 'Bay',
#                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
#                    'bootMode': {'manageMode':True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
#                    'firmware':{'manageFirmware':False,'firmwareBaselineUri':'','forceInstallFirmware':False,'firmwareInstallType':None},
#                    'bios':{'manageBios':False,'overriddenSettings':[]},
#                    'hideUnusedFlexNics':True,
#                    'iscsiInitiatorName':'',
#                    'osDeploymentSettings':None,
#                    'connections': [
#  								    {'id': 1, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 2, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 3, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '7500', 'networkUri': 'NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 4, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 5, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 6, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500', 'networkUri': 'NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 7, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '7500', 'networkUri': 'NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 8, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#                                    ]},
#                   {'type': 'ServerProfileV6', 'serverHardwareUri': 'CN75450498, bay 12',
#                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:CN75450498', 'enclosureGroupUri': 'EG:EG-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'E47-Bay12-12', 'description': '', 'affinity': 'Bay',
#                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
#                    'bootMode': {'manageMode':True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
#                    'firmware':{'manageFirmware':False,'firmwareBaselineUri':'','forceInstallFirmware':False,'firmwareInstallType':None},
#                    'bios':{'manageBios':False,'overriddenSettings':[]},
#                    'hideUnusedFlexNics':True,
#                    'iscsiInitiatorName':'',
#                    'osDeploymentSettings':None,
#                    'connections': [
#  								    {'id': 1, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 2, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 3, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '7500', 'networkUri': 'NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 4, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 5, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 6, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500', 'networkUri': 'NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 7, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '7500', 'networkUri': 'NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 8, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#                                    ]},
#                   {'type': 'ServerProfileV6', 'serverHardwareUri': 'CN7545049J, bay 1',
#                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:CN7545049J', 'enclosureGroupUri': 'EG:EG-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'E48-Bay1-13', 'description': '', 'affinity': 'Bay',
#                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
#                    'bootMode': {'manageMode':True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
#                    'firmware':{'manageFirmware':False,'firmwareBaselineUri':'','forceInstallFirmware':False,'firmwareInstallType':None},
#                    'bios':{'manageBios':False,'overriddenSettings':[]},
#                    'hideUnusedFlexNics':True,
#                    'iscsiInitiatorName':'',
#                    'osDeploymentSettings':None,
#                    'connections': [
#  								    {'id': 1, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 2, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 3, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '7500', 'networkUri': 'NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 4, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 5, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 6, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500', 'networkUri': 'NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 7, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '7500', 'networkUri': 'NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 8, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#                                    ]},
#                   {'type': 'ServerProfileV6', 'serverHardwareUri': 'CN7545049J, bay 2',
#                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:CN7545049J', 'enclosureGroupUri': 'EG:EG-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'E48-Bay2-14', 'description': '', 'affinity': 'Bay',
#                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
#                    'bootMode': {'manageMode':True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
#                    'firmware':{'manageFirmware':False,'firmwareBaselineUri':'','forceInstallFirmware':False,'firmwareInstallType':None},
#                    'bios':{'manageBios':False,'overriddenSettings':[]},
#                    'hideUnusedFlexNics':True,
#                    'iscsiInitiatorName':'',
#                    'osDeploymentSettings':None,
#                    'connections': [
#  								    {'id': 1, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 2, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 3, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '7500', 'networkUri': 'NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 4, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 5, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 6, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500', 'networkUri': 'NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 7, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '7500', 'networkUri': 'NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 8, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#                                    ]},
#                   {'type': 'ServerProfileV6', 'serverHardwareUri': 'CN7545049J, bay 3',
#                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:CN7545049J', 'enclosureGroupUri': 'EG:EG-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'E48-Bay3-15', 'description': '', 'affinity': 'Bay',
#                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
#                    'bootMode': {'manageMode':True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
#                    'firmware':{'manageFirmware':False,'firmwareBaselineUri':'','forceInstallFirmware':False,'firmwareInstallType':None},
#                    'bios':{'manageBios':False,'overriddenSettings':[]},
#                    'hideUnusedFlexNics':True,
#                    'iscsiInitiatorName':'',
#                    'osDeploymentSettings':None,
#                    'connections': [
#  								    {'id': 1, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 2, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 3, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '7500', 'networkUri': 'NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 4, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 5, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 6, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500', 'networkUri': 'NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 7, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '7500', 'networkUri': 'NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 8, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#                                    ]},
#                   {'type': 'ServerProfileV6', 'serverHardwareUri': 'CN7545049J, bay 4',
#                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:CN7545049J', 'enclosureGroupUri': 'EG:EG-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'E48-Bay4-16', 'description': '', 'affinity': 'Bay',
#                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
#                    'bootMode': {'manageMode':True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
#                    'firmware':{'manageFirmware':False,'firmwareBaselineUri':'','forceInstallFirmware':False,'firmwareInstallType':None},
#                    'bios':{'manageBios':False,'overriddenSettings':[]},
#                    'hideUnusedFlexNics':True,
#                    'iscsiInitiatorName':'',
#                    'osDeploymentSettings':None,
#                    'connections': [
#  								    {'id': 1, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 2, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 3, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '7500', 'networkUri': 'NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 4, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 5, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 6, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500', 'networkUri': 'NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 7, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '7500', 'networkUri': 'NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 8, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#                                    ]},
#                   {'type': 'ServerProfileV6', 'serverHardwareUri': 'CN7545049J, bay 5',
#                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:CN7545049J', 'enclosureGroupUri': 'EG:EG-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'E48-Bay5-17', 'description': '', 'affinity': 'Bay',
#                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
#                    'bootMode': {'manageMode':True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
#                    'firmware':{'manageFirmware':False,'firmwareBaselineUri':'','forceInstallFirmware':False,'firmwareInstallType':None},
#                    'bios':{'manageBios':False,'overriddenSettings':[]},
#                    'hideUnusedFlexNics':True,
#                    'iscsiInitiatorName':'',
#                    'osDeploymentSettings':None,
#                    'connections': [
#  								    {'id': 1, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 2, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 3, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '7500', 'networkUri': 'NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 4, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 5, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 6, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500', 'networkUri': 'NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 7, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '7500', 'networkUri': 'NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 8, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#                                    ]},
#                   {'type': 'ServerProfileV6', 'serverHardwareUri': 'CN7545049J, bay 6',
#                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:CN7545049J', 'enclosureGroupUri': 'EG:EG-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'E48-Bay6-18', 'description': '', 'affinity': 'Bay',
#                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
#                    'bootMode': {'manageMode':True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
#                    'firmware':{'manageFirmware':False,'firmwareBaselineUri':'','forceInstallFirmware':False,'firmwareInstallType':None},
#                    'bios':{'manageBios':False,'overriddenSettings':[]},
#                    'hideUnusedFlexNics':True,
#                    'iscsiInitiatorName':'',
#                    'osDeploymentSettings':None,
#                    'connections': [
#  								    {'id': 1, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 2, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 3, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '7500', 'networkUri': 'NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 4, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 5, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 6, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500', 'networkUri': 'NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 7, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '7500', 'networkUri': 'NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 8, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#                                    ]},
#                   {'type': 'ServerProfileV6', 'serverHardwareUri': 'CN7545049J, bay 7',
#                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:CN7545049J', 'enclosureGroupUri': 'EG:EG-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'E48-Bay7-18', 'description': '', 'affinity': 'Bay',
#                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
#                    'bootMode': {'manageMode':True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
#                    'firmware':{'manageFirmware':False,'firmwareBaselineUri':'','forceInstallFirmware':False,'firmwareInstallType':None},
#                    'bios':{'manageBios':False,'overriddenSettings':[]},
#                    'hideUnusedFlexNics':True,
#                    'iscsiInitiatorName':'',
#                    'osDeploymentSettings':None,
#                    'connections': [
#  								    {'id': 1, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 2, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 3, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '7500', 'networkUri': 'NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 4, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 5, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 6, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500', 'networkUri': 'NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 7, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '7500', 'networkUri': 'NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 8, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#                                    ]},
#                   {'type': 'ServerProfileV6', 'serverHardwareUri': 'CN7545049J, bay 8',
#                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:CN7545049J', 'enclosureGroupUri': 'EG:EG-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'E48-Bay8-19', 'description': '', 'affinity': 'Bay',
#                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
#                    'bootMode': {'manageMode':True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
#                    'firmware':{'manageFirmware':False,'firmwareBaselineUri':'','forceInstallFirmware':False,'firmwareInstallType':None},
#                    'bios':{'manageBios':False,'overriddenSettings':[]},
#                    'hideUnusedFlexNics':True,
#                    'iscsiInitiatorName':'',
#                    'osDeploymentSettings':None,
#                    'connections': [
#  								    {'id': 1, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 2, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 3, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '7500', 'networkUri': 'NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 4, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 5, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 6, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500', 'networkUri': 'NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 7, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '7500', 'networkUri': 'NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 8, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#                                    ]},
#                   {'type': 'ServerProfileV6', 'serverHardwareUri': 'CN7545049J, bay 9',
#                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:CN7545049J', 'enclosureGroupUri': 'EG:EG-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'E48-Bay9-20', 'description': '', 'affinity': 'Bay',
#                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
#                    'bootMode': {'manageMode':True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
#                    'firmware':{'manageFirmware':False,'firmwareBaselineUri':'','forceInstallFirmware':False,'firmwareInstallType':None},
#                    'bios':{'manageBios':False,'overriddenSettings':[]},
#                    'hideUnusedFlexNics':True,
#                    'iscsiInitiatorName':'',
#                    'osDeploymentSettings':None,
#                    'connections': [
#  								    {'id': 1, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 2, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 3, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '7500', 'networkUri': 'NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 4, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 5, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 6, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500', 'networkUri': 'NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 7, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '7500', 'networkUri': 'NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 8, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#                                    ]},
#                   {'type': 'ServerProfileV6', 'serverHardwareUri': 'CN7545049J, bay 10',
#                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:CN7545049J', 'enclosureGroupUri': 'EG:EG-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'E48-Bay10-21', 'description': '', 'affinity': 'Bay',
#                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
#                    'bootMode': {'manageMode':True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
#                    'firmware':{'manageFirmware':False,'firmwareBaselineUri':'','forceInstallFirmware':False,'firmwareInstallType':None},
#                    'bios':{'manageBios':False,'overriddenSettings':[]},
#                    'hideUnusedFlexNics':True,
#                    'iscsiInitiatorName':'',
#                    'osDeploymentSettings':None,
#                    'connections': [
#  								    {'id': 1, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 2, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 3, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '7500', 'networkUri': 'NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 4, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 5, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 6, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500', 'networkUri': 'NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 7, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '7500', 'networkUri': 'NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 8, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#                                    ]},
#                   {'type': 'ServerProfileV6', 'serverHardwareUri': 'CN7545049J, bay 11',
#                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:CN7545049J', 'enclosureGroupUri': 'EG:EG-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'E48-Bay11-22', 'description': '', 'affinity': 'Bay',
#                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
#                    'bootMode': {'manageMode':True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
#                    'firmware':{'manageFirmware':False,'firmwareBaselineUri':'','forceInstallFirmware':False,'firmwareInstallType':None},
#                    'bios':{'manageBios':False,'overriddenSettings':[]},
#                    'hideUnusedFlexNics':True,
#                    'iscsiInitiatorName':'',
#                    'osDeploymentSettings':None,
#                    'connections': [
#  								    {'id': 1, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 2, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 3, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '7500', 'networkUri': 'NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 4, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 5, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 6, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500', 'networkUri': 'NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 7, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '7500', 'networkUri': 'NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 8, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#                                    ]},
#                   {'type': 'ServerProfileV6', 'serverHardwareUri': 'CN7545049J, bay 12',
#                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:CN7545049J', 'enclosureGroupUri': 'EG:EG-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'E48-Bay12-23', 'description': '', 'affinity': 'Bay',
#                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
#                    'bootMode': {'manageMode':True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
#                    'firmware':{'manageFirmware':False,'firmwareBaselineUri':'','forceInstallFirmware':False,'firmwareInstallType':None},
#                    'bios':{'manageBios':False,'overriddenSettings':[]},
#                    'hideUnusedFlexNics':True,
#                    'iscsiInitiatorName':'',
#                    'osDeploymentSettings':None,
#                    'connections': [
#  								    {'id': 1, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 2, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 3, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '7500', 'networkUri': 'NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 4, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 5, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 6, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500', 'networkUri': 'NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 7, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '7500', 'networkUri': 'NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  								    {'id': 8, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#                                    ]},
#
#                    ]

"""
Server Profile no hardware assigned.
Boot 'order' options are 'PXE' or 'HardDisk'.
"""

server_profiles_nohw = [
                   {'type': 'ServerProfileV6', 'serverHardwareUri': None,
                    'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'E47-Bay1-1', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'bootMode': {'manageMode':True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                    'firmware': {'manageFirmware':False,'firmwareBaselineUri':'','forceInstallFirmware':False,'firmwareInstallType':None},
                    'bios':{'manageBios':False,'overriddenSettings':[]},
                    'hideUnusedFlexNics':True,
                    'iscsiInitiatorName':'',
                    'osDeploymentSettings':None,
                    'connections': [
  								    {'id': 1, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NS:NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 2, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'NS:NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 3, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '7500', 'networkUri': 'NS:NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 4, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 5, 'name': 'conn-2a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NS:NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 6, 'name': 'conn-2b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500', 'networkUri': 'NS:NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 7, 'name': 'conn-2c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '7500', 'networkUri': 'NS:NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 8, 'name': 'conn-2d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    ]},
                   {'type': 'ServerProfileV6', 'serverHardwareUri': None,
                    'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'E47-Bay2-2', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'bootMode': {'manageMode':True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                    'firmware':{'manageFirmware':False,'firmwareBaselineUri':'','forceInstallFirmware':False,'firmwareInstallType':None},
                    'bios':{'manageBios':False,'overriddenSettings':[]},
                    'hideUnusedFlexNics':True,
                    'iscsiInitiatorName':'',
                    'osDeploymentSettings':None,
                    'connections': [
  								    {'id': 1, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NS:NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 2, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'NS:NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 3, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '7500', 'networkUri': 'NS:NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 4, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 5, 'name': 'conn-2a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NS:NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 6, 'name': 'conn-2b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500', 'networkUri': 'NS:NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 7, 'name': 'conn-2c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '7500', 'networkUri': 'NS:NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 8, 'name': 'conn-2d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    ]},
                   {'type': 'ServerProfileV6', 'serverHardwareUri': None,
                    'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'E47-Bay3-3', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'bootMode': {'manageMode':True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                    'firmware':{'manageFirmware':False,'firmwareBaselineUri':'','forceInstallFirmware':False,'firmwareInstallType':None},
                    'bios':{'manageBios':False,'overriddenSettings':[]},
                    'hideUnusedFlexNics':True,
                    'iscsiInitiatorName':'',
                    'osDeploymentSettings':None,
                    'connections': [
  								    {'id': 1, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NS:NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 2, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'NS:NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 3, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '7500', 'networkUri': 'NS:NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 4, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 5, 'name': 'conn-2a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NS:NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 6, 'name': 'conn-2b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500', 'networkUri': 'NS:NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 7, 'name': 'conn-2c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '7500', 'networkUri': 'NS:NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 8, 'name': 'conn-2d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    ]},
                   {'type': 'ServerProfileV6', 'serverHardwareUri': None,
                    'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'E47-Bay4-4', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'bootMode': {'manageMode':True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                    'firmware':{'manageFirmware':False,'firmwareBaselineUri':'','forceInstallFirmware':False,'firmwareInstallType':None},
                    'bios':{'manageBios':False,'overriddenSettings':[]},
                    'hideUnusedFlexNics':True,
                    'iscsiInitiatorName':'',
                    'osDeploymentSettings':None,
                    'connections': [
  								    {'id': 1, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NS:NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 2, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'NS:NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 3, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '7500', 'networkUri': 'NS:NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 4, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 5, 'name': 'conn-2a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NS:NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 6, 'name': 'conn-2b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500', 'networkUri': 'NS:NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 7, 'name': 'conn-2c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '7500', 'networkUri': 'NS:NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 8, 'name': 'conn-2d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    ]},
                   {'type': 'ServerProfileV6', 'serverHardwareUri': None,
                    'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'E47-Bay5-5', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'bootMode': {'manageMode':True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                    'firmware':{'manageFirmware':False,'firmwareBaselineUri':'','forceInstallFirmware':False,'firmwareInstallType':None},
                    'bios':{'manageBios':False,'overriddenSettings':[]},
                    'hideUnusedFlexNics':True,
                    'iscsiInitiatorName':'',
                    'osDeploymentSettings':None,
                    'connections': [
  								    {'id': 1, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NS:NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 2, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'NS:NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 3, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '7500', 'networkUri': 'NS:NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 4, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 5, 'name': 'conn-2a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NS:NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 6, 'name': 'conn-2b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500', 'networkUri': 'NS:NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 7, 'name': 'conn-2c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '7500', 'networkUri': 'NS:NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 8, 'name': 'conn-2d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    ]},
                   {'type': 'ServerProfileV6', 'serverHardwareUri': None,
                    'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'E47-Bay6-6', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'bootMode': {'manageMode':True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                    'firmware':{'manageFirmware':False,'firmwareBaselineUri':'','forceInstallFirmware':False,'firmwareInstallType':None},
                    'bios':{'manageBios':False,'overriddenSettings':[]},
                    'hideUnusedFlexNics':True,
                    'iscsiInitiatorName':'',
                    'osDeploymentSettings':None,
                    'connections': [
  								    {'id': 1, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NS:NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 2, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'NS:NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 3, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '7500', 'networkUri': 'NS:NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 4, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 5, 'name': 'conn-2a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NS:NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 6, 'name': 'conn-2b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500', 'networkUri': 'NS:NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 7, 'name': 'conn-2c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '7500', 'networkUri': 'NS:NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 8, 'name': 'conn-2d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    ]},
                   {'type': 'ServerProfileV6', 'serverHardwareUri': None,
                    'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'E47-Bay7-7', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'bootMode': {'manageMode':True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                    'firmware':{'manageFirmware':False,'firmwareBaselineUri':'','forceInstallFirmware':False,'firmwareInstallType':None},
                    'bios':{'manageBios':False,'overriddenSettings':[]},
                    'hideUnusedFlexNics':True,
                    'iscsiInitiatorName':'',
                    'osDeploymentSettings':None,
                    'connections': [
  								    {'id': 1, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NS:NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 2, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'NS:NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 3, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '7500', 'networkUri': 'NS:NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 4, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 5, 'name': 'conn-2a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NS:NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 6, 'name': 'conn-2b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500', 'networkUri': 'NS:NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 7, 'name': 'conn-2c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '7500', 'networkUri': 'NS:NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 8, 'name': 'conn-2d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    ]},
                   {'type': 'ServerProfileV6', 'serverHardwareUri': None,
                    'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'E47-Bay8-8', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'bootMode': {'manageMode':True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                    'firmware':{'manageFirmware':False,'firmwareBaselineUri':'','forceInstallFirmware':False,'firmwareInstallType':None},
                    'bios':{'manageBios':False,'overriddenSettings':[]},
                    'hideUnusedFlexNics':True,
                    'iscsiInitiatorName':'',
                    'osDeploymentSettings':None,
                    'connections': [
  								    {'id': 1, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NS:NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 2, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'NS:NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 3, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '7500', 'networkUri': 'NS:NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 4, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 5, 'name': 'conn-2a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NS:NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 6, 'name': 'conn-2b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500', 'networkUri': 'NS:NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 7, 'name': 'conn-2c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '7500', 'networkUri': 'NS:NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 8, 'name': 'conn-2d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    ]},
                   {'type': 'ServerProfileV6', 'serverHardwareUri': None,
                    'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'E47-Bay9-9', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'bootMode': {'manageMode':True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                    'firmware':{'manageFirmware':False,'firmwareBaselineUri':'','forceInstallFirmware':False,'firmwareInstallType':None},
                    'bios':{'manageBios':False,'overriddenSettings':[]},
                    'hideUnusedFlexNics':True,
                    'iscsiInitiatorName':'',
                    'osDeploymentSettings':None,
                    'connections': [
  								    {'id': 1, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NS:NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 2, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'NS:NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 3, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '7500', 'networkUri': 'NS:NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 4, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 5, 'name': 'conn-2a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NS:NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 6, 'name': 'conn-2b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500', 'networkUri': 'NS:NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 7, 'name': 'conn-2c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '7500', 'networkUri': 'NS:NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 8, 'name': 'conn-2d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    ]},
                   {'type': 'ServerProfileV6', 'serverHardwareUri': None,
                    'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'E47-Bay10-10', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'bootMode': {'manageMode':True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                    'firmware':{'manageFirmware':False,'firmwareBaselineUri':'','forceInstallFirmware':False,'firmwareInstallType':None},
                    'bios':{'manageBios':False,'overriddenSettings':[]},
                    'hideUnusedFlexNics':True,
                    'iscsiInitiatorName':'',
                    'osDeploymentSettings':None,
                    'connections': [
  								    {'id': 1, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NS:NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 2, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'NS:NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 3, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '7500', 'networkUri': 'NS:NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 4, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 5, 'name': 'conn-2a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NS:NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 6, 'name': 'conn-2b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500', 'networkUri': 'NS:NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 7, 'name': 'conn-2c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '7500', 'networkUri': 'NS:NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 8, 'name': 'conn-2d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    ]},
                   {'type': 'ServerProfileV6', 'serverHardwareUri': None,
                    'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'E47-Bay11-11', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'bootMode': {'manageMode':True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                    'firmware':{'manageFirmware':False,'firmwareBaselineUri':'','forceInstallFirmware':False,'firmwareInstallType':None},
                    'bios':{'manageBios':False,'overriddenSettings':[]},
                    'hideUnusedFlexNics':True,
                    'iscsiInitiatorName':'',
                    'osDeploymentSettings':None,
                    'connections': [
  								    {'id': 1, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NS:NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 2, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'NS:NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 3, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '7500', 'networkUri': 'NS:NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 4, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 5, 'name': 'conn-2a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NS:NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 6, 'name': 'conn-2b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500', 'networkUri': 'NS:NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 7, 'name': 'conn-2c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '7500', 'networkUri': 'NS:NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 8, 'name': 'conn-2d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    ]},
                   {'type': 'ServerProfileV6', 'serverHardwareUri': None,
                    'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'E47-Bay12-12', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'bootMode': {'manageMode':True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                    'firmware':{'manageFirmware':False,'firmwareBaselineUri':'','forceInstallFirmware':False,'firmwareInstallType':None},
                    'bios':{'manageBios':False,'overriddenSettings':[]},
                    'hideUnusedFlexNics':True,
                    'iscsiInitiatorName':'',
                    'osDeploymentSettings':None,
                    'connections': [
  								    {'id': 1, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NS:NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 2, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'NS:NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 3, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '7500', 'networkUri': 'NS:NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 4, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 5, 'name': 'conn-2a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NS:NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 6, 'name': 'conn-2b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500', 'networkUri': 'NS:NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 7, 'name': 'conn-2c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '7500', 'networkUri': 'NS:NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 8, 'name': 'conn-2d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    ]},
                   {'type': 'ServerProfileV6', 'serverHardwareUri': None,
                    'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'E48-Bay1-13', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'bootMode': {'manageMode':True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                    'firmware':{'manageFirmware':False,'firmwareBaselineUri':'','forceInstallFirmware':False,'firmwareInstallType':None},
                    'bios':{'manageBios':False,'overriddenSettings':[]},
                    'hideUnusedFlexNics':True,
                    'iscsiInitiatorName':'',
                    'osDeploymentSettings':None,
                    'connections': [
  								    {'id': 1, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NS:NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 2, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'NS:NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 3, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '7500', 'networkUri': 'NS:NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 4, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 5, 'name': 'conn-2a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NS:NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 6, 'name': 'conn-2b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500', 'networkUri': 'NS:NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 7, 'name': 'conn-2c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '7500', 'networkUri': 'NS:NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 8, 'name': 'conn-2d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    ]},
                   {'type': 'ServerProfileV6', 'serverHardwareUri': None,
                    'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'E48-Bay2-14', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'bootMode': {'manageMode':True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                    'firmware':{'manageFirmware':False,'firmwareBaselineUri':'','forceInstallFirmware':False,'firmwareInstallType':None},
                    'bios':{'manageBios':False,'overriddenSettings':[]},
                    'hideUnusedFlexNics':True,
                    'iscsiInitiatorName':'',
                    'osDeploymentSettings':None,
                    'connections': [
  								    {'id': 1, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NS:NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 2, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'NS:NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 3, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '7500', 'networkUri': 'NS:NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 4, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 5, 'name': 'conn-2a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NS:NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 6, 'name': 'conn-2b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500', 'networkUri': 'NS:NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 7, 'name': 'conn-2c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '7500', 'networkUri': 'NS:NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 8, 'name': 'conn-2d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    ]},
                   {'type': 'ServerProfileV6', 'serverHardwareUri': None,
                    'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'E48-Bay3-15', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'bootMode': {'manageMode':True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                    'firmware':{'manageFirmware':False,'firmwareBaselineUri':'','forceInstallFirmware':False,'firmwareInstallType':None},
                    'bios':{'manageBios':False,'overriddenSettings':[]},
                    'hideUnusedFlexNics':True,
                    'iscsiInitiatorName':'',
                    'osDeploymentSettings':None,
                    'connections': [
  								    {'id': 1, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NS:NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 2, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'NS:NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 3, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '7500', 'networkUri': 'NS:NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 4, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 5, 'name': 'conn-2a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NS:NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 6, 'name': 'conn-2b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500', 'networkUri': 'NS:NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 7, 'name': 'conn-2c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '7500', 'networkUri': 'NS:NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 8, 'name': 'conn-2d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    ]},
                   {'type': 'ServerProfileV6', 'serverHardwareUri': None,
                    'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'E48-Bay4-16', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'bootMode': {'manageMode':True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                    'firmware':{'manageFirmware':False,'firmwareBaselineUri':'','forceInstallFirmware':False,'firmwareInstallType':None},
                    'bios':{'manageBios':False,'overriddenSettings':[]},
                    'hideUnusedFlexNics':True,
                    'iscsiInitiatorName':'',
                    'osDeploymentSettings':None,
                    'connections': [
  								    {'id': 1, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NS:NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 2, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'NS:NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 3, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '7500', 'networkUri': 'NS:NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 4, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 5, 'name': 'conn-2a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NS:NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 6, 'name': 'conn-2b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500', 'networkUri': 'NS:NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 7, 'name': 'conn-2c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '7500', 'networkUri': 'NS:NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 8, 'name': 'conn-2d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    ]},
                   {'type': 'ServerProfileV6', 'serverHardwareUri': None,
                    'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'E48-Bay5-17', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'bootMode': {'manageMode':True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                    'firmware':{'manageFirmware':False,'firmwareBaselineUri':'','forceInstallFirmware':False,'firmwareInstallType':None},
                    'bios':{'manageBios':False,'overriddenSettings':[]},
                    'hideUnusedFlexNics':True,
                    'iscsiInitiatorName':'',
                    'osDeploymentSettings':None,
                    'connections': [
  								    {'id': 1, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NS:NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 2, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'NS:NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 3, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '7500', 'networkUri': 'NS:NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 4, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 5, 'name': 'conn-2a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NS:NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 6, 'name': 'conn-2b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500', 'networkUri': 'NS:NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 7, 'name': 'conn-2c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '7500', 'networkUri': 'NS:NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 8, 'name': 'conn-2d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    ]},
                   {'type': 'ServerProfileV6', 'serverHardwareUri': None,
                    'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'E48-Bay6-18', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'bootMode': {'manageMode':True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                    'firmware':{'manageFirmware':False,'firmwareBaselineUri':'','forceInstallFirmware':False,'firmwareInstallType':None},
                    'bios':{'manageBios':False,'overriddenSettings':[]},
                    'hideUnusedFlexNics':True,
                    'iscsiInitiatorName':'',
                    'osDeploymentSettings':None,
                    'connections': [
  								    {'id': 1, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NS:NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 2, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'NS:NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 3, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '7500', 'networkUri': 'NS:NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 4, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 5, 'name': 'conn-2a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NS:NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 6, 'name': 'conn-2b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500', 'networkUri': 'NS:NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 7, 'name': 'conn-2c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '7500', 'networkUri': 'NS:NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 8, 'name': 'conn-2d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    ]},
                   {'type': 'ServerProfileV6', 'serverHardwareUri': None,
                    'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'E48-Bay7-19', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'bootMode': {'manageMode':True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                    'firmware':{'manageFirmware':False,'firmwareBaselineUri':'','forceInstallFirmware':False,'firmwareInstallType':None},
                    'bios':{'manageBios':False,'overriddenSettings':[]},
                    'hideUnusedFlexNics':True,
                    'iscsiInitiatorName':'',
                    'osDeploymentSettings':None,
                    'connections': [
  								    {'id': 1, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NS:NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 2, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'NS:NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 3, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '7500', 'networkUri': 'NS:NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 4, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 5, 'name': 'conn-2a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NS:NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 6, 'name': 'conn-2b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500', 'networkUri': 'NS:NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 7, 'name': 'conn-2c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '7500', 'networkUri': 'NS:NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 8, 'name': 'conn-2d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    ]},
                   {'type': 'ServerProfileV6', 'serverHardwareUri': None,
                    'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'E48-Bay8-20', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'bootMode': {'manageMode':True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                    'firmware':{'manageFirmware':False,'firmwareBaselineUri':'','forceInstallFirmware':False,'firmwareInstallType':None},
                    'bios':{'manageBios':False,'overriddenSettings':[]},
                    'hideUnusedFlexNics':True,
                    'iscsiInitiatorName':'',
                    'osDeploymentSettings':None,
                    'connections': [
  								    {'id': 1, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NS:NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 2, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'NS:NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 3, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '7500', 'networkUri': 'NS:NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 4, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 5, 'name': 'conn-2a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NS:NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 6, 'name': 'conn-2b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500', 'networkUri': 'NS:NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 7, 'name': 'conn-2c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '7500', 'networkUri': 'NS:NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 8, 'name': 'conn-2d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    ]},
                   {'type': 'ServerProfileV6', 'serverHardwareUri': None,
                    'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'E48-Bay9-21', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'bootMode': {'manageMode':True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                    'firmware':{'manageFirmware':False,'firmwareBaselineUri':'','forceInstallFirmware':False,'firmwareInstallType':None},
                    'bios':{'manageBios':False,'overriddenSettings':[]},
                    'hideUnusedFlexNics':True,
                    'iscsiInitiatorName':'',
                    'osDeploymentSettings':None,
                    'connections': [
  								    {'id': 1, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NS:NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 2, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'NS:NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 3, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '7500', 'networkUri': 'NS:NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 4, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 5, 'name': 'conn-2a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NS:NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 6, 'name': 'conn-2b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500', 'networkUri': 'NS:NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 7, 'name': 'conn-2c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '7500', 'networkUri': 'NS:NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 8, 'name': 'conn-2d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    ]},
                   {'type': 'ServerProfileV6', 'serverHardwareUri': None,
                    'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'E48-Bay10-22', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'bootMode': {'manageMode':True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                    'firmware':{'manageFirmware':False,'firmwareBaselineUri':'','forceInstallFirmware':False,'firmwareInstallType':None},
                    'bios':{'manageBios':False,'overriddenSettings':[]},
                    'hideUnusedFlexNics':True,
                    'iscsiInitiatorName':'',
                    'osDeploymentSettings':None,
                    'connections': [
  								    {'id': 1, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NS:NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 2, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'NS:NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 3, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '7500', 'networkUri': 'NS:NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 4, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 5, 'name': 'conn-2a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NS:NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 6, 'name': 'conn-2b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500', 'networkUri': 'NS:NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 7, 'name': 'conn-2c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '7500', 'networkUri': 'NS:NW-30-14', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 8, 'name': 'conn-2d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    ]},
                   {'type': 'ServerProfileV6', 'serverHardwareUri': None,
                    'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'E48-Bay11-23', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'bootMode': {'manageMode':True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                    'firmware':{'manageFirmware':False,'firmwareBaselineUri':'','forceInstallFirmware':False,'firmwareInstallType':None},
                    'bios':{'manageBios':False,'overriddenSettings':[]},
                    'hideUnusedFlexNics':True,
                    'iscsiInitiatorName':'',
                    'osDeploymentSettings':None,
                    'connections': [
  								    {'id': 1, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NS:NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 2, 'name': 'FC-A', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'FC:FC-A', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 3, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '7500', 'networkUri': 'NS:NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 4, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 5, 'name': 'conn-2a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NS:NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 6, 'name': 'FC-B', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500', 'networkUri': 'FC:FC-B', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 7, 'name': 'conn-2c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '7500', 'networkUri': 'NS:NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 8, 'name': 'conn-2d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    ]},
                   {'type': 'ServerProfileV6', 'serverHardwareUri': None,
                    'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'E48-Bay12-24', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'bootMode': {'manageMode':True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                    'firmware':{'manageFirmware':False,'firmwareBaselineUri':'','forceInstallFirmware':False,'firmwareInstallType':None},
                    'bios':{'manageBios':False,'overriddenSettings':[]},
                    'hideUnusedFlexNics':True,
                    'iscsiInitiatorName':'',
                    'osDeploymentSettings':None,
                    'connections': [
  								    {'id': 1, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NS:NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 2, 'name': 'FCoE-A', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'FCOE:FCoE-A-3064', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 3, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '7500', 'networkUri': 'NS:NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 4, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 5, 'name': 'conn-2a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'NS:NW-3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 6, 'name': 'FCoE-B', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500', 'networkUri': 'FCOE:FCoE-B-3065', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 7, 'name': 'conn-2c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '7500', 'networkUri': 'NS:NW-7', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
  								    {'id': 8, 'name': 'conn-2d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:NW-13', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    ]},

                   ]


"""
Maps sever profile to encl, bay.  First column: server profile name. Second column: Enclosure, bay # 
"""
server_profile_to_bay_map = {
                             'E47-Bay1-1': 'CN75450498, bay 1',
                             'E47-Bay2-2': 'CN75450498, bay 2',
                             'E47-Bay3-3': 'CN75450498, bay 3',
                             'E47-Bay4-4': 'CN75450498, bay 4',
                             'E47-Bay5-5': 'CN75450498, bay 5',
                             'E47-Bay6-6': 'CN75450498, bay 6',
                             'E47-Bay7-7': 'CN75450498, bay 7',
                             'E47-Bay8-8': 'CN75450498, bay 8',
                             'E47-Bay9-9': 'CN75450498, bay 9',
                             'E47-Bay10-10': 'CN75450498, bay 10',
                             'E47-Bay11-11': 'CN75450498, bay 11',
                             'E47-Bay12-12': 'CN75450498, bay 12',
                             'E48-Bay1-13': 'CN7545049J, bay 1',
                             'E48-Bay2-14': 'CN7545049J, bay 2',
                             'E48-Bay3-15': 'CN7545049J, bay 3',
                             'E48-Bay4-16': 'CN7545049J, bay 4',
                             'E48-Bay5-17': 'CN7545049J, bay 5',
                             'E48-Bay6-18': 'CN7545049J, bay 6',
                             'E48-Bay7-19': 'CN7545049J, bay 7',
                             'E48-Bay8-20': 'CN7545049J, bay 8',
                             'E48-Bay9-21': 'CN7545049J, bay 9',
                             'E48-Bay10-22': 'CN7545049J, bay 10',
                             'E48-Bay11-23': 'CN7545049J, bay 11',
                             'E48-Bay12-24': 'CN7545049J, bay 12',
                             }


server_profile_templates = [
                   {'type': 'ServerProfileTemplateV2',
                    'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1', 'enclosureGroupUri': 'EG:EG-2ME',
                    'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                    'name': 'server-profile-template', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'bootMode': {'manageMode':True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4 only'},
                    'connections': [
  								    {'id': 1, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 
                                        'requestedMbps': '2500', 'networkUri': 'NS:NW-3', 'boot': {'priority': 'NotBootable'}},
  								    {'id': 2, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 
                                        'requestedMbps': '2500', 'networkUri': 'NS:NW-7', 'boot': {'priority': 'NotBootable'}},
  								    {'id': 3, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 
                                        'requestedMbps': '7500', 'networkUri': 'NS:NW-30-14', 'boot': {'priority': 'NotBootable'}},
  								    {'id': 4, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 
                                        'requestedMbps': '2500', 'networkUri': 'NS:NW-13', 'boot': {'priority': 'NotBootable'}},
  								    {'id': 5, 'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 
                                        'requestedMbps': '2500', 'networkUri': 'NS:NW-3', 'boot': {'priority': 'NotBootable'}},
  								    {'id': 6, 'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b', 
                                        'requestedMbps': '2500', 'networkUri': 'NS:NW-7', 'boot': {'priority': 'NotBootable'}},
  								    {'id': 7, 'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 
                                        'requestedMbps': '7500', 'networkUri': 'NS:NW-30-14', 'boot': {'priority': 'NotBootable'}},
  								    {'id': 8, 'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 
                                        'requestedMbps': '2500', 'networkUri': 'NS:NW-13', 'boot': {'priority': 'NotBootable'}},
                                    ]},
                    ]

""""server_profile_templates = [
                   {'type': 'ServerProfileTemplateV2',
                    'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1', 'enclosureGroupUri': 'EG:EG 1',
                    'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                    'name': 'Profile1', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'bootMode': {'manageMode':True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                    'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                     'requestedMbps': '2000', 'networkUri': 'ETH:net_101',
                                     'boot': {'priority': 'Primary'}},
                                    {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                     'requestedMbps': '2000', 'networkUri': 'ETH:net_102',
                                     'boot': {'priority': 'NotBootable'}},
                                    ]},
                   {'type': 'ServerProfileTemplateV2',
                    'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1', 'enclosureGroupUri': 'EG:EG 1',
                    'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                    'name': 'Profile2', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'bootMode': {'manageMode':True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                    'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                     'requestedMbps': '2000', 'networkUri': 'ETH:net_101',
                                     'boot': {'priority': 'Primary'}},
                                    {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                     'requestedMbps': '2000', 'networkUri': 'ETH:net_102',
                                     'boot': {'priority': 'NotBootable'}},
                                    {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c',
                                     'requestedMbps': '2000', 'networkUri': 'ETH:net_103',
                                     'boot': {'priority': 'NotBootable'}},
                                    {'id': 4, 'name': '4', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c',
                                     'requestedMbps': '2000', 'networkUri': 'ETH:net_104',
                                     'boot': {'priority': 'NotBootable'}},
                                    ]},
                  ]
"""


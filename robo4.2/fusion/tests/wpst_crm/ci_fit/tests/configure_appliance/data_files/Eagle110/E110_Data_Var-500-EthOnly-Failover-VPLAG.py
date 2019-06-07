"""
    Eagle 110 setup/teardown data file.
"""


def make_range_list(vrange):
    """
        Make range list off dictionary of vlan range data.
        Argument:
            vrange: dictionary of data for vlan range concatenating prefix, vlan, and suffix
        Return:
            mrlist: list of vlan range network names
    """
    mrlist = []
    for x in xrange(vrange['start'], (vrange['end'] + 1)):
        mrlist.append(vrange['prefix'] + str(x) + vrange['suffix'])
    return mrlist


def rlist(start, end, prefix='ENet', suffix=''):
    """
        Make range list based on provided arguments.
        Arguments:
            start: start of the vlan id range
            end: end of the vlan id range
            prefix: prefix of the network name of vlan id
            suffix: suffix of the network name of vlan id
        Return:
            rlist: list of vlan range network names
    """
    arlist = []
    for x in xrange(start, end + 1):
        arlist.append(prefix + str(x) + suffix)
    return arlist


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
               'app1Ipv4Addr': '15.186.10.110',
               'app2Ipv4Addr': '15.186.11.110',
               'virtIpv4Addr': '15.186.9.110',
               'ipv6Type': 'UNCONFIGURE',
               'hostname': 'ci-manager-eagle110.us.rdlabs.hpecorp.net',
               'confOneNode': True,
               'domainName': 'usa.hp.com',
               'aliasDisabled': True,
               }],
             }

"""
This is the time and locale settings used during FTS.
"""
timeandlocale = {'type': 'TimeAndLocale', 'dateTime': None, 'timezone': 'UTC', 'ntpServers': ['ntp.hpecorp.net'], 'locale': 'en_US.UTF-8'}

remote_backup = {
    "remoteServerName": "15.186.7.138",
    "remoteServerDir": "Backups_2ME",
    "remoteServerPublicKey": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDkic3KU+PQAZ71nL11W8HXSMKqOQeCGrgfsL6Z+3knr5LQjJIVVQDNlreXllp0smpSECumtxve5t4EETG6B94JJgjx4fZAhHp2HXY/0gIzI5UF/XJOAw5YDs0LQ4yvfNdyubfHVbnn+Zax7Ee42d5V6rttxRGu8SWI8VdCcoR/vQSSimEU+Aui0tgAGtv3dyvdXbxwH+Swli0aSD1PxKHHCYB7H5B/2LLAo7N0oIfOzqGikxDr0ydnkcAtGoBiPEft49ITcSiHidhlXsy/3h19MowP8pmlhsD/be/+uYBP88Q0EaEDpftj4HrR1SgemQNuZ/Hm4CX6UMZJFctF+C9H",
    "userName": "root",
                "password": "rootpwd",
                "enabled": True,
                "protocol": "SCP",
                "scheduleInterval": "DAILY",
                "scheduleDays": [],
    "scheduleTime": "23:30",
}

"""
These are the virtual address ranges for MAC, WWN and SERIAL numbers
"""

ranges = [{'name': 'Eagle110-MAC', 'type': 'Range', 'category': 'id-range-VMAC', 'rangeCategory': 'CUSTOM', 'startAddress': '36:85:EA:C0:00:00', 'endAddress': '36:85:EA:CF:FF:FF', 'enabled': True},
          {'name': 'Eagle110-WWN', 'type': 'Range', 'category': 'id-range-VWWN', 'rangeCategory': 'CUSTOM', 'startAddress': '50:06:0B:00:00:C3:26:00', 'endAddress': '50:06:0B:00:00:C3:26:7F', 'enabled': True},
          {'name': 'Eagle110-SN', 'type': 'Range', 'category': 'id-range-VSN', 'rangeCategory': 'CUSTOM', 'startAddress': 'VCUPM9W000', 'endAddress': 'VCUPM9WZZZ', 'enabled': True}]

"""
These are the ID Pools IPv4 Subnets
"""
ipv4_subnets = [
    {
        "type": "Subnet",
        "name": "Eagle110_IPv4_Subnet",
        "networkId": "172.16.2.0",
        "subnetmask": "255.255.255.0",
        #        "gateway":"10.10.1.1",
        #        "domain":"example.com",
        #        "dnsServers":["10.10.10.215"]
    }
]

"""
These the IP Pools IPv4 Ranges
"""
ipv4_ranges = [
    {
        "type": "Range",
        "name": "Eagle110_IPv4_Ranges",
        "startStopFragments": [
            {
                "startAddress": "172.16.2.249",
                "endAddress": "172.16.2.250"
            }
        ],
        "subnetUri": "Eagle110_IPv4_Subnet"
    }
]

"""
These are the users you want to create on the appliance
"""
users = [{'userName': 'Serveradmin', 'password': 'Serveradmin', 'fullName': 'Serveradmin', 'permissions': [{'roleName': 'Server administrator'}], 'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions'},
         {'userName': 'Networkadmin', 'password': 'Networkadmin', 'fullName': 'Networkadmin', 'permissions': [{'roleName': 'Network administrator'}], 'emailAddress': 'nat@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions'},
         {'userName': 'Backupadmin', 'password': 'Backupadmin', 'fullName': 'Backupadmin', 'permissions': [{'roleName': 'Backup administrator'}], 'emailAddress': 'backup@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions'},
         {'userName': 'Noprivledge', 'password': 'Noprivledge', 'fullName': 'Noprivledge', 'permissions': [{'roleName': 'Read only'}], 'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions'}
         ]


"""
These are the Licenses you want to add to the appliance
"""
licenses = [
    {'key': 'AA9C CQAA H9PY CHXY V7B5 HWWB Y9JL KMPL 3V2E PEZU DXAU 2CSM GHTG L762 AQ72 XCB9 KJVT D5KM EFVW DT5J 2JUL 6ZS8 SPS9 YG66 Z99R MWSN 6Z84 46XT WZJL HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTFG LS8T XU4E "EVAL-HPOV-NFR1 HPOV-NFR1 HP_OneView_16_Seat_NFR 7T36AEJG7JJ9"_3MNZV-XHZRH-YHJY3-X5PZ2-3KDX6'},
    {'key': 'QB2C D9MA P9PQ LHUY VTB5 HG7X Y9JL KMPL B89H MZVU GRUU 9HWE JHTG TNTE CMRG HPMR 4G5U A5G9 EUG2 9CQ9 HKDU LWWP ZQT6 UPJE 6SQC 43QG V2TH AZRY P2ZV RHMQ F4BH BGWB AZS8 2F9G LL4U R4WA V886 VC93 HQT5 6CAD 3WJY YLJ6 CCUG 2EQ7 "Synergy 32Gb FC Upgrade License E-LTU"'},
    {'key': 'QBSE D9MA P9PY LHUZ VTB5 HG77 Y9JL KMPL B89H MZVU 8RUU 9HWE 9YSH XNY6 CMRG HPMR 4H5U A589 EUG2 9CQ9 HKDU LWWP ZQT6 UPJE 6SQC 43QG V2TH AZRY P2ZV RHMQ F4BH BGWB AZS8 2F9G LL4U R4WA V886 VC93 HQT5 6CAD 3WJY YLJ6 CCUG 2EQ7 "Synergy 50Gb Downlink Upgrade License E-LTU"'}, {'key': '9B2G D9MA H9PA CHVZ V2B4 HWWV Y9JL KMPL B89H MZVU 6RMS 9HWE 92R6 3FZ3 CMRG HPMR MFVU A5K9 MHGK EKX9 HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'},
    {'key': 'YBKA D9MA H9P9 8HX3 V2B4 HWWV Y9JL KMPL B89H MZVU GR4S JHWE J2SP XNZ8 CMRG HPMR UFVU A5K9 MWHC 9K4K HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'}
]
"""
Added per Sabin to allow the use of the internally reserved VLAN IDs from 3967 to 4094.
"""
reserved_vlan = {
    'type': 'vlan-pool',
    'start': 4035,
    'length': 60
}


"""
These are the ETHERNET networks you want to add to the appliance
"""
ethernet_networks = [{'name': 'Untagged-1',
                      'type': 'ethernet-networkV4',
                      'vlanId': None,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Untagged'},
                     {'name': 'Tunnel1',
                      'type': 'ethernet-networkV4',
                      'vlanId': None,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tunnel'},
                     #                      {'name': 'iscsi-Net_3',
                     #                          'type': 'ethernet-networkV4',
                     #                          'vlanId': None,
                     #                          'purpose': 'General',
                     #                          'smartLink': True,
                     #                          'privateNetwork': False,
                     #                          'connectionTemplateUri': None,
                     #                          'ethernetNetworkType': 'Untagged'},
                     #                      {'name': 'iscsi_3par_1',
                     #                          'type': 'ethernet-networkV4',
                     #                          'vlanId': None,
                     #                          'purpose': 'General',
                     #                          'smartLink': True,
                     #                          'privateNetwork': False,
                     #                          'connectionTemplateUri': None,
                     #                          'ethernetNetworkType': 'Untagged'},
                     {'name': 'Net_2',
                      'type': 'ethernet-networkV4',
                      'vlanId': 2,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged',
                      'subnetUri': 'Eagle110_IPv4_Subnet'
                      },
                     ]


"""
These are the RANGES of ETHERNET networks you want to add to the appliance.
"""
# ethernet_ranges = [
# #JRT {'prefix': 'Net_', 'suffix': '', 'start': 1050, 'end': 3400, 'name': None, 'type': 'ethernet-networkV4',
# {'prefix': 'Net_', 'suffix': '', 'start': 3, 'end': 4034, 'name': None, 'type': 'ethernet-networkV4',
# 'vlanId': None, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False, 'connectionTemplateUri': None,
# 'ethernetNetworkType': 'Tagged'},
# ]

bulk_etherNet_network = [{"vlanIdRange": "3-4034", "purpose": "General", "namePrefix": "Net", "smartLink": True, "privateNetwork": False, "bandwidth": {"maximumBandwidth": 10000, "typicalBandwidth": 2000}, "type": "bulk-ethernet-networkV2"}]

"""
These are the network sets you want to add to the appliance.
NOTE: There are 2 fields that use data that MUST have also been defined in either 'ethernet_networks' or 'ethernet_ranges' above:
 networkUris = a list of network names that you want to include in the set.  Example ['net1', 'net2']
 nativeNetworkUri = a string with only 1 network name to use as the native network
"""
network_sets = [
    {'name': 'NS1', 'type': 'network-setV5', 'networkUris': rlist(4, 50, 'Net_', ''), 'nativeNetworkUri': 'Net_4'},
    {'name': 'NS2', 'type': 'network-setV5', 'networkUris': rlist(51, 150, 'Net_', ''), 'nativeNetworkUri': 'Net_51'},
    {'name': 'NS3', 'type': 'network-setV5', 'networkUris': rlist(151, 225, 'Net_', ''), 'nativeNetworkUri': 'Net_151'},
    {'name': 'NS4', 'type': 'network-setV5', 'networkUris': rlist(226, 400, 'Net_', ''), 'nativeNetworkUri': 'Net_226'},
    {'name': 'NS5', 'type': 'network-setV5', 'networkUris': rlist(401, 500, 'Net_', ''), 'nativeNetworkUri': 'Net_401'},
    {'name': 'NS6', 'type': 'network-setV5', 'networkUris': rlist(501, 583, 'Net_', ''), 'nativeNetworkUri': 'Net_501'},
    {'name': 'NS7', 'type': 'network-setV5', 'networkUris': rlist(584, 708, 'Net_', ''), 'nativeNetworkUri': 'Net_584'},
    {'name': 'NS8', 'type': 'network-setV5', 'networkUris': rlist(709, 805, 'Net_', ''), 'nativeNetworkUri': 'Net_709'},
    {'name': 'NS9', 'type': 'network-setV5', 'networkUris': rlist(806, 900, 'Net_', ''), 'nativeNetworkUri': 'Net_806'},
    {'name': 'NS10', 'type': 'network-setV5', 'networkUris': rlist(901, 925, 'Net_', ''), 'nativeNetworkUri': 'Net_901'},
    {'name': 'NS11', 'type': 'network-setV5', 'networkUris': rlist(926, 998, 'Net_', ''), 'nativeNetworkUri': 'Net_926'},
    {'name': 'NS12', 'type': 'network-setV5', 'networkUris': rlist(999, 1100, 'Net_', ''), 'nativeNetworkUri': 'Net_999'},
    {'name': 'NS13', 'type': 'network-setV5', 'networkUris': rlist(1101, 1200, 'Net_', ''), 'nativeNetworkUri': 'Net_1101'},
    {'name': 'NS14', 'type': 'network-setV5', 'networkUris': rlist(1201, 1300, 'Net_', ''), 'nativeNetworkUri': 'Net_1201'},
    {'name': 'NS15', 'type': 'network-setV5', 'networkUris': rlist(1301, 1400, 'Net_', ''), 'nativeNetworkUri': 'Net_1301'},
    {'name': 'NS16', 'type': 'network-setV5', 'networkUris': rlist(1401, 1495, 'Net_', ''), 'nativeNetworkUri': 'Net_1401'},
    {'name': 'NS17', 'type': 'network-setV5', 'networkUris': rlist(1496, 1594, 'Net_', ''), 'nativeNetworkUri': 'Net_1496'},
    {'name': 'NS18', 'type': 'network-setV5', 'networkUris': rlist(1595, 1694, 'Net_', ''), 'nativeNetworkUri': 'Net_1595'},
    {'name': 'NS19', 'type': 'network-setV5', 'networkUris': rlist(1696, 1793, 'Net_', ''), 'nativeNetworkUri': 'Net_1696'},
    {'name': 'NS20', 'type': 'network-setV5', 'networkUris': rlist(1794, 1892, 'Net_', ''), 'nativeNetworkUri': 'Net_1794'},
    {'name': 'NS21', 'type': 'network-setV5', 'networkUris': rlist(1893, 1992, 'Net_', ''), 'nativeNetworkUri': 'Net_1893'},
    {'name': 'NS22', 'type': 'network-setV5', 'networkUris': rlist(1993, 2027, 'Net_', ''), 'nativeNetworkUri': 'Net_1993'},
    {'name': 'NS23', 'type': 'network-setV5', 'networkUris': rlist(2028, 2062, 'Net_', ''), 'nativeNetworkUri': 'Net_2028'},
    {'name': 'NS24', 'type': 'network-setV5', 'networkUris': rlist(2063, 2097, 'Net_', ''), 'nativeNetworkUri': 'Net_2063'},
    {'name': 'NS25', 'type': 'network-setV5', 'networkUris': rlist(2098, 2132, 'Net_', ''), 'nativeNetworkUri': 'Net_2098'},
    {'name': 'NS26', 'type': 'network-setV5', 'networkUris': rlist(2133, 2167, 'Net_', ''), 'nativeNetworkUri': 'Net_2133'},
    {'name': 'NS27', 'type': 'network-setV5', 'networkUris': rlist(2168, 2202, 'Net_', ''), 'nativeNetworkUri': 'Net_2168'},
    {'name': 'NS28', 'type': 'network-setV5', 'networkUris': rlist(2203, 2237, 'Net_', ''), 'nativeNetworkUri': 'Net_2203'},
    {'name': 'NS29', 'type': 'network-setV5', 'networkUris': rlist(2238, 2272, 'Net_', ''), 'nativeNetworkUri': 'Net_2238'},
    {'name': 'NS30', 'type': 'network-setV5', 'networkUris': rlist(2273, 2307, 'Net_', ''), 'nativeNetworkUri': 'Net_2273'},
    {'name': 'NS31', 'type': 'network-setV5', 'networkUris': rlist(2308, 2342, 'Net_', ''), 'nativeNetworkUri': 'Net_2308'},
    {'name': 'NS32', 'type': 'network-setV5', 'networkUris': rlist(2343, 2377, 'Net_', ''), 'nativeNetworkUri': 'Net_2343'},
    {'name': 'NS33', 'type': 'network-setV5', 'networkUris': rlist(2378, 2412, 'Net_', ''), 'nativeNetworkUri': 'Net_2378'},
    {'name': 'NS34', 'type': 'network-setV5', 'networkUris': rlist(2413, 2447, 'Net_', ''), 'nativeNetworkUri': 'Net_2413'},
    {'name': 'NS35', 'type': 'network-setV5', 'networkUris': rlist(2448, 2490, 'Net_', ''), 'nativeNetworkUri': 'Net_2448'},
    {'name': 'NS36', 'type': 'network-setV5', 'networkUris': rlist(2491, 2589, 'Net_', ''), 'nativeNetworkUri': 'Net_2491'},
    {'name': 'NS37', 'type': 'network-setV5', 'networkUris': rlist(2590, 2689, 'Net_', ''), 'nativeNetworkUri': 'Net_2590'},
    {'name': 'NS38', 'type': 'network-setV5', 'networkUris': rlist(2690, 2788, 'Net_', ''), 'nativeNetworkUri': 'Net_2690'},
    {'name': 'NS39', 'type': 'network-setV5', 'networkUris': rlist(2789, 2888, 'Net_', ''), 'nativeNetworkUri': 'Net_2789'},
    {'name': 'NS40', 'type': 'network-setV5', 'networkUris': rlist(2889, 2987, 'Net_', ''), 'nativeNetworkUri': 'Net_2889'},
    {'name': 'NS41', 'type': 'network-setV5', 'networkUris': rlist(2988, 3070, 'Net_', ''), 'nativeNetworkUri': 'Net_2988'},
    {'name': 'NS42', 'type': 'network-setV5', 'networkUris': rlist(3071, 3153, 'Net_', ''), 'nativeNetworkUri': 'Net_3071'},
    {'name': 'NS43', 'type': 'network-setV5', 'networkUris': rlist(3154, 3236, 'Net_', ''), 'nativeNetworkUri': 'Net_3154'},
    {'name': 'NS44', 'type': 'network-setV5', 'networkUris': rlist(3237, 3319, 'Net_', ''), 'nativeNetworkUri': 'Net_3237'},
    {'name': 'NS45', 'type': 'network-setV5', 'networkUris': rlist(3320, 3402, 'Net_', ''), 'nativeNetworkUri': 'Net_3320'},
    {'name': 'NS46', 'type': 'network-setV5', 'networkUris': rlist(3403, 3485, 'Net_', ''), 'nativeNetworkUri': 'Net_3403'},
    {'name': 'NS47', 'type': 'network-setV5', 'networkUris': rlist(3486, 3585, 'Net_', ''), 'nativeNetworkUri': 'Net_3486'},
    {'name': 'NS48', 'type': 'network-setV5', 'networkUris': rlist(3586, 3685, 'Net_', ''), 'nativeNetworkUri': 'Net_3586'},
    {'name': 'NS49', 'type': 'network-setV5', 'networkUris': rlist(3686, 3775, 'Net_', ''), 'nativeNetworkUri': 'Net_3686'},
    {'name': 'NS50', 'type': 'network-setV5', 'networkUris': rlist(3840, 3939, 'Net_', ''), 'nativeNetworkUri': 'Net_3840'},
    {'name': 'NS51', 'type': 'network-setV5', 'networkUris': rlist(3940, 4034, 'Net_', ''), 'nativeNetworkUri': 'Net_3940'},
    {'name': 'NS52-Bigpipe-1', 'type': 'network-setV5', 'networkUris': rlist(2, 1999, 'Net_', ''), 'networkSetType': 'Large', 'nativeNetworkUri': 'Net_2'},
    {'name': 'NS53-Big-Pipe-ACI', 'type': 'network-setV5', 'networkUris': rlist(2000, 2999, 'Net_', ''), 'networkSetType': 'Regular', 'nativeNetworkUri': 'Net_2000'},
    {'name': 'NS54-Big-Pipe-2', 'type': 'network-setV5', 'networkUris': rlist(3000, 4034, 'Net_', ''), 'networkSetType': 'Large', 'nativeNetworkUri': 'Net_4000'}
]


"""
These are the network set ranges you want to add to the appliance.
NOTE: referenced ethernet network data that MUST have also been defined in either 'ethernet_networks' or 'ethernet_ranges' above:
 networkUris = This becomes populated with all the networks in the range you specify
 nativeNetworkUri = a string with only 1 network name to use as the native network
"""
# network_set_ranges = [
# {'prefix': 'NS', 'suffix': '', 'start': 1, 'end': 51, 'name': 'VlanTrunk1', 'type': 'network-setV300', 'networkUris': None, 'nativeNetworkUri': 'Net_2'},
# {'prefix': 'Net_', 'suffix': '', 'start': 161, 'end': 319, 'name': 'VlanTrunk2', 'type': 'network-setV300', 'networkUris': None, 'nativeNetworkUri': 'Net_161'},
# {'prefix': 'Net_', 'suffix': '', 'start': 320, 'end': 478, 'name': 'VlanTrunk3', 'type': 'network-setV300', 'networkUris': None, 'nativeNetworkUri': 'Net_320'},
# {'prefix': 'Net_', 'suffix': '', 'start': 479, 'end': 637, 'name': 'VlanTrunk4', 'type': 'network-setV300', 'networkUris': None, 'nativeNetworkUri': 'Net_479'},
# ]


"""
These are the FibreChannel networks you want to add to the appliance
"""
# fc_networks = [ {'name': 'FC-A', 'type': 'fc-networkV4', 'linkStabilityTime':30, 'autoLoginRedistribution':True, 'connectionTemplateUri': None, 'managedSanUri':None, 'fabricType':'FabricAttach'},
#                 {'name': 'FC-B', 'type': 'fc-networkV4', 'linkStabilityTime':30, 'autoLoginRedistribution':True, 'connectionTemplateUri': None, 'managedSanUri':None, 'fabricType':'FabricAttach'},
#                {'name': 'SAN-C-FA', 'type': 'fc-networkV4', 'linkStabilityTime':30, 'autoLoginRedistribution':True, 'connectionTemplateUri': None, 'managedSanUri':None, 'fabricType':'FabricAttach'},#JRT                 {'name': 'SAN-3A-FA', 'type': 'fc-networkV4', 'linkStabilityTime': 30, 'autoLoginRedistribution': True, 'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'},
# JRT 				{'name': 'SAN-3B-FA', 'type': 'fc-networkV4', 'linkStabilityTime': 30, 'autoLoginRedistribution': True, 'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'},
# JRT                 {'name': 'SAN-3A-DIRECT', 'type': 'fc-networkV4', 'linkStabilityTime': 30, 'autoLoginRedistribution': True, 'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'DirectAttach'},
# JRT                 {'name': 'SAN-6B-DIRECT', 'type': 'fc-networkV4', 'linkStabilityTime': 30, 'autoLoginRedistribution': True, 'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'DirectAttach'},
#                ]


"""
These are the FCoE networks you want to add to the appliance
"""
# fcoe_networks = [{'name': 'FCOE-3776', 'type': 'fcoe-networkV4', 'vlanId': 3776},
#                 {'name': 'FCOE_3808', 'type': 'fcoe-networkV4', 'vlanId': 3808},
#                 {'name': 'FCOE_201', 'type': 'fcoe-networkV4', 'vlanId': 201},
#                 {'name': 'FCOE_202', 'type': 'fcoe-networkV4', 'vlanId': 202},
#                 ]

"""
These are the RANGES of FCoE networks you want to add to the appliance.
"""
# fcoe_ranges = [{'prefix': 'FCOE-', 'suffix': '-A', 'start': 3776, 'end': 3807, 'type': 'fcoe-networkV4',},
# 			   {'prefix': 'FCOE-', 'suffix': '-B', 'start': 3808, 'end': 3839, 'type': 'fcoe-networkV4',},
# ]


"""
# Synergy
These are the enclosure group(s) you want to add to the appliance.
NOTE:  There are some special fields:
 enclosureTypeUri = /rest/enclosure-types/SY12000
 logicalInterconnectGroupUri = for each ic bay, you must specify 'LIG:' + the name of the LIG for that bay
                               The LIG you choose MUST be defined in your datafile (or exist on the appliance)
 enclosureCount = The number of enclosures in the group
"""
enc_groups = [
    {'name': 'EG-110-2ME',
     'enclosureCount': 2,
     'configurationScript': None,
     'interconnectBayMappings':
     [
         {'enclosureIndex': 1, 'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:LIG_Nitro_ACI'},
         {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
         {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
         #                                 {'enclosureIndex': 1, 'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG_Potash'},
         {'enclosureIndex': 1, 'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:LIG_Nitro_ACI'},
         {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
         {'interconnectBay': 6, 'logicalInterconnectGroupUri': None},
         #                                 {'enclosureIndex': 1, 'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG_Potash'},
         {'enclosureIndex': 2, 'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:LIG_Nitro_ACI'},
         #                                 {'enclosureIndex': 2, 'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG_Potash'},
         {'enclosureIndex': 2, 'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:LIG_Nitro_ACI'}
         #                                 {'enclosureIndex': 2, 'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG_Potash'}
     ],
     'ipAddressingMode': "DHCP",
     'ipRangeUris': [],
     'powerMode': "RedundantPowerSupply"
     }
]


"""
These are the TBird enclosure(s) you want to add to the appliance
NOTE: There is a special field:
 enclosureGroupUri = You must specify EG: + the name of the enclosure group to associate the enclosure with
                     The EG you choose MUST be defined in your datafile (or exist on the appliance)
"""
encs = [
    {'hostname': '15.186.9.110', 'username': 'Administrator', 'password': 'hpvse123', 'enclosureGroupUri': 'EG:EG-110-2ME', 'force': False, 'licensingIntent': 'OneViewNoiLO'},
]


"""
Rename your enclosures to the corresponding new names
"""

enc_names = {
    'MXQ80600H8': 'Eagle110_ENC1_MXQ80600H8',
    'MXQ80600H9': 'Eagle110_ENC2_MXQ80600H9'
}


"""
The uplinkset(s) you want to use in your LIG(s)
NOTE:  There are some special fields
 networkUris = a list of network names to include in the uplinkset
 nativeNetworkUri = a string containing the name of the network you want to be the native network
"""
uplink_sets = {
    'BigPipe-1': {'name': 'BigPipe-1',
                  'ethernetNetworkType': 'Tagged',
                  'consistencyChecking': 'ExactMatch',
                  'networkType': 'Ethernet',
                  'networkUris': make_range_list({'prefix': 'Net_', 'suffix': '', 'start': 4, 'end': 3775}) + make_range_list({'prefix': 'Net_', 'suffix': '', 'start': 3840, 'end': 4034},),
                  'nativeNetworkUri': None,
                  'mode': 'Auto',
                  'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '1', 'port': 'Q1', 'speed': 'Auto'},
                                             {'enclosure': '2', 'bay': '4', 'port': 'Q1', 'speed': 'Auto'}, ]},

    'Tunnel1': {'name': 'Tunnel1',
                'ethernetNetworkType': 'Tunnel',
                        'consistencyChecking': 'ExactMatch',
                'networkType': 'Ethernet',
                'networkUris': ['Tunnel1'],
                'nativeNetworkUri': None,
                'mode': 'Auto',
                'lacpTimer': 'Long',
                'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '1', 'port': 'Q2', 'speed': 'Auto'},
                                           {'enclosure': '2', 'bay': '4', 'port': 'Q2', 'speed': 'Auto'}, ]},
    'Eth_Q3_1': {'name': 'Eth_Q3_1',
                 'ethernetNetworkType': 'Tagged',
                 'consistencyChecking': 'ExactMatch',
                 'networkType': 'Ethernet',
                 'networkUris': ['Net_3777', 'Net_3809'],
                 'nativeNetworkUri': None,
                 'mode': 'Auto',
                 'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '1', 'port': 'Q3.1', 'speed': 'Auto'},
                                            {'enclosure': '2', 'bay': '4', 'port': 'Q3.1', 'speed': 'Auto'}, ]},
    'Eth_Q4_1': {'name': 'Eth_Q4_1',
                 'ethernetNetworkType': 'Tagged',
                 'consistencyChecking': 'ExactMatch',
                 'networkType': 'Ethernet',
                 'networkUris': ['Net_3'],
                 'nativeNetworkUri': None,
                 'mode': 'Auto',
                 'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '1', 'port': 'Q4.1', 'speed': 'Auto'},
                                            {'enclosure': '2', 'bay': '4', 'port': 'Q4.1', 'speed': 'Auto'}, ]},

    #      'SAN-C-FA': {'name': 'SAN-C-FA',
    #           'ethernetNetworkType': 'NotApplicable',
    #           'networkType': 'FibreChannel',
    #           'networkUris': ['SAN-C-FA'],
    #           'nativeNetworkUri': None,
    #           'mode': 'Auto',
    #           'logicalPortConfigInfos': [{'enclosure': '2', 'bay': '4', 'port': 'Q4.1', 'speed': 'Speed32G'},]},
    'Eth_Q5_1': {'name': 'Eth_Q5_1',
                 'ethernetNetworkType': 'Tagged',
                 'consistencyChecking': 'ExactMatch',
                 'networkType': 'Ethernet',
                 'networkUris': ['Net_3776', 'Net_3808'],
                 'nativeNetworkUri': None,
                 'mode': 'Auto',
                 'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '1', 'port': 'Q5.1', 'speed': 'Auto'},  # JN _ was 25
                                            {'enclosure': '2', 'bay': '4', 'port': 'Q5.1', 'speed': 'Auto'}, ]},

    'Untagged_ports': {'name': 'Untagged_ports',
                       'ethernetNetworkType': 'Untagged',
                       'consistencyChecking': 'ExactMatch',
                       'networkType': 'Ethernet',
                       'networkUris': ['Untagged-1'],
                       'nativeNetworkUri': None,
                       'mode': 'Auto',
                       'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '1', 'port': 'Q6.1', 'speed': 'Auto'},
                                                  {'enclosure': '2', 'bay': '4', 'port': 'Q6.1', 'speed': 'Auto'}, ]},  # JN _ was 25
    'BigPipe-1-new': {'name': 'BigPipe-1',
                      'ethernetNetworkType': 'Tagged',
                      'consistencyChecking': 'ExactMatch',
                      'networkType': 'Ethernet',
                      'networkUris': make_range_list({'prefix': 'Net_', 'suffix': '', 'start': 2, 'end': 1999}),
                      'nativeNetworkUri': 'Net_3',
                      'mode': 'Auto',
                      'lacpTimer': 'Long',
                      'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '1', 'port': 'Q1', 'speed': 'Auto'},
                                                 {'enclosure': '1', 'bay': '1', 'port': 'Q2', 'speed': 'Auto'},
                                                 {'enclosure': '2', 'bay': '4', 'port': 'Q1', 'speed': 'Auto'},
                                                 {'enclosure': '2', 'bay': '4', 'port': 'Q2', 'speed': 'Auto'}, ]},
    'BigPipe-2-new': {'name': 'BigPipe-2',
                      'ethernetNetworkType': 'Tagged',
                      'consistencyChecking': 'ExactMatch',
                      'networkType': 'Ethernet',
                      'networkUris': make_range_list({'prefix': 'Net_', 'suffix': '', 'start': 3000, 'end': 4034}),
                      'nativeNetworkUri': 'Net_4000',
                      'mode': 'Auto',
                      'lacpTimer': 'Long',
                      'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '1', 'port': 'Q3.1', 'speed': 'Speed25G', 'desiredFecMode': 'Cl74'},
                                                 {'enclosure': '1', 'bay': '1', 'port': 'Q3.2', 'speed': 'Speed25G', 'desiredFecMode': 'Cl74'},
                                                 {'enclosure': '1', 'bay': '1', 'port': 'Q3.3', 'speed': 'Speed25G', 'desiredFecMode': 'Cl74'},
                                                 {'enclosure': '1', 'bay': '1', 'port': 'Q3.4', 'speed': 'Speed25G', 'desiredFecMode': 'Cl74'},
                                                 {'enclosure': '1', 'bay': '1', 'port': 'Q4.1', 'speed': 'Speed25G', 'desiredFecMode': 'Cl74'},
                                                 {'enclosure': '1', 'bay': '1', 'port': 'Q4.2', 'speed': 'Speed25G', 'desiredFecMode': 'Cl74'},
                                                 {'enclosure': '1', 'bay': '1', 'port': 'Q4.3', 'speed': 'Speed25G', 'desiredFecMode': 'Cl74'},
                                                 {'enclosure': '1', 'bay': '1', 'port': 'Q4.4', 'speed': 'Speed25G', 'desiredFecMode': 'Cl74'},
                                                 {'enclosure': '2', 'bay': '4', 'port': 'Q3.1', 'speed': 'Speed25G', 'desiredFecMode': 'Cl74'},
                                                 {'enclosure': '2', 'bay': '4', 'port': 'Q3.2', 'speed': 'Speed25G', 'desiredFecMode': 'Cl74'},
                                                 {'enclosure': '2', 'bay': '4', 'port': 'Q3.3', 'speed': 'Speed25G', 'desiredFecMode': 'Cl74'},
                                                 {'enclosure': '2', 'bay': '4', 'port': 'Q3.4', 'speed': 'Speed25G', 'desiredFecMode': 'Cl74'},
                                                 {'enclosure': '2', 'bay': '4', 'port': 'Q4.1', 'speed': 'Speed25G', 'desiredFecMode': 'Cl74'},
                                                 {'enclosure': '2', 'bay': '4', 'port': 'Q4.2', 'speed': 'Speed25G', 'desiredFecMode': 'Cl74'},
                                                 {'enclosure': '2', 'bay': '4', 'port': 'Q4.3', 'speed': 'Speed25G', 'desiredFecMode': 'Cl74'},
                                                 {'enclosure': '2', 'bay': '4', 'port': 'Q4.4', 'speed': 'Speed25G', 'desiredFecMode': 'Cl74'}, ]},

    'Tunnel1_new': {'name': 'Tunnel1',
                    'ethernetNetworkType': 'Tunnel',
                    'consistencyChecking': 'ExactMatch',
                    'networkType': 'Ethernet',
                    'networkUris': ['Tunnel1'],
                    'nativeNetworkUri': None,
                    'mode': 'Auto',
                    'lacpTimer': 'Long',
                    'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '1', 'port': 'Q5.1', 'speed': 'Speed25G', 'desiredFecMode': 'None'},
                                               {'enclosure': '1', 'bay': '1', 'port': 'Q5.2', 'speed': 'Speed25G', 'desiredFecMode': 'None'},
                                               {'enclosure': '2', 'bay': '4', 'port': 'Q5.1', 'speed': 'Speed25G', 'desiredFecMode': 'None'},
                                               {'enclosure': '2', 'bay': '4', 'port': 'Q5.2', 'speed': 'Speed25G', 'desiredFecMode': 'None'}, ]},
    'Untagged': {'name': 'Untagged_ports',
                 'ethernetNetworkType': 'Untagged',
                 'consistencyChecking': 'ExactMatch',
                 'networkType': 'Ethernet',
                 'networkUris': ['Untagged-1'],
                 'nativeNetworkUri': None,
                 'mode': 'Auto',
                 'lacpTimer': 'Long',
                 'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '1', 'port': 'Q5.3', 'speed': 'Speed25G', 'desiredFecMode': 'None'},
                                            {'enclosure': '1', 'bay': '1', 'port': 'Q5.4', 'speed': 'Speed25G', 'desiredFecMode': 'None'},
                                            {'enclosure': '2', 'bay': '4', 'port': 'Q5.3', 'speed': 'Speed25G', 'desiredFecMode': 'None'},
                                            {'enclosure': '2', 'bay': '4', 'port': 'Q5.4', 'speed': 'Speed25G', 'desiredFecMode': 'None'}, ]},
    'BigPipe-2-ACI': {'name': 'BigPipe-ACI',
                      'ethernetNetworkType': 'Tagged',
                      'consistencyChecking': 'ExactMatch',
                      'networkType': 'Ethernet',
                      'networkUris': make_range_list({'prefix': 'Net_', 'suffix': '', 'start': 2000, 'end': 2999}),
                      'nativeNetworkUri': 'Net_2000',
                      'lacpTimer': 'Long',
                      'mode': 'Auto',
                      'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '1', 'port': 'Q6.1', 'speed': 'Speed25G', 'desiredFecMode': 'Cl74'},
                                                 {'enclosure': '1', 'bay': '1', 'port': 'Q6.2', 'speed': 'Speed25G', 'desiredFecMode': 'Cl74'},
                                                 {'enclosure': '1', 'bay': '1', 'port': 'Q6.3', 'speed': 'Speed25G', 'desiredFecMode': 'Cl74'},
                                                 {'enclosure': '1', 'bay': '1', 'port': 'Q6.4', 'speed': 'Speed25G', 'desiredFecMode': 'Cl74'},
                                                 {'enclosure': '2', 'bay': '4', 'port': 'Q6.1', 'speed': 'Speed25G', 'desiredFecMode': 'Cl74'},
                                                 {'enclosure': '2', 'bay': '4', 'port': 'Q6.2', 'speed': 'Speed25G', 'desiredFecMode': 'Cl74'},
                                                 {'enclosure': '2', 'bay': '4', 'port': 'Q6.3', 'speed': 'Speed25G', 'desiredFecMode': 'Cl74'},
                                                 {'enclosure': '2', 'bay': '4', 'port': 'Q6.4', 'speed': 'Speed25G', 'desiredFecMode': 'Cl74'}, ]},

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
 sflowConfiguration: dictionary of sflow attributes. Using 'ipMode':'Static' (is currently not supported in our setup code but will be adding this in the future) requires 2-step process: 1. create lig, 2. edit LI to set ipAddr and subnetMask. 'ipMode':'IpPool' is the one we currently used and is fully supported, this requires (all should be handled by the script provided that data file is set accordingly) the network defined in sflowNetwork to be created with subnetUri from the pool ('subnetUri':'<subnet name>'). In this ipMode of IpPool, ipAddr and subnetMask will be pulled from the IP/subnet pool during creation of LI.
"""
ligs = [
    # Nitro
    #       {
    #          'name': 'LIG_Nitro',
    #         'type': 'logical-interconnect-groupV6',
    #           'enclosureType': 'SY12000',
    #           'ethernetSettings': None,
    #           'consistencyCheckingForInternalNetworks': 'ExactMatch',
    #           'interconnectMapTemplate': [
    #               {'bay': 1, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
    #               {'bay': 4, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2},
    #               {'bay': 4, 'enclosure': 1, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 1},
    #               {'bay': 1, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2}
    #            ],
    #            'enclosureIndexes': [1,2],
    #            'interconnectBaySet': 1,
    #            'redundancyType': 'HighlyAvailable',
    #            'uplinkSets': [
    #                uplink_sets['BigPipe-1'],
    #                uplink_sets['Eth_Q3_1'],
    #                uplink_sets['Tunnel1'],
    #                uplink_sets['Eth_Q5_1'],
    #                uplink_sets['Untagged_ports'],
    #                uplink_sets['Eth_Q4_1']
    #            ],
    #            'stackingMode': 'Enclosure',
    #            'state': 'Active',
    #            'telemetryConfiguration': None,
    #            'snmpConfiguration': None,
    #            'downlinkSpeedMode':'SPEED_50GB',
    #        },
    {
        'name': 'LIG_Nitro_ACI',
        'type': 'logical-interconnect-groupV6',
        'enclosureType': 'SY12000',
        'ethernetSettings': {
            'enableTaggedLldp': True,
            'type': 'EthernetInterconnectSettingsV6'},
        'consistencyCheckingForInternalNetworks': 'ExactMatch',
        'interconnectMapTemplate': [
            {'bay': 1, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
            {'bay': 4, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2},
            {'bay': 4, 'enclosure': 1, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 1},
            {'bay': 1, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2}
        ],
        'enclosureIndexes': [1, 2],
        'interconnectBaySet': 1,
        'redundancyType': 'HighlyAvailable',
        'uplinkSets': [
            uplink_sets['BigPipe-1-new'],
            uplink_sets['BigPipe-2-new'],
            uplink_sets['Tunnel1_new'],
            uplink_sets['Untagged'],
            uplink_sets['BigPipe-2-ACI']
        ],
        'stackingMode': 'Enclosure',
        'state': 'Active',
        'telemetryConfiguration': None,
        'snmpConfiguration': None,
        'downlinkSpeedMode':'SPEED_50GB',
        "sflowConfiguration": {
                        "category": "sflow-configuration",
                        "consistencyChecking": "ExactMatch",
                        "enabled": True,
                        "sflowAgents": [
                            {
                                "ipMode": "IpPool",
                            }
                        ],
            "sflowCollectors": [
                            {
                                "collectorEnabled": True,
                                "collectorId": 1,
                                "ipAddress": "172.16.2.254",
                                "maxDatagramSize": 1400,
                                "maxHeaderSize": 256,
                                "name": "WinTCS",
                                "port": 6343
                            }
                        ],
            "sflowNetwork": {
                            "name": "Net_2",
                            "vlanId": 2
                        },
            "sflowPorts": [
                            {
                                "bayNumber": 1,
                                "collectorId": 1,
                                "enclosureIndex": 1,
                                "icmName": "Virtual Connect SE 100Gb F32 Module for Synergy",
                                "portName": "d1",
                                "sflowConfigurationModes": [
                                    {
                                        "configurationMode": "Polling",
                                        "pollingInterval": 20
                                    },
                                    {
                                        "configurationMode": "Sampling",
                                        "direction": "Both",
                                        "samplingRate": 256
                                    }
                                ]
                            },
                            {
                                "bayNumber": 4,
                                "collectorId": 1,
                                "enclosureIndex": 2,
                                "icmName": "Virtual Connect SE 100Gb F32 Module for Synergy",
                                "portName": "d1",
                                "sflowConfigurationModes": [
                                    {
                                        "configurationMode": "Polling",
                                        "pollingInterval": 20
                                    },
                                    {
                                        "configurationMode": "Sampling",
                                        "direction": "Both",
                                        "samplingRate": 256
                                    }
                                ]
                            },
                            {
                                "bayNumber": 4,
                                "collectorId": 1,
                                "enclosureIndex": 2,
                                "icmName": "Virtual Connect SE 100Gb F32 Module for Synergy",
                                "portName": "Q1",
                                "sflowConfigurationModes": [
                                    {
                                        "configurationMode": "Polling",
                                        "pollingInterval": 20
                                    },
                                    {
                                        "configurationMode": "Sampling",
                                        "direction": "Both",
                                        "samplingRate": 256
                                    }
                                ]
                            },
                            {
                                "bayNumber": 1,
                                "collectorId": 1,
                                "enclosureIndex": 1,
                                "icmName": "Virtual Connect SE 100Gb F32 Module for Synergy",
                                "portName": "Q2",
                                "sflowConfigurationModes": [
                                    {
                                        "configurationMode": "Polling",
                                        "pollingInterval": 20
                                    },
                                    {
                                        "configurationMode": "Sampling",
                                        "direction": "Both",
                                        "samplingRate": 256
                                    }
                                ]
                            },
                            {
                                "bayNumber": 4,
                                "collectorId": 1,
                                "enclosureIndex": 2,
                                "icmName": "Virtual Connect SE 100Gb F32 Module for Synergy",
                                "portName": "Q3:1",
                                "sflowConfigurationModes": [
                                    {
                                        "configurationMode": "Polling",
                                        "pollingInterval": 20
                                    },
                                    {
                                        "configurationMode": "Sampling",
                                        "direction": "Both",
                                        "samplingRate": 256
                                    }
                                ]
                            },
                            {
                                "bayNumber": 1,
                                "collectorId": 1,
                                "enclosureIndex": 1,
                                "icmName": "Virtual Connect SE 100Gb F32 Module for Synergy",
                                "portName": "Q4:1",
                                "sflowConfigurationModes": [
                                    {
                                        "configurationMode": "Polling",
                                        "pollingInterval": 20
                                    },
                                    {
                                        "configurationMode": "Sampling",
                                        "direction": "Both",
                                        "samplingRate": 256
                                    }
                                ]
                            },
                            {
                                "bayNumber": 1,
                                "collectorId": 1,
                                "enclosureIndex": 1,
                                "icmName": "Virtual Connect SE 100Gb F32 Module for Synergy",
                                "portName": "Q5:1",
                                "sflowConfigurationModes": [
                                    {
                                        "configurationMode": "Polling",
                                        "pollingInterval": 20
                                    },
                                    {
                                        "configurationMode": "Sampling",
                                        "direction": "Both",
                                        "samplingRate": 256
                                    }
                                ]
                            },
                            {
                                "bayNumber": 4,
                                "collectorId": 1,
                                "enclosureIndex": 2,
                                "icmName": "Virtual Connect SE 100Gb F32 Module for Synergy",
                                "portName": "Q5:1",
                                "sflowConfigurationModes": [
                                    {
                                        "configurationMode": "Polling",
                                        "pollingInterval": 20
                                    },
                                    {
                                        "configurationMode": "Sampling",
                                        "direction": "Both",
                                        "samplingRate": 256
                                    }
                                ]
                            },
                            {
                                "bayNumber": 1,
                                "collectorId": 1,
                                "enclosureIndex": 1,
                                "icmName": "Virtual Connect SE 100Gb F32 Module for Synergy",
                                "portName": "Q5:3",
                                "sflowConfigurationModes": [
                                    {
                                        "configurationMode": "Polling",
                                        "pollingInterval": 20
                                    },
                                    {
                                        "configurationMode": "Sampling",
                                        "direction": "Both",
                                        "samplingRate": 256
                                    }
                                ]
                            },
                            {
                                "bayNumber": 4,
                                "collectorId": 1,
                                "enclosureIndex": 2,
                                "icmName": "Virtual Connect SE 100Gb F32 Module for Synergy",
                                "portName": "Q5:3",
                                "sflowConfigurationModes": [
                                    {
                                        "configurationMode": "Polling",
                                        "pollingInterval": 20
                                    },
                                    {
                                        "configurationMode": "Sampling",
                                        "direction": "Both",
                                        "samplingRate": 256
                                    }
                                ]
                            },
                            {
                                "bayNumber": 1,
                                "collectorId": 1,
                                "enclosureIndex": 1,
                                "icmName": "Virtual Connect SE 100Gb F32 Module for Synergy",
                                "portName": "Q6:1",
                                "sflowConfigurationModes": [
                                    {
                                        "configurationMode": "Polling",
                                        "pollingInterval": 20
                                    },
                                    {
                                        "configurationMode": "Sampling",
                                        "direction": "Both",
                                        "samplingRate": 256
                                    }
                                ]
                            },
                            {
                                "bayNumber": 4,
                                "collectorId": 1,
                                "enclosureIndex": 2,
                                "icmName": "Virtual Connect SE 100Gb F32 Module for Synergy",
                                "portName": "Q6:1",
                                "sflowConfigurationModes": [
                                    {
                                        "configurationMode": "Polling",
                                        "pollingInterval": 20
                                    },
                                    {
                                        "configurationMode": "Sampling",
                                        "direction": "Both",
                                        "samplingRate": 256
                                    }
                                ]
                            }
                        ],
            "type": "sflow-configuration",
        },
    },

    # Potash
    #        {
    #            'name': 'LIG_Potash',
    #            'type': 'logical-interconnect-groupV6',
    #            'enclosureType': 'SY12000',
    #            'ethernetSettings': None,
    #            'interconnectMapTemplate': [
    #                {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
    #                {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
    #                {'bay': 6, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
    #                {'bay': 3, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2}
    #            ],
    #            'enclosureIndexes': [1,2],
    #            'interconnectBaySet': 3,
    #            'redundancyType': 'HighlyAvailable',
    #            'uplinkSets': [
    #            ],
    #            'stackingMode': 'Enclosure',
    #            'state': 'Active',
    #            'telemetryConfiguration': None,
    #            'snmpConfiguration': None
    #        }
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
les = [{'name': 'LE-2ME',
        'enclosureUris': ['ENC:Eagle110_ENC1_MXQ80600H8', 'ENC:Eagle110_ENC2_MXQ80600H9'],
        'enclosureGroupUri': 'EG:EG-110-2ME',
        'firmwareBaselineUri': None,
        'forceInstallFirmware': False
        }]


FORCE_PROFILE_APPLY = "all"

"""
Server Profile boot 'order' options are 'PXE' or 'HardDisk'.
"""
# server_profiles = [


server_profiles_nohw = [
    {'type': 'ServerProfileV11', 'serverHardwareUri': None,
     'serverHardwareTypeUri': 'SY 480 Gen10 1', 'enclosureGroupUri': 'EG:EG-110-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'CI-FIT-Eagle110-Enc1-Bay1', 'description': 'Eagle110 Bay1', 'affinity': 'Bay',
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'hideUnusedFlexNics':True,
     # 'serialNumber':'VCUVVV0000',
     # 'uuid':'9b9f89d1-a4b6-4045-88ed-7a310d6f57ef',
     'iscsiInitiatorName':'',
     'osDeploymentSettings':None,
     'connectionSettings':{
             'connections': [
                 {'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Untagged-1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG1', 'mac': '36:85:EA:C0:10:01', 'wwpn': '', 'wwnn': ''},
                 {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Untagged-1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG1', 'mac': '36:85:EA:C0:11:01', 'wwpn': '', 'wwnn': ''},
                 {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:Tunnel1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG2', 'mac': '36:85:EA:C0:10:02', 'wwpn': '', 'wwnn': ''},
                 {'id': 4, 'name': '4', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-b', 'requestedMbps': '2500', 'networkUri': 'ETH:Tunnel1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG2', 'mac': '36:85:EA:C0:11:02', 'wwpn': '', 'wwnn': ''},
                 {'id': 5, 'name': '5', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_3', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG3', 'mac': '36:85:EA:C0:10:03', 'wwpn': '', 'wwnn': ''},
                 {'id': 6, 'name': '6', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-c', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_3', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG3', 'mac': '36:85:EA:C0:11:03', 'wwpn': '', 'wwnn': ''},
                 {'id': 7, 'name': '7', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG4', 'mac': '36:85:EA:C0:10:04', 'wwpn': '', 'wwnn': ''},
                 {'id': 8, 'name': '8', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG4', 'mac': '36:85:EA:C0:11:04', 'wwpn': '', 'wwnn': ''},
                 {'id': 9, 'name': '9', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-e', 'requestedMbps': '2500', 'networkUri': 'NS:NS2', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG5', 'mac': '36:85:EA:C0:10:05', 'wwpn': '', 'wwnn': ''},
                 {'id': 10, 'name': '10', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-e', 'requestedMbps': '2500', 'networkUri': 'NS:NS2', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG5', 'mac': '36:85:EA:C0:11:05', 'wwpn': '', 'wwnn': ''},
                 {'id': 11, 'name': '11', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-f', 'requestedMbps': '2500', 'networkUri': 'NS:NS3', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG6', 'mac': '36:85:EA:C0:10:06', 'wwpn': '', 'wwnn': ''},
                 {'id': 12, 'name': '12', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-f', 'requestedMbps': '2500', 'networkUri': 'NS:NS3', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG6', 'mac': '36:85:EA:C0:11:06', 'wwpn': '', 'wwnn': ''},
                 {'id': 13, 'name': '13', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-g', 'requestedMbps': '2500', 'networkUri': 'NS:NS4', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG7', 'mac': '36:85:EA:C0:10:07', 'wwpn': '', 'wwnn': ''},
                 {'id': 14, 'name': '14', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-g', 'requestedMbps': '2500', 'networkUri': 'NS:NS4', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG7', 'mac': '36:85:EA:C0:11:07', 'wwpn': '', 'wwnn': ''},
                 {'id': 15, 'name': '15', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-h', 'requestedMbps': '2500', 'networkUri': 'NS:NS5', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG8', 'mac': '36:85:EA:C0:10:08', 'wwpn': '', 'wwnn': ''},
                 {'id': 16, 'name': '16', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-h', 'requestedMbps': '2500', 'networkUri': 'NS:NS5', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG8', 'mac': '36:85:EA:C0:11:08', 'wwpn': '', 'wwnn': ''},
             ]}},

    {'type': 'ServerProfileV11', 'serverHardwareUri': None,
     'serverHardwareTypeUri': 'SY 480 Gen10 1', 'enclosureGroupUri': 'EG:EG-110-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'CI-FIT-Eagle110-Enc1-Bay2', 'description': 'Eagle110 Bay2', 'affinity': 'Bay',
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'hideUnusedFlexNics':True,
     'iscsiInitiatorName':'',
     'osDeploymentSettings':None,
     'connectionSettings':{
             'connections': [
                 {'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Untagged-1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG1', 'mac': '36:85:EA:C0:10:09', 'wwpn': '', 'wwnn': ''},
                 {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Untagged-1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG1', 'mac': '36:85:EA:C0:11:09', 'wwpn': '', 'wwnn': ''},
                 {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_3776', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG2', 'mac': '36:85:EA:C0:10:0A', 'wwpn': '', 'wwnn': ''},
                 {'id': 4, 'name': '4', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-b', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_3776', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG2', 'mac': '36:85:EA:C0:11:0A', 'wwpn': '', 'wwnn': ''},
                 {'id': 5, 'name': '5', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-c', 'requestedMbps': '2500', 'networkUri': 'NS:NS6', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG3', 'mac': '36:85:EA:C0:10:0B', 'wwpn': '', 'wwnn': ''},
                 {'id': 6, 'name': '6', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-c', 'requestedMbps': '2500', 'networkUri': 'NS:NS6', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG3', 'mac': '36:85:EA:C0:11:0B', 'wwpn': '', 'wwnn': ''},
                 {'id': 7, 'name': '7', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS7', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG4', 'mac': '36:85:EA:C0:10:0C', 'wwpn': '', 'wwnn': ''},
                 {'id': 8, 'name': '8', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS7', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG4', 'mac': '36:85:EA:C0:11:0C', 'wwpn': '', 'wwnn': ''},
                 {'id': 9, 'name': '9', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-e', 'requestedMbps': '2500', 'networkUri': 'NS:NS8', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG5', 'mac': '36:85:EA:C0:10:0D', 'wwpn': '', 'wwnn': ''},
                 {'id': 10, 'name': '10', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-e', 'requestedMbps': '2500', 'networkUri': 'NS:NS8', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG5', 'mac': '36:85:EA:C0:11:0D', 'wwpn': '', 'wwnn': ''},
                 {'id': 11, 'name': '11', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-f', 'requestedMbps': '2500', 'networkUri': 'NS:NS9', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG6', 'mac': '36:85:EA:C0:10:0E', 'wwpn': '', 'wwnn': ''},
                 {'id': 12, 'name': '12', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-f', 'requestedMbps': '2500', 'networkUri': 'NS:NS9', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG6', 'mac': '36:85:EA:C0:11:0E', 'wwpn': '', 'wwnn': ''},
                 {'id': 13, 'name': '13', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-g', 'requestedMbps': '2500', 'networkUri': 'NS:NS10', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG7', 'mac': '36:85:EA:C0:10:0F', 'wwpn': '', 'wwnn': ''},
                 {'id': 14, 'name': '14', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-g', 'requestedMbps': '2500', 'networkUri': 'NS:NS10', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG7', 'mac': '36:85:EA:C0:11:0F', 'wwpn': '', 'wwnn': ''},
                 {'id': 15, 'name': '15', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-h', 'requestedMbps': '2500', 'networkUri': 'NS:NS11', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG8', 'mac': '36:85:EA:C0:10:10', 'wwpn': '', 'wwnn': ''},
                 {'id': 16, 'name': '16', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-h', 'requestedMbps': '2500', 'networkUri': 'NS:NS11', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG8', 'mac': '36:85:EA:C0:11:10', 'wwpn': '', 'wwnn': ''},
             ]}},

    {'type': 'ServerProfileV11', 'serverHardwareUri': None,
     'serverHardwareTypeUri': 'SY 480 Gen10 1', 'enclosureGroupUri': 'EG:EG-110-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'CI-FIT-Eagle110-Enc1-Bay3', 'description': 'Eagle110 Bay3', 'affinity': 'Bay',
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'hideUnusedFlexNics':True,
     'iscsiInitiatorName':'',
     'osDeploymentSettings':None,
     'connectionSettings':{
             'connections': [
                 {'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Untagged-1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG1', 'mac': '36:85:EA:C0:10:11', 'wwpn': '', 'wwnn': ''},
                 {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Untagged-1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG1', 'mac': '36:85:EA:C0:11:11', 'wwpn': '', 'wwnn': ''},
                 {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_3777', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG2', 'mac': '36:85:EA:C0:10:12', 'wwpn': '', 'wwnn': ''},
                 {'id': 4, 'name': '4', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-b', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_3777', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG2', 'mac': '36:85:EA:C0:11:12', 'wwpn': '', 'wwnn': ''},
                 {'id': 5, 'name': '5', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-c', 'requestedMbps': '2500', 'networkUri': 'NS:NS12', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG3', 'mac': '36:85:EA:C0:10:13', 'wwpn': '', 'wwnn': ''},
                 {'id': 6, 'name': '6', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-c', 'requestedMbps': '2500', 'networkUri': 'NS:NS12', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG3', 'mac': '36:85:EA:C0:11:13', 'wwpn': '', 'wwnn': ''},
                 {'id': 7, 'name': '7', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS13', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG4', 'mac': '36:85:EA:C0:10:14', 'wwpn': '', 'wwnn': ''},
                 {'id': 8, 'name': '8', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS13', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG4', 'mac': '36:85:EA:C0:11:14', 'wwpn': '', 'wwnn': ''},
                 {'id': 9, 'name': '9', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-e', 'requestedMbps': '2500', 'networkUri': 'NS:NS14', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG5', 'mac': '36:85:EA:C0:10:15', 'wwpn': '', 'wwnn': ''},
                 {'id': 10, 'name': '10', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-e', 'requestedMbps': '2500', 'networkUri': 'NS:NS14', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG5', 'mac': '36:85:EA:C0:11:15', 'wwpn': '', 'wwnn': ''},
                 {'id': 11, 'name': '11', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-f', 'requestedMbps': '2500', 'networkUri': 'NS:NS15', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG6', 'mac': '36:85:EA:C0:10:16', 'wwpn': '', 'wwnn': ''},
                 {'id': 12, 'name': '12', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-f', 'requestedMbps': '2500', 'networkUri': 'NS:NS15', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG6', 'mac': '36:85:EA:C0:11:16', 'wwpn': '', 'wwnn': ''},
                 {'id': 13, 'name': '13', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-g', 'requestedMbps': '2500', 'networkUri': 'NS:NS16', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG7', 'mac': '36:85:EA:C0:10:17', 'wwpn': '', 'wwnn': ''},
                 {'id': 14, 'name': '14', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-g', 'requestedMbps': '2500', 'networkUri': 'NS:NS16', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG7', 'mac': '36:85:EA:C0:11:17', 'wwpn': '', 'wwnn': ''},
                 {'id': 15, 'name': '15', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-h', 'requestedMbps': '2500', 'networkUri': 'ETH:Tunnel1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG8', 'mac': '36:85:EA:C0:10:18', 'wwpn': '', 'wwnn': ''},
                 {'id': 16, 'name': '16', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-h', 'requestedMbps': '2500', 'networkUri': 'ETH:Tunnel1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG8', 'mac': '36:85:EA:C0:11:18', 'wwpn': '', 'wwnn': ''},
             ]}},

    {'type': 'ServerProfileV11', 'serverHardwareUri': None,
     'serverHardwareTypeUri': 'SY 480 Gen10 1', 'enclosureGroupUri': 'EG:EG-110-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'CI-FIT-Eagle110-Enc1-Bay4', 'description': 'Eagle110 Bay4', 'affinity': 'Bay',
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'hideUnusedFlexNics':True,
     'iscsiInitiatorName':'',
     'osDeploymentSettings':None,
     'connectionSettings':{
             'connections': [
                 {'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Untagged-1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG1', 'mac': '36:85:EA:C0:10:19', 'wwpn': '', 'wwnn': ''},
                 {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Untagged-1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG1', 'mac': '36:85:EA:C0:11:19', 'wwpn': '', 'wwnn': ''},
                 {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-b', 'requestedMbps': '2500', 'networkUri': 'NS:NS17', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG2', 'mac': '36:85:EA:C0:10:1A', 'wwpn': '', 'wwnn': ''},
                 {'id': 4, 'name': '4', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-b', 'requestedMbps': '2500', 'networkUri': 'NS:NS17', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG2', 'mac': '36:85:EA:C0:11:1A', 'wwpn': '', 'wwnn': ''},
                 {'id': 5, 'name': '5', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_3', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG3', 'mac': '36:85:EA:C0:10:1B', 'wwpn': '', 'wwnn': ''},
                 {'id': 6, 'name': '6', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-c', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_3', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG3', 'mac': '36:85:EA:C0:11:1B', 'wwpn': '', 'wwnn': ''},

                 #                    {'id': 3, 'name': '3', 'functionType': 'iSCSI', 'portId': 'Mezz 1:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:iSCSI-Net_3', 'mac': '36:85:EA:C0:10:1A', 'wwpn': '', 'wwnn': '', 'requestedVFs':None, 'ipv4':{'ipAddressSource':'UserDefined', 'subnetMask':'255.255.255.0', 'gateway':'', 'ipAddress':'10.1.1.5'},'boot':{'priority':'Primary', 'bootVlanId':'', 'bootVolumeSource':'UserDefined', 'iscsi':{'initiatorNameSource':'UserDefined', 'firstBootTargetIp':'10.1.1.1', 'firstBootTargetPort':'3260', 'secondBootTargetIp':'', 'secondBootTargetPort':'', 'chapLevel':'None', 'initiatorName':'iqn.2015-02.com.hpe:oneview-vcupm9w00m', 'bootTargetName':'iqn.2000-05.com.3pardata:20210002ac019d91', 'bootTargetLun':'0', 'chapName':'', 'chapSecret':None, 'mutualChapName':'', 'mutualChapSecret':None}}},
                 #                    {'id': 4, 'name': '4', 'functionType': 'iSCSI', 'portId': 'Mezz 1:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:iSCSI-Net_3', 'mac': '36:85:EA:C0:11:1A', 'wwpn': '', 'wwnn': '', 'requestedVFs':None, 'ipv4':{'ipAddressSource':'UserDefined', 'subnetMask':'255.255.255.0', 'gateway':'', 'ipAddress':'10.1.1.5'},'boot':{'priority':'Primary', 'bootVlanId':'', 'bootVolumeSource':'UserDefined', 'iscsi':{'initiatorNameSource':'UserDefined', 'firstBootTargetIp':'10.1.1.1', 'firstBootTargetPort':'3260', 'secondBootTargetIp':'', 'secondBootTargetPort':'', 'chapLevel':'None', 'initiatorName':'iqn.2015-02.com.hpe:oneview-vcupm9w00m', 'bootTargetName':'iqn.2000-05.com.3pardata:20210002ac019d91', 'bootTargetLun':'0', 'chapName':'', 'chapSecret':None, 'mutualChapName':'', 'mutualChapSecret':None}}},
                 {'id': 7, 'name': '7', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS18', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG4', 'mac': '36:85:EA:C0:10:1C', 'wwpn': '', 'wwnn': ''},
                 {'id': 8, 'name': '8', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS18', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG4', 'mac': '36:85:EA:C0:11:1C', 'wwpn': '', 'wwnn': ''},
                 {'id': 9, 'name': '9', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-e', 'requestedMbps': '2500', 'networkUri': 'ETH:Tunnel1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG5', 'mac': '36:85:EA:C0:10:1D', 'wwpn': '', 'wwnn': ''},
                 {'id': 10, 'name': '10', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-e', 'requestedMbps': '2500', 'networkUri': 'ETH:Tunnel1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG5', 'mac': '36:85:EA:C0:11:1D', 'wwpn': '', 'wwnn': ''},
                 {'id': 11, 'name': '11', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-f', 'requestedMbps': '2500', 'networkUri': 'NS:NS19', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG6', 'mac': '36:85:EA:C0:10:1E', 'wwpn': '', 'wwnn': ''},
                 {'id': 12, 'name': '12', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-f', 'requestedMbps': '2500', 'networkUri': 'NS:NS19', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG6', 'mac': '36:85:EA:C0:11:1E', 'wwpn': '', 'wwnn': ''},
                 {'id': 13, 'name': '13', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-g', 'requestedMbps': '2500', 'networkUri': 'NS:NS20', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG7', 'mac': '36:85:EA:C0:10:1F', 'wwpn': '', 'wwnn': ''},
                 {'id': 14, 'name': '14', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-g', 'requestedMbps': '2500', 'networkUri': 'NS:NS20', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG7', 'mac': '36:85:EA:C0:11:1F', 'wwpn': '', 'wwnn': ''},
                 {'id': 15, 'name': '15', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-h', 'requestedMbps': '2500', 'networkUri': 'NS:NS21', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG8', 'mac': '36:85:EA:C0:10:20', 'wwpn': '', 'wwnn': ''},
                 {'id': 16, 'name': '16', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-h', 'requestedMbps': '2500', 'networkUri': 'NS:NS21', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG8', 'mac': '36:85:EA:C0:11:20', 'wwpn': '', 'wwnn': ''},
             ]}},

    {'type': 'ServerProfileV11', 'serverHardwareUri': None,
     'serverHardwareTypeUri': 'SY 660 Gen10 1', 'enclosureGroupUri': 'EG:EG-110-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'CI-FIT-Eagle110-Enc1-Bay5', 'description': 'Eagle110 Gen10 FH Bay5', 'affinity': 'Bay',
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'hideUnusedFlexNics':True,
     'iscsiInitiatorName':'',
     'osDeploymentSettings':None,
     'connectionSettings':{
             'connections': [
                 {'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Untagged-1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG1', 'mac': '36:85:EA:C0:10:21', 'wwpn': '', 'wwnn': ''},
                 {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Untagged-1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG1', 'mac': '36:85:EA:C0:11:21', 'wwpn': '', 'wwnn': ''},
                 {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_3808', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG2', 'mac': '36:85:EA:C0:10:22', 'wwpn': '', 'wwnn': ''},
                 {'id': 4, 'name': '4', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-b', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_3808', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG2', 'mac': '36:85:EA:C0:11:22', 'wwpn': '', 'wwnn': ''},
                 {'id': 5, 'name': '5', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-c', 'requestedMbps': '2500', 'networkUri': 'NS:NS22', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG3', 'mac': '36:85:EA:C0:10:23', 'wwpn': '', 'wwnn': ''},
                 {'id': 6, 'name': '6', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-c', 'requestedMbps': '2500', 'networkUri': 'NS:NS22', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG3', 'mac': '36:85:EA:C0:11:23', 'wwpn': '', 'wwnn': ''},
                 {'id': 7, 'name': '7', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS23', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG4', 'mac': '36:85:EA:C0:10:24', 'wwpn': '', 'wwnn': ''},
                 {'id': 8, 'name': '8', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS23', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG4', 'mac': '36:85:EA:C0:11:24', 'wwpn': '', 'wwnn': ''},
                 {'id': 9, 'name': '9', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-e', 'requestedMbps': '2500', 'networkUri': 'NS:NS24', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG5', 'mac': '36:85:EA:C0:10:25', 'wwpn': '', 'wwnn': ''},
                 {'id': 10, 'name': '10', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-e', 'requestedMbps': '2500', 'networkUri': 'NS:NS24', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG5', 'mac': '36:85:EA:C0:11:25', 'wwpn': '', 'wwnn': ''},
                 {'id': 11, 'name': '11', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-f', 'requestedMbps': '2500', 'networkUri': 'NS:NS25', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG6', 'mac': '36:85:EA:C0:10:26', 'wwpn': '', 'wwnn': ''},
                 {'id': 12, 'name': '12', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-f', 'requestedMbps': '2500', 'networkUri': 'NS:NS25', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG6', 'mac': '36:85:EA:C0:11:26', 'wwpn': '', 'wwnn': ''},
                 {'id': 13, 'name': '13', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-g', 'requestedMbps': '2500', 'networkUri': 'NS:NS26', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG7', 'mac': '36:85:EA:C0:10:27', 'wwpn': '', 'wwnn': ''},
                 {'id': 14, 'name': '14', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-g', 'requestedMbps': '2500', 'networkUri': 'NS:NS26', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG7', 'mac': '36:85:EA:C0:11:27', 'wwpn': '', 'wwnn': ''},
                 {'id': 15, 'name': '15', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-h', 'requestedMbps': '2500', 'networkUri': 'NS:NS27', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG8', 'mac': '36:85:EA:C0:10:28', 'wwpn': '', 'wwnn': ''},
                 {'id': 16, 'name': '16', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-h', 'requestedMbps': '2500', 'networkUri': 'NS:NS27', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG8', 'mac': '36:85:EA:C0:11:28', 'wwpn': '', 'wwnn': ''},
                 {'id': 17, 'name': '17', 'functionType': 'Ethernet', 'portId': 'Mezz 4:1-a', 'requestedMbps': '2500', 'networkUri': 'NS:NS28', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG9', 'mac': '36:85:EA:C0:10:29', 'wwpn': '', 'wwnn': ''},
                 {'id': 18, 'name': '18', 'functionType': 'Ethernet', 'portId': 'Mezz 4:2-a', 'requestedMbps': '2500', 'networkUri': 'NS:NS28', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG9', 'mac': '36:85:EA:C0:11:29', 'wwpn': '', 'wwnn': ''},
                 {'id': 19, 'name': '19', 'functionType': 'Ethernet', 'portId': 'Mezz 4:1-b', 'requestedMbps': '2500', 'networkUri': 'NS:NS29', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG10', 'mac': '36:85:EA:C0:10:2A', 'wwpn': '', 'wwnn': ''},
                 {'id': 20, 'name': '20', 'functionType': 'Ethernet', 'portId': 'Mezz 4:2-b', 'requestedMbps': '2500', 'networkUri': 'NS:NS29', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG10', 'mac': '36:85:EA:C0:11:2A', 'wwpn': '', 'wwnn': ''},
                 {'id': 21, 'name': '21', 'functionType': 'Ethernet', 'portId': 'Mezz 4:1-c', 'requestedMbps': '2500', 'networkUri': 'NS:NS30', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG11', 'mac': '36:85:EA:C0:10:2B', 'wwpn': '', 'wwnn': ''},
                 {'id': 22, 'name': '22', 'functionType': 'Ethernet', 'portId': 'Mezz 4:2-c', 'requestedMbps': '2500', 'networkUri': 'NS:NS30', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG11', 'mac': '36:85:EA:C0:11:2B', 'wwpn': '', 'wwnn': ''},
                 {'id': 23, 'name': '23', 'functionType': 'Ethernet', 'portId': 'Mezz 4:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS31', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG12', 'mac': '36:85:EA:C0:10:2C', 'wwpn': '', 'wwnn': ''},
                 {'id': 24, 'name': '24', 'functionType': 'Ethernet', 'portId': 'Mezz 4:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS31', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG12', 'mac': '36:85:EA:C0:11:2C', 'wwpn': '', 'wwnn': ''},
                 {'id': 25, 'name': '25', 'functionType': 'Ethernet', 'portId': 'Mezz 4:1-e', 'requestedMbps': '2500', 'networkUri': 'NS:NS32', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG13', 'mac': '36:85:EA:C0:10:2D', 'wwpn': '', 'wwnn': ''},
                 {'id': 26, 'name': '26', 'functionType': 'Ethernet', 'portId': 'Mezz 4:2-e', 'requestedMbps': '2500', 'networkUri': 'NS:NS32', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG13', 'mac': '36:85:EA:C0:11:2D', 'wwpn': '', 'wwnn': ''},
                 {'id': 27, 'name': '27', 'functionType': 'Ethernet', 'portId': 'Mezz 4:1-f', 'requestedMbps': '2500', 'networkUri': 'NS:NS33', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG14', 'mac': '36:85:EA:C0:10:2E', 'wwpn': '', 'wwnn': ''},
                 {'id': 28, 'name': '28', 'functionType': 'Ethernet', 'portId': 'Mezz 4:2-f', 'requestedMbps': '2500', 'networkUri': 'NS:NS33', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG14', 'mac': '36:85:EA:C0:11:2E', 'wwpn': '', 'wwnn': ''},
                 {'id': 29, 'name': '29', 'functionType': 'Ethernet', 'portId': 'Mezz 4:1-g', 'requestedMbps': '2500', 'networkUri': 'NS:NS34', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG15', 'mac': '36:85:EA:C0:10:2F', 'wwpn': '', 'wwnn': ''},
                 {'id': 30, 'name': '30', 'functionType': 'Ethernet', 'portId': 'Mezz 4:2-g', 'requestedMbps': '2500', 'networkUri': 'NS:NS34', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG15', 'mac': '36:85:EA:C0:11:2F', 'wwpn': '', 'wwnn': ''},
                 {'id': 31, 'name': '31', 'functionType': 'Ethernet', 'portId': 'Mezz 4:1-h', 'requestedMbps': '2500', 'networkUri': 'NS:NS35', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG16', 'mac': '36:85:EA:C0:10:30', 'wwpn': '', 'wwnn': ''},
                 {'id': 32, 'name': '32', 'functionType': 'Ethernet', 'portId': 'Mezz 4:2-h', 'requestedMbps': '2500', 'networkUri': 'NS:NS35', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG16', 'mac': '36:85:EA:C0:11:30', 'wwpn': '', 'wwnn': ''},
             ]}},

    {'type': 'ServerProfileV11', 'serverHardwareUri': None,
     'serverHardwareTypeUri': 'SY 660 Gen10 1', 'enclosureGroupUri': 'EG:EG-110-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'CI-FIT-Eagle110-Enc1-Bay6', 'description': 'Eagle110 Gen10 FH Bay6', 'affinity': 'Bay',
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'hideUnusedFlexNics':True,
     'iscsiInitiatorName':'',
     'osDeploymentSettings':None,
     'connectionSettings':{
             'connections': [
                 {'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Untagged-1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG1', 'mac': '36:85:EA:C0:10:31', 'wwpn': '', 'wwnn': ''},
                 {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Untagged-1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG1', 'mac': '36:85:EA:C0:11:31', 'wwpn': '', 'wwnn': ''},
                 {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_3809', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG2', 'mac': '36:85:EA:C0:10:32', 'wwpn': '', 'wwnn': ''},
                 {'id': 4, 'name': '4', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-b', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_3809', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG2', 'mac': '36:85:EA:C0:11:32', 'wwpn': '', 'wwnn': ''},
                 {'id': 5, 'name': '5', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-c', 'requestedMbps': '2500', 'networkUri': 'NS:NS22', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG3', 'mac': '36:85:EA:C0:10:33', 'wwpn': '', 'wwnn': ''},
                 {'id': 6, 'name': '6', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-c', 'requestedMbps': '2500', 'networkUri': 'NS:NS22', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG3', 'mac': '36:85:EA:C0:11:33', 'wwpn': '', 'wwnn': ''},
                 {'id': 7, 'name': '7', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS23', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG4', 'mac': '36:85:EA:C0:10:34', 'wwpn': '', 'wwnn': ''},
                 {'id': 8, 'name': '8', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS23', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG4', 'mac': '36:85:EA:C0:11:34', 'wwpn': '', 'wwnn': ''},
                 {'id': 9, 'name': '9', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-e', 'requestedMbps': '2500', 'networkUri': 'NS:NS24', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG5', 'mac': '36:85:EA:C0:10:35', 'wwpn': '', 'wwnn': ''},
                 {'id': 10, 'name': '10', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-e', 'requestedMbps': '2500', 'networkUri': 'NS:NS24', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG5', 'mac': '36:85:EA:C0:11:35', 'wwpn': '', 'wwnn': ''},
                 {'id': 11, 'name': '11', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-f', 'requestedMbps': '2500', 'networkUri': 'NS:NS25', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG6', 'mac': '36:85:EA:C0:10:36', 'wwpn': '', 'wwnn': ''},
                 {'id': 12, 'name': '12', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-f', 'requestedMbps': '2500', 'networkUri': 'NS:NS25', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG6', 'mac': '36:85:EA:C0:11:36', 'wwpn': '', 'wwnn': ''},
                 {'id': 13, 'name': '13', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-g', 'requestedMbps': '2500', 'networkUri': 'NS:NS26', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG7', 'mac': '36:85:EA:C0:10:37', 'wwpn': '', 'wwnn': ''},
                 {'id': 14, 'name': '14', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-g', 'requestedMbps': '2500', 'networkUri': 'NS:NS26', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG7', 'mac': '36:85:EA:C0:11:37', 'wwpn': '', 'wwnn': ''},
                 {'id': 15, 'name': '15', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-h', 'requestedMbps': '2500', 'networkUri': 'NS:NS27', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG8', 'mac': '36:85:EA:C0:10:38', 'wwpn': '', 'wwnn': ''},
                 {'id': 16, 'name': '16', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-h', 'requestedMbps': '2500', 'networkUri': 'NS:NS27', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG8', 'mac': '36:85:EA:C0:11:38', 'wwpn': '', 'wwnn': ''},
                 {'id': 17, 'name': '17', 'functionType': 'Ethernet', 'portId': 'Mezz 4:1-a', 'requestedMbps': '2500', 'networkUri': 'NS:NS28', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG9', 'mac': '36:85:EA:C0:10:39', 'wwpn': '', 'wwnn': ''},
                 {'id': 18, 'name': '18', 'functionType': 'Ethernet', 'portId': 'Mezz 4:2-a', 'requestedMbps': '2500', 'networkUri': 'NS:NS28', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG9', 'mac': '36:85:EA:C0:11:39', 'wwpn': '', 'wwnn': ''},
                 {'id': 19, 'name': '19', 'functionType': 'Ethernet', 'portId': 'Mezz 4:1-b', 'requestedMbps': '2500', 'networkUri': 'NS:NS29', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG10', 'mac': '36:85:EA:C0:10:3A', 'wwpn': '', 'wwnn': ''},
                 {'id': 20, 'name': '20', 'functionType': 'Ethernet', 'portId': 'Mezz 4:2-b', 'requestedMbps': '2500', 'networkUri': 'NS:NS29', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG10', 'mac': '36:85:EA:C0:11:3A', 'wwpn': '', 'wwnn': ''},
                 {'id': 21, 'name': '21', 'functionType': 'Ethernet', 'portId': 'Mezz 4:1-c', 'requestedMbps': '2500', 'networkUri': 'NS:NS30', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG11', 'mac': '36:85:EA:C0:10:3B', 'wwpn': '', 'wwnn': ''},
                 {'id': 22, 'name': '22', 'functionType': 'Ethernet', 'portId': 'Mezz 4:2-c', 'requestedMbps': '2500', 'networkUri': 'NS:NS30', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG11', 'mac': '36:85:EA:C0:11:3B', 'wwpn': '', 'wwnn': ''},
                 {'id': 23, 'name': '23', 'functionType': 'Ethernet', 'portId': 'Mezz 4:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS31', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG12', 'mac': '36:85:EA:C0:10:3C', 'wwpn': '', 'wwnn': ''},
                 {'id': 24, 'name': '24', 'functionType': 'Ethernet', 'portId': 'Mezz 4:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS31', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG12', 'mac': '36:85:EA:C0:11:3C', 'wwpn': '', 'wwnn': ''},
                 {'id': 25, 'name': '25', 'functionType': 'Ethernet', 'portId': 'Mezz 4:1-e', 'requestedMbps': '2500', 'networkUri': 'NS:NS32', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG13', 'mac': '36:85:EA:C0:10:3D', 'wwpn': '', 'wwnn': ''},
                 {'id': 26, 'name': '26', 'functionType': 'Ethernet', 'portId': 'Mezz 4:2-e', 'requestedMbps': '2500', 'networkUri': 'NS:NS32', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG13', 'mac': '36:85:EA:C0:11:3D', 'wwpn': '', 'wwnn': ''},
                 {'id': 27, 'name': '27', 'functionType': 'Ethernet', 'portId': 'Mezz 4:1-f', 'requestedMbps': '2500', 'networkUri': 'NS:NS33', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG14', 'mac': '36:85:EA:C0:10:3E', 'wwpn': '', 'wwnn': ''},
                 {'id': 28, 'name': '28', 'functionType': 'Ethernet', 'portId': 'Mezz 4:2-f', 'requestedMbps': '2500', 'networkUri': 'NS:NS33', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG14', 'mac': '36:85:EA:C0:11:3E', 'wwpn': '', 'wwnn': ''},
                 {'id': 29, 'name': '29', 'functionType': 'Ethernet', 'portId': 'Mezz 4:1-g', 'requestedMbps': '2500', 'networkUri': 'NS:NS34', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG15', 'mac': '36:85:EA:C0:10:3F', 'wwpn': '', 'wwnn': ''},
                 {'id': 30, 'name': '30', 'functionType': 'Ethernet', 'portId': 'Mezz 4:2-g', 'requestedMbps': '2500', 'networkUri': 'NS:NS34', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG15', 'mac': '36:85:EA:C0:11:3F', 'wwpn': '', 'wwnn': ''},
                 {'id': 31, 'name': '31', 'functionType': 'Ethernet', 'portId': 'Mezz 4:1-h', 'requestedMbps': '2500', 'networkUri': 'NS:NS35', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG16', 'mac': '36:85:EA:C0:10:40', 'wwpn': '', 'wwnn': ''},
                 {'id': 32, 'name': '32', 'functionType': 'Ethernet', 'portId': 'Mezz 4:2-h', 'requestedMbps': '2500', 'networkUri': 'NS:NS35', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG16', 'mac': '36:85:EA:C0:11:40', 'wwpn': '', 'wwnn': ''},
             ]}},

    {'type': 'ServerProfileV11', 'serverHardwareUri': None,
     'serverHardwareTypeUri': 'SY 480 Gen10 1', 'enclosureGroupUri': 'EG:EG-110-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'CI-FIT-Eagle110-Enc1-Bay7', 'description': 'Eagle110 Bay7', 'affinity': 'Bay',
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'hideUnusedFlexNics':True,
     'iscsiInitiatorName':'',
     'osDeploymentSettings':None,
     'connectionSettings':{
             'connections': [
                 {'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Untagged-1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG1', 'mac': '36:85:EA:C0:10:41', 'wwpn': '', 'wwnn': ''},
                 {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Untagged-1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG1', 'mac': '36:85:EA:C0:11:41', 'wwpn': '', 'wwnn': ''},
                 {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:Tunnel1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG2', 'mac': '36:85:EA:C0:10:42', 'wwpn': '', 'wwnn': ''},
                 {'id': 4, 'name': '4', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-b', 'requestedMbps': '2500', 'networkUri': 'ETH:Tunnel1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG2', 'mac': '36:85:EA:C0:11:42', 'wwpn': '', 'wwnn': ''},
                 {'id': 5, 'name': '5', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_3', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG3', 'mac': '36:85:EA:C0:10:43', 'wwpn': '', 'wwnn': ''},
                 {'id': 6, 'name': '6', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-c', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_3', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG3', 'mac': '36:85:EA:C0:11:43', 'wwpn': '', 'wwnn': ''},
                 {'id': 7, 'name': '7', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS36', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG4', 'mac': '36:85:EA:C0:10:44', 'wwpn': '', 'wwnn': ''},
                 {'id': 8, 'name': '8', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS36', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG4', 'mac': '36:85:EA:C0:11:44', 'wwpn': '', 'wwnn': ''},
                 {'id': 9, 'name': '9', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-e', 'requestedMbps': '2500', 'networkUri': 'NS:NS37', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG5', 'mac': '36:85:EA:C0:10:45', 'wwpn': '', 'wwnn': ''},
                 {'id': 10, 'name': '10', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-e', 'requestedMbps': '2500', 'networkUri': 'NS:NS37', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG5', 'mac': '36:85:EA:C0:11:45', 'wwpn': '', 'wwnn': ''},
                 {'id': 11, 'name': '11', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-f', 'requestedMbps': '2500', 'networkUri': 'NS:NS38', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG6', 'mac': '36:85:EA:C0:10:46', 'wwpn': '', 'wwnn': ''},
                 {'id': 12, 'name': '12', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-f', 'requestedMbps': '2500', 'networkUri': 'NS:NS38', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG6', 'mac': '36:85:EA:C0:11:46', 'wwpn': '', 'wwnn': ''},
                 {'id': 13, 'name': '13', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-g', 'requestedMbps': '2500', 'networkUri': 'NS:NS39', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG7', 'mac': '36:85:EA:C0:10:47', 'wwpn': '', 'wwnn': ''},
                 {'id': 14, 'name': '14', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-g', 'requestedMbps': '2500', 'networkUri': 'NS:NS39', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG7', 'mac': '36:85:EA:C0:11:47', 'wwpn': '', 'wwnn': ''},
                 {'id': 15, 'name': '15', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-h', 'requestedMbps': '2500', 'networkUri': 'NS:NS40', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG8', 'mac': '36:85:EA:C0:10:48', 'wwpn': '', 'wwnn': ''},
                 {'id': 16, 'name': '16', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-h', 'requestedMbps': '2500', 'networkUri': 'NS:NS40', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG8', 'mac': '36:85:EA:C0:11:48', 'wwpn': '', 'wwnn': ''},
             ]}},

    {'type': 'ServerProfileV11', 'serverHardwareUri': None,
     'serverHardwareTypeUri': 'SY 480 Gen10 1', 'enclosureGroupUri': 'EG:EG-110-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'CI-FIT-Eagle110-Enc1-Bay8', 'description': 'Eagle110 Bay8', 'affinity': 'Bay',
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'hideUnusedFlexNics':True,
     'iscsiInitiatorName':'',
     'osDeploymentSettings':None,
     'connectionSettings':{
             'connections': [
                 {'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Untagged-1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG1', 'mac': '36:85:EA:C0:10:49', 'wwpn': '', 'wwnn': ''},
                 {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Untagged-1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG1', 'mac': '36:85:EA:C0:11:49', 'wwpn': '', 'wwnn': ''},
                 {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_3776', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG2', 'mac': '36:85:EA:C0:10:4A', 'wwpn': '', 'wwnn': ''},
                 {'id': 4, 'name': '4', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-b', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_3776', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG2', 'mac': '36:85:EA:C0:11:4A', 'wwpn': '', 'wwnn': ''},
                 {'id': 5, 'name': '5', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-c', 'requestedMbps': '2500', 'networkUri': 'NS:NS41', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG3', 'mac': '36:85:EA:C0:10:4B', 'wwpn': '', 'wwnn': ''},
                 {'id': 6, 'name': '6', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-c', 'requestedMbps': '2500', 'networkUri': 'NS:NS41', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG3', 'mac': '36:85:EA:C0:11:4B', 'wwpn': '', 'wwnn': ''},
                 {'id': 7, 'name': '7', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS42', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG4', 'mac': '36:85:EA:C0:10:4C', 'wwpn': '', 'wwnn': ''},
                 {'id': 8, 'name': '8', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS42', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG4', 'mac': '36:85:EA:C0:11:4C', 'wwpn': '', 'wwnn': ''},
                 {'id': 9, 'name': '9', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-e', 'requestedMbps': '2500', 'networkUri': 'NS:NS43', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG5', 'mac': '36:85:EA:C0:10:4D', 'wwpn': '', 'wwnn': ''},
                 {'id': 10, 'name': '10', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-e', 'requestedMbps': '2500', 'networkUri': 'NS:NS43', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG5', 'mac': '36:85:EA:C0:11:4D', 'wwpn': '', 'wwnn': ''},
                 {'id': 11, 'name': '11', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-f', 'requestedMbps': '2500', 'networkUri': 'NS:NS44', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG6', 'mac': '36:85:EA:C0:10:4E', 'wwpn': '', 'wwnn': ''},
                 {'id': 12, 'name': '12', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-f', 'requestedMbps': '2500', 'networkUri': 'NS:NS44', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG6', 'mac': '36:85:EA:C0:11:4E', 'wwpn': '', 'wwnn': ''},
                 {'id': 13, 'name': '13', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-g', 'requestedMbps': '2500', 'networkUri': 'NS:NS45', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG7', 'mac': '36:85:EA:C0:10:4F', 'wwpn': '', 'wwnn': ''},
                 {'id': 14, 'name': '14', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-g', 'requestedMbps': '2500', 'networkUri': 'NS:NS45', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG7', 'mac': '36:85:EA:C0:11:4F', 'wwpn': '', 'wwnn': ''},
                 {'id': 15, 'name': '15', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-h', 'requestedMbps': '2500', 'networkUri': 'NS:NS46', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG8', 'mac': '36:85:EA:C0:10:50', 'wwpn': '', 'wwnn': ''},
                 {'id': 16, 'name': '16', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-h', 'requestedMbps': '2500', 'networkUri': 'NS:NS46', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG8', 'mac': '36:85:EA:C0:11:50', 'wwpn': '', 'wwnn': ''},
             ]}},

    {'type': 'ServerProfileV11', 'serverHardwareUri': None,
     'serverHardwareTypeUri': 'SY 480 Gen10 1', 'enclosureGroupUri': 'EG:EG-110-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'CI-FIT-Eagle110-Enc1-Bay9', 'description': 'Eagle110 Bay9', 'affinity': 'Bay',
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'hideUnusedFlexNics':True,
     'iscsiInitiatorName':'',
     'osDeploymentSettings':None,
     'connectionSettings':{
             'connections': [
                 {'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Untagged-1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG1', 'mac': '36:85:EA:C0:10:51', 'wwpn': '', 'wwnn': ''},
                 {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Untagged-1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG1', 'mac': '36:85:EA:C0:11:51', 'wwpn': '', 'wwnn': ''},
                 {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-b', 'requestedMbps': '2500', 'networkUri': 'NS:NS47', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG2', 'mac': '36:85:EA:C0:10:52', 'wwpn': '', 'wwnn': ''},
                 {'id': 4, 'name': '4', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-b', 'requestedMbps': '2500', 'networkUri': 'NS:NS47', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG2', 'mac': '36:85:EA:C0:11:52', 'wwpn': '', 'wwnn': ''},
                 {'id': 5, 'name': '5', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_3', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG3', 'mac': '36:85:EA:C0:10:53', 'wwpn': '', 'wwnn': ''},
                 {'id': 6, 'name': '6', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-c', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_3', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG3', 'mac': '36:85:EA:C0:11:53', 'wwpn': '', 'wwnn': ''},
                 {'id': 7, 'name': '7', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS48', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG4', 'mac': '36:85:EA:C0:10:54', 'wwpn': '', 'wwnn': ''},
                 {'id': 8, 'name': '8', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS48', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG4', 'mac': '36:85:EA:C0:11:54', 'wwpn': '', 'wwnn': ''},
                 {'id': 9, 'name': '9', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-e', 'requestedMbps': '2500', 'networkUri': 'NS:NS49', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG5', 'mac': '36:85:EA:C0:10:55', 'wwpn': '', 'wwnn': ''},
                 {'id': 10, 'name': '10', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-e', 'requestedMbps': '2500', 'networkUri': 'NS:NS49', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG5', 'mac': '36:85:EA:C0:11:55', 'wwpn': '', 'wwnn': ''},
                 {'id': 11, 'name': '11', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-f', 'requestedMbps': '2500', 'networkUri': 'NS:NS50', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG6', 'mac': '36:85:EA:C0:10:56', 'wwpn': '', 'wwnn': ''},
                 {'id': 12, 'name': '12', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-f', 'requestedMbps': '2500', 'networkUri': 'NS:NS50', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG6', 'mac': '36:85:EA:C0:11:56', 'wwpn': '', 'wwnn': ''},
                 {'id': 13, 'name': '13', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-g', 'requestedMbps': '2500', 'networkUri': 'NS:NS51', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG7', 'mac': '36:85:EA:C0:10:57', 'wwpn': '', 'wwnn': ''},
                 {'id': 14, 'name': '14', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-g', 'requestedMbps': '2500', 'networkUri': 'NS:NS51', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG7', 'mac': '36:85:EA:C0:11:57', 'wwpn': '', 'wwnn': ''},
                 {'id': 15, 'name': '15', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-h', 'requestedMbps': '2500', 'networkUri': 'ETH:Tunnel1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG8', 'mac': '36:85:EA:C0:10:58', 'wwpn': '', 'wwnn': ''},
                 {'id': 16, 'name': '16', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-h', 'requestedMbps': '2500', 'networkUri': 'ETH:Tunnel1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG8', 'mac': '36:85:EA:C0:11:58', 'wwpn': '', 'wwnn': ''},
             ]}},

    {'type': 'ServerProfileV11', 'serverHardwareUri': None,
     'serverHardwareTypeUri': 'SY 480 Gen10 1', 'enclosureGroupUri': 'EG:EG-110-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'CI-FIT-Eagle110-Enc1-Bay10', 'description': 'Eagle110 Bay10', 'affinity': 'Bay',
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'hideUnusedFlexNics':True,
     'iscsiInitiatorName':'',
     'osDeploymentSettings':None,
     'connectionSettings':{
             'connections': [
                 {'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Untagged-1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG1', 'mac': '36:85:EA:C0:10:59', 'wwpn': '', 'wwnn': ''},
                 {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Untagged-1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG1', 'mac': '36:85:EA:C0:11:59', 'wwpn': '', 'wwnn': ''},
                 {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_3777', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG2', 'mac': '36:85:EA:C0:10:5A', 'wwpn': '', 'wwnn': ''},
                 {'id': 4, 'name': '4', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-b', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_3777', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG2', 'mac': '36:85:EA:C0:11:5A', 'wwpn': '', 'wwnn': ''},
                 {'id': 5, 'name': '5', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-c', 'requestedMbps': '2500', 'networkUri': 'NS:NS17', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG3', 'mac': '36:85:EA:C0:10:5B', 'wwpn': '', 'wwnn': ''},
                 {'id': 6, 'name': '6', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-c', 'requestedMbps': '2500', 'networkUri': 'NS:NS17', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG3', 'mac': '36:85:EA:C0:11:5B', 'wwpn': '', 'wwnn': ''},
                 {'id': 7, 'name': '7', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS18', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG4', 'mac': '36:85:EA:C0:10:5C', 'wwpn': '', 'wwnn': ''},
                 {'id': 8, 'name': '8', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS18', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG4', 'mac': '36:85:EA:C0:11:5C', 'wwpn': '', 'wwnn': ''},
                 {'id': 9, 'name': '9', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-e', 'requestedMbps': '2500', 'networkUri': 'ETH:Tunnel1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG5', 'mac': '36:85:EA:C0:10:5D', 'wwpn': '', 'wwnn': ''},
                 {'id': 10, 'name': '10', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-e', 'requestedMbps': '2500', 'networkUri': 'ETH:Tunnel1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG5', 'mac': '36:85:EA:C0:11:5D', 'wwpn': '', 'wwnn': ''},
                 {'id': 11, 'name': '11', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-f', 'requestedMbps': '2500', 'networkUri': 'NS:NS19', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG6', 'mac': '36:85:EA:C0:10:5E', 'wwpn': '', 'wwnn': ''},
                 {'id': 12, 'name': '12', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-f', 'requestedMbps': '2500', 'networkUri': 'NS:NS19', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG6', 'mac': '36:85:EA:C0:11:5E', 'wwpn': '', 'wwnn': ''},
                 {'id': 13, 'name': '13', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-g', 'requestedMbps': '2500', 'networkUri': 'NS:NS20', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG7', 'mac': '36:85:EA:C0:10:5F', 'wwpn': '', 'wwnn': ''},
                 {'id': 14, 'name': '14', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-g', 'requestedMbps': '2500', 'networkUri': 'NS:NS20', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG7', 'mac': '36:85:EA:C0:11:5F', 'wwpn': '', 'wwnn': ''},
                 {'id': 15, 'name': '15', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-h', 'requestedMbps': '2500', 'networkUri': 'NS:NS21', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG8', 'mac': '36:85:EA:C0:10:60', 'wwpn': '', 'wwnn': ''},
                 {'id': 16, 'name': '16', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-h', 'requestedMbps': '2500', 'networkUri': 'NS:NS21', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG8', 'mac': '36:85:EA:C0:11:60', 'wwpn': '', 'wwnn': ''},
             ]}},

    {'type': 'ServerProfileV11', 'serverHardwareUri': None,
     'serverHardwareTypeUri': 'SY 480 Gen9 1', 'enclosureGroupUri': 'EG:EG-110-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'CI-FIT-Eagle110-Enc2-Bay1', 'description': 'Eagle110 Enc2 Bay1', 'affinity': 'Bay',
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'hideUnusedFlexNics':True,
     'iscsiInitiatorName':'',
     'osDeploymentSettings':None,
     'connectionSettings':{
             'connections': [
                 {'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Untagged-1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG1', 'mac': '36:85:EA:C0:10:61', 'wwpn': '', 'wwnn': ''},
                 {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Untagged-1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG1', 'mac': '36:85:EA:C0:11:61', 'wwpn': '', 'wwnn': ''},
                 {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:Tunnel1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG2', 'mac': '36:85:EA:C0:10:62', 'wwpn': '', 'wwnn': ''},
                 {'id': 4, 'name': '4', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-b', 'requestedMbps': '2500', 'networkUri': 'ETH:Tunnel1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG2', 'mac': '36:85:EA:C0:11:62', 'wwpn': '', 'wwnn': ''},
                 {'id': 5, 'name': '5', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_3', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG3', 'mac': '36:85:EA:C0:10:63', 'wwpn': '', 'wwnn': ''},
                 {'id': 6, 'name': '6', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-c', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_3', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG3', 'mac': '36:85:EA:C0:11:63', 'wwpn': '', 'wwnn': ''},
                 {'id': 7, 'name': '7', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG4', 'mac': '36:85:EA:C0:10:64', 'wwpn': '', 'wwnn': ''},
                 {'id': 8, 'name': '8', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG4', 'mac': '36:85:EA:C0:11:64', 'wwpn': '', 'wwnn': ''},
                 {'id': 9, 'name': '9', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-e', 'requestedMbps': '2500', 'networkUri': 'NS:NS2', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG5', 'mac': '36:85:EA:C0:10:65', 'wwpn': '', 'wwnn': ''},
                 {'id': 10, 'name': '10', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-e', 'requestedMbps': '2500', 'networkUri': 'NS:NS2', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG5', 'mac': '36:85:EA:C0:11:65', 'wwpn': '', 'wwnn': ''},
                 {'id': 11, 'name': '11', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-f', 'requestedMbps': '2500', 'networkUri': 'NS:NS3', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG6', 'mac': '36:85:EA:C0:10:66', 'wwpn': '', 'wwnn': ''},
                 {'id': 12, 'name': '12', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-f', 'requestedMbps': '2500', 'networkUri': 'NS:NS3', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG6', 'mac': '36:85:EA:C0:11:66', 'wwpn': '', 'wwnn': ''},
                 {'id': 13, 'name': '13', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-g', 'requestedMbps': '2500', 'networkUri': 'NS:NS4', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG7', 'mac': '36:85:EA:C0:10:67', 'wwpn': '', 'wwnn': ''},
                 {'id': 14, 'name': '14', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-g', 'requestedMbps': '2500', 'networkUri': 'NS:NS4', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG7', 'mac': '36:85:EA:C0:11:67', 'wwpn': '', 'wwnn': ''},
                 {'id': 15, 'name': '15', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-h', 'requestedMbps': '2500', 'networkUri': 'NS:NS5', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG8', 'mac': '36:85:EA:C0:10:68', 'wwpn': '', 'wwnn': ''},
                 {'id': 16, 'name': '16', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-h', 'requestedMbps': '2500', 'networkUri': 'NS:NS5', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG8', 'mac': '36:85:EA:C0:11:68', 'wwpn': '', 'wwnn': ''},
             ]}},

    {'type': 'ServerProfileV11', 'serverHardwareUri': None,
     'serverHardwareTypeUri': 'SY 480 Gen9 1', 'enclosureGroupUri': 'EG:EG-110-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'CI-FIT-Eagle110-Enc2-Bay2', 'description': 'Eagle110 Enc2 Bay2', 'affinity': 'Bay',
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'hideUnusedFlexNics':True,
     'iscsiInitiatorName':'',
     'osDeploymentSettings':None,
     'connectionSettings':{
             'connections': [
                 {'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Untagged-1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG1', 'mac': '36:85:EA:C0:10:69', 'wwpn': '', 'wwnn': ''},
                 {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Untagged-1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG1', 'mac': '36:85:EA:C0:11:69', 'wwpn': '', 'wwnn': ''},
                 {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_3808', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG2', 'mac': '36:85:EA:C0:10:6A', 'wwpn': '', 'wwnn': ''},
                 {'id': 4, 'name': '4', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-b', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_3808', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG2', 'mac': '36:85:EA:C0:11:6A', 'wwpn': '', 'wwnn': ''},
                 {'id': 5, 'name': '5', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-c', 'requestedMbps': '2500', 'networkUri': 'NS:NS6', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG3', 'mac': '36:85:EA:C0:10:6B', 'wwpn': '', 'wwnn': ''},
                 {'id': 6, 'name': '6', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-c', 'requestedMbps': '2500', 'networkUri': 'NS:NS6', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG3', 'mac': '36:85:EA:C0:11:6B', 'wwpn': '', 'wwnn': ''},
                 {'id': 7, 'name': '7', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS7', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG4', 'mac': '36:85:EA:C0:10:6C', 'wwpn': '', 'wwnn': ''},
                 {'id': 8, 'name': '8', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS7', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG4', 'mac': '36:85:EA:C0:11:6C', 'wwpn': '', 'wwnn': ''},
                 {'id': 9, 'name': '9', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-e', 'requestedMbps': '2500', 'networkUri': 'NS:NS8', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG5', 'mac': '36:85:EA:C0:10:6D', 'wwpn': '', 'wwnn': ''},
                 {'id': 10, 'name': '10', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-e', 'requestedMbps': '2500', 'networkUri': 'NS:NS8', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG5', 'mac': '36:85:EA:C0:11:6D', 'wwpn': '', 'wwnn': ''},
                 {'id': 11, 'name': '11', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-f', 'requestedMbps': '2500', 'networkUri': 'NS:NS9', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG6', 'mac': '36:85:EA:C0:10:6E', 'wwpn': '', 'wwnn': ''},
                 {'id': 12, 'name': '12', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-f', 'requestedMbps': '2500', 'networkUri': 'NS:NS9', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG6', 'mac': '36:85:EA:C0:11:6E', 'wwpn': '', 'wwnn': ''},
                 {'id': 13, 'name': '13', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-g', 'requestedMbps': '2500', 'networkUri': 'NS:NS10', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG7', 'mac': '36:85:EA:C0:10:6F', 'wwpn': '', 'wwnn': ''},
                 {'id': 14, 'name': '14', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-g', 'requestedMbps': '2500', 'networkUri': 'NS:NS10', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG7', 'mac': '36:85:EA:C0:11:6F', 'wwpn': '', 'wwnn': ''},
                 {'id': 15, 'name': '15', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-h', 'requestedMbps': '2500', 'networkUri': 'NS:NS11', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG8', 'mac': '36:85:EA:C0:10:70', 'wwpn': '', 'wwnn': ''},
                 {'id': 16, 'name': '16', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-h', 'requestedMbps': '2500', 'networkUri': 'NS:NS11', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG8', 'mac': '36:85:EA:C0:11:70', 'wwpn': '', 'wwnn': ''},
             ]}},


    {'type': 'ServerProfileV11', 'serverHardwareUri': None,
     'serverHardwareTypeUri': 'SY 480 Gen10 1', 'enclosureGroupUri': 'EG:EG-110-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'CI-FIT-Eagle110-Enc2-Bay3', 'description': 'Eagle110 Enc2 Bay3', 'affinity': 'Bay',
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'hideUnusedFlexNics':True,
     'iscsiInitiatorName':'',
     'osDeploymentSettings':None,
     'connectionSettings':{
             'connections': [
                 {'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Untagged-1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG1', 'mac': '36:85:EA:C0:10:71', 'wwpn': '', 'wwnn': ''},
                 {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Untagged-1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG1', 'mac': '36:85:EA:C0:11:71', 'wwpn': '', 'wwnn': ''},
                 {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_3809', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG2', 'mac': '36:85:EA:C0:10:72', 'wwpn': '', 'wwnn': ''},
                 {'id': 4, 'name': '4', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-b', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_3809', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG2', 'mac': '36:85:EA:C0:11:72', 'wwpn': '', 'wwnn': ''},
                 {'id': 5, 'name': '5', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-c', 'requestedMbps': '2500', 'networkUri': 'NS:NS12', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG3', 'mac': '36:85:EA:C0:10:73', 'wwpn': '', 'wwnn': ''},
                 {'id': 6, 'name': '6', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-c', 'requestedMbps': '2500', 'networkUri': 'NS:NS12', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG3', 'mac': '36:85:EA:C0:11:73', 'wwpn': '', 'wwnn': ''},
                 {'id': 7, 'name': '7', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS13', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG4', 'mac': '36:85:EA:C0:10:74', 'wwpn': '', 'wwnn': ''},
                 {'id': 8, 'name': '8', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS13', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG4', 'mac': '36:85:EA:C0:11:74', 'wwpn': '', 'wwnn': ''},
                 {'id': 9, 'name': '9', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-e', 'requestedMbps': '2500', 'networkUri': 'NS:NS14', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG5', 'mac': '36:85:EA:C0:10:75', 'wwpn': '', 'wwnn': ''},
                 {'id': 10, 'name': '10', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-e', 'requestedMbps': '2500', 'networkUri': 'NS:NS14', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG5', 'mac': '36:85:EA:C0:11:75', 'wwpn': '', 'wwnn': ''},
                 {'id': 11, 'name': '11', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-f', 'requestedMbps': '2500', 'networkUri': 'NS:NS15', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG6', 'mac': '36:85:EA:C0:10:76', 'wwpn': '', 'wwnn': ''},
                 {'id': 12, 'name': '12', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-f', 'requestedMbps': '2500', 'networkUri': 'NS:NS15', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG6', 'mac': '36:85:EA:C0:11:76', 'wwpn': '', 'wwnn': ''},
                 {'id': 13, 'name': '13', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-g', 'requestedMbps': '2500', 'networkUri': 'NS:NS16', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG7', 'mac': '36:85:EA:C0:10:77', 'wwpn': '', 'wwnn': ''},
                 {'id': 14, 'name': '14', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-g', 'requestedMbps': '2500', 'networkUri': 'NS:NS16', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG7', 'mac': '36:85:EA:C0:11:77', 'wwpn': '', 'wwnn': ''},
                 {'id': 15, 'name': '15', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-h', 'requestedMbps': '2500', 'networkUri': 'ETH:Tunnel1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG8', 'mac': '36:85:EA:C0:10:78', 'wwpn': '', 'wwnn': ''},
                 {'id': 16, 'name': '16', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-h', 'requestedMbps': '2500', 'networkUri': 'ETH:Tunnel1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG8', 'mac': '36:85:EA:C0:11:78', 'wwpn': '', 'wwnn': ''},
             ]}},

    {'type': 'ServerProfileV11', 'serverHardwareUri': None,
     'serverHardwareTypeUri': 'SY 480 Gen10 1', 'enclosureGroupUri': 'EG:EG-110-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'CI-FIT-Eagle110-Enc2-Bay4', 'description': 'Eagle110 Enc2 Bay4', 'affinity': 'Bay',
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'hideUnusedFlexNics':True,
     'iscsiInitiatorName':'',
     'osDeploymentSettings':None,
     'connectionSettings':{
             'connections': [
                 {'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Untagged-1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG1', 'mac': '36:85:EA:C0:10:79', 'wwpn': '', 'wwnn': ''},
                 {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Untagged-1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG1', 'mac': '36:85:EA:C0:11:79', 'wwpn': '', 'wwnn': ''},
                 {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-b', 'requestedMbps': '2500', 'networkUri': 'NS:NS17', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG2', 'mac': '36:85:EA:C0:10:7A', 'wwpn': '', 'wwnn': ''},
                 {'id': 4, 'name': '4', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-b', 'requestedMbps': '2500', 'networkUri': 'NS:NS17', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG2', 'mac': '36:85:EA:C0:11:7A', 'wwpn': '', 'wwnn': ''},
                 {'id': 5, 'name': '5', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_3', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG3', 'mac': '36:85:EA:C0:10:7B', 'wwpn': '', 'wwnn': ''},
                 {'id': 6, 'name': '6', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-c', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_3', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG3', 'mac': '36:85:EA:C0:11:7B', 'wwpn': '', 'wwnn': ''},
                 {'id': 7, 'name': '7', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS18', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG4', 'mac': '36:85:EA:C0:10:7C', 'wwpn': '', 'wwnn': ''},
                 {'id': 8, 'name': '8', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS18', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG4', 'mac': '36:85:EA:C0:11:7C', 'wwpn': '', 'wwnn': ''},
                 {'id': 9, 'name': '9', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-e', 'requestedMbps': '2500', 'networkUri': 'ETH:Tunnel1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG5', 'mac': '36:85:EA:C0:10:7D', 'wwpn': '', 'wwnn': ''},
                 {'id': 10, 'name': '10', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-e', 'requestedMbps': '2500', 'networkUri': 'ETH:Tunnel1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG5', 'mac': '36:85:EA:C0:11:7D', 'wwpn': '', 'wwnn': ''},
                 {'id': 11, 'name': '11', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-f', 'requestedMbps': '2500', 'networkUri': 'NS:NS19', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG6', 'mac': '36:85:EA:C0:10:7E', 'wwpn': '', 'wwnn': ''},
                 {'id': 12, 'name': '12', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-f', 'requestedMbps': '2500', 'networkUri': 'NS:NS19', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG6', 'mac': '36:85:EA:C0:11:7E', 'wwpn': '', 'wwnn': ''},
                 {'id': 13, 'name': '13', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-g', 'requestedMbps': '2500', 'networkUri': 'NS:NS20', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG7', 'mac': '36:85:EA:C0:10:7F', 'wwpn': '', 'wwnn': ''},
                 {'id': 14, 'name': '14', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-g', 'requestedMbps': '2500', 'networkUri': 'NS:NS20', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG7', 'mac': '36:85:EA:C0:11:7F', 'wwpn': '', 'wwnn': ''},
                 {'id': 15, 'name': '15', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-h', 'requestedMbps': '2500', 'networkUri': 'NS:NS21', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG8', 'mac': '36:85:EA:C0:10:80', 'wwpn': '', 'wwnn': ''},
                 {'id': 16, 'name': '16', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-h', 'requestedMbps': '2500', 'networkUri': 'NS:NS21', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG8', 'mac': '36:85:EA:C0:11:80', 'wwpn': '', 'wwnn': ''},
             ]}},


    {'type': 'ServerProfileV11', 'serverHardwareUri': None,
     'serverHardwareTypeUri': 'SY 480 Gen10 1', 'enclosureGroupUri': 'EG:EG-110-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'CI-FIT-Eagle110-Enc2-Bay5', 'description': 'Eagle110 Enc2 Bay5', 'affinity': 'Bay',
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'hideUnusedFlexNics':True,
     'iscsiInitiatorName':'',
     'osDeploymentSettings':None,
     'connectionSettings':{
             'connections': [
                 {'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Untagged-1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG1', 'mac': '36:85:EA:C0:10:81', 'wwpn': '', 'wwnn': ''},
                 {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Untagged-1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG1', 'mac': '36:85:EA:C0:11:81', 'wwpn': '', 'wwnn': ''},
                 {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_3776', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG2', 'mac': '36:85:EA:C0:10:82', 'wwpn': '', 'wwnn': ''},
                 {'id': 4, 'name': '4', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-b', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_3776', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG2', 'mac': '36:85:EA:C0:11:82', 'wwpn': '', 'wwnn': ''},
                 {'id': 5, 'name': '5', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-c', 'requestedMbps': '2500', 'networkUri': 'NS:NS22', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG3', 'mac': '36:85:EA:C0:10:83', 'wwpn': '', 'wwnn': ''},
                 {'id': 6, 'name': '6', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-c', 'requestedMbps': '2500', 'networkUri': 'NS:NS22', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG3', 'mac': '36:85:EA:C0:11:83', 'wwpn': '', 'wwnn': ''},
                 {'id': 7, 'name': '7', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS23', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG4', 'mac': '36:85:EA:C0:10:84', 'wwpn': '', 'wwnn': ''},
                 {'id': 8, 'name': '8', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS23', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG4', 'mac': '36:85:EA:C0:11:84', 'wwpn': '', 'wwnn': ''},
                 {'id': 9, 'name': '9', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-e', 'requestedMbps': '2500', 'networkUri': 'NS:NS24', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG5', 'mac': '36:85:EA:C0:10:85', 'wwpn': '', 'wwnn': ''},
                 {'id': 10, 'name': '10', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-e', 'requestedMbps': '2500', 'networkUri': 'NS:NS24', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG5', 'mac': '36:85:EA:C0:11:85', 'wwpn': '', 'wwnn': ''},
                 {'id': 11, 'name': '11', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-f', 'requestedMbps': '2500', 'networkUri': 'NS:NS25', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG6', 'mac': '36:85:EA:C0:10:86', 'wwpn': '', 'wwnn': ''},
                 {'id': 12, 'name': '12', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-f', 'requestedMbps': '2500', 'networkUri': 'NS:NS25', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG6', 'mac': '36:85:EA:C0:11:86', 'wwpn': '', 'wwnn': ''},
                 {'id': 13, 'name': '13', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-g', 'requestedMbps': '2500', 'networkUri': 'NS:NS26', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG7', 'mac': '36:85:EA:C0:10:87', 'wwpn': '', 'wwnn': ''},
                 {'id': 14, 'name': '14', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-g', 'requestedMbps': '2500', 'networkUri': 'NS:NS26', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG7', 'mac': '36:85:EA:C0:11:87', 'wwpn': '', 'wwnn': ''},
                 {'id': 15, 'name': '15', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-h', 'requestedMbps': '2500', 'networkUri': 'NS:NS27', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG8', 'mac': '36:85:EA:C0:10:88', 'wwpn': '', 'wwnn': ''},
                 {'id': 16, 'name': '16', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-h', 'requestedMbps': '2500', 'networkUri': 'NS:NS27', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG8', 'mac': '36:85:EA:C0:11:88', 'wwpn': '', 'wwnn': ''},
             ]}},

    {'type': 'ServerProfileV11', 'serverHardwareUri': None,
     'serverHardwareTypeUri': 'SY 480 Gen10 1', 'enclosureGroupUri': 'EG:EG-110-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'CI-FIT-Eagle110-Enc2-Bay6', 'description': 'Eagle110 Enc2 Bay6', 'affinity': 'Bay',
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'hideUnusedFlexNics':True,
     'iscsiInitiatorName':'',
     'osDeploymentSettings':None,
     'connectionSettings':{
             'connections': [
                 {'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Untagged-1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG1', 'mac': '36:85:EA:C0:10:89', 'wwpn': '', 'wwnn': ''},
                 {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Untagged-1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG1', 'mac': '36:85:EA:C0:11:89', 'wwpn': '', 'wwnn': ''},
                 {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_3777', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG2', 'mac': '36:85:EA:C0:10:8A', 'wwpn': '', 'wwnn': ''},
                 {'id': 4, 'name': '4', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-b', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_3777', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG2', 'mac': '36:85:EA:C0:11:8A', 'wwpn': '', 'wwnn': ''},
                 {'id': 5, 'name': '5', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-c', 'requestedMbps': '2500', 'networkUri': 'NS:NS28', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG3', 'mac': '36:85:EA:C0:10:8B', 'wwpn': '', 'wwnn': ''},
                 {'id': 6, 'name': '6', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-c', 'requestedMbps': '2500', 'networkUri': 'NS:NS28', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG3', 'mac': '36:85:EA:C0:11:8B', 'wwpn': '', 'wwnn': ''},
                 {'id': 7, 'name': '7', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS29', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG4', 'mac': '36:85:EA:C0:10:8C', 'wwpn': '', 'wwnn': ''},
                 {'id': 8, 'name': '8', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS29', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG4', 'mac': '36:85:EA:C0:11:8C', 'wwpn': '', 'wwnn': ''},
                 {'id': 9, 'name': '9', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-e', 'requestedMbps': '2500', 'networkUri': 'NS:NS30', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG5', 'mac': '36:85:EA:C0:10:8D', 'wwpn': '', 'wwnn': ''},
                 {'id': 10, 'name': '10', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-e', 'requestedMbps': '2500', 'networkUri': 'NS:NS30', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG5', 'mac': '36:85:EA:C0:11:8D', 'wwpn': '', 'wwnn': ''},
                 {'id': 11, 'name': '11', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-f', 'requestedMbps': '2500', 'networkUri': 'NS:NS31', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG6', 'mac': '36:85:EA:C0:10:8E', 'wwpn': '', 'wwnn': ''},
                 {'id': 12, 'name': '12', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-f', 'requestedMbps': '2500', 'networkUri': 'NS:NS31', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG6', 'mac': '36:85:EA:C0:11:8E', 'wwpn': '', 'wwnn': ''},
                 {'id': 13, 'name': '13', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-g', 'requestedMbps': '2500', 'networkUri': 'NS:NS32', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG7', 'mac': '36:85:EA:C0:10:8F', 'wwpn': '', 'wwnn': ''},
                 {'id': 14, 'name': '14', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-g', 'requestedMbps': '2500', 'networkUri': 'NS:NS32', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG7', 'mac': '36:85:EA:C0:11:8F', 'wwpn': '', 'wwnn': ''},
                 {'id': 15, 'name': '15', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-h', 'requestedMbps': '2500', 'networkUri': 'NS:NS33', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG8', 'mac': '36:85:EA:C0:10:90', 'wwpn': '', 'wwnn': ''},
                 {'id': 16, 'name': '16', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-h', 'requestedMbps': '2500', 'networkUri': 'NS:NS33', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG8', 'mac': '36:85:EA:C0:11:90', 'wwpn': '', 'wwnn': ''},
             ]}},

    {'type': 'ServerProfileV11', 'serverHardwareUri': None,
     'serverHardwareTypeUri': 'SY 480 Gen9 1', 'enclosureGroupUri': 'EG:EG-110-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'CI-FIT-Eagle110-Enc2-Bay7', 'description': 'Eagle110 Enc2 Bay7', 'affinity': 'Bay',
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'hideUnusedFlexNics':True,
     'iscsiInitiatorName':'',
     'osDeploymentSettings':None,
     'connectionSettings':{
             'connections': [
                 {'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Untagged-1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG1', 'mac': '36:85:EA:C0:10:91', 'wwpn': '', 'wwnn': ''},
                 {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Untagged-1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG1', 'mac': '36:85:EA:C0:11:91', 'wwpn': '', 'wwnn': ''},
                 {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:Tunnel1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG2', 'mac': '36:85:EA:C0:10:92', 'wwpn': '', 'wwnn': ''},
                 {'id': 4, 'name': '4', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-b', 'requestedMbps': '2500', 'networkUri': 'ETH:Tunnel1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG2', 'mac': '36:85:EA:C0:11:92', 'wwpn': '', 'wwnn': ''},
                 {'id': 5, 'name': '5', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_3', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG3', 'mac': '36:85:EA:C0:10:93', 'wwpn': '', 'wwnn': ''},
                 {'id': 6, 'name': '6', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-c', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_3', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG3', 'mac': '36:85:EA:C0:11:93', 'wwpn': '', 'wwnn': ''},
                 {'id': 7, 'name': '7', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS36', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG4', 'mac': '36:85:EA:C0:10:94', 'wwpn': '', 'wwnn': ''},
                 {'id': 8, 'name': '8', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS36', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG4', 'mac': '36:85:EA:C0:11:94', 'wwpn': '', 'wwnn': ''},
                 {'id': 9, 'name': '9', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-e', 'requestedMbps': '2500', 'networkUri': 'NS:NS37', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG5', 'mac': '36:85:EA:C0:10:95', 'wwpn': '', 'wwnn': ''},
                 {'id': 10, 'name': '10', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-e', 'requestedMbps': '2500', 'networkUri': 'NS:NS37', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG5', 'mac': '36:85:EA:C0:11:95', 'wwpn': '', 'wwnn': ''},
                 {'id': 11, 'name': '11', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-f', 'requestedMbps': '2500', 'networkUri': 'NS:NS38', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG6', 'mac': '36:85:EA:C0:10:96', 'wwpn': '', 'wwnn': ''},
                 {'id': 12, 'name': '12', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-f', 'requestedMbps': '2500', 'networkUri': 'NS:NS38', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG6', 'mac': '36:85:EA:C0:11:96', 'wwpn': '', 'wwnn': ''},
                 {'id': 13, 'name': '13', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-g', 'requestedMbps': '2500', 'networkUri': 'NS:NS39', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG7', 'mac': '36:85:EA:C0:10:97', 'wwpn': '', 'wwnn': ''},
                 {'id': 14, 'name': '14', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-g', 'requestedMbps': '2500', 'networkUri': 'NS:NS39', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG7', 'mac': '36:85:EA:C0:11:97', 'wwpn': '', 'wwnn': ''},
                 {'id': 15, 'name': '15', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-h', 'requestedMbps': '2500', 'networkUri': 'NS:NS40', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG8', 'mac': '36:85:EA:C0:10:98', 'wwpn': '', 'wwnn': ''},
                 {'id': 16, 'name': '16', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-h', 'requestedMbps': '2500', 'networkUri': 'NS:NS40', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG8', 'mac': '36:85:EA:C0:11:98', 'wwpn': '', 'wwnn': ''},
             ]}},

    {'type': 'ServerProfileV11', 'serverHardwareUri': None,
     'serverHardwareTypeUri': 'SY 480 Gen9 1', 'enclosureGroupUri': 'EG:EG-110-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'CI-FIT-Eagle110-Enc2-Bay8', 'description': 'Eagle110 Enc2 Bay8', 'affinity': 'Bay',
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
     #         'bios':{'manageBios':False,'overriddenSettings':[]},
     'hideUnusedFlexNics': True,
     'iscsiInitiatorName': '',
     'osDeploymentSettings': None,
     'connectionSettings': {
             'connections': [
                 {'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Untagged-1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG1', 'mac': '36:85:EA:C0:10:99', 'wwpn': '', 'wwnn': ''},
                 {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Untagged-1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG1', 'mac': '36:85:EA:C0:11:99', 'wwpn': '', 'wwnn': ''},
                 {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_3809', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG2', 'mac': '36:85:EA:C0:10:9A', 'wwpn': '', 'wwnn': ''},
                 {'id': 4, 'name': '4', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-b', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_3809', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG2', 'mac': '36:85:EA:C0:11:9A', 'wwpn': '', 'wwnn': ''},
                 {'id': 5, 'name': '5', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-c', 'requestedMbps': '2500', 'networkUri': 'NS:NS41', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG3', 'mac': '36:85:EA:C0:10:9B', 'wwpn': '', 'wwnn': ''},
                 {'id': 6, 'name': '6', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-c', 'requestedMbps': '2500', 'networkUri': 'NS:NS41', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG3', 'mac': '36:85:EA:C0:11:9B', 'wwpn': '', 'wwnn': ''},
                 {'id': 7, 'name': '7', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS42', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG4', 'mac': '36:85:EA:C0:10:9C', 'wwpn': '', 'wwnn': ''},
                 {'id': 8, 'name': '8', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS42', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG4', 'mac': '36:85:EA:C0:11:9C', 'wwpn': '', 'wwnn': ''},
                 {'id': 9, 'name': '9', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-e', 'requestedMbps': '2500', 'networkUri': 'NS:NS43', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG5', 'mac': '36:85:EA:C0:10:9D', 'wwpn': '', 'wwnn': ''},
                 {'id': 10, 'name': '10', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-e', 'requestedMbps': '2500', 'networkUri': 'NS:NS43', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG5', 'mac': '36:85:EA:C0:11:9D', 'wwpn': '', 'wwnn': ''},
                 {'id': 11, 'name': '11', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-f', 'requestedMbps': '2500', 'networkUri': 'NS:NS44', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG6', 'mac': '36:85:EA:C0:10:9E', 'wwpn': '', 'wwnn': ''},
                 {'id': 12, 'name': '12', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-f', 'requestedMbps': '2500', 'networkUri': 'NS:NS44', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG6', 'mac': '36:85:EA:C0:11:9E', 'wwpn': '', 'wwnn': ''},
                 {'id': 13, 'name': '13', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-g', 'requestedMbps': '2500', 'networkUri': 'NS:NS45', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG7', 'mac': '36:85:EA:C0:10:9F', 'wwpn': '', 'wwnn': ''},
                 {'id': 14, 'name': '14', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-g', 'requestedMbps': '2500', 'networkUri': 'NS:NS45', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG7', 'mac': '36:85:EA:C0:11:9F', 'wwpn': '', 'wwnn': ''},
                 {'id': 15, 'name': '15', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-h', 'requestedMbps': '2500', 'networkUri': 'NS:NS46', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG8', 'mac': '36:85:EA:C0:10:A0', 'wwpn': '', 'wwnn': ''},
                 {'id': 16, 'name': '16', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-h', 'requestedMbps': '2500', 'networkUri': 'NS:NS46', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG8', 'mac': '36:85:EA:C0:11:A0', 'wwpn': '', 'wwnn': ''},
             ]}},

    {'type': 'ServerProfileV11', 'serverHardwareUri': None,
     'serverHardwareTypeUri': 'SY 480 Gen10 1', 'enclosureGroupUri': 'EG:EG-110-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'CI-FIT-Eagle110-Enc2-Bay9', 'description': 'Eagle110 Enc2 Bay9', 'affinity': 'Bay',
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'hideUnusedFlexNics':True,
     'iscsiInitiatorName':'',
     'osDeploymentSettings':None,
     'connectionSettings':{
             'connections': [
                 {'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Untagged-1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG1', 'mac': '36:85:EA:C0:10:A1', 'wwpn': '', 'wwnn': ''},
                 {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Untagged-1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG1', 'mac': '36:85:EA:C0:11:A1', 'wwpn': '', 'wwnn': ''},
                 {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-b', 'requestedMbps': '2500', 'networkUri': 'NS:NS47', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG2', 'mac': '36:85:EA:C0:10:A2', 'wwpn': '', 'wwnn': ''},
                 {'id': 4, 'name': '4', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-b', 'requestedMbps': '2500', 'networkUri': 'NS:NS47', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG2', 'mac': '36:85:EA:C0:11:A2', 'wwpn': '', 'wwnn': ''},
                 {'id': 5, 'name': '5', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_3', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG3', 'mac': '36:85:EA:C0:10:A3', 'wwpn': '', 'wwnn': ''},
                 {'id': 6, 'name': '6', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-c', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_3', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG3', 'mac': '36:85:EA:C0:11:A3', 'wwpn': '', 'wwnn': ''},
                 {'id': 7, 'name': '7', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS48', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG4', 'mac': '36:85:EA:C0:10:A4', 'wwpn': '', 'wwnn': ''},
                 {'id': 8, 'name': '8', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS48', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG4', 'mac': '36:85:EA:C0:11:A4', 'wwpn': '', 'wwnn': ''},
                 {'id': 9, 'name': '9', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-e', 'requestedMbps': '2500', 'networkUri': 'NS:NS49', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG5', 'mac': '36:85:EA:C0:10:A5', 'wwpn': '', 'wwnn': ''},
                 {'id': 10, 'name': '10', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-e', 'requestedMbps': '2500', 'networkUri': 'NS:NS49', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG5', 'mac': '36:85:EA:C0:11:A5', 'wwpn': '', 'wwnn': ''},
                 {'id': 11, 'name': '11', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-f', 'requestedMbps': '2500', 'networkUri': 'NS:NS50', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG6', 'mac': '36:85:EA:C0:10:A6', 'wwpn': '', 'wwnn': ''},
                 {'id': 12, 'name': '12', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-f', 'requestedMbps': '2500', 'networkUri': 'NS:NS50', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG6', 'mac': '36:85:EA:C0:11:A6', 'wwpn': '', 'wwnn': ''},
                 {'id': 13, 'name': '13', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-g', 'requestedMbps': '2500', 'networkUri': 'NS:NS51', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG7', 'mac': '36:85:EA:C0:10:A7', 'wwpn': '', 'wwnn': ''},
                 {'id': 14, 'name': '14', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-g', 'requestedMbps': '2500', 'networkUri': 'NS:NS51', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG7', 'mac': '36:85:EA:C0:11:A7', 'wwpn': '', 'wwnn': ''},
                 {'id': 15, 'name': '15', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-h', 'requestedMbps': '2500', 'networkUri': 'ETH:Tunnel1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG8', 'mac': '36:85:EA:C0:10:A8', 'wwpn': '', 'wwnn': ''},
                 {'id': 16, 'name': '16', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-h', 'requestedMbps': '2500', 'networkUri': 'ETH:Tunnel1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG8', 'mac': '36:85:EA:C0:11:A8', 'wwpn': '', 'wwnn': ''},
             ]}},

    {'type': 'ServerProfileV11', 'serverHardwareUri': None,
     'serverHardwareTypeUri': 'SY 480 Gen10 1', 'enclosureGroupUri': 'EG:EG-110-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'CI-FIT-Eagle110-Enc2-Bay10', 'description': 'Eagle110 Enc2 Bay10', 'affinity': 'Bay',
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'hideUnusedFlexNics':True,
     'iscsiInitiatorName':'',
     'osDeploymentSettings':None,
     'connectionSettings':{
             'connections': [
                 {'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Untagged-1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG1', 'mac': '36:85:EA:C0:10:A9', 'wwpn': '', 'wwnn': ''},
                 {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Untagged-1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG1', 'mac': '36:85:EA:C0:11:A9', 'wwpn': '', 'wwnn': ''},
                 {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_3808', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG2', 'mac': '36:85:EA:C0:10:AA', 'wwpn': '', 'wwnn': ''},
                 {'id': 4, 'name': '4', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-b', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_3808', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG2', 'mac': '36:85:EA:C0:11:AA', 'wwpn': '', 'wwnn': ''},
                 {'id': 5, 'name': '5', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-c', 'requestedMbps': '2500', 'networkUri': 'NS:NS17', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG3', 'mac': '36:85:EA:C0:10:AB', 'wwpn': '', 'wwnn': ''},
                 {'id': 6, 'name': '6', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-c', 'requestedMbps': '2500', 'networkUri': 'NS:NS17', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG3', 'mac': '36:85:EA:C0:11:AB', 'wwpn': '', 'wwnn': ''},
                 {'id': 7, 'name': '7', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS18', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG4', 'mac': '36:85:EA:C0:10:AC', 'wwpn': '', 'wwnn': ''},
                 {'id': 8, 'name': '8', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS18', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG4', 'mac': '36:85:EA:C0:11:AC', 'wwpn': '', 'wwnn': ''},
                 {'id': 9, 'name': '9', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-e', 'requestedMbps': '2500', 'networkUri': 'ETH:Tunnel1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG5', 'mac': '36:85:EA:C0:10:AD', 'wwpn': '', 'wwnn': ''},
                 {'id': 10, 'name': '10', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-e', 'requestedMbps': '2500', 'networkUri': 'ETH:Tunnel1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG5', 'mac': '36:85:EA:C0:11:AD', 'wwpn': '', 'wwnn': ''},
                 {'id': 11, 'name': '11', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-f', 'requestedMbps': '2500', 'networkUri': 'NS:NS19', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG6', 'mac': '36:85:EA:C0:10:AE', 'wwpn': '', 'wwnn': ''},
                 {'id': 12, 'name': '12', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-f', 'requestedMbps': '2500', 'networkUri': 'NS:NS19', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG6', 'mac': '36:85:EA:C0:11:AE', 'wwpn': '', 'wwnn': ''},
                 {'id': 13, 'name': '13', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-g', 'requestedMbps': '2500', 'networkUri': 'NS:NS20', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG7', 'mac': '36:85:EA:C0:10:AF', 'wwpn': '', 'wwnn': ''},
                 {'id': 14, 'name': '14', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-g', 'requestedMbps': '2500', 'networkUri': 'NS:NS20', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG7', 'mac': '36:85:EA:C0:11:AF', 'wwpn': '', 'wwnn': ''},
                 {'id': 15, 'name': '15', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-h', 'requestedMbps': '2500', 'networkUri': 'NS:NS21', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG8', 'mac': '36:85:EA:C0:10:B0', 'wwpn': '', 'wwnn': ''},
                 {'id': 16, 'name': '16', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-h', 'requestedMbps': '2500', 'networkUri': 'NS:NS21', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG8', 'mac': '36:85:EA:C0:11:B0', 'wwpn': '', 'wwnn': ''},
             ]}},

    {'type': 'ServerProfileV11', 'serverHardwareUri': None,
     'serverHardwareTypeUri': 'SY 480 Gen10 1', 'enclosureGroupUri': 'EG:EG-110-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'CI-FIT-Eagle110-Enc2-Bay11', 'description': 'Eagle110 Enc2 Bay11', 'affinity': 'Bay',
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'hideUnusedFlexNics':True,
     'iscsiInitiatorName':'',
     'osDeploymentSettings':None,
     'connectionSettings':{
             'connections': [
                 {'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Untagged-1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG1', 'mac': '36:85:EA:C0:10:B1', 'wwpn': '', 'wwnn': ''},
                 {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Untagged-1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG1', 'mac': '36:85:EA:C0:11:B1', 'wwpn': '', 'wwnn': ''},
                 {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_3776', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG2', 'mac': '36:85:EA:C0:10:B2', 'wwpn': '', 'wwnn': ''},
                 {'id': 4, 'name': '4', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-b', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_3776', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG2', 'mac': '36:85:EA:C0:11:B2', 'wwpn': '', 'wwnn': ''},
                 {'id': 5, 'name': '5', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-c', 'requestedMbps': '2500', 'networkUri': 'NS:NS6', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG3', 'mac': '36:85:EA:C0:10:B3', 'wwpn': '', 'wwnn': ''},
                 {'id': 6, 'name': '6', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-c', 'requestedMbps': '2500', 'networkUri': 'NS:NS6', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG3', 'mac': '36:85:EA:C0:11:B3', 'wwpn': '', 'wwnn': ''},
                 {'id': 7, 'name': '7', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS7', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG4', 'mac': '36:85:EA:C0:10:B4', 'wwpn': '', 'wwnn': ''},
                 {'id': 8, 'name': '8', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS7', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG4', 'mac': '36:85:EA:C0:11:B4', 'wwpn': '', 'wwnn': ''},
                 {'id': 9, 'name': '9', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-e', 'requestedMbps': '2500', 'networkUri': 'NS:NS8', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG5', 'mac': '36:85:EA:C0:10:B5', 'wwpn': '', 'wwnn': ''},
                 {'id': 10, 'name': '10', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-e', 'requestedMbps': '2500', 'networkUri': 'NS:NS8', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG5', 'mac': '36:85:EA:C0:11:B5', 'wwpn': '', 'wwnn': ''},
                 {'id': 11, 'name': '11', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-f', 'requestedMbps': '2500', 'networkUri': 'NS:NS9', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG6', 'mac': '36:85:EA:C0:10:B6', 'wwpn': '', 'wwnn': ''},
                 {'id': 12, 'name': '12', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-f', 'requestedMbps': '2500', 'networkUri': 'NS:NS9', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG6', 'mac': '36:85:EA:C0:11:B6', 'wwpn': '', 'wwnn': ''},
                 {'id': 13, 'name': '13', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-g', 'requestedMbps': '2500', 'networkUri': 'NS:NS10', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG7', 'mac': '36:85:EA:C0:10:B7', 'wwpn': '', 'wwnn': ''},
                 {'id': 14, 'name': '14', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-g', 'requestedMbps': '2500', 'networkUri': 'NS:NS10', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG7', 'mac': '36:85:EA:C0:11:B7', 'wwpn': '', 'wwnn': ''},
                 {'id': 15, 'name': '15', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-h', 'requestedMbps': '2500', 'networkUri': 'NS:NS11', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG8', 'mac': '36:85:EA:C0:10:B8', 'wwpn': '', 'wwnn': ''},
                 {'id': 16, 'name': '16', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-h', 'requestedMbps': '2500', 'networkUri': 'NS:NS11', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG8', 'mac': '36:85:EA:C0:11:B8', 'wwpn': '', 'wwnn': ''},
             ]}},

    {'type': 'ServerProfileV11', 'serverHardwareUri': None,
     'serverHardwareTypeUri': 'SY 480 Gen10 1', 'enclosureGroupUri': 'EG:EG-110-2ME', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'CI-FIT-Eagle110-Enc2-Bay12', 'description': 'Eagle110 Enc2 Bay12', 'affinity': 'Bay',
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'hideUnusedFlexNics':True,
     'iscsiInitiatorName':'',
     'osDeploymentSettings':None,
     'connectionSettings':{
             'connections': [
                 {'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Untagged-1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG1', 'mac': '36:85:EA:C0:10:B9', 'wwpn': '', 'wwnn': ''},
                 {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Untagged-1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG1', 'mac': '36:85:EA:C0:11:B9', 'wwpn': '', 'wwnn': ''},
                 {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_3777', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG2', 'mac': '36:85:EA:C0:10:BA', 'wwpn': '', 'wwnn': ''},
                 {'id': 4, 'name': '4', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-b', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_3777', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG2', 'mac': '36:85:EA:C0:11:BA', 'wwpn': '', 'wwnn': ''},
                 {'id': 5, 'name': '5', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-c', 'requestedMbps': '2500', 'networkUri': 'NS:NS12', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG3', 'mac': '36:85:EA:C0:10:BB', 'wwpn': '', 'wwnn': ''},
                 {'id': 6, 'name': '6', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-c', 'requestedMbps': '2500', 'networkUri': 'NS:NS12', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG3', 'mac': '36:85:EA:C0:11:BB', 'wwpn': '', 'wwnn': ''},
                 {'id': 7, 'name': '7', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS13', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG4', 'mac': '36:85:EA:C0:10:BC', 'wwpn': '', 'wwnn': ''},
                 {'id': 8, 'name': '8', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:NS13', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG4', 'mac': '36:85:EA:C0:11:BC', 'wwpn': '', 'wwnn': ''},
                 {'id': 9, 'name': '9', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-e', 'requestedMbps': '2500', 'networkUri': 'NS:NS14', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG5', 'mac': '36:85:EA:C0:10:BD', 'wwpn': '', 'wwnn': ''},
                 {'id': 10, 'name': '10', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-e', 'requestedMbps': '2500', 'networkUri': 'NS:NS14', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG5', 'mac': '36:85:EA:C0:11:BD', 'wwpn': '', 'wwnn': ''},
                 {'id': 11, 'name': '11', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-f', 'requestedMbps': '2500', 'networkUri': 'NS:NS15', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG6', 'mac': '36:85:EA:C0:10:BE', 'wwpn': '', 'wwnn': ''},
                 {'id': 12, 'name': '12', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-f', 'requestedMbps': '2500', 'networkUri': 'NS:NS15', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG6', 'mac': '36:85:EA:C0:11:BE', 'wwpn': '', 'wwnn': ''},
                 {'id': 13, 'name': '13', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-g', 'requestedMbps': '2500', 'networkUri': 'NS:NS16', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG7', 'mac': '36:85:EA:C0:10:BF', 'wwpn': '', 'wwnn': ''},
                 {'id': 14, 'name': '14', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-g', 'requestedMbps': '2500', 'networkUri': 'NS:NS16', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG7', 'mac': '36:85:EA:C0:11:BF', 'wwpn': '', 'wwnn': ''},
                 {'id': 15, 'name': '15', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-h', 'requestedMbps': '2500', 'networkUri': 'ETH:Tunnel1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG8', 'mac': '36:85:EA:C0:10:C0', 'wwpn': '', 'wwnn': ''},
                 {'id': 16, 'name': '16', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-h', 'requestedMbps': '2500', 'networkUri': 'ETH:Tunnel1', 'boot': {'priority': 'NotBootable'}, 'lagName': 'LAG8', 'mac': '36:85:EA:C0:11:C0', 'wwpn': '', 'wwnn': ''},
             ]}},
]


"""
Server Profile No Hardware Assigned. Boot 'order' options are 'PXE' or 'HardDisk'.
"""
# This is for Eagle110
FORCE_PROFILE_APPLY = 'all'
server_profile_to_bay_map = {
    'CI-FIT-Eagle110-Enc1-Bay1': 'Eagle110_ENC1_MXQ80600H8, bay 1',
    'CI-FIT-Eagle110-Enc1-Bay2': 'Eagle110_ENC1_MXQ80600H8, bay 2',
    'CI-FIT-Eagle110-Enc1-Bay3': 'Eagle110_ENC1_MXQ80600H8, bay 3',
    'CI-FIT-Eagle110-Enc1-Bay4': 'Eagle110_ENC1_MXQ80600H8, bay 4',
    'CI-FIT-Eagle110-Enc1-Bay5': 'Eagle110_ENC1_MXQ80600H8, bay 5',
    'CI-FIT-Eagle110-Enc1-Bay6': 'Eagle110_ENC1_MXQ80600H8, bay 6',
    'CI-FIT-Eagle110-Enc1-Bay7': 'Eagle110_ENC1_MXQ80600H8, bay 7',
    'CI-FIT-Eagle110-Enc1-Bay8': 'Eagle110_ENC1_MXQ80600H8, bay 8',
    'CI-FIT-Eagle110-Enc1-Bay9': 'Eagle110_ENC1_MXQ80600H8, bay 9',
    'CI-FIT-Eagle110-Enc1-Bay10': 'Eagle110_ENC1_MXQ80600H8, bay 10',
    # Bays 10/11 populated by FH blades.
    # '': 'MXQ80600H8, bay 11',
    # '': 'MXQ80600H8, bay 12',
    # finished on enc2-bay1
    'CI-FIT-Eagle110-Enc2-Bay1': 'Eagle110_ENC2_MXQ80600H9, bay 1',
    'CI-FIT-Eagle110-Enc2-Bay2': 'Eagle110_ENC2_MXQ80600H9, bay 2',
    'CI-FIT-Eagle110-Enc2-Bay3': 'Eagle110_ENC2_MXQ80600H9, bay 3',
    'CI-FIT-Eagle110-Enc2-Bay4': 'Eagle110_ENC2_MXQ80600H9, bay 4',
    'CI-FIT-Eagle110-Enc2-Bay5': 'Eagle110_ENC2_MXQ80600H9, bay 5',
    'CI-FIT-Eagle110-Enc2-Bay6': 'Eagle110_ENC2_MXQ80600H9, bay 6',
    'CI-FIT-Eagle110-Enc2-Bay7': 'Eagle110_ENC2_MXQ80600H9, bay 7',
    'CI-FIT-Eagle110-Enc2-Bay8': 'Eagle110_ENC2_MXQ80600H9, bay 8',
    'CI-FIT-Eagle110-Enc2-Bay9': 'Eagle110_ENC2_MXQ80600H9, bay 9',
    'CI-FIT-Eagle110-Enc2-Bay10': 'Eagle110_ENC2_MXQ80600H9, bay 10',
    'CI-FIT-Eagle110-Enc2-Bay11': 'Eagle110_ENC2_MXQ80600H9, bay 11',
    'CI-FIT-Eagle110-Enc2-Bay12': 'Eagle110_ENC2_MXQ80600H9, bay 12',
}


APIC_CREDENTIAL = {
    "userName": "admin",
    "password": "password"
}
tenants = [
    "Eagle110_1",
    "Eagle110_2",
    "Eagle110_3",
    "Eagle110_4",
    "Eagle110_5",
]

fabric_manager = {
    "name": "Eagle110-ACI",
    "fabricManagerType": "Cisco ACI",
    "userName": APIC_CREDENTIAL['userName'],
    "password": APIC_CREDENTIAL['password'],
    "fabricManagerClusterNodeInfo": [{
            "oobMgmtAddr": "15.186.7.19"
    }],
    "type": "FabricManager"
}

apic_certificate = {
    "type": "CertificateInfoV2",
    "certificateDetails": [{
            "base64Data": "",
            "aliasName": fabric_manager['name'],
            "type": "CertificateDetailV2"
    }]
}


REPOSITORY_NAME = "EAG110_TCS_Repo"
REPOSITORY_USERNAME = "test"
REPOSITORY_PASSWORD = "hpvse123"
REPOSITORY_WEBADDRESS = "http://15.186.7.138/webdav"

switch_names = ["15.186.26.2", "15.186.26.4"]
SWITCHES_CREDENTIALS = {
    '1': {
        'ip': switch_names[0],
        'username': 'admin',
        'password': 'admin'
    },
    '2': {
        'ip': switch_names[1],
        'username': 'admin',
        'password': 'admin'
    },
}
LSG_NAME = ['Arista-Eag110']
lsgs = [
    {
        'name': LSG_NAME[0],
        'type': 'logical-switch-groupV4',
        'switchMapTemplate': {
            'switchMapEntryTemplates': [
                {
                    'logicalLocation': {
                        'locationEntries': [
                            {
                                'relativeValue': 1,
                                'type': 'StackingMemberId'
                            }
                        ]
                    },
                    'permittedSwitchTypeUri': 'SWT:Arista 7160X'
                },
                {
                    'logicalLocation': {
                        'locationEntries': [
                            {
                                'relativeValue': 2,
                                'type': 'StackingMemberId'
                            }
                        ]
                    },
                    'permittedSwitchTypeUri': 'SWT:Arista 7160X'
                }
            ]
        }
    }
]

# this is as of 8/13 ToT build
lss = [
    {
        "logicalSwitch": {
            "name": "Arista-Eag110-LS",
            "state": "Active",
            "status": None,
            "type": "logical-switchV5",
            # "managementLevel": "BASIC_MANAGED",
            "managementLevel": "MONITORED",
            "logicalSwitchGroupUri": "LSG:" + LSG_NAME[0],
            "switchMap": None,
            "switchCredentialConfiguration": [
                {
                    "snmpV1Configuration": {
                        "communityString": None
                    },
                    "snmpV3Configuration": {
                        "authorizationProtocol": None,
                        "privacyProtocol": None,
                        "securityLevel": None
                    },
                    "logicalSwitchManagementHost": SWITCHES_CREDENTIALS['1']['ip'],
                    "snmpVersion": None,
                    "snmpPort": 0,
                    "logicalSwitchManagementHostIpAddress": SWITCHES_CREDENTIALS['1']['ip'],
                    #                    "memberId": 0,
                    #                    "sshUsername": SWITCHES_CREDENTIALS['1']['username'],
                    #                    "switchUri": [switch_names[0]]
                },
                {
                    "snmpV1Configuration": {
                        "communityString": None
                    },
                    "snmpV3Configuration": {
                        "authorizationProtocol": None,
                        "privacyProtocol": None,
                        "securityLevel": None
                    },
                    "logicalSwitchManagementHost": SWITCHES_CREDENTIALS['2']['ip'],
                    "snmpVersion": None,
                    "snmpPort": 0,
                    "logicalSwitchManagementHostIpAddress": SWITCHES_CREDENTIALS['2']['ip'],
                    #                    "memberId": 0,
                    #                    "sshUsername": SWITCHES_CREDENTIALS['1']['username'],
                    #                    "switchUri": [switch_names[0]]
                },

            ],
        },
        "logicalSwitchCredentials": [
            {
                "connectionProperties": [
                    {
                        "propertyName": "SshBasicAuthCredentialUser",
                        "value": SWITCHES_CREDENTIALS['1']['username'],
                        "valueFormat": "Unknown",
                        "valueType": "String"
                    },
                    {
                        "propertyName": "SshBasicAuthCredentialPassword",
                        "value": SWITCHES_CREDENTIALS['1']['password'],
                        "valueFormat": "SecuritySensitive",
                        "valueType": "String"
                    }
                ],
            },
            {
                "connectionProperties": [
                    {
                        "propertyName": "SshBasicAuthCredentialUser",
                        "value": SWITCHES_CREDENTIALS['2']['username'],
                        "valueFormat": "Unknown",
                        "valueType": "String"
                    },
                    {
                        "propertyName": "SshBasicAuthCredentialPassword",
                        "value": SWITCHES_CREDENTIALS['2']['password'],
                        "valueFormat": "SecuritySensitive",
                        "valueType": "String"
                    }
                ]
            }
        ]
    }
]

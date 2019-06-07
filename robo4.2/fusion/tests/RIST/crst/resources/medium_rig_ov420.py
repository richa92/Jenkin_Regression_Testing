from copy import deepcopy


def make_range_list(vrange):
    rlist = []
    for x in xrange(vrange['start'], (vrange['end'] + 1)):
        rlist.append(vrange['prefix'] + str(x) + vrange['suffix'])
    return rlist


def merge_two_dicts(x, y):
    z = x.copy()
    z.update(y)
    return z


def clean_server_hardware(L):
    L = deepcopy(L)
    for d in L:
        del d['deployment_network']
        del d['os']
        del d['profile']
    return L

#####################
# CPT Data\methods
#####################


def create_seed(os, net, ilou, ilop):
    return {"os_name": os['os_name'],
            "os_repo": os['os_repo'],
            "deployment_network": net,
            "ilo_user": ilou,
            "ilo_pass": ilop,
            "system_password": "Hpvse123!"
            }


cpt_host = {"host": "192.168.1.1",
            "user": "root",
            "password": "rootpwd"}

ESXi65 = {"os_name": "ESXi65x64",
          "os_repo": "http://{}/deployment/iso/vmware/VMware-ESXi-6.5.0-Update2-9298722-HPE-Gen9plus-650.U2.10.4.0.4-Mar2019.iso".format(cpt_host['host']),
          }

ESXi67 = {"os_name": "ESXi67x64",
          "os_repo": "http://{}/deployment/iso/vmware/VMware-ESXi-6.7.0-OS-Release-9256182-HPE-Gen9plus-670.U1.10.3.0.7-Oct2018.iso".format(cpt_host['host'])
          }

RHEL75 = {"os_name": "RH75x64",
          "os_repo": "http://{}/deployment/linux/rhel75/".format(cpt_host['host']),
          }

WIN2016 = {"os_name": "Win2016_DTC_x64",
           "os_repo": r"\\{}\win2016".format(cpt_host['host']),
           }

WIN2019 = {"os_name": "Win2019_DTC_x64",
           "os_repo": r"\\{}\win2019".format(cpt_host['host']),
           }

#####################
# OVA Appliance Data
#####################
ov_vm = 'HPEOneView_large'
ov_ova_data = {'import_spec': {'entityName': ov_vm,
                               'networkMapping': [{'source': 'VM Network',
                                                   'target': 'VLAN1172-PLEXXI'}]},
               'resource_pool': 'Plexxi_Medium'}

cfm_vm = 'CFM_Medium'
cfm_ova_data = {'import_spec': {'propertyMapping': {'Hostname': cfm_vm,
                                                    'Domainname': 'dom1172.lab',
                                                    'NTP1': 'ntp.hpecorp.net',
                                                    'DHCP': 'False',
                                                    'IP': '10.172.14.2',
                                                    'Netmask': '255.255.0.0',
                                                    'Gateway': '10.172.0.1',
                                                    'DNS1': '10.171.0.11',
                                                    'DNS2': ''
                                                    },
                                'entityName': cfm_vm,
                                'networkMapping': [{'source': 'VM Network',
                                                    'target': 'VLAN1172-PLEXXI'}]},
                'resource_pool': 'Plexxi_Medium'}

#####################
# OneView Data
#####################


def rlist(start, end, prefix='net_', suffix=''):
    return ["{}{}{}".format(prefix, str(x), suffix) for x in xrange(start, end + 1)]


admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

vcenter = {'server': '10.120.0.15', 'user': 'crst_auto1', 'password': 'Russell!sCo0l'}

appliance = {'type': 'ApplianceNetworkConfigurationV2',
             'applianceNetworks':
             [{'macAddress': None,
               'interfaceName': 'hpqcorpnet',
               'activeNode': '1',
               'unconfigure': False,
               'ipv4Type': 'STATIC',
               'ipv4Subnet': '255.255.0.0',
               'ipv4Gateway': '10.172.0.1',
               'ipv4NameServers': ['10.171.0.11'],
               'app1Ipv4Addr': '10.172.14.1',
               'ipv6Type': 'UNCONFIGURE',
               'hostname': 'oneviewmed.dom1172.lab',
               'confOneNode': True,
               'domainName': 'dom1172.lab',
               'aliasDisabled': True,
               }],
             }

timeandlocale = {'type': 'TimeAndLocale', 'dateTime': None, 'timezone': 'UTC', 'ntpServers': ['16.110.135.123'], 'locale': 'en_US.UTF-8'}

ranges = [{'name': 'CR-MED-MAC', 'type': 'Range', 'category': 'id-range-VMAC', 'rangeCategory': 'Custom', 'startAddress': 'A2:22:22:00:00:00', 'endAddress': 'A2:22:22:0F:FF:FF', 'enabled': True},
          {'name': 'CR-MED-WWN', 'type': 'Range', 'category': 'id-range-VWWN', 'rangeCategory': 'Custom', 'startAddress': '22:22:2C:22:00:00:00:00', 'endAddress': '22:22:2C:22:00:0F:FF:FF', 'enabled': True},
          {'name': 'CR-MED-SN', 'type': 'Range', 'category': 'id-range-VSN', 'rangeCategory': 'Custom', 'startAddress': 'VCUCCC0000', 'endAddress': 'VCUCCC0ZZZ', 'enabled': True}]

# scopes = [{'type': 'ScopeV3', 'name': 'MySampleScope2', 'description': 'Sample Scope Description2', 'addedResourceUris': ['server-profiles:Profile9'], 'initialScopeUris': ['MySampleScope']}]

users = [{'userName': 'Serveradmin2', 'password': 'Serveradmin2', 'fullName': 'Server Admin2', 'permissions': [{'roleName': 'Server administrator', 'scopeUri': 'MySampleScope2'}, {'roleName': 'Server administrator', 'scopeUri': 'ProfileManager'}], 'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions'}]

remote_backup = {
    "remoteServerName": "15.186.16.25",
    "remoteServerDir": "backups",
    "remoteServerPublicKey": "ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAsj3Wt+L+/uM4p0UzPmgL5JM43iCy6HVlAhDi7uShqS6I0R/4hFEk2Cnd43M6swDqM0pxNddknqe19eX5AV8uX/G0aEcHF08DQ5rw0YJDYh8wvs762mXxQpocgeo3F9wsRnEbIg7qW7ykqyjxxswZWQnEv0QrL6dHPFx1mzc/4EVTkvXl5iqTqog/U76hsewUs2WQLI5mtvB4DjSC3emVuqREJSUML2Z2ghM23WW74dXwD0iOG85GWG2ETS4ot5q0spZd2S0C/JOgHyKFkqYH84VQRlX0vF9b2PsT3jMirNKVzF5ruF2p9WAYFBPmBE8vnOe+7WGm70dYcmJsIG17yw==",
    "userName": "root",
    "password": "rootpwd",
    "enabled": True,
    "protocol": "SCP",
    "scheduleInterval": "DAILY",
    "scheduleDays": [],
    "scheduleTime": "12:30",
}

licenses = [
    {'key': 'AA9C CQAA H9PY CHXY V7B5 HWWB Y9JL KMPL 3V2E PEZU DXAU 2CSM GHTG L762 AQ72 XCB9 KJVT D5KM EFVW DT5J 2JUL 6ZS8 SPS9 YG66 Z99R MWSN 6Z84 46XT WZJL HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTFG LS8T XU4E "EVAL-HPOV-NFR1 HPOV-NFR1 HP_OneView_16_Seat_NFR 7T36AEJG7JJ9"_3MNZV-XHZRH-YHJY3-X5PZ2-3KDX6'},
    {'key': '9DKC D9AA H9PY GHXY V7B5 HWWB Y9JL KMPL 9NSD 8CVE WREW JHWE JHS7 TV3P CMRG HPMR EFFW AFG9 4U8C E2TK HKDU LWWP 2R3F QPZE 7RQ4 U3US T42G 4BQM 94K2 HFTE GF7C DMJ3 BKT8 WVDC T84V R42A U887 FC2H 5KG2 F6QD NWZA JDEB TCJB 4JJY 589U BBRB "24R2-02192-002 T2222A HP_OneView_Explicit_Feature J4E8IAMANEON"_32Q6W-PQWTB-H7XYL-39968-RR53R'},
    {'key': 'ADCA A9AA H9P9 8HV3 U7B5 HWW5 Y9JL KMPL 9NSD 8CVE WREW JHWE 98QH 35TL CMRG HPMR EFFW AFG9 4U8C E2TK HKDU LWWP 2R3F QPZE 7RQ4 U3US T42G 4BQM 94K2 HFTE GF7C DMJ3 BKT8 WVDC T84V R42A U887 FC2H 5KG2 F6QD NWZA JDEB TCJB 4JJY 589U BBRB"24R2-02192-002 T2222A HP_OneView_w/o_iLO_Explicit_Feature J4E8IAMANEON"'}
]

reserved_vlan = {
    'type': 'vlan-pool',
    'start': 4035,
    'length': 60
}

ethernet_networks = [
    {'name': 'net1',
     'description': 'General networking',
     'type': 'ethernet-networkV4',
     'vlanId': 1,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged'
     },
    {'name': 'crst-mgmt',
     'description': 'Management and deployment network',
     'type': 'ethernet-networkV4',
     'vlanId': 2,
     'purpose': 'Management',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged'
     },
    {'name': 'crst-vmotion',
     'description': 'VMWare vmotion network',
     'type': 'ethernet-networkV4',
     'vlanId': 33,
     'purpose': 'VMMigration',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged'
     },
    {'name': 'crst-vsan',
     'description': 'VMWare vsan network',
     'type': 'ethernet-networkV4',
     'vlanId': 34,
     'purpose': 'FaultTolerance',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged'
     }
]

ethernet_ranges = [
    {'prefix': 'net', 'suffix': '', 'start': 3, 'end': 32, 'name': None, 'type': 'ethernet-networkV4',
        'vlanId': None, 'purpose': 'General', 'description': 'General networking', 'smartLink': True, 'privateNetwork': False, 'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged'},
]

"""
These create ethernet networks in bulk.
"""
bulk_ethernet_network = {
    "vlanIdRange": "35-4000", "description": "General networking", "purpose": "General", "namePrefix": "net", "smartLink": True, "privateNetwork": False, "bandwidth": {"maximumBandwidth": 10000, "typicalBandwidth": 2500}, "type": "bulk-ethernet-networkV1"}

network_sets_4k = [
    {'networkSetType': 'Large', 'name': 'esx-trunk-1k', 'type': 'network-setV4', 'networkUris': ['crst-mgmt', 'crst-vmotion', 'crst-vsan'] + rlist(2001, 3000, 'net_', ''), 'nativeNetworkUri': 'crst-mgmt'},
    {'networkSetType': 'Regular', 'name': 'win-trunk', 'type': 'network-setV4', 'networkUris': ['net1', 'crst-mgmt'] + rlist(3, 32, 'net', ''), 'nativeNetworkUri': 'crst-mgmt'},
    {'networkSetType': 'Large', 'name': 'linux-trunk-1k', 'type': 'network-setV4', 'networkUris': ['crst-mgmt'] + rlist(2501, 3499, 'net_', ''), 'nativeNetworkUri': 'crst-mgmt'},
    {'networkSetType': 'Large', 'name': 'linux-trunk-1k-a', 'type': 'network-setV4', 'networkUris': ['crst-mgmt'] + rlist(2501, 3499, 'net_', ''), 'nativeNetworkUri': 'crst-mgmt'},
    {'networkSetType': 'Large', 'name': 'linux-trunk-1k-b', 'type': 'network-setV4', 'networkUris': ['crst-mgmt'] + rlist(2501, 3499, 'net_', ''), 'nativeNetworkUri': 'crst-mgmt'},
    {'networkSetType': 'Large', 'name': 'linux-trunk-4k', 'type': 'network-setV4', 'networkUris': ['net1', 'crst-mgmt', 'crst-vmotion', 'crst-vsan'] + rlist(3, 32, 'net', '') + rlist(35, 4000, 'net_', ''), 'nativeNetworkUri': 'crst-mgmt'},
]
# temporary until 4k vlan max becomes available in OneView
network_sets_162 = [
    {'name': 'esx-trunk-1k', 'type': 'network-setV4', 'networkUris': ['crst-mgmt', 'crst-vmotion', 'crst-vsan'] + rlist(2001, 2159, 'net_', ''), 'nativeNetworkUri': 'crst-mgmt'},
    {'name': 'win-trunk', 'type': 'network-setV4', 'networkUris': ['net1'] + ['crst-mgmt'] + rlist(3, 32, 'net', ''), 'nativeNetworkUri': 'crst-mgmt'},
    {'name': 'linux-trunk-1k', 'type': 'network-setV4', 'networkUris': ['crst-mgmt'] + rlist(2501, 2661, 'net_', ''), 'nativeNetworkUri': 'crst-mgmt'},
    {'name': 'linux-trunk-1k-a', 'type': 'network-setV4', 'networkUris': ['crst-mgmt'] + rlist(2501, 2661, 'net_', ''), 'nativeNetworkUri': 'crst-mgmt'},
    {'name': 'linux-trunk-1k-b', 'type': 'network-setV4', 'networkUris': ['crst-mgmt'] + rlist(2501, 2661, 'net_', ''), 'nativeNetworkUri': 'crst-mgmt'},
    {'name': 'linux-trunk-4k', 'type': 'network-setV4', 'networkUris': ['net1'] + ['crst-mgmt', 'crst-vmotion', 'crst-vsan'] + rlist(3, 32, 'net', '') + rlist(35, 162, 'net_', ''), 'nativeNetworkUri': 'crst-mgmt'},
]
network_sets = network_sets_4k

network_set_ranges = [
]

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

# Assign server profile to server hardware even if server status is not OK
FORCE_PROFILE_APPLY = 'all'

#####################
# DL Server Hardware section
#####################
server_hardware_medium1 = [
    # Medium1
    # rack u #1
    {
        "hostname": "10.172.12.12",
        "username": "Administrator",
        "password": "RYDNCSRD",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-trunk-1k",
        "os": ESXi67,
        "profile": "ProfileU1"
    },
    # rack u #2
    {
        "hostname": "10.172.12.9",
        "username": "Administrator",
        "password": "U59PJ685",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-trunk-1k",
        "os": ESXi67,
        "profile": "ProfileU2"
    },
    # rack u #3
    {
        "hostname": "10.172.12.7",
        "username": "Administrator",
        "password": "7J4AAE93",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-trunk-1k",
        "os": ESXi67,
        "profile": "ProfileU3"
    },
    # rack u #4
    {
        "hostname": "10.172.12.24",
        "username": "Administrator",
        "password": "7BMUAQPM",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-trunk-1k",
        "os": ESXi67,
        "profile": "ProfileU4"
    },
    # rack u #5
    {
        "hostname": "10.172.12.21",
        "username": "Administrator",
        "password": "BBXHNK26",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-trunk-1k",
        "os": ESXi67,
        "profile": "ProfileU5"
    },
    # rack u #6
    {
        "hostname": "10.172.12.20",
        "username": "Administrator",
        "password": "AENS7R5M",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-trunk-1k",
        "os": ESXi67,
        "profile": "ProfileU6"
    },
    # rack u #7
    {
        "hostname": "10.172.12.15",
        "username": "Administrator",
        "password": "MAT3X9FB",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-trunk-1k",
        "os": ESXi67,
        "profile": "ProfileU7"
    },
    # rack u #8
    {
        "hostname": "10.172.12.13",
        "username": "Administrator",
        "password": "EDPHPHZ9",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-trunk-1k",
        "os": ESXi67,
        "profile": "ProfileU8"
    },
    # rack u #9
    {
        "hostname": "10.172.12.22",
        "username": "Administrator",
        "password": "5CABHQPJ",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-trunk-1k",
        "os": ESXi67,
        "profile": "ProfileU9"
    },
    # rack u #10
    {
        "hostname": "10.172.12.17",
        "username": "Administrator",
        "password": "B86CNSGC",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-trunk-1k",
        "os": ESXi67,
        "profile": "ProfileU10"
    },
    # rack u #11
    {
        "hostname": "10.172.12.16",
        "username": "Administrator",
        "password": "7E62YHSK",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-trunk-1k",
        "os": ESXi67,
        "profile": "ProfileU11"
    },
    # rack u #12
    {
        "hostname": "10.172.12.14",
        "username": "Administrator",
        "password": "2R9D74JU",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "linux-trunk-1k-a",
        "os": RHEL75,
        "profile": "ProfileU12"
    },
    # rack u #13
    {
        "hostname": "10.172.12.8",
        "username": "Administrator",
        "password": "5TPGEG2D",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "linux-trunk-1k-a",
        "os": RHEL75,
        "profile": "ProfileU13"
    },
    # rack u #14
    {
        "hostname": "10.172.12.23",
        "username": "Administrator",
        "password": "Z63DEGYA",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "linux-trunk-1k-a",
        "os": RHEL75,
        "profile": "ProfileU14"
    },
    # rack u #15
    {
        "hostname": "10.172.12.19",
        "username": "Administrator",
        "password": "ZYNE2XXT",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "linux-trunk-1k-a",
        "os": RHEL75,
        "profile": "ProfileU15"
    },
    # rack u #16
    {
        "hostname": "10.172.12.18",
        "username": "Administrator",
        "password": "XFJ2U2K7",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "linux-trunk-1k-a",
        "os": RHEL75,
        "profile": "ProfileU16"
    },
    # rack u #17
    {
        "hostname": "10.172.12.11",
        "username": "Administrator",
        "password": "4Y727D6B",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "linux-trunk-4k",
        "os": RHEL75,
        "profile": "ProfileU17"
    },
    # rack u #18
    {
        "hostname": "10.172.12.10",
        "username": "Administrator",
        "password": "4ZYG8GFP",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "linux-trunk-4k",
        "os": RHEL75,
        "profile": "ProfileU18"
    },
    # rack u #19
    {
        "hostname": "10.172.12.4",
        "username": "Administrator",
        "password": "ZWFQ344J",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "linux-trunk-4k",
        "os": RHEL75,
        "profile": "ProfileU19"
    },
    # rack u #20
    {
        "hostname": "10.172.12.3",
        "username": "Administrator",
        "password": "BNGQSD5W",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "linux-trunk-4k",
        "os": RHEL75,
        "profile": "ProfileU20"
    },
    # rack u #22
    {
        "hostname": "10.172.12.6",
        "username": "Administrator",
        "password": "A2H5WZCK",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "linux-trunk-4k",
        "os": RHEL75,
        "profile": "ProfileU22"
    },
    # rack u #23
    {
        "hostname": "10.172.12.5",
        "username": "Administrator",
        "password": "G9T3DFRM",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "linux-trunk-4k",
        "os": RHEL75,
        "profile": "ProfileU23"
    }
]

server_hardware_medium2 = [
    # Medium2
    # rack u1-2
    {
        "hostname": "10.172.12.50",
        "username": "Administrator",
        "password": "SYQQBJ62",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-trunk-1k",
        "os": ESXi67,
        "profile": "ProfileU1-2"
    },
    # rack u3-4
    {
        "hostname": "10.172.12.49",
        "username": "Administrator",
        "password": "X8KHHPC6",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-trunk-1k",
        "os": ESXi67,
        "profile": "ProfileU3-4"
    },
    # rack u5-6
    {
        "hostname": "10.172.12.48",
        "username": "Administrator",
        "password": "LHRYW5Z5",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-trunk-1k",
        "os": ESXi67,
        "profile": "ProfileU5-6"
    },
    # rack u7-8
    {
        "hostname": "10.172.12.47",
        "username": "Administrator",
        "password": "VG2HX2Z7",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-trunk-1k",
        "os": ESXi67,
        "profile": "ProfileU7-8"
    },
    # rack u9-10
    {
        "hostname": "10.172.12.46",
        "username": "Administrator",
        "password": "HRFHWSS7",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-trunk-1k",
        "os": ESXi67,
        "profile": "ProfileU9-10"
    },
    # rack u11-12
    {
        "hostname": "10.172.12.45",
        "username": "Administrator",
        "password": "2QTFSV66",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-trunk-1k",
        "os": ESXi67,
        "profile": "ProfileU11-12"
    },
    # rack u13-14
    {
        "hostname": "10.172.12.44",
        "username": "Administrator",
        "password": "RFN5F5N5",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "linux-trunk-4k",
        "os": RHEL75,
        "profile": "ProfileU13-14"
    },
    # rack u15-16
    {
        "hostname": "10.172.12.43",
        "username": "Administrator",
        "password": "SHQQCYF7",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "linux-trunk-4k",
        "os": RHEL75,
        "profile": "ProfileU15-16"
    },
    # rack u17-18
    {
        "hostname": "10.172.12.42",
        "username": "Administrator",
        "password": "ZKKQRRP6",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "linux-trunk-4k",
        "os": RHEL75,
        "profile": "ProfileU17-18"
    },
    # rack u19-20
    {
        "hostname": "10.172.12.41",
        "username": "Administrator",
        "password": "ZGN7HTF7",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "linux-trunk-1k-a",
        "os": RHEL75,
        "profile": "ProfileU19-20"
    },
    # rack u22-23
    {
        "hostname": "10.172.12.40",
        "username": "Administrator",
        "password": "MD6KGSG7",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "linux-trunk-1k-a",
        "os": RHEL75,
        "profile": "ProfileU22-23"
    },
    # rack u24-25
    {
        "hostname": "10.172.12.39",
        "username": "Administrator",
        "password": "HCNQMTC7",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "linux-trunk-1k-a",
        "os": RHEL75,
        "profile": "ProfileU24-25"
    }
]

server_hardware_cpt = server_hardware_medium1 + server_hardware_medium2
server_hardware = clean_server_hardware(server_hardware_cpt)

#####################
# DL Server Profiles section
#####################
server_profile_to_bay_map_medium1 = {
    'ProfileU1': 'ILOMXQ824046F.dom1172.lab',
    'ProfileU2': 'ILOMXQ824046D.dom1172.lab',
    'ProfileU3': 'ILOMXQ82501T3.dom1172.lab',
    'ProfileU4': 'ILODL360GXIE1.dom1172.lab',
    'ProfileU5': 'ILOMXQ82501SV.dom1172.lab',
    'ProfileU6': 'ILOMXQ82501T0.dom1172.lab',
    'ProfileU7': 'ILOMXQ82501SG.dom1172.lab',
    'ProfileU8': 'ILOMXQ82501T5.dom1172.lab',
    'ProfileU9': 'ILOMXQ82501SS.dom1172.lab',
    'ProfileU10': 'ILOMXQ824046K.dom1172.lab',
    'ProfileU11': 'ILOMXQ8240459.dom1172.lab',
    'ProfileU12': 'ILOMXQ8240456.dom1172.lab',
    'ProfileU13': 'ILOMXQ824045R.dom1172.lab',
    'ProfileU14': 'ILOMXQ824046R.dom1172.lab',
    'ProfileU15': 'ILOMXQ824046Q.dom1172.lab',
    'ProfileU16': 'ILOMXQ824046L.dom1172.lab',
    'ProfileU17': 'ILOMXQ824045Y.dom1172.lab',
    'ProfileU18': 'ILOMXQ82501T8.dom1172.lab',
    'ProfileU19': 'ILOMXQ82501SP.dom1172.lab',
    'ProfileU20': 'ILOMXQ825028D.dom1172.lab',
    'ProfileU22': 'ILOMXQ824046N.dom1172.lab',
    'ProfileU23': 'ILOMXQ824046V.dom1172.lab'
}

server_profile_to_bay_map_medium2 = {
    'ProfileU1-2': 'ILO2M282501KH.dom1172.lab',
    'ProfileU3-4': 'ILO2M282501KJ.dom1172.lab',
    'ProfileU5-6': 'ILO2M282501KN.dom1172.lab',
    'ProfileU7-8': 'ILO2M282501KP.dom1172.lab',
    'ProfileU9-10': 'ILO2M282501X3.dom1172.lab',
    'ProfileU11-12': 'ILO2M282501WQ.dom1172.lab',
    'ProfileU13-14': 'ILO2M282501KQ.dom1172.lab',
    'ProfileU15-16': 'ILO2M282501KD.dom1172.lab',
    'ProfileU17-18': 'ILO2M282501KX.dom1172.lab',
    'ProfileU19-20': 'ILO2M282501KF.dom1172.lab',
    'ProfileU22-23': 'ILO2M282501KM.dom1172.lab',
    'ProfileU24-25': 'ILO2M282501KS.dom1172.lab'
}

server_profile_to_bay_map = merge_two_dicts(server_profile_to_bay_map_medium1, server_profile_to_bay_map_medium2)

server_profile_templates_medium1 = [
    {
        'type': 'ServerProfileTemplateV6',
        'serverProfileDescription': 'ESXi DL360 Gen10 1 Profile',
        'serverHardwareTypeUri': 'SHT:DL360 Gen10 1',
        'enclosureGroupUri': '',
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': 'esx-dl360',
        'description': '',
        'affinity': None,
        'connectionSettings': {
            'connections': [
                {
                                    'id': 1,
                                    'name': 'c1',
                                    'functionType': 'Ethernet',
                                    'portId': 'Flr 1:1',
                                    'requestedMbps': 0,
                                    'networkUri': 'NS:esx-trunk-1k',
                                    'ipv4': {}
                },
                {
                    'id': 2,
                    'name': 'c2',
                    'functionType': 'Ethernet',
                                    'portId': 'Flr 1:2',
                                    'requestedMbps': 0,
                                    'networkUri': 'NS:esx-trunk-1k',
                                    'ipv4': {}
                }
            ],
            'manageConnections': True
        },
        'boot': {'manageBoot': False},
        'bootMode': {
            'manageMode': True,
            "mode": "UEFIOptimized",
            "pxeBootPolicy": "Auto",
            "secureBoot": "Disabled"
        },
        'firmware': {
            'manageFirmware': False,
            'firmwareBaselineUri': '',
            'forceInstallFirmware': False,
            'firmwareInstallType': None,
            'firmwareActivationType': 'Immediate'
        },
        'bios': {
            'manageBios': False,
            'overriddenSettings': []
        },
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',
        'localStorage': {
            'sasLogicalJBODs': [],
            'controllers': []
        },
        'sanStorage': None,
        'osDeploymentSettings': None,
        'initialScopeUris': []
    },
    {
        'type': 'ServerProfileTemplateV6',
        'serverProfileDescription': 'Linux LAG DL360 Gen10 1 Profile',
        'serverHardwareTypeUri': 'SHT:DL360 Gen10 1',
        'enclosureGroupUri': '',
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': 'linux-lag-dl360',
        'description': '',
        'affinity': None,
        'connectionSettings': {
            'connections': [
                {
                                    'id': 1,
                                    'name': 'c1',
                                    'functionType': 'Ethernet',
                                    'portId': 'Flr 1:1',
                                    'requestedMbps': 0,
                                    'networkUri': 'NS:linux-trunk-4k',
                                    'ipv4': {},
                                    'lagName': 'LAG1'
                },
                {
                    'id': 2,
                    'name': 'c2',
                    'functionType': 'Ethernet',
                                    'portId': 'Flr 1:2',
                                    'requestedMbps': 0,
                                    'networkUri': 'NS:linux-trunk-4k',
                                    'ipv4': {},
                                    'lagName': 'LAG1'
                }
            ],
            'manageConnections': True
        },
        'boot': {'manageBoot': False},
        'bootMode': {
            'manageMode': True,
            "mode": "UEFIOptimized",
            "pxeBootPolicy": "Auto",
            "secureBoot": "Disabled"
        },
        'firmware': {
            'manageFirmware': False,
            'firmwareBaselineUri': '',
            'forceInstallFirmware': False,
            'firmwareInstallType': None,
            'firmwareActivationType': 'Immediate'
        },
        'bios': {
            'manageBios': False,
            'overriddenSettings': []
        },
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',
        'localStorage': {
            'sasLogicalJBODs': [],
            'controllers': []
        },
        'sanStorage': None,
        'osDeploymentSettings': None,
        'initialScopeUris': []
    },
    {
        'type': 'ServerProfileTemplateV6',
        'serverProfileDescription': 'Linux NoLAG DL360 Gen10 1 Profile',
        'serverHardwareTypeUri': 'SHT:DL360 Gen10 1',
        'enclosureGroupUri': '',
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': 'linux-dl360',
        'description': '',
        'affinity': None,
        'connectionSettings': {
            'connections': [
                {
                                    'id': 1,
                                    'name': 'c1',
                                    'functionType': 'Ethernet',
                                    'portId': 'Flr 1:1',
                                    'requestedMbps': 0,
                                    'networkUri': 'NS:linux-trunk-1k-a',
                                    'ipv4': {}
                },
                {
                    'id': 2,
                    'name': 'c2',
                    'functionType': 'Ethernet',
                                    'portId': 'Flr 1:2',
                                    'requestedMbps': 0,
                                    'networkUri': 'NS:linux-trunk-1k-b',
                                    'ipv4': {}
                }
            ],
            'manageConnections': True
        },
        'boot': {'manageBoot': False},
        'bootMode': {
            'manageMode': True,
            "mode": "UEFIOptimized",
            "pxeBootPolicy": "Auto",
            "secureBoot": "Disabled"
        },
        'firmware': {
            'manageFirmware': False,
            'firmwareBaselineUri': '',
            'forceInstallFirmware': False,
            'firmwareInstallType': None,
            'firmwareActivationType': 'Immediate'
        },
        'bios': {
            'manageBios': False,
            'overriddenSettings': []
        },
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',
        'localStorage': {
            'sasLogicalJBODs': [],
            'controllers': []
        },
        'sanStorage': None,
        'osDeploymentSettings': None,
        'initialScopeUris': []
    }
]

server_profile_templates_medium2 = [
    {
        'type': 'ServerProfileTemplateV6',
        'serverProfileDescription': 'ESXi DL380 Gen10 1 Profile',
        'serverHardwareTypeUri': 'SHT:DL380 Gen10 1',
        'enclosureGroupUri': '',
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': 'esx-dl380',
        'description': '',
        'affinity': None,
        'connectionSettings': {
            'connections': [
                {
                                    'id': 1,
                                    'name': 'c1',
                                    'functionType': 'Ethernet',
                                    'portId': 'Flr 1:1',
                                    'requestedMbps': 0,
                                    'networkUri': 'NS:esx-trunk-1k',
                                    'ipv4': {}
                },
                {
                    'id': 2,
                    'name': 'c2',
                    'functionType': 'Ethernet',
                                    'portId': 'Flr 1:2',
                                    'requestedMbps': 0,
                                    'networkUri': 'NS:esx-trunk-1k',
                                    'ipv4': {}
                }
            ],
            'manageConnections': True
        },
        'boot': {'manageBoot': False},
        'bootMode': {
            'manageMode': True,
            "mode": "UEFIOptimized",
            "pxeBootPolicy": "Auto",
            "secureBoot": "Disabled"
        },
        'firmware': {
            'manageFirmware': False,
            'firmwareBaselineUri': '',
            'forceInstallFirmware': False,
            'firmwareInstallType': None,
            'firmwareActivationType': 'Immediate'
        },
        'bios': {
            'manageBios': False,
            'overriddenSettings': []
        },
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',
        'localStorage': {
            'sasLogicalJBODs': [],
            'controllers': []
        },
        'sanStorage': None,
        'osDeploymentSettings': None,
        'initialScopeUris': []
    },
    {
        'type': 'ServerProfileTemplateV6',
        'serverProfileDescription': 'Linux LAG DL380 Gen10 1 Profile',
        'serverHardwareTypeUri': 'SHT:DL380 Gen10 1',
        'enclosureGroupUri': '',
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': 'linux-lag-dl380',
        'description': '',
        'affinity': None,
        'connectionSettings': {
            'connections': [
                {
                                    'id': 1,
                                    'name': 'c1',
                                    'functionType': 'Ethernet',
                                    'portId': 'Flr 1:1',
                                    'requestedMbps': 0,
                                    'networkUri': 'NS:linux-trunk-4k',
                                    'ipv4': {},
                                    'lagName': 'LAG1'
                },
                {
                    'id': 2,
                    'name': 'c2',
                    'functionType': 'Ethernet',
                                    'portId': 'Flr 1:2',
                                    'requestedMbps': 0,
                                    'networkUri': 'NS:linux-trunk-4k',
                                    'ipv4': {},
                                    'lagName': 'LAG1'
                }
            ],
            'manageConnections': True
        },
        'boot': {'manageBoot': False},
        'bootMode': {
            'manageMode': True,
            "mode": "UEFIOptimized",
            "pxeBootPolicy": "Auto",
            "secureBoot": "Disabled"
        },
        'firmware': {
            'manageFirmware': False,
            'firmwareBaselineUri': '',
            'forceInstallFirmware': False,
            'firmwareInstallType': None,
            'firmwareActivationType': 'Immediate'
        },
        'bios': {
            'manageBios': False,
            'overriddenSettings': []
        },
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',
        'localStorage': {
            'sasLogicalJBODs': [],
            'controllers': []
        },
        'sanStorage': None,
        'osDeploymentSettings': None,
        'initialScopeUris': []
    },
    {
        'type': 'ServerProfileTemplateV6',
        'serverProfileDescription': 'Linux NoLAG DL380 Gen10 1 Profile',
        'serverHardwareTypeUri': 'SHT:DL380 Gen10 1',
        'enclosureGroupUri': '',
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': 'linux-dl380',
        'description': '',
        'affinity': None,
        'connectionSettings': {
            'connections': [
                {
                                    'id': 1,
                                    'name': 'c1',
                                    'functionType': 'Ethernet',
                                    'portId': 'Flr 1:1',
                                    'requestedMbps': 0,
                                    'networkUri': 'NS:linux-trunk-1k-a',
                                    'ipv4': {}
                },
                {
                    'id': 2,
                    'name': 'c2',
                    'functionType': 'Ethernet',
                                    'portId': 'Flr 1:2',
                                    'requestedMbps': 0,
                                    'networkUri': 'NS:linux-trunk-1k-b',
                                    'ipv4': {}
                }
            ],
            'manageConnections': True
        },
        'boot': {'manageBoot': False},
        'bootMode': {
            'manageMode': True,
            "mode": "UEFIOptimized",
            "pxeBootPolicy": "Auto",
            "secureBoot": "Disabled"
        },
        'firmware': {
            'manageFirmware': False,
            'firmwareBaselineUri': '',
            'forceInstallFirmware': False,
            'firmwareInstallType': None,
            'firmwareActivationType': 'Immediate'
        },
        'bios': {
            'manageBios': False,
            'overriddenSettings': []
        },
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',
        'localStorage': {
            'sasLogicalJBODs': [],
            'controllers': []
        },
        'sanStorage': None,
        'osDeploymentSettings': None,
        'initialScopeUris': []
    },
]

server_profile_templates = server_profile_templates_medium1 + server_profile_templates_medium2

server_profiles_using_template_medium1 = [
    # Medium 1 server profiles using templates
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map_medium1['ProfileU1'],
        'serverProfileTemplateUri': 'SPT:esx-dl360',
        'name': 'ProfileU1',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map_medium1['ProfileU2'],
        'serverProfileTemplateUri': 'SPT:esx-dl360',
        'name': 'ProfileU2',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map_medium1['ProfileU3'],
        'serverProfileTemplateUri': 'SPT:esx-dl360',
        'name': 'ProfileU3',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map_medium1['ProfileU4'],
        'serverProfileTemplateUri': 'SPT:esx-dl360',
        'name': 'ProfileU4',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map_medium1['ProfileU5'],
        'serverProfileTemplateUri': 'SPT:esx-dl360',
        'name': 'ProfileU5',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map_medium1['ProfileU6'],
        'serverProfileTemplateUri': 'SPT:esx-dl360',
        'name': 'ProfileU6',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map_medium1['ProfileU7'],
        'serverProfileTemplateUri': 'SPT:esx-dl360',
        'name': 'ProfileU7',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map_medium1['ProfileU8'],
        'serverProfileTemplateUri': 'SPT:esx-dl360',
        'name': 'ProfileU8',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map_medium1['ProfileU9'],
        'serverProfileTemplateUri': 'SPT:esx-dl360',
        'name': 'ProfileU9',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map_medium1['ProfileU10'],
        'serverProfileTemplateUri': 'SPT:esx-dl360',
        'name': 'ProfileU10',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map_medium1['ProfileU11'],
        'serverProfileTemplateUri': 'SPT:esx-dl360',
        'name': 'ProfileU11',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map_medium1['ProfileU12'],
        'serverProfileTemplateUri': 'SPT:linux-dl360',
        'name': 'ProfileU12',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map_medium1['ProfileU13'],
        'serverProfileTemplateUri': 'SPT:linux-dl360',
        'name': 'ProfileU13',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map_medium1['ProfileU14'],
        'serverProfileTemplateUri': 'SPT:linux-dl360',
        'name': 'ProfileU14',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map_medium1['ProfileU15'],
        'serverProfileTemplateUri': 'SPT:linux-dl360',
        'name': 'ProfileU15',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map_medium1['ProfileU16'],
        'serverProfileTemplateUri': 'SPT:linux-dl360',
        'name': 'ProfileU16',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map_medium1['ProfileU17'],
        'serverProfileTemplateUri': 'SPT:linux-lag-dl360',
        'name': 'ProfileU17',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map_medium1['ProfileU18'],
        'serverProfileTemplateUri': 'SPT:linux-lag-dl360',
        'name': 'ProfileU18',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map_medium1['ProfileU19'],
        'serverProfileTemplateUri': 'SPT:linux-lag-dl360',
        'name': 'ProfileU19',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map_medium1['ProfileU20'],
        'serverProfileTemplateUri': 'SPT:linux-lag-dl360',
        'name': 'ProfileU20',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map_medium1['ProfileU22'],
        'serverProfileTemplateUri': 'SPT:linux-lag-dl360',
        'name': 'ProfileU22',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map_medium1['ProfileU23'],
        'serverProfileTemplateUri': 'SPT:linux-lag-dl360',
        'name': 'ProfileU23',
    }
]

server_profiles_using_template_medium2 = [
    # Medium 2 server profiles using templates
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map_medium2['ProfileU1-2'],
        'serverProfileTemplateUri': 'SPT:esx-dl380',
        'name': 'ProfileU1-2',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map_medium2['ProfileU3-4'],
        'serverProfileTemplateUri': 'SPT:esx-dl380',
        'name': 'ProfileU3-4',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map_medium2['ProfileU5-6'],
        'serverProfileTemplateUri': 'SPT:esx-dl380',
        'name': 'ProfileU5-6',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map_medium2['ProfileU7-8'],
        'serverProfileTemplateUri': 'SPT:esx-dl380',
        'name': 'ProfileU7-8',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map_medium2['ProfileU9-10'],
        'serverProfileTemplateUri': 'SPT:esx-dl380',
        'name': 'ProfileU9-10',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map_medium2['ProfileU11-12'],
        'serverProfileTemplateUri': 'SPT:esx-dl380',
        'name': 'ProfileU11-12',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map_medium2['ProfileU13-14'],
        'serverProfileTemplateUri': 'SPT:linux-lag-dl380',
        'name': 'ProfileU13-14',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map_medium2['ProfileU15-16'],
        'serverProfileTemplateUri': 'SPT:linux-lag-dl380',
        'name': 'ProfileU15-16',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map_medium2['ProfileU17-18'],
        'serverProfileTemplateUri': 'SPT:linux-lag-dl380',
        'name': 'ProfileU17-18',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map_medium2['ProfileU19-20'],
        'serverProfileTemplateUri': 'SPT:linux-dl380',
        'name': 'ProfileU19-20',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map_medium2['ProfileU22-23'],
        'serverProfileTemplateUri': 'SPT:linux-dl380',
        'name': 'ProfileU22-23',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map_medium2['ProfileU24-25'],
        'serverProfileTemplateUri': 'SPT:linux-dl380',
        'name': 'ProfileU24-25',
    }
]

server_profiles_using_template = server_profiles_using_template_medium1 + server_profiles_using_template_medium2

#####################
# Plexxi section
#####################
# Plexxi connect credentials
plexxi_connect_host = '10.172.14.2'
plexxi_connect_user = 'admin'
plexxi_connect_password = 'plexxi'
# OneView configuration request bodies
#    :List of dictionary of request bodies
oneview_config = [
    {
        "host": appliance['applianceNetworks'][0]['app1Ipv4Addr'],
        "username": admin_credentials['userName'],
        "password": admin_credentials['password'],
        "description": "",
        "enabled": True,
        "verify_ssl": True,
        "name": "HPE OneView Configuration"
    }
]
#####################
# Logical Switches and Logical Switch Groups section
#####################
PLEXXI_SWITCHES_CREDENTIALS_MEDIUM1 = {
    '1': {
        'ip': '10.172.14.3',
        'username': 'admin',
        'password': 'plexxi'
    },
    '2': {
        'ip': '10.172.14.4',
        'username': 'admin',
        'password': 'plexxi'
    }
}

PLEXXI_SWITCHES_CREDENTIALS_MEDIUM2 = {
    '3': {
        'ip': '10.172.14.5',
        'username': 'admin',
        'password': 'plexxi'
    },
    '4': {
        'ip': '10.172.14.6',
        'username': 'admin',
        'password': 'plexxi'
    }
}

PLEXXI_SWITCHES_CREDENTIALS = merge_two_dicts(PLEXXI_SWITCHES_CREDENTIALS_MEDIUM1, PLEXXI_SWITCHES_CREDENTIALS_MEDIUM2)

fabric_name = "CRST Medium Rig Fabric"
# Transition fabrics to Adding, Configured
# Keeping this 2-state transition for now because of pending question to CRM on initiate fabric claim with 'Configured' transition that can cause problem
# fabric_states = [[{"op":"replace","path":"/state","value":"Adding"}], [{"op":"replace","path":"/state","value":"Configured"}]]
fabric_adding = [{"op": "replace", "path": "/state", "value": "Adding"}]
# Plexxi Fabric request bodies
#    :List of dictionary of request bodies
plexxi_fabrics = [
    {
        "host": PLEXXI_SWITCHES_CREDENTIALS_MEDIUM1['1']['ip'],
        "name": fabric_name,
        "description": "CRST Medium Rig Fabric"
    }
]

LSG_NAME = ['LSG_MediumRig']

"""
10.172.14.3	p1r1med.dom1172.lab		e039d7842280
10.172.14.4	p2r1med.dom1172.lab		e039d7841600

10.172.14.5	p1r2med.dom1172.lab			e039d7841c80
10.172.14.6	p2r2med.dom1172.lab			e039d7841a00
"""

switch_names_medium1 = ["E0:39:D7:84:22:80", "E0:39:D7:84:16:00"]
switch_names_medium2 = ["E0:39:D7:84:1C:80", "E0:39:D7:84:1A:00"]
switch_names = switch_names_medium1 + switch_names_medium2

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
                    'permittedSwitchTypeUri': 'SWT:Composable Fabric FM 3180'
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
                    'permittedSwitchTypeUri': 'SWT:Composable Fabric FM 3180'
                },
            ]
        }
    }
]

# this is as of 8/13 ToT build
lss_medium1 = [
    {
        "logicalSwitch": {
            "name": "LS_Medium1Rig",
            "state": "Active",
            "status": None,
            "type": "logical-switchV5",
            "managementLevel": "BASIC_MANAGED",
            "logicalSwitchGroupUri": "LSG:" + LSG_NAME[0],
            "switchCredentialConfiguration": [
                {
                    "snmpV1Configuration": {
                        "communityString": "public"
                    },
                    "snmpV3Configuration": {
                        "authorizationProtocol": None,
                        "privacyProtocol": None,
                        "securityLevel": None
                    },
                    "logicalSwitchManagementHost": PLEXXI_SWITCHES_CREDENTIALS_MEDIUM1['1']['ip'],
                    "snmpVersion": "SNMPv1",
                    "snmpPort": 161
                }
            ],
            # name of switches, script will find their appropriate uris by name
            "switchUris": [switch_names_medium1[0], switch_names_medium1[1]]
        },
        "logicalSwitchCredentials": [
            {
                "connectionProperties": [
                    {
                        "propertyName": "SshBasicAuthCredentialUser",
                        "value": PLEXXI_SWITCHES_CREDENTIALS_MEDIUM1['1']['username'],
                        "valueFormat": "Unknown",
                        "valueType": "String"
                    },
                    {
                        "propertyName": "SshBasicAuthCredentialPassword",
                        "value": PLEXXI_SWITCHES_CREDENTIALS_MEDIUM1['1']['password'],
                        "valueFormat": "SecuritySensitive",
                        "valueType": "String"
                    }
                ]
            }
        ]
    }
]

lss_medium2 = [
    {
        "logicalSwitch": {
            "name": "LS_Medium2Rig",
            "state": "Active",
            "status": None,
            "type": "logical-switchV5",
            "managementLevel": "BASIC_MANAGED",
            "logicalSwitchGroupUri": "LSG:" + LSG_NAME[0],
            "switchCredentialConfiguration": [
                {
                    "snmpV1Configuration": {
                        "communityString": "public"
                    },
                    "snmpV3Configuration": {
                        "authorizationProtocol": None,
                        "privacyProtocol": None,
                        "securityLevel": None
                    },
                    "logicalSwitchManagementHost": PLEXXI_SWITCHES_CREDENTIALS_MEDIUM2['3']['ip'],
                    "snmpVersion": "SNMPv1",
                    "snmpPort": 161
                }
            ],
            # name of switches, script will find their appropriate uris by name
            "switchUris": [switch_names_medium2[0], switch_names_medium2[1]]
        },
        "logicalSwitchCredentials": [
            {
                "connectionProperties": [
                    {
                        "propertyName": "SshBasicAuthCredentialUser",
                        "value": PLEXXI_SWITCHES_CREDENTIALS_MEDIUM2['3']['username'],
                        "valueFormat": "Unknown",
                        "valueType": "String"
                    },
                    {
                        "propertyName": "SshBasicAuthCredentialPassword",
                        "value": PLEXXI_SWITCHES_CREDENTIALS_MEDIUM2['4']['password'],
                        "valueFormat": "SecuritySensitive",
                        "valueType": "String"
                    }
                ]
            }
        ]
    }
]

lss = lss_medium1 + lss_medium2

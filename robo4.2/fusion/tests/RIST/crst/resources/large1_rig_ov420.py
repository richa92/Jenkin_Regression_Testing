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


def clean_server_hardware(dc_l):
    dc_l = deepcopy(dc_l)
    for d in dc_l:
        del d['deployment_network']
        del d['os']
        del d['profile']
    return dc_l

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


cpt_host = {"host": "10.178.12.99",
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
                                                   'target': 'VLAN1178-PLEXXI'}]},
               'resource_pool': 'Plexxi_Large'}
cfm_vm = 'CFM_Large'
cfm_ova_data = {'import_spec': {'propertyMapping': {'Hostname': cfm_vm,
                                                    'Domainname': 'dom1178.lab',
                                                    'NTP1': 'ntp.hpecorp.net',
                                                    'DHCP': 'False',
                                                    'IP': '10.178.14.2',
                                                    'Netmask': '255.255.0.0',
                                                    'Gateway': '10.178.0.1',
                                                    'DNS1': '10.171.0.11',
                                                    'DNS2': ''
                                                    },
                                'entityName': cfm_vm,
                                'networkMapping': [{'source': 'VM Network',
                                                    'target': 'VLAN1178-PLEXXI'}]},
                'resource_pool': 'Plexxi_Large'}

#####################
# OneView Data
#####################


def rlist(start, end, prefix='net_', suffix=''):
    return ["{}{}{}".format(prefix, str(x), suffix) for x in xrange(start, end + 1)]


admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

vcenter = {'server': '10.120.0.15', 'user': 'crst_auto1', 'password': 'Russell!sCo0l'}

appliance = {'type': 'ApplianceNetworkConfigurationV2',
             'applianceNetworks':
             [{
                 'macAddress': None,
                 'interfaceName': 'hpqcorpnet',
                 'activeNode': '1',
                 'unconfigure': False,
                 'ipv4Type': 'STATIC',
                 'ipv4Subnet': '255.255.0.0',
                 'ipv4Gateway': '10.178.0.1',
                 'ipv4NameServers': ['10.171.0.11'],
                 'app1Ipv4Addr': '10.178.14.1',
                 'ipv6Type': 'UNCONFIGURE',
                 'hostname': 'oneviewlarge.dom1178.lab',
                 'confOneNode': True,
                 'domainName': 'dom1178.lab',
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
    {'key': 'AD2G C9AA H9PQ KHUY V7B5 HWWB Y9JL KMPL 8ZWC 6FFM 6RMW 9HWE 9JRH XN4Y CMRG HPMR EFFW ANG9 4V8C 92S9 HKDU LWWP 2R3F QPZE 7RQ4 U3US T42G 4BQM 94K2 HFTE GF7C DMJ3 BKT8 WVDC T84V R42A U887 FC2H 5KG2 F6QD NWZA JDEB TCJB 4JJY N8QS DBRB "24R2-02192-002 T2222A HP_OneView_Explicit_Feature J4E8IAMANEON"_32Q6W-PQWTB-H7XYL-39968-RR53R'},
    #    {'key': 'ADCA A9AA H9P9 8HV3 U7B5 HWW5 Y9JL KMPL 9NSD 8CVE WREW JHWE 98QH 35TL CMRG HPMR EFFW AFG9 4U8C E2TK HKDU LWWP 2R3F QPZE 7RQ4 U3US T42G 4BQM 94K2 HFTE GF7C DMJ3 BKT8 WVDC T84V R42A U887 FC2H 5KG2 F6QD NWZA JDEB TCJB 4JJY 589U BBRB"24R2-02192-002 T2222A HP_OneView_w/o_iLO_Explicit_Feature J4E8IAMANEON"'}
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
    {'networkSetType': 'Large', 'name': 'esx-64', 'type': 'network-setV4', 'networkUris': ['crst-mgmt', 'crst-vmotion', 'crst-vsan'] + rlist(35, 232, 'net_', ''), 'nativeNetworkUri': 'crst-mgmt'},
    {'networkSetType': 'Large', 'name': 'linux-trunk-4k', 'type': 'network-setV4', 'networkUris': ['net1', 'crst-mgmt', 'crst-vmotion', 'crst-vsan'] + rlist(3, 32, 'net', '') + rlist(35, 4000, 'net_', ''), 'nativeNetworkUri': 'crst-mgmt'},
]
# temporary until 4k vlan max becomes available in OneView
network_sets_162 = [
    {'name': 'esx-64', 'type': 'network-setV4', 'networkUris': ['crst-mgmt', 'crst-vmotion', 'crst-vsan'] + rlist(35, 232, 'net_', ''), 'nativeNetworkUri': 'crst-mgmt'},
    {'name': 'linux-trunk-4k', 'type': 'network-setV4', 'networkUris': ['net1', 'crst-mgmt', 'crst-vmotion', 'crst-vsan'] + rlist(3, 32, 'net', '') + rlist(35, 162, 'net_', ''), 'nativeNetworkUri': 'crst-mgmt'},
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
server_hardware_large1 = [
    # Large1
    # rack u #1
    {
        "hostname": "10.178.12.54",
        "username": "Administrator",
        "password": "PERJZ4JY",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-64",
        "os": ESXi67,
        "profile": "ProfileL1_U1"
    },
    # rack u #2
    {
        "hostname": "10.178.12.36",
        "username": "Administrator",
        "password": "W67NMGJH",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-64",
        "os": ESXi67,
        "profile": "ProfileL1_U2"
    },
    # rack u #3
    {
        "hostname": "10.178.12.112",
        "username": "Administrator",
        "password": "GU6AY47V",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-64",
        "os": ESXi67,
        "profile": "ProfileL1_U3"
    },
    # rack u #4
    {
        "hostname": "10.178.12.3",
        "username": "Administrator",
        "password": "X287AQFJ",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-64",
        "os": ESXi67,
        "profile": "ProfileL1_U4"
    },
    # rack u #5
    {
        "hostname": "10.178.12.26",
        "username": "Administrator",
        "password": "XBTTXEH4",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-64",
        "os": ESXi67,
        "profile": "ProfileL1_U5"
    },
    # rack u #6
    {
        "hostname": "10.178.12.35",
        "username": "Administrator",
        "password": "RP2ZXBAZ",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-64",
        "os": ESXi67,
        "profile": "ProfileL1_U6"
    },
    # rack u #7
    {
        "hostname": "10.178.12.30",
        "username": "Administrator",
        "password": "HZBYDZEG",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-64",
        "os": ESXi67,
        "profile": "ProfileL1_U7"
    },
    # rack u #8
    {
        "hostname": "10.178.12.82",
        "username": "Administrator",
        "password": "KVUUTPBG",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-64",
        "os": ESXi67,
        "profile": "ProfileL1_U8"
    },
    # rack u #9
    {
        "hostname": "10.178.12.61",
        "username": "Administrator",
        "password": "2QBU6FDG",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-64",
        "os": ESXi67,
        "profile": "ProfileL1_U9"
    },
    # rack u #10
    {
        "hostname": "10.178.12.16",
        "username": "Administrator",
        "password": "M5RQTN5T",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-64",
        "os": ESXi67,
        "profile": "ProfileL1_U10"
    },
    # rack u #11
    {
        "hostname": "10.178.12.50",
        "username": "Administrator",
        "password": "XENF9RRZ",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-64",
        "os": ESXi67,
        "profile": "ProfileL1_U11"
    },
    # rack u #12
    {
        "hostname": "10.178.12.85",
        "username": "Administrator",
        "password": "BBG9S8F9",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-64",
        "os": ESXi67,
        "profile": "ProfileL1_U12"
    },
    # rack u #13
    {
        "hostname": "10.178.12.91",
        "username": "Administrator",
        "password": "TZTPBTRU",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-64",
        "os": ESXi67,
        "profile": "ProfileL1_U13"
    },
    # rack u #14
    {
        "hostname": "10.178.12.40",
        "username": "Administrator",
        "password": "F5QYNPUA",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-64",
        "os": ESXi67,
        "profile": "ProfileL1_U14"
    },
    # rack u #15
    {
        "hostname": "10.178.12.42",
        "username": "Administrator",
        "password": "5E9FPE9V",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-64",
        "os": ESXi67,
        "profile": "ProfileL1_U15"
    },
    # rack u #16
    {
        "hostname": "10.178.12.11",
        "username": "Administrator",
        "password": "2W636W3M",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-64",
        "os": ESXi67,
        "profile": "ProfileL1_U16"
    },
    # rack u #17
    {
        "hostname": "10.178.12.18",
        "username": "Administrator",
        "password": "4ETYD98C",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-64",
        "os": ESXi67,
        "profile": "ProfileL1_U17"
    },
    # rack u #18
    {
        "hostname": "10.178.12.77",
        "username": "Administrator",
        "password": "5MJ797V7",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-64",
        "os": ESXi67,
        "profile": "ProfileL1_U18"
    },
    # rack u #19
    {
        "hostname": "10.178.12.55",
        "username": "Administrator",
        "password": "CB8PQJ6X",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-64",
        "os": ESXi67,
        "profile": "ProfileL1_U19"
    },
    # rack u #20
    {
        "hostname": "10.178.12.10",
        "username": "Administrator",
        "password": "XRUTAUKP",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-64",
        "os": ESXi67,
        "profile": "ProfileL1_U20"
    },
    # rack u #22
    {
        "hostname": "10.178.12.1",
        "username": "Administrator",
        "password": "N9MZYQ62",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-64",
        "os": ESXi67,
        "profile": "ProfileL1_U22"
    },
    # rack u #23
    {
        "hostname": "10.178.12.2",
        "username": "Administrator",
        "password": "27Z6WS9C",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-64",
        "os": ESXi67,
        "profile": "ProfileL1_U23"
    },
    # rack u #24
    {
        "hostname": "10.178.12.32",
        "username": "Administrator",
        "password": "WFSGFHE8",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-64",
        "os": ESXi67,
        "profile": "ProfileL1_U24"
    },
    # rack u #25
    {
        "hostname": "10.178.12.56",
        "username": "Administrator",
        "password": "4WUBRTBC",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-64",
        "os": ESXi67,
        "profile": "ProfileL1_U25"
    },
    # rack u #26
    {
        "hostname": "10.178.12.22",
        "username": "Administrator",
        "password": "C7PASHQA",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-64",
        "os": ESXi67,
        "profile": "ProfileL1_U26"
    },
    # rack u #27
    {
        "hostname": "10.178.12.39",
        "username": "Administrator",
        "password": "WZ99TNN5",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-64",
        "os": ESXi67,
        "profile": "ProfileL1_U27"
    },
    # rack u #28
    {
        "hostname": "10.178.12.60",
        "username": "Administrator",
        "password": "TAN8X9HW",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-64",
        "os": ESXi67,
        "profile": "ProfileL1_U28"
    },
    # rack u #29
    {
        "hostname": "10.178.12.17",
        "username": "Administrator",
        "password": "7NAJ44KD",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-64",
        "os": ESXi67,
        "profile": "ProfileL1_U29"
    },
    # rack u #30
    {
        "hostname": "10.178.12.84",
        "username": "Administrator",
        "password": "QVEWNE24",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-64",
        "os": ESXi67,
        "profile": "ProfileL1_U30"
    },
    # rack u #31
    {
        "hostname": "10.178.12.65",
        "username": "Administrator",
        "password": "HRV7T4DA",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-64",
        "os": ESXi67,
        "profile": "ProfileL1_U31"
    },
    # rack u #32
    {
        "hostname": "10.178.12.29",
        "username": "Administrator",
        "password": "TDQW2GSW",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-64",
        "os": ESXi67,
        "profile": "ProfileL1_U32"
    },
    # rack u #33
    {
        "hostname": "10.178.12.13",
        "username": "Administrator",
        "password": "MPY3APUC",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-64",
        "os": ESXi67,
        "profile": "ProfileL1_U33"
    },
    # rack u #34
    {
        "hostname": "10.178.12.76",
        "username": "Administrator",
        "password": "KYM5QMV5",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-64",
        "os": ESXi67,
        "profile": "ProfileL1_U34"
    },
    # rack u #35
    {
        "hostname": "10.178.12.51",
        "username": "Administrator",
        "password": "E5YYCV65",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "linux-trunk-4k",
        "os": RHEL75,
        "profile": "ProfileL1_U35"
    },
    # rack u #36
    {
        "hostname": "10.178.12.45",
        "username": "Administrator",
        "password": "ZUHE3VNQ",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "linux-trunk-4k",
        "os": RHEL75,
        "profile": "ProfileL1_U36"
    },
    # rack u #37
    {
        "hostname": "10.178.12.28",
        "username": "Administrator",
        "password": "BYUBKREA",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "linux-trunk-4k",
        "os": RHEL75,
        "profile": "ProfileL1_U37"
    },
    # rack u #38
    {
        "hostname": "10.178.12.62",
        "username": "Administrator",
        "password": "TE6MGGV4",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "linux-trunk-4k",
        "os": RHEL75,
        "profile": "ProfileL1_U38"
    },
    # rack u #39
    {
        "hostname": "10.178.12.64",
        "username": "Administrator",
        "password": "387QU5BB",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "linux-trunk-4k",
        "os": RHEL75,
        "profile": "ProfileL1_U39"
    },
]

server_hardware_cpt = server_hardware_large1
server_hardware = clean_server_hardware(server_hardware_cpt)

#####################
# DL Server Profiles section
#####################
server_profile_to_bay_map = {
    # Large1
    'ProfileL1_U1': 'ILOMXQ8240453.dom1178.lab',
    'ProfileL1_U2': 'ILOMXQ82500NF.dom1178.lab',
    'ProfileL1_U3': 'ILOMXQ82500MT.dom1178.lab',
    'ProfileL1_U4': 'ILOMXQ82500MS.dom1178.lab',
    'ProfileL1_U5': 'ILOMXQ82500NH.dom1178.lab',
    'ProfileL1_U6': 'ILOMXQ824045H.dom1178.lab',
    'ProfileL1_U7': 'ILOMXQ824045K.dom1178.lab',
    'ProfileL1_U8': 'ILOMXQ824045D.dom1178.lab',
    'ProfileL1_U9': 'ILOMXQ82405LY.dom1178.lab',
    'ProfileL1_U10': 'ILOMXQ824046Z.dom1178.lab',
    'ProfileL1_U11': 'ILOMXQ82405LM.dom1178.lab',
    'ProfileL1_U12': 'ILOMXQ824046S.dom1178.lab',
    'ProfileL1_U13': 'ILOMXQ824046X.dom1178.lab',
    'ProfileL1_U14': 'ILOMXQ82405LK.dom1178.lab',
    'ProfileL1_U15': 'ILOMXQ824045P.dom1178.lab',
    'ProfileL1_U16': 'ILOMXQ824046P.dom1178.lab',
    'ProfileL1_U17': 'ILOMXQ8240454.dom1178.lab',
    'ProfileL1_U18': 'ILOMXQ824045V.dom1178.lab',
    'ProfileL1_U19': 'ILOMXQ82405LT.dom1178.lab',
    'ProfileL1_U20': 'ILOMXQ8240462.dom1178.lab',
    'ProfileL1_U22': 'ILOMXQ824045L.dom1178.lab',
    'ProfileL1_U23': 'ILOMXQ824046Y.dom1178.lab',
    'ProfileL1_U24': 'ILOMXQ824045J.dom1178.lab',
    'ProfileL1_U25': 'ILOMXQ8240467.dom1178.lab',
    'ProfileL1_U26': 'ILOMXQ824046T.dom1178.lab',
    'ProfileL1_U27': 'ILOMXQ82500MY.dom1178.lab',
    'ProfileL1_U28': 'ILOMXQ82500N0.dom1178.lab',
    'ProfileL1_U29': 'ILOMXQ8240466.dom1178.lab',
    'ProfileL1_U30': 'ILOMXQ82500MW.dom1178.lab',
    'ProfileL1_U31': 'ILOMXQ82405LV.dom1178.lab',
    'ProfileL1_U32': 'ILOMXQ82501T4.dom1178.lab',
    'ProfileL1_U33': 'ILOMXQ82501SQ.dom1178.lab',
    'ProfileL1_U34': 'ILOMXQ82501TD.dom1178.lab',
    'ProfileL1_U35': 'ILOMXQ82501T9.dom1178.lab',
    'ProfileL1_U36': 'ILOMXQ82501T1.dom1178.lab',
    'ProfileL1_U37': 'ILOMXQ824046G.dom1178.lab',
    'ProfileL1_U38': 'ILOMXQ8240460.dom1178.lab',
    'ProfileL1_U39': 'ILOMXQ8240457.dom1178.lab',
}

server_profile_templates = [
    {
        'type': 'ServerProfileTemplateV6',
        'serverProfileDescription': 'ESXi DL360 Gen10 1 Profile',
        'serverHardwareTypeUri': 'SHT:DL360 Gen10 1',
        'enclosureGroupUri': '',
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': 'esx',
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
                                    'networkUri': 'NS:esx-64',
                                    'ipv4': {}
                },
                {
                    'id': 2,
                    'name': 'c2',
                    'functionType': 'Ethernet',
                                    'portId': 'Flr 1:2',
                                    'requestedMbps': 0,
                                    'networkUri': 'NS:esx-64',
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
        'name': 'linux-4k-lag-dl360',
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
]

server_profiles_using_template_large1 = [
    # Large 1 server profiles using templates
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileL1_U1'],
        'serverProfileTemplateUri': 'SPT:esx',
        'name': 'ProfileL1_U1',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileL1_U2'],
        'serverProfileTemplateUri': 'SPT:esx',
        'name': 'ProfileL1_U2',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileL1_U3'],
        'serverProfileTemplateUri': 'SPT:esx',
        'name': 'ProfileL1_U3',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileL1_U4'],
        'serverProfileTemplateUri': 'SPT:esx',
        'name': 'ProfileL1_U4',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileL1_U5'],
        'serverProfileTemplateUri': 'SPT:esx',
        'name': 'ProfileL1_U5',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileL1_U6'],
        'serverProfileTemplateUri': 'SPT:esx',
        'name': 'ProfileL1_U6',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileL1_U7'],
        'serverProfileTemplateUri': 'SPT:esx',
        'name': 'ProfileL1_U7',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileL1_U8'],
        'serverProfileTemplateUri': 'SPT:esx',
        'name': 'ProfileL1_U8',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileL1_U9'],
        'serverProfileTemplateUri': 'SPT:esx',
        'name': 'ProfileL1_U9',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileL1_U10'],
        'serverProfileTemplateUri': 'SPT:esx',
        'name': 'ProfileL1_U10',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileL1_U11'],
        'serverProfileTemplateUri': 'SPT:esx',
        'name': 'ProfileL1_U11',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileL1_U12'],
        'serverProfileTemplateUri': 'SPT:esx',
        'name': 'ProfileL1_U12',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileL1_U13'],
        'serverProfileTemplateUri': 'SPT:esx',
        'name': 'ProfileL1_U13',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileL1_U14'],
        'serverProfileTemplateUri': 'SPT:esx',
        'name': 'ProfileL1_U14',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileL1_U15'],
        'serverProfileTemplateUri': 'SPT:esx',
        'name': 'ProfileL1_U15',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileL1_U16'],
        'serverProfileTemplateUri': 'SPT:esx',
        'name': 'ProfileL1_U16',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileL1_U17'],
        'serverProfileTemplateUri': 'SPT:esx',
        'name': 'ProfileL1_U17',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileL1_U18'],
        'serverProfileTemplateUri': 'SPT:esx',
        'name': 'ProfileL1_U18',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileL1_U19'],
        'serverProfileTemplateUri': 'SPT:esx',
        'name': 'ProfileL1_U19',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileL1_U20'],
        'serverProfileTemplateUri': 'SPT:esx',
        'name': 'ProfileL1_U20',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileL1_U22'],
        'serverProfileTemplateUri': 'SPT:esx',
        'name': 'ProfileL1_U22',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileL1_U23'],
        'serverProfileTemplateUri': 'SPT:esx',
        'name': 'ProfileL1_U23',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileL1_U24'],
        'serverProfileTemplateUri': 'SPT:esx',
        'name': 'ProfileL1_U24',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileL1_U25'],
        'serverProfileTemplateUri': 'SPT:esx',
        'name': 'ProfileL1_U25',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileL1_U26'],
        'serverProfileTemplateUri': 'SPT:esx',
        'name': 'ProfileL1_U26',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileL1_U27'],
        'serverProfileTemplateUri': 'SPT:esx',
        'name': 'ProfileL1_U27',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileL1_U28'],
        'serverProfileTemplateUri': 'SPT:esx',
        'name': 'ProfileL1_U28',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileL1_U29'],
        'serverProfileTemplateUri': 'SPT:esx',
        'name': 'ProfileL1_U29',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileL1_U30'],
        'serverProfileTemplateUri': 'SPT:esx',
        'name': 'ProfileL1_U30',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileL1_U31'],
        'serverProfileTemplateUri': 'SPT:esx',
        'name': 'ProfileL1_U31',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileL1_U32'],
        'serverProfileTemplateUri': 'SPT:esx',
        'name': 'ProfileL1_U32',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileL1_U33'],
        'serverProfileTemplateUri': 'SPT:esx',
        'name': 'ProfileL1_U33',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileL1_U34'],
        'serverProfileTemplateUri': 'SPT:esx',
        'name': 'ProfileL1_U34',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileL1_U35'],
        'serverProfileTemplateUri': 'SPT:linux-4k-lag-dl360',
        'name': 'ProfileL1_U35',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileL1_U36'],
        'serverProfileTemplateUri': 'SPT:linux-4k-lag-dl360',
        'name': 'ProfileL1_U36',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileL1_U37'],
        'serverProfileTemplateUri': 'SPT:linux-4k-lag-dl360',
        'name': 'ProfileL1_U37',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileL1_U38'],
        'serverProfileTemplateUri': 'SPT:linux-4k-lag-dl360',
        'name': 'ProfileL1_U38',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileL1_U39'],
        'serverProfileTemplateUri': 'SPT:linux-4k-lag-dl360',
        'name': 'ProfileL1_U39',
    },
]

server_profiles_using_template = server_profiles_using_template_large1

#####################
# Plexxi section
#####################
# Plexxi connect credentials
plexxi_connect_host = '10.178.14.2'
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
PLEXXI_SWITCHES_CREDENTIALS_LARGE1 = {
    '1': {
        'ip': '10.178.14.3',
        'username': 'admin',
        'password': 'plexxi'
    },
    '2': {
        'ip': '10.178.14.4',
        'username': 'admin',
        'password': 'plexxi'
    }
}

fabric_name = "CRST Large Rig Fabric"
# Transition fabrics to Adding, Configured
# Keeping this 2-state transition for now because of pending question to CRM on initiate fabric claim with 'Configured' transition that can cause problem
# fabric_states = [[{"op":"replace","path":"/state","value":"Adding"}], [{"op":"replace","path":"/state","value":"Configured"}]]
fabric_adding = [{"op": "replace", "path": "/state", "value": "Adding"}]
# Plexxi Fabric request bodies
#    :List of dictionary of request bodies
plexxi_fabrics = [
    {
        "host": PLEXXI_SWITCHES_CREDENTIALS_LARGE1['1']['ip'],
        "name": fabric_name,
        "description": "CRST Large Rig Fabric"
    }
]

LSG_NAME = ['LSG_LargeRig']

switch_names_large1 = ["E0:39:D7:84:29:80", "E0:39:D7:84:24:80"]
switch_names = switch_names_large1

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

# this is as of 8/13/2018 ToT build
lss_large1 = [
    {
        "logicalSwitch": {
            "name": "LS_Large1Rig",
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
                    "logicalSwitchManagementHost": PLEXXI_SWITCHES_CREDENTIALS_LARGE1['1']['ip'],
                    "snmpVersion": "SNMPv1",
                    "snmpPort": 161
                }
            ],
            # name of switches, script will find their appropriate uris by name
            "switchUris": [switch_names_large1[0], switch_names_large1[1]]
        },
        "logicalSwitchCredentials": [
            {
                "connectionProperties": [
                    {
                        "propertyName": "SshBasicAuthCredentialUser",
                        "value": PLEXXI_SWITCHES_CREDENTIALS_LARGE1['1']['username'],
                        "valueFormat": "Unknown",
                        "valueType": "String"
                    },
                    {
                        "propertyName": "SshBasicAuthCredentialPassword",
                        "value": PLEXXI_SWITCHES_CREDENTIALS_LARGE1['1']['password'],
                        "valueFormat": "SecuritySensitive",
                        "valueType": "String"
                    }
                ]
            }
        ]
    }
]

lss = lss_large1

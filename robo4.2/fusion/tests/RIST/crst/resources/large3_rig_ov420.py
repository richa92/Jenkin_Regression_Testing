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


def clean_server_hardare(dc_l):
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

# ethernet_networks = [
#     {'name': 'net1',
#      'description': 'General networking',
#      'type': 'ethernet-networkV4',
#      'vlanId': 1,
#      'purpose': 'General',
#      'smartLink': True,
#      'privateNetwork': False,
#      'connectionTemplateUri': None,
#      'ethernetNetworkType': 'Tagged'
#      },
#     {'name': 'crst-mgmt',
#      'description': 'Management and deployment network',
#      'type': 'ethernet-networkV4',
#      'vlanId': 2,
#      'purpose': 'Management',
#      'smartLink': True,
#      'privateNetwork': False,
#      'connectionTemplateUri': None,
#      'ethernetNetworkType': 'Tagged'
#      },
#     {'name': 'crst-vmotion',
#      'description': 'VMWare vmotion network',
#      'type': 'ethernet-networkV4',
#      'vlanId': 33,
#      'purpose': 'VMMigration',
#      'smartLink': True,
#      'privateNetwork': False,
#      'connectionTemplateUri': None,
#      'ethernetNetworkType': 'Tagged'
#      },
#     {'name': 'crst-vsan',
#      'description': 'VMWare vsan network',
#      'type': 'ethernet-networkV4',
#      'vlanId': 34,
#      'purpose': 'FaultTolerance',
#      'smartLink': True,
#      'privateNetwork': False,
#      'connectionTemplateUri': None,
#      'ethernetNetworkType': 'Tagged'
#      }
# ]
#
# ethernet_ranges = [
#     {'prefix': 'net', 'suffix': '', 'start': 3, 'end': 32, 'name': None, 'type': 'ethernet-networkV4',
#         'vlanId': None, 'purpose': 'General', 'description': 'General networking', 'smartLink': True, 'privateNetwork': False, 'connectionTemplateUri': None,
#      'ethernetNetworkType': 'Tagged'},
# ]

"""
These create ethernet networks in bulk.
"""
# bulk_ethernet_network = {
#     "vlanIdRange": "35-4000", "description": "General networking", "purpose": "General", "namePrefix": "net", "smartLink": True, "privateNetwork": False, "bandwidth": {"maximumBandwidth": 10000, "typicalBandwidth": 2500}, "type": "bulk-ethernet-networkV1"}
#
network_sets_4k = [
    #     {'networkSetType': 'Large', 'name': 'esx-64', 'type': 'network-setV4', 'networkUris': ['crst-mgmt', 'crst-vmotion', 'crst-vsan'] + rlist(35, 232, 'net_', ''), 'nativeNetworkUri': 'crst-mgmt'},
    #     {'name': 'win-trunk', 'type': 'network-setV4', 'networkUris': ['crst-mgmt'] + rlist(3500, 3531, 'net_', ''), 'nativeNetworkUri': 'crst-mgmt'},
    {'networkSetType': 'Large', 'name': 'linux-trunk-1k-a', 'type': 'network-setV4', 'networkUris': ['net1', 'crst-mgmt', 'crst-vmotion', 'crst-vsan'] + rlist(3, 32, 'net', '') + rlist(35, 1000, 'net_', ''), 'nativeNetworkUri': 'crst-mgmt'},
    {'networkSetType': 'Large', 'name': 'linux-trunk-1k-b', 'type': 'network-setV4', 'networkUris': ['net1', 'crst-mgmt', 'crst-vmotion', 'crst-vsan'] + rlist(3, 32, 'net', '') + rlist(35, 1000, 'net_', ''), 'nativeNetworkUri': 'crst-mgmt'},
    #     {'networkSetType': 'Large', 'name': 'linux-trunk-4k', 'type': 'network-setV4', 'networkUris': ['net1', 'crst-mgmt', 'crst-vmotion', 'crst-vsan'] + rlist(3, 32, 'net', '') + rlist(35, 4000, 'net_', ''), 'nativeNetworkUri': 'crst-mgmt'},
]
# temporary until 4k vlan max becomes available in OneView
# network_sets_162 = [
#     {'name': 'esx-64', 'type': 'network-setV4', 'networkUris': ['crst-mgmt', 'crst-vmotion', 'crst-vsan'] + rlist(35, 232, 'net_', ''), 'nativeNetworkUri': 'crst-mgmt'},
#     {'name': 'win-trunk', 'type': 'network-setV4', 'networkUris': ['crst-mgmt'] + rlist(3500, 3531, 'net_', ''), 'nativeNetworkUri': 'crst-mgmt'},
#     {'name': 'linux-trunk-1k-a', 'type': 'network-setV4', 'networkUris': ['net1', 'crst-mgmt', 'crst-vmotion', 'crst-vsan'] + rlist(3, 32, 'net', '') + rlist(35, 162, 'net_', ''), 'nativeNetworkUri': 'crst-mgmt'},
#     {'name': 'linux-trunk-1k-b', 'type': 'network-setV4', 'networkUris': ['net1', 'crst-mgmt', 'crst-vmotion', 'crst-vsan'] + rlist(3, 32, 'net', '') + rlist(35, 162, 'net_', ''), 'nativeNetworkUri': 'crst-mgmt'},
#     {'name': 'linux-trunk-4k', 'type': 'network-setV4', 'networkUris': ['net1', 'crst-mgmt', 'crst-vmotion', 'crst-vsan'] + rlist(3, 32, 'net', '') + rlist(35, 162, 'net_', ''), 'nativeNetworkUri': 'crst-mgmt'},
# ]
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
server_hardware_large3 = [
    # rack u1-2
    {
        "hostname": "10.178.12.71",
        "username": "Administrator",
        "password": "XFDMQ2R7",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "linux-trunk-1k-a",
        "os": RHEL75,
        "profile": "ProfileL3_U1-2"
    },
    # rack u3-4
    {
        "hostname": "10.178.12.43",
        "username": "Administrator",
        "password": "GCJS2RN5",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "linux-trunk-1k-a",
        "os": RHEL75,
        "profile": "ProfileL3_U3-4"
    },
    # rack u5-6
    {
        "hostname": "10.178.12.63",
        "username": "Administrator",
        "password": "GKNMVBF5",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "linux-trunk-1k-a",
        "os": RHEL75,
        "profile": "ProfileL3_U5-6"
    },
    # rack u7-8
    {
        "hostname": "10.178.12.88",
        "username": "Administrator",
        "password": "WY75DMZ8",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "linux-trunk-1k-a",
        "os": RHEL75,
        "profile": "ProfileL3_U7-8"
    },
    # rack u9-10
    {
        "hostname": "10.178.12.59",
        "username": "Administrator",
        "password": "CJJJBVL7",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "linux-trunk-1k-a",
        "os": RHEL75,
        "profile": "ProfileL3_U9-10"
    },
    # rack u11-12
    {
        "hostname": "10.178.12.57",
        "username": "Administrator",
        "password": "GTBCH2W6",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "linux-trunk-1k-a",
        "os": RHEL75,
        "profile": "ProfileL3_U11-12"
    },
    # rack u13-14
    {
        "hostname": "10.178.12.86",
        "username": "Administrator",
        "password": "QNHQHZC5",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "linux-trunk-1k-a",
        "os": RHEL75,
        "profile": "ProfileL3_U13-14"
    },
    # rack u15-16
    {
        "hostname": "10.178.12.47",
        "username": "Administrator",
        "password": "MZXJNZD6",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "linux-trunk-1k-a",
        "os": RHEL75,
        "profile": "ProfileL3_U15-16"
    },
    # rack u17-18
    {
        "hostname": "10.178.12.81",
        "username": "Administrator",
        "password": "WFWZRBM7",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "linux-trunk-1k-a",
        "os": RHEL75,
        "profile": "ProfileL3_U17-18"
    },
    # rack u19-20
    {
        "hostname": "10.178.12.83",
        "username": "Administrator",
        "password": "DMXM7MJ8",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "linux-trunk-1k-a",
        "os": RHEL75,
        "profile": "ProfileL3_U19-20"
    },
    # rack u22-23
    {
        "hostname": "10.178.12.41",
        "username": "Administrator",
        "password": "CT2YZSG7",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "linux-trunk-4k",
        "os": RHEL75,
        "profile": "ProfileL3_U22-23"
    },
    # rack u24-25
    {
        "hostname": "10.178.12.23",
        "username": "Administrator",
        "password": "GWKYSRR6",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "linux-trunk-4k",
        "os": RHEL75,
        "profile": "ProfileL3_U24-25"
    },
    # rack u26-27
    {
        "hostname": "10.178.12.70",
        "username": "Administrator",
        "password": "5QNGG256",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "linux-trunk-4k",
        "os": RHEL75,
        "profile": "ProfileL3_U26-27"
    },
    # rack u28-29
    {
        "hostname": "10.178.12.27",
        "username": "Administrator",
        "password": "X5R2TDM5",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "linux-trunk-4k",
        "os": RHEL75,
        "profile": "ProfileL3_U28-29"
    },
    # rack u30-31
    {
        "hostname": "10.178.12.72",
        "username": "Administrator",
        "password": "RDSDZQ58",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "linux-trunk-4k",
        "os": RHEL75,
        "profile": "ProfileL3_U30-31"
    },
    # rack u32-33
    {
        "hostname": "10.178.12.87",
        "username": "Administrator",
        "password": "HFLDMM28",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "linux-trunk-4k",
        "os": RHEL75,
        "profile": "ProfileL3_U32-33"
    },
    # rack u34-35
    {
        "hostname": "10.178.12.53",
        "username": "Administrator",
        "password": "GQ5JXGB5",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "linux-trunk-4k",
        "os": RHEL75,
        "profile": "ProfileL3_U34-35"
    },
    # rack u36-37
    {
        "hostname": "10.178.12.15",
        "username": "Administrator",
        "password": "RVDDSH56",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "linux-trunk-4k",
        "os": RHEL75,
        "profile": "ProfileL3_U36-37"
    },
    # rack u38-39
    {
        "hostname": "10.178.12.89",
        "username": "Administrator",
        "password": "XGCTDZW7",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "linux-trunk-4k",
        "os": RHEL75,
        "profile": "ProfileL3_U38-39"
    },
]

server_hardware_cpt = server_hardware_large3
server_hardware = clean_server_hardare(server_hardware_cpt)

#####################
# DL Server Profiles section
#####################
server_profile_to_bay_map = {
    # Large3
    'ProfileL3_U1-2': 'ILO2M282501WP.dom1178.lab',
    'ProfileL3_U3-4': 'ILO2M282501X9.dom1178.lab',
    'ProfileL3_U5-6': 'ILO2M282501X8.dom1178.lab',
    'ProfileL3_U7-8': 'ILO2M282501X4.dom1178.lab',
    'ProfileL3_U9-10': 'ILO2M282501X6.dom1178.lab',
    'ProfileL3_U11-12': 'ILO2M282501X7.dom1178.lab',
    'ProfileL3_U13-14': 'ILO2M282501WW.dom1178.lab',
    'ProfileL3_U15-16': 'ILO2M282501WX.dom1178.lab',
    'ProfileL3_U17-18': 'ILO2M282501WZ.dom1178.lab',
    'ProfileL3_U19-20': 'ILO2M282501WY.dom1178.lab',
    'ProfileL3_U22-23': 'ILO2M282501X0.dom1178.lab',
    'ProfileL3_U24-25': 'ILO2M282501X1.dom1178.lab',
    'ProfileL3_U26-27': 'ILO2M282501X2.dom1178.lab',
    'ProfileL3_U28-29': 'ILO2M282501KY.dom1178.lab',
    'ProfileL3_U30-31': 'ILO2M282501KT.dom1178.lab',
    'ProfileL3_U32-33': 'ILO2M282501KV.dom1178.lab',
    'ProfileL3_U34-35': 'ILO2M282501KK.dom1178.lab',
    'ProfileL3_U36-37': 'ILO2M282501WS.dom1178.lab',
    'ProfileL3_U38-39': 'ILO2M282501KR.dom1178.lab',
}

server_profile_templates = [
    {
        'type': 'ServerProfileTemplateV6',
        'serverProfileDescription': 'Linux NoLAG DL380 Gen10 1 Profile',
        'serverHardwareTypeUri': 'SHT:DL380 Gen10 1',
        'enclosureGroupUri': '',
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': 'linux-1k',
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
                                    'ipv4': {},
                },
                {
                    'id': 2,
                    'name': 'c2',
                    'functionType': 'Ethernet',
                                    'portId': 'Flr 1:2',
                                    'requestedMbps': 0,
                                    'networkUri': 'NS:linux-trunk-1k-b',
                                    'ipv4': {},
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
        'name': 'linux-4k-lag-dl380',
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

server_profiles_using_template_large3 = [
    # Large 3 server profiles using templates
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileL3_U1-2'],
        'serverProfileTemplateUri': 'SPT:linux-1k',
        'name': 'ProfileL3_U1-2',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileL3_U3-4'],
        'serverProfileTemplateUri': 'SPT:linux-1k',
        'name': 'ProfileL3_U3-4',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileL3_U5-6'],
        'serverProfileTemplateUri': 'SPT:linux-1k',
        'name': 'ProfileL3_U5-6',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileL3_U7-8'],
        'serverProfileTemplateUri': 'SPT:linux-1k',
        'name': 'ProfileL3_U7-8',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileL3_U9-10'],
        'serverProfileTemplateUri': 'SPT:linux-1k',
        'name': 'ProfileL3_U9-10',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileL3_U11-12'],
        'serverProfileTemplateUri': 'SPT:linux-1k',
        'name': 'ProfileL3_U11-12',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileL3_U13-14'],
        'serverProfileTemplateUri': 'SPT:linux-1k',
        'name': 'ProfileL3_U13-14',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileL3_U15-16'],
        'serverProfileTemplateUri': 'SPT:linux-1k',
        'name': 'ProfileL3_U15-16',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileL3_U17-18'],
        'serverProfileTemplateUri': 'SPT:linux-1k',
        'name': 'ProfileL3_U17-18',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileL3_U19-20'],
        'serverProfileTemplateUri': 'SPT:linux-1k',
        'name': 'ProfileL3_U19-20',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileL3_U22-23'],
        'serverProfileTemplateUri': 'SPT:linux-4k-lag-dl380',
        'name': 'ProfileL3_U22-23',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileL3_U24-25'],
        'serverProfileTemplateUri': 'SPT:linux-4k-lag-dl380',
        'name': 'ProfileL3_U24-25',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileL3_U26-27'],
        'serverProfileTemplateUri': 'SPT:linux-4k-lag-dl380',
        'name': 'ProfileL3_U26-27',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileL3_U28-29'],
        'serverProfileTemplateUri': 'SPT:linux-4k-lag-dl380',
        'name': 'ProfileL3_U28-29',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileL3_U30-31'],
        'serverProfileTemplateUri': 'SPT:linux-4k-lag-dl380',
        'name': 'ProfileL3_U30-31',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileL3_U32-33'],
        'serverProfileTemplateUri': 'SPT:linux-4k-lag-dl380',
        'name': 'ProfileL3_U32-33',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileL3_U34-35'],
        'serverProfileTemplateUri': 'SPT:linux-4k-lag-dl380',
        'name': 'ProfileL3_U34-35',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileL3_U36-37'],
        'serverProfileTemplateUri': 'SPT:linux-4k-lag-dl380',
        'name': 'ProfileL3_U36-37',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileL3_U38-39'],
        'serverProfileTemplateUri': 'SPT:linux-4k-lag-dl380',
        'name': 'ProfileL3_U38-39',
    },
]

server_profiles_using_template = server_profiles_using_template_large3

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
PLEXXI_SWITCHES_CREDENTIALS_LARGE3 = {
    '5': {
        'ip': '10.178.14.7',
        'username': 'admin',
        'password': 'plexxi'
    },
    '6': {
        'ip': '10.178.14.8',
        'username': 'admin',
        'password': 'plexxi'
    },
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
        "host": PLEXXI_SWITCHES_CREDENTIALS_LARGE3['5']['ip'],
        "name": fabric_name,
        "description": "CRST Large Rig Fabric"
    }
]

LSG_NAME = ['LSG_LargeRig']

switch_names_large3 = ["E0:39:D7:84:1F:00", "E0:39:D7:84:19:00"]
switch_names = switch_names_large3

# lsgs = [
#     {
#         'name': LSG_NAME[0],
#         'type': 'logical-switch-groupV4',
#         'switchMapTemplate': {
#             'switchMapEntryTemplates': [
#                 {
#                     'logicalLocation': {
#                         'locationEntries': [
#                             {
#                                 'relativeValue': 1,
#                                 'type': 'StackingMemberId'
#                             }
#                         ]
#                     },
#                     'permittedSwitchTypeUri': 'SWT:Composable Fabric FM 3180'
#                 },
#                 {
#                     'logicalLocation': {
#                         'locationEntries': [
#                             {
#                                 'relativeValue': 2,
#                                 'type': 'StackingMemberId'
#                             }
#                         ]
#                     },
#                     'permittedSwitchTypeUri': 'SWT:Composable Fabric FM 3180'
#                 },
#             ]
#         }
#     }
# ]

# this is as of 8/13/2018 ToT build
lss_large3 = [
    {
        "logicalSwitch": {
            "name": "LS_Large3Rig",
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
                    "logicalSwitchManagementHost": PLEXXI_SWITCHES_CREDENTIALS_LARGE3['5']['ip'],
                    "snmpVersion": "SNMPv1",
                    "snmpPort": 161
                }
            ],
            # name of switches, script will find their appropriate uris by name
            "switchUris": [switch_names_large3[0], switch_names_large3[1]]
        },
        "logicalSwitchCredentials": [
            {
                "connectionProperties": [
                    {
                        "propertyName": "SshBasicAuthCredentialUser",
                        "value": PLEXXI_SWITCHES_CREDENTIALS_LARGE3['5']['username'],
                        "valueFormat": "Unknown",
                        "valueType": "String"
                    },
                    {
                        "propertyName": "SshBasicAuthCredentialPassword",
                        "value": PLEXXI_SWITCHES_CREDENTIALS_LARGE3['5']['password'],
                        "valueFormat": "SecuritySensitive",
                        "valueType": "String"
                    }
                ]
            }
        ]
    }
]

lss = lss_large3

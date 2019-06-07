"""
Vader rig data file
"""
from copy import deepcopy


def rlist(start, end, prefix='net_', suffix=''):
    """ generate net names """
    return ["{}{}{}".format(prefix, str(x), suffix)
            for x in xrange(start, end + 1)]


def merge_two_dicts(x, y):
    """ merge dicts """
    z = x.copy()
    z.update(y)
    return z


def clean_server_hardware(dc_l):
    """ cpt method to remove unwanted attributes """
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
    """ create cpt payload  """
    return {"os_name": os['os_name'],
            "os_repo": os['os_repo'],
            "deployment_network": net,
            "ilo_user": ilou,
            "ilo_pass": ilop,
            "system_password": "Hpvse123!"
            }


cpt_host = {"host": "10.177.12.192",
            "user": "root",
            "password": "rootpwd"}

ESXi65 = {"os_name": "ESXi65x64",
          "os_repo": "http://{}/deployment/iso/vmware/VMware-ESXi-6.5.0-Update2-9298722-HPE-Gen9plus-650.U2.10.4.0.4-Mar2019.iso".format(cpt_host['host']),
          }

ESXi67 = {"os_name": "ESXi67x64",
          "os_repo": "http://{}/deployment/iso/vmware/VMware-ESXi-6.7.0-Update1-10302608-HPE-Gen9plus-670.U1.10.3.5.12-Oct2018.iso".format(cpt_host['host'])
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
ov_vm = 'HPEOneView_Vader'
ov_ova_data = {'import_spec': {'entityName': ov_vm,
                               'networkMapping': [{'source': 'VM Network',
                                                   'target': 'VLAN1177-PLEXXI'}]},
               'resource_pool': 'Plexxi_Vader'}
cfm_vm = 'CFM_Vader'
cfm_ova_data = {'import_spec': {'propertyMapping': {'Hostname': cfm_vm,
                                                    'Domainname': 'dom1177.lab',
                                                    'NTP1': 'ntp.hpecorp.net',
                                                    'DHCP': 'False',
                                                    'IP': '10.177.14.2',
                                                    'Netmask': '255.255.0.0',
                                                    'Gateway': '10.177.0.1',
                                                    'DNS1': '10.171.0.11',
                                                    'DNS2': ''
                                                    },
                                'entityName': cfm_vm,
                                'networkMapping': [{'source': 'VM Network',
                                                    'target': 'VLAN1177-PLEXXI'}]},
                'resource_pool': 'Plexxi_Vader'}

#####################
# OneView Data
#####################
admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

vcenter = {
    'server': '10.120.0.15',
    'user': 'crst_auto1',
    'password': 'Russell!sCo0l'}

appliance = {'type': 'ApplianceNetworkConfigurationV2',
             'applianceNetworks':
             [{
                 'macAddress': None,
                 'interfaceName': 'hpqcorpnet',
                 'activeNode': '1',
                 'unconfigure': False,
                 'ipv4Type': 'STATIC',
                 'ipv4Subnet': '255.255.0.0',
                 'ipv4Gateway': '10.177.0.1',
                 'ipv4NameServers': ['10.171.0.11'],
                 'app1Ipv4Addr': '10.177.14.1',
                 'ipv6Type': 'UNCONFIGURE',
                 'hostname': 'oneviewVADER.dom1177.lab',
                 'confOneNode': True,
                 'domainName': 'dom1177.lab',
                 'aliasDisabled': True,
             }],
             }

timeandlocale = {
    'type': 'TimeAndLocale',
    'dateTime': None,
    'timezone': 'UTC',
    'ntpServers': ['16.110.135.123'],
    'locale': 'en_US.UTF-8'}

ranges = [{'name': 'CR-MED-MAC', 'type': 'Range', 'category': 'id-range-VMAC', 'rangeCategory': 'Custom', 'startAddress': 'A2:22:22:00:00:00', 'endAddress': 'A2:22:22:0F:FF:FF', 'enabled': True},
          {'name': 'CR-MED-WWN',
           'type': 'Range',
           'category': 'id-range-VWWN',
           'rangeCategory': 'Custom',
           'startAddress': '22:22:2C:22:00:00:00:00',
           'endAddress': '22:22:2C:22:00:0F:FF:FF',
           'enabled': True},
          {'name': 'CR-MED-SN', 'type': 'Range', 'category': 'id-range-VSN', 'rangeCategory': 'Custom', 'startAddress': 'VCUCCC0000', 'endAddress': 'VCUCCC0ZZZ', 'enabled': True}]

users = [{'userName': 'Serveradmin2',
          'password': 'Serveradmin2',
          'fullName': 'Server Admin2',
          'permissions': [{'roleName': 'Server administrator',
                           'scopeUri': 'MySampleScope2'},
                          {'roleName': 'Server administrator',
                           'scopeUri': 'ProfileManager'}],
          'emailAddress': 'sarah@hp.com',
          'officePhone': '970-555-0003',
          'mobilePhone': '970-500-0003',
          'type': 'UserAndPermissions'}]

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

licenses = [{'key': 'QDSE A9AA H9PY KHV3 V7B5 HWWB Y9JL KMPL PRWC 6BZE GR4W 9HWE 9SS8 TN63 CMRG HPMR MHFW AVG9 4V8S MSWL HKDU LWWP 2R3F QPZE 7RQ4 U3US T42G 4BQM 94K2 HFTE GF7C DMJ3 BKT8 WVDC N84V B78E X8MG JKYX FK82 F6AD ZMJC JDEB ZHJ9 MJAA 5NMC CG6C "24R2-02192-002 T2222A HP_OneView_Explicit_Feature J4E8IAMANEON"_333M7-K2ZY2-XQRN6-99WGK-2HKJR'},
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
    "vlanIdRange": "35-4000", "description": "General networking", "purpose": "General", "namePrefix": "net", "smartLink": True, "privateNetwork": False, "bandwidth": {"maximumBandwidth": 10000, "typicalBandwidth": 2500}, "type": "bulk-ethernet-networkV2"}

network_sets_4k = [
    {'networkSetType': 'Large',
     'name': 'esx-200',
     'type': 'network-setV5',
     'networkUris': ['crst-mgmt',
                     'crst-vmotion',
                     'crst-vsan'] + rlist(35,
                                          232,
                                          'net_',
                                          ''),
     'nativeNetworkUri': 'crst-mgmt'},
    {'networkSetType': 'Large',
     'name': 'esx-400',
     'type': 'network-setV5',
     'networkUris': ['crst-mgmt',
                     'crst-vmotion',
                     'crst-vsan'] + rlist(501,
                                          897,
                                          'net_',
                                          ''),
     'nativeNetworkUri': 'crst-mgmt'},
    {'name': 'win-trunk',
     'type': 'network-setV5',
     'networkUris': ['crst-mgmt'] + rlist(3500,
                                          3531,
                                          'net_',
                                          ''),
     'nativeNetworkUri': 'crst-mgmt'},
    {'networkSetType': 'Large',
     'name': 'linux-trunk-1k-a',
     'type': 'network-setV5',
     'networkUris': ['net1',
                     'crst-mgmt',
                     'crst-vmotion',
                     'crst-vsan'] + rlist(3,
                                          32,
                                          'net',
                                          '') + rlist(35,
                                                      1000,
                                                      'net_',
                                                      ''),
     'nativeNetworkUri': 'crst-mgmt'},
    {'networkSetType': 'Large',
     'name': 'linux-trunk-1k-b',
     'type': 'network-setV5',
     'networkUris': ['net1',
                     'crst-mgmt',
                     'crst-vmotion',
                     'crst-vsan'] + rlist(3,
                                          32,
                                          'net',
                                          '') + rlist(35,
                                                      1000,
                                                      'net_',
                                                      ''),
     'nativeNetworkUri': 'crst-mgmt'},
    {'networkSetType': 'Large',
     'name': 'linux-trunk-4k',
     'type': 'network-setV5',
     'networkUris': ['net1',
                     'crst-mgmt',
                     'crst-vmotion',
                     'crst-vsan'] + rlist(3,
                                          32,
                                          'net',
                                          '') + rlist(35,
                                                      4000,
                                                      'net_',
                                                      ''),
     'nativeNetworkUri': 'crst-mgmt'},
]

network_sets = network_sets_4k

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
server_hardware_Vader1 = [
    # Vader1
    # rack u #1
    {
        "hostname": "10.177.12.152",
        "username": "Administrator",
        "password": "MQZRJ7VX",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR1_U1"
    },
    # rack u #2
    {
        "hostname": "10.177.12.149",
        "username": "Administrator",
        "password": "TDG2RMHB",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR1_U2"
    },
    # rack u #3
    {
        "hostname": "10.177.12.158",
        "username": "Administrator",
        "password": "6NZNBXTS",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR1_U3"
    },
    # rack u #4
    {
        "hostname": "10.177.12.139",
        "username": "Administrator",
        "password": "66S2WKMZ",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR1_U4"
    },
    # rack u #5
    {
        "hostname": "10.177.12.145",
        "username": "Administrator",
        "password": "8ZJ2CWRP",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR1_U5"
    },
    # rack u #6
    {
        "hostname": "10.177.12.148",
        "username": "Administrator",
        "password": "CLRGS6HN",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR1_U6"
    },
    # rack u #7
    {
        "hostname": "10.177.12.141",
        "username": "Administrator",
        "password": "WSJ6DNVM",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR1_U7"
    },
    # rack u #8
    {
        "hostname": "10.177.12.140",
        "username": "Administrator",
        "password": "HGBB9BD7",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR1_U8"
    },
    # rack u #9
    {
        "hostname": "10.177.12.157",
        "username": "Administrator",
        "password": "GRGGK9DD",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR1_U9"
    },
    # rack u #10
    {
        "hostname": "10.177.12.154",
        "username": "Administrator",
        "password": "HST2WVHR",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR1_U10"
    },
    # rack u #11
    {
        "hostname": "10.177.12.155",
        "username": "Administrator",
        "password": "YJ7JYWLY",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR1_U11"
    },
    # rack u #12
    {
        "hostname": "10.177.12.143",
        "username": "Administrator",
        "password": "6GKDST5Y",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-400",
        "os": ESXi67,
        "profile": "ProfileR1_U12"
    },
    # rack u #13
    {
        "hostname": "10.177.12.147",
        "username": "Administrator",
        "password": "FHK7ZMDJ",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-400",
        "os": ESXi67,
        "profile": "ProfileR1_U13"
    },
    # rack u #14
    {
        "hostname": "10.177.12.151",
        "username": "Administrator",
        "password": "ZPFSV6KF",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-400",
        "os": ESXi67,
        "profile": "ProfileR1_U14"
    },
    # rack u #15
    {
        "hostname": "10.177.12.144",
        "username": "Administrator",
        "password": "2LZLT29W",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-400",
        "os": ESXi67,
        "profile": "ProfileR1_U15"
    },
    # rack u #16
    {
        "hostname": "10.177.12.142",
        "username": "Administrator",
        "password": "SDD9KSQC",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-400",
        "os": ESXi67,
        "profile": "ProfileR1_U16"
    },
    # rack u #17
    {
        "hostname": "10.177.12.150",
        "username": "Administrator",
        "password": "MT26WNZK",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-400",
        "os": ESXi67,
        "profile": "ProfileR1_U16"
    },
    # rack u #18
    {
        "hostname": "10.177.12.156",
        "username": "Administrator",
        "password": "DVYDZ2S8",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-400",
        "os": ESXi67,
        "profile": "ProfileR1_U16"
    },
    # rack u #19
    {
        "hostname": "10.177.12.146",
        "username": "Administrator",
        "password": "NG9VNTJW",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-400",
        "os": ESXi67,
        "profile": "ProfileR1_U19"
    },
    # rack u #20
    {
        "hostname": "10.177.12.153",
        "username": "Administrator",
        "password": "822N7YKJ",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-400",
        "os": ESXi67,
        "profile": "ProfileR1_U20"
    },
]

server_hardware_Vader2 = [
    # Vader2
    # rack u #1
    {
        "hostname": "10.177.12.172",
        "username": "Administrator",
        "password": "9C5DZF29",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR2_U1"
    },
    # rack u #2
    {
        "hostname": "10.177.12.173",
        "username": "Administrator",
        "password": "T59KLWDK",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR2_U2"
    },
    # rack u #3
    {
        "hostname": "10.177.12.171",
        "username": "Administrator",
        "password": "CLPJL5GV",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR2_U3"
    },
    # rack u #4
    {
        "hostname": "10.177.12.170",
        "username": "Administrator",
        "password": "R8BBYHCV",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR2_U4"
    },
    # rack u #5
    {
        "hostname": "10.177.12.183",
        "username": "Administrator",
        "password": "V2VCRRVG",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR2_U5"
    },
    # rack u #6
    {
        "hostname": "10.177.12.167",
        "username": "Administrator",
        "password": "85P6KJ7M",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR2_U6"
    },
    # rack u #7
    # {
    # "hostname": "10.177.12.182",
    # "username": "Administrator",
    # "password": "ZMV8QDGF",
    # "force": True,
    # "licensingIntent": "OneView",
    # "configurationState": "Managed",
    # "deployment_network": "esx-200",
    # "os": ESXi67,
    # "profile": "ProfileR2_U7"
    # },
    # rack u #8
    # {
    # "hostname": "10.177.12.169",
    # "username": "Administrator",
    # "password": "CXJH8HK2",
    # "force": True,
    # "licensingIntent": "OneView",
    # "configurationState": "Managed",
    # "deployment_network": "esx-200",
    # "os": ESXi67,
    # "profile": "ProfileR2_U8"
    # },
    # rack u #9
    # {
    # "hostname": "10.177.12.168",
    # "username": "Administrator",
    # "password": "KXY6QQYJ",
    # "force": True,
    # "licensingIntent": "OneView",
    # "configurationState": "Managed",
    # "deployment_network": "esx-200",
    # "os": ESXi67,
    # "profile": "ProfileR2_U9"
    # },
    # rack u #10
    # {
    # "hostname": "10.177.12.166",
    # "username": "Administrator",
    # "password": "TWNXC8FM",
    # "force": True,
    # "licensingIntent": "OneView",
    # "configurationState": "Managed",
    # "deployment_network": "esx-200",
    # "os": ESXi67,
    # "profile": "ProfileR2_U10"
    # },
    # rack u #11
    # {
    # "hostname": "10.177.12.165",
    # "username": "Administrator",
    # "password": "ZTQV7QZT",
    # "force": True,
    # "licensingIntent": "OneView",
    # "configurationState": "Managed",
    # "deployment_network": "esx-200",
    # "os": ESXi67,
    # "profile": "ProfileR2_U11"
    # },
    # rack u #12
    # {
    # "hostname": "10.177.12.161",
    # "username": "Administrator",
    # "password": "BG8VYHJL",
    # "force": True,
    # "licensingIntent": "OneView",
    # "configurationState": "Managed",
    # "deployment_network": "esx-200",
    # "os": ESXi67,
    # "profile": "ProfileR2_U12"
    # },
    # rack u #13
    # {
    # "hostname": "10.177.12.164",
    # "username": "Administrator",
    # "password": "T9SGQVQL",
    # "force": True,
    # "licensingIntent": "OneView",
    # "configurationState": "Managed",
    # "deployment_network": "esx-200",
    # "os": ESXi67,
    # "profile": "ProfileR2_U13"
    # },
    # rack u #14
    # {
    # "hostname": "10.177.12.162",
    # "username": "Administrator",
    # "password": "X8SG6DL9",
    # "force": True,
    # "licensingIntent": "OneView",
    # "configurationState": "Managed",
    # "deployment_network": "esx-200",
    # "os": ESXi67,
    # "profile": "ProfileR2_U14"
    # },
    # rack u #15
    # {
    # "hostname": "10.177.12.163",
    # "username": "Administrator",
    # "password": "WFP896MJ",
    # "force": True,
    # "licensingIntent": "OneView",
    # "configurationState": "Managed",
    # "deployment_network": "esx-200",
    # "os": ESXi67,
    # "profile": "ProfileR2_U15"
    # },
    # rack u #16
    # {
    # "hostname": "10.177.12.179",
    # "username": "Administrator",
    # "password": "BSS8YJ2P",
    # "force": True,
    # "licensingIntent": "OneView",
    # "configurationState": "Managed",
    # "deployment_network": "esx-200",
    # "os": ESXi67,
    # "profile": "ProfileR2_U16"
    # },
    # rack u #17
    # {
    # "hostname": "10.177.12.181",
    # "username": "Administrator",
    # "password": "2WLMMLMY",
    # "force": True,
    # "licensingIntent": "OneView",
    # "configurationState": "Managed",
    # "deployment_network": "esx-200",
    # "os": ESXi67,
    # "profile": "ProfileR2_U17"
    # },
    # rack u #18
    # {
    # "hostname": "10.177.12.178",
    # "username": "Administrator",
    # "password": "N7WQ5XPY",
    # "force": True,
    # "licensingIntent": "OneView",
    # "configurationState": "Managed",
    # "deployment_network": "esx-200",
    # "os": ESXi67,
    # "profile": "ProfileR2_U18"
    # },
    # rack u #19
    # {
    # "hostname": "10.177.12.177",
    # "username": "Administrator",
    # "password": "ZN826HPN",
    # "force": True,
    # "licensingIntent": "OneView",
    # "configurationState": "Managed",
    # "deployment_network": "esx-200",
    # "os": ESXi67,
    # "profile": "ProfileR2_U19"
    # },
    # rack u #20
    # {
    # "hostname": "10.177.12.180",
    # "username": "Administrator",
    # "password": "T7Q586GN",
    # "force": True,
    # "licensingIntent": "OneView",
    # "configurationState": "Managed",
    # "deployment_network": "esx-200",
    # "os": ESXi67,
    # "profile": "ProfileR2_U20"
    # },
    # rack u #21
    # {
    # "hostname": "10.177.12.176",
    # "username": "Administrator",
    # "password": "X7YVY2NZ",
    # "force": True,
    # "licensingIntent": "OneView",
    # "configurationState": "Managed",
    # "deployment_network": "esx-200",
    # "os": ESXi67,
    # "profile": "ProfileR2_U21"
    # },
    # rack u #22
    # {
    # "hostname": "10.177.12.175",
    # "username": "Administrator",
    # "password": "5C9VPMQJ",
    # "force": True,
    # "licensingIntent": "OneView",
    # "configurationState": "Managed",
    # "deployment_network": "esx-200",
    # "os": ESXi67,
    # "profile": "ProfileR2_U22"
    # },
    # rack u #23
    # {
    # "hostname": "10.177.12.174",
    # "username": "Administrator",
    # "password": "X2KXMYQM",
    # "force": True,
    # "licensingIntent": "OneView",
    # "configurationState": "Managed",
    # "deployment_network": "esx-200",
    # "os": ESXi67,
    # "profile": "ProfileR2_U23"
    # },
]

server_hardware_Vader3 = [
    # Vader3
    # rack u1
    {
        "hostname": "10.177.12.131",
        "username": "Administrator",
        "password": "9S68WGDJ",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR3_U1"
    },
    # rack u2
    {
        "hostname": "10.177.12.84",
        "username": "Administrator",
        "password": "QBSRF9GH",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR3_U2"
    },
    # rack u3
    {
        "hostname": "10.177.12.129",
        "username": "Administrator",
        "password": "L8Z9X6KH",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR3_U3"
    },
    # rack u4
    {
        "hostname": "10.177.12.110",
        "username": "Administrator",
        "password": "MJQL8W8T",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR3_U4"
    },
    # rack u5
    {
        "hostname": "10.177.12.133",
        "username": "Administrator",
        "password": "LMSFNX79",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR3_U5"
    },
    # rack u6
    {
        "hostname": "10.177.12.122",
        "username": "Administrator",
        "password": "TMTX7NR6",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR3_U6"
    },
    # rack u7
    {
        "hostname": "10.177.12.136",
        "username": "Administrator",
        "password": "SVJF8BN2",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR3_U7"
    },
    # rack u8
    {
        "hostname": "10.177.12.53",
        "username": "Administrator",
        "password": "LD25PPJD",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR3_U8"
    },
    # rack u9
    {
        "hostname": "10.177.12.126",
        "username": "Administrator",
        "password": "22FRSPD7",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR3_U9"
    },
    # rack u10
    {
        "hostname": "10.177.12.118",
        "username": "Administrator",
        "password": "ZBFZZ9HW",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR3_U10"
    },
    # rack u11
    {
        "hostname": "10.177.12.121",
        "username": "Administrator",
        "password": "6PX2N9CV",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-400",
        "os": ESXi67,
        "profile": "ProfileR3_U11"
    },
    # rack u12
    {
        "hostname": "10.177.12.119",
        "username": "Administrator",
        "password": "BC85LJZS",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-400",
        "os": ESXi67,
        "profile": "ProfileR3_U12"
    },
    # rack u13
    {
        "hostname": "10.177.12.132",
        "username": "Administrator",
        "password": "W7XTXW2Y",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-400",
        "os": ESXi67,
        "profile": "ProfileR3_U13"
    },
    # rack u14
    {
        "hostname": "10.177.12.128",
        "username": "Administrator",
        "password": "8LXX6S8J",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-400",
        "os": ESXi67,
        "profile": "ProfileR3_U14"
    },
    # rack u15
    {
        "hostname": "10.177.12.134",
        "username": "Administrator",
        "password": "9JZBKXMK",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-400",
        "os": ESXi67,
        "profile": "ProfileR3_U15"
    },
    # rack u16
    {
        "hostname": "10.177.12.120",
        "username": "Administrator",
        "password": "KV9D7CRM",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-400",
        "os": ESXi67,
        "profile": "ProfileR3_U16"
    },
    # rack u17
    {
        "hostname": "10.177.12.123",
        "username": "Administrator",
        "password": "HNQKPRM7",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-400",
        "os": ESXi67,
        "profile": "ProfileR3_U17"
    },
    # rack u18
    {
        "hostname": "10.177.12.124",
        "username": "Administrator",
        "password": "YSMHZD2H",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-400",
        "os": ESXi67,
        "profile": "ProfileR3_U18"
    },
    # rack u19
    # {
    # "hostname": "10.177.12.130",
    # "username": "Administrator",
    # "password": "2VDYR9ZX",
    # "force": True,
    # "licensingIntent": "OneView",
    # "configurationState": "Managed",
    # "deployment_network": "esx-400",
    # "os": ESXi67,
    # "profile": "ProfileR3_U19"
    # },
    # rack u20
    # {
    # "hostname": "10.177.12.135",
    # "username": "Administrator",
    # "password": "C2NW8PLF",
    # "force": True,
    # "licensingIntent": "OneView",
    # "configurationState": "Managed",
    # "deployment_network": "esx-400",
    # "os": ESXi67,
    # "profile": "ProfileR3_U20"
    # },
    # rack u21
    # {
    # "hostname": "10.177.12.101",
    # "username": "Administrator",
    # "password": "2DYMSVJ9",
    # "force": True,
    # "licensingIntent": "OneView",
    # "configurationState": "Managed",
    # "deployment_network": "linux-trunk-4k",
    # "os": RHEL75,
    # "profile": "ProfileR3_U21"
    # },
    # rack u22
    # {
    # "hostname": "10.177.12.125",
    # "username": "Administrator",
    # "password": "NDX8L5FZ",
    # "force": True,
    # "licensingIntent": "OneView",
    # "configurationState": "Managed",
    # "deployment_network": "linux-trunk-4k",
    # "os": RHEL75,
    # "profile": "ProfileR3_U22"
    # },
    # rack u23
    # {
    # "hostname": "10.177.12.127",
    # "username": "Administrator",
    # "password": "LWH2K2DS",
    # "force": True,
    # "licensingIntent": "OneView",
    # "configurationState": "Managed",
    # "deployment_network": "linux-trunk-4k",
    # "os": RHEL75,
    # "profile": "ProfileR3_U23"
    # },
]

server_hardware_Vader4 = [
    # rack u1
    {
        "hostname": "10.177.12.108",
        "username": "Administrator",
        "password": "QD58CMDN",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR4_U1"
    },
    # rack u2
    {
        "hostname": "10.177.12.107",
        "username": "Administrator",
        "password": "2K969LWC",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR4_U2"
    },
    # rack u3
    {
        "hostname": "10.177.12.106",
        "username": "Administrator",
        "password": "9RZLPHPZ",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR4_U3"
    },
    # rack u4
    {
        "hostname": "10.177.12.105",
        "username": "Administrator",
        "password": "Q8C6P76Z",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR4_U4"
    },
    # rack u5
    {
        "hostname": "10.177.12.104",
        "username": "Administrator",
        "password": "G69JZXM7",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR4_U5"
    },
    # rack u6
    {
        "hostname": "10.177.12.103",
        "username": "Administrator",
        "password": "C89T7CYL",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR4_U6"
    },
    # rack u7
    {
        "hostname": "10.177.12.102",
        "username": "Administrator",
        "password": "LQP8M75V",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR4_U7"
    },
    # rack u8
    {
        "hostname": "10.177.12.117",
        "username": "Administrator",
        "password": "F7Q9CCRX",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR4_U8"
    },
    # rack u9
    {
        "hostname": "10.177.12.100",
        "username": "Administrator",
        "password": "7VSYXWND",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR4_U9"
    },
    # rack u10
    {
        "hostname": "10.177.12.99",
        "username": "Administrator",
        "password": "2WY5JM2M",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR4_U10"
    },
    # rack u11
    {
        "hostname": "10.177.12.98",
        "username": "Administrator",
        "password": "NYTCD68H",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR4_U11"
    },
    # rack u12
    {
        "hostname": "10.177.12.97",
        "username": "Administrator",
        "password": "NV7L8LRD",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-400",
        "os": ESXi67,
        "profile": "ProfileR4_U12"
    },
    # rack u13
    {
        "hostname": "10.177.12.96",
        "username": "Administrator",
        "password": "SW2LVQPR",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-400",
        "os": ESXi67,
        "profile": "ProfileR4_U13"
    },
    # rack u14
    {
        "hostname": "10.177.12.95",
        "username": "Administrator",
        "password": "5SPRGM77",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-400",
        "os": ESXi67,
        "profile": "ProfileR4_U14"
    },
    # rack u15
    {
        "hostname": "10.177.12.94",
        "username": "Administrator",
        "password": "5SKB2RGW",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-400",
        "os": ESXi67,
        "profile": "ProfileR4_U15"
    },
    # rack u16
    {
        "hostname": "10.177.12.93",
        "username": "Administrator",
        "password": "CB7SGFRD",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-400",
        "os": ESXi67,
        "profile": "ProfileR4_U16"
    },
    # rack u17
    {
        "hostname": "10.177.12.92",
        "username": "Administrator",
        "password": "SH89BJCC",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-400",
        "os": ESXi67,
        "profile": "ProfileR4_U17"
    },
    # rack u18
    {
        "hostname": "10.177.12.91",
        "username": "Administrator",
        "password": "RZ2VQFBX",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-400",
        "os": ESXi67,
        "profile": "ProfileR4_U17"
    },
    # rack u19
    {
        "hostname": "10.177.12.90",
        "username": "Administrator",
        "password": "XGND2BN9",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-400",
        "os": ESXi67,
        "profile": "ProfileR4_U19"
    },
    # rack u20
    {
        "hostname": "10.177.12.89",
        "username": "Administrator",
        "password": "MQG5VPH5",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-400",
        "os": ESXi67,
        "profile": "ProfileR4_U20"
    },
    # rack u21
    {
        "hostname": "10.177.12.88",
        "username": "Administrator",
        "password": "TWJS7TVB",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-400",
        "os": ESXi67,
        "profile": "ProfileR4_U21"
    },
    # rack u22
    {
        "hostname": "10.177.12.87",
        "username": "Administrator",
        "password": "LCTQK22V",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR4_U22"
    },
    # rack u23
    {
        "hostname": "10.177.12.86",
        "username": "Administrator",
        "password": "Q6NNF8Y2",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR4_U23"
    },
    # rack u24
    {
        "hostname": "10.177.12.85",
        "username": "Administrator",
        "password": "Q5999LKF",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR4_U24"
    },
    # rack u25
    {
        "hostname": "10.177.12.112",
        "username": "Administrator",
        "password": "JSCLXB8C",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR4_U25"
    },
    # rack u26
    {
        "hostname": "10.177.12.83",
        "username": "Administrator",
        "password": "NNTFWQ2X",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR4_U26"
    },
    # rack u27
    {
        "hostname": "10.177.12.82",
        "username": "Administrator",
        "password": "VNN6Q5M9",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR4_U27"
    },
    # rack u28
    {
        "hostname": "10.177.12.81",
        "username": "Administrator",
        "password": "66XQMX2F",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR4_U28"
    },
    # rack u29
    {
        "hostname": "10.177.12.80",
        "username": "Administrator",
        "password": "T5R9CXXS",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR4_U29"
    },
    # rack u30
    {
        "hostname": "10.177.12.79",
        "username": "Administrator",
        "password": "DF8FWKSS",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR4_U30"
    },
    # rack u31
    {
        "hostname": "10.177.12.78",
        "username": "Administrator",
        "password": "YJ6RMY2X",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR4_U31"
    },
    # rack u32
    {
        "hostname": "10.177.12.77",
        "username": "Administrator",
        "password": "LD25HXQ5",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR4_U32"
    },
    # rack u33
    {
        "hostname": "10.177.12.76",
        "username": "Administrator",
        "password": "TFQQHDS6",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR4_U33"
    },
    # rack u34
    {
        "hostname": "10.177.12.75",
        "username": "Administrator",
        "password": "CPYH9GKY",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR4_U34"
    },
    # rack u35
    {
        "hostname": "10.177.12.74",
        "username": "Administrator",
        "password": "KTWCHNM8",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR4_U35"
    },
    # rack u36
    {
        "hostname": "10.177.12.73",
        "username": "Administrator",
        "password": "LZ8XBXMG",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "linux-trunk-4k",
        "os": RHEL75,
        "profile": "ProfileR4_U36"
    },
    # rack u37
    {
        "hostname": "10.177.12.114",
        "username": "Administrator",
        "password": "LY6DCQT2",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "linux-trunk-4k",
        "os": RHEL75,
        "profile": "ProfileR4_U37"
    },
    # rack u38
    {
        "hostname": "10.177.12.116",
        "username": "Administrator",
        "password": "SNCYMFH9",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "linux-trunk-1k-a",
        "os": RHEL75,
        "profile": "ProfileR4_U38"
    },
    # rack u39
    {
        "hostname": "10.177.12.115",
        "username": "Administrator",
        "password": "RNC2HCNL",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "linux-trunk-1k-a",
        "os": RHEL75,
        "profile": "ProfileR4_U39"
    },
]

server_hardware_Vader5 = [
    # rack u1
    {
        "hostname": "10.177.12.72",
        "username": "Administrator",
        "password": "C2R9S29G",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR5_U1"
    },
    # rack u2
    {
        "hostname": "10.177.12.71",
        "username": "Administrator",
        "password": "WLSJ2SGM",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR5_U2"
    },
    # rack u3
    {
        "hostname": "10.177.12.70",
        "username": "Administrator",
        "password": "6RSRSFJP",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR5_U3"
    },
    # rack u4
    {
        "hostname": "10.177.12.69",
        "username": "Administrator",
        "password": "7M22WVK5",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR5_U4"
    },
    # rack u5
    {
        "hostname": "10.177.12.68",
        "username": "Administrator",
        "password": "TFG58R2H",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR5_U5"
    },
    # rack u6
    {
        "hostname": "10.177.12.67",
        "username": "Administrator",
        "password": "9ZTYCFZ9",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR5_U6"
    },
    # rack u7
    {
        "hostname": "10.177.12.66",
        "username": "Administrator",
        "password": "SWP8DBC7",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR5_U7"
    },
    # rack u8
    {
        "hostname": "10.177.12.65",
        "username": "Administrator",
        "password": "GKRRL96R",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR5_U8"
    },
    # rack u9
    {
        "hostname": "10.177.12.64",
        "username": "Administrator",
        "password": "CQMM5L7M",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR5_U9"
    },
    # rack u10
    {
        "hostname": "10.177.12.63",
        "username": "Administrator",
        "password": "5BR6J2P5",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR5_U10"
    },
    # rack u11
    {
        "hostname": "10.177.12.62",
        "username": "Administrator",
        "password": "52JGGPC5",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR5_U11"
    },
    # rack u12
    {
        "hostname": "10.177.12.61",
        "username": "Administrator",
        "password": "WPWVCM2P",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-400",
        "os": ESXi67,
        "profile": "ProfileR5_U12"
    },
    # rack u13
    {
        "hostname": "10.177.12.60",
        "username": "Administrator",
        "password": "MXWKYMT8",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-400",
        "os": ESXi67,
        "profile": "ProfileR5_U13"
    },
    # rack u14
    {
        "hostname": "10.177.12.59",
        "username": "Administrator",
        "password": "BPWMSM2N",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-400",
        "os": ESXi67,
        "profile": "ProfileR5_U14"
    },
    # rack u15
    {
        "hostname": "10.177.12.58",
        "username": "Administrator",
        "password": "7ZZXJL2W",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-400",
        "os": ESXi67,
        "profile": "ProfileR5_U15"
    },
    # rack u16
    {
        "hostname": "10.177.12.57",
        "username": "Administrator",
        "password": "WH8BRL6S",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-400",
        "os": ESXi67,
        "profile": "ProfileR5_U16"
    },
    # rack u17
    {
        "hostname": "10.177.12.56",
        "username": "Administrator",
        "password": "ZK5HK87B",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-400",
        "os": ESXi67,
        "profile": "ProfileR5_U17"
    },
    # rack u18
    {
        "hostname": "10.177.12.55",
        "username": "Administrator",
        "password": "66JPGZXD",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-400",
        "os": ESXi67,
        "profile": "ProfileR5_U18"
    },
    # rack u19
    {
        "hostname": "10.177.12.54",
        "username": "Administrator",
        "password": "L9WSZDBH",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-400",
        "os": ESXi67,
        "profile": "ProfileR5_U19"
    },
    # rack u20
    {
        "hostname": "10.177.12.37",
        "username": "Administrator",
        "password": "PZ77HMV7",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-400",
        "os": ESXi67,
        "profile": "ProfileR5_U20"
    },
    # rack u21
    {
        "hostname": "10.177.12.52",
        "username": "Administrator",
        "password": "XGL6QSN2",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-400",
        "os": ESXi67,
        "profile": "ProfileR5_U21"
    },
    # rack u22
    {
        "hostname": "10.177.12.51",
        "username": "Administrator",
        "password": "S5K8Y7GQ",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-400",
        "os": ESXi67,
        "profile": "ProfileR5_U22"
    },
    # rack u23
    {
        "hostname": "10.177.12.50",
        "username": "Administrator",
        "password": "MXQ7VS2M",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR5_U23"
    },
    # rack u24
    {
        "hostname": "10.177.12.49",
        "username": "Administrator",
        "password": "BFYVF9ZD",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR5_U24"
    },
    # rack u25
    {
        "hostname": "10.177.12.48",
        "username": "Administrator",
        "password": "QTKCXC5R",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR5_U25"
    },
    # rack u26
    {
        "hostname": "10.177.12.47",
        "username": "Administrator",
        "password": "HCQ86YJQ",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR5_U26"
    },
    # rack u27
    {
        "hostname": "10.177.12.46",
        "username": "Administrator",
        "password": "GQT6HRRH",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR5_U27"
    },
    # rack u28
    {
        "hostname": "10.177.12.45",
        "username": "Administrator",
        "password": "B6PJ99FK",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR5_U28"
    },
    # rack u29
    {
        "hostname": "10.177.12.44",
        "username": "Administrator",
        "password": "FPJK2J8N",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR5_U29"
    },
    # rack u30
    {
        "hostname": "10.177.12.43",
        "username": "Administrator",
        "password": "H759PVDY",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR5_U30"
    },
    # rack u31
    {
        "hostname": "10.177.12.42",
        "username": "Administrator",
        "password": "V9MCHYYD",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR5_U31"
    },
    # rack u32
    {
        "hostname": "10.177.12.41",
        "username": "Administrator",
        "password": "GFQVZHS7",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "linux-trunk-4k",
        "os": RHEL75,
        "profile": "ProfileR5_U32"
    },
    # rack u33
    {
        "hostname": "10.177.12.40",
        "username": "Administrator",
        "password": "6WGXN726",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "linux-trunk-4k",
        "os": RHEL75,
        "profile": "ProfileR5_U33"
    },
    # rack u34
    {
        "hostname": "10.177.12.109",
        "username": "Administrator",
        "password": "GQNX8NSR",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "linux-trunk-4k",
        "os": RHEL75,
        "profile": "ProfileR5_U34"
    },
    # rack u35
    {
        "hostname": "10.177.12.39",
        "username": "Administrator",
        "password": "S2GRNFKP",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "linux-trunk-4k",
        "os": RHEL75,
        "profile": "ProfileR5_U35"
    },
    # rack u36
    {
        "hostname": "10.177.12.38",
        "username": "Administrator",
        "password": "6FT7KV5H",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "linux-trunk-1k-a",
        "os": RHEL75,
        "profile": "ProfileR5_U36"
    },
    # rack u37
    {
        "hostname": "10.177.12.111",
        "username": "Administrator",
        "password": "5227DJB5",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "linux-trunk-1k-a",
        "os": RHEL75,
        "profile": "ProfileR5_U37"
    },
    # rack u38
    {
        "hostname": "10.177.12.113",
        "username": "Administrator",
        "password": "F5DJ6S7D",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "linux-trunk-1k-a",
        "os": RHEL75,
        "profile": "ProfileR5_U38"
    },
]

server_hardware_Vader6 = [
    # rack u1
    {
        "hostname": "10.177.12.36",
        "username": "Administrator",
        "password": "PB9Y8FXJ",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR6_U1"
    },
    # rack u2
    {
        "hostname": "10.177.12.35",
        "username": "Administrator",
        "password": "X5NB6HQ5",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR6_U2"
    },
    # rack u3
    {
        "hostname": "10.177.12.34",
        "username": "Administrator",
        "password": "YNLL8JQY",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR6_U3"
    },
    # rack u4
    {
        "hostname": "10.177.12.33",
        "username": "Administrator",
        "password": "XSHH7DH2",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR6_U4"
    },
    # rack u5
    {
        "hostname": "10.177.12.32",
        "username": "Administrator",
        "password": "2QCQL2WW",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR6_U5"
    },
    # rack u6
    {
        "hostname": "10.177.12.31",
        "username": "Administrator",
        "password": "NZR9SWTB",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR6_U6"
    },
    # rack u7
    {
        "hostname": "10.177.12.30",
        "username": "Administrator",
        "password": "95TB6SDW",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR6_U7"
    },
    # rack u8
    {
        "hostname": "10.177.12.29",
        "username": "Administrator",
        "password": "WNYRLMT9",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR6_U8"
    },
    # rack u9
    {
        "hostname": "10.177.12.28",
        "username": "Administrator",
        "password": "LBPCD5VR",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR6_U9"
    },
    # rack u10
    {
        "hostname": "10.177.12.27",
        "username": "Administrator",
        "password": "8ZY72BQB",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR6_U10"
    },
    # rack u11
    {
        "hostname": "10.177.12.26",
        "username": "Administrator",
        "password": "NSJXRHT2",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-400",
        "os": ESXi67,
        "profile": "ProfileR6_U11"
    },
    # rack u12
    {
        "hostname": "10.177.12.25",
        "username": "Administrator",
        "password": "8LQLHRNN",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-400",
        "os": ESXi67,
        "profile": "ProfileR6_U12"
    },
    # rack u13
    {
        "hostname": "10.177.12.24",
        "username": "Administrator",
        "password": "GLQPZ8M8",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-400",
        "os": ESXi67,
        "profile": "ProfileR6_U13"
    },
    # rack u14
    {
        "hostname": "10.177.12.23",
        "username": "Administrator",
        "password": "SJZ62G87",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-400",
        "os": ESXi67,
        "profile": "ProfileR6_U14"
    },
    # rack u15
    {
        "hostname": "10.177.12.22",
        "username": "Administrator",
        "password": "HRN89D2C",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-400",
        "os": ESXi67,
        "profile": "ProfileR6_U15"
    },
    # rack u16
    {
        "hostname": "10.177.12.21",
        "username": "Administrator",
        "password": "2796QHTN",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-400",
        "os": ESXi67,
        "profile": "ProfileR6_U16"
    },
    # rack u17
    {
        "hostname": "10.177.12.20",
        "username": "Administrator",
        "password": "Y9X2T6QZ",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-400",
        "os": ESXi67,
        "profile": "ProfileR6_U17"
    },
    # rack u18
    {
        "hostname": "10.177.12.19",
        "username": "Administrator",
        "password": "LY6XKQL8",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-400",
        "os": ESXi67,
        "profile": "ProfileR6_U18"
    },
    # rack u19
    {
        "hostname": "10.177.12.18",
        "username": "Administrator",
        "password": "YFS76F9C",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-400",
        "os": ESXi67,
        "profile": "ProfileR6_U19"
    },
    # rack u20
    {
        "hostname": "10.177.12.17",
        "username": "Administrator",
        "password": "8HWMSRC2",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-400",
        "os": ESXi67,
        "profile": "ProfileR6_U20"
    },
    # rack u21
    {
        "hostname": "10.177.12.16",
        "username": "Administrator",
        "password": "BMD9C7LH",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-400",
        "os": ESXi67,
        "profile": "ProfileR6_U21"
    },
    # rack u22
    {
        "hostname": "10.177.12.15",
        "username": "Administrator",
        "password": "8NQK82M2",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR6_U22"
    },
    # rack u23
    {
        "hostname": "10.177.12.14",
        "username": "Administrator",
        "password": "966KBS2M",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR6_U23"
    },
    # rack u24
    {
        "hostname": "10.177.12.13",
        "username": "Administrator",
        "password": "GZR6V92B",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR6_U24"
    },
    # rack u25
    {
        "hostname": "10.177.12.12",
        "username": "Administrator",
        "password": "QVT9QTTT",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR6_U25"
    },
    # rack u26
    {
        "hostname": "10.177.12.11",
        "username": "Administrator",
        "password": "9DX82P2V",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR6_U26"
    },
    # rack u27
    {
        "hostname": "10.177.12.10",
        "username": "Administrator",
        "password": "DTXWYNC8",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR6_U27"
    },
    # rack u28
    {
        "hostname": "10.177.12.9",
        "username": "Administrator",
        "password": "7J8MCQNX",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR6_U28"
    },
    # rack u29
    {
        "hostname": "10.177.12.7",
        "username": "Administrator",
        "password": "PNQ2LVFC",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR6_U29"
    },
    # rack u30
    {
        "hostname": "10.177.12.6",
        "username": "Administrator",
        "password": "NW5FHQDC",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "esx-200",
        "os": ESXi67,
        "profile": "ProfileR6_U30"
    },
    # rack u31
    {
        "hostname": "10.177.12.8",
        "username": "Administrator",
        "password": "XD88QKH9",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "linux-trunk-4k",
        "os": RHEL75,
        "profile": "ProfileR6_U31"
    },
    # rack u32
    {
        "hostname": "10.177.12.5",
        "username": "Administrator",
        "password": "XHBF7C7X",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "linux-trunk-4k",
        "os": RHEL75,
        "profile": "ProfileR6_U32"
    },
    # rack u33
    {
        "hostname": "10.177.12.4",
        "username": "Administrator",
        "password": "KVKFTR9Y",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "linux-trunk-4k",
        "os": RHEL75,
        "profile": "ProfileR6_U33"
    },
    # rack u34
    {
        "hostname": "10.177.12.3",
        "username": "Administrator",
        "password": "6GLXPFQ2",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "linux-trunk-1k-a",
        "os": RHEL75,
        "profile": "ProfileR6_U34"
    },
    # rack u35
    {
        "hostname": "10.177.12.2",
        "username": "Administrator",
        "password": "FWYKD2KL",
        "force": True,
        "licensingIntent": "OneView",
        "configurationState": "Managed",
        "deployment_network": "linux-trunk-1k-a",
        "os": RHEL75,
        "profile": "ProfileR6_U35"
    },
]

server_hardware_cpt = server_hardware_Vader1 + server_hardware_Vader2 + \
    server_hardware_Vader3 + server_hardware_Vader4 + \
    server_hardware_Vader5 + server_hardware_Vader6
server_hardware = clean_server_hardware(server_hardware_cpt)

#####################
# DL Server Profiles section
#####################
server_profile_to_bay_map = {
    # Vader1
    'ProfileR1_U1': 'ILOMXQ90502G1.dom1177.lab',
    'ProfileR1_U2': 'ILOMXQ90502G4.dom1177.lab',
    'ProfileR1_U3': 'ILOMXQ90502G7.dom1177.lab',
    'ProfileR1_U4': 'ILOMXQ90502GL.dom1177.lab',
    'ProfileR1_U5': 'ILOMXQ90502G0.dom1177.lab',
    'ProfileR1_U6': 'ILOMXQ90502GJ.dom1177.lab',
    'ProfileR1_U7': 'ILOMXQ90502GM.dom1177.lab',
    'ProfileR1_U8': 'ILOMXQ90502GH.dom1177.lab',
    'ProfileR1_U9': 'ILOMXQ90502H3.dom1177.lab',
    'ProfileR1_U10': 'ILOMXQ90502GG.dom1177.lab',
    'ProfileR1_U11': 'ILOMXQ90501XQ.dom1177.lab',
    'ProfileR1_U12': 'ILOMXQ90501XR.dom1177.lab',
    'ProfileR1_U13': 'ILOMXQ90501XN.dom1177.lab',
    'ProfileR1_U14': 'ILOMXQ90501XS.dom1177.lab',
    'ProfileR1_U15': 'ILOMXQ90501XT.dom1177.lab',
    'ProfileR1_U16': 'ILOMXQ90501XM.dom1177.lab',
    'ProfileR1_U17': 'ILOMXQ90501XX.dom1177.lab',
    'ProfileR1_U18': 'ILOMXQ90501XW.dom1177.lab',
    'ProfileR1_U19': 'ILOMXQ90501XZ.dom1177.lab',
    'ProfileR1_U20': 'ILOMXQ90501XY.dom1177.lab',
    # Vader2
    'ProfileR2_U1': 'ILOMXQ90501YR.dom1177.lab',
    'ProfileR2_U2': 'ILOMXQ90501YH.dom1177.lab',
    'ProfileR2_U3': 'ILOMXQ90501XB.dom1177.lab',
    'ProfileR2_U4': 'ILOMXQ90501YG.dom1177.lab',
    'ProfileR2_U5': 'ILOMXQ90501YF.dom1177.lab',
    'ProfileR2_U6': 'ILOMXQ90501XD.dom1177.lab',
    # 'ProfileR2_U7':'ILOMXQ90501XK.dom1177.lab',
    # 'ProfileR2_U8':'ILOMXQ90501XJ.dom1177.lab',
    # 'ProfileR2_U9':'ILOMXQ90501XH.dom1177.lab',
    # 'ProfileR2_U10':'ILOMXQ90501XG.dom1177.lab',
    # 'ProfileR2_U11':'ILOMXQ90701GS.dom1177.lab',
    # 'ProfileR2_U12':'ILOMXQ90701GV.dom1177.lab',
    # 'ProfileR2_U13':'ILOMXQ90701GP.dom1177.lab',
    # 'ProfileR2_U14':'ILOMXQ90701H9.dom1177.lab',
    # 'ProfileR2_U15':'ILOMXQ90701J0.dom1177.lab',
    # 'ProfileR2_U16':'ILOMXQ90701H5.dom1177.lab',
    # 'ProfileR2_U17':'ILOMXQ90701J2.dom1177.lab',
    # 'ProfileR2_U18':'ILOMXQ90701H8.dom1177.lab',
    # 'ProfileR2_U19':'ILOMXQ90701H7.dom1177.lab',
    # 'ProfileR2_U20':'ILOMXQ90701H6.dom1177.lab',
    # 'ProfileR2_U21':'ILOMXQ90701J1.dom1177.lab',
    # 'ProfileR2_U22':'ILOMXQ90701H2.dom1177.lab',
    # 'ProfileR2_U23':'ILOMXQ90701GY.dom1177.lab',
    # Vader3
    'ProfileR3_U1': 'ILOMXQ9050101.dom1177.lab',
    'ProfileR3_U2': 'ILOMXQ905010F.dom1177.lab',
    'ProfileR3_U3': 'ILOMXQ905010L.dom1177.lab',
    'ProfileR3_U4': 'ILOMXQ9050108.dom1177.lab',
    'ProfileR3_U5': 'ILOMXQ905010J.dom1177.lab',
    'ProfileR3_U6': 'ILOMXQ905010G.dom1177.lab',
    'ProfileR3_U7': 'ILOMXQ9050105.dom1177.lab',
    'ProfileR3_U8': 'ILOMXQ905010M.dom1177.lab',
    'ProfileR3_U9': 'ILOMXQ905010N.dom1177.lab',
    'ProfileR3_U10': 'ILOMXQ905010C.dom1177.lab',
    'ProfileR3_U11': 'ILOMXQ905010B.dom1177.lab',
    'ProfileR3_U12': 'ILOMXQ9050102.dom1177.lab',
    'ProfileR3_U13': 'ILOMXQ905010H.dom1177.lab',
    'ProfileR3_U14': 'ILOMXQ9050103.dom1177.lab',
    'ProfileR3_U15': 'ILOMXQ905010K.dom1177.lab',
    'ProfileR3_U16': 'ILOMXQ905010D.dom1177.lab',
    'ProfileR3_U17': 'ILOMXQ9050109.dom1177.lab',
    'ProfileR3_U18': 'ILOMXQ9050107.dom1177.lab',
    # 'ProfileR3_U19':'ILOMXQ9050104.dom1177.lab',
    # 'ProfileR3_U20':'ILOMXQ9050106.dom1177.lab',
    # 'ProfileR3_U21':'ILOMXQ90502GW.dom1177.lab',
    # 'ProfileR3_U22':'ILOMXQ90501F1.dom1177.lab',
    # 'ProfileR3_U23':'ILOMXQ90501FK.dom1177.lab',
    # Vader4
    'ProfileR4_U39': 'ILOMXQ90701G8.dom1177.lab',
    'ProfileR4_U38': 'ILOMXQ90701G6.dom1177.lab',
    'ProfileR4_U37': 'ILOMXQ90701G7.dom1177.lab',
    'ProfileR4_U36': 'ILOMXQ90501FG.dom1177.lab',
    'ProfileR4_U35': 'ILOMXQ90501FC.dom1177.lab',
    'ProfileR4_U34': 'ILOMXQ90501FD.dom1177.lab',
    'ProfileR4_U33': 'ILOMXQ90501F4.dom1177.lab',
    'ProfileR4_U32': 'ILOMXQ90501FB.dom1177.lab',
    'ProfileR4_U31': 'ILOMXQ90501F9.dom1177.lab',
    'ProfileR4_U30': 'ILOMXQ90501FH.dom1177.lab',
    'ProfileR4_U29': 'ILOMXQ90501FJ.dom1177.lab',
    'ProfileR4_U28': 'ILOMXQ90501X1.dom1177.lab',
    'ProfileR4_U27': 'ILOMXQ90501X5.dom1177.lab',
    'ProfileR4_U26': 'ILOMXQ90501X7.dom1177.lab',
    'ProfileR4_U25': 'ILOMXQ90501X4.dom1177.lab',
    'ProfileR4_U24': 'ILOMXQ90501X8.dom1177.lab',
    'ProfileR4_U23': 'ILOMXQ90501XV.dom1177.lab',
    'ProfileR4_U22': 'ILOMXQ90501Y0.dom1177.lab',
    'ProfileR4_U21': 'ILOMXQ90501Y1.dom1177.lab',
    'ProfileR4_U20': 'ILOMXQ90501Y2.dom1177.lab',
    'ProfileR4_U19': 'ILOMXQ90501X9.dom1177.lab',
    'ProfileR4_U18': 'ILOMXQ90502G6.dom1177.lab',
    'ProfileR4_U17': 'ILOMXQ90502FY.dom1177.lab',
    'ProfileR4_U16': 'ILOMXQ90502FX.dom1177.lab',
    'ProfileR4_U15': 'ILOMXQ90501XP.dom1177.lab',
    'ProfileR4_U14': 'ILOMXQ90502G3.dom1177.lab',
    'ProfileR4_U13': 'ILOMXQ90501WX.dom1177.lab',
    'ProfileR4_U12': 'ILOMXQ90502QH.dom1177.lab',
    'ProfileR4_U11': 'ILOMXQ90502QQ.dom1177.lab',
    'ProfileR4_U10': 'ILOMXQ90502G2.dom1177.lab',
    'ProfileR4_U9': 'ILOMXQ90502QP.dom1177.lab',
    'ProfileR4_U8': 'ILOMXQ90502QM.dom1177.lab',
    'ProfileR4_U7': 'ILOMXQ90502QN.dom1177.lab',
    'ProfileR4_U6': 'ILOMXQ90502QL.dom1177.lab',
    'ProfileR4_U5': 'ILOMXQ90502QS.dom1177.lab',
    'ProfileR4_U4': 'ILOMXQ90502QZ.dom1177.lab',
    'ProfileR4_U3': 'ILOMXQ90502QR.dom1177.lab',
    'ProfileR4_U2': 'ILOMXQ90501X6.dom1177.lab',
    'ProfileR4_U1': 'ILOMXQ90502GK.dom1177.lab',
    # Vader5
    'ProfileR5_U38': 'ILOMXQ91001TS.dom1177.lab',
    'ProfileR5_U37': 'ILOMXQ90701GB.dom1177.lab',
    'ProfileR5_U36': 'ILOMXQ90501Y4.dom1177.lab',
    'ProfileR5_U35': 'ILOMXQ90502GP.dom1177.lab',
    'ProfileR5_U34': 'ILOMXQ90501FL.dom1177.lab',
    'ProfileR5_U33': 'ILOMXQ90501F2.dom1177.lab',
    'ProfileR5_U32': 'ILOMXQ90501F8.dom1177.lab',
    'ProfileR5_U31': 'ILOMXQ90501FM.dom1177.lab',
    'ProfileR5_U30': 'ILOMXQ90501F7.dom1177.lab',
    'ProfileR5_U29': 'ILOMXQ90501F3.dom1177.lab',
    'ProfileR5_U28': 'ILOMXQ90501FF.dom1177.lab',
    'ProfileR5_U27': 'ILOMXQ90501F6.dom1177.lab',
    'ProfileR5_U26': 'ILOMXQ90501F5.dom1177.lab',
    'ProfileR5_U25': 'ILOMXQ90501F0.dom1177.lab',
    'ProfileR5_U24': 'ILOMXQ90502GR.dom1177.lab',
    'ProfileR5_U23': 'ILOMXQ90502GN.dom1177.lab',
    'ProfileR5_U22': 'ILOMXQ90502GX.dom1177.lab',
    'ProfileR5_U21': 'ILOMXQ90502GV.dom1177.lab',
    'ProfileR5_U20': 'ILOMXQ90502FQ.dom1177.lab',
    'ProfileR5_U19': 'ILOMXQ90502QY.dom1177.lab',
    'ProfileR5_U18': 'ILOMXQ90502FP.dom1177.lab',
    'ProfileR5_U17': 'ILOMXQ90502GD.dom1177.lab',
    'ProfileR5_U16': 'ILOMXQ90502G8.dom1177.lab',
    'ProfileR5_U15': 'ILOMXQ90502G5.dom1177.lab',
    'ProfileR5_U14': 'ILOMXQ90502GC.dom1177.lab',
    'ProfileR5_U13': 'ILOMXQ90502GB.dom1177.lab',
    'ProfileR5_U12': 'ILOMXQ90502G9.dom1177.lab',
    'ProfileR5_U11': 'ILOMXQ90502GF.dom1177.lab',
    'ProfileR5_U10': 'ILOMXQ90502QW.dom1177.lab',
    'ProfileR5_U9': 'ILOMXQ90502QT.dom1177.lab',
    'ProfileR5_U8': 'ILOMXQ90502QX.dom1177.lab',
    'ProfileR5_U7': 'ILOMXQ90502QV.dom1177.lab',
    'ProfileR5_U6': 'ILOMXQ90501Y3.dom1177.lab',
    'ProfileR5_U5': 'ILOMXQ90502QF.dom1177.lab',
    'ProfileR5_U4': 'ILOMXQ90502QK.dom1177.lab',
    'ProfileR5_U3': 'ILOMXQ90502R0.dom1177.lab',
    'ProfileR5_U2': 'ILOMXQ90502QJ.dom1177.lab',
    'ProfileR5_U1': 'ILOMXQ90502QG.dom1177.lab',
    # Vader6
    'ProfileR6_U35': 'ILOMXQ90502GQ.dom1177.lab',
    'ProfileR6_U34': 'ILOMXQ90502GS.dom1177.lab',
    'ProfileR6_U33': 'ILOMXQ90502GT.dom1177.lab',
    'ProfileR6_U32': 'ILOMXQ90502FV.dom1177.lab',
    'ProfileR6_U31': 'ILOMXQ90502FW.dom1177.lab',
    'ProfileR6_U30': 'ILOMXQ90501YL.dom1177.lab',
    'ProfileR6_U29': 'ILOMXQ90501YK.dom1177.lab',
    'ProfileR6_U28': 'ILOMXQ90501Y8.dom1177.lab',
    'ProfileR6_U27': 'ILOMXQ90501YB.dom1177.lab',
    'ProfileR6_U26': 'ILOMXQ90501Y7.dom1177.lab',
    'ProfileR6_U25': 'ILOMXQ90501YC.dom1177.lab',
    'ProfileR6_U24': 'ILOMXQ90501Y6.dom1177.lab',
    'ProfileR6_U23': 'ILOMXQ90501YD.dom1177.lab',
    'ProfileR6_U22': 'ILOMXQ90501Y5.dom1177.lab',
    'ProfileR6_U21': 'ILOMXQ90501Y9.dom1177.lab',
    'ProfileR6_U20': 'ILOMXQ90501WZ.dom1177.lab',
    'ProfileR6_U19': 'ILOMXQ90501YS.dom1177.lab',
    'ProfileR6_U18': 'ILOMXQ90501YP.dom1177.lab',
    'ProfileR6_U17': 'ILOMXQ90501YM.dom1177.lab',
    'ProfileR6_U16': 'ILOMXQ90501YN.dom1177.lab',
    'ProfileR6_U15': 'ILOMXQ90501X2.dom1177.lab',
    'ProfileR6_U14': 'ILOMXQ90501X0.dom1177.lab',
    'ProfileR6_U13': 'ILOMXQ90501WW.dom1177.lab',
    'ProfileR6_U12': 'ILOMXQ90501WY.dom1177.lab',
    'ProfileR6_U11': 'ILOMXQ90501XL.dom1177.lab',
    'ProfileR6_U10': 'ILOMXQ90502H1.dom1177.lab',
    'ProfileR6_U9': 'ILOMXQ90502FS.dom1177.lab',
    'ProfileR6_U8': 'ILOMXQ90502H2.dom1177.lab',
    'ProfileR6_U7': 'ILOMXQ90501YQ.dom1177.lab',
    'ProfileR6_U6': 'ILOMXQ90501XF.dom1177.lab',
    'ProfileR6_U5': 'ILOMXQ90502GY.dom1177.lab',
    'ProfileR6_U4': 'ILOMXQ90502GZ.dom1177.lab',
    'ProfileR6_U3': 'ILOMXQ90501XC.dom1177.lab',
    'ProfileR6_U2': 'ILOMXQ90502H0.dom1177.lab',
    'ProfileR6_U1': 'ILOMXQ90501X3.dom1177.lab',
}

# ESXI 631 with lag-200 network
server_profile_templates = [
    {
        'type': 'ServerProfileTemplateV7',
        'serverProfileDescription': 'ESXi DL360 Gen10 1 Profile',
        'serverHardwareTypeUri': 'SHT:DL360 Gen10 1',
        'enclosureGroupUri': '',
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': 'esx-lag-631',
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
                                    'networkUri': 'NS:esx-200',
                                    'ipv4': {},
                                    'lagName': 'LAG1'
                },
                {
                    'id': 2,
                    'name': 'c2',
                    'functionType': 'Ethernet',
                                    'portId': 'Flr 1:2',
                                    'requestedMbps': 0,
                                    'networkUri': 'NS:esx-200',
                                    'ipv4': {},
                                    'lagName': 'LAG1'
                }
            ],
            'manageConnections': True,
        },
        'boot': {'manageBoot': True,
                 'order': ['HardDisk']},
        'localStorage': {
            'sasLogicalJBODs': [],
            'controllers': []
        },
        'bootMode': {
            'manageMode': True,
            "mode": "BIOS",
            "pxeBootPolicy": None,
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
        'sanStorage': None,
        'osDeploymentSettings': None,
        'initialScopeUris': []
    },
    # ESXI-LAG 640 adaptor - 200 network
    {
        'type': 'ServerProfileTemplateV7',
        'serverProfileDescription': 'ESXi DL360 Gen10 1 Profile',
        'serverHardwareTypeUri': 'SHT:DL360 Gen10 1',
        'enclosureGroupUri': '',
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': 'esx-lag-640',
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
                                    'networkUri': 'NS:esx-200',
                                    'ipv4': {},
                                    'lagName': 'LAG1'
                },
                {
                    'id': 2,
                    'name': 'c2',
                    'functionType': 'Ethernet',
                                    'portId': 'Flr 1:2',
                                    'requestedMbps': 0,
                                    'networkUri': 'NS:esx-200',
                                    'ipv4': {},
                                    'lagName': 'LAG1'
                }
            ],
            'manageConnections': True,
        },
        'boot': {'manageBoot': True,
                 'order': ['CD', 'USB', 'HardDisk', 'PXE']},
        'localStorage': {
            'sasLogicalJBODs': [],
            'controllers': []
        },
        'bootMode': {
            'manageMode': True,
            "mode": "BIOS",
            "pxeBootPolicy": None,
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
        'sanStorage': None,
        'osDeploymentSettings': None,
        'initialScopeUris': []
    },

    # ESXi-Nolag-631-1000 network
    {
        'type': 'ServerProfileTemplateV7',
        'serverProfileDescription': 'ESXi DL360 Gen10 1 Profile',
        'serverHardwareTypeUri': 'SHT:DL360 Gen10 1',
        'enclosureGroupUri': '',
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': 'esx-631',
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
                                    'networkUri': 'NS:esx-400',
                                    'ipv4': {},
                },
                {
                    'id': 2,
                    'name': 'c2',
                    'functionType': 'Ethernet',
                                    'portId': 'Flr 1:2',
                                    'requestedMbps': 0,
                                    'networkUri': 'NS:esx-400',
                                    'ipv4': {},
                }
            ],
            'manageConnections': True,
        },
        'boot': {'manageBoot': True,
                 'order': ['CD', 'USB', 'HardDisk', 'PXE']},
        'localStorage': {
            'sasLogicalJBODs': [],
            'controllers': []
        },
        'bootMode': {
            'manageMode': True,
            "mode": "BIOS",
            "pxeBootPolicy": None,
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
        'sanStorage': None,
        'osDeploymentSettings': None,
        'initialScopeUris': []
    },
    #  ESXI 1000 adaptor 640 No lag
    {
        'type': 'ServerProfileTemplateV7',
        'serverProfileDescription': 'ESXi DL360 Gen10 1 Profile',
        'serverHardwareTypeUri': 'SHT:DL360 Gen10 1',
        'enclosureGroupUri': '',
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': 'esx-640',
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
                                    'networkUri': 'NS:esx-400',
                                    'ipv4': {},
                },
                {
                    'id': 2,
                    'name': 'c2',
                    'functionType': 'Ethernet',
                                    'portId': 'Flr 1:2',
                                    'requestedMbps': 0,
                                    'networkUri': 'NS:esx-400',
                                    'ipv4': {},
                }
            ],
            'manageConnections': True,
        },
        'boot': {'manageBoot': True,
                 'order': ['CD', 'USB', 'HardDisk', 'PXE']},
        'localStorage': {
            'sasLogicalJBODs': [],
            'controllers': []
        },
        'bootMode': {
            'manageMode': True,
            "mode": "BIOS",
            "pxeBootPolicy": None,
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
        'sanStorage': None,
        'osDeploymentSettings': None,
        'initialScopeUris': []
    },
    # Linux-1k NoLAG 631
    {
        'type': 'ServerProfileTemplateV7',
        'serverProfileDescription': 'Linux NoLAG DL360 Gen10 1 Profile',
        'serverHardwareTypeUri': 'SHT:DL360 Gen10 1',
        'enclosureGroupUri': '',
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': 'linux-1k-631',
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
        'boot': {'manageBoot': True,
                 'order': ['CD', 'USB', 'HardDisk', 'PXE']},
        'bootMode': {
            'manageMode': True,
            "mode": "BIOS",
            "pxeBootPolicy": None,
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
    # Linux-1k 640
    {
        'type': 'ServerProfileTemplateV7',
        'serverProfileDescription': 'Linux NoLAG DL360 Gen10 1 Profile',
        'serverHardwareTypeUri': 'SHT:DL360 Gen10 1',
        'enclosureGroupUri': '',
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': 'linux-1k-640',
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
        'boot': {'manageBoot': True,
                 'order': ['CD', 'USB', 'HardDisk', 'PXE']},
        'bootMode': {
            'manageMode': True,
            "mode": "BIOS",
            "pxeBootPolicy": None,
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

    # Linux-4k-LAG-631
    {
        'type': 'ServerProfileTemplateV7',
        'serverProfileDescription': 'Linux LAG DL360 Gen10 1 Profile',
        'serverHardwareTypeUri': 'SHT:DL360 Gen10 1',
        'enclosureGroupUri': '',
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': 'linux-4k-lag-631',
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
        'boot': {'manageBoot': True,
                 'order': ['CD', 'USB', 'HardDisk', 'PXE']},
        'bootMode': {
            'manageMode': True,
            "mode": "BIOS",
            "pxeBootPolicy": None,
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
    # Linux4k-lag 640FLR
    {
        'type': 'ServerProfileTemplateV7',
        'serverProfileDescription': 'Linux LAG DL360 Gen10 1 Profile',
        'serverHardwareTypeUri': 'SHT:DL360 Gen10 1',
        'enclosureGroupUri': '',
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': 'linux-4k-lag-640',
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
        'boot': {'manageBoot': True,
                 'order': ['CD', 'USB', 'HardDisk', 'PXE']},
        'bootMode': {
            'manageMode': True,
            "mode": "BIOS",
            "pxeBootPolicy": None,
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

server_profiles_using_template_Vader1 = [
    # Vader 1 server profiles using templates
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR1_U1'],
        'serverProfileTemplateUri': 'SPT:esx-lag-631',
        'name': 'ProfileR1_U1',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR1_U2'],
        'serverProfileTemplateUri': 'SPT:esx-lag-631',
        'name': 'ProfileR1_U2',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR1_U3'],
        'serverProfileTemplateUri': 'SPT:esx-lag-631',
        'name': 'ProfileR1_U3',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR1_U4'],
        'serverProfileTemplateUri': 'SPT:esx-lag-631',
        'name': 'ProfileR1_U4',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR1_U5'],
        'serverProfileTemplateUri': 'SPT:esx-lag-631',
        'name': 'ProfileR1_U5',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR1_U6'],
        'serverProfileTemplateUri': 'SPT:esx-lag-631',
        'name': 'ProfileR1_U6',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR1_U7'],
        'serverProfileTemplateUri': 'SPT:esx-lag-631',
        'name': 'ProfileR1_U7',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR1_U8'],
        'serverProfileTemplateUri': 'SPT:esx-lag-631',
        'name': 'ProfileR1_U8',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR1_U9'],
        'serverProfileTemplateUri': 'SPT:esx-lag-631',
        'name': 'ProfileR1_U9',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR1_U10'],
        'serverProfileTemplateUri': 'SPT:esx-lag-631',
        'name': 'ProfileR1_U10',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR1_U11'],
        'serverProfileTemplateUri': 'SPT:esx-lag-631',
        'name': 'ProfileR1_U11',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR1_U12'],
        'serverProfileTemplateUri': 'SPT:esx-631',
        'name': 'ProfileR1_U12',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR1_U13'],
        'serverProfileTemplateUri': 'SPT:esx-631',
        'name': 'ProfileR1_U13',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR1_U14'],
        'serverProfileTemplateUri': 'SPT:esx-631',
        'name': 'ProfileR1_U14',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR1_U15'],
        'serverProfileTemplateUri': 'SPT:esx-631',
        'name': 'ProfileR1_U15',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR1_U16'],
        'serverProfileTemplateUri': 'SPT:esx-631',
        'name': 'ProfileR1_U16',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR1_U17'],
        'serverProfileTemplateUri': 'SPT:esx-631',
        'name': 'ProfileR1_U17',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR1_U18'],
        'serverProfileTemplateUri': 'SPT:esx-631',
        'name': 'ProfileR1_U18',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR1_U19'],
        'serverProfileTemplateUri': 'SPT:esx-631',
        'name': 'ProfileR1_U19',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR1_U20'],
        'serverProfileTemplateUri': 'SPT:esx-631',
        'name': 'ProfileR1_U20',
    },
    # {
    # 'type': 'ServerProfileV10',
    # 'serverHardwareUri': server_profile_to_bay_map['ProfileR1_U22'],
    # 'serverProfileTemplateUri': 'SPT:esx',
    # 'name': 'ProfileR1_U22',
    # },
    # {
    # 'type': 'ServerProfileV10',
    # 'serverHardwareUri': server_profile_to_bay_map['ProfileR1_U23'],
    # 'serverProfileTemplateUri': 'SPT:esx',
    # 'name': 'ProfileR1_U23',
    # },
    # {
    # 'type': 'ServerProfileV10',
    # 'serverHardwareUri': server_profile_to_bay_map['ProfileR1_U24'],
    # 'serverProfileTemplateUri': 'SPT:esx',
    # 'name': 'ProfileR1_U24',
    # },
    # {
    # 'type': 'ServerProfileV10',
    # 'serverHardwareUri': server_profile_to_bay_map['ProfileR1_U25'],
    # 'serverProfileTemplateUri': 'SPT:esx',
    # 'name': 'ProfileR1_U25',
    # },
    # {
    # 'type': 'ServerProfileV10',
    # 'serverHardwareUri': server_profile_to_bay_map['ProfileR1_U26'],
    # 'serverProfileTemplateUri': 'SPT:esx',
    # 'name': 'ProfileR1_U26',
    # },
    # {
    # 'type': 'ServerProfileV10',
    # 'serverHardwareUri': server_profile_to_bay_map['ProfileR1_U27'],
    # 'serverProfileTemplateUri': 'SPT:esx',
    # 'name': 'ProfileR1_U27',
    # },
    # {
    # 'type': 'ServerProfileV10',
    # 'serverHardwareUri': server_profile_to_bay_map['ProfileR1_U28'],
    # 'serverProfileTemplateUri': 'SPT:esx',
    # 'name': 'ProfileR1_U28',
    # },
    # {
    # 'type': 'ServerProfileV10',
    # 'serverHardwareUri': server_profile_to_bay_map['ProfileR1_U29'],
    # 'serverProfileTemplateUri': 'SPT:esx',
    # 'name': 'ProfileR1_U29',
    # },
    # {
    # 'type': 'ServerProfileV10',
    # 'serverHardwareUri': server_profile_to_bay_map['ProfileR1_U30'],
    # 'serverProfileTemplateUri': 'SPT:esx',
    # 'name': 'ProfileR1_U30',
    # },
    # {
    # 'type': 'ServerProfileV10',
    # 'serverHardwareUri': server_profile_to_bay_map['ProfileR1_U31'],
    # 'serverProfileTemplateUri': 'SPT:esx',
    # 'name': 'ProfileR1_U31',
    # },
    # {
    # 'type': 'ServerProfileV10',
    # 'serverHardwareUri': server_profile_to_bay_map['ProfileR1_U32'],
    # 'serverProfileTemplateUri': 'SPT:esx',
    # 'name': 'ProfileR1_U32',
    # },
    # {
    # 'type': 'ServerProfileV10',
    # 'serverHardwareUri': server_profile_to_bay_map['ProfileR1_U33'],
    # 'serverProfileTemplateUri': 'SPT:esx',
    # 'name': 'ProfileR1_U33',
    # },
    # {
    # 'type': 'ServerProfileV10',
    # 'serverHardwareUri': server_profile_to_bay_map['ProfileR1_U34'],
    # 'serverProfileTemplateUri': 'SPT:esx',
    # 'name': 'ProfileR1_U34',
    # },
    # {
    # 'type': 'ServerProfileV10',
    # 'serverHardwareUri': server_profile_to_bay_map['ProfileR1_U35'],
    # 'serverProfileTemplateUri': 'SPT:linux-4k-lag-dl360',
    # 'name': 'ProfileR1_U35',
    # },
    # {
    # 'type': 'ServerProfileV10',
    # 'serverHardwareUri': server_profile_to_bay_map['ProfileR1_U36'],
    # 'serverProfileTemplateUri': 'SPT:linux-4k-lag-dl360',
    # 'name': 'ProfileR1_U36',
    # },
    # {
    # 'type': 'ServerProfileV10',
    # 'serverHardwareUri': server_profile_to_bay_map['ProfileR1_U37'],
    # 'serverProfileTemplateUri': 'SPT:linux-4k-lag-dl360',
    # 'name': 'ProfileR1_U37',
    # },
    # {
    # 'type': 'ServerProfileV10',
    # 'serverHardwareUri': server_profile_to_bay_map['ProfileR1_U38'],
    # 'serverProfileTemplateUri': 'SPT:linux-4k-lag-dl360',
    # 'name': 'ProfileR1_U38',
    # },
    # {
    # 'type': 'ServerProfileV10',
    # 'serverHardwareUri': server_profile_to_bay_map['ProfileR1_U39'],
    # 'serverProfileTemplateUri': 'SPT:linux-4k-lag-dl360',
    # 'name': 'ProfileR1_U39',
    #    },
]

server_profiles_using_template_Vader2 = [
    # Vader 2 server profiles using templates
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR2_U1'],
        'serverProfileTemplateUri': 'SPT:esx-lag-631',
        'name': 'ProfileR2_U1',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR2_U2'],
        'serverProfileTemplateUri': 'SPT:esx-lag-631',
        'name': 'ProfileR2_U2',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR2_U3'],
        'serverProfileTemplateUri': 'SPT:esx-lag-631',
        'name': 'ProfileR2_U3',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR2_U4'],
        'serverProfileTemplateUri': 'SPT:esx-lag-631',
        'name': 'ProfileR2_U4',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR2_U5'],
        'serverProfileTemplateUri': 'SPT:esx-lag-631',
        'name': 'ProfileR2_U5',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR2_U6'],
        'serverProfileTemplateUri': 'SPT:esx-lag-631',
        'name': 'ProfileR2_U6',
    },
    # {
    # 'type': 'ServerProfileV10',
    # 'serverHardwareUri': server_profile_to_bay_map['ProfileR2_U7'],
    # 'serverProfileTemplateUri': 'SPT:esx-lag-631',
    # 'name': 'ProfileR2_U7',
    # },
    # {
    # 'type': 'ServerProfileV10',
    # 'serverHardwareUri': server_profile_to_bay_map['ProfileR2_U8'],
    # 'serverProfileTemplateUri': 'SPT:esx-lag-631',
    # 'name': 'ProfileR2_U8',
    # },
    # {
    # 'type': 'ServerProfileV10',
    # 'serverHardwareUri': server_profile_to_bay_map['ProfileR2_U9'],
    # 'serverProfileTemplateUri': 'SPT:esx-lag-631',
    # 'name': 'ProfileR2_U9',
    # },
    # {
    # 'type': 'ServerProfileV10',
    # 'serverHardwareUri': server_profile_to_bay_map['ProfileR2_U10'],
    # 'serverProfileTemplateUri': 'SPT:esx-lag-631',
    # 'name': 'ProfileR2_U10',
    # },
    # {
    # 'type': 'ServerProfileV10',
    # 'serverHardwareUri': server_profile_to_bay_map['ProfileR2_U11'],
    # 'serverProfileTemplateUri': 'SPT:esx-lag-631',
    # 'name': 'ProfileR2_U11',
    # },
    # {
    # 'type': 'ServerProfileV10',
    # 'serverHardwareUri': server_profile_to_bay_map['ProfileR2_U12'],
    # 'serverProfileTemplateUri': 'SPT:esx-631',
    # 'name': 'ProfileR2_U12',
    # },
    # {
    # 'type': 'ServerProfileV10',
    # 'serverHardwareUri': server_profile_to_bay_map['ProfileR2_U13'],
    # 'serverProfileTemplateUri': 'SPT:esx-631',
    # 'name': 'ProfileR2_U13',
    # },
    # {
    # 'type': 'ServerProfileV10',
    # 'serverHardwareUri': server_profile_to_bay_map['ProfileR2_U14'],
    # 'serverProfileTemplateUri': 'SPT:esx-631',
    # 'name': 'ProfileR2_U14',
    # },
    # {
    # 'type': 'ServerProfileV10',
    # 'serverHardwareUri': server_profile_to_bay_map['ProfileR2_U15'],
    # 'serverProfileTemplateUri': 'SPT:esx-631',
    # 'name': 'ProfileR2_U15',
    # },
    # {
    # 'type': 'ServerProfileV10',
    # 'serverHardwareUri': server_profile_to_bay_map['ProfileR2_U16'],
    # 'serverProfileTemplateUri': 'SPT:esx-631',
    # 'name': 'ProfileR2_U16',
    # },
    # {
    # 'type': 'ServerProfileV10',
    # 'serverHardwareUri': server_profile_to_bay_map['ProfileR2_U17'],
    # 'serverProfileTemplateUri': 'SPT:esx-631',
    # 'name': 'ProfileR2_U17',
    # },
    # {
    # 'type': 'ServerProfileV10',
    # 'serverHardwareUri': server_profile_to_bay_map['ProfileR2_U18'],
    # 'serverProfileTemplateUri': 'SPT:esx-631',
    # 'name': 'ProfileR2_U18',
    # },
    # {
    # 'type': 'ServerProfileV10',
    # 'serverHardwareUri': server_profile_to_bay_map['ProfileR2_U19'],
    # 'serverProfileTemplateUri': 'SPT:esx-631',
    # 'name': 'ProfileR2_U19',
    # },
    # {
    # 'type': 'ServerProfileV10',
    # 'serverHardwareUri': server_profile_to_bay_map['ProfileR2_U20'],
    # 'serverProfileTemplateUri': 'SPT:esx-631',
    # 'name': 'ProfileR2_U20',
    # },
    # {
    # 'type': 'ServerProfileV10',
    # 'serverHardwareUri': server_profile_to_bay_map['ProfileR2_U21'],
    # 'serverProfileTemplateUri': 'SPT:esx-631',
    # 'name': 'ProfileR2_U21',
    # },
    # {
    # 'type': 'ServerProfileV10',
    # 'serverHardwareUri': server_profile_to_bay_map['ProfileR2_U22'],
    # 'serverProfileTemplateUri': 'SPT:esx-631',
    # 'name': 'ProfileR2_U22',
    # },
    # {
    # 'type': 'ServerProfileV10',
    # 'serverHardwareUri': server_profile_to_bay_map['ProfileR2_U23'],
    # 'serverProfileTemplateUri': 'SPT:esx-lag-631',
    # 'name': 'ProfileR2_U23',
    # },
    # {
    # 'type': 'ServerProfileV10',
    # 'serverHardwareUri': server_profile_to_bay_map['ProfileR2_U24'],
    # 'serverProfileTemplateUri': 'SPT:esx',
    # 'name': 'ProfileR2_U24',
    # },
    # {
    # 'type': 'ServerProfileV10',
    # 'serverHardwareUri': server_profile_to_bay_map['ProfileR2_U25'],
    # 'serverProfileTemplateUri': 'SPT:esx',
    # 'name': 'ProfileR2_U25',
    # },
    # {
    # 'type': 'ServerProfileV10',
    # 'serverHardwareUri': server_profile_to_bay_map['ProfileR2_U26'],
    # 'serverProfileTemplateUri': 'SPT:esx',
    # 'name': 'ProfileR2_U26',
    # },
    # {
    # 'type': 'ServerProfileV10',
    # 'serverHardwareUri': server_profile_to_bay_map['ProfileR2_U27'],
    # 'serverProfileTemplateUri': 'SPT:esx',
    # 'name': 'ProfileR2_U27',
    # },
    # {
    # 'type': 'ServerProfileV10',
    # 'serverHardwareUri': server_profile_to_bay_map['ProfileR2_U28'],
    # 'serverProfileTemplateUri': 'SPT:esx',
    # 'name': 'ProfileR2_U28',
    # },
    # {
    # 'type': 'ServerProfileV10',
    # 'serverHardwareUri': server_profile_to_bay_map['ProfileR2_U29'],
    # 'serverProfileTemplateUri': 'SPT:esx',
    # 'name': 'ProfileR2_U29',
    # },
    # {
    # 'type': 'ServerProfileV10',
    # 'serverHardwareUri': server_profile_to_bay_map['ProfileR2_U30'],
    # 'serverProfileTemplateUri': 'SPT:esx',
    # 'name': 'ProfileR2_U30',
    # },
    # {
    # 'type': 'ServerProfileV10',
    # 'serverHardwareUri': server_profile_to_bay_map['ProfileR2_U31'],
    # 'serverProfileTemplateUri': 'SPT:esx',
    # 'name': 'ProfileR2_U31',
    # },
    # {
    # 'type': 'ServerProfileV10',
    # 'serverHardwareUri': server_profile_to_bay_map['ProfileR2_U32'],
    # 'serverProfileTemplateUri': 'SPT:esx',
    # 'name': 'ProfileR2_U32',
    # },
    # {
    # 'type': 'ServerProfileV10',
    # 'serverHardwareUri': server_profile_to_bay_map['ProfileR2_U33'],
    # 'serverProfileTemplateUri': 'SPT:linux-4k-lag-dl360',
    # 'name': 'ProfileR2_U33',
    # },
    # {
    # 'type': 'ServerProfileV10',
    # 'serverHardwareUri': server_profile_to_bay_map['ProfileR2_U34'],
    # 'serverProfileTemplateUri': 'SPT:linux-4k-lag-dl360',
    # 'name': 'ProfileR2_U34',
    # },
    # {
    # 'type': 'ServerProfileV10',
    # 'serverHardwareUri': server_profile_to_bay_map['ProfileR2_U35'],
    # 'serverProfileTemplateUri': 'SPT:linux-4k-lag-dl360',
    # 'name': 'ProfileR2_U35',
    # },
    # {
    # 'type': 'ServerProfileV10',
    # 'serverHardwareUri': server_profile_to_bay_map['ProfileR2_U36'],
    # 'serverProfileTemplateUri': 'SPT:linux-4k-lag-dl360',
    # 'name': 'ProfileR2_U36',
    # },
    # {
    # 'type': 'ServerProfileV10',
    # 'serverHardwareUri': server_profile_to_bay_map['ProfileR2_U37'],
    # 'serverProfileTemplateUri': 'SPT:linux-4k-lag-dl360',
    # 'name': 'ProfileR2_U37',
    # },
]

server_profiles_using_template_Vader3 = [
    # Vader 3 server profiles using templates
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR3_U1'],
        'serverProfileTemplateUri': 'SPT:esx-lag-631',
        'name': 'ProfileR3_U1',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR3_U2'],
        'serverProfileTemplateUri': 'SPT:esx-lag-631',
        'name': 'ProfileR3_U2',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR3_U3'],
        'serverProfileTemplateUri': 'SPT:esx-lag-631',
        'name': 'ProfileR3_U3',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR3_U4'],
        'serverProfileTemplateUri': 'SPT:esx-lag-631',
        'name': 'ProfileR3_U4',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR3_U5'],
        'serverProfileTemplateUri': 'SPT:esx-lag-631',
        'name': 'ProfileR3_U5',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR3_U6'],
        'serverProfileTemplateUri': 'SPT:esx-lag-631',
        'name': 'ProfileR3_U6',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR3_U7'],
        'serverProfileTemplateUri': 'SPT:esx-lag-631',
        'name': 'ProfileR3_U7',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR3_U8'],
        'serverProfileTemplateUri': 'SPT:esx-lag-631',
        'name': 'ProfileR3_U8',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR3_U9'],
        'serverProfileTemplateUri': 'SPT:esx-lag-631',
        'name': 'ProfileR3_U9',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR3_U10'],
        'serverProfileTemplateUri': 'SPT:esx-lag-631',
        'name': 'ProfileR3_U10',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR3_U11'],
        'serverProfileTemplateUri': 'SPT:esx-631',
        'name': 'ProfileR3_U11',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR3_U12'],
        'serverProfileTemplateUri': 'SPT:esx-631',
        'name': 'ProfileR3_U12',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR3_U13'],
        'serverProfileTemplateUri': 'SPT:esx-631',
        'name': 'ProfileR3_U13',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR3_U14'],
        'serverProfileTemplateUri': 'SPT:esx-631',
        'name': 'ProfileR3_U14',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR3_U15'],
        'serverProfileTemplateUri': 'SPT:esx-631',
        'name': 'ProfileR3_U15',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR3_U16'],
        'serverProfileTemplateUri': 'SPT:esx-631',
        'name': 'ProfileR3_U16',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR3_U17'],
        'serverProfileTemplateUri': 'SPT:esx-631',
        'name': 'ProfileR3_U17',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR3_U18'],
        'serverProfileTemplateUri': 'SPT:esx-631',
        'name': 'ProfileR3_U18',
    },
    # {
    #    'type': 'ServerProfileV10',
    #    'serverHardwareUri': server_profile_to_bay_map['ProfileR3_U19'],
    #    'serverProfileTemplateUri': 'SPT:esx-631',
    #    'name': 'ProfileR3_U19',
    # },
    # {
    # 'type': 'ServerProfileV10',
    # 'serverHardwareUri': server_profile_to_bay_map['ProfileR3_U20'],
    # 'serverProfileTemplateUri': 'SPT:esx-631',
    # 'name': 'ProfileR3_U20',
    # },
    # {
    # 'type': 'ServerProfileV10',
    # 'serverHardwareUri': server_profile_to_bay_map['ProfileR3_U21'],
    # 'serverProfileTemplateUri': 'SPT:esx-lag-631',
    # 'name': 'ProfileR3_U21',
    # },
    # {
    # 'type': 'ServerProfileV10',
    # 'serverHardwareUri': server_profile_to_bay_map['ProfileR3_U22'],
    # 'serverProfileTemplateUri': 'SPT:esx-lag-631',
    # 'name': 'ProfileR3_U22',
    # },
    # {
    # 'type': 'ServerProfileV10',
    # 'serverHardwareUri': server_profile_to_bay_map['ProfileR3_U23'],
    # 'serverProfileTemplateUri': 'SPT:esx-lag-631',
    # 'name': 'ProfileR3_U23',
    # },
]

server_profiles_using_template_Vader4 = [
    # Vader 4 server profiles using templates
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR4_U1'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR4_U1',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR4_U2'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR4_U2',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR4_U3'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR4_U3',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR4_U4'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR4_U4',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR4_U5'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR4_U5',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR4_U6'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR4_U6',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR4_U7'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR4_U7',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR4_U8'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR4_U8',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR4_U9'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR4_U9',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR4_U10'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR4_U10',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR4_U11'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR4_U11',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR4_U12'],
        'serverProfileTemplateUri': 'SPT:esx-640',
        'name': 'ProfileR4_U12',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR4_U13'],
        'serverProfileTemplateUri': 'SPT:esx-640',
        'name': 'ProfileR4_U13',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR4_U14'],
        'serverProfileTemplateUri': 'SPT:esx-640',
        'name': 'ProfileR4_U14',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR4_U15'],
        'serverProfileTemplateUri': 'SPT:esx-640',
        'name': 'ProfileR4_U15',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR4_U16'],
        'serverProfileTemplateUri': 'SPT:esx-640',
        'name': 'ProfileR4_U16',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR4_U17'],
        'serverProfileTemplateUri': 'SPT:esx-640',
        'name': 'ProfileR4_U17',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR4_U18'],
        'serverProfileTemplateUri': 'SPT:esx-640',
        'name': 'ProfileR4_U18',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR4_U19'],
        'serverProfileTemplateUri': 'SPT:esx-640',
        'name': 'ProfileR4_U19',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR4_U20'],
        'serverProfileTemplateUri': 'SPT:esx-640',
        'name': 'ProfileR4_U20',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR4_U21'],
        'serverProfileTemplateUri': 'SPT:esx-640',
        'name': 'ProfileR4_U21',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR4_U22'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR4_U22',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR4_U23'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR4_U23',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR4_U24'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR4_U24',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR4_U25'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR4_U25',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR4_U26'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR4_U26',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR4_U27'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR4_U27',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR4_U28'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR4_U28',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR4_U29'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR4_U29',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR4_U30'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR4_U30',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR4_U31'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR4_U31',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR4_U32'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR4_U32',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR4_U33'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR4_U33',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR4_U34'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR4_U34',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR4_U35'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR4_U35',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR4_U36'],
        'serverProfileTemplateUri': 'SPT:linux-4k-lag-640',
        'name': 'ProfileR4_U36',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR4_U37'],
        'serverProfileTemplateUri': 'SPT:linux-4k-lag-640',
        'name': 'ProfileR4_U37',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR4_U38'],
        'serverProfileTemplateUri': 'SPT:linux-1k-640',
        'name': 'ProfileR4_U38',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR4_U39'],
        'serverProfileTemplateUri': 'SPT:linux-1k-640',
        'name': 'ProfileR4_U39',
    },
]

server_profiles_using_template_Vader5 = [
    # Vader 5 server profiles using templates
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR5_U1'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR5_U1',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR5_U2'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR5_U2',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR5_U3'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR5_U3',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR5_U4'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR5_U4',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR5_U5'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR5_U5',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR5_U6'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR5_U6',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR5_U7'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR5_U7',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR5_U8'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR5_U8',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR5_U9'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR5_U9',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR5_U10'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR5_U10',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR5_U11'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR5_U11',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR5_U12'],
        'serverProfileTemplateUri': 'SPT:esx-640',
        'name': 'ProfileR5_U12',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR5_U13'],
        'serverProfileTemplateUri': 'SPT:esx-640',
        'name': 'ProfileR5_U13',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR5_U14'],
        'serverProfileTemplateUri': 'SPT:esx-640',
        'name': 'ProfileR5_U14',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR5_U15'],
        'serverProfileTemplateUri': 'SPT:esx-640',
        'name': 'ProfileR5_U15',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR5_U16'],
        'serverProfileTemplateUri': 'SPT:esx-640',
        'name': 'ProfileR5_U16',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR5_U17'],
        'serverProfileTemplateUri': 'SPT:esx-640',
        'name': 'ProfileR5_U17',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR5_U18'],
        'serverProfileTemplateUri': 'SPT:esx-640',
        'name': 'ProfileR5_U18',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR5_U19'],
        'serverProfileTemplateUri': 'SPT:esx-640',
        'name': 'ProfileR5_U19',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR5_U20'],
        'serverProfileTemplateUri': 'SPT:esx-640',
        'name': 'ProfileR5_U20',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR5_U21'],
        'serverProfileTemplateUri': 'SPT:esx-640',
        'name': 'ProfileR5_U21',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR5_U22'],
        'serverProfileTemplateUri': 'SPT:esx-640',
        'name': 'ProfileR5_U22',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR5_U23'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR5_U23',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR5_U24'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR5_U24',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR5_U25'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR5_U25',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR5_U26'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR5_U26',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR5_U27'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR5_U27',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR5_U28'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR5_U28',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR5_U29'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR5_U29',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR5_U30'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR5_U30',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR5_U31'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR5_U31',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR5_U32'],
        'serverProfileTemplateUri': 'SPT:linux-4k-lag-640',
        'name': 'ProfileR5_U32',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR5_U33'],
        'serverProfileTemplateUri': 'SPT:linux-4k-lag-640',
        'name': 'ProfileR5_U33',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR5_U34'],
        'serverProfileTemplateUri': 'SPT:linux-4k-lag-640',
        'name': 'ProfileR5_U34',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR5_U35'],
        'serverProfileTemplateUri': 'SPT:linux-4k-lag-640',
        'name': 'ProfileR5_U35',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR5_U36'],
        'serverProfileTemplateUri': 'SPT:linux-1k-640',
        'name': 'ProfileR5_U36',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR5_U37'],
        'serverProfileTemplateUri': 'SPT:linux-1k-640',
        'name': 'ProfileR5_U37',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR5_U38'],
        'serverProfileTemplateUri': 'SPT:linux-1k-640',
        'name': 'ProfileR5_U38',
    },
]

server_profiles_using_template_Vader6 = [
    # Vader 6 server profiles using templates
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR6_U1'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR6_U1',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR6_U2'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR6_U2',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR6_U3'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR6_U3',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR6_U4'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR6_U4',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR6_U5'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR6_U5',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR6_U6'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR6_U6',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR6_U7'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR6_U7',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR6_U8'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR6_U8',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR6_U9'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR6_U9',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR6_U10'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR6_U10',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR6_U11'],
        'serverProfileTemplateUri': 'SPT:esx-640',
        'name': 'ProfileR6_U11',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR6_U12'],
        'serverProfileTemplateUri': 'SPT:esx-640',
        'name': 'ProfileR6_U12',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR6_U13'],
        'serverProfileTemplateUri': 'SPT:esx-640',
        'name': 'ProfileR6_U13',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR6_U14'],
        'serverProfileTemplateUri': 'SPT:esx-640',
        'name': 'ProfileR6_U14',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR6_U15'],
        'serverProfileTemplateUri': 'SPT:esx-640',
        'name': 'ProfileR6_U15',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR6_U16'],
        'serverProfileTemplateUri': 'SPT:esx-640',
        'name': 'ProfileR6_U16',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR6_U17'],
        'serverProfileTemplateUri': 'SPT:esx-640',
        'name': 'ProfileR6_U17',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR6_U18'],
        'serverProfileTemplateUri': 'SPT:esx-640',
        'name': 'ProfileR6_U18',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR6_U19'],
        'serverProfileTemplateUri': 'SPT:esx-640',
        'name': 'ProfileR6_U19',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR6_U20'],
        'serverProfileTemplateUri': 'SPT:esx-640',
        'name': 'ProfileR6_U20',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR6_U21'],
        'serverProfileTemplateUri': 'SPT:esx-640',
        'name': 'ProfileR6_U21',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR6_U22'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR6_U22',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR6_U23'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR6_U23',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR6_U24'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR6_U24',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR6_U25'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR6_U25',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR6_U26'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR6_U26',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR6_U27'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR6_U27',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR6_U28'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR6_U28',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR6_U29'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR6_U29',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR6_U30'],
        'serverProfileTemplateUri': 'SPT:esx-lag-640',
        'name': 'ProfileR6_U30',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR6_U31'],
        'serverProfileTemplateUri': 'SPT:linux-4k-lag-640',
        'name': 'ProfileR6_U31',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR6_U32'],
        'serverProfileTemplateUri': 'SPT:linux-4k-lag-640',
        'name': 'ProfileR6_U32',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR6_U33'],
        'serverProfileTemplateUri': 'SPT:linux-4k-lag-640',
        'name': 'ProfileR6_U33',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR6_U34'],
        'serverProfileTemplateUri': 'SPT:linux-1k-640',
        'name': 'ProfileR6_U34',
    },
    {
        'type': 'ServerProfileV10',
        'serverHardwareUri': server_profile_to_bay_map['ProfileR6_U35'],
        'serverProfileTemplateUri': 'SPT:linux-1k-640',
        'name': 'ProfileR6_U35',
    },
]

server_profiles_using_template = server_profiles_using_template_Vader1 + server_profiles_using_template_Vader2 + server_profiles_using_template_Vader3 + \
    server_profiles_using_template_Vader4 + \
    server_profiles_using_template_Vader5 + \
    server_profiles_using_template_Vader6

#####################
# Plexxi section
#####################
# Plexxi connect credentials
plexxi_connect_host = '10.177.14.2'
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

cfm_ntp = {'name': 'NTP Client Configuration',
           'servers': ['ntp.hpecorp.net'],
           'switch_uuids': [],
           'fabric_uuids': [],
           'description': 'NTP Client Configuration'
           }

cfm_dns = {'description': 'DNS Client Configuration',
           'domain_name': 'dom1177.lab',
           'search_path': [],
           'management_software': True,
           'switch_uuids': [],
           'fabric_uuids': [],
           'name_servers': ['10.171.0.11'],
           'name': 'DNS Client Configuration'
           }

#####################
# Logical Switches and Logical Switch Groups section
#####################
PLEXXI_SWITCHES_CREDENTIALS_VADER1 = {
    '1': {
        'ip': '10.177.14.3',
        'username': 'admin',
        'password': 'plexxi'
    },
    '2': {
        'ip': '10.177.14.4',
        'username': 'admin',
        'password': 'plexxi'
    }
}

PLEXXI_SWITCHES_CREDENTIALS_VADER2 = {
    '3': {
        'ip': '10.177.14.5',
        'username': 'admin',
        'password': 'plexxi'
    },
    '4': {
        'ip': '10.177.14.6',
        'username': 'admin',
        'password': 'plexxi'
    }
}

PLEXXI_SWITCHES_CREDENTIALS_VADER3 = {
    '5': {
        'ip': '10.177.14.7',
        'username': 'admin',
        'password': 'plexxi'
    },
    '6': {
        'ip': '10.177.14.8',
        'username': 'admin',
        'password': 'plexxi'
    },
}

PLEXXI_SWITCHES_CREDENTIALS_VADER4 = {
    '7': {
        'ip': '10.177.14.9',
        'username': 'admin',
        'password': 'plexxi'
    },
    '8': {
        'ip': '10.177.14.10',
        'username': 'admin',
        'password': 'plexxi'
    },
}

PLEXXI_SWITCHES_CREDENTIALS_VADER5 = {
    '9': {
        'ip': '10.177.14.11',
        'username': 'admin',
        'password': 'plexxi'
    },
    '10': {
        'ip': '10.177.14.12',
        'username': 'admin',
        'password': 'plexxi'
    },
}

PLEXXI_SWITCHES_CREDENTIALS_VADER6 = {
    '11': {
        'ip': '10.177.14.13',
        'username': 'admin',
        'password': 'plexxi'
    },
    '12': {
        'ip': '10.178.14.14',
        'username': 'admin',
        'password': 'plexxi'
    },
}

fabric_name = "CRST Vader Rig Fabric"
# Transition fabrics to Adding, Configured
# Keeping this 2-state transition for now because of pending question to CRM on initiate fabric claim with 'Configured' transition that can cause problem
# fabric_states = [[{"op":"replace","path":"/state","value":"Adding"}], [{"op":"replace","path":"/state","value":"Configured"}]]
fabric_adding = [{"op": "replace", "path": "/state", "value": "Adding"}]
# Plexxi Fabric request bodies
#    :List of dictionary of request bodies
plexxi_fabrics = [
    {
        "host": PLEXXI_SWITCHES_CREDENTIALS_VADER1['1']['ip'],
        "name": fabric_name,
        "description": "CRST Vader Rig Fabric"
    }
]

LSG_NAME = ['LSG_VaderRig']

switch_names_Vader1 = ["E0:39:D7:84:B6:80", "E0:39:D7:84:B9:80"]
switch_names_Vader2 = ["E0:39:D7:84:B3:80", "E0:39:D7:84:B8:00"]
switch_names_Vader3 = ["E0:39:D7:84:7D:80", "E0:39:D7:84:B6:00"]
switch_names_Vader4 = ["E0:39:D7:84:BA:80", "E0:39:D7:84:B2:00"]
switch_names_Vader5 = ["E0:39:D7:84:BA:00", "E0:39:D7:84:B1:80"]
switch_names_Vader6 = ["E0:39:D7:84:B8:80", "E0:39:D7:84:B3:00"]

switch_names = switch_names_Vader1 + switch_names_Vader2 + switch_names_Vader3 + \
    switch_names_Vader4 + switch_names_Vader5 + switch_names_Vader6

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
lss_Vader1 = [
    {
        "logicalSwitch": {
            "name": "LS_Vader1Rig",
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
                    "logicalSwitchManagementHost": PLEXXI_SWITCHES_CREDENTIALS_VADER1['1']['ip'],
                    "snmpVersion": "SNMPv1",
                    "snmpPort": 161
                }
            ],
            # name of switches, script will find their appropriate uris by name
            "switchUris": [switch_names_Vader1[0], switch_names_Vader1[1]]
        },
        "logicalSwitchCredentials": [
            {
                "connectionProperties": [
                    {
                        "propertyName": "SshBasicAuthCredentialUser",
                        "value": PLEXXI_SWITCHES_CREDENTIALS_VADER1['1']['username'],
                        "valueFormat": "Unknown",
                        "valueType": "String"
                    },
                    {
                        "propertyName": "SshBasicAuthCredentialPassword",
                        "value": PLEXXI_SWITCHES_CREDENTIALS_VADER1['1']['password'],
                        "valueFormat": "SecuritySensitive",
                        "valueType": "String"
                    }
                ]
            }
        ]
    }
]

lss_Vader2 = [
    {
        "logicalSwitch": {
            "name": "LS_Vader2Rig",
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
                    "logicalSwitchManagementHost": PLEXXI_SWITCHES_CREDENTIALS_VADER2['3']['ip'],
                    "snmpVersion": "SNMPv1",
                    "snmpPort": 161
                }
            ],
            # name of switches, script will find their appropriate uris by name
            "switchUris": [switch_names_Vader2[0], switch_names_Vader2[1]]
        },
        "logicalSwitchCredentials": [
            {
                "connectionProperties": [
                    {
                        "propertyName": "SshBasicAuthCredentialUser",
                        "value": PLEXXI_SWITCHES_CREDENTIALS_VADER2['3']['username'],
                        "valueFormat": "Unknown",
                        "valueType": "String"
                    },
                    {
                        "propertyName": "SshBasicAuthCredentialPassword",
                        "value": PLEXXI_SWITCHES_CREDENTIALS_VADER2['3']['password'],
                        "valueFormat": "SecuritySensitive",
                        "valueType": "String"
                    }
                ]
            }
        ]
    }
]

lss_Vader3 = [
    {
        "logicalSwitch": {
            "name": "LS_Vader3Rig",
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
                    "logicalSwitchManagementHost": PLEXXI_SWITCHES_CREDENTIALS_VADER3['5']['ip'],
                    "snmpVersion": "SNMPv1",
                    "snmpPort": 161
                }
            ],
            # name of switches, script will find their appropriate uris by name
            "switchUris": [switch_names_Vader3[0], switch_names_Vader3[1]]
        },
        "logicalSwitchCredentials": [
            {
                "connectionProperties": [
                    {
                        "propertyName": "SshBasicAuthCredentialUser",
                        "value": PLEXXI_SWITCHES_CREDENTIALS_VADER3['5']['username'],
                        "valueFormat": "Unknown",
                        "valueType": "String"
                    },
                    {
                        "propertyName": "SshBasicAuthCredentialPassword",
                        "value": PLEXXI_SWITCHES_CREDENTIALS_VADER3['5']['password'],
                        "valueFormat": "SecuritySensitive",
                        "valueType": "String"
                    }
                ]
            }
        ]
    }
]

lss_Vader4 = [
    {
        "logicalSwitch": {
            "name": "LS_Vader4Rig",
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
                    "logicalSwitchManagementHost": PLEXXI_SWITCHES_CREDENTIALS_VADER4['7']['ip'],
                    "snmpVersion": "SNMPv1",
                    "snmpPort": 161
                }
            ],
            # name of switches, script will find their appropriate uris by name
            "switchUris": [switch_names_Vader4[0], switch_names_Vader4[1]]
        },
        "logicalSwitchCredentials": [
            {
                "connectionProperties": [
                    {
                        "propertyName": "SshBasicAuthCredentialUser",
                        "value": PLEXXI_SWITCHES_CREDENTIALS_VADER4['7']['username'],
                        "valueFormat": "Unknown",
                        "valueType": "String"
                    },
                    {
                        "propertyName": "SshBasicAuthCredentialPassword",
                        "value": PLEXXI_SWITCHES_CREDENTIALS_VADER4['7']['password'],
                        "valueFormat": "SecuritySensitive",
                        "valueType": "String"
                    }
                ]
            }
        ]
    }
]

lss_Vader5 = [
    {
        "logicalSwitch": {
            "name": "LS_Vader5Rig",
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
                    "logicalSwitchManagementHost": PLEXXI_SWITCHES_CREDENTIALS_VADER5['9']['ip'],
                    "snmpVersion": "SNMPv1",
                    "snmpPort": 161
                }
            ],
            # name of switches, script will find their appropriate uris by name
            "switchUris": [switch_names_Vader5[0], switch_names_Vader5[1]]
        },
        "logicalSwitchCredentials": [
            {
                "connectionProperties": [
                    {
                        "propertyName": "SshBasicAuthCredentialUser",
                        "value": PLEXXI_SWITCHES_CREDENTIALS_VADER5['9']['username'],
                        "valueFormat": "Unknown",
                        "valueType": "String"
                    },
                    {
                        "propertyName": "SshBasicAuthCredentialPassword",
                        "value": PLEXXI_SWITCHES_CREDENTIALS_VADER5['9']['password'],
                        "valueFormat": "SecuritySensitive",
                        "valueType": "String"
                    }
                ]
            }
        ]
    }
]

lss_Vader6 = [
    {
        "logicalSwitch": {
            "name": "LS_Vader6Rig",
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
                    "logicalSwitchManagementHost": PLEXXI_SWITCHES_CREDENTIALS_VADER6['11']['ip'],
                    "snmpVersion": "SNMPv1",
                    "snmpPort": 161
                }
            ],
            # name of switches, script will find their appropriate uris by name
            "switchUris": [switch_names_Vader6[0], switch_names_Vader6[1]]
        },
        "logicalSwitchCredentials": [
            {
                "connectionProperties": [
                    {
                        "propertyName": "SshBasicAuthCredentialUser",
                        "value": PLEXXI_SWITCHES_CREDENTIALS_VADER6['11']['username'],
                        "valueFormat": "Unknown",
                        "valueType": "String"
                    },
                    {
                        "propertyName": "SshBasicAuthCredentialPassword",
                        "value": PLEXXI_SWITCHES_CREDENTIALS_VADER6['11']['password'],
                        "valueFormat": "SecuritySensitive",
                        "valueType": "String"
                    }
                ]
            }
        ]
    }
]

lss = lss_Vader1 + lss_Vader2 + lss_Vader3 + \
    lss_Vader4 + lss_Vader5 + lss_Vader6

######################
# CFM Gateway section
######################
gateway_ports_split = [49.1, 50.1]
gateway_ports = [49]   # Currently, 100gb DAC cables only connected to port 49
gateway_qsfp_mode = 'qsfp_1x100_gbps'
gateway_fec_mode = 'enabled'
gateway_vlan_range = '1-4000'
gateway_native_vlan = 0
gateway_lag_ports = [{'p1r1Vader': 49},
                     {'p12r6Vader': 49}]

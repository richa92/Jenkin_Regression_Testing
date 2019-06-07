"""resources/defaults.py - Default variables used for WPST CRM Austin RoboGalaxyLibrary testing

    = Usage =
        | *** Settings ***      |
        | variables | resources/defaults.py |
    or
        | pybot --variablefile resources/defaults.py
"""
# Default excluding list for OV resources  (ov-x.json)
general_ignoreList = ['created', 'category', 'eTag', 'modified', 'id', 'headers']
networkset_ignoreList = ['networkUris']
profile_ignoreList = ['iscsiInitiatorName']
other_ignoreList = ['locationEntries', 'logicalLocation', 'location']
ovExcList = general_ignoreList + networkset_ignoreList + profile_ignoreList + other_ignoreList
# Default excluding list for Compatibility Report (rpt-x.json)
rptExcList = ['vcmLastConfigurationChangeTimeStamp']

excList = ovExcList + rptExcList

licenses = [{'key': '9B3C A99A H9P9 GHUZ U7B5 HWW5 Y9JL KMPL 5AWA 8CBE DXAU 2CSM GHTG L762 7NGZ GDV4 KJVT D5KM EFRW DS5R 5XP8 4XK2 GNSL 9F82 7JKT QVXB XZKH ABB4 NV2C LHXU KN7U 5NA6 BKRK 35QB D8UW R42A X3BN LQ6M 5V9A PM6Q 4MN9 9GGS EZU7 GEMX VUJW CDB5 JVRX 8HEN 2J98 ACPB "TKOPREN HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR ATJUJJEDAT2Y"'},
            {'key': 'YBLG B99A H9PQ 8HVZ U7B5 HWW5 Y9JL KMPL VAWA 8CBE DXAU 2CSM GHTG L762 5NW5 HDV4 KJVT D5KM EFVW DT5J VXP8 4XK2 GNSL 9F82 7JKT QVXB XZKH ABB4 NV2C LHXU KN7U 5NA6 BKRK 35QB D8UW R42A X3BN LQ6M 5V9A PM6Q 4MN9 9GGS EZU7 GEMX VUJW CDB5 JVRX 8HEN 2J98 ACPB "TKOPREN HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR JJADJJEDATCA"'}
            ]
# Variables for generating migration statistics report
groupingResShort = ['/migratable-vc-domains', '/migratable-vc-domains/migratable-vc-domains', '/migratable-vc-domains/enclosures', '/migratable-vc-domains/server-profiles']
groupingResLong = ['Migration', 'Migration:Networks and Network Sets', 'Migration:Enclosure', 'Migration:Profiles']


appliance_STATIC = {'type': 'ApplianceNetworkConfiguration',
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
                      'app1Ipv4Addr': '15.186.4.141',
                      'ipv6Type': 'UNCONFIGURE',
                      'hostname': 'I10-FlexFabric-HH.austin.hp.com',
                      'confOneNode': True,
                      'domainName': 'usa.hp.com',
                      'aliasDisabled': True,
                      }],
                    }

appliance_DHCP = {'type': 'ApplianceNetworkConfiguration',
                  'applianceNetworks':
                  [{'device': 'eth0',
                    'macAddress': None,
                    'interfaceName': '',
                    'activeNode': '1',
                    'unconfigure': False,
                    'ipv4Type': 'DHCP',
                    'ipv4Subnet': None,
                    'ipv4Gateway': None,
                    'ipv4NameServers': ['', ''],
                    'app1Ipv4Addr': None,
                    'ipv6Type': 'UNCONFIGURE',
                    'hostname': 'wpst-austin-vm.austin.hp.com',
                    'confOneNode': True,
                    'domainName': 'usa.hp.com',
                    'aliasDisabled': True,
                    }],
                  }

timeandlocale = {'type': 'TimeAndLocale', 'dateTime': None, 'timezone': 'UTC', 'ntpServers': ['ntp.hp.net'], 'locale': 'en_US.UTF-8'}

fts_admin_cred = {'userName': 'Administrator', 'password': 'hpvse123'}


vCenters = {
    "vc-vcenter03": {"vCenter_IP": 'vc-vcenter-03.usa.hp.com',
                     "vCenter_User": 'wpstuser',
                     "vCenter_Password": 'HPvse123',
                     "datacenter": "VCAL-Austin_LRVCb",
                     "cluster": 'WPST-OneView-LRVCb',
                     "network": 'LRVCb',
                     "datastores": ["WPST-Cluster-DS01", "WPST-Cluster-DS02", "WPST-Cluster-DS03", "WPST-Cluster-DS04"],
                     "target_Folder": "Austin_VMs",
                     "target_FolderPath": "WPST/WPST-VC/Austin_VMs"
                     },
    "wpstwork2": {"vCenter_IP": '15.186.4.110',
                  "vCenter_User": 'lliu',
                  "vCenter_Password": 'Compaq123',
                  "datacenter": 'austin-wpst',
                  'cluster': 'wpstcluster',
                  'network': 'hpqcorpnet',
                  "datastores": ["wpstcluster-datastore1", "wpstcluster-datastore2", "wpstcluster-datastore3"],
                  "target_Folder": "Austin_VMs",
                  "target_FolderPath": "development/Austin_VMs"
                  }
}

selectedVCenter = vCenters['vc-vcenter03']

default_variables = {
    "FUSION_SSH_USERNAME": 'root',             # Fusion SSH Username
    "FUSION_SSH_PASSWORD": 'hpvse1',           # Fusion SSH Password
    "FUSION_FACTORY_PASSWORD": "admin",        # Fusion Factory Default Password
    "FUSION_PROMPT": '#',
    "FUSION_TIMEOUT": 300,
    "excList": excList,
    "licenses": licenses,
    "appliance": appliance_DHCP,
    "timeandlocale": timeandlocale,
    "ADMIN_CRED": fts_admin_cred,
    "VCENTER_IP": selectedVCenter['vCenter_IP'],
    "VCENTER_USER": selectedVCenter['vCenter_User'],
    "VCENTER_PWD": selectedVCenter['vCenter_Password'],
    "VCENTER_DATACENTER": selectedVCenter['datacenter'],
    "VCENTER_NW": selectedVCenter['network'],
    "VCENTER_CLUSTER": selectedVCenter['cluster'],
    "VCENTER_DATASTORES": selectedVCenter['datastores'],
    "VCENTER_FOLDER": selectedVCenter['target_Folder'],
    "VCENTER_FOLDERPATH": selectedVCenter['target_FolderPath'],
    "TASK_GROUP_SN": groupingResShort,
    "TASK_GROUP_LN": groupingResLong
}


def get_variables():
    """Variable files can have a special get_variables method that returns variables as a mapping.
    """
    variables = default_variables

    return variables

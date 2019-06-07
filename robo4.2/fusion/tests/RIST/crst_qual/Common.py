"""Common items shared by all ring data files"""
ADMIN_CREDENTIALS = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
ILO_CREDENTIALS = {'username': 'Administrator', 'password': 'hpvse1-ilo'}
CFM_CREDENTIAlS = {'username': 'admin', 'password': 'plexxi'}

# DTO Types
APPLIANCE_NETWORK_CONFIGURATION_TYPE = 'ApplianceNetworkConfigurationV2'

ENCLOSURE_GROUP_TYPE = 'EnclosureGroupV7'
ENCLOSURE_TYPE = 'EnclosureV7'
ETHERNET_NETWORK_TYPE = 'ethernet-networkV4'
BULK_ETHERNET_NETWORK_TYPE = 'bulk-ethernet-networkV2'

FCOE_NETWORK_TYPE = 'fcoe-networkV4'
FC_NETWORK_TYPE = 'fc-networkV4'

INTERCONNECT_TYPE = 'InterconnectV4'

LOGICAL_INTERCONNECT_GROUP_TYPE = 'logical-interconnect-groupV6'

NETWORK_SET_TYPE = 'network-setV5'

SAS_LOGICAL_INTERCONNECT_GROUP_TYPE = 'sas-logical-interconnect-group'
SERVER_HARDWARE_TYPE = "server-hardware-10"
SERVER_PROFILE_TEMPLATE_TYPE = 'ServerProfileTemplateV6'
SERVER_PROFILE_TYPE = 'ServerProfileV11'
SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE = 'ServerProfileCompliancePreviewV1'
STORAGE_SYSTEM_TYPE = 'StorageSystemV4'

TIME_AND_LOCALE_TYPE = 'TimeAndLocale'

USER_AND_PERMISSION_TYPE = 'UserAndPermissions'
# End DTO Types

# http return codes
BADREQUEST = 400
FORBIDDEN = 403
OK = 200

support_dump = [{"errorCode": "CI", "encrypt": False}]

# Fabric
FABRIC_ADD_BODY = [{"op": "replace", "path": "/state", "value": "Adding"}]

ONEVIEW_CONFIG = {
    "host": "Passed_In_As_Variable",  # obtained from ${APPLIANCE_IP}
    "username": ADMIN_CREDENTIALS['userName'],
    "password": ADMIN_CREDENTIALS['password'],
    "description": "",
    "enabled": True,
    "verify_ssl": True,
    "name": "HPE OneView Configuration"
}

SHTypes = ["SHT:DL360 Gen10 1"]

APPLIANCE = {'type': APPLIANCE_NETWORK_CONFIGURATION_TYPE,
             'applianceNetworks':
             [{'device': 'eth0',
               'macAddress': None,
               'interfaceName': 'Appliance',
               'activeNode': '1',
               'unconfigure': False,
               'ipv4Type': 'STATIC',
               'app1Ipv4Addr': 'Set me to ${APPLIANCE_IP} at runtime',
               'ipv4Subnet': '255.255.240.0',
               'ipv4Gateway': '16.114.208.1',
               'ipv4NameServers': ['16.125.25.81', '16.125.25.82'],
               'hostname': 'Set me to ${OV_HOSTNAME} at runtime',
               'ipv6Type': 'UNCONFIGURE',
               'ipv6Gateway': '',
               'ipv6Subnet': '',
               'app1Ipv6Addr': '',
               'confOneNode': True,
               'domainName': 'Set me to ${DOMAIN} at runtime',
               'aliasDisabled': False,
               }]
             }
USERS = [
    {"type": USER_AND_PERMISSION_TYPE,
     "userName": "Serveradmin",
     "fullName": "Serveradmin",
     "password": "Serveradmin",
     "emailAddress": "sarah@hp.com",
     "officePhone": "970-555-0003",
     "mobilePhone": "970-500-0003",
     "enabled": True,
     "permissions": [{"roleName": "Server administrator",
                      "scopeUri": None}
                     ]
     },
    {'userName': 'Networkadmin',
     'password': 'Networkadmin',
     'fullName': 'Networkadmin',
     "permissions": [{"roleName": "Network administrator",
                      "scopeUri": None}
                     ],
     'emailAddress': 'nat@hp.com',
     'officePhone': '970-555-0003',
     'mobilePhone': '970-500-0003',
     'type': USER_AND_PERMISSION_TYPE},
    {'userName': 'Backupadmin',
     'password': 'Backupadmin',
     'fullName': 'Backupadmin',
     "permissions": [{"roleName": "Backup administrator",
                      "scopeUri": None}
                     ],
     'emailAddress': 'backup@hp.com',
     'officePhone': '970-555-0003',
     'mobilePhone': '970-500-0003',
     'type': USER_AND_PERMISSION_TYPE},
    {'userName': 'Noprivledge',
     'password': 'Noprivledge',
     'fullName': 'Noprivledge',
     "permissions": [{"roleName": "Read only",
                      "scopeUri": None}
                     ],
     'emailAddress': 'rheid@hp.com',
     'officePhone': '970-555-0003',
     'mobilePhone': '970-500-0003',
     'type': USER_AND_PERMISSION_TYPE}
]

LICENSES = [
    {'key':
        '9A9C DQAA H9PY CHV2 V7B5 HWWB Y9JL KMPL DJKD 5FFM DXAU 2CSM GHTG L762 TT66 VZRY KJVT D5KM EFVW DT5J EBE9 M2CC SPS9 YG66 Z99R MWSN 6Z84 46XT WZJL HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTFG LS8T XU4E "EVAL-HPOV-NFR1 HPOV-NFR1 HP_OneView_16_Seat_NFR 7T36AEJG7JJ9"_3MBSY-CJZY2-LDVV4-92DQT-L6TTW'},
    {'key':
        'AA9C DQAA H9PA GHX3 U7B5 HWW5 Y9JL KMPL SR6C MHJU DXAU 2CSM GHTG L762 9AVY WXJY KJVT D5KM EFVW DT5J TFQ9 74C8 SPS9 YG66 Z99R MWSN 6Z84 46XT WZJT HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTVG LS8T XU4E "EVAL-HPOV-NFR2 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR 9G6UAEJGUA4U"'},
]

# keyword requires lower case
timeandlocale = {'type': TIME_AND_LOCALE_TYPE,
                 'locale': 'en_US.UTF-8',
                 'timezone': 'UTC',
                 'ntpServers': [
                     '16.110.135.123'
                 ]
                 }

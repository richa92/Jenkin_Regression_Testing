#!/usr/bin/env python

admin_credentials = {'userName': 'Administrator', 'password': 'Nextgen9'}
timeandlocale = {'localeDisplayName': 'English (United States)', 'locale': 'en_US.UTF-8', 'dateTime': '2018-09-03T09:20:30.061Z', 'ntpServers': [], 'timezone': 'UTC', 'type': 'TimeAndLocale'}
licenses = [
    {
        'key': '9AAG CQAA H9PA 8HW3 V7B5 HWWB Y9JL KMPL DNCD 4CZE DXAU 2CSM GHTG L762 B582 VPRU KJVT D5KM EFVW DT5J FBYP 87S6 SPS9 YG66 Z99R MWSN 6Z84 46XT WZJL HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTFG LS8T XU4E "EVAL-HPOV-NFR1 HPOV-NFR1 HP_OneView_16_Seat_NFR 7T36AEJG7JJ9"'
    },
    {
        'key': 'YAQG DQAA H9PQ 8HV2 V7B5 HWWB Y9JL KMPL 3NSB 6CZE DXAU 2CSM GHTG L762 T566 GNB4 KJVT D5KM EFVW DT5J 5B9P M7S6 SPS9 YG66 Z99R MWSN 6Z84 46XT WZJL HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTFG LS8T XU4E "EVAL-HPOV-NFR1 HPOV-NFR1 HP_OneView_16_Seat_NFR 7T36AEJG7JJ9"'
    },
    {
        'key': 'YAYC CQAA H9PQ GHX2 U7B5 HWW5 Y9JL KMPL FJ2H PFFM DXAU 2CSM GHTG L762 WTC5 GYBQ KJVT D5KM EFVW DT5J EBUM 62CC SPS9 YG66 Z99R MWSN 6Z84 46XT WZJT HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTVG LS8T XU4E "EVAL-HPOV-NFR2 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR 9G6UAEJGUA4U"'
    },
    {
        'key': 'QA9C DQAA H9PY CHXZ V7B5 HWWB Y9JL KMPL LN6F 6GZ9 DXAU 2CSM GHTG L762 VZS7 XNNU KJVT D5KM EFVW DT5J MFQK N3SC SPS9 YG66 Z99R MWSN 6Z84 46XT WZJL HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTFG LS8T XU4E "EVAL-HPOV-NFR1 HPOV-NFR1 HP_OneView_16_Seat_NFR 7T36AEJG7JJ9"'
    },
    {
        'key': '9A9C DQAA H9PY CHV2 V7B5 HWWB Y9JL KMPL DJKD 5FFM DXAU 2CSM GHTG L762 TT66 VZRY KJVT D5KM EFVW DT5J EBE9 M2CC SPS9 YG66 Z99R MWSN 6Z84 46XT WZJL HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTFG LS8T XU4E "EVAL-HPOV-NFR1 HPOV-NFR1 HP_OneView_16_Seat_NFR 7T36AEJG7JJ9"'
    },
    {
        'key': 'YAQE DQAA H9PY 8HUY U7B5 HWW5 Y9JL KMPL UN6D NGJQ DXAU 2CSM GHTG L762 GMZ7 W9BA KJVT D5KM EFVW DT5J VBQJ 43CK SPS9 YG66 Z99R MWSN 6Z84 46XT WZJT HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTVG LS8T XU4E "EVAL-HPOV-NFR2 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR 9G6UAEJGUA4U"'
    },
    {
        'key': '9AYC BQAA H9PQ GHXY U7B5 HWW5 Y9JL KMPL 3JSH 4FVM DXAU 2CSM GHTG L762 ETCZ WZRE KJVT D5KM EFVW DT5J 4BMM P2SC SPS9 YG66 Z99R MWSN 6Z84 46XT WZJT HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTVG LS8T XU4E "EVAL-HPOV-NFR2 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR 9G6UAEJGUA4U"'
    },
    {
        'key': 'AA9C AQAA H9PY CHVY V7B5 HWWB Y9JL KMPL 3JKH 5FVM DXAU 2CSM GHTG L762 MTK7 FYB9 KJVT D5KM EFVW DT5J 4BEM M2SC SPS9 YG66 Z99R MWSN 6Z84 46XT WZJL HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTFG LS8T XU4E "EVAL-HPOV-NFR1 HPOV-NFR1 HP_OneView_16_Seat_NFR 7T36AEJG7JJ9"'
    },
    {
        'key': 'AAYA AQAA H9PQ 8HX3 U7B5 HWW5 Y9JL KMPL ENWB 5GZQ DXAU 2CSM GHTG L762 BMJ3 HPBM KJVT D5KM EFVW DT5J HB9P P3SK SPS9 YG66 Z99R MWSN 6Z84 46XT WZJT HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTVG LS8T XU4E "EVAL-HPOV-NFR2 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR 9G6UAEJGUA4U"'
    },
    {
        'key': 'QAYA AQAA H9PA 8HVZ U7B5 HWW5 Y9JL KMPL TNCF 7CJE DXAU 2CSM GHTG L762 L5S6 VNRA KJVT D5KM EFVW DT5J VBYJ 87C6 SPS9 YG66 Z99R MWSN 6Z84 46XT WZJT HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTVG LS8T XU4E "EVAL-HPOV-NFR2 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR 9G6UAEJGUA4U"'
    },
    {
        'key': 'QAYE DQAA H9P9 GHX3 U7B5 HWW5 Y9JL KMPL FNGH PGJ9 DXAU 2CSM GHTG L762 PZC7 HN5Y KJVT D5KM EFVW DT5J EFYK 63CC SPS9 YG66 Z99R MWSN 6Z84 46XT WZJT HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTVG LS8T XU4E "EVAL-HPOV-NFR2 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR 9G6UAEJGUA4U"'
    },
    {
        'key': 'AAYC BQAA H9P9 KHXY V7B5 HWWB Y9JL KMPL JN6B 6HJ9 DXAU 2CSM GHTG L762 ZBW4 XN5A KJVT D5KM EFVW DT5J KFQ8 M4CC SPS9 YG66 Z99R MWSN 6Z84 46XT WZJL HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTFG LS8T XU4E "EVAL-HPOV-NFR1 HPOV-NFR1 HP_OneView_16_Seat_NFR 7T36AEJG7JJ9"'
    }
]

appliance = {
    'type': "ApplianceNetworkConfigurationV2",
    'applianceNetworks':
    [{
        "device": "eth0",
        "macAddress": "52:54:00:df:60:76",
        "interfaceName": "Appliance",
        "activeNode": 1,
        "unconfigure": False,
        "ipv4Type": "STATIC",
        "ipv4Subnet": "255.255.255.0",
        "ipv4Gateway": "172.25.11.1",
        "ipv4NameServers": [u'172.25.104.104'],
        "app1Ipv4Addr": "172.25.11.180",
        "ipv6Type": "UNCONFIGURE",
        "hostname": "ci-525400df6076.fusion.com",
        "confOneNode": True,
        "domainName": "fusion.com",
        "aliasDisabled": False
    }]
}
users = [
    {
        "type": "UserAndPermissions",
        "password": "Cosmos123",
        "userName": "SA12",
        "permissions": [{u'roleName': u'Storage administrator', u'scopeUri': u'/rest/scopes/b141f364-0eaa-49f5-b93b-484d5ca32eea'}],
        "emailAddress": "",
        "officePhone": "",
        "mobilePhone": ""
    },
    {
        "type": "UserAndPermissions",
        "password": "Cosmos123",
        "userName": "SFO",
        "permissions": [{u'roleName': u'Server firmware operator', u'scopeUri': u'/rest/scopes/a26da32f-fe19-4521-9168-1e6d017d1218'}],
        "emailAddress": "",
        "officePhone": "",
        "mobilePhone": ""
    },
    {
        "type": "UserAndPermissions",
        "password": "Cosmos123",
        "userName": "SPA",
        "permissions": [{u'roleName': u'Server profile administrator', u'scopeUri': None}],
        "emailAddress": "",
        "officePhone": "",
        "mobilePhone": ""
    },
    {
        "type": "UserAndPermissions",
        "password": "Cosmos123",
        "userName": "SPO",
        "permissions": [{u'roleName': u'Server profile operator', u'scopeUri': u'/rest/scopes/e624b24c-6eb9-41ba-9624-6feab7bfb342'}],
        "emailAddress": "",
        "officePhone": "",
        "mobilePhone": ""
    },
    {
        "type": "UserAndPermissions",
        "password": "Cosmos123",
        "userName": "administrator",
        "permissions": [{u'roleName': u'Infrastructure administrator', u'scopeUri': None}],
        "emailAddress": "",
        "officePhone": "",
        "mobilePhone": ""
    },
    {
        "type": "UserAndPermissions",
        "password": "Cosmos123",
        "userName": "sa",
        "permissions": [{u'roleName': u'Server administrator', u'scopeUri': u'/rest/scopes/e624b24c-6eb9-41ba-9624-6feab7bfb342'}],
        "emailAddress": "",
        "officePhone": "",
        "mobilePhone": ""
    },
    {
        "type": "UserAndPermissions",
        "password": "Cosmos123",
        "userName": "spo_sfo",
        "permissions": [{u'roleName': u'Server profile operator', u'scopeUri': None}, {u'roleName': u'Server firmware operator', u'scopeUri': None}],
        "emailAddress": "",
        "officePhone": "",
        "mobilePhone": ""
    }
]
expected_users = [
    {
        "enabled": True,
        "name": None,
        "category": "users",
        "fullName": "",
        "status": None,
        "type": "UserAndPermissions",
        "userName": "SA12",
        "permissions": [{u'roleName': u'Storage administrator', u'scopeUri': u'/rest/scopes/b141f364-0eaa-49f5-b93b-484d5ca32eea'}],
        "emailAddress": "",
        "officePhone": "",
        "mobilePhone": ""
    },
    {
        "enabled": True,
        "name": None,
        "category": "users",
        "fullName": "",
        "status": None,
        "type": "UserAndPermissions",
        "userName": "SFO",
        "permissions": [{u'roleName': u'Server firmware operator', u'scopeUri': u'/rest/scopes/a26da32f-fe19-4521-9168-1e6d017d1218'}],
        "emailAddress": "",
        "officePhone": "",
        "mobilePhone": ""
    },
    {
        "enabled": True,
        "name": None,
        "category": "users",
        "fullName": "",
        "status": None,
        "type": "UserAndPermissions",
        "userName": "SPA",
        "permissions": [{u'roleName': u'Server profile administrator', u'scopeUri': None}],
        "emailAddress": "",
        "officePhone": "",
        "mobilePhone": ""
    },
    {
        "enabled": True,
        "name": None,
        "category": "users",
        "fullName": "",
        "status": None,
        "type": "UserAndPermissions",
        "userName": "SPO",
        "permissions": [{u'roleName': u'Server profile operator', u'scopeUri': u'/rest/scopes/e624b24c-6eb9-41ba-9624-6feab7bfb342'}],
        "emailAddress": "",
        "officePhone": "",
        "mobilePhone": ""
    },
    {
        "enabled": True,
        "name": None,
        "category": "users",
        "fullName": "Default appliance administrator",
        "status": None,
        "type": "UserAndPermissions",
        "userName": "administrator",
        "permissions": [{u'roleName': u'Infrastructure administrator', u'scopeUri': None}],
        "emailAddress": "",
        "officePhone": "",
        "mobilePhone": ""
    },
    {
        "enabled": True,
        "name": None,
        "category": "users",
        "fullName": "",
        "status": None,
        "type": "UserAndPermissions",
        "userName": "sa",
        "permissions": [{u'roleName': u'Server administrator', u'scopeUri': u'/rest/scopes/e624b24c-6eb9-41ba-9624-6feab7bfb342'}],
        "emailAddress": "",
        "officePhone": "",
        "mobilePhone": ""
    },
    {
        "enabled": True,
        "name": None,
        "category": "users",
        "fullName": "",
        "status": None,
        "type": "UserAndPermissions",
        "userName": "spo_sfo",
        "permissions": [{u'roleName': u'Server profile operator', u'scopeUri': None}, {u'roleName': u'Server firmware operator', u'scopeUri': None}],
        "emailAddress": "",
        "officePhone": "",
        "mobilePhone": ""
    }
]

san_managers = [
    {
        "connectionInfo": [
            {
                "name": 'type',
                "value": 'HPE',
            },
            {
                "name": "Host",
                "value": "172.25.9.22"
            },
            {
                "name": "SnmpPort",
                "value": 161
            },
            {
                "name": "SnmpUserName",
                "value": "defaultUser"
            },
            {
                "name": "SnmpAuthLevel",
                "value": "authpriv"
            },
            {
                "name": "SnmpAuthString",
                "value": "authPass123"
            },
            {
                "name": "SnmpPrivString",
                "value": "privPass123"
            },
            {
                "name": "SnmpAuthProtocol",
                "value": "md5"
            },
            {
                "name": "SnmpPrivProtocol",
                "value": "aes"
            }
        ]
    },
    {
        "connectionInfo": [
            {
                "name": 'type',
                "value": 'Brocade Network Advisor',
            },
            {
                "name": "Host",
                "value": "172.25.9.127"
            },
            {
                "name": "Port",
                "value": 5989
            },
            {
                "name": "UseSsl",
                "value": True
            },
            {
                "name": "Password",
                "value": "password"
            },
            {
                "name": "Username",
                "value": "Administrator"
            }
        ]
    },
    {
        "connectionInfo": [
            {
                "name": 'type',
                "value": 'HPE',
            },
            {
                "name": "Host",
                "value": "172.25.9.21"
            },
            {
                "name": "SnmpPort",
                "value": 161
            },
            {
                "name": "SnmpUserName",
                "value": "defaultUser"
            },
            {
                "name": "SnmpAuthLevel",
                "value": "authpriv"
            },
            {
                "name": "SnmpAuthString",
                "value": "authPass123"
            },
            {
                "name": "SnmpPrivString",
                "value": "privPass123"
            },
            {
                "name": "SnmpAuthProtocol",
                "value": "md5"
            },
            {
                "name": "SnmpPrivProtocol",
                "value": "aes"
            }
        ]
    }
]
expected_san_managers = [
    {
        "uri": "SAN:172.25.9.22",
        "name": "172.25.9.22",
        "type": "FCDeviceManagerV2",
        "category": "fc-device-managers",
        "state": "Managed",
        "description": "HPE 5900AF-48XG-4QSFP+ Switch",
        "deviceManagerVersion": "7.1.045 Release 2422P03",
        "isInternal": "False",
        "providerDisplayName": "HPE",
        "refreshState": "Stable",
        "status": "OK",
        "connectionInfo": [
            {
                "name": "Host",
                "value": "172.25.9.22"
            },
            {
                "name": "SnmpPort",
                "value": 161
            },
            {
                "name": "SnmpUserName",
                "value": "defaultUser"
            },
            {
                "name": "SnmpAuthLevel",
                "value": "authpriv"
            },
            {
                "name": "SnmpAuthString",
                "value": ""
            },
            {
                "name": "SnmpPrivString",
                "value": ""
            },
            {
                "name": "SnmpAuthProtocol",
                "value": "md5"
            },
            {
                "name": "SnmpPrivProtocol",
                "value": "aes"
            }
        ]
    },
    {
        "uri": "SAN:172.25.9.127",
        "name": "172.25.9.127",
        "type": "FCDeviceManagerV2",
        "category": "fc-device-managers",
        "state": "Managed",
        "description": "Brocade Network Advisor",
        "deviceManagerVersion": "14.0.1.170",
        "isInternal": "False",
        "providerDisplayName": "Brocade Network Advisor",
        "refreshState": "Stable",
        "status": "OK",
        "connectionInfo": [
            {
                "name": "Host",
                "value": "172.25.9.127"
            },
            {
                "name": "Port",
                "value": 5989
            },
            {
                "name": "UseSsl",
                "value": True
            },
            {
                "name": "Password",
                "value": ""
            },
            {
                "name": "Username",
                "value": "Administrator"
            }
        ]
    },
    {
        "uri": "SAN:172.25.9.21",
        "name": "172.25.9.21",
        "type": "FCDeviceManagerV2",
        "category": "fc-device-managers",
        "state": "Managed",
        "description": "HP 5900AF-48XG-4QSFP+ Switch",
        "deviceManagerVersion": "7.1.045 Release 2416",
        "isInternal": "False",
        "providerDisplayName": "HPE",
        "refreshState": "Stable",
        "status": "OK",
        "connectionInfo": [
            {
                "name": "Host",
                "value": "172.25.9.21"
            },
            {
                "name": "SnmpPort",
                "value": 161
            },
            {
                "name": "SnmpUserName",
                "value": "defaultUser"
            },
            {
                "name": "SnmpAuthLevel",
                "value": "authpriv"
            },
            {
                "name": "SnmpAuthString",
                "value": ""
            },
            {
                "name": "SnmpPrivString",
                "value": ""
            },
            {
                "name": "SnmpAuthProtocol",
                "value": "md5"
            },
            {
                "name": "SnmpPrivProtocol",
                "value": "aes"
            }
        ]
    }
]

ethernet_networks = [
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth1_1098",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1098
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth1_1097",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1097
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth1_1096",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1096
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth2_1097",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1097
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "iscsi1",
        "privateNetwork": False,
        "purpose": "ISCSI",
        "smartLink": True,
        "vlanId": 1009
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "iscsi2",
        "privateNetwork": False,
        "purpose": "ISCSI",
        "smartLink": True,
        "vlanId": 1009
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "VSA_Iscsi2",
        "privateNetwork": False,
        "purpose": "ISCSI",
        "smartLink": True,
        "vlanId": 1026
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "vsa_iscsi1",
        "privateNetwork": False,
        "purpose": "ISCSI",
        "smartLink": True,
        "vlanId": 1025
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth2_1096",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1096
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth2_1098",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1098
    }
]
expected_ethernet_networks = [
    {
        "uri": "ETH:eth1_1098",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth1_1098",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1098
    },
    {
        "uri": "ETH:eth1_1097",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth1_1097",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1097
    },
    {
        "uri": "ETH:eth1_1096",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth1_1096",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1096
    },
    {
        "uri": "ETH:eth2_1097",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth2_1097",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1097
    },
    {
        "uri": "ETH:iscsi1",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "iscsi1",
        "privateNetwork": False,
        "purpose": "ISCSI",
        "smartLink": True,
        "vlanId": 1009
    },
    {
        "uri": "ETH:iscsi2",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "iscsi2",
        "privateNetwork": False,
        "purpose": "ISCSI",
        "smartLink": True,
        "vlanId": 1009
    },
    {
        "uri": "ETH:VSA_Iscsi2",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "VSA_Iscsi2",
        "privateNetwork": False,
        "purpose": "ISCSI",
        "smartLink": True,
        "vlanId": 1026
    },
    {
        "uri": "ETH:vsa_iscsi1",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "vsa_iscsi1",
        "privateNetwork": False,
        "purpose": "ISCSI",
        "smartLink": True,
        "vlanId": 1025
    },
    {
        "uri": "ETH:eth2_1096",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth2_1096",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1096
    },
    {
        "uri": "ETH:eth2_1098",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth2_1098",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1098
    }
]

fc_networks = [
    {
        "type": "fc-networkV4",
        "name": "das1",
        "fabricType": "DirectAttach",
        "linkStabilityTime": 0,
        "autoLoginRedistribution": False,
        "managedSanUri": None
    },
    {
        "type": "fc-networkV4",
        "name": "fc2",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:NFV-BNA-SW2"
    },
    {
        "type": "fc-networkV4",
        "name": "das2",
        "fabricType": "DirectAttach",
        "linkStabilityTime": 0,
        "autoLoginRedistribution": False,
        "managedSanUri": None
    },
    {
        "type": "fc-networkV4",
        "name": "fc1",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:NFV-BNA-SW1"
    }
]
expected_fc_networks = [
    {
        "category": "fc-networks",
        "state": "Active",
        "description": None,
        "uri": "FC:das1",
        "status": "OK",
        "type": "fc-networkV4",
        "name": "das1",
        "fabricType": "DirectAttach",
        "linkStabilityTime": 0,
        "autoLoginRedistribution": False,
        "managedSanUri": None
    },
    {
        "category": "fc-networks",
        "state": "Active",
        "description": None,
        "uri": "FC:fc2",
        "status": "OK",
        "type": "fc-networkV4",
        "name": "fc2",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:NFV-BNA-SW2"
    },
    {
        "category": "fc-networks",
        "state": "Active",
        "description": None,
        "uri": "FC:das2",
        "status": "OK",
        "type": "fc-networkV4",
        "name": "das2",
        "fabricType": "DirectAttach",
        "linkStabilityTime": 0,
        "autoLoginRedistribution": False,
        "managedSanUri": None
    },
    {
        "category": "fc-networks",
        "state": "Active",
        "description": None,
        "uri": "FC:fc1",
        "status": "OK",
        "type": "fc-networkV4",
        "name": "fc1",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:NFV-BNA-SW1"
    }
]

fcoe_networks = [
    {
        "name": "fcoe2",
        "type": "fcoe-networkV4",
        "vlanId": 1022,
        "managedSanUri": "FCSan:VSAN1022"
    },
    {
        "name": "fcoe1",
        "type": "fcoe-networkV4",
        "vlanId": 1021,
        "managedSanUri": "FCSan:VSAN1021"
    }
]
expected_fcoe_networks = [
    {
        "uri": "FCOE:fcoe2",
        "state": "Active",
        "status": "OK",
        "name": "fcoe2",
        "type": "fcoe-networkV4",
        "vlanId": 1022,
        "managedSanUri": "FCSan:VSAN1022"
    },
    {
        "uri": "FCOE:fcoe1",
        "state": "Active",
        "status": "OK",
        "name": "fcoe1",
        "type": "fcoe-networkV4",
        "vlanId": 1021,
        "managedSanUri": "FCSan:VSAN1021"
    }
]

networksets = [
    {
        "type": "network-setV4",
        "name": "SET2",
        "nativeNetworkUri": None,
        "networkUris": [
            "eth2_1098",
            "eth2_1096",
            "eth2_1097"
        ]
    },
    {
        "type": "network-setV4",
        "name": "SET1",
        "nativeNetworkUri": None,
        "networkUris": [
            "eth1_1098",
            "eth1_1096",
            "eth1_1097"
        ]
    }
]
expected_networksets = [
    {
        "category": "network-sets",
        "state": "Active",
        "description": None,
        "uri": "NS:SET2",
        "status": "OK",
        "type": "network-setV4",
        "name": "SET2",
        "nativeNetworkUri": None,
        "networkUris": [
            "ETH:eth2_1098",
            "ETH:eth2_1096",
            "ETH:eth2_1097"
        ]
    },
    {
        "category": "network-sets",
        "state": "Active",
        "description": None,
        "uri": "NS:SET1",
        "status": "OK",
        "type": "network-setV4",
        "name": "SET1",
        "nativeNetworkUri": None,
        "networkUris": [
            "ETH:eth1_1098",
            "ETH:eth1_1096",
            "ETH:eth1_1097"
        ]
    }
]

storage_systems_with_pools = [
    {
        "credentials": {'username': 'cosmos', 'password': 'Nextgen9'},
        "name": "COSMOS-7400-9.125",
        "family": "StoreServ",
        "hostname": "172.25.9.125",
        "deviceSpecificAttributes": {
            "managedDomain": "Cosmos-MainStream",
            "managedPools": [{'domain': 'Cosmos-MainStream', 'name': 'MainStream-CPG', 'raidLevel': 'RAID5', 'state': 'Managed', 'deviceType': 'FC', 'freeCapacity': '400505700352', 'totalCapacity': '1099511627776', 'uuid': '63c15e24-d9f3-48b4-a416-7f65d94884c4'}],
            "discoveredPools": [],

        },
    },
    {
        "credentials": {'username': 'cosmos', 'password': 'Nextgen9'},
        "name": "COSMOS-P7400-9.110",
        "family": "StoreServ",
        "hostname": "172.25.9.110",
        "deviceSpecificAttributes": {
            "managedDomain": "COSMOS",
            "managedPools": [{'domain': 'COSMOS', 'name': 'asds', 'raidLevel': 'RAID0', 'state': 'Managed', 'deviceType': 'FC', 'freeCapacity': '1806033747968', 'totalCapacity': '2974264852480', 'uuid': 'cd0f1f1e-29ca-4280-9d6b-4f33c9e9cf88'}, {'domain': 'COSMOS', 'name': 'cosmos-cpg', 'raidLevel': 'RAID0', 'state': 'Managed', 'deviceType': 'FC', 'freeCapacity': '1806033747968', 'totalCapacity': '3906272755712', 'uuid': 'a5980e24-091d-47f4-ac02-977fb11ec5cd'}, {'domain': 'COSMOS', 'name': 'FC_r1', 'raidLevel': 'RAID1', 'state': 'Managed', 'deviceType': 'FC', 'freeCapacity': '897648164864', 'totalCapacity': '897648164864', 'uuid': 'a31b7e03-843c-454c-ace7-7d72f49d47e8'}, {'domain': 'COSMOS', 'name': 'FC_r5', 'raidLevel': 'RAID5', 'state': 'Managed', 'deviceType': 'FC', 'freeCapacity': '1327144894464', 'totalCapacity': '1327144894464', 'uuid': '8797b209-b00c-4d1a-b499-075999bc66d2'}, {'domain': 'COSMOS', 'name': 'Test-CPG-change.1', 'raidLevel': 'RAID0', 'state': 'Managed', 'deviceType': 'FC', 'freeCapacity': '1806033747968', 'totalCapacity': '1891933093888', 'uuid': 'e438fcae-86d8-4286-aa15-11c2742e9fb0'}],
            "discoveredPools": [],

        },
    },
    {
        "credentials": {'username': 'admin', 'password': 'Cosmos123'},
        "name": "Cosmos_Cluster",
        "family": "StoreVirtual",
        "hostname": "172.25.16.4"
    },
    {
        "credentials": {'username': 'admin', 'password': 'Cosmos123'},
        "name": "Cosmos_HWVSAClust",
        "family": "StoreVirtual",
        "hostname": "172.25.15.4"
    }
]
expected_storage_systems_with_pools = [
    {
        "uri": "SSYS:COSMOS-7400-9.125",
        "type": "StorageSystemV5",
        "state": "Managed",
        "category": "storage-systems",
        "status": "OK",
        "name": "COSMOS-7400-9.125",
        "family": "StoreServ",
        "hostname": "172.25.9.125",
        "deviceSpecificAttributes": {
            "managedDomain": "Cosmos-MainStream",
            "serialNumber": "1615657"
        },
    },
    {
        "uri": "SSYS:COSMOS-P7400-9.110",
        "type": "StorageSystemV5",
        "state": "Managed",
        "category": "storage-systems",
        "status": "OK",
        "name": "COSMOS-P7400-9.110",
        "family": "StoreServ",
        "hostname": "172.25.9.110",
        "deviceSpecificAttributes": {
            "managedDomain": "COSMOS",
            "serialNumber": "1644257"
        },
    },
    {
        "uri": "SSYS:Cosmos_Cluster",
        "type": "StorageSystemV5",
        "state": "Managed",
        "category": "storage-systems",
        "status": "OK",
        "name": "Cosmos_Cluster",
        "family": "StoreVirtual",
        "hostname": "172.25.16.4"
    },
    {
        "uri": "SSYS:Cosmos_HWVSAClust",
        "type": "StorageSystemV5",
        "state": "Managed",
        "category": "storage-systems",
        "status": "OK",
        "name": "Cosmos_HWVSAClust",
        "family": "StoreVirtual",
        "hostname": "172.25.15.4"
    }
]

storage_pools_toedit = [
    {
        "storageSystemUri": "Cosmos_Cluster",
        "name": "Cosmos_Cluster",
        "isManaged": True,
    },
    {
        "storageSystemUri": "COSMOS-7400-9.125",
        "name": "MainStream-CPG",
        "isManaged": True,
    },
    {
        "storageSystemUri": "COSMOS-P7400-9.110",
        "name": "asds",
        "isManaged": True,
    },
    {
        "storageSystemUri": "COSMOS-P7400-9.110",
        "name": "cosmos-cpg",
        "isManaged": True,
    },
    {
        "storageSystemUri": "COSMOS-P7400-9.110",
        "name": "FC_r1",
        "isManaged": True,
    },
    {
        "storageSystemUri": "COSMOS-P7400-9.110",
        "name": "FC_r5",
        "isManaged": True,
    },
    {
        "storageSystemUri": "COSMOS-P7400-9.110",
        "name": "Test-CPG-change.1",
        "isManaged": True,
    },
    {
        "storageSystemUri": "Cosmos_HWVSAClust",
        "name": "Cosmos_HWVSAClust",
        "isManaged": True,
    }
]

add_existing_storage_volumes = [
]
expected_existing_storage_volumes = [
]
storage_volume_templates = [
    {
        "name": "Volume_temp1",
        "description": "",
        "properties": {
            "description": {
                "description": "A description for the volume",
                "title": "Description",
                "default": "",
                "minLength": 0,
                "meta": {
                    "locked": False,
                },
                "maxLength": 2000,
                "type": "string",
            },
            "name": {
                "description": "A volume name between 1 and 100 characters",
                "title": "Volume name",
                "minLength": 1,
                "required": True,
                "meta": {
                    "locked": False,
                },
                "maxLength": 100,
                "type": "string",
            },
            "storagePool": {
                "description": "StoragePoolURI the volume should be added to",
                "format": "x-uri-reference",
                "default": "Cosmos_Cluster",
                "required": True,
                "meta": {
                    "createOnly": True,
                    "semanticType": "device-storage-pool",
                    "locked": False,
                },
                "title": "Storage Pool",
                "type": "string",
            },
            "provisioningType": {
                "description": "The provisioning type for the volume",
                "title": "Provisioning Type",
                "default": "Thin",
                "enum": [u'Thin', u'Full'],
                "meta": {
                    "createOnly": "true",
                    "semanticType": "device-provisioningType",
                    "locked": True,
                },
                "type": "string",
            },
            "isShareable": {
                "default": False,
                "meta": {
                    "locked": False,
                },
                "type": "boolean",
                "description": "The shareability of the volume",
                "title": "Is Shareable",
            },
            "size": {
                "description": "Capacity of the volume in bytes",
                "title": "Capacity",
                "default": 1073741824,
                "required": True,
                "maximum": 17592186044416,
                "minimum": 1073741824,
                "meta": {
                    "semanticType": "capacity",
                    "locked": False,
                },
                "type": "integer",
            },
        },
    },
    {
        "name": "volume_temp2",
        "description": "",
        "properties": {
            "description": {
                "description": "A description for the volume",
                "title": "Description",
                "default": "",
                "minLength": 0,
                "meta": {
                    "locked": False,
                },
                "maxLength": 2000,
                "type": "string",
            },
            "name": {
                "description": "A volume name between 1 and 100 characters",
                "title": "Volume name",
                "minLength": 1,
                "required": True,
                "meta": {
                    "locked": False,
                },
                "maxLength": 100,
                "type": "string",
            },
            "storagePool": {
                "description": "StoragePoolURI the volume should be added to",
                "format": "x-uri-reference",
                "default": "Cosmos_Cluster",
                "required": True,
                "meta": {
                    "createOnly": True,
                    "semanticType": "device-storage-pool",
                    "locked": False,
                },
                "title": "Storage Pool",
                "type": "string",
            },
            "provisioningType": {
                "description": "The provisioning type for the volume",
                "title": "Provisioning Type",
                "default": "Thin",
                "enum": [u'Thin', u'Full'],
                "meta": {
                    "createOnly": "true",
                    "semanticType": "device-provisioningType",
                    "locked": True,
                },
                "type": "string",
            },
            "isShareable": {
                "default": False,
                "meta": {
                    "locked": False,
                },
                "type": "boolean",
                "description": "The shareability of the volume",
                "title": "Is Shareable",
            },
            "size": {
                "description": "Capacity of the volume in bytes",
                "title": "Capacity",
                "default": 1073741824,
                "required": True,
                "maximum": 17592186044416,
                "minimum": 1073741824,
                "meta": {
                    "semanticType": "capacity",
                    "locked": False,
                },
                "type": "integer",
            },
        },
    },
    {
        "name": "vt12",
        "description": "",
        "properties": {
            "description": {
                "description": "A description for the volume",
                "title": "Description",
                "default": "",
                "minLength": 0,
                "meta": {
                    "locked": False,
                },
                "maxLength": 2000,
                "type": "string",
            },
            "name": {
                "description": "A volume name between 1 and 100 characters",
                "title": "Volume name",
                "minLength": 1,
                "required": True,
                "meta": {
                    "locked": False,
                },
                "maxLength": 100,
                "type": "string",
            },
            "snapshotPool": {
                "description": "A URI reference to the common provisioning group used to create snapshots",
                "format": "x-uri-reference",
                "default": "MainStream-CPG",
                "title": "Snapshot Pool",
                "meta": {
                    "semanticType": "device-snapshot-storage-pool",
                    "locked": True,
                },
                "type": "string",
            },
            "storagePool": {
                "description": "A common provisioning group URI reference",
                "format": "x-uri-reference",
                "default": "MainStream-CPG",
                "required": True,
                "meta": {
                    "createOnly": True,
                    "semanticType": "device-storage-pool",
                    "locked": False,
                },
                "title": "Storage Pool",
                "type": "string",
            },
            "provisioningType": {
                "description": "The provisioning type for the volume",
                "title": "Provisioning Type",
                "default": "Thin",
                "enum": [u'Thin', u'Full'],
                "meta": {
                    "createOnly": True,
                    "locked": True,
                },
                "type": "string",
            },
            "isShareable": {
                "default": False,
                "meta": {
                    "locked": False,
                },
                "type": "boolean",
                "description": "The shareability of the volume",
                "title": "Is Shareable",
            },
            "size": {
                "description": "The capacity of the volume in bytes",
                "title": "Capacity",
                "default": 1073741824,
                "required": True,
                "maximum": 17592186044416,
                "minimum": 1073741824,
                "meta": {
                    "semanticType": "capacity",
                    "locked": False,
                },
                "type": "integer",
            },
        },
    },
    {
        "name": "temp",
        "description": "",
        "properties": {
            "description": {
                "description": "A description for the volume",
                "title": "Description",
                "default": "",
                "minLength": 0,
                "meta": {
                    "locked": False,
                },
                "maxLength": 2000,
                "type": "string",
            },
            "name": {
                "description": "A volume name between 1 and 100 characters",
                "title": "Volume name",
                "minLength": 1,
                "required": True,
                "meta": {
                    "locked": False,
                },
                "maxLength": 100,
                "type": "string",
            },
            "snapshotPool": {
                "description": "A URI reference to the common provisioning group used to create snapshots",
                "format": "x-uri-reference",
                "default": "cosmos-cpg",
                "title": "Snapshot Pool",
                "meta": {
                    "semanticType": "device-snapshot-storage-pool",
                    "locked": True,
                },
                "type": "string",
            },
            "storagePool": {
                "description": "A common provisioning group URI reference",
                "format": "x-uri-reference",
                "default": "cosmos-cpg",
                "required": True,
                "meta": {
                    "createOnly": True,
                    "semanticType": "device-storage-pool",
                    "locked": False,
                },
                "title": "Storage Pool",
                "type": "string",
            },
            "provisioningType": {
                "description": "The provisioning type for the volume",
                "title": "Provisioning Type",
                "default": "Thin",
                "enum": [u'Thin', u'Full'],
                "meta": {
                    "createOnly": True,
                    "locked": True,
                },
                "type": "string",
            },
            "isShareable": {
                "default": False,
                "meta": {
                    "locked": True,
                },
                "type": "boolean",
                "description": "The shareability of the volume",
                "title": "Is Shareable",
            },
            "size": {
                "description": "The capacity of the volume in bytes",
                "title": "Capacity",
                "default": 1073741824,
                "required": True,
                "maximum": 17592186044416,
                "minimum": 1073741824,
                "meta": {
                    "semanticType": "capacity",
                    "locked": True,
                },
                "type": "integer",
            },
        },
    },
    {
        "name": "VT",
        "description": "",
        "properties": {
            "description": {
                "description": "A description for the volume",
                "title": "Description",
                "default": "",
                "minLength": 0,
                "meta": {
                    "locked": False,
                },
                "maxLength": 2000,
                "type": "string",
            },
            "name": {
                "description": "A volume name between 1 and 100 characters",
                "title": "Volume name",
                "minLength": 1,
                "required": True,
                "meta": {
                    "locked": False,
                },
                "maxLength": 100,
                "type": "string",
            },
            "snapshotPool": {
                "description": "A URI reference to the common provisioning group used to create snapshots",
                "format": "x-uri-reference",
                "default": "MainStream-CPG",
                "title": "Snapshot Pool",
                "meta": {
                    "semanticType": "device-snapshot-storage-pool",
                    "locked": True,
                },
                "type": "string",
            },
            "storagePool": {
                "description": "A common provisioning group URI reference",
                "format": "x-uri-reference",
                "default": "MainStream-CPG",
                "required": True,
                "meta": {
                    "createOnly": True,
                    "semanticType": "device-storage-pool",
                    "locked": False,
                },
                "title": "Storage Pool",
                "type": "string",
            },
            "provisioningType": {
                "description": "The provisioning type for the volume",
                "title": "Provisioning Type",
                "default": "Thin",
                "enum": [u'Thin', u'Full'],
                "meta": {
                    "createOnly": True,
                    "locked": True,
                },
                "type": "string",
            },
            "isShareable": {
                "default": False,
                "meta": {
                    "locked": False,
                },
                "type": "boolean",
                "description": "The shareability of the volume",
                "title": "Is Shareable",
            },
            "size": {
                "description": "The capacity of the volume in bytes",
                "title": "Capacity",
                "default": 1073741824,
                "required": True,
                "maximum": 17592186044416,
                "minimum": 1073741824,
                "meta": {
                    "semanticType": "capacity",
                    "locked": False,
                },
                "type": "integer",
            },
        }
    }
]
expected_storage_volume_templates = [
    {
        "category": "storage-volume-templates",
        "state": "Configured",
        "type": "StorageVolumeTemplateV6",
        "uri": "SVT:Volume_temp1",
        "status": "OK",
        "name": "Volume_temp1",
        "description": "",
        "properties": {
            "description": {
                "description": "A description for the volume",
                "title": "Description",
                "default": "",
                "minLength": 0,
                "meta": {
                    "locked": False,
                },
                "maxLength": 2000,
                "type": "string",
            },
            "name": {
                "description": "A volume name between 1 and 100 characters",
                "title": "Volume name",
                "minLength": 1,
                "required": True,
                "meta": {
                    "locked": False,
                },
                "maxLength": 100,
                "type": "string",
            },
            "storagePool": {
                "description": "StoragePoolURI the volume should be added to",
                "format": "x-uri-reference",
                "default": "SPOOL:Cosmos_Cluster",
                "required": True,
                "meta": {
                    "createOnly": True,
                    "semanticType": "device-storage-pool",
                    "locked": False,
                },
                "title": "Storage Pool",
                "type": "string",
            },
            "provisioningType": {
                "description": "The provisioning type for the volume",
                "title": "Provisioning Type",
                "default": "Thin",
                "enum": [u'Thin', u'Full'],
                "meta": {
                    "createOnly": "true",
                    "semanticType": "device-provisioningType",
                    "locked": True,
                },
                "type": "string",
            },
            "isShareable": {
                "default": False,
                "meta": {
                    "locked": False,
                },
                "type": "boolean",
                "description": "The shareability of the volume",
                "title": "Is Shareable",
            },
            "size": {
                "description": "Capacity of the volume in bytes",
                "title": "Capacity",
                "default": 1073741824,
                "required": True,
                "minimum": 1073741824,
                "meta": {
                    "semanticType": "capacity",
                    "locked": False,
                },
                "type": "integer",
            },
        },
    },
    {
        "category": "storage-volume-templates",
        "state": "Configured",
        "type": "StorageVolumeTemplateV6",
        "uri": "SVT:volume_temp2",
        "status": "OK",
        "name": "volume_temp2",
        "description": "",
        "properties": {
            "description": {
                "description": "A description for the volume",
                "title": "Description",
                "default": "",
                "minLength": 0,
                "meta": {
                    "locked": False,
                },
                "maxLength": 2000,
                "type": "string",
            },
            "name": {
                "description": "A volume name between 1 and 100 characters",
                "title": "Volume name",
                "minLength": 1,
                "required": True,
                "meta": {
                    "locked": False,
                },
                "maxLength": 100,
                "type": "string",
            },
            "storagePool": {
                "description": "StoragePoolURI the volume should be added to",
                "format": "x-uri-reference",
                "default": "SPOOL:Cosmos_Cluster",
                "required": True,
                "meta": {
                    "createOnly": True,
                    "semanticType": "device-storage-pool",
                    "locked": False,
                },
                "title": "Storage Pool",
                "type": "string",
            },
            "provisioningType": {
                "description": "The provisioning type for the volume",
                "title": "Provisioning Type",
                "default": "Thin",
                "enum": [u'Thin', u'Full'],
                "meta": {
                    "createOnly": "true",
                    "semanticType": "device-provisioningType",
                    "locked": True,
                },
                "type": "string",
            },
            "isShareable": {
                "default": False,
                "meta": {
                    "locked": False,
                },
                "type": "boolean",
                "description": "The shareability of the volume",
                "title": "Is Shareable",
            },
            "size": {
                "description": "Capacity of the volume in bytes",
                "title": "Capacity",
                "default": 1073741824,
                "required": True,
                "minimum": 1073741824,
                "meta": {
                    "semanticType": "capacity",
                    "locked": False,
                },
                "type": "integer",
            },
        },
    },
    {
        "category": "storage-volume-templates",
        "state": "Configured",
        "type": "StorageVolumeTemplateV6",
        "uri": "SVT:vt12",
        "status": "OK",
        "name": "vt12",
        "description": "",
        "properties": {
            "description": {
                "description": "A description for the volume",
                "title": "Description",
                "default": "",
                "minLength": 0,
                "meta": {
                    "locked": False,
                },
                "maxLength": 2000,
                "type": "string",
            },
            "name": {
                "description": "A volume name between 1 and 100 characters",
                "title": "Volume name",
                "minLength": 1,
                "required": True,
                "meta": {
                    "locked": False,
                },
                "maxLength": 100,
                "type": "string",
            },
            "snapshotPool": {
                "description": "A URI reference to the common provisioning group used to create snapshots",
                "format": "x-uri-reference",
                "default": "SPOOL:MainStream-CPG",
                "title": "Snapshot Pool",
                "meta": {
                    "semanticType": "device-snapshot-storage-pool",
                    "locked": True,
                },
                "type": "string",
            },
            "storagePool": {
                "description": "A common provisioning group URI reference",
                "format": "x-uri-reference",
                "default": "SPOOL:MainStream-CPG",
                "required": True,
                "meta": {
                    "createOnly": True,
                    "semanticType": "device-storage-pool",
                    "locked": False,
                },
                "title": "Storage Pool",
                "type": "string",
            },
            "provisioningType": {
                "description": "The provisioning type for the volume",
                "title": "Provisioning Type",
                "default": "Thin",
                "enum": [u'Thin', u'Full'],
                "meta": {
                    "createOnly": True,
                    "locked": True,
                },
                "type": "string",
            },
            "isShareable": {
                "default": False,
                "meta": {
                    "locked": False,
                },
                "type": "boolean",
                "description": "The shareability of the volume",
                "title": "Is Shareable",
            },
            "size": {
                "description": "The capacity of the volume in bytes",
                "title": "Capacity",
                "default": 1073741824,
                "required": True,
                "maximum": 17592186044416,
                "minimum": 1073741824,
                "meta": {
                    "semanticType": "capacity",
                    "locked": False,
                },
                "type": "integer",
            },
        },
    },
    {
        "category": "storage-volume-templates",
        "state": "Configured",
        "type": "StorageVolumeTemplateV6",
        "uri": "SVT:temp",
        "status": "OK",
        "name": "temp",
        "description": "",
        "properties": {
            "description": {
                "description": "A description for the volume",
                "title": "Description",
                "default": "",
                "minLength": 0,
                "meta": {
                    "locked": False,
                },
                "maxLength": 2000,
                "type": "string",
            },
            "name": {
                "description": "A volume name between 1 and 100 characters",
                "title": "Volume name",
                "minLength": 1,
                "required": True,
                "meta": {
                    "locked": False,
                },
                "maxLength": 100,
                "type": "string",
            },
            "snapshotPool": {
                "description": "A URI reference to the common provisioning group used to create snapshots",
                "format": "x-uri-reference",
                "default": "SPOOL:cosmos-cpg",
                "title": "Snapshot Pool",
                "meta": {
                    "semanticType": "device-snapshot-storage-pool",
                    "locked": True,
                },
                "type": "string",
            },
            "storagePool": {
                "description": "A common provisioning group URI reference",
                "format": "x-uri-reference",
                "default": "SPOOL:cosmos-cpg",
                "required": True,
                "meta": {
                    "createOnly": True,
                    "semanticType": "device-storage-pool",
                    "locked": False,
                },
                "title": "Storage Pool",
                "type": "string",
            },
            "provisioningType": {
                "description": "The provisioning type for the volume",
                "title": "Provisioning Type",
                "default": "Thin",
                "enum": [u'Thin', u'Full'],
                "meta": {
                    "createOnly": True,
                    "locked": True,
                },
                "type": "string",
            },
            "isShareable": {
                "default": False,
                "meta": {
                    "locked": True,
                },
                "type": "boolean",
                "description": "The shareability of the volume",
                "title": "Is Shareable",
            },
            "size": {
                "description": "The capacity of the volume in bytes",
                "title": "Capacity",
                "default": 1073741824,
                "required": True,
                "maximum": 17592186044416,
                "minimum": 1073741824,
                "meta": {
                    "semanticType": "capacity",
                    "locked": True,
                },
                "type": "integer",
            },
        },
    },
    {
        "category": "storage-volume-templates",
        "state": "Configured",
        "type": "StorageVolumeTemplateV6",
        "uri": "SVT:VT",
        "status": "OK",
        "name": "VT",
        "description": "",
        "properties": {
            "description": {
                "description": "A description for the volume",
                "title": "Description",
                "default": "",
                "minLength": 0,
                "meta": {
                    "locked": False,
                },
                "maxLength": 2000,
                "type": "string",
            },
            "name": {
                "description": "A volume name between 1 and 100 characters",
                "title": "Volume name",
                "minLength": 1,
                "required": True,
                "meta": {
                    "locked": False,
                },
                "maxLength": 100,
                "type": "string",
            },
            "snapshotPool": {
                "description": "A URI reference to the common provisioning group used to create snapshots",
                "format": "x-uri-reference",
                "default": "SPOOL:MainStream-CPG",
                "title": "Snapshot Pool",
                "meta": {
                    "semanticType": "device-snapshot-storage-pool",
                    "locked": True,
                },
                "type": "string",
            },
            "storagePool": {
                "description": "A common provisioning group URI reference",
                "format": "x-uri-reference",
                "default": "SPOOL:MainStream-CPG",
                "required": True,
                "meta": {
                    "createOnly": True,
                    "semanticType": "device-storage-pool",
                    "locked": False,
                },
                "title": "Storage Pool",
                "type": "string",
            },
            "provisioningType": {
                "description": "The provisioning type for the volume",
                "title": "Provisioning Type",
                "default": "Thin",
                "enum": [u'Thin', u'Full'],
                "meta": {
                    "createOnly": True,
                    "locked": True,
                },
                "type": "string",
            },
            "isShareable": {
                "default": False,
                "meta": {
                    "locked": False,
                },
                "type": "boolean",
                "description": "The shareability of the volume",
                "title": "Is Shareable",
            },
            "size": {
                "description": "The capacity of the volume in bytes",
                "title": "Capacity",
                "default": 1073741824,
                "required": True,
                "maximum": 17592186044416,
                "minimum": 1073741824,
                "meta": {
                    "semanticType": "capacity",
                    "locked": False,
                },
                "type": "integer",
            },
        }
    }
]

storage_volumes = [
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "DAS_TEMP",
            "provisioningType": "Thin",
            "size": 53687091200,
            "storagePool": "MainStream-CPG"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "VSA_new_vol_en41",
            "provisioningType": "Thin",
            "size": 42949672960,
            "storagePool": "Cosmos_Cluster"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "unassigned_vol",
            "provisioningType": "Thin",
            "size": 21474836480,
            "storagePool": "MainStream-CPG"
        },
    },
    {
        "templateUri": "ROOT",
        "isPermanent": True,
        "properties": {
            "description": "",
            "isShareable": True,
            "name": "share_mainstream",
            "provisioningType": "Thin",
            "size": 75161927680,
            "storagePool": "MainStream-CPG"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "gen9_2server_vol",
            "provisioningType": "Thin",
            "size": 53687091200,
            "storagePool": "MainStream-CPG"
        },
    },
    {
        "templateUri": "volume_temp2",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "volume_from_temp2",
            "provisioningType": "Thin",
            "size": 21474836480,
            "storagePool": "Cosmos_Cluster"
        },
    },
    {
        "templateUri": "volume_temp2",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "volume_from_temp2_2",
            "provisioningType": "Thin",
            "size": 21474836480,
            "storagePool": "Cosmos_Cluster"
        },
    },
    {
        "templateUri": "vt12",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "vt2_vol",
            "provisioningType": "Thin",
            "size": 1073741824,
            "storagePool": "MainStream-CPG"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "test123-vv",
            "provisioningType": "Thin",
            "size": 10737418240,
            "storagePool": "cosmos-cpg"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "en46_bay9_iscsi_vol",
            "provisioningType": "Thin",
            "size": 42949672960,
            "storagePool": "cosmos-cpg"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "gen9_2server_vol (3996)",
            "provisioningType": "Thin",
            "size": 53687091200,
            "storagePool": "MainStream-CPG"
        },
    },
    {
        "templateUri": "temp",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "temp",
            "provisioningType": "Thin",
            "size": 6442450944,
            "storagePool": "cosmos-cpg"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "vsa_en41_vol1",
            "provisioningType": "Full",
            "size": 11811160064,
            "storagePool": "Cosmos_HWVSAClust"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "infra_vol_snap",
            "provisioningType": "Thin",
            "size": 10737418240,
            "storagePool": "MainStream-CPG"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "infra_snap",
            "provisioningType": "Thin",
            "size": 21474836480,
            "storagePool": "MainStream-CPG"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "vol",
            "provisioningType": "Thin",
            "size": 10737418240,
            "storagePool": "MainStream-CPG"
        },
    },
    {
        "templateUri": "VT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "VOL_VT",
            "provisioningType": "Thin",
            "size": 2147483648,
            "storagePool": "MainStream-CPG"
        }
    }
]
expected_storage_volumes = [
    {
        "status": "OK",
        "uri": "SVOL:DAS_TEMP",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "DAS_TEMP",
            "provisioningType": "Thin",
            "size": 53687091200,
            "storagePoolUri": "SPOOL:MainStream-CPG"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:VSA_new_vol_en41",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "VSA_new_vol_en41",
            "provisioningType": "Thin",
            "size": 42949672960,
            "storagePoolUri": "SPOOL:Cosmos_Cluster"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:unassigned_vol",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "unassigned_vol",
            "provisioningType": "Thin",
            "size": 21474836480,
            "storagePoolUri": "SPOOL:MainStream-CPG"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:share_mainstream",
        "isPermanent": True,
        "properties": {
            "description": "",
            "isShareable": True,
            "name": "share_mainstream",
            "provisioningType": "Thin",
            "size": 75161927680,
            "storagePoolUri": "SPOOL:MainStream-CPG"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:gen9_2server_vol",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "gen9_2server_vol",
            "provisioningType": "Thin",
            "size": 53687091200,
            "storagePoolUri": "SPOOL:MainStream-CPG"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:volume_from_temp2",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "volume_from_temp2",
            "provisioningType": "Thin",
            "size": 21474836480,
            "storagePoolUri": "SPOOL:Cosmos_Cluster"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:volume_from_temp2_2",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "volume_from_temp2_2",
            "provisioningType": "Thin",
            "size": 21474836480,
            "storagePoolUri": "SPOOL:Cosmos_Cluster"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:vt2_vol",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "vt2_vol",
            "provisioningType": "Thin",
            "size": 1073741824,
            "storagePoolUri": "SPOOL:MainStream-CPG"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:test123-vv",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "test123-vv",
            "provisioningType": "Thin",
            "size": 10737418240,
            "storagePoolUri": "SPOOL:cosmos-cpg"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:en46_bay9_iscsi_vol",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "en46_bay9_iscsi_vol",
            "provisioningType": "Thin",
            "size": 42949672960,
            "storagePoolUri": "SPOOL:cosmos-cpg"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:gen9_2server_vol (3996)",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "gen9_2server_vol (3996)",
            "provisioningType": "Thin",
            "size": 53687091200,
            "storagePoolUri": "SPOOL:MainStream-CPG"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:temp",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "temp",
            "provisioningType": "Thin",
            "size": 6442450944,
            "storagePoolUri": "SPOOL:cosmos-cpg"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:vsa_en41_vol1",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "vsa_en41_vol1",
            "provisioningType": "Full",
            "size": 11811160064,
            "storagePoolUri": "SPOOL:Cosmos_HWVSAClust"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:infra_vol_snap",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "infra_vol_snap",
            "provisioningType": "Thin",
            "size": 10737418240,
            "storagePoolUri": "SPOOL:MainStream-CPG"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:infra_snap",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "infra_snap",
            "provisioningType": "Thin",
            "size": 21474836480,
            "storagePoolUri": "SPOOL:MainStream-CPG"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:vol",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "vol",
            "provisioningType": "Thin",
            "size": 10737418240,
            "storagePoolUri": "SPOOL:MainStream-CPG"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:VOL_VT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "VOL_VT",
            "provisioningType": "Thin",
            "size": 2147483648,
            "storagePoolUri": "SPOOL:MainStream-CPG"
        }
    }
]

sas_lig = [
]
expected_sas_lig = [
]

ligs = [
    {
        "name": "En36_lig2",
        "type": "logical-interconnect-groupV6",
        "enclosureType": "C7000",
        "ethernetSettings": {
            "enableFastMacCacheFailover": True,
            "enableIgmpSnooping": False,
            "enableNetworkLoopProtection": True,
            "enablePauseFloodProtection": True,
            "igmpIdleTimeoutInterval": 260,
            "interconnectType": "Ethernet",
            "macRefreshInterval": 5
        },
        "interconnectMapTemplate": [
            {
                "enclosureIndex": 1,
                "bay": 4,
                "enclosure": 1,
                "type": "HP VC FlexFabric 10Gb/24-Port Module"
            },
            {
                "enclosureIndex": 1,
                "bay": 3,
                "enclosure": 1,
                "type": "HP VC FlexFabric 10Gb/24-Port Module"
            }

        ],
        "interconnectBaySet": None,
        "redundancyType": None,
        "telemetryConfiguration": {
            "enableTelemetry": True,
            "sampleCount": 12,
            "sampleInterval": 300
        },
        "uplinkSets": [{
            "ethernetNetworkType": "Tagged",
            "lacpTimer": "Short",
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "enclosure": "1",
                    "port": "X4",
                    "bay": "3"
                }
            ],
            "mode": "Auto",
            "name": "fcoe1",
            "nativeNetworkUri": None,
            "networkType": "Ethernet",
            "networkUris": [
                "fcoe1"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "Tagged",
            "lacpTimer": "Short",
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "enclosure": "1",
                    "port": "X4",
                    "bay": "4"
                }
            ],
            "mode": "Auto",
            "name": "fcoe2",
            "nativeNetworkUri": None,
            "networkType": "Ethernet",
            "networkUris": [
                "fcoe2"
            ],
            "primaryPort": None
        }
        ],
        "qosConfiguration": {
            "activeQosConfig": {u'category': u'qos-aggregated-configuration', u'status': None, u'description': None, u'created': None, u'uri': None, u'modified': None, u'configType': u'Passthrough', u'state': None, u'eTag': None, u'downlinkClassificationType': None, u'uplinkClassificationType': None, u'qosTrafficClassifiers': [], u'type': u'QosConfiguration', u'name': None},
            "inactiveFCoEQosConfig": None,
            "inactiveNonFCoEQosConfig": None,
            "name": None,
            "type": "qos-aggregated-configuration"
        },
        "enclosureIndexes": [1]
    }, {
        "name": "en41_lig2",
        "type": "logical-interconnect-groupV6",
        "enclosureType": "C7000",
        "ethernetSettings": {
            "enableFastMacCacheFailover": True,
            "enableIgmpSnooping": False,
            "enableNetworkLoopProtection": True,
            "enablePauseFloodProtection": True,
            "igmpIdleTimeoutInterval": 260,
            "interconnectType": "Ethernet",
            "macRefreshInterval": 5
        },
        "interconnectMapTemplate": [
            {
                "enclosureIndex": 1,
                "bay": 3,
                "enclosure": 1,
                "type": "HP VC 8Gb 24-Port FC Module"
            },
            {
                "enclosureIndex": 1,
                "bay": 4,
                "enclosure": 1,
                "type": "HP VC 8Gb 24-Port FC Module"
            }

        ],
        "interconnectBaySet": None,
        "redundancyType": None,
        "telemetryConfiguration": {
            "enableTelemetry": True,
            "sampleCount": 12,
            "sampleInterval": 300
        },
        "uplinkSets": [{
            "ethernetNetworkType": "NotApplicable",
            "lacpTimer": None,
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "enclosure": "1",
                    "port": "1",
                    "bay": "4"
                }
            ],
            "mode": "Auto",
            "name": "fc2",
            "nativeNetworkUri": None,
            "networkType": "FibreChannel",
            "networkUris": [
                "fc2"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "NotApplicable",
            "lacpTimer": None,
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "enclosure": "1",
                    "port": "1",
                    "bay": "3"
                }
            ],
            "mode": "Auto",
            "name": "fc1",
            "nativeNetworkUri": None,
            "networkType": "FibreChannel",
            "networkUris": [
                "fc1"
            ],
            "primaryPort": None
        }
        ],
        "qosConfiguration": {
            "activeQosConfig": {u'category': u'qos-aggregated-configuration', u'status': None, u'description': None, u'created': None, u'uri': None, u'modified': None, u'configType': u'Passthrough', u'state': None, u'eTag': None, u'downlinkClassificationType': None, u'uplinkClassificationType': None, u'qosTrafficClassifiers': [], u'type': u'QosConfiguration', u'name': None},
            "inactiveFCoEQosConfig": None,
            "inactiveNonFCoEQosConfig": None,
            "name": None,
            "type": "qos-aggregated-configuration"
        },
        "enclosureIndexes": [1]
    },
    {
        "name": "en46_lig2",
        "type": "logical-interconnect-groupV6",
        "enclosureType": "C7000",
        "ethernetSettings": {
            "enableFastMacCacheFailover": True,
            "enableIgmpSnooping": False,
            "enableNetworkLoopProtection": True,
            "enablePauseFloodProtection": True,
            "igmpIdleTimeoutInterval": 260,
            "interconnectType": "Ethernet",
            "macRefreshInterval": 5
        },
        "interconnectMapTemplate": [
            {
                "enclosureIndex": 1,
                "bay": 4,
                "enclosure": 1,
                "type": "HP VC FlexFabric-20/40 F8 Module"
            },
            {
                "enclosureIndex": 1,
                "bay": 3,
                "enclosure": 1,
                "type": "HP VC FlexFabric-20/40 F8 Module"
            }
        ],
        "interconnectBaySet": None,
        "redundancyType": None,
        "telemetryConfiguration": {
            "enableTelemetry": True,
            "sampleCount": 12,
            "sampleInterval": 300
        },
        "uplinkSets": [{
            "ethernetNetworkType": "Tagged",
            "lacpTimer": "Short",
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "enclosure": "1",
                    "port": "X4",
                    "bay": "4"
                }
            ],
            "mode": "Auto",
            "name": "iscsi2",
            "nativeNetworkUri": None,
            "networkType": "Ethernet",
            "networkUris": [
                "iscsi2"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "Tagged",
            "lacpTimer": "Short",
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "enclosure": "1",
                    "port": "X4",
                    "bay": "3"
                }
            ],
            "mode": "Auto",
            "name": "iscsi1",
            "nativeNetworkUri": None,
            "networkType": "Ethernet",
            "networkUris": [
                "iscsi1"
            ],
            "primaryPort": None
        }
        ],
        "qosConfiguration": {
            "activeQosConfig": {u'category': u'qos-aggregated-configuration', u'status': None, u'description': None, u'created': None, u'uri': None, u'modified': None, u'configType': u'Passthrough', u'state': None, u'eTag': None, u'downlinkClassificationType': None, u'uplinkClassificationType': None, u'qosTrafficClassifiers': [], u'type': u'QosConfiguration', u'name': None},
            "inactiveFCoEQosConfig": None,
            "inactiveNonFCoEQosConfig": None,
            "name": None,
            "type": "qos-aggregated-configuration"
        },
        "enclosureIndexes": [1]
    },
    {
        "name": "en46_lig1",
        "type": "logical-interconnect-groupV6",
        "enclosureType": "C7000",
        "ethernetSettings": {
            "enableFastMacCacheFailover": True,
            "enableIgmpSnooping": False,
            "enableNetworkLoopProtection": True,
            "enablePauseFloodProtection": True,
            "igmpIdleTimeoutInterval": 260,
            "interconnectType": "Ethernet",
            "macRefreshInterval": 5
        },
        "interconnectMapTemplate": [
            {
                "enclosureIndex": 1,
                "bay": 2,
                "enclosure": 1,
                "type": "HP VC FlexFabric 10Gb/24-Port Module"
            },
            {
                "enclosureIndex": 1,
                "bay": 1,
                "enclosure": 1,
                "type": "HP VC FlexFabric 10Gb/24-Port Module"
            }
        ],
        "interconnectBaySet": None,
        "redundancyType": None,
        "telemetryConfiguration": {
            "enableTelemetry": True,
            "sampleCount": 12,
            "sampleInterval": 300
        },
        "uplinkSets": [{
            "ethernetNetworkType": "NotApplicable",
            "lacpTimer": None,
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "enclosure": "1",
                    "port": "X1",
                    "bay": "2"
                }
            ],
            "mode": "Auto",
            "name": "fc2",
            "nativeNetworkUri": None,
            "networkType": "FibreChannel",
            "networkUris": [
                "fc2"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "Tagged",
            "lacpTimer": "Short",
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "enclosure": "1",
                    "port": "X5",
                    "bay": "1"
                }
            ],
            "mode": "Auto",
            "name": "eth1",
            "nativeNetworkUri": None,
            "networkType": "Ethernet",
            "networkUris": [
                "eth1_1098",
                "eth1_1096",
                "eth1_1097"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "Tagged",
            "lacpTimer": "Short",
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "enclosure": "1",
                    "port": "X5",
                    "bay": "2"
                }
            ],
            "mode": "Auto",
            "name": "eth2",
            "nativeNetworkUri": None,
            "networkType": "Ethernet",
            "networkUris": [
                "eth2_1098",
                "eth2_1096",
                "eth2_1097"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "NotApplicable",
            "lacpTimer": None,
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "enclosure": "1",
                    "port": "X1",
                    "bay": "1"
                }
            ],
            "mode": "Auto",
            "name": "fc1",
            "nativeNetworkUri": None,
            "networkType": "FibreChannel",
            "networkUris": [
                "fc1"
            ],
            "primaryPort": None
        }
        ],
        "qosConfiguration": {
            "activeQosConfig": {u'category': u'qos-aggregated-configuration', u'status': None, u'description': None, u'created': None, u'uri': None, u'modified': None, u'configType': u'Passthrough', u'state': None, u'eTag': None, u'downlinkClassificationType': None, u'uplinkClassificationType': None, u'qosTrafficClassifiers': [], u'type': u'QosConfiguration', u'name': None},
            "inactiveFCoEQosConfig": None,
            "inactiveNonFCoEQosConfig": None,
            "name": None,
            "type": "qos-aggregated-configuration"
        },
        "enclosureIndexes": [1]
    },
    {
        "name": "en41_lig3",
        "type": "logical-interconnect-groupV6",
        "enclosureType": "C7000",
        "ethernetSettings": {
            "enableFastMacCacheFailover": True,
            "enableIgmpSnooping": False,
            "enableNetworkLoopProtection": True,
            "enablePauseFloodProtection": True,
            "igmpIdleTimeoutInterval": 260,
            "interconnectType": "Ethernet",
            "macRefreshInterval": 5
        },
        "interconnectMapTemplate": [
            {
                "enclosureIndex": 1,
                "bay": 5,
                "enclosure": 1,
                "type": "HP VC 8Gb 20-Port FC Module"
            },
            {
                "enclosureIndex": 1,
                "bay": 6,
                "enclosure": 1,
                "type": "HP VC 8Gb 20-Port FC Module"
            }

        ],
        "interconnectBaySet": None,
        "redundancyType": None,
        "telemetryConfiguration": {
            "enableTelemetry": True,
            "sampleCount": 12,
            "sampleInterval": 300
        },
        "uplinkSets": [{
            "ethernetNetworkType": "NotApplicable",
            "lacpTimer": None,
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "port": "3",
                    "enclosure": "1",
                    "bay": "5"
                }
            ],
            "mode": "Auto",
            "name": "fc1",
            "nativeNetworkUri": None,
            "networkType": "FibreChannel",
            "networkUris": [
                "fc1"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "NotApplicable",
            "lacpTimer": None,
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "port": "3",
                    "enclosure": "1",
                    "bay": "6"
                }
            ],
            "mode": "Auto",
            "name": "fc2",
            "nativeNetworkUri": None,
            "networkType": "FibreChannel",
            "networkUris": [
                "fc2"
            ],
            "primaryPort": None
        }
        ],
        "qosConfiguration": {
            "activeQosConfig": {u'category': u'qos-aggregated-configuration', u'status': None, u'description': None, u'created': None, u'uri': None, u'modified': None, u'configType': u'Passthrough', u'state': None, u'eTag': None, u'downlinkClassificationType': None, u'uplinkClassificationType': None, u'qosTrafficClassifiers': [], u'type': u'QosConfiguration', u'name': None},
            "inactiveFCoEQosConfig": None,
            "inactiveNonFCoEQosConfig": None,
            "name": None,
            "type": "qos-aggregated-configuration"
        },
        "enclosureIndexes": [1]
    },
    {
        "name": "en41_lig1",
        "type": "logical-interconnect-groupV6",
        "enclosureType": "C7000",
        "ethernetSettings": {
            "enableFastMacCacheFailover": True,
            "enableIgmpSnooping": False,
            "enableNetworkLoopProtection": True,
            "enablePauseFloodProtection": True,
            "igmpIdleTimeoutInterval": 260,
            "interconnectType": "Ethernet",
            "macRefreshInterval": 5
        },
        "interconnectMapTemplate": [
            {
                "enclosureIndex": 1,
                "bay": 1,
                "enclosure": 1,
                "type": "HP VC FlexFabric-20/40 F8 Module"
            },
            {
                "enclosureIndex": 1,
                "bay": 2,
                "enclosure": 1,
                "type": "HP VC FlexFabric-20/40 F8 Module"
            }

        ],
        "interconnectBaySet": None,
        "redundancyType": None,
        "telemetryConfiguration": {
            "enableTelemetry": True,
            "sampleCount": 12,
            "sampleInterval": 300
        },
        "uplinkSets": [{
            "ethernetNetworkType": "NotApplicable",
            "lacpTimer": None,
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "enclosure": "1",
                    "port": "X1",
                    "bay": "1"
                }
            ],
            "mode": "Auto",
            "name": "das1",
            "nativeNetworkUri": None,
            "networkType": "FibreChannel",
            "networkUris": [
                "das1"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "NotApplicable",
            "lacpTimer": None,
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "enclosure": "1",
                    "port": "X1",
                    "bay": "2"
                }
            ],
            "mode": "Auto",
            "name": "das2",
            "nativeNetworkUri": None,
            "networkType": "FibreChannel",
            "networkUris": [
                "das2"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "Tagged",
            "lacpTimer": "Short",
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "port": "X3",
                    "enclosure": "1",
                    "bay": "2"
                },
                {
                    "speed": "Auto",
                    "port": "X3",
                    "enclosure": "1",
                    "bay": "1"
                }
            ],
            "mode": "Auto",
            "name": "eth1",
            "nativeNetworkUri": None,
            "networkType": "Ethernet",
            "networkUris": [
                "eth1_1098",
                "eth1_1096",
                "vsa_iscsi1",
                "VSA_Iscsi2",
                "eth1_1097"
            ],
            "primaryPort": None
        }
        ],
        "qosConfiguration": {
            "activeQosConfig": {u'category': u'qos-aggregated-configuration', u'status': None, u'description': None, u'created': None, u'uri': None, u'modified': None, u'configType': u'Passthrough', u'state': None, u'eTag': None, u'downlinkClassificationType': None, u'uplinkClassificationType': None, u'qosTrafficClassifiers': [], u'type': u'QosConfiguration', u'name': None},
            "inactiveFCoEQosConfig": None,
            "inactiveNonFCoEQosConfig": None,
            "name": None,
            "type": "qos-aggregated-configuration"
        },
        "enclosureIndexes": [1]
    },
    {
        "name": "En36_lig1",
        "type": "logical-interconnect-groupV6",
        "enclosureType": "C7000",
        "ethernetSettings": {
            "enableFastMacCacheFailover": True,
            "enableIgmpSnooping": False,
            "enableNetworkLoopProtection": True,
            "enablePauseFloodProtection": True,
            "igmpIdleTimeoutInterval": 260,
            "interconnectType": "Ethernet",
            "macRefreshInterval": 5
        },
        "interconnectMapTemplate": [
            {
                "enclosureIndex": 1,
                "bay": 2,
                "enclosure": 1,
                "type": "HP VC FlexFabric-20/40 F8 Module"
            },
            {
                "enclosureIndex": 1,
                "bay": 1,
                "enclosure": 1,
                "type": "HP VC FlexFabric-20/40 F8 Module"
            }
        ],
        "interconnectBaySet": None,
        "redundancyType": None,
        "telemetryConfiguration": {
            "enableTelemetry": True,
            "sampleCount": 12,
            "sampleInterval": 300
        },
        "uplinkSets": [{
            "ethernetNetworkType": "NotApplicable",
            "lacpTimer": None,
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "port": "X3",
                    "enclosure": "1",
                    "bay": "2"
                }
            ],
            "mode": "Auto",
            "name": "fc2",
            "nativeNetworkUri": None,
            "networkType": "FibreChannel",
            "networkUris": [
                "fc2"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "Tagged",
            "lacpTimer": "Short",
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "enclosure": "1",
                    "port": "X1",
                    "bay": "1"
                }
            ],
            "mode": "Auto",
            "name": "eth1",
            "nativeNetworkUri": None,
            "networkType": "Ethernet",
            "networkUris": [
                "eth1_1098",
                "eth1_1096",
                "eth1_1097"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "Tagged",
            "lacpTimer": "Short",
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "enclosure": "1",
                    "port": "X1",
                    "bay": "2"
                }
            ],
            "mode": "Auto",
            "name": "eth2",
            "nativeNetworkUri": None,
            "networkType": "Ethernet",
            "networkUris": [
                "eth2_1098",
                "eth2_1096",
                "eth2_1097"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "NotApplicable",
            "lacpTimer": None,
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "port": "X3",
                    "enclosure": "1",
                    "bay": "1"
                }
            ],
            "mode": "Auto",
            "name": "fc1",
            "nativeNetworkUri": None,
            "networkType": "FibreChannel",
            "networkUris": [
                "fc1"
            ],
            "primaryPort": None
        }
        ],
        "qosConfiguration": {
            "activeQosConfig": {u'category': u'qos-aggregated-configuration', u'status': None, u'description': None, u'created': None, u'uri': None, u'modified': None, u'configType': u'Passthrough', u'state': None, u'eTag': None, u'downlinkClassificationType': None, u'uplinkClassificationType': None, u'qosTrafficClassifiers': [], u'type': u'QosConfiguration', u'name': None},
            "inactiveFCoEQosConfig": None,
            "inactiveNonFCoEQosConfig": None,
            "name": None,
            "type": "qos-aggregated-configuration"
        },
        "enclosureIndexes": [1]
    }
]
expected_lig = [
    {
        "uri": "LIG:En36_lig2",
        "status": None,
        "stackingHealth": None,
        "category": "logical-interconnect-groups",
        "state": "Active",
        "internalNetworkUris": "[]",
        "stackingMode": None,
        "description": None,
        "name": "En36_lig2",
        "type": "logical-interconnect-groupV6",
        "enclosureType": "C7000",
        "ethernetSettings": {
            "enableFastMacCacheFailover": True,
            "enableIgmpSnooping": False,
            "enableNetworkLoopProtection": True,
            "enablePauseFloodProtection": True,
            "igmpIdleTimeoutInterval": 260,
            "interconnectType": "Ethernet",
            "macRefreshInterval": 5
        },
        "interconnectBaySet": None,
        "redundancyType": None,
        "telemetryConfiguration": {
            "enableTelemetry": True,
            "sampleCount": 12,
            "sampleInterval": 300
        },
        "qosConfiguration": {
            "activeQosConfig": {u'category': u'qos-aggregated-configuration', u'status': None, u'description': None, u'created': None, u'uri': None, u'modified': None, u'configType': u'Passthrough', u'state': None, u'eTag': None, u'downlinkClassificationType': None, u'uplinkClassificationType': None, u'qosTrafficClassifiers': [], u'type': u'QosConfiguration', u'name': None},
            "inactiveFCoEQosConfig": None,
            "inactiveNonFCoEQosConfig": None,
            "name": None,
            "type": "qos-aggregated-configuration"
        },
        "enclosureIndexes": [1]
    },
    {
        "uri": "LIG:en41_lig2",
        "status": None,
        "stackingHealth": None,
        "category": "logical-interconnect-groups",
        "state": "Active",
        "internalNetworkUris": "[]",
        "stackingMode": None,
        "description": None,
        "name": "en41_lig2",
        "type": "logical-interconnect-groupV6",
        "enclosureType": "C7000",
        "ethernetSettings": {
            "enableFastMacCacheFailover": True,
            "enableIgmpSnooping": False,
            "enableNetworkLoopProtection": True,
            "enablePauseFloodProtection": True,
            "igmpIdleTimeoutInterval": 260,
            "interconnectType": "Ethernet",
            "macRefreshInterval": 5
        },
        "interconnectBaySet": None,
        "redundancyType": None,
        "telemetryConfiguration": {
            "enableTelemetry": True,
            "sampleCount": 12,
            "sampleInterval": 300
        },
        "qosConfiguration": {
            "activeQosConfig": {u'category': u'qos-aggregated-configuration', u'status': None, u'description': None, u'created': None, u'uri': None, u'modified': None, u'configType': u'Passthrough', u'state': None, u'eTag': None, u'downlinkClassificationType': None, u'uplinkClassificationType': None, u'qosTrafficClassifiers': [], u'type': u'QosConfiguration', u'name': None},
            "inactiveFCoEQosConfig": None,
            "inactiveNonFCoEQosConfig": None,
            "name": None,
            "type": "qos-aggregated-configuration"
        },
        "enclosureIndexes": [1]
    },
    {
        "uri": "LIG:en46_lig2",
        "status": None,
        "stackingHealth": None,
        "category": "logical-interconnect-groups",
        "state": "Active",
        "internalNetworkUris": "[]",
        "stackingMode": None,
        "description": None,
        "name": "en46_lig2",
        "type": "logical-interconnect-groupV6",
        "enclosureType": "C7000",
        "ethernetSettings": {
            "enableFastMacCacheFailover": True,
            "enableIgmpSnooping": False,
            "enableNetworkLoopProtection": True,
            "enablePauseFloodProtection": True,
            "igmpIdleTimeoutInterval": 260,
            "interconnectType": "Ethernet",
            "macRefreshInterval": 5
        },
        "interconnectBaySet": None,
        "redundancyType": None,
        "telemetryConfiguration": {
            "enableTelemetry": True,
            "sampleCount": 12,
            "sampleInterval": 300
        },
        "qosConfiguration": {
            "activeQosConfig": {u'category': u'qos-aggregated-configuration', u'status': None, u'description': None, u'created': None, u'uri': None, u'modified': None, u'configType': u'Passthrough', u'state': None, u'eTag': None, u'downlinkClassificationType': None, u'uplinkClassificationType': None, u'qosTrafficClassifiers': [], u'type': u'QosConfiguration', u'name': None},
            "inactiveFCoEQosConfig": None,
            "inactiveNonFCoEQosConfig": None,
            "name": None,
            "type": "qos-aggregated-configuration"
        },
        "enclosureIndexes": [1]
    },
    {
        "uri": "LIG:en46_lig1",
        "status": None,
        "stackingHealth": None,
        "category": "logical-interconnect-groups",
        "state": "Active",
        "internalNetworkUris": "[]",
        "stackingMode": None,
        "description": None,
        "name": "en46_lig1",
        "type": "logical-interconnect-groupV6",
        "enclosureType": "C7000",
        "ethernetSettings": {
            "enableFastMacCacheFailover": True,
            "enableIgmpSnooping": False,
            "enableNetworkLoopProtection": True,
            "enablePauseFloodProtection": True,
            "igmpIdleTimeoutInterval": 260,
            "interconnectType": "Ethernet",
            "macRefreshInterval": 5
        },
        "interconnectBaySet": None,
        "redundancyType": None,
        "telemetryConfiguration": {
            "enableTelemetry": True,
            "sampleCount": 12,
            "sampleInterval": 300
        },
        "qosConfiguration": {
            "activeQosConfig": {u'category': u'qos-aggregated-configuration', u'status': None, u'description': None, u'created': None, u'uri': None, u'modified': None, u'configType': u'Passthrough', u'state': None, u'eTag': None, u'downlinkClassificationType': None, u'uplinkClassificationType': None, u'qosTrafficClassifiers': [], u'type': u'QosConfiguration', u'name': None},
            "inactiveFCoEQosConfig": None,
            "inactiveNonFCoEQosConfig": None,
            "name": None,
            "type": "qos-aggregated-configuration"
        },
        "enclosureIndexes": [1]
    },
    {
        "uri": "LIG:en41_lig3",
        "status": None,
        "stackingHealth": None,
        "category": "logical-interconnect-groups",
        "state": "Active",
        "internalNetworkUris": "[]",
        "stackingMode": None,
        "description": None,
        "name": "en41_lig3",
        "type": "logical-interconnect-groupV6",
        "enclosureType": "C7000",
        "ethernetSettings": {
            "enableFastMacCacheFailover": True,
            "enableIgmpSnooping": False,
            "enableNetworkLoopProtection": True,
            "enablePauseFloodProtection": True,
            "igmpIdleTimeoutInterval": 260,
            "interconnectType": "Ethernet",
            "macRefreshInterval": 5
        },
        "interconnectBaySet": None,
        "redundancyType": None,
        "telemetryConfiguration": {
            "enableTelemetry": True,
            "sampleCount": 12,
            "sampleInterval": 300
        },
        "qosConfiguration": {
            "activeQosConfig": {u'category': u'qos-aggregated-configuration', u'status': None, u'description': None, u'created': None, u'uri': None, u'modified': None, u'configType': u'Passthrough', u'state': None, u'eTag': None, u'downlinkClassificationType': None, u'uplinkClassificationType': None, u'qosTrafficClassifiers': [], u'type': u'QosConfiguration', u'name': None},
            "inactiveFCoEQosConfig": None,
            "inactiveNonFCoEQosConfig": None,
            "name": None,
            "type": "qos-aggregated-configuration"
        },
        "enclosureIndexes": [1]
    },
    {
        "uri": "LIG:en41_lig1",
        "status": None,
        "stackingHealth": None,
        "category": "logical-interconnect-groups",
        "state": "Active",
        "internalNetworkUris": "[]",
        "stackingMode": None,
        "description": None,
        "name": "en41_lig1",
        "type": "logical-interconnect-groupV6",
        "enclosureType": "C7000",
        "ethernetSettings": {
            "enableFastMacCacheFailover": True,
            "enableIgmpSnooping": False,
            "enableNetworkLoopProtection": True,
            "enablePauseFloodProtection": True,
            "igmpIdleTimeoutInterval": 260,
            "interconnectType": "Ethernet",
            "macRefreshInterval": 5
        },
        "interconnectBaySet": None,
        "redundancyType": None,
        "telemetryConfiguration": {
            "enableTelemetry": True,
            "sampleCount": 12,
            "sampleInterval": 300
        },
        "qosConfiguration": {
            "activeQosConfig": {u'category': u'qos-aggregated-configuration', u'status': None, u'description': None, u'created': None, u'uri': None, u'modified': None, u'configType': u'Passthrough', u'state': None, u'eTag': None, u'downlinkClassificationType': None, u'uplinkClassificationType': None, u'qosTrafficClassifiers': [], u'type': u'QosConfiguration', u'name': None},
            "inactiveFCoEQosConfig": None,
            "inactiveNonFCoEQosConfig": None,
            "name": None,
            "type": "qos-aggregated-configuration"
        },
        "enclosureIndexes": [1]
    },
    {
        "uri": "LIG:En36_lig1",
        "status": None,
        "stackingHealth": None,
        "category": "logical-interconnect-groups",
        "state": "Active",
        "internalNetworkUris": "[]",
        "stackingMode": None,
        "description": None,
        "name": "En36_lig1",
        "type": "logical-interconnect-groupV6",
        "enclosureType": "C7000",
        "ethernetSettings": {
            "enableFastMacCacheFailover": True,
            "enableIgmpSnooping": False,
            "enableNetworkLoopProtection": True,
            "enablePauseFloodProtection": True,
            "igmpIdleTimeoutInterval": 260,
            "interconnectType": "Ethernet",
            "macRefreshInterval": 5
        },
        "interconnectBaySet": None,
        "redundancyType": None,
        "telemetryConfiguration": {
            "enableTelemetry": True,
            "sampleCount": 12,
            "sampleInterval": 300
        },
        "qosConfiguration": {
            "activeQosConfig": {u'category': u'qos-aggregated-configuration', u'status': None, u'description': None, u'created': None, u'uri': None, u'modified': None, u'configType': u'Passthrough', u'state': None, u'eTag': None, u'downlinkClassificationType': None, u'uplinkClassificationType': None, u'qosTrafficClassifiers': [], u'type': u'QosConfiguration', u'name': None},
            "inactiveFCoEQosConfig": None,
            "inactiveNonFCoEQosConfig": None,
            "name": None,
            "type": "qos-aggregated-configuration"
        },
        "enclosureIndexes": [1]
    }
]

encgroups_add = [
    {
        "name": "EG_36",
        "interconnectBayMappings": [
            {
                "interconnectBay": 1,
                "logicalInterconnectGroupUri": "LIG:En36_lig1",

            },
            {
                "interconnectBay": 2,
                "logicalInterconnectGroupUri": "LIG:En36_lig1",

            },
            {
                "interconnectBay": 3,
                "logicalInterconnectGroupUri": "LIG:En36_lig2",

            },
            {
                "interconnectBay": 4,
                "logicalInterconnectGroupUri": "LIG:En36_lig2",

            }
        ],
        "ipAddressingMode": "External",
        "enclosureCount": 1
    },
    {
        "name": "EG_46",
        "interconnectBayMappings": [
            {
                "interconnectBay": 1,
                "logicalInterconnectGroupUri": "LIG:en46_lig1",

            },
            {
                "interconnectBay": 2,
                "logicalInterconnectGroupUri": "LIG:en46_lig1",

            },
            {
                "interconnectBay": 3,
                "logicalInterconnectGroupUri": "LIG:en46_lig2",

            },
            {
                "interconnectBay": 4,
                "logicalInterconnectGroupUri": "LIG:en46_lig2",

            }
        ],
        "ipAddressingMode": "External",
        "enclosureCount": 1
    },
    {
        "name": "EG_41",
        "interconnectBayMappings": [
            {
                "interconnectBay": 1,
                "logicalInterconnectGroupUri": "LIG:en41_lig1",

            },
            {
                "interconnectBay": 2,
                "logicalInterconnectGroupUri": "LIG:en41_lig1",

            },
            {
                "interconnectBay": 3,
                "logicalInterconnectGroupUri": "LIG:en41_lig2",

            },
            {
                "interconnectBay": 4,
                "logicalInterconnectGroupUri": "LIG:en41_lig2",

            },
            {
                "interconnectBay": 5,
                "logicalInterconnectGroupUri": "LIG:en41_lig3",

            },
            {
                "interconnectBay": 6,
                "logicalInterconnectGroupUri": "LIG:en41_lig3",

            }
        ],
        "ipAddressingMode": "External",
        "enclosureCount": 1
    }
]
expected_encgroups_add = [
    {
        "uri": "EG:EG_36",
        "description": None,
        "category": "enclosure-groups",
        "state": "Normal",
        "status": "OK",
        "powerMode": None,
        "portMappingCount": 8,
        "portMappings": [{u'midplanePort': 1, u'interconnectBay': 1}, {u'midplanePort': 2, u'interconnectBay': 2}, {u'midplanePort': 3, u'interconnectBay': 3}, {u'midplanePort': 4, u'interconnectBay': 4}, {u'midplanePort': 5, u'interconnectBay': 5}, {u'midplanePort': 6, u'interconnectBay': 6}, {u'midplanePort': 7, u'interconnectBay': 7}, {u'midplanePort': 8, u'interconnectBay': 8}],
        "ipRangeUris": [],
        "associatedLogicalInterconnectGroups": [u'LIG:En36_lig2', u'LIG:En36_lig1'],
        "name": "EG_36",
        "type": "EnclosureGroupV7",
        "enclosureTypeUri": "/rest/enclosure-types/c7000",
        "stackingMode": "Enclosure",
        "name": "EG_36",
        "interconnectBayMappingCount": "4",
        "interconnectBayMappings": [
            {
                "interconnectBay": 1,
                "logicalInterconnectGroupUri": "LIG:En36_lig1",

            },
            {
                "interconnectBay": 2,
                "logicalInterconnectGroupUri": "LIG:En36_lig1",

            },
            {
                "interconnectBay": 3,
                "logicalInterconnectGroupUri": "LIG:En36_lig2",

            },
            {
                "interconnectBay": 4,
                "logicalInterconnectGroupUri": "LIG:En36_lig2",

            }
        ],
        "ipAddressingMode": "External",
        "enclosureCount": 1
    },
    {
        "uri": "EG:EG_46",
        "description": None,
        "category": "enclosure-groups",
        "state": "Normal",
        "status": "OK",
        "powerMode": None,
        "portMappingCount": 8,
        "portMappings": [{u'midplanePort': 1, u'interconnectBay': 1}, {u'midplanePort': 2, u'interconnectBay': 2}, {u'midplanePort': 3, u'interconnectBay': 3}, {u'midplanePort': 4, u'interconnectBay': 4}, {u'midplanePort': 5, u'interconnectBay': 5}, {u'midplanePort': 6, u'interconnectBay': 6}, {u'midplanePort': 7, u'interconnectBay': 7}, {u'midplanePort': 8, u'interconnectBay': 8}],
        "ipRangeUris": [],
        "associatedLogicalInterconnectGroups": [u'LIG:en46_lig2', u'LIG:en46_lig1'],
        "name": "EG_46",
        "type": "EnclosureGroupV7",
        "enclosureTypeUri": "/rest/enclosure-types/c7000",
        "stackingMode": "Enclosure",
        "name": "EG_46",
        "interconnectBayMappingCount": "4",
        "interconnectBayMappings": [
            {
                "interconnectBay": 1,
                "logicalInterconnectGroupUri": "LIG:en46_lig1",

            },
            {
                "interconnectBay": 2,
                "logicalInterconnectGroupUri": "LIG:en46_lig1",

            },
            {
                "interconnectBay": 3,
                "logicalInterconnectGroupUri": "LIG:en46_lig2",

            },
            {
                "interconnectBay": 4,
                "logicalInterconnectGroupUri": "LIG:en46_lig2",

            }
        ],
        "ipAddressingMode": "External",
        "enclosureCount": 1
    },
    {
        "uri": "EG:EG_41",
        "description": None,
        "category": "enclosure-groups",
        "state": "Normal",
        "status": "OK",
        "powerMode": None,
        "portMappingCount": 8,
        "portMappings": [{u'midplanePort': 1, u'interconnectBay': 1}, {u'midplanePort': 2, u'interconnectBay': 2}, {u'midplanePort': 3, u'interconnectBay': 3}, {u'midplanePort': 4, u'interconnectBay': 4}, {u'midplanePort': 5, u'interconnectBay': 5}, {u'midplanePort': 6, u'interconnectBay': 6}, {u'midplanePort': 7, u'interconnectBay': 7}, {u'midplanePort': 8, u'interconnectBay': 8}],
        "ipRangeUris": [],
        "associatedLogicalInterconnectGroups": [u'LIG:en41_lig2', u'LIG:en41_lig3', u'LIG:en41_lig1'],
        "name": "EG_41",
        "type": "EnclosureGroupV7",
        "enclosureTypeUri": "/rest/enclosure-types/c7000",
        "stackingMode": "Enclosure",
        "name": "EG_41",
        "interconnectBayMappingCount": "6",
        "interconnectBayMappings": [
            {
                "interconnectBay": 1,
                "logicalInterconnectGroupUri": "LIG:en41_lig1",

            },
            {
                "interconnectBay": 2,
                "logicalInterconnectGroupUri": "LIG:en41_lig1",

            },
            {
                "interconnectBay": 3,
                "logicalInterconnectGroupUri": "LIG:en41_lig2",

            },
            {
                "interconnectBay": 4,
                "logicalInterconnectGroupUri": "LIG:en41_lig2",

            },
            {
                "interconnectBay": 5,
                "logicalInterconnectGroupUri": "LIG:en41_lig3",

            },
            {
                "interconnectBay": 6,
                "logicalInterconnectGroupUri": "LIG:en41_lig3",

            }
        ],
        "ipAddressingMode": "External",
        "enclosureCount": 1
    }
]

logical_enclosure = [
    {
        "name": "ENC_41",
        "enclosureUris": [
            "ENC:ENC_41"
        ],
        "enclosureGroupUri": "EG:EG_41"
    },
    {
        "name": "ENCL_21",
        "enclosureUris": [
            "ENC:ENCL_21"
        ],
        "enclosureGroupUri": "EG:EG_36"
    },
    {
        "name": "ENC-46",
        "enclosureUris": [
            "ENC:ENC-46"
        ],
        "enclosureGroupUri": "EG:EG_46"
    }
]
expected_logical_enclosure = [
    {
        "type": "LogicalEnclosureV4",
        "uri": "ENC_41",
        "status": "OK",
        "name": "ENC_41",
        "enclosureUris": [
            "ENC:ENC_41"
        ],
        "enclosureGroupUri": "EG:EG_41"
    },
    {
        "type": "LogicalEnclosureV4",
        "uri": "ENCL_21",
        "status": "OK",
        "name": "ENCL_21",
        "enclosureUris": [
            "ENC:ENCL_21"
        ],
        "enclosureGroupUri": "EG:EG_36"
    },
    {
        "type": "LogicalEnclosureV4",
        "uri": "ENC-46",
        "status": "OK",
        "name": "ENC-46",
        "enclosureUris": [
            "ENC:ENC-46"
        ],
        "enclosureGroupUri": "EG:EG_46"
    }
]

enclosures = [
    {
        "username": "Admin",
        "name": "ENC_41",
        "password": "Insight7",
        "force": True,
        "hostname": "172.25.41.11",
        "enclosureGroupUri": "EG:EG_41",
        "forceInstallFirmware": True,
        "licensingIntent": "OneView",
    },
    {
        "username": "Admin",
        "name": "ENC-46",
        "password": "Insight7",
        "force": True,
        "hostname": "172.25.46.11",
        "enclosureGroupUri": "EG:EG_46",
        "forceInstallFirmware": True,
        "licensingIntent": "OneView",
    },
    {
        "username": "Admin",
        "name": "ENCL_21",
        "password": "Insight7",
        "force": True,
        "hostname": "172.25.36.11",
        "enclosureGroupUri": "EG:EG_36",
        "forceInstallFirmware": False,
        "licensingIntent": "OneView",
    }
]

expected_enclosures = [
    {
        "name": "ENC-46",
        'logicalEnclosureUri': 'LE:ENC-46',
        'status': 'OK',
        'state': 'Configured',
        "enclosureGroupUri": "EG:EG_46",
        "licensingIntent": "OneView"
    },
    {
        "name": "ENC_41",
        'logicalEnclosureUri': 'LE:ENC_41',
        'status': 'OK',
        'state': 'Configured',
        "enclosureGroupUri": "EG:EG_41",
        "licensingIntent": "OneView"
    },
    {
        "name": "ENCL_21",
        'logicalEnclosureUri': 'LE:ENCL_21',
        "enclosureGroupUri": "EG:EG_36",
        'status': 'OK',
        'state': 'Configured',
        "licensingIntent": "OneView"
    }
]
servers = [
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "OneView",
        "memoryMb": 16384,
        "model": "ProLiant BL465c Gen8",
        "mpFirmwareVersion": "2.55 Aug 16 2017",
        "mpModel": "iLO4",
        "name": "ENC-46, bay 2",
        "partNumber": "634969-B21",
        "position": 2,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 16,
        "processorCount": 1,
        "processorSpeedMhz": 2300,
        "processorType": "AMD Opteron(TM) Processor 6276",
        "refreshState": "RefreshFailed",
        "romVersion": "A26 03/07/2016",
        "serialNumber": "MXQ2310M0V",
        "shortModel": "BL465c Gen8",
        "state": "Unmanaged",
        "stateReason": "BadUuid",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "OneView",
        "memoryMb": 16384,
        "model": "ProLiant BL465c Gen8",
        "mpFirmwareVersion": "2.55 Aug 16 2017",
        "mpModel": "iLO4",
        "name": "ENC-46, bay 1",
        "partNumber": "634969-B21",
        "position": 1,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 16,
        "processorCount": 1,
        "processorSpeedMhz": 2300,
        "processorType": "AMD Opteron(TM) Processor 6276",
        "refreshState": "NotRefreshing",
        "romVersion": "A26 03/07/2016",
        "serialNumber": "MXQ2220CFX",
        "shortModel": "BL465c Gen8",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "OneView",
        "memoryMb": 16384,
        "model": "ProLiant BL460c Gen9",
        "mpFirmwareVersion": "2.60 May 23 2018",
        "mpModel": "iLO4",
        "name": "ENC-46, bay 9",
        "partNumber": "727027-B21",
        "position": 9,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 6,
        "processorCount": 1,
        "processorSpeedMhz": 2400,
        "processorType": "Intel(R) Xeon(R) CPU E5-2620 v3 @ 2.40GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I36 v2.60 (05/21/2018)",
        "serialNumber": "2M2550035G",
        "shortModel": "BL460c Gen9",
        "state": "ProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "OneViewNoiLO",
        "memoryMb": 32768,
        "model": "ProLiant BL460c Gen8",
        "mpFirmwareVersion": "2.55 Aug 16 2017",
        "mpModel": "iLO4",
        "name": "ENC-46, bay 3",
        "partNumber": "670658-S01",
        "position": 3,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 8,
        "processorCount": 2,
        "processorSpeedMhz": 2000,
        "processorType": "Intel(R) Xeon(R) CPU E5-2650 0 @ 2.00GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I31 06/01/2015",
        "serialNumber": "MXQ2310LPD",
        "shortModel": "BL460c Gen8",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "OneViewNoiLO",
        "memoryMb": 16384,
        "model": "ProLiant BL460c Gen9",
        "mpFirmwareVersion": "2.60 May 23 2018",
        "mpModel": "iLO4",
        "name": "ENC-46, bay 10",
        "partNumber": "727027-B21",
        "position": 10,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 6,
        "processorCount": 1,
        "processorSpeedMhz": 2400,
        "processorType": "Intel(R) Xeon(R) CPU E5-2620 v3 @ 2.40GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I36 v2.60 (05/21/2018)",
        "serialNumber": "2M260804T2",
        "shortModel": "BL460c Gen9",
        "state": "ProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "OneView",
        "memoryMb": 131072,
        "model": "ProLiant BL460c Gen9",
        "mpFirmwareVersion": "2.60 May 23 2018",
        "mpModel": "iLO4",
        "name": "ENC_41, bay 9",
        "partNumber": "779803-S01",
        "position": 9,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 12,
        "processorCount": 2,
        "processorSpeedMhz": 2600,
        "processorType": "Intel(R) Xeon(R) CPU E5-2690 v3 @ 2.60GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I36 v2.60 (05/21/2018)",
        "serialNumber": "2M25450CS3",
        "shortModel": "BL460c Gen9",
        "state": "ProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "OneView",
        "memoryMb": 32768,
        "model": "ProLiant BL460c Gen8",
        "mpFirmwareVersion": "2.55 Aug 16 2017",
        "mpModel": "iLO4",
        "name": "ENC_41, bay 2",
        "partNumber": "670658-S01",
        "position": 2,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 6,
        "processorCount": 2,
        "processorSpeedMhz": 2000,
        "processorType": "Intel(R) Xeon(R) CPU E5-2620 0 @ 2.00GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I31 06/01/2015",
        "serialNumber": "MXQ2310LPY",
        "shortModel": "BL460c Gen8",
        "state": "ProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "OneView",
        "memoryMb": 131072,
        "model": "ProLiant BL460c Gen9",
        "mpFirmwareVersion": "2.60 May 23 2018",
        "mpModel": "iLO4",
        "name": "ENC_41, bay 10",
        "partNumber": "779803-S01",
        "position": 10,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 12,
        "processorCount": 2,
        "processorSpeedMhz": 2600,
        "processorType": "Intel(R) Xeon(R) CPU E5-2690 v3 @ 2.60GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I36 v2.60 (05/21/2018)",
        "serialNumber": "2M25470MP9",
        "shortModel": "BL460c Gen9",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "OneView",
        "memoryMb": 32768,
        "model": "ProLiant BL460c Gen8",
        "mpFirmwareVersion": "2.55 Aug 16 2017",
        "mpModel": "iLO4",
        "name": "ENC_41, bay 11",
        "partNumber": "670658-S01",
        "position": 11,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 6,
        "processorCount": 2,
        "processorSpeedMhz": 2000,
        "processorType": "Intel(R) Xeon(R) CPU E5-2620 0 @ 2.00GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I31 06/01/2015",
        "serialNumber": "MXQ2280F0F",
        "shortModel": "BL460c Gen8",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "OneView",
        "memoryMb": 32768,
        "model": "ProLiant BL460c Gen8",
        "mpFirmwareVersion": "2.55 Aug 16 2017",
        "mpModel": "iLO4",
        "name": "ENC_41, bay 1",
        "partNumber": "670658-S01",
        "position": 1,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 6,
        "processorCount": 2,
        "processorSpeedMhz": 2000,
        "processorType": "Intel(R) Xeon(R) CPU E5-2620 0 @ 2.00GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I31 06/01/2015",
        "serialNumber": "MXQ2240R3Z",
        "shortModel": "BL460c Gen8",
        "state": "ProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "OneView",
        "memoryMb": 16384,
        "model": "ProLiant BL460c Gen9",
        "mpFirmwareVersion": "2.55 Aug 16 2017",
        "mpModel": "iLO4",
        "name": "ENC_41, bay 16",
        "partNumber": "727027-B21",
        "position": 16,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 6,
        "processorCount": 1,
        "processorSpeedMhz": 2400,
        "processorType": "Intel(R) Xeon(R) CPU E5-2620 v3 @ 2.40GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I36 v2.52 (10/25/2017)",
        "serialNumber": "2M260804TJ",
        "shortModel": "BL460c Gen9",
        "state": "ProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "2U",
        "licensingIntent": "OneViewNoiLO",
        "memoryMb": 16384,
        "model": "ProLiant DL380p Gen8",
        "mpFirmwareVersion": "2.55 Aug 16 2017",
        "mpModel": "iLO4",
        "name": "ILO2M22290308",
        "partNumber": "642107-001",
        "position": 0,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 6,
        "processorCount": 1,
        "processorSpeedMhz": 2500,
        "processorType": "Intel(R) Xeon(R) CPU E5-2640 0 @ 2.50GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "P70 07/01/2015",
        "serialNumber": "2M22290308",
        "shortModel": "DL380p Gen8",
        "state": "ProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "2U",
        "licensingIntent": "OneViewNoiLO",
        "memoryMb": 49152,
        "model": "ProLiant DL380p Gen8",
        "mpFirmwareVersion": "2.55 Aug 16 2017",
        "mpModel": "iLO4",
        "name": "ILO2M22290306",
        "partNumber": "642107-001",
        "position": 0,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 6,
        "processorCount": 1,
        "processorSpeedMhz": 2500,
        "processorType": "Intel(R) Xeon(R) CPU E5-2640 0 @ 2.50GHz",
        "refreshState": "RefreshFailed",
        "romVersion": "P70 07/01/2015",
        "serialNumber": "2M22290306",
        "shortModel": "DL380p Gen8",
        "state": "Unmanaged",
        "stateReason": "Unconfigured",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "OneView",
        "memoryMb": 16384,
        "model": "ProLiant BL460c Gen9",
        "mpFirmwareVersion": "2.60 May 23 2018",
        "mpModel": "iLO4",
        "name": "ENCL_21, bay 10",
        "partNumber": "727027-B21",
        "position": 10,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 6,
        "processorCount": 1,
        "processorSpeedMhz": 2400,
        "processorType": "Intel(R) Xeon(R) CPU E5-2620 v3 @ 2.40GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I36 v2.60 (05/21/2018)",
        "serialNumber": "2M2550035R",
        "shortModel": "BL460c Gen9",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "OneView",
        "memoryMb": 32768,
        "model": "ProLiant BL460c Gen8",
        "mpFirmwareVersion": "2.55 Aug 16 2017",
        "mpModel": "iLO4",
        "name": "ENCL_21, bay 8",
        "partNumber": "670656-S01",
        "position": 8,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 8,
        "processorCount": 2,
        "processorSpeedMhz": 2000,
        "processorType": "Intel(R) Xeon(R) CPU E5-2650 0 @ 2.00GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I31 06/01/2015",
        "serialNumber": "MXQ230006R",
        "shortModel": "BL460c Gen8",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "OneView",
        "memoryMb": 16384,
        "model": "ProLiant BL460c Gen9",
        "mpFirmwareVersion": "2.60 May 23 2018",
        "mpModel": "iLO4",
        "name": "ENCL_21, bay 5",
        "partNumber": "727027-B21",
        "position": 5,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 6,
        "processorCount": 1,
        "processorSpeedMhz": 2400,
        "processorType": "Intel(R) Xeon(R) CPU E5-2620 v3 @ 2.40GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I36 v2.60 (05/21/2018)",
        "serialNumber": "2M260804TR",
        "shortModel": "BL460c Gen9",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "OneView",
        "memoryMb": 32768,
        "model": "ProLiant BL460c Gen8",
        "mpFirmwareVersion": "2.55 Aug 16 2017",
        "mpModel": "iLO4",
        "name": "ENCL_21, bay 11",
        "partNumber": "670658-S01",
        "position": 11,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 6,
        "processorCount": 2,
        "processorSpeedMhz": 2000,
        "processorType": "Intel(R) Xeon(R) CPU E5-2620 0 @ 2.00GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I31 06/01/2015",
        "serialNumber": "MXQ2240SMG",
        "shortModel": "BL460c Gen8",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "OneView",
        "memoryMb": 16384,
        "model": "ProLiant BL465c Gen8",
        "mpFirmwareVersion": "2.60 Mar 30 2018",
        "mpModel": "iLO4",
        "name": "ENCL_21, bay 9",
        "partNumber": "634969-B21",
        "position": 9,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 16,
        "processorCount": 1,
        "processorSpeedMhz": 2300,
        "processorType": "AMD Opteron(TM) Processor 6276",
        "refreshState": "RefreshFailed",
        "romVersion": "A26 11/02/2014",
        "serialNumber": "MXQ2510FWV",
        "shortModel": "BL465c Gen8",
        "state": "Unmanaged",
        "stateReason": "Unconfigured",
        "status": "OK",
        "type": "server-hardware-10"
    }
]

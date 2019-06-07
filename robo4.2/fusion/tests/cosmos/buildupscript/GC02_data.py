#!/usr/bin/env python

admin_credentials = {'userName': 'Administrator', 'password': 'Cosmos123'}
timeandlocale = {'localeDisplayName': 'English (United States)', 'locale': 'en_US.UTF-8', 'dateTime': '2018-09-07T06:04:49.886Z', 'ntpServers': [], 'timezone': 'UTC', 'type': 'TimeAndLocale'}
licenses = [
    {
        'key': 'YAQE DQAA H9PY 8HUY U7B5 HWW5 Y9JL KMPL UN6D NGJQ DXAU 2CSM GHTG L762 GMZ7 W9BA KJVT D5KM EFVW DT5J VBQJ 43CK SPS9 YG66 Z99R MWSN 6Z84 46XT WZJT HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTVG LS8T XU4E "EVAL-HPOV-NFR2 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR 9G6UAEJGUA4U"'
    },
    {
        'key': 'AA9C AQAA H9PY CHVY V7B5 HWWB Y9JL KMPL 3JKH 5FVM DXAU 2CSM GHTG L762 MTK7 FYB9 KJVT D5KM EFVW DT5J 4BEM M2SC SPS9 YG66 Z99R MWSN 6Z84 46XT WZJL HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTFG LS8T XU4E "EVAL-HPOV-NFR1 HPOV-NFR1 HP_OneView_16_Seat_NFR 7T36AEJG7JJ9"'
    },
    {
        'key': 'YAYC CQAA H9PQ GHX2 U7B5 HWW5 Y9JL KMPL FJ2H PFFM DXAU 2CSM GHTG L762 WTC5 GYBQ KJVT D5KM EFVW DT5J EBUM 62CC SPS9 YG66 Z99R MWSN 6Z84 46XT WZJT HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTVG LS8T XU4E "EVAL-HPOV-NFR2 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR 9G6UAEJGUA4U"'
    },
    {
        'key': '9AYC BQAA H9PQ GHXY U7B5 HWW5 Y9JL KMPL 3JSH 4FVM DXAU 2CSM GHTG L762 ETCZ WZRE KJVT D5KM EFVW DT5J 4BMM P2SC SPS9 YG66 Z99R MWSN 6Z84 46XT WZJT HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTVG LS8T XU4E "EVAL-HPOV-NFR2 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR 9G6UAEJGUA4U"'
    },
    {
        'key': '9A9C DQAA H9PY CHV2 V7B5 HWWB Y9JL KMPL DJKD 5FFM DXAU 2CSM GHTG L762 TT66 VZRY KJVT D5KM EFVW DT5J EBE9 M2CC SPS9 YG66 Z99R MWSN 6Z84 46XT WZJL HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTFG LS8T XU4E "EVAL-HPOV-NFR1 HPOV-NFR1 HP_OneView_16_Seat_NFR 7T36AEJG7JJ9"'
    },
    {
        'key': 'AAYC BQAA H9P9 KHXY V7B5 HWWB Y9JL KMPL JN6B 6HJ9 DXAU 2CSM GHTG L762 ZBW4 XN5A KJVT D5KM EFVW DT5J KFQ8 M4CC SPS9 YG66 Z99R MWSN 6Z84 46XT WZJL HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTFG LS8T XU4E "EVAL-HPOV-NFR1 HPOV-NFR1 HP_OneView_16_Seat_NFR 7T36AEJG7JJ9"'
    },
    {
        'key': '9AAG CQAA H9PA 8HW3 V7B5 HWWB Y9JL KMPL DNCD 4CZE DXAU 2CSM GHTG L762 B582 VPRU KJVT D5KM EFVW DT5J FBYP 87S6 SPS9 YG66 Z99R MWSN 6Z84 46XT WZJL HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTFG LS8T XU4E "EVAL-HPOV-NFR1 HPOV-NFR1 HP_OneView_16_Seat_NFR 7T36AEJG7JJ9"'
    }
]

appliance = {
    'type': "ApplianceNetworkConfigurationV2",
    'applianceNetworks':
    [{
        "device": "eth0",
        "macAddress": "00:50:56:a1:a9:f8",
        "interfaceName": "Appliance",
        "activeNode": 1,
        "unconfigure": False,
        "ipv4Type": "STATIC",
        "ipv4Subnet": "255.255.255.0",
        "ipv4Gateway": "172.25.56.1",
        "ipv4NameServers": [u'172.25.9.20'],
        "app1Ipv4Addr": "172.25.56.157",
        "ipv6Type": "UNCONFIGURE",
        "hostname": "Gc02upgrade.cosmos.net",
        "confOneNode": True,
        "domainName": "cosmos.net",
        "aliasDisabled": False
    }]
}

users = [
    {
        "type": "UserAndPermissions",
        "password": "wpsthpvse1",
        "userName": "administrator",
        "permissions": [{u'roleName': u'Infrastructure administrator', u'scopeUri': None}],
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
        "fullName": "Default appliance administrator",
        "status": None,
        "type": "UserAndPermissions",
        "userName": "administrator",
        "permissions": [{u'roleName': u'Infrastructure administrator', u'scopeUri': None}],
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
        "name": "eth2_1063",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1063
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth1_1065",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1065
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "DL_eth1",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1026
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "mgmnt",
        "privateNetwork": False,
        "purpose": "Management",
        "smartLink": True,
        "vlanId": 1027
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth_1057",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1057
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth2_1065",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1065
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth2_1066",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1066
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth2_1060",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1060
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth2_1061",
        "privateNetwork": False,
        "purpose": "VMMigration",
        "smartLink": True,
        "vlanId": 1061
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth_1056",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1056
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth1_1063",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1063
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth1_1064",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1064
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth1_1060",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1060
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth2_1067",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1067
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth1_1062",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1062
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth_1058",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1058
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth2_1068",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1068
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
        "name": "eth2_1069",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1069
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth1_1069",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1069
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
        "name": "eth1_1070",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1070
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth1_1067",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1067
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth2_1062",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1062
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "DL_eth2",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1026
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth1_1068",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1068
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth1_1066",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1066
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth2_1070",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1070
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "mgmnt1",
        "privateNetwork": False,
        "purpose": "Management",
        "smartLink": True,
        "vlanId": 1027
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth2_1064",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1064
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth1_1061",
        "privateNetwork": False,
        "purpose": "VMMigration",
        "smartLink": True,
        "vlanId": 1061
    }
]
expected_ethernet_networks = [
    {
        "uri": "ETH:eth2_1063",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth2_1063",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1063
    },
    {
        "uri": "ETH:eth1_1065",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth1_1065",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1065
    },
    {
        "uri": "ETH:DL_eth1",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "DL_eth1",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1026
    },
    {
        "uri": "ETH:mgmnt",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "mgmnt",
        "privateNetwork": False,
        "purpose": "Management",
        "smartLink": True,
        "vlanId": 1027
    },
    {
        "uri": "ETH:eth_1057",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth_1057",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1057
    },
    {
        "uri": "ETH:eth2_1065",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth2_1065",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1065
    },
    {
        "uri": "ETH:eth2_1066",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth2_1066",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1066
    },
    {
        "uri": "ETH:eth2_1060",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth2_1060",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1060
    },
    {
        "uri": "ETH:eth2_1061",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth2_1061",
        "privateNetwork": False,
        "purpose": "VMMigration",
        "smartLink": True,
        "vlanId": 1061
    },
    {
        "uri": "ETH:eth_1056",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth_1056",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1056
    },
    {
        "uri": "ETH:eth1_1063",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth1_1063",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1063
    },
    {
        "uri": "ETH:eth1_1064",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth1_1064",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1064
    },
    {
        "uri": "ETH:eth1_1060",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth1_1060",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1060
    },
    {
        "uri": "ETH:eth2_1067",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth2_1067",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1067
    },
    {
        "uri": "ETH:eth1_1062",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth1_1062",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1062
    },
    {
        "uri": "ETH:eth_1058",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth_1058",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1058
    },
    {
        "uri": "ETH:eth2_1068",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth2_1068",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1068
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
        "uri": "ETH:eth2_1069",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth2_1069",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1069
    },
    {
        "uri": "ETH:eth1_1069",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth1_1069",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1069
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
        "uri": "ETH:eth1_1070",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth1_1070",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1070
    },
    {
        "uri": "ETH:eth1_1067",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth1_1067",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1067
    },
    {
        "uri": "ETH:eth2_1062",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth2_1062",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1062
    },
    {
        "uri": "ETH:DL_eth2",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "DL_eth2",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1026
    },
    {
        "uri": "ETH:eth1_1068",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth1_1068",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1068
    },
    {
        "uri": "ETH:eth1_1066",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth1_1066",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1066
    },
    {
        "uri": "ETH:eth2_1070",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth2_1070",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1070
    },
    {
        "uri": "ETH:mgmnt1",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "mgmnt1",
        "privateNetwork": False,
        "purpose": "Management",
        "smartLink": True,
        "vlanId": 1027
    },
    {
        "uri": "ETH:eth2_1064",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth2_1064",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1064
    },
    {
        "uri": "ETH:eth1_1061",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth1_1061",
        "privateNetwork": False,
        "purpose": "VMMigration",
        "smartLink": True,
        "vlanId": 1061
    }
]

fc_networks = [
    {
        "type": "fc-networkV4",
        "name": "DAS1",
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
    },
    {
        "type": "fc-networkV4",
        "name": "DAS2",
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
    }
]
expected_fc_networks = [
    {
        "category": "fc-networks",
        "state": "Active",
        "description": None,
        "uri": "FC:DAS1",
        "status": "OK",
        "type": "fc-networkV4",
        "name": "DAS1",
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
    },
    {
        "category": "fc-networks",
        "state": "Active",
        "description": None,
        "uri": "FC:DAS2",
        "status": "OK",
        "type": "fc-networkV4",
        "name": "DAS2",
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
    }
]

fcoe_networks = [
    {
        "name": "fcoe1",
        "type": "fcoe-networkV4",
        "vlanId": 1021,
        "managedSanUri": "FCSan:VSAN1021"
    },
    {
        "name": "fcoe2",
        "type": "fcoe-networkV4",
        "vlanId": 1022,
        "managedSanUri": "FCSan:VSAN1022"
    }
]
expected_fcoe_networks = [
    {
        "uri": "FCOE:fcoe1",
        "state": "Active",
        "status": "OK",
        "name": "fcoe1",
        "type": "fcoe-networkV4",
        "vlanId": 1021,
        "managedSanUri": "FCSan:VSAN1021"
    },
    {
        "uri": "FCOE:fcoe2",
        "state": "Active",
        "status": "OK",
        "name": "fcoe2",
        "type": "fcoe-networkV4",
        "vlanId": 1022,
        "managedSanUri": "FCSan:VSAN1022"
    }
]

networksets = [
]
expected_networksets = [
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

        }
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
        }
    }
]

storage_pools_toedit = [
    {
        "storageSystemUri": "COSMOS-7400-9.125",
        "name": "MainStream-CPG",
        "isManaged": True,
    }
]

storage_volume_templates = [
]
expected_storage_volume_templates = [
]

add_existing_storage_volumes = [
]
expected_existing_storage_volumes = [
]

storage_volumes = [
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "Private",
            "isShareable": False,
            "name": "E16_CLRM_VOL",
            "provisioningType": "Thin",
            "size": 32212254720,
            "storagePool": "MainStream-CPG"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "Private",
            "isShareable": False,
            "name": "E16_CLRM_VOL (438)",
            "provisioningType": "Thin",
            "size": 32212254720,
            "storagePool": "MainStream-CPG"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "E16_DAS_ESX6.0U3",
            "provisioningType": "Thin",
            "size": 32212254720,
            "storagePool": "MainStream-CPG"
        },
    },
    {
        "templateUri": "ROOT",
        "isPermanent": True,
        "properties": {
            "description": "",
            "isShareable": True,
            "name": "E16_CLRM_Shared_VOL",
            "provisioningType": "Thin",
            "size": 214748364800,
            "storagePool": "MainStream-CPG"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "E26B12_RHEL7.4",
            "provisioningType": "Thin",
            "size": 32212254720,
            "storagePool": "MainStream-CPG"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "E16B9_FCOE_W2012",
            "provisioningType": "Thin",
            "size": 48318382080,
            "storagePool": "MainStream-CPG"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "Private",
            "isShareable": False,
            "name": "E16_CLRM_VOL (8058)",
            "provisioningType": "Thin",
            "size": 32212254720,
            "storagePool": "MainStream-CPG"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "Private",
            "isShareable": False,
            "name": "E16_CLRM_VOL (476)",
            "provisioningType": "Thin",
            "size": 32212254720,
            "storagePool": "MainStream-CPG"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "C02-E2, bay 9_QMH",
            "provisioningType": "Thin",
            "size": 48318382080,
            "storagePool": "MainStream-CPG"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "SpecifyBootTarget",
            "isShareable": False,
            "name": "C02-E2, bay 11_SLES12SP3",
            "provisioningType": "Thin",
            "size": 42949672960,
            "storagePool": "MainStream-CPG"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "E26B9_w16",
            "provisioningType": "Thin",
            "size": 48318382080,
            "storagePool": "MainStream-CPG"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "Private",
            "isShareable": False,
            "name": "E16_CLRM_VOL (4953)",
            "provisioningType": "Thin",
            "size": 32212254720,
            "storagePool": "MainStream-CPG"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "E26_B9CLRM_VOL",
            "provisioningType": "Thin",
            "size": 32212254720,
            "storagePool": "MainStream-CPG"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "cc02E3-b10",
            "provisioningType": "Full",
            "size": 21474836480,
            "storagePool": "MainStream-CPG"
        }
    }
]
expected_storage_volumes = [
    {
        "status": "OK",
        "uri": "SVOL:E16_CLRM_VOL",
        "properties": {
            "description": "Private",
            "isShareable": False,
            "name": "E16_CLRM_VOL",
            "provisioningType": "Thin",
            "size": 32212254720,
            "storagePoolUri": "SPOOL:MainStream-CPG"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:E16_CLRM_VOL (438)",
        "properties": {
            "description": "Private",
            "isShareable": False,
            "name": "E16_CLRM_VOL (438)",
            "provisioningType": "Thin",
            "size": 32212254720,
            "storagePoolUri": "SPOOL:MainStream-CPG"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:E16_DAS_ESX6.0U3",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "E16_DAS_ESX6.0U3",
            "provisioningType": "Thin",
            "size": 32212254720,
            "storagePoolUri": "SPOOL:MainStream-CPG"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:E16_CLRM_Shared_VOL",
        "isPermanent": True,
        "properties": {
            "description": "",
            "isShareable": True,
            "name": "E16_CLRM_Shared_VOL",
            "provisioningType": "Thin",
            "size": 214748364800,
            "storagePoolUri": "SPOOL:MainStream-CPG"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:E26B12_RHEL7.4",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "E26B12_RHEL7.4",
            "provisioningType": "Thin",
            "size": 32212254720,
            "storagePoolUri": "SPOOL:MainStream-CPG"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:E16B9_FCOE_W2012",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "E16B9_FCOE_W2012",
            "provisioningType": "Thin",
            "size": 48318382080,
            "storagePoolUri": "SPOOL:MainStream-CPG"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:E16_CLRM_VOL (8058)",
        "properties": {
            "description": "Private",
            "isShareable": False,
            "name": "E16_CLRM_VOL (8058)",
            "provisioningType": "Thin",
            "size": 32212254720,
            "storagePoolUri": "SPOOL:MainStream-CPG"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:E16_CLRM_VOL (476)",
        "properties": {
            "description": "Private",
            "isShareable": False,
            "name": "E16_CLRM_VOL (476)",
            "provisioningType": "Thin",
            "size": 32212254720,
            "storagePoolUri": "SPOOL:MainStream-CPG"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:C02-E2, bay 9_QMH",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "C02-E2, bay 9_QMH",
            "provisioningType": "Thin",
            "size": 48318382080,
            "storagePoolUri": "SPOOL:MainStream-CPG"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:C02-E2, bay 11_SLES12SP3",
        "properties": {
            "description": "SpecifyBootTarget",
            "isShareable": False,
            "name": "C02-E2, bay 11_SLES12SP3",
            "provisioningType": "Thin",
            "size": 42949672960,
            "storagePoolUri": "SPOOL:MainStream-CPG"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:E26B9_w16",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "E26B9_w16",
            "provisioningType": "Thin",
            "size": 48318382080,
            "storagePoolUri": "SPOOL:MainStream-CPG"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:E16_CLRM_VOL (4953)",
        "properties": {
            "description": "Private",
            "isShareable": False,
            "name": "E16_CLRM_VOL (4953)",
            "provisioningType": "Thin",
            "size": 32212254720,
            "storagePoolUri": "SPOOL:MainStream-CPG"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:E26_B9CLRM_VOL",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "E26_B9CLRM_VOL",
            "provisioningType": "Thin",
            "size": 32212254720,
            "storagePoolUri": "SPOOL:MainStream-CPG"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:cc02E3-b10",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "cc02E3-b10",
            "provisioningType": "Full",
            "size": 21474836480,
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
        "name": "Lig26_1",
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
                "enclosure": 1,
                "bay": 2,
                "type": "HP VC FlexFabric 10Gb/24-Port Module"
            },
            {
                "enclosureIndex": 1,
                "enclosure": 1,
                "bay": 1,
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
                    "bay": "2",
                    "port": "X5",
                    "enclosure": "1"
                }
            ],
            "mode": "Auto",
            "name": "eth2",
            "nativeNetworkUri": None,
            "networkType": "Ethernet",
            "networkUris": [
                "eth2_1060",
                "eth2_1065",
                "eth2_1069",
                "eth2_1061",
                "eth2_1070",
                "eth2_1067",
                "eth2_1066",
                "eth2_1063",
                "eth2_1064",
                "mgmnt1",
                "eth2_1068",
                "eth2_1062"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "Tagged",
            "lacpTimer": "Short",
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "bay": "1",
                    "port": "X5",
                    "enclosure": "1"
                }
            ],
            "mode": "Auto",
            "name": "eth1",
            "nativeNetworkUri": None,
            "networkType": "Ethernet",
            "networkUris": [
                "eth1_1064",
                "eth1_1070",
                "eth1_1065",
                "eth1_1063",
                "eth1_1061",
                "eth1_1068",
                "eth1_1066",
                "eth1_1069",
                "eth1_1060",
                "mgmnt",
                "eth1_1067",
                "eth1_1062"
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
            "ethernetNetworkType": "NotApplicable",
            "lacpTimer": None,
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "bay": "1",
                    "enclosure": "1",
                    "port": "X3"
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
        "name": "Lig21_2",
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
                "enclosure": 1,
                "bay": 3,
                "type": "HP VC 16Gb 24-Port FC Module"
            },
            {
                "enclosureIndex": 1,
                "enclosure": 1,
                "bay": 4,
                "type": "HP VC 16Gb 24-Port FC Module"
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
        }, {
            "ethernetNetworkType": "NotApplicable",
            "lacpTimer": None,
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "port": "3",
                    "enclosure": "1",
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
        "name": "Lig16_2",
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
                "enclosure": 1,
                "bay": 4,
                "type": "HP VC FlexFabric-20/40 F8 Module"
            },
            {
                "enclosureIndex": 1,
                "enclosure": 1,
                "bay": 3,
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
                    "port": "X1",
                    "enclosure": "1",
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
                    "port": "X1",
                    "enclosure": "1",
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
        }, {
            "ethernetNetworkType": "NotApplicable",
            "lacpTimer": None,
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "port": "X3",
                    "enclosure": "1",
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
        }, {
            "ethernetNetworkType": "NotApplicable",
            "lacpTimer": None,
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "port": "X3",
                    "enclosure": "1",
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
        "name": "Lig21_1",
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
                "enclosure": 1,
                "bay": 1,
                "type": "HP VC Flex-10/10D Module"
            },
            {
                "enclosureIndex": 1,
                "enclosure": 1,
                "bay": 2,
                "type": "HP VC Flex-10/10D Module"
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
                    "bay": "2",
                    "port": "X5",
                    "enclosure": "1"
                }
            ],
            "mode": "Auto",
            "name": "eth2",
            "nativeNetworkUri": None,
            "networkType": "Ethernet",
            "networkUris": [
                "eth2_1060",
                "eth2_1065",
                "eth2_1069",
                "eth2_1061",
                "eth2_1070",
                "eth2_1067",
                "eth2_1066",
                "eth2_1063",
                "eth2_1064",
                "mgmnt1",
                "eth2_1068",
                "eth2_1062"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "Tagged",
            "lacpTimer": "Short",
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "bay": "1",
                    "port": "X5",
                    "enclosure": "1"
                }
            ],
            "mode": "Auto",
            "name": "eth1",
            "nativeNetworkUri": None,
            "networkType": "Ethernet",
            "networkUris": [
                "eth1_1064",
                "eth1_1070",
                "eth1_1065",
                "eth1_1063",
                "eth1_1061",
                "eth1_1068",
                "eth1_1066",
                "eth1_1069",
                "eth1_1060",
                "mgmnt",
                "eth1_1067",
                "eth1_1062"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "Tagged",
            "lacpTimer": "Short",
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "port": "X1",
                    "enclosure": "1",
                    "bay": "1"
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
        }, {
            "ethernetNetworkType": "Tagged",
            "lacpTimer": "Short",
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "port": "X1",
                    "enclosure": "1",
                    "bay": "2"
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
        "name": "Lig26_2",
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
                "enclosure": 1,
                "bay": 3,
                "type": "HP VC FlexFabric-20/40 F8 Module"
            },
            {
                "enclosureIndex": 1,
                "enclosure": 1,
                "bay": 4,
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
        }, {
            "ethernetNetworkType": "NotApplicable",
            "lacpTimer": None,
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "port": "X3",
                    "enclosure": "1",
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
        "name": "eg1 logical interconnect group",
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
                "bay": 6,
                "enclosure": 1,
                "type": "HP VC 8Gb 20-Port FC Module"
            },
            {
                "enclosureIndex": 1,
                "enclosure": 1,
                "bay": 2,
                "type": "HP VC FlexFabric-20/40 F8 Module"
            },
            {
                "enclosureIndex": 1,
                "enclosure": 1,
                "bay": 3,
                "type": "HP VC 8Gb 24-Port FC Module"
            },
            {
                "enclosureIndex": 1,
                "enclosure": 1,
                "bay": 5,
                "type": "HP VC 8Gb 20-Port FC Module"
            },
            {
                "enclosureIndex": 1,
                "enclosure": 1,
                "bay": 4,
                "type": "HP VC 8Gb 24-Port FC Module"
            },
            {
                "enclosureIndex": 1,
                "enclosure": 1,
                "bay": 1,
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
        "uplinkSets": [
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
        "name": "Lig16_1",
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
                "enclosure": 1,
                "bay": 2,
                "type": "HP VC FlexFabric 10Gb/24-Port Module"
            },
            {
                "enclosureIndex": 1,
                "enclosure": 1,
                "bay": 1,
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
                    "bay": "1",
                    "enclosure": "1",
                    "port": "X3"
                }
            ],
            "mode": "Auto",
            "name": "das1",
            "nativeNetworkUri": None,
            "networkType": "FibreChannel",
            "networkUris": [
                "DAS1"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "Tagged",
            "lacpTimer": "Short",
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "bay": "2",
                    "port": "X5",
                    "enclosure": "1"
                }
            ],
            "mode": "Auto",
            "name": "eth2",
            "nativeNetworkUri": None,
            "networkType": "Ethernet",
            "networkUris": [
                "eth2_1060",
                "eth2_1065",
                "eth2_1069",
                "eth2_1061",
                "eth2_1070",
                "eth2_1067",
                "eth2_1066",
                "eth2_1063",
                "eth2_1064",
                "mgmnt1",
                "eth2_1068",
                "eth2_1062"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "Tagged",
            "lacpTimer": "Short",
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "bay": "1",
                    "port": "X5",
                    "enclosure": "1"
                }
            ],
            "mode": "Auto",
            "name": "eth1",
            "nativeNetworkUri": None,
            "networkType": "Ethernet",
            "networkUris": [
                "eth1_1064",
                "eth1_1070",
                "eth1_1065",
                "eth1_1063",
                "eth1_1061",
                "eth1_1068",
                "eth1_1066",
                "eth1_1069",
                "eth1_1060",
                "mgmnt",
                "eth1_1067",
                "eth1_1062"
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
                    "bay": "2"
                }
            ],
            "mode": "Auto",
            "name": "das2",
            "nativeNetworkUri": None,
            "networkType": "FibreChannel",
            "networkUris": [
                "DAS2"
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
        "uri": "LIG:Lig26_1",
        "status": None,
        "stackingHealth": None,
        "category": "logical-interconnect-groups",
        "state": "Active",
        "internalNetworkUris": "[]",
        "stackingMode": None,
        "description": None,
        "name": "Lig26_1",
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
        "uri": "LIG:Lig21_2",
        "status": None,
        "stackingHealth": None,
        "category": "logical-interconnect-groups",
        "state": "Active",
        "internalNetworkUris": "[]",
        "stackingMode": None,
        "description": None,
        "name": "Lig21_2",
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
        "uri": "LIG:Lig16_2",
        "status": None,
        "stackingHealth": None,
        "category": "logical-interconnect-groups",
        "state": "Active",
        "internalNetworkUris": "[]",
        "stackingMode": None,
        "description": None,
        "name": "Lig16_2",
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
        "uri": "LIG:Lig21_1",
        "status": None,
        "stackingHealth": None,
        "category": "logical-interconnect-groups",
        "state": "Active",
        "internalNetworkUris": "[]",
        "stackingMode": None,
        "description": None,
        "name": "Lig21_1",
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
        "uri": "LIG:Lig26_2",
        "status": None,
        "stackingHealth": None,
        "category": "logical-interconnect-groups",
        "state": "Active",
        "internalNetworkUris": "[]",
        "stackingMode": None,
        "description": None,
        "name": "Lig26_2",
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
        "uri": "LIG:eg1 logical interconnect group",
        "status": None,
        "stackingHealth": None,
        "category": "logical-interconnect-groups",
        "state": "Active",
        "internalNetworkUris": "[]",
        "stackingMode": "Enclosure",
        "description": None,
        "name": "eg1 logical interconnect group",
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
        "uri": "LIG:Lig16_1",
        "status": None,
        "stackingHealth": None,
        "category": "logical-interconnect-groups",
        "state": "Active",
        "internalNetworkUris": "[]",
        "stackingMode": None,
        "description": None,
        "name": "Lig16_1",
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
        "name": "EG_21",
        "interconnectBayMappings": [
            {
                "interconnectBay": 1,
                "logicalInterconnectGroupUri": "LIG:Lig21_1",

            },
            {
                "interconnectBay": 2,
                "logicalInterconnectGroupUri": "LIG:Lig21_1",

            },
            {
                "interconnectBay": 3,
                "logicalInterconnectGroupUri": "LIG:Lig21_2",

            },
            {
                "interconnectBay": 4,
                "logicalInterconnectGroupUri": "LIG:Lig21_2",

            }
        ],
        "ipAddressingMode": "External",
        "enclosureCount": 1
    },
    {
        "name": "EG_16",
        "interconnectBayMappings": [
            {
                "interconnectBay": 1,
                "logicalInterconnectGroupUri": "LIG:Lig16_1",
            },
            {
                "interconnectBay": 2,
                "logicalInterconnectGroupUri": "LIG:Lig16_1",
            },
            {
                "interconnectBay": 3,
                "logicalInterconnectGroupUri": "LIG:Lig16_2",
            },
            {
                "interconnectBay": 4,
                "logicalInterconnectGroupUri": "LIG:Lig16_2",
            }
        ],
        "ipAddressingMode": "External",
        "enclosureCount": 1
    },
    {
        "name": "EG_26",
        "interconnectBayMappings": [
            {
                "interconnectBay": 1,
                "logicalInterconnectGroupUri": "LIG:Lig26_1",

            },
            {
                "interconnectBay": 2,
                "logicalInterconnectGroupUri": "LIG:Lig26_1",

            },
            {
                "interconnectBay": 3,
                "logicalInterconnectGroupUri": "LIG:Lig26_2",
            },
            {
                "interconnectBay": 4,
                "logicalInterconnectGroupUri": "LIG:Lig26_2",
            }
        ],
        "ipAddressingMode": "External",
        "enclosureCount": 1
    }
]
expected_encgroups_add = [
    {
        "uri": "EG:EG_21",
        "description": None,
        "category": "enclosure-groups",
        "state": "Normal",
        "status": "OK",
        "powerMode": None,
        "portMappingCount": 8,
        "portMappings": [{u'midplanePort': 1, u'interconnectBay': 1}, {u'midplanePort': 2, u'interconnectBay': 2}, {u'midplanePort': 3, u'interconnectBay': 3}, {u'midplanePort': 4, u'interconnectBay': 4}, {u'midplanePort': 5, u'interconnectBay': 5}, {u'midplanePort': 6, u'interconnectBay': 6}, {u'midplanePort': 7, u'interconnectBay': 7}, {u'midplanePort': 8, u'interconnectBay': 8}],
        "ipRangeUris": [],
        "associatedLogicalInterconnectGroups": [u'LIG:Lig21_2', u'LIG:Lig21_1'],
        "name": "EG_21",
        "type": "EnclosureGroupV7",
        "enclosureTypeUri": "/rest/enclosure-types/c7000",
        "stackingMode": "Enclosure",
        "name": "EG_21",
        "interconnectBayMappingCount": "4",
        "interconnectBayMappings": [
            {
                "interconnectBay": 1,
                "logicalInterconnectGroupUri": "LIG:Lig21_1",
            },
            {
                "interconnectBay": 2,
                "logicalInterconnectGroupUri": "LIG:Lig21_1",
            },
            {
                "interconnectBay": 3,
                "logicalInterconnectGroupUri": "LIG:Lig21_2",
            },
            {
                "interconnectBay": 4,
                "logicalInterconnectGroupUri": "LIG:Lig21_2",
            }
        ],
        "ipAddressingMode": "External",
        "enclosureCount": 1
    },
    {
        "uri": "EG:EG_16",
        "description": None,
        "category": "enclosure-groups",
        "state": "Normal",
        "status": "OK",
        "powerMode": None,
        "portMappingCount": 8,
        "portMappings": [{u'midplanePort': 1, u'interconnectBay': 1}, {u'midplanePort': 2, u'interconnectBay': 2}, {u'midplanePort': 3, u'interconnectBay': 3}, {u'midplanePort': 4, u'interconnectBay': 4}, {u'midplanePort': 5, u'interconnectBay': 5}, {u'midplanePort': 6, u'interconnectBay': 6}, {u'midplanePort': 7, u'interconnectBay': 7}, {u'midplanePort': 8, u'interconnectBay': 8}],
        "ipRangeUris": [],
        "associatedLogicalInterconnectGroups": [u'LIG:Lig16_2', u'LIG:Lig16_1'],
        "name": "EG_16",
        "type": "EnclosureGroupV7",
        "enclosureTypeUri": "/rest/enclosure-types/c7000",
        "stackingMode": "Enclosure",
        "name": "EG_16",
        "interconnectBayMappingCount": "4",
        "interconnectBayMappings": [
            {
                "interconnectBay": 1,
                "logicalInterconnectGroupUri": "LIG:Lig16_1",

            },
            {
                "interconnectBay": 2,
                "logicalInterconnectGroupUri": "LIG:Lig16_1",

            },
            {
                "interconnectBay": 3,
                "logicalInterconnectGroupUri": "LIG:Lig16_2",

            },
            {
                "interconnectBay": 4,
                "logicalInterconnectGroupUri": "LIG:Lig16_2",

            }
        ],
        "ipAddressingMode": "External",
        "enclosureCount": 1
    },
    {
        "uri": "EG:EG_26",
        "description": None,
        "category": "enclosure-groups",
        "state": "Normal",
        "status": "OK",
        "powerMode": None,
        "portMappingCount": 8,
        "portMappings": [{u'midplanePort': 1, u'interconnectBay': 1}, {u'midplanePort': 2, u'interconnectBay': 2}, {u'midplanePort': 3, u'interconnectBay': 3}, {u'midplanePort': 4, u'interconnectBay': 4}, {u'midplanePort': 5, u'interconnectBay': 5}, {u'midplanePort': 6, u'interconnectBay': 6}, {u'midplanePort': 7, u'interconnectBay': 7}, {u'midplanePort': 8, u'interconnectBay': 8}],
        "ipRangeUris": [],
        "associatedLogicalInterconnectGroups": [u'LIG:Lig26_1', u'LIG:Lig26_2'],
        "name": "EG_26",
        "type": "EnclosureGroupV7",
        "enclosureTypeUri": "/rest/enclosure-types/c7000",
        "stackingMode": "Enclosure",
        "name": "EG_26",
        "interconnectBayMappingCount": "4",
        "interconnectBayMappings": [
            {
                "interconnectBay": 1,
                "logicalInterconnectGroupUri": "LIG:Lig26_1",

            },
            {
                "interconnectBay": 2,
                "logicalInterconnectGroupUri": "LIG:Lig26_1",

            },
            {
                "interconnectBay": 3,
                "logicalInterconnectGroupUri": "LIG:Lig26_2",

            },
            {
                "interconnectBay": 4,
                "logicalInterconnectGroupUri": "LIG:Lig26_2",

            }
        ],
        "ipAddressingMode": "External",
        "enclosureCount": 1
    }
]

logical_enclosure = [
    {
        "name": "Encl_96_CC02",
        "enclosureUris": [
            "ENC:C02-E3"
        ],
        "enclosureGroupUri": "EG:EG_26"
    },
    {
        "name": "Encl_21_11",
        "enclosureUris": [
            "ENC:C02-E2"
        ],
        "enclosureGroupUri": "EG:EG_21"
    },
    {
        "name": "Encl_91_CC03",
        "enclosureUris": [
            "ENC:C02-E1"
        ],
        "enclosureGroupUri": "EG:EG_16"
    }
]
expected_logical_enclosure = [
    {
        "type": "LogicalEnclosureV4",
        "uri": "Encl_96_CC02",
        "status": "OK",
        "name": "Encl_96_CC02",
        "enclosureUris": [
            "ENC:C02-E3"
        ],
        "enclosureGroupUri": "EG:EG_26"
    },
    {
        "type": "LogicalEnclosureV4",
        "uri": "Encl_21_11",
        "status": "OK",
        "name": "Encl_21_11",
        "enclosureUris": [
            "ENC:C02-E2"
        ],
        "enclosureGroupUri": "EG:EG_21"
    },
    {
        "type": "LogicalEnclosureV4",
        "uri": "Encl_91_CC03",
        "status": "OK",
        "name": "Encl_91_CC03",
        "enclosureUris": [
            "ENC:C02-E1"
        ],
        "enclosureGroupUri": "EG:EG_16"
    }
]

enclosures = [
    {
        "username": "Admin",
        "name": "C02-E1",
        "password": "Insight7",
        "force": True,
        "hostname": "172.25.16.11",
        "enclosureGroupUri": "EG:EG_16",
        "forceInstallFirmware": False,
        "licensingIntent": "OneView",
    },
    {
        "username": "Admin",
        "name": "C02-E2",
        "password": "Insight7",
        "force": True,
        "hostname": "172.25.21.11",
        "enclosureGroupUri": "EG:EG_21",
        "forceInstallFirmware": False,
        "licensingIntent": "OneView",
    },
    {
        "username": "Admin",
        "name": "C02-E3",
        "password": "Insight7",
        "force": True,
        "hostname": "172.25.26.11",
        "enclosureGroupUri": "EG:EG_26",
        "forceInstallFirmware": False,
        "licensingIntent": "OneView",
    }
]
expected_enclosures = [
    {
        "name": "C02-E3",
        'status': 'OK',
        'state': 'Configured',
        'logicalEnclosureUri': 'LE:Encl_96_CC02',
        "enclosureGroupUri": "EG:EG_26",
        "licensingIntent": "OneView"
    },
    {
        "name": "C02-E2",
        'status': 'OK',
        'state': 'Configured',
        'logicalEnclosureUri': 'LE:Encl_21_11',
        "enclosureGroupUri": "EG:EG_21",
        "licensingIntent": "OneView"
    },
    {
        "name": "C02-E3",
        'status': 'OK',
        'state': 'Configured',
        'logicalEnclosureUri': 'LE:Encl_91_CC03',
        "enclosureGroupUri": "EG:EG_16",
        "licensingIntent": "OneView"
    }
]
servers = [
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "OneViewNoiLO",
        "memoryMb": 32768,
        "model": "ProLiant BL460c Gen10",
        "mpFirmwareVersion": "1.40 Aug 20 2018",
        "mpModel": "iLO5",
        "name": "C02-E2, bay 10",
        "partNumber": "863445-B21",
        "position": 10,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 8,
        "processorCount": 2,
        "processorSpeedMhz": 1800,
        "processorType": "Intel(R) Xeon(R) Silver 4108 CPU @ 1.80GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I41 v2.00 (08/07/2018)",
        "serialNumber": "2M274505BB",
        "shortModel": "BL460c Gen10",
        "state": "ProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "OneView",
        "memoryMb": 32768,
        "model": "ProLiant BL460c Gen9",
        "mpFirmwareVersion": "2.60 May 23 2018",
        "mpModel": "iLO4",
        "name": "C02-E2, bay 11",
        "partNumber": "779806-S01",
        "position": 11,
        "powerLock": True,
        "powerState": "On",
        "processorCoreCount": 6,
        "processorCount": 1,
        "processorSpeedMhz": 2400,
        "processorType": "Intel(R) Xeon(R) CPU E5-2620 v3 @ 2.40GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I36 v2.60 (05/21/2018)",
        "serialNumber": "2M252614FW",
        "shortModel": "BL460c Gen9",
        "state": "ApplyingProfile",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "OneView",
        "memoryMb": 8192,
        "model": "ProLiant BL465c Gen8",
        "mpFirmwareVersion": "2.60 May 23 2018",
        "mpModel": "iLO4",
        "name": "C02-E2, bay 1",
        "partNumber": "634969-B21",
        "position": 1,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 16,
        "processorCount": 1,
        "processorSpeedMhz": 2300,
        "processorType": "AMD Opteron(TM) Processor 6276",
        "refreshState": "NotRefreshing",
        "romVersion": "A26 03/07/2016",
        "serialNumber": "MXQ2220CGG",
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
        "mpFirmwareVersion": "2.61 Jul 27 2018",
        "mpModel": "iLO4",
        "name": "C02-E1, bay 10",
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
        "serialNumber": "2M2638049K",
        "shortModel": "BL460c Gen9",
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
        "mpFirmwareVersion": "2.61 Jul 27 2018",
        "mpModel": "iLO4",
        "name": "C02-E1, bay 11",
        "partNumber": "727027-B21",
        "position": 11,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 6,
        "processorCount": 1,
        "processorSpeedMhz": 2400,
        "processorType": "Intel(R) Xeon(R) CPU E5-2620 v3 @ 2.40GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I36 v2.60 (05/21/2018)",
        "serialNumber": "2M2550035T",
        "shortModel": "BL460c Gen9",
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
        "mpFirmwareVersion": "2.61 Jul 27 2018",
        "mpModel": "iLO4",
        "name": "C02-E1, bay 2",
        "partNumber": "727027-B21",
        "position": 2,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 6,
        "processorCount": 1,
        "processorSpeedMhz": 2400,
        "processorType": "Intel(R) Xeon(R) CPU E5-2620 v3 @ 2.40GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I36 v2.60 (05/21/2018)",
        "serialNumber": "2M260804T3",
        "shortModel": "BL460c Gen9",
        "state": "ProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "OneView",
        "memoryMb": 24576,
        "model": "ProLiant BL420c Gen8",
        "mpFirmwareVersion": "2.60 Apr 13 2018",
        "mpModel": "iLO4",
        "name": "C02-E3, bay 1",
        "partNumber": "668356-B21",
        "position": 1,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 8,
        "processorCount": 2,
        "processorSpeedMhz": 2100,
        "processorType": "Intel(R) Xeon(R) CPU E5-2450 0 @ 2.10GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I30 11/03/2014",
        "serialNumber": "2M22330120",
        "shortModel": "BL420c Gen8",
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
        "mpFirmwareVersion": "2.55 Aug 16 2017",
        "mpModel": "iLO4",
        "name": "C02-E3, bay 2",
        "partNumber": "634969-B21",
        "position": 2,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 16,
        "processorCount": 1,
        "processorSpeedMhz": 2300,
        "processorType": "AMD Opteron(TM) Processor 6276",
        "refreshState": "NotRefreshing",
        "romVersion": "A26 03/07/2016",
        "serialNumber": "MXQ2310M0X",
        "shortModel": "BL465c Gen8",
        "state": "ProfileApplied",
        "stateReason": "NotApplicable",
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
        "name": "C02-E3, bay 3",
        "partNumber": "634969-B21",
        "position": 3,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 16,
        "processorCount": 1,
        "processorSpeedMhz": 2300,
        "processorType": "AMD Opteron(TM) Processor 6276",
        "refreshState": "NotRefreshing",
        "romVersion": "A26 03/07/2016",
        "serialNumber": "MXQ2310M08",
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
        "model": "ProLiant BL465c Gen8",
        "mpFirmwareVersion": "2.55 Aug 16 2017",
        "mpModel": "iLO4",
        "name": "C02-E3, bay 4",
        "partNumber": "634969-B21",
        "position": 4,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 16,
        "processorCount": 1,
        "processorSpeedMhz": 2300,
        "processorType": "AMD Opteron(TM) Processor 6276",
        "refreshState": "NotRefreshing",
        "romVersion": "A26 11/02/2014",
        "serialNumber": "MXQ2310GH7",
        "shortModel": "BL465c Gen8",
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
        "name": "C02-E3, bay 5",
        "partNumber": "670658-S01",
        "position": 5,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 6,
        "processorCount": 2,
        "processorSpeedMhz": 2000,
        "processorType": "Intel(R) Xeon(R) CPU E5-2620 0 @ 2.00GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I31 06/01/2015",
        "serialNumber": "MXQ2310LPC",
        "shortModel": "BL460c Gen8",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "OneViewNoiLO",
        "memoryMb": 32768,
        "model": "ProLiant BL460c Gen9",
        "mpFirmwareVersion": "2.61 Jul 27 2018",
        "mpModel": "iLO4",
        "name": "C02-E3, bay 9",
        "partNumber": "813194-B21",
        "position": 9,
        "powerLock": True,
        "powerState": "On",
        "processorCoreCount": 10,
        "processorCount": 1,
        "processorSpeedMhz": 2400,
        "processorType": "Intel(R) Xeon(R) CPU E5-2640 v4 @ 2.40GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I36 v2.60 (05/21/2018)",
        "serialNumber": "2M2619032Z",
        "shortModel": "BL460c Gen9",
        "state": "ApplyingProfile",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "OneView",
        "memoryMb": 32768,
        "model": "ProLiant BL460c Gen10",
        "mpFirmwareVersion": "1.40 Aug 20 2018",
        "mpModel": "iLO5",
        "name": "C02-E3, bay 12",
        "partNumber": "863445-B21",
        "position": 12,
        "powerLock": True,
        "powerState": "Off",
        "processorCoreCount": 8,
        "processorCount": 2,
        "processorSpeedMhz": 1800,
        "processorType": "Intel(R) Xeon(R) Silver 4108 CPU @ 1.80GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I41 v1.36 (02/14/2018)",
        "serialNumber": "2M274505BH",
        "shortModel": "BL460c Gen10",
        "state": "ApplyingProfile",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "OneView",
        "memoryMb": 32768,
        "model": "ProLiant BL460c Gen9",
        "mpFirmwareVersion": "2.61 Jul 27 2018",
        "mpModel": "iLO4",
        "name": "C02-E3, bay 13",
        "partNumber": "779806-S01",
        "position": 13,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 6,
        "processorCount": 1,
        "processorSpeedMhz": 2400,
        "processorType": "Intel(R) Xeon(R) CPU E5-2620 v3 @ 2.40GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I36 v2.56 (01/22/2018)",
        "serialNumber": "2M252614FX",
        "shortModel": "BL460c Gen9",
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
        "mpFirmwareVersion": "2.60 May 23 2018",
        "mpModel": "iLO4",
        "name": "C02-E2, bay 9",
        "partNumber": "727027-B21",
        "position": 9,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 6,
        "processorCount": 1,
        "processorSpeedMhz": 2400,
        "processorType": "Intel(R) Xeon(R) CPU E5-2620 v3 @ 2.40GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I36 v2.60 (05/21/2018)",
        "serialNumber": "2M260804TL",
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
        "mpFirmwareVersion": "2.60 May 23 2018",
        "mpModel": "iLO4",
        "name": "C02-E2, bay 2",
        "partNumber": "670658-S01",
        "position": 2,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 6,
        "processorCount": 2,
        "processorSpeedMhz": 2000,
        "processorType": "Intel(R) Xeon(R) CPU E5-2620 0 @ 2.00GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I31 06/01/2015",
        "serialNumber": "MXQ2260JHG",
        "shortModel": "BL460c Gen8",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "1U",
        "licensingIntent": "OneViewNoiLO",
        "memoryMb": 32768,
        "model": "ProLiant DL360p Gen8",
        "mpFirmwareVersion": "2.50 pass 50 May 23 2016",
        "mpModel": "iLO4",
        "name": "ILOMXQ23407LJ",
        "partNumber": "670635-S01",
        "position": 0,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 8,
        "processorCount": 2,
        "processorSpeedMhz": 2200,
        "processorType": "Intel(R) Xeon(R) CPU E5-2660 0 @ 2.20GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "P71 11/01/2014",
        "serialNumber": "MXQ23407LJ",
        "shortModel": "DL360p Gen8",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "2U",
        "licensingIntent": "OneView",
        "memoryMb": 163840,
        "model": "ProLiant DL380 Gen9",
        "mpFirmwareVersion": "2.60 May 23 2018",
        "mpModel": "iLO4",
        "name": "ILOMXQ63601X9",
        "partNumber": "719064-B21",
        "position": 0,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 10,
        "processorCount": 1,
        "processorSpeedMhz": 2400,
        "processorType": "Intel(R) Xeon(R) CPU E5-2640 v4 @ 2.40GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "P89 v2.60 (05/21/2018)",
        "serialNumber": "MXQ63601X9",
        "shortModel": "DL380 Gen9",
        "state": "ProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "OneViewNoiLO",
        "memoryMb": 32768,
        "model": "ProLiant BL460c Gen10",
        "mpFirmwareVersion": "1.40 Aug 20 2018",
        "mpModel": "iLO5",
        "name": "C02-E3, bay 10",
        "partNumber": "863445-B21",
        "position": 10,
        "powerLock": True,
        "powerState": "Off",
        "processorCoreCount": 8,
        "processorCount": 2,
        "processorSpeedMhz": 1800,
        "processorType": "Intel(R) Xeon(R) Silver 4108 CPU @ 1.80GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I41 v2.00 (08/17/2018)",
        "serialNumber": "2M274505BK",
        "shortModel": "BL460c Gen10",
        "state": "ApplyingProfile",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "OneView",
        "memoryMb": 16384,
        "model": "ProLiant BL460c Gen9",
        "mpFirmwareVersion": "2.61 Jul 27 2018",
        "mpModel": "iLO4",
        "name": "C02-E1, bay 9",
        "partNumber": "727027-B21",
        "position": 9,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 6,
        "processorCount": 1,
        "processorSpeedMhz": 2400,
        "processorType": "Intel(R) Xeon(R) CPU E5-2620 v3 @ 2.40GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I36 v2.60 (05/21/2018)",
        "serialNumber": "2M260804TT",
        "shortModel": "BL460c Gen9",
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
        "mpFirmwareVersion": "2.61 Jul 27 2018",
        "mpModel": "iLO4",
        "name": "C02-E1, bay 3",
        "partNumber": "727027-B21",
        "position": 3,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 6,
        "processorCount": 1,
        "processorSpeedMhz": 2400,
        "processorType": "Intel(R) Xeon(R) CPU E5-2620 v3 @ 2.40GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I36 v2.60 (05/21/2018)",
        "serialNumber": "2M260804TN",
        "shortModel": "BL460c Gen9",
        "state": "ProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    }
]

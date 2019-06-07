#!/usr/bin/env python

admin_credentials = {'userName': 'Administrator', 'password': 'Cosmos123'}
timeandlocale = {'localeDisplayName': 'English (United States)', 'locale': 'en_US.UTF-8', 'dateTime': '2018-09-11T10:18:52.711Z', 'ntpServers': [], 'timezone': 'UTC', 'type': 'TimeAndLocale'}
licenses = [
    {
        'key': '9AYC BQAA H9PQ GHXY U7B5 HWW5 Y9JL KMPL 3JSH 4FVM DXAU 2CSM GHTG L762 ETCZ WZRE KJVT D5KM EFVW DT5J 4BMM P2SC SPS9 YG66 Z99R MWSN 6Z84 46XT WZJT HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTVG LS8T XU4E "EVAL-HPOV-NFR2 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR 9G6UAEJGUA4U"'
    },
    {
        'key': 'YAYC CQAA H9PQ GHX2 U7B5 HWW5 Y9JL KMPL FJ2H PFFM DXAU 2CSM GHTG L762 WTC5 GYBQ KJVT D5KM EFVW DT5J EBUM 62CC SPS9 YG66 Z99R MWSN 6Z84 46XT WZJT HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTVG LS8T XU4E "EVAL-HPOV-NFR2 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR 9G6UAEJGUA4U"'
    },
    {
        'key': '9A9C DQAA H9PY CHV2 V7B5 HWWB Y9JL KMPL DJKD 5FFM DXAU 2CSM GHTG L762 TT66 VZRY KJVT D5KM EFVW DT5J EBE9 M2CC SPS9 YG66 Z99R MWSN 6Z84 46XT WZJL HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTFG LS8T XU4E "EVAL-HPOV-NFR1 HPOV-NFR1 HP_OneView_16_Seat_NFR 7T36AEJG7JJ9"'
    },
    {
        'key': 'AA9C AQAA H9PY CHVY V7B5 HWWB Y9JL KMPL 3JKH 5FVM DXAU 2CSM GHTG L762 MTK7 FYB9 KJVT D5KM EFVW DT5J 4BEM M2SC SPS9 YG66 Z99R MWSN 6Z84 46XT WZJL HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTFG LS8T XU4E "EVAL-HPOV-NFR1 HPOV-NFR1 HP_OneView_16_Seat_NFR 7T36AEJG7JJ9"'
    }
]

appliance = {
    'type': "ApplianceNetworkConfigurationV2",
    'applianceNetworks':
    [{
        "device": "eth0",
        "macAddress": "00:15:5d:38:b5:15",
        "interfaceName": "Appliance",
        "activeNode": 1,
        "unconfigure": False,
        "ipv4Type": "STATIC",
        "ipv4Subnet": "255.255.255.0",
        "ipv4Gateway": "172.25.27.1",
        "ipv4NameServers": [],
        "app1Ipv4Addr": "172.25.27.51",
        "ipv6Type": "UNCONFIGURE",
        "hostname": "ci-00155d38b515",
        "confOneNode": True,
        "domainName": "",
        "aliasDisabled": False
    }]
}

users = [
    {
        "type": "UserAndPermissions",
        "password": "Cosmos123",
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
    }
]
expected_san_managers = [
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
    }
]

ethernet_networks = [
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth2_1059",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1059
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth1_1053",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1053
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth2_1052",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1052
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth_1014",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1014
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth_1012",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1012
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "iSCSI-1",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1009
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth2_1055",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1055
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth2_1054",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1054
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth1_1057",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1057
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth_1013",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1013
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth1_1058",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1058
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth1_1059",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1059
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth2_1053",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1053
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth2_1061",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1061
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth2_1058",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1058
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth1_1060",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1060
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth1_1061",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1061
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth1_1052",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1052
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth2_1060",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1060
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth_1011",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1011
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth2_1057",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1057
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth2_1056",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1056
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth1_1051",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1051
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "iSCSI-2",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1009
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth1_1055",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1055
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth1_1054",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1054
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth1_1056",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1056
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth2_1051",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1051
    }
]
expected_ethernet_networks = [
    {
        "uri": "ETH:Eth2_1059",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth2_1059",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1059
    },
    {
        "uri": "ETH:Eth1_1053",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth1_1053",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1053
    },
    {
        "uri": "ETH:Eth2_1052",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth2_1052",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1052
    },
    {
        "uri": "ETH:eth_1014",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth_1014",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1014
    },
    {
        "uri": "ETH:eth_1012",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth_1012",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1012
    },
    {
        "uri": "ETH:iSCSI-1",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "iSCSI-1",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1009
    },
    {
        "uri": "ETH:Eth2_1055",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth2_1055",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1055
    },
    {
        "uri": "ETH:Eth2_1054",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth2_1054",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1054
    },
    {
        "uri": "ETH:Eth1_1057",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth1_1057",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1057
    },
    {
        "uri": "ETH:eth_1013",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth_1013",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1013
    },
    {
        "uri": "ETH:Eth1_1058",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth1_1058",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1058
    },
    {
        "uri": "ETH:Eth1_1059",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth1_1059",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1059
    },
    {
        "uri": "ETH:Eth2_1053",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth2_1053",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1053
    },
    {
        "uri": "ETH:Eth2_1061",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth2_1061",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1061
    },
    {
        "uri": "ETH:Eth2_1058",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth2_1058",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1058
    },
    {
        "uri": "ETH:Eth1_1060",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth1_1060",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1060
    },
    {
        "uri": "ETH:Eth1_1061",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth1_1061",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1061
    },
    {
        "uri": "ETH:Eth1_1052",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth1_1052",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1052
    },
    {
        "uri": "ETH:Eth2_1060",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth2_1060",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1060
    },
    {
        "uri": "ETH:eth_1011",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth_1011",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1011
    },
    {
        "uri": "ETH:Eth2_1057",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth2_1057",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1057
    },
    {
        "uri": "ETH:Eth2_1056",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth2_1056",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1056
    },
    {
        "uri": "ETH:Eth1_1051",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth1_1051",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1051
    },
    {
        "uri": "ETH:iSCSI-2",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "iSCSI-2",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1009
    },
    {
        "uri": "ETH:Eth1_1055",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth1_1055",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1055
    },
    {
        "uri": "ETH:Eth1_1054",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth1_1054",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1054
    },
    {
        "uri": "ETH:Eth1_1056",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth1_1056",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1056
    },
    {
        "uri": "ETH:Eth2_1051",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth2_1051",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1051
    }
]

fc_networks = [
    {
        "type": "fc-networkV4",
        "name": "DASnet_2",
        "fabricType": "DirectAttach",
        "linkStabilityTime": 0,
        "autoLoginRedistribution": False,
        "managedSanUri": None
    },
    {
        "type": "fc-networkV4",
        "name": "FC1",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:NFV-BNA-SW1"
    },
    {
        "type": "fc-networkV4",
        "name": "FC2",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:NFV-BNA-SW2"
    },
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
        "name": "FC_net1",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:NFV-BNA-SW1"
    },
    {
        "type": "fc-networkV4",
        "name": "FC_net2",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:NFV-BNA-SW2"
    },
    {
        "type": "fc-networkV4",
        "name": "DASnet_1",
        "fabricType": "DirectAttach",
        "linkStabilityTime": 0,
        "autoLoginRedistribution": False,
        "managedSanUri": None
    },
    {
        "type": "fc-networkV4",
        "name": "DAS2",
        "fabricType": "DirectAttach",
        "linkStabilityTime": 0,
        "autoLoginRedistribution": False,
        "managedSanUri": None
    }
]
expected_fc_networks = [
    {
        "category": "fc-networks",
        "state": "Active",
        "description": None,
        "uri": "FC:DASnet_2",
        "status": "OK",
        "type": "fc-networkV4",
        "name": "DASnet_2",
        "fabricType": "DirectAttach",
        "linkStabilityTime": 0,
        "autoLoginRedistribution": False,
        "managedSanUri": None
    },
    {
        "category": "fc-networks",
        "state": "Active",
        "description": None,
        "uri": "FC:FC1",
        "status": "OK",
        "type": "fc-networkV4",
        "name": "FC1",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:NFV-BNA-SW1"
    },
    {
        "category": "fc-networks",
        "state": "Active",
        "description": None,
        "uri": "FC:FC2",
        "status": "OK",
        "type": "fc-networkV4",
        "name": "FC2",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:NFV-BNA-SW2"
    },
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
        "uri": "FC:FC_net1",
        "status": "OK",
        "type": "fc-networkV4",
        "name": "FC_net1",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:NFV-BNA-SW1"
    },
    {
        "category": "fc-networks",
        "state": "Active",
        "description": None,
        "uri": "FC:FC_net2",
        "status": "OK",
        "type": "fc-networkV4",
        "name": "FC_net2",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:NFV-BNA-SW2"
    },
    {
        "category": "fc-networks",
        "state": "Active",
        "description": None,
        "uri": "FC:DASnet_1",
        "status": "OK",
        "type": "fc-networkV4",
        "name": "DASnet_1",
        "fabricType": "DirectAttach",
        "linkStabilityTime": 0,
        "autoLoginRedistribution": False,
        "managedSanUri": None
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
    }
]

fcoe_networks = [
    {
        "name": "VSAN1022",
        "type": "fcoe-networkV4",
        "vlanId": 1022,
        "managedSanUri": "FCSan:VSAN1022"
    },
    {
        "name": "FCOE_net1",
        "type": "fcoe-networkV4",
        "vlanId": 1021,
        "managedSanUri": "FCSan:VSAN1021"
    },
    {
        "name": "VSAN1021",
        "type": "fcoe-networkV4",
        "vlanId": 1021,
        "managedSanUri": "FCSan:VSAN1021"
    },
    {
        "name": "FCOE_net2",
        "type": "fcoe-networkV4",
        "vlanId": 1022,
        "managedSanUri": "FCSan:VSAN1022"
    }
]
expected_fcoe_networks = [
    {
        "uri": "FCOE:VSAN1022",
        "state": "Active",
        "status": "OK",
        "name": "VSAN1022",
        "type": "fcoe-networkV4",
        "vlanId": 1022,
        "managedSanUri": "FCSan:VSAN1022"
    },
    {
        "uri": "FCOE:FCOE_net1",
        "state": "Active",
        "status": "OK",
        "name": "FCOE_net1",
        "type": "fcoe-networkV4",
        "vlanId": 1021,
        "managedSanUri": "FCSan:VSAN1021"
    },
    {
        "uri": "FCOE:VSAN1021",
        "state": "Active",
        "status": "OK",
        "name": "VSAN1021",
        "type": "fcoe-networkV4",
        "vlanId": 1021,
        "managedSanUri": "FCSan:VSAN1021"
    },
    {
        "uri": "FCOE:FCOE_net2",
        "state": "Active",
        "status": "OK",
        "name": "FCOE_net2",
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
        "isPermanent": True,
        "properties": {
            "description": "",
            "isShareable": True,
            "name": "Quorum",
            "provisioningType": "Thin",
            "size": 5368709120,
            "storagePool": "MainStream-CPG"
        },
    },
    {
        "templateUri": "ROOT",
        "isPermanent": True,
        "properties": {
            "description": "",
            "isShareable": True,
            "name": "Shared Volume",
            "provisioningType": "Thin",
            "size": 107374182400,
            "storagePool": "MainStream-CPG"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "OS VOL 2016_Ravi",
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
            "name": "Node2OS_Ravi",
            "provisioningType": "Thin",
            "size": 53687091200,
            "storagePool": "MainStream-CPG"
        },
    },
    {
        "templateUri": "ROOT",
        "isPermanent": True,
        "properties": {
            "description": "",
            "isShareable": True,
            "name": "ESX shared vol",
            "provisioningType": "Thin",
            "size": 107374182400,
            "storagePool": "MainStream-CPG"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "ESXi Boot vol",
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
            "name": "Vol1",
            "provisioningType": "Thin",
            "size": 64424509440,
            "storagePool": "MainStream-CPG"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "Vol1 (1254)",
            "provisioningType": "Thin",
            "size": 64424509440,
            "storagePool": "MainStream-CPG"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "Vol2",
            "provisioningType": "Thin",
            "size": 107374182400,
            "storagePool": "MainStream-CPG"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "Vol3",
            "provisioningType": "Thin",
            "size": 107374182400,
            "storagePool": "MainStream-CPG"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "SLESVOL",
            "provisioningType": "Thin",
            "size": 107374182400,
            "storagePool": "MainStream-CPG"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "RHELVOL",
            "provisioningType": "Thin",
            "size": 85899345920,
            "storagePool": "MainStream-CPG"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "DAS1_vol",
            "provisioningType": "Thin",
            "size": 85899345920,
            "storagePool": "MainStream-CPG"
        }
    }
]
expected_storage_volumes = [
    {
        "status": "OK",
        "uri": "SVOL:Quorum",
        "isPermanent": True,
        "properties": {
            "description": "",
            "isShareable": True,
            "name": "Quorum",
            "provisioningType": "Thin",
            "size": 5368709120,
            "storagePoolUri": "SPOOL:MainStream-CPG"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:Shared Volume",
        "isPermanent": True,
        "properties": {
            "description": "",
            "isShareable": True,
            "name": "Shared Volume",
            "provisioningType": "Thin",
            "size": 107374182400,
            "storagePoolUri": "SPOOL:MainStream-CPG"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:OS VOL 2016_Ravi",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "OS VOL 2016_Ravi",
            "provisioningType": "Thin",
            "size": 53687091200,
            "storagePoolUri": "SPOOL:MainStream-CPG"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:Node2OS_Ravi",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "Node2OS_Ravi",
            "provisioningType": "Thin",
            "size": 53687091200,
            "storagePoolUri": "SPOOL:MainStream-CPG"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:ESX shared vol",
        "isPermanent": True,
        "properties": {
            "description": "",
            "isShareable": True,
            "name": "ESX shared vol",
            "provisioningType": "Thin",
            "size": 107374182400,
            "storagePoolUri": "SPOOL:MainStream-CPG"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:ESXi Boot vol",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "ESXi Boot vol",
            "provisioningType": "Thin",
            "size": 21474836480,
            "storagePoolUri": "SPOOL:MainStream-CPG"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:Vol1",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "Vol1",
            "provisioningType": "Thin",
            "size": 64424509440,
            "storagePoolUri": "SPOOL:MainStream-CPG"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:Vol1 (1254)",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "Vol1 (1254)",
            "provisioningType": "Thin",
            "size": 64424509440,
            "storagePoolUri": "SPOOL:MainStream-CPG"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:Vol2",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "Vol2",
            "provisioningType": "Thin",
            "size": 107374182400,
            "storagePoolUri": "SPOOL:MainStream-CPG"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:Vol3",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "Vol3",
            "provisioningType": "Thin",
            "size": 107374182400,
            "storagePoolUri": "SPOOL:MainStream-CPG"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:SLESVOL",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "SLESVOL",
            "provisioningType": "Thin",
            "size": 107374182400,
            "storagePoolUri": "SPOOL:MainStream-CPG"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:RHELVOL",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "RHELVOL",
            "provisioningType": "Thin",
            "size": 85899345920,
            "storagePoolUri": "SPOOL:MainStream-CPG"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:DAS1_vol",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "DAS1_vol",
            "provisioningType": "Thin",
            "size": 85899345920,
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
        "name": "LIG_C",
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
                "bay": 5,
                "type": "HP VC 8Gb 20-Port FC Module"
            },
            {
                "enclosureIndex": 1,
                "enclosure": 1,
                "bay": 6,
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
                    "bay": "6"
                }
            ],
            "mode": "Auto",
            "name": "fc2",
            "nativeNetworkUri": None,
            "networkType": "FibreChannel",
            "networkUris": [
                "FC_net2"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "NotApplicable",
            "lacpTimer": None,
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "bay": "5",
                    "enclosure": "1",
                    "port": "3"
                }
            ],
            "mode": "Auto",
            "name": "fc1",
            "nativeNetworkUri": None,
            "networkType": "FibreChannel",
            "networkUris": [
                "FC_net1"
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
        "name": "51.11-Lig Bay 3 & 4",
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
                "type": "HP VC FlexFabric 10Gb/24-Port Module"
            },
            {
                "enclosureIndex": 1,
                "enclosure": 1,
                "bay": 4,
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
                    "port": "X1",
                    "enclosure": "1",
                    "bay": "4"
                }
            ],
            "mode": "Auto",
            "name": "VSAN1022",
            "nativeNetworkUri": None,
            "networkType": "Ethernet",
            "networkUris": [
                "VSAN1022"
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
                    "bay": "3"
                }
            ],
            "mode": "Auto",
            "name": "VSAN1021",
            "nativeNetworkUri": None,
            "networkType": "Ethernet",
            "networkUris": [
                "VSAN1021"
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
        "name": "61.11 Bay 5 & 6",
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
                "bay": 6,
                "type": "HP VC 8Gb 20-Port FC Module"
            },
            {
                "enclosureIndex": 1,
                "enclosure": 1,
                "bay": 5,
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
                    "bay": "6"
                }
            ],
            "mode": "Auto",
            "name": "FC2",
            "nativeNetworkUri": None,
            "networkType": "FibreChannel",
            "networkUris": [
                "FC2"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "NotApplicable",
            "lacpTimer": None,
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "bay": "5",
                    "enclosure": "1",
                    "port": "3"
                }
            ],
            "mode": "Auto",
            "name": "FC1",
            "nativeNetworkUri": None,
            "networkType": "FibreChannel",
            "networkUris": [
                "FC1"
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
        "name": "56.11 LIG Bay 2 & 3",
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
                    "bay": "4",
                    "enclosure": "1",
                    "port": "X4"
                }
            ],
            "mode": "Auto",
            "name": "iSCSI-2",
            "nativeNetworkUri": None,
            "networkType": "Ethernet",
            "networkUris": [
                "iSCSI-2"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "Tagged",
            "lacpTimer": "Short",
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "port": "X4",
                    "enclosure": "1",
                    "bay": "3"
                }
            ],
            "mode": "Auto",
            "name": "iSCSCI-1",
            "nativeNetworkUri": None,
            "networkType": "Ethernet",
            "networkUris": [
                "iSCSI-1"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "NotApplicable",
            "lacpTimer": None,
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "bay": "4",
                    "enclosure": "1",
                    "port": "X3"
                }
            ],
            "mode": "Auto",
            "name": "FC2",
            "nativeNetworkUri": None,
            "networkType": "FibreChannel",
            "networkUris": [
                "FC2"
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
            "name": "FC1",
            "nativeNetworkUri": None,
            "networkType": "FibreChannel",
            "networkUris": [
                "FC1"
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
        "name": "61.11 Bay 3 & 4",
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
            "name": "FC1",
            "nativeNetworkUri": None,
            "networkType": "FibreChannel",
            "networkUris": [
                "FC1"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "NotApplicable",
            "lacpTimer": None,
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "bay": "4",
                    "enclosure": "1",
                    "port": "3"
                }
            ],
            "mode": "Auto",
            "name": "FC2",
            "nativeNetworkUri": None,
            "networkType": "FibreChannel",
            "networkUris": [
                "FC2"
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
        "name": "56.11 LIG Bay 1 & 2",
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
                    "bay": "1",
                    "enclosure": "1",
                    "port": "X5"
                }
            ],
            "mode": "Auto",
            "name": "Eth1",
            "nativeNetworkUri": None,
            "networkType": "Ethernet",
            "networkUris": [
                "Eth1_1059",
                "Eth1_1051",
                "Eth1_1057",
                "Eth1_1052",
                "Eth1_1060",
                "Eth1_1056",
                "Eth1_1053",
                "Eth1_1058",
                "Eth1_1054",
                "Eth1_1061",
                "Eth1_1055"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "Tagged",
            "lacpTimer": "Short",
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "bay": "2",
                    "enclosure": "1",
                    "port": "X5"
                }
            ],
            "mode": "Auto",
            "name": "Eth2",
            "nativeNetworkUri": None,
            "networkType": "Ethernet",
            "networkUris": [
                "Eth2_1057",
                "Eth2_1051",
                "Eth2_1052",
                "Eth2_1058",
                "Eth2_1053",
                "Eth2_1054",
                "Eth2_1056",
                "Eth2_1055",
                "Eth2_1059",
                "Eth2_1061",
                "Eth2_1060"
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
        "name": "61.11 Bay 1 & 2",
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
                "type": "HP VC FlexFabric-20/40 F8 Module"
            },
            {
                "enclosureIndex": 1,
                "enclosure": 1,
                "bay": 2,
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
                    "port": "X2",
                    "enclosure": "1",
                    "bay": "1"
                }
            ],
            "mode": "Auto",
            "name": "DAS-1",
            "nativeNetworkUri": None,
            "networkType": "FibreChannel",
            "networkUris": [
                "DAS1"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "NotApplicable",
            "lacpTimer": None,
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "port": "X1",
                    "enclosure": "1",
                    "bay": "1"
                }
            ],
            "mode": "Auto",
            "name": "FCOE-1",
            "nativeNetworkUri": None,
            "networkType": "FibreChannel",
            "networkUris": [
                "FC1"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "NotApplicable",
            "lacpTimer": None,
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "port": "X1",
                    "enclosure": "1",
                    "bay": "2"
                }
            ],
            "mode": "Auto",
            "name": "FCOE-2",
            "nativeNetworkUri": None,
            "networkType": "FibreChannel",
            "networkUris": [
                "FC2"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "Tagged",
            "lacpTimer": "Short",
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "bay": "2",
                    "enclosure": "1",
                    "port": "X5"
                }
            ],
            "mode": "Auto",
            "name": "Eth2",
            "nativeNetworkUri": None,
            "networkType": "Ethernet",
            "networkUris": [
                "Eth2_1057",
                "Eth2_1051",
                "Eth2_1052",
                "Eth2_1058",
                "Eth2_1053",
                "Eth2_1054",
                "Eth2_1056",
                "Eth2_1055",
                "Eth2_1059",
                "Eth2_1061",
                "Eth2_1060"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "NotApplicable",
            "lacpTimer": None,
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "port": "X2",
                    "enclosure": "1",
                    "bay": "2"
                }
            ],
            "mode": "Auto",
            "name": "DAS-2",
            "nativeNetworkUri": None,
            "networkType": "FibreChannel",
            "networkUris": [
                "DAS2"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "Tagged",
            "lacpTimer": "Short",
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "bay": "1",
                    "enclosure": "1",
                    "port": "X5"
                }
            ],
            "mode": "Auto",
            "name": "Eth1",
            "nativeNetworkUri": None,
            "networkType": "Ethernet",
            "networkUris": [
                "Eth1_1059",
                "Eth1_1051",
                "Eth1_1057",
                "Eth1_1052",
                "Eth1_1060",
                "Eth1_1056",
                "Eth1_1053",
                "Eth1_1058",
                "Eth1_1054",
                "Eth1_1061",
                "Eth1_1055"
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
        "name": "51.11-LIG bay 1 & 2",
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
                "type": "HP VC FlexFabric-20/40 F8 Module"
            },
            {
                "enclosureIndex": 1,
                "enclosure": 1,
                "bay": 2,
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
                    "bay": "2",
                    "enclosure": "1",
                    "port": "X5"
                }
            ],
            "mode": "Auto",
            "name": "Eth2",
            "nativeNetworkUri": None,
            "networkType": "Ethernet",
            "networkUris": [
                "Eth2_1057",
                "Eth2_1051",
                "Eth2_1052",
                "Eth2_1058",
                "Eth2_1053",
                "Eth2_1054",
                "Eth2_1056",
                "Eth2_1055",
                "Eth2_1059",
                "Eth2_1061",
                "Eth2_1060"
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
            "name": "FC1",
            "nativeNetworkUri": None,
            "networkType": "FibreChannel",
            "networkUris": [
                "FC1"
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
            "name": "FC2",
            "nativeNetworkUri": None,
            "networkType": "FibreChannel",
            "networkUris": [
                "FC2"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "Tagged",
            "lacpTimer": "Short",
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "bay": "1",
                    "enclosure": "1",
                    "port": "X5"
                }
            ],
            "mode": "Auto",
            "name": "Eth1",
            "nativeNetworkUri": None,
            "networkType": "Ethernet",
            "networkUris": [
                "Eth1_1059",
                "Eth1_1051",
                "Eth1_1057",
                "Eth1_1052",
                "Eth1_1060",
                "Eth1_1056",
                "Eth1_1053",
                "Eth1_1058",
                "Eth1_1054",
                "Eth1_1061",
                "Eth1_1055"
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
        "name": "LIG_A",
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
                "type": "HP VC FlexFabric-20/40 F8 Module"
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
        "uplinkSets": [{
            "ethernetNetworkType": "Tagged",
            "lacpTimer": "Short",
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "bay": "1",
                    "enclosure": "1",
                    "port": "X5"
                }
            ],
            "mode": "Auto",
            "name": "eth1",
            "nativeNetworkUri": None,
            "networkType": "Ethernet",
            "networkUris": [
                "eth_1012",
                "eth_1011"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "NotApplicable",
            "lacpTimer": None,
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "port": "X4",
                    "enclosure": "1",
                    "bay": "1"
                }
            ],
            "mode": "Auto",
            "name": "das1",
            "nativeNetworkUri": None,
            "networkType": "FibreChannel",
            "networkUris": [
                "DASnet_1"
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
            "name": "fcoe2",
            "nativeNetworkUri": None,
            "networkType": "Ethernet",
            "networkUris": [
                "FCOE_net2"
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
            "name": "fcoe1",
            "nativeNetworkUri": None,
            "networkType": "Ethernet",
            "networkUris": [
                "FCOE_net1"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "Tagged",
            "lacpTimer": "Short",
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "bay": "2",
                    "enclosure": "1",
                    "port": "X5"
                }
            ],
            "mode": "Auto",
            "name": "eth2",
            "nativeNetworkUri": None,
            "networkType": "Ethernet",
            "networkUris": [
                "eth_1014",
                "eth_1013"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "NotApplicable",
            "lacpTimer": None,
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "port": "X4",
                    "enclosure": "1",
                    "bay": "2"
                }
            ],
            "mode": "Auto",
            "name": "das2",
            "nativeNetworkUri": None,
            "networkType": "FibreChannel",
            "networkUris": [
                "DASnet_2"
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
        "name": "LIG_B",
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
                "FC_net1"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "NotApplicable",
            "lacpTimer": None,
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "bay": "4",
                    "enclosure": "1",
                    "port": "3"
                }
            ],
            "mode": "Auto",
            "name": "fc2",
            "nativeNetworkUri": None,
            "networkType": "FibreChannel",
            "networkUris": [
                "FC_net2"
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
        "uri": "LIG:LIG_C",
        "status": None,
        "stackingHealth": None,
        "category": "logical-interconnect-groups",
        "state": "Active",
        "internalNetworkUris": "[]",
        "stackingMode": None,
        "description": None,
        "name": "LIG_C",
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
        "uri": "LIG:51.11-Lig Bay 3 & 4",
        "status": None,
        "stackingHealth": None,
        "category": "logical-interconnect-groups",
        "state": "Active",
        "internalNetworkUris": "[]",
        "stackingMode": None,
        "description": None,
        "name": "51.11-Lig Bay 3 & 4",
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
        "uri": "LIG:61.11 Bay 5 & 6",
        "status": None,
        "stackingHealth": None,
        "category": "logical-interconnect-groups",
        "state": "Active",
        "internalNetworkUris": "[]",
        "stackingMode": None,
        "description": None,
        "name": "61.11 Bay 5 & 6",
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
        "uri": "LIG:56.11 LIG Bay 2 & 3",
        "status": None,
        "stackingHealth": None,
        "category": "logical-interconnect-groups",
        "state": "Active",
        "internalNetworkUris": "[]",
        "stackingMode": None,
        "description": None,
        "name": "56.11 LIG Bay 2 & 3",
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
        "uri": "LIG:61.11 Bay 3 & 4",
        "status": None,
        "stackingHealth": None,
        "category": "logical-interconnect-groups",
        "state": "Active",
        "internalNetworkUris": "[]",
        "stackingMode": None,
        "description": None,
        "name": "61.11 Bay 3 & 4",
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
        "uri": "LIG:56.11 LIG Bay 1 & 2",
        "status": None,
        "stackingHealth": None,
        "category": "logical-interconnect-groups",
        "state": "Active",
        "internalNetworkUris": "[]",
        "stackingMode": None,
        "description": None,
        "name": "56.11 LIG Bay 1 & 2",
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
        "uri": "LIG:61.11 Bay 1 & 2",
        "status": None,
        "stackingHealth": None,
        "category": "logical-interconnect-groups",
        "state": "Active",
        "internalNetworkUris": "[]",
        "stackingMode": None,
        "description": None,
        "name": "61.11 Bay 1 & 2",
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
        "uri": "LIG:51.11-LIG bay 1 & 2",
        "status": None,
        "stackingHealth": None,
        "category": "logical-interconnect-groups",
        "state": "Active",
        "internalNetworkUris": "[]",
        "stackingMode": None,
        "description": None,
        "name": "51.11-LIG bay 1 & 2",
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
        "uri": "LIG:LIG_A",
        "status": None,
        "stackingHealth": None,
        "category": "logical-interconnect-groups",
        "state": "Active",
        "internalNetworkUris": "[]",
        "stackingMode": None,
        "description": None,
        "name": "LIG_A",
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
        "uri": "LIG:LIG_B",
        "status": None,
        "stackingHealth": None,
        "category": "logical-interconnect-groups",
        "state": "Active",
        "internalNetworkUris": "[]",
        "stackingMode": None,
        "description": None,
        "name": "LIG_B",
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
        "name": "Enclosure_61.11",
        "interconnectBayMappings": [
            {
                "interconnectBay": 1,
                "logicalInterconnectGroupUri": "LIG:LIG_A",

            },
            {
                "interconnectBay": 2,
                "logicalInterconnectGroupUri": "LIG:LIG_A",

            },
            {
                "interconnectBay": 3,
                "logicalInterconnectGroupUri": "LIG:LIG_B",

            },
            {
                "interconnectBay": 4,
                "logicalInterconnectGroupUri": "LIG:LIG_B",

            },
            {
                "interconnectBay": 5,
                "logicalInterconnectGroupUri": "LIG:LIG_C",

            },
            {
                "interconnectBay": 6,
                "logicalInterconnectGroupUri": "LIG:LIG_C",

            }
        ],
        "ipAddressingMode": "External",
        "enclosureCount": 1
    },
    {
        "name": "Encl Grp 61.11",
        "interconnectBayMappings": [
            {
                "interconnectBay": 1,
                "logicalInterconnectGroupUri": "LIG:61.11 Bay 1 & 2",

            },
            {
                "interconnectBay": 2,
                "logicalInterconnectGroupUri": "LIG:61.11 Bay 1 & 2",

            },
            {
                "interconnectBay": 3,
                "logicalInterconnectGroupUri": "LIG:61.11 Bay 3 & 4",

            },
            {
                "interconnectBay": 4,
                "logicalInterconnectGroupUri": "LIG:61.11 Bay 3 & 4",

            },
            {
                "interconnectBay": 5,
                "logicalInterconnectGroupUri": "LIG:61.11 Bay 5 & 6",

            },
            {
                "interconnectBay": 6,
                "logicalInterconnectGroupUri": "LIG:61.11 Bay 5 & 6",

            }
        ],
        "ipAddressingMode": "External",
        "enclosureCount": 1
    },
    {
        "name": "Encl Grp 56.11",
        "interconnectBayMappings": [
            {
                "interconnectBay": 1,
                "logicalInterconnectGroupUri": "LIG:56.11 LIG Bay 1 & 2",

            },
            {
                "interconnectBay": 2,
                "logicalInterconnectGroupUri": "LIG:56.11 LIG Bay 1 & 2",

            },
            {
                "interconnectBay": 3,
                "logicalInterconnectGroupUri": "LIG:56.11 LIG Bay 2 & 3",

            },
            {
                "interconnectBay": 4,
                "logicalInterconnectGroupUri": "LIG:56.11 LIG Bay 2 & 3",

            }
        ],
        "ipAddressingMode": "External",
        "enclosureCount": 1
    },
    {
        "name": "Encl Grp 51.11",
        "interconnectBayMappings": [
            {
                "interconnectBay": 1,
                "logicalInterconnectGroupUri": "LIG:51.11-LIG bay 1 & 2",

            },
            {
                "interconnectBay": 2,
                "logicalInterconnectGroupUri": "LIG:51.11-LIG bay 1 & 2",

            },
            {
                "interconnectBay": 3,
                "logicalInterconnectGroupUri": "LIG:51.11-Lig Bay 3 & 4",

            },
            {
                "interconnectBay": 4,
                "logicalInterconnectGroupUri": "LIG:51.11-Lig Bay 3 & 4",

            }
        ],
        "ipAddressingMode": "External",
        "enclosureCount": 1
    }
]
expected_encgroups_add = [
    {
        "uri": "EG:Enclosure_61.11",
        "description": None,
        "category": "enclosure-groups",
        "state": "Normal",
        "status": "OK",
        "powerMode": None,
        "portMappingCount": 8,
        "portMappings": [{u'midplanePort': 1, u'interconnectBay': 1}, {u'midplanePort': 2, u'interconnectBay': 2}, {u'midplanePort': 3, u'interconnectBay': 3}, {u'midplanePort': 4, u'interconnectBay': 4}, {u'midplanePort': 5, u'interconnectBay': 5}, {u'midplanePort': 6, u'interconnectBay': 6}, {u'midplanePort': 7, u'interconnectBay': 7}, {u'midplanePort': 8, u'interconnectBay': 8}],
        "ipRangeUris": [],
        "associatedLogicalInterconnectGroups": [u'LIG:LIG_C', u'LIG:LIG_A', u'LIG:LIG_B'],
        "name": "Enclosure_61.11",
        "type": "EnclosureGroupV7",
        "enclosureTypeUri": "/rest/enclosure-types/c7000",
        "stackingMode": "Enclosure",
        "name": "Enclosure_61.11",
        "interconnectBayMappingCount": "6",
        "interconnectBayMappings": [
            {
                "interconnectBay": 1,
                "logicalInterconnectGroupUri": "LIG:LIG_A",

            },
            {
                "interconnectBay": 2,
                "logicalInterconnectGroupUri": "LIG:LIG_A",

            },
            {
                "interconnectBay": 3,
                "logicalInterconnectGroupUri": "LIG:LIG_B",

            },
            {
                "interconnectBay": 4,
                "logicalInterconnectGroupUri": "LIG:LIG_B",

            },
            {
                "interconnectBay": 5,
                "logicalInterconnectGroupUri": "LIG:LIG_C",

            },
            {
                "interconnectBay": 6,
                "logicalInterconnectGroupUri": "LIG:LIG_C",

            }
        ],
        "ipAddressingMode": "External",
        "enclosureCount": 1
    },
    {
        "uri": "EG:Encl Grp 61.11",
        "description": None,
        "category": "enclosure-groups",
        "state": "Normal",
        "status": "OK",
        "powerMode": None,
        "portMappingCount": 8,
        "portMappings": [{u'midplanePort': 1, u'interconnectBay': 1}, {u'midplanePort': 2, u'interconnectBay': 2}, {u'midplanePort': 3, u'interconnectBay': 3}, {u'midplanePort': 4, u'interconnectBay': 4}, {u'midplanePort': 5, u'interconnectBay': 5}, {u'midplanePort': 6, u'interconnectBay': 6}, {u'midplanePort': 7, u'interconnectBay': 7}, {u'midplanePort': 8, u'interconnectBay': 8}],
        "ipRangeUris": [],
        "associatedLogicalInterconnectGroups": [u'LIG:61.11 Bay 5 & 6', u'LIG:61.11 Bay 3 & 4', u'LIG:61.11 Bay 1 & 2'],
        "name": "Encl Grp 61.11",
        "type": "EnclosureGroupV7",
        "enclosureTypeUri": "/rest/enclosure-types/c7000",
        "stackingMode": "Enclosure",
        "name": "Encl Grp 61.11",
        "interconnectBayMappingCount": "6",
        "interconnectBayMappings": [
            {
                "interconnectBay": 1,
                "logicalInterconnectGroupUri": "LIG:61.11 Bay 1 & 2",

            },
            {
                "interconnectBay": 2,
                "logicalInterconnectGroupUri": "LIG:61.11 Bay 1 & 2",

            },
            {
                "interconnectBay": 3,
                "logicalInterconnectGroupUri": "LIG:61.11 Bay 3 & 4",

            },
            {
                "interconnectBay": 4,
                "logicalInterconnectGroupUri": "LIG:61.11 Bay 3 & 4",

            },
            {
                "interconnectBay": 5,
                "logicalInterconnectGroupUri": "LIG:61.11 Bay 5 & 6",

            },
            {
                "interconnectBay": 6,
                "logicalInterconnectGroupUri": "LIG:61.11 Bay 5 & 6",

            }
        ],
        "ipAddressingMode": "External",
        "enclosureCount": 1
    },
    {
        "uri": "EG:Encl Grp 56.11",
        "description": None,
        "category": "enclosure-groups",
        "state": "Normal",
        "status": "OK",
        "powerMode": None,
        "portMappingCount": 8,
        "portMappings": [{u'midplanePort': 1, u'interconnectBay': 1}, {u'midplanePort': 2, u'interconnectBay': 2}, {u'midplanePort': 3, u'interconnectBay': 3}, {u'midplanePort': 4, u'interconnectBay': 4}, {u'midplanePort': 5, u'interconnectBay': 5}, {u'midplanePort': 6, u'interconnectBay': 6}, {u'midplanePort': 7, u'interconnectBay': 7}, {u'midplanePort': 8, u'interconnectBay': 8}],
        "ipRangeUris": [],
        "associatedLogicalInterconnectGroups": [u'LIG:56.11 LIG Bay 2 & 3', u'LIG:56.11 LIG Bay 1 & 2'],
        "name": "Encl Grp 56.11",
        "type": "EnclosureGroupV7",
        "enclosureTypeUri": "/rest/enclosure-types/c7000",
        "stackingMode": "Enclosure",
        "name": "Encl Grp 56.11",
        "interconnectBayMappingCount": "4",
        "interconnectBayMappings": [
            {
                "interconnectBay": 1,
                "logicalInterconnectGroupUri": "LIG:56.11 LIG Bay 1 & 2",

            },
            {
                "interconnectBay": 2,
                "logicalInterconnectGroupUri": "LIG:56.11 LIG Bay 1 & 2",

            },
            {
                "interconnectBay": 3,
                "logicalInterconnectGroupUri": "LIG:56.11 LIG Bay 2 & 3",

            },
            {
                "interconnectBay": 4,
                "logicalInterconnectGroupUri": "LIG:56.11 LIG Bay 2 & 3",

            }
        ],
        "ipAddressingMode": "External",
        "enclosureCount": 1
    },
    {
        "uri": "EG:Encl Grp 51.11",
        "description": None,
        "category": "enclosure-groups",
        "state": "Normal",
        "status": "OK",
        "powerMode": None,
        "portMappingCount": 8,
        "portMappings": [{u'midplanePort': 1, u'interconnectBay': 1}, {u'midplanePort': 2, u'interconnectBay': 2}, {u'midplanePort': 3, u'interconnectBay': 3}, {u'midplanePort': 4, u'interconnectBay': 4}, {u'midplanePort': 5, u'interconnectBay': 5}, {u'midplanePort': 6, u'interconnectBay': 6}, {u'midplanePort': 7, u'interconnectBay': 7}, {u'midplanePort': 8, u'interconnectBay': 8}],
        "ipRangeUris": [],
        "associatedLogicalInterconnectGroups": [u'LIG:51.11-Lig Bay 3 & 4', u'LIG:51.11-LIG bay 1 & 2'],
        "name": "Encl Grp 51.11",
        "type": "EnclosureGroupV7",
        "enclosureTypeUri": "/rest/enclosure-types/c7000",
        "stackingMode": "Enclosure",
        "name": "Encl Grp 51.11",
        "interconnectBayMappingCount": "4",
        "interconnectBayMappings": [
            {
                "interconnectBay": 1,
                "logicalInterconnectGroupUri": "LIG:51.11-LIG bay 1 & 2",

            },
            {
                "interconnectBay": 2,
                "logicalInterconnectGroupUri": "LIG:51.11-LIG bay 1 & 2",

            },
            {
                "interconnectBay": 3,
                "logicalInterconnectGroupUri": "LIG:51.11-Lig Bay 3 & 4",

            },
            {
                "interconnectBay": 4,
                "logicalInterconnectGroupUri": "LIG:51.11-Lig Bay 3 & 4",

            }
        ],
        "ipAddressingMode": "External",
        "enclosureCount": 1
    }
]

logical_enclosure = [
    {
        "name": "ENCL_21",
        "enclosureUris": [
            "ENC:ENCL_21"
        ],
        "enclosureGroupUri": "EG:Encl Grp 56.11"
    },
    {
        "name": "SGH747C0LP",
        "enclosureUris": [
            "ENC:SGH747C0LP"
        ],
        "enclosureGroupUri": "EG:Encl Grp 51.11"
    },
    {
        "name": "SGH221M0DZ",
        "enclosureUris": [
            "ENC:SGH221M0DZ"
        ],
        "enclosureGroupUri": "EG:Enclosure_61.11"
    }
]
expected_logical_enclosure = [
    {
        "type": "LogicalEnclosureV4",
        "uri": "ENCL_21",
        "status": "OK",
        "name": "ENCL_21",
        "enclosureUris": [
            "ENC:ENCL_21"
        ],
        "enclosureGroupUri": "EG:Encl Grp 56.11"
    },
    {
        "type": "LogicalEnclosureV4",
        "uri": "SGH747C0LP",
        "status": "OK",
        "name": "SGH747C0LP",
        "enclosureUris": [
            "ENC:SGH747C0LP"
        ],
        "enclosureGroupUri": "EG:Encl Grp 51.11"
    },
    {
        "type": "LogicalEnclosureV4",
        "uri": "SGH221M0DZ",
        "status": "OK",
        "name": "SGH221M0DZ",
        "enclosureUris": [
            "ENC:SGH221M0DZ"
        ],
        "enclosureGroupUri": "EG:Enclosure_61.11"
    }
]

enclosures = [
    {
        "username": "Admin",
        "name": "SGH747C0LP",
        "password": "Insight7",
        "force": True,
        "hostname": "172.25.51.11",
        "enclosureGroupUri": "EG:Encl Grp 51.11",
        "forceInstallFirmware": True,
        "licensingIntent": "OneViewNoiLO",
    },
    {
        "username": "Admin",
        "name": "SGH221M0DZ",
        "password": "Insight7",
        "force": True,
        "hostname": "172.25.61.11",
        "enclosureGroupUri": "EG:Enclosure_61.11",
        "forceInstallFirmware": True,
        "licensingIntent": "OneView",
    },
    {
        "username": "Admin",
        "name": "ENCL_21",
        "password": "Insight7",
        "force": True,
        "hostname": "172.25.56.11",
        "enclosureGroupUri": "EG:Encl Grp 56.11",
        "forceInstallFirmware": True,
        "licensingIntent": "OneViewNoiLO",
    }
]
expected_enclosures = [
    {
        "name": "SGH747C0LP",
        "enclosureGroupUri": "EG:Encl Grp 51.11",
        "licensingIntent": "OneViewNoiLO",
        'logicalEnclosureUri': 'LE:SGH747C0LP',
        'status': 'OK',
        'state': 'Configured'
    },
    {
        "name": "SGH221M0DZ",
        "enclosureGroupUri": "EG:Enclosure_61.11",
        "licensingIntent": "OneView",
        'logicalEnclosureUri': 'LE:SGH221M0DZ',
        'status': 'OK',
        'state': 'Configured'
    },
    {
        "name": "ENCL_21",
        "enclosureGroupUri": "EG:Encl Grp 56.11",
        "forceInstallFirmware": True,
        "licensingIntent": "OneViewNoiLO",
        'logicalEnclosureUri': 'LE:ENCL_21',
        'status': 'OK',
        'state': 'Configured'
    }
]

servers = [
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "OneViewNoiLO",
        "memoryMb": 16384,
        "model": "ProLiant BL460c Gen9",
        "mpFirmwareVersion": "2.60 May 23 2018",
        "mpModel": "iLO4",
        "name": "SGH747C0LP, bay 1",
        "partNumber": "727027-B21",
        "position": 1,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 6,
        "processorCount": 1,
        "processorSpeedMhz": 2400,
        "processorType": "Intel(R) Xeon(R) CPU E5-2620 v3 @ 2.40GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I36 v2.60 (05/21/2018)",
        "serialNumber": "2M2638049F",
        "shortModel": "BL460c Gen9",
        "state": "ProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-8"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "OneViewNoiLO",
        "memoryMb": 16384,
        "model": "ProLiant BL460c Gen9",
        "mpFirmwareVersion": "2.60 May 23 2018",
        "mpModel": "iLO4",
        "name": "SGH747C0LP, bay 2",
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
        "serialNumber": "2M260804TQ",
        "shortModel": "BL460c Gen9",
        "state": "ProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-8"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "OneViewNoiLO",
        "memoryMb": 32768,
        "model": "ProLiant BL460c Gen8",
        "mpFirmwareVersion": "2.60 May 23 2018",
        "mpModel": "iLO4",
        "name": "SGH747C0LP, bay 9",
        "partNumber": "670658-S01",
        "position": 9,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 6,
        "processorCount": 2,
        "processorSpeedMhz": 2000,
        "processorType": "Intel(R) Xeon(R) CPU E5-2620 0 @ 2.00GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I31 06/01/2015",
        "serialNumber": "MXQ2310LP7",
        "shortModel": "BL460c Gen8",
        "state": "Unmanaged",
        "stateReason": "Unconfigured",
        "status": "OK",
        "type": "server-hardware-8"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "OneViewNoiLO",
        "memoryMb": 57344,
        "model": "ProLiant BL460c Gen8",
        "mpFirmwareVersion": "2.60 May 23 2018",
        "mpModel": "iLO4",
        "name": "SGH747C0LP, bay 11",
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
        "serialNumber": "MXQ23102WJ",
        "shortModel": "BL460c Gen8",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-8"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "OneViewNoiLO",
        "memoryMb": 16384,
        "model": "ProLiant BL460c Gen8",
        "mpFirmwareVersion": "2.50 Sep 23 2016",
        "mpModel": "iLO4",
        "name": "SGH747C0LP, bay 10",
        "partNumber": "670658-S01",
        "position": 10,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 6,
        "processorCount": 2,
        "processorSpeedMhz": 2000,
        "processorType": "Intel(R) Xeon(R) CPU E5-2620 0 @ 2.00GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I31 06/01/2015",
        "serialNumber": "MXQ2310LPD",
        "shortModel": "BL460c Gen8",
        "state": "Unmanaged",
        "stateReason": "Unconfigured",
        "status": "OK",
        "type": "server-hardware-8"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "OneViewNoiLO",
        "memoryMb": 65536,
        "model": "ProLiant BL460c Gen8",
        "mpFirmwareVersion": "2.55 Aug 16 2017",
        "mpModel": "iLO4",
        "name": "ENCL_21, bay 4",
        "partNumber": "666157-B21",
        "position": 4,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 8,
        "processorCount": 2,
        "processorSpeedMhz": 2600,
        "processorType": "Intel(R) Xeon(R) CPU E5-2670 0 @ 2.60GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I31 06/01/2015",
        "serialNumber": "MXQ21602WB",
        "shortModel": "BL460c Gen8",
        "state": "Unmanaged",
        "stateReason": "Unconfigured",
        "status": "OK",
        "type": "server-hardware-8"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "OneViewNoiLO",
        "memoryMb": 16384,
        "model": "ProLiant BL460c Gen9",
        "mpFirmwareVersion": "2.60 May 23 2018",
        "mpModel": "iLO4",
        "name": "ENCL_21, bay 16",
        "partNumber": "727027-B21",
        "position": 16,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 6,
        "processorCount": 1,
        "processorSpeedMhz": 2400,
        "processorType": "Intel(R) Xeon(R) CPU E5-2620 v3 @ 2.40GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I36 v2.60 (05/21/2018)",
        "serialNumber": "2M2638049H",
        "shortModel": "BL460c Gen9",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-8"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "OneViewNoiLO",
        "memoryMb": 32768,
        "model": "ProLiant BL460c Gen8",
        "mpFirmwareVersion": "2.60 May 23 2018",
        "mpModel": "iLO4",
        "name": "ENCL_21, bay 8",
        "partNumber": "670658-S01",
        "position": 8,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 6,
        "processorCount": 2,
        "processorSpeedMhz": 2000,
        "processorType": "Intel(R) Xeon(R) CPU E5-2620 0 @ 2.00GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I31 06/01/2015",
        "serialNumber": "MXQ2260JHJ",
        "shortModel": "BL460c Gen8",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-8"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "OneViewNoiLO",
        "memoryMb": 65536,
        "model": "ProLiant BL460c Gen8",
        "mpFirmwareVersion": "2.60 May 23 2018",
        "mpModel": "iLO4",
        "name": "ENCL_21, bay 5",
        "partNumber": "741446-S01",
        "position": 5,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 8,
        "processorCount": 2,
        "processorSpeedMhz": 2600,
        "processorType": "Intel(R) Xeon(R) CPU E5-2650 v2 @ 2.60GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I31 06/01/2015",
        "serialNumber": "MXQ43600SZ",
        "shortModel": "BL460c Gen8",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-8"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "OneViewNoiLO",
        "memoryMb": 32768,
        "model": "ProLiant BL460c Gen8",
        "mpFirmwareVersion": "2.60 May 23 2018",
        "mpModel": "iLO4",
        "name": "ENCL_21, bay 9",
        "partNumber": "670656-S01",
        "position": 9,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 8,
        "processorCount": 2,
        "processorSpeedMhz": 2000,
        "processorType": "Intel(R) Xeon(R) CPU E5-2650 0 @ 2.00GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I31 06/01/2015",
        "serialNumber": "2D2233022A",
        "shortModel": "BL460c Gen8",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-8"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "OneViewNoiLO",
        "memoryMb": 16384,
        "model": "ProLiant BL460c Gen8",
        "mpFirmwareVersion": "2.60 May 23 2018",
        "mpModel": "iLO4",
        "name": "ENCL_21, bay 12",
        "partNumber": "cosmos123",
        "position": 12,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 6,
        "processorCount": 2,
        "processorSpeedMhz": 2000,
        "processorType": "Intel(R) Xeon(R) CPU E5-2620 0 @ 2.00GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I31 06/01/2015",
        "serialNumber": "123cosmos",
        "shortModel": "BL460c Gen8",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-8"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "OneViewNoiLO",
        "memoryMb": 16384,
        "model": "ProLiant BL465c Gen8",
        "mpFirmwareVersion": "2.60 May 23 2018",
        "mpModel": "iLO4",
        "name": "ENCL_21, bay 7",
        "partNumber": "634969-B21",
        "position": 7,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 16,
        "processorCount": 1,
        "processorSpeedMhz": 2300,
        "processorType": "AMD Opteron(TM) Processor 6276",
        "refreshState": "NotRefreshing",
        "romVersion": "A26 03/07/2016",
        "serialNumber": "MXQ2310M1F",
        "shortModel": "BL465c Gen8",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-8"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "OneViewNoiLO",
        "memoryMb": 16384,
        "model": "ProLiant BL465c Gen8",
        "mpFirmwareVersion": "2.60 May 23 2018",
        "mpModel": "iLO4",
        "name": "ENCL_21, bay 6",
        "partNumber": "634969-B21",
        "position": 6,
        "powerLock": False,
        "powerState": "Unknown",
        "processorCoreCount": 16,
        "processorCount": 1,
        "processorSpeedMhz": 2300,
        "processorType": "AMD Opteron(TM) Processor 6276",
        "refreshState": "NotRefreshing",
        "romVersion": "A26 03/07/2016",
        "serialNumber": "MXQ2220CGZ",
        "shortModel": "BL465c Gen8",
        "state": "Unmanaged",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-8"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "OneViewNoiLO",
        "memoryMb": 24576,
        "model": "ProLiant BL420c Gen8",
        "mpFirmwareVersion": "2.55 Aug 16 2017",
        "mpModel": "iLO4",
        "name": "ENCL_21, bay 1",
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
        "serialNumber": "2M2233011Z",
        "shortModel": "BL420c Gen8",
        "state": "Unmanaged",
        "stateReason": "Unconfigured",
        "status": "OK",
        "type": "server-hardware-8"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "OneViewNoiLO",
        "memoryMb": 16384,
        "model": "ProLiant BL460c Gen9",
        "mpFirmwareVersion": "2.60 May 23 2018",
        "mpModel": "iLO4",
        "name": "ENCL_21, bay 13",
        "partNumber": "727027-B21",
        "position": 13,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 6,
        "processorCount": 1,
        "processorSpeedMhz": 2400,
        "processorType": "Intel(R) Xeon(R) CPU E5-2620 v3 @ 2.40GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I36 v2.60 (05/21/2018)",
        "serialNumber": "2M2550035L",
        "shortModel": "BL460c Gen9",
        "state": "ProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-8"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "OneView",
        "memoryMb": 32768,
        "model": "ProLiant BL460c Gen10",
        "mpFirmwareVersion": "1.30 May 31 2018",
        "mpModel": "iLO5",
        "name": "SGH221M0DZ, bay 1",
        "partNumber": "863445-B21",
        "position": 1,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 8,
        "processorCount": 2,
        "processorSpeedMhz": 1800,
        "processorType": "Intel(R) Xeon(R) Silver 4108 CPU @ 1.80GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I41 v1.40 (06/15/2018)",
        "serialNumber": "2M274505BD",
        "shortModel": "BL460c Gen10",
        "state": "ProfileError",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-8"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "OneView",
        "memoryMb": 32768,
        "model": "ProLiant BL460c Gen10",
        "mpFirmwareVersion": "1.30 May 31 2018",
        "mpModel": "iLO5",
        "name": "SGH221M0DZ, bay 11",
        "partNumber": "863445-B21",
        "position": 11,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 8,
        "processorCount": 2,
        "processorSpeedMhz": 1800,
        "processorType": "Intel(R) Xeon(R) Silver 4108 CPU @ 1.80GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I41 v1.40 (06/15/2018)",
        "serialNumber": "2M274505BG",
        "shortModel": "BL460c Gen10",
        "state": "ProfileError",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-8"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "OneViewNoiLO",
        "memoryMb": 262144,
        "model": "ProLiant BL460c Gen9",
        "mpFirmwareVersion": "2.60 May 23 2018",
        "mpModel": "iLO4",
        "name": "SGH221M0DZ, bay 2",
        "partNumber": "727021-B21",
        "position": 2,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 8,
        "processorCount": 2,
        "processorSpeedMhz": 2600,
        "processorType": "Intel(R) Xeon(R) CPU E5-2640 v3 @ 2.60GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I36 v2.60 (05/21/2018)",
        "serialNumber": "USE449FREJ",
        "shortModel": "BL460c Gen9",
        "state": "ProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-8"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "OneView",
        "memoryMb": 245760,
        "model": "ProLiant BL460c Gen9",
        "mpFirmwareVersion": "2.60 May 23 2018",
        "mpModel": "iLO4",
        "name": "SGH221M0DZ, bay 3",
        "partNumber": "727021-B21",
        "position": 3,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 8,
        "processorCount": 2,
        "processorSpeedMhz": 2600,
        "processorType": "Intel(R) Xeon(R) CPU E5-2640 v3 @ 2.60GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I36 v2.60 (05/21/2018)",
        "serialNumber": "USE449FRES",
        "shortModel": "BL460c Gen9",
        "state": "ProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-8"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "OneViewNoiLO",
        "memoryMb": 32768,
        "model": "ProLiant BL460c Gen8",
        "mpFirmwareVersion": "2.55 Aug 16 2017",
        "mpModel": "iLO4",
        "name": "SGH221M0DZ, bay 9",
        "partNumber": "670658-S01",
        "position": 9,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 6,
        "processorCount": 2,
        "processorSpeedMhz": 2000,
        "processorType": "Intel(R) Xeon(R) CPU E5-2620 0 @ 2.00GHz",
        "refreshState": "RefreshFailed",
        "romVersion": "I31 06/01/2015",
        "serialNumber": "MXQ2280F0B",
        "shortModel": "BL460c Gen8",
        "state": "ProfileError",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-8"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "OneViewNoiLO",
        "memoryMb": 32768,
        "model": "ProLiant BL460c Gen8",
        "mpFirmwareVersion": "2.55 Aug 16 2017",
        "mpModel": "iLO4",
        "name": "SGH221M0DZ, bay 10",
        "partNumber": "670658-S01",
        "position": 10,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 6,
        "processorCount": 2,
        "processorSpeedMhz": 2000,
        "processorType": "Intel(R) Xeon(R) CPU E5-2620 0 @ 2.00GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I31 06/01/2015",
        "serialNumber": "MXQ23102W8",
        "shortModel": "BL460c Gen8",
        "state": "Unmanaged",
        "stateReason": "Unconfigured",
        "status": "OK",
        "type": "server-hardware-8"
    }
]

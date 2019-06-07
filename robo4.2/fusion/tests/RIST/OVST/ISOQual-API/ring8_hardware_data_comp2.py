"""
Goose Hardware Ring 8
"""
# !/usr/bin/env python

admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
timeandlocale = {'type': 'TimeAndLocale', 'dateTime': None, 'timezone': 'UTC', 'ntpServers': ['ntp.hpecorp.net'], 'locale': 'en_US.UTF-8'}

licenses = [
    {'key': 'ABAG AQEA H9PQ 8HV2 V7B5 HWWB Y9JL KMPL B89H MZVU DXAU 2CSM GHTG L762 DMF5 GRRM KJVT D5KM EFVW TSNJ XFU9 4ZSK E828 LFK6 FKA6 DU5N TZZX 9B5X 82Z5 WHEF D9ED 3RUX BJS2 XFXC T84U R42A 58S5 XA2D WXAP GMTQ 4YLB MM2S CZU7 2E4X E8UW BGB5 C324 SFUZ CMSB VNTJ ESB7 KVGR UNPC H4N5 NGHL 97D4 "EG3188881 KEY-E5Y35A#FUSION HP_OV_3yr_24x7_Supp_Phys_Flex_Lic ED4UATGCG2A9"_3JMZZ-RB9CN-DQD7H-CPB8P-M7WW2'},
    {'key': 'AA9C AQAA H9PY CHVY V7B5 HWWB Y9JL KMPL 3JKH 5FVM DXAU 2CSM GHTG L762 MTK7 FYB9 KJVT D5KM EFVW DT5J 4BEM M2SC SPS9 YG66 Z99R MWSN 6Z84 46XT WZJL HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTFG LS8T XU4E "EVAL-HPOV-NFR1 HPOV-NFR1 HP_OneView_16_Seat_NFR 7T36AEJG7JJ9"_3MBSY-CJZXJ-RDCJQ-55T3M-BP3H2'},
    {'key': 'QCLG C9MA H9PQ 8HUZ U7B5 HWW5 Y9JL KMPL KRWA NBZY DXAU 2CSM GHTG L762 DNV7 GQFQ KJVT D5KM EFVW DT5J LFM8 76S8 C8SN YGSG Y8JC QUXV XZKH ABB4 NV2C LHXU VLXL HFMP J8TG 2VEB LK4U R6UF S7QS TRRL GX96 CMH4 6MPA M8LC KZU7 WE4X YN9X CDNB NT35 GH9J JGTJ QCV6 3EJF N975 "OV_NFR2 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR EY67ATGDTH6C"'},
    {'key': 'YAYC CQAA H9PQ GHX2 U7B5 HWW5 Y9JL KMPL FJ2H PFFM DXAU 2CSM GHTG L762 WTC5 GYBQ KJVT D5KM EFVW DT5J EBUM 62CC SPS9 YG66 Z99R MWSN 6Z84 46XT WZJT HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTVG LS8T XU4E "EVAL-HPOV-NFR2 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR 9G6UAEJGUA4U"'},
    {'key': 'QB9A DQEA H9PY 8HXY V2B4 HWWV Y9JL KMPL B89H MZVU DXAU 2CSM GHTG L762 6S74 ERB4 KJVT D5KM EFVW TSNJ YF4J 86CS SMT9 YGS6 SMQQ MUCF UW2L MYN7 N2QC DHKQ XJUL LUQH TU8F 3DQC SW7N VEQW V886 FE23 YWAT J8U3 2YT5 RNNV MHS3 QKTQ 688U F8A7 F8SE Z2DX RJQ6 MHPE SN9R 3UNK TVPT 74UF NGGT EHM4 "EVAL-N3R43A_ILR N3R43A_ILR Synergy_8Gb_FC_Upgrade_License EVAL-N3R43A_ILR"'},
    {'key': 'YBYE CQEA H9PA CHXZ V2B4 HWWV Y9JL KMPL LJ2A PGVQ DXAU 2CSM GHTG L762 2ET7 FQV9 KJVT D5KM EFVW TSNJ K4UP 536G SMT9 YGS6 SMQQ MUCF 4WCN MYN7 N2QS LHJQ XJUL LUQH TU8F 3DQC SW7N VEQW V886 FE23 YWAT J8U3 2YT5 RNNV MHS3 QKTQ 688U F8A7 F8SE Z2DX RJQ6 MHPE SN9R 3UNK TX83 T45F NGG3 EHM4 "EVAL-N3R43A_NFR N3R43A_NFR Synergy_8Gb_FC_Upgrade_License_NFR EVAL-N3R43A_NFR"'}]

appliance = {
    'type': "ApplianceNetworkConfigurationV2",
    'applianceNetworks':
    [{
        "device": "bond0",
        "macAddress": "14:02:ec:45:ed:08",
        "interfaceName": "Appliance",
        "activeNode": 1,
        "unconfigure": False,
        "ipv4Type": "STATIC",
        "ipv4Subnet": "255.255.240.0",
        "ipv4Gateway": "16.114.208.1",
        "ipv4NameServers": [u'16.125.25.81', u'16.125.25.82'],
        "app1Ipv4Addr": "16.114.208.99",
        "ipv6Type": "UNCONFIGURE",
        "hostname": "ovst02-ov.vse.rdlabs.hpecorp.net",
        "confOneNode": True,
        "domainName": "",
        "aliasDisabled": False
    }
    ]}

users = [{'userName': 'appliance', 'password': 'wpsthpvse1', "permissions": [{"roleName": "Infrastructure administrator"}], 'emailAddress': 'appliance@hp.com', 'officePhone': '970-898-2222', 'mobilePhone': '970-898-0022', 'type': 'UserAndPermissions'},
         {'userName': 'network', 'password': 'wpsthpvse1', "permissions": [{"roleName": "Network administrator"}], 'emailAddress': 'network@hp.com', 'officePhone': '970-555-0001', 'mobilePhone': '970-500-0001', 'type': 'UserAndPermissions'},
         {'userName': 'readonly', 'password': 'wpsthpvse1', "permissions": [{"roleName": "Read only"}], 'emailAddress': 'readonly@hp.com', 'officePhone': '970-666-1919', 'mobilePhone': '970-600-1919', 'type': 'UserAndPermissions'},
         {'userName': 'server', 'password': 'wpsthpvse1', "permissions": [{"roleName": "Server administrator"}], 'emailAddress': 'server@hp.com', 'officePhone': '970-555-0001', 'mobilePhone': '970-500-0001', 'type': 'UserAndPermissions'},
         {'userName': 'storage', 'password': 'wpsthpvse1', "permissions": [{"roleName": "Storage administrator"}], 'emailAddress': 'storage@hp.com', 'officePhone': '970-555-0001', 'mobilePhone': '970-500-0001', 'type': 'UserAndPermissions'}]

expected_users = [{'type': 'UserAndPermissions', 'userName': 'appliance', 'fullName': '', 'emailAddress': 'appliance@hp.com', 'officePhone': '970-898-2222', 'mobilePhone': '970-898-0022', 'enabled': True, 'uri': '/rest/users/appliance', 'name': None, 'category': 'users'},
                  {'type': 'UserAndPermissions', 'userName': 'network', 'fullName': '', 'emailAddress': 'network@hp.com', 'officePhone': '970-555-0001', 'mobilePhone': '970-500-0001', 'enabled': True, 'uri': '/rest/users/network', 'name': None, 'category': 'users'},
                  {'type': 'UserAndPermissions', 'userName': 'readonly', 'fullName': '', 'emailAddress': 'readonly@hp.com', 'officePhone': '970-666-1919', 'mobilePhone': '970-600-1919', 'enabled': True, 'uri': '/rest/users/readonly', 'name': None, 'category': 'users'},
                  {'type': 'UserAndPermissions', 'userName': 'server', 'fullName': '', 'emailAddress': 'server@hp.com', 'officePhone': '970-555-0001', 'mobilePhone': '970-500-0001', 'enabled': True, 'uri': '/rest/users/server', 'name': None, 'category': 'users'},
                  {'type': 'UserAndPermissions', 'userName': 'storage', 'fullName': '', 'emailAddress': 'storage@hp.com', 'officePhone': '970-555-0001', 'mobilePhone': '970-500-0001', 'enabled': True, 'uri': '/rest/users/storage', 'name': None, 'category': 'users'}, ]

san_managers = [
    {
        "connectionInfo": [
            {
                "name": 'type',
                "value": 'Brocade Network Advisor',
            },
            {
                "name": "Host",
                "value": "16.125.75.15"
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
        "uri": "SAN:16.125.75.15",
        "name": "16.125.75.15",
        "type": "FCDeviceManagerV2",
        "category": "fc-device-managers",
        "state": "Managed",
        "description": "Brocade Network Advisor",
        "deviceManagerVersion": "14.2.0.146",
        "isInternal": "False",
        "providerDisplayName": "Brocade Network Advisor",
        "refreshState": "Stable",
        "status": "OK",
        "connectionInfo": [
            {
                "name": "Host",
                "value": "16.125.75.15"
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
        "name": "net16",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 16
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net300",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 300
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net11",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 11
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net25",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 25
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net12",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 12
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net20",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 20
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net22",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 22
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net24",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 24
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net17",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 17
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net15",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 15
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net21",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 21
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net18",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 18
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net19",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 19
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net13",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 13
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net10",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 10
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net23",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 23
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net14",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 14
    }
]
expected_ethernet_networks = [
    {
        "uri": "ETH:net16",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net16",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 16
    },
    {
        "uri": "ETH:net300",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net300",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 300
    },
    {
        "uri": "ETH:net11",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net11",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 11
    },
    {
        "uri": "ETH:net25",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net25",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 25
    },
    {
        "uri": "ETH:net12",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net12",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 12
    },
    {
        "uri": "ETH:net20",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net20",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 20
    },
    {
        "uri": "ETH:net22",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net22",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 22
    },
    {
        "uri": "ETH:net24",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net24",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 24
    },
    {
        "uri": "ETH:net17",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net17",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 17
    },
    {
        "uri": "ETH:net15",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net15",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 15
    },
    {
        "uri": "ETH:net21",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net21",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 21
    },
    {
        "uri": "ETH:net18",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net18",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 18
    },
    {
        "uri": "ETH:net19",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net19",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 19
    },
    {
        "uri": "ETH:net13",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net13",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 13
    },
    {
        "uri": "ETH:net10",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net10",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 10
    },
    {
        "uri": "ETH:net23",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net23",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 23
    },
    {
        "uri": "ETH:net14",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net14",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 14
    }
]

fc_networks = [
    {
        "type": "fc-networkV4",
        "name": "FC-A",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:ovstsan25-a"
    },
    {
        "type": "fc-networkV4",
        "name": "3par-b",
        "fabricType": "DirectAttach",
        "linkStabilityTime": 0,
        "autoLoginRedistribution": False,
        "managedSanUri": None
    },
    {
        "type": "fc-networkV4",
        "name": "FC-B",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:ovstsan25-b"
    },
    {
        "type": "fc-networkV4",
        "name": "3par-a",
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
        "uri": "FC:FC-A",
        "status": "OK",
        "type": "fc-networkV4",
        "name": "FC-A",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:ovstsan25-a"
    },
    {
        "category": "fc-networks",
        "state": "Active",
        "description": None,
        "uri": "FC:3par-b",
        "status": "OK",
        "type": "fc-networkV4",
        "name": "3par-b",
        "fabricType": "DirectAttach",
        "linkStabilityTime": 0,
        "autoLoginRedistribution": False,
        "managedSanUri": None
    },
    {
        "category": "fc-networks",
        "state": "Active",
        "description": None,
        "uri": "FC:FC-B",
        "status": "OK",
        "type": "fc-networkV4",
        "name": "FC-B",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:ovstsan25-b"
    },
    {
        "category": "fc-networks",
        "state": "Active",
        "description": None,
        "uri": "FC:3par-a",
        "status": "OK",
        "type": "fc-networkV4",
        "name": "3par-a",
        "fabricType": "DirectAttach",
        "linkStabilityTime": 0,
        "autoLoginRedistribution": False,
        "managedSanUri": None
    }
]

networksets = [{'name': 'netset1', 'nativeNetworkUri': 'net10', 'type': 'network-setV5', 'networkUris': ['net10', 'net11', 'net12', 'net13']},
               {'name': 'netset2', 'nativeNetworkUri': 'net14', 'type': 'network-setV5', 'networkUris': ['net14', 'net15', 'net16', 'net17']},
               {'name': 'netset3', 'nativeNetworkUri': 'net18', 'type': 'network-setV5', 'networkUris': ['net18', 'net19', 'net20', 'net21']},
               {'name': 'netset4', 'nativeNetworkUri': 'net22', 'type': 'network-setV5', 'networkUris': ['net22', 'net23', 'net24', 'net25']}]

expected_networksets = [{'name': 'netset1', 'type': 'network-setV5', 'networkUris': ['ETH:net10', 'ETH:net11', 'ETH:net12', 'ETH:net13'], 'nativeNetworkUri':'ETH:net10', 'description':None, 'status':'OK', 'state':'Active', 'category':'network-sets', 'uri':'NS:netset1'},
                        {'name': 'netset2', 'type': 'network-setV5', 'networkUris': ['ETH:net14', 'ETH:net15', 'ETH:net16', 'ETH:net17'], 'nativeNetworkUri':'ETH:net14', 'description':None, 'status':'OK', 'state':'Active', 'category':'network-sets', 'uri':'NS:netset2'},
                        {'name': 'netset3', 'type': 'network-setV5', 'networkUris': ['ETH:net18', 'ETH:net19', 'ETH:net20', 'ETH:net21'], 'nativeNetworkUri':'ETH:net18', 'description':None, 'status':'OK', 'state':'Active', 'category':'network-sets', 'uri':'NS:netset3'},
                        {'name': 'netset4', 'type': 'network-setV5', 'networkUris': ['ETH:net22', 'ETH:net23', 'ETH:net24', 'ETH:net25'], 'nativeNetworkUri':'ETH:net22', 'description':None, 'status':'OK', 'state':'Active', 'category':'network-sets', 'uri':'NS:netset4'}]


storage_systems_with_pools = [
    {
        "credentials": {'username': 'fusionadm', 'password': 'hpvse1'},
        "name": "ovst-3par-8400-03-srv",
        "family": "StoreServ",
        "hostname": "ovst-3par-8400-03-srv.vse.rdlabs.hpecorp.net",
        "deviceSpecificAttributes": {
            "managedDomain": "DDRing8",
            "managedPools": [{'domain': 'DDRing8', 'name': 'FC_Goo_r1', 'raidLevel': 'RAID1', 'state': 'Managed', 'deviceType': 'FC', 'freeCapacity': '2607045148672', 'totalCapacity': '2649994821632', 'uuid': '682df4be-f786-4073-8f01-3b795b3131e5'}, {'domain': 'DDRing8', 'name': 'FC_Goo_r5', 'raidLevel': 'RAID5', 'state': 'Managed', 'deviceType': 'FC', 'freeCapacity': '3907346497536', 'totalCapacity': '3954591137792', 'uuid': '97362619-4303-4d85-8a91-c0ede5555555'}, {'domain': 'DDRing8', 'name': 'FC_Goo_r6', 'raidLevel': 'RAID6', 'state': 'Managed', 'deviceType': 'FC', 'freeCapacity': '3456374931456', 'totalCapacity': '3507646103552', 'uuid': 'b93fa503-c172-4a7b-8e9b-4459515c95ec'}],
            "discoveredPools": [],

        }
    }
]
expected_storage_systems_with_pools = [
    {
        "uri": "SSYS:ovst-3par-8400-03-srv",
        "type": "StorageSystemV5",
        "state": "Managed",
        "category": "storage-systems",
        "status": "OK",
        "name": "ovst-3par-8400-03-srv",
        "family": "StoreServ",
        "hostname": "ovst-3par-8400-03-srv.vse.rdlabs.hpecorp.net",
        "deviceSpecificAttributes": {
            "managedDomain": "DDRing8",
            "serialNumber": "2M271502C2"
        }
    }
]

storage_pools_toedit = [
    {
        "storageSystemUri": "ovst-3par-8400-03-srv",
        "name": "FC_Goo_r1",
        "isManaged": True,
    },
    {
        "storageSystemUri": "ovst-3par-8400-03-srv",
        "name": "FC_Goo_r5",
        "isManaged": True,
    },
    {
        "storageSystemUri": "ovst-3par-8400-03-srv",
        "name": "FC_Goo_r6",
        "isManaged": True,
    }
]

delete_storage_volumes_from_DCS = []

storage_volume_templates = [{"name": "iso-private-thin", "description": "", "rootTemplateUri": "SVT:iso-private-thin", "description": "private non-boot volume template",
                             "properties": {"name": {"title": "Volume name", "description": "A volume name between 1 and 100 characters",
                                                     "type": "string", "minLength": 1, "maxLength": 100, "required": True, "meta": {"locked": False}},
                                            "description": {"title": "Description", "description": "A description for the volume",
                                                            "type": "string", "minLength": 0, "maxLength": 2000, "default": "", "meta": {"locked": False}},
                                            "storagePool": {"title": "Storage Pool", "description": "A common provisioning group URI reference",
                                                            "type": "string", "required": True, "format": "x-uri-reference",
                                                            "meta": {"locked": False, "createOnly": True, "semanticType": "device-storage-pool"},
                                                            "default": "FC_Goo_r1"},
                                            "size": {"title": "Capacity", "description": "The capacity of the volume in bytes",
                                                     "type": "integer", "required": True, "minimum": 1073741824, "maximum": 17592186044416,
                                                     "meta": {"locked": False, "semanticType": "capacity"}, "default": 1073741824, },
                                            "isShareable": {"title": "Is Shareable", "description": "The shareability of the volume",
                                                            "type": "boolean", "meta": {"locked": False}, "default": False, },
                                            "provisioningType": {"title": "Provisioning Type", "description": "The provisioning type for the volume",
                                                                 "type": "string", "enum": ["Thin", "Full"], "meta":{"locked": True, "createOnly": True},
                                                                 "default": "Thin"},
                                            "snapshotPool": {"title": "Snapshot Pool", "description": "A URI reference to the common provisioning group used to create snapshots",
                                                             "type": "string", "format": "x-uri-reference", "meta": {"locked": True, "semanticType": "device-snapshot-storage-pool"},
                                                             "default": "FC_Goo_r1"}}}]

expected_storage_volume_templates = [{"category": "storage-volume-templates", "name": "iso-private-thin", "status": "OK", "state": "Configured", "type": "StorageVolumeTemplateV6", "uri": "SVT:iso-private-thin",
                                      "properties": {"name": {"title": "Volume name", "description": "A volume name between 1 and 100 characters",
                                                              "type": "string", "minLength": 1, "maxLength": 100, "required": True, "meta": {"locked": False}},
                                                     "description": {"title": "Description", "description": "A description for the volume",
                                                                     "type": "string", "minLength": 0, "maxLength": 2000, "default": "", "meta": {"locked": False}},
                                                     "storagePool": {"title": "Storage Pool", "description": "A common provisioning group URI reference",
                                                                     "type": "string", "required": True, "format": "x-uri-reference",
                                                                     "meta": {"locked": False, "createOnly": True, "semanticType": "device-storage-pool"},
                                                                     "default": "SPOOL:FC_Goo_r1"},
                                                     "size": {"title": "Capacity", "description": "The capacity of the volume in bytes",
                                                              "type": "integer", "required": True, "minimum": 1073741824, "maximum": 17592186044416,
                                                              "meta": {"locked": False, "semanticType": "capacity"}, "default": 1073741824, },
                                                     "isShareable": {"title": "Is Shareable", "description": "The shareability of the volume",
                                                                     "type": "boolean", "meta": {"locked": False}, "default": False, },
                                                     "provisioningType": {"title": "Provisioning Type", "description": "The provisioning type for the volume",
                                                                          "type": "string", "enum": ["Thin", "Full"], "meta":{"locked": True, "createOnly": True},
                                                                          "default": "Thin"},
                                                     "snapshotPool": {"title": "Snapshot Pool", "description": "A URI reference to the common provisioning group used to create snapshots",
                                                                      "type": "string", "format": "x-uri-reference", "meta": {"locked": True, "semanticType": "device-snapshot-storage-pool"},
                                                                      "default": "SPOOL:FC_Goo_r1"}}}]

add_existing_storage_volumes = [{"storageSystemUri": "ovst-3par-8400-03-srv", "deviceVolumeName": "ovstQR8-e1bay1-bfsDoNotDelFrom2",
                                 "name": "ovstQR8-e1bay1-bfsDoNotDelFrom2", "isShareable": False},
                                {"storageSystemUri": "ovst-3par-8400-03-srv", "deviceVolumeName": "ovstQR8-e1bay2-bfsDoNotDelFrom2",
                                 "name": "ovstQR8-e1bay2-bfsDoNotDelFrom2", "isShareable": False},
                                {"storageSystemUri": "ovst-3par-8400-03-srv", "deviceVolumeName": "ovstQR8-e1bay5-bfsDoNotDelFrom2",
                                 "name": "ovstQR8-e1bay5-bfsDoNotDelFrom2", "isShareable": False},
                                {"storageSystemUri": "ovst-3par-8400-03-srv", "deviceVolumeName": "ovstQR8-e1bay8-bfsDoNotDelFrom2",
                                 "name": "ovstQR8-e1bay8-bfsDoNotDelFrom2", "isShareable": False},
                                {"storageSystemUri": "ovst-3par-8400-03-srv", "deviceVolumeName": "ovstQR8-e2bay1-bfsDoNotDelFrom2",
                                 "name": "ovstQR8-e2bay1-bfsDoNotDelFrom2", "isShareable": False},
                                {"storageSystemUri": "ovst-3par-8400-03-srv", "deviceVolumeName": "ovstQR8-e2bay2-bfsDoNotDelFrom2",
                                 "name": "ovstQR8-e2bay2-bfsDoNotDelFrom2", "isShareable": False},
                                {"storageSystemUri": "ovst-3par-8400-03-srv", "deviceVolumeName": "ovstQR8-e2bay5-bfsDoNotDelFrom2",
                                 "name": "ovstQR8-e2bay5-bfsDoNotDelFrom2", "isShareable": False},
                                {"storageSystemUri": "ovst-3par-8400-03-srv", "deviceVolumeName": "ovstQR8-e2bay6-bfsDoNotDelFrom2",
                                 "name": "ovstQR8-e2bay6-bfsDoNotDelFrom2", "isShareable": False},
                                {"storageSystemUri": "ovst-3par-8400-03-srv", "deviceVolumeName": "ovstQR8-e2bay10-bfsDoNotDelFrm2",
                                 "name": "ovstQR8-e2bay10-bfsDoNotDelFrm2", "isShareable": False},
                                {"storageSystemUri": "ovst-3par-8400-03-srv", "deviceVolumeName": "ovstQR8-e3bay1-bfsDoNotDelFrom2",
                                 "name": "ovstQR8-e3bay1-bfsDoNotDelFrom2", "isShareable": False},
                                {"storageSystemUri": "ovst-3par-8400-03-srv", "deviceVolumeName": "ovstQR8-e3bay2-bfsDoNotDelFrom2",
                                 "name": "ovstQR8-e3bay2-bfsDoNotDelFrom2", "isShareable": False},
                                {"storageSystemUri": "ovst-3par-8400-03-srv", "deviceVolumeName": "ovstQR8-e3bay5-bfsDoNotDelFrom2",
                                 "name": "ovstQR8-e3bay5-bfsDoNotDelFrom2", "isShareable": False},
                                {"storageSystemUri": "ovst-3par-8400-03-srv", "deviceVolumeName": "ovstQR8-e3bay8-bfsDoNotDelFrom2",
                                 "name": "ovstQR8-e3bay8-bfsDoNotDelFrom2", "isShareable": False}, ]

expected_existing_storage_volumes = [{'isShareable': False, 'name': 'ovstQR8-e1bay1-bfsDoNotDelFrom2', 'state': 'Managed', 'status': 'OK', 'storageSystemVolumeName': 'ovstQR2-e1bay1-bfsDoNotDelFrom3', 'provisioningParameters': {'shareable': False}},
                                     {'isShareable': False, 'name': 'ovstQR8-e1bay2-bfsDoNotDelFrom2', 'state': 'Managed', 'status': 'OK', 'storageSystemVolumeName': 'ovstQR2-e1bay1-bfsDoNotDelFrom3', 'provisioningParameters': {'shareable': False}},
                                     {'isShareable': False, 'name': 'ovstQR8-e1bay5-bfsDoNotDelFrom2', 'state': 'Managed', 'status': 'OK', 'storageSystemVolumeName': 'ovstQR2-e1bay1-bfsDoNotDelFrom3', 'provisioningParameters': {'shareable': False}},
                                     {'isShareable': False, 'name': 'ovstQR8-e1bay8-bfsDoNotDelFrom2', 'state': 'Managed', 'status': 'OK', 'storageSystemVolumeName': 'ovstQR2-e1bay1-bfsDoNotDelFrom3', 'provisioningParameters': {'shareable': False}},
                                     {'isShareable': False, 'name': 'ovstQR8-e2bay1-bfsDoNotDelFrom2', 'state': 'Managed', 'status': 'OK', 'storageSystemVolumeName': 'ovstQR2-e1bay1-bfsDoNotDelFrom3', 'provisioningParameters': {'shareable': False}},
                                     {'isShareable': False, 'name': 'ovstQR8-e2bay2-bfsDoNotDelFrom2', 'state': 'Managed', 'status': 'OK', 'storageSystemVolumeName': 'ovstQR2-e1bay1-bfsDoNotDelFrom3', 'provisioningParameters': {'shareable': False}},
                                     {'isShareable': False, 'name': 'ovstQR8-e2bay5-bfsDoNotDelFrom2', 'state': 'Managed', 'status': 'OK', 'storageSystemVolumeName': 'ovstQR2-e1bay1-bfsDoNotDelFrom3', 'provisioningParameters': {'shareable': False}},
                                     {'isShareable': False, 'name': 'ovstQR8-e2bay6-bfsDoNotDelFrom2', 'state': 'Managed', 'status': 'OK', 'storageSystemVolumeName': 'ovstQR2-e1bay1-bfsDoNotDelFrom3', 'provisioningParameters': {'shareable': False}},
                                     {'isShareable': False, 'name': 'ovstQR8-e2bay10-bfsDoNotDelFrm2', 'state': 'Managed', 'status': 'OK', 'storageSystemVolumeName': 'ovstQR2-e1bay1-bfsDoNotDelFrom3', 'provisioningParameters': {'shareable': False}},
                                     {'isShareable': False, 'name': 'ovstQR8-e3bay1-bfsDoNotDelFrom2', 'state': 'Managed', 'status': 'OK', 'storageSystemVolumeName': 'ovstQR2-e1bay1-bfsDoNotDelFrom3', 'provisioningParameters': {'shareable': False}},
                                     {'isShareable': False, 'name': 'ovstQR8-e3bay2-bfsDoNotDelFrom2', 'state': 'Managed', 'status': 'OK', 'storageSystemVolumeName': 'ovstQR2-e1bay1-bfsDoNotDelFrom3', 'provisioningParameters': {'shareable': False}},
                                     {'isShareable': False, 'name': 'ovstQR8-e3bay5-bfsDoNotDelFrom2', 'state': 'Managed', 'status': 'OK', 'storageSystemVolumeName': 'ovstQR2-e1bay1-bfsDoNotDelFrom3', 'provisioningParameters': {'shareable': False}},
                                     {'isShareable': False, 'name': 'ovstQR8-e3bay8-bfsDoNotDelFrom2', 'state': 'Managed', 'status': 'OK', 'storageSystemVolumeName': 'ovstQR2-e1bay1-bfsDoNotDelFrom3', 'provisioningParameters': {'shareable': False}}, ]
storage_volumes = [  # new private no template
    {"properties": {"description": "non-boot private volume", "isShareable": False, "name": "dd8-tbird-1bay1priv",
                                   "provisioningType": "Full", "size": 5368709120, "storagePool": "FC_Goo_r1"}, "templateUri": "ROOT", "isPermanent": True, },
    {"properties": {"description": "non-boot private volume", "isShareable": False, "name": "dd8-tbird-1bay2priv",
                                   "provisioningType": "Full", "size": 5368709120, "storagePool": "FC_Goo_r1"}, "templateUri": "ROOT", "isPermanent": True, },
    {"properties": {"description": "non-boot private volume", "isShareable": False, "name": "dd8-tbird-1bay3priv",
                                   "provisioningType": "Full", "size": 5368709120, "storagePool": "FC_Goo_r1"}, "templateUri": "ROOT", "isPermanent": True, },
    {"properties": {"description": "non-boot private volume", "isShareable": False, "name": "dd8-tbird-1bay4priv",
                                   "provisioningType": "Full", "size": 5368709120, "storagePool": "FC_Goo_r1"}, "templateUri": "ROOT", "isPermanent": True, },
    {"properties": {"description": "non-boot private volume", "isShareable": False, "name": "dd8-tbird-2bay1priv",
                                   "provisioningType": "Full", "size": 5368709120, "storagePool": "FC_Goo_r5"}, "templateUri": "ROOT", "isPermanent": True, },
    {"properties": {"description": "non-boot private volume", "isShareable": False, "name": "dd8-tbird-2bay2priv",
                                   "provisioningType": "Full", "size": 5368709120, "storagePool": "FC_Goo_r5"}, "templateUri": "ROOT", "isPermanent": True, },
    {"properties": {"description": "non-boot private volume", "isShareable": False, "name": "dd8-tbird-2bay3priv",
                                   "provisioningType": "Full", "size": 5368709120, "storagePool": "FC_Goo_r5"}, "templateUri": "ROOT", "isPermanent": True, },
    {"properties": {"description": "non-boot private volume", "isShareable": False, "name": "dd8-tbird-2bay4priv",
                                   "provisioningType": "Full", "size": 5368709120, "storagePool": "FC_Goo_r5"}, "templateUri": "ROOT", "isPermanent": True, },

    # new private with template
    {"properties": {"description": "non-boot private volume", "isShareable": False, "name": "dd8-tbird-2bay5priv",
                                   "size": 5368709120, "storagePool": "FC_Goo_r1"}, "templateUri": "iso-private-thin", "isPermanent": True, },
    {"properties": {"description": "non-boot private volume", "isShareable": False, "name": "dd8-tbird-3bay1priv",
                                   "size": 5368709120, "storagePool": "FC_Goo_r1"}, "templateUri": "iso-private-thin", "isPermanent": True, },
    {"properties": {"description": "non-boot private volume", "isShareable": False, "name": "dd8-tbird-3bay2priv",
                                   "size": 5368709120, "storagePool": "FC_Goo_r1"}, "templateUri": "iso-private-thin", "isPermanent": True, },
    {"properties": {"description": "non-boot private volume", "isShareable": False, "name": "dd8-tbird-3bay3priv",
                                   "size": 5368709120, "storagePool": "FC_Goo_r1"}, "templateUri": "iso-private-thin", "isPermanent": True, },
    {"properties": {"description": "non-boot private volume", "isShareable": False, "name": "dd8-tbird-3bay4priv",
                                   "size": 5368709120, "storagePool": "FC_Goo_r1"}, "templateUri": "iso-private-thin", "isPermanent": True, },
    {"properties": {"description": "non-boot private volume", "isShareable": False, "name": "dd8-tbird-3bay5priv",
                                   "size": 5368709120, "storagePool": "FC_Goo_r1"}, "templateUri": "iso-private-thin", "isPermanent": True, },
    # shared volume
    {"properties": {"description": "shared volume", "isShareable": True, "name": "dd8-shared",
                                   "provisioningType": "Full", "size": 5368709120, "storagePool": "FC_Goo_r1"}, "templateUri": "ROOT", "isPermanent": True}]

expected_storage_volumes = [{'isShareable': False, 'name': 'dd8-tbird-1bay1priv', 'state': 'Managed', 'status': 'OK', 'storageSystemVolumeName': 'ovstQR2-e1bay1-bfsDoNotDelFrom3', 'provisioningParameters': {'shareable': False}},
                            {'isShareable': False, 'name': 'dd8-tbird-1bay2priv', 'state': 'Managed', 'status': 'OK', 'storageSystemVolumeName': 'ovstQR2-e1bay1-bfsDoNotDelFrom3', 'provisioningParameters': {'shareable': False}},
                            {'isShareable': False, 'name': 'dd8-tbird-1bay3priv', 'state': 'Managed', 'status': 'OK', 'storageSystemVolumeName': 'ovstQR2-e1bay1-bfsDoNotDelFrom3', 'provisioningParameters': {'shareable': False}},
                            {'isShareable': False, 'name': 'dd8-tbird-1bay4priv', 'state': 'Managed', 'status': 'OK', 'storageSystemVolumeName': 'ovstQR2-e1bay1-bfsDoNotDelFrom3', 'provisioningParameters': {'shareable': False}},
                            {'isShareable': False, 'name': 'dd8-tbird-2bay1priv', 'state': 'Managed', 'status': 'OK', 'storageSystemVolumeName': 'ovstQR2-e1bay1-bfsDoNotDelFrom3', 'provisioningParameters': {'shareable': False}},
                            {'isShareable': False, 'name': 'dd8-tbird-2bay2priv', 'state': 'Managed', 'status': 'OK', 'storageSystemVolumeName': 'ovstQR2-e1bay1-bfsDoNotDelFrom3', 'provisioningParameters': {'shareable': False}},
                            {'isShareable': False, 'name': 'dd8-tbird-2bay3priv', 'state': 'Managed', 'status': 'OK', 'storageSystemVolumeName': 'ovstQR2-e1bay1-bfsDoNotDelFrom3', 'provisioningParameters': {'shareable': False}},
                            {'isShareable': False, 'name': 'dd8-tbird-2bay4priv', 'state': 'Managed', 'status': 'OK', 'storageSystemVolumeName': 'ovstQR2-e1bay1-bfsDoNotDelFrom3', 'provisioningParameters': {'shareable': False}},

                            {'isShareable': False, 'name': 'dd8-tbird-2bay5priv', 'state': 'Managed', 'status': 'OK', 'storageSystemVolumeName': 'ovstQR2-e1bay1-bfsDoNotDelFrom3', 'provisioningParameters': {'shareable': False}},
                            {'isShareable': False, 'name': 'dd8-tbird-3bay1priv', 'state': 'Managed', 'status': 'OK', 'storageSystemVolumeName': 'ovstQR2-e1bay1-bfsDoNotDelFrom3', 'provisioningParameters': {'shareable': False}},
                            {'isShareable': False, 'name': 'dd8-tbird-3bay2priv', 'state': 'Managed', 'status': 'OK', 'storageSystemVolumeName': 'ovstQR2-e1bay1-bfsDoNotDelFrom3', 'provisioningParameters': {'shareable': False}},
                            {'isShareable': False, 'name': 'dd8-tbird-3bay3priv', 'state': 'Managed', 'status': 'OK', 'storageSystemVolumeName': 'ovstQR2-e1bay1-bfsDoNotDelFrom3', 'provisioningParameters': {'shareable': False}},
                            {'isShareable': False, 'name': 'dd8-tbird-3bay4priv', 'state': 'Managed', 'status': 'OK', 'storageSystemVolumeName': 'ovstQR2-e1bay1-bfsDoNotDelFrom3', 'provisioningParameters': {'shareable': False}},
                            {'isShareable': False, 'name': 'dd8-tbird-3bay5priv', 'state': 'Managed', 'status': 'OK', 'storageSystemVolumeName': 'ovstQR2-e1bay1-bfsDoNotDelFrom3', 'provisioningParameters': {'shareable': False}},
                            {'isShareable': True, 'name': 'dd8-shared', 'state': 'Managed', 'status': 'OK', 'storageSystemVolumeName': 'ovstQR2-e1bay1-bfsDoNotDelFrom3', 'provisioningParameters': {'shareable': False}}]


sas_lig = [
    {
        "name": "LIG-Natasha",
        "type": "sas-logical-interconnect-groupV2",
        "enclosureType": "SY12000",
        "interconnectMapTemplate": [
            {
                "enclosureIndex": 1,
                "enclosure": 1,
                "bay": 1,
                "type": "Synergy 12Gb SAS Connection Module"
            },
            {
                "enclosureIndex": 1,
                "bay": 4,
                "enclosure": 1,
                "type": "Synergy 12Gb SAS Connection Module"
            }

        ],
        "interconnectBaySet": 1,
        "enclosureIndexes": [1]
    }
]
expected_sas_lig = [
    {
        "uri": "SASLIG:LIG-Natasha",
        "state": "Active",
        "status": "OK",
        "description": None,
        "name": "LIG-Natasha",
        "type": "sas-logical-interconnect-groupV2",
        "enclosureType": "SY12000",
        "interconnectBaySet": 1,
        "enclosureIndexes": [1]
    }
]

ligs = [
    {
        "name": "LIG-Potash",
        "type": "logical-interconnect-groupV7",
        "enclosureType": "SY12000",
        "ethernetSettings": None,
        "interconnectMapTemplate": [
            {
                "enclosureIndex": 2,
                "bay": 3,
                "enclosure": 2,
                "type": "Synergy 20Gb Interconnect Link Module"
            },
            {
                "enclosureIndex": 3,
                "bay": 6,
                "enclosure": 3,
                "type": "Synergy 20Gb Interconnect Link Module"
            },
            {
                "enclosureIndex": 2,
                "enclosure": 2,
                "bay": 6,
                "type": "Virtual Connect SE 40Gb F8 Module for Synergy"
            },
            {
                "enclosureIndex": 1,
                "enclosure": 1,
                "bay": 6,
                "type": "Synergy 20Gb Interconnect Link Module"
            },
            {
                "enclosureIndex": 1,
                "bay": 3,
                "enclosure": 1,
                "type": "Virtual Connect SE 40Gb F8 Module for Synergy"
            },
            {
                "enclosureIndex": 3,
                "bay": 3,
                "enclosure": 3,
                "type": "Synergy 20Gb Interconnect Link Module"
            }

        ],
        "interconnectBaySet": 3,
        "redundancyType": "HighlyAvailable",
        "telemetryConfiguration": {
            "enableTelemetry": True,
            "sampleCount": 12,
            "sampleInterval": 300
        },
        "uplinkSets": [
            {
                "ethernetNetworkType": "NotApplicable",
                "lacpTimer": None,
                "logicalPortConfigInfos": [
                    {
                        "speed": "Auto",
                        "bay": "6",
                        "enclosure": "2",
                        "port": "Q2:1"
                    }
                ],
                "mode": "Auto",
                "name": "FC-b",
                "nativeNetworkUri": None,
                "networkType": "FibreChannel",
                "networkUris": [
                    "FC-B"
                ],
                "primaryPort": None
            },
            {
                "ethernetNetworkType": "NotApplicable",
                "lacpTimer": None,
                "logicalPortConfigInfos": [
                    {
                        "speed": "Auto",
                        "port": "Q2:1",
                        "enclosure": "1",
                        "bay": "3"
                    }
                ],
                "mode": "Auto",
                "name": "FC-a",
                "nativeNetworkUri": None,
                "networkType": "FibreChannel",
                "networkUris": [
                    "FC-A"
                ],
                "primaryPort": None
            },
            {
                "ethernetNetworkType": "Tagged",
                "lacpTimer": "Short",
                "logicalPortConfigInfos": [
                    {
                        "speed": "Auto",
                        "port": "Q1.1",
                        "enclosure": "2",
                        "bay": "6"
                    },
                    {
                        "speed": "Auto",
                        "port": "Q1.1",
                        "enclosure": "1",
                        "bay": "3"
                    }
                ],
                "mode": "Auto",
                "name": "Ethernet",
                "nativeNetworkUri": None,
                "networkType": "Ethernet",
                "networkUris": [
                    "net10",
                    "net12",
                    "net13",
                    "net11"
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
        "enclosureIndexes": [1, 2, 3]
    },
    {
        "name": "LIG-Carbon",
        "type": "logical-interconnect-groupV7",
        "enclosureType": "SY12000",
        "ethernetSettings": None,
        "interconnectMapTemplate": [
            {
                "enclosureIndex": -1,
                "enclosure": -1,
                "bay": 1,
                "type": "Virtual Connect SE 16Gb FC Module for Synergy"
            },
            {
                "enclosureIndex": -1,
                "bay": 4,
                "enclosure": -1,
                "type": "Virtual Connect SE 16Gb FC Module for Synergy"
            }

        ],
        "interconnectBaySet": 1,
        "redundancyType": "Redundant",
        "telemetryConfiguration": {
            "enableTelemetry": True,
            "sampleCount": 60,
            "sampleInterval": 60
        },
        "uplinkSets": [
            {
                "ethernetNetworkType": "NotApplicable",
                "lacpTimer": None,
                "logicalPortConfigInfos": [
                    {
                        "speed": "Auto",
                        "enclosure": "-1",
                        "port": "1",
                        "bay": "4"
                    }
                ],
                "mode": "Auto",
                "name": "FC-Carbon-B",
                "nativeNetworkUri": None,
                "networkType": "FibreChannel",
                "networkUris": [
                    "FC-B"
                ],
                "primaryPort": None
            },
            {
                "ethernetNetworkType": "NotApplicable",
                "lacpTimer": None,
                "logicalPortConfigInfos": [
                    {
                        "speed": "Auto",
                        "bay": "1",
                        "port": "1",
                        "enclosure": "-1"
                    }
                ],
                "mode": "Auto",
                "name": "FC-Carbon-A",
                "nativeNetworkUri": None,
                "networkType": "FibreChannel",
                "networkUris": [
                    "FC-A"
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
        "enclosureIndexes": [-1]
    },
    {
        "name": "LIG-Carbon-tmp",
        "type": "logical-interconnect-groupV7",
        "enclosureType": "SY12000",
        "ethernetSettings": None,
        "interconnectMapTemplate": [
            {
                "enclosureIndex": -1,
                "enclosure": -1,
                "bay": 1,
                "type": "Virtual Connect SE 16Gb FC Module for Synergy"
            },
            {
                "enclosureIndex": -1,
                "bay": 4,
                "enclosure": -1,
                "type": "Virtual Connect SE 16Gb FC Module for Synergy"
            }

        ],
        "interconnectBaySet": 1,
        "redundancyType": "Redundant",
        "telemetryConfiguration": {
            "enableTelemetry": True,
            "sampleCount": 60,
            "sampleInterval": 60
        },
        "uplinkSets": [],
        "qosConfiguration": {
            "activeQosConfig": {u'category': u'qos-aggregated-configuration', u'status': None, u'description': None, u'created': None, u'uri': None, u'modified': None, u'configType': u'Passthrough', u'state': None, u'eTag': None, u'downlinkClassificationType': None, u'uplinkClassificationType': None, u'qosTrafficClassifiers': [], u'type': u'QosConfiguration', u'name': None},
            "inactiveFCoEQosConfig": None,
            "inactiveNonFCoEQosConfig": None,
            "name": None,
            "type": "qos-aggregated-configuration"
        },
        "enclosureIndexes": [-1]
    },
]
expected_lig = [
    {
        "uri": "LIG:LIG-Potash",
        "status": None,
        "stackingHealth": None,
        "category": "logical-interconnect-groups",
        "state": "Active",
        "internalNetworkUris": "[]",
        "stackingMode": None,
        "description": None,
        "name": "LIG-Potash",
        "type": "logical-interconnect-groupV7",
        "enclosureType": "SY12000",
        "ethernetSettings": {
            "enableFastMacCacheFailover": True,
            "enableIgmpSnooping": False,
            "enableNetworkLoopProtection": True,
            "enablePauseFloodProtection": True,
            "igmpIdleTimeoutInterval": 260,
            "interconnectType": "Ethernet",
            "macRefreshInterval": 5
        },
        "interconnectBaySet": 3,
        "redundancyType": "HighlyAvailable",
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
        "enclosureIndexes": [1, 2, 3]
    },
    {
        "uri": "LIG:LIG-Carbon",
        "status": None,
        "stackingHealth": None,
        "category": "logical-interconnect-groups",
        "state": "Active",
        "internalNetworkUris": "[]",
        "stackingMode": None,
        "description": None,
        "name": "LIG-Carbon",
        "type": "logical-interconnect-groupV7",
        "enclosureType": "SY12000",
        "ethernetSettings": {
            "enableFastMacCacheFailover": True,
            "enableIgmpSnooping": False,
            "enableNetworkLoopProtection": True,
            "enablePauseFloodProtection": True,
            "igmpIdleTimeoutInterval": 260,
            "interconnectType": "Ethernet",
            "macRefreshInterval": 5
        },
        "interconnectBaySet": 1,
        "redundancyType": "Redundant",
        "telemetryConfiguration": {
            "enableTelemetry": True,
            "sampleCount": 60,
            "sampleInterval": 60
        },
        "qosConfiguration": {
            "activeQosConfig": {u'category': u'qos-aggregated-configuration', u'status': None, u'description': None, u'created': None, u'uri': None, u'modified': None, u'configType': u'Passthrough', u'state': None, u'eTag': None, u'downlinkClassificationType': None, u'uplinkClassificationType': None, u'qosTrafficClassifiers': [], u'type': u'QosConfiguration', u'name': None},
            "inactiveFCoEQosConfig": None,
            "inactiveNonFCoEQosConfig": None,
            "name": None,
            "type": "qos-aggregated-configuration"
        },
        "enclosureIndexes": [-1]
    },
]

encgroups_add = [{"name": "EG-Goose",
                  "interconnectBayMappings":
                  [
                      {"interconnectBay": 1, "logicalInterconnectGroupUri": "LIG:LIG-Carbon-tmp", "enclosureIndex": 1},
                      {"interconnectBay": 1, "logicalInterconnectGroupUri": "SASLIG:LIG-Natasha", "enclosureIndex": 2},
                      {"interconnectBay": 3, "logicalInterconnectGroupUri": "LIG:LIG-Potash", },
                      {"interconnectBay": 4, "logicalInterconnectGroupUri": "LIG:LIG-Carbon-tmp", "enclosureIndex": 1},
                      {"interconnectBay": 4, "logicalInterconnectGroupUri": "SASLIG:LIG-Natasha", "enclosureIndex": 2},
                      {"interconnectBay": 6, "logicalInterconnectGroupUri": "LIG:LIG-Potash", }
                  ], "ipAddressingMode": "DHCP", "enclosureCount": 3}]

expected_encgroups_add = [{"uri": "EG:EG-Goose", "description": None, "category": "enclosure-groups", "state": "Normal", "status": "OK", "powerMode": "RedundantPowerFeed", "portMappingCount": 8,
                           "portMappings": [{u'midplanePort': 1, u'interconnectBay': 1}, {u'midplanePort': 2, u'interconnectBay': 2}, {u'midplanePort': 3, u'interconnectBay': 3}, {u'midplanePort': 4, u'interconnectBay': 4}, {u'midplanePort': 5, u'interconnectBay': 5}, {u'midplanePort': 6, u'interconnectBay': 6}, {u'midplanePort': 7, u'interconnectBay': 7}, {u'midplanePort': 8, u'interconnectBay': 8}],
                           "ipRangeUris": [], "associatedLogicalInterconnectGroups": [u'LIG:LIG-Potash', u'LIG:LIG-Carbon-tmp', u'SASLIG:LIG-Natasha'],
                           "name": "EG-Goose", "type": "EnclosureGroupV8", "enclosureTypeUri": "/rest/enclosure-types/SY12000", "stackingMode": "Enclosure", "name": "EG-Goose", "interconnectBayMappingCount": "6",
                           "interconnectBayMappings":
                           [
                               {"interconnectBay": 1, "logicalInterconnectGroupUri": "LIG:LIG-Carbon-tmp", },
                               {"interconnectBay": 1, "logicalInterconnectGroupUri": "SASLIG:LIG-Natasha", },
                               {"interconnectBay": 3, "logicalInterconnectGroupUri": "LIG:LIG-Potash", },
                               {"interconnectBay": 4, "logicalInterconnectGroupUri": "LIG:LIG-Carbon-tmp", },
                               {"interconnectBay": 4, "logicalInterconnectGroupUri": "SASLIG:LIG-Natasha", },
                               {"interconnectBay": 6, "logicalInterconnectGroupUri": "LIG:LIG-Potash", }
                           ], "ipAddressingMode": "DHCP", "enclosureCount": 3}]

logical_enclosure = [{"name": "LE-Goose", "enclosureUris": ["ENC:MXQ718061G", "ENC:MXQ718061H", "ENC:MXQ718061J"], "enclosureGroupUri": "EG:EG-Goose"}]

expected_logical_enclosure = [{"type": "LogicalEnclosureV5", "uri": "LE-Goose", "status": "OK", "name": "LE-Goose", "enclosureUris": ["ENC:MXQ718061G", "ENC:MXQ718061H", "ENC:MXQ718061J"], "enclosureGroupUri": "EG:EG-Goose"}]

edit_enclosure_group = {'name': 'EG-Goose', 'type': 'EnclosureGroupV8',
                        "stackingMode": "Enclosure", "configurationScript": "", "uri": None, "powerMode": 'RedundantPowerFeed', "ipRangeUris": [],
                        'interconnectBayMappings':
                        [{"interconnectBay": 1, "logicalInterconnectGroupUri": "LIG:LIG-Carbon", "enclosureIndex": 1},
                         {"interconnectBay": 1, "logicalInterconnectGroupUri": "SASLIG:LIG-Natasha", "enclosureIndex": 2},
                            {"interconnectBay": 3, "logicalInterconnectGroupUri": "LIG:LIG-Potash", },
                            {"interconnectBay": 4, "logicalInterconnectGroupUri": "LIG:LIG-Carbon", "enclosureIndex": 1},
                            {"interconnectBay": 4, "logicalInterconnectGroupUri": "SASLIG:LIG-Natasha", "enclosureIndex": 2},
                            {"interconnectBay": 6, "logicalInterconnectGroupUri": "LIG:LIG-Potash", }
                         ],
                        "enclosureCount": 3, "osDeploymentSettings": None, 'ipAddressingMode': 'External', 'enclosureTypeUri': 'SY12000'}

update_logical_enclosure_from_group = {'name': 'LE-Goose'}

edit_li_telemetry_config = {'name': 'LE-Goose-LIG-Potash', 'type': 'telemetry-configuration', 'enableTelemetry': True, 'sampleCount': 20, 'sampleInterval': 200,
                            'description': None, 'status': None, 'state': None, 'category': 'telemetry-configurations', 'uri': '/rest/logical-interconnects'}

update_logical_interconnect_from_group = {'name': 'LE-Goose-LIG-Potash'}

li_state = {"name": "LE-Goose-LIG-Carbon-tmp-1"}

li_state_after_update = {"name": "LE-Goose-LIG-Carbon-1"}

le_support_dump = [{"name": "LE-Goose", "errorCode": "LESD1", "encrypt": True, "excludeApplianceDump": False}]


server_profile_templates = [
    {
        "name": "ISO-UI1Bay8-Template",
        "type": "ServerProfileTemplateV7",
        "serverProfileDescription": "",
        "serverHardwareTypeUri": "SHT:SY 480 Gen10:1:Synergy 3830C 16G FC HBA:3:Synergy 3820C 10/20Gb CNA",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "manageConnections": True,
            "connections": [
                {
                    "id": 1,
                    "name": "",
                    "functionType": "FibreChannel",
                    "portId": "Mezz 1:1",
                    "requestedMbps": "16000",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable', u'bootVlanId': None},
                },
                {
                    "id": 2,
                    "name": "",
                    "functionType": "FibreChannel",
                    "portId": "Mezz 1:2",
                    "requestedMbps": "16000",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable', u'bootVlanId': None},
                },
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk', u'CD', u'USB', u'PXE']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "forceInstallFirmware": False
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorNameType": "AutoGenerated",
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": [
            ]

        },
    },
    {
        "name": "ISO-UI1Bay6-Template",
        "type": "ServerProfileTemplateV7",
        "serverProfileDescription": "",
        "serverHardwareTypeUri": "SHT:SY 660 Gen10:1:HP Synergy 3830C 16G FC HBA:3:Synergy 3820C 10/20Gb CNA:4:Synergy 3830C 16G FC HBA:6:Synergy 3820C 10/20Gb CNA",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "manageConnections": True,
            "connections": [
                {
                    "id": 1,
                    "name": "",
                    "functionType": "Ethernet",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable', u'bootVlanId': None},
                },
                {
                    "id": 3,
                    "name": "",
                    "functionType": "FibreChannel",
                    "portId": "Mezz 1:1",
                    "requestedMbps": "Auto",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable', u'bootVlanId': None},
                },
                {
                    "id": 4,
                    "name": "",
                    "functionType": "FibreChannel",
                    "portId": "Mezz 1:2",
                    "requestedMbps": "Auto",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable', u'bootVlanId': None},
                },
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'CD', u'USB', u'HardDisk', u'PXE']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "forceInstallFirmware": False
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorNameType": "AutoGenerated",
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": [
            ]

        },
    },
    {
        "name": "ISO-UI1Bay7-Template",
        "type": "ServerProfileTemplateV7",
        "serverProfileDescription": "",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9:1:Synergy 3530C 16G HBA:3:Synergy 3820C 10/20Gb CNA",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "manageConnections": True,
            "connections": [
                {
                    "id": 1,
                    "name": "",
                    "functionType": "Ethernet",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable', u'bootVlanId': None},
                },
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'CD', u'USB', u'HardDisk', u'PXE']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "forceInstallFirmware": False
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorNameType": "AutoGenerated",
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": [
            ]

        },
    }
]
expected_server_profile_templates = [
    {
        "uri": "SPT:ISO-UI1Bay8-Template",
        "status": "OK",
        "name": "ISO-UI1Bay8-Template",
        "type": "ServerProfileTemplateV7",
        "serverProfileDescription": "",
        "serverHardwareTypeUri": "SHT:SY 480 Gen10:1:Synergy 3830C 16G FC HBA:3:Synergy 3820C 10/20Gb CNA",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "manageConnections": True,
            "connections": [
                {
                    "id": 1,
                    "name": "",
                    "functionType": "FibreChannel",
                    "portId": "Mezz 1:1",
                    "requestedMbps": "16000",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable', u'bootVlanId': None},
                },
                {
                    "id": 2,
                    "name": "",
                    "functionType": "FibreChannel",
                    "portId": "Mezz 1:2",
                    "requestedMbps": "16000",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable', u'bootVlanId': None},
                },
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk', u'CD', u'USB', u'PXE']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "forceInstallFirmware": False
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorNameType": "AutoGenerated",
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": [
            ]

        },
    },
    {
        "uri": "SPT:ISO-UI1Bay6-Template",
        "status": "OK",
        "name": "ISO-UI1Bay6-Template",
        "type": "ServerProfileTemplateV7",
        "serverProfileDescription": "",
        "serverHardwareTypeUri": "SHT:SY 660 Gen10:1:HP Synergy 3830C 16G FC HBA:3:Synergy 3820C 10/20Gb CNA:4:Synergy 3830C 16G FC HBA:6:Synergy 3820C 10/20Gb CNA",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "manageConnections": True,
            "connections": [
                {
                    "id": 1,
                    "name": "",
                    "functionType": "Ethernet",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable', u'bootVlanId': None},
                },
                {
                    "id": 3,
                    "name": "",
                    "functionType": "FibreChannel",
                    "portId": "Mezz 1:1",
                    "requestedMbps": "Auto",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable', u'bootVlanId': None},
                },
                {
                    "id": 4,
                    "name": "",
                    "functionType": "FibreChannel",
                    "portId": "Mezz 1:2",
                    "requestedMbps": "Auto",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable', u'bootVlanId': None},
                },
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'CD', u'USB', u'HardDisk', u'PXE']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "forceInstallFirmware": False
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorNameType": "AutoGenerated",
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": [
            ]

        },
    },
    {
        "uri": "SPT:ISO-UI1Bay7-Template",
        "status": "OK",
        "name": "ISO-UI1Bay7-Template",
        "type": "ServerProfileTemplateV7",
        "serverProfileDescription": "",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9:1:Synergy 3530C 16G HBA:3:Synergy 3820C 10/20Gb CNA",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "manageConnections": True,
            "connections": [
                {
                    "id": 1,
                    "name": "",
                    "functionType": "Ethernet",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable', u'bootVlanId': None},
                },
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'CD', u'USB', u'HardDisk', u'PXE']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "forceInstallFirmware": False
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorNameType": "AutoGenerated",
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": [
            ]

        },
    }
]

edit_server_profile_templates = [
    {
        "name": "ISO-UI1Bay6-Template",
        "type": "ServerProfileTemplateV7",
        "serverProfileDescription": "",
        "serverHardwareTypeUri": "SHT:SY 660 Gen10:1:HP Synergy 3830C 16G FC HBA:3:Synergy 3820C 10/20Gb CNA:4:Synergy 3830C 16G FC HBA:6:Synergy 3820C 10/20Gb CNA",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "manageConnections": True,
            "connections": [
                {
                    "id": 1,
                    "name": "",
                    "functionType": "Ethernet",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable', u'bootVlanId': None},
                },
                {
                    "id": 3,
                    "name": "",
                    "functionType": "FibreChannel",
                    "portId": "Mezz 1:1",
                    "requestedMbps": "Auto",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable', u'bootVlanId': None},
                },
                {
                    "id": 4,
                    "name": "",
                    "functionType": "FibreChannel",
                    "portId": "Mezz 1:2",
                    "requestedMbps": "Auto",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable', u'bootVlanId': None},
                },
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'CD', u'USB', u'HardDisk', u'PXE']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "forceInstallFirmware": False
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorNameType": "AutoGenerated",
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:dd8-shared",
                    "lunType": "Manual",
                    "lun": 1,
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                },
            ]

        },
    },
    {
        "name": "ISO-UI1Bay8-Template",
        "type": "ServerProfileTemplateV7",
        "serverProfileDescription": "",
        "serverHardwareTypeUri": "SHT:SY 480 Gen10:1:Synergy 3830C 16G FC HBA:3:Synergy 3820C 10/20Gb CNA",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "manageConnections": True,
            "connections": [
                {
                    "id": 1,
                    "name": "",
                    "functionType": "FibreChannel",
                    "portId": "Mezz 1:1",
                    "requestedMbps": "16000",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable', u'bootVlanId': None},
                },
                {
                    "id": 2,
                    "name": "",
                    "functionType": "FibreChannel",
                    "portId": "Mezz 1:2",
                    "requestedMbps": "16000",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable', u'bootVlanId': None},
                },
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk', u'CD', u'USB', u'PXE']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "forceInstallFirmware": False
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorNameType": "AutoGenerated",
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:dd8-shared",
                    "lunType": "Manual",
                    "lun": 1,
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 1,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:01:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:01:00:02:AC:01:D9:ED"
                                        }],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:02:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:02:00:02:AC:01:D9:ED"
                                        }],
                        },

                    ]
                },
            ]

        },
    },
    {
        "name": "ISO-UI1Bay7-Template",
        "type": "ServerProfileTemplateV7",
        "serverProfileDescription": "",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9:1:Synergy 3530C 16G HBA:3:Synergy 3820C 10/20Gb CNA",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "manageConnections": True,
            "connections": [
                {
                    "id": 1,
                    "name": "",
                    "functionType": "Ethernet",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable', u'bootVlanId': None},
                },
                {
                    "id": 2,
                    "name": "",
                    "functionType": "Ethernet",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net11",
                    "boot": {u'priority': u'NotBootable', u'bootVlanId': None},
                },
                {
                    "id": 3,
                    "name": "",
                    "functionType": "Ethernet",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net12",
                    "boot": {u'priority': u'NotBootable', u'bootVlanId': None},
                },
                {
                    "id": 4,
                    "name": "",
                    "functionType": "FibreChannel",
                    "portId": "Mezz 1:1",
                    "requestedMbps": "16000",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable', u'bootVlanId': None},
                },
                {
                    "id": 5,
                    "name": "",
                    "functionType": "FibreChannel",
                    "portId": "Mezz 1:2",
                    "requestedMbps": "16000",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable', u'bootVlanId': None},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'CD', u'USB', u'HardDisk', u'PXE']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "forceInstallFirmware": False
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorNameType": "AutoGenerated",
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:dd8-shared",
                    "lunType": "Manual",
                    "lun": 1,
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        }, {
                            "isEnabled": True,
                            "connectionId": 5,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ],
                },
            ]

        },
    }
]

expected_edit_server_profile_templates = [
    {
        "name": "ISO-UI1Bay6-Template",
        "type": "ServerProfileTemplateV7",
        "serverProfileDescription": "",
        "serverHardwareTypeUri": "SHT:SY 660 Gen10:1:HP Synergy 3830C 16G FC HBA:3:Synergy 3820C 10/20Gb CNA:4:Synergy 3830C 16G FC HBA:6:Synergy 3820C 10/20Gb CNA",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "manageConnections": True,
            "connections": [
                {
                    "id": 1,
                    "name": "",
                    "functionType": "Ethernet",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable', u'bootVlanId': None},
                },
                {
                    "id": 3,
                    "name": "",
                    "functionType": "FibreChannel",
                    "portId": "Mezz 1:1",
                    "requestedMbps": "Auto",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable', u'bootVlanId': None},
                },
                {
                    "id": 4,
                    "name": "",
                    "functionType": "FibreChannel",
                    "portId": "Mezz 1:2",
                    "requestedMbps": "Auto",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable', u'bootVlanId': None},
                },
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'CD', u'USB', u'HardDisk', u'PXE']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "forceInstallFirmware": False
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorNameType": "AutoGenerated",
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:dd8-shared",
                    "lunType": "Manual",
                    "lun": 1,
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [],
                        }, {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ],
                },
            ]

        },
    },
    {
        "name": "ISO-UI1Bay8-Template",
        "type": "ServerProfileTemplateV7",
        "serverProfileDescription": "",
        "serverHardwareTypeUri": "SHT:SY 480 Gen10:1:Synergy 3830C 16G FC HBA:3:Synergy 3820C 10/20Gb CNA",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "manageConnections": True,
            "connections": [
                {
                    "id": 1,
                    "name": "",
                    "functionType": "FibreChannel",
                    "portId": "Mezz 1:1",
                    "requestedMbps": "16000",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable', u'bootVlanId': None},
                },
                {
                    "id": 2,
                    "name": "",
                    "functionType": "FibreChannel",
                    "portId": "Mezz 1:2",
                    "requestedMbps": "16000",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable', u'bootVlanId': None},
                },
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk', u'CD', u'USB', u'PXE']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "forceInstallFirmware": False
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorNameType": "AutoGenerated",
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {"id": 1, "volumeUri": "SVOL:dd8-shared", "lunType": "Manual", "lun": 1,
                    "storagePaths": [{"isEnabled": True, "connectionId": 1, "targetSelector": "Auto", "targets": [], },
                                     {"isEnabled": True, "connectionId": 2, "targetSelector": "Auto", "targets": [], }, ]
                 }, ]},
    },
    {
        "name": "ISO-UI1Bay7-Template",
        "type": "ServerProfileTemplateV7",
        "serverProfileDescription": "",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9:1:Synergy 3530C 16G HBA:3:Synergy 3820C 10/20Gb CNA",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "manageConnections": True,
            "connections": [
                {
                    "id": 1,
                    "name": "",
                    "functionType": "Ethernet",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable', u'bootVlanId': None},
                },
                {
                    "id": 2,
                    "name": "",
                    "functionType": "Ethernet",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net11",
                    "boot": {u'priority': u'NotBootable', u'bootVlanId': None},
                },
                {
                    "id": 3,
                    "name": "",
                    "functionType": "Ethernet",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net12",
                    "boot": {u'priority': u'NotBootable', u'bootVlanId': None},
                },
                {
                    "id": 4,
                    "name": "",
                    "functionType": "FibreChannel",
                    "portId": "Mezz 1:1",
                    "requestedMbps": "16000",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable', u'bootVlanId': None},
                },
                {
                    "id": 5,
                    "name": "",
                    "functionType": "FibreChannel",
                    "portId": "Mezz 1:2",
                    "requestedMbps": "16000",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable', u'bootVlanId': None},
                },
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'CD', u'USB', u'HardDisk', u'PXE']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "forceInstallFirmware": False
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorNameType": "AutoGenerated",
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:dd8-shared",
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        }, {
                            "isEnabled": True,
                            "connectionId": 5,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ],
                },
            ]

        },
    }
]

expected_edit_server_profiles_from_spt = [
    {
        "uri": "SP:ENCL1Bay6",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 660 Gen10:1:HP Synergy 3830C 16G FC HBA:3:Synergy 3820C 10/20Gb CNA:4:Synergy 3830C 16G FC HBA:6:Synergy 3820C 10/20Gb CNA",
        "name": "ENCL1Bay6",
        "type": "ServerProfileV11",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "id": 1,
                    "name": "",
                    "functionType": "Ethernet",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "maximumMbps": 16000,
                    "name": "",
                    "portId": "Mezz 1:1",
                    "requestedMbps": "Auto",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": 16000,
                    "name": "",
                    "portId": "Mezz 1:2",
                    "requestedMbps": "Auto",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": ['CD', 'USB', 'HardDisk', 'PXE']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:dd8-shared",
                    "lunType": "Manual",
                    "lun": 1,
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:01:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:01:00:02:AC:01:D9:ED"
                                        }],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:02:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:02:00:02:AC:01:D9:ED"
                                        }],
                        },

                    ]
                }
            ]

        },
    },
    {
        "uri": "SP:ENCL1Bay8",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen10:1:Synergy 3830C 16G FC HBA:3:Synergy 3820C 10/20Gb CNA",
        "name": "ENCL1Bay8",
        "type": "ServerProfileV11",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "maximumMbps": 16000,
                    "name": "",
                    "portId": "Mezz 1:1",
                    "requestedMbps": "16000",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 2,
                    "maximumMbps": 16000,
                    "name": "",
                    "portId": "Mezz 1:2",
                    "requestedMbps": "16000",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable'},
                },
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": ['CD', 'USB', 'HardDisk', 'PXE']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:dd8-shared",
                    "lunType": "Manual",
                    "lun": 1,
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 1,
                            "targetSelector": "Auto",
                            "targets": [{
                                "name": "21:01:00:02:AC:01:D9:ED"
                            },
                                {
                                "name": "20:01:00:02:AC:01:D9:ED"
                            }],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:02:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:02:00:02:AC:01:D9:ED"
                                        }],
                        },

                    ]
                }
            ]

        },
    },
    {
        "uri": "SP:ENCL1Bay7",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9:1:Synergy 3530C 16G HBA:3:Synergy 3820C 10/20Gb CNA",
        "name": "ENCL1Bay7",
        "type": "ServerProfileV11",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net11",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net12",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": 16000,
                    "name": "",
                    "portId": "Mezz 1:1",
                    "requestedMbps": "16000",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 5,
                    "maximumMbps": 16000,
                    "name": "",
                    "portId": "Mezz 1:2",
                    "requestedMbps": "16000",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": ['CD', 'USB', 'HardDisk', 'PXE']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:dd8-shared",
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 5,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:02:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:02:00:02:AC:01:D9:ED"
                                        }],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:01:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:01:00:02:AC:01:D9:ED"
                                        }],
                        },

                    ]
                }
            ]

        },
    }
]

server_profiles_from_spt = [{'name': 'ENCL1Bay6', 'type': 'ServerProfileV11', 'serverHardwareUri': 'SH:MXQ718061G, bay 6', 'serverProfileTemplateUri': 'SPT:ISO-UI1Bay6-Template'},
                            {'name': 'ENCL1Bay7', 'type': 'ServerProfileV11', 'serverHardwareUri': 'SH:MXQ718061G, bay 7', 'serverProfileTemplateUri': 'SPT:ISO-UI1Bay7-Template'},
                            {'name': 'ENCL1Bay8', 'type': 'ServerProfileV11', 'serverHardwareUri': 'SH:MXQ718061G, bay 8', 'serverProfileTemplateUri': 'SPT:ISO-UI1Bay8-Template'}, ]

expected_server_profiles_from_spt = [
    {
        "uri": "SP:ENCL1Bay6",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 660 Gen10:1:HP Synergy 3830C 16G FC HBA:3:Synergy 3820C 10/20Gb CNA:4:Synergy 3830C 16G FC HBA:6:Synergy 3820C 10/20Gb CNA",
        "name": "ENCL1Bay6",
        "type": "ServerProfileV11",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "maximumMbps": 16000,
                    "name": "",
                    "portId": "Mezz 1:1",
                    "requestedMbps": "Auto",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": 16000,
                    "name": "",
                    "portId": "Mezz 1:2",
                    "requestedMbps": "Auto",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": ['CD', 'USB', 'HardDisk', 'PXE']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": [
            ]

        },
    },
    {
        "uri": "SP:ENCL1Bay7",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9:1:Synergy 3530C 16G HBA:3:Synergy 3820C 10/20Gb CNA",
        "name": "ENCL1Bay7",
        "type": "ServerProfileV11",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": ['CD', 'USB', 'HardDisk', 'PXE']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": [
            ]

        },
    },
    {
        "uri": "SP:ENCL1Bay8",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen10:1:Synergy 3830C 16G FC HBA:3:Synergy 3820C 10/20Gb CNA",
        "name": "ENCL1Bay8",
        "type": "ServerProfileV11",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "maximumMbps": 16000,
                    "name": "",
                    "portId": "Mezz 1:1",
                    "requestedMbps": "16000",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 2,
                    "maximumMbps": 16000,
                    "name": "",
                    "portId": "Mezz 1:2",
                    "requestedMbps": "16000",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": ['CD', 'USB', 'HardDisk', 'PXE']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": [
            ]

        },
    }
]

server_profiles = [
    {
        "name": "MXQ718061Hbay10",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061H, bay 10",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'CD']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": [
            ]

        },
    },
    {
        "name": "MXQ718061Gbay1",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061G, bay 1",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": [
            ]

        },
    },
    {
        "name": "MXQ718061Gbay3",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061G, bay 3",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "NS:netset1",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": [
            ]

        },
    },
    {
        "name": "MXQ718061Jbay4",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061J, bay 4",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'CD']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": [
            ]

        },
    },
    {
        "name": "MXQ718061Hbay4",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061H, bay 4",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "NS:netset1",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'CD']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": [
            ]

        },
    },
    {
        "name": "MXQ718061Jbay8",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061J, bay 8",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": [
            ]

        },
    },
    {
        "name": "MXQ718061Jbay7",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061J, bay 7",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": [
            ]

        },
    },
    {
        "name": "MXQ718061Hbay5",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061H, bay 5",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 6:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 6:2-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 6:2-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 6:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": [
            ]

        },
    },
    {
        "name": "MXQ718061Gbay4",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061G, bay 4",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": [
            ]

        },
    },
    {
        "name": "MXQ718061Gbay5",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061G, bay 5",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 6:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 6:1-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 6:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 6:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'CD']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": [
            ]

        },
    }
]
expected_server_profiles = [
    {
        "uri": "SP:MXQ718061Hbay10",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen10:1:HPE Smart Array P416ie-m SR G10:3:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ718061Hbay10",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061H, bay 10",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": ['CD', 'USB', 'HardDisk', 'PXE']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": [
            ]

        },
    },
    {
        "uri": "SP:MXQ718061Gbay1",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9:1:Synergy 3830C 16G FC HBA:3:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ718061Gbay1",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061G, bay 1",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": ['HardDisk', 'CD', 'USB', 'PXE']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": [
            ]

        },
    },
    {
        "uri": "SP:MXQ718061Gbay3",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9:1:Synergy 3830C 16G FC HBA:3:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ718061Gbay3",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061G, bay 3",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "NS:netset1",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": ['HardDisk', 'CD', 'USB', 'PXE']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": [
            ]

        },
    },
    {
        "uri": "SP:MXQ718061Jbay4",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9:3:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ718061Jbay4",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061J, bay 4",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": ['CD', 'USB', 'HardDisk', 'PXE']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": [
            ]

        },
    },
    {
        "uri": "SP:MXQ718061Hbay4",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9:1:Smart Array P542D Controller:3:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ718061Hbay4",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061H, bay 4",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "NS:netset1",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": ['CD', 'USB', 'HardDisk', 'PXE']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": [
            ]

        },
    },
    {
        "uri": "SP:MXQ718061Jbay8",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen10:3:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ718061Jbay8",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061J, bay 8",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": ['HardDisk', 'CD', 'USB', 'PXE']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": [
            ]

        },
    },
    {
        "uri": "SP:MXQ718061Jbay7",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9:3:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ718061Jbay7",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061J, bay 7",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk', 'CD', 'USB', 'PXE']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": [
            ]

        },
    },
    {
        "uri": "SP:MXQ718061Hbay5",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 680 Gen9:1:Smart Array P542D Controller:3:Synergy 3820C 10/20Gb CNA:4:Smart Array P542D Controller:6:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ718061Hbay5",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061H, bay 5",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 6:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 6:2-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 6:2-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 6:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk', 'CD', 'USB', 'PXE']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": [
            ]

        },
    },
    {
        "uri": "SP:MXQ718061Gbay4",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9:1:Synergy 3830C 16G FC HBA:3:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ718061Gbay4",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061G, bay 4",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk', 'CD', 'USB', 'PXE']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": [
            ]

        },
    },
    {
        "uri": "SP:MXQ718061Gbay5",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 660 Gen9:1:Synergy 3830C 16G FC HBA:3:Synergy 3820C 10/20Gb CNA:4:HP Synergy 3830C 16G FC HBA:6:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ718061Gbay5",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061G, bay 5",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 6:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 6:1-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 6:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 6:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": ['CD', 'USB', 'HardDisk', 'PXE']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": [
            ]

        },
    }
]

server_profile_with_storage = [
    {
        "name": "MXQ718061Gbay4",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061G, bay 4",
        "enclosureUri": "ENC:MXQ718061G",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 16000,
                    "name": "",
                    "portId": "Mezz 1:1",
                    "requestedMbps": "Auto",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 16000,
                    "name": "",
                    "portId": "Mezz 1:2",
                    "requestedMbps": "Auto",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'CD']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:dd8-tbird-1bay1priv",
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:ovstQR8-e1bay1-bfsDoNotDelFrom2",
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:dd8-shared",
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                }
            ]

        },
    },
    {
        "name": "MXQ718061Jbay7",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061J, bay 7",
        "enclosureUri": "ENC:MXQ718061J",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 5,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:dd8-tbird-3bay3priv",
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 5,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:ovstQR8-e3bay5-bfsDoNotDelFrom2",
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 5,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:dd8-shared",
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 5,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                }
            ]

        },
    },
    {
        "name": "MXQ718061Gbay6",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061G, bay 6",
        "enclosureUri": "ENC:MXQ718061G",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net11",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 16000,
                    "name": "",
                    "portId": "Mezz 1:1",
                    "requestedMbps": "16000",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 16000,
                    "name": "",
                    "portId": "Mezz 1:2",
                    "requestedMbps": "Auto",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'CD']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:dd8-tbird-1bay4priv",
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:ovstQR8-e1bay5-bfsDoNotDelFrom2",
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:dd8-shared",
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                }
            ]

        },
    },
    {
        "name": "MXQ718061Hbay4",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061H, bay 4",
        "enclosureUri": "ENC:MXQ718061H",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:netset1",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'CD']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:dd8-tbird-2bay4priv",
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:dd8-shared",
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                },
                {
                    "id": 4,
                    "volumeUri": "SVOL:ovstQR8-e2bay6-bfsDoNotDelFrom2",
                    "lunType": "Auto",
                    "lun": None,
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                }
            ]

        },
    },
    {
        "name": "MXQ718061Jbay8",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061J, bay 8",
        "enclosureUri": "ENC:MXQ718061J",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 6,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:dd8-tbird-3bay5priv",
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:ovstQR8-e3bay8-bfsDoNotDelFrom2",
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:dd8-shared",
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                }
            ]

        },
    },
    {
        "name": "MXQ718061Hbay5",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061H, bay 5",
        "enclosureUri": "ENC:MXQ718061H",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 6:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 6:2-b",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net11",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 6:2-c",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net12",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 6:1-d",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net13",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 5,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 6,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 2,
                    "volumeUri": "SVOL:dd8-tbird-2bay5priv",
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 5,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 6,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:dd8-shared",
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 5,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 6,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                },
                {
                    "id": 4,
                    "volumeUri": "SVOL:ovstQR8-e2bay5-bfsDoNotDelFrom2",
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 5,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 6,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                }
            ]

        },
    },
    {
        "name": "MXQ718061Gbay5",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061G, bay 5",
        "enclosureUri": "ENC:MXQ718061G",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net11",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 16000,
                    "name": "",
                    "portId": "Mezz 1:1",
                    "requestedMbps": "Auto",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 16000,
                    "name": "",
                    "portId": "Mezz 1:2",
                    "requestedMbps": "Auto",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'CD']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:dd8-tbird-1bay3priv",
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:ovstQR8-e1bay8-bfsDoNotDelFrom2",
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:dd8-shared",
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                }
            ]

        },
    },
    {
        "name": "MXQ718061Hbay10",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061H, bay 10",
        "enclosureUri": "ENC:MXQ718061H",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net13",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'CD']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:dd8-tbird-2bay1priv",
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:ovstQR8-e2bay10-bfsDoNotDelFrm2",
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:dd8-shared",
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                }
            ]

        },
    }
]
expected_server_profile_with_storage = [
    {
        "uri": "SP:MXQ718061Gbay4",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9:1:Synergy 3830C 16G FC HBA:3:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ718061Gbay4",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061G, bay 4",
        "enclosureUri": "ENC:MXQ718061G",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "maximumMbps": 16000,
                    "name": "",
                    "portId": "Mezz 1:1",
                    "requestedMbps": "Auto",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": 16000,
                    "name": "",
                    "portId": "Mezz 1:2",
                    "requestedMbps": "Auto",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": ['CD', 'USB', 'HardDisk', 'PXE']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:dd8-tbird-1bay1priv",
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:02:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:02:00:02:AC:01:D9:ED"
                                        }],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:01:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:01:00:02:AC:01:D9:ED"
                                        }],
                        },

                    ]
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:ovstQR8-e1bay1-bfsDoNotDelFrom2",
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:01:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:01:00:02:AC:01:D9:ED"
                                        }],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [{
                                "name": "21:02:00:02:AC:01:D9:ED"
                            },
                                {
                                "name": "20:02:00:02:AC:01:D9:ED"
                            }],
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:dd8-shared",
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:01:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:01:00:02:AC:01:D9:ED"
                                        }],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [{
                                "name": "21:02:00:02:AC:01:D9:ED"
                            },
                                {
                                "name": "20:02:00:02:AC:01:D9:ED"
                            }],
                        },

                    ]
                }
            ]

        },
    },
    {
        "uri": "SP:MXQ718061Jbay7",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9:3:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ718061Jbay7",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061J, bay 7",
        "enclosureUri": "ENC:MXQ718061J",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 5,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": ['CD', 'USB', 'HardDisk', 'PXE']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:dd8-tbird-3bay3priv",
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [{"name": "20:01:00:02:AC:01:D9:ED"}, {"name": "21:01:00:02:AC:01:D9:ED"}, ],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 5,
                            "targetSelector": "Auto",
                            "targets": [{"name": "20:02:00:02:AC:01:D9:ED"}, {"name": "21:02:00:02:AC:01:D9:ED"}],
                        },

                    ]
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:ovstQR8-e3bay5-bfsDoNotDelFrom2",
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [{"name": "20:01:00:02:AC:01:D9:ED"}, {"name": "21:01:00:02:AC:01:D9:ED"}],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 5,
                            "targetSelector": "Auto",
                            "targets": [{"name": "20:02:00:02:AC:01:D9:ED"}, {"name": "21:02:00:02:AC:01:D9:ED"}],
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:dd8-shared",
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 5,
                            "targetSelector": "Auto",
                            "targets": [{"name": "20:02:00:02:AC:01:D9:ED"}, {"name": "21:02:00:02:AC:01:D9:ED"}],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [{"name": "20:01:00:02:AC:01:D9:ED"}, {"name": "21:01:00:02:AC:01:D9:ED"}],
                        },

                    ]
                }
            ]

        },
    },
    {
        "uri": "SP:MXQ718061Gbay6",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 660 Gen10:1:HP Synergy 3830C 16G FC HBA:3:Synergy 3820C 10/20Gb CNA:4:Synergy 3830C 16G FC HBA:6:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ718061Gbay6",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061G, bay 6",
        "enclosureUri": "ENC:MXQ718061G",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net11",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "maximumMbps": 16000,
                    "name": "",
                    "portId": "Mezz 1:1",
                    "requestedMbps": "16000",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": 16000,
                    "name": "",
                    "portId": "Mezz 1:2",
                    "requestedMbps": "Auto",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": ['CD', 'USB', 'HardDisk', 'PXE']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:dd8-tbird-1bay4priv",
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [{
                                "name": "21:01:00:02:AC:01:D9:ED"
                            },
                                {
                                "name": "20:01:00:02:AC:01:D9:ED"
                            }],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:02:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:02:00:02:AC:01:D9:ED"
                                        }],
                        },

                    ]
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:ovstQR8-e1bay5-bfsDoNotDelFrom2",
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:01:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:01:00:02:AC:01:D9:ED"
                                        }],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [{
                                "name": "21:02:00:02:AC:01:D9:ED"
                            },
                                {
                                "name": "20:02:00:02:AC:01:D9:ED"
                            }],
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:dd8-shared",
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:01:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:01:00:02:AC:01:D9:ED"
                                        }],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [{
                                "name": "21:02:00:02:AC:01:D9:ED"
                            },
                                {
                                "name": "20:02:00:02:AC:01:D9:ED"
                            }],
                        },

                    ]
                }
            ]

        },
    },
    {
        "uri": "SP:MXQ718061Hbay4",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9:1:Smart Array P542D Controller:3:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ718061Hbay4",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061H, bay 4",
        "enclosureUri": "ENC:MXQ718061H",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:netset1",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": ['CD', 'USB', 'HardDisk', 'PXE']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:dd8-tbird-2bay4priv",
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:01:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:01:00:02:AC:01:D9:ED"
                                        }],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:02:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:02:00:02:AC:01:D9:ED"
                                        }],
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:dd8-shared",
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:01:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:01:00:02:AC:01:D9:ED"
                                        }],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:02:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:02:00:02:AC:01:D9:ED"
                                        }],
                        },

                    ]
                },
                {
                    "id": 4,
                    "volumeUri": "SVOL:ovstQR8-e2bay6-bfsDoNotDelFrom2",
                    "lunType": "Auto",
                    "lun": 2,
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:01:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:01:00:02:AC:01:D9:ED"
                                        }],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [{
                                "name": "21:02:00:02:AC:01:D9:ED"
                            },
                                {
                                "name": "20:02:00:02:AC:01:D9:ED"
                            }],
                        },

                    ]
                }
            ]

        },
    },
    {
        "uri": "SP:MXQ718061Jbay8",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen10:3:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ718061Jbay8",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061J, bay 8",
        "enclosureUri": "ENC:MXQ718061J",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 6,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": ['CD', 'USB', 'HardDisk', 'PXE']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:dd8-tbird-3bay5priv",
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [{
                                "name": "21:01:00:02:AC:01:D9:ED"
                            },
                                {
                                "name": "20:01:00:02:AC:01:D9:ED"
                            }],
                        },

                    ]
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:ovstQR8-e3bay8-bfsDoNotDelFrom2",
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:01:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:01:00:02:AC:01:D9:ED"
                                        }],
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:dd8-shared",
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:01:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:01:00:02:AC:01:D9:ED"
                                        }],
                        },

                    ]
                }
            ]

        },
    },
    {
        "uri": "SP:MXQ718061Hbay5",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 680 Gen9:1:Smart Array P542D Controller:3:Synergy 3820C 10/20Gb CNA:4:Smart Array P542D Controller:6:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ718061Hbay5",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061H, bay 5",
        "enclosureUri": "ENC:MXQ718061H",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 6:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 6:2-b",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net11",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 6:2-c",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net12",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 6:1-d",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net13",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 5,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 6,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": ['CD', 'USB', 'HardDisk', 'PXE']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 2,
                    "volumeUri": "SVOL:dd8-tbird-2bay5priv",
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 5,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:01:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:01:00:02:AC:01:D9:ED"
                                        }],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 6,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:02:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:02:00:02:AC:01:D9:ED"
                                        }],
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:dd8-shared",
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 5,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:01:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:01:00:02:AC:01:D9:ED"
                                        }],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 6,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:02:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:02:00:02:AC:01:D9:ED"
                                        }],
                        },

                    ]
                },
                {
                    "id": 4,
                    "volumeUri": "SVOL:ovstQR8-e2bay5-bfsDoNotDelFrom2",
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 5,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:01:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:01:00:02:AC:01:D9:ED"
                                        }],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 6,
                            "targetSelector": "Auto",
                            "targets": [{
                                "name": "21:02:00:02:AC:01:D9:ED"
                            },
                                {
                                "name": "20:02:00:02:AC:01:D9:ED"
                            }],
                        },

                    ]
                }
            ]

        },
    },
    {
        "uri": "SP:MXQ718061Gbay5",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 660 Gen9:1:Synergy 3830C 16G FC HBA:3:Synergy 3820C 10/20Gb CNA:4:HP Synergy 3830C 16G FC HBA:6:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ718061Gbay5",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061G, bay 5",
        "enclosureUri": "ENC:MXQ718061G",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net11",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "maximumMbps": 16000,
                    "name": "",
                    "portId": "Mezz 1:1",
                    "requestedMbps": "Auto",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": 16000,
                    "name": "",
                    "portId": "Mezz 1:2",
                    "requestedMbps": "Auto",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": ['CD', 'USB', 'HardDisk', 'PXE']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:dd8-tbird-1bay3priv",
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:02:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:02:00:02:AC:01:D9:ED"
                                        }],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [{
                                "name": "21:01:00:02:AC:01:D9:ED"
                            },
                                {
                                "name": "20:01:00:02:AC:01:D9:ED"
                            }],
                        },

                    ]
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:ovstQR8-e1bay8-bfsDoNotDelFrom2",
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [{
                                "name": "21:01:00:02:AC:01:D9:ED"
                            },
                                {
                                "name": "20:01:00:02:AC:01:D9:ED"
                            }],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [{
                                "name": "21:02:00:02:AC:01:D9:ED"
                            },
                                {
                                "name": "20:02:00:02:AC:01:D9:ED"
                            }],
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:dd8-shared",
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [{
                                "name": "21:01:00:02:AC:01:D9:ED"
                            },
                                {
                                "name": "20:01:00:02:AC:01:D9:ED"
                            }],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [{
                                "name": "21:02:00:02:AC:01:D9:ED"
                            },
                                {
                                "name": "20:02:00:02:AC:01:D9:ED"
                            }],
                        },

                    ]
                }
            ]

        },
    },
    {
        "uri": "SP:MXQ718061Hbay10",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen10:1:HPE Smart Array P416ie-m SR G10:3:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ718061Hbay10",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061H, bay 10",
        "enclosureUri": "ENC:MXQ718061H",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net13",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": ['CD', 'USB', 'HardDisk', 'PXE']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:dd8-tbird-2bay1priv",
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:02:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:02:00:02:AC:01:D9:ED"
                                        }],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [{
                                "name": "21:01:00:02:AC:01:D9:ED"
                            },
                                {
                                "name": "20:01:00:02:AC:01:D9:ED"
                            }],
                        },

                    ]
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:ovstQR8-e2bay10-bfsDoNotDelFrm2",
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [{
                                "name": "21:01:00:02:AC:01:D9:ED"
                            },
                                {
                                "name": "20:01:00:02:AC:01:D9:ED"
                            }],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:02:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:02:00:02:AC:01:D9:ED"
                                        }],
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:dd8-shared",
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [{
                                "name": "21:01:00:02:AC:01:D9:ED"
                            },
                                {
                                "name": "20:01:00:02:AC:01:D9:ED"
                            }],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:02:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:02:00:02:AC:01:D9:ED"
                                        }],
                        },

                    ]
                }
            ]

        },
    }
]

edit_server_profile_with_storage = [
    {
        "name": "MXQ718061Gbay4",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061G, bay 4",
        "enclosureUri": "ENC:MXQ718061G",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 16000,
                    "name": "",
                    "portId": "Mezz 1:1",
                    "requestedMbps": "Auto",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 16000,
                    "name": "",
                    "portId": "Mezz 1:2",
                    "requestedMbps": "Auto",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'CD']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:dd8-tbird-1bay1priv",
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:ovstQR8-e1bay1-bfsDoNotDelFrom2",
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:dd8-shared",
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                }
            ]

        },
    },
    {
        "name": "MXQ718061Jbay7",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061J, bay 7",
        "enclosureUri": "ENC:MXQ718061J",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 5,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:dd8-tbird-3bay3priv",
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 5,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:ovstQR8-e3bay5-bfsDoNotDelFrom2",
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 5,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:dd8-shared",
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 5,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                }
            ]

        },
    },
    {
        "name": "MXQ718061Gbay6",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061G, bay 6",
        "enclosureUri": "ENC:MXQ718061G",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net11",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 16000,
                    "name": "",
                    "portId": "Mezz 1:1",
                    "requestedMbps": "16000",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 16000,
                    "name": "",
                    "portId": "Mezz 1:2",
                    "requestedMbps": "Auto",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'CD']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:dd8-tbird-1bay4priv",
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:ovstQR8-e1bay5-bfsDoNotDelFrom2",
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:dd8-shared",
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                }
            ]

        },
    },
    {
        "name": "MXQ718061Hbay4",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061H, bay 4",
        "enclosureUri": "ENC:MXQ718061H",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:netset1",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'CD']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:dd8-tbird-2bay4priv",
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:dd8-shared",
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                },
                {
                    "id": 4,
                    "volumeUri": "SVOL:ovstQR8-e2bay6-bfsDoNotDelFrom2",
                    "lunType": "Auto",
                    "lun": None,
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                }
            ]

        },
    },
    {
        "name": "MXQ718061Jbay8",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061J, bay 8",
        "enclosureUri": "ENC:MXQ718061J",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 6,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:dd8-tbird-3bay5priv",
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:ovstQR8-e3bay8-bfsDoNotDelFrom2",
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:dd8-shared",
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                }
            ]

        },
    },
    {
        "name": "MXQ718061Hbay5",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061H, bay 5",
        "enclosureUri": "ENC:MXQ718061H",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 6:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 6:2-b",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net11",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 6:2-c",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net12",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 6:1-d",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net13",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 5,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 6,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 2,
                    "volumeUri": "SVOL:dd8-tbird-2bay5priv",
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 5,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 6,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:dd8-shared",
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 5,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 6,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                },
                {
                    "id": 4,
                    "volumeUri": "SVOL:ovstQR8-e2bay5-bfsDoNotDelFrom2",
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 5,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 6,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                }
            ]

        },
    },
    {
        "name": "MXQ718061Gbay5",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061G, bay 5",
        "enclosureUri": "ENC:MXQ718061G",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net11",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 16000,
                    "name": "",
                    "portId": "Mezz 1:1",
                    "requestedMbps": "Auto",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 16000,
                    "name": "",
                    "portId": "Mezz 1:2",
                    "requestedMbps": "Auto",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'CD']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:dd8-tbird-1bay3priv",
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:ovstQR8-e1bay8-bfsDoNotDelFrom2",
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:dd8-shared",
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                }
            ]

        },
    },
    {
        "name": "MXQ718061Hbay10",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061H, bay 10",
        "enclosureUri": "ENC:MXQ718061H",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net13",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'CD']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:dd8-tbird-2bay1priv",
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:ovstQR8-e2bay10-bfsDoNotDelFrm2",
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:dd8-shared",
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                }
            ]

        },
    }
]
expected_edit_server_profile_with_storage = [
    {
        "uri": "SP:MXQ718061Gbay4",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9:1:Synergy 3830C 16G FC HBA:3:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ718061Gbay4",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061G, bay 4",
        "enclosureUri": "ENC:MXQ718061G",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "maximumMbps": 16000,
                    "name": "",
                    "portId": "Mezz 1:1",
                    "requestedMbps": "Auto",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": 16000,
                    "name": "",
                    "portId": "Mezz 1:2",
                    "requestedMbps": "Auto",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": ['CD', 'USB', 'HardDisk', 'PXE']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:dd8-tbird-1bay1priv",
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:02:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:02:00:02:AC:01:D9:ED"
                                        }],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:01:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:01:00:02:AC:01:D9:ED"
                                        }],
                        },

                    ]
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:ovstQR8-e1bay1-bfsDoNotDelFrom2",
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:01:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:01:00:02:AC:01:D9:ED"
                                        }],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [{
                                "name": "21:02:00:02:AC:01:D9:ED"
                            },
                                {
                                "name": "20:02:00:02:AC:01:D9:ED"
                            }],
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:dd8-shared",
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:01:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:01:00:02:AC:01:D9:ED"
                                        }],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [{
                                "name": "21:02:00:02:AC:01:D9:ED"
                            },
                                {
                                "name": "20:02:00:02:AC:01:D9:ED"
                            }],
                        },

                    ]
                }
            ]

        },
    },
    {
        "uri": "SP:MXQ718061Jbay7",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9:3:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ718061Jbay7",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061J, bay 7",
        "enclosureUri": "ENC:MXQ718061J",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 5,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": ['CD', 'USB', 'HardDisk', 'PXE']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:dd8-tbird-3bay3priv",
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [{"name": "20:01:00:02:AC:01:D9:ED"}, {"name": "21:01:00:02:AC:01:D9:ED"}, ],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 5,
                            "targetSelector": "Auto",
                            "targets": [{"name": "20:02:00:02:AC:01:D9:ED"}, {"name": "21:02:00:02:AC:01:D9:ED"}],
                        },

                    ]
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:ovstQR8-e3bay5-bfsDoNotDelFrom2",
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [{"name": "20:01:00:02:AC:01:D9:ED"}, {"name": "21:01:00:02:AC:01:D9:ED"}],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 5,
                            "targetSelector": "Auto",
                            "targets": [{"name": "20:02:00:02:AC:01:D9:ED"}, {"name": "21:02:00:02:AC:01:D9:ED"}],
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:dd8-shared",
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 5,
                            "targetSelector": "Auto",
                            "targets": [{"name": "20:02:00:02:AC:01:D9:ED"}, {"name": "21:02:00:02:AC:01:D9:ED"}],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [{"name": "20:01:00:02:AC:01:D9:ED"}, {"name": "21:01:00:02:AC:01:D9:ED"}],
                        },

                    ]
                }
            ]

        },
    },
    {
        "uri": "SP:MXQ718061Gbay6",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 660 Gen10:1:HP Synergy 3830C 16G FC HBA:3:Synergy 3820C 10/20Gb CNA:4:Synergy 3830C 16G FC HBA:6:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ718061Gbay6",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061G, bay 6",
        "enclosureUri": "ENC:MXQ718061G",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net11",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "maximumMbps": 16000,
                    "name": "",
                    "portId": "Mezz 1:1",
                    "requestedMbps": "16000",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": 16000,
                    "name": "",
                    "portId": "Mezz 1:2",
                    "requestedMbps": "Auto",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": ['CD', 'USB', 'HardDisk', 'PXE']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:dd8-tbird-1bay4priv",
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [{
                                "name": "21:01:00:02:AC:01:D9:ED"
                            },
                                {
                                "name": "20:01:00:02:AC:01:D9:ED"
                            }],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:02:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:02:00:02:AC:01:D9:ED"
                                        }],
                        },

                    ]
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:ovstQR8-e1bay5-bfsDoNotDelFrom2",
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:01:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:01:00:02:AC:01:D9:ED"
                                        }],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [{
                                "name": "21:02:00:02:AC:01:D9:ED"
                            },
                                {
                                "name": "20:02:00:02:AC:01:D9:ED"
                            }],
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:dd8-shared",
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:01:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:01:00:02:AC:01:D9:ED"
                                        }],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [{
                                "name": "21:02:00:02:AC:01:D9:ED"
                            },
                                {
                                "name": "20:02:00:02:AC:01:D9:ED"
                            }],
                        },

                    ]
                }
            ]

        },
    },
    {
        "uri": "SP:MXQ718061Hbay4",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9:1:Smart Array P542D Controller:3:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ718061Hbay4",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061H, bay 4",
        "enclosureUri": "ENC:MXQ718061H",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:netset1",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": ['CD', 'USB', 'HardDisk', 'PXE']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:dd8-tbird-2bay4priv",
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:01:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:01:00:02:AC:01:D9:ED"
                                        }],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:02:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:02:00:02:AC:01:D9:ED"
                                        }],
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:dd8-shared",
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:01:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:01:00:02:AC:01:D9:ED"
                                        }],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:02:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:02:00:02:AC:01:D9:ED"
                                        }],
                        },

                    ]
                },
                {
                    "id": 4,
                    "volumeUri": "SVOL:ovstQR8-e2bay6-bfsDoNotDelFrom2",
                    "lunType": "Auto",
                    "lun": 2,
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:01:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:01:00:02:AC:01:D9:ED"
                                        }],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [{
                                "name": "21:02:00:02:AC:01:D9:ED"
                            },
                                {
                                "name": "20:02:00:02:AC:01:D9:ED"
                            }],
                        },

                    ]
                }
            ]

        },
    },
    {
        "uri": "SP:MXQ718061Jbay8",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen10:3:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ718061Jbay8",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061J, bay 8",
        "enclosureUri": "ENC:MXQ718061J",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 6,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": ['CD', 'USB', 'HardDisk', 'PXE']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:dd8-tbird-3bay5priv",
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [{
                                "name": "21:01:00:02:AC:01:D9:ED"
                            },
                                {
                                "name": "20:01:00:02:AC:01:D9:ED"
                            }],
                        },

                    ]
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:ovstQR8-e3bay8-bfsDoNotDelFrom2",
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:01:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:01:00:02:AC:01:D9:ED"
                                        }],
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:dd8-shared",
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:01:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:01:00:02:AC:01:D9:ED"
                                        }],
                        },

                    ]
                }
            ]

        },
    },
    {
        "uri": "SP:MXQ718061Hbay5",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 680 Gen9:1:Smart Array P542D Controller:3:Synergy 3820C 10/20Gb CNA:4:Smart Array P542D Controller:6:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ718061Hbay5",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061H, bay 5",
        "enclosureUri": "ENC:MXQ718061H",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 6:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 6:2-b",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net11",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 6:2-c",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net12",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 6:1-d",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net13",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 5,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 6,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": ['CD', 'USB', 'HardDisk', 'PXE']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 2,
                    "volumeUri": "SVOL:dd8-tbird-2bay5priv",
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 5,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:01:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:01:00:02:AC:01:D9:ED"
                                        }],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 6,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:02:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:02:00:02:AC:01:D9:ED"
                                        }],
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:dd8-shared",
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 5,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:01:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:01:00:02:AC:01:D9:ED"
                                        }],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 6,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:02:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:02:00:02:AC:01:D9:ED"
                                        }],
                        },

                    ]
                },
                {
                    "id": 4,
                    "volumeUri": "SVOL:ovstQR8-e2bay5-bfsDoNotDelFrom2",
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 5,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:01:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:01:00:02:AC:01:D9:ED"
                                        }],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 6,
                            "targetSelector": "Auto",
                            "targets": [{
                                "name": "21:02:00:02:AC:01:D9:ED"
                            },
                                {
                                "name": "20:02:00:02:AC:01:D9:ED"
                            }],
                        },

                    ]
                }
            ]

        },
    },
    {
        "uri": "SP:MXQ718061Gbay5",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 660 Gen9:1:Synergy 3830C 16G FC HBA:3:Synergy 3820C 10/20Gb CNA:4:HP Synergy 3830C 16G FC HBA:6:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ718061Gbay5",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061G, bay 5",
        "enclosureUri": "ENC:MXQ718061G",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net11",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "maximumMbps": 16000,
                    "name": "",
                    "portId": "Mezz 1:1",
                    "requestedMbps": "Auto",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": 16000,
                    "name": "",
                    "portId": "Mezz 1:2",
                    "requestedMbps": "Auto",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": ['CD', 'USB', 'HardDisk', 'PXE']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:dd8-tbird-1bay3priv",
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:02:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:02:00:02:AC:01:D9:ED"
                                        }],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [{
                                "name": "21:01:00:02:AC:01:D9:ED"
                            },
                                {
                                "name": "20:01:00:02:AC:01:D9:ED"
                            }],
                        },

                    ]
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:ovstQR8-e1bay8-bfsDoNotDelFrom2",
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [{
                                "name": "21:01:00:02:AC:01:D9:ED"
                            },
                                {
                                "name": "20:01:00:02:AC:01:D9:ED"
                            }],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [{
                                "name": "21:02:00:02:AC:01:D9:ED"
                            },
                                {
                                "name": "20:02:00:02:AC:01:D9:ED"
                            }],
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:dd8-shared",
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [{
                                "name": "21:01:00:02:AC:01:D9:ED"
                            },
                                {
                                "name": "20:01:00:02:AC:01:D9:ED"
                            }],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [{
                                "name": "21:02:00:02:AC:01:D9:ED"
                            },
                                {
                                "name": "20:02:00:02:AC:01:D9:ED"
                            }],
                        },

                    ]
                }
            ]

        },
    },
    {
        "uri": "SP:MXQ718061Hbay10",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen10:1:HPE Smart Array P416ie-m SR G10:3:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ718061Hbay10",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061H, bay 10",
        "enclosureUri": "ENC:MXQ718061H",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net13",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": ['CD', 'USB', 'HardDisk', 'PXE']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:dd8-tbird-2bay1priv",
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:02:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:02:00:02:AC:01:D9:ED"
                                        }],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [{
                                "name": "21:01:00:02:AC:01:D9:ED"
                            },
                                {
                                "name": "20:01:00:02:AC:01:D9:ED"
                            }],
                        },

                    ]
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:ovstQR8-e2bay10-bfsDoNotDelFrm2",
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [{
                                "name": "21:01:00:02:AC:01:D9:ED"
                            },
                                {
                                "name": "20:01:00:02:AC:01:D9:ED"
                            }],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:02:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:02:00:02:AC:01:D9:ED"
                                        }],
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:dd8-shared",
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [{
                                "name": "21:01:00:02:AC:01:D9:ED"
                            },
                                {
                                "name": "20:01:00:02:AC:01:D9:ED"
                            }],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:02:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:02:00:02:AC:01:D9:ED"
                                        }],
                        },

                    ]
                }
            ]

        },
    }
]

update_server_profile_with_storage = [
    {
        "name": "MXQ718061Gbay6",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061G, bay 6",
        "enclosureUri": "ENC:MXQ718061G",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 16000,
                    "name": "",
                    "portId": "Mezz 1:1",
                    "requestedMbps": "16000",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 16000,
                    "name": "",
                    "portId": "Mezz 1:2",
                    "requestedMbps": "Auto",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net12",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 6,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net13",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:dd8-tbird-1bay4priv",
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                }
            ]

        },
    },
    {
        "name": "MXQ718061Hbay4",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061H, bay 4",
        "enclosureUri": "ENC:MXQ718061H",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'CD']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:dd8-tbird-2bay4priv",
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                }
            ]

        },
    },
    {
        "name": "MXQ718061Gbay5",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061G, bay 5",
        "enclosureUri": "ENC:MXQ718061G",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 16000,
                    "name": "",
                    "portId": "Mezz 1:1",
                    "requestedMbps": "Auto",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 16000,
                    "name": "",
                    "portId": "Mezz 1:2",
                    "requestedMbps": "Auto",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net13",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'CD']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 2,
                    "volumeUri": "SVOL:ovstQR8-e1bay8-bfsDoNotDelFrom2",
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                },
                {
                    "id": 4,
                    "volumeUri": "SVOL:dd8-tbird-1bay2priv",
                    "lunType": "Auto",
                    "lun": None,
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                }
            ]

        },
    },
    {
        "name": "MXQ718061Hbay5",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061H, bay 5",
        "enclosureUri": "ENC:MXQ718061H",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 6:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 5,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 6,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 2,
                    "volumeUri": "SVOL:dd8-tbird-2bay5priv",
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 5,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 6,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:dd8-shared",
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 6,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 5,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                },
                {
                    "id": 4,
                    "volumeUri": "SVOL:ovstQR8-e2bay5-bfsDoNotDelFrom2",
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 5,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 6,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                },
                {
                    "id": 5,
                    "volumeUri": "SVOL:dd8-tbird-2bay2priv",
                    "lunType": "Manual",
                    "lun": "4",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 5,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 6,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                },
                {
                    "id": 6,
                    "volumeUri": "SVOL:ovstQR8-e2bay2-bfsDoNotDelFrom2",
                    "lunType": "Manual",
                    "lun": "6",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 5,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 6,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                }
            ]

        },
    },
    {
        "name": "MXQ718061Jbay8",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061J, bay 8",
        "enclosureUri": "ENC:MXQ718061J",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 6,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 7,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net11",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 8,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net12",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 9,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-c",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net13",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:dd8-tbird-3bay5priv",
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:ovstQR8-e3bay8-bfsDoNotDelFrom2",
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                },
                {
                    "id": 4,
                    "volumeUri": "SVOL:ovstQR8-e3bay2-bfsDoNotDelFrom2",
                    "lunType": "Manual",
                    "lun": "5",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 6,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                },
                {
                    "id": 5,
                    "volumeUri": "SVOL:ovstQR8-e2bay1-bfsDoNotDelFrom2",
                    "lunType": "Manual",
                    "lun": "6",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 6,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                }
            ]

        },
    },
    {
        "name": "MXQ718061Gbay4",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061G, bay 4",
        "enclosureUri": "ENC:MXQ718061G",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 16000,
                    "name": "",
                    "portId": "Mezz 1:1",
                    "requestedMbps": "Auto",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 16000,
                    "name": "",
                    "portId": "Mezz 1:2",
                    "requestedMbps": "Auto",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net11",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 6,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net12",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:dd8-tbird-1bay1priv",
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:dd8-shared",
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                }
            ]

        },
    },
    {
        "name": "MXQ718061Hbay10",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061H, bay 10",
        "enclosureUri": "ENC:MXQ718061H",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net13",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-c",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net11",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 6,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-d",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net12",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'CD']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 2,
                    "volumeUri": "SVOL:ovstQR8-e2bay10-bfsDoNotDelFrm2",
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                },
                {
                    "id": 4,
                    "volumeUri": "SVOL:ovstQR8-e2bay6-bfsDoNotDelFrom2",
                    "lunType": "Manual",
                    "lun": "4",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                }
            ]

        },
    },
    {
        "name": "MXQ718061Jbay7",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061J, bay 7",
        "enclosureUri": "ENC:MXQ718061J",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 5,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 6,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net11",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 7,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net12",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 8,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-c",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net13",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:dd8-tbird-3bay3priv",
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 5,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:ovstQR8-e3bay5-bfsDoNotDelFrom2",
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 5,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:dd8-shared",
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 5,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                },
                {
                    "id": 4,
                    "volumeUri": "SVOL:dd8-tbird-3bay2priv",
                    "lunType": "Manual",
                    "lun": "6",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 5,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                }
            ]

        },
    }
]
expected_update_server_profile_with_storage = [
    {
        "uri": "SP:MXQ718061Gbay6",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 660 Gen10:1:HP Synergy 3830C 16G FC HBA:3:Synergy 3820C 10/20Gb CNA:4:Synergy 3830C 16G FC HBA:6:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ718061Gbay6",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061G, bay 6",
        "enclosureUri": "ENC:MXQ718061G",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "maximumMbps": 16000,
                    "name": "",
                    "portId": "Mezz 1:1",
                    "requestedMbps": "16000",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": 16000,
                    "name": "",
                    "portId": "Mezz 1:2",
                    "requestedMbps": "Auto",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net12",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 6,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net13",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": ['CD', 'USB', 'HardDisk', 'PXE']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:dd8-tbird-1bay4priv",
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [{
                                "name": "21:01:00:02:AC:01:D9:ED"
                            },
                                {
                                "name": "20:01:00:02:AC:01:D9:ED"
                            }],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:02:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:02:00:02:AC:01:D9:ED"
                                        }],
                        },

                    ]
                }
            ]

        },
    },
    {
        "uri": "SP:MXQ718061Hbay4",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9:1:Smart Array P542D Controller:3:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ718061Hbay4",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061H, bay 4",
        "enclosureUri": "ENC:MXQ718061H",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": ['CD', 'USB', 'HardDisk', 'PXE']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:dd8-tbird-2bay4priv",
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:01:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:01:00:02:AC:01:D9:ED"
                                        }],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:02:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:02:00:02:AC:01:D9:ED"
                                        }],
                        },

                    ]
                }
            ]

        },
    },
    {
        "uri": "SP:MXQ718061Gbay5",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 660 Gen9:1:Synergy 3830C 16G FC HBA:3:Synergy 3820C 10/20Gb CNA:4:HP Synergy 3830C 16G FC HBA:6:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ718061Gbay5",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061G, bay 5",
        "enclosureUri": "ENC:MXQ718061G",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "maximumMbps": 16000,
                    "name": "",
                    "portId": "Mezz 1:1",
                    "requestedMbps": "Auto",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": 16000,
                    "name": "",
                    "portId": "Mezz 1:2",
                    "requestedMbps": "Auto",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net13",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": ['CD', 'USB', 'HardDisk', 'PXE']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 2,
                    "volumeUri": "SVOL:ovstQR8-e1bay8-bfsDoNotDelFrom2",
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [{
                                "name": "21:01:00:02:AC:01:D9:ED"
                            },
                                {
                                "name": "20:01:00:02:AC:01:D9:ED"
                            }],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:02:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:02:00:02:AC:01:D9:ED"
                                        }],
                        },

                    ]
                },
                {
                    "id": 4,
                    "volumeUri": "SVOL:dd8-tbird-1bay2priv",
                    "lunType": "Auto",
                    "lun": "4",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:01:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:01:00:02:AC:01:D9:ED"
                                        }],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:02:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:02:00:02:AC:01:D9:ED"
                                        }],
                        },

                    ]
                }
            ]

        },
    },
    {
        "uri": "SP:MXQ718061Hbay5",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 680 Gen9:1:Smart Array P542D Controller:3:Synergy 3820C 10/20Gb CNA:4:Smart Array P542D Controller:6:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ718061Hbay5",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061H, bay 5",
        "enclosureUri": "ENC:MXQ718061H",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 6:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 5,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 6,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": ['CD', 'USB', 'HardDisk', 'PXE']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 2,
                    "volumeUri": "SVOL:dd8-tbird-2bay5priv",
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 5,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:01:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:01:00:02:AC:01:D9:ED"
                                        }],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 6,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:02:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:02:00:02:AC:01:D9:ED"
                                        }],
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:dd8-shared",
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 6,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:02:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:02:00:02:AC:01:D9:ED"
                                        }],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 5,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:01:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:01:00:02:AC:01:D9:ED"
                                        }],
                        },

                    ]
                },
                {
                    "id": 4,
                    "volumeUri": "SVOL:ovstQR8-e2bay5-bfsDoNotDelFrom2",
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 5,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:01:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:01:00:02:AC:01:D9:ED"
                                        }],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 6,
                            "targetSelector": "Auto",
                            "targets": [{
                                "name": "21:02:00:02:AC:01:D9:ED"
                            },
                                {
                                "name": "20:02:00:02:AC:01:D9:ED"
                            }],
                        },

                    ]
                },
                {
                    "id": 5,
                    "volumeUri": "SVOL:dd8-tbird-2bay2priv",
                    "lunType": "Manual",
                    "lun": "4",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 5,
                            "targetSelector": "Auto",
                            "targets": [{
                                "name": "21:01:00:02:AC:01:D9:ED"
                            },
                                {
                                "name": "20:01:00:02:AC:01:D9:ED"
                            }],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 6,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:02:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:02:00:02:AC:01:D9:ED"
                                        }],
                        },

                    ]
                },
                {
                    "id": 6,
                    "volumeUri": "SVOL:ovstQR8-e2bay2-bfsDoNotDelFrom2",
                    "lunType": "Manual",
                    "lun": "6",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 5,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:01:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:01:00:02:AC:01:D9:ED"
                                        }],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 6,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:02:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:02:00:02:AC:01:D9:ED"
                                        }],
                        },

                    ]
                }
            ]

        },
    },
    {
        "uri": "SP:MXQ718061Jbay8",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen10:3:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ718061Jbay8",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061J, bay 8",
        "enclosureUri": "ENC:MXQ718061J",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 6,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 7,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net11",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 8,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net12",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 9,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-c",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net13",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": ['CD', 'USB', 'HardDisk', 'PXE']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:dd8-tbird-3bay5priv",
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:01:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:01:00:02:AC:01:D9:ED"
                                        }],
                        },

                    ]
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:ovstQR8-e3bay8-bfsDoNotDelFrom2",
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [{
                                "name": "21:01:00:02:AC:01:D9:ED"
                            },
                                {
                                "name": "20:01:00:02:AC:01:D9:ED"
                            }],
                        },

                    ]
                },
                {
                    "id": 4,
                    "volumeUri": "SVOL:ovstQR8-e3bay2-bfsDoNotDelFrom2",
                    "lunType": "Manual",
                    "lun": "5",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:01:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:01:00:02:AC:01:D9:ED"
                                        }],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 6,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:02:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:02:00:02:AC:01:D9:ED"
                                        }],
                        },

                    ]
                },
                {
                    "id": 5,
                    "volumeUri": "SVOL:ovstQR8-e2bay1-bfsDoNotDelFrom2",
                    "lunType": "Manual",
                    "lun": "6",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 6,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:02:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:02:00:02:AC:01:D9:ED"
                                        }],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:01:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:01:00:02:AC:01:D9:ED"
                                        }],
                        },

                    ]
                }
            ]

        },
    },
    {
        "uri": "SP:MXQ718061Gbay4",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9:1:Synergy 3830C 16G FC HBA:3:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ718061Gbay4",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061G, bay 4",
        "enclosureUri": "ENC:MXQ718061G",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "maximumMbps": 16000,
                    "name": "",
                    "portId": "Mezz 1:1",
                    "requestedMbps": "Auto",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": 16000,
                    "name": "",
                    "portId": "Mezz 1:2",
                    "requestedMbps": "Auto",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net11",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 6,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net12",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": ['CD', 'USB', 'HardDisk', 'PXE']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:dd8-tbird-1bay1priv",
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:01:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:01:00:02:AC:01:D9:ED"
                                        }],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:02:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:02:00:02:AC:01:D9:ED"
                                        }],
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:dd8-shared",
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:01:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:01:00:02:AC:01:D9:ED"
                                        }],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:02:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:02:00:02:AC:01:D9:ED"
                                        }],
                        },

                    ]
                }
            ]

        },
    },
    {
        "uri": "SP:MXQ718061Hbay10",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen10:1:HPE Smart Array P416ie-m SR G10:3:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ718061Hbay10",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061H, bay 10",
        "enclosureUri": "ENC:MXQ718061H",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net13",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-c",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net11",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 6,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-d",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net12",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": ['CD', 'USB', 'HardDisk', 'PXE']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 2,
                    "volumeUri": "SVOL:ovstQR8-e2bay10-bfsDoNotDelFrm2",
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [{
                                "name": "21:01:00:02:AC:01:D9:ED"
                            },
                                {
                                "name": "20:01:00:02:AC:01:D9:ED"
                            }],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:02:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:02:00:02:AC:01:D9:ED"
                                        }],
                        },

                    ]
                },
                {
                    "id": 4,
                    "volumeUri": "SVOL:ovstQR8-e2bay6-bfsDoNotDelFrom2",
                    "lunType": "Manual",
                    "lun": "4",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:01:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:01:00:02:AC:01:D9:ED"
                                        }],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:02:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:02:00:02:AC:01:D9:ED"
                                        }],
                        },

                    ]
                }
            ]

        },
    },
    {
        "uri": "SP:MXQ718061Jbay7",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9:3:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ718061Jbay7",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ718061J, bay 7",
        "enclosureUri": "ENC:MXQ718061J",
        "enclosureGroupUri": "EG:EG-Goose",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 5,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 6,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net11",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 7,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net12",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 8,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-c",
                    "networkUri": "ETH:net13",
                    "boot": {u'priority': u'NotBootable'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": ['CD', 'USB', 'HardDisk', 'PXE']
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:dd8-tbird-3bay3priv",
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:01:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:01:00:02:AC:01:D9:ED"
                                        }],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 5,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:02:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:02:00:02:AC:01:D9:ED"
                                        }],
                        },

                    ]
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:ovstQR8-e3bay5-bfsDoNotDelFrom2",
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 5,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:02:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:02:00:02:AC:01:D9:ED"
                                        }],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:01:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:01:00:02:AC:01:D9:ED"
                                        }],
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:dd8-shared",
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 5,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:02:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:02:00:02:AC:01:D9:ED"
                                        }],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [{
                                "name": "21:01:00:02:AC:01:D9:ED"
                            },
                                {
                                "name": "20:01:00:02:AC:01:D9:ED"
                            }],
                        },

                    ]
                },
                {
                    "id": 4,
                    "volumeUri": "SVOL:dd8-tbird-3bay2priv",
                    "lunType": "Manual",
                    "lun": "6",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:01:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:01:00:02:AC:01:D9:ED"
                                        }],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 5,
                            "targetSelector": "Auto",
                            "targets": [{
                                        "name": "21:02:00:02:AC:01:D9:ED"
                                        },
                                        {
                                        "name": "20:02:00:02:AC:01:D9:ED"
                                        }],
                        },

                    ]
                }
            ]

        },
    }
]

enclosures = [
    {
        "enclosureGroupUri": "EG:EG-Goose",
        "forceInstallFirmware": True,
        "licensingIntent": "NotApplicable"
    },
    {
        "enclosureGroupUri": "EG:EG-Goose",
        "forceInstallFirmware": True,
        "licensingIntent": "NotApplicable"
    },
    {
        "enclosureGroupUri": "EG:EG-Goose",
        "forceInstallFirmware": True,
        "licensingIntent": "NotApplicable"
    }
]

monitored_enclosures = [{'name': 'MXQ718061G', 'type': 'EnclosureV8', 'enclosureType': 'SY12000', 'serialNumber': 'MXQ718061G',
                         'refreshState': 'NotRefreshing', 'state': 'Monitored',
                         'deviceBays': [{'bayNumber': 1, 'devicePresence': 'Present'}, {'bayNumber': 2, 'devicePresence': 'Present'}, {'bayNumber': 3, 'devicePresence': 'Present'},
                                        {'bayNumber': 4, 'devicePresence': 'Present'}, {'bayNumber': 5, 'devicePresence': 'Present'}, {'bayNumber': 6, 'devicePresence': 'Present'},
                                        {'bayNumber': 7, 'devicePresence': 'Present'}, {'bayNumber': 8, 'devicePresence': 'Present'}, {'bayNumber': 9}, {'bayNumber': 10}, {'bayNumber': 11}, {'bayNumber': 12}],
                         'interconnectBays': [{'bayNumber': 1, 'bayPowerState': 'Unknown'}, {'bayNumber': 2, 'bayPowerState': 'Unknown'},
                                              {'bayNumber': 3, 'bayPowerState': 'Unknown'}, {'bayNumber': 4, 'bayPowerState': 'Unknown'},
                                              {'bayNumber': 5, 'bayPowerState': 'Unknown'}, {'bayNumber': 6, 'bayPowerState': 'Unknown'}],
                         'fanBays': [{'bayNumber': 1, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 2, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 3, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 4, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 5, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 6, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 7, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 8, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 9, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 10, 'status': 'OK', 'devicePresence': 'Present'}],
                         'powerSupplyBays': [{'bayNumber': 1, 'status': 'OK', 'devicePresence': 'Present'},
                                             {'bayNumber': 2, 'status': 'OK', 'devicePresence': 'Present'},
                                             {'bayNumber': 3, 'status': 'OK', 'devicePresence': 'Present'},
                                             {'bayNumber': 4, 'status': 'OK', 'devicePresence': 'Present'},
                                             {'bayNumber': 5, 'status': 'OK', 'devicePresence': 'Present'},
                                             {'bayNumber': 6, 'status': 'OK', 'devicePresence': 'Present'}],
                         'applianceBays': [{'bayNumber': 1, 'status': None, 'devicePresence': 'Absent'},
                                           {'bayNumber': 2, 'status': 'OK', 'devicePresence': 'Present'}],
                         'managerBays': [{'bayNumber': 1, 'status': 'OK', 'devicePresence': 'Present', 'mgmtPortStatus': 'OK'},
                                         {'bayNumber': 2, 'status': 'OK', 'devicePresence': 'Present', 'mgmtPortStatus': 'OK'}]},

                        {'name': 'MXQ718061H', 'type': 'EnclosureV8', 'enclosureType': 'SY12000', 'serialNumber': 'MXQ718061H',
                         'refreshState': 'NotRefreshing', 'state': 'Monitored',
                         'deviceBays': [{'bayNumber': 1, 'devicePresence': 'Present'}, {'bayNumber': 2}, {'bayNumber': 3, 'devicePresence': 'Present'},
                                        {'bayNumber': 4, 'devicePresence': 'Present'}, {'bayNumber': 5, 'devicePresence': 'Present'}, {'bayNumber': 6},
                                        {'bayNumber': 7, 'devicePresence': 'Present'}, {'bayNumber': 8, 'devicePresence': 'Present'}, {'bayNumber': 9, 'devicePresence': 'Present'},
                                        {'bayNumber': 10, 'devicePresence': 'Present'}, {'bayNumber': 11}, {'bayNumber': 12}],
                         'interconnectBays': [{'bayNumber': 1, 'bayPowerState': 'Unknown'}, {'bayNumber': 2, 'bayPowerState': 'Unknown'},
                                              {'bayNumber': 3, 'bayPowerState': 'Unknown'}, {'bayNumber': 4, 'bayPowerState': 'Unknown'},
                                              {'bayNumber': 5, 'bayPowerState': 'Unknown'}, {'bayNumber': 6, 'bayPowerState': 'Unknown'}],
                         'fanBays': [{'bayNumber': 1, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 2, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 3, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 4, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 5, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 6, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 7, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 8, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 9, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 10, 'status': 'OK', 'devicePresence': 'Present'}],
                         'powerSupplyBays': [{'bayNumber': 1, 'status': 'OK', 'devicePresence': 'Present'},
                                             {'bayNumber': 2, 'status': 'OK', 'devicePresence': 'Present'},
                                             {'bayNumber': 3, 'status': 'OK', 'devicePresence': 'Present'},
                                             {'bayNumber': 4, 'status': 'OK', 'devicePresence': 'Present'},
                                             {'bayNumber': 5, 'status': 'OK', 'devicePresence': 'Present'},
                                             {'bayNumber': 6, 'status': 'OK', 'devicePresence': 'Present'}],
                         'applianceBays': [{'bayNumber': 1, 'status': 'OK', 'devicePresence': 'Present'},
                                           {'bayNumber': 2, 'status': None, 'devicePresence': 'Absent'}],
                         'managerBays': [{'bayNumber': 1, 'status': 'OK', 'devicePresence': 'Present', 'mgmtPortStatus': 'OK'},
                                         {'bayNumber': 2, 'status': 'OK', 'devicePresence': 'Present', 'mgmtPortStatus': 'OK'}]},

                        {'name': 'MXQ718061J', 'type': 'EnclosureV8', 'enclosureType': 'SY12000', 'serialNumber': 'MXQ718061J',
                         'refreshState': 'NotRefreshing', 'state': 'Monitored',
                         'deviceBays': [{'bayNumber': 1, 'devicePresence': 'Present'}, {'bayNumber': 2, 'devicePresence': 'Present'}, {'bayNumber': 3, 'devicePresence': 'Present'},
                                        {'bayNumber': 4, 'devicePresence': 'Present'}, {'bayNumber': 5}, {'bayNumber': 6}, {'bayNumber': 7, 'devicePresence': 'Present'},
                                        {'bayNumber': 8, 'devicePresence': 'Present'}, {'bayNumber': 9}, {'bayNumber': 10}, {'bayNumber': 11}, {'bayNumber': 12}],
                         'interconnectBays': [{'bayNumber': 1, 'bayPowerState': 'Unknown'}, {'bayNumber': 2, 'bayPowerState': 'Unknown'},
                                              {'bayNumber': 3, 'bayPowerState': 'Unknown'}, {'bayNumber': 4, 'bayPowerState': 'Unknown'},
                                              {'bayNumber': 5, 'bayPowerState': 'Unknown'}, {'bayNumber': 6, 'bayPowerState': 'Unknown'}],
                         'fanBays': [{'bayNumber': 1, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 2, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 3, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 4, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 5, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 6, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 7, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 8, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 9, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 10, 'status': 'OK', 'devicePresence': 'Present'}],
                         'powerSupplyBays': [{'bayNumber': 1, 'status': 'OK', 'devicePresence': 'Present'},
                                             {'bayNumber': 2, 'status': 'OK', 'devicePresence': 'Present'},
                                             {'bayNumber': 3, 'status': 'OK', 'devicePresence': 'Present'},
                                             {'bayNumber': 4, 'status': 'OK', 'devicePresence': 'Present'},
                                             {'bayNumber': 5, 'status': 'OK', 'devicePresence': 'Present'},
                                             {'bayNumber': 6, 'status': 'OK', 'devicePresence': 'Present'}],
                         'applianceBays': [{'bayNumber': 1, 'status': None, 'devicePresence': 'Absent'},
                                           {'bayNumber': 2, 'status': None, 'devicePresence': 'Absent'}],
                         'managerBays': [{'bayNumber': 1, 'status': 'OK', 'devicePresence': 'Present', 'mgmtPortStatus': 'OK'},
                                         {'bayNumber': 2, 'status': 'OK', 'devicePresence': 'Present', 'mgmtPortStatus': 'OK'}]}]

configured_enclosures = [{'name': 'MXQ718061G', 'type': 'EnclosureV8', 'enclosureType': 'SY12000', 'serialNumber': 'MXQ718061G',
                          'refreshState': 'NotRefreshing', 'state': 'Configured',
                          'deviceBays': [{'bayNumber': 1, 'devicePresence': 'Present'}, {'bayNumber': 2, 'devicePresence': 'Present'}, {'bayNumber': 3, 'devicePresence': 'Present'},
                                         {'bayNumber': 4, 'devicePresence': 'Present'}, {'bayNumber': 5, 'devicePresence': 'Present'}, {'bayNumber': 6, 'devicePresence': 'Present'},
                                         {'bayNumber': 7, 'devicePresence': 'Present'}, {'bayNumber': 8, 'devicePresence': 'Present'}, {'bayNumber': 9}, {'bayNumber': 10}, {'bayNumber': 11}, {'bayNumber': 12}],
                          'interconnectBays': [{'bayNumber': 1, 'bayPowerState': 'Unknown'}, {'bayNumber': 2, 'bayPowerState': 'Unknown'},
                                               {'bayNumber': 3, 'bayPowerState': 'Unknown'}, {'bayNumber': 4, 'bayPowerState': 'Unknown'},
                                               {'bayNumber': 5, 'bayPowerState': 'Unknown'}, {'bayNumber': 6, 'bayPowerState': 'Unknown'}],
                          'fanBays': [{'bayNumber': 1, 'status': 'OK', 'devicePresence': 'Present'},
                                      {'bayNumber': 2, 'status': 'OK', 'devicePresence': 'Present'},
                                      {'bayNumber': 3, 'status': 'OK', 'devicePresence': 'Present'},
                                      {'bayNumber': 4, 'status': 'OK', 'devicePresence': 'Present'},
                                      {'bayNumber': 5, 'status': 'OK', 'devicePresence': 'Present'},
                                      {'bayNumber': 6, 'status': 'OK', 'devicePresence': 'Present'},
                                      {'bayNumber': 7, 'status': 'OK', 'devicePresence': 'Present'},
                                      {'bayNumber': 8, 'status': 'OK', 'devicePresence': 'Present'},
                                      {'bayNumber': 9, 'status': 'OK', 'devicePresence': 'Present'},
                                      {'bayNumber': 10, 'status': 'OK', 'devicePresence': 'Present'}],
                          'powerSupplyBays': [{'bayNumber': 1, 'status': 'OK', 'devicePresence': 'Present'},
                                              {'bayNumber': 2, 'status': 'OK', 'devicePresence': 'Present'},
                                              {'bayNumber': 3, 'status': 'OK', 'devicePresence': 'Present'},
                                              {'bayNumber': 4, 'status': 'OK', 'devicePresence': 'Present'},
                                              {'bayNumber': 5, 'status': 'OK', 'devicePresence': 'Present'},
                                              {'bayNumber': 6, 'status': 'OK', 'devicePresence': 'Present'}],
                          'applianceBays': [{'bayNumber': 1, 'status': None, 'devicePresence': 'Absent'},
                                            {'bayNumber': 2, 'status': 'OK', 'devicePresence': 'Present'}],
                          'managerBays': [{'bayNumber': 1, 'status': 'OK', 'devicePresence': 'Present', 'mgmtPortStatus': 'OK'},
                                          {'bayNumber': 2, 'status': 'OK', 'devicePresence': 'Present', 'mgmtPortStatus': 'OK'}]},

                         {'name': 'MXQ718061H', 'type': 'EnclosureV8', 'enclosureType': 'SY12000', 'serialNumber': 'MXQ718061H',
                          'refreshState': 'NotRefreshing', 'state': 'Configured',
                          'deviceBays': [{'bayNumber': 1, 'devicePresence': 'Present'}, {'bayNumber': 2}, {'bayNumber': 3, 'devicePresence': 'Present'},
                                         {'bayNumber': 4, 'devicePresence': 'Present'}, {'bayNumber': 5, 'devicePresence': 'Present'}, {'bayNumber': 6},
                                         {'bayNumber': 7, 'devicePresence': 'Present'}, {'bayNumber': 8, 'devicePresence': 'Present'}, {'bayNumber': 9, 'devicePresence': 'Present'},
                                         {'bayNumber': 10, 'devicePresence': 'Present'}, {'bayNumber': 11}, {'bayNumber': 12}],
                          'interconnectBays': [{'bayNumber': 1, 'bayPowerState': 'Unknown'}, {'bayNumber': 2, 'bayPowerState': 'Unknown'},
                                               {'bayNumber': 3, 'bayPowerState': 'Unknown'}, {'bayNumber': 4, 'bayPowerState': 'Unknown'},
                                               {'bayNumber': 5, 'bayPowerState': 'Unknown'}, {'bayNumber': 6, 'bayPowerState': 'Unknown'}],
                          'fanBays': [{'bayNumber': 1, 'status': 'OK', 'devicePresence': 'Present'},
                                      {'bayNumber': 2, 'status': 'OK', 'devicePresence': 'Present'},
                                      {'bayNumber': 3, 'status': 'OK', 'devicePresence': 'Present'},
                                      {'bayNumber': 4, 'status': 'OK', 'devicePresence': 'Present'},
                                      {'bayNumber': 5, 'status': 'OK', 'devicePresence': 'Present'},
                                      {'bayNumber': 6, 'status': 'OK', 'devicePresence': 'Present'},
                                      {'bayNumber': 7, 'status': 'OK', 'devicePresence': 'Present'},
                                      {'bayNumber': 8, 'status': 'OK', 'devicePresence': 'Present'},
                                      {'bayNumber': 9, 'status': 'OK', 'devicePresence': 'Present'},
                                      {'bayNumber': 10, 'status': 'OK', 'devicePresence': 'Present'}],
                          'powerSupplyBays': [{'bayNumber': 1, 'status': 'OK', 'devicePresence': 'Present'},
                                              {'bayNumber': 2, 'status': 'OK', 'devicePresence': 'Present'},
                                              {'bayNumber': 3, 'status': 'OK', 'devicePresence': 'Present'},
                                              {'bayNumber': 4, 'status': 'OK', 'devicePresence': 'Present'},
                                              {'bayNumber': 5, 'status': 'OK', 'devicePresence': 'Present'},
                                              {'bayNumber': 6, 'status': 'OK', 'devicePresence': 'Present'}],
                          'applianceBays': [{'bayNumber': 1, 'status': 'OK', 'devicePresence': 'Present'},
                                            {'bayNumber': 2, 'status': None, 'devicePresence': 'Absent'}],
                          'managerBays': [{'bayNumber': 1, 'status': 'OK', 'devicePresence': 'Present', 'mgmtPortStatus': 'OK'},
                                          {'bayNumber': 2, 'status': 'OK', 'devicePresence': 'Present', 'mgmtPortStatus': 'OK'}]},

                         {'name': 'MXQ718061J', 'type': 'EnclosureV8', 'enclosureType': 'SY12000', 'serialNumber': 'MXQ718061J',
                          'refreshState': 'NotRefreshing', 'state': 'Configured',
                          'deviceBays': [{'bayNumber': 1, 'devicePresence': 'Present'}, {'bayNumber': 2, 'devicePresence': 'Present'}, {'bayNumber': 3, 'devicePresence': 'Present'},
                                         {'bayNumber': 4, 'devicePresence': 'Present'}, {'bayNumber': 5}, {'bayNumber': 6}, {'bayNumber': 7, 'devicePresence': 'Present'},
                                         {'bayNumber': 8, 'devicePresence': 'Present'}, {'bayNumber': 9}, {'bayNumber': 10}, {'bayNumber': 11}, {'bayNumber': 12}],
                          'interconnectBays': [{'bayNumber': 1, 'bayPowerState': 'Unknown'}, {'bayNumber': 2, 'bayPowerState': 'Unknown'},
                                               {'bayNumber': 3, 'bayPowerState': 'Unknown'}, {'bayNumber': 4, 'bayPowerState': 'Unknown'},
                                               {'bayNumber': 5, 'bayPowerState': 'Unknown'}, {'bayNumber': 6, 'bayPowerState': 'Unknown'}],
                          'fanBays': [{'bayNumber': 1, 'status': 'OK', 'devicePresence': 'Present'},
                                      {'bayNumber': 2, 'status': 'OK', 'devicePresence': 'Present'},
                                      {'bayNumber': 3, 'status': 'OK', 'devicePresence': 'Present'},
                                      {'bayNumber': 4, 'status': 'OK', 'devicePresence': 'Present'},
                                      {'bayNumber': 5, 'status': 'OK', 'devicePresence': 'Present'},
                                      {'bayNumber': 6, 'status': 'OK', 'devicePresence': 'Present'},
                                      {'bayNumber': 7, 'status': 'OK', 'devicePresence': 'Present'},
                                      {'bayNumber': 8, 'status': 'OK', 'devicePresence': 'Present'},
                                      {'bayNumber': 9, 'status': 'OK', 'devicePresence': 'Present'},
                                      {'bayNumber': 10, 'status': 'OK', 'devicePresence': 'Present'}],
                          'powerSupplyBays': [{'bayNumber': 1, 'status': 'OK', 'devicePresence': 'Present'},
                                              {'bayNumber': 2, 'status': 'OK', 'devicePresence': 'Present'},
                                              {'bayNumber': 3, 'status': 'OK', 'devicePresence': 'Present'},
                                              {'bayNumber': 4, 'status': 'OK', 'devicePresence': 'Present'},
                                              {'bayNumber': 5, 'status': 'OK', 'devicePresence': 'Present'},
                                              {'bayNumber': 6, 'status': 'OK', 'devicePresence': 'Present'}],
                          'applianceBays': [{'bayNumber': 1, 'status': None, 'devicePresence': 'Absent'},
                                            {'bayNumber': 2, 'status': None, 'devicePresence': 'Absent'}],
                          'managerBays': [{'bayNumber': 1, 'status': 'OK', 'devicePresence': 'Present', 'mgmtPortStatus': 'OK'},
                                          {'bayNumber': 2, 'status': 'OK', 'devicePresence': 'Present', 'mgmtPortStatus': 'OK'}]}]

delete_storage_volumes_from_OV_only = [
    {'type': 'AddStorageVolumeV3', 'name': 'ovstQR8-e1bay1-bfsDoNotDelFrom2', 'description': '', 'storageSystemUri': 'ovst-3par-8400-03-srv', 'storageSystemVolumeName': 'ovstQR8-e1bay1-bfsDoNotDelFrom3', 'provisioningParameters': {'shareable': False}},
    {'type': 'AddStorageVolumeV3', 'name': 'ovstQR8-e1bay2-bfsDoNotDelFrom2', 'description': '', 'storageSystemUri': 'ovst-3par-8400-03-srv', 'storageSystemVolumeName': 'ovstQR8-e1bay2-bfsDoNotDelFrom3', 'provisioningParameters': {'shareable': False}},
    {'type': 'AddStorageVolumeV3', 'name': 'ovstQR8-e1bay5-bfsDoNotDelFrom2', 'description': '', 'storageSystemUri': 'ovst-3par-8400-03-srv', 'storageSystemVolumeName': 'ovstQR8-e1bay5-bfsDoNotDelFrom3', 'provisioningParameters': {'shareable': False}},
    {'type': 'AddStorageVolumeV3', 'name': 'ovstQR8-e1bay8-bfsDoNotDelFrom2', 'description': '', 'storageSystemUri': 'ovst-3par-8400-03-srv', 'storageSystemVolumeName': 'ovstQR8-e1bay8-bfsDoNotDelFrom3', 'provisioningParameters': {'shareable': False}},
    {'type': 'AddStorageVolumeV3', 'name': 'ovstQR8-e2bay1-bfsDoNotDelFrom2', 'description': '', 'storageSystemUri': 'ovst-3par-8400-03-srv', 'storageSystemVolumeName': 'ovstQR8-e2bay1-bfsDoNotDelFrom3', 'provisioningParameters': {'shareable': False}},
    {'type': 'AddStorageVolumeV3', 'name': 'ovstQR8-e2bay2-bfsDoNotDelFrom2', 'description': '', 'storageSystemUri': 'ovst-3par-8400-03-srv', 'storageSystemVolumeName': 'ovstQR8-e2bay2-bfsDoNotDelFrom3', 'provisioningParameters': {'shareable': False}},
    {'type': 'AddStorageVolumeV3', 'name': 'ovstQR8-e2bay5-bfsDoNotDelFrom2', 'description': '', 'storageSystemUri': 'ovst-3par-8400-03-srv', 'storageSystemVolumeName': 'ovstQR8-e2bay5-bfsDoNotDelFrom3', 'provisioningParameters': {'shareable': False}},
    {'type': 'AddStorageVolumeV3', 'name': 'ovstQR8-e2bay6-bfsDoNotDelFrom2', 'description': '', 'storageSystemUri': 'ovst-3par-8400-03-srv', 'storageSystemVolumeName': 'ovstQR8-e2bay6-bfsDoNotDelFrom3', 'provisioningParameters': {'shareable': False}},
    {'type': 'AddStorageVolumeV3', 'name': 'ovstQR8-e2bay10-bfsDoNotDelFrm2', 'description': '', 'storageSystemUri': 'ovst-3par-8400-03-srv', 'storageSystemVolumeName': 'ovstQR8-e2bay10-bfsDoNotDelFrom3', 'provisioningParameters': {'shareable': False}},
    {'type': 'AddStorageVolumeV3', 'name': 'ovstQR8-e3bay1-bfsDoNotDelFrom2', 'description': '', 'storageSystemUri': 'ovst-3par-8400-03-srv', 'storageSystemVolumeName': 'ovstQR8-e3bay1-bfsDoNotDelFrom3', 'provisioningParameters': {'shareable': False}},
    {'type': 'AddStorageVolumeV3', 'name': 'ovstQR8-e3bay2-bfsDoNotDelFrom2', 'description': '', 'storageSystemUri': 'ovst-3par-8400-03-srv', 'storageSystemVolumeName': 'ovstQR8-e3bay2-bfsDoNotDelFrom3', 'provisioningParameters': {'shareable': False}},
    {'type': 'AddStorageVolumeV3', 'name': 'ovstQR8-e3bay5-bfsDoNotDelFrom2', 'description': '', 'storageSystemUri': 'ovst-3par-8400-03-srv', 'storageSystemVolumeName': 'ovstQR8-e3bay5-bfsDoNotDelFrom3', 'provisioningParameters': {'shareable': False}},
    {'type': 'AddStorageVolumeV3', 'name': 'ovstQR8-e3bay8-bfsDoNotDelFrom2', 'description': '', 'storageSystemUri': 'ovst-3par-8400-03-srv', 'storageSystemVolumeName': 'ovstQR8-e3bay8-bfsDoNotDelFrom3', 'provisioningParameters': {'shareable': False}},
]

storage_volumes_to_delete = [{"name": "dd8-tbird-1bay1priv", "storageSystemVolumeName": "dd8-tbird-1bay1priv"},
                             {"name": "dd8-tbird-1bay2priv", "storageSystemVolumeName": "dd8-tbird-1bay2priv"},
                             {"name": "dd8-tbird-1bay3priv", "storageSystemVolumeName": "dd8-tbird-1bay3priv"},
                             {"name": "dd8-tbird-1bay4priv", "storageSystemVolumeName": "dd8-tbird-1bay4priv"},
                             {"name": "dd8-tbird-2bay1priv", "storageSystemVolumeName": "dd8-tbird-2bay1priv"},
                             {"name": "dd8-tbird-2bay2priv", "storageSystemVolumeName": "dd8-tbird-2bay2priv"},
                             {"name": "dd8-tbird-2bay3priv", "storageSystemVolumeName": "dd8-tbird-2bay3priv"},
                             {"name": "dd8-tbird-2bay4priv", "storageSystemVolumeName": "dd8-tbird-2bay4priv"},
                             {"name": "dd8-tbird-2bay5priv", "storageSystemVolumeName": "dd8-tbird-2bay5priv"},
                             {"name": "dd8-tbird-3bay1priv", "storageSystemVolumeName": "dd8-tbird-3bay1priv"},
                             {"name": "dd8-tbird-3bay2priv", "storageSystemVolumeName": "dd8-tbird-3bay2priv"},
                             {"name": "dd8-tbird-3bay3priv", "storageSystemVolumeName": "dd8-tbird-3bay3priv"},
                             {"name": "dd8-tbird-3bay4priv", "storageSystemVolumeName": "dd8-tbird-3bay4priv"},
                             {"name": "dd8-tbird-3bay5priv", "storageSystemVolumeName": "dd8-tbird-3bay5priv"},
                             {"name": "dd8-shared", "storageSystemVolumeName": "dd8-shared"}]

support_dump = [{"errorCode": "CI", "encrypt": False}]

le_support_dump = [{"name": "LE-Goose", "errorCode": "LESD1", "encrypt": True, "excludeApplianceDump": False}]
le_support_dump_with_profile = [{"name": "LE-Goose", "errorCode": "LESD1", "encrypt": True, "excludeApplianceDump": False}]

# Data for Cleanup Storage
storage_credentials = {'host': 'ovst-3par-8400-03-srv.vse.rdlabs.hpecorp.net', 'username': 'fusionadm', 'password': 'hpvse1'}

cleanup_hosts = [{'name': 'MXQ718061Gbay1'}, {'name': 'MXQ718061Gbay2'}, {'name': 'MXQ718061Hbay2'},
                 {'name': 'MXQ718061Hbay5'}, {'name': 'MXQ718061Gbay5'}, {'name': 'MXQ718061Hbay1'},
                 {'name': 'MXQ718061Jbay2'}, {'name': 'MXQ718061Jbay1'}, {'name': 'MXQ718061Jbay5'}]

cleanup_volumes = [{'name': 'dd8-tbird-1bay1priv'}, {'name': 'dd8-tbird-1bay2priv'}, {'name': 'dd8-tbird-1bay3priv'},
                   {'name': 'dd8-tbird-1bay4priv'}, {'name': 'dd8-tbird-2bay1priv'}, {'name': 'dd8-tbird-2bay2priv'},
                   {'name': 'dd8-tbird-2bay3priv'}, {'name': 'dd8-tbird-2bay4priv'}, {'name': 'dd8-tbird-2bay5priv'},
                   {'name': 'dd8-tbird-3bay1priv'}, {'name': 'dd8-tbird-3bay2priv'}, {'name': 'dd8-tbird-3bay3priv'},
                   {'name': 'dd8-tbird-3bay4priv'}, {'name': 'dd8-tbird-3bay5priv'}, {'name': 'dd8-shared'}]


remotesupport_edit = [{'op': 'replace', 'path': '/configuration/enableRemoteSupport', 'value': True},
                      {'op': 'replace', 'path': '/configuration/companyName', 'value': 'HPE'},
                      {'op': 'replace', 'path': '/configuration/marketingOptIn', 'value': True},
                      {"op": "replace", "path": "/configuration/autoEnableDevices", "value": True},
                      {'op': 'add', 'path': '/sites/default',
                       'value': {'name': 'DEFAULT SITE', 'streetAddress1': 'Compaq Center Dr', 'streetAddress2': '', 'city': 'Houston', 'provinceState': 'TX',
                                 'postalCode': '', 'timeZone': 'US/Central', 'countryCode': 'US', 'type': 'Site', 'default': True}},
                      {'op': 'add', 'path': '/contacts',
                       'value': {'contactKey': 'default', 'firstName': 'FFF', 'lastName': 'LLL', 'email': 'fff.ll@hpe.com', 'primaryPhone': '8884442222',
                                 'alternatePhone': '', 'notes': '', 'language': 'en', 'default': True, 'type': 'Contact'}}]

remotesupport_enable = [{'op': 'replace', 'path': '/configuration/enableRemoteSupport', 'value': True},
                        {"op": "replace", "path": "/configuration/autoEnableDevices", "value": True}]

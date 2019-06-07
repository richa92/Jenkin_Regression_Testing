"""
OneView SSH console Username and Password
"""
ONEVIEW_SSH_USERNAME = 'root'  # SSH UserName
ONEVIEW_SSH_PASSWORD = 'hpvse1'  # SSH Password

appliance = {
    'type': "ApplianceNetworkConfigurationV2",
    'applianceNetworks':
        [{
            "device": "bond0",
            "macAddress": "14:02:EC:46:01:D8",
            "interfaceName": "Appliance",
            "activeNode": 1,
            "unconfigure": False,
            "ipv4Type": "STATIC",
            "ipv4Subnet": "255.255.240.0",
            "ipv4Gateway": "16.114.208.1",
            "ipv4NameServers": [u'16.125.25.81', u'16.125.25.82'],
            "app1Ipv4Addr": "16.114.216.233",
            "ipv6Type": "UNCONFIGURE",
            "hostname": "ovst09-ov.vse.rdlabs.hpecorp.net",
            "confOneNode": False,
            "domainName": "",
            "aliasDisabled": False
        }
        ]}

admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}

"""
This is the time and locale settings used during FTS.
"""
timeandlocale = {
    'type': 'TimeAndLocale',
    'dateTime': None,
    'timezone': 'UTC',
    'ntpServers': ['ntp.hpecorp.net'],
    'locale': 'en_US.UTF-8'}

licenses = [
    {'key': 'ABAG AQEA H9PQ 8HV2 V7B5 HWWB Y9JL KMPL B89H MZVU DXAU 2CSM GHTG L762 DMF5 GRRM KJVT D5KM EFVW TSNJ XFU9 4ZSK E828 LFK6 FKA6 DU5N TZZX 9B5X 82Z5 WHEF D9ED 3RUX BJS2 XFXC T84U R42A 58S5 XA2D WXAP GMTQ 4YLB MM2S CZU7 2E4X E8UW BGB5 C324 SFUZ CMSB VNTJ ESB7 KVGR UNPC H4N5 NGHL 97D4 "EG3188881 KEY-E5Y35A#FUSION HP_OV_3yr_24x7_Supp_Phys_Flex_Lic ED4UATGCG2A9"_3JMZZ-RB9CN-DQD7H-CPB8P-M7WW2'},
    {'key': 'QCLG C9MA H9PQ 8HUZ U7B5 HWW5 Y9JL KMPL KRWA NBZY DXAU 2CSM GHTG L762 DNV7 GQFQ KJVT D5KM EFVW DT5J LFM8 76S8 C8SN YGSG Y8JC QUXV XZKH ABB4 NV2C LHXU VLXL HFMP J8TG 2VEB LK4U R6UF S7QS TRRL GX96 CMH4 6MPA M8LC KZU7 WE4X YN9X CDNB NT35 GH9J JGTJ QCV6 3EJF N975 "OV_NFR2 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR EY67ATGDTH6C"'},
]

users = [
    {
        "type": "UserAndPermissions",
        "password": "wpsthpvse1",
        "userName": "administrator",
        "permissions": [{u'roleName': u'Infrastructure administrator', u'scopeUri': None}],
        "emailAddress": "",
        "officePhone": "",
        "mobilePhone": "",

    },
    {
        "type": "UserAndPermissions",
        "password": "wpsthpvse1",
        "userName": "HardwareSetup",
        "permissions": [{u'roleName': u'Hardware setup', u'scopeUri': None}],
        "emailAddress": "",
        "officePhone": "",
        "mobilePhone": "",

    },
    {
        "type": "UserAndPermissions",
        "password": "wpsthpvse1",
        "userName": "appliance",
        "permissions": [{u'roleName': u'Infrastructure administrator', u'scopeUri': None}],
        "emailAddress": "appliance@hp.com",
        "officePhone": "970-898-2222",
        "mobilePhone": "970-898-0022",

    },
    {
        "type": "UserAndPermissions",
        "password": "wpsthpvse1",
        "userName": "network",
        "permissions": [{u'roleName': u'Network administrator', u'scopeUri': None}],
        "emailAddress": "network@hp.com",
        "officePhone": "970-555-0001",
        "mobilePhone": "970-555-0001",

    },
    {
        "type": "UserAndPermissions",
        "password": "wpsthpvse1",
        "userName": "readonly",
        "permissions": [{u'roleName': u'Read only', u'scopeUri': None}],
        "emailAddress": "readonly@hp.com",
        "officePhone": "970-666-1919",
        "mobilePhone": "970-666-1919",

    },
    {
        "type": "UserAndPermissions",
        "password": "wpsthpvse1",
        "userName": "server",
        "permissions": [{u'roleName': u'Server administrator', u'scopeUri': None}],
        "emailAddress": "server@hp.com",
        "officePhone": "970-555-0001",
        "mobilePhone": "970-555-0001",

    },
    {
        "type": "UserAndPermissions",
        "password": "wpsthpvse1",
        "userName": "storage",
        "permissions": [{u'roleName': u'Storage administrator', u'scopeUri': None}],
        "emailAddress": "storage@hp.com",
        "officePhone": "970-555-0001",
        "mobilePhone": "970-555-0001",

    }
]
expected_users = [
    {
        "uri": "/rest/users/administrator",
        "enabled": True,
        "type": "UserAndPermissions",
        "userName": "administrator",
        "permissions": [{u'roleName': u'Infrastructure administrator', u'scopeUri': None}],
        "emailAddress": "",
        "officePhone": "",
        "mobilePhone": "",
        "status": None
    },
    {
        "uri": "/rest/users/HardwareSetup",
        "enabled": True,
        "type": "UserAndPermissions",
        "userName": "HardwareSetup",
        "permissions": [{u'roleName': u'Hardware setup', u'scopeUri': None}],
        "emailAddress": "",
        "officePhone": "",
        "mobilePhone": "",
        "status": None
    },
    {
        "uri": "/rest/users/appliance",
        "enabled": True,
        "type": "UserAndPermissions",
        "userName": "appliance",
        "permissions": [{u'roleName': u'Infrastructure administrator', u'scopeUri': None}],
        "emailAddress": "appliance@hp.com",
        "officePhone": "970-898-2222",
        "mobilePhone": "970-898-0022",
        "status": None
    },
    {
        "uri": "/rest/users/network",
        "enabled": True,
        "type": "UserAndPermissions",
        "userName": "network",
        "permissions": [{u'roleName': u'Network administrator', u'scopeUri': None}],
        "emailAddress": "network@hp.com",
        "officePhone": "970-555-0001",
        "mobilePhone": "970-555-0001",
        "status": None
    },
    {
        "uri": "/rest/users/readonly",
        "enabled": True,
        "type": "UserAndPermissions",
        "userName": "readonly",
        "permissions": [{u'roleName': u'Read only', u'scopeUri': None}],
        "emailAddress": "readonly@hp.com",
        "officePhone": "970-666-1919",
        "mobilePhone": "970-666-1919",
        "status": None
    },
    {
        "uri": "/rest/users/server",
        "enabled": True,
        "type": "UserAndPermissions",
        "userName": "server",
        "permissions": [{u'roleName': u'Server administrator', u'scopeUri': None}],
        "emailAddress": "server@hp.com",
        "officePhone": "970-555-0001",
        "mobilePhone": "970-555-0001",
        "status": None
    },
    {
        "uri": "/rest/users/storage",
        "enabled": True,
        "type": "UserAndPermissions",
        "userName": "storage",
        "permissions": [{u'roleName': u'Storage administrator', u'scopeUri': None}],
        "emailAddress": "storage@hp.com",
        "officePhone": "970-555-0001",
        "mobilePhone": "970-555-0001",
        "status": None
    }
]

san_managers = [
    {
        "connectionInfo": [
            {
                "name": "Type",
                "value": "Brocade Network Advisor"
            },

            {
                "name": "Host",
                "value": "16.125.75.101"
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
        ],
    }
]
expected_san_managers = [
    {
        "uri": "SAN:16.125.75.101",
        "connectionInfo": [
            {
                "name": "Type",
                "value": "Brocade Network Advisor"
            },
            {
                "name": "Host",
                "value": "16.125.75.101"
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
        ],
        "status": "OK",
    }
]

ethernet_networks = [
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net22",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": False,
        "vlanId": 22,

    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net16",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": False,
        "vlanId": 16,

    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net24",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": False,
        "vlanId": 24,

    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net13",
        "privateNetwork": False,
        "purpose": "Management",
        "smartLink": False,
        "vlanId": 13,

    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net12",
        "privateNetwork": False,
        "purpose": "Management",
        "smartLink": False,
        "vlanId": 12,

    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net15",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": False,
        "vlanId": 15,

    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net19",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": False,
        "vlanId": 19,

    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net11",
        "privateNetwork": False,
        "purpose": "Management",
        "smartLink": False,
        "vlanId": 11,

    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net20",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": False,
        "vlanId": 20,

    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net300",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": False,
        "vlanId": 300,

    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net10",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": False,
        "vlanId": 10,

    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net21",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": False,
        "vlanId": 21,

    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net23",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": False,
        "vlanId": 23,

    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net14",
        "privateNetwork": False,
        "purpose": "Management",
        "smartLink": False,
        "vlanId": 14,

    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net17",
        "privateNetwork": False,
        "purpose": "VMMigration",
        "smartLink": False,
        "vlanId": 17,

    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net18",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": False,
        "vlanId": 18,

    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net25",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": False,
        "vlanId": 25,

    }
]
expected_ethernet_networks = [
    {
        "uri": "ETH:net22",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net22",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": False,
        "vlanId": 22,
        "status": "OK"
    },
    {
        "uri": "ETH:net16",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net16",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": False,
        "vlanId": 16,
        "status": "OK"
    },
    {
        "uri": "ETH:net24",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net24",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": False,
        "vlanId": 24,
        "status": "OK"
    },
    {
        "uri": "ETH:net13",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net13",
        "privateNetwork": False,
        "purpose": "Management",
        "smartLink": False,
        "vlanId": 13,
        "status": "OK"
    },
    {
        "uri": "ETH:net12",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net12",
        "privateNetwork": False,
        "purpose": "Management",
        "smartLink": False,
        "vlanId": 12,
        "status": "OK"
    },
    {
        "uri": "ETH:net15",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net15",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": False,
        "vlanId": 15,
        "status": "OK"
    },
    {
        "uri": "ETH:net19",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net19",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": False,
        "vlanId": 19,
        "status": "OK"
    },
    {
        "uri": "ETH:net11",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net11",
        "privateNetwork": False,
        "purpose": "Management",
        "smartLink": False,
        "vlanId": 11,
        "status": "OK"
    },
    {
        "uri": "ETH:net20",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net20",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": False,
        "vlanId": 20,
        "status": "OK"
    },
    {
        "uri": "ETH:net300",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net300",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": False,
        "vlanId": 300,
        "status": "OK"
    },
    {
        "uri": "ETH:net10",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net10",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": False,
        "vlanId": 10,
        "status": "OK"
    },
    {
        "uri": "ETH:net21",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net21",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": False,
        "vlanId": 21,
        "status": "OK"
    },
    {
        "uri": "ETH:net23",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net23",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": False,
        "vlanId": 23,
        "status": "OK"
    },
    {
        "uri": "ETH:net14",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net14",
        "privateNetwork": False,
        "purpose": "Management",
        "smartLink": False,
        "vlanId": 14,
        "status": "OK"
    },
    {
        "uri": "ETH:net17",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net17",
        "privateNetwork": False,
        "purpose": "VMMigration",
        "smartLink": False,
        "vlanId": 17,
        "status": "OK"
    },
    {
        "uri": "ETH:net18",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net18",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": False,
        "vlanId": 18,
        "status": "OK"
    },
    {
        "uri": "ETH:net25",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "net25",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": False,
        "vlanId": 25,
        "status": "OK"
    }
]

fc_networks = [
    {
        "type": "fc-networkV4",
        "name": "3par-a",
        "fabricType": "DirectAttach",
        "linkStabilityTime": 0,
        "autoLoginRedistribution": False,
        "managedSanUri": None,

    },
    {
        "type": "fc-networkV4",
        "name": "3par-b",
        "fabricType": "DirectAttach",
        "linkStabilityTime": 0,
        "autoLoginRedistribution": False,
        "managedSanUri": None,

    },
    {
        "type": "fc-networkV4",
        "name": "ovstsan216-240-mezz3-b",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:ovstsan216-240-b",

    },
    {
        "type": "fc-networkV4",
        "name": "ovstsan216-240-a",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:ovstsan216-240-a",

    },
    {
        "type": "fc-networkV4",
        "name": "ovstsan216-240-mezz1-b",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:ovstsan216-240-b",

    },
    {
        "type": "fc-networkV4",
        "name": "ovstsan216-240-lom-b",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:ovstsan216-240-b",

    },
    {
        "type": "fc-networkV4",
        "name": "ovstsan216-240-mezz1-a",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:ovstsan216-240-a",

    },
    {
        "type": "fc-networkV4",
        "name": "ovstsan216-240-mezz2-b",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:ovstsan216-240-b",

    },
    {
        "type": "fc-networkV4",
        "name": "ovstsan216-240-mezz2-a",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:ovstsan216-240-a",

    },
    {
        "type": "fc-networkV4",
        "name": "ovstsan216-240-b",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:ovstsan216-240-b",

    },
    {
        "type": "fc-networkV4",
        "name": "ovstsan216-240-mezz3-a",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:ovstsan216-240-a",

    },
    {
        "type": "fc-networkV4",
        "name": "ovstsan216-240-lom-a",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:ovstsan216-240-a",

    }
]
expected_fc_networks = [
    {
        "uri": "FC:3par-a",
        "type": "fc-networkV4",
        "name": "3par-a",
        "fabricType": "DirectAttach",
        "linkStabilityTime": 0,
        "autoLoginRedistribution": False,
        "managedSanUri": None,
        "status": "OK"
    },
    {
        "uri": "FC:3par-b",
        "type": "fc-networkV4",
        "name": "3par-b",
        "fabricType": "DirectAttach",
        "linkStabilityTime": 0,
        "autoLoginRedistribution": False,
        "managedSanUri": None,
        "status": "OK"
    },
    {
        "uri": "FC:ovstsan216-240-mezz3-b",
        "type": "fc-networkV4",
        "name": "ovstsan216-240-mezz3-b",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:ovstsan216-240-b",
        "status": "OK"
    },
    {
        "uri": "FC:ovstsan216-240-a",
        "type": "fc-networkV4",
        "name": "ovstsan216-240-a",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:ovstsan216-240-a",
        "status": "OK"
    },
    {
        "uri": "FC:ovstsan216-240-mezz1-b",
        "type": "fc-networkV4",
        "name": "ovstsan216-240-mezz1-b",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:ovstsan216-240-b",
        "status": "OK"
    },
    {
        "uri": "FC:ovstsan216-240-lom-b",
        "type": "fc-networkV4",
        "name": "ovstsan216-240-lom-b",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:ovstsan216-240-b",
        "status": "OK"
    },
    {
        "uri": "FC:ovstsan216-240-mezz1-a",
        "type": "fc-networkV4",
        "name": "ovstsan216-240-mezz1-a",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:ovstsan216-240-a",
        "status": "OK"
    },
    {
        "uri": "FC:ovstsan216-240-mezz2-b",
        "type": "fc-networkV4",
        "name": "ovstsan216-240-mezz2-b",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:ovstsan216-240-b",
        "status": "OK"
    },
    {
        "uri": "FC:ovstsan216-240-mezz2-a",
        "type": "fc-networkV4",
        "name": "ovstsan216-240-mezz2-a",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:ovstsan216-240-a",
        "status": "OK"
    },
    {
        "uri": "FC:ovstsan216-240-b",
        "type": "fc-networkV4",
        "name": "ovstsan216-240-b",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:ovstsan216-240-b",
        "status": "OK"
    },
    {
        "uri": "FC:ovstsan216-240-mezz3-a",
        "type": "fc-networkV4",
        "name": "ovstsan216-240-mezz3-a",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:ovstsan216-240-a",
        "status": "OK"
    },
    {
        "uri": "FC:ovstsan216-240-lom-a",
        "type": "fc-networkV4",
        "name": "ovstsan216-240-lom-a",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:ovstsan216-240-a",
        "status": "OK"
    }
]

fcoenets = [
]
expected_fcoenets = [
]

iscsi_networks = [{'name': 'iscsi28', 'vlanId': '28', 'purpose': 'ISCSI', 'smartLink': True, 'privateNetwork': False, 'ethernetNetworkType': 'Tagged', 'type': 'ethernet-networkV4'},
                  {'name': 'iscsi29', 'vlanId': '29', 'purpose': 'ISCSI', 'smartLink': True, 'privateNetwork': False, 'ethernetNetworkType': 'Tagged', 'type': 'ethernet-networkV4'}
                  ]
expected_iscsi_networks = [{'name': 'iscsi28', 'type': 'ethernet-networkV4', 'ethernetNetworkType': 'Tagged', 'vlanId': '28', 'smartLink': True, 'purpose': 'ISCSI', 'privateNetwork': False, 'subnetUri': None, 'description': None, 'status': 'OK', 'state': 'Active', 'category': 'ethernet-networks', 'uri': 'ETH:iscsi28'},
                           {'name': 'iscsi29', 'type': 'ethernet-networkV4', 'ethernetNetworkType': 'Tagged', 'vlanId': '29', 'smartLink': True, 'purpose': 'ISCSI', 'privateNetwork': False, 'subnetUri': None, 'description': None, 'status': 'OK', 'state': 'Active', 'category': 'ethernet-networks', 'uri': 'ETH:iscsi29'}]

networksets = [
    {
        "type": "network-setV5",
        "name": "netset2",
        "nativeNetworkUri": "net14",
        "networkUris": [
            "net17",
            "net16",
            "net14",
            "net15"
        ],

    },
    {
        "type": "network-setV5",
        "name": "netset1",
        "nativeNetworkUri": "net10",
        "networkUris": [
            "net10",
            "net12",
            "net11",
            "net13"
        ],

    },
    {
        "type": "network-setV5",
        "name": "netset4",
        "nativeNetworkUri": "net22",
        "networkUris": [
            "net23",
            "net25",
            "net24",
            "net22"
        ],

    },
    {
        "type": "network-setV5",
        "name": "netset3",
        "nativeNetworkUri": "net18",
        "networkUris": [
            "net21",
            "net18",
            "net20",
            "net19"
        ],

    }
]
expected_networksets = [
    {
        "uri": "NS:netset2",
        "type": "network-setV5",
        "name": "netset2",
        "nativeNetworkUri": "ETH:net14",
        "networkUris": [
            "ETH:net17",
            "ETH:net16",
            "ETH:net14",
            "ETH:net15"
        ],
        "status": "OK"
    },
    {
        "uri": "NS:netset1",
        "type": "network-setV5",
        "name": "netset1",
        "nativeNetworkUri": "ETH:net10",
        "networkUris": [
            "ETH:net10",
            "ETH:net12",
            "ETH:net11",
            "ETH:net13"
        ],
        "status": "OK"
    },
    {
        "uri": "NS:netset4",
        "type": "network-setV5",
        "name": "netset4",
        "nativeNetworkUri": "ETH:net22",
        "networkUris": [
            "ETH:net23",
            "ETH:net25",
            "ETH:net24",
            "ETH:net22"
        ],
        "status": "OK"
    },
    {
        "uri": "NS:netset3",
        "type": "network-setV5",
        "name": "netset3",
        "nativeNetworkUri": "ETH:net18",
        "networkUris": [
            "ETH:net21",
            "ETH:net18",
            "ETH:net20",
            "ETH:net19"
        ],
        "status": "OK"
    }
]

ligs = [
    {
        "name": "dd-Carbon-tmp",
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
        "interconnectMapTemplate": [
            {
                "enclosureIndex": -1,
                "bay": 1,
                "enclosure": -1,
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
        "snmpConfiguration": {
            "enabled": True,
            "readCommunity": "public",
            "snmpAccess": [],
            "systemContact": "",
            "trapDestinations": []
        },
        "uplinkSets": [
        ],
        "qosConfiguration": {
            "activeQosConfig": {u'status': None, u'category': u'qos-aggregated-configuration', u'name': None,
                                u'created': None, u'modified': None, u'uri': None, u'configType': u'Passthrough',
                                u'state': None, u'eTag': None, u'downlinkClassificationType': None,
                                u'uplinkClassificationType': None, u'qosTrafficClassifiers': [],
                                u'type': u'QosConfiguration', u'description': None},
            "inactiveFCoEQosConfig": None,
            "inactiveNonFCoEQosConfig": None,
            "name": None,
            "type": "qos-aggregated-configuration"
        },
        "enclosureIndexes": [-1]
    },
    {
        "name": "dd-Potash",
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
        "interconnectMapTemplate": [
            {
                "enclosureIndex": 3,
                "bay": 3,
                "enclosure": 3,
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
                "bay": 3,
                "type": "Synergy 20Gb Interconnect Link Module"
            },
            {
                "enclosureIndex": 2,
                "bay": 6,
                "enclosure": 2,
                "type": "Virtual Connect SE 40Gb F8 Module for Synergy"
            },
            {
                "enclosureIndex": 1,
                "bay": 6,
                "enclosure": 1,
                "type": "Synergy 20Gb Interconnect Link Module"
            },
            {
                "enclosureIndex": 1,
                "bay": 3,
                "enclosure": 1,
                "type": "Virtual Connect SE 40Gb F8 Module for Synergy"
            }

        ],
        "interconnectBaySet": 3,
        "redundancyType": "HighlyAvailable",
        "telemetryConfiguration": {
            "enableTelemetry": True,
            "sampleCount": 12,
            "sampleInterval": 300
        },
        "snmpConfiguration": {
            "enabled": True,
            "v3Enabled": True,
            "readCommunity": "public",
            "snmpAccess": [],
            "systemContact": "",
            "trapDestinations": [],
            "type": "snmp-configuration"
        },
        "uplinkSets": [
            {
                "ethernetNetworkType": "Tagged",
                "lacpTimer": "Short",
                "logicalPortConfigInfos": [
                    {
                        "speed": "Auto",
                        "port": "Q1.1",
                        "enclosure": "1",
                        "bay": "3"
                    },
                    {
                        "speed": "Auto",
                        "port": "Q1.1",
                        "enclosure": "2",
                        "bay": "6"
                    }
                ],
                "mode": "Auto",
                "name": "Ethernet",
                "nativeNetworkUri": None,
                "networkType": "Ethernet",
                "networkUris": [
                    "net13",
                    "net11",
                    "net12",
                    "net10"
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
                        "enclosure": "2",
                        "bay": "6"
                    }
                ],
                "mode": "Auto",
                "name": "FC-b",
                "nativeNetworkUri": None,
                "networkType": "FibreChannel",
                "networkUris": [
                    "ovstsan216-240-b"
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
                    "ovstsan216-240-a"
                ],
                "primaryPort": None
            }
        ],
        "qosConfiguration": {
            "activeQosConfig": {u'status': None, u'category': u'qos-aggregated-configuration', u'name': None,
                                u'created': None, u'modified': None, u'uri': None, u'configType': u'Passthrough',
                                u'state': None, u'eTag': None, u'downlinkClassificationType': None,
                                u'uplinkClassificationType': None, u'qosTrafficClassifiers': [],
                                u'type': u'QosConfiguration', u'description': None},
            "inactiveFCoEQosConfig": None,
            "inactiveNonFCoEQosConfig": None,
            "name": None,
            "type": "qos-aggregated-configuration"
        },
        "enclosureIndexes": [1, 2, 3]
    },
    {
        "name": "dd-Carbon",
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
        "interconnectMapTemplate": [
            {
                "enclosureIndex": -1,
                "bay": 4,
                "enclosure": -1,
                "type": "Virtual Connect SE 16Gb FC Module for Synergy"
            },
            {
                "enclosureIndex": -1,
                "bay": 1,
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
        "snmpConfiguration": {
            "enabled": True,
            "readCommunity": "public",
            "snmpAccess": [],
            "systemContact": "",
            "trapDestinations": []
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
                        "bay": "1"
                    }
                ],
                "mode": "Auto",
                "name": "FC-carbon-a",
                "nativeNetworkUri": None,
                "networkType": "FibreChannel",
                "networkUris": [
                    "ovstsan216-240-a"
                ],
                "primaryPort": None
            },
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
                "name": "FC-carbon-b",
                "nativeNetworkUri": None,
                "networkType": "FibreChannel",
                "networkUris": [
                    "ovstsan216-240-lom-b"
                ],
                "primaryPort": None
            }
        ],
        "qosConfiguration": {
            "activeQosConfig": {u'status': None, u'category': u'qos-aggregated-configuration', u'name': None,
                                u'created': None, u'modified': None, u'uri': None, u'configType': u'Passthrough',
                                u'state': None, u'eTag': None, u'downlinkClassificationType': None,
                                u'uplinkClassificationType': None, u'qosTrafficClassifiers': [],
                                u'type': u'QosConfiguration', u'description': None},
            "inactiveFCoEQosConfig": None,
            "inactiveNonFCoEQosConfig": None,
            "name": None,
            "type": "qos-aggregated-configuration"
        },
        "enclosureIndexes": [-1]
    }
]
expected_lig = [
    {
        "uri": "LIG:dd-Carbon-tmp",
        "status": None,
        "stackingHealth": None,
        "category": "logical-interconnect-groups",
        "state": "Active",
        "internalNetworkUris": "[]",
        "stackingMode": None,
        "description": None,
        "name": "dd-Carbon-tmp",
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
        "snmpConfiguration": {
            "enabled": True,
            "readCommunity": "public",
            "snmpAccess": [],
            "systemContact": "",
            "trapDestinations": []
        },
        "qosConfiguration": {
            "activeQosConfig": {u'status': None, u'category': u'qos-aggregated-configuration', u'name': None,
                                u'created': None, u'modified': None, u'uri': None, u'configType': u'Passthrough',
                                u'state': None, u'eTag': None, u'downlinkClassificationType': None,
                                u'uplinkClassificationType': None, u'qosTrafficClassifiers': [],
                                u'type': u'QosConfiguration', u'description': None},
            "inactiveFCoEQosConfig": None,
            "inactiveNonFCoEQosConfig": None,
            "name": None,
            "type": "qos-aggregated-configuration"
        },
        "enclosureIndexes": [-1]
    },
    {
        "uri": "LIG:dd-Potash",
        "status": None,
        "stackingHealth": None,
        "category": "logical-interconnect-groups",
        "state": "Active",
        "internalNetworkUris": "[]",
        "stackingMode": None,
        "description": None,
        "name": "dd-Potash",
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
        "snmpConfiguration": {
            "enabled": True,
            "v3Enabled": True,
            "readCommunity": "public",
            "snmpAccess": [],
            "systemContact": "",
            "trapDestinations": [],
            "type": "snmp-configuration"
        },
        "qosConfiguration": {
            "activeQosConfig": {u'status': None, u'category': u'qos-aggregated-configuration', u'name': None,
                                u'created': None, u'modified': None, u'uri': None, u'configType': u'Passthrough',
                                u'state': None, u'eTag': None, u'downlinkClassificationType': None,
                                u'uplinkClassificationType': None, u'qosTrafficClassifiers': [],
                                u'type': u'QosConfiguration', u'description': None},
            "inactiveFCoEQosConfig": None,
            "inactiveNonFCoEQosConfig": None,
            "name": None,
            "type": "qos-aggregated-configuration"
        },
        "enclosureIndexes": [1, 2, 3]
    },
    {
        "uri": "LIG:dd-Carbon",
        "status": None,
        "stackingHealth": None,
        "category": "logical-interconnect-groups",
        "state": "Active",
        "internalNetworkUris": "[]",
        "stackingMode": None,
        "description": None,
        "name": "dd-Carbon",
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
        "snmpConfiguration": {
            "enabled": True,
            "readCommunity": "public",
            "snmpAccess": [],
            "systemContact": "",
            "trapDestinations": []
        },
        "qosConfiguration": {
            "activeQosConfig": {u'status': None, u'category': u'qos-aggregated-configuration', u'name': None,
                                u'created': None, u'modified': None, u'uri': None, u'configType': u'Passthrough',
                                u'state': None, u'eTag': None, u'downlinkClassificationType': None,
                                u'uplinkClassificationType': None, u'qosTrafficClassifiers': [],
                                u'type': u'QosConfiguration', u'description': None},
            "inactiveFCoEQosConfig": None,
            "inactiveNonFCoEQosConfig": None,
            "name": None,
            "type": "qos-aggregated-configuration"
        },
        "enclosureIndexes": [-1]
    }
]

sas_lig = [
    {
        "name": "dd-Natasha",
        "type": "sas-logical-interconnect-groupV2",
        "enclosureType": "SY12000",
        "interconnectMapTemplate": [
            {
                "enclosureIndex": 1,
                "bay": 1,
                "enclosure": 1,
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
        "uri": "SASLIG:dd-Natasha",
        "status": "OK",
        "name": "dd-Natasha",
        "type": "sas-logical-interconnect-groupV2",
        "enclosureType": "SY12000",
        "interconnectBaySet": 1,
        "enclosureIndexes": [1]
    }
]

encgroups_add = [
    {
        "name": "dd-EG",
        "interconnectBayMappings": [
            {
                "interconnectBay": 1,
                "logicalInterconnectGroupUri": "LIG:dd-Carbon-tmp",
                "enclosureIndex": 1
            },
            {
                "interconnectBay": 1,
                "logicalInterconnectGroupUri": "SASLIG:dd-Natasha",
                "enclosureIndex": 2
            },
            {
                "interconnectBay": 3,
                "logicalInterconnectGroupUri": "LIG:dd-Potash",

            },
            {
                "interconnectBay": 4,
                "logicalInterconnectGroupUri": "LIG:dd-Carbon-tmp",
                "enclosureIndex": 1
            },
            {
                "interconnectBay": 4,
                "logicalInterconnectGroupUri": "SASLIG:dd-Natasha",
                "enclosureIndex": 2
            },
            {
                "interconnectBay": 6,
                "logicalInterconnectGroupUri": "LIG:dd-Potash",

            }
        ],
        "ipAddressingMode": "External",
        "enclosureCount": 3,
    }
]
expected_encgroups_add = [
    {
        "uri": "EG:dd-EG",
        "name": "dd-EG",
        "type": "EnclosureGroupV8",
        "enclosureTypeUri": "/rest/enclosure-types/SY12000",
        "stackingMode": "Enclosure",
        "interconnectBayMappingCount": "6",
        "interconnectBayMappings": [
            {
                "interconnectBay": 1,
                "logicalInterconnectGroupUri": "LIG:dd-Carbon-tmp",

            },
            {
                "interconnectBay": 1,
                "logicalInterconnectGroupUri": "SASLIG:dd-Natasha",

            },
            {
                "interconnectBay": 3,
                "logicalInterconnectGroupUri": "LIG:dd-Potash",

            },
            {
                "interconnectBay": 4,
                "logicalInterconnectGroupUri": "LIG:dd-Carbon-tmp",

            },
            {
                "interconnectBay": 4,
                "logicalInterconnectGroupUri": "SASLIG:dd-Natasha",

            },
            {
                "interconnectBay": 6,
                "logicalInterconnectGroupUri": "LIG:dd-Potash",

            }
        ],
        "ipAddressingMode": "External",
        "enclosureCount": 3,
        "status": "OK",
    }
]

storage_systems_with_pools = [
    {
        "credentials": {'username': 'fusionadm', 'password': 'hpvse1'},
        "name": "ovst-3par-8400-04-srv",
        "family": "StoreServ",
        "hostname": "ovst-3par-8400-04-srv.vse.rdlabs.hpecorp.net",
        "deviceSpecificAttributes": {
            "managedDomain": "ddRing9",
            "managedPools": [
                {'domain': 'ddRing9', 'name': 'FC_Hol_r1', 'raidLevel': 'RAID1', 'state': 'Managed', 'deviceType': 'FC',
                 'freeCapacity': '4545149140992', 'totalCapacity': '4599909974016',
                 'uuid': '00e28034-d3cc-4063-b028-9f688bcee098'},
                {'domain': 'ddRing9', 'name': 'FC_Hol_r5', 'raidLevel': 'RAID5', 'state': 'Managed', 'deviceType': 'FC',
                 'freeCapacity': '7564511150080', 'totalCapacity': '7616050757632',
                 'uuid': 'bee71ef8-2ff0-438d-81ec-d6ef9030474b'},
                {'domain': 'ddRing9', 'name': 'FC_Hol_r6', 'raidLevel': 'RAID6', 'state': 'Managed', 'deviceType': 'FC',
                 'freeCapacity': '6777458393088', 'totalCapacity': '6824703033344',
                 'uuid': '85f7c214-8bbe-496e-bc5d-da46f9579101'}],
            "discoveredPools": []
        },
    }
]
expected_storage_systems_with_pools = [
    {
        "uri": "SSYS:ovst-3par-8400-04-srv",
        "name": "ovst-3par-8400-04-srv",
        "family": "StoreServ",
        "hostname": "ovst-3par-8400-04-srv.vse.rdlabs.hpecorp.net",
        "deviceSpecificAttributes": {
            "managedDomain": "ddRing9",
        },
        "status": "OK"}
]

storage_pools_toedit = [
    {
        "storageSystemUri": "ovst-3par-8400-04-srv",
        "name": "FC_Hol_r1",
        "isManaged": True
    },
    {
        "storageSystemUri": "ovst-3par-8400-04-srv",
        "name": "FC_Hol_r5",
        "isManaged": True
    },
    {
        "storageSystemUri": "ovst-3par-8400-04-srv",
        "name": "FC_Hol_r6",
        "isManaged": True
    }
]

storage_volume_templates = [
    {
        "name": "iso-private-thin",
        "description": "private non-boot volume template",
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
                "default": "FC_Hol_r1",
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
                "default": "FC_Hol_r1",
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
        "uri": "SVT:iso-private-thin",
        "status": "OK",
        "name": "iso-private-thin",
        "description": "private non-boot volume template",
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
                "default": "FC_Hol_r1",
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
                "default": "FC_Hol_r1",
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
        "isPermanent": True,
        "properties": {
            "description": "shared volume",
            "isShareable": True,
            "name": "dd9-shared",
            "provisioningType": "Full",
            "size": 5368709120,
            "storagePool": "FC_Hol_r1"
        },
    },
    {
        "templateUri": "ROOT",
        "isPermanent": True,
        "properties": {
            "description": "non-boot private volume",
            "isShareable": False,
            "name": "dd9-tbird-1bay1priv",
            "provisioningType": "Full",
            "size": 5368709120,
            "storagePool": "FC_Hol_r1"
        },
    },
    {
        "templateUri": "ROOT",
        "isPermanent": True,
        "properties": {
            "description": "non-boot private volume",
            "isShareable": False,
            "name": "dd9-tbird-1bay2priv",
            "provisioningType": "Full",
            "size": 5368709120,
            "storagePool": "FC_Hol_r1"
        },
    },
    {
        "templateUri": "ROOT",
        "isPermanent": True,
        "properties": {
            "description": "non-boot private volume",
            "isShareable": False,
            "name": "dd9-tbird-1bay3priv",
            "provisioningType": "Full",
            "size": 5368709120,
            "storagePool": "FC_Hol_r1"
        },
    },
    {
        "templateUri": "ROOT",
        "isPermanent": True,
        "properties": {
            "description": "non-boot private volume",
            "isShareable": False,
            "name": "dd9-tbird-1bay4priv",
            "provisioningType": "Full",
            "size": 5368709120,
            "storagePool": "FC_Hol_r1"
        },
    },
    {
        "templateUri": "ROOT",
        "isPermanent": True,
        "properties": {
            "description": "non-boot private volume",
            "isShareable": False,
            "name": "dd9-tbird-2bay1priv",
            "provisioningType": "Full",
            "size": 5368709120,
            "storagePool": "FC_Hol_r1"
        },
    },
    {
        "templateUri": "ROOT",
        "isPermanent": True,
        "properties": {
            "description": "non-boot private volume",
            "isShareable": False,
            "name": "dd9-tbird-2bay2priv",
            "provisioningType": "Full",
            "size": 5368709120,
            "storagePool": "FC_Hol_r1"
        },
    },
    {
        "templateUri": "ROOT",
        "isPermanent": True,
        "properties": {
            "description": "non-boot private volume",
            "isShareable": False,
            "name": "dd9-tbird-2bay3priv",
            "provisioningType": "Full",
            "size": 5368709120,
            "storagePool": "FC_Hol_r1"
        },
    },
    {
        "templateUri": "ROOT",
        "isPermanent": True,
        "properties": {
            "description": "non-boot private volume",
            "isShareable": False,
            "name": "dd9-tbird-2bay4priv",
            "provisioningType": "Full",
            "size": 5368709120,
            "storagePool": "FC_Hol_r1"
        },
    },
    {
        "templateUri": "iso-private-thin",
        "isPermanent": True,
        "properties": {
            "description": "non-boot private volume",
            "isShareable": False,
            "name": "dd9-tbird-2bay5priv",
            "provisioningType": "Thin",
            "size": 5368709120,
            "storagePool": "FC_Hol_r1"
        },
    },
    {
        "templateUri": "iso-private-thin",
        "isPermanent": True,
        "properties": {
            "description": "non-boot private volume",
            "isShareable": False,
            "name": "dd9-tbird-3bay1priv",
            "provisioningType": "Thin",
            "size": 5368709120,
            "storagePool": "FC_Hol_r1"
        },
    },
    {
        "templateUri": "iso-private-thin",
        "isPermanent": True,
        "properties": {
            "description": "non-boot private volume",
            "isShareable": False,
            "name": "dd9-tbird-3bay2priv",
            "provisioningType": "Thin",
            "size": 5368709120,
            "storagePool": "FC_Hol_r1"
        },
    },
    {
        "templateUri": "iso-private-thin",
        "isPermanent": True,
        "properties": {
            "description": "non-boot private volume",
            "isShareable": False,
            "name": "dd9-tbird-3bay3priv",
            "provisioningType": "Thin",
            "size": 5368709120,
            "storagePool": "FC_Hol_r1"
        },
    },
    {
        "templateUri": "iso-private-thin",
        "isPermanent": True,
        "properties": {
            "description": "non-boot private volume",
            "isShareable": False,
            "name": "dd9-tbird-3bay4priv",
            "provisioningType": "Thin",
            "size": 5368709120,
            "storagePool": "FC_Hol_r1"
        },
    },
    {
        "templateUri": "iso-private-thin",
        "isPermanent": True,
        "properties": {
            "description": "non-boot private volume",
            "isShareable": False,
            "name": "dd9-tbird-3bay5priv",
            "provisioningType": "Thin",
            "size": 5368709120,
            "storagePool": "FC_Hol_r1"
        },
    }
]
expected_storage_volumes = [
    {'isShareable': True, 'name': 'dd9-shared', 'state': 'Managed', 'status': 'OK', 'storagePoolUri': 'SPOOL:FC_Hol_r1',
     'type': 'StorageVolumeV8'},
    {'isShareable': False, 'name': 'dd9-tbird-1bay1priv', 'state': 'Managed', 'status': 'OK',
     'storagePoolUri': 'SPOOL:FC_Hol_r1', 'type': 'StorageVolumeV8'},
    {'isShareable': False, 'name': 'dd9-tbird-1bay2priv', 'state': 'Managed', 'status': 'OK',
     'storagePoolUri': 'SPOOL:FC_Hol_r1', 'type': 'StorageVolumeV8'},
    {'isShareable': False, 'name': 'dd9-tbird-1bay3priv', 'state': 'Managed', 'status': 'OK',
     'storagePoolUri': 'SPOOL:FC_Hol_r1', 'type': 'StorageVolumeV8'},
    {'isShareable': False, 'name': 'dd9-tbird-1bay4priv', 'state': 'Managed', 'status': 'OK',
     'storagePoolUri': 'SPOOL:FC_Hol_r1', 'type': 'StorageVolumeV8'},
    {'isShareable': False, 'name': 'dd9-tbird-2bay1priv', 'state': 'Managed', 'status': 'OK',
     'storagePoolUri': 'SPOOL:FC_Hol_r1', 'type': 'StorageVolumeV8'},
    {'isShareable': False, 'name': 'dd9-tbird-2bay2priv', 'state': 'Managed', 'status': 'OK',
     'storagePoolUri': 'SPOOL:FC_Hol_r1', 'type': 'StorageVolumeV8'},
    {'isShareable': False, 'name': 'dd9-tbird-2bay3priv', 'state': 'Managed', 'status': 'OK',
     'storagePoolUri': 'SPOOL:FC_Hol_r1', 'type': 'StorageVolumeV8'},

    {'isShareable': False, 'name': 'dd9-tbird-2bay4priv', 'state': 'Managed', 'status': 'OK',
     'storagePoolUri': 'SPOOL:FC_Hol_r1', 'type': 'StorageVolumeV8'},
    {'isShareable': False, 'name': 'dd9-tbird-2bay5priv', 'state': 'Managed', 'status': 'OK',
     'storagePoolUri': 'SPOOL:FC_Hol_r1', 'type': 'StorageVolumeV8'},
    {'isShareable': False, 'name': 'dd9-tbird-3bay1priv', 'state': 'Managed', 'status': 'OK',
     'storagePoolUri': 'SPOOL:FC_Hol_r1', 'type': 'StorageVolumeV8'},
    {'isShareable': False, 'name': 'dd9-tbird-3bay2priv', 'state': 'Managed', 'status': 'OK',
     'storagePoolUri': 'SPOOL:FC_Hol_r1', 'type': 'StorageVolumeV8'},
    {'isShareable': False, 'name': 'dd9-tbird-3bay3priv', 'state': 'Managed', 'status': 'OK',
     'storagePoolUri': 'SPOOL:FC_Hol_r1', 'type': 'StorageVolumeV8'},
    {'isShareable': False, 'name': 'dd9-tbird-3bay4priv', 'state': 'Managed', 'status': 'OK',
     'storagePoolUri': 'SPOOL:FC_Hol_r1', 'type': 'StorageVolumeV8'},
    {'isShareable': False, 'name': 'dd9-tbird-3bay5priv', 'state': 'Managed', 'status': 'OK',
     'storagePoolUri': 'SPOOL:FC_Hol_r1', 'type': 'StorageVolumeV8'}]

add_existing_storage_volumes = [
    {
        "deviceVolumeName": "ovstQR9-e1bay1-bfsDoNotDelFrom3",
        "description": "Existing_Volume",
        "isShareable": False,
        "name": "ovstQR9-e1bay1-bfsDoNotDelFrom3",
        "storageSystemUri": "ovst-3par-8400-04-srv"
    },
    {
        "deviceVolumeName": "ovstQR9-e1bay2-bfsDoNotDelFrom3",
        "description": "Existing_Volume",
        "isShareable": False,
        "name": "ovstQR9-e1bay2-bfsDoNotDelFrom3",
        "storageSystemUri": "ovst-3par-8400-04-srv"
    },
    {
        "deviceVolumeName": "ovstQR9-e1bay8-bfsDoNotDelFrom3",
        "description": "Existing_Volume",
        "isShareable": False,
        "name": "ovstQR9-e1bay8-bfsDoNotDelFrom3",
        "storageSystemUri": "ovst-3par-8400-04-srv"
    },
    {
        "deviceVolumeName": "ovstQR9-e2bay1-bfsDoNotDelFrom3",
        "description": "Existing_Volume",
        "isShareable": False,
        "name": "ovstQR9-e2bay1-bfsDoNotDelFrom3",
        "storageSystemUri": "ovst-3par-8400-04-srv"
    },
    {
        "deviceVolumeName": "ovstQR9-e2bay2-bfsDoNotDelFrom3",
        "description": "Existing_Volume",
        "isShareable": False,
        "name": "ovstQR9-e2bay2-bfsDoNotDelFrom3",
        "storageSystemUri": "ovst-3par-8400-04-srv"
    },
    {
        "deviceVolumeName": "ovstQR9-e2bay10-bfsDoNotDelFrm3",
        "description": "Existing_Volume",
        "isShareable": False,
        "name": "ovstQR9-e2bay10-bfsDoNotDelFrm3",
        "storageSystemUri": "ovst-3par-8400-04-srv"
    },
    {
        "deviceVolumeName": "ovstQR9-e2bay5-bfsDoNotDelFrom3",
        "description": "Existing_Volume",
        "isShareable": False,
        "name": "ovstQR9-e2bay5-bfsDoNotDelFrom3",
        "storageSystemUri": "ovst-3par-8400-04-srv"
    },
    {
        "deviceVolumeName": "ovstQR9-e2bay6-bfsDoNotDelFrom3",
        "description": "Existing_Volume",
        "isShareable": False,
        "name": "ovstQR9-e2bay6-bfsDoNotDelFrom3",
        "storageSystemUri": "ovst-3par-8400-04-srv"
    },
    {
        "deviceVolumeName": "ovstQR9-e3bay1-bfsDoNotDelFrom3",
        "description": "Existing_Volume",
        "isShareable": False,
        "name": "ovstQR9-e3bay1-bfsDoNotDelFrom3",
        "storageSystemUri": "ovst-3par-8400-04-srv"
    },
    {
        "deviceVolumeName": "ovstQR9-e3bay2-bfsDoNotDelFrom3",
        "description": "Existing_Volume",
        "isShareable": False,
        "name": "ovstQR9-e3bay2-bfsDoNotDelFrom3",
        "storageSystemUri": "ovst-3par-8400-04-srv"
    },
    {
        "deviceVolumeName": "ovstQR9-e3bay5-bfsDoNotDelFrom3",
        "description": "Existing_Volume",
        "isShareable": False,
        "name": "ovstQR9-e3bay5-bfsDoNotDelFrom3",
        "storageSystemUri": "ovst-3par-8400-04-srv"
    },
    {
        "deviceVolumeName": "ovstQR9-e3bay8-bfsDoNotDelFrom3",
        "description": "Existing_Volume",
        "isShareable": False,
        "name": "ovstQR9-e3bay8-bfsDoNotDelFrom3",
        "storageSystemUri": "ovst-3par-8400-04-srv"
    },
    {
        "deviceVolumeName": "ovstQR9-e1bay5-bfsDoNotDelFrom3",
        "description": "Existing_Volume",
        "isShareable": False,
        "name": "ovstQR9-e1bay5-bfsDoNotDelFrom3",
        "storageSystemUri": "ovst-3par-8400-04-srv"
    }
]
expected_existing_storage_volumes = [
    {
        "status": "OK",
        "uri": "SVOL:ovstQR9-e1bay1-bfsDoNotDelFrom3",
        "deviceVolumeName": "ovstQR9-e1bay1-bfsDoNotDelFrom3",
        "description": "Existing_Volume",
        "isShareable": False,
        "name": "ovstQR9-e1bay1-bfsDoNotDelFrom3",
        "storagePoolUri": "SPOOL:FC_Hol_r1"
    },
    {
        "status": "OK",
        "uri": "SVOL:ovstQR9-e1bay2-bfsDoNotDelFrom3",
        "deviceVolumeName": "ovstQR9-e1bay2-bfsDoNotDelFrom3",
        "description": "Existing_Volume",
        "isShareable": False,
        "name": "ovstQR9-e1bay2-bfsDoNotDelFrom3",
        "storagePoolUri": "SPOOL:FC_Hol_r1"
    },
    {
        "status": "OK",
        "uri": "SVOL:ovstQR9-e1bay8-bfsDoNotDelFrom3",
        "deviceVolumeName": "ovstQR9-e1bay8-bfsDoNotDelFrom3",
        "description": "Existing_Volume",
        "isShareable": False,
        "name": "ovstQR9-e1bay8-bfsDoNotDelFrom3",
        "storagePoolUri": "SPOOL:FC_Hol_r1"
    },
    {
        "status": "OK",
        "uri": "SVOL:ovstQR9-e2bay1-bfsDoNotDelFrom3",
        "deviceVolumeName": "ovstQR9-e2bay1-bfsDoNotDelFrom3",
        "description": "Existing_Volume",
        "isShareable": False,
        "name": "ovstQR9-e2bay1-bfsDoNotDelFrom3",
        "storagePoolUri": "SPOOL:FC_Hol_r5"
    },
    {
        "status": "OK",
        "uri": "SVOL:ovstQR9-e2bay2-bfsDoNotDelFrom3",
        "deviceVolumeName": "ovstQR9-e2bay2-bfsDoNotDelFrom3",
        "description": "Existing_Volume",
        "isShareable": False,
        "name": "ovstQR9-e2bay2-bfsDoNotDelFrom3",
        "storagePoolUri": "SPOOL:FC_Hol_r5"
    },
    {
        "status": "OK",
        "uri": "SVOL:ovstQR9-e2bay10-bfsDoNotDelFrm3",
        "deviceVolumeName": "ovstQR9-e2bay10-bfsDoNotDelFrm3",
        "description": "Existing_Volume",
        "isShareable": False,
        "name": "ovstQR9-e2bay10-bfsDoNotDelFrm3",
        "storagePoolUri": "SPOOL:FC_Hol_r5"
    },
    {
        "status": "OK",
        "uri": "SVOL:ovstQR9-e2bay5-bfsDoNotDelFrom3",
        "deviceVolumeName": "ovstQR9-e2bay5-bfsDoNotDelFrom3",
        "description": "Existing_Volume",
        "isShareable": False,
        "name": "ovstQR9-e2bay5-bfsDoNotDelFrom3",
        "storagePoolUri": "SPOOL:FC_Hol_r5"
    },
    {
        "status": "OK",
        "uri": "SVOL:ovstQR9-e2bay6-bfsDoNotDelFrom3",
        "deviceVolumeName": "ovstQR9-e2bay6-bfsDoNotDelFrom3",
        "description": "Existing_Volume",
        "isShareable": False,
        "name": "ovstQR9-e2bay6-bfsDoNotDelFrom3",
        "storagePoolUri": "SPOOL:FC_Hol_r5"
    },
    {
        "status": "OK",
        "uri": "SVOL:ovstQR9-e3bay1-bfsDoNotDelFrom3",
        "deviceVolumeName": "ovstQR9-e3bay1-bfsDoNotDelFrom3",
        "description": "Existing_Volume",
        "isShareable": False,
        "name": "ovstQR9-e3bay1-bfsDoNotDelFrom3",
        "storagePoolUri": "SPOOL:FC_Hol_r6"
    },
    {
        "status": "OK",
        "uri": "SVOL:ovstQR9-e3bay2-bfsDoNotDelFrom3",
        "deviceVolumeName": "ovstQR9-e3bay2-bfsDoNotDelFrom3",
        "description": "Existing_Volume",
        "isShareable": False,
        "name": "ovstQR9-e3bay2-bfsDoNotDelFrom3",
        "storagePoolUri": "SPOOL:FC_Hol_r6"
    },
    {
        "status": "OK",
        "uri": "SVOL:ovstQR9-e3bay5-bfsDoNotDelFrom3",
        "deviceVolumeName": "ovstQR9-e3bay5-bfsDoNotDelFrom3",
        "description": "Existing_Volume",
        "isShareable": False,
        "name": "ovstQR9-e3bay5-bfsDoNotDelFrom3",
        "storagePoolUri": "SPOOL:FC_Hol_r6"
    },
    {
        "status": "OK",
        "uri": "SVOL:ovstQR9-e3bay8-bfsDoNotDelFrom3",
        "deviceVolumeName": "ovstQR9-e3bay8-bfsDoNotDelFrom3",
        "description": "Existing_Volume",
        "isShareable": False,
        "name": "ovstQR9-e3bay8-bfsDoNotDelFrom3",
        "storagePoolUri": "SPOOL:FC_Hol_r6"
    },
    {
        "status": "OK",
        "uri": "SVOL:ovstQR9-e1bay5-bfsDoNotDelFrom3",
        "deviceVolumeName": "ovstQR9-e1bay5-bfsDoNotDelFrom3",
        "description": "Existing_Volume",
        "isShareable": False,
        "name": "ovstQR9-e1bay5-bfsDoNotDelFrom3",
        "storagePoolUri": "SPOOL:FC_Hol_r1"
    }
]

logical_enclosure = [
    {
        "name": "ISOLIG_3EncICM",
        "enclosureUris": [
            "ENC:MXQ73705W4",
            "ENC:MXQ73705WF",
            "ENC:MXQ73708NK"
        ],
        "enclosureGroupUri": "EG:dd-EG"
    }
]
expected_logical_enclosure = [
    {
        "uri": "ISOLIG_3EncICM",
        "status": "OK",
        "name": "ISOLIG_3EncICM",
        "enclosureUris": [
            "ENC:MXQ73705W4",
            "ENC:MXQ73705WF",
            "ENC:MXQ73708NK"
        ],
        "enclosureGroupUri": "EG:dd-EG"
    }
]

server_profiles = [
    {
        "name": "MXQ73705W4, bay 8",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705W4, bay 8",
        "enclosureUri": "ENC:MXQ73705W4",
        "enclosureGroupUri": "EG:dd-EG",
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
                    "mac": "7A:74:BB:A0:00:14",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "7A:74:BB:A0:00:15",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "7A:74:BB:A0:00:16",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "7A:74:BB:A0:00:17",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13"
                }
            ]
        },
        "boot": {
            "manageBoot": False,
            "order": []
        },
        "bootMode": {
            "manageMode": True,
            "pxeBootPolicy": "IPv4",
            "mode": "UEFI"
        },
        "firmware": {
            "forceInstallFirmware": False,
            "firmwareActivationType": None,
            "firmwareScheduleDateTime": None,
            "firmwareBaselineUri": None,
            "manageFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "overriddenSettings": [],
            "manageBios": False
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "controllers": [],
            "sasLogicalJBODs": []
        },
    },
    {
        "name": "MXQ73705WF, bay 8",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705WF, bay 8",
        "enclosureUri": "ENC:MXQ73705WF",
        "enclosureGroupUri": "EG:dd-EG",
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
                    "mac": "7A:74:BB:A0:00:28",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "7A:74:BB:A0:00:29",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "7A:74:BB:A0:00:2A",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "7A:74:BB:A0:00:2B",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13"
                }
            ]
        },
        "boot": {
            "manageBoot": False,
            "order": []
        },
        "bootMode": {
            "manageMode": True,
            "pxeBootPolicy": "IPv4",
            "mode": "UEFI"
        },
        "firmware": {
            "forceInstallFirmware": False,
            "firmwareActivationType": None,
            "firmwareScheduleDateTime": None,
            "firmwareBaselineUri": None,
            "manageFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "overriddenSettings": [],
            "manageBios": False
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "controllers": [],
            "sasLogicalJBODs": []
        },
    },
    {
        "name": "MXQ73705W4, bay 7",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705W4, bay 7",
        "enclosureUri": "ENC:MXQ73705W4",
        "enclosureGroupUri": "EG:dd-EG",
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
                    "mac": "7A:74:BB:A0:00:10",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "7A:74:BB:A0:00:11",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1b",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "7A:74:BB:A0:00:12",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "7A:74:BB:A0:00:13",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13"
                }
            ]
        },
        "boot": {
            "manageBoot": False,
            "order": []
        },
        "bootMode": {
            "manageMode": True,
            "pxeBootPolicy": "IPv4",
            "mode": "UEFI"
        },
        "firmware": {
            "forceInstallFirmware": False,
            "firmwareActivationType": None,
            "firmwareScheduleDateTime": None,
            "firmwareBaselineUri": None,
            "manageFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "overriddenSettings": [],
            "manageBios": False
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "controllers": [],
            "sasLogicalJBODs": []
        },
    },
    {
        "name": "MXQ73705WF, bay 9",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705WF, bay 9",
        "enclosureUri": "ENC:MXQ73705WF",
        "enclosureGroupUri": "EG:dd-EG",
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
                    "mac": "7A:74:BB:A0:00:2C",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "7A:74:BB:A0:00:2D",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "7A:74:BB:A0:00:2E",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "7A:74:BB:A0:00:2F",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13"
                }
            ]
        },
        "boot": {
            "manageBoot": False,
            "order": []
        },
        "bootMode": {
            "manageMode": True,
            "pxeBootPolicy": "IPv4",
            "mode": "UEFI"
        },
        "firmware": {
            "forceInstallFirmware": False,
            "firmwareActivationType": None,
            "firmwareScheduleDateTime": None,
            "firmwareBaselineUri": None,
            "manageFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "overriddenSettings": [],
            "manageBios": False
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "controllers": [],
            "sasLogicalJBODs": []
        },
    },
    {
        "name": "MXQ73705W4, bay 2",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705W4, bay 2",
        "enclosureUri": "ENC:MXQ73705W4",
        "enclosureGroupUri": "EG:dd-EG",
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
                    "mac": "7A:74:BB:A0:00:04",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "7A:74:BB:A0:00:05",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "7A:74:BB:A0:00:06",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "7A:74:BB:A0:00:07",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13"
                }
            ]
        },
        "firmware": {
            "forceInstallFirmware": False,
            "firmwareActivationType": None,
            "firmwareScheduleDateTime": None,
            "firmwareBaselineUri": None,
            "manageFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "overriddenSettings": [],
            "manageBios": False
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "controllers": [],
            "sasLogicalJBODs": []
        },
    },
    {
        "name": "MXQ73705WF, bay 3",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705WF, bay 3",
        "enclosureUri": "ENC:MXQ73705WF",
        "enclosureGroupUri": "EG:dd-EG",
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
                    "mac": "7A:74:BB:A0:00:18",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "7A:74:BB:A0:00:19",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "7A:74:BB:A0:00:1A",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "7A:74:BB:A0:00:1B",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13"
                }
            ]
        },
        "boot": {
            "manageBoot": False,
            "order": []
        },
        "bootMode": {
            "manageMode": True,
            "pxeBootPolicy": "IPv4",
            "mode": "UEFI"
        },
        "firmware": {
            "forceInstallFirmware": False,
            "firmwareActivationType": None,
            "firmwareScheduleDateTime": None,
            "firmwareBaselineUri": None,
            "manageFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "overriddenSettings": [{'id': 'AdminName', 'value': 'WPST Tester1'}, {'id': 'AdminPhone', 'value': '111-111-1111'}],
            "manageBios": True
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "controllers": [],
            "sasLogicalJBODs": []
        },
    },
    {
        "name": "MXQ73708NK, bay 2",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73708NK, bay 2",
        "enclosureUri": "ENC:MXQ73708NK",
        "enclosureGroupUri": "EG:dd-EG",
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
                    "mac": "7A:74:BB:A0:00:38",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "7A:74:BB:A0:00:39",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "7A:74:BB:A0:00:3A",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "7A:74:BB:A0:00:3B",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13"
                }
            ]
        },
        "firmware": {
            "forceInstallFirmware": False,
            "firmwareActivationType": None,
            "firmwareScheduleDateTime": None,
            "firmwareBaselineUri": None,
            "manageFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "overriddenSettings": [{'id': 'AdminName', 'value': 'WPST Tester1'}, {'id': 'AdminPhone', 'value': '111-111-1111'}],
            "manageBios": True
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "controllers": [],
            "sasLogicalJBODs": []
        },
    },
    {
        "name": "MXQ73708NK, bay 7",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73708NK, bay 7",
        "enclosureUri": "ENC:MXQ73708NK",
        "enclosureGroupUri": "EG:dd-EG",
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
                    "mac": "7A:74:BB:A0:00:44",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "7A:74:BB:A0:00:45",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "7A:74:BB:A0:00:46",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "7A:74:BB:A0:00:47",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13"
                }
            ]
        },
        "boot": {
            "manageBoot": False,
            "order": []
        },
        "bootMode": {
            "manageMode": True,
            "pxeBootPolicy": "IPv4",
            "mode": "UEFI"
        },
        "firmware": {
            "forceInstallFirmware": False,
            "firmwareActivationType": None,
            "firmwareScheduleDateTime": None,
            "firmwareBaselineUri": None,
            "manageFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "overriddenSettings": [],
            "manageBios": False
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "controllers": [],
            "sasLogicalJBODs": []
        },
    },
    {
        "name": "MXQ73705W4, bay 1",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705W4, bay 1",
        "enclosureUri": "ENC:MXQ73705W4",
        "enclosureGroupUri": "EG:dd-EG",
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
                    "mac": "7A:74:BB:A0:00:00",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "7A:74:BB:A0:00:01",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "7A:74:BB:A0:00:02",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "7A:74:BB:A0:00:03",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13"
                }
            ]
        },
        "boot": {
            "manageBoot": False,
            "order": []
        },
        "bootMode": {
            "manageMode": True,
            "pxeBootPolicy": "IPv4",
            "mode": "UEFI"
        },
        "firmware": {
            "forceInstallFirmware": False,
            "firmwareActivationType": None,
            "firmwareScheduleDateTime": None,
            "firmwareBaselineUri": None,
            "manageFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "overriddenSettings": [],
            "manageBios": False
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "controllers": [],
            "sasLogicalJBODs": []
        },
    },
    {
        "name": "MXQ73708NK, bay 1",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73708NK, bay 1",
        "enclosureUri": "ENC:MXQ73708NK",
        "enclosureGroupUri": "EG:dd-EG",
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
                    "mac": "7A:74:BB:A0:00:34",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "7A:74:BB:A0:00:35",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "7A:74:BB:A0:00:36",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "7A:74:BB:A0:00:37",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13"
                }
            ]
        },
        "boot": {
            "manageBoot": False,
            "order": []
        },
        "bootMode": {
            "manageMode": True,
            "pxeBootPolicy": "IPv4",
            "mode": "UEFI"
        },
        "firmware": {
            "forceInstallFirmware": False,
            "firmwareActivationType": None,
            "firmwareScheduleDateTime": None,
            "firmwareBaselineUri": None,
            "manageFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "overriddenSettings": [],
            "manageBios": False
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "controllers": [],
            "sasLogicalJBODs": []
        },
    },
    {
        "name": "MXQ73708NK, bay 4",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73708NK, bay 4",
        "enclosureUri": "ENC:MXQ73708NK",
        "enclosureGroupUri": "EG:dd-EG",
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
                    "mac": "7A:74:BB:A0:00:40",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "7A:74:BB:A0:00:41",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "7A:74:BB:A0:00:42",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "7A:74:BB:A0:00:43",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13"
                }
            ]
        },
        "boot": {
            "manageBoot": False,
            "order": []
        },
        "bootMode": {
            "manageMode": True,
            "pxeBootPolicy": "IPv4",
            "mode": "UEFI"
        },
        "firmware": {
            "forceInstallFirmware": False,
            "firmwareActivationType": None,
            "firmwareScheduleDateTime": None,
            "firmwareBaselineUri": None,
            "manageFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "overriddenSettings": [],
            "manageBios": False
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "controllers": [],
            "sasLogicalJBODs": []
        },
    },
    {
        "name": "MXQ73705W4, bay 4",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705W4, bay 4",
        "enclosureUri": "ENC:MXQ73705W4",
        "enclosureGroupUri": "EG:dd-EG",
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
                    "mac": "7A:74:BB:A0:00:0C",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "7A:74:BB:A0:00:0D",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "7A:74:BB:A0:00:0E",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "7A:74:BB:A0:00:0F",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13"
                }
            ]
        },
        "boot": {
            "manageBoot": False,
            "order": []
        },
        "bootMode": {
            "manageMode": True,
            "pxeBootPolicy": "IPv4",
            "mode": "UEFI"
        },
        "firmware": {
            "forceInstallFirmware": False,
            "firmwareActivationType": None,
            "firmwareScheduleDateTime": None,
            "firmwareBaselineUri": None,
            "manageFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "overriddenSettings": [],
            "manageBios": False
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "controllers": [],
            "sasLogicalJBODs": []
        },
    },
    {
        "name": "MXQ73708NK, bay 8",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73708NK, bay 8",
        "enclosureUri": "ENC:MXQ73708NK",
        "enclosureGroupUri": "EG:dd-EG",
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
                    "mac": "7A:74:BB:A0:00:48",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "7A:74:BB:A0:00:49",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "7A:74:BB:A0:00:4A",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "7A:74:BB:A0:00:4B",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13"
                }
            ]
        },
        "boot": {
            "manageBoot": False,
            "order": []
        },
        "bootMode": {
            "manageMode": True,
            "pxeBootPolicy": "Auto",
            "mode": "UEFI"
        },
        "firmware": {
            "forceInstallFirmware": False,
            "firmwareActivationType": None,
            "firmwareScheduleDateTime": None,
            "firmwareBaselineUri": None,
            "manageFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "overriddenSettings": [],
            "manageBios": False
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "controllers": [],
            "sasLogicalJBODs": []
        },
    },
    {
        "name": "MXQ73705WF, bay 4",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705WF, bay 4",
        "enclosureUri": "ENC:MXQ73705WF",
        "enclosureGroupUri": "EG:dd-EG",
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
                    "mac": "7A:74:BB:A0:00:1C",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "7A:74:BB:A0:00:1D",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "7A:74:BB:A0:00:1E",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "7A:74:BB:A0:00:1F",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13"
                }
            ]
        },
        "boot": {
            "manageBoot": False,
            "order": []
        },
        "bootMode": {
            "manageMode": True,
            "pxeBootPolicy": "IPv4",
            "mode": "UEFI"
        },
        "firmware": {
            "forceInstallFirmware": False,
            "firmwareActivationType": None,
            "firmwareScheduleDateTime": None,
            "firmwareBaselineUri": None,
            "manageFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "overriddenSettings": [],
            "manageBios": False
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "controllers": [],
            "sasLogicalJBODs": []
        },
    },
    {
        "name": "MXQ73708NK, bay 3",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73708NK, bay 3",
        "enclosureUri": "ENC:MXQ73708NK",
        "enclosureGroupUri": "EG:dd-EG",
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
                    "mac": "7A:74:BB:A0:00:3C",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "7A:74:BB:A0:00:3D",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "7A:74:BB:A0:00:3E",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "7A:74:BB:A0:00:3F",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13"
                }
            ]
        },
        "boot": {
            "manageBoot": False,
            "order": []
        },
        "bootMode": {
            "manageMode": True,
            "pxeBootPolicy": "IPv4",
            "mode": "UEFI"
        },
        "firmware": {
            "forceInstallFirmware": False,
            "firmwareActivationType": None,
            "firmwareScheduleDateTime": None,
            "firmwareBaselineUri": None,
            "manageFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "overriddenSettings": [],
            "manageBios": False
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "controllers": [],
            "sasLogicalJBODs": []
        },
    },
    {
        "name": "MXQ73705WF, bay 7",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705WF, bay 7",
        "enclosureUri": "ENC:MXQ73705WF",
        "enclosureGroupUri": "EG:dd-EG",
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
                    "mac": "7A:74:BB:A0:00:24",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "7A:74:BB:A0:00:25",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "7A:74:BB:A0:00:26",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "7A:74:BB:A0:00:27",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13"
                }
            ]
        },
        "boot": {
            "manageBoot": False,
            "order": []
        },
        "bootMode": {
            "manageMode": True,
            "pxeBootPolicy": "IPv4",
            "mode": "UEFI"
        },
        "firmware": {
            "forceInstallFirmware": False,
            "firmwareActivationType": None,
            "firmwareScheduleDateTime": None,
            "firmwareBaselineUri": None,
            "manageFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "overriddenSettings": [],
            "manageBios": False
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "controllers": [],
            "sasLogicalJBODs": []
        },
    },
    {
        "name": "MXQ73705WF, bay 6",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705WF, bay 6",
        "enclosureUri": "ENC:MXQ73705WF",
        "enclosureGroupUri": "EG:dd-EG",
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
                    "mac": "7A:74:BB:A0:00:20",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "7A:74:BB:A0:00:21",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "7A:74:BB:A0:00:22",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "7A:74:BB:A0:00:23",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13"
                }
            ]
        },
        "boot": {
            "manageBoot": False,
            "order": []
        },
        "bootMode": {
            "manageMode": True,
            "pxeBootPolicy": "IPv4",
            "mode": "UEFI"
        },
        "firmware": {
            "forceInstallFirmware": False,
            "firmwareActivationType": None,
            "firmwareScheduleDateTime": None,
            "firmwareBaselineUri": None,
            "manageFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "overriddenSettings": [],
            "manageBios": False
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "controllers": [],
            "sasLogicalJBODs": []
        },
    },
    {
        "name": "MXQ73705WF, bay 10",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705WF, bay 10",
        "enclosureUri": "ENC:MXQ73705WF",
        "enclosureGroupUri": "EG:dd-EG",
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
                    "mac": "7A:74:BB:A0:00:30",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "7A:74:BB:A0:00:31",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "7A:74:BB:A0:00:32",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "7A:74:BB:A0:00:33",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13"
                }
            ]
        },
        "boot": {
            "manageBoot": False,
            "order": []
        },
        "bootMode": {
            "manageMode": True,
            "pxeBootPolicy": "IPv4",
            "mode": "UEFI"
        },
        "firmware": {
            "forceInstallFirmware": False,
            "firmwareActivationType": None,
            "firmwareScheduleDateTime": None,
            "firmwareBaselineUri": None,
            "manageFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "overriddenSettings": [{'id': 'AdminName', 'value': 'WPST Tester1'}, {'id': 'AdminPhone', 'value': '111-111-1111'}],
            "manageBios": True
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "controllers": [],
            "sasLogicalJBODs": []
        },
    },
    {
        "name": "MXQ73705W4, bay 3",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705W4, bay 3",
        "enclosureUri": "ENC:MXQ73705W4",
        "enclosureGroupUri": "EG:dd-EG",
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
                    "mac": "7A:74:BB:A0:00:08",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "7A:74:BB:A0:00:09",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "7A:74:BB:A0:00:0A",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "7A:74:BB:A0:00:0B",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13"
                }
            ]
        },
        "boot": {
            "manageBoot": False,
            "order": []
        },
        "bootMode": {
            "manageMode": True,
            "pxeBootPolicy": "IPv4",
            "mode": "UEFI"
        },
        "firmware": {
            "forceInstallFirmware": False,
            "firmwareActivationType": None,
            "firmwareScheduleDateTime": None,
            "firmwareBaselineUri": None,
            "manageFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "overriddenSettings": [],
            "manageBios": False
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "controllers": [],
            "sasLogicalJBODs": []
        },
    },
    {
        "name": "MXQ73705WF, bay 5",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705WF, bay 5",
        "enclosureUri": "ENC:MXQ73705WF",
        "enclosureGroupUri": "EG:dd-EG",
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
                    "mac": "3A:C6:63:20:00:1E",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "3A:C6:63:20:00:1F",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "3A:C6:63:20:00:20",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "3A:C6:63:20:00:21",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13"
                }
            ]
        },
        "boot": {
            "manageBoot": False,
            "order": []
        },
        "bootMode": {
            "manageMode": True,
            "pxeBootPolicy": "IPv4",
            "mode": "UEFI"
        },
        "firmware": {
            "forceInstallFirmware": False,
            "firmwareActivationType": None,
            "firmwareScheduleDateTime": None,
            "firmwareBaselineUri": None,
            "manageFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "overriddenSettings": [],
            "manageBios": False
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "controllers": [],
            "sasLogicalJBODs": []
        },
    }
]
expected_server_profiles = [
    {
        "uri": "SP:MXQ73705W4, bay 8",
        "name": "MXQ73705W4, bay 8",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705W4, bay 8",
        "enclosureUri": "ENC:MXQ73705W4",
        "enclosureGroupUri": "EG:dd-EG",
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
                    "mac": "7A:74:BB:A0:00:14",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "7A:74:BB:A0:00:15",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "7A:74:BB:A0:00:16",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "7A:74:BB:A0:00:17",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13"
                }
            ]
        },
        "boot": {
            "manageBoot": False,
            "order": []
        },
        "bootMode": {
            "manageMode": True,
            "pxeBootPolicy": "IPv4",
            "mode": "UEFI"
        },
        "firmware": {
            "forceInstallFirmware": False,
            "firmwareActivationType": None,
            "firmwareScheduleDateTime": None,
            "firmwareBaselineUri": None,
            "manageFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "overriddenSettings": [],
            "manageBios": False
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "controllers": [],
            "sasLogicalJBODs": []
        },
        "status": "OK",
    },
    {
        "uri": "SP:MXQ73705WF, bay 8",
        "name": "MXQ73705WF, bay 8",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705WF, bay 8",
        "enclosureUri": "ENC:MXQ73705WF",
        "enclosureGroupUri": "EG:dd-EG",
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
                    "mac": "7A:74:BB:A0:00:28",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "7A:74:BB:A0:00:29",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "7A:74:BB:A0:00:2A",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "7A:74:BB:A0:00:2B",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13"
                }
            ]
        },
        "boot": {
            "manageBoot": False,
            "order": []
        },
        "bootMode": {
            "manageMode": True,
            "pxeBootPolicy": "IPv4",
            "mode": "UEFI"
        },
        "firmware": {
            "forceInstallFirmware": False,
            "firmwareActivationType": None,
            "firmwareScheduleDateTime": None,
            "firmwareBaselineUri": None,
            "manageFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "overriddenSettings": [],
            "manageBios": False
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "controllers": [],
            "sasLogicalJBODs": []
        },
        "status": "OK",
    },
    {
        "uri": "SP:MXQ73705W4, bay 7",
        "name": "MXQ73705W4, bay 7",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705W4, bay 7",
        "enclosureUri": "ENC:MXQ73705W4",
        "enclosureGroupUri": "EG:dd-EG",
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
                    "mac": "7A:74:BB:A0:00:10",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "7A:74:BB:A0:00:11",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1b",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "7A:74:BB:A0:00:12",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "7A:74:BB:A0:00:13",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13"
                }
            ]
        },
        "boot": {
            "manageBoot": False,
            "order": []
        },
        "bootMode": {
            "manageMode": True,
            "pxeBootPolicy": "IPv4",
            "mode": "UEFI"
        },
        "firmware": {
            "forceInstallFirmware": False,
            "firmwareActivationType": None,
            "firmwareScheduleDateTime": None,
            "firmwareBaselineUri": None,
            "manageFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "overriddenSettings": [],
            "manageBios": False
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "controllers": [],
            "sasLogicalJBODs": []
        },
        "status": "OK",
    },
    {
        "uri": "SP:MXQ73705WF, bay 9",
        "name": "MXQ73705WF, bay 9",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705WF, bay 9",
        "enclosureUri": "ENC:MXQ73705WF",
        "enclosureGroupUri": "EG:dd-EG",
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
                    "mac": "7A:74:BB:A0:00:2C",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "7A:74:BB:A0:00:2D",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "7A:74:BB:A0:00:2E",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "7A:74:BB:A0:00:2F",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13"
                }
            ]
        },
        "boot": {
            "manageBoot": False,
            "order": []
        },
        "bootMode": {
            "manageMode": True,
            "pxeBootPolicy": "IPv4",
            "mode": "UEFI"
        },
        "firmware": {
            "forceInstallFirmware": False,
            "firmwareActivationType": None,
            "firmwareScheduleDateTime": None,
            "firmwareBaselineUri": None,
            "manageFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "overriddenSettings": [],
            "manageBios": False
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "controllers": [],
            "sasLogicalJBODs": []
        },
        "status": "OK",
    },
    {
        "uri": "SP:MXQ73705W4, bay 2",
        "name": "MXQ73705W4, bay 2",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705W4, bay 2",
        "enclosureUri": "ENC:MXQ73705W4",
        "enclosureGroupUri": "EG:dd-EG",
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
                    "mac": "7A:74:BB:A0:00:04",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "7A:74:BB:A0:00:05",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "7A:74:BB:A0:00:06",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "7A:74:BB:A0:00:07",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13"
                }
            ]
        },
        "firmware": {
            "forceInstallFirmware": False,
            "firmwareActivationType": None,
            "firmwareScheduleDateTime": None,
            "firmwareBaselineUri": None,
            "manageFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "overriddenSettings": [],
            "manageBios": False
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "controllers": [],
            "sasLogicalJBODs": []
        },
        "status": "OK",
    },
    {
        "uri": "SP:MXQ73705WF, bay 3",
        "name": "MXQ73705WF, bay 3",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705WF, bay 3",
        "enclosureUri": "ENC:MXQ73705WF",
        "enclosureGroupUri": "EG:dd-EG",
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
                    "mac": "7A:74:BB:A0:00:18",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "7A:74:BB:A0:00:19",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "7A:74:BB:A0:00:1A",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "7A:74:BB:A0:00:1B",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13"
                }
            ]
        },
        "boot": {
            "manageBoot": False,
            "order": []
        },
        "bootMode": {
            "manageMode": True,
            "pxeBootPolicy": "IPv4",
            "mode": "UEFI"
        },
        "firmware": {
            "forceInstallFirmware": False,
            "firmwareActivationType": None,
            "firmwareScheduleDateTime": None,
            "firmwareBaselineUri": None,
            "manageFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "overriddenSettings": [{'id': 'AdminName', 'value': 'WPST Tester1'}, {'id': 'AdminPhone', 'value': '111-111-1111'}],
            "manageBios": True
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "controllers": [],
            "sasLogicalJBODs": []
        },
        "status": "OK",
    },
    {
        "uri": "SP:MXQ73708NK, bay 2",
        "name": "MXQ73708NK, bay 2",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73708NK, bay 2",
        "enclosureUri": "ENC:MXQ73708NK",
        "enclosureGroupUri": "EG:dd-EG",
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
                    "mac": "7A:74:BB:A0:00:38",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "7A:74:BB:A0:00:39",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "7A:74:BB:A0:00:3A",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "7A:74:BB:A0:00:3B",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13"
                }
            ]
        },
        "firmware": {
            "forceInstallFirmware": False,
            "firmwareActivationType": None,
            "firmwareScheduleDateTime": None,
            "firmwareBaselineUri": None,
            "manageFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "overriddenSettings": [{'id': 'AdminName', 'value': 'WPST Tester1'}, {'id': 'AdminPhone', 'value': '111-111-1111'}],
            "manageBios": True
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "controllers": [],
            "sasLogicalJBODs": []
        },
        "status": "OK",
    },
    {
        "uri": "SP:MXQ73708NK, bay 7",
        "name": "MXQ73708NK, bay 7",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73708NK, bay 7",
        "enclosureUri": "ENC:MXQ73708NK",
        "enclosureGroupUri": "EG:dd-EG",
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
                    "mac": "7A:74:BB:A0:00:44",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "7A:74:BB:A0:00:45",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "7A:74:BB:A0:00:46",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "7A:74:BB:A0:00:47",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13"
                }
            ]
        },
        "boot": {
            "manageBoot": False,
            "order": []
        },
        "bootMode": {
            "manageMode": True,
            "pxeBootPolicy": "IPv4",
            "mode": "UEFI"
        },
        "firmware": {
            "forceInstallFirmware": False,
            "firmwareActivationType": None,
            "firmwareScheduleDateTime": None,
            "firmwareBaselineUri": None,
            "manageFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "overriddenSettings": [],
            "manageBios": False
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "controllers": [],
            "sasLogicalJBODs": []
        },
        "status": "OK",
    },
    {
        "uri": "SP:MXQ73705W4, bay 1",
        "name": "MXQ73705W4, bay 1",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705W4, bay 1",
        "enclosureUri": "ENC:MXQ73705W4",
        "enclosureGroupUri": "EG:dd-EG",
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
                    "mac": "7A:74:BB:A0:00:00",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "7A:74:BB:A0:00:01",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "7A:74:BB:A0:00:02",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "7A:74:BB:A0:00:03",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13"
                }
            ]
        },
        "boot": {
            "manageBoot": False,
            "order": []
        },
        "bootMode": {
            "manageMode": True,
            "pxeBootPolicy": "IPv4",
            "mode": "UEFI"
        },
        "firmware": {
            "forceInstallFirmware": False,
            "firmwareActivationType": None,
            "firmwareScheduleDateTime": None,
            "firmwareBaselineUri": None,
            "manageFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "overriddenSettings": [],
            "manageBios": False
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "controllers": [],
            "sasLogicalJBODs": []
        },
        "status": "OK",
    },
    {
        "uri": "SP:MXQ73708NK, bay 1",
        "name": "MXQ73708NK, bay 1",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73708NK, bay 1",
        "enclosureUri": "ENC:MXQ73708NK",
        "enclosureGroupUri": "EG:dd-EG",
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
                    "mac": "7A:74:BB:A0:00:34",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "7A:74:BB:A0:00:35",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "7A:74:BB:A0:00:36",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "7A:74:BB:A0:00:37",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13"
                }
            ]
        },
        "boot": {
            "manageBoot": False,
            "order": []
        },
        "bootMode": {
            "manageMode": True,
            "pxeBootPolicy": "IPv4",
            "mode": "UEFI"
        },
        "firmware": {
            "forceInstallFirmware": False,
            "firmwareActivationType": None,
            "firmwareScheduleDateTime": None,
            "firmwareBaselineUri": None,
            "manageFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "overriddenSettings": [],
            "manageBios": False
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "controllers": [],
            "sasLogicalJBODs": []
        },
        "status": "OK",
    },
    {
        "uri": "SP:MXQ73708NK, bay 4",
        "name": "MXQ73708NK, bay 4",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73708NK, bay 4",
        "enclosureUri": "ENC:MXQ73708NK",
        "enclosureGroupUri": "EG:dd-EG",
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
                    "mac": "7A:74:BB:A0:00:40",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "7A:74:BB:A0:00:41",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "7A:74:BB:A0:00:42",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "7A:74:BB:A0:00:43",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13"
                }
            ]
        },
        "boot": {
            "manageBoot": False,
            "order": []
        },
        "bootMode": {
            "manageMode": True,
            "pxeBootPolicy": "IPv4",
            "mode": "UEFI"
        },
        "firmware": {
            "forceInstallFirmware": False,
            "firmwareActivationType": None,
            "firmwareScheduleDateTime": None,
            "firmwareBaselineUri": None,
            "manageFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "overriddenSettings": [],
            "manageBios": False
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "controllers": [],
            "sasLogicalJBODs": []
        },
        "status": "OK",
    },
    {
        "uri": "SP:MXQ73705W4, bay 4",
        "name": "MXQ73705W4, bay 4",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705W4, bay 4",
        "enclosureUri": "ENC:MXQ73705W4",
        "enclosureGroupUri": "EG:dd-EG",
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
                    "mac": "7A:74:BB:A0:00:0C",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "7A:74:BB:A0:00:0D",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "7A:74:BB:A0:00:0E",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "7A:74:BB:A0:00:0F",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13"
                }
            ]
        },
        "boot": {
            "manageBoot": False,
            "order": []
        },
        "bootMode": {
            "manageMode": True,
            "pxeBootPolicy": "IPv4",
            "mode": "UEFI"
        },
        "firmware": {
            "forceInstallFirmware": False,
            "firmwareActivationType": None,
            "firmwareScheduleDateTime": None,
            "firmwareBaselineUri": None,
            "manageFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "overriddenSettings": [],
            "manageBios": False
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "controllers": [],
            "sasLogicalJBODs": []
        },
        "status": "OK",
    },
    {
        "uri": "SP:MXQ73708NK, bay 8",
        "name": "MXQ73708NK, bay 8",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73708NK, bay 8",
        "enclosureUri": "ENC:MXQ73708NK",
        "enclosureGroupUri": "EG:dd-EG",
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
                    "mac": "7A:74:BB:A0:00:48",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "7A:74:BB:A0:00:49",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "7A:74:BB:A0:00:4A",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "7A:74:BB:A0:00:4B",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13"
                }
            ]
        },
        "boot": {
            "manageBoot": False,
            "order": []
        },
        "bootMode": {
            "manageMode": True,
            "pxeBootPolicy": "Auto",
            "mode": "UEFI"
        },
        "firmware": {
            "forceInstallFirmware": False,
            "firmwareActivationType": None,
            "firmwareScheduleDateTime": None,
            "firmwareBaselineUri": None,
            "manageFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "overriddenSettings": [],
            "manageBios": False
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "controllers": [],
            "sasLogicalJBODs": []
        },
        "status": "OK",
    },
    {
        "uri": "SP:MXQ73705WF, bay 4",
        "name": "MXQ73705WF, bay 4",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705WF, bay 4",
        "enclosureUri": "ENC:MXQ73705WF",
        "enclosureGroupUri": "EG:dd-EG",
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
                    "mac": "7A:74:BB:A0:00:1C",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "7A:74:BB:A0:00:1D",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "7A:74:BB:A0:00:1E",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "7A:74:BB:A0:00:1F",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13"
                }
            ]
        },
        "boot": {
            "manageBoot": False,
            "order": []
        },
        "bootMode": {
            "manageMode": True,
            "pxeBootPolicy": "IPv4",
            "mode": "UEFI"
        },
        "firmware": {
            "forceInstallFirmware": False,
            "firmwareActivationType": None,
            "firmwareScheduleDateTime": None,
            "firmwareBaselineUri": None,
            "manageFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "overriddenSettings": [],
            "manageBios": False
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "controllers": [],
            "sasLogicalJBODs": []
        },
        "status": "OK",
    },
    {
        "uri": "SP:MXQ73708NK, bay 3",
        "name": "MXQ73708NK, bay 3",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73708NK, bay 3",
        "enclosureUri": "ENC:MXQ73708NK",
        "enclosureGroupUri": "EG:dd-EG",
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
                    "mac": "7A:74:BB:A0:00:3C",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "7A:74:BB:A0:00:3D",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "7A:74:BB:A0:00:3E",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "7A:74:BB:A0:00:3F",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13"
                }
            ]
        },
        "boot": {
            "manageBoot": False,
            "order": []
        },
        "bootMode": {
            "manageMode": True,
            "pxeBootPolicy": "IPv4",
            "mode": "UEFI"
        },
        "firmware": {
            "forceInstallFirmware": False,
            "firmwareActivationType": None,
            "firmwareScheduleDateTime": None,
            "firmwareBaselineUri": None,
            "manageFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "overriddenSettings": [],
            "manageBios": False
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "controllers": [],
            "sasLogicalJBODs": []
        },
        "status": "OK",
    },
    {
        "uri": "SP:MXQ73705WF, bay 7",
        "name": "MXQ73705WF, bay 7",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705WF, bay 7",
        "enclosureUri": "ENC:MXQ73705WF",
        "enclosureGroupUri": "EG:dd-EG",
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
                    "mac": "7A:74:BB:A0:00:24",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "7A:74:BB:A0:00:25",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "7A:74:BB:A0:00:26",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "7A:74:BB:A0:00:27",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13"
                }
            ]
        },
        "boot": {
            "manageBoot": False,
            "order": []
        },
        "bootMode": {
            "manageMode": True,
            "pxeBootPolicy": "IPv4",
            "mode": "UEFI"
        },
        "firmware": {
            "forceInstallFirmware": False,
            "firmwareActivationType": None,
            "firmwareScheduleDateTime": None,
            "firmwareBaselineUri": None,
            "manageFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "overriddenSettings": [],
            "manageBios": False
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "controllers": [],
            "sasLogicalJBODs": []
        },
        "status": "OK",
    },
    {
        "uri": "SP:MXQ73705WF, bay 6",
        "name": "MXQ73705WF, bay 6",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705WF, bay 6",
        "enclosureUri": "ENC:MXQ73705WF",
        "enclosureGroupUri": "EG:dd-EG",
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
                    "mac": "7A:74:BB:A0:00:20",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "7A:74:BB:A0:00:21",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "7A:74:BB:A0:00:22",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "7A:74:BB:A0:00:23",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13"
                }
            ]
        },
        "boot": {
            "manageBoot": False,
            "order": []
        },
        "bootMode": {
            "manageMode": True,
            "pxeBootPolicy": "IPv4",
            "mode": "UEFI"
        },
        "firmware": {
            "forceInstallFirmware": False,
            "firmwareActivationType": None,
            "firmwareScheduleDateTime": None,
            "firmwareBaselineUri": None,
            "manageFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "overriddenSettings": [],
            "manageBios": False
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "controllers": [],
            "sasLogicalJBODs": []
        },
        "status": "OK",
    },
    {
        "uri": "SP:MXQ73705WF, bay 10",
        "name": "MXQ73705WF, bay 10",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705WF, bay 10",
        "enclosureUri": "ENC:MXQ73705WF",
        "enclosureGroupUri": "EG:dd-EG",
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
                    "mac": "7A:74:BB:A0:00:30",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "7A:74:BB:A0:00:31",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "7A:74:BB:A0:00:32",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "7A:74:BB:A0:00:33",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13"
                }
            ]
        },
        "boot": {
            "manageBoot": False,
            "order": []
        },
        "bootMode": {
            "manageMode": True,
            "pxeBootPolicy": "IPv4",
            "mode": "UEFI"
        },
        "firmware": {
            "forceInstallFirmware": False,
            "firmwareActivationType": None,
            "firmwareScheduleDateTime": None,
            "firmwareBaselineUri": None,
            "manageFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "overriddenSettings": [{'id': 'AdminName', 'value': 'WPST Tester1'}, {'id': 'AdminPhone', 'value': '111-111-1111'}],
            "manageBios": True
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "controllers": [],
            "sasLogicalJBODs": []
        },
        "status": "OK",
    },
    {
        "uri": "SP:MXQ73705W4, bay 3",
        "name": "MXQ73705W4, bay 3",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705W4, bay 3",
        "enclosureUri": "ENC:MXQ73705W4",
        "enclosureGroupUri": "EG:dd-EG",
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
                    "mac": "7A:74:BB:A0:00:08",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "7A:74:BB:A0:00:09",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "7A:74:BB:A0:00:0A",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "7A:74:BB:A0:00:0B",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13"
                }
            ]
        },
        "boot": {
            "manageBoot": False,
            "order": []
        },
        "bootMode": {
            "manageMode": True,
            "pxeBootPolicy": "IPv4",
            "mode": "UEFI"
        },
        "firmware": {
            "forceInstallFirmware": False,
            "firmwareActivationType": None,
            "firmwareScheduleDateTime": None,
            "firmwareBaselineUri": None,
            "manageFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "overriddenSettings": [],
            "manageBios": False
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "controllers": [],
            "sasLogicalJBODs": []
        },
        "status": "OK",
    },
    {
        "uri": "SP:MXQ73705WF, bay 5",
        "name": "MXQ73705WF, bay 5",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705WF, bay 5",
        "enclosureUri": "ENC:MXQ73705WF",
        "enclosureGroupUri": "EG:dd-EG",
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
                    "mac": "3A:C6:63:20:00:1E",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "3A:C6:63:20:00:1F",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "3A:C6:63:20:00:20",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12"
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "3A:C6:63:20:00:21",
                    "macType": "UserDefined",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13"
                }
            ]
        },
        "boot": {
            "manageBoot": False,
            "order": []
        },
        "bootMode": {
            "manageMode": True,
            "pxeBootPolicy": "IPv4",
            "mode": "UEFI"
        },
        "firmware": {
            "forceInstallFirmware": False,
            "firmwareActivationType": None,
            "firmwareScheduleDateTime": None,
            "firmwareBaselineUri": None,
            "manageFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "overriddenSettings": [],
            "manageBios": False
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "controllers": [],
            "sasLogicalJBODs": []
        },
        "status": "OK",
    }
]

server_profile_templates = [
    {
        "name": "Bios and local storage with connections",
        "type": "ServerProfileTemplateV7",
        "serverProfileDescription": "",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9 1:3:Synergy 3820C 10/20Gb CNA",
        "enclosureGroupUri": "EG:dd-EG",
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
                    "name": "ETH",
                    "functionType": "Ethernet",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {

                    },
                },
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": "IPv4",
            "manageMode": True,
            "mode": "UEFI"
        },
        "firmware": {
            "manageFirmware": False,
            "forceInstallFirmware": False
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": [{'id': 'AdminName', 'value': 'WPST Tester1'}, {'id': 'AdminPhone', 'value': '111-111-1111'}]
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
        "name": "DD-21RBay10-Gen10-Template",
        "type": "ServerProfileTemplateV7",
        "serverProfileDescription": "",
        "serverHardwareTypeUri": "SHT:SY 480 Gen10 1:3:Synergy 3820C 10/20Gb CNA",
        "enclosureGroupUri": "EG:dd-EG",
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
                    "name": "FC-a",
                    "functionType": "FibreChannel",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "networkUri": "FC:ovstsan216-240-a",
                    "boot": {

                    },
                },
                {
                    "id": 2,
                    "name": "FC-b",
                    "functionType": "FibreChannel",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "networkUri": "FC:ovstsan216-240-b",
                    "boot": {

                    },
                },
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": "IPv4",
            "manageMode": True,
            "mode": "UEFI"
        },
        "firmware": {
            "manageFirmware": False,
            "forceInstallFirmware": False
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": [{'id': 'AdminName', 'value': 'WPST Tester1'}, {'id': 'AdminPhone', 'value': '111-111-1111'}]
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorNameType": "AutoGenerated",
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 1,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ],
                },
            ]

        },
    },
    {
        "name": "DD-21RBay3-Gen9-Template",
        "type": "ServerProfileTemplateV7",
        "serverProfileDescription": "",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9:1:Smart Array P542D Controller:3:Synergy 3820C 10/20Gb CNA",
        "enclosureGroupUri": "EG:dd-EG",
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
                    "name": "ETH",
                    "functionType": "Ethernet",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {
                    },
                },
            ]

        },
        "firmware": {
            "manageFirmware": False,
            "forceInstallFirmware": False
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorNameType": "AutoGenerated"
    }
]
expected_server_profile_templates = [
    {
        "uri": "SPT:Bios and local storage with connections",
        "status": "OK",
        "name": "Bios and local storage with connections",
        "type": "ServerProfileTemplateV7",
        "serverProfileDescription": "",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9 1:3:Synergy 3820C 10/20Gb CNA",
        "enclosureGroupUri": "EG:dd-EG",
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
                    "name": "ETH",
                    "functionType": "Ethernet",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {

                    },
                },
            ]

        },
        "bootMode": {
            "pxeBootPolicy": "IPv4",
            "manageMode": True,
            "mode": "UEFI"
        },
        "firmware": {
            "manageFirmware": False,
            "forceInstallFirmware": False
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": [{'id': 'AdminName', 'value': 'WPST Tester1'}, {'id': 'AdminPhone', 'value': '111-111-1111'}]
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
        "uri": "SPT:DD-21RBay10-Gen10-Template",
        "status": "OK",
        "name": "DD-21RBay10-Gen10-Template",
        "type": "ServerProfileTemplateV7",
        "serverProfileDescription": "",
        "serverHardwareTypeUri": "SHT:SY 480 Gen10 1:3:Synergy 3820C 10/20Gb CNA",
        "enclosureGroupUri": "EG:dd-EG",
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
                    "name": "FC-a",
                    "functionType": "FibreChannel",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "networkUri": "FC:ovstsan216-240-a",
                    "boot": {

                    },
                },
                {
                    "id": 2,
                    "name": "FC-b",
                    "functionType": "FibreChannel",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "networkUri": "FC:ovstsan216-240-b",
                    "boot": {

                    },
                },
            ]

        },
        "bootMode": {
            "pxeBootPolicy": "IPv4",
            "manageMode": True,
            "mode": "UEFI"
        },
        "firmware": {
            "manageFirmware": False,
            "forceInstallFirmware": False
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": [{'id': 'AdminName', 'value': 'WPST Tester1'}, {'id': 'AdminPhone', 'value': '111-111-1111'}]
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorNameType": "AutoGenerated",
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 1,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ],
                },
            ]

        },
    },
    {
        "uri": "SPT:DD-21RBay3-Gen9-Template",
        "status": "OK",
        "name": "DD-21RBay3-Gen9-Template",
        "type": "ServerProfileTemplateV7",
        "serverProfileDescription": "",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9:1:Smart Array P542D Controller:3:Synergy 3820C 10/20Gb CNA",
        "enclosureGroupUri": "EG:dd-EG",
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
                    "name": "ETH",
                    "functionType": "Ethernet",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                },
            ]

        },

        "firmware": {
            "manageFirmware": False,
            "forceInstallFirmware": False
        },

        "hideUnusedFlexNics": True,
        "iscsiInitiatorNameType": "AutoGenerated"
    }
]

edit_server_profile_templates = [
    {
        "name": "Bios and local storage with connections",
        "type": "ServerProfileTemplateV7",
        "serverProfileDescription": "",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9 1:3:Synergy 3820C 10/20Gb CNA",
        "enclosureGroupUri": "EG:dd-EG",
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
                    "name": "ETH",
                    "functionType": "Ethernet",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {

                    }},
                {
                    "id": 2,
                    "name": "FC-a",
                    "functionType": "FibreChannel",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "networkUri": "FC:ovstsan216-240-a",
                    "boot": {

                    },
                },
                {
                    "id": 3,
                    "name": "FC-b",
                    "functionType": "FibreChannel",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "networkUri": "FC:ovstsan216-240-b",
                    "boot": {

                    },

                },
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": ["CD", "USB", 'HardDisk', "PXE"]
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
            "overriddenSettings": [{"id": "CustomPostMessage", "value": "WindowSysetm"}, {"id": "ServerPrimaryOs", "value": "Window10"}, {"id": "ServerOtherInfo", "value": "severos"}, {"id": "AdminName", "value": "OvstQuall"}, {"id": "AdminPhone", "value": "564654654645"}, {"id": "AdminEmail", "value": "OvstQuall@hpe.com"}, {"id": "AdminOtherInfo", "value": "OvstQuallRing7"}]
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorNameType": "AutoGenerated",
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        },

                    ],
                },
            ]

        },
    },
    {
        "name": "DD-21RBay10-Gen10-Template",
        "type": "ServerProfileTemplateV7",
        "serverProfileDescription": "",
        "serverHardwareTypeUri": "SHT:SY 480 Gen10 1:3:Synergy 3820C 10/20Gb CNA",
        "enclosureGroupUri": "EG:dd-EG",
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
                    "name": "FC-a",
                    "functionType": "FibreChannel",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "networkUri": "FC:ovstsan216-240-a",
                    "boot": {

                    },
                },
                {
                    "id": 2,
                    "name": "FC-b",
                    "functionType": "FibreChannel",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "networkUri": "FC:ovstsan216-240-b",
                    "boot": {

                    },
                },
                {
                    "id": 3,
                    "name": "ETH",
                    "functionType": "Ethernet",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {
                    },
                },
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": ["CD", "USB", 'HardDisk', "PXE"]
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
            "overriddenSettings": [{"id": "CustomPostMessage", "value": "WindowSysetm"}, {"id": "ServerPrimaryOs", "value": "Window10"}, {"id": "ServerOtherInfo", "value": "severos"}, {"id": "AdminName", "value": "OvstQuall"}, {"id": "AdminPhone", "value": "564654654645"}, {"id": "AdminEmail", "value": "OvstQuall@hpe.com"}, {"id": "AdminOtherInfo", "value": "OvstQuallRing7"}]
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorNameType": "AutoGenerated",
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
    },
    {
        "name": "DD-21RBay3-Gen9-Template",
        "type": "ServerProfileTemplateV7",
        "serverProfileDescription": "",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9:1:Smart Array P542D Controller:3:Synergy 3820C 10/20Gb CNA",
        "enclosureGroupUri": "EG:dd-EG",
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
                    "name": "ETH",
                    "functionType": "Ethernet",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {
                    },
                },
                {
                    "id": 2,
                    "name": "FC-a",
                    "functionType": "FibreChannel",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "networkUri": "FC:ovstsan216-240-a",
                    "boot": {

                    },
                },
                {
                    "id": 3,
                    "name": "FC-b",
                    "functionType": "FibreChannel",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "networkUri": "FC:ovstsan216-240-b",
                    "boot": {

                    },

                },
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": ["CD", "USB", 'HardDisk', "PXE"]
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
            "overriddenSettings": [{"id": "CustomPostMessage", "value": "WindowSysetm"}, {"id": "ServerPrimaryOs", "value": "Window10"}, {"id": "ServerOtherInfo", "value": "severos"}, {"id": "AdminName", "value": "OvstQuall"}, {"id": "AdminPhone", "value": "564654654645"}, {"id": "AdminEmail", "value": "OvstQuall@hpe.com"}, {"id": "AdminOtherInfo", "value": "OvstQuallRing7"}]
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorNameType": "AutoGenerated",
        "sanStorage": {
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        },

                    ],
                },
            ]

        },
    }
]
expected_edit_server_profile_templates = [
    {
        "uri": "SPT:Bios and local storage with connections",
        "status": "OK",
        "name": "Bios and local storage with connections",
        "type": "ServerProfileTemplateV7",
        "serverProfileDescription": "",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9 1:3:Synergy 3820C 10/20Gb CNA",
        "enclosureGroupUri": "EG:dd-EG",
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
                    "name": "ETH",
                    "functionType": "Ethernet",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {

                    },
                },
                {
                    "id": 2,
                    "name": "FC-a",
                    "functionType": "FibreChannel",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "networkUri": "FC:ovstsan216-240-a",
                    "boot": {

                    },
                },
                {
                    "id": 3,
                    "name": "FC-b",
                    "functionType": "FibreChannel",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "networkUri": "FC:ovstsan216-240-b",
                    "boot": {

                    },
                },
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": ["CD", "USB", 'HardDisk', "PXE"]
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": [{"id": "CustomPostMessage", "value": "WindowSysetm"}, {"id": "ServerPrimaryOs", "value": "Window10"}, {"id": "ServerOtherInfo", "value": "severos"}, {"id": "AdminName", "value": "OvstQuall"}, {"id": "AdminPhone", "value": "564654654645"}, {"id": "AdminEmail", "value": "OvstQuall@hpe.com"}, {"id": "AdminOtherInfo", "value": "OvstQuallRing7"}]
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorNameType": "AutoGenerated",
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        },
                    ],
                },
            ]

        },
    },
    {
        "uri": "SPT:DD-21RBay10-Gen10-Template",
        "status": "OK",
        "name": "DD-21RBay10-Gen10-Template",
        "type": "ServerProfileTemplateV7",
        "serverProfileDescription": "",
        "serverHardwareTypeUri": "SHT:SY 480 Gen10 1:3:Synergy 3820C 10/20Gb CNA",
        "enclosureGroupUri": "EG:dd-EG",
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
                    "name": "FC-a",
                    "functionType": "FibreChannel",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "networkUri": "FC:ovstsan216-240-a",
                    "boot": {

                    },
                },
                {
                    "id": 2,
                    "name": "FC-b",
                    "functionType": "FibreChannel",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "networkUri": "FC:ovstsan216-240-b",
                    "boot": {

                    },
                },
                {
                    "id": 3,
                    "name": "ETH",
                    "functionType": "Ethernet",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {

                    },
                },
            ]
        },
        "boot": {
            "manageBoot": True,
            "order": ["CD", "USB", 'HardDisk', "PXE"]
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": [{"id": "CustomPostMessage", "value": "WindowSysetm"}, {"id": "ServerPrimaryOs", "value": "Window10"}, {"id": "ServerOtherInfo", "value": "severos"}, {"id": "AdminName", "value": "OvstQuall"}, {"id": "AdminPhone", "value": "564654654645"}, {"id": "AdminEmail", "value": "OvstQuall@hpe.com"}, {"id": "AdminOtherInfo", "value": "OvstQuallRing7"}]
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorNameType": "AutoGenerated",
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
    },
    {
        "uri": "SPT:DD-21RBay3-Gen9-Template",
        "status": "OK",
        "name": "DD-21RBay3-Gen9-Template",
        "type": "ServerProfileTemplateV7",
        "serverProfileDescription": "",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9:1:Smart Array P542D Controller:3:Synergy 3820C 10/20Gb CNA",
        "enclosureGroupUri": "EG:dd-EG",
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
                    "name": "ETH",
                    "functionType": "Ethernet",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {
                    },
                },
                {
                    "id": 2,
                    "name": "FC-a",
                    "functionType": "FibreChannel",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "networkUri": "FC:ovstsan216-240-a",
                    "boot": {
                    },
                },
                {
                    "id": 3,
                    "name": "FC-b",
                    "functionType": "FibreChannel",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "networkUri": "FC:ovstsan216-240-b",
                    "boot": {
                    },
                },
            ]

        },
        "firmware": {
            "manageFirmware": False,
            "forceInstallFirmware": False
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorNameType": "AutoGenerated",
        "sanStorage": {
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        },
                    ],
                },
            ]

        },
    }
]
expected_edit_server_profiles_from_spt = [
    {
        "uri": "SP:MXQ73708NK, bay 3",
        "name": "MXQ73708NK, bay 3",
        "type": "ServerProfileV11",
        "serverProfileTemplateUri": "SPT:Bios and local storage with connections",
        "serverHardwareUri": "SH:MXQ73708NK, bay 3",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {"reapplyState": "NotApplying",
                               "connections": [
                                    {
                                        "id": 1,
                                        "name": "ETH",
                                        "functionType": "Ethernet",
                                        "portId": "Mezz 3:1-a",
                                        "requestedMbps": "2500",
                                        "networkUri": "ETH:net10",
                                        "boot": {
                                        },
                                    },
                                   {
                                        "id": 2,
                                        "name": "FC-a",
                                        "functionType": "FibreChannel",
                                        "portId": "Mezz 3:1-b",
                                        "requestedMbps": "4000",
                                        "networkUri": "FC:ovstsan216-240-a",
                                        "boot": {
                                        },
                                    },
                                   {
                                        "id": 3,
                                        "name": "FC-b",
                                        "functionType": "FibreChannel",
                                        "portId": "Mezz 3:2-b",
                                        "requestedMbps": "4000",
                                        "networkUri": "FC:ovstsan216-240-b",
                                        "boot": {
                                        },
                                    },
                               ]},
        "boot": {
            "manageBoot": True,
            "order": ["CD", "USB", 'HardDisk', "PXE"]
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": [{"id": "CustomPostMessage", "value": "WindowSysetm"}, {"id": "ServerPrimaryOs", "value": "Window10"}, {"id": "ServerOtherInfo", "value": "severos"}, {"id": "AdminName", "value": "OvstQuall"}, {"id": "AdminPhone", "value": "564654654645"}, {"id": "AdminEmail", "value": "OvstQuall@hpe.com"}, {"id": "AdminOtherInfo", "value": "OvstQuallRing7"}]
        },
        "hideUnusedFlexNics": True,
        "sanStorage": {
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        },
                    ],
                },
            ]

        },
    },
    {
        "uri": "SP:MXQ73705WF, bay 3",
        "name": "MXQ73705WF, bay 3",
        "type": "ServerProfileV11",
        "serverProfileTemplateUri": "SPT:DD-21RBay3-Gen9-Template",
        "serverHardwareUri": "SH:MXQ73705WF, bay 3",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {"reapplyState": "NotApplying",
                               "connections": [
                                    {
                                        "id": 1,
                                        "name": "ETH",
                                        "functionType": "Ethernet",
                                        "portId": "Mezz 3:1-a",
                                        "requestedMbps": "2500",
                                        "networkUri": "ETH:net10",
                                        "boot": {
                                        },
                                    },
                                   {
                                        "id": 2,
                                        "name": "FC-a",
                                        "functionType": "FibreChannel",
                                        "portId": "Mezz 3:1-b",
                                        "requestedMbps": "4000",
                                        "networkUri": "FC:ovstsan216-240-a",
                                        "boot": {
                                        },
                                    },
                                   {
                                        "id": 3,
                                        "name": "FC-b",
                                        "functionType": "FibreChannel",
                                        "portId": "Mezz 3:2-b",
                                        "requestedMbps": "4000",
                                        "networkUri": "FC:ovstsan216-240-b",
                                        "boot": {
                                        },
                                    },
                               ]},
        "hideUnusedFlexNics": True,
        "sanStorage": {
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        },
                    ],
                },
            ]

        },
        "status": "OK",
    },
    {
        "uri": "SP:MXQ73705W4, bay 8",
        "name": "MXQ73705W4, bay 8",
        "type": "ServerProfileV11",
        "serverProfileTemplateUri": "SPT:DD-21RBay10-Gen10-Template",
        "serverHardwareUri": "SH:MXQ73705W4, bay 8",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "reapplyState": "NotApplying",
            "connections": [
                {
                    "id": 1,
                    "name": "FC-a",
                    "functionType": "FibreChannel",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "networkUri": "FC:ovstsan216-240-a",
                    "boot": {

                    },
                },
                {
                    "id": 2,
                    "name": "FC-b",
                    "functionType": "FibreChannel",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "networkUri": "FC:ovstsan216-240-b",
                    "boot": {

                    },
                },
                {
                    "id": 3,
                    "name": "ETH",
                    "functionType": "Ethernet",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:net10",
                    "boot": {

                    },
                },
            ]
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
            "overriddenSettings": [{"id": "CustomPostMessage", "value": "WindowSysetm"}, {"id": "ServerPrimaryOs", "value": "Window10"}, {"id": "ServerOtherInfo", "value": "severos"}, {"id": "AdminName", "value": "OvstQuall"}, {"id": "AdminPhone", "value": "564654654645"}, {"id": "AdminEmail", "value": "OvstQuall@hpe.com"}, {"id": "AdminOtherInfo", "value": "OvstQuallRing7"}]
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorNameType": "AutoGenerated",
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
    }
]

server_profiles_from_spt = [
    {
        'name': 'MXQ73708NK, bay 3',
        'type': 'ServerProfileV11',
        'serverProfileTemplateUri': 'SPT:Bios and local storage with connections',
        'serverHardwareUri': 'SH:MXQ73708NK, bay 3',
    },
    {
        'name': 'MXQ73705WF, bay 3',
        'type': 'ServerProfileV11',
        'serverProfileTemplateUri': 'SPT:DD-21RBay3-Gen9-Template',
        'serverHardwareUri': 'SH:MXQ73705WF, bay 3',
    },
    {
        'name': 'MXQ73705W4, bay 8',
        'type': 'ServerProfileV11',
        'serverProfileTemplateUri': 'SPT:DD-21RBay10-Gen10-Template',
        'serverHardwareUri': 'SH:MXQ73705W4, bay 8'
    }
]

expected_server_profiles_from_spt = [
    {
        "uri": "SP:MXQ73708NK, bay 3",
        "name": "MXQ73708NK, bay 3",
        "type": "ServerProfileV11",
        "serverProfileTemplateUri": "SPT:Bios and local storage with connections",
        "serverHardwareUri": "SH:MXQ73708NK, bay 3",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {"reapplyState": "NotApplying",
                               "connections": [
                                    {
                                        "allocatedMbps": 2500,
                                        "functionType": "Ethernet",
                                        "id": 1,
                                        "macType": "Virtual",
                                        "maximumMbps": 10000,
                                        "name": "ETH",
                                        "portId": "Mezz 3:1-a",
                                        "requestedMbps": "2500",
                                        "wwnn": None,
                                        "wwpn": None,
                                        "networkUri": "ETH:net10"
                                    }
                               ]},
        "bootMode": {
            "manageMode": True,
            "pxeBootPolicy": "IPv4",
            "mode": "UEFI"
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": [{'id': 'AdminName', 'value': 'WPST Tester1'}, {'id': 'AdminPhone', 'value': '111-111-1111'}]
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "status": "OK",
    },
    {
        "uri": "SP:MXQ73705WF, bay 3",
        "name": "MXQ73705WF, bay 3",
        "type": "ServerProfileV11",
        "serverProfileTemplateUri": "SPT:DD-21RBay3-Gen9-Template",
        "serverHardwareUri": "SH:MXQ73705WF, bay 3",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {"reapplyState": "NotApplying", "connections": [
            {
                "allocatedMbps": 2500,
                "functionType": "Ethernet",
                "id": 1,
                "macType": "Virtual",
                "maximumMbps": 10000,
                "name": "ETH",
                "portId": "Mezz 3:1-a",
                "requestedMbps": "2500",
                "wwnn": None,
                "wwpn": None,
                "networkUri": "ETH:net10"
            }
        ]},
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "status": "OK",
    },
    {
        "uri": "SP:MXQ73705W4, bay 8",
        "status": "OK",
        "name": "MXQ73705W4, bay 8",
        "type": "ServerProfileV11",
        "serverProfileTemplateUri": "SPT:DD-21RBay10-Gen10-Template",
        "serverHardwareUri": "SH:MXQ73705W4, bay 8",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "reapplyState": "NotApplying",
            "connections": [
                {
                    "id": 1,
                    "name": "FC-a",
                    "functionType": "FibreChannel",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "networkUri": "FC:ovstsan216-240-a",
                    "boot": {
                    },
                },
                {
                    "id": 2,
                    "name": "FC-b",
                    "functionType": "FibreChannel",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "networkUri": "FC:ovstsan216-240-b",
                    "boot": {

                    },
                },
            ]
        },
        "bootMode": {
            "pxeBootPolicy": "IPv4",
            "manageMode": True,
            "mode": "UEFI"
        },
        "firmware": {
            "manageFirmware": False,
            "forceInstallFirmware": False
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": [{'id': 'AdminName', 'value': 'WPST Tester1'}, {'id': 'AdminPhone', 'value': '111-111-1111'}]
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorNameType": "AutoGenerated",
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 1,
                            "targetSelector": "Auto",
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ],
                },
            ]
        },
    }
]

server_profile_with_storage = [
    {
        "name": "MXQ73708NK, bay 2",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73708NK, bay 2",
        "enclosureUri": "ENC:MXQ73708NK",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-a",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:29",
                    "wwpn": "10:00:7e:77:18:50:00:28",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 6,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-b",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:2b",
                    "wwpn": "10:00:7e:77:18:50:00:2a",
                    "networkUri": "FC:ovstsan216-240-b",
                }
            ]
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": [{'id': 'AdminName', 'value': 'WPST Tester1'}, {'id': 'AdminPhone', 'value': '111-111-1111'}]
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "volume": None,
                    "id": 1,
                    "volumeUri": "SVOL:dd9-tbird-3bay2priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 1,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 2,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 6,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 3,
                    "volumeUri": "SVOL:ovstQR9-e3bay2-bfsDoNotDelFrom3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 6,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                }
            ]
        },
    },
    {
        "name": "MXQ73708NK, bay 1",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73708NK, bay 1",
        "enclosureUri": "ENC:MXQ73708NK",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-a",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:25",
                    "wwpn": "10:00:7e:77:18:50:00:24",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 2,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-b",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:27",
                    "wwpn": "10:00:7e:77:18:50:00:26",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 6,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                }
            ]
        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": "IPv4",
            "manageMode": True,
            "mode": "UEFIOptimized"
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
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "volume": None,
                    "id": 1,
                    "volumeUri": "SVOL:dd9-tbird-3bay1priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 2,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 3,
                    "volumeUri": "SVOL:ovstQR9-e3bay1-bfsDoNotDelFrom3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                }
            ]
        },
    },
    {
        "name": "MXQ73705WF, bay 5",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705WF, bay 5",
        "enclosureUri": "ENC:MXQ73705WF",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-a",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:11",
                    "wwpn": "10:00:7e:77:18:50:00:10",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 2,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-b",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:13",
                    "wwpn": "10:00:7e:77:18:50:00:12",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-a2",
                    "portId": "Mezz 6:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:15",
                    "wwpn": "10:00:7e:77:18:50:00:14",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-b2",
                    "portId": "Mezz 6:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:17",
                    "wwpn": "10:00:7e:77:18:50:00:16",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 6,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 7,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 8,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                }
            ]
        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": "IPv4",
            "manageMode": True,
            "mode": "UEFIOptimized"
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
            "sasLogicalJBODs": [{u'deviceSlot': u'Mezz 4', u'status': u'OK', u'driveMinSizeGB': 146, u'name': u'BBird2',
                                 u'driveMaxSizeGB': 146, u'eraseData': False, u'driveTechnology': u'SasHdd',
                                 u'numPhysicalDrives': 1, u'id': 2},
                                {u'deviceSlot': u'Mezz 1', u'status': u'OK', u'driveMinSizeGB': 146, u'name': u'BBird1',
                                 u'driveMaxSizeGB': 146, u'eraseData': False, u'driveTechnology': u'SasHdd',
                                 u'numPhysicalDrives': 1, u'id': 1}],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "volume": None,
                    "id": 1,
                    "volumeUri": "SVOL:dd9-tbird-2bay2priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 2,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 3,
                    "volumeUri": "SVOL:ovstQR9-e2bay5-bfsDoNotDelFrom3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                }
            ]
        },
    },
    {
        "name": "MXQ73705W4, bay 1",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705W4, bay 1",
        "enclosureUri": "ENC:MXQ73705W4",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-a",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:01",
                    "wwpn": "10:00:7e:77:18:50:00:00",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 2,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-b",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:03",
                    "wwpn": "10:00:7e:77:18:50:00:02",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 6,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                }
            ]
        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": "IPv4",
            "manageMode": True,
            "mode": "UEFIOptimized"
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
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "volume": None,
                    "id": 1,
                    "volumeUri": "SVOL:dd9-tbird-1bay1priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 2,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 3,
                    "volumeUri": "SVOL:ovstQR9-e1bay1-bfsDoNotDelFrom3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                }
            ]
        },
    },
    {
        "name": "MXQ73705WF, bay 6",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705WF, bay 6",
        "enclosureUri": "ENC:MXQ73705WF",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-a",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:19",
                    "wwpn": "10:00:7e:77:18:50:00:18",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 2,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-b",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:1b",
                    "wwpn": "10:00:7e:77:18:50:00:1a",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-a2",
                    "portId": "Mezz 6:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:1d",
                    "wwpn": "10:00:7e:77:18:50:00:1c",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-b2",
                    "portId": "Mezz 6:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:1f",
                    "wwpn": "10:00:7e:77:18:50:00:1e",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "Ethernet",
                    "id": 5,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "4000",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "Ethernet",
                    "id": 6,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "4000",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "Ethernet",
                    "id": 7,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "4000",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "Ethernet",
                    "id": 8,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "4000",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                }
            ]
        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": "IPv4",
            "manageMode": True,
            "mode": "UEFIOptimized"
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
            "sasLogicalJBODs": [{u'deviceSlot': u'Mezz 1', u'status': u'OK', u'driveMinSizeGB': 146, u'name': u'BBird1',
                                 u'driveMaxSizeGB': 146, u'eraseData': False, u'driveTechnology': u'SasHdd',
                                 u'numPhysicalDrives': 1, u'id': 1}],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "volume": None,
                    "id": 2,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 3,
                    "volumeUri": "SVOL:ovstQR9-e2bay6-bfsDoNotDelFrom3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 4,
                    "volumeUri": "SVOL:dd9-tbird-2bay3priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                }
            ]
        },
    },
    {
        "name": "MXQ73708NK, bay 8",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73708NK, bay 8",
        "enclosureUri": "ENC:MXQ73708NK",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-a",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:2d",
                    "wwpn": "10:00:7e:77:18:50:00:2c",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 2,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-b",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:2f",
                    "wwpn": "10:00:7e:77:18:50:00:2e",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:2-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 6,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                }
            ]
        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": "IPv4",
            "manageMode": True,
            "mode": "UEFIOptimized"
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
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "volume": None,
                    "id": 1,
                    "volumeUri": "SVOL:dd9-tbird-3bay3priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 2,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 3,
                    "volumeUri": "SVOL:ovstQR9-e3bay8-bfsDoNotDelFrom3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                }
            ]
        },
    },
    {
        "name": "MXQ73705W4, bay 2",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705W4, bay 2",
        "enclosureUri": "ENC:MXQ73705W4",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-a",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:05",
                    "wwpn": "10:00:7e:77:18:50:00:04",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 2,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-b",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:07",
                    "wwpn": "10:00:7e:77:18:50:00:06",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 6,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:2-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                }
            ]
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
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "volume": None,
                    "id": 1,
                    "volumeUri": "SVOL:dd9-tbird-1bay2priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 2,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 3,
                    "volumeUri": "SVOL:ovstQR9-e1bay2-bfsDoNotDelFrom3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 1,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                }
            ]
        },
    },
    {
        "name": "MXQ73705WF, bay 10",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705WF, bay 10",
        "enclosureUri": "ENC:MXQ73705WF",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-a",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:21",
                    "wwpn": "10:00:7e:77:18:50:00:20",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 2,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-b",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:23",
                    "wwpn": "10:00:7e:77:18:50:00:22",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 6,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                }
            ]
        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": "IPv4",
            "manageMode": True,
            "mode": "UEFIOptimized"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": [{'id': 'AdminName', 'value': 'WPST Tester1'}, {'id': 'AdminPhone', 'value': '111-111-1111'}]
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [{u'deviceSlot': u'Mezz 1', u'status': u'OK', u'driveMinSizeGB': 146, u'name': u'BBird1',
                                 u'driveMaxSizeGB': 146, u'eraseData': False, u'driveTechnology': u'SasHdd',
                                 u'numPhysicalDrives': 1, u'id': 1}],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "volume": None,
                    "id": 1,
                    "volumeUri": "SVOL:dd9-tbird-2bay4priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 2,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 1,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 3,
                    "volumeUri": "SVOL:ovstQR9-e2bay10-bfsDoNotDelFrm3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                }
            ]
        },
    },
    {
        "name": "MXQ73705W4, bay 8",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705W4, bay 8",
        "enclosureUri": "ENC:MXQ73705W4",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-a",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:09",
                    "wwpn": "10:00:7e:77:18:50:00:08",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 2,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-b",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:0b",
                    "wwpn": "10:00:7e:77:18:50:00:0a",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 6,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                }
            ]
        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": "IPv4",
            "manageMode": True,
            "mode": "UEFIOptimized"
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
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "volume": None,
                    "id": 1,
                    "volumeUri": "SVOL:dd9-tbird-1bay3priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 2,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 3,
                    "volumeUri": "SVOL:ovstQR9-e1bay8-bfsDoNotDelFrom3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 1,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                }
            ]
        },
    },
    {
        "name": "MXQ73705WF, bay 3",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705WF, bay 3",
        "enclosureUri": "ENC:MXQ73705WF",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-a",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:0d",
                    "wwpn": "10:00:7e:77:18:50:00:0c",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 2,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-b",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:0f",
                    "wwpn": "10:00:7e:77:18:50:00:0e",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 6,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                }
            ]
        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": "IPv4",
            "manageMode": True,
            "mode": "UEFIOptimized"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": [{'id': 'AdminName', 'value': 'WPST Tester1'}, {'id': 'AdminPhone', 'value': '111-111-1111'}]
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [{u'deviceSlot': u'Mezz 1', u'status': u'OK', u'driveMinSizeGB': 146, u'name': u'BBird1',
                                 u'driveMaxSizeGB': 146, u'eraseData': False, u'driveTechnology': u'SasHdd',
                                 u'numPhysicalDrives': 1, u'id': 1}],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "volume": None,
                    "id": 1,
                    "volumeUri": "SVOL:dd9-tbird-2bay1priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 2,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 3,
                    "volumeUri": "SVOL:ovstQR9-e2bay1-bfsDoNotDelFrom3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                }
            ]
        },
    }
]
expected_server_profile_with_storage = [
    {
        "uri": "SP:MXQ73708NK, bay 2",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9:3:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ73708NK, bay 2",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73708NK, bay 2",
        "enclosureUri": "ENC:MXQ73708NK",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "FC-a",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:29",
                    "wwpn": "10:00:7e:77:18:50:00:28",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 6,
                    "maximumMbps": 10000,
                    "name": "FC-b",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:2b",
                    "wwpn": "10:00:7e:77:18:50:00:2a",
                    "networkUri": "FC:ovstsan216-240-b",
                }
            ]
        },

        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": [{'id': 'AdminName', 'value': 'WPST Tester1'}, {'id': 'AdminPhone', 'value': '111-111-1111'}]
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "volume": None,
                    "id": 1,
                    "volumeUri": "SVOL:dd9-tbird-3bay2priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 1,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 2,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 6,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 3,
                    "volumeUri": "SVOL:ovstQR9-e3bay2-bfsDoNotDelFrom3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 6,
                            "targetSelector": "Auto",
                        }
                    ]
                }
            ]
        },
    },
    {
        "uri": "SP:MXQ73708NK, bay 1",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9:3:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ73708NK, bay 1",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73708NK, bay 1",
        "enclosureUri": "ENC:MXQ73708NK",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "FC-a",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:25",
                    "wwpn": "10:00:7e:77:18:50:00:24",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "FC-b",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:27",
                    "wwpn": "10:00:7e:77:18:50:00:26",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 6,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                }
            ]
        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": "IPv4",
            "manageMode": True,
            "mode": "UEFIOptimized"
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
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "volume": None,
                    "id": 1,
                    "volumeUri": "SVOL:dd9-tbird-3bay1priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 2,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 3,
                    "volumeUri": "SVOL:ovstQR9-e3bay1-bfsDoNotDelFrom3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                }
            ]
        },
    },
    {
        "uri": "SP:MXQ73705WF, bay 5",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 660 Gen9:1:Smart Array P542D Controller:3:Synergy 3820C 10/20Gb CNA:4:Smart Array P542D Controller:6:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ73705WF, bay 5",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705WF, bay 5",
        "enclosureUri": "ENC:MXQ73705WF",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "FC-a",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:11",
                    "wwpn": "10:00:7e:77:18:50:00:10",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "FC-b",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:13",
                    "wwpn": "10:00:7e:77:18:50:00:12",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "FC-a2",
                    "portId": "Mezz 6:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:15",
                    "wwpn": "10:00:7e:77:18:50:00:14",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "FC-b2",
                    "portId": "Mezz 6:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:17",
                    "wwpn": "10:00:7e:77:18:50:00:16",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 6,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 7,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 8,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                }
            ]
        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": "IPv4",
            "manageMode": True,
            "mode": "UEFIOptimized"
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
            "sasLogicalJBODs": [{u'deviceSlot': u'Mezz 4', u'status': u'OK', u'driveMinSizeGB': 146, u'name': u'BBird2',
                                 u'driveMaxSizeGB': 146, u'eraseData': False, u'driveTechnology': u'SasHdd',
                                 u'numPhysicalDrives': 1, u'id': 2},
                                {u'deviceSlot': u'Mezz 1', u'status': u'OK', u'driveMinSizeGB': 146, u'name': u'BBird1',
                                 u'driveMaxSizeGB': 146, u'eraseData': False, u'driveTechnology': u'SasHdd',
                                 u'numPhysicalDrives': 1, u'id': 1}],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "volume": None,
                    "id": 1,
                    "volumeUri": "SVOL:dd9-tbird-2bay2priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 2,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 3,
                    "volumeUri": "SVOL:ovstQR9-e2bay5-bfsDoNotDelFrom3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                }
            ]
        },
    },
    {
        "uri": "SP:MXQ73705W4, bay 1",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9 3:1:HP Synergy 3830C 16G FC HBA:3:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ73705W4, bay 1",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705W4, bay 1",
        "enclosureUri": "ENC:MXQ73705W4",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "FC-a",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:01",
                    "wwpn": "10:00:7e:77:18:50:00:00",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "FC-b",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:03",
                    "wwpn": "10:00:7e:77:18:50:00:02",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 6,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                }
            ]
        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": "IPv4",
            "manageMode": True,
            "mode": "UEFIOptimized"
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
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "volume": None,
                    "id": 1,
                    "volumeUri": "SVOL:dd9-tbird-1bay1priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 2,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 3,
                    "volumeUri": "SVOL:ovstQR9-e1bay1-bfsDoNotDelFrom3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                }
            ]
        },
    },
    {
        "uri": "SP:MXQ73705WF, bay 6",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 660 Gen10:1:HPE Smart Array P416ie-m SR G10:3:Synergy 3820C 10/20Gb CNA:6:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ73705WF, bay 6",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705WF, bay 6",
        "enclosureUri": "ENC:MXQ73705WF",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "FC-a",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:19",
                    "wwpn": "10:00:7e:77:18:50:00:18",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "FC-b",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:1b",
                    "wwpn": "10:00:7e:77:18:50:00:1a",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "FC-a2",
                    "portId": "Mezz 6:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:1d",
                    "wwpn": "10:00:7e:77:18:50:00:1c",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "FC-b2",
                    "portId": "Mezz 6:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:1f",
                    "wwpn": "10:00:7e:77:18:50:00:1e",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "Ethernet",
                    "id": 5,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "4000",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "Ethernet",
                    "id": 6,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "4000",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "Ethernet",
                    "id": 7,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "4000",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "Ethernet",
                    "id": 8,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "4000",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                }
            ]
        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": "IPv4",
            "manageMode": True,
            "mode": "UEFIOptimized"
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
            "sasLogicalJBODs": [{u'deviceSlot': u'Mezz 1', u'status': u'OK', u'driveMinSizeGB': 146, u'name': u'BBird1',
                                 u'driveMaxSizeGB': 146, u'eraseData': False, u'driveTechnology': u'SasHdd',
                                 u'numPhysicalDrives': 1, u'id': 1}],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "volume": None,
                    "id": 2,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 3,
                    "volumeUri": "SVOL:ovstQR9-e2bay6-bfsDoNotDelFrom3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 4,
                    "volumeUri": "SVOL:dd9-tbird-2bay3priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                }
            ]
        },
    },
    {
        "uri": "SP:MXQ73708NK, bay 8",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen10:3:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ73708NK, bay 8",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73708NK, bay 8",
        "enclosureUri": "ENC:MXQ73708NK",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "FC-a",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:2d",
                    "wwpn": "10:00:7e:77:18:50:00:2c",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "FC-b",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:2f",
                    "wwpn": "10:00:7e:77:18:50:00:2e",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:2-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 6,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                }
            ]
        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": "IPv4",
            "manageMode": True,
            "mode": "UEFIOptimized"
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
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "volume": None,
                    "id": 1,
                    "volumeUri": "SVOL:dd9-tbird-3bay3priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 2,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 3,
                    "volumeUri": "SVOL:ovstQR9-e3bay8-bfsDoNotDelFrom3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                }
            ]
        },
    },
    {
        "uri": "SP:MXQ73705W4, bay 2",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9 3:1:HP Synergy 3830C 16G FC HBA:3:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ73705W4, bay 2",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705W4, bay 2",
        "enclosureUri": "ENC:MXQ73705W4",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "FC-a",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:05",
                    "wwpn": "10:00:7e:77:18:50:00:04",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "FC-b",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:07",
                    "wwpn": "10:00:7e:77:18:50:00:06",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 6,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:2-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                }
            ]
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
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "volume": None,
                    "id": 1,
                    "volumeUri": "SVOL:dd9-tbird-1bay2priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 2,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 3,
                    "volumeUri": "SVOL:ovstQR9-e1bay2-bfsDoNotDelFrom3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 1,
                            "targetSelector": "Auto",
                        }
                    ]
                }
            ]
        },
    },
    {
        "uri": "SP:MXQ73705WF, bay 10",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen10:1:HPE Smart Array P416ie-m SR G10:3:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ73705WF, bay 10",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705WF, bay 10",
        "enclosureUri": "ENC:MXQ73705WF",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "FC-a",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:21",
                    "wwpn": "10:00:7e:77:18:50:00:20",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "FC-b",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:23",
                    "wwpn": "10:00:7e:77:18:50:00:22",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 6,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                }
            ]
        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": "IPv4",
            "manageMode": True,
            "mode": "UEFIOptimized"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": [{'id': 'AdminName', 'value': 'WPST Tester1'}, {'id': 'AdminPhone', 'value': '111-111-1111'}]
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [{u'deviceSlot': u'Mezz 1', u'status': u'OK', u'driveMinSizeGB': 146, u'name': u'BBird1',
                                 u'driveMaxSizeGB': 146, u'eraseData': False, u'driveTechnology': u'SasHdd',
                                 u'numPhysicalDrives': 1, u'id': 1}],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "volume": None,
                    "id": 1,
                    "volumeUri": "SVOL:dd9-tbird-2bay4priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 2,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 1,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 3,
                    "volumeUri": "SVOL:ovstQR9-e2bay10-bfsDoNotDelFrm3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                }
            ]
        },
    },
    {
        "uri": "SP:MXQ73705W4, bay 8",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen10:3:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ73705W4, bay 8",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705W4, bay 8",
        "enclosureUri": "ENC:MXQ73705W4",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "FC-a",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:09",
                    "wwpn": "10:00:7e:77:18:50:00:08",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "FC-b",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:0b",
                    "wwpn": "10:00:7e:77:18:50:00:0a",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 6,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                }
            ]
        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": "IPv4",
            "manageMode": True,
            "mode": "UEFIOptimized"
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
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "volume": None,
                    "id": 1,
                    "volumeUri": "SVOL:dd9-tbird-1bay3priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 2,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 3,
                    "volumeUri": "SVOL:ovstQR9-e1bay8-bfsDoNotDelFrom3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 1,
                            "targetSelector": "Auto",
                        }
                    ]
                }
            ]
        },
    },
    {
        "uri": "SP:MXQ73705WF, bay 3",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9:1:Smart Array P542D Controller:3:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ73705WF, bay 3",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705WF, bay 3",
        "enclosureUri": "ENC:MXQ73705WF",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "FC-a",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:0d",
                    "wwpn": "10:00:7e:77:18:50:00:0c",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "FC-b",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:0f",
                    "wwpn": "10:00:7e:77:18:50:00:0e",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 6,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                }
            ]
        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": "IPv4",
            "manageMode": True,
            "mode": "UEFIOptimized"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": [{'id': 'AdminName', 'value': 'WPST Tester1'}, {'id': 'AdminPhone', 'value': '111-111-1111'}]
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [{u'deviceSlot': u'Mezz 1', u'status': u'OK', u'driveMinSizeGB': 146, u'name': u'BBird1',
                                 u'driveMaxSizeGB': 146, u'eraseData': False, u'driveTechnology': u'SasHdd',
                                 u'numPhysicalDrives': 1, u'id': 1}],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "volume": None,
                    "id": 1,
                    "volumeUri": "SVOL:dd9-tbird-2bay1priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 2,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 3,
                    "volumeUri": "SVOL:ovstQR9-e2bay1-bfsDoNotDelFrom3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                }
            ]
        },
    }
]

edit_server_profile_with_storage = [
    {
        "name": "MXQ73708NK, bay 2",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73708NK, bay 2",
        "enclosureUri": "ENC:MXQ73708NK",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-a",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:29",
                    "wwpn": "10:00:7e:77:18:50:00:28",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 6,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-b",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:2b",
                    "wwpn": "10:00:7e:77:18:50:00:2a",
                    "networkUri": "FC:ovstsan216-240-b",
                }
            ]
        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": "IPv4",
            "manageMode": True,
            "mode": "UEFIOptimized"
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
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "volume": None,
                    "id": 1,
                    "volumeUri": "SVOL:dd9-tbird-3bay2priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 1,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 2,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 6,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 3,
                    "volumeUri": "SVOL:ovstQR9-e3bay2-bfsDoNotDelFrom3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 6,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                }
            ]
        },
    },
    {
        "name": "MXQ73708NK, bay 1",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73708NK, bay 1",
        "enclosureUri": "ENC:MXQ73708NK",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-a",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:25",
                    "wwpn": "10:00:7e:77:18:50:00:24",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 2,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-b",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:27",
                    "wwpn": "10:00:7e:77:18:50:00:26",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 6,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                }
            ]
        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": "IPv4",
            "manageMode": True,
            "mode": "UEFIOptimized"
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
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "volume": None,
                    "id": 1,
                    "volumeUri": "SVOL:dd9-tbird-3bay1priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 2,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 3,
                    "volumeUri": "SVOL:ovstQR9-e3bay1-bfsDoNotDelFrom3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                }
            ]
        },
    },
    {
        "name": "MXQ73705WF, bay 5",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705WF, bay 5",
        "enclosureUri": "ENC:MXQ73705WF",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-a",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:11",
                    "wwpn": "10:00:7e:77:18:50:00:10",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 2,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-b",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:13",
                    "wwpn": "10:00:7e:77:18:50:00:12",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-a2",
                    "portId": "Mezz 6:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:15",
                    "wwpn": "10:00:7e:77:18:50:00:14",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-b2",
                    "portId": "Mezz 6:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:17",
                    "wwpn": "10:00:7e:77:18:50:00:16",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 6,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 7,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 8,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                }
            ]
        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": "IPv4",
            "manageMode": True,
            "mode": "UEFIOptimized"
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
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "volume": None,
                    "id": 1,
                    "volumeUri": "SVOL:dd9-tbird-2bay2priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 2,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 3,
                    "volumeUri": "SVOL:ovstQR9-e2bay5-bfsDoNotDelFrom3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                }
            ]
        },
    },
    {
        "name": "MXQ73705W4, bay 1",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705W4, bay 1",
        "enclosureUri": "ENC:MXQ73705W4",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-a",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:01",
                    "wwpn": "10:00:7e:77:18:50:00:00",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 2,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-b",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:03",
                    "wwpn": "10:00:7e:77:18:50:00:02",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 6,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                }
            ]
        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": "IPv4",
            "manageMode": True,
            "mode": "UEFIOptimized"
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
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "volume": None,
                    "id": 1,
                    "volumeUri": "SVOL:dd9-tbird-1bay1priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 2,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 3,
                    "volumeUri": "SVOL:ovstQR9-e1bay1-bfsDoNotDelFrom3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                }
            ]
        },
    },
    {
        "name": "MXQ73705WF, bay 6",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705WF, bay 6",
        "enclosureUri": "ENC:MXQ73705WF",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-a",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:19",
                    "wwpn": "10:00:7e:77:18:50:00:18",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 2,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-b",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:1b",
                    "wwpn": "10:00:7e:77:18:50:00:1a",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-a2",
                    "portId": "Mezz 6:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:1d",
                    "wwpn": "10:00:7e:77:18:50:00:1c",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-b2",
                    "portId": "Mezz 6:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:1f",
                    "wwpn": "10:00:7e:77:18:50:00:1e",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "Ethernet",
                    "id": 5,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "4000",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "Ethernet",
                    "id": 6,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "4000",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "Ethernet",
                    "id": 7,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "4000",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "Ethernet",
                    "id": 8,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "4000",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                }
            ]
        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": "IPv4",
            "manageMode": True,
            "mode": "UEFIOptimized"
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
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "volume": None,
                    "id": 2,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 3,
                    "volumeUri": "SVOL:ovstQR9-e2bay6-bfsDoNotDelFrom3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 4,
                    "volumeUri": "SVOL:dd9-tbird-2bay3priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                }
            ]
        },
    },
    {
        "name": "MXQ73708NK, bay 8",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73708NK, bay 8",
        "enclosureUri": "ENC:MXQ73708NK",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-a",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:2d",
                    "wwpn": "10:00:7e:77:18:50:00:2c",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 2,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-b",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:2f",
                    "wwpn": "10:00:7e:77:18:50:00:2e",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:2-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 6,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                }
            ]
        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": "IPv4",
            "manageMode": True,
            "mode": "UEFIOptimized"
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
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "volume": None,
                    "id": 1,
                    "volumeUri": "SVOL:dd9-tbird-3bay3priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 2,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 3,
                    "volumeUri": "SVOL:ovstQR9-e3bay8-bfsDoNotDelFrom3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                }
            ]
        },
    },
    {
        "name": "MXQ73705W4, bay 2",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705W4, bay 2",
        "enclosureUri": "ENC:MXQ73705W4",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-a",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:05",
                    "wwpn": "10:00:7e:77:18:50:00:04",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 2,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-b",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:07",
                    "wwpn": "10:00:7e:77:18:50:00:06",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 6,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:2-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                }
            ]
        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": "IPv4",
            "manageMode": True,
            "mode": "UEFIOptimized"
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
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "volume": None,
                    "id": 1,
                    "volumeUri": "SVOL:dd9-tbird-1bay2priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 2,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 3,
                    "volumeUri": "SVOL:ovstQR9-e1bay2-bfsDoNotDelFrom3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 1,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                }
            ]
        },
    },
    {
        "name": "MXQ73705WF, bay 10",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705WF, bay 10",
        "enclosureUri": "ENC:MXQ73705WF",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-a",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:21",
                    "wwpn": "10:00:7e:77:18:50:00:20",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 2,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-b",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:23",
                    "wwpn": "10:00:7e:77:18:50:00:22",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 6,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                }
            ]
        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": "IPv4",
            "manageMode": True,
            "mode": "UEFIOptimized"
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
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "volume": None,
                    "id": 1,
                    "volumeUri": "SVOL:dd9-tbird-2bay4priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 2,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 1,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 3,
                    "volumeUri": "SVOL:ovstQR9-e2bay10-bfsDoNotDelFrm3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                }
            ]
        },
    },
    {
        "name": "MXQ73705W4, bay 8",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705W4, bay 8",
        "enclosureUri": "ENC:MXQ73705W4",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-a",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:09",
                    "wwpn": "10:00:7e:77:18:50:00:08",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 2,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-b",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:0b",
                    "wwpn": "10:00:7e:77:18:50:00:0a",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 6,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                }
            ]
        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": "IPv4",
            "manageMode": True,
            "mode": "UEFIOptimized"
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
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "volume": None,
                    "id": 1,
                    "volumeUri": "SVOL:dd9-tbird-1bay3priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 2,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 3,
                    "volumeUri": "SVOL:ovstQR9-e1bay8-bfsDoNotDelFrom3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 1,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                }
            ]
        },
    },
    {
        "name": "MXQ73705WF, bay 3",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705WF, bay 3",
        "enclosureUri": "ENC:MXQ73705WF",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-a",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:0d",
                    "wwpn": "10:00:7e:77:18:50:00:0c",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 2,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-b",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:0f",
                    "wwpn": "10:00:7e:77:18:50:00:0e",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 6,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                }
            ]
        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": "IPv4",
            "manageMode": True,
            "mode": "UEFIOptimized"
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
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "volume": None,
                    "id": 1,
                    "volumeUri": "SVOL:dd9-tbird-2bay1priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 2,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 3,
                    "volumeUri": "SVOL:ovstQR9-e2bay1-bfsDoNotDelFrom3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                }
            ]
        },
    }
]
expected_edit_server_profile_with_storage = [
    {
        "uri": "SP:MXQ73708NK, bay 2",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9:3:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ73708NK, bay 2",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73708NK, bay 2",
        "enclosureUri": "ENC:MXQ73708NK",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "FC-a",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:29",
                    "wwpn": "10:00:7e:77:18:50:00:28",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 6,
                    "maximumMbps": 10000,
                    "name": "FC-b",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:2b",
                    "wwpn": "10:00:7e:77:18:50:00:2a",
                    "networkUri": "FC:ovstsan216-240-b",
                }
            ]
        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": "IPv4",
            "manageMode": True,
            "mode": "UEFIOptimized"
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
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "volume": None,
                    "id": 1,
                    "volumeUri": "SVOL:dd9-tbird-3bay2priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 1,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 2,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 6,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 3,
                    "volumeUri": "SVOL:ovstQR9-e3bay2-bfsDoNotDelFrom3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 6,
                            "targetSelector": "Auto",
                        }
                    ]
                }
            ]
        },
    },
    {
        "uri": "SP:MXQ73708NK, bay 1",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9:3:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ73708NK, bay 1",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73708NK, bay 1",
        "enclosureUri": "ENC:MXQ73708NK",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "FC-a",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:25",
                    "wwpn": "10:00:7e:77:18:50:00:24",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "FC-b",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:27",
                    "wwpn": "10:00:7e:77:18:50:00:26",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 6,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                }
            ]
        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": "IPv4",
            "manageMode": True,
            "mode": "UEFIOptimized"
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
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "volume": None,
                    "id": 1,
                    "volumeUri": "SVOL:dd9-tbird-3bay1priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 2,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 3,
                    "volumeUri": "SVOL:ovstQR9-e3bay1-bfsDoNotDelFrom3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                }
            ]
        },
    },
    {
        "uri": "SP:MXQ73705WF, bay 5",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 660 Gen9:1:Smart Array P542D Controller:3:Synergy 3820C 10/20Gb CNA:4:Smart Array P542D Controller:6:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ73705WF, bay 5",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705WF, bay 5",
        "enclosureUri": "ENC:MXQ73705WF",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "FC-a",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:11",
                    "wwpn": "10:00:7e:77:18:50:00:10",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "FC-b",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:13",
                    "wwpn": "10:00:7e:77:18:50:00:12",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "FC-a2",
                    "portId": "Mezz 6:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:15",
                    "wwpn": "10:00:7e:77:18:50:00:14",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "FC-b2",
                    "portId": "Mezz 6:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:17",
                    "wwpn": "10:00:7e:77:18:50:00:16",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 6,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 7,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 8,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                }
            ]
        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": "IPv4",
            "manageMode": True,
            "mode": "UEFIOptimized"
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
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "volume": None,
                    "id": 1,
                    "volumeUri": "SVOL:dd9-tbird-2bay2priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 2,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 3,
                    "volumeUri": "SVOL:ovstQR9-e2bay5-bfsDoNotDelFrom3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                }
            ]
        },
    },
    {
        "uri": "SP:MXQ73705W4, bay 1",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9 3:1:HP Synergy 3830C 16G FC HBA:3:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ73705W4, bay 1",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705W4, bay 1",
        "enclosureUri": "ENC:MXQ73705W4",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "FC-a",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:01",
                    "wwpn": "10:00:7e:77:18:50:00:00",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "FC-b",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:03",
                    "wwpn": "10:00:7e:77:18:50:00:02",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 6,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                }
            ]
        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": "IPv4",
            "manageMode": True,
            "mode": "UEFIOptimized"
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
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "volume": None,
                    "id": 1,
                    "volumeUri": "SVOL:dd9-tbird-1bay1priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 2,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 3,
                    "volumeUri": "SVOL:ovstQR9-e1bay1-bfsDoNotDelFrom3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                }
            ]
        },
    },
    {
        "uri": "SP:MXQ73705WF, bay 6",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 660 Gen10:1:HPE Smart Array P416ie-m SR G10:3:Synergy 3820C 10/20Gb CNA:6:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ73705WF, bay 6",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705WF, bay 6",
        "enclosureUri": "ENC:MXQ73705WF",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "FC-a",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:19",
                    "wwpn": "10:00:7e:77:18:50:00:18",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "FC-b",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:1b",
                    "wwpn": "10:00:7e:77:18:50:00:1a",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "FC-a2",
                    "portId": "Mezz 6:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:1d",
                    "wwpn": "10:00:7e:77:18:50:00:1c",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "FC-b2",
                    "portId": "Mezz 6:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:1f",
                    "wwpn": "10:00:7e:77:18:50:00:1e",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "Ethernet",
                    "id": 5,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "4000",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "Ethernet",
                    "id": 6,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "4000",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "Ethernet",
                    "id": 7,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "4000",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "Ethernet",
                    "id": 8,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "4000",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                }
            ]
        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": "IPv4",
            "manageMode": True,
            "mode": "UEFIOptimized"
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
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "volume": None,
                    "id": 2,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 3,
                    "volumeUri": "SVOL:ovstQR9-e2bay6-bfsDoNotDelFrom3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 4,
                    "volumeUri": "SVOL:dd9-tbird-2bay3priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                }
            ]
        },
    },
    {
        "uri": "SP:MXQ73708NK, bay 8",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen10:3:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ73708NK, bay 8",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73708NK, bay 8",
        "enclosureUri": "ENC:MXQ73708NK",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "FC-a",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:2d",
                    "wwpn": "10:00:7e:77:18:50:00:2c",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "FC-b",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:2f",
                    "wwpn": "10:00:7e:77:18:50:00:2e",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:2-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 6,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                }
            ]
        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": "IPv4",
            "manageMode": True,
            "mode": "UEFIOptimized"
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
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "volume": None,
                    "id": 1,
                    "volumeUri": "SVOL:dd9-tbird-3bay3priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 2,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 3,
                    "volumeUri": "SVOL:ovstQR9-e3bay8-bfsDoNotDelFrom3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                }
            ]
        },
    },
    {
        "uri": "SP:MXQ73705W4, bay 2",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9 3:1:HP Synergy 3830C 16G FC HBA:3:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ73705W4, bay 2",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705W4, bay 2",
        "enclosureUri": "ENC:MXQ73705W4",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "FC-a",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:05",
                    "wwpn": "10:00:7e:77:18:50:00:04",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "FC-b",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:07",
                    "wwpn": "10:00:7e:77:18:50:00:06",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 6,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:2-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                }
            ]
        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": "IPv4",
            "manageMode": True,
            "mode": "UEFIOptimized"
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
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "volume": None,
                    "id": 1,
                    "volumeUri": "SVOL:dd9-tbird-1bay2priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 2,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 3,
                    "volumeUri": "SVOL:ovstQR9-e1bay2-bfsDoNotDelFrom3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 1,
                            "targetSelector": "Auto",
                        }
                    ]
                }
            ]
        },
    },
    {
        "uri": "SP:MXQ73705WF, bay 10",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen10:1:HPE Smart Array P416ie-m SR G10:3:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ73705WF, bay 10",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705WF, bay 10",
        "enclosureUri": "ENC:MXQ73705WF",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "FC-a",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:21",
                    "wwpn": "10:00:7e:77:18:50:00:20",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "FC-b",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:23",
                    "wwpn": "10:00:7e:77:18:50:00:22",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 6,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                }
            ]
        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": "IPv4",
            "manageMode": True,
            "mode": "UEFIOptimized"
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
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "volume": None,
                    "id": 1,
                    "volumeUri": "SVOL:dd9-tbird-2bay4priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 2,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 1,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 3,
                    "volumeUri": "SVOL:ovstQR9-e2bay10-bfsDoNotDelFrm3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                }
            ]
        },
    },
    {
        "uri": "SP:MXQ73705W4, bay 8",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen10:3:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ73705W4, bay 8",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705W4, bay 8",
        "enclosureUri": "ENC:MXQ73705W4",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "FC-a",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:09",
                    "wwpn": "10:00:7e:77:18:50:00:08",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "FC-b",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:0b",
                    "wwpn": "10:00:7e:77:18:50:00:0a",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 6,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                }
            ]
        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": "IPv4",
            "manageMode": True,
            "mode": "UEFIOptimized"
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
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "volume": None,
                    "id": 1,
                    "volumeUri": "SVOL:dd9-tbird-1bay3priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 2,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 3,
                    "volumeUri": "SVOL:ovstQR9-e1bay8-bfsDoNotDelFrom3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 1,
                            "targetSelector": "Auto",
                        }
                    ]
                }
            ]
        },
    },
    {
        "uri": "SP:MXQ73705WF, bay 3",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9:1:Smart Array P542D Controller:3:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ73705WF, bay 3",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705WF, bay 3",
        "enclosureUri": "ENC:MXQ73705WF",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "FC-a",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:0d",
                    "wwpn": "10:00:7e:77:18:50:00:0c",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "FC-b",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:0f",
                    "wwpn": "10:00:7e:77:18:50:00:0e",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 6,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                }
            ]
        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": "IPv4",
            "manageMode": True,
            "mode": "UEFIOptimized"
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
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "volume": None,
                    "id": 1,
                    "volumeUri": "SVOL:dd9-tbird-2bay1priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 2,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 3,
                    "volumeUri": "SVOL:ovstQR9-e2bay1-bfsDoNotDelFrom3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                }
            ]
        },
    }
]

update_server_profile_with_storage = [
    {
        "name": "MXQ73708NK, bay 2",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73708NK, bay 2",
        "enclosureUri": "ENC:MXQ73708NK",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "MXQ73708NK, bay 2 is updated with new Eth, FC connections, Bios, BootSettings and sansorage",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-a",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:29",
                    "wwpn": "10:00:7e:77:18:50:00:28",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 6,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-b",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:2b",
                    "wwpn": "10:00:7e:77:18:50:00:2a",
                    "networkUri": "FC:ovstsan216-240-b",
                },

            ]
        },
        "boot": {
            "manageBoot": True,
            "order": ["CD", "USB", 'HardDisk', "PXE"]
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
            "overriddenSettings": [{"id": "CustomPostMessage", "value": "WindowSysetm"}, {"id": "ServerPrimaryOs", "value": "Window10"}, {"id": "ServerOtherInfo", "value": "severos"}, {"id": "AdminName", "value": "OvstQuall"}, {"id": "AdminPhone", "value": "564654654645"}, {"id": "AdminEmail", "value": "OvstQuall@hpe.com"}, {"id": "AdminOtherInfo", "value": "OvstQuallRing7"}]
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "volume": None,
                    "id": 1,
                    "volumeUri": "SVOL:dd9-tbird-3bay2priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 1,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 2,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 6,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 3,
                    "volumeUri": "SVOL:ovstQR9-e3bay2-bfsDoNotDelFrom3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 6,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 4,
                    "volumeUri": "SVOL:dd9-tbird-1bay4priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "4",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 1,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
            ]
        },
    },
    {
        "name": "MXQ73708NK, bay 1",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73708NK, bay 1",
        "enclosureUri": "ENC:MXQ73708NK",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "MXQ73708NK, bay 1 is updated with new Eth, FC connections, Bios, BootSettings and sansorage",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-a",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:25",
                    "wwpn": "10:00:7e:77:18:50:00:24",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 2,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-b",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:27",
                    "wwpn": "10:00:7e:77:18:50:00:26",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 6,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                }
            ]
        },
        "boot": {
            "manageBoot": True,
            "order": ["CD", "USB", 'HardDisk', "PXE"]
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
            "overriddenSettings": [{"id": "CustomPostMessage", "value": "WindowSysetm"}, {"id": "ServerPrimaryOs", "value": "Window10"}, {"id": "ServerOtherInfo", "value": "severos"}, {"id": "AdminName", "value": "OvstQuall"}, {"id": "AdminPhone", "value": "564654654645"}, {"id": "AdminEmail", "value": "OvstQuall@hpe.com"}, {"id": "AdminOtherInfo", "value": "OvstQuallRing7"}]
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "volume": None,
                    "id": 2,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 3,
                    "volumeUri": "SVOL:ovstQR9-e3bay1-bfsDoNotDelFrom3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 4,
                    "volumeUri": "SVOL:dd9-tbird-2bay5priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "4",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
            ]
        },
    },
    {
        "name": "MXQ73705WF, bay 5",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705WF, bay 5",
        "enclosureUri": "ENC:MXQ73705WF",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "MXQ73705WF, bay 5 is updated with new Eth, FC connections, Bios, BootSettings and sansorage",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-a",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:11",
                    "wwpn": "10:00:7e:77:18:50:00:10",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 2,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-b",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:13",
                    "wwpn": "10:00:7e:77:18:50:00:12",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-a2",
                    "portId": "Mezz 6:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:15",
                    "wwpn": "10:00:7e:77:18:50:00:14",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-b2",
                    "portId": "Mezz 6:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:17",
                    "wwpn": "10:00:7e:77:18:50:00:16",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 6,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 7,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 8,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                }
            ]
        },
        "boot": {
            "manageBoot": True,
            "order": ["CD", "USB", 'HardDisk', "PXE"]
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
            "overriddenSettings": [{"id": "CustomPostMessage", "value": "WindowSysetm"}, {"id": "ServerPrimaryOs", "value": "Window10"}, {"id": "ServerOtherInfo", "value": "severos"}, {"id": "AdminName", "value": "OvstQuall"}, {"id": "AdminPhone", "value": "564654654645"}, {"id": "AdminEmail", "value": "OvstQuall@hpe.com"}, {"id": "AdminOtherInfo", "value": "OvstQuallRing7"}]
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [{u'deviceSlot': u'Mezz 4', u'status': u'OK', u'driveMinSizeGB': 146, u'name': u'BBird2',
                                 u'driveMaxSizeGB': 146, u'eraseData': False, u'driveTechnology': u'SasHdd',
                                 u'numPhysicalDrives': 1, u'id': 2},
                                {u'deviceSlot': u'Mezz 1', u'status': u'OK', u'driveMinSizeGB': 146, u'name': u'BBird1',
                                 u'driveMaxSizeGB': 146, u'eraseData': False, u'driveTechnology': u'SasHdd',
                                 u'numPhysicalDrives': 1, u'id': 1}],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "volume": None,
                    "id": 1,
                    "volumeUri": "SVOL:dd9-tbird-2bay2priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 3,
                    "volumeUri": "SVOL:ovstQR9-e2bay5-bfsDoNotDelFrom3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                }
            ]
        },
    },
    {
        "name": "MXQ73705W4, bay 1",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705W4, bay 1",
        "enclosureUri": "ENC:MXQ73705W4",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "MXQ73705W4, bay 1 is updated with new Eth, FC connections, Bios, BootSettings and sansorage",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-a",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:01",
                    "wwpn": "10:00:7e:77:18:50:00:00",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 2,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-b",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:03",
                    "wwpn": "10:00:7e:77:18:50:00:02",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 6,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                }
            ]
        },
        "boot": {
            "manageBoot": True,
            "order": ["CD", "USB", 'HardDisk', "PXE"]
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
            "overriddenSettings": [{"id": "CustomPostMessage", "value": "WindowSysetm"}, {"id": "ServerPrimaryOs", "value": "Window10"}, {"id": "ServerOtherInfo", "value": "severos"}, {"id": "AdminName", "value": "OvstQuall"}, {"id": "AdminPhone", "value": "564654654645"}, {"id": "AdminEmail", "value": "OvstQuall@hpe.com"}, {"id": "AdminOtherInfo", "value": "OvstQuallRing7"}]
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "volume": None,
                    "id": 1,
                    "volumeUri": "SVOL:dd9-tbird-1bay1priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 2,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 3,
                    "volumeUri": "SVOL:ovstQR9-e1bay1-bfsDoNotDelFrom3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 4,
                    "volumeUri": "SVOL:ovstQR9-e1bay5-bfsDoNotDelFrom3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "4",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
            ]
        },
    },
    {
        "name": "MXQ73705WF, bay 6",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705WF, bay 6",
        "enclosureUri": "ENC:MXQ73705WF",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "MXQ73705WF, bay 6 is updated with new Eth, FC connections, Bios, BootSettings and sansorage",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-a",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:19",
                    "wwpn": "10:00:7e:77:18:50:00:18",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 2,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-b",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:1b",
                    "wwpn": "10:00:7e:77:18:50:00:1a",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-a2",
                    "portId": "Mezz 6:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:1d",
                    "wwpn": "10:00:7e:77:18:50:00:1c",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-b2",
                    "portId": "Mezz 6:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:1f",
                    "wwpn": "10:00:7e:77:18:50:00:1e",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "Ethernet",
                    "id": 5,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "4000",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "Ethernet",
                    "id": 6,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "4000",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "Ethernet",
                    "id": 7,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "4000",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "Ethernet",
                    "id": 8,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "4000",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                }
            ]
        },
        "boot": {
            "manageBoot": True,
            "order": ["CD", "USB", 'HardDisk', "PXE"]
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
            "overriddenSettings": [{"id": "CustomPostMessage", "value": "WindowSysetm"}, {"id": "ServerPrimaryOs", "value": "Window10"}, {"id": "ServerOtherInfo", "value": "severos"}, {"id": "AdminName", "value": "OvstQuall"}, {"id": "AdminPhone", "value": "564654654645"}, {"id": "AdminEmail", "value": "OvstQuall@hpe.com"}, {"id": "AdminOtherInfo", "value": "OvstQuallRing7"}]
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [{u'deviceSlot': u'Mezz 1', u'status': u'OK', u'driveMinSizeGB': 146, u'name': u'BBird1',
                                 u'driveMaxSizeGB': 146, u'eraseData': False, u'driveTechnology': u'SasHdd',
                                 u'numPhysicalDrives': 1, u'id': 1}],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "volume": None,
                    "id": 2,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 4,
                    "volumeUri": "SVOL:dd9-tbird-2bay3priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                }
            ]
        },
    },
    {
        "name": "MXQ73708NK, bay 8",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73708NK, bay 8",
        "enclosureUri": "ENC:MXQ73708NK",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "MXQ73708NK, bay 8 is updated with new Eth, FC connections, Bios, BootSettings and sansorage",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-a",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:2d",
                    "wwpn": "10:00:7e:77:18:50:00:2c",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 2,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-b",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:2f",
                    "wwpn": "10:00:7e:77:18:50:00:2e",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:2-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 6,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                }
            ]
        },
        "boot": {
            "manageBoot": True,
            "order": ["CD", "USB", 'HardDisk', "PXE"]
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
            "overriddenSettings": [{"id": "CustomPostMessage", "value": "WindowSysetm"}, {"id": "ServerPrimaryOs", "value": "Window10"}, {"id": "ServerOtherInfo", "value": "severos"}, {"id": "AdminName", "value": "OvstQuall"}, {"id": "AdminPhone", "value": "564654654645"}, {"id": "AdminEmail", "value": "OvstQuall@hpe.com"}, {"id": "AdminOtherInfo", "value": "OvstQuallRing7"}]
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "volume": None,
                    "id": 1,
                    "volumeUri": "SVOL:dd9-tbird-3bay3priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 2,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 3,
                    "volumeUri": "SVOL:ovstQR9-e3bay8-bfsDoNotDelFrom3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 4,
                    "volumeUri": "SVOL:ovstQR9-e3bay5-bfsDoNotDelFrom3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "4",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
            ]
        },
    },
    {
        "name": "MXQ73705W4, bay 2",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705W4, bay 2",
        "enclosureUri": "ENC:MXQ73705W4",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "MXQ73705W4, bay 2 is updated with new Eth, FC connections, Bios, BootSettings and sansorage",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-a",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:05",
                    "wwpn": "10:00:7e:77:18:50:00:04",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 2,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-b",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:07",
                    "wwpn": "10:00:7e:77:18:50:00:06",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 6,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:2-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                }
            ]
        },
        "boot": {
            "manageBoot": True,
            "order": ["CD", "USB", 'HardDisk', "PXE"]
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
            "overriddenSettings": [{"id": "CustomPostMessage", "value": "WindowSysetm"}, {"id": "ServerPrimaryOs", "value": "Window10"}, {"id": "ServerOtherInfo", "value": "severos"}, {"id": "AdminName", "value": "OvstQuall"}, {"id": "AdminPhone", "value": "564654654645"}, {"id": "AdminEmail", "value": "OvstQuall@hpe.com"}, {"id": "AdminOtherInfo", "value": "OvstQuallRing7"}]
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "volume": None,
                    "id": 1,
                    "volumeUri": "SVOL:dd9-tbird-1bay2priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 2,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 3,
                    "volumeUri": "SVOL:ovstQR9-e1bay2-bfsDoNotDelFrom3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 1,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 4,
                    "volumeUri": "SVOL:ovstQR9-e2bay2-bfsDoNotDelFrom3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "4",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 1,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                }
            ]
        },
    },
    {
        "name": "MXQ73705WF, bay 10",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705WF, bay 10",
        "enclosureUri": "ENC:MXQ73705WF",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "MXQ73705WF, bay 10 is updated with new Eth, FC connections, Bios, BootSettings and sansorage",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-a",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:21",
                    "wwpn": "10:00:7e:77:18:50:00:20",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 2,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-b",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:23",
                    "wwpn": "10:00:7e:77:18:50:00:22",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 6,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                }
            ]
        },
        "boot": {
            "manageBoot": True,
            "order": ["CD", "USB", 'HardDisk', "PXE"]
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
            "overriddenSettings": [{"id": "CustomPostMessage", "value": "WindowSysetm"}, {"id": "ServerPrimaryOs", "value": "Window10"}, {"id": "ServerOtherInfo", "value": "severos"}, {"id": "AdminName", "value": "OvstQuall"}, {"id": "AdminPhone", "value": "564654654645"}, {"id": "AdminEmail", "value": "OvstQuall@hpe.com"}, {"id": "AdminOtherInfo", "value": "OvstQuallRing7"}]
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [{u'deviceSlot': u'Mezz 1', u'status': u'OK', u'driveMinSizeGB': 146, u'name': u'BBird1',
                                 u'driveMaxSizeGB': 146, u'eraseData': False, u'driveTechnology': u'SasHdd',
                                 u'numPhysicalDrives': 1, u'id': 1}],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "volume": None,
                    "id": 1,
                    "volumeUri": "SVOL:dd9-tbird-2bay4priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 2,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 1,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
            ]
        },
    },
    {
        "name": "MXQ73705W4, bay 8",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705W4, bay 8",
        "enclosureUri": "ENC:MXQ73705W4",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "MXQ73705W4, bay 8 is updated with new Eth, FC connections, Bios, BootSettings and sansorage",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-a",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:09",
                    "wwpn": "10:00:7e:77:18:50:00:08",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 2,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-b",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:0b",
                    "wwpn": "10:00:7e:77:18:50:00:0a",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 6,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                }
            ]
        },
        "boot": {
            "manageBoot": True,
            "order": ["CD", "USB", 'HardDisk', "PXE"]
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
            "overriddenSettings": [{"id": "CustomPostMessage", "value": "WindowSysetm"}, {"id": "ServerPrimaryOs", "value": "Window10"}, {"id": "ServerOtherInfo", "value": "severos"}, {"id": "AdminName", "value": "OvstQuall"}, {"id": "AdminPhone", "value": "564654654645"}, {"id": "AdminEmail", "value": "OvstQuall@hpe.com"}, {"id": "AdminOtherInfo", "value": "OvstQuallRing7"}]
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "volume": None,
                    "id": 1,
                    "volumeUri": "SVOL:dd9-tbird-1bay3priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 2,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 3,
                    "volumeUri": "SVOL:ovstQR9-e1bay8-bfsDoNotDelFrom3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 1,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 4,
                    "volumeUri": "SVOL:dd9-tbird-3bay4priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "4",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
            ]
        },
    },
    {
        "name": "MXQ73705WF, bay 3",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705WF, bay 3",
        "enclosureUri": "ENC:MXQ73705WF",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "MXQ73705WF, bay 3 is updated with new Eth, FC connections, Bios, BootSettings and sansorage",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-a",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:0d",
                    "wwpn": "10:00:7e:77:18:50:00:0c",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 2,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "FC-b",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:0f",
                    "wwpn": "10:00:7e:77:18:50:00:0e",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 6,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                }
            ]
        },
        "boot": {
            "manageBoot": True,
            "order": ["CD", "USB", 'HardDisk', "PXE"]
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
            "overriddenSettings": [{"id": "CustomPostMessage", "value": "WindowSysetm"}, {"id": "ServerPrimaryOs", "value": "Window10"}, {"id": "ServerOtherInfo", "value": "severos"}, {"id": "AdminName", "value": "OvstQuall"}, {"id": "AdminPhone", "value": "564654654645"}, {"id": "AdminEmail", "value": "OvstQuall@hpe.com"}, {"id": "AdminOtherInfo", "value": "OvstQuallRing7"}]
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [{u'deviceSlot': u'Mezz 1', u'status': u'OK', u'driveMinSizeGB': 146, u'name': u'BBird1',
                                 u'driveMaxSizeGB': 146, u'eraseData': False, u'driveTechnology': u'SasHdd',
                                 u'numPhysicalDrives': 1, u'id': 1}],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "volume": None,
                    "id": 1,
                    "volumeUri": "SVOL:dd9-tbird-2bay1priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 3,
                    "volumeUri": "SVOL:ovstQR9-e2bay1-bfsDoNotDelFrom3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                }
            ]
        },
    }
]
expected_update_server_profile_with_storage = [
    {
        "uri": "SP:MXQ73708NK, bay 2",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9:3:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ73708NK, bay 2",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73708NK, bay 2",
        "enclosureUri": "ENC:MXQ73708NK",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "MXQ73708NK, bay 2 is updated with new Eth, FC connections, Bios, BootSettings and sansorage",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "FC-a",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:29",
                    "wwpn": "10:00:7e:77:18:50:00:28",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 6,
                    "maximumMbps": 10000,
                    "name": "FC-b",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:2b",
                    "wwpn": "10:00:7e:77:18:50:00:2a",
                    "networkUri": "FC:ovstsan216-240-b",
                }
            ]
        },
        "boot": {
            "manageBoot": True,
            "order": ["CD", "USB", 'HardDisk', "PXE"]
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
            "overriddenSettings": [{"id": "CustomPostMessage", "value": "WindowSysetm"}, {"id": "ServerPrimaryOs", "value": "Window10"}, {"id": "ServerOtherInfo", "value": "severos"}, {"id": "AdminName", "value": "OvstQuall"}, {"id": "AdminPhone", "value": "564654654645"}, {"id": "AdminEmail", "value": "OvstQuall@hpe.com"}, {"id": "AdminOtherInfo", "value": "OvstQuallRing7"}]
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "volume": None,
                    "id": 1,
                    "volumeUri": "SVOL:dd9-tbird-3bay2priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 1,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 2,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 6,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 3,
                    "volumeUri": "SVOL:ovstQR9-e3bay2-bfsDoNotDelFrom3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 6,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 4,
                    "volumeUri": "SVOL:dd9-tbird-1bay4priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "4",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 1,
                            "targetSelector": "Auto",
                        }
                    ]
                },
            ]
        },
    },
    {
        "uri": "SP:MXQ73708NK, bay 1",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9:3:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ73708NK, bay 1",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73708NK, bay 1",
        "enclosureUri": "ENC:MXQ73708NK",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "MXQ73708NK, bay 1 is updated with new Eth, FC connections, Bios, BootSettings and sansorage",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "FC-a",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:25",
                    "wwpn": "10:00:7e:77:18:50:00:24",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "FC-b",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:27",
                    "wwpn": "10:00:7e:77:18:50:00:26",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 6,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                }
            ]
        },
        "boot": {
            "manageBoot": True,
            "order": ["CD", "USB", 'HardDisk', "PXE"]
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
            "overriddenSettings": [{"id": "CustomPostMessage", "value": "WindowSysetm"}, {"id": "ServerPrimaryOs", "value": "Window10"}, {"id": "ServerOtherInfo", "value": "severos"}, {"id": "AdminName", "value": "OvstQuall"}, {"id": "AdminPhone", "value": "564654654645"}, {"id": "AdminEmail", "value": "OvstQuall@hpe.com"}, {"id": "AdminOtherInfo", "value": "OvstQuallRing7"}]
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "volume": None,
                    "id": 2,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 3,
                    "volumeUri": "SVOL:ovstQR9-e3bay1-bfsDoNotDelFrom3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 4,
                    "volumeUri": "SVOL:dd9-tbird-2bay5priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "4",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                },
            ]
        },
    },
    {
        "uri": "SP:MXQ73705WF, bay 5",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 660 Gen9:1:Smart Array P542D Controller:3:Synergy 3820C 10/20Gb CNA:4:Smart Array P542D Controller:6:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ73705WF, bay 5",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705WF, bay 5",
        "enclosureUri": "ENC:MXQ73705WF",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "MXQ73705WF, bay 5 is updated with new Eth, FC connections, Bios, BootSettings and sansorage",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "FC-a",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:11",
                    "wwpn": "10:00:7e:77:18:50:00:10",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "FC-b",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:13",
                    "wwpn": "10:00:7e:77:18:50:00:12",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "FC-a2",
                    "portId": "Mezz 6:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:15",
                    "wwpn": "10:00:7e:77:18:50:00:14",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "FC-b2",
                    "portId": "Mezz 6:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:17",
                    "wwpn": "10:00:7e:77:18:50:00:16",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 6,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 7,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 8,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                }
            ]
        },
        "boot": {
            "manageBoot": True,
            "order": ["CD", "USB", 'HardDisk', "PXE"]
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
            "overriddenSettings": [{"id": "CustomPostMessage", "value": "WindowSysetm"}, {"id": "ServerPrimaryOs", "value": "Window10"}, {"id": "ServerOtherInfo", "value": "severos"}, {"id": "AdminName", "value": "OvstQuall"}, {"id": "AdminPhone", "value": "564654654645"}, {"id": "AdminEmail", "value": "OvstQuall@hpe.com"}, {"id": "AdminOtherInfo", "value": "OvstQuallRing7"}]
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [{u'deviceSlot': u'Mezz 4', u'status': u'OK', u'driveMinSizeGB': 146, u'name': u'BBird2',
                                 u'driveMaxSizeGB': 146, u'eraseData': False, u'driveTechnology': u'SasHdd',
                                 u'numPhysicalDrives': 1, u'id': 2},
                                {u'deviceSlot': u'Mezz 1', u'status': u'OK', u'driveMinSizeGB': 146, u'name': u'BBird1',
                                 u'driveMaxSizeGB': 146, u'eraseData': False, u'driveTechnology': u'SasHdd',
                                 u'numPhysicalDrives': 1, u'id': 1}],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "volume": None,
                    "id": 1,
                    "volumeUri": "SVOL:dd9-tbird-2bay2priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 3,
                    "volumeUri": "SVOL:ovstQR9-e2bay5-bfsDoNotDelFrom3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                }
            ]
        },
    },
    {
        "uri": "SP:MXQ73705W4, bay 1",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9 3:1:HP Synergy 3830C 16G FC HBA:3:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ73705W4, bay 1",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705W4, bay 1",
        "enclosureUri": "ENC:MXQ73705W4",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "MXQ73705W4, bay 1 is updated with new Eth, FC connections, Bios, BootSettings and sansorage",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "FC-a",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:01",
                    "wwpn": "10:00:7e:77:18:50:00:00",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "FC-b",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:03",
                    "wwpn": "10:00:7e:77:18:50:00:02",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 6,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                }
            ]
        },
        "boot": {
            "manageBoot": True,
            "order": ["CD", "USB", 'HardDisk', "PXE"]
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
            "overriddenSettings": [{"id": "CustomPostMessage", "value": "WindowSysetm"}, {"id": "ServerPrimaryOs", "value": "Window10"}, {"id": "ServerOtherInfo", "value": "severos"}, {"id": "AdminName", "value": "OvstQuall"}, {"id": "AdminPhone", "value": "564654654645"}, {"id": "AdminEmail", "value": "OvstQuall@hpe.com"}, {"id": "AdminOtherInfo", "value": "OvstQuallRing7"}]
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "volume": None,
                    "id": 1,
                    "volumeUri": "SVOL:dd9-tbird-1bay1priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 2,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 3,
                    "volumeUri": "SVOL:ovstQR9-e1bay1-bfsDoNotDelFrom3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 4,
                    "volumeUri": "SVOL:ovstQR9-e1bay5-bfsDoNotDelFrom3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "4",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                },
            ]
        },
    },
    {
        "uri": "SP:MXQ73705WF, bay 6",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 660 Gen10:1:HPE Smart Array P416ie-m SR G10:3:Synergy 3820C 10/20Gb CNA:6:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ73705WF, bay 6",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705WF, bay 6",
        "enclosureUri": "ENC:MXQ73705WF",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "MXQ73705WF, bay 6 is updated with new Eth, FC connections, Bios, BootSettings and sansorage",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "FC-a",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:19",
                    "wwpn": "10:00:7e:77:18:50:00:18",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "FC-b",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:1b",
                    "wwpn": "10:00:7e:77:18:50:00:1a",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "FC-a2",
                    "portId": "Mezz 6:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:1d",
                    "wwpn": "10:00:7e:77:18:50:00:1c",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "FC-b2",
                    "portId": "Mezz 6:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:1f",
                    "wwpn": "10:00:7e:77:18:50:00:1e",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "Ethernet",
                    "id": 5,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "4000",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "Ethernet",
                    "id": 6,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "4000",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "Ethernet",
                    "id": 7,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "4000",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "Ethernet",
                    "id": 8,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "4000",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                }
            ]
        },
        "boot": {
            "manageBoot": True,
            "order": ["CD", "USB", 'HardDisk', "PXE"]
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
            "overriddenSettings": [{"id": "CustomPostMessage", "value": "WindowSysetm"}, {"id": "ServerPrimaryOs", "value": "Window10"}, {"id": "ServerOtherInfo", "value": "severos"}, {"id": "AdminName", "value": "OvstQuall"}, {"id": "AdminPhone", "value": "564654654645"}, {"id": "AdminEmail", "value": "OvstQuall@hpe.com"}, {"id": "AdminOtherInfo", "value": "OvstQuallRing7"}]
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [{u'deviceSlot': u'Mezz 1', u'status': u'OK', u'driveMinSizeGB': 146, u'name': u'BBird1',
                                 u'driveMaxSizeGB': 146, u'eraseData': False, u'driveTechnology': u'SasHdd',
                                 u'numPhysicalDrives': 1, u'id': 1}],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "volume": None,
                    "id": 2,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 4,
                    "volumeUri": "SVOL:dd9-tbird-2bay3priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                }
            ]
        },
    },
    {
        "uri": "SP:MXQ73708NK, bay 8",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen10:3:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ73708NK, bay 8",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73708NK, bay 8",
        "enclosureUri": "ENC:MXQ73708NK",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "MXQ73708NK, bay 8 is updated with new Eth, FC connections, Bios, BootSettings and sansorage",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "FC-a",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:2d",
                    "wwpn": "10:00:7e:77:18:50:00:2c",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "FC-b",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:2f",
                    "wwpn": "10:00:7e:77:18:50:00:2e",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:2-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 6,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                }
            ]
        },
        "boot": {
            "manageBoot": True,
            "order": ["CD", "USB", 'HardDisk', "PXE"]
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
            "overriddenSettings": [{"id": "CustomPostMessage", "value": "WindowSysetm"}, {"id": "ServerPrimaryOs", "value": "Window10"}, {"id": "ServerOtherInfo", "value": "severos"}, {"id": "AdminName", "value": "OvstQuall"}, {"id": "AdminPhone", "value": "564654654645"}, {"id": "AdminEmail", "value": "OvstQuall@hpe.com"}, {"id": "AdminOtherInfo", "value": "OvstQuallRing7"}]
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "volume": None,
                    "id": 1,
                    "volumeUri": "SVOL:dd9-tbird-3bay3priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 2,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 3,
                    "volumeUri": "SVOL:ovstQR9-e3bay8-bfsDoNotDelFrom3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 4,
                    "volumeUri": "SVOL:ovstQR9-e3bay5-bfsDoNotDelFrom3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "4",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                },
            ]
        },
    },
    {
        "uri": "SP:MXQ73705W4, bay 2",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9 3:1:HP Synergy 3830C 16G FC HBA:3:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ73705W4, bay 2",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705W4, bay 2",
        "enclosureUri": "ENC:MXQ73705W4",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "MXQ73705W4, bay 2 is updated with new Eth, FC connections, Bios, BootSettings and sansorage",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "FC-a",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:05",
                    "wwpn": "10:00:7e:77:18:50:00:04",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "FC-b",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:07",
                    "wwpn": "10:00:7e:77:18:50:00:06",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 6,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:2-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                }
            ]
        },
        "boot": {
            "manageBoot": True,
            "order": ["CD", "USB", 'HardDisk', "PXE"]
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
            "overriddenSettings": [{"id": "CustomPostMessage", "value": "WindowSysetm"}, {"id": "ServerPrimaryOs", "value": "Window10"}, {"id": "ServerOtherInfo", "value": "severos"}, {"id": "AdminName", "value": "OvstQuall"}, {"id": "AdminPhone", "value": "564654654645"}, {"id": "AdminEmail", "value": "OvstQuall@hpe.com"}, {"id": "AdminOtherInfo", "value": "OvstQuallRing7"}]
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "volume": None,
                    "id": 1,
                    "volumeUri": "SVOL:dd9-tbird-1bay2priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 2,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 3,
                    "volumeUri": "SVOL:ovstQR9-e1bay2-bfsDoNotDelFrom3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 1,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 4,
                    "volumeUri": "SVOL:ovstQR9-e2bay2-bfsDoNotDelFrom3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "4",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 1,
                            "targetSelector": "Auto",
                        }
                    ]
                }
            ]
        },
    },
    {
        "uri": "SP:MXQ73705WF, bay 10",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen10:1:HPE Smart Array P416ie-m SR G10:3:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ73705WF, bay 10",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705WF, bay 10",
        "enclosureUri": "ENC:MXQ73705WF",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "MXQ73705WF, bay 10 is updated with new Eth, FC connections, Bios, BootSettings and sansorage",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "FC-a",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:21",
                    "wwpn": "10:00:7e:77:18:50:00:20",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "FC-b",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:23",
                    "wwpn": "10:00:7e:77:18:50:00:22",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 6,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                }
            ]
        },
        "boot": {
            "manageBoot": True,
            "order": ["CD", "USB", 'HardDisk', "PXE"]
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
            "overriddenSettings": [{"id": "CustomPostMessage", "value": "WindowSysetm"}, {"id": "ServerPrimaryOs", "value": "Window10"}, {"id": "ServerOtherInfo", "value": "severos"}, {"id": "AdminName", "value": "OvstQuall"}, {"id": "AdminPhone", "value": "564654654645"}, {"id": "AdminEmail", "value": "OvstQuall@hpe.com"}, {"id": "AdminOtherInfo", "value": "OvstQuallRing7"}]
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [{u'deviceSlot': u'Mezz 1', u'status': u'OK', u'driveMinSizeGB': 146, u'name': u'BBird1',
                                 u'driveMaxSizeGB': 146, u'eraseData': False, u'driveTechnology': u'SasHdd',
                                 u'numPhysicalDrives': 1, u'id': 1}],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "volume": None,
                    "id": 1,
                    "volumeUri": "SVOL:dd9-tbird-2bay4priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 2,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 1,
                            "targetSelector": "Auto",
                        }
                    ]
                },
            ]
        },
    },
    {
        "uri": "SP:MXQ73705W4, bay 8",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen10:3:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ73705W4, bay 8",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705W4, bay 8",
        "enclosureUri": "ENC:MXQ73705W4",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "MXQ73705W4, bay 8 is updated with new Eth, FC connections, Bios, BootSettings and sansorage",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "FC-a",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:09",
                    "wwpn": "10:00:7e:77:18:50:00:08",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "FC-b",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:0b",
                    "wwpn": "10:00:7e:77:18:50:00:0a",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 6,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                }
            ]
        },
        "boot": {
            "manageBoot": True,
            "order": ["CD", "USB", 'HardDisk', "PXE"]
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
            "overriddenSettings": [{"id": "CustomPostMessage", "value": "WindowSysetm"}, {"id": "ServerPrimaryOs", "value": "Window10"}, {"id": "ServerOtherInfo", "value": "severos"}, {"id": "AdminName", "value": "OvstQuall"}, {"id": "AdminPhone", "value": "564654654645"}, {"id": "AdminEmail", "value": "OvstQuall@hpe.com"}, {"id": "AdminOtherInfo", "value": "OvstQuallRing7"}]
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "volume": None,
                    "id": 1,
                    "volumeUri": "SVOL:dd9-tbird-1bay3priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 2,
                    "volumeUri": "SVOL:dd9-shared",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "2",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 3,
                    "volumeUri": "SVOL:ovstQR9-e1bay8-bfsDoNotDelFrom3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 1,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 4,
                    "volumeUri": "SVOL:dd9-tbird-3bay4priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "4",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                },
            ]
        },
    },
    {
        "uri": "SP:MXQ73705WF, bay 3",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9:1:Smart Array P542D Controller:3:Synergy 3820C 10/20Gb CNA",
        "name": "MXQ73705WF, bay 3",
        "type": "ServerProfileV11",
        "serverHardwareUri": "SH:MXQ73705WF, bay 3",
        "enclosureUri": "ENC:MXQ73705WF",
        "enclosureGroupUri": "EG:dd-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "MXQ73705WF, bay 3 is updated with new Eth, FC connections, Bios, BootSettings and sansorage",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "FC-a",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:0d",
                    "wwpn": "10:00:7e:77:18:50:00:0c",
                    "networkUri": "FC:ovstsan216-240-a",
                },
                {
                    "allocatedMbps": 4000,
                    "functionType": "FibreChannel",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "FC-b",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "4000",
                    "wwnn": "10:00:7e:77:18:50:00:0f",
                    "wwpn": "10:00:7e:77:18:50:00:0e",
                    "networkUri": "FC:ovstsan216-240-b",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-a",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net10",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-b",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net11",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-c",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net12",
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 6,
                    "maximumMbps": 10000,
                    "name": "Mezz 3:1-d",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:net13",
                }
            ]
        },
        "boot": {
            "manageBoot": True,
            "order": ["CD", "USB", 'HardDisk', "PXE"]
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
            "overriddenSettings": [{"id": "CustomPostMessage", "value": "WindowSysetm"}, {"id": "ServerPrimaryOs", "value": "Window10"}, {"id": "ServerOtherInfo", "value": "severos"}, {"id": "AdminName", "value": "OvstQuall"}, {"id": "AdminPhone", "value": "564654654645"}, {"id": "AdminEmail", "value": "OvstQuall@hpe.com"}, {"id": "AdminOtherInfo", "value": "OvstQuallRing7"}]
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [{u'deviceSlot': u'Mezz 1', u'status': u'OK', u'driveMinSizeGB': 146, u'name': u'BBird1',
                                 u'driveMaxSizeGB': 146, u'eraseData': False, u'driveTechnology': u'SasHdd',
                                 u'numPhysicalDrives': 1, u'id': 1}],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Ubuntu",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "volume": None,
                    "id": 1,
                    "volumeUri": "SVOL:dd9-tbird-2bay1priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                },
                {
                    "volume": None,
                    "id": 3,
                    "volumeUri": "SVOL:ovstQR9-e2bay1-bfsDoNotDelFrom3",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "3",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                        }
                    ]
                }
            ]
        },
    }
]

delete_storage_volumes_from_OV_only = [
    {'type': 'AddStorageVolumeV3', 'name': 'ovstQR9-e1bay1-bfsDoNotDelFrom3', 'description': '',
     'storageSystemUri': 'ovst-3par-8440-01-srv', 'storageSystemVolumeName': 'ovstQR9-e1bay1-bfsDoNotDelFrom3',
     'provisioningParameters': {'shareable': False}},
    {'type': 'AddStorageVolumeV3', 'name': 'ovstQR9-e1bay2-bfsDoNotDelFrom3', 'description': '',
     'storageSystemUri': 'ovst-3par-8440-01-srv', 'storageSystemVolumeName': 'ovstQR9-e1bay2-bfsDoNotDelFrom3',
     'provisioningParameters': {'shareable': False}},
    {'type': 'AddStorageVolumeV3', 'name': 'ovstQR9-e1bay5-bfsDoNotDelFrom3', 'description': '',
     'storageSystemUri': 'ovst-3par-8440-01-srv', 'storageSystemVolumeName': 'ovstQR9-e1bay5-bfsDoNotDelFrom3',
     'provisioningParameters': {'shareable': False}},
    {'type': 'AddStorageVolumeV3', 'name': 'ovstQR9-e1bay8-bfsDoNotDelFrom3', 'description': '',
     'storageSystemUri': 'ovst-3par-8440-01-srv', 'storageSystemVolumeName': 'ovstQR9-e1bay8-bfsDoNotDelFrom3',
     'provisioningParameters': {'shareable': False}},
    {'type': 'AddStorageVolumeV3', 'name': 'ovstQR9-e2bay1-bfsDoNotDelFrom3', 'description': '',
     'storageSystemUri': 'ovst-3par-8440-01-srv', 'storageSystemVolumeName': 'ovstQR9-e2bay1-bfsDoNotDelFrom3',
     'provisioningParameters': {'shareable': False}},
    {'type': 'AddStorageVolumeV3', 'name': 'ovstQR9-e2bay2-bfsDoNotDelFrom3', 'description': '',
     'storageSystemUri': 'ovst-3par-8440-01-srv', 'storageSystemVolumeName': 'ovstQR9-e2bay2-bfsDoNotDelFrom3',
     'provisioningParameters': {'shareable': False}},
    {'type': 'AddStorageVolumeV3', 'name': 'ovstQR9-e2bay5-bfsDoNotDelFrom3', 'description': '',
     'storageSystemUri': 'ovst-3par-8440-01-srv', 'storageSystemVolumeName': 'ovstQR9-e2bay5-bfsDoNotDelFrom3',
     'provisioningParameters': {'shareable': False}},
    {'type': 'AddStorageVolumeV3', 'name': 'ovstQR9-e2bay6-bfsDoNotDelFrom3', 'description': '',
     'storageSystemUri': 'ovst-3par-8440-01-srv', 'storageSystemVolumeName': 'ovstQR9-e2bay6-bfsDoNotDelFrom3',
     'provisioningParameters': {'shareable': False}},
    {'type': 'AddStorageVolumeV3', 'name': 'ovstQR9-e2bay10-bfsDoNotDelFrm3', 'description': '',
     'storageSystemUri': 'ovst-3par-8440-01-srv', 'storageSystemVolumeName': 'ovstQR9-e2bay10-bfsDoNotDelFrm3',
     'provisioningParameters': {'shareable': False}},
    {'type': 'AddStorageVolumeV3', 'name': 'ovstQR9-e3bay1-bfsDoNotDelFrom3', 'description': '',
     'storageSystemUri': 'ovst-3par-8440-01-srv', 'storageSystemVolumeName': 'ovstQR9-e3bay1-bfsDoNotDelFrom3',
     'provisioningParameters': {'shareable': False}},
    {'type': 'AddStorageVolumeV3', 'name': 'ovstQR9-e3bay2-bfsDoNotDelFrom3', 'description': '',
     'storageSystemUri': 'ovst-3par-8440-01-srv', 'storageSystemVolumeName': 'ovstQR9-e3bay2-bfsDoNotDelFrom3',
     'provisioningParameters': {'shareable': False}},
    {'type': 'AddStorageVolumeV3', 'name': 'ovstQR9-e3bay5-bfsDoNotDelFrom3', 'description': '',
     'storageSystemUri': 'ovst-3par-8440-01-srv', 'storageSystemVolumeName': 'ovstQR9-e3bay5-bfsDoNotDelFrom3',
     'provisioningParameters': {'shareable': False}},
    {'type': 'AddStorageVolumeV3', 'name': 'ovstQR9-e3bay8-bfsDoNotDelFrom3', 'description': '',
     'storageSystemUri': 'ovst-3par-8440-01-srv', 'storageSystemVolumeName': 'ovstQR9-e3bay8-bfsDoNotDelFrom3',
     'provisioningParameters': {'shareable': False}}]

storage_volumes_to_delete = [{"name": "dd9-tbird-1bay1priv", "storageSystemVolumeName": "dd9-tbird-1bay1priv"},
                             {"name": "dd9-tbird-1bay2priv",
                              "storageSystemVolumeName": "dd9-tbird-1bay2priv"},
                             {"name": "dd9-tbird-1bay3priv",
                              "storageSystemVolumeName": "dd9-tbird-1bay3priv"},
                             {"name": "dd9-tbird-1bay4priv",
                              "storageSystemVolumeName": "dd9-tbird-1bay4priv"},
                             {"name": "dd9-tbird-2bay1priv",
                              "storageSystemVolumeName": "dd9-tbird-2bay1priv"},
                             {"name": "dd9-tbird-2bay2priv",
                              "storageSystemVolumeName": "dd9-tbird-2bay2priv"},
                             {"name": "dd9-tbird-2bay3priv",
                              "storageSystemVolumeName": "dd9-tbird-2bay3priv"},
                             {"name": "dd9-tbird-2bay4priv",
                              "storageSystemVolumeName": "dd9-tbird-2bay4priv"},
                             {"name": "dd9-tbird-2bay5priv",
                              "storageSystemVolumeName": "dd9-tbird-2bay5priv"},
                             {"name": "dd9-tbird-3bay1priv",
                              "storageSystemVolumeName": "dd9-tbird-3bay1priv"},
                             {"name": "dd9-tbird-3bay2priv",
                              "storageSystemVolumeName": "dd9-tbird-3bay2priv"},
                             {"name": "dd9-tbird-3bay3priv",
                              "storageSystemVolumeName": "dd9-tbird-3bay3priv"},
                             {"name": "dd9-tbird-3bay4priv",
                              "storageSystemVolumeName": "dd9-tbird-3bay4priv"},
                             {"name": "dd9-tbird-3bay5priv",
                              "storageSystemVolumeName": "dd9-tbird-3bay5priv"},
                             {"name": "dd9-shared", "storageSystemVolumeName": "dd9-shared"}]

monitored_enclosures = [
    {
        "name": "MXQ73705W4",
        "state": "Monitored",
        "serialNumber": "MXQ73705W4",
        "type": "EnclosureV8",
        "refreshState": "NotRefreshing",
        "deviceBays": [
            {
                "bayNumber": 1,
                "devicePresence": "Present"
            },
            {
                "bayNumber": 2,
                "devicePresence": "Present"
            },
            {
                "bayNumber": 3,
                "devicePresence": "Present"
            },
            {
                "bayNumber": 4,
                "devicePresence": "Present"
            },
            {
                "bayNumber": 5,
                "devicePresence": "Present"
            },
            {
                "bayNumber": 6,
                "devicePresence": "Subsumed"
            },
            {
                "bayNumber": 7,
                "devicePresence": "Present"
            },
            {
                "bayNumber": 8,
                "devicePresence": "Present"
            },
            {
                "bayNumber": 9,
                "devicePresence": "Absent"
            },
            {
                "bayNumber": 10,
                "devicePresence": "Absent"
            },
            {
                "bayNumber": 11,
                "devicePresence": "Subsumed"
            },
            {
                "bayNumber": 12,
                "devicePresence": "Subsumed"
            }
        ],
        "interconnectBays": [
            {
                "bayNumber": 1,
                "bayPowerState": "Unknown"
            },
            {
                "bayNumber": 2,
                "bayPowerState": "Unknown"
            },
            {
                "bayNumber": 3,
                "bayPowerState": "Unknown"
            },
            {
                "bayNumber": 4,
                "bayPowerState": "Unknown"
            },
            {
                "bayNumber": 5,
                "bayPowerState": "Unknown"
            },
            {
                "bayNumber": 6,
                "bayPowerState": "Unknown"
            }
        ],
        "fanBays": [
            {
                "bayNumber": 1,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 2,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 3,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 4,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 5,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 6,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 7,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 8,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 9,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 10,
                "devicePresence": "Present",
                "status": "OK"
            }
        ],
        "powerSupplyBays": [
            {
                "bayNumber": 1,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 2,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 3,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 4,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 5,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 6,
                "devicePresence": "Present",
                "status": "OK"
            }
        ],
        "applianceBays": [
            {
                "bayNumber": 1,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 2,
                "devicePresence": "Absent",
                "status": None
            }
        ],
        "managerBays": [
            {
                "bayNumber": 1,
                "devicePresence": "Present",
                "status": "OK",
                "mgmtPortStatus": "OK"
            },
            {
                "bayNumber": 2,
                "devicePresence": "Present",
                "status": "OK",
                "mgmtPortStatus": "OK"
            }
        ],
    },
    {
        "name": "MXQ73708NK",
        "state": "Monitored",
        "serialNumber": "MXQ73708NK",
        "type": "EnclosureV8",
        "refreshState": "NotRefreshing",
        "deviceBays": [
            {
                "bayNumber": 1,
                "devicePresence": "Present"
            },
            {
                "bayNumber": 2,
                "devicePresence": "Present"
            },
            {
                "bayNumber": 3,
                "devicePresence": "Present"
            },
            {
                "bayNumber": 4,
                "devicePresence": "Present"
            },
            {
                "bayNumber": 5,
                "devicePresence": "Absent"
            },
            {
                "bayNumber": 6,
                "devicePresence": "Absent"
            },
            {
                "bayNumber": 7,
                "devicePresence": "Present"
            },
            {
                "bayNumber": 8,
                "devicePresence": "Present"
            },
            {
                "bayNumber": 9,
                "devicePresence": "Absent"
            },
            {
                "bayNumber": 10,
                "devicePresence": "Absent"
            },
            {
                "bayNumber": 11,
                "devicePresence": "Absent"
            },
            {
                "bayNumber": 12,
                "devicePresence": "Absent"
            }
        ],
        "interconnectBays": [
            {
                "bayNumber": 1,
                "bayPowerState": "Unknown"
            },
            {
                "bayNumber": 2,
                "bayPowerState": "Unknown"
            },
            {
                "bayNumber": 3,
                "bayPowerState": "Unknown"
            },
            {
                "bayNumber": 4,
                "bayPowerState": "Unknown"
            },
            {
                "bayNumber": 5,
                "bayPowerState": "Unknown"
            },
            {
                "bayNumber": 6,
                "bayPowerState": "Unknown"
            }
        ],
        "fanBays": [
            {
                "bayNumber": 1,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 2,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 3,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 4,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 5,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 6,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 7,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 8,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 9,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 10,
                "devicePresence": "Present",
                "status": "OK"
            }
        ],
        "powerSupplyBays": [
            {
                "bayNumber": 1,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 2,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 3,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 4,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 5,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 6,
                "devicePresence": "Present",
                "status": "OK"
            }
        ],
        "applianceBays": [
            {
                "bayNumber": 1,
                "devicePresence": "Absent",
                "status": None
            },
            {
                "bayNumber": 2,
                "devicePresence": "Absent",
                "status": None
            }
        ],
        "managerBays": [
            {
                "bayNumber": 1,
                "devicePresence": "Present",
                "status": "OK",
                "mgmtPortStatus": "OK"
            },
            {
                "bayNumber": 2,
                "devicePresence": "Present",
                "status": "OK",
                "mgmtPortStatus": "OK"
            }
        ],
    },
    {
        "name": "MXQ73705WF",
        "state": "Monitored",
        "serialNumber": "MXQ73705WF",
        "type": "EnclosureV8",
        "refreshState": "NotRefreshing",
        "deviceBays": [
            {
                "bayNumber": 1,
                "devicePresence": "Present"
            },
            {
                "bayNumber": 2,
                "devicePresence": "Subsumed"
            },
            {
                "bayNumber": 3,
                "devicePresence": "Present"
            },
            {
                "bayNumber": 4,
                "devicePresence": "Present"
            },
            {
                "bayNumber": 5,
                "devicePresence": "Present"
            },
            {
                "bayNumber": 6,
                "devicePresence": "Present"
            },
            {
                "bayNumber": 7,
                "devicePresence": "Present"
            },
            {
                "bayNumber": 8,
                "devicePresence": "Present"
            },
            {
                "bayNumber": 9,
                "devicePresence": "Present"
            },
            {
                "bayNumber": 10,
                "devicePresence": "Present"
            },
            {
                "bayNumber": 11,
                "devicePresence": "Subsumed"
            },
            {
                "bayNumber": 12,
                "devicePresence": "Subsumed"
            }
        ],
        "interconnectBays": [
            {
                "bayNumber": 1,
                "bayPowerState": "Unknown"
            },
            {
                "bayNumber": 2,
                "bayPowerState": "Unknown"
            },
            {
                "bayNumber": 3,
                "bayPowerState": "Unknown"
            },
            {
                "bayNumber": 4,
                "bayPowerState": "Unknown"
            },
            {
                "bayNumber": 5,
                "bayPowerState": "Unknown"
            },
            {
                "bayNumber": 6,
                "bayPowerState": "Unknown"
            }
        ],
        "fanBays": [
            {
                "bayNumber": 1,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 2,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 3,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 4,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 5,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 6,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 7,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 8,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 9,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 10,
                "devicePresence": "Present",
                "status": "OK"
            }
        ],
        "powerSupplyBays": [
            {
                "bayNumber": 1,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 2,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 3,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 4,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 5,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 6,
                "devicePresence": "Present",
                "status": "OK"
            }
        ],
        "applianceBays": [
            {
                "bayNumber": 1,
                "devicePresence": "Absent",
                "status": None
            },
            {
                "bayNumber": 2,
                "devicePresence": "Present",
                "status": "OK"
            }
        ],
        "managerBays": [
            {
                "bayNumber": 1,
                "devicePresence": "Present",
                "status": "OK",
                "mgmtPortStatus": "OK"
            },
            {
                "bayNumber": 2,
                "devicePresence": "Present",
                "status": "OK",
                "mgmtPortStatus": "OK"
            }
        ],
    }
]

configured_enclosures = [
    {
        "name": "MXQ73705W4",
        "state": "Configured",
        "serialNumber": "MXQ73705W4",
        "type": "EnclosureV8",
        "refreshState": "NotRefreshing",
        "deviceBays": [
            {
                "bayNumber": 1,
                "devicePresence": "Present"
            },
            {
                "bayNumber": 2,
                "devicePresence": "Present"
            },
            {
                "bayNumber": 3,
                "devicePresence": "Present"
            },
            {
                "bayNumber": 4,
                "devicePresence": "Present"
            },
            {
                "bayNumber": 5,
                "devicePresence": "Present"
            },
            {
                "bayNumber": 6,
                "devicePresence": "Subsumed"
            },
            {
                "bayNumber": 7,
                "devicePresence": "Present"
            },
            {
                "bayNumber": 8,
                "devicePresence": "Present"
            },
            {
                "bayNumber": 9,
                "devicePresence": "Absent"
            },
            {
                "bayNumber": 10,
                "devicePresence": "Absent"
            },
            {
                "bayNumber": 11,
                "devicePresence": "Subsumed"
            },
            {
                "bayNumber": 12,
                "devicePresence": "Subsumed"
            }
        ],
        "interconnectBays": [
            {
                "bayNumber": 1,
                "bayPowerState": "Unknown"
            },
            {
                "bayNumber": 2,
                "bayPowerState": "Unknown"
            },
            {
                "bayNumber": 3,
                "bayPowerState": "Unknown"
            },
            {
                "bayNumber": 4,
                "bayPowerState": "Unknown"
            },
            {
                "bayNumber": 5,
                "bayPowerState": "Unknown"
            },
            {
                "bayNumber": 6,
                "bayPowerState": "Unknown"
            }
        ],
        "fanBays": [
            {
                "bayNumber": 1,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 2,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 3,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 4,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 5,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 6,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 7,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 8,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 9,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 10,
                "devicePresence": "Present",
                "status": "OK"
            }
        ],
        "powerSupplyBays": [
            {
                "bayNumber": 1,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 2,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 3,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 4,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 5,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 6,
                "devicePresence": "Present",
                "status": "OK"
            }
        ],
        "applianceBays": [
            {
                "bayNumber": 1,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 2,
                "devicePresence": "Absent",
                "status": None
            }
        ],
        "managerBays": [
            {
                "bayNumber": 1,
                "devicePresence": "Present",
                "status": "OK",
                "mgmtPortStatus": "OK"
            },
            {
                "bayNumber": 2,
                "devicePresence": "Present",
                "status": "OK",
                "mgmtPortStatus": "OK"
            }
        ],
    },
    {
        "name": "MXQ73705WF",
        "state": "Configured",
        "serialNumber": "MXQ73705WF",
        "type": "EnclosureV8",
        "refreshState": "NotRefreshing",
        "deviceBays": [
            {
                "bayNumber": 1,
                "devicePresence": "Present"
            },
            {
                "bayNumber": 2,
                "devicePresence": "Subsumed"
            },
            {
                "bayNumber": 3,
                "devicePresence": "Present"
            },
            {
                "bayNumber": 4,
                "devicePresence": "Present"
            },
            {
                "bayNumber": 5,
                "devicePresence": "Present"
            },
            {
                "bayNumber": 6,
                "devicePresence": "Present"
            },
            {
                "bayNumber": 7,
                "devicePresence": "Present"
            },
            {
                "bayNumber": 8,
                "devicePresence": "Present"
            },
            {
                "bayNumber": 9,
                "devicePresence": "Present"
            },
            {
                "bayNumber": 10,
                "devicePresence": "Present"
            },
            {
                "bayNumber": 11,
                "devicePresence": "Subsumed"
            },
            {
                "bayNumber": 12,
                "devicePresence": "Subsumed"
            }
        ],
        "interconnectBays": [
            {
                "bayNumber": 1,
                "bayPowerState": "Unknown"
            },
            {
                "bayNumber": 2,
                "bayPowerState": "Unknown"
            },
            {
                "bayNumber": 3,
                "bayPowerState": "Unknown"
            },
            {
                "bayNumber": 4,
                "bayPowerState": "Unknown"
            },
            {
                "bayNumber": 5,
                "bayPowerState": "Unknown"
            },
            {
                "bayNumber": 6,
                "bayPowerState": "Unknown"
            }
        ],
        "fanBays": [
            {
                "bayNumber": 1,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 2,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 3,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 4,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 5,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 6,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 7,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 8,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 9,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 10,
                "devicePresence": "Present",
                "status": "OK"
            }
        ],
        "powerSupplyBays": [
            {
                "bayNumber": 1,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 2,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 3,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 4,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 5,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 6,
                "devicePresence": "Present",
                "status": "OK"
            }
        ],
        "applianceBays": [
            {
                "bayNumber": 1,
                "devicePresence": "Absent",
                "status": None
            },
            {
                "bayNumber": 2,
                "devicePresence": "Present",
                "status": "OK"
            }
        ],
        "managerBays": [
            {
                "bayNumber": 1,
                "devicePresence": "Present",
                "status": "OK",
                "mgmtPortStatus": "OK"
            },
            {
                "bayNumber": 2,
                "devicePresence": "Present",
                "status": "OK",
                "mgmtPortStatus": "OK"
            }
        ],
    },
    {
        "name": "MXQ73708NK",
        "state": "Configured",
        "serialNumber": "MXQ73708NK",
        "type": "EnclosureV8",
        "refreshState": "NotRefreshing",
        "deviceBays": [
            {
                "bayNumber": 1,
                "devicePresence": "Present"
            },
            {
                "bayNumber": 2,
                "devicePresence": "Present"
            },
            {
                "bayNumber": 3,
                "devicePresence": "Present"
            },
            {
                "bayNumber": 4,
                "devicePresence": "Present"
            },
            {
                "bayNumber": 5,
                "devicePresence": "Absent"
            },
            {
                "bayNumber": 6,
                "devicePresence": "Absent"
            },
            {
                "bayNumber": 7,
                "devicePresence": "Present"
            },
            {
                "bayNumber": 8,
                "devicePresence": "Present"
            },
            {
                "bayNumber": 9,
                "devicePresence": "Absent"
            },
            {
                "bayNumber": 10,
                "devicePresence": "Absent"
            },
            {
                "bayNumber": 11,
                "devicePresence": "Absent"
            },
            {
                "bayNumber": 12,
                "devicePresence": "Absent"
            }
        ],
        "interconnectBays": [
            {
                "bayNumber": 1,
                "bayPowerState": "Unknown"
            },
            {
                "bayNumber": 2,
                "bayPowerState": "Unknown"
            },
            {
                "bayNumber": 3,
                "bayPowerState": "Unknown"
            },
            {
                "bayNumber": 4,
                "bayPowerState": "Unknown"
            },
            {
                "bayNumber": 5,
                "bayPowerState": "Unknown"
            },
            {
                "bayNumber": 6,
                "bayPowerState": "Unknown"
            }
        ],
        "fanBays": [
            {
                "bayNumber": 1,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 2,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 3,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 4,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 5,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 6,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 7,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 8,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 9,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 10,
                "devicePresence": "Present",
                "status": "OK"
            }
        ],
        "powerSupplyBays": [
            {
                "bayNumber": 1,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 2,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 3,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 4,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 5,
                "devicePresence": "Present",
                "status": "OK"
            },
            {
                "bayNumber": 6,
                "devicePresence": "Present",
                "status": "OK"
            }
        ],
        "applianceBays": [
            {
                "bayNumber": 1,
                "devicePresence": "Absent",
                "status": None
            },
            {
                "bayNumber": 2,
                "devicePresence": "Absent",
                "status": None
            }
        ],
        "managerBays": [
            {
                "bayNumber": 1,
                "devicePresence": "Present",
                "status": "OK",
                "mgmtPortStatus": "OK"
            },
            {
                "bayNumber": 2,
                "devicePresence": "Present",
                "status": "OK",
                "mgmtPortStatus": "OK"
            }
        ],
    }
]

support_dump = [{"errorCode": "CI", "encrypt": False}]

le_support_dump = [{"name": "ISOLIG_3EncICM",
                    "errorCode": "LESD1",
                    "encrypt": True,
                    "excludeApplianceDump": False}]

le_support_dump_with_profile = [
    {"name": "ISOLIG_3EncICM", "errorCode": "LESD1", "encrypt": True, "excludeApplianceDump": False}]

edit_enclosure_group = {'name': 'dd-EG',
                        'type': 'EnclosureGroupV8',
                        'interconnectBayMappings': [
                            {'enclosureIndex': 1,
                             'interconnectBay': 1,
                             'logicalInterconnectGroupUri': 'LIG:dd-Carbon'},
                            {'enclosureIndex': 1,
                             'interconnectBay': 4,
                             'logicalInterconnectGroupUri': 'LIG:dd-Carbon'},
                            {'interconnectBay': 3,
                             'logicalInterconnectGroupUri': 'LIG:dd-Potash'},
                            {'interconnectBay': 6,
                             'logicalInterconnectGroupUri': 'LIG:dd-Potash'},
                            {'enclosureIndex': 2, 'interconnectBay': 1,
                             'logicalInterconnectGroupUri': 'SASLIG:dd-Natasha'},
                            {'enclosureIndex': 2, 'interconnectBay': 4,
                             'logicalInterconnectGroupUri': 'SASLIG:dd-Natasha'},
                        ],
                        "stackingMode": "Enclosure",
                        "configurationScript": "",
                        "uri": None,
                        "powerMode": 'RedundantPowerFeed',
                        "ipRangeUris": [],
                        "enclosureCount": 3,
                        "osDeploymentSettings": None,
                        'ipAddressingMode': 'External',
                        'enclosureTypeUri': 'SY12000'}

update_logical_enclosure_from_group = {'name': 'ISOLIG_3EncICM'}

edit_li_telemetry_config = {'name': 'ISOLIG_3EncICM-dd-Potash', 'type': 'telemetry-configuration',
                            'enableTelemetry': True, 'sampleCount': 20, 'sampleInterval': 200,
                            'description': None, 'status': None, 'state': None, 'category': 'telemetry-configurations',
                            'uri': '/rest/logical-interconnects'}

update_logical_interconnect_from_group = {'name': 'ISOLIG_3EncICM-dd-Potash'}

li_state = {"name": "ISOLIG_3EncICM-dd-Carbon-tmp-1"}

li_state_after_update = {"name": "ISOLIG_3EncICM-dd-Carbon-1"}

# Data for Cleanup Storage

storage_credentials = {
    'host': 'ovst-3par-8400-04-srv.vse.rdlabs.hpecorp.net',
    'username': 'fusionadm',
    'password': 'hpvse1'}

cleanup_hosts = [{'name': 'MXQ73708NKbay2'}, {'name': 'MXQ73708NKbay1'}, {'name': 'MXQ73705WFbay5'},
                 {'name': 'MXQ73705W4bay1'}, {'name': 'MXQ73705WFbay6'}, {
                     'name': 'MXQ73708NKbay8'},
                 {'name': 'MXQ73705W4bay2'}, {'name': 'MXQ73705WFbay10'}, {
                     'name': 'MXQ73705W4bay8'},
                 {'name': 'MXQ73705WFbay3'}]

cleanup_volumes = [{'name': 'dd9-shared'}, {'name': 'dd9-tbird-1bay1priv'}, {'name': 'dd9-tbird-1bay2priv'},
                   {'name': 'dd9-tbird-1bay3priv'}, {'name':
                                                     'dd9-tbird-1bay4priv'}, {'name': 'dd9-tbird-2bay1priv'},
                   {'name': 'dd9-tbird-2bay2priv'}, {'name':
                                                     'dd9-tbird-2bay3priv'}, {'name': 'dd9-tbird-2bay4priv'},
                   {'name': 'dd9-tbird-2bay5priv'}, {'name':
                                                     'dd9-tbird-3bay1priv'}, {'name': 'dd9-tbird-3bay2priv'},
                   {'name': 'dd9-tbird-3bay3priv'}, {'name': 'dd9-tbird-3bay4priv'}, {'name': 'dd9-tbird-3bay5priv'}]

cleanup_vluns = [{'host': 'MXQ73708NKbay2', 'volume': 'dd9-tbird-3bay2priv'},
                 {'host': 'MXQ73708NKbay2', 'volume': 'dd9-shared'},
                 {'host': 'MXQ73708NKbay2',
                  'volume': 'ovstQR9-e3bay2-bfsDoNotDelFrom3'},
                 {'host': 'MXQ73708NKbay1', 'volume': 'dd9-tbird-3bay1priv'},
                 {'host': 'MXQ73708NKbay1', 'volume': 'dd9-shared'},
                 {'host': 'MXQ73708NKbay1',
                  'volume': 'ovstQR9-e3bay1-bfsDoNotDelFrom3'},
                 {'host': 'MXQ73705WFbay5', 'volume': 'dd9-tbird-2bay2priv'},
                 {'host': 'MXQ73705WFbay5', 'volume': 'dd9-shared'},
                 {'host': 'MXQ73705WFbay5',
                  'volume': 'ovstQR9-e2bay5-bfsDoNotDelFrom3'},
                 {'host': 'MXQ73705W4bay1', 'volume': 'dd9-tbird-1bay1priv'},
                 {'host': 'MXQ73705W4bay1', 'volume': 'dd9-shared'},
                 {'host': 'MXQ73705W4bay1',
                  'volume': 'ovstQR9-e1bay1-bfsDoNotDelFrom3'},
                 {'host': 'MXQ73705WFbay6', 'volume': 'dd9-shared'},
                 {'host': 'MXQ73705WFbay6',
                  'volume': 'ovstQR9-e2bay6-bfsDoNotDelFrom3'},
                 {'host': 'MXQ73705WFbay6', 'volume': 'dd9-tbird-2bay3priv'},
                 {'host': 'MXQ73708NKbay8', 'volume': 'dd9-tbird-3bay3priv'},
                 {'host': 'MXQ73708NKbay8', 'volume': 'dd9-shared'},
                 {'host': 'MXQ73708NKbay8',
                  'volume': 'ovstQR9-e3bay8-bfsDoNotDelFrom3'},
                 {'host': 'MXQ73705W4bay2', 'volume': 'dd9-tbird-1bay2priv'},
                 {'host': 'MXQ73705W4bay2', 'volume': 'dd9-shared'},
                 {'host': 'MXQ73705W4bay2',
                  'volume': 'ovstQR9-e1bay2-bfsDoNotDelFrom3'},
                 {'host': 'MXQ73705WFbay10', 'volume': 'dd9-tbird-2bay4priv'},
                 {'host': 'MXQ73705WFbay10', 'volume': 'dd9-shared'},
                 {'host': 'MXQ73705WFbay10',
                  'volume': 'ovstQR9-e2bay10-bfsDoNotDelFrm3'},
                 {'host': 'MXQ73705W4bay8', 'volume': 'dd9-tbird-1bay3priv'},
                 {'host': 'MXQ73705W4bay8', 'volume': 'dd9-shared'},
                 {'host': 'MXQ73705W4bay8',
                  'volume': 'ovstQR9-e1bay8-bfsDoNotDelFrom3'},
                 {'host': 'MXQ73705WFbay3', 'volume': 'dd9-tbird-2bay1priv'},
                 {'host': 'MXQ73705WFbay3', 'volume': 'dd9-shared'},
                 {'host': 'MXQ73705WFbay3', 'volume': 'ovstQR9-e2bay1-bfsDoNotDelFrom3'}]


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

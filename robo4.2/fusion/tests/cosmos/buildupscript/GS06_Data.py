#!/usr/bin/env python

admin_credentials = {'userName': 'Administrator', 'password': 'Cosmos123'}
timeandlocale = {'localeDisplayName': 'English (United States)', 'locale': 'en_US.UTF-8', 'dateTime': '2018-11-17T03:59:03.688Z', 'ntpServers': [], 'timezone': 'UTC', 'type': 'TimeAndLocale'}
licenses = [
    {
        'key': 'YBKA D9MA H9P9 8HX3 V2B4 HWWV Y9JL KMPL B89H MZVU GR4S JHWE J2SP XNZ8 CMRG HPMR UFVU A5K9 MWHC 9K4K HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'
    },
    {
        'key': 'YB2C D9MA H9PA 8HU3 V2B4 HWWV Y9JL KMPL B89H MZVU GR4S JHWE 9QSP XFR8 CMRG HPMR UFVU A5K9 MWHC 9K4K HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'
    },
    {
        'key': 'QBYC CQEA H9PQ KHX2 V2B4 HWWV Y9JL KMPL DJ6G PGFA DXAU 2CSM GHTG L762 HN63 HWR4 KJVT D5KM EFVW TSNJ D4QM 6382 SMT9 YGS6 SMQQ MUCF 4WCN MYN7 N2QS LHJQ XJUL LUQH TU8F 3DQC SW7N VEQW V886 FE23 YWAT J8U3 2YT5 RNNV MHS3 QKTQ 688U F8A7 F8SE Z2DX RJQ6 MHPE SN9R 3UNK TX83 T45F NGG3 EHM4 "EVAL-N3R43A_NFR N3R43A_NFR Synergy_8Gb_FC_Upgrade_License_NFR EVAL-N3R43A_NFR"'
    },
    {
        'key': '9B2G D9MA H9PA CHVZ V2B4 HWWV Y9JL KMPL B89H MZVU 6RMS 9HWE 92R6 3FZ3 CMRG HPMR MFVU A5K9 MHGK EKX9 HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'
    }
]

appliance = {
    'type': "ApplianceNetworkConfigurationV2",
    'applianceNetworks':
    [{
        "device": "bond0",
        "macAddress": "14:02:ec:46:73:68",
        "interfaceName": "Appliance",
        "activeNode": 1,
        "unconfigure": False,
        "ipv4Type": "STATIC",
        "ipv4Subnet": "255.255.0.0",
        "ipv4Gateway": "10.134.0.1",
        "ipv4NameServers": [u'10.120.0.10'],
        "app1Ipv4Addr": "10.134.1.16",
        "ipv6Type": "UNCONFIGURE",
        "hostname": "ci-1402ec466360.dom1134.lab",
        "confOneNode": False,
        "domainName": "dom1134.lab",
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
    },
    {
        "type": "UserAndPermissions",
        "password": "wpsthpvse1",
        "userName": "HardwareSetup",
        "permissions": [{u'roleName': u'Hardware setup', u'scopeUri': None}],
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
    },
    {
        "enabled": True,
        "name": None,
        "category": "users",
        "fullName": "HardwareSetup",
        "status": None,
        "type": "UserAndPermissions",
        "userName": "HardwareSetup",
        "permissions": [{u'roleName': u'Hardware setup', u'scopeUri': None}],
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
                "value": "10.120.1.29"
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
                "value": "10.120.1.38"
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
        "uri": "SAN:10.120.1.29",
        "name": "10.120.1.29",
        "type": "FCDeviceManagerV2",
        "category": "fc-device-managers",
        "state": "Managed",
        "description": "HP FF 5930-4Slot Switch",
        "deviceManagerVersion": "7.1.045 Release 2418P01",
        "isInternal": "False",
        "providerDisplayName": "HPE",
        "refreshState": "Stable",
        "status": "OK",
        "connectionInfo": [
            {
                "name": "Host",
                "value": "10.120.1.29"
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
        "uri": "SAN:10.120.1.38",
        "name": "10.120.1.38",
        "type": "FCDeviceManagerV2",
        "category": "fc-device-managers",
        "state": "Managed",
        "description": "Brocade Network Advisor",
        "deviceManagerVersion": "14.2.1.66",
        "isInternal": "False",
        "providerDisplayName": "Brocade Network Advisor",
        "refreshState": "Stable",
        "status": "OK",
        "connectionInfo": [
            {
                "name": "Host",
                "value": "10.120.1.38"
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
        "name": "Eth_1133",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1133
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth_1134",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1134
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "iSCSI_1121",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1121
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth_1139",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1139
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth_1130",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1130
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth_1138",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1138
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth_1131",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1131
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "iSCSI_1120",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1120
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth_1140",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1140
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth_1137",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1137
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth_1135",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1135
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth_1132",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1132
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth_1136",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1136
    }
]
expected_ethernet_networks = [
    {
        "uri": "ETH:Eth_1133",
        "category": "ethernet-networks",
        "state": "Active",
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth_1133",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1133
    },
    {
        "uri": "ETH:Eth_1134",
        "category": "ethernet-networks",
        "state": "Active",
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth_1134",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1134
    },
    {
        "uri": "ETH:iSCSI_1121",
        "category": "ethernet-networks",
        "state": "Active",
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "iSCSI_1121",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1121
    },
    {
        "uri": "ETH:Eth_1139",
        "category": "ethernet-networks",
        "state": "Active",
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth_1139",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1139
    },
    {
        "uri": "ETH:Eth_1130",
        "category": "ethernet-networks",
        "state": "Active",
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth_1130",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1130
    },
    {
        "uri": "ETH:Eth_1138",
        "category": "ethernet-networks",
        "state": "Active",
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth_1138",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1138
    },
    {
        "uri": "ETH:Eth_1131",
        "category": "ethernet-networks",
        "state": "Active",
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth_1131",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1131
    },
    {
        "uri": "ETH:iSCSI_1120",
        "category": "ethernet-networks",
        "state": "Active",
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "iSCSI_1120",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1120
    },
    {
        "uri": "ETH:Eth_1140",
        "category": "ethernet-networks",
        "state": "Active",
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth_1140",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1140
    },
    {
        "uri": "ETH:Eth_1137",
        "category": "ethernet-networks",
        "state": "Active",
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth_1137",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1137
    },
    {
        "uri": "ETH:Eth_1135",
        "category": "ethernet-networks",
        "state": "Active",
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth_1135",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1135
    },
    {
        "uri": "ETH:Eth_1132",
        "category": "ethernet-networks",
        "state": "Active",
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth_1132",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1132
    },
    {
        "uri": "ETH:Eth_1136",
        "category": "ethernet-networks",
        "state": "Active",
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth_1136",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1136
    }
]

i3s_networks = [
]
expected_i3s_networks = [
]
subnet_association = [
]

fc_networks = [
    {
        "type": "fc-networkV4",
        "name": "FC-1",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:FAB1-Frel"
    },
    {
        "type": "fc-networkV4",
        "name": "FC_DA_1",
        "fabricType": "DirectAttach",
        "linkStabilityTime": 0,
        "autoLoginRedistribution": False,
        "managedSanUri": None
    },
    {
        "type": "fc-networkV4",
        "name": "FC-2",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:FAB2-Frel"
    },
    {
        "type": "fc-networkV4",
        "name": "FC_DA_2",
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
        "uri": "FC:FC-1",
        "status": "OK",
        "type": "fc-networkV4",
        "name": "FC-1",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:FAB1-Frel"
    },
    {
        "category": "fc-networks",
        "state": "Active",
        "description": None,
        "uri": "FC:FC_DA_1",
        "status": "OK",
        "type": "fc-networkV4",
        "name": "FC_DA_1",
        "fabricType": "DirectAttach",
        "linkStabilityTime": 0,
        "autoLoginRedistribution": False,
        "managedSanUri": None
    },
    {
        "category": "fc-networks",
        "state": "Active",
        "description": None,
        "uri": "FC:FC-2",
        "status": "OK",
        "type": "fc-networkV4",
        "name": "FC-2",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:FAB2-Frel"
    },
    {
        "category": "fc-networks",
        "state": "Active",
        "description": None,
        "uri": "FC:FC_DA_2",
        "status": "OK",
        "type": "fc-networkV4",
        "name": "FC_DA_2",
        "fabricType": "DirectAttach",
        "linkStabilityTime": 0,
        "autoLoginRedistribution": False,
        "managedSanUri": None
    }
]

fcoe_networks = [
    {
        "name": "FCoE-1",
        "type": "fcoe-networkV4",
        "vlanId": 3201,
        "managedSanUri": "FCSan:VSAN3201"
    },
    {
        "name": "FCoE-2",
        "type": "fcoe-networkV4",
        "vlanId": 3202,
        "managedSanUri": "FCSan:VSAN3202"
    }
]
expected_fcoe_networks = [
    {
        "uri": "FCOE:FCoE-1",
        "state": "Active",
        "status": "OK",
        "name": "FCoE-1",
        "type": "fcoe-networkV4",
        "vlanId": 3201,
        "managedSanUri": "FCSan:VSAN3201"
    },
    {
        "uri": "FCOE:FCoE-2",
        "state": "Active",
        "status": "OK",
        "name": "FCoE-2",
        "type": "fcoe-networkV4",
        "vlanId": 3202,
        "managedSanUri": "FCSan:VSAN3202"
    }
]

networksets = [
]
expected_networksets = [
]

storage_systems_with_pools = [
    {
        "credentials": {u'username': u'cosmosvsa', u'password': 'Cosmos123'},
        "name": "cosmos-vsa-cluster",
        "family": "StoreVirtual",
        "hostname": "10.120.0.204",
        "ports": [
            {
                "expectedNetworkUri": "ETH:iSCSI_1120",
                "expectedNetworkName": "iSCSI_1120",
                "mode": "Managed",
                "name": "10.120.0.204"
            }
        ]
    },
    {
        "credentials": {u'username': u'cosmos', u'password': 'Insight7'},
        "name": "TB-82003PAR",
        "family": "StoreServ",
        "hostname": "10.120.1.36",
        "deviceSpecificAttributes": {
            "managedDomain": "NO DOMAIN",
            "managedPools": [{'domain': 'NO DOMAIN', 'name': 'FC_r1', 'raidLevel': 'RAID1', 'state': 'Managed', 'deviceType': 'FC', 'freeCapacity': '343597383680', 'totalCapacity': '867583393792', 'uuid': 'c109951e-4791-4f6b-8555-c5cabbfd4999'}, {'domain': 'NO DOMAIN', 'name': 'FC_r5', 'raidLevel': 'RAID5', 'state': 'Managed', 'deviceType': 'FC', 'freeCapacity': '569083166720', 'totalCapacity': '1667521052672', 'uuid': 'febf1c11-d7af-4fe8-9d6f-b05182cd33d9'}, {'domain': 'NO DOMAIN', 'name': 'SSD_r1', 'raidLevel': 'RAID1', 'state': 'Managed', 'deviceType': 'SSD', 'freeCapacity': '603442905088', 'totalCapacity': '732291923968', 'uuid': 'db2f06b0-b778-42e1-9395-c5197f9ba5ce'}, {'domain': 'NO DOMAIN', 'name': 'SSD_r5', 'raidLevel': 'RAID5', 'state': 'Managed', 'deviceType': 'SSD', 'freeCapacity': '1003948605440', 'totalCapacity': '1225139421184', 'uuid': '9b295078-7dd0-4c2e-881f-e1fba0a7cd07'}, {'domain': 'NO DOMAIN', 'name': 'SSD_r6', 'raidLevel': 'RAID6', 'state': 'Managed', 'deviceType': 'SSD', 'freeCapacity': '882615779328', 'totalCapacity': '882615779328', 'uuid': '936b5842-01a3-4a27-b586-9853bac6008f'}],
            "discoveredPools": [],

        },
    },
    {
        "credentials": {u'username': u'cosmos', u'password': 'Insight7'},
        "name": "CST-Nimble-CS5000",
        "family": "Nimble",
        "hostname": "10.120.0.155",
        "ports": [
            {
                "expectedNetworkUri": "ETH:iSCSI_1121",
                "expectedNetworkName": "iSCSI_1121",
                "mode": "Managed",
                "name": "Subnet-1121"
            }
        ]
    },
    {
        "credentials": {u'username': u'cosmos', u'password': 'Insight7'},
        "name": "cos-oob-p7200",
        "family": "StoreServ",
        "hostname": "10.120.1.64",
        "deviceSpecificAttributes": {
            "managedDomain": "NO DOMAIN",
            "managedPools": [{'domain': 'NO DOMAIN', 'name': 'FC_r1', 'raidLevel': 'RAID1', 'state': 'Managed', 'deviceType': 'FC', 'freeCapacity': '2163589775360', 'totalCapacity': '2249489121280', 'uuid': '392a04b7-601d-4725-8675-66415c16d308'}, {'domain': 'NO DOMAIN', 'name': 'FC_r5', 'raidLevel': 'RAID5', 'state': 'Managed', 'deviceType': 'FC', 'freeCapacity': '3597035110400', 'totalCapacity': '3850438180864', 'uuid': 'c6f82cf9-f897-452d-bd78-9a811798031d'}, {'domain': 'NO DOMAIN', 'name': 'FC_r6', 'raidLevel': 'RAID6', 'state': 'Managed', 'deviceType': 'FC', 'freeCapacity': '2876822781952', 'totalCapacity': '2876822781952', 'uuid': '66e71942-27f8-4ae7-aac2-6b0a019bc68c'}],
            "discoveredPools": [],

        }
    }
]
expected_storage_systems_with_pools = [
    {
        "uri": "SSYS:cosmos-vsa-cluster",
        "type": "StorageSystemV5",
        "state": "Managed",
        "category": "storage-systems",
        "status": "OK",
        "name": "cosmos-vsa-cluster",
        "family": "StoreVirtual",
        "hostname": "10.120.0.204",
        "ports": [
            {
                "expectedNetworkUri": "ETH:iSCSI_1120",
                "expectedNetworkName": "iSCSI_1120",
                "mode": "Managed",
                "name": "10.120.0.204"
            }
        ]
    },
    {
        "uri": "SSYS:TB-82003PAR",
        "type": "StorageSystemV5",
        "state": "Managed",
        "category": "storage-systems",
        "status": "OK",
        "name": "TB-82003PAR",
        "family": "StoreServ",
        "hostname": "10.120.1.36",
        "deviceSpecificAttributes": {
            "managedDomain": "NO DOMAIN",
            "serialNumber": "MXN55225W1"
        },
    },
    {
        "uri": "SSYS:CST-Nimble-CS5000",
        "type": "StorageSystemV5",
        "state": "Managed",
        "category": "storage-systems",
        "status": "OK",
        "name": "CST-Nimble-CS5000",
        "family": "Nimble",
        "hostname": "10.120.0.155",
        "ports": [
            {
                "expectedNetworkUri": "ETH:iSCSI_1121",
                "expectedNetworkName": "iSCSI_1121",
                "mode": "Managed",
                "name": "Subnet-1121"
            }
        ]
    },
    {
        "uri": "SSYS:cos-oob-p7200",
        "type": "StorageSystemV5",
        "state": "Managed",
        "category": "storage-systems",
        "status": "OK",
        "name": "cos-oob-p7200",
        "family": "StoreServ",
        "hostname": "10.120.1.64",
        "deviceSpecificAttributes": {
            "managedDomain": "NO DOMAIN",
            "serialNumber": "1648204"
        }
    }
]

storage_pools_toedit = [
    {
        "storageSystemUri": "cosmos-vsa-cluster",
        "name": "cosmos-vsa-cluster",
        "isManaged": True,
    },
    {
        "storageSystemUri": "CST-Nimble-CS5000",
        "name": "default",
        "isManaged": True,
    },
    {
        "storageSystemUri": "TB-82003PAR",
        "name": "FC_r1",
        "isManaged": True,
    },
    {
        "storageSystemUri": "TB-82003PAR",
        "name": "FC_r5",
        "isManaged": True,
    },
    {
        "storageSystemUri": "TB-82003PAR",
        "name": "SSD_r1",
        "isManaged": True,
    },
    {
        "storageSystemUri": "TB-82003PAR",
        "name": "SSD_r5",
        "isManaged": True,
    },
    {
        "storageSystemUri": "TB-82003PAR",
        "name": "SSD_r6",
        "isManaged": True,
    },
    {
        "storageSystemUri": "cos-oob-p7200",
        "name": "FC_r1",
        "isManaged": True,
    },
    {
        "storageSystemUri": "cos-oob-p7200",
        "name": "FC_r5",
        "isManaged": True,
    },
    {
        "storageSystemUri": "cos-oob-p7200",
        "name": "FC_r6",
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
]
expected_storage_volumes = [
]

sas_lig = [
]
expected_sas_lig = [
]

ligs = [
    {
        "name": "LIG_Potash_25",
        "type": "logical-interconnect-groupV6",
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
                "enclosureIndex": 2,
                "enclosure": 2,
                "bay": 5,
                "type": "Synergy 10Gb Interconnect Link Module"
            },
            {
                "enclosureIndex": 1,
                "enclosure": 1,
                "bay": 5,
                "type": "Virtual Connect SE 40Gb F8 Module for Synergy"
            },
            {
                "enclosureIndex": 2,
                "enclosure": 2,
                "bay": 2,
                "type": "Synergy 10Gb Interconnect Link Module"
            },
            {
                "enclosureIndex": 1,
                "enclosure": 1,
                "bay": 2,
                "type": "Virtual Connect SE 40Gb F8 Module for Synergy"
            }

        ],
        "interconnectBaySet": 2,
        "redundancyType": "Redundant",
        "telemetryConfiguration": {
            "enableTelemetry": True,
            "sampleCount": 12,
            "sampleInterval": 300
        },
        "uplinkSets": [
            {
                "ethernetNetworkType": "Tagged",
                "lacpTimer": "Short",
                "logicalPortConfigInfos": [
                    {
                        "speed": "Auto",
                        "port": "Q2:3",
                        "enclosure": "1",
                        "bay": "5"
                    },
                    {
                        "speed": "Auto",
                        "bay": "5",
                        "enclosure": "1",
                        "port": "Q2:4"
                    },
                    {
                        "speed": "Auto",
                        "port": "Q1:3",
                        "enclosure": "1",
                        "bay": "5"
                    },
                    {
                        "speed": "Auto",
                        "port": "Q1:4",
                        "enclosure": "1",
                        "bay": "5"
                    }
                ],
                "mode": "Auto",
                "name": "FCoE-5",
                "nativeNetworkUri": None,
                "networkType": "Ethernet",
                "networkUris": [
                    "FCoE-2"
                ],
                "primaryPort": None
            },
            {
                "ethernetNetworkType": "NotApplicable",
                "lacpTimer": None,
                "logicalPortConfigInfos": [
                    {
                        "speed": "Auto",
                        "port": "Q6:1",
                        "enclosure": "1",
                        "bay": "5"
                    },
                    {
                        "speed": "Auto",
                        "port": "Q5:1",
                        "enclosure": "1",
                        "bay": "5"
                    }
                ],
                "mode": "Auto",
                "name": "FC-5",
                "nativeNetworkUri": None,
                "networkType": "FibreChannel",
                "networkUris": [
                    "FC-2"
                ],
                "primaryPort": None
            },
            {
                "ethernetNetworkType": "Tagged",
                "lacpTimer": "Short",
                "logicalPortConfigInfos": [
                    {
                        "speed": "Auto",
                        "bay": "2",
                        "enclosure": "1",
                        "port": "Q2:3"
                    },
                    {
                        "speed": "Auto",
                        "bay": "2",
                        "enclosure": "1",
                        "port": "Q2:4"
                    },
                    {
                        "speed": "Auto",
                        "port": "Q1:4",
                        "enclosure": "1",
                        "bay": "2"
                    },
                    {
                        "speed": "Auto",
                        "port": "Q1:3",
                        "enclosure": "1",
                        "bay": "2"
                    }
                ],
                "mode": "Auto",
                "name": "FCoE-2",
                "nativeNetworkUri": None,
                "networkType": "Ethernet",
                "networkUris": [
                    "FCoE-1"
                ],
                "primaryPort": None
            },
            {
                "ethernetNetworkType": "NotApplicable",
                "lacpTimer": None,
                "logicalPortConfigInfos": [
                    {
                        "speed": "Auto",
                        "port": "Q5:1",
                        "enclosure": "1",
                        "bay": "2"
                    },
                    {
                        "speed": "Auto",
                        "bay": "2",
                        "enclosure": "1",
                        "port": "Q6:1"
                    }
                ],
                "mode": "Auto",
                "name": "FC-3",
                "nativeNetworkUri": None,
                "networkType": "FibreChannel",
                "networkUris": [
                    "FC-1"
                ],
                "primaryPort": None
            },
            {
                "ethernetNetworkType": "Tagged",
                "lacpTimer": "Short",
                "logicalPortConfigInfos": [
                    {
                        "speed": "Auto",
                        "bay": "2",
                        "enclosure": "1",
                        "port": "Q2:2"
                    },
                    {
                        "speed": "Auto",
                        "port": "Q2:1",
                        "enclosure": "1",
                        "bay": "2"
                    },
                    {
                        "speed": "Auto",
                        "port": "Q1:1",
                        "enclosure": "1",
                        "bay": "5"
                    },
                    {
                        "speed": "Auto",
                        "port": "Q1:2",
                        "enclosure": "1",
                        "bay": "5"
                    },
                    {
                        "speed": "Auto",
                        "port": "Q1:2",
                        "enclosure": "1",
                        "bay": "2"
                    },
                    {
                        "speed": "Auto",
                        "port": "Q2:1",
                        "enclosure": "1",
                        "bay": "5"
                    },
                    {
                        "speed": "Auto",
                        "port": "Q2:2",
                        "enclosure": "1",
                        "bay": "5"
                    },
                    {
                        "speed": "Auto",
                        "port": "Q1:1",
                        "enclosure": "1",
                        "bay": "2"
                    }
                ],
                "mode": "Auto",
                "name": "EtherNet",
                "nativeNetworkUri": None,
                "networkType": "Ethernet",
                "networkUris": [
                    "Eth_1135",
                    "Eth_1139",
                    "Eth_1140",
                    "Eth_1130",
                    "Eth_1137",
                    "iSCSI_1121",
                    "Eth_1132",
                    "iSCSI_1120",
                    "Eth_1131",
                    "Eth_1138",
                    "Eth_1133",
                    "Eth_1134",
                    "Eth_1136"
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
        "enclosureIndexes": [1, 2]
    },
    {
        "name": "LIG_Carbon_14",
        "type": "logical-interconnect-groupV6",
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
                    },
                    {
                        "speed": "Auto",
                        "port": "2",
                        "enclosure": "-1",
                        "bay": "4"
                    }
                ],
                "mode": "Auto",
                "name": "FC2",
                "nativeNetworkUri": None,
                "networkType": "FibreChannel",
                "networkUris": [
                    "FC-2"
                ],
                "primaryPort": None
            },
            {
                "ethernetNetworkType": "NotApplicable",
                "lacpTimer": None,
                "logicalPortConfigInfos": [
                    {
                        "speed": "Auto",
                        "port": "2",
                        "enclosure": "-1",
                        "bay": "1"
                    },
                    {
                        "speed": "Auto",
                        "bay": "1",
                        "port": "1",
                        "enclosure": "-1"
                    }
                ],
                "mode": "Auto",
                "name": "FC1",
                "nativeNetworkUri": None,
                "networkType": "FibreChannel",
                "networkUris": [
                    "FC-1"
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
        "name": "LIG_Potash_36",
        "type": "logical-interconnect-groupV6",
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
                "enclosureIndex": 2,
                "enclosure": 2,
                "bay": 6,
                "type": "Virtual Connect SE 40Gb F8 Module for Synergy"
            },
            {
                "enclosureIndex": 2,
                "enclosure": 2,
                "bay": 3,
                "type": "Synergy 20Gb Interconnect Link Module"
            },
            {
                "enclosureIndex": 1,
                "enclosure": 1,
                "bay": 3,
                "type": "Virtual Connect SE 40Gb F8 Module for Synergy"
            },
            {
                "enclosureIndex": 1,
                "bay": 6,
                "enclosure": 1,
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
                        "port": "Q6:1",
                        "enclosure": "2",
                        "bay": "6"
                    },
                    {
                        "speed": "Auto",
                        "port": "Q5:1",
                        "enclosure": "2",
                        "bay": "6"
                    }
                ],
                "mode": "Auto",
                "name": "DA-6",
                "nativeNetworkUri": None,
                "networkType": "FibreChannel",
                "networkUris": [
                    "FC_DA_2"
                ],
                "primaryPort": None
            },
            {
                "ethernetNetworkType": "NotApplicable",
                "lacpTimer": None,
                "logicalPortConfigInfos": [
                    {
                        "speed": "Auto",
                        "bay": "3",
                        "enclosure": "1",
                        "port": "Q6:1"
                    },
                    {
                        "speed": "Auto",
                        "port": "Q5:1",
                        "enclosure": "1",
                        "bay": "3"
                    }
                ],
                "mode": "Auto",
                "name": "DA-3",
                "nativeNetworkUri": None,
                "networkType": "FibreChannel",
                "networkUris": [
                    "FC_DA_1"
                ],
                "primaryPort": None
            },
            {
                "ethernetNetworkType": "Tagged",
                "lacpTimer": "Short",
                "logicalPortConfigInfos": [
                    {
                        "speed": "Auto",
                        "bay": "3",
                        "enclosure": "1",
                        "port": "Q3"
                    },
                    {
                        "speed": "Auto",
                        "bay": "3",
                        "port": "Q4",
                        "enclosure": "1"
                    }
                ],
                "mode": "Auto",
                "name": "FCoE-3",
                "nativeNetworkUri": None,
                "networkType": "Ethernet",
                "networkUris": [
                    "FCoE-1"
                ],
                "primaryPort": None
            },
            {
                "ethernetNetworkType": "Tagged",
                "lacpTimer": "Short",
                "logicalPortConfigInfos": [
                    {
                        "speed": "Auto",
                        "port": "Q3",
                        "enclosure": "2",
                        "bay": "6"
                    },
                    {
                        "speed": "Auto",
                        "bay": "6",
                        "port": "Q4",
                        "enclosure": "2"
                    }
                ],
                "mode": "Auto",
                "name": "FCoE-6",
                "nativeNetworkUri": None,
                "networkType": "Ethernet",
                "networkUris": [
                    "FCoE-2"
                ],
                "primaryPort": None
            },
            {
                "ethernetNetworkType": "Tagged",
                "lacpTimer": "Short",
                "logicalPortConfigInfos": [
                    {
                        "speed": "Auto",
                        "bay": "6",
                        "port": "Q1",
                        "enclosure": "2"
                    },
                    {
                        "speed": "Auto",
                        "bay": "3",
                        "port": "Q1",
                        "enclosure": "1"
                    },
                    {
                        "speed": "Auto",
                        "port": "Q2",
                        "enclosure": "1",
                        "bay": "3"
                    },
                    {
                        "speed": "Auto",
                        "port": "Q2",
                        "enclosure": "2",
                        "bay": "6"
                    }
                ],
                "mode": "Auto",
                "name": "EtherNet",
                "nativeNetworkUri": None,
                "networkType": "Ethernet",
                "networkUris": [
                    "Eth_1135",
                    "Eth_1139",
                    "Eth_1130",
                    "Eth_1140",
                    "Eth_1137",
                    "iSCSI_1121",
                    "Eth_1132",
                    "iSCSI_1120",
                    "Eth_1131",
                    "Eth_1138",
                    "Eth_1133",
                    "Eth_1134",
                    "Eth_1136"
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
        "enclosureIndexes": [1, 2]
    }
]
expected_lig = [
    {
        "uri": "LIG:LIG_Potash_25",
        "status": None,
        "stackingHealth": None,
        "category": "logical-interconnect-groups",
        "state": "Active",
        "internalNetworkUris": "[]",
        "stackingMode": None,
        "description": None,
        "name": "LIG_Potash_25",
        "type": "logical-interconnect-groupV6",
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
        "interconnectBaySet": 2,
        "redundancyType": "Redundant",
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
        "enclosureIndexes": [1, 2]
    },
    {
        "uri": "LIG:LIG_Carbon_14",
        "status": None,
        "stackingHealth": None,
        "category": "logical-interconnect-groups",
        "state": "Active",
        "internalNetworkUris": "[]",
        "stackingMode": None,
        "description": None,
        "name": "LIG_Carbon_14",
        "type": "logical-interconnect-groupV6",
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
    {
        "uri": "LIG:LIG_Potash_36",
        "status": None,
        "stackingHealth": None,
        "category": "logical-interconnect-groups",
        "state": "Active",
        "internalNetworkUris": "[]",
        "stackingMode": None,
        "description": None,
        "name": "LIG_Potash_36",
        "type": "logical-interconnect-groupV6",
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
        "enclosureIndexes": [1, 2]
    }
]

encgroups_add = [
    {
        "name": "EG",
        "interconnectBayMappings": [
            {
                "interconnectBay": 1,
                "logicalInterconnectGroupUri": "LIG:LIG_Carbon_14",
                "enclosureIndex": 1
            },
            {
                "interconnectBay": 2,
                "logicalInterconnectGroupUri": "LIG:LIG_Potash_25",

            },
            {
                "interconnectBay": 3,
                "logicalInterconnectGroupUri": "LIG:LIG_Potash_36",

            },
            {
                "interconnectBay": 4,
                "logicalInterconnectGroupUri": "LIG:LIG_Carbon_14",
                "enclosureIndex": 1
            },
            {
                "interconnectBay": 5,
                "logicalInterconnectGroupUri": "LIG:LIG_Potash_25",

            },
            {
                "interconnectBay": 6,
                "logicalInterconnectGroupUri": "LIG:LIG_Potash_36",

            }
        ],
        "ipAddressingMode": "DHCP",
        "enclosureCount": 2
    }
]
expected_encgroups_add = [
    {
        "uri": "EG:EG",
        "description": None,
        "category": "enclosure-groups",
        "state": "Normal",
        "status": "OK",
        "powerMode": "RedundantPowerFeed",
        "portMappingCount": 8,
        "portMappings": [{u'midplanePort': 1, u'interconnectBay': 1}, {u'midplanePort': 2, u'interconnectBay': 2}, {u'midplanePort': 3, u'interconnectBay': 3}, {u'midplanePort': 4, u'interconnectBay': 4}, {u'midplanePort': 5, u'interconnectBay': 5}, {u'midplanePort': 6, u'interconnectBay': 6}, {u'midplanePort': 7, u'interconnectBay': 7}, {u'midplanePort': 8, u'interconnectBay': 8}],
        "ipRangeUris": [],
        "associatedLogicalInterconnectGroups": [u'LIG:LIG_Potash_25', u'LIG:LIG_Carbon_14', u'LIG:LIG_Potash_36'],
        "name": "EG",
        "type": "EnclosureGroupV7",
        "enclosureTypeUri": "/rest/enclosure-types/SY12000",
        "stackingMode": "Enclosure",
        "name": "EG",
        "interconnectBayMappingCount": "6",
        "interconnectBayMappings": [
            {
                "interconnectBay": 1,
                "logicalInterconnectGroupUri": "LIG:LIG_Carbon_14",

            },
            {
                "interconnectBay": 2,
                "logicalInterconnectGroupUri": "LIG:LIG_Potash_25",

            },
            {
                "interconnectBay": 3,
                "logicalInterconnectGroupUri": "LIG:LIG_Potash_36",

            },
            {
                "interconnectBay": 4,
                "logicalInterconnectGroupUri": "LIG:LIG_Carbon_14",

            },
            {
                "interconnectBay": 5,
                "logicalInterconnectGroupUri": "LIG:LIG_Potash_25",

            },
            {
                "interconnectBay": 6,
                "logicalInterconnectGroupUri": "LIG:LIG_Potash_36",

            }
        ],
        "ipAddressingMode": "DHCP",
        "enclosureCount": 2
    }
]

logical_enclosure = [
    {
        "name": "LE",
        "enclosureUris": [
            "ENC:MXQ74606ZN",
            "ENC:MXQ74606ZJ"
        ],
        "enclosureGroupUri": "EG:EG"
    }
]
expected_logical_enclosure = [
    {
        "type": "LogicalEnclosureV4",
        "uri": "LE:LE",
        "status": "OK",
        "name": "LE",
        "enclosureUris": [
            "ENC:MXQ74606ZN",
            "ENC:MXQ74606ZJ"
        ],
        "enclosureGroupUri": "EG:EG"
    }
]

server_profile_templates = [
]
expected_server_profile_templates = [
]

server_profiles = [
]
expected_server_profiles = [
]

server_profile_with_storage = [
]
expected_server_profile_with_storage = [
]

configured_enclosures = [
    {
        "name": "MXQ74606ZJ",
        "state": "Configured",
        "serialNumber": "MXQ74606ZJ",
        "type": "EnclosureV7",
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
                "devicePresence": "Present"
            },
            {
                "bayNumber": 7,
                "devicePresence": "Present"
            },
            {
                "bayNumber": 8,
                "devicePresence": "Absent"
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
        "name": "MXQ74606ZN",
        "state": "Configured",
        "serialNumber": "MXQ74606ZN",
        "type": "EnclosureV7",
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
                "devicePresence": "Absent"
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
    }
]

servers = [
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 32768,
        "model": "Synergy 480 Gen9",
        "mpFirmwareVersion": "2.61 Jul 27 2018",
        "mpModel": "iLO4",
        "name": "MXQ74606ZJ, bay 6",
        "partNumber": "754683-001",
        "position": 6,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 10,
        "processorCount": 1,
        "processorSpeedMhz": 2200,
        "processorType": "Intel(R) Xeon(R) CPU E5-2630 v4 @ 2.20GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v2.62 (10/11/2018)",
        "serialNumber": "MXQ819009W",
        "shortModel": "SY 480 Gen9",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 32768,
        "model": "Synergy 480 Gen9",
        "mpFirmwareVersion": "2.61 Jul 27 2018",
        "mpModel": "iLO4",
        "name": "MXQ74606ZJ, bay 4",
        "partNumber": "754683-001",
        "position": 4,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 10,
        "processorCount": 1,
        "processorSpeedMhz": 2200,
        "processorType": "Intel(R) Xeon(R) CPU E5-2630 v4 @ 2.20GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v2.62 (10/11/2018)",
        "serialNumber": "MXQ819009X",
        "shortModel": "SY 480 Gen9",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 32768,
        "model": "Synergy 480 Gen9",
        "mpFirmwareVersion": "2.61 Jul 27 2018",
        "mpModel": "iLO4",
        "name": "MXQ74606ZJ, bay 5",
        "partNumber": "754683-001",
        "position": 5,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 10,
        "processorCount": 1,
        "processorSpeedMhz": 2200,
        "processorType": "Intel(R) Xeon(R) CPU E5-2630 v4 @ 2.20GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v2.62 (10/11/2018)",
        "serialNumber": "MXQ819009R",
        "shortModel": "SY 480 Gen9",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 32768,
        "model": "Synergy 480 Gen9",
        "mpFirmwareVersion": "2.61 Jul 27 2018",
        "mpModel": "iLO4",
        "name": "MXQ74606ZJ, bay 7",
        "partNumber": "754683-001",
        "position": 7,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 10,
        "processorCount": 2,
        "processorSpeedMhz": 2200,
        "processorType": "Intel(R) Xeon(R) CPU E5-2630 v4 @ 2.20GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v2.62 (10/11/2018)",
        "serialNumber": "MXQ744022X",
        "shortModel": "SY 480 Gen9",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 32768,
        "model": "Synergy 480 Gen9",
        "mpFirmwareVersion": "2.61 Jul 27 2018",
        "mpModel": "iLO4",
        "name": "MXQ74606ZJ, bay 3",
        "partNumber": "754683-001",
        "position": 3,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 10,
        "processorCount": 2,
        "processorSpeedMhz": 2200,
        "processorType": "Intel(R) Xeon(R) CPU E5-2630 v4 @ 2.20GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v2.62 (10/11/2018)",
        "serialNumber": "MXQ744024T",
        "shortModel": "SY 480 Gen9",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 16384,
        "model": "Synergy 480 Gen10",
        "mpFirmwareVersion": "1.40 Oct 29 2018",
        "mpModel": "iLO5",
        "name": "MXQ74606ZJ, bay 2",
        "partNumber": "854354-001",
        "position": 2,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 6,
        "processorCount": 2,
        "processorSpeedMhz": 1700,
        "processorType": "Intel(R) Xeon(R) Bronze 3104 CPU @ 1.70GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v2.00 (10/15/2018)",
        "serialNumber": "MXQ74603H2",
        "shortModel": "SY 480 Gen10",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 16384,
        "model": "Synergy 480 Gen10",
        "mpFirmwareVersion": "1.40 Oct 08 2018",
        "mpModel": "iLO5",
        "name": "MXQ74606ZN, bay 3",
        "partNumber": "854354-001",
        "position": 3,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 20,
        "processorCount": 2,
        "processorSpeedMhz": 2500,
        "processorType": "Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v2.00 (10/03/2018)",
        "serialNumber": "MXQ74603GS",
        "shortModel": "SY 480 Gen10",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 65536,
        "model": "Synergy 480 Gen10",
        "mpFirmwareVersion": "1.40 Oct 29 2018",
        "mpModel": "iLO5",
        "name": "MXQ74606ZN, bay 8",
        "partNumber": "854354-001",
        "position": 8,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 20,
        "processorCount": 2,
        "processorSpeedMhz": 2500,
        "processorType": "Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v2.00 (10/15/2018)",
        "serialNumber": "MXQ73306GJ",
        "shortModel": "SY 480 Gen10",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 65536,
        "model": "Synergy 480 Gen9",
        "mpFirmwareVersion": "2.61 Jul 27 2018",
        "mpModel": "iLO4",
        "name": "MXQ74606ZN, bay 7",
        "partNumber": "754683-001",
        "position": 7,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 14,
        "processorCount": 2,
        "processorSpeedMhz": 2000,
        "processorType": "Intel(R) Xeon(R) CPU E5-2660 v4 @ 2.00GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v2.62 (10/11/2018)",
        "serialNumber": "MXQ71902GY",
        "shortModel": "SY 480 Gen9",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 16384,
        "model": "Synergy 480 Gen10",
        "mpFirmwareVersion": "1.40 Oct 29 2018",
        "mpModel": "iLO5",
        "name": "MXQ74606ZN, bay 1",
        "partNumber": "854354-001",
        "position": 1,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 6,
        "processorCount": 2,
        "processorSpeedMhz": 1700,
        "processorType": "Intel(R) Xeon(R) Bronze 3104 CPU @ 1.70GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v2.00 (10/15/2018)",
        "serialNumber": "MXQ74603H8",
        "shortModel": "SY 480 Gen10",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 16384,
        "model": "Synergy 480 Gen10",
        "mpFirmwareVersion": "1.40 Oct 29 2018",
        "mpModel": "iLO5",
        "name": "MXQ74606ZN, bay 2",
        "partNumber": "854354-001",
        "position": 2,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 6,
        "processorCount": 2,
        "processorSpeedMhz": 1700,
        "processorType": "Intel(R) Xeon(R) Bronze 3104 CPU @ 1.70GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v2.00 (10/15/2018)",
        "serialNumber": "MXQ74603H4",
        "shortModel": "SY 480 Gen10",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 32768,
        "model": "Synergy 480 Gen9",
        "mpFirmwareVersion": "2.61 Jul 27 2018",
        "mpModel": "iLO4",
        "name": "MXQ74606ZJ, bay 1",
        "partNumber": "754683-001",
        "position": 1,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 10,
        "processorCount": 2,
        "processorSpeedMhz": 2200,
        "processorType": "Intel(R) Xeon(R) CPU E5-2630 v4 @ 2.20GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v2.62 (10/11/2018)",
        "serialNumber": "MXQ7440231",
        "shortModel": "SY 480 Gen9",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    }
]

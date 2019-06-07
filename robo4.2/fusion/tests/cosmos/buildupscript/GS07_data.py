#!/usr/bin/env python

admin_credentials = {'userName': 'Administrator', 'password': 'Cosmos123'}
timeandlocale = {'localeDisplayName': 'English (United States)', 'locale': 'en_US.UTF-8', 'dateTime': '2018-09-17T19:03:32.602Z', 'ntpServers': [], 'timezone': 'UTC', 'type': 'TimeAndLocale'}
licenses = [
    {
        'key': '9B2G D9MA H9PA CHVZ V2B4 HWWV Y9JL KMPL B89H MZVU 6RMS 9HWE 92R6 3FZ3 CMRG HPMR MFVU A5K9 MHGK EKX9 HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'
    },
    {
        'key': 'YB2C D9MA H9PA 8HU3 V2B4 HWWV Y9JL KMPL B89H MZVU GR4S JHWE 9QSP XFR8 CMRG HPMR UFVU A5K9 MWHC 9K4K HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'
    },
    {
        'key': 'YBKA D9MA H9P9 8HX3 V2B4 HWWV Y9JL KMPL B89H MZVU GR4S JHWE J2SP XNZ8 CMRG HPMR UFVU A5K9 MWHC 9K4K HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'
    },
    {
        'key': 'YBCG D9MA H9PA GHUY V2B4 HWWV Y9JL KMPL B89H MZVU GR4S JHWE JVSH XV5S CMRG HPMR UFVU A5K9 MWHC 9K4K HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'
    }
]

appliance = {
    'type': "ApplianceNetworkConfigurationV2",
    'applianceNetworks':
    [{
        "device": "bond0",
        "macAddress": "30:e1:71:68:da:30",
        "interfaceName": "Appliance",
        "activeNode": 1,
        "unconfigure": False,
        "ipv4Type": "STATIC",
        "ipv4Subnet": "255.255.255.0",
        "ipv4Gateway": "10.5.0.1",
        "ipv4NameServers": [u'10.5.0.11'],
        "app1Ipv4Addr": "10.5.0.16",
        "ipv6Type": "UNCONFIGURE",
        "hostname": "GS07.cosmosblrinfra.net",
        "confOneNode": False,
        "domainName": "cosmosblrinfra.net",
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
                "value": 'Cisco',
            },
            {
                "name": "Host",
                "value": "10.2.0.5"
            },
            {
                "name": "SnmpPort",
                "value": 161
            },
            {
                "name": "SnmpUserName",
                "value": "cst"
            },
            {
                "name": "SnmpAuthLevel",
                "value": "authpriv"
            },
            {
                "name": "SnmpAuthString",
                "value": "cosmos@123"
            },
            {
                "name": "SnmpPrivString",
                "value": "cosmos@123"
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
                "value": 'Cisco',
            },
            {
                "name": "Host",
                "value": "10.2.0.6"
            },
            {
                "name": "SnmpPort",
                "value": 161
            },
            {
                "name": "SnmpUserName",
                "value": "cst"
            },
            {
                "name": "SnmpAuthLevel",
                "value": "authpriv"
            },
            {
                "name": "SnmpAuthString",
                "value": "cosmos@123"
            },
            {
                "name": "SnmpPrivString",
                "value": "cosmos@123"
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
                "value": "10.6.0.10"
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
                "value": "10.2.0.17"
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
        "uri": "SAN:10.2.0.5",
        "name": "10.2.0.5",
        "type": "FCDeviceManagerV2",
        "category": "fc-device-managers",
        "state": "Managed",
        "description": "MDS 9148 FC (1 Slot) Chassis",
        "deviceManagerVersion": "6.2(21)",
        "isInternal": "False",
        "providerDisplayName": "Cisco",
        "refreshState": "Stable",
        "status": "OK",
        "connectionInfo": [
            {
                "name": "Host",
                "value": "10.2.0.5"
            },
            {
                "name": "SnmpPort",
                "value": 161
            },
            {
                "name": "SnmpUserName",
                "value": "cst"
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
        "uri": "SAN:10.2.0.6",
        "name": "10.2.0.6",
        "type": "FCDeviceManagerV2",
        "category": "fc-device-managers",
        "state": "Managed",
        "description": "MDS 9148 FC (1 Slot) Chassis",
        "deviceManagerVersion": "6.2(21)",
        "isInternal": "False",
        "providerDisplayName": "Cisco",
        "refreshState": "Stable",
        "status": "OK",
        "connectionInfo": [
            {
                "name": "Host",
                "value": "10.2.0.6"
            },
            {
                "name": "SnmpPort",
                "value": 161
            },
            {
                "name": "SnmpUserName",
                "value": "cst"
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
        "uri": "SAN:10.6.0.10",
        "name": "10.6.0.10",
        "type": "FCDeviceManagerV2",
        "category": "fc-device-managers",
        "state": "Managed",
        "description": "HPE FF 5700-40XG-2QSFP+ Switch",
        "deviceManagerVersion": "7.1.045 Release 2422P01",
        "isInternal": "False",
        "providerDisplayName": "HPE",
        "refreshState": "Stable",
        "status": "OK",
        "connectionInfo": [
            {
                "name": "Host",
                "value": "10.6.0.10"
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
        "uri": "SAN:10.2.0.17",
        "name": "10.2.0.17",
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
                "value": "10.2.0.17"
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
        "name": "Eth_1003",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1003
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth_1004",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1004
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth_1001",
        "privateNetwork": False,
        "purpose": "Management",
        "smartLink": True,
        "vlanId": 1001
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth_1002",
        "privateNetwork": False,
        "purpose": "VMMigration",
        "smartLink": True,
        "vlanId": 1002
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth_1005",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1005
    }
]
expected_ethernet_networks = [
    {
        "uri": "ETH:Eth_1003",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth_1003",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1003
    },
    {
        "uri": "ETH:Eth_1004",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth_1004",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1004
    },
    {
        "uri": "ETH:Eth_1001",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth_1001",
        "privateNetwork": False,
        "purpose": "Management",
        "smartLink": True,
        "vlanId": 1001
    },
    {
        "uri": "ETH:Eth_1002",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth_1002",
        "privateNetwork": False,
        "purpose": "VMMigration",
        "smartLink": True,
        "vlanId": 1002
    },
    {
        "uri": "ETH:Eth_1005",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth_1005",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1005
    }
]

fc_networks = [
    {
        "type": "fc-networkV4",
        "name": "Potash-FC1",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:SN660B-2"
    },
    {
        "type": "fc-networkV4",
        "name": "FC-Cisco-2",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:VSAN1005"
    },
    {
        "type": "fc-networkV4",
        "name": "Potash-DA1",
        "fabricType": "DirectAttach",
        "linkStabilityTime": 0,
        "autoLoginRedistribution": False,
        "managedSanUri": None
    },
    {
        "type": "fc-networkV4",
        "name": "FC-Cisco-1",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:VSAN1002"
    },
    {
        "type": "fc-networkV4",
        "name": "Carbon-FC2",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:SN6600B"
    },
    {
        "type": "fc-networkV4",
        "name": "Potash-FC2",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:SN660B-2"
    },
    {
        "type": "fc-networkV4",
        "name": "Carbon-FC1",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:SN6600B"
    },
    {
        "type": "fc-networkV4",
        "name": "Potash-DA2",
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
        "uri": "FC:Potash-FC1",
        "status": "OK",
        "type": "fc-networkV4",
        "name": "Potash-FC1",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:SN660B-2"
    },
    {
        "category": "fc-networks",
        "state": "Active",
        "description": None,
        "uri": "FC:FC-Cisco-2",
        "status": "OK",
        "type": "fc-networkV4",
        "name": "FC-Cisco-2",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:VSAN1005"
    },
    {
        "category": "fc-networks",
        "state": "Active",
        "description": None,
        "uri": "FC:Potash-DA1",
        "status": "OK",
        "type": "fc-networkV4",
        "name": "Potash-DA1",
        "fabricType": "DirectAttach",
        "linkStabilityTime": 0,
        "autoLoginRedistribution": False,
        "managedSanUri": None
    },
    {
        "category": "fc-networks",
        "state": "Active",
        "description": None,
        "uri": "FC:FC-Cisco-1",
        "status": "OK",
        "type": "fc-networkV4",
        "name": "FC-Cisco-1",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:VSAN1002"
    },
    {
        "category": "fc-networks",
        "state": "Active",
        "description": None,
        "uri": "FC:Carbon-FC2",
        "status": "OK",
        "type": "fc-networkV4",
        "name": "Carbon-FC2",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:SN6600B"
    },
    {
        "category": "fc-networks",
        "state": "Active",
        "description": None,
        "uri": "FC:Potash-FC2",
        "status": "OK",
        "type": "fc-networkV4",
        "name": "Potash-FC2",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:SN660B-2"
    },
    {
        "category": "fc-networks",
        "state": "Active",
        "description": None,
        "uri": "FC:Carbon-FC1",
        "status": "OK",
        "type": "fc-networkV4",
        "name": "Carbon-FC1",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:SN6600B"
    },
    {
        "category": "fc-networks",
        "state": "Active",
        "description": None,
        "uri": "FC:Potash-DA2",
        "status": "OK",
        "type": "fc-networkV4",
        "name": "Potash-DA2",
        "fabricType": "DirectAttach",
        "linkStabilityTime": 0,
        "autoLoginRedistribution": False,
        "managedSanUri": None
    }
]

fcoe_networks = [
    {
        "name": "FCF-1900",
        "type": "fcoe-networkV4",
        "vlanId": 1900,
        "managedSanUri": "FCSan:VSAN1900"
    },
    {
        "name": "FCF-2000",
        "type": "fcoe-networkV4",
        "vlanId": 2000,
        "managedSanUri": "FCSan:VSAN2000"
    },
    {
        "name": "Transit-3400",
        "type": "fcoe-networkV4",
        "vlanId": 3400,
        "managedSanUri": "FCSan:VSAN3400"
    },
    {
        "name": "Transit-3500",
        "type": "fcoe-networkV4",
        "vlanId": 3500,
        "managedSanUri": "FCSan:VSAN3500"
    }
]
expected_fcoe_networks = [
    {
        "uri": "FCOE:FCF-1900",
        "state": "Active",
        "status": "OK",
        "name": "FCF-1900",
        "type": "fcoe-networkV4",
        "vlanId": 1900,
        "managedSanUri": "FCSan:VSAN1900"
    },
    {
        "uri": "FCOE:FCF-2000",
        "state": "Active",
        "status": "OK",
        "name": "FCF-2000",
        "type": "fcoe-networkV4",
        "vlanId": 2000,
        "managedSanUri": "FCSan:VSAN2000"
    },
    {
        "uri": "FCOE:Transit-3400",
        "state": "Active",
        "status": "OK",
        "name": "Transit-3400",
        "type": "fcoe-networkV4",
        "vlanId": 3400,
        "managedSanUri": "FCSan:VSAN3400"
    },
    {
        "uri": "FCOE:Transit-3500",
        "state": "Active",
        "status": "OK",
        "name": "Transit-3500",
        "type": "fcoe-networkV4",
        "vlanId": 3500,
        "managedSanUri": "FCSan:VSAN3500"
    }
]

networksets = [
]
expected_networksets = [
]

storage_systems_with_pools = [
    {
        "credentials": {'username': '3paradm', 'password': '3pardata'},
        "name": "3PAR8200-CHO-10",
        "family": "StoreServ",
        "hostname": "10.2.0.10",
        "deviceSpecificAttributes": {
            "managedDomain": "CST-AS",
            "managedPools": [{'domain': 'CST-AS', 'name': 'FC_r5', 'raidLevel': 'RAID5', 'state': 'Managed', 'deviceType': 'FC', 'freeCapacity': '396210733056', 'totalCapacity': '4490388307968', 'uuid': '21b964d9-a57c-4335-a73c-cd6d8346e475'}],
            "discoveredPools": [],

        },
    },
    {
        "credentials": {'username': '3paradm', 'password': '3pardata'},
        "name": "CST-iSCSI-8200N-20",
        "family": "StoreServ",
        "hostname": "10.2.0.20",
        "deviceSpecificAttributes": {
            "managedDomain": "CST-AS",
            "managedPools": [{'domain': 'CST-AS', 'name': 'Domain20', 'raidLevel': 'RAID0', 'state': 'Managed', 'deviceType': 'FC', 'freeCapacity': '8814346633216', 'totalCapacity': '9003325194240', 'uuid': 'c325edaa-46a8-4aab-85c2-dbce08676d16'}],
            "discoveredPools": [{'domain': 'CST-AS', 'name': 'FC_r6', 'raidLevel': 'RAID6', 'state': 'Discovered', 'deviceType': 'FC', 'freeCapacity': '5873904648192', 'totalCapacity': '5873904648192', 'uuid': '020bde4b-cdfb-4203-8a67-d08020842075'}],

        },
    },
    {
        "credentials": {'username': '3paradm', 'password': '3pardata'},
        "name": "CST-FCoE-8200N-30",
        "family": "StoreServ",
        "hostname": "10.2.0.30",
        "deviceSpecificAttributes": {
            "managedDomain": "CST-AS",
            "managedPools": [{'domain': 'CST-AS', 'name': 'Domain30', 'raidLevel': 'RAID0', 'state': 'Managed', 'deviceType': 'FC', 'freeCapacity': '8277475721216', 'totalCapacity': '8397734805504', 'uuid': '86088da5-429c-4663-8df1-0faf6fb794c5'}],
            "discoveredPools": [{'domain': 'CST-AS', 'name': 'FC_r6', 'raidLevel': 'RAID6', 'state': 'Discovered', 'deviceType': 'FC', 'freeCapacity': '5513127395328', 'totalCapacity': '5564398567424', 'uuid': '1244ce78-3709-4cb0-8b09-804c28295602'}],

        },
    },
    {
        "credentials": {'username': '3paradm', 'password': '3pardata'},
        "name": "3PAR20K_EB2603_5",
        "family": "StoreServ",
        "hostname": "10.5.0.5",
        "deviceSpecificAttributes": {
            "managedDomain": "NO DOMAIN",
            "managedPools": [{'domain': 'NO DOMAIN', 'name': 'SSD_r5', 'raidLevel': 'RAID5', 'state': 'Managed', 'deviceType': 'SSD', 'freeCapacity': '705448378368', 'totalCapacity': '774167855104', 'uuid': 'ad0cf501-5a8a-46a9-9781-923c1be32a1f'}],
            "discoveredPools": [{'domain': 'NO DOMAIN', 'name': 'NL_r6', 'raidLevel': 'RAID6', 'state': 'Discovered', 'deviceType': 'NL', 'freeCapacity': '41811506626560', 'totalCapacity': '41983305318400', 'uuid': 'b5f1f42d-cd2b-4d1d-9c29-a68d800515e7'}, {'domain': 'NO DOMAIN', 'name': 'SSD_r1', 'raidLevel': 'RAID1', 'state': 'Discovered', 'deviceType': 'SSD', 'freeCapacity': '470298918912', 'totalCapacity': '470298918912', 'uuid': '5cfcb074-d008-447f-9ae6-a0b0d1a56af4'}],

        }
    }
]
expected_storage_systems_with_pools = [
    {
        "uri": "SSYS:3PAR8200-CHO-10",
        "type": "StorageSystemV5",
        "state": "Managed",
        "category": "storage-systems",
        "status": "OK",
        "name": "3PAR8200-CHO-10",
        "family": "StoreServ",
        "hostname": "10.2.0.10",
        "deviceSpecificAttributes": {
            "managedDomain": "CST-AS",
            "serialNumber": "7CE611P3Y3"
        },
    },
    {
        "uri": "SSYS:CST-iSCSI-8200N-20",
        "type": "StorageSystemV5",
        "state": "Managed",
        "category": "storage-systems",
        "status": "OK",
        "name": "CST-iSCSI-8200N-20",
        "family": "StoreServ",
        "hostname": "10.2.0.20",
        "deviceSpecificAttributes": {
            "managedDomain": "CST-AS",
            "serialNumber": "CZ3742Y540"
        },
    },
    {
        "uri": "SSYS:CST-FCoE-8200N-30",
        "type": "StorageSystemV5",
        "state": "Managed",
        "category": "storage-systems",
        "status": "OK",
        "name": "CST-FCoE-8200N-30",
        "family": "StoreServ",
        "hostname": "10.2.0.30",
        "deviceSpecificAttributes": {
            "managedDomain": "CST-AS",
            "serialNumber": "CZ3742Y541"
        },
    },
    {
        "uri": "SSYS:3PAR20K_EB2603_5",
        "type": "StorageSystemV5",
        "state": "Managed",
        "category": "storage-systems",
        "status": "OK",
        "name": "3PAR20K_EB2603_5",
        "family": "StoreServ",
        "hostname": "10.5.0.5",
        "deviceSpecificAttributes": {
            "managedDomain": "NO DOMAIN",
            "serialNumber": "SGH825SKKJ"
        }
    }
]

storage_pools_toedit = [
    {
        "storageSystemUri": "3PAR8200-CHO-10",
        "name": "FC_r5",
        "isManaged": True,
    },
    {
        "storageSystemUri": "CST-iSCSI-8200N-20",
        "name": "Domain20",
        "isManaged": True,
    },
    {
        "storageSystemUri": "CST-iSCSI-8200N-20",
        "name": "FC_r6",
        "isManaged": True,
    },
    {
        "storageSystemUri": "CST-FCoE-8200N-30",
        "name": "Domain30",
        "isManaged": True,
    },
    {
        "storageSystemUri": "CST-FCoE-8200N-30",
        "name": "FC_r6",
        "isManaged": True,
    },
    {
        "storageSystemUri": "3PAR20K_EB2603_5",
        "name": "NL_r6",
        "isManaged": True,
    },
    {
        "storageSystemUri": "3PAR20K_EB2603_5",
        "name": "SSD_r1",
        "isManaged": True,
    },
    {
        "storageSystemUri": "3PAR20K_EB2603_5",
        "name": "SSD_r5",
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
        "name": "Bayset2-Carbon",
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
                "bay": 2,
                "enclosure": -1,
                "type": "Virtual Connect SE 16Gb FC Module for Synergy"
            },
            {
                "enclosureIndex": -1,
                "enclosure": -1,
                "bay": 5,
                "type": "Virtual Connect SE 16Gb FC Module for Synergy"
            }

        ],
        "interconnectBaySet": 2,
        "redundancyType": "Redundant",
        "telemetryConfiguration": {
            "enableTelemetry": True,
            "sampleCount": 60,
            "sampleInterval": 60
        },
        "uplinkSets": [{
            "ethernetNetworkType": "NotApplicable",
            "lacpTimer": None,
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "enclosure": "-1",
                    "port": "1",
                    "bay": "2"
                },
                {
                    "speed": "Auto",
                    "enclosure": "-1",
                    "port": "2",
                    "bay": "2"
                }
            ],
            "mode": "Auto",
            "name": "FC-1",
            "nativeNetworkUri": None,
            "networkType": "FibreChannel",
            "networkUris": [
                "Carbon-FC1"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "NotApplicable",
            "lacpTimer": None,
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "bay": "5",
                    "port": "1",
                    "enclosure": "-1"
                },
                {
                    "speed": "Auto",
                    "bay": "5",
                    "port": "2",
                    "enclosure": "-1"
                }
            ],
            "mode": "Auto",
            "name": "FC-2",
            "nativeNetworkUri": None,
            "networkType": "FibreChannel",
            "networkUris": [
                "Carbon-FC2"
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
        "name": "Bayset3-Potash",
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
                "enclosureIndex": 1,
                "enclosure": 1,
                "bay": 3,
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
                "bay": 6,
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
        "uplinkSets": [{
            "ethernetNetworkType": "Tagged",
            "lacpTimer": "Short",
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "bay": "3",
                    "enclosure": "1",
                    "port": "Q2"
                },
                {
                    "speed": "Auto",
                    "bay": "6",
                    "enclosure": "2",
                    "port": "Q2"
                },
                {
                    "speed": "Auto",
                    "bay": "3",
                    "port": "Q1",
                    "enclosure": "1"
                },
                {
                    "speed": "Auto",
                    "bay": "6",
                    "port": "Q1",
                    "enclosure": "2"
                }
            ],
            "mode": "Auto",
            "name": "Eth-Transit",
            "nativeNetworkUri": None,
            "networkType": "Ethernet",
            "networkUris": [
                "Eth_1005",
                "Eth_1001",
                "Eth_1002",
                "Eth_1004",
                "Eth_1003",
                "Transit-3400",
                "Transit-3500"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "NotApplicable",
            "lacpTimer": None,
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "bay": "6",
                    "port": "Q3.1",
                    "enclosure": "2"
                }
            ],
            "mode": "Auto",
            "name": "Potash-FC2",
            "nativeNetworkUri": None,
            "networkType": "FibreChannel",
            "networkUris": [
                "Potash-FC2"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "Tagged",
            "lacpTimer": "Short",
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "port": "Q4.4",
                    "enclosure": "1",
                    "bay": "3"
                },
                {
                    "speed": "Auto",
                    "bay": "3",
                    "port": "Q4.3",
                    "enclosure": "1"
                },
                {
                    "speed": "Auto",
                    "port": "Q4.4",
                    "enclosure": "2",
                    "bay": "6"
                },
                {
                    "speed": "Auto",
                    "bay": "3",
                    "port": "Q4.2",
                    "enclosure": "1"
                },
                {
                    "speed": "Auto",
                    "bay": "6",
                    "port": "Q4.3",
                    "enclosure": "2"
                },
                {
                    "speed": "Auto",
                    "bay": "3",
                    "port": "Q4.1",
                    "enclosure": "1"
                },
                {
                    "speed": "Auto",
                    "bay": "6",
                    "port": "Q4.2",
                    "enclosure": "2"
                },
                {
                    "speed": "Auto",
                    "bay": "6",
                    "port": "Q4.1",
                    "enclosure": "2"
                }
            ],
            "mode": "Auto",
            "name": "FCF-1900-2000",
            "nativeNetworkUri": None,
            "networkType": "Ethernet",
            "networkUris": [
                "FCF-1900",
                "FCF-2000"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "NotApplicable",
            "lacpTimer": None,
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "bay": "6",
                    "enclosure": "2",
                    "port": "Q6:1"
                }
            ],
            "mode": "Auto",
            "name": "Cisco-FC2",
            "nativeNetworkUri": None,
            "networkType": "FibreChannel",
            "networkUris": [
                "FC-Cisco-2"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "NotApplicable",
            "lacpTimer": None,
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "bay": "3",
                    "port": "Q6:1",
                    "enclosure": "1"
                }
            ],
            "mode": "Auto",
            "name": "Cisco-FC1",
            "nativeNetworkUri": None,
            "networkType": "FibreChannel",
            "networkUris": [
                "FC-Cisco-1"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "NotApplicable",
            "lacpTimer": None,
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "bay": "3",
                    "port": "Q3.1",
                    "enclosure": "1"
                }
            ],
            "mode": "Auto",
            "name": "Potash-FC1",
            "nativeNetworkUri": None,
            "networkType": "FibreChannel",
            "networkUris": [
                "Potash-FC1"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "NotApplicable",
            "lacpTimer": None,
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "bay": "3",
                    "enclosure": "1",
                    "port": "Q5:1"
                }
            ],
            "mode": "Auto",
            "name": "DA-1",
            "nativeNetworkUri": None,
            "networkType": "FibreChannel",
            "networkUris": [
                "Potash-DA1"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "NotApplicable",
            "lacpTimer": None,
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "bay": "6",
                    "enclosure": "2",
                    "port": "Q5:1"
                }
            ],
            "mode": "Auto",
            "name": "DA-2",
            "nativeNetworkUri": None,
            "networkType": "FibreChannel",
            "networkUris": [
                "Potash-DA2"
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
        "uri": "LIG:Bayset2-Carbon",
        "status": None,
        "stackingHealth": None,
        "category": "logical-interconnect-groups",
        "state": "Active",
        "internalNetworkUris": "[]",
        "stackingMode": None,
        "description": None,
        "name": "Bayset2-Carbon",
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
        "uri": "LIG:Bayset3-Potash",
        "status": None,
        "stackingHealth": None,
        "category": "logical-interconnect-groups",
        "state": "Active",
        "internalNetworkUris": "[]",
        "stackingMode": None,
        "description": None,
        "name": "Bayset3-Potash",
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
                "interconnectBay": 2,
                "logicalInterconnectGroupUri": "LIG:Bayset2-Carbon",
                "enclosureIndex": 1
            },
            {
                "interconnectBay": 3,
                "logicalInterconnectGroupUri": "LIG:Bayset3-Potash",

            },
            {
                "interconnectBay": 5,
                "logicalInterconnectGroupUri": "LIG:Bayset2-Carbon",
                "enclosureIndex": 1
            },
            {
                "interconnectBay": 6,
                "logicalInterconnectGroupUri": "LIG:Bayset3-Potash",

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
        "associatedLogicalInterconnectGroups": [u'LIG:Bayset2-Carbon', u'LIG:Bayset3-Potash'],
        "name": "EG",
        "type": "EnclosureGroupV7",
        "enclosureTypeUri": "/rest/enclosure-types/SY12000",
        "stackingMode": "Enclosure",
        "name": "EG",
        "interconnectBayMappingCount": "4",
        "interconnectBayMappings": [
            {
                "interconnectBay": 2,
                "logicalInterconnectGroupUri": "LIG:Bayset2-Carbon",

            },
            {
                "interconnectBay": 3,
                "logicalInterconnectGroupUri": "LIG:Bayset3-Potash",

            },
            {
                "interconnectBay": 5,
                "logicalInterconnectGroupUri": "LIG:Bayset2-Carbon",

            },
            {
                "interconnectBay": 6,
                "logicalInterconnectGroupUri": "LIG:Bayset3-Potash",

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
            "ENC:CN7545084D",
            "ENC:MXQ74700C0"
        ],
        "enclosureGroupUri": "EG:EG"
    }
]
expected_logical_enclosure = [
    {
        "type": "LogicalEnclosureV4",
        "uri": "LE",
        "status": "OK",
        "name": "LE",
        "enclosureUris": [
            "ENC:CN7545084D",
            "ENC:MXQ74700C0"
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
        "name": "CN7545084D",
        "state": "Configured",
        "serialNumber": "CN7545084D",
        "type": "EnclosureV7",
        "refreshState": "NotRefreshing",
        "deviceBays": [
            {
                "bayNumber": 1,
                "devicePresence": "Present"
            },
            {
                "bayNumber": 2,
                "devicePresence": "Absent"
            },
            {
                "bayNumber": 3,
                "devicePresence": "Absent"
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
                "devicePresence": "Subsumed"
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
        "name": "MXQ74700C0",
        "state": "Configured",
        "serialNumber": "MXQ74700C0",
        "type": "EnclosureV7",
        "refreshState": "NotRefreshing",
        "deviceBays": [
            {
                "bayNumber": 1,
                "devicePresence": "Absent"
            },
            {
                "bayNumber": 2,
                "devicePresence": "Absent"
            },
            {
                "bayNumber": 3,
                "devicePresence": "Absent"
            },
            {
                "bayNumber": 4,
                "devicePresence": "Absent"
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
                "devicePresence": "Present"
            },
            {
                "bayNumber": 12,
                "devicePresence": "Present"
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
        "model": "Synergy 480 Gen10",
        "mpFirmwareVersion": "1.40 Aug 20 2018",
        "mpModel": "iLO5",
        "name": "CN7545084D, bay 4",
        "partNumber": "871945-B21",
        "position": 4,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 12,
        "processorCount": 1,
        "processorSpeedMhz": 2300,
        "processorType": "Intel(R) Xeon(R) Gold 5118 CPU @ 2.30GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v2.00 (08/07/2018)",
        "serialNumber": "CN7809003V",
        "shortModel": "SY 480 Gen10",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "FullHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 131072,
        "model": "Synergy 660 Gen10",
        "mpFirmwareVersion": "1.40 Aug 20 2018",
        "mpModel": "iLO5",
        "name": "CN7545084D, bay 1",
        "partNumber": "871933-B21",
        "position": 1,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 18,
        "processorCount": 2,
        "processorSpeedMhz": 2300,
        "processorType": "Intel(R) Xeon(R) Gold 6140 CPU @ 2.30GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I43 v2.00 (08/07/2018)",
        "serialNumber": "CN780900VQ",
        "shortModel": "SY 660 Gen10",
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
        "mpFirmwareVersion": "1.40 Aug 20 2018",
        "mpModel": "iLO5",
        "name": "MXQ74700C0, bay 8",
        "partNumber": "871946-B21",
        "position": 8,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 6,
        "processorCount": 1,
        "processorSpeedMhz": 1700,
        "processorType": "Intel(R) Xeon(R) Bronze 3104 CPU @ 1.70GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v2.00 (08/07/2018)",
        "serialNumber": "MXQ74306BM",
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
        "model": "Synergy 480 Gen10",
        "mpFirmwareVersion": "1.40 Aug 20 2018",
        "mpModel": "iLO5",
        "name": "MXQ74700C0, bay 6",
        "partNumber": "871945-B21",
        "position": 6,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 12,
        "processorCount": 1,
        "processorSpeedMhz": 2300,
        "processorType": "Intel(R) Xeon(R) Gold 5118 CPU @ 2.30GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v2.00 (08/07/2018)",
        "serialNumber": "CN7809003S",
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
        "mpFirmwareVersion": "1.40 Aug 20 2018",
        "mpModel": "iLO5",
        "name": "MXQ74700C0, bay 9",
        "partNumber": "871943-B21",
        "position": 9,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 16,
        "processorCount": 2,
        "processorSpeedMhz": 2100,
        "processorType": "Intel(R) Xeon(R) Gold 6130 CPU @ 2.10GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v2.00 (08/07/2018)",
        "serialNumber": "MXQ74201G0",
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
        "mpFirmwareVersion": "1.40 Aug 20 2018",
        "mpModel": "iLO5",
        "name": "MXQ74700C0, bay 11",
        "partNumber": "871940-B21",
        "position": 11,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 4,
        "processorCount": 2,
        "processorSpeedMhz": 2600,
        "processorType": "Intel(R) Xeon(R) Silver 4112 CPU @ 2.60GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v2.00 (08/07/2018)",
        "serialNumber": "SGH820TL9J",
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
        "name": "MXQ74700C0, bay 10",
        "partNumber": "826951-B21",
        "position": 10,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 14,
        "processorCount": 2,
        "processorSpeedMhz": 2000,
        "processorType": "Intel(R) Xeon(R) CPU E5-2660 v4 @ 2.00GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v2.60 (05/21/2018)",
        "serialNumber": "MXQ74306T4",
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
        "name": "MXQ74700C0, bay 5",
        "partNumber": "826953-B21",
        "position": 5,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 10,
        "processorCount": 1,
        "processorSpeedMhz": 2200,
        "processorType": "Intel(R) Xeon(R) CPU E5-2630 v4 @ 2.20GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v2.60 (05/21/2018)",
        "serialNumber": "MXQ744023C",
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
        "mpFirmwareVersion": "1.40 Aug 20 2018",
        "mpModel": "iLO5",
        "name": "MXQ74700C0, bay 12",
        "partNumber": "871940-B21",
        "position": 12,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 4,
        "processorCount": 2,
        "processorSpeedMhz": 2600,
        "processorType": "Intel(R) Xeon(R) Silver 4112 CPU @ 2.60GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v2.00 (08/07/2018)",
        "serialNumber": "SGH820VALP",
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
        "model": "Synergy 480 Gen10",
        "mpFirmwareVersion": "1.40 Aug 20 2018",
        "mpModel": "iLO5",
        "name": "MXQ74700C0, bay 7",
        "partNumber": "871945-B21",
        "position": 7,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 12,
        "processorCount": 1,
        "processorSpeedMhz": 2300,
        "processorType": "Intel(R) Xeon(R) Gold 5118 CPU @ 2.30GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v2.00 (08/07/2018)",
        "serialNumber": "MXQ74307K5",
        "shortModel": "SY 480 Gen10",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    }
]

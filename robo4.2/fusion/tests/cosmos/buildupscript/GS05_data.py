#!/usr/bin/env python

admin_credentials = {'userName': 'Administrator', 'password': 'Cosmos123'}
timeandlocale = {'localeDisplayName': 'English (United States)', 'locale': 'en_US.UTF-8', 'dateTime': '2018-09-17T07:59:43.713Z', 'ntpServers': [], 'timezone': 'UTC', 'type': 'TimeAndLocale'}
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
        "macAddress": "14:02:ec:46:43:f0",
        "interfaceName": "Appliance",
        "activeNode": 1,
        "unconfigure": False,
        "ipv4Type": "STATIC",
        "ipv4Subnet": "255.255.255.0",
        "ipv4Gateway": "10.4.0.1",
        "ipv4NameServers": [u'10.4.0.11'],
        "app1Ipv4Addr": "10.4.0.16",
        "ipv6Type": "UNCONFIGURE",
        "hostname": "T05.cosmosblrinfra.net",
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

ipv4_subnet = [
    {
        'type': "Subnet",
        'name': "10.3.0.0",
        'networkId': "10.3.0.0",
        'subnetmask': "255.255.255.0",
        'gateway': "10.3.0.1",
        'domain': "cosmosblrinfra.net",
        'dnsServers': [u'10.3.0.11', u'10.4.0.11']
    },
    {
        'type': "Subnet",
        'name': "10.4.0.0",
        'networkId': "10.4.0.0",
        'subnetmask': "255.255.255.0",
        'gateway': "10.4.0.1",
        'domain': "cosmosblrinfra.net",
        'dnsServers': [u'10.4.0.11']
    },
    {
        'type': "Subnet",
        'name': "192.168.0.0",
        'networkId': "192.168.0.0",
        'subnetmask': "255.255.0.0",
        'gateway': "192.168.2.1",
        'domain': "i3s.net",
        'dnsServers': None
    }
]

ipv4_ranges = [
    {
        'type': "Range",
        'name': "clrn",
        'startAddress': "10.3.0.230",
        'endAddress': "10.3.0.245",
        "subnetUri": "10.3.0.0"
    },
    {
        'type': "Range",
        'name': "MGMT",
        'startAddress': "10.4.0.150",
        'endAddress': "10.4.0.250",
        "subnetUri": "10.4.0.0"
    },
    {
        'type': "Range",
        'name': "i3s-net",
        'startAddress': "192.168.2.3",
        'endAddress': "192.168.2.254",
        "subnetUri": "192.168.0.0"
    }
]

ranges = [
    {
        'type': "Range",
        'name': "VMAC",
        'category': "id-range-VMAC",
        'rangeCategory': "Generated",
        'startAddress': "36:48:DA:F0:00:00",
        'endAddress': "36:48:DA:FF:FF:FF",
        'enabled': True
    },
    {
        'type': "Range",
        'name': "VWWN",
        'category': "id-range-VWWN",
        'rangeCategory': "Generated",
        'startAddress': "10:00:fa:26:06:80:00:00",
        'endAddress': "10:00:fa:26:06:8f:ff:ff",
        'enabled': True
    },
    {
        'type': "Range",
        'name': "VSN",
        'category': "id-range-VSN",
        'rangeCategory': "Generated",
        'startAddress': "VCGOIBW000",
        'endAddress': "VCGOIBWZZZ",
        'enabled': True
    }
]

deployment_server = [
    {
        'deplManagersType': "Image Streamer",
        'name': "T05-OSDS",
        'description': "",
        'mgmtNetworkUri': [u'i3s-mgmt'],
        'applianceUri': 'MXQ74606ZM, appliance 1'
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
    }
]

ethernet_networks = [
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth-1001",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1001
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth-1002",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1002
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth-1005",
        "privateNetwork": False,
        "purpose": "VMMigration",
        "smartLink": True,
        "vlanId": 1005
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth-1004",
        "privateNetwork": False,
        "purpose": "Management",
        "smartLink": True,
        "vlanId": 1004
    }
]
expected_ethernet_networks = [
    {
        "uri": "ETH:Eth-1001",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth-1001",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1001
    },
    {
        "uri": "ETH:Eth-1002",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth-1002",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1002
    },
    {
        "uri": "ETH:Eth-1005",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth-1005",
        "privateNetwork": False,
        "purpose": "VMMigration",
        "smartLink": True,
        "vlanId": 1005
    },
    {
        "uri": "ETH:Eth-1004",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth-1004",
        "privateNetwork": False,
        "purpose": "Management",
        "smartLink": True,
        "vlanId": 1004
    }
]
i3s_networks = [
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth-1004-mgmt",
        "privateNetwork": False,
        "purpose": "Management",
        "smartLink": True,
        "vlanId": 1004
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "i3s-deploy",
        "privateNetwork": False,
        "purpose": "ISCSI",
        "smartLink": True,
        "vlanId": 2450
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "i3s-mgmt",
        "privateNetwork": False,
        "purpose": "Management",
        "smartLink": True,
        "vlanId": 1004
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth-1003",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1003
    }
]
expected_i3s_networks = [
    {
        "type": "ethernet-networkV4",
        "status": "OK",
        "state": "Active",
        "ethernetNetworkType": "Tagged",
        "name": "Eth-1004-mgmt",
        "uri": "ETH:Eth-1004-mgmt",
        "privateNetwork": False,
        "purpose": "Management",
        "smartLink": True,
        "vlanId": 1004
    },
    {
        "type": "ethernet-networkV4",
        "status": "OK",
        "state": "Active",
        "ethernetNetworkType": "Tagged",
        "name": "i3s-deploy",
        "uri": "ETH:i3s-deploy",
        "privateNetwork": False,
        "purpose": "ISCSI",
        "smartLink": True,
        "vlanId": 2450
    },
    {
        "type": "ethernet-networkV4",
        "status": "OK",
        "state": "Active",
        "ethernetNetworkType": "Tagged",
        "name": "i3s-mgmt",
        "uri": "ETH:i3s-mgmt",
        "privateNetwork": False,
        "purpose": "Management",
        "smartLink": True,
        "vlanId": 1004
    },
    {
        "type": "ethernet-networkV4",
        "status": "OK",
        "state": "Active",
        "ethernetNetworkType": "Tagged",
        "name": "Eth-1003",
        "uri": "ETH:Eth-1003",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1003
    }
]

fc_networks = [
    {
        "type": "fc-networkV4",
        "name": "FC-CIS-A",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:VSAN1002"
    },
    {
        "type": "fc-networkV4",
        "name": "FC-CIS-B",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:VSAN1005"
    },
    {
        "type": "fc-networkV4",
        "name": "FC-B",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:Fabric-2"
    },
    {
        "type": "fc-networkV4",
        "name": "FC-A",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:Fabric-1"
    }
]
expected_fc_networks = [
    {
        "category": "fc-networks",
        "state": "Active",
        "description": None,
        "uri": "FC:FC-CIS-A",
        "status": "OK",
        "type": "fc-networkV4",
        "name": "FC-CIS-A",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:VSAN1002"
    },
    {
        "category": "fc-networks",
        "state": "Active",
        "description": None,
        "uri": "FC:FC-CIS-B",
        "status": "OK",
        "type": "fc-networkV4",
        "name": "FC-CIS-B",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:VSAN1005"
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
        "managedSanUri": "FCSan:Fabric-2"
    },
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
        "managedSanUri": "FCSan:Fabric-1"
    }
]

fcoe_networks = [
    {
        "name": "FCoE-3500",
        "type": "fcoe-networkV4",
        "vlanId": 3500,
        "managedSanUri": "FCSan:VSAN3500"
    },
    {
        "name": "FCoE-3400",
        "type": "fcoe-networkV4",
        "vlanId": 3400,
        "managedSanUri": "FCSan:VSAN3400"
    }
]
expected_fcoe_networks = [
    {
        "uri": "FCOE:FCoE-3500",
        "state": "Active",
        "status": "OK",
        "name": "FCoE-3500",
        "type": "fcoe-networkV4",
        "vlanId": 3500,
        "managedSanUri": "FCSan:VSAN3500"
    },
    {
        "uri": "FCOE:FCoE-3400",
        "state": "Active",
        "status": "OK",
        "name": "FCoE-3400",
        "type": "fcoe-networkV4",
        "vlanId": 3400,
        "managedSanUri": "FCSan:VSAN3400"
    }
]

networksets = [
    {
        "type": "network-setV4",
        "name": "Prod-set",
        "nativeNetworkUri": None,
        "networkUris": [
            "Eth-1005",
            "Eth-1003"
        ]
    },
    {
        "type": "network-setV4",
        "name": "prod-set1",
        "nativeNetworkUri": None,
        "networkUris": [
            "Eth-1005",
            "Eth-1004"
        ]
    }
]
expected_networksets = [
    {
        "category": "network-sets",
        "state": "Active",
        "description": None,
        "uri": "NS:Prod-set",
        "status": "OK",
        "type": "network-setV4",
        "name": "Prod-set",
        "nativeNetworkUri": None,
        "networkUris": [
            "ETH:Eth-1005",
            "ETH:Eth-1003"
        ]
    },
    {
        "category": "network-sets",
        "state": "Active",
        "description": None,
        "uri": "NS:prod-set1",
        "status": "OK",
        "type": "network-setV4",
        "name": "prod-set1",
        "nativeNetworkUri": None,
        "networkUris": [
            "ETH:Eth-1005",
            "ETH:Eth-1004"
        ]
    }
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
        }
    }
]
expected_storage_systems_with_pools = [
    {
        "uri": "SSYS:3PAR8200-CHO-10",
        "type": "StorageSystemV4",
        "state": "Managed",
        "category": "storage-systems",
        "status": "OK",
        "name": "3PAR8200-CHO-10",
        "family": "StoreServ",
        "hostname": "10.2.0.10",
        "deviceSpecificAttributes": {
            "managedDomain": "CST-AS",
            "serialNumber": "7CE611P3Y3"
        }
    }
]

storage_pools_toedit = [
    {
        "storageSystemUri": "3PAR8200-CHO-10",
        "name": "FC_r5",
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
            "name": "T05-Shared1",
            "provisioningType": "Thin",
            "size": 536870912000,
            "storagePool": "FC_r5"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "0F-bay6-vol",
            "provisioningType": "Thin",
            "size": 42949672960,
            "storagePool": "FC_r5"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "0F-bay10-vol",
            "provisioningType": "Thin",
            "size": 42949672960,
            "storagePool": "FC_r5"
        }
    }
]
expected_storage_volumes = [
    {
        "status": "OK",
        "uri": "SVOL:T05-Shared1",
        "isPermanent": True,
        "properties": {
            "description": "",
            "isShareable": True,
            "name": "T05-Shared1",
            "provisioningType": "Thin",
            "size": 536870912000,
            "storagePoolUri": "SPOOL:FC_r5"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:0F-bay6-vol",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "0F-bay6-vol",
            "provisioningType": "Thin",
            "size": 42949672960,
            "storagePoolUri": "SPOOL:FC_r5"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:0F-bay10-vol",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "0F-bay10-vol",
            "provisioningType": "Thin",
            "size": 42949672960,
            "storagePoolUri": "SPOOL:FC_r5"
        }
    }
]

sas_lig = [
]
expected_sas_lig = [
]

ligs = [
    {
        "name": "T05-Carbon",
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
                "bay": 5,
                "type": "Virtual Connect SE 16Gb FC Module for Synergy"
            },
            {
                "enclosureIndex": -1,
                "enclosure": -1,
                "bay": 2,
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
                    "bay": "5",
                    "port": "2",
                    "enclosure": "-1"
                },
                {
                    "speed": "Auto",
                    "bay": "5",
                    "port": "1",
                    "enclosure": "-1"
                }
            ],
            "mode": "Auto",
            "name": "FC-CIS-B",
            "nativeNetworkUri": None,
            "networkType": "FibreChannel",
            "networkUris": [
                "FC-CIS-B"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "NotApplicable",
            "lacpTimer": None,
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "bay": "2",
                    "port": "2",
                    "enclosure": "-1"
                },
                {
                    "speed": "Auto",
                    "bay": "2",
                    "port": "1",
                    "enclosure": "-1"
                }
            ],
            "mode": "Auto",
            "name": "FC-CIS-A",
            "nativeNetworkUri": None,
            "networkType": "FibreChannel",
            "networkUris": [
                "FC-CIS-A"
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
        "name": "T05-Potash1",
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
                "enclosureIndex": 1,
                "enclosure": 1,
                "bay": 1,
                "type": "Virtual Connect SE 40Gb F8 Module for Synergy"
            },
            {
                "enclosureIndex": 2,
                "bay": 1,
                "enclosure": 2,
                "type": "Synergy 20Gb Interconnect Link Module"
            },
            {
                "enclosureIndex": 1,
                "enclosure": 1,
                "bay": 4,
                "type": "Virtual Connect SE 40Gb F8 Module for Synergy"
            },
            {
                "enclosureIndex": 2,
                "enclosure": 2,
                "bay": 4,
                "type": "Synergy 20Gb Interconnect Link Module"
            },
            {
                "enclosureIndex": 3,
                "bay": 4,
                "enclosure": 3,
                "type": "Synergy 20Gb Interconnect Link Module"
            },
            {
                "enclosureIndex": 3,
                "bay": 1,
                "enclosure": 3,
                "type": "Synergy 20Gb Interconnect Link Module"
            }

        ],
        "interconnectBaySet": 1,
        "redundancyType": "Redundant",
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
                    "port": "Q2:1"
                },
                {
                    "speed": "Auto",
                    "bay": "1",
                    "enclosure": "1",
                    "port": "Q1.1"
                },
                {
                    "speed": "Auto",
                    "port": "Q2:1",
                    "enclosure": "1",
                    "bay": "1"
                },
                {
                    "speed": "Auto",
                    "bay": "4",
                    "enclosure": "1",
                    "port": "Q1.1"
                }
            ],
            "mode": "Auto",
            "name": "Eth",
            "nativeNetworkUri": None,
            "networkType": "Ethernet",
            "networkUris": [
                "Eth-1005",
                "Eth-1002",
                "Eth-1003",
                "Eth-1004",
                "Eth-1001"
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
        "name": "T05-Potash2",
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
                "enclosureIndex": 1,
                "enclosure": 1,
                "bay": 3,
                "type": "Virtual Connect SE 40Gb F8 Module for Synergy"
            },
            {
                "enclosureIndex": 2,
                "bay": 6,
                "enclosure": 2,
                "type": "Virtual Connect SE 40Gb F8 Module for Synergy"
            },
            {
                "enclosureIndex": 3,
                "bay": 3,
                "enclosure": 3,
                "type": "Synergy 10Gb Interconnect Link Module"
            },
            {
                "enclosureIndex": 3,
                "bay": 6,
                "enclosure": 3,
                "type": "Synergy 10Gb Interconnect Link Module"
            },
            {
                "enclosureIndex": 2,
                "bay": 3,
                "enclosure": 2,
                "type": "Synergy 10Gb Interconnect Link Module"
            },
            {
                "enclosureIndex": 1,
                "bay": 6,
                "enclosure": 1,
                "type": "Synergy 10Gb Interconnect Link Module"
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
                    "port": "67",
                    "enclosure": "2",
                    "bay": "6"
                },
                {
                    "speed": "Auto",
                    "port": "67",
                    "enclosure": "1",
                    "bay": "3"
                },
                {
                    "speed": "Auto",
                    "bay": "3",
                    "enclosure": "1",
                    "port": "62"
                },
                {
                    "speed": "Auto",
                    "enclosure": "2",
                    "port": "62",
                    "bay": "6"
                }
            ],
            "mode": "Auto",
            "name": "Eth",
            "nativeNetworkUri": None,
            "networkType": "Ethernet",
            "networkUris": [
                "Eth-1005",
                "Eth-1002",
                "Eth-1003",
                "Eth-1004",
                "Eth-1001"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "Tagged",
            "lacpTimer": "Short",
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "enclosure": "2",
                    "port": "71",
                    "bay": "6"
                }
            ],
            "mode": "Auto",
            "name": "FCoE-3500",
            "nativeNetworkUri": None,
            "networkType": "Ethernet",
            "networkUris": [
                "FCoE-3500"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "ImageStreamer",
            "lacpTimer": "Short",
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "enclosure": "2",
                    "port": "87",
                    "bay": "6"
                },
                {
                    "speed": "Auto",
                    "enclosure": "2",
                    "port": "88",
                    "bay": "6"
                },
                {
                    "speed": "Auto",
                    "bay": "3",
                    "port": "87",
                    "enclosure": "1"
                },
                {
                    "speed": "Auto",
                    "bay": "3",
                    "port": "88",
                    "enclosure": "1"
                }
            ],
            "mode": "Auto",
            "name": "i3s",
            "nativeNetworkUri": None,
            "networkType": "Ethernet",
            "networkUris": [
                "i3s-deploy"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "Tagged",
            "lacpTimer": "Short",
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "bay": "3",
                    "port": "71",
                    "enclosure": "1"
                }
            ],
            "mode": "Auto",
            "name": "FCoE-3400",
            "nativeNetworkUri": None,
            "networkType": "Ethernet",
            "networkUris": [
                "FCoE-3400"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "NotApplicable",
            "lacpTimer": None,
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "enclosure": "2",
                    "port": "82",
                    "bay": "6"
                }
            ],
            "mode": "Auto",
            "name": "FC-B",
            "nativeNetworkUri": None,
            "networkType": "FibreChannel",
            "networkUris": [
                "FC-B"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "NotApplicable",
            "lacpTimer": None,
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "port": "82",
                    "enclosure": "1",
                    "bay": "3"
                }
            ],
            "mode": "Auto",
            "name": "FC-A",
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
        "enclosureIndexes": [1, 2, 3]
    }
]
expected_lig = [
    {
        "uri": "LIG:T05-Carbon",
        "status": None,
        "stackingHealth": None,
        "category": "logical-interconnect-groups",
        "state": "Active",
        "internalNetworkUris": "[]",
        "stackingMode": None,
        "description": None,
        "name": "T05-Carbon",
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
        "uri": "LIG:T05-Potash1",
        "status": None,
        "stackingHealth": None,
        "category": "logical-interconnect-groups",
        "state": "Active",
        "internalNetworkUris": "[]",
        "stackingMode": None,
        "description": None,
        "name": "T05-Potash1",
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
        "uri": "LIG:T05-Potash2",
        "status": None,
        "stackingHealth": None,
        "category": "logical-interconnect-groups",
        "state": "Active",
        "internalNetworkUris": "[]",
        "stackingMode": None,
        "description": None,
        "name": "T05-Potash2",
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
        "enclosureIndexes": [1, 2, 3]
    }
]

encgroups_add = [
    {
        "name": "T05-EG",
        "interconnectBayMappings": [
            {
                "interconnectBay": 1,
                "logicalInterconnectGroupUri": "LIG:T05-Potash1",

            },
            {
                "interconnectBay": 2,
                "logicalInterconnectGroupUri": "LIG:T05-Carbon",
                "enclosureIndex": 1
            },
            {
                "interconnectBay": 3,
                "logicalInterconnectGroupUri": "LIG:T05-Potash2",

            },
            {
                "interconnectBay": 4,
                "logicalInterconnectGroupUri": "LIG:T05-Potash1",

            },
            {
                "interconnectBay": 5,
                "logicalInterconnectGroupUri": "LIG:T05-Carbon",
                "enclosureIndex": 1
            },
            {
                "interconnectBay": 6,
                "logicalInterconnectGroupUri": "LIG:T05-Potash2",

            }
        ],
        "ipAddressingMode": "DHCP",
        'osDeploymentSettings': {'manageOSDeployment': True,
                                 'deploymentModeSettings': {'deploymentMode': 'Internal',
                                                            'deploymentNetworkUri': None}},
        "enclosureCount": 3
    }
]
expected_encgroups_add = [
    {
        "uri": "EG:T05-EG",
        "description": None,
        "category": "enclosure-groups",
        "state": "Normal",
        "status": "OK",
        "powerMode": "RedundantPowerFeed",
        "portMappingCount": 8,
        "portMappings": [{u'midplanePort': 1, u'interconnectBay': 1}, {u'midplanePort': 2, u'interconnectBay': 2}, {u'midplanePort': 3, u'interconnectBay': 3}, {u'midplanePort': 4, u'interconnectBay': 4}, {u'midplanePort': 5, u'interconnectBay': 5}, {u'midplanePort': 6, u'interconnectBay': 6}, {u'midplanePort': 7, u'interconnectBay': 7}, {u'midplanePort': 8, u'interconnectBay': 8}],
        "ipRangeUris": [],
        "associatedLogicalInterconnectGroups": [u'LIG:T05-Carbon', u'LIG:T05-Potash1', u'LIG:T05-Potash2'],
        "name": "T05-EG",
        "type": "EnclosureGroupV7",
        "enclosureTypeUri": "/rest/enclosure-types/SY12000",
        "stackingMode": "Enclosure",
        "name": "T05-EG",
        "interconnectBayMappingCount": "6",
        "interconnectBayMappings": [
            {
                "interconnectBay": 1,
                "logicalInterconnectGroupUri": "LIG:T05-Potash1",

            },
            {
                "interconnectBay": 2,
                "logicalInterconnectGroupUri": "LIG:T05-Carbon",

            },
            {
                "interconnectBay": 3,
                "logicalInterconnectGroupUri": "LIG:T05-Potash2",

            },
            {
                "interconnectBay": 4,
                "logicalInterconnectGroupUri": "LIG:T05-Potash1",

            },
            {
                "interconnectBay": 5,
                "logicalInterconnectGroupUri": "LIG:T05-Carbon",

            },
            {
                "interconnectBay": 6,
                "logicalInterconnectGroupUri": "LIG:T05-Potash2",

            }
        ],
        "ipAddressingMode": "DHCP",
        "enclosureCount": 3
    }
]

logical_enclosure = [
    {
        "name": "T05-LE",
        "enclosureUris": [
            "ENC:MXQ74606ZM",
            "ENC:MXQ747038W",
            "ENC:SGH807TR0F"
        ],
        "enclosureGroupUri": "EG:T05-EG"
    }
]
expected_logical_enclosure = [
    {
        "type": "LogicalEnclosureV4",
        "uri": "T05-LE",
        "status": "OK",
        "name": "T05-LE",
        "enclosureUris": [
            "ENC:MXQ74606ZM",
            "ENC:MXQ747038W",
            "ENC:SGH807TR0F"
        ],
        "enclosureGroupUri": "EG:T05-EG"
    }
]

configured_enclosures = [
    {
        "name": "MXQ747038W",
        "state": "Configured",
        "serialNumber": "MXQ747038W",
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
                "devicePresence": "Absent"
            },
            {
                "bayNumber": 8,
                "devicePresence": "Absent"
            },
            {
                "bayNumber": 9,
                "devicePresence": "Present"
            },
            {
                "bayNumber": 10,
                "devicePresence": "Absent"
            },
            {
                "bayNumber": 11,
                "devicePresence": "Present"
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
        "name": "SGH807TR0F",
        "state": "Configured",
        "serialNumber": "SGH807TR0F",
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
                "devicePresence": "Present"
            },
            {
                "bayNumber": 7,
                "devicePresence": "Absent"
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
                "devicePresence": "Absent"
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
    },
    {
        "name": "MXQ74606ZM",
        "state": "Configured",
        "serialNumber": "MXQ74606ZM",
        "type": "EnclosureV7",
        "refreshState": "NotRefreshing",
        "deviceBays": [
            {
                "bayNumber": 1,
                "devicePresence": "Absent"
            },
            {
                "bayNumber": 2,
                "devicePresence": "Present"
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
                "devicePresence": "Present"
            },
            {
                "bayNumber": 6,
                "devicePresence": "Absent"
            },
            {
                "bayNumber": 7,
                "devicePresence": "Absent"
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
                "devicePresence": "Absent"
            },
            {
                "bayNumber": 11,
                "devicePresence": "Subsumed"
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

servers = [
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 65536,
        "model": "Synergy 480 Gen9",
        "mpFirmwareVersion": "2.60 May 23 2018",
        "mpModel": "iLO4",
        "name": "MXQ747038W, bay 9",
        "partNumber": "826952-B21",
        "position": 9,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 12,
        "processorCount": 1,
        "processorSpeedMhz": 2200,
        "processorType": "Intel(R) Xeon(R) CPU E5-2650 v4 @ 2.20GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v2.60 (05/21/2018)",
        "serialNumber": "MXQ74306SZ",
        "shortModel": "SY 480 Gen9",
        "state": "ProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-8"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 65536,
        "model": "Synergy 480 Gen9",
        "mpFirmwareVersion": "2.60 May 23 2018",
        "mpModel": "iLO4",
        "name": "MXQ747038W, bay 4",
        "partNumber": "826952-B21",
        "position": 4,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 12,
        "processorCount": 1,
        "processorSpeedMhz": 2200,
        "processorType": "Intel(R) Xeon(R) CPU E5-2650 v4 @ 2.20GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v2.60 (05/21/2018)",
        "serialNumber": "MXQ74306SY",
        "shortModel": "SY 480 Gen9",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-8"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 32768,
        "model": "Synergy 480 Gen9",
        "mpFirmwareVersion": "2.60 May 23 2018",
        "mpModel": "iLO4",
        "name": "MXQ747038W, bay 3",
        "partNumber": "826953-B21",
        "position": 3,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 10,
        "processorCount": 1,
        "processorSpeedMhz": 2200,
        "processorType": "Intel(R) Xeon(R) CPU E5-2630 v4 @ 2.20GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v2.60 (05/21/2018)",
        "serialNumber": "MXQ7440235",
        "shortModel": "SY 480 Gen9",
        "state": "ProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-8"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 32768,
        "model": "Synergy 480 Gen10",
        "mpFirmwareVersion": "1.30 May 31 2018",
        "mpModel": "iLO5",
        "name": "SGH807TR0F, bay 4",
        "partNumber": "871945-B21",
        "position": 4,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 12,
        "processorCount": 1,
        "processorSpeedMhz": 2300,
        "processorType": "Intel(R) Xeon(R) Gold 5118 CPU @ 2.30GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v1.42 (06/20/2018)",
        "serialNumber": "MXQ74307K6",
        "shortModel": "SY 480 Gen10",
        "state": "ProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-8"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 32768,
        "model": "Synergy 480 Gen10",
        "mpFirmwareVersion": "1.30 May 31 2018",
        "mpModel": "iLO5",
        "name": "SGH807TR0F, bay 8",
        "partNumber": "871945-B21",
        "position": 8,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 12,
        "processorCount": 1,
        "processorSpeedMhz": 2300,
        "processorType": "Intel(R) Xeon(R) Gold 5118 CPU @ 2.30GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v1.42 (06/20/2018)",
        "serialNumber": "MXQ74307K2",
        "shortModel": "SY 480 Gen10",
        "state": "ProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-8"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 16384,
        "model": "Synergy 480 Gen10",
        "mpFirmwareVersion": "1.30 May 31 2018",
        "mpModel": "iLO5",
        "name": "SGH807TR0F, bay 12",
        "partNumber": "871946-B21",
        "position": 12,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 6,
        "processorCount": 1,
        "processorSpeedMhz": 1700,
        "processorType": "Intel(R) Xeon(R) Bronze 3104 CPU @ 1.70GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v1.42 (06/20/2018)",
        "serialNumber": "MXQ74306BN",
        "shortModel": "SY 480 Gen10",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-8"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 16384,
        "model": "Synergy 480 Gen10",
        "mpFirmwareVersion": "1.30 May 31 2018",
        "mpModel": "iLO5",
        "name": "SGH807TR0F, bay 3",
        "partNumber": "871946-B21",
        "position": 3,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 6,
        "processorCount": 1,
        "processorSpeedMhz": 1700,
        "processorType": "Intel(R) Xeon(R) Bronze 3104 CPU @ 1.70GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v1.42 (06/20/2018)",
        "serialNumber": "MXQ74306BH",
        "shortModel": "SY 480 Gen10",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-8"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 32768,
        "model": "Synergy 480 Gen9",
        "mpFirmwareVersion": "2.60 May 23 2018",
        "mpModel": "iLO4",
        "name": "MXQ74606ZM, bay 2",
        "partNumber": "826953-B21",
        "position": 2,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 10,
        "processorCount": 1,
        "processorSpeedMhz": 2200,
        "processorType": "Intel(R) Xeon(R) CPU E5-2630 v4 @ 2.20GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v2.60 (05/21/2018)",
        "serialNumber": "MXQ7440236",
        "shortModel": "SY 480 Gen9",
        "state": "ProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-8"
    },
    {
        "formFactor": "FullHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 131072,
        "model": "Synergy 660 Gen10",
        "mpFirmwareVersion": "1.30 May 31 2018",
        "mpModel": "iLO5",
        "name": "MXQ74606ZM, bay 5",
        "partNumber": "871933-B21",
        "position": 5,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 18,
        "processorCount": 2,
        "processorSpeedMhz": 2300,
        "processorType": "Intel(R) Xeon(R) Gold 6140 CPU @ 2.30GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I43 v1.42 (06/20/2018)",
        "serialNumber": "CN780900VP",
        "shortModel": "SY 660 Gen10",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-8"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 65536,
        "model": "Synergy 480 Gen9",
        "mpFirmwareVersion": "2.60 May 23 2018",
        "mpModel": "iLO4",
        "name": "SGH807TR0F, bay 9",
        "partNumber": "826951-B21",
        "position": 9,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 14,
        "processorCount": 2,
        "processorSpeedMhz": 2000,
        "processorType": "Intel(R) Xeon(R) CPU E5-2660 v4 @ 2.00GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v2.60 (05/21/2018)",
        "serialNumber": "MXQ74306T8",
        "shortModel": "SY 480 Gen9",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-8"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 65536,
        "model": "Synergy 480 Gen10",
        "mpFirmwareVersion": "1.30 May 31 2018",
        "mpModel": "iLO5",
        "name": "MXQ74606ZM, bay 4",
        "partNumber": "871943-B21",
        "position": 4,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 16,
        "processorCount": 2,
        "processorSpeedMhz": 2100,
        "processorType": "Intel(R) Xeon(R) Gold 6130 CPU @ 2.10GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v1.42 (06/20/2018)",
        "serialNumber": "MXQ74401D3",
        "shortModel": "SY 480 Gen10",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-8"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 131072,
        "model": "Synergy 480 Gen9",
        "mpFirmwareVersion": "2.60 May 23 2018",
        "mpModel": "iLO4",
        "name": "MXQ747038W, bay 11",
        "partNumber": "826950-B21",
        "position": 11,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 14,
        "processorCount": 2,
        "processorSpeedMhz": 2400,
        "processorType": "Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v2.60 (05/21/2018)",
        "serialNumber": "CN78100F2P",
        "shortModel": "SY 480 Gen9",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-8"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 65536,
        "model": "Synergy 480 Gen10",
        "mpFirmwareVersion": "1.30 May 31 2018",
        "mpModel": "iLO5",
        "name": "MXQ74606ZM, bay 9",
        "partNumber": "871943-B21",
        "position": 9,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 16,
        "processorCount": 2,
        "processorSpeedMhz": 2100,
        "processorType": "Intel(R) Xeon(R) Gold 6130 CPU @ 2.10GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v1.42 (06/20/2018)",
        "serialNumber": "MXQ74307KC",
        "shortModel": "SY 480 Gen10",
        "state": "ProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-8"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 65536,
        "model": "Synergy 480 Gen9",
        "mpFirmwareVersion": "2.60 May 23 2018",
        "mpModel": "iLO4",
        "name": "MXQ74606ZM, bay 8",
        "partNumber": "826951-B21",
        "position": 8,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 14,
        "processorCount": 2,
        "processorSpeedMhz": 2000,
        "processorType": "Intel(R) Xeon(R) CPU E5-2660 v4 @ 2.00GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v2.60 (05/21/2018)",
        "serialNumber": "MXQ74306T2",
        "shortModel": "SY 480 Gen9",
        "state": "ProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-8"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 65536,
        "model": "Synergy 480 Gen9",
        "mpFirmwareVersion": "2.60 May 23 2018",
        "mpModel": "iLO4",
        "name": "SGH807TR0F, bay 6",
        "partNumber": "826951-B21",
        "position": 6,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 14,
        "processorCount": 2,
        "processorSpeedMhz": 2000,
        "processorType": "Intel(R) Xeon(R) CPU E5-2660 v4 @ 2.00GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v2.60 (05/21/2018)",
        "serialNumber": "MXQ74306T3",
        "shortModel": "SY 480 Gen9",
        "state": "ProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-8"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 65536,
        "model": "Synergy 480 Gen10",
        "mpFirmwareVersion": "1.30 May 31 2018",
        "mpModel": "iLO5",
        "name": "SGH807TR0F, bay 10",
        "partNumber": "871943-B21",
        "position": 10,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 16,
        "processorCount": 2,
        "processorSpeedMhz": 2100,
        "processorType": "Intel(R) Xeon(R) Gold 6130 CPU @ 2.10GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v1.42 (06/20/2018)",
        "serialNumber": "MXQ7430030",
        "shortModel": "SY 480 Gen10",
        "state": "ProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-8"
    }
]

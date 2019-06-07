#!/usr/bin/env python

admin_credentials = {'userName': 'Administrator', 'password': 'Cosmos123'}
timeandlocale = {'localeDisplayName': 'English (United States)', 'locale': 'en_US.UTF-8', 'dateTime': '2018-09-07T08:12:24.306Z', 'ntpServers': [u'10.3.0.11'], 'timezone': 'UTC', 'type': 'TimeAndLocale'}
licenses = [
    {
        'key': 'YBCG D9MA H9PA GHUY V2B4 HWWV Y9JL KMPL B89H MZVU GR4S JHWE JVSH XV5S CMRG HPMR UFVU A5K9 MWHC 9K4K HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'
    },
    {
        'key': '9B2G D9MA H9PA CHVZ V2B4 HWWV Y9JL KMPL B89H MZVU 6RMS 9HWE 92R6 3FZ3 CMRG HPMR MFVU A5K9 MHGK EKX9 HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'
    },
    {
        'key': 'QALA B9EA H9P9 KHWZ V2B4 HWWV Y9JL KMPL KFWC 4DBE GREQ JHWE 9LT6 XF6Z CMRG HPMR EEGW A5G9 EUX2 ESWK HKDU LWWP 3QL6 UPJE 6NAV U3ES R5KG MZYE N365 WAA5 D9ED 3RUX BJS6 WFHC 5KQS D2GM V88G BEYZ 5KG2 J6AD 4M5A 9G9B 7BRZ MJMM EVV5 J8JW 58JM ZCPX"Synergy 8Gb FC Upgrade License E-LTU"'
    },
    {
        'key': 'ABSE D9MA H9P9 CHUZ V2B4 HWWV Y9JL KMPL B89H MZVU GR4S JHWE 9FQP XN5W CMRG HPMR UFVU A5K9 MWHC 9K4K HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'
    },
    {
        'key': 'YBKA D9MA H9P9 8HX3 V2B4 HWWV Y9JL KMPL B89H MZVU GR4S JHWE J2SP XNZ8 CMRG HPMR UFVU A5K9 MWHC 9K4K HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'
    },
    {
        'key': 'YB2C D9MA H9PA 8HU3 V2B4 HWWV Y9JL KMPL B89H MZVU GR4S JHWE 9QSP XFR8 CMRG HPMR UFVU A5K9 MWHC 9K4K HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'
    }
]

appliance = {
    'type': "ApplianceNetworkConfigurationV2",
    'applianceNetworks':
    [{
        "device": "bond0",
        "macAddress": "14:02:ec:46:43:a0",
        "interfaceName": "Appliance",
        "activeNode": 1,
        "unconfigure": False,
        "ipv4Type": "STATIC",
        "ipv4Subnet": "255.255.255.0",
        "ipv4Gateway": "10.3.0.1",
        "ipv4NameServers": [u'10.3.0.11', u'10.4.0.11'],
        "app1Ipv4Addr": "10.3.0.16",
        "ipv6Type": "UNCONFIGURE",
        "hostname": "GS04.cosmosblrinfra.net",
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
        'dnsServers': [u'10.3.0.11']
    },
    {
        'type': "Subnet",
        'name': "10.5.0.0",
        'networkId': "10.5.0.0",
        'subnetmask': "255.255.255.0",
        'gateway': "10.5.0.1",
        'domain': "cosmosblrinfra.net",
        'dnsServers': [u'10.3.0.11', u'10.5.0.11']
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
        'name': "MGMT",
        'startAddress': "10.3.0.150",
        'endAddress': "10.3.0.250",
        "subnetUri": "10.3.0.0"
    },
    {
        'type': "Range",
        'name': "i3S-DEPLOY",
        'startAddress': "192.168.2.3",
        'endAddress': "192.168.2.254",
        "subnetUri": "192.168.0.0"
    },
    {
        'type': "Range",
        'name': "MGMT-CLRM",
        'startAddress': "10.5.0.150",
        'endAddress': "10.5.0.250",
        "subnetUri": "10.5.0.0"
    }
]

subnet_association = [{'network type': 'ethernet-networkV4', 'name': 'MGMT', 'subnetUri': '10.3.0.0'},
                      {'network type': 'ethernet-networkV4', 'name': 'i3S-DEPLOY', 'subnetUri': '192.168.0.0'},
                      {'network type': 'ethernet-networkV4', 'name': 'ETH-1005', 'subnetUri': '10.5.0.0'}
                      ]
ranges = [
    {
        'type': "Range",
        'name': "VMAC",
        'category': "id-range-VMAC",
        'rangeCategory': "Generated",
        'startAddress': "E6:D2:F3:20:00:00",
        'endAddress': "E6:D2:F3:2F:FF:FF",
        'enabled': True
    },
    {
        'type': "Range",
        'name': "VWWN",
        'category': "id-range-VWWN",
        'rangeCategory': "Generated",
        'startAddress': "10:00:7e:d3:8d:10:00:00",
        'endAddress': "10:00:7e:d3:8d:1f:ff:ff",
        'enabled': True
    },
    {
        'type': "Range",
        'name': "VSN",
        'category': "id-range-VSN",
        'rangeCategory': "Generated",
        'startAddress': "VCGYRH9000",
        'endAddress': "VCGYRH9ZZZ",
        'enabled': True
    }
]

deployment_server = [
    {
        'deplManagersType': "Image Streamer",
        'name': "i3S-OSDS",
        'description': "",
        'mgmtNetworkUri': [u'MGMT'],
        'applianceUri': 'MXQ746072X, appliance 1'
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
        "name": "ETH-1004",
        "privateNetwork": False,
        "purpose": "VMMigration",
        "smartLink": True,
        "vlanId": 1004
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "ETH-1002",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1002
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "ETH-1003",
        "privateNetwork": False,
        "purpose": "Management",
        "smartLink": True,
        "vlanId": 1003
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "ETH-1001",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1001
    }
]
expected_ethernet_networks = [
    {
        "uri": "ETH:ETH-1004",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "ETH-1004",
        "privateNetwork": False,
        "purpose": "VMMigration",
        "smartLink": True,
        "vlanId": 1004
    },
    {
        "uri": "ETH:ETH-1002",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "ETH-1002",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1002
    },
    {
        "uri": "ETH:ETH-1003",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "ETH-1003",
        "privateNetwork": False,
        "purpose": "Management",
        "smartLink": True,
        "vlanId": 1003
    },
    {
        "uri": "ETH:ETH-1001",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "ETH-1001",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1001
    }
]
i3s_networks = [
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "i3S-DEPLOY",
        "privateNetwork": False,
        "purpose": "ISCSI",
        "smartLink": True,
        "vlanId": 2450
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "MGMT",
        "privateNetwork": False,
        "purpose": "Management",
        "smartLink": True,
        "vlanId": 1003
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "ETH-1005",
        "privateNetwork": False,
        "purpose": "Management",
        "smartLink": True,
        "vlanId": 1005
    }]
expected_i3s_networks = [
    {
        "uri": "ETH:i3S-DEPLOY",
        "category": "ethernet-networks",
        "state": "Active",
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "i3S-DEPLOY",
        "privateNetwork": False,
        "purpose": "ISCSI",
        "smartLink": True,
        "vlanId": 2450
    },
    {
        "uri": "ETH:MGMT",
        "category": "ethernet-networks",
        "state": "Active",
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "MGMT",
        "privateNetwork": False,
        "purpose": "Management",
        "smartLink": True,
        "vlanId": 1003
    },
    {
        "uri": "ETH:ETH-1005",
        "category": "ethernet-networks",
        "state": "Active",
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "ETH-1005",
        "privateNetwork": False,
        "purpose": "Management",
        "smartLink": True,
        "vlanId": 1005
    }]

fc_networks = [
    {
        "type": "fc-networkV4",
        "name": "FC-DA2",
        "fabricType": "DirectAttach",
        "linkStabilityTime": 0,
        "autoLoginRedistribution": False,
        "managedSanUri": None
    },
    {
        "type": "fc-networkV4",
        "name": "FC-CIS-1002",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:VSAN1002"
    },
    {
        "type": "fc-networkV4",
        "name": "FC-DA1",
        "fabricType": "DirectAttach",
        "linkStabilityTime": 0,
        "autoLoginRedistribution": False,
        "managedSanUri": None
    },
    {
        "type": "fc-networkV4",
        "name": "FC-CIS-1005",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:VSAN1005"
    },
    {
        "type": "fc-networkV4",
        "name": "FC-A",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:Fabric-1"
    },
    {
        "type": "fc-networkV4",
        "name": "FC-B",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:Fabric-2"
    }
]
expected_fc_networks = [
    {
        "category": "fc-networks",
        "state": "Active",
        "description": None,
        "uri": "FC:FC-DA2",
        "status": "OK",
        "type": "fc-networkV4",
        "name": "FC-DA2",
        "fabricType": "DirectAttach",
        "linkStabilityTime": 0,
        "autoLoginRedistribution": False,
        "managedSanUri": None
    },
    {
        "category": "fc-networks",
        "state": "Active",
        "description": None,
        "uri": "FC:FC-CIS-1002",
        "status": "OK",
        "type": "fc-networkV4",
        "name": "FC-CIS-1002",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:VSAN1002"
    },
    {
        "category": "fc-networks",
        "state": "Active",
        "description": None,
        "uri": "FC:FC-DA1",
        "status": "OK",
        "type": "fc-networkV4",
        "name": "FC-DA1",
        "fabricType": "DirectAttach",
        "linkStabilityTime": 0,
        "autoLoginRedistribution": False,
        "managedSanUri": None
    },
    {
        "category": "fc-networks",
        "state": "Active",
        "description": None,
        "uri": "FC:FC-CIS-1005",
        "status": "OK",
        "type": "fc-networkV4",
        "name": "FC-CIS-1005",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:VSAN1005"
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
        "name": "FCoE-1900",
        "type": "fcoe-networkV4",
        "vlanId": 1900,
        "managedSanUri": "FCSan:VSAN1900"
    },
    {
        "name": "FCoE-3400",
        "type": "fcoe-networkV4",
        "vlanId": 3400,
        "managedSanUri": "FCSan:VSAN3400"
    },
    {
        "name": "FcoE-2000",
        "type": "fcoe-networkV4",
        "vlanId": 2000,
        "managedSanUri": "FCSan:VSAN2000"
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
        "uri": "FCOE:FCoE-1900",
        "state": "Active",
        "status": "OK",
        "name": "FCoE-1900",
        "type": "fcoe-networkV4",
        "vlanId": 1900,
        "managedSanUri": "FCSan:VSAN1900"
    },
    {
        "uri": "FCOE:FCoE-3400",
        "state": "Active",
        "status": "OK",
        "name": "FCoE-3400",
        "type": "fcoe-networkV4",
        "vlanId": 3400,
        "managedSanUri": "FCSan:VSAN3400"
    },
    {
        "uri": "FCOE:FcoE-2000",
        "state": "Active",
        "status": "OK",
        "name": "FcoE-2000",
        "type": "fcoe-networkV4",
        "vlanId": 2000,
        "managedSanUri": "FCSan:VSAN2000"
    }
]

networksets = [
    {
        "type": "network-setV4",
        "name": "NS-1",
        "nativeNetworkUri": None,
        "networkUris": [
            "ETH-1004",
            "ETH-1001",
            "ETH-1002"
        ]
    }
]
expected_networksets = [
    {
        "category": "network-sets",
        "state": "Active",
        "description": None,
        "uri": "NS:NS-1",
        "status": "OK",
        "type": "network-setV4",
        "name": "NS-1",
        "nativeNetworkUri": None,
        "networkUris": [
            "ETH:ETH-1004",
            "ETH:ETH-1001",
            "ETH:ETH-1002"
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
            "managedPools": [{'domain': 'NO DOMAIN', 'name': 'NL_r6', 'raidLevel': 'RAID6', 'state': 'Managed', 'deviceType': 'NL', 'freeCapacity': '41888816037888', 'totalCapacity': '41983305318400', 'uuid': 'b5f1f42d-cd2b-4d1d-9c29-a68d800515e7'}],
            "discoveredPools": [{'domain': 'NO DOMAIN', 'name': 'SSD_r1', 'raidLevel': 'RAID1', 'state': 'Discovered', 'deviceType': 'SSD', 'freeCapacity': '470298918912', 'totalCapacity': '470298918912', 'uuid': '5cfcb074-d008-447f-9ae6-a0b0d1a56af4'}, {'domain': 'NO DOMAIN', 'name': 'SSD_r5', 'raidLevel': 'RAID5', 'state': 'Discovered', 'deviceType': 'SSD', 'freeCapacity': '705448378368', 'totalCapacity': '774167855104', 'uuid': 'ad0cf501-5a8a-46a9-9781-923c1be32a1f'}],

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
    {
        "name": "GS04-FC-SHARED",
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
                "default": "FC_r5",
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
                "default": "FC_r5",
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
                "default": True,
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
        "name": "GS04-iSCSI-SHARED",
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
                "default": "Domain20",
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
                "default": "Domain20",
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
                "default": True,
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
        "name": "GS04-FCoE-SHARED",
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
                "default": "FC_r5",
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
                "default": "FC_r5",
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
                "default": True,
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
        "uri": "SVT:GS04-FC-SHARED",
        "status": "OK",
        "name": "GS04-FC-SHARED",
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
                "default": "SPOOL:FC_r5",
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
                "default": "SPOOL:FC_r5",
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
                "default": True,
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
        "uri": "SVT:GS04-iSCSI-SHARED",
        "status": "OK",
        "name": "GS04-iSCSI-SHARED",
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
                "default": "SPOOL:Domain20",
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
                "default": "SPOOL:Domain20",
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
                "default": True,
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
        "uri": "SVT:GS04-FCoE-SHARED",
        "status": "OK",
        "name": "GS04-FCoE-SHARED",
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
                "default": "SPOOL:FC_r5",
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
                "default": "SPOOL:FC_r5",
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
                "default": True,
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

add_existing_storage_volumes = [
]
expected_existing_storage_volumes = [
]

storage_volumes = [
    {
        "templateUri": "GS04-FC-SHARED",
        "isPermanent": True,
        "properties": {
            "description": "",
            "isShareable": True,
            "name": "GS04-FC-SHARED",
            "provisioningType": "Thin",
            "size": 1099511627776,
            "storagePool": "FC_r5"
        },
    },
    {
        "templateUri": "GS04-FCoE-SHARED",
        "isPermanent": True,
        "properties": {
            "description": "",
            "isShareable": True,
            "name": "GS04-FCoE-SHARED",
            "provisioningType": "Thin",
            "size": 805306368000,
            "storagePool": "FC_r5"
        },
    },
    {
        "templateUri": "GS04-iSCSI-SHARED",
        "isPermanent": True,
        "properties": {
            "description": "",
            "isShareable": True,
            "name": "GS04-iSCSI-SHARED",
            "provisioningType": "Thin",
            "size": 751619276800,
            "storagePool": "Domain20"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "TEST-WIN1",
            "provisioningType": "Thin",
            "size": 85899345920,
            "storagePool": "FC_r5"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "TEST-WIN2",
            "provisioningType": "Thin",
            "size": 85899345920,
            "storagePool": "FC_r5"
        }
    }
]
expected_storage_volumes = [
    {
        "status": "OK",
        "uri": "SVOL:GS04-FC-SHARED",
        "isPermanent": True,
        "properties": {
            "description": "",
            "isShareable": True,
            "name": "GS04-FC-SHARED",
            "provisioningType": "Thin",
            "size": 1099511627776,
            "storagePoolUri": "SPOOL:FC_r5"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:GS04-FCoE-SHARED",
        "isPermanent": True,
        "properties": {
            "description": "",
            "isShareable": True,
            "name": "GS04-FCoE-SHARED",
            "provisioningType": "Thin",
            "size": 805306368000,
            "storagePoolUri": "SPOOL:FC_r5"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:GS04-iSCSI-SHARED",
        "isPermanent": True,
        "properties": {
            "description": "",
            "isShareable": True,
            "name": "GS04-iSCSI-SHARED",
            "provisioningType": "Thin",
            "size": 751619276800,
            "storagePoolUri": "SPOOL:Domain20"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:TEST-WIN1",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "TEST-WIN1",
            "provisioningType": "Thin",
            "size": 85899345920,
            "storagePoolUri": "SPOOL:FC_r5"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:TEST-WIN2",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "TEST-WIN2",
            "provisioningType": "Thin",
            "size": 85899345920,
            "storagePoolUri": "SPOOL:FC_r5"
        }
    }
]

sas_lig = [
    {
        "name": "GS04-REMOTE1-NATASHA-LIG",
        "type": "sas-logical-interconnect-groupV2",
        "enclosureType": "SY12000",
        "interconnectMapTemplate": [
            {
                "enclosureIndex": 1,
                "enclosure": 1,
                "bay": 4,
                "type": "Synergy 12Gb SAS Connection Module"
            },
            {
                "enclosureIndex": 1,
                "enclosure": 1,
                "bay": 1,
                "type": "Synergy 12Gb SAS Connection Module"
            }

        ],
        "interconnectBaySet": 1,
        "enclosureIndexes": [1]
    }
]
expected_sas_lig = [
    {
        "uri": "SASLIG:GS04-REMOTE1-NATASHA-LIG",
        "state": "Active",
        "status": "OK",
        "description": None,
        "name": "GS04-REMOTE1-NATASHA-LIG",
        "type": "sas-logical-interconnect-groupV2",
        "enclosureType": "SY12000",
        "interconnectBaySet": 1,
        "enclosureIndexes": [1]
    }
]
grow_ligs = [
    {
        "name": "GS04-LOCAL-POTASH-GROW-LIG",
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
                "bay": 3,
                "enclosure": 1,
                "type": "Virtual Connect SE 40Gb F8 Module for Synergy"
            },
            {
                "enclosureIndex": 2,
                "bay": 3,
                "enclosure": 2,
                "type": "Synergy 10Gb Interconnect Link Module"
            },
            {
                "enclosureIndex": 1,
                "enclosure": 1,
                "bay": 6,
                "type": "Virtual Connect SE 40Gb F8 Module for Synergy"
            },
            {
                "enclosureIndex": 2,
                "enclosure": 2,
                "bay": 6,
                "type": "Synergy 10Gb Interconnect Link Module"
            }

        ],
        "interconnectBaySet": 3,
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
                    "port": "71",
                    "enclosure": "1",
                    "bay": "3"
                },
                {
                    "speed": "Auto",
                    "enclosure": "1",
                    "port": "66",
                    "bay": "3"
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
                    "enclosure": "1",
                    "port": "77",
                    "bay": "3"
                }
            ],
            "mode": "Auto",
            "name": "FC-DA1",
            "nativeNetworkUri": None,
            "networkType": "FibreChannel",
            "networkUris": [
                "FC-DA1"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "Tagged",
            "lacpTimer": "Short",
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "bay": "6",
                    "port": "66",
                    "enclosure": "1"
                },
                {
                    "speed": "Auto",
                    "bay": "6",
                    "enclosure": "1",
                    "port": "71"
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
            "ethernetNetworkType": "NotApplicable",
            "lacpTimer": None,
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "bay": "6",
                    "port": "77",
                    "enclosure": "1"
                }
            ],
            "mode": "Auto",
            "name": "FC-DA-2",
            "nativeNetworkUri": None,
            "networkType": "FibreChannel",
            "networkUris": [
                "FC-DA2"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "Tagged",
            "lacpTimer": "Short",
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "bay": "6",
                    "port": "61",
                    "enclosure": "1"
                },
                {
                    "speed": "Auto",
                    "enclosure": "1",
                    "port": "61",
                    "bay": "3"
                }
            ],
            "mode": "Auto",
            "name": "ETH-UL",
            "nativeNetworkUri": None,
            "networkType": "Ethernet",
            "networkUris": [
                "ETH-1004",
                "ETH-1005",
                "ETH-1003",
                "ETH-1001",
                "ETH-1002"
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
        "name": "GS04-REMOTE2-POTASH-LIG",
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
                "bay": 3,
                "enclosure": 1,
                "type": "Virtual Connect SE 40Gb F8 Module for Synergy"
            },
            {
                "enclosureIndex": 1,
                "enclosure": 1,
                "bay": 6,
                "type": "Synergy 10Gb Interconnect Link Module"
            },
            {
                "enclosureIndex": 2,
                "bay": 3,
                "enclosure": 2,
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
                    "enclosure": "1",
                    "port": "62",
                    "bay": "3"
                },
                {
                    "speed": "Auto",
                    "bay": "6",
                    "port": "67",
                    "enclosure": "2"
                },
                {
                    "speed": "Auto",
                    "bay": "6",
                    "port": "62",
                    "enclosure": "2"
                },
                {
                    "speed": "Auto",
                    "enclosure": "1",
                    "port": "67",
                    "bay": "3"
                }
            ],
            "mode": "Auto",
            "name": "ETH-UL",
            "nativeNetworkUri": None,
            "networkType": "Ethernet",
            "networkUris": [
                "ETH-1004",
                "ETH-1005",
                "ETH-1003",
                "ETH-1001",
                "ETH-1002"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "NotApplicable",
            "lacpTimer": None,
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "enclosure": "1",
                    "port": "77",
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
        }, {
            "ethernetNetworkType": "ImageStreamer",
            "lacpTimer": "Short",
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "port": "87",
                    "enclosure": "1",
                    "bay": "3"
                },
                {
                    "speed": "Auto",
                    "bay": "6",
                    "enclosure": "2",
                    "port": "88"
                },
                {
                    "speed": "Auto",
                    "port": "88",
                    "enclosure": "1",
                    "bay": "3"
                },
                {
                    "speed": "Auto",
                    "bay": "6",
                    "enclosure": "2",
                    "port": "87"
                }
            ],
            "mode": "Auto",
            "name": "i3S-UL",
            "nativeNetworkUri": None,
            "networkType": "Ethernet",
            "networkUris": [
                "i3S-DEPLOY"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "NotApplicable",
            "lacpTimer": None,
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "bay": "6",
                    "port": "77",
                    "enclosure": "2"
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

expected_grow_ligs = [
    {
        "uri": "LIG:GS04-LOCAL-POTASH-GROW-LIG",
        "status": None,
        "stackingHealth": None,
        "category": "logical-interconnect-groups",
        "state": "Active",
        "internalNetworkUris": "[]",
        "stackingMode": None,
        "description": None,
        "name": "GS04-LOCAL-POTASH-GROW-LIG",
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
        "uri": "LIG:GS04-REMOTE2-POTASH-LIG",
        "status": None,
        "stackingHealth": None,
        "category": "logical-interconnect-groups",
        "state": "Active",
        "internalNetworkUris": "[]",
        "stackingMode": None,
        "description": None,
        "name": "GS04-REMOTE2-POTASH-LIG",
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

ligs = [
    {
        "name": "GS04-REMOTE1-POTASH-LIG",
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
                "bay": 6,
                "type": "Synergy 20Gb Interconnect Link Module"
            },
            {
                "enclosureIndex": 3,
                "enclosure": 3,
                "bay": 6,
                "type": "Synergy 10Gb Interconnect Link Module"
            },
            {
                "enclosureIndex": 2,
                "bay": 3,
                "enclosure": 2,
                "type": "Synergy 20Gb Interconnect Link Module"
            },
            {
                "enclosureIndex": 2,
                "enclosure": 2,
                "bay": 6,
                "type": "Virtual Connect SE 40Gb F8 Module for Synergy"
            },
            {
                "enclosureIndex": 3,
                "bay": 3,
                "enclosure": 3,
                "type": "Synergy 10Gb Interconnect Link Module"
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
        "uplinkSets": [{
            "ethernetNetworkType": "NotApplicable",
            "lacpTimer": None,
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "enclosure": "1",
                    "port": "Q5:1",
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
        }, {
            "ethernetNetworkType": "Tagged",
            "lacpTimer": "Short",
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "bay": "6",
                    "port": "Q4",
                    "enclosure": "2"
                },
                {
                    "speed": "Auto",
                    "bay": "6",
                    "enclosure": "2",
                    "port": "Q3"
                }
            ],
            "mode": "Auto",
            "name": "FCoE-2000",
            "nativeNetworkUri": None,
            "networkType": "Ethernet",
            "networkUris": [
                "FcoE-2000"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "ImageStreamer",
            "lacpTimer": "Short",
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "port": "Q6:1",
                    "enclosure": "1",
                    "bay": "3"
                },
                {
                    "speed": "Auto",
                    "bay": "6",
                    "enclosure": "2",
                    "port": "Q6:2"
                },
                {
                    "speed": "Auto",
                    "port": "Q6:2",
                    "enclosure": "1",
                    "bay": "3"
                },
                {
                    "speed": "Auto",
                    "bay": "6",
                    "enclosure": "2",
                    "port": "Q6:1"
                }
            ],
            "mode": "Auto",
            "name": "i3S-UL",
            "nativeNetworkUri": None,
            "networkType": "Ethernet",
            "networkUris": [
                "i3S-DEPLOY"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "Tagged",
            "lacpTimer": "Short",
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "enclosure": "1",
                    "port": "Q4",
                    "bay": "3"
                },
                {
                    "speed": "Auto",
                    "port": "Q3",
                    "enclosure": "1",
                    "bay": "3"
                }
            ],
            "mode": "Auto",
            "name": "FCoE-1900",
            "nativeNetworkUri": None,
            "networkType": "Ethernet",
            "networkUris": [
                "FCoE-1900"
            ],
            "primaryPort": None
        }, {
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
                    "enclosure": "1",
                    "port": "Q1",
                    "bay": "3"
                }
            ],
            "mode": "Auto",
            "name": "ETH-UL",
            "nativeNetworkUri": None,
            "networkType": "Ethernet",
            "networkUris": [
                "ETH-1004",
                "ETH-1005",
                "ETH-1003",
                "ETH-1001",
                "ETH-1002"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "NotApplicable",
            "lacpTimer": None,
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "bay": "6",
                    "port": "Q5:1",
                    "enclosure": "2"
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
        "name": "GS04-REMOTE1-CARBON-LIG",
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
                "bay": 2,
                "enclosure": -1,
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
                    "port": "2",
                    "bay": "2"
                },
                {
                    "speed": "Auto",
                    "enclosure": "-1",
                    "port": "1",
                    "bay": "2"
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
        }, {
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
            "name": "FC-B",
            "nativeNetworkUri": None,
            "networkType": "FibreChannel",
            "networkUris": [
                "FC-B"
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
        "name": "GS04-LOCAL-POTASH-LIG",
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
                "bay": 6,
                "type": "Virtual Connect SE 40Gb F8 Module for Synergy"
            },
            {
                "enclosureIndex": 1,
                "bay": 3,
                "enclosure": 1,
                "type": "Virtual Connect SE 40Gb F8 Module for Synergy"
            }

        ],
        "interconnectBaySet": 3,
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
                    "port": "Q3",
                    "enclosure": "1",
                    "bay": "3"
                },
                {
                    "speed": "Auto",
                    "enclosure": "1",
                    "port": "Q2",
                    "bay": "3"
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
                    "enclosure": "1",
                    "port": "Q4.1",
                    "bay": "3"
                }
            ],
            "mode": "Auto",
            "name": "FC-DA1",
            "nativeNetworkUri": None,
            "networkType": "FibreChannel",
            "networkUris": [
                "FC-DA1"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "Tagged",
            "lacpTimer": "Short",
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "bay": "6",
                    "port": "Q2",
                    "enclosure": "1"
                },
                {
                    "speed": "Auto",
                    "bay": "6",
                    "enclosure": "1",
                    "port": "Q3"
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
            "ethernetNetworkType": "NotApplicable",
            "lacpTimer": None,
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "bay": "6",
                    "port": "Q4.1",
                    "enclosure": "1"
                }
            ],
            "mode": "Auto",
            "name": "FC-DA-2",
            "nativeNetworkUri": None,
            "networkType": "FibreChannel",
            "networkUris": [
                "FC-DA2"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "Tagged",
            "lacpTimer": "Short",
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "bay": "6",
                    "port": "Q1",
                    "enclosure": "1"
                },
                {
                    "speed": "Auto",
                    "enclosure": "1",
                    "port": "Q1",
                    "bay": "3"
                }
            ],
            "mode": "Auto",
            "name": "ETH-UL",
            "nativeNetworkUri": None,
            "networkType": "Ethernet",
            "networkUris": [
                "ETH-1004",
                "ETH-1005",
                "ETH-1003",
                "ETH-1001",
                "ETH-1002"
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
        "uri": "LIG:GS04-REMOTE1-POTASH-LIG",
        "status": None,
        "stackingHealth": None,
        "category": "logical-interconnect-groups",
        "state": "Active",
        "internalNetworkUris": "[]",
        "stackingMode": None,
        "description": None,
        "name": "GS04-REMOTE1-POTASH-LIG",
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
    },
    {
        "uri": "LIG:GS04-REMOTE1-CARBON-LIG",
        "status": None,
        "stackingHealth": None,
        "category": "logical-interconnect-groups",
        "state": "Active",
        "internalNetworkUris": "[]",
        "stackingMode": None,
        "description": None,
        "name": "GS04-REMOTE1-CARBON-LIG",
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
        "uri": "LIG:GS04-LOCAL-POTASH-LIG",
        "status": None,
        "stackingHealth": None,
        "category": "logical-interconnect-groups",
        "state": "Active",
        "internalNetworkUris": "[]",
        "stackingMode": None,
        "description": None,
        "name": "GS04-LOCAL-POTASH-LIG",
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
        "enclosureIndexes": [1]
    }
]
grow_encgroups_add = [
    {
        "name": "GS04-REMOTE2-EG",
        "interconnectBayMappings": [
            {
                "interconnectBay": 3,
                "logicalInterconnectGroupUri": "LIG:GS04-REMOTE2-POTASH-LIG",

            },
            {
                "interconnectBay": 6,
                "logicalInterconnectGroupUri": "LIG:GS04-REMOTE2-POTASH-LIG",

            }
        ],
        "ipAddressingMode": "DHCP",
        "enclosureCount": 2
    },
    {
        "name": "GS04-LOCAL-GROW-EG",
        "interconnectBayMappings": [
            {
                "interconnectBay": 3,
                "logicalInterconnectGroupUri": "LIG:GS04-LOCAL-POTASH-GROW-LIG",

            },
            {
                "interconnectBay": 6,
                "logicalInterconnectGroupUri": "LIG:GS04-LOCAL-POTASH-GROW-LIG",

            }
        ],
        "ipAddressingMode": "DHCP",
        "enclosureCount": 2
    },
]

expected_grow_encgroups_add = [
    {
        "uri": "EG:GS04-REMOTE2-EG",
        "description": None,
        "category": "enclosure-groups",
        "state": "Normal",
        "status": "OK",
        "powerMode": "RedundantPowerFeed",
        "portMappingCount": 8,
        "portMappings": [{u'midplanePort': 1, u'interconnectBay': 1}, {u'midplanePort': 2, u'interconnectBay': 2}, {u'midplanePort': 3, u'interconnectBay': 3}, {u'midplanePort': 4, u'interconnectBay': 4}, {u'midplanePort': 5, u'interconnectBay': 5}, {u'midplanePort': 6, u'interconnectBay': 6}, {u'midplanePort': 7, u'interconnectBay': 7}, {u'midplanePort': 8, u'interconnectBay': 8}],
        "ipRangeUris": [],
        "associatedLogicalInterconnectGroups": [u'LIG:GS04-REMOTE2-POTASH-LIG'],
        "name": "GS04-REMOTE2-EG",
        "type": "EnclosureGroupV7",
        "enclosureTypeUri": "/rest/enclosure-types/SY12000",
        "stackingMode": "Enclosure",
        "name": "GS04-REMOTE2-EG",
        "interconnectBayMappingCount": "2",
        "interconnectBayMappings": [
            {
                "interconnectBay": 3,
                "logicalInterconnectGroupUri": "LIG:GS04-REMOTE2-POTASH-LIG",

            },
            {
                "interconnectBay": 6,
                "logicalInterconnectGroupUri": "LIG:GS04-REMOTE2-POTASH-LIG",

            }
        ],
        "ipAddressingMode": "DHCP",
        "enclosureCount": 2
    },
    {
        "uri": "EG:GS04-LOCAL-GROW-EG",
        "description": None,
        "category": "enclosure-groups",
        "state": "Normal",
        "status": "OK",
        "powerMode": "RedundantPowerFeed",
        "portMappingCount": 8,
        "portMappings": [{u'midplanePort': 1, u'interconnectBay': 1}, {u'midplanePort': 2, u'interconnectBay': 2}, {u'midplanePort': 3, u'interconnectBay': 3}, {u'midplanePort': 4, u'interconnectBay': 4}, {u'midplanePort': 5, u'interconnectBay': 5}, {u'midplanePort': 6, u'interconnectBay': 6}, {u'midplanePort': 7, u'interconnectBay': 7}, {u'midplanePort': 8, u'interconnectBay': 8}],
        "ipRangeUris": [],
        "associatedLogicalInterconnectGroups": [u'LIG:GS04-LOCAL-POTASH-GROW-LIG'],
        "name": "GS04-LOCAL-GROW-EG",
        "type": "EnclosureGroupV7",
        "enclosureTypeUri": "/rest/enclosure-types/SY12000",
        "stackingMode": "Enclosure",
        "name": "GS04-LOCAL-GROW-EG",
        "interconnectBayMappingCount": "2",
        "interconnectBayMappings": [
            {
                "interconnectBay": 3,
                "logicalInterconnectGroupUri": "LIG:GS04-LOCAL-POTASH-GROW-LIG",

            },
            {
                "interconnectBay": 6,
                "logicalInterconnectGroupUri": "LIG:GS04-LOCAL-POTASH-GROW-LIG",

            }
        ],
        "ipAddressingMode": "DHCP",
        "enclosureCount": 2
    },
]

encgroups_add = [
    {
        "name": "GS04-REMOTE1-EG",
        "interconnectBayMappings": [
            {
                "interconnectBay": 1,
                "logicalInterconnectGroupUri": "SASLIG:GS04-REMOTE1-NATASHA-LIG",
                "enclosureIndex": 1
            },
            {
                "interconnectBay": 2,
                "logicalInterconnectGroupUri": "LIG:GS04-REMOTE1-CARBON-LIG",
                "enclosureIndex": 1
            },
            {
                "interconnectBay": 3,
                "logicalInterconnectGroupUri": "LIG:GS04-REMOTE1-POTASH-LIG",

            },
            {
                "interconnectBay": 4,
                "logicalInterconnectGroupUri": "SASLIG:GS04-REMOTE1-NATASHA-LIG",
                "enclosureIndex": 1
            },
            {
                "interconnectBay": 5,
                "logicalInterconnectGroupUri": "LIG:GS04-REMOTE1-CARBON-LIG",
                "enclosureIndex": 1
            },
            {
                "interconnectBay": 6,
                "logicalInterconnectGroupUri": "LIG:GS04-REMOTE1-POTASH-LIG",
            }
        ],
        "ipAddressingMode": "DHCP",
        'osDeploymentSettings': {'manageOSDeployment': True,
                                 'deploymentModeSettings': {'deploymentMode': 'Internal',
                                                            'deploymentNetworkUri': None}},
        "enclosureCount": 3
    },
    {
        "name": "GS04-LOCAL-EG",
        "interconnectBayMappings": [
            {
                "interconnectBay": 3,
                "logicalInterconnectGroupUri": "LIG:GS04-LOCAL-POTASH-LIG",

            },
            {
                "interconnectBay": 6,
                "logicalInterconnectGroupUri": "LIG:GS04-LOCAL-POTASH-LIG",

            }
        ],
        "ipAddressingMode": "DHCP",
        "enclosureCount": 1
    }
]
expected_encgroups_add = [
    {
        "uri": "EG:GS04-REMOTE1-EG",
        "description": None,
        "category": "enclosure-groups",
        "state": "Normal",
        "status": "OK",
        "powerMode": "RedundantPowerFeed",
        "portMappingCount": 8,
        "portMappings": [{u'midplanePort': 1, u'interconnectBay': 1}, {u'midplanePort': 2, u'interconnectBay': 2}, {u'midplanePort': 3, u'interconnectBay': 3}, {u'midplanePort': 4, u'interconnectBay': 4}, {u'midplanePort': 5, u'interconnectBay': 5}, {u'midplanePort': 6, u'interconnectBay': 6}, {u'midplanePort': 7, u'interconnectBay': 7}, {u'midplanePort': 8, u'interconnectBay': 8}],
        "ipRangeUris": [],
        "associatedLogicalInterconnectGroups": [u'LIG:GS04-REMOTE1-POTASH-LIG', u'LIG:GS04-REMOTE1-CARBON-LIG', u'SASLIG:GS04-REMOTE1-NATASHA-LIG'],
        "name": "GS04-REMOTE1-EG",
        "type": "EnclosureGroupV7",
        "enclosureTypeUri": "/rest/enclosure-types/SY12000",
        "stackingMode": "Enclosure",
        "name": "GS04-REMOTE1-EG",
        "interconnectBayMappingCount": "6",
        "interconnectBayMappings": [
            {
                "interconnectBay": 1,
                "logicalInterconnectGroupUri": "SASLIG:GS04-REMOTE1-NATASHA-LIG",

            },
            {
                "interconnectBay": 2,
                "logicalInterconnectGroupUri": "LIG:GS04-REMOTE1-CARBON-LIG",

            },
            {
                "interconnectBay": 3,
                "logicalInterconnectGroupUri": "LIG:GS04-REMOTE1-POTASH-LIG",

            },
            {
                "interconnectBay": 4,
                "logicalInterconnectGroupUri": "SASLIG:GS04-REMOTE1-NATASHA-LIG",

            },
            {
                "interconnectBay": 5,
                "logicalInterconnectGroupUri": "LIG:GS04-REMOTE1-CARBON-LIG",

            },
            {
                "interconnectBay": 6,
                "logicalInterconnectGroupUri": "LIG:GS04-REMOTE1-POTASH-LIG",

            }
        ],
        "ipAddressingMode": "DHCP",
        "enclosureCount": 3
    },
    {
        "uri": "EG:GS04-LOCAL-EG",
        "description": None,
        "category": "enclosure-groups",
        "state": "Normal",
        "status": "OK",
        "powerMode": "RedundantPowerFeed",
        "portMappingCount": 8,
        "portMappings": [{u'midplanePort': 1, u'interconnectBay': 1}, {u'midplanePort': 2, u'interconnectBay': 2}, {u'midplanePort': 3, u'interconnectBay': 3}, {u'midplanePort': 4, u'interconnectBay': 4}, {u'midplanePort': 5, u'interconnectBay': 5}, {u'midplanePort': 6, u'interconnectBay': 6}, {u'midplanePort': 7, u'interconnectBay': 7}, {u'midplanePort': 8, u'interconnectBay': 8}],
        "ipRangeUris": [],
        "associatedLogicalInterconnectGroups": [u'LIG:GS04-LOCAL-POTASH-LIG'],
        "name": "GS04-LOCAL-EG",
        "type": "EnclosureGroupV7",
        "enclosureTypeUri": "/rest/enclosure-types/SY12000",
        "stackingMode": "Enclosure",
        "name": "GS04-LOCAL-EG",
        "interconnectBayMappingCount": "2",
        "interconnectBayMappings": [
            {
                "interconnectBay": 3,
                "logicalInterconnectGroupUri": "LIG:GS04-LOCAL-POTASH-LIG",

            },
            {
                "interconnectBay": 6,
                "logicalInterconnectGroupUri": "LIG:GS04-LOCAL-POTASH-LIG",

            }
        ],
        "ipAddressingMode": "DHCP",
        "enclosureCount": 1
    }
]

logical_enclosure = [
    {
        "name": "GS04-REMOTE-LE",
        "enclosureUris": [
            "ENC:SGH807TR0K",
            "ENC:MXQ74606ZP",
            "ENC:MXQ746072X"
        ],
        "enclosureGroupUri": "EG:GS04-REMOTE1-EG"
    }
]
expected_logical_enclosure = [
    {
        "type": "LogicalEnclosureV4",
        "uri": "GS04-REMOTE-LE",
        "status": "OK",
        "name": "GS04-REMOTE-LE",
        "enclosureUris": [
            "ENC:SGH807TR0K",
            "ENC:MXQ74606ZP",
            "ENC:MXQ746072X"
        ],
        "enclosureGroupUri": "EG:GS04-REMOTE1-EG"
    }
]

configured_enclosures = [
    {
        "name": "SGH807TR0K",
        "state": "Configured",
        "serialNumber": "SGH807TR0K",
        "type": "EnclosureV7",
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
                "devicePresence": "Subsumed"
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
        "name": "MXQ74606ZP",
        "state": "Configured",
        "serialNumber": "MXQ74606ZP",
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
                "devicePresence": "Subsumed"
            },
            {
                "bayNumber": 9,
                "devicePresence": "Subsumed"
            },
            {
                "bayNumber": 10,
                "devicePresence": "Subsumed"
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
                "status": "Unknown"
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
        "name": "SGH720W0TB",
        "state": "Configured",
        "serialNumber": "SGH720W0TB",
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
                "devicePresence": "Absent"
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
        "name": "SGH720W0T8",
        "state": "Configured",
        "serialNumber": "SGH720W0T8",
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
                "devicePresence": "Subsumed"
            },
            {
                "bayNumber": 10,
                "devicePresence": "Subsumed"
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
        "name": "SGH807TR0J",
        "state": "Configured",
        "serialNumber": "SGH807TR0J",
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
                "devicePresence": "Present"
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
                "devicePresence": "Absent"
            },
            {
                "bayNumber": 10,
                "devicePresence": "Subsumed"
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
                "status": "Unknown"
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
        "name": "MXQ746072X",
        "state": "Configured",
        "serialNumber": "MXQ746072X",
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
                "status": "Unknown"
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
        "mpFirmwareVersion": "2.55 Aug 16 2017",
        "mpModel": "iLO4",
        "name": "SGH807TR0K, bay 9",
        "partNumber": "826953-B21",
        "position": 9,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 10,
        "processorCount": 1,
        "processorSpeedMhz": 2200,
        "processorType": "Intel(R) Xeon(R) CPU E5-2630 v4 @ 2.20GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v2.60 (05/21/2018)",
        "serialNumber": "MXQ7440238",
        "shortModel": "SY 480 Gen9",
        "state": "ProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 32768,
        "model": "Synergy 480 Gen9",
        "mpFirmwareVersion": "2.55 Aug 16 2017",
        "mpModel": "iLO4",
        "name": "MXQ746072X, bay 1",
        "partNumber": "826953-B21",
        "position": 1,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 10,
        "processorCount": 1,
        "processorSpeedMhz": 2200,
        "processorType": "Intel(R) Xeon(R) CPU E5-2630 v4 @ 2.20GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v2.60 (05/21/2018)",
        "serialNumber": "MXQ7440232",
        "shortModel": "SY 480 Gen9",
        "state": "ProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 32768,
        "model": "Synergy 480 Gen10",
        "mpFirmwareVersion": "1.22 Mar 06 2018",
        "mpModel": "iLO5",
        "name": "MXQ746072X, bay 11",
        "partNumber": "871945-B21",
        "position": 11,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 12,
        "processorCount": 1,
        "processorSpeedMhz": 2300,
        "processorType": "Intel(R) Xeon(R) Gold 5118 CPU @ 2.30GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v1.36 (02/14/2018)",
        "serialNumber": "CN7809003T",
        "shortModel": "SY 480 Gen10",
        "state": "ProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 16384,
        "model": "Synergy 480 Gen10",
        "mpFirmwareVersion": "1.22 Mar 06 2018",
        "mpModel": "iLO5",
        "name": "MXQ746072X, bay 4",
        "partNumber": "871946-B21",
        "position": 4,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 6,
        "processorCount": 1,
        "processorSpeedMhz": 1700,
        "processorType": "Intel(R) Xeon(R) Bronze 3104 CPU @ 1.70GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v1.36 (02/14/2018)",
        "serialNumber": "MXQ74306BQ",
        "shortModel": "SY 480 Gen10",
        "state": "ProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 32768,
        "model": "Synergy 480 Gen10",
        "mpFirmwareVersion": "1.22 Mar 06 2018",
        "mpModel": "iLO5",
        "name": "MXQ746072X, bay 10",
        "partNumber": "871945-B21",
        "position": 10,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 12,
        "processorCount": 1,
        "processorSpeedMhz": 2300,
        "processorType": "Intel(R) Xeon(R) Gold 5118 CPU @ 2.30GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v1.36 (02/14/2018)",
        "serialNumber": "CN7809003N",
        "shortModel": "SY 480 Gen10",
        "state": "ProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 65536,
        "model": "Synergy 480 Gen10",
        "mpFirmwareVersion": "1.22 Mar 06 2018",
        "mpModel": "iLO5",
        "name": "MXQ746072X, bay 12",
        "partNumber": "871943-B21",
        "position": 12,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 16,
        "processorCount": 2,
        "processorSpeedMhz": 2100,
        "processorType": "Intel(R) Xeon(R) Gold 6130 CPU @ 2.10GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v1.36 (02/14/2018)",
        "serialNumber": "MXQ74401CZ",
        "shortModel": "SY 480 Gen10",
        "state": "ProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 32768,
        "model": "Synergy 480 Gen10",
        "mpFirmwareVersion": "1.22 Mar 06 2018",
        "mpModel": "iLO5",
        "name": "MXQ746072X, bay 7",
        "partNumber": "871943-B21",
        "position": 7,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 12,
        "processorCount": 1,
        "processorSpeedMhz": 2300,
        "processorType": "Intel(R) Xeon(R) Gold 5118 CPU @ 2.30GHz",
        "refreshState": "RefreshFailed",
        "romVersion": "I42 v1.36 (02/14/2018)",
        "serialNumber": "MXQ74307KD",
        "shortModel": "SY 480 Gen10",
        "state": "Unmanaged",
        "stateReason": "Unconfigured",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 65536,
        "model": "Synergy 480 Gen10",
        "mpFirmwareVersion": "1.22 Mar 06 2018",
        "mpModel": "iLO5",
        "name": "MXQ746072X, bay 8",
        "partNumber": "871943-B21",
        "position": 8,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 16,
        "processorCount": 2,
        "processorSpeedMhz": 2100,
        "processorType": "Intel(R) Xeon(R) Gold 6130 CPU @ 2.10GHz",
        "refreshState": "RefreshFailed",
        "romVersion": "I42 v1.36 (02/14/2018)",
        "serialNumber": "MXQ74401D0",
        "shortModel": "SY 480 Gen10",
        "state": "Unmanaged",
        "stateReason": "Unconfigured",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "FullHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 65536,
        "model": "Synergy 660 Gen9",
        "mpFirmwareVersion": "2.55 Aug 16 2017",
        "mpModel": "iLO4",
        "name": "MXQ74606ZP, bay 2",
        "partNumber": "826958-B21",
        "position": 2,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 10,
        "processorCount": 2,
        "processorSpeedMhz": 1800,
        "processorType": "Intel(R) Xeon(R) CPU E5-4610 v4 @ 1.80GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I39 v2.60 (05/21/2018)",
        "serialNumber": "MXQ74308KX",
        "shortModel": "SY 660 Gen9",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "FullHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 65536,
        "model": "Synergy 660 Gen9",
        "mpFirmwareVersion": "2.55 Aug 16 2017",
        "mpModel": "iLO4",
        "name": "MXQ74606ZP, bay 1",
        "partNumber": "826958-B21",
        "position": 1,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 10,
        "processorCount": 2,
        "processorSpeedMhz": 1800,
        "processorType": "Intel(R) Xeon(R) CPU E5-4610 v4 @ 1.80GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I39 v2.60 (05/21/2018)",
        "serialNumber": "MXQ74308KT",
        "shortModel": "SY 660 Gen9",
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
        "mpFirmwareVersion": "1.22 Mar 06 2018",
        "mpModel": "iLO5",
        "name": "MXQ74606ZP, bay 12",
        "partNumber": "871945-B21",
        "position": 12,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 12,
        "processorCount": 1,
        "processorSpeedMhz": 2300,
        "processorType": "Intel(R) Xeon(R) Gold 5118 CPU @ 2.30GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v1.36 (02/14/2018)",
        "serialNumber": "CN78090042",
        "shortModel": "SY 480 Gen10",
        "state": "ProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 32768,
        "model": "Synergy 480 Gen10",
        "mpFirmwareVersion": "1.22 Mar 06 2018",
        "mpModel": "iLO5",
        "name": "SGH720W0TB, bay 3",
        "partNumber": "871945-B21",
        "position": 3,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 12,
        "processorCount": 1,
        "processorSpeedMhz": 2300,
        "processorType": "Intel(R) Xeon(R) Gold 5118 CPU @ 2.30GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v1.36 (02/14/2018)",
        "serialNumber": "CN78090044",
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
        "mpFirmwareVersion": "1.22 Mar 06 2018",
        "mpModel": "iLO5",
        "name": "SGH720W0TB, bay 8",
        "partNumber": "871945-B21",
        "position": 8,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 12,
        "processorCount": 1,
        "processorSpeedMhz": 2300,
        "processorType": "Intel(R) Xeon(R) Gold 5118 CPU @ 2.30GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v1.36 (02/14/2018)",
        "serialNumber": "CN7809003Z",
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
        "mpFirmwareVersion": "1.22 Mar 06 2018",
        "mpModel": "iLO5",
        "name": "SGH720W0TB, bay 7",
        "partNumber": "871940-B21",
        "position": 7,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 4,
        "processorCount": 2,
        "processorSpeedMhz": 2600,
        "processorType": "Intel(R) Xeon(R) Silver 4112 CPU @ 2.60GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v1.36 (02/14/2018)",
        "serialNumber": "SGH825SKJK",
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
        "mpFirmwareVersion": "1.22 Mar 06 2018",
        "mpModel": "iLO5",
        "name": "SGH720W0TB, bay 6",
        "partNumber": "871943-B21",
        "position": 6,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 16,
        "processorCount": 2,
        "processorSpeedMhz": 2100,
        "processorType": "Intel(R) Xeon(R) Gold 6130 CPU @ 2.10GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v1.36 (02/14/2018)",
        "serialNumber": "MXQ74307K9",
        "shortModel": "SY 480 Gen10",
        "state": "ProfileError",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 32768,
        "model": "Synergy 480 Gen10",
        "mpFirmwareVersion": "1.22 Mar 06 2018",
        "mpModel": "iLO5",
        "name": "SGH807TR0K, bay 10",
        "partNumber": "871945-B21",
        "position": 10,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 16,
        "processorCount": 1,
        "processorSpeedMhz": 2100,
        "processorType": "Intel(R) Xeon(R) Gold 6130 CPU @ 2.10GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v1.36 (02/14/2018)",
        "serialNumber": "CN7809003Q",
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
        "mpFirmwareVersion": "2.55 Aug 16 2017",
        "mpModel": "iLO4",
        "name": "SGH807TR0K, bay 11",
        "partNumber": "826951-B21",
        "position": 11,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 14,
        "processorCount": 2,
        "processorSpeedMhz": 2000,
        "processorType": "Intel(R) Xeon(R) CPU E5-2660 v4 @ 2.00GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v2.60 (05/21/2018)",
        "serialNumber": "MXQ74306T6",
        "shortModel": "SY 480 Gen9",
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
        "mpFirmwareVersion": "1.22 Mar 06 2018",
        "mpModel": "iLO5",
        "name": "SGH807TR0K, bay 6",
        "partNumber": "871943-B21",
        "position": 6,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 16,
        "processorCount": 2,
        "processorSpeedMhz": 2100,
        "processorType": "Intel(R) Xeon(R) Gold 6130 CPU @ 2.10GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v1.36 (02/14/2018)",
        "serialNumber": "MXQ7430031",
        "shortModel": "SY 480 Gen10",
        "state": "Unmanaged",
        "stateReason": "Unconfigured",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 65536,
        "model": "Synergy 480 Gen10",
        "mpFirmwareVersion": "1.22 Mar 06 2018",
        "mpModel": "iLO5",
        "name": "SGH807TR0K, bay 5",
        "partNumber": "871943-B21",
        "position": 5,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 16,
        "processorCount": 2,
        "processorSpeedMhz": 2100,
        "processorType": "Intel(R) Xeon(R) Gold 6130 CPU @ 2.10GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v1.36 (02/14/2018)",
        "serialNumber": "CN78090046",
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
        "mpFirmwareVersion": "2.55 Aug 16 2017",
        "mpModel": "iLO4",
        "name": "SGH807TR0K, bay 12",
        "partNumber": "826951-B21",
        "position": 12,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 14,
        "processorCount": 2,
        "processorSpeedMhz": 2000,
        "processorType": "Intel(R) Xeon(R) CPU E5-2660 v4 @ 2.00GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v2.60 (05/21/2018)",
        "serialNumber": "MXQ74306TG",
        "shortModel": "SY 480 Gen9",
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
        "mpFirmwareVersion": "1.22 Mar 06 2018",
        "mpModel": "iLO5",
        "name": "MXQ74606ZP, bay 3",
        "partNumber": "871933-B21",
        "position": 3,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 18,
        "processorCount": 2,
        "processorSpeedMhz": 2300,
        "processorType": "Intel(R) Xeon(R) Gold 6140 CPU @ 2.30GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I43 v1.36 (02/14/2018)",
        "serialNumber": "CN780900VN",
        "shortModel": "SY 660 Gen10",
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
        "mpFirmwareVersion": "2.55 Aug 16 2017",
        "mpModel": "iLO4",
        "name": "SGH807TR0K, bay 7",
        "partNumber": "826951-B21",
        "position": 7,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 14,
        "processorCount": 2,
        "processorSpeedMhz": 2000,
        "processorType": "Intel(R) Xeon(R) CPU E5-2660 v4 @ 2.00GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v2.60 (05/21/2018)",
        "serialNumber": "MXQ74306TF",
        "shortModel": "SY 480 Gen9",
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
        "mpFirmwareVersion": "2.55 Aug 16 2017",
        "mpModel": "iLO4",
        "name": "SGH807TR0K, bay 8",
        "partNumber": "826951-B21",
        "position": 8,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 14,
        "processorCount": 2,
        "processorSpeedMhz": 2000,
        "processorType": "Intel(R) Xeon(R) CPU E5-2660 v4 @ 2.00GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v2.60 (05/21/2018)",
        "serialNumber": "MXQ74306T9",
        "shortModel": "SY 480 Gen9",
        "state": "ProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "FullHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 262144,
        "model": "Synergy 660 Gen10",
        "mpFirmwareVersion": "1.22 Mar 06 2018",
        "mpModel": "iLO5",
        "name": "MXQ74606ZP, bay 4",
        "partNumber": "871932-B21",
        "position": 4,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 24,
        "processorCount": 4,
        "processorSpeedMhz": 2100,
        "processorType": "Intel(R) Xeon(R) Platinum 8160 CPU @ 2.10GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I43 v1.36 (02/14/2018)",
        "serialNumber": "CN780900VT",
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
        "mpFirmwareVersion": "1.22 Mar 06 2018",
        "mpModel": "iLO5",
        "name": "SGH807TR0J, bay 2",
        "partNumber": "871940-B21",
        "position": 2,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 4,
        "processorCount": 2,
        "processorSpeedMhz": 2600,
        "processorType": "Intel(R) Xeon(R) Silver 4112 CPU @ 2.60GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v1.36 (02/14/2018)",
        "serialNumber": "SGH825SKJM",
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
        "mpFirmwareVersion": "1.22 Mar 06 2018",
        "mpModel": "iLO5",
        "name": "SGH807TR0J, bay 4",
        "partNumber": "871933-B21",
        "position": 4,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 18,
        "processorCount": 2,
        "processorSpeedMhz": 2300,
        "processorType": "Intel(R) Xeon(R) Gold 6140 CPU @ 2.30GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I43 v1.36 (02/14/2018)",
        "serialNumber": "CN780900VS",
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
        "mpFirmwareVersion": "1.22 Mar 06 2018",
        "mpModel": "iLO5",
        "name": "SGH807TR0J, bay 5",
        "partNumber": "871940-B21",
        "position": 5,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 4,
        "processorCount": 2,
        "processorSpeedMhz": 2600,
        "processorType": "Intel(R) Xeon(R) Silver 4112 CPU @ 2.60GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v1.36 (02/14/2018)",
        "serialNumber": "SGH825SKJH",
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
        "mpFirmwareVersion": "1.22 Mar 06 2018",
        "mpModel": "iLO5",
        "name": "SGH807TR0J, bay 1",
        "partNumber": "871940-B21",
        "position": 1,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 4,
        "processorCount": 2,
        "processorSpeedMhz": 2600,
        "processorType": "Intel(R) Xeon(R) Silver 4112 CPU @ 2.60GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v1.36 (02/14/2018)",
        "serialNumber": "SGH825SKJP",
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
        "mpFirmwareVersion": "1.22 Mar 06 2018",
        "mpModel": "iLO5",
        "name": "SGH807TR0J, bay 6",
        "partNumber": "871945-B21",
        "position": 6,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 12,
        "processorCount": 1,
        "processorSpeedMhz": 2300,
        "processorType": "Intel(R) Xeon(R) Gold 5118 CPU @ 2.30GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v1.36 (02/14/2018)",
        "serialNumber": "CN78090041",
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
        "mpFirmwareVersion": "1.22 Mar 06 2018",
        "mpModel": "iLO5",
        "name": "SGH723YN4R, bay 6",
        "partNumber": "871943-B21",
        "position": 6,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 16,
        "processorCount": 2,
        "processorSpeedMhz": 2100,
        "processorType": "Intel(R) Xeon(R) Gold 6130 CPU @ 2.10GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v1.36 (02/14/2018)",
        "serialNumber": "CN78090045",
        "shortModel": "SY 480 Gen10",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 131072,
        "model": "Synergy 480 Gen9",
        "mpFirmwareVersion": "2.55 Aug 16 2017",
        "mpModel": "iLO4",
        "name": "SGH723YN4R, bay 1",
        "partNumber": "732350-B21",
        "position": 1,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 12,
        "processorCount": 2,
        "processorSpeedMhz": 2200,
        "processorType": "Intel(R) Xeon(R) CPU E5-2650 v4 @ 2.20GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v2.56 (01/22/2018)",
        "serialNumber": "SGH723YN52",
        "shortModel": "SY 480 Gen9",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 131072,
        "model": "Synergy 480 Gen9",
        "mpFirmwareVersion": "2.55 Aug 16 2017",
        "mpModel": "iLO4",
        "name": "SGH723YN4R, bay 8",
        "partNumber": "732350-B21",
        "position": 8,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 10,
        "processorCount": 2,
        "processorSpeedMhz": 2200,
        "processorType": "Intel(R) Xeon(R) CPU E5-2630 v4 @ 2.20GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v2.56 (01/22/2018)",
        "serialNumber": "SGH720W0TC",
        "shortModel": "SY 480 Gen9",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 131072,
        "model": "Synergy 480 Gen9",
        "mpFirmwareVersion": "2.55 Aug 16 2017",
        "mpModel": "iLO4",
        "name": "SGH723YN4R, bay 2",
        "partNumber": "732350-B21",
        "position": 2,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 12,
        "processorCount": 2,
        "processorSpeedMhz": 2200,
        "processorType": "Intel(R) Xeon(R) CPU E5-2650 v4 @ 2.20GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v2.56 (01/22/2018)",
        "serialNumber": "SGH723YN4V",
        "shortModel": "SY 480 Gen9",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 131072,
        "model": "Synergy 480 Gen9",
        "mpFirmwareVersion": "2.55 Aug 16 2017",
        "mpModel": "iLO4",
        "name": "SGH723YN4R, bay 12",
        "partNumber": "732350-B21",
        "position": 12,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 12,
        "processorCount": 2,
        "processorSpeedMhz": 2200,
        "processorType": "Intel(R) Xeon(R) CPU E5-2650 v4 @ 2.20GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v2.56 (01/22/2018)",
        "serialNumber": "SGH723YN4X",
        "shortModel": "SY 480 Gen9",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 131072,
        "model": "Synergy 480 Gen9",
        "mpFirmwareVersion": "2.55 Aug 16 2017",
        "mpModel": "iLO4",
        "name": "SGH723YN4R, bay 7",
        "partNumber": "732350-B21",
        "position": 7,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 12,
        "processorCount": 2,
        "processorSpeedMhz": 2200,
        "processorType": "Intel(R) Xeon(R) CPU E5-2650 v4 @ 2.20GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v2.56 (01/22/2018)",
        "serialNumber": "SGH723YN50",
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
        "model": "Synergy 480 Gen10",
        "mpFirmwareVersion": "1.30 May 31 2018",
        "mpModel": "iLO5",
        "name": "SGH720W0T8, bay 7",
        "partNumber": "871945-B21",
        "position": 7,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 12,
        "processorCount": 1,
        "processorSpeedMhz": 2300,
        "processorType": "Intel(R) Xeon(R) Gold 5118 CPU @ 2.30GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v1.40 (05/18/2018)",
        "serialNumber": "CN78090040",
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
        "mpFirmwareVersion": "1.30 May 31 2018",
        "mpModel": "iLO5",
        "name": "SGH720W0T8, bay 6",
        "partNumber": "871945-B21",
        "position": 6,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 12,
        "processorCount": 1,
        "processorSpeedMhz": 2300,
        "processorType": "Intel(R) Xeon(R) Gold 5118 CPU @ 2.30GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v1.40 (05/18/2018)",
        "serialNumber": "CN7809003W",
        "shortModel": "SY 480 Gen10",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 131072,
        "model": "Synergy 480 Gen9",
        "mpFirmwareVersion": "2.60 May 23 2018",
        "mpModel": "iLO4",
        "name": "SGH720W0T8, bay 1",
        "partNumber": "732350-B21",
        "position": 1,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 10,
        "processorCount": 2,
        "processorSpeedMhz": 2200,
        "processorType": "Intel(R) Xeon(R) CPU E5-2630 v4 @ 2.20GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v2.60 (05/21/2018)",
        "serialNumber": "SGH720W0T9",
        "shortModel": "SY 480 Gen9",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "FullHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 8192,
        "model": "Synergy 620 Gen9",
        "mpFirmwareVersion": "2.60 May 23 2018",
        "mpModel": "iLO4",
        "name": "SGH720W0T8, bay 3",
        "partNumber": "834485-B21",
        "position": 3,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 10,
        "processorCount": 1,
        "processorSpeedMhz": 2000,
        "processorType": "Intel(R) Xeon(R) CPU E7-4820 v4 @ 2.00GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I40 v2.60 (05/23/2018)",
        "serialNumber": "SGH733V67C",
        "shortModel": "SY 620 Gen9",
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
        "mpFirmwareVersion": "1.30 May 31 2018",
        "mpModel": "iLO5",
        "name": "SGH720W0T8, bay 5",
        "partNumber": "871945-B21",
        "position": 5,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 12,
        "processorCount": 1,
        "processorSpeedMhz": 2300,
        "processorType": "Intel(R) Xeon(R) Gold 5118 CPU @ 2.30GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v1.40 (05/18/2018)",
        "serialNumber": "CN7809003Y",
        "shortModel": "SY 480 Gen10",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "FullHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 8192,
        "model": "Synergy 620 Gen9",
        "mpFirmwareVersion": "2.60 May 23 2018",
        "mpModel": "iLO4",
        "name": "SGH720W0T8, bay 4",
        "partNumber": "834485-B21",
        "position": 4,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 10,
        "processorCount": 1,
        "processorSpeedMhz": 2000,
        "processorType": "Intel(R) Xeon(R) CPU E7-4820 v4 @ 2.00GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I40 v2.60 (05/23/2018)",
        "serialNumber": "SGH733V67D",
        "shortModel": "SY 620 Gen9",
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
        "mpFirmwareVersion": "1.22 Mar 06 2018",
        "mpModel": "iLO5",
        "name": "SGH723YN4R, bay 11",
        "partNumber": "871943-B21",
        "position": 11,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 16,
        "processorCount": 2,
        "processorSpeedMhz": 2100,
        "processorType": "Intel(R) Xeon(R) Gold 6130 CPU @ 2.10GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v1.36 (02/14/2018)",
        "serialNumber": "CN773407QV",
        "shortModel": "SY 480 Gen10",
        "state": "ProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    }
]

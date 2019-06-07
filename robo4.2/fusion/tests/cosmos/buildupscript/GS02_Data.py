#!/usr/bin/env python

admin_credentials = {'userName': 'Administrator', 'password': 'Cosmos123'}
timeandlocale = {'localeDisplayName': 'English (United States)', 'locale': 'en_US.UTF-8',
                 'dateTime': '2018-08-10T00:53:18.227Z', 'ntpServers': [], 'timezone': 'UTC', 'type': 'TimeAndLocale'}
licenses = [
    {
        'key': 'YBKA D9MA H9P9 8HX3 V2B4 HWWV Y9JL KMPL B89H MZVU GR4S JHWE J2SP XNZ8 CMRG HPMR UFVU A5K9 MWHC 9K4K HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'
    },
    {
        'key': 'YB2C D9MA H9PA 8HU3 V2B4 HWWV Y9JL KMPL B89H MZVU GR4S JHWE 9QSP XFR8 CMRG HPMR UFVU A5K9 MWHC 9K4K HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'
    },
    {
        'key': '9B2G D9MA H9PA CHVZ V2B4 HWWV Y9JL KMPL B89H MZVU 6RMS 9HWE 92R6 3FZ3 CMRG HPMR MFVU A5K9 MHGK EKX9 HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'
    }
]

appliance = {'type': "ApplianceNetworkConfigurationV2",
             'applianceNetworks':
                 [{
                     "device": "bond0",
                     "macAddress": "14:02:ec:46:e2:20",
                     "interfaceName": "Appliance",
                     "activeNode": 1,
                     "unconfigure": False,
                     "ipv4Type": "STATIC",
                     "ipv4Subnet": "255.255.0.0",
                     "ipv4Gateway": "10.142.0.1",
                     "ipv4NameServers": [u'10.120.0.10'],
                     "app1Ipv4Addr": "10.142.1.16",
                     "ipv6Type": "UNCONFIGURE",
                     "hostname": "EPICTB8.dom1142.lab",
                     "confOneNode": False,
                     "domainName": "dom1142.lab",
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
    },
    {
        "type": "UserAndPermissions",
        "password": "Cosmos123",
        "userName": "HardwareSetup",
        "permissions": [{u'roleName': u'Hardware setup', u'scopeUri': None}],
        "emailAddress": "",
        "officePhone": "",
        "mobilePhone": ""
    },
    {
        "type": "UserAndPermissions",
        "password": "Cosmos123",
        "userName": "appliance",
        "permissions": [{u'roleName': u'Software administrator', u'scopeUri': None}],
        "emailAddress": "",
        "officePhone": "",
        "mobilePhone": ""
    },
    {
        "type": "UserAndPermissions",
        "password": "wpsthpvse1",
        "userName": "network",
        "permissions": [{u'roleName': u'Network administrator', u'scopeUri': None}],
        "emailAddress": "",
        "officePhone": "",
        "mobilePhone": ""
    },
    {
        "type": "UserAndPermissions",
        "password": "wpsthpvse1",
        "userName": "readonly",
        "permissions": [{u'roleName': u'Read only', u'scopeUri': None}],
        "emailAddress": "",
        "officePhone": "",
        "mobilePhone": ""
    },
    {
        "type": "UserAndPermissions",
        "password": "wpsthpvse1",
        "userName": "server",
        "permissions": [{u'roleName': u'Server administrator', u'scopeUri': None}],
        "emailAddress": "",
        "officePhone": "",
        "mobilePhone": ""
    },
    {
        "type": "UserAndPermissions",
        "password": "wpsthpvse1",
        "userName": "storage",
        "permissions": [{u'roleName': u'Storage administrator', u'scopeUri': None}, {u'roleName': u'Backup administrator', u'scopeUri': None}],
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
    },
    {
        "enabled": True,
        "name": None,
        "category": "users",
        "fullName": "appliance",
        "status": None,
        "type": "UserAndPermissions",
        "userName": "appliance",
        "permissions": [{u'roleName': u'Software administrator', u'scopeUri': None}],
        "emailAddress": "",
        "officePhone": "",
        "mobilePhone": ""
    },
    {
        "enabled": True,
        "name": None,
        "category": "users",
        "fullName": "network",
        "status": None,
        "type": "UserAndPermissions",
        "userName": "network",
        "permissions": [{u'roleName': u'Network administrator', u'scopeUri': None}],
        "emailAddress": "",
        "officePhone": "",
        "mobilePhone": ""
    },
    {
        "enabled": True,
        "name": None,
        "category": "users",
        "fullName": "readonly",
        "status": None,
        "type": "UserAndPermissions",
        "userName": "readonly",
        "permissions": [{u'roleName': u'Read only', u'scopeUri': None}],
        "emailAddress": "",
        "officePhone": "",
        "mobilePhone": ""
    },
    {
        "enabled": True,
        "name": None,
        "category": "users",
        "fullName": "server",
        "status": None,
        "type": "UserAndPermissions",
        "userName": "server",
        "permissions": [{u'roleName': u'Server administrator', u'scopeUri': None}],
        "emailAddress": "",
        "officePhone": "",
        "mobilePhone": ""
    },
    {
        "enabled": True,
        "name": None,
        "category": "users",
        "fullName": "storage",
        "status": None,
        "type": "UserAndPermissions",
        "userName": "storage",
        "permissions": [{u'roleName': u'Storage administrator', u'scopeUri': None}, {u'roleName': u'Backup administrator', u'scopeUri': None}],
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
                "value": "10.120.1.65"
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
                "value": "Cosmos123"
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
                "value": "10.120.1.1"
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
                "value": "10.120.1.2"
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
        "uri": "SAN:10.120.1.65",
        "name": "10.120.1.65",
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
                "value": "10.120.1.65"
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
        "uri": "SAN:10.120.1.1",
        "name": "10.120.1.1",
        "type": "FCDeviceManagerV2",
        "category": "fc-device-managers",
        "state": "Managed",
        "description": "HP FF 5900CP-48XG-4QSFP+ Switch",
        "deviceManagerVersion": "7.1.045 Release 2416",
        "isInternal": "False",
        "providerDisplayName": "HPE",
        "refreshState": "Stable",
        "status": "OK",
        "connectionInfo": [
            {
                "name": "Host",
                "value": "10.120.1.1"
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
        "uri": "SAN:10.120.1.2",
        "name": "10.120.1.2",
        "type": "FCDeviceManagerV2",
        "category": "fc-device-managers",
        "state": "Managed",
        "description": "HP FF 5900CP-48XG-4QSFP+ Switch",
        "deviceManagerVersion": "7.1.045 Release 2416",
        "isInternal": "False",
        "providerDisplayName": "HPE",
        "refreshState": "Stable",
        "status": "OK",
        "connectionInfo": [
            {
                "name": "Host",
                "value": "10.120.1.2"
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
        "name": "Eth_1148",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1148
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth_1150",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1150
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth_1149",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1149
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth_1146",
        "privateNetwork": False,
        "purpose": "Management",
        "smartLink": True,
        "vlanId": 1146
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth_1147",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1147
    }
]
expected_ethernet_networks = [
    {
        "uri": "ETH:Eth_1148",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth_1148",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1148
    },
    {
        "uri": "ETH:Eth_1150",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth_1150",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1150
    },
    {
        "uri": "ETH:Eth_1149",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth_1149",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1149
    },
    {
        "uri": "ETH:Eth_1146",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth_1146",
        "privateNetwork": False,
        "purpose": "Management",
        "smartLink": True,
        "vlanId": 1146
    },
    {
        "uri": "ETH:Eth_1147",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth_1147",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1147
    }
]

fc_networks = [
    {
        "type": "fc-networkV4",
        "name": "FC-1",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:EPIC-G10-Snap3-Fab1-10:00:50:eb:1a:23:52:af"
    },
    {
        "type": "fc-networkV4",
        "name": "FC-2",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:EPIC-G10-Snap3-Fab2-10:00:50:eb:1a:23:52:b0"
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
        "managedSanUri": "FCSan:EPIC-G10-Snap3-Fab1-10:00:50:eb:1a:23:52:af"
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
        "managedSanUri": "FCSan:EPIC-G10-Snap3-Fab2-10:00:50:eb:1a:23:52:b0"
    }
]

fcoenets = [
    {
        "name": "FCoE-2",
        "type": "fcoe-networkV4",
        "vlanId": 3502,
        "managedSanUri": "FCSan:VSAN3502"
    },
    {
        "name": "FCoE-1",
        "type": "fcoe-networkV4",
        "vlanId": 3501,
        "managedSanUri": "FCSan:VSAN3501"
    }
]
expected_fcoenets = [
    {
        "uri": "FCOE:FCoE-2",
        "state": "Active",
        "status": "OK",
        "name": "FCoE-2",
        "type": "fcoe-networkV4",
        "vlanId": 3502,
        "managedSanUri": "FCSan:VSAN3502"
    },
    {
        "uri": "FCOE:FCoE-1",
        "state": "Active",
        "status": "OK",
        "name": "FCoE-1",
        "type": "fcoe-networkV4",
        "vlanId": 3501,
        "managedSanUri": "FCSan:VSAN3501"
    }
]

networksets = [
]
expected_networksets = [
]

storage_systems_with_pools = [
    {
        "credentials": {'username': 'cosmos', 'password': 'Insight7'},
        "name": "cos-oob-p7200",
        "family": "StoreServ",
        "hostname": "10.120.1.64",
        "deviceSpecificAttributes": {
            "managedDomain": "OOBE2",
            "managedPools": [{'domain': 'OOBE2', 'name': 'OOB2-CPG-R0', 'raidLevel': 'RAID0', 'state': 'Managed', 'deviceType': 'FC', 'freeCapacity': '5263482421248', 'totalCapacity': '5516885491712', 'uuid': 'f750b2c7-cc00-4a89-9c01-9ead327361c3'}],
            "discoveredPools": [],

        },
    },
    {
        "credentials": {'username': 'cosmos', 'password': 'Insight7'},
        "name": "tbr13par",
        "family": "StoreServ",
        "hostname": "10.120.1.7",
        "deviceSpecificAttributes": {
            "managedDomain": "TB4",
            "managedPools": [{'domain': 'TB4', 'name': 'TB4-Raid5-FC', 'raidLevel': 'RAID5', 'state': 'Managed', 'deviceType': 'FC', 'freeCapacity': '2551210573824', 'totalCapacity': '3715146711040', 'uuid': '08753949-7f62-4986-a649-8ac1e890eb67'}],
            "discoveredPools": [],

        },
    },
    {
        "credentials": {'username': 'cosmos', 'password': 'Insight7'},
        "name": "HPE_3PAR_8200_ISCSI_EPIC",
        "family": "StoreServ",
        "hostname": "10.120.1.48",
        "deviceSpecificAttributes": {
            "managedDomain": "EPIC_TB5",
            "managedPools": [{'domain': 'EPIC_TB5', 'name': 'EPICTB5', 'raidLevel': 'RAID1', 'state': 'Managed', 'deviceType': 'FC', 'freeCapacity': '66571993088', 'totalCapacity': '324270030848', 'uuid': 'b4f6a17f-2ad1-4aa1-a268-1e359bc62780'}],
            "discoveredPools": [],

        }
    }
]
expected_storage_systems_with_pools = [
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
            "managedDomain": "OOBE2",
            "serialNumber": "1648204"
        },
    },
    {
        "uri": "SSYS:tbr13par",
        "type": "StorageSystemV5",
        "state": "Managed",
        "category": "storage-systems",
        "status": "OK",
        "name": "tbr13par",
        "family": "StoreServ",
        "hostname": "10.120.1.7",
        "deviceSpecificAttributes": {
            "managedDomain": "TB4",
            "serialNumber": "1649938"
        },
    },
    {
        "uri": "SSYS:HPE_3PAR_8200_ISCSI_EPIC",
        "type": "StorageSystemV5",
        "state": "Managed",
        "category": "storage-systems",
        "status": "OK",
        "name": "HPE_3PAR_8200_ISCSI_EPIC",
        "family": "StoreServ",
        "hostname": "10.120.1.48",
        "deviceSpecificAttributes": {
            "managedDomain": "EPIC_TB5",
            "serialNumber": "2M271500PZ"
        }
    }
]

storage_pools_toedit = [
    {
        "storageSystemUri": "cos-oob-p7200",
        "name": "OOB2-CPG-R0",
        "isManaged": True,
    },
    {
        "storageSystemUri": "tbr13par",
        "name": "TB4-Raid5-FC",
        "isManaged": True,
    },
    {
        "storageSystemUri": "HPE_3PAR_8200_ISCSI_EPIC",
        "name": "EPICTB5",
        "isManaged": True,
    }
]

storage_volume_templates = [
    {
        "name": "Carbon Volume Template",
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
                "default": "OOB2-CPG-R0",
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
                "default": "OOB2-CPG-R0",
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
                "default": 53687091200,
                "required": True,
                "maximum": 17592186044416,
                "minimum": 268435456,
                "meta": {
                    "semanticType": "capacity",
                    "locked": False,
                },
                "type": "integer",
            },
        },
    },
    {
        "name": "Potash Volume Template",
        "description": "Potash Volume Template",
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
                "default": "TB4-Raid5-FC",
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
                "default": "TB4-Raid5-FC",
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
                "default": 53687091200,
                "required": True,
                "maximum": 17592186044416,
                "minimum": 268435456,
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
        "uri": "SVT:Carbon Volume Template",
        "status": "OK",
        "name": "Carbon Volume Template",
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
                "default": "SPOOL:OOB2-CPG-R0",
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
                "default": "SPOOL:OOB2-CPG-R0",
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
                "default": 53687091200,
                "required": True,
                "maximum": 17592186044416,
                "minimum": 268435456,
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
        "uri": "SVT:Potash Volume Template",
        "status": "OK",
        "name": "Potash Volume Template",
        "description": "Potash Volume Template",
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
                "default": "SPOOL:TB4-Raid5-FC",
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
                "default": "SPOOL:TB4-Raid5-FC",
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
                "default": 53687091200,
                "required": True,
                "maximum": 17592186044416,
                "minimum": 268435456,
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
        "templateUri": "ROOT",
        "isPermanent": True,
        "properties": {
            "description": "",
            "isShareable": True,
            "name": "Shared-Volume-GS02",
            "provisioningType": "Thin",
            "size": 536870912000,
            "storagePool": "TB4-Raid5-FC"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "ESXi-6.0U3-GS02",
            "provisioningType": "Thin",
            "size": 21474836480,
            "storagePool": "TB4-Raid5-FC"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "ESXi-6.0U3-GS02 (9854)",
            "provisioningType": "Thin",
            "size": 21474836480,
            "storagePool": "TB4-Raid5-FC"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "ESXi-6.0U3-GS02 (3323)",
            "provisioningType": "Thin",
            "size": 21474836480,
            "storagePool": "TB4-Raid5-FC"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "ESXi-6.0U3-GS02 (7755)",
            "provisioningType": "Thin",
            "size": 21474836480,
            "storagePool": "TB4-Raid5-FC"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "Enc1-bay-1-SLSE12-SP3-GS02",
            "provisioningType": "Thin",
            "size": 53687091200,
            "storagePool": "OOB2-CPG-R0"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "Enc1-Bay6-Windows16-GS02",
            "provisioningType": "Thin",
            "size": 53687091200,
            "storagePool": "OOB2-CPG-R0"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "C4-Bay4-RHEL7.4-GS02",
            "provisioningType": "Thin",
            "size": 53687091200,
            "storagePool": "OOB2-CPG-R0"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "Windows 12",
            "provisioningType": "Thin",
            "size": 53687091200,
            "storagePool": "TB4-Raid5-FC"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "test",
            "provisioningType": "Thin",
            "size": 10737418240,
            "storagePool": "OOB2-CPG-R0"
        }
    }
]
expected_storage_volumes = [
    {
        "status": "OK",
        "uri": "SVOL:Shared-Volume-GS02",
        "isPermanent": True,
        "properties": {
            "description": "",
            "isShareable": True,
            "name": "Shared-Volume-GS02",
            "provisioningType": "Thin",
            "size": 536870912000,
            "storagePoolUri": "SPOOL:TB4-Raid5-FC"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:ESXi-6.0U3-GS02",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "ESXi-6.0U3-GS02",
            "provisioningType": "Thin",
            "size": 21474836480,
            "storagePoolUri": "SPOOL:TB4-Raid5-FC"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:ESXi-6.0U3-GS02 (9854)",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "ESXi-6.0U3-GS02 (9854)",
            "provisioningType": "Thin",
            "size": 21474836480,
            "storagePoolUri": "SPOOL:TB4-Raid5-FC"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:ESXi-6.0U3-GS02 (3323)",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "ESXi-6.0U3-GS02 (3323)",
            "provisioningType": "Thin",
            "size": 21474836480,
            "storagePoolUri": "SPOOL:TB4-Raid5-FC"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:ESXi-6.0U3-GS02 (7755)",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "ESXi-6.0U3-GS02 (7755)",
            "provisioningType": "Thin",
            "size": 21474836480,
            "storagePoolUri": "SPOOL:TB4-Raid5-FC"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:Enc1-bay-1-SLSE12-SP3-GS02",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "Enc1-bay-1-SLSE12-SP3-GS02",
            "provisioningType": "Thin",
            "size": 53687091200,
            "storagePoolUri": "SPOOL:OOB2-CPG-R0"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:Enc1-Bay6-Windows16-GS02",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "Enc1-Bay6-Windows16-GS02",
            "provisioningType": "Thin",
            "size": 53687091200,
            "storagePoolUri": "SPOOL:OOB2-CPG-R0"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:C4-Bay4-RHEL7.4-GS02",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "C4-Bay4-RHEL7.4-GS02",
            "provisioningType": "Thin",
            "size": 53687091200,
            "storagePoolUri": "SPOOL:OOB2-CPG-R0"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:Windows 12",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "Windows 12",
            "provisioningType": "Thin",
            "size": 53687091200,
            "storagePoolUri": "SPOOL:TB4-Raid5-FC"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:test",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "test",
            "provisioningType": "Thin",
            "size": 10737418240,
            "storagePoolUri": "SPOOL:OOB2-CPG-R0"
        }
    }
]

sas_lig = [
    {
        "name": "Natasha",
        "type": "sas-logical-interconnect-groupV2",
        "enclosureType": "SY12000",
        "interconnectMapTemplate": [
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
        "uri": "SASLIG:Natasha",
        "state": "Active",
        "status": "OK",
        "description": None,
        "name": "Natasha",
        "type": "sas-logical-interconnect-groupV2",
        "enclosureType": "SY12000",
        "interconnectBaySet": 1,
        "enclosureIndexes": [1]
    }
]

ligs = [
    {
        "name": "LIG-Carbon",
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
                        "port": "2",
                        "bay": "4"
                    },
                    {
                        "speed": "Auto",
                        "enclosure": "-1",
                        "port": "1",
                        "bay": "4"
                    }
                ],
                "mode": "Auto",
                "name": "FC-2",
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
                        "bay": "1",
                        "port": "1",
                        "enclosure": "-1"
                    },
                    {
                        "speed": "Auto",
                        "bay": "1",
                        "port": "2",
                        "enclosure": "-1"
                    }
                ],
                "mode": "Auto",
                "name": "FC-1",
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
        "name": "LIG-Potash",
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
                "enclosureIndex": 3,
                "bay": 3,
                "enclosure": 3,
                "type": "Synergy 20Gb Interconnect Link Module"
            },
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
            },
            {
                "enclosureIndex": 2,
                "bay": 6,
                "enclosure": 2,
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
        "uplinkSets": [
            {
                "ethernetNetworkType": "NotApplicable",
                "lacpTimer": None,
                "logicalPortConfigInfos": [
                    {
                        "speed": "Auto",
                        "enclosure": "2",
                        "port": "Q6:1",
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
                "name": "FC 2",
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
                        "enclosure": "1",
                        "port": "Q6:1",
                        "bay": "3"
                    },
                    {
                        "speed": "Auto",
                        "port": "Q5:1",
                        "enclosure": "1",
                        "bay": "3"
                    }
                ],
                "mode": "Auto",
                "name": "FC 1",
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
                        "enclosure": "1",
                        "port": "Q4",
                        "bay": "3"
                    },
                    {
                        "speed": "Auto",
                        "enclosure": "1",
                        "port": "Q3",
                        "bay": "3"
                    }
                ],
                "mode": "Auto",
                "name": "FCoE-1",
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
                        "enclosure": "2",
                        "port": "Q1",
                        "bay": "6"
                    },
                    {
                        "speed": "Auto",
                        "enclosure": "1",
                        "port": "Q1",
                        "bay": "3"
                    },
                    {
                        "speed": "Auto",
                        "port": "Q2",
                        "enclosure": "2",
                        "bay": "6"
                    },
                    {
                        "speed": "Auto",
                        "port": "Q2",
                        "enclosure": "1",
                        "bay": "3"
                    }
                ],
                "mode": "Auto",
                "name": "Eth",
                "nativeNetworkUri": None,
                "networkType": "Ethernet",
                "networkUris": [
                    "Eth_1146",
                    "Eth_1150",
                    "Eth_1148",
                    "Eth_1147",
                    "Eth_1149"
                ],
                "primaryPort": None
            },
            {
                "ethernetNetworkType": "Tagged",
                "lacpTimer": "Short",
                "logicalPortConfigInfos": [
                    {
                        "speed": "Auto",
                        "enclosure": "2",
                        "port": "Q4",
                        "bay": "6"
                    },
                    {
                        "speed": "Auto",
                        "enclosure": "2",
                        "port": "Q3",
                        "bay": "6"
                    }
                ],
                "mode": "Auto",
                "name": "FCoE-2",
                "nativeNetworkUri": None,
                "networkType": "Ethernet",
                "networkUris": [
                    "FCoE-2"
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
        "uri": "LIG:LIG-Carbon",
        "status": None,
        "stackingHealth": None,
        "category": "logical-interconnect-groups",
        "state": "Active",
        "internalNetworkUris": "[]",
        "stackingMode": None,
        "description": None,
        "name": "LIG-Carbon",
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
        "uri": "LIG:LIG-Potash",
        "status": None,
        "stackingHealth": None,
        "category": "logical-interconnect-groups",
        "state": "Active",
        "internalNetworkUris": "[]",
        "stackingMode": None,
        "description": None,
        "name": "LIG-Potash",
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
        "name": "EG",
        "interconnectBayMappings": [
            {
                "interconnectBay": 1,
                "logicalInterconnectGroupUri": "LIG:LIG-Carbon",
                "enclosureIndex": 1
            },
            {
                "interconnectBay": 3,
                "logicalInterconnectGroupUri": "LIG:LIG-Potash",

            },
            {
                "interconnectBay": 4,
                "logicalInterconnectGroupUri": "LIG:LIG-Carbon",
                "enclosureIndex": 1
            },
            {
                "interconnectBay": 4,
                "logicalInterconnectGroupUri": "SASLIG:Natasha",
                "enclosureIndex": 2
            },
            {
                "interconnectBay": 6,
                "logicalInterconnectGroupUri": "LIG:LIG-Potash",

            }
        ],
        "ipAddressingMode": "DHCP",
        "enclosureCount": 3
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
        "associatedLogicalInterconnectGroups": [u'LIG:LIG-Carbon', u'LIG:LIG-Potash', u'SASLIG:Natasha'],
        "name": "EG",
        "type": "EnclosureGroupV7",
        "enclosureTypeUri": "/rest/enclosure-types/SY12000",
        "stackingMode": "Enclosure",
        "name": "EG",
        "interconnectBayMappingCount": "5",
        "interconnectBayMappings": [
            {
                "interconnectBay": 1,
                "logicalInterconnectGroupUri": "LIG:LIG-Carbon",

            },
            {
                "interconnectBay": 3,
                "logicalInterconnectGroupUri": "LIG:LIG-Potash",

            },
            {
                "interconnectBay": 4,
                "logicalInterconnectGroupUri": "LIG:LIG-Carbon",

            },
            {
                "interconnectBay": 4,
                "logicalInterconnectGroupUri": "SASLIG:Natasha",

            },
            {
                "interconnectBay": 6,
                "logicalInterconnectGroupUri": "LIG:LIG-Potash",

            }
        ],
        "ipAddressingMode": "DHCP",
        "enclosureCount": 3
    }
]

logical_enclosure = [
    {
        "name": "LE",
        "enclosureUris": [
            "ENC:MXQ746072Z",
            "ENC:MXQ74700C4",
            "ENC:MXQ7480420"
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
            "ENC:MXQ746072Z",
            "ENC:MXQ74700C4",
            "ENC:MXQ7480420"
        ],
        "enclosureGroupUri": "EG:EG"
    }
]

server_profile_templates = [
    {
        "name": "ESXI-6.0U3-CLRM",
        "type": "ServerProfileTemplateV6",
        "serverProfileDescription": "",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9 1:3:Synergy 3820C 10/20Gb CNA",
        "enclosureGroupUri": "EG:EG",
        "serialNumberType": "Virtual",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "SY 480 Gen 9",
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
                    "networkUri": "ETH:Eth_1146",
                    "boot": {u'priority': u'NotBootable', u'bootVlanId': None},
                },
                {
                    "id": 2,
                    "name": "",
                    "functionType": "Ethernet",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:Eth_1146",
                    "boot": {u'priority': u'NotBootable', u'bootVlanId': None},
                },
                {
                    "id": 3,
                    "name": "",
                    "functionType": "Ethernet",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:Eth_1147",
                    "boot": {u'priority': u'NotBootable', u'bootVlanId': None},
                },
                {
                    "id": 4,
                    "name": "",
                    "functionType": "Ethernet",
                    "portId": "Mezz 3:2-c",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:Eth_1147",
                    "boot": {u'priority': u'NotBootable', u'bootVlanId': None},
                },
                {
                    "id": 7,
                    "name": "",
                    "functionType": "FibreChannel",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "FCOE:FCoE-1",
                    "boot": {u'priority': u'Primary', u'bootVlanId': None, u'bootVolumeSource': u'ManagedVolume'},
                },
                {
                    "id": 8,
                    "name": "",
                    "functionType": "FibreChannel",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "networkUri": "FCOE:FCoE-2",
                    "boot": {u'priority': u'Secondary', u'bootVlanId': None, u'bootVolumeSource': u'ManagedVolume'},
                },
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": "Auto",
            "manageMode": True,
            "mode": "UEFIOptimized"
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
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "None",
                    "lunType": "Auto",
                    "lun": None,
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 8,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 7,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ],
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:Shared-Volume-GS02",
                    "lunType": "Auto",
                    "lun": None,
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 7,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 8,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ],
                },
            ]

        },
    }
]
expected_server_profile_templates = [
    {
        "uri": "SPT:ESXI-6.0U3-CLRM",
        "status": "OK",
        "name": "ESXI-6.0U3-CLRM",
        "type": "ServerProfileTemplateV6",
        "serverProfileDescription": "",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9 1:3:Synergy 3820C 10/20Gb CNA",
        "enclosureGroupUri": "EG:EG",
        "serialNumberType": "Virtual",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "SY 480 Gen 9",
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
                    "networkUri": "ETH:Eth_1146",
                    "boot": {u'priority': u'NotBootable', u'bootVlanId': None},
                },
                {
                    "id": 2,
                    "name": "",
                    "functionType": "Ethernet",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:Eth_1146",
                    "boot": {u'priority': u'NotBootable', u'bootVlanId': None},
                },
                {
                    "id": 3,
                    "name": "",
                    "functionType": "Ethernet",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:Eth_1147",
                    "boot": {u'priority': u'NotBootable', u'bootVlanId': None},
                },
                {
                    "id": 4,
                    "name": "",
                    "functionType": "Ethernet",
                    "portId": "Mezz 3:2-c",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:Eth_1147",
                    "boot": {u'priority': u'NotBootable', u'bootVlanId': None},
                },
                {
                    "id": 7,
                    "name": "",
                    "functionType": "FibreChannel",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "FCOE:FCoE-1",
                    "boot": {u'priority': u'Primary', u'bootVlanId': None, u'bootVolumeSource': u'ManagedVolume'},
                },
                {
                    "id": 8,
                    "name": "",
                    "functionType": "FibreChannel",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "networkUri": "FCOE:FCoE-2",
                    "boot": {u'priority': u'Secondary', u'bootVlanId': None, u'bootVolumeSource': u'ManagedVolume'},
                },
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": "Auto",
            "manageMode": True,
            "mode": "UEFIOptimized"
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
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "None",
                    "lunType": "Auto",
                    "lun": None,
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 8,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 7,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ],
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:Shared-Volume-GS02",
                    "lunType": "Auto",
                    "lun": None,
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 7,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 8,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ],
                },
            ]

        },
    }
]

server_profiles_from_spt = [
    {
        "serverProfileTemplateUri": "SPT:ESXI-6.0U3-CLRM",
        "name": "Enc3-bay8-ESXI-6",
        "type": "ServerProfileV10",
        "serverHardwareUri": "MXQ7480420, bay 8",
        "enclosureGroupUri": "EG:EG",
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
                    "networkUri": "ETH:Eth_1146",
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
                    "networkUri": "ETH:Eth_1146",
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
                    "networkUri": "ETH:Eth_1147",
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
                    "portId": "Mezz 3:2-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1147",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 7,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": "10:00:66:49:b3:90:00:35",
                    "wwpn": "10:00:66:49:b3:90:00:34",
                    "networkUri": "FCOE:FCoE-1",
                    "boot": {u'priority': u'Primary', u'bootVolumeSource': u'ManagedVolume'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 8,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "wwnn": "10:00:66:49:b3:90:00:37",
                    "wwpn": "10:00:66:49:b3:90:00:36",
                    "networkUri": "FCOE:FCoE-2",
                    "boot": {u'priority': u'Secondary', u'bootVolumeSource': u'ManagedVolume'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": "Auto",
            "manageMode": True,
            "mode": "UEFIOptimized"
        },
        "firmware": {
            "manageFirmware": True,
            "firmwareBaselineUri": "/rest/firmware-drivers/bp-2018-06-28-01",
            "forceInstallFirmware": False,
            "firmwareInstallType": "FirmwareAndOSDrivers"
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
                    "volumeUri": "SVOL:ESXi-6.0U3-GS02 (3323)",
                    "bootVolumePriority": "Primary",
                    "lunType": "Auto",
                    "lun": None,
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 8,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 7,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:Shared-Volume-GS02",
                    "bootVolumePriority": "NotBootable",
                    "lunType": "Auto",
                    "lun": None,
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 7,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 8,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                }
            ]

        },
    },
    {
        "serverProfileTemplateUri": "SPT:ESXI-6.0U3-CLRM",
        "name": "Enc1-Bay3-Esxi-6.0",
        "type": "ServerProfileV10",
        "serverHardwareUri": "MXQ746072Z, bay 3",
        "enclosureGroupUri": "EG:EG",
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
                    "networkUri": "ETH:Eth_1146",
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
                    "networkUri": "ETH:Eth_1146",
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
                    "networkUri": "ETH:Eth_1147",
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
                    "portId": "Mezz 3:2-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1147",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 7,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": "10:00:66:49:b3:90:00:2d",
                    "wwpn": "10:00:66:49:b3:90:00:2c",
                    "networkUri": "FCOE:FCoE-1",
                    "boot": {u'priority': u'Primary', u'bootVolumeSource': u'ManagedVolume'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 8,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "wwnn": "10:00:66:49:b3:90:00:2f",
                    "wwpn": "10:00:66:49:b3:90:00:2e",
                    "networkUri": "FCOE:FCoE-2",
                    "boot": {u'priority': u'Secondary', u'bootVolumeSource': u'ManagedVolume'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": "Auto",
            "manageMode": True,
            "mode": "UEFIOptimized"
        },
        "firmware": {
            "manageFirmware": True,
            "firmwareBaselineUri": "/rest/firmware-drivers/bp-2018-06-28-01",
            "forceInstallFirmware": False,
            "firmwareInstallType": "FirmwareAndOSDrivers"
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
                    "volumeUri": "SVOL:ESXi-6.0U3-GS02",
                    "bootVolumePriority": "Primary",
                    "lunType": "Auto",
                    "lun": None,
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 8,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 7,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:Shared-Volume-GS02",
                    "bootVolumePriority": "NotBootable",
                    "lunType": "Auto",
                    "lun": None,
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 7,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 8,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                }
            ]

        },
    },
    {
        "serverProfileTemplateUri": "SPT:ESXI-6.0U3-CLRM",
        "name": "Enc2-Bay3-ESXI-6.0",
        "type": "ServerProfileV10",
        "serverHardwareUri": "MXQ74700C4, bay 3",
        "enclosureGroupUri": "EG:EG",
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
                    "networkUri": "ETH:Eth_1146",
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
                    "networkUri": "ETH:Eth_1146",
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
                    "networkUri": "ETH:Eth_1147",
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
                    "portId": "Mezz 3:2-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1147",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 7,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": "10:00:66:49:b3:90:00:31",
                    "wwpn": "10:00:66:49:b3:90:00:30",
                    "networkUri": "FCOE:FCoE-1",
                    "boot": {u'priority': u'Primary', u'bootVolumeSource': u'ManagedVolume'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 8,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "wwnn": "10:00:66:49:b3:90:00:33",
                    "wwpn": "10:00:66:49:b3:90:00:32",
                    "networkUri": "FCOE:FCoE-2",
                    "boot": {u'priority': u'Secondary', u'bootVolumeSource': u'ManagedVolume'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": "Auto",
            "manageMode": True,
            "mode": "UEFIOptimized"
        },
        "firmware": {
            "manageFirmware": True,
            "firmwareBaselineUri": "/rest/firmware-drivers/bp-2018-06-28-01",
            "forceInstallFirmware": False,
            "firmwareInstallType": "FirmwareAndOSDrivers"
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
                    "volumeUri": "SVOL:ESXi-6.0U3-GS02 (9854)",
                    "bootVolumePriority": "Primary",
                    "lunType": "Auto",
                    "lun": None,
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 8,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 7,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:Shared-Volume-GS02",
                    "bootVolumePriority": "NotBootable",
                    "lunType": "Auto",
                    "lun": None,
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 8,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 7,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                }
            ]

        },
    },
    {
        "serverProfileTemplateUri": "SPT:ESXI-6.0U3-CLRM",
        "name": "Enc2-Bay8-ESXI-6.0",
        "type": "ServerProfileV10",
        "serverHardwareUri": "MXQ74700C4, bay 8",
        "enclosureGroupUri": "EG:EG",
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
                    "networkUri": "ETH:Eth_1146",
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
                    "networkUri": "ETH:Eth_1146",
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
                    "networkUri": "ETH:Eth_1147",
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
                    "portId": "Mezz 3:2-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1147",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 7,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": "10:00:66:49:b3:90:00:39",
                    "wwpn": "10:00:66:49:b3:90:00:38",
                    "networkUri": "FCOE:FCoE-1",
                    "boot": {u'priority': u'Primary', u'bootVolumeSource': u'ManagedVolume'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 8,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "wwnn": "10:00:66:49:b3:90:00:3b",
                    "wwpn": "10:00:66:49:b3:90:00:3a",
                    "networkUri": "FCOE:FCoE-2",
                    "boot": {u'priority': u'Secondary', u'bootVolumeSource': u'ManagedVolume'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": "Auto",
            "manageMode": True,
            "mode": "UEFIOptimized"
        },
        "firmware": {
            "manageFirmware": True,
            "firmwareBaselineUri": "/rest/firmware-drivers/bp-2018-06-28-01",
            "forceInstallFirmware": False,
            "firmwareInstallType": "FirmwareAndOSDrivers"
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
                    "volumeUri": "SVOL:ESXi-6.0U3-GS02 (7755)",
                    "bootVolumePriority": "Primary",
                    "lunType": "Auto",
                    "lun": None,
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 8,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 7,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:Shared-Volume-GS02",
                    "bootVolumePriority": "NotBootable",
                    "lunType": "Auto",
                    "lun": None,
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 7,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 8,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                }
            ]

        },
    }
]
expected_server_profiles_from_spt = [
    {
        "uri": "SP:Enc3-bay8-ESXI-6",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9 1:3:Synergy 3820C 10/20Gb CNA",
        "name": "Enc3-bay8-ESXI-6",
        "type": "ServerProfileV10",
        "serverHardwareUri": "MXQ7480420, bay 8",
        "enclosureGroupUri": "EG:EG",
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
                    "networkUri": "ETH:Eth_1146",
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
                    "networkUri": "ETH:Eth_1146",
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
                    "networkUri": "ETH:Eth_1147",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1147",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 7,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": "10:00:66:49:b3:90:00:35",
                    "wwpn": "10:00:66:49:b3:90:00:34",
                    "networkUri": "FCOE:FCoE-1",
                    "boot": {u'priority': u'Primary', u'bootVolumeSource': u'ManagedVolume'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 8,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "wwnn": "10:00:66:49:b3:90:00:37",
                    "wwpn": "10:00:66:49:b3:90:00:36",
                    "networkUri": "FCOE:FCoE-2",
                    "boot": {u'priority': u'Secondary', u'bootVolumeSource': u'ManagedVolume'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": "Auto",
            "manageMode": True,
            "mode": "UEFIOptimized"
        },
        "firmware": {
            "manageFirmware": True,
            "firmwareBaselineUri": "/rest/firmware-drivers/bp-2018-06-28-01",
            "forceInstallFirmware": False,
            "firmwareInstallType": "FirmwareAndOSDrivers"
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
                    "volumeUri": "SVOL:ESXi-6.0U3-GS02 (3323)",
                    "bootVolumePriority": "Primary",
                    "lunType": "Auto",
                    "lun": None,
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 8,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 7,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:Shared-Volume-GS02",
                    "bootVolumePriority": "NotBootable",
                    "lunType": "Auto",
                    "lun": None,
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 7,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 8,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                }
            ]

        },
    },
    {
        "uri": "SP:Enc1-Bay3-Esxi-6.0",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9 1:3:Synergy 3820C 10/20Gb CNA",
        "name": "Enc1-Bay3-Esxi-6.0",
        "type": "ServerProfileV10",
        "serverHardwareUri": "MXQ746072Z, bay 3",
        "enclosureGroupUri": "EG:EG",
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
                    "networkUri": "ETH:Eth_1146",
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
                    "networkUri": "ETH:Eth_1146",
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
                    "networkUri": "ETH:Eth_1147",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1147",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 7,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": "10:00:66:49:b3:90:00:2d",
                    "wwpn": "10:00:66:49:b3:90:00:2c",
                    "networkUri": "FCOE:FCoE-1",
                    "boot": {u'priority': u'Primary', u'bootVolumeSource': u'ManagedVolume'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 8,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "wwnn": "10:00:66:49:b3:90:00:2f",
                    "wwpn": "10:00:66:49:b3:90:00:2e",
                    "networkUri": "FCOE:FCoE-2",
                    "boot": {u'priority': u'Secondary', u'bootVolumeSource': u'ManagedVolume'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": "Auto",
            "manageMode": True,
            "mode": "UEFIOptimized"
        },
        "firmware": {
            "manageFirmware": True,
            "firmwareBaselineUri": "/rest/firmware-drivers/bp-2018-06-28-01",
            "forceInstallFirmware": False,
            "firmwareInstallType": "FirmwareAndOSDrivers"
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
                    "volumeUri": "SVOL:ESXi-6.0U3-GS02",
                    "bootVolumePriority": "Primary",
                    "lunType": "Auto",
                    "lun": None,
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 8,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 7,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:Shared-Volume-GS02",
                    "bootVolumePriority": "NotBootable",
                    "lunType": "Auto",
                    "lun": None,
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 7,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 8,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                }
            ]

        },
    },
    {
        "uri": "SP:Enc2-Bay3-ESXI-6.0",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9 1:3:Synergy 3820C 10/20Gb CNA",
        "name": "Enc2-Bay3-ESXI-6.0",
        "type": "ServerProfileV10",
        "serverHardwareUri": "MXQ74700C4, bay 3",
        "enclosureGroupUri": "EG:EG",
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
                    "networkUri": "ETH:Eth_1146",
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
                    "networkUri": "ETH:Eth_1146",
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
                    "networkUri": "ETH:Eth_1147",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1147",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 7,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": "10:00:66:49:b3:90:00:31",
                    "wwpn": "10:00:66:49:b3:90:00:30",
                    "networkUri": "FCOE:FCoE-1",
                    "boot": {u'priority': u'Primary', u'bootVolumeSource': u'ManagedVolume'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 8,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "wwnn": "10:00:66:49:b3:90:00:33",
                    "wwpn": "10:00:66:49:b3:90:00:32",
                    "networkUri": "FCOE:FCoE-2",
                    "boot": {u'priority': u'Secondary', u'bootVolumeSource': u'ManagedVolume'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": "Auto",
            "manageMode": True,
            "mode": "UEFIOptimized"
        },
        "firmware": {
            "manageFirmware": True,
            "firmwareBaselineUri": "/rest/firmware-drivers/bp-2018-06-28-01",
            "forceInstallFirmware": False,
            "firmwareInstallType": "FirmwareAndOSDrivers"
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
                    "volumeUri": "SVOL:ESXi-6.0U3-GS02 (9854)",
                    "bootVolumePriority": "Primary",
                    "lunType": "Auto",
                    "lun": None,
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 8,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 7,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:Shared-Volume-GS02",
                    "bootVolumePriority": "NotBootable",
                    "lunType": "Auto",
                    "lun": None,
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 8,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 7,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                }
            ]

        },
    },
    {
        "uri": "SP:Enc2-Bay8-ESXI-6.0",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9 1:3:Synergy 3820C 10/20Gb CNA",
        "name": "Enc2-Bay8-ESXI-6.0",
        "type": "ServerProfileV10",
        "serverHardwareUri": "MXQ74700C4, bay 8",
        "enclosureGroupUri": "EG:EG",
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
                    "networkUri": "ETH:Eth_1146",
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
                    "networkUri": "ETH:Eth_1146",
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
                    "networkUri": "ETH:Eth_1147",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1147",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 7,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": "10:00:66:49:b3:90:00:39",
                    "wwpn": "10:00:66:49:b3:90:00:38",
                    "networkUri": "FCOE:FCoE-1",
                    "boot": {u'priority': u'Primary', u'bootVolumeSource': u'ManagedVolume'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 8,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "wwnn": "10:00:66:49:b3:90:00:3b",
                    "wwpn": "10:00:66:49:b3:90:00:3a",
                    "networkUri": "FCOE:FCoE-2",
                    "boot": {u'priority': u'Secondary', u'bootVolumeSource': u'ManagedVolume'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": "Auto",
            "manageMode": True,
            "mode": "UEFIOptimized"
        },
        "firmware": {
            "manageFirmware": True,
            "firmwareBaselineUri": "/rest/firmware-drivers/bp-2018-06-28-01",
            "forceInstallFirmware": False,
            "firmwareInstallType": "FirmwareAndOSDrivers"
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
                    "volumeUri": "SVOL:ESXi-6.0U3-GS02 (7755)",
                    "bootVolumePriority": "Primary",
                    "lunType": "Auto",
                    "lun": None,
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 8,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 7,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:Shared-Volume-GS02",
                    "bootVolumePriority": "NotBootable",
                    "lunType": "Auto",
                    "lun": None,
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 7,
                            "targetSelector": "Auto",
                            "targets": [],
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 8,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                }
            ]

        },
    }
]

server_profiles = [
]
expected_server_profiles = [
]

server_profile_with_storage = [
    {
        "name": "C4-Bay7-Windows12",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:MXQ74700C4, bay 7",
        "enclosureUri": "ENC:MXQ74700C4",
        "enclosureGroupUri": "EG:EG",
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
                    "networkUri": "ETH:Eth_1146",
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
                    "networkUri": "ETH:Eth_1146",
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
                    "wwnn": "10:00:66:49:b3:90:00:49",
                    "wwpn": "10:00:66:49:b3:90:00:48",
                    "networkUri": "FCOE:FCoE-1",
                    "boot": {u'priority': u'Primary', u'bootVolumeSource': u'ManagedVolume'},
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
                    "wwnn": "10:00:66:49:b3:90:00:4b",
                    "wwpn": "10:00:66:49:b3:90:00:4a",
                    "networkUri": "FCOE:FCoE-2",
                    "boot": {u'priority': u'Secondary', u'bootVolumeSource': u'ManagedVolume'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": "Auto",
            "manageMode": True,
            "mode": "UEFI"
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
                    "volumeUri": "SVOL:Windows 12",
                    "bootVolumePriority": "Primary",
                    "lunType": "Auto",
                    "lun": None,
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
    },
    {
        "name": "BAY-1-SLSE12SP3-FC",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:MXQ746072Z, bay 1",
        "enclosureUri": "ENC:MXQ746072Z",
        "enclosureGroupUri": "EG:EG",
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
                    "networkUri": "ETH:Eth_1146",
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
                    "networkUri": "ETH:Eth_1146",
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
                    "networkUri": "ETH:Eth_1147",
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
                    "portId": "Mezz 3:2-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1147",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 5,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 16000,
                    "name": "",
                    "portId": "Mezz 1:1",
                    "requestedMbps": "Auto",
                    "wwnn": "10:00:66:49:b3:90:00:3d",
                    "wwpn": "10:00:66:49:b3:90:00:3c",
                    "networkUri": "FC:FC-1",
                    "boot": {u'priority': u'Primary', u'bootVolumeSource': u'ManagedVolume'},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 6,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 16000,
                    "name": "",
                    "portId": "Mezz 1:2",
                    "requestedMbps": "16000",
                    "wwnn": "10:00:66:49:b3:90:00:3f",
                    "wwpn": "10:00:66:49:b3:90:00:3e",
                    "networkUri": "FC:FC-2",
                    "boot": {u'priority': u'Secondary', u'bootVolumeSource': u'ManagedVolume'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": "Auto",
            "manageMode": True,
            "mode": "UEFI"
        },
        "firmware": {
            "manageFirmware": True,
            "firmwareBaselineUri": "/rest/firmware-drivers/bp-2018-06-28-01",
            "forceInstallFirmware": False,
            "firmwareInstallType": "FirmwareAndOSDrivers"
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
            "hostOSType": "SuSE (10.x, 11.x, 12.x)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:Enc1-bay-1-SLSE12-SP3-GS02",
                    "bootVolumePriority": "Primary",
                    "lunType": "Auto",
                    "lun": None,
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
        "name": "test",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:MXQ7480420, bay 2",
        "enclosureUri": "ENC:MXQ7480420",
        "enclosureGroupUri": "EG:EG",
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
                    "networkUri": "ETH:Eth_1146",
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
                    "networkUri": "ETH:Eth_1146",
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
                    "wwnn": "10:00:66:49:b3:90:00:4d",
                    "wwpn": "10:00:66:49:b3:90:00:4c",
                    "networkUri": "FC:FC-1",
                    "boot": {u'priority': u'Primary', u'bootVolumeSource': u'ManagedVolume'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": "Auto",
            "manageMode": True,
            "mode": "UEFI"
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
                    "volumeUri": "SVOL:test",
                    "bootVolumePriority": "Primary",
                    "lunType": "Auto",
                    "lun": None,
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                }
            ]

        },
    },
    {
        "name": "C4-Bay4-RHEL7.4",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:MXQ74700C4, bay 4",
        "enclosureUri": "ENC:MXQ74700C4",
        "enclosureGroupUri": "EG:EG",
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
                    "networkUri": "ETH:Eth_1146",
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
                    "networkUri": "ETH:Eth_1146",
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
                    "wwnn": "10:00:66:49:b3:90:00:45",
                    "wwpn": "10:00:66:49:b3:90:00:44",
                    "networkUri": "FC:FC-1",
                    "boot": {u'priority': u'Primary', u'bootVolumeSource': u'ManagedVolume'},
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
                    "wwnn": "10:00:66:49:b3:90:00:47",
                    "wwpn": "10:00:66:49:b3:90:00:46",
                    "networkUri": "FC:FC-2",
                    "boot": {u'priority': u'Secondary', u'bootVolumeSource': u'ManagedVolume'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": "Auto",
            "manageMode": True,
            "mode": "UEFI"
        },
        "firmware": {
            "manageFirmware": True,
            "firmwareBaselineUri": "/rest/firmware-drivers/bp-2018-06-28-01",
            "forceInstallFirmware": False,
            "firmwareInstallType": "FirmwareAndOSDrivers"
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
                    "volumeUri": "SVOL:C4-Bay4-RHEL7.4-GS02",
                    "bootVolumePriority": "Primary",
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
        "name": "Enc1-Bay6-Windows16",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:MXQ746072Z, bay 6",
        "enclosureUri": "ENC:MXQ746072Z",
        "enclosureGroupUri": "EG:EG",
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
                    "networkUri": "ETH:Eth_1146",
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
                    "networkUri": "ETH:Eth_1146",
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
                    "portId": "Mezz 6:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1147",
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
                    "portId": "Mezz 6:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1147",
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
                    "wwnn": "10:00:66:49:b3:90:00:41",
                    "wwpn": "10:00:66:49:b3:90:00:40",
                    "networkUri": "FC:FC-1",
                    "boot": {u'priority': u'Primary', u'bootVolumeSource': u'ManagedVolume'},
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
                    "wwnn": "10:00:66:49:b3:90:00:43",
                    "wwpn": "10:00:66:49:b3:90:00:42",
                    "networkUri": "FC:FC-2",
                    "boot": {u'priority': u'Secondary', u'bootVolumeSource': u'ManagedVolume'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": "Auto",
            "manageMode": True,
            "mode": "UEFI"
        },
        "firmware": {
            "manageFirmware": True,
            "firmwareBaselineUri": "/rest/firmware-drivers/bp-2018-06-28-01",
            "forceInstallFirmware": False,
            "firmwareInstallType": "FirmwareAndOSDrivers"
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
                    "volumeUri": "SVOL:Enc1-Bay6-Windows16-GS02",
                    "bootVolumePriority": "Primary",
                    "lunType": "Auto",
                    "lun": None,
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
                }
            ]

        },
    }
]
expected_server_profile_with_storage = [
    {
        "uri": "SP:C4-Bay7-Windows12",
        "state": "Normal",
        "status": "Critical",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9 2:1:Smart Array P542D Controller:3:Synergy 3820C 10/20Gb CNA",
        "name": "C4-Bay7-Windows12",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:MXQ74700C4, bay 7",
        "enclosureUri": "ENC:MXQ74700C4",
        "enclosureGroupUri": "EG:EG",
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
                    "networkUri": "ETH:Eth_1146",
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
                    "networkUri": "ETH:Eth_1146",
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
                    "wwnn": "10:00:66:49:b3:90:00:49",
                    "wwpn": "10:00:66:49:b3:90:00:48",
                    "networkUri": "FCOE:FCoE-1",
                    "boot": {u'priority': u'Primary', u'bootVolumeSource': u'ManagedVolume'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 5,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "wwnn": "10:00:66:49:b3:90:00:4b",
                    "wwpn": "10:00:66:49:b3:90:00:4a",
                    "networkUri": "FCOE:FCoE-2",
                    "boot": {u'priority': u'Secondary', u'bootVolumeSource': u'ManagedVolume'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": "Auto",
            "manageMode": True,
            "mode": "UEFI"
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
                    "volumeUri": "SVOL:Windows 12",
                    "bootVolumePriority": "Primary",
                    "lunType": "Auto",
                    "lun": None,
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
    },
    {
        "uri": "SP:BAY-1-SLSE12SP3-FC",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9 3:1:Synergy 3530C 16G HBA:3:Synergy 3820C 10/20Gb CNA",
        "name": "BAY-1-SLSE12SP3-FC",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:MXQ746072Z, bay 1",
        "enclosureUri": "ENC:MXQ746072Z",
        "enclosureGroupUri": "EG:EG",
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
                    "networkUri": "ETH:Eth_1146",
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
                    "networkUri": "ETH:Eth_1146",
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
                    "networkUri": "ETH:Eth_1147",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1147",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 5,
                    "maximumMbps": 16000,
                    "name": "",
                    "portId": "Mezz 1:1",
                    "requestedMbps": "Auto",
                    "wwnn": "10:00:66:49:b3:90:00:3d",
                    "wwpn": "10:00:66:49:b3:90:00:3c",
                    "networkUri": "FC:FC-1",
                    "boot": {u'priority': u'Primary', u'bootVolumeSource': u'ManagedVolume'},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 6,
                    "maximumMbps": 16000,
                    "name": "",
                    "portId": "Mezz 1:2",
                    "requestedMbps": "16000",
                    "wwnn": "10:00:66:49:b3:90:00:3f",
                    "wwpn": "10:00:66:49:b3:90:00:3e",
                    "networkUri": "FC:FC-2",
                    "boot": {u'priority': u'Secondary', u'bootVolumeSource': u'ManagedVolume'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": "Auto",
            "manageMode": True,
            "mode": "UEFI"
        },
        "firmware": {
            "manageFirmware": True,
            "firmwareBaselineUri": "/rest/firmware-drivers/bp-2018-06-28-01",
            "forceInstallFirmware": False,
            "firmwareInstallType": "FirmwareAndOSDrivers"
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
            "hostOSType": "SuSE (10.x, 11.x, 12.x)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:Enc1-bay-1-SLSE12-SP3-GS02",
                    "bootVolumePriority": "Primary",
                    "lunType": "Auto",
                    "lun": None,
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
        "uri": "SP:test",
        "state": "Normal",
        "status": "Critical",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9 1:3:Synergy 3820C 10/20Gb CNA",
        "name": "test",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:MXQ7480420, bay 2",
        "enclosureUri": "ENC:MXQ7480420",
        "enclosureGroupUri": "EG:EG",
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
                    "networkUri": "ETH:Eth_1146",
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
                    "networkUri": "ETH:Eth_1146",
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
                    "wwnn": "10:00:66:49:b3:90:00:4d",
                    "wwpn": "10:00:66:49:b3:90:00:4c",
                    "networkUri": "FC:FC-1",
                    "boot": {u'priority': u'Primary', u'bootVolumeSource': u'ManagedVolume'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": "Auto",
            "manageMode": True,
            "mode": "UEFI"
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
                    "volumeUri": "SVOL:test",
                    "bootVolumePriority": "Primary",
                    "lunType": "Auto",
                    "lun": None,
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                            "targets": [],
                        },

                    ]
                }
            ]

        },
    },
    {
        "uri": "SP:C4-Bay4-RHEL7.4",
        "state": "Normal",
        "status": "Critical",
        "serverHardwareTypeUri": "SHT:SY 480 Gen10 1:3:Synergy 3820C 10/20Gb CNA",
        "name": "C4-Bay4-RHEL7.4",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:MXQ74700C4, bay 4",
        "enclosureUri": "ENC:MXQ74700C4",
        "enclosureGroupUri": "EG:EG",
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
                    "networkUri": "ETH:Eth_1146",
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
                    "networkUri": "ETH:Eth_1146",
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
                    "wwnn": "10:00:66:49:b3:90:00:45",
                    "wwpn": "10:00:66:49:b3:90:00:44",
                    "networkUri": "FC:FC-1",
                    "boot": {u'priority': u'Primary', u'bootVolumeSource': u'ManagedVolume'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "wwnn": "10:00:66:49:b3:90:00:47",
                    "wwpn": "10:00:66:49:b3:90:00:46",
                    "networkUri": "FC:FC-2",
                    "boot": {u'priority': u'Secondary', u'bootVolumeSource': u'ManagedVolume'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": "Auto",
            "manageMode": True,
            "mode": "UEFI"
        },
        "firmware": {
            "manageFirmware": True,
            "firmwareBaselineUri": "/rest/firmware-drivers/bp-2018-06-28-01",
            "forceInstallFirmware": False,
            "firmwareInstallType": "FirmwareAndOSDrivers"
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
                    "volumeUri": "SVOL:C4-Bay4-RHEL7.4-GS02",
                    "bootVolumePriority": "Primary",
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
        "uri": "SP:Enc1-Bay6-Windows16",
        "state": "UpdateFailed",
        "status": "Critical",
        "serverHardwareTypeUri": "SHT:SY 660 Gen10 1:3:Synergy 3820C 10/20Gb CNA:6:Synergy 3820C 10/20Gb CNA",
        "name": "Enc1-Bay6-Windows16",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:MXQ746072Z, bay 6",
        "enclosureUri": "ENC:MXQ746072Z",
        "enclosureGroupUri": "EG:EG",
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
                    "networkUri": "ETH:Eth_1146",
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
                    "networkUri": "ETH:Eth_1146",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 6:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1147",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 6:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1147",
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
                    "wwnn": "10:00:66:49:b3:90:00:41",
                    "wwpn": "10:00:66:49:b3:90:00:40",
                    "networkUri": "FC:FC-1",
                    "boot": {u'priority': u'Primary', u'bootVolumeSource': u'ManagedVolume'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 6,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "wwnn": "10:00:66:49:b3:90:00:43",
                    "wwpn": "10:00:66:49:b3:90:00:42",
                    "networkUri": "FC:FC-2",
                    "boot": {u'priority': u'Secondary', u'bootVolumeSource': u'ManagedVolume'},
                }
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": "Auto",
            "manageMode": True,
            "mode": "UEFI"
        },
        "firmware": {
            "manageFirmware": True,
            "firmwareBaselineUri": "/rest/firmware-drivers/bp-2018-06-28-01",
            "forceInstallFirmware": False,
            "firmwareInstallType": "FirmwareAndOSDrivers"
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
                    "volumeUri": "SVOL:Enc1-Bay6-Windows16-GS02",
                    "bootVolumePriority": "Primary",
                    "lunType": "Auto",
                    "lun": None,
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
                }
            ]

        },
    }
]

configured_enclosures = [
    {
        "name": "MXQ746072Z",
        "state": "Configured",
        "serialNumber": "MXQ746072Z",
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
        "name": "MXQ7480420",
        "state": "Configured",
        "serialNumber": "MXQ7480420",
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
                "devicePresence": "Absent"
            },
            {
                "bayNumber": 11,
                "devicePresence": "Absent"
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
        "name": "MXQ74700C4",
        "state": "Configured",
        "serialNumber": "MXQ74700C4",
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
                "devicePresence": "Present"
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
        "mpFirmwareVersion": "2.60 May 23 2018",
        "mpModel": "iLO4",
        "name": "MXQ7480420, bay 9",
        "partNumber": "826953-B21",
        "position": 9,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 10,
        "processorCount": 2,
        "processorSpeedMhz": 2200,
        "processorType": "Intel(R) Xeon(R) CPU E5-2630 v4 @ 2.20GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v2.60 (05/21/2018)",
        "serialNumber": "MXQ7480487",
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
        "mpFirmwareVersion": "1.30 May 31 2018",
        "mpModel": "iLO5",
        "name": "MXQ7480420, bay 1",
        "partNumber": "871946-B21",
        "position": 1,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 6,
        "processorCount": 2,
        "processorSpeedMhz": 1700,
        "processorType": "Intel(R) Xeon(R) Bronze 3104 CPU @ 1.70GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v1.42 (06/20/2018)",
        "serialNumber": "MXQ74603HB",
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
        "mpFirmwareVersion": "2.60 May 23 2018",
        "mpModel": "iLO4",
        "name": "MXQ7480420, bay 8",
        "partNumber": "826953-B21",
        "position": 8,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 10,
        "processorCount": 2,
        "processorSpeedMhz": 2200,
        "processorType": "Intel(R) Xeon(R) CPU E5-2630 v4 @ 2.20GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v2.60 (05/21/2018)",
        "serialNumber": "MXQ748048K",
        "shortModel": "SY 480 Gen9",
        "state": "ProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 16384,
        "model": "Synergy 480 Gen9",
        "mpFirmwareVersion": "2.60 May 23 2018",
        "mpModel": "iLO4",
        "name": "MXQ7480420, bay 2",
        "partNumber": "754683-001",
        "position": 2,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 6,
        "processorCount": 2,
        "processorSpeedMhz": 1600,
        "processorType": "Intel(R) Xeon(R) CPU E5-2603 v3 @ 1.60GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v2.60 (05/21/2018)",
        "serialNumber": "CN75460709",
        "shortModel": "SY 480 Gen9",
        "state": "ProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "FullHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 32768,
        "model": "Synergy 660 Gen9",
        "mpFirmwareVersion": "2.60 May 23 2018",
        "mpModel": "iLO4",
        "name": "MXQ7480420, bay 6",
        "partNumber": "732360-B21",
        "position": 6,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 10,
        "processorCount": 4,
        "processorSpeedMhz": 1800,
        "processorType": "Intel(R) Xeon(R) CPU E5-4610 v4 @ 1.80GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I39 v2.60 (05/21/2018)",
        "serialNumber": "MXQ75107SM",
        "shortModel": "SY 660 Gen9",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 16384,
        "model": "Synergy 480 Gen9",
        "mpFirmwareVersion": "2.60 May 23 2018",
        "mpModel": "iLO4",
        "name": "MXQ74700C4, bay 8",
        "partNumber": "754683-001",
        "position": 8,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 12,
        "processorCount": 1,
        "processorSpeedMhz": 2600,
        "processorType": "Intel(R) Xeon(R) CPU E5-2690 v3 @ 2.60GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v2.60 (05/21/2018)",
        "serialNumber": "CN7518006B",
        "shortModel": "SY 480 Gen9",
        "state": "ProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 16384,
        "model": "Synergy 480 Gen9",
        "mpFirmwareVersion": "2.60 May 23 2018",
        "mpModel": "iLO4",
        "name": "MXQ74700C4, bay 3",
        "partNumber": "754683-001",
        "position": 3,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 6,
        "processorCount": 2,
        "processorSpeedMhz": 1600,
        "processorType": "Intel(R) Xeon(R) CPU E5-2603 v3 @ 1.60GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v2.60 (05/21/2018)",
        "serialNumber": "CN7546070C",
        "shortModel": "SY 480 Gen9",
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
        "mpFirmwareVersion": "1.30 May 31 2018",
        "mpModel": "iLO5",
        "name": "MXQ74700C4, bay 9",
        "partNumber": "871946-B21",
        "position": 9,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 16,
        "processorCount": 2,
        "processorSpeedMhz": 2100,
        "processorType": "Intel(R) Xeon(R) Gold 6130 CPU @ 2.10GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v1.42 (06/20/2018)",
        "serialNumber": "MXQ807050G",
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
        "mpFirmwareVersion": "2.60 May 23 2018",
        "mpModel": "iLO4",
        "name": "MXQ74700C4, bay 7",
        "partNumber": "826953-B21",
        "position": 7,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 10,
        "processorCount": 1,
        "processorSpeedMhz": 2200,
        "processorType": "Intel(R) Xeon(R) CPU E5-2630 v4 @ 2.20GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v2.60 (05/21/2018)",
        "serialNumber": "MXQ74604HQ",
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
        "mpFirmwareVersion": "1.30 May 31 2018",
        "mpModel": "iLO5",
        "name": "MXQ746072Z, bay 7",
        "partNumber": "871945-B21",
        "position": 7,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 12,
        "processorCount": 2,
        "processorSpeedMhz": 2300,
        "processorType": "Intel(R) Xeon(R) Gold 5118 CPU @ 2.30GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v1.42 (06/20/2018)",
        "serialNumber": "MXQ819037N",
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
        "model": "Synergy 480 Gen9",
        "mpFirmwareVersion": "2.60 May 23 2018",
        "mpModel": "iLO4",
        "name": "MXQ746072Z, bay 3",
        "partNumber": "754683-001",
        "position": 3,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 6,
        "processorCount": 2,
        "processorSpeedMhz": 1600,
        "processorType": "Intel(R) Xeon(R) CPU E5-2603 v3 @ 1.60GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v2.60 (05/21/2018)",
        "serialNumber": "CN7546070K",
        "shortModel": "SY 480 Gen9",
        "state": "ProfileApplied",
        "stateReason": "NotApplicable",
        "status": "Warning",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "FullHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 65536,
        "model": "Synergy 660 Gen10",
        "mpFirmwareVersion": "1.30 May 31 2018",
        "mpModel": "iLO5",
        "name": "MXQ746072Z, bay 6",
        "partNumber": "871934-B21",
        "position": 6,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 12,
        "processorCount": 2,
        "processorSpeedMhz": 2300,
        "processorType": "Intel(R) Xeon(R) Gold 5118 CPU @ 2.30GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I43 v1.42 (06/20/2018)",
        "serialNumber": "MXQ75104BC",
        "shortModel": "SY 660 Gen10",
        "state": "ProfileError",
        "stateReason": "NotApplicable",
        "status": "Critical",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 32768,
        "model": "Synergy 480 Gen9",
        "mpFirmwareVersion": "2.60 May 23 2018",
        "mpModel": "iLO4",
        "name": "MXQ746072Z, bay 1",
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
        "serialNumber": "MXQ74604HM",
        "shortModel": "SY 480 Gen9",
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
        "mpFirmwareVersion": "1.30 May 31 2018",
        "mpModel": "iLO5",
        "name": "MXQ74700C4, bay 4",
        "partNumber": "871946-B21",
        "position": 4,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 6,
        "processorCount": 2,
        "processorSpeedMhz": 1700,
        "processorType": "Intel(R) Xeon(R) Bronze 3104 CPU @ 1.70GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v1.42 (06/20/2018)",
        "serialNumber": "MXQ74603HJ",
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
        "mpFirmwareVersion": "1.30 May 31 2018",
        "mpModel": "iLO5",
        "name": "MXQ7480420, bay 4",
        "partNumber": "871946-B21",
        "position": 4,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 6,
        "processorCount": 2,
        "processorSpeedMhz": 1700,
        "processorType": "Intel(R) Xeon(R) Bronze 3104 CPU @ 1.70GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v1.40 (05/18/2018)",
        "serialNumber": "MXQ74603HG",
        "shortModel": "SY 480 Gen10",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    }
]

#!/usr/bin/env python

admin_credentials = {'userName': 'Administrator', 'password': 'Cosmos123'}
timeandlocale = {'localeDisplayName': 'English (United States)', 'locale': 'en_US.UTF-8',
                 'dateTime': '2018-10-26T00:59:28.661Z', 'ntpServers': [], 'timezone': 'UTC', 'type': 'TimeAndLocale'}
licenses = [
    {
        'key': 'YB2C D9MA H9PA 8HU3 V2B4 HWWV Y9JL KMPL B89H MZVU GR4S JHWE 9QSP XFR8 CMRG HPMR UFVU A5K9 MWHC 9K4K HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'
    },
    {
        'key': 'YBKA D9MA H9P9 8HX3 V2B4 HWWV Y9JL KMPL B89H MZVU GR4S JHWE J2SP XNZ8 CMRG HPMR UFVU A5K9 MWHC 9K4K HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'
    }
]

appliance = {
    'type': "ApplianceNetworkConfigurationV2",
    'applianceNetworks':
    [{
        "device": "bond0",
        "macAddress": "14:02:ec:46:83:58",
        "interfaceName": "Appliance",
        "activeNode": 1,
        "unconfigure": False,
        "ipv4Type": "STATIC",
        "ipv4Subnet": "255.255.0.0",
        "ipv4Gateway": "10.153.0.1",
        "ipv4NameServers": [u'10.120.0.10'],
        "app1Ipv4Addr": "10.153.1.16",
        "ipv6Type": "UNCONFIGURE",
        "hostname": "BFS3.dom1153.lab",
        "confOneNode": False,
        "domainName": "dom1153.lab",
        "aliasDisabled": False
    }
    ]}

ipv4_subnet = [
]

ipv4_ranges = [
]

ranges = [
    {
        'type': "Range",
        'name': "VMAC",
        'category': "id-range-VMAC",
        'rangeCategory': "Generated",
        'startAddress': "E6:51:E7:40:00:00",
        'endAddress': "E6:51:E7:4F:FF:FF",
        'enabled': True
    },
    {
        'type': "Range",
        'name': "VWWN",
        'category': "id-range-VWWN",
        'rangeCategory': "Generated",
        'startAddress': "10:00:b2:1a:26:b0:00:00",
        'endAddress': "10:00:b2:1a:26:bf:ff:ff",
        'enabled': True
    },
    {
        'type': "Range",
        'name': "VSN",
        'category': "id-range-VSN",
        'rangeCategory': "Generated",
        'startAddress': "VCGW0D9000",
        'endAddress': "VCGW0D9ZZZ",
        'enabled': True
    }
]

deployment_server = [
]

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
                "value": 'Brocade Network Advisor',
            },
            {
                "name": "Host",
                "value": "10.120.1.85"
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
                "value": "10.120.1.80"
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
                "value": "10.120.1.86"
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
        "uri": "SAN:10.120.1.85",
        "name": "10.120.1.85",
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
                "value": "10.120.1.85"
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
        "uri": "SAN:10.120.1.80",
        "name": "10.120.1.80",
        "type": "FCDeviceManagerV2",
        "category": "fc-device-managers",
        "state": "Managed",
        "description": "HPE 5900AF-48G-4XG-2QSFP+ Switc",
        "deviceManagerVersion": "7.1.045 Release 2422P03",
        "isInternal": "False",
        "providerDisplayName": "HPE",
        "refreshState": "Stable",
        "status": "OK",
        "connectionInfo": [
            {
                "name": "Host",
                "value": "10.120.1.80"
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
        "uri": "SAN:10.120.1.86",
        "name": "10.120.1.86",
        "type": "FCDeviceManagerV2",
        "category": "fc-device-managers",
        "state": "Managed",
        "description": "HPE 5900AF-48G-4XG-2QSFP+ Switc",
        "deviceManagerVersion": "7.1.045 Release 2422P03",
        "isInternal": "False",
        "providerDisplayName": "HPE",
        "refreshState": "Stable",
        "status": "OK",
        "connectionInfo": [
            {
                "name": "Host",
                "value": "10.120.1.86"
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

ethernet_networks = [
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "1120",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1120
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "1151",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1151
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "1152",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1152
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "iscsi-1121",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1121
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "1153",
        "privateNetwork": False,
        "purpose": "Management",
        "smartLink": True,
        "vlanId": 1153
    }
]
expected_ethernet_networks = [
    {
        "uri": "ETH:1120",
        "category": "ethernet-networks",
        "state": "Active",
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "1120",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1120
    },
    {
        "uri": "ETH:1151",
        "category": "ethernet-networks",
        "state": "Active",
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "1151",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1151
    },
    {
        "uri": "ETH:1152",
        "category": "ethernet-networks",
        "state": "Active",
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "1152",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1152
    },
    {
        "uri": "ETH:iscsi-1121",
        "category": "ethernet-networks",
        "state": "Active",
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "iscsi-1121",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1121
    },
    {
        "uri": "ETH:1153",
        "category": "ethernet-networks",
        "state": "Active",
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "1153",
        "privateNetwork": False,
        "purpose": "Management",
        "smartLink": True,
        "vlanId": 1153
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
        "name": "FC A",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:RIST-R1-SN6600B-SW1"
    },
    {
        "type": "fc-networkV4",
        "name": "FC B",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:RIST-R1-SN6600B-SW2"
    }
]
expected_fc_networks = [
    {
        "category": "fc-networks",
        "state": "Active",
        "description": None,
        "uri": "FC:FC A",
        "status": "OK",
        "type": "fc-networkV4",
        "name": "FC A",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:RIST-R1-SN6600B-SW1"
    },
    {
        "category": "fc-networks",
        "state": "Active",
        "description": None,
        "uri": "FC:FC B",
        "status": "OK",
        "type": "fc-networkV4",
        "name": "FC B",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:RIST-R1-SN6600B-SW2"
    }
]

fcoe_networks = [
    {
        "name": "fcoe 3802",
        "type": "fcoe-networkV4",
        "vlanId": 3802,
        "managedSanUri": "FCSan:VSAN3802"
    },
    {
        "name": "fcoe 3801",
        "type": "fcoe-networkV4",
        "vlanId": 3801,
        "managedSanUri": "FCSan:VSAN3801"
    }
]
expected_fcoe_networks = [
    {
        "uri": "FCOE:fcoe 3802",
        "state": "Active",
        "status": "OK",
        "name": "fcoe 3802",
        "type": "fcoe-networkV4",
        "vlanId": 3802,
        "managedSanUri": "FCSan:VSAN3802"
    },
    {
        "uri": "FCOE:fcoe 3801",
        "state": "Active",
        "status": "OK",
        "name": "fcoe 3801",
        "type": "fcoe-networkV4",
        "vlanId": 3801,
        "managedSanUri": "FCSan:VSAN3801"
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
        "hostname": "10.120.0.201",
        "ports": [
            {
                "expectedNetworkUri": "ETH:iscsi-1121",
                "expectedNetworkName": "iscsi-1121",
                "mode": "Managed",
                "name": "10.120.0.204"
            }
        ]
    },
    {
        "credentials": {u'username': u'cosmos', u'password': 'Insight7'},
        "name": "CST-Nimble-CS5000",
        "family": "Nimble",
        "hostname": "10.120.0.155",
        "ports": [
            {
                "expectedNetworkUri": "ETH:iscsi-1121",
                "expectedNetworkName": "iscsi-1121",
                "mode": "Managed",
                "name": "Subnet-1121"
            }
        ]
    },
    {
        "credentials": {u'username': u'cosmos', u'password': 'Insight7'},
        "name": "HPE_3PAR_8200_ISCSI_EPIC",
        "family": "StoreServ",
        "hostname": "10.120.1.48",
        "deviceSpecificAttributes": {
            "managedDomain": "EPIC_TB5",
            "managedPools": [{'domain': 'EPIC_TB5', 'name': 'EPICTB5', 'raidLevel': 'RAID1', 'state': 'Managed', 'deviceType': 'FC', 'freeCapacity': '1897301803008', 'totalCapacity': '1897301803008', 'uuid': 'b4f6a17f-2ad1-4aa1-a268-1e359bc62780'}],
            "discoveredPools": [],

        },
    },
    {
        "credentials": {u'username': u'cosmos', u'password': 'Insight7'},
        "name": "RIST-R1-3PAR",
        "family": "StoreServ",
        "hostname": "10.120.1.81",
        "deviceSpecificAttributes": {
            "managedDomain": "NO DOMAIN",
            "managedPools": [{'domain': 'NO DOMAIN', 'name': 'FC_r1', 'raidLevel': 'RAID1', 'state': 'Managed', 'deviceType': 'FC', 'freeCapacity': '1215475744768', 'totalCapacity': '2788507516928', 'uuid': 'd5aed6dd-6ea8-4ac5-ae51-72112a7bc43a'}, {'domain': 'NO DOMAIN', 'name': 'FC_r5', 'raidLevel': 'RAID5', 'state': 'Managed', 'deviceType': 'FC', 'freeCapacity': '1073741824000', 'totalCapacity': '1125281431552', 'uuid': 'd991ad64-3cf2-459b-886c-d63deb4c3737'}, {'domain': 'NO DOMAIN', 'name': 'FC_r6', 'raidLevel': 'RAID6', 'state': 'Managed', 'deviceType': 'FC', 'freeCapacity': '858725023744', 'totalCapacity': '858725023744', 'uuid': '9f3043ce-5dc2-4a48-9d5f-d1fc393d5c57'}],
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
        "hostname": "10.120.0.201",
        "ports": [
            {
                "expectedNetworkUri": "ETH:iscsi-1121",
                "expectedNetworkName": "iscsi-1121",
                "mode": "Managed",
                "name": "10.120.0.204"
            }
        ]
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
                "expectedNetworkUri": "ETH:iscsi-1121",
                "expectedNetworkName": "iscsi-1121",
                "mode": "Managed",
                "name": "Subnet-1121"
            }
        ]
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
        },
    },
    {
        "uri": "SSYS:RIST-R1-3PAR",
        "type": "StorageSystemV5",
        "state": "Managed",
        "category": "storage-systems",
        "status": "OK",
        "name": "RIST-R1-3PAR",
        "family": "StoreServ",
        "hostname": "10.120.1.81",
        "deviceSpecificAttributes": {
            "managedDomain": "NO DOMAIN",
            "serialNumber": "2M273304WT"
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
        "storageSystemUri": "HPE_3PAR_8200_ISCSI_EPIC",
        "name": "EPICTB5",
        "isManaged": True,
    },
    {
        "storageSystemUri": "RIST-R1-3PAR",
        "name": "FC_r1",
        "isManaged": True,
    },
    {
        "storageSystemUri": "RIST-R1-3PAR",
        "name": "FC_r5",
        "isManaged": True,
    },
    {
        "storageSystemUri": "RIST-R1-3PAR",
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
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "422_bay2_bronco_iscsi_rh76",
            "provisioningType": "Thin",
            "size": 53687091200,
            "storagePool": "default"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "VT-win2016",
            "provisioningType": "Thin",
            "size": 32212254720,
            "storagePool": "FC_r1"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "41xbay5broncoiscsirh76",
            "provisioningType": "Thin",
            "size": 53687091200,
            "storagePool": "default"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "bfs3-41X_bay2_Quack_iscsi_Win16",
            "provisioningType": "Thin",
            "size": 53687091200,
            "storagePool": "default"
        }
    }
]
expected_storage_volumes = [
    {
        "status": "OK",
        "uri": "SVOL:422_bay2_bronco_iscsi_rh76",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "422_bay2_bronco_iscsi_rh76",
            "provisioningType": "Thin",
            "size": 53687091200,
            "storagePoolUri": "SPOOL:default"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:VT-win2016",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "VT-win2016",
            "provisioningType": "Thin",
            "size": 32212254720,
            "storagePoolUri": "SPOOL:FC_r1"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:41xbay5broncoiscsirh76",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "41xbay5broncoiscsirh76",
            "provisioningType": "Thin",
            "size": 53687091200,
            "storagePoolUri": "SPOOL:default"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:bfs3-41X_bay2_Quack_iscsi_Win16",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "bfs3-41X_bay2_Quack_iscsi_Win16",
            "provisioningType": "Thin",
            "size": 53687091200,
            "storagePoolUri": "SPOOL:default"
        }
    }
]

sas_lig = [
]
expected_sas_lig = [
]

ligs = [
    {
        "name": "LIG-potash",
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
                "bay": 6,
                "enclosure": 1,
                "type": "Synergy 20Gb Interconnect Link Module"
            },
            {
                "enclosureIndex": 2,
                "enclosure": 2,
                "bay": 3,
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
                        "enclosure": "1",
                        "port": "Q5:1",
                        "bay": "3"
                    },
                    {
                        "speed": "Auto",
                        "port": "Q6:1",
                        "enclosure": "1",
                        "bay": "3"
                    }
                ],
                "mode": "Auto",
                "name": "FC-A",
                "nativeNetworkUri": None,
                "networkType": "FibreChannel",
                "networkUris": [
                    "FC A"
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
                        "enclosure": "1",
                        "bay": "3"
                    },
                    {
                        "speed": "Auto",
                        "enclosure": "1",
                        "port": "Q4",
                        "bay": "3"
                    }
                ],
                "mode": "Auto",
                "name": "FCoE A",
                "nativeNetworkUri": None,
                "networkType": "Ethernet",
                "networkUris": [
                    "fcoe 3801"
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
                        "port": "Q2",
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
                        "enclosure": "1",
                        "port": "Q1",
                        "bay": "3"
                    },
                    {
                        "speed": "Auto",
                        "enclosure": "2",
                        "port": "Q1",
                        "bay": "6"
                    }
                ],
                "mode": "Auto",
                "name": "eth + iscsi",
                "nativeNetworkUri": None,
                "networkType": "Ethernet",
                "networkUris": [
                    "1153",
                    "1152",
                    "iscsi-1121",
                    "1151",
                    "1120"
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
                        "enclosure": "2",
                        "port": "Q4",
                        "bay": "6"
                    }
                ],
                "mode": "Auto",
                "name": "FCOE B",
                "nativeNetworkUri": None,
                "networkType": "Ethernet",
                "networkUris": [
                    "fcoe 3802"
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
                        "enclosure": "2",
                        "bay": "6"
                    },
                    {
                        "speed": "Auto",
                        "port": "Q6:1",
                        "enclosure": "2",
                        "bay": "6"
                    }
                ],
                "mode": "Auto",
                "name": "FC-B",
                "nativeNetworkUri": None,
                "networkType": "FibreChannel",
                "networkUris": [
                    "FC B"
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
        "uri": "LIG:LIG-potash",
        "status": None,
        "stackingHealth": None,
        "category": "logical-interconnect-groups",
        "state": "Active",
        "internalNetworkUris": "[]",
        "stackingMode": None,
        "description": None,
        "name": "LIG-potash",
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
                "interconnectBay": 3,
                "logicalInterconnectGroupUri": "LIG:LIG-potash",

            },
            {
                "interconnectBay": 6,
                "logicalInterconnectGroupUri": "LIG:LIG-potash",

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
        "associatedLogicalInterconnectGroups": [u'LIG:LIG-potash'],
        "name": "EG",
        "type": "EnclosureGroupV7",
        "enclosureTypeUri": "/rest/enclosure-types/SY12000",
        "stackingMode": "Enclosure",
        "name": "EG",
        "interconnectBayMappingCount": "2",
        "interconnectBayMappings": [
            {
                "interconnectBay": 3,
                "logicalInterconnectGroupUri": "LIG:LIG-potash",

            },
            {
                "interconnectBay": 6,
                "logicalInterconnectGroupUri": "LIG:LIG-potash",

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
            "ENC:MXQ748041X",
            "ENC:MXQ7480422"
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
            "ENC:MXQ748041X",
            "ENC:MXQ7480422"
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
    {
        "name": "422, bay 7",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:MXQ7480422, bay 7",
        "enclosureUri": "ENC:MXQ7480422",
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
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:1152",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:2-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:1152",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:1-e",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:1153",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:2-e",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:1153",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:iscsi-1121",
                    "boot": {u'priority': u'Primary', u'iscsi': {u'chapName': u'iqn.2015-02.com.hpe:oneview-vcgw0d9003', u'firstBootTargetPort': u'3260', u'bootTargetName': u'iqn.2007-11.com.nimblestorage:bfs3-41xbay2quackiscsiwin16-v3d023acce95d7b7c.000000e2.d45f41b0', u'initiatorName': u'iqn.2015-02.com.hpe:oneview-vcgw0d9003', u'bootTargetLun': u'0', u'firstBootTargetIp': u'10.121.0.155', u'chapLevel': u'Chap', u'initiatorNameSource': u'ProfileInitiatorName'}, u'ethernetBootType': u'iSCSI', u'bootVolumeSource': u'ManagedVolume'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 6,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:iscsi-1121",
                    "boot": {u'priority': u'Secondary', u'iscsi': {u'chapName': u'iqn.2015-02.com.hpe:oneview-vcgw0d9003', u'firstBootTargetPort': u'3260', u'bootTargetName': u'iqn.2007-11.com.nimblestorage:bfs3-41xbay2quackiscsiwin16-v3d023acce95d7b7c.000000e2.d45f41b0', u'initiatorName': u'iqn.2015-02.com.hpe:oneview-vcgw0d9003', u'bootTargetLun': u'0', u'firstBootTargetIp': u'10.121.0.155', u'chapLevel': u'Chap', u'initiatorNameSource': u'ProfileInitiatorName'}, u'ethernetBootType': u'iSCSI', u'bootVolumeSource': u'ManagedVolume'},
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
                    "volumeUri": "SVOL:bfs3-41X_bay2_Quack_iscsi_Win16",
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
        "name": "22-1-Vananh",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:MXQ7480422, bay 1",
        "enclosureUri": "ENC:MXQ7480422",
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
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:1151",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:1151",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:1152",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:2-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:1152",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 5,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": "10:00:b2:1a:26:b0:00:01",
                    "wwpn": "10:00:b2:1a:26:b0:00:00",
                    "networkUri": "FC:FC A",
                    "boot": {u'priority': u'Primary', u'bootVolumeSource': u'ManagedVolume'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 6,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "wwnn": "10:00:b2:1a:26:b0:00:03",
                    "wwpn": "10:00:b2:1a:26:b0:00:02",
                    "networkUri": "FC:FC B",
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
            "hostOSType": "Windows Server 2016",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:VT-win2016",
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
        "name": "41x_bay5_bronco_iscsi_rh76",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:MXQ748041X, bay 5",
        "enclosureUri": "ENC:MXQ748041X",
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
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:1153",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:1153",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:1152",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:2-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:1152",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "iSCSI",
                    "id": 5,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:iscsi-1121",
                    "boot": {u'priority': u'Primary', u'iscsi': {u'chapName': u'iqn.2015-02.com.hpe:oneview-vcgw0d9002', u'firstBootTargetPort': u'3260', u'bootTargetName': u'iqn.2007-11.com.nimblestorage:41xbay5broncoiscsirh76-v3d023acce95d7b7c.000000de.d45f41b0', u'initiatorName': u'iqn.2015-02.com.hpe:oneview-vcgw0d9002', u'bootTargetLun': u'0', u'firstBootTargetIp': u'10.121.0.155', u'chapLevel': u'Chap', u'initiatorNameSource': u'ProfileInitiatorName'}, u'bootVolumeSource': u'ManagedVolume'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "iSCSI",
                    "id": 6,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:iscsi-1121",
                    "boot": {u'priority': u'Secondary', u'iscsi': {u'chapName': u'iqn.2015-02.com.hpe:oneview-vcgw0d9002', u'firstBootTargetPort': u'3260', u'bootTargetName': u'iqn.2007-11.com.nimblestorage:41xbay5broncoiscsirh76-v3d023acce95d7b7c.000000de.d45f41b0', u'initiatorName': u'iqn.2015-02.com.hpe:oneview-vcgw0d9002', u'bootTargetLun': u'0', u'firstBootTargetIp': u'10.121.0.155', u'chapLevel': u'Chap', u'initiatorNameSource': u'ProfileInitiatorName'}, u'bootVolumeSource': u'ManagedVolume'},
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
            "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:41xbay5broncoiscsirh76",
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
        "name": "422_bay2_bronco_iscsi_RH76",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:MXQ7480422, bay 2",
        "enclosureUri": "ENC:MXQ7480422",
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
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:1153",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:1153",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:1152",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:2-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:1152",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "iSCSI",
                    "id": 5,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:iscsi-1121",
                    "boot": {u'priority': u'Primary', u'iscsi': {u'mutualChapName': u'', u'secondBootTargetPort': u'', u'chapName': u'iqn.2015-02.com.hpe:oneview-vcgw0d9001', u'firstBootTargetPort': u'3260', u'bootTargetName': u'iqn.2007-11.com.nimblestorage:422bay2broncoiscsirh76-v3d023acce95d7b7c.000000db.d45f41b0', u'initiatorName': u'iqn.2015-02.com.hpe:oneview-vcgw0d9001', u'bootTargetLun': u'0', u'secondBootTargetIp': u'', u'firstBootTargetIp': u'10.121.0.155', u'chapLevel': u'Chap', u'initiatorNameSource': u'ProfileInitiatorName'}, u'bootVolumeSource': u'UserDefined'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "iSCSI",
                    "id": 6,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:iscsi-1121",
                    "boot": {u'priority': u'Secondary', u'iscsi': {u'mutualChapName': u'', u'secondBootTargetPort': u'', u'chapName': u'iqn.2015-02.com.hpe:oneview-vcgw0d9001', u'firstBootTargetPort': u'3260', u'bootTargetName': u'iqn.2007-11.com.nimblestorage:422bay2broncoiscsirh76-v3d023acce95d7b7c.000000db.d45f41b0', u'initiatorName': u'iqn.2015-02.com.hpe:oneview-vcgw0d9001', u'bootTargetLun': u'0', u'secondBootTargetIp': u'', u'firstBootTargetIp': u'10.121.0.155', u'chapLevel': u'Chap', u'initiatorNameSource': u'ProfileInitiatorName'}, u'bootVolumeSource': u'UserDefined'},
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
            "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:422_bay2_bronco_iscsi_rh76",
                    "bootVolumePriority": "NotBootable",
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
    }
]
expected_server_profile_with_storage = [
    {
        "uri": "SP:422, bay 7",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen10 2:2:Synergy 3830C 16G FC HBA:3:Synergy 4820C 10/20/25Gb CNA",
        "name": "422, bay 7",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:MXQ7480422, bay 7",
        "enclosureUri": "ENC:MXQ7480422",
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
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:1152",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:2-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:1152",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:1-e",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:1153",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:2-e",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:1153",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 5,
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:iscsi-1121",
                    "boot": {u'priority': u'Primary', u'iscsi': {u'chapName': u'iqn.2015-02.com.hpe:oneview-vcgw0d9003', u'firstBootTargetPort': u'3260', u'bootTargetName': u'iqn.2007-11.com.nimblestorage:bfs3-41xbay2quackiscsiwin16-v3d023acce95d7b7c.000000e2.d45f41b0', u'initiatorName': u'iqn.2015-02.com.hpe:oneview-vcgw0d9003', u'bootTargetLun': u'0', u'firstBootTargetIp': u'10.121.0.155', u'chapLevel': u'Chap', u'initiatorNameSource': u'ProfileInitiatorName'}, u'ethernetBootType': u'iSCSI', u'bootVolumeSource': u'ManagedVolume'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 6,
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:iscsi-1121",
                    "boot": {u'priority': u'Secondary', u'iscsi': {u'chapName': u'iqn.2015-02.com.hpe:oneview-vcgw0d9003', u'firstBootTargetPort': u'3260', u'bootTargetName': u'iqn.2007-11.com.nimblestorage:bfs3-41xbay2quackiscsiwin16-v3d023acce95d7b7c.000000e2.d45f41b0', u'initiatorName': u'iqn.2015-02.com.hpe:oneview-vcgw0d9003', u'bootTargetLun': u'0', u'firstBootTargetIp': u'10.121.0.155', u'chapLevel': u'Chap', u'initiatorNameSource': u'ProfileInitiatorName'}, u'ethernetBootType': u'iSCSI', u'bootVolumeSource': u'ManagedVolume'},
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
                    "volumeUri": "SVOL:bfs3-41X_bay2_Quack_iscsi_Win16",
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
        "uri": "SP:22-1-Vananh",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9 1:3:Synergy 3820C 10/20Gb CNA",
        "name": "22-1-Vananh",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:MXQ7480422, bay 1",
        "enclosureUri": "ENC:MXQ7480422",
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
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:1151",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:1151",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:1152",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:2-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:1152",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 5,
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": "10:00:b2:1a:26:b0:00:01",
                    "wwpn": "10:00:b2:1a:26:b0:00:00",
                    "networkUri": "FC:FC A",
                    "boot": {u'priority': u'Primary', u'bootVolumeSource': u'ManagedVolume'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 6,
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "wwnn": "10:00:b2:1a:26:b0:00:03",
                    "wwpn": "10:00:b2:1a:26:b0:00:02",
                    "networkUri": "FC:FC B",
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
            "hostOSType": "Windows Server 2016",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:VT-win2016",
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
        "uri": "SP:41x_bay5_bronco_iscsi_rh76",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 680 Gen9 1:1:Smart Array P542D Controller:3:Synergy 3820C 10/20Gb CNA",
        "name": "41x_bay5_bronco_iscsi_rh76",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:MXQ748041X, bay 5",
        "enclosureUri": "ENC:MXQ748041X",
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
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:1153",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:1153",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:1152",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:2-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:1152",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "iSCSI",
                    "id": 5,
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:iscsi-1121",
                    "boot": {u'priority': u'Primary', u'iscsi': {u'chapName': u'iqn.2015-02.com.hpe:oneview-vcgw0d9002', u'firstBootTargetPort': u'3260', u'bootTargetName': u'iqn.2007-11.com.nimblestorage:41xbay5broncoiscsirh76-v3d023acce95d7b7c.000000de.d45f41b0', u'initiatorName': u'iqn.2015-02.com.hpe:oneview-vcgw0d9002', u'bootTargetLun': u'0', u'firstBootTargetIp': u'10.121.0.155', u'chapLevel': u'Chap', u'initiatorNameSource': u'ProfileInitiatorName'}, u'bootVolumeSource': u'ManagedVolume'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "iSCSI",
                    "id": 6,
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:iscsi-1121",
                    "boot": {u'priority': u'Secondary', u'iscsi': {u'chapName': u'iqn.2015-02.com.hpe:oneview-vcgw0d9002', u'firstBootTargetPort': u'3260', u'bootTargetName': u'iqn.2007-11.com.nimblestorage:41xbay5broncoiscsirh76-v3d023acce95d7b7c.000000de.d45f41b0', u'initiatorName': u'iqn.2015-02.com.hpe:oneview-vcgw0d9002', u'bootTargetLun': u'0', u'firstBootTargetIp': u'10.121.0.155', u'chapLevel': u'Chap', u'initiatorNameSource': u'ProfileInitiatorName'}, u'bootVolumeSource': u'ManagedVolume'},
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
            "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:41xbay5broncoiscsirh76",
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
        "uri": "SP:422_bay2_bronco_iscsi_RH76",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen10 4:3:Synergy 3820C 10/20Gb CNA",
        "name": "422_bay2_bronco_iscsi_RH76",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:MXQ7480422, bay 2",
        "enclosureUri": "ENC:MXQ7480422",
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
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:1153",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:1153",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:1152",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:2-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:1152",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "iSCSI",
                    "id": 5,
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:iscsi-1121",
                    "boot": {u'priority': u'Primary', u'iscsi': {u'mutualChapName': u'', u'secondBootTargetPort': u'', u'chapName': u'iqn.2015-02.com.hpe:oneview-vcgw0d9001', u'firstBootTargetPort': u'3260', u'bootTargetName': u'iqn.2007-11.com.nimblestorage:422bay2broncoiscsirh76-v3d023acce95d7b7c.000000db.d45f41b0', u'initiatorName': u'iqn.2015-02.com.hpe:oneview-vcgw0d9001', u'bootTargetLun': u'0', u'secondBootTargetIp': u'', u'firstBootTargetIp': u'10.121.0.155', u'chapLevel': u'Chap', u'initiatorNameSource': u'ProfileInitiatorName'}, u'bootVolumeSource': u'UserDefined'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "iSCSI",
                    "id": 6,
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:iscsi-1121",
                    "boot": {u'priority': u'Secondary', u'iscsi': {u'mutualChapName': u'', u'secondBootTargetPort': u'', u'chapName': u'iqn.2015-02.com.hpe:oneview-vcgw0d9001', u'firstBootTargetPort': u'3260', u'bootTargetName': u'iqn.2007-11.com.nimblestorage:422bay2broncoiscsirh76-v3d023acce95d7b7c.000000db.d45f41b0', u'initiatorName': u'iqn.2015-02.com.hpe:oneview-vcgw0d9001', u'bootTargetLun': u'0', u'secondBootTargetIp': u'', u'firstBootTargetIp': u'10.121.0.155', u'chapLevel': u'Chap', u'initiatorNameSource': u'ProfileInitiatorName'}, u'bootVolumeSource': u'UserDefined'},
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
            "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:422_bay2_bronco_iscsi_rh76",
                    "bootVolumePriority": "NotBootable",
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
    }
]

servers = [
    {
        "formFactor": "FullHeightDoubleWide",
        "licensingIntent": "NotApplicable",
        "memoryMb": 262144,
        "model": "Synergy 680 Gen9",
        "mpFirmwareVersion": "2.61 Jul 27 2018",
        "mpModel": "iLO4",
        "name": "MXQ748041X, bay 5",
        "partNumber": "834481-B21",
        "position": 5,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 18,
        "processorCount": 4,
        "processorSpeedMhz": 2200,
        "processorType": "Intel(R) Xeon(R) CPU E7-8860 v4 @ 2.20GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I40 v2.60 (05/23/2018)",
        "serialNumber": "MXQ75105SW",
        "shortModel": "SY 680 Gen9",
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
        "mpFirmwareVersion": "1.40 Oct 11 2018",
        "mpModel": "iLO5",
        "name": "MXQ748041X, bay 9",
        "partNumber": "871945-B21",
        "position": 9,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 12,
        "processorCount": 2,
        "processorSpeedMhz": 2300,
        "processorType": "Intel(R) Xeon(R) Gold 5118 CPU @ 2.30GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v2.00 (10/03/2018)",
        "serialNumber": "MXQ819037R",
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
        "mpFirmwareVersion": "1.40 Oct 11 2018",
        "mpModel": "iLO5",
        "name": "MXQ748041X, bay 7",
        "partNumber": "871945-B21",
        "position": 7,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 12,
        "processorCount": 2,
        "processorSpeedMhz": 2300,
        "processorType": "Intel(R) Xeon(R) Gold 5118 CPU @ 2.30GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v2.00 (10/03/2018)",
        "serialNumber": "MXQ819037P",
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
        "mpFirmwareVersion": "1.40 Oct 11 2018",
        "mpModel": "iLO5",
        "name": "MXQ748041X, bay 8",
        "partNumber": "871946-B21",
        "position": 8,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 6,
        "processorCount": 2,
        "processorSpeedMhz": 1700,
        "processorType": "Intel(R) Xeon(R) Bronze 3104 CPU @ 1.70GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v2.00 (10/03/2018)",
        "serialNumber": "MXQ81103JS",
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
        "mpFirmwareVersion": "1.40 Oct 11 2018",
        "mpModel": "iLO5",
        "name": "MXQ748041X, bay 10",
        "partNumber": "871946-B21",
        "position": 10,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 6,
        "processorCount": 2,
        "processorSpeedMhz": 1700,
        "processorType": "Intel(R) Xeon(R) Bronze 3104 CPU @ 1.70GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v2.00 (10/03/2018)",
        "serialNumber": "MXQ750059N",
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
        "mpFirmwareVersion": "1.40 Oct 11 2018",
        "mpModel": "iLO5",
        "name": "MXQ748041X, bay 2",
        "partNumber": "871943-B21",
        "position": 2,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 16,
        "processorCount": 2,
        "processorSpeedMhz": 2100,
        "processorType": "Intel(R) Xeon(R) Gold 6130 CPU @ 2.10GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v2.00 (10/03/2018)",
        "serialNumber": "MXQ807050D",
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
        "mpFirmwareVersion": "1.40 Oct 11 2018",
        "mpModel": "iLO5",
        "name": "MXQ7480422, bay 7",
        "partNumber": "871946-B21",
        "position": 7,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 6,
        "processorCount": 2,
        "processorSpeedMhz": 1700,
        "processorType": "Intel(R) Xeon(R) Bronze 3104 CPU @ 1.70GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v2.00 (10/03/2018)",
        "serialNumber": "MXQ81103JJ",
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
        "mpFirmwareVersion": "1.40 Oct 11 2018",
        "mpModel": "iLO5",
        "name": "MXQ7480422, bay 9",
        "partNumber": "871946-B21",
        "position": 9,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 6,
        "processorCount": 2,
        "processorSpeedMhz": 1700,
        "processorType": "Intel(R) Xeon(R) Bronze 3104 CPU @ 1.70GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v2.00 (10/03/2018)",
        "serialNumber": "MXQ811045J",
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
        "mpFirmwareVersion": "1.40 Sep 27 2018",
        "mpModel": "iLO5",
        "name": "MXQ7480422, bay 8",
        "partNumber": "871946-B21",
        "position": 8,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 6,
        "processorCount": 2,
        "processorSpeedMhz": 1700,
        "processorType": "Intel(R) Xeon(R) Bronze 3104 CPU @ 1.70GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v2.00 (10/03/2018)",
        "serialNumber": "MXQ81103JN",
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
        "mpFirmwareVersion": "2.61 Jul 27 2018",
        "mpModel": "iLO4",
        "name": "MXQ7480422, bay 1",
        "partNumber": "826950-B21",
        "position": 1,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 14,
        "processorCount": 2,
        "processorSpeedMhz": 2400,
        "processorType": "Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v2.60 (05/21/2018)",
        "serialNumber": "MXQ80803KY",
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
        "mpFirmwareVersion": "1.40 Oct 11 2018",
        "mpModel": "iLO5",
        "name": "MXQ7480422, bay 2",
        "partNumber": "871943-B21",
        "position": 2,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 16,
        "processorCount": 2,
        "processorSpeedMhz": 2100,
        "processorType": "Intel(R) Xeon(R) Gold 6130 CPU @ 2.10GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v2.00 (10/03/2018)",
        "serialNumber": "MXQ8070509",
        "shortModel": "SY 480 Gen10",
        "state": "ProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    }
]

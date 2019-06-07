#!/usr/bin/env python

admin_credentials = {'userName': 'Administrator', 'password': 'Cosmos123'}
timeandlocale = {'localeDisplayName': 'English (United States)', 'locale': 'en_US.UTF-8',
                 'dateTime': '2018-08-09T19:29:17.073Z', 'ntpServers': [], 'timezone': 'UTC', 'type': 'TimeAndLocale'}
licenses = [
    {
        'key': 'QB9A DQEA H9PY 8HXY V2B4 HWWV Y9JL KMPL B89H MZVU DXAU 2CSM GHTG L762 6S74 ERB4 KJVT D5KM EFVW TSNJ YF4J 86CS SMT9 YGS6 SMQQ MUCF UW2L MYN7 N2QC DHKQ XJUL LUQH TU8F 3DQC SW7N VEQW V886 FE23 YWAT J8U3 2YT5 RNNV MHS3 QKTQ 688U F8A7 F8SE Z2DX RJQ6 MHPE SN9R 3UNK TVPT 74UF NGGT EHM4 "EVAL-N3R43A_ILR N3R43A_ILR Synergy_8Gb_FC_Upgrade_License EVAL-N3R43A_ILR"'
    },
    {
        'key': 'YBYE CQEA H9PA CHXZ V2B4 HWWV Y9JL KMPL LJ2A PGVQ DXAU 2CSM GHTG L762 2ET7 FQV9 KJVT D5KM EFVW TSNJ K4UP 536G SMT9 YGS6 SMQQ MUCF 4WCN MYN7 N2QS LHJQ XJUL LUQH TU8F 3DQC SW7N VEQW V886 FE23 YWAT J8U3 2YT5 RNNV MHS3 QKTQ 688U F8A7 F8SE Z2DX RJQ6 MHPE SN9R 3UNK TX83 T45F NGG3 EHM4 "EVAL-N3R43A_NFR N3R43A_NFR Synergy_8Gb_FC_Upgrade_License_NFR EVAL-N3R43A_NFR"'
    }
]

appliance = {'type': "ApplianceNetworkConfigurationV2",
             'applianceNetworks':
                 [{
                     "device": "bond0",
                     "macAddress": "9c:b6:54:97:ef:78",
                     "interfaceName": "Appliance",
                     "activeNode": 1,
                     "unconfigure": False,
                     "ipv4Type": "STATIC",
                     "ipv4Subnet": "255.255.0.0",
                     "ipv4Gateway": "10.131.0.1",
                     "ipv4NameServers": [u'10.120.0.10'],
                     "app1Ipv4Addr": "10.131.1.16",
                     "ipv6Type": "UNCONFIGURE",
                     "hostname": "T01.dom1131.lab",
                     "confOneNode": False,
                     "domainName": "dom1131.lab",
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
                "value": "10.120.1.30"
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
expected_san_managers = [
    {
        "uri": "SAN:10.120.1.30",
        "name": "10.120.1.30",
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
                "value": "10.120.1.30"
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
        "name": "Eth_1133",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1133
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "i3s-deploy",
        "privateNetwork": False,
        "purpose": "ISCSI",
        "smartLink": True,
        "vlanId": 2345
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
        "name": "i_1121",
        "privateNetwork": False,
        "purpose": "ISCSI",
        "smartLink": True,
        "vlanId": 1121
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "i_1122",
        "privateNetwork": False,
        "purpose": "ISCSI",
        "smartLink": True,
        "vlanId": 1122
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth",
        "privateNetwork": False,
        "purpose": "Management",
        "smartLink": True,
        "vlanId": 1131
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
        "name": "Eth_1134",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1134
    }
]
expected_ethernet_networks = [
    {
        "uri": "ETH:Eth_1133",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
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
        "uri": "ETH:i3s-deploy",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": "/rest/id-pools/ipv4/subnets/e06f523e-b53c-42ca-ab0c-1682fc6c4d85",
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "i3s-deploy",
        "privateNetwork": False,
        "purpose": "ISCSI",
        "smartLink": True,
        "vlanId": 2345
    },
    {
        "uri": "ETH:Eth_1132",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
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
        "uri": "ETH:i_1121",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "i_1121",
        "privateNetwork": False,
        "purpose": "ISCSI",
        "smartLink": True,
        "vlanId": 1121
    },
    {
        "uri": "ETH:i_1122",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "i_1122",
        "privateNetwork": False,
        "purpose": "ISCSI",
        "smartLink": True,
        "vlanId": 1122
    },
    {
        "uri": "ETH:Eth",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": "/rest/id-pools/ipv4/subnets/8ccc3b23-a775-4f27-9f65-2c11cddee21d",
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth",
        "privateNetwork": False,
        "purpose": "Management",
        "smartLink": True,
        "vlanId": 1131
    },
    {
        "uri": "ETH:Eth_1135",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
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
        "uri": "ETH:Eth_1134",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth_1134",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1134
    }
]

fc_networks = [
    {
        "type": "fc-networkV4",
        "name": "FC-1",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:T01-Fab1"
    },
    {
        "type": "fc-networkV4",
        "name": "FC-2",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:T01-Fab2"
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
        "managedSanUri": "FCSan:T01-Fab1"
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
        "managedSanUri": "FCSan:T01-Fab2"
    }
]

fcoenets = [
    {
        "name": "FCoE-1",
        "type": "fcoe-networkV4",
        "vlanId": 3501,
        "managedSanUri": "FCSan:VSAN3501"
    },
    {
        "name": "FCoE-2",
        "type": "fcoe-networkV4",
        "vlanId": 3502,
        "managedSanUri": "FCSan:VSAN3502"
    }
]
expected_fcoenets = [
    {
        "uri": "FCOE:FCoE-1",
        "state": "Active",
        "status": "OK",
        "name": "FCoE-1",
        "type": "fcoe-networkV4",
        "vlanId": 3501,
        "managedSanUri": "FCSan:VSAN3501"
    },
    {
        "uri": "FCOE:FCoE-2",
        "state": "Active",
        "status": "OK",
        "name": "FCoE-2",
        "type": "fcoe-networkV4",
        "vlanId": 3502,
        "managedSanUri": "FCSan:VSAN3502"
    }
]

networksets = [
]
expected_networksets = [
]

storage_systems_with_pools = [
    {
        "credentials": {'username': 'cosmos', 'password': 'Insight7'},
        "name": "tbr13par",
        "family": "StoreServ",
        "hostname": "10.120.1.7",
        "deviceSpecificAttributes": {
            "managedDomain": "T01",
            "managedPools": [{'domain': 'T01', 'name': 'FC-R5', 'raidLevel': 'RAID5', 'state': 'Managed', 'deviceType': 'FC', 'freeCapacity': '2551210573824', 'totalCapacity': '3474628542464', 'uuid': 'b3c7bd7d-1fdf-4d9d-b49e-5f2a22e5bb75'}],
            "discoveredPools": [],

        },
    },
    {
        "credentials": {'username': 'cosmos', 'password': 'Insight7'},
        "name": "HPE_3PAR_8200_ISCSI_EPIC",
        "family": "StoreServ",
        "hostname": "10.120.1.48",
        "deviceSpecificAttributes": {
            "managedDomain": "T01",
            "managedPools": [{'domain': 'T01', 'name': 'FC-R1', 'raidLevel': 'RAID1', 'state': 'Managed', 'deviceType': 'FC', 'freeCapacity': '66571993088', 'totalCapacity': '666793672704', 'uuid': 'f737d349-c709-4c28-9fe1-e06f7c14bbdd'}],
            "discoveredPools": [],

        }
    }
]
expected_storage_systems_with_pools = [
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
            "managedDomain": "T01",
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
            "managedDomain": "T01",
            "serialNumber": "2M271500PZ"
        }
    }
]

storage_pools_toedit = [
    {
        "storageSystemUri": "tbr13par",
        "name": "FC-R5",
        "isManaged": True,
    },
    {
        "storageSystemUri": "HPE_3PAR_8200_ISCSI_EPIC",
        "name": "FC-R1",
        "isManaged": True,
    }
]

storage_volume_templates = [
    {
        "name": "vol_temp",
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
                "default": "FC-R5",
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
                "default": "FC-R5",
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
                "default": 47244640256,
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
        "uri": "SVT:vol_temp",
        "status": "OK",
        "name": "vol_temp",
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
                "default": "SPOOL:FC-R5",
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
                "default": "SPOOL:FC-R5",
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
                "default": 47244640256,
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
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "win 2016",
            "provisioningType": "Thin",
            "size": 27917287424,
            "storagePool": "FC-R5"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "RHEL 7.4",
            "provisioningType": "Thin",
            "size": 24696061952,
            "storagePool": "FC-R5"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "22-1_vol22",
            "provisioningType": "Thin",
            "size": 32212254720,
            "storagePool": "FC-R5"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "22-3_vol23",
            "provisioningType": "Thin",
            "size": 37580963840,
            "storagePool": "FC-R5"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "win 2012 r2",
            "provisioningType": "Thin",
            "size": 42949672960,
            "storagePool": "FC-R5"
        },
    },
    {
        "templateUri": "ROOT",
        "isPermanent": True,
        "properties": {
            "description": "",
            "isShareable": True,
            "name": "postup_shared_vol",
            "provisioningType": "Thin",
            "size": 85899345920,
            "storagePool": "FC-R5"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "postup_priv_vol_edit",
            "provisioningType": "Thin",
            "size": 35433480192,
            "storagePool": "FC-R5"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "Test1",
            "provisioningType": "Thin",
            "size": 44023414784,
            "storagePool": "FC-R5"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "spt_vol",
            "provisioningType": "Thin",
            "size": 32212254720,
            "storagePool": "FC-R5"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "wiin 2016-fc",
            "provisioningType": "Thin",
            "size": 37580963840,
            "storagePool": "FC-R5"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "20-5",
            "provisioningType": "Thin",
            "size": 32212254720,
            "storagePool": "FC-R5"
        }
    }
]
expected_storage_volumes = [
    {
        "status": "OK",
        "uri": "SVOL:win 2016",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "win 2016",
            "provisioningType": "Thin",
            "size": 27917287424,
            "storagePoolUri": "SPOOL:FC-R5"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:RHEL 7.4",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "RHEL 7.4",
            "provisioningType": "Thin",
            "size": 24696061952,
            "storagePoolUri": "SPOOL:FC-R5"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:22-1_vol22",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "22-1_vol22",
            "provisioningType": "Thin",
            "size": 32212254720,
            "storagePoolUri": "SPOOL:FC-R5"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:22-3_vol23",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "22-3_vol23",
            "provisioningType": "Thin",
            "size": 37580963840,
            "storagePoolUri": "SPOOL:FC-R5"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:win 2012 r2",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "win 2012 r2",
            "provisioningType": "Thin",
            "size": 42949672960,
            "storagePoolUri": "SPOOL:FC-R5"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:postup_shared_vol",
        "isPermanent": True,
        "properties": {
            "description": "",
            "isShareable": True,
            "name": "postup_shared_vol",
            "provisioningType": "Thin",
            "size": 85899345920,
            "storagePoolUri": "SPOOL:FC-R5"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:postup_priv_vol_edit",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "postup_priv_vol_edit",
            "provisioningType": "Thin",
            "size": 35433480192,
            "storagePoolUri": "SPOOL:FC-R5"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:Test1",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "Test1",
            "provisioningType": "Thin",
            "size": 44023414784,
            "storagePoolUri": "SPOOL:FC-R5"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:spt_vol",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "spt_vol",
            "provisioningType": "Thin",
            "size": 32212254720,
            "storagePoolUri": "SPOOL:FC-R5"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:wiin 2016-fc",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "wiin 2016-fc",
            "provisioningType": "Thin",
            "size": 37580963840,
            "storagePoolUri": "SPOOL:FC-R5"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:20-5",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "20-5",
            "provisioningType": "Thin",
            "size": 32212254720,
            "storagePoolUri": "SPOOL:FC-R5"
        }
    }
]

sas_lig = [
    {
        "name": "LIG-Natasha",
        "type": "sas-logical-interconnect-groupV2",
        "enclosureType": "SY12000",
        "interconnectMapTemplate": [
            {
                "enclosureIndex": 1,
                "bay": 4,
                "enclosure": 1,
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
        "uplinkSets": [
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
                        "port": "1",
                        "enclosure": "-1",
                        "bay": "1"
                    }
                ],
                "mode": "Auto",
                "name": "F-1",
                "nativeNetworkUri": None,
                "networkType": "FibreChannel",
                "networkUris": [
                    "FC-1"
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
                        "bay": "4"
                    },
                    {
                        "speed": "Auto",
                        "port": "1",
                        "enclosure": "-1",
                        "bay": "4"
                    }
                ],
                "mode": "Auto",
                "name": "F-2",
                "nativeNetworkUri": None,
                "networkType": "FibreChannel",
                "networkUris": [
                    "FC-2"
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
        "name": "LIG-Potash3,6",
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
                "type": "Synergy 10Gb Interconnect Link Module"
            },
            {
                "enclosureIndex": 1,
                "bay": 3,
                "enclosure": 1,
                "type": "Virtual Connect SE 40Gb F8 Module for Synergy"
            },
            {
                "enclosureIndex": 3,
                "bay": 6,
                "enclosure": 3,
                "type": "Synergy 10Gb Interconnect Link Module"
            },
            {
                "enclosureIndex": 2,
                "bay": 6,
                "enclosure": 2,
                "type": "Virtual Connect SE 40Gb F8 Module for Synergy"
            },
            {
                "enclosureIndex": 2,
                "bay": 3,
                "enclosure": 2,
                "type": "Synergy 20Gb Interconnect Link Module"
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
                "ethernetNetworkType": "Tagged",
                "lacpTimer": "Short",
                "logicalPortConfigInfos": [
                    {
                        "speed": "Auto",
                        "port": "Q1",
                        "enclosure": "1",
                        "bay": "3"
                    },
                    {
                        "speed": "Auto",
                        "port": "Q1",
                        "enclosure": "2",
                        "bay": "6"
                    },
                    {
                        "speed": "Auto",
                        "enclosure": "1",
                        "port": "Q2",
                        "bay": "3"
                    },
                    {
                        "speed": "Auto",
                        "enclosure": "2",
                        "port": "Q2",
                        "bay": "6"
                    }
                ],
                "mode": "Auto",
                "name": "eth- 3,6",
                "nativeNetworkUri": None,
                "networkType": "Ethernet",
                "networkUris": [
                    "Eth_1134",
                    "Eth_1135",
                    "Eth_1132",
                    "Eth",
                    "Eth_1133"
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
                        "port": "Q3",
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
                "name": "FCoE-1",
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
                        "enclosure": "1",
                        "port": "Q5:1",
                        "bay": "3"
                    },
                    {
                        "speed": "Auto",
                        "enclosure": "1",
                        "port": "Q6:1",
                        "bay": "3"
                    }
                ],
                "mode": "Auto",
                "name": "F-1",
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
                        "enclosure": "2",
                        "port": "Q3",
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
                "name": "FCoE-2",
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
                        "enclosure": "2",
                        "port": "Q5:1",
                        "bay": "6"
                    },
                    {
                        "speed": "Auto",
                        "enclosure": "2",
                        "port": "Q6:1",
                        "bay": "6"
                    }
                ],
                "mode": "Auto",
                "name": "F-2",
                "nativeNetworkUri": None,
                "networkType": "FibreChannel",
                "networkUris": [
                    "FC-2"
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
        "name": "LIG-Potash 2,5",
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
                "bay": 5,
                "enclosure": 2,
                "type": "Synergy 20Gb Interconnect Link Module"
            },
            {
                "enclosureIndex": 1,
                "bay": 2,
                "enclosure": 1,
                "type": "Virtual Connect SE 40Gb F8 Module for Synergy"
            },
            {
                "enclosureIndex": 3,
                "bay": 2,
                "enclosure": 3,
                "type": "Synergy 20Gb Interconnect Link Module"
            },
            {
                "enclosureIndex": 1,
                "bay": 5,
                "enclosure": 1,
                "type": "Virtual Connect SE 40Gb F8 Module for Synergy"
            },
            {
                "enclosureIndex": 2,
                "bay": 2,
                "enclosure": 2,
                "type": "Synergy 20Gb Interconnect Link Module"
            },
            {
                "enclosureIndex": 3,
                "bay": 5,
                "enclosure": 3,
                "type": "Synergy 20Gb Interconnect Link Module"
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
                        "port": "Q1:3",
                        "enclosure": "1",
                        "bay": "5"
                    },
                    {
                        "speed": "Auto",
                        "enclosure": "1",
                        "port": "Q2:3",
                        "bay": "5"
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
            },
            {
                "ethernetNetworkType": "ImageStreamer",
                "lacpTimer": "Short",
                "logicalPortConfigInfos": [
                    {
                        "speed": "Auto",
                        "enclosure": "1",
                        "port": "Q5:1",
                        "bay": "5"
                    },
                    {
                        "speed": "Auto",
                        "enclosure": "1",
                        "port": "Q5.2",
                        "bay": "5"
                    },
                    {
                        "speed": "Auto",
                        "enclosure": "1",
                        "port": "Q5:1",
                        "bay": "2"
                    },
                    {
                        "speed": "Auto",
                        "port": "Q4.1",
                        "enclosure": "1",
                        "bay": "2"
                    }
                ],
                "mode": "Auto",
                "name": "i3s-deploy",
                "nativeNetworkUri": None,
                "networkType": "Ethernet",
                "networkUris": [
                    "i3s-deploy"
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
                        "port": "Q2:4",
                        "bay": "2"
                    },
                    {
                        "speed": "Auto",
                        "enclosure": "1",
                        "port": "Q1:4",
                        "bay": "2"
                    }
                ],
                "mode": "Auto",
                "name": "i-1",
                "nativeNetworkUri": None,
                "networkType": "Ethernet",
                "networkUris": [
                    "i_1121"
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
                        "port": "Q2:3",
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
                        "enclosure": "1",
                        "port": "Q1:4",
                        "bay": "5"
                    },
                    {
                        "speed": "Auto",
                        "enclosure": "1",
                        "port": "Q2:4",
                        "bay": "5"
                    }
                ],
                "mode": "Auto",
                "name": "i-2",
                "nativeNetworkUri": None,
                "networkType": "Ethernet",
                "networkUris": [
                    "i_1122"
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
                        "port": "Q3",
                        "bay": "5"
                    },
                    {
                        "speed": "Auto",
                        "enclosure": "1",
                        "port": "Q3",
                        "bay": "2"
                    }
                ],
                "mode": "Auto",
                "name": "eth-2/5",
                "nativeNetworkUri": None,
                "networkType": "Ethernet",
                "networkUris": [
                    "Eth_1134",
                    "Eth_1135",
                    "Eth_1132",
                    "Eth",
                    "Eth_1133"
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
        "uri": "LIG:LIG-Potash3,6",
        "status": None,
        "stackingHealth": None,
        "category": "logical-interconnect-groups",
        "state": "Active",
        "internalNetworkUris": "[]",
        "stackingMode": None,
        "description": None,
        "name": "LIG-Potash3,6",
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
        "uri": "LIG:LIG-Potash 2,5",
        "status": None,
        "stackingHealth": None,
        "category": "logical-interconnect-groups",
        "state": "Active",
        "internalNetworkUris": "[]",
        "stackingMode": None,
        "description": None,
        "name": "LIG-Potash 2,5",
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
        "enclosureIndexes": [1, 2, 3]
    }
]

encgroups_add = [
    {
        "name": "EG",
        "interconnectBayMappings": [
            {
                "interconnectBay": 1,
                "logicalInterconnectGroupUri": "SASLIG:LIG-Natasha",
                "enclosureIndex": 1
            },
            {
                "interconnectBay": 1,
                "logicalInterconnectGroupUri": "LIG:LIG-Carbon",
                "enclosureIndex": 3
            },
            {
                "interconnectBay": 2,
                "logicalInterconnectGroupUri": "LIG:LIG-Potash 2,5",

            },
            {
                "interconnectBay": 3,
                "logicalInterconnectGroupUri": "LIG:LIG-Potash3,6",

            },
            {
                "interconnectBay": 4,
                "logicalInterconnectGroupUri": "SASLIG:LIG-Natasha",
                "enclosureIndex": 1
            },
            {
                "interconnectBay": 4,
                "logicalInterconnectGroupUri": "LIG:LIG-Carbon",
                "enclosureIndex": 3
            },
            {
                "interconnectBay": 5,
                "logicalInterconnectGroupUri": "LIG:LIG-Potash 2,5",

            },
            {
                "interconnectBay": 6,
                "logicalInterconnectGroupUri": "LIG:LIG-Potash3,6",

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
        "associatedLogicalInterconnectGroups": [u'LIG:LIG-Carbon', u'LIG:LIG-Potash3,6', u'LIG:LIG-Potash 2,5', u'SASLIG:LIG-Natasha'],
        "name": "EG",
        "type": "EnclosureGroupV7",
        "enclosureTypeUri": "/rest/enclosure-types/SY12000",
        "stackingMode": "Enclosure",
        "name": "EG",
        "interconnectBayMappingCount": "8",
        "interconnectBayMappings": [
            {
                "interconnectBay": 1,
                "logicalInterconnectGroupUri": "SASLIG:LIG-Natasha",

            },
            {
                "interconnectBay": 1,
                "logicalInterconnectGroupUri": "LIG:LIG-Carbon",

            },
            {
                "interconnectBay": 2,
                "logicalInterconnectGroupUri": "LIG:LIG-Potash 2,5",

            },
            {
                "interconnectBay": 3,
                "logicalInterconnectGroupUri": "LIG:LIG-Potash3,6",

            },
            {
                "interconnectBay": 4,
                "logicalInterconnectGroupUri": "SASLIG:LIG-Natasha",

            },
            {
                "interconnectBay": 4,
                "logicalInterconnectGroupUri": "LIG:LIG-Carbon",

            },
            {
                "interconnectBay": 5,
                "logicalInterconnectGroupUri": "LIG:LIG-Potash 2,5",

            },
            {
                "interconnectBay": 6,
                "logicalInterconnectGroupUri": "LIG:LIG-Potash3,6",

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
            "ENC:CN751302CF",
            "ENC:CN75450620",
            "ENC:CN75450622"
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
            "ENC:CN751302CF",
            "ENC:CN75450620",
            "ENC:CN75450622"
        ],
        "enclosureGroupUri": "EG:EG"
    }
]

server_profile_templates = [
    {
        "name": "SY 480 Gen9 5",
        "type": "ServerProfileTemplateV6",
        "serverProfileDescription": "",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9 5:2:Synergy 3820C 10/20Gb CNA:3:Synergy 3820C 10/20Gb CNA",
        "enclosureGroupUri": "EG:EG",
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
                    "portId": "Mezz 2:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:Eth_1132",
                    "boot": {u'priority': u'NotBootable', u'bootVlanId': None},
                },
                {
                    "id": 2,
                    "name": "",
                    "functionType": "Ethernet",
                    "portId": "Mezz 2:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:Eth_1132",
                    "boot": {u'priority': u'NotBootable', u'bootVlanId': None},
                },
                {
                    "id": 3,
                    "name": "",
                    "functionType": "Ethernet",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:Eth_1133",
                    "boot": {u'priority': u'NotBootable', u'bootVlanId': None},
                },
                {
                    "id": 4,
                    "name": "",
                    "functionType": "Ethernet",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:Eth_1133",
                    "boot": {u'priority': u'NotBootable', u'bootVlanId': None},
                },
                {
                    "id": 5,
                    "name": "",
                    "functionType": "FibreChannel",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-1",
                    "boot": {u'priority': u'Primary', u'bootVlanId': None, u'bootVolumeSource': u'ManagedVolume'},
                },
                {
                    "id": 6,
                    "name": "",
                    "functionType": "FibreChannel",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-2",
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
            "mode": "UEFI"
        },
        "firmware": {
            "manageFirmware": False,
            "forceInstallFirmware": False
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": [{u'id': u'DaylightSavingsTime', u'value': u'Enabled'}, {u'id': u'TimeZone', u'value': u'UtcM6'}]
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
                    "volumeUri": "SVOL:postup_shared_vol",
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
                        }
                    ],
                },
                {
                    "id": 2,
                    "volumeUri": "None",
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
                        }
                    ],
                },
            ]

        },
    }
]
expected_server_profile_templates = [
    {
        "uri": "SPT:SY 480 Gen9 5",
        "status": "OK",
        "name": "SY 480 Gen9 5",
        "type": "ServerProfileTemplateV6",
        "serverProfileDescription": "",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9 5:2:Synergy 3820C 10/20Gb CNA:3:Synergy 3820C 10/20Gb CNA",
        "enclosureGroupUri": "EG:EG",
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
                    "portId": "Mezz 2:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:Eth_1132",
                    "boot": {u'priority': u'NotBootable', u'bootVlanId': None},
                },
                {
                    "id": 2,
                    "name": "",
                    "functionType": "Ethernet",
                    "portId": "Mezz 2:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:Eth_1132",
                    "boot": {u'priority': u'NotBootable', u'bootVlanId': None},
                },
                {
                    "id": 3,
                    "name": "",
                    "functionType": "Ethernet",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:Eth_1133",
                    "boot": {u'priority': u'NotBootable', u'bootVlanId': None},
                },
                {
                    "id": 4,
                    "name": "",
                    "functionType": "Ethernet",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:Eth_1133",
                    "boot": {u'priority': u'NotBootable', u'bootVlanId': None},
                },
                {
                    "id": 5,
                    "name": "",
                    "functionType": "FibreChannel",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-1",
                    "boot": {u'priority': u'Primary', u'bootVlanId': None, u'bootVolumeSource': u'ManagedVolume'},
                },
                {
                    "id": 6,
                    "name": "",
                    "functionType": "FibreChannel",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:FC-2",
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
            "mode": "UEFI"
        },
        "firmware": {
            "manageFirmware": False,
            "forceInstallFirmware": False
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": [{u'id': u'DaylightSavingsTime', u'value': u'Enabled'}, {u'id': u'TimeZone', u'value': u'UtcM6'}]
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
                    "volumeUri": "SVOL:postup_shared_vol",
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
                        }
                    ],
                },
                {
                    "id": 2,
                    "volumeUri": "None",
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
                        }
                    ],
                },
            ]

        },
    }
]

server_profiles_from_spt = [
    {
        "serverProfileTemplateUri": "SPT:SY 480 Gen9 5",
        "name": "22-2",
        "type": "ServerProfileV10",
        "serverHardwareUri": "CN75450622, bay 2",
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
                    "portId": "Mezz 2:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1132",
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
                    "portId": "Mezz 2:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1132",
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
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1133",
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
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1133",
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
                    "wwnn": "10:00:a6:5e:00:d0:00:17",
                    "wwpn": "10:00:a6:5e:00:d0:00:16",
                    "networkUri": "FC:FC-1",
                    "boot": {u'priority': u'Primary', u'bootVolumeSource': u'ManagedVolume', u'targets': [{u'lun': u'1', u'arrayWwpn': u'21110002AC00C312'}]},
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
                    "wwnn": "10:00:a6:5e:00:d0:00:19",
                    "wwpn": "10:00:a6:5e:00:d0:00:18",
                    "networkUri": "FC:FC-2",
                    "boot": {u'priority': u'Secondary', u'bootVolumeSource': u'ManagedVolume', u'targets': [{u'lun': u'1', u'arrayWwpn': u'20120002AC00C312'}]},
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
            "manageBios": True,
            "overriddenSettings": [{u'id': u'DaylightSavingsTime', u'value': u'Enabled'}, {u'id': u'TimeZone', u'value': u'UtcM6'}]
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
                    "volumeUri": "SVOL:postup_shared_vol",
                    "bootVolumePriority": "NotBootable",
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
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:spt_vol",
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
expected_server_profiles_from_spt = [
    {
        "uri": "SP:22-2",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9 5:2:Synergy 3820C 10/20Gb CNA:3:Synergy 3820C 10/20Gb CNA",
        "name": "22-2",
        "type": "ServerProfileV10",
        "serverHardwareUri": "CN75450622, bay 2",
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
                    "portId": "Mezz 2:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1132",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 2:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1132",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1133",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1133",
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
                    "wwnn": "10:00:a6:5e:00:d0:00:17",
                    "wwpn": "10:00:a6:5e:00:d0:00:16",
                    "networkUri": "FC:FC-1",
                    "boot": {u'priority': u'Primary', u'bootVolumeSource': u'ManagedVolume', u'targets': [{u'lun': u'1', u'arrayWwpn': u'21110002AC00C312'}]},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 6,
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "wwnn": "10:00:a6:5e:00:d0:00:19",
                    "wwpn": "10:00:a6:5e:00:d0:00:18",
                    "networkUri": "FC:FC-2",
                    "boot": {u'priority': u'Secondary', u'bootVolumeSource': u'ManagedVolume', u'targets': [{u'lun': u'1', u'arrayWwpn': u'20120002AC00C312'}]},
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
            "manageBios": True,
            "overriddenSettings": [{u'id': u'DaylightSavingsTime', u'value': u'Enabled'}, {u'id': u'TimeZone', u'value': u'UtcM6'}]
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
                    "volumeUri": "SVOL:postup_shared_vol",
                    "bootVolumePriority": "NotBootable",
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
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:spt_vol",
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

server_profiles = [
    {
        "name": "22-8",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:CN75450622, bay 8",
        "enclosureGroupUri": "EG:EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "i3s- esxi",
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
                    "name": "Deployment Network A",
                    "portId": "Mezz 2:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:i3s-deploy",
                    "boot": {u'priority': u'Primary', u'iscsi': {u'chapLevel': u'None', u'initiatorName': u'iqn.2015-02.com.hpe:oneview-vcg3d90005', u'secondBootTargetPort': u'', u'secondBootTargetIp': u'', u'initiatorNameSource': u'ProfileInitiatorName'}, u'ethernetBootType': u'iSCSI', u'bootVolumeSource': u'UserDefined'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "Deployment Network B",
                    "portId": "Mezz 2:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:i3s-deploy",
                    "boot": {u'priority': u'Secondary', u'iscsi': {u'chapLevel': u'None', u'initiatorName': u'iqn.2015-02.com.hpe:oneview-vcg3d90005', u'secondBootTargetPort': u'', u'secondBootTargetIp': u'', u'initiatorNameSource': u'ProfileInitiatorName'}, u'ethernetBootType': u'iSCSI', u'bootVolumeSource': u'UserDefined'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 2:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1132",
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
                    "portId": "Mezz 2:2-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1132",
                    "boot": {u'priority': u'NotBootable'},
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
        "name": "CF-2",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:CN751302CF, bay 2",
        "enclosureGroupUri": "EG:EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "SLES 12 sp3- BIg bird",
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
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1132",
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
                    "portId": "Mezz 3:2-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1132",
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
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1133",
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
                    "portId": "Mezz 3:2-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1133",
                    "boot": {u'priority': u'NotBootable'},
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
            "sasLogicalJBODs": [{u'deviceSlot': u'Mezz 1', u'status': u'OK', u'driveMinSizeGB': 146, u'description': None, u'driveMaxSizeGB': 146, u'persistent': False, u'eraseData': False, u'driveTechnology': u'SasHdd', u'numPhysicalDrives': 1, u'id': 1, u'name': u'LD-1'}],
            "controllers": [{u'deviceSlot': u'Mezz 1', u'predictiveSpareRebuild': u'Unmanaged', u'importConfiguration': False, u'mode': u'RAID', u'driveWriteCache': u'Unmanaged', u'initialize': False, u'logicalDrives': [{u'name': None, u'accelerator': u'Unmanaged', u'bootable': True, u'raidLevel': u'RAID0', u'sasLogicalJBODId': 1, u'driveTechnology': None, u'numSpareDrives': None, u'numPhysicalDrives': None}]}]
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
        "uri": "SP:22-8",
        "state": "UpdateFailed",
        "status": "Critical",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9 6:2:Synergy 2820C 10Gb CNA",
        "name": "22-8",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:CN75450622, bay 8",
        "enclosureGroupUri": "EG:EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "i3s- esxi",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "Deployment Network A",
                    "portId": "Mezz 2:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:i3s-deploy",
                    "boot": {u'priority': u'Primary', u'iscsi': {u'chapLevel': u'None', u'initiatorName': u'iqn.2015-02.com.hpe:oneview-vcg3d90005', u'secondBootTargetPort': u'', u'secondBootTargetIp': u'', u'initiatorNameSource': u'ProfileInitiatorName'}, u'ethernetBootType': u'iSCSI', u'bootVolumeSource': u'UserDefined'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "Deployment Network B",
                    "portId": "Mezz 2:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:i3s-deploy",
                    "boot": {u'priority': u'Secondary', u'iscsi': {u'chapLevel': u'None', u'initiatorName': u'iqn.2015-02.com.hpe:oneview-vcg3d90005', u'secondBootTargetPort': u'', u'secondBootTargetIp': u'', u'initiatorNameSource': u'ProfileInitiatorName'}, u'ethernetBootType': u'iSCSI', u'bootVolumeSource': u'UserDefined'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 2:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1132",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 2:2-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1132",
                    "boot": {u'priority': u'NotBootable'},
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
        "uri": "SP:CF-2",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9 4:1:Smart Array P542D Controller:3:Synergy 3820C 10/20Gb CNA",
        "name": "CF-2",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:CN751302CF, bay 2",
        "enclosureGroupUri": "EG:EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "SLES 12 sp3- BIg bird",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1132",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:2-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1132",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1133",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:2-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1133",
                    "boot": {u'priority': u'NotBootable'},
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
            "sasLogicalJBODs": [{u'deviceSlot': u'Mezz 1', u'status': u'OK', u'driveMinSizeGB': 146, u'description': None, u'driveMaxSizeGB': 146, u'persistent': False, u'eraseData': False, u'driveTechnology': u'SasHdd', u'numPhysicalDrives': 1, u'id': 1, u'name': u'LD-1'}],
            "controllers": [{u'deviceSlot': u'Mezz 1', u'predictiveSpareRebuild': u'Unmanaged', u'importConfiguration': False, u'mode': u'RAID', u'driveWriteCache': u'Unmanaged', u'initialize': False, u'logicalDrives': [{u'name': None, u'accelerator': u'Unmanaged', u'bootable': True, u'raidLevel': u'RAID0', u'sasLogicalJBODId': 1, u'driveTechnology': None, u'numSpareDrives': None, u'numPhysicalDrives': None}]}]
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
        "name": "22-1",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:CN75450622, bay 1",
        "enclosureUri": "ENC:CN75450622",
        "enclosureGroupUri": "EG:EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "esxi-6.5u2",
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
                    "portId": "Mezz 2:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1132",
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
                    "portId": "Mezz 2:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1132",
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
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1133",
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
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1133",
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
                    "portId": "Mezz 2:1-b",
                    "requestedMbps": "2500",
                    "wwnn": "10:00:a6:5e:00:d0:00:09",
                    "wwpn": "10:00:a6:5e:00:d0:00:08",
                    "networkUri": "FCOE:FCoE-1",
                    "boot": {u'priority': u'Primary', u'bootVolumeSource': u'ManagedVolume', u'targets': [{u'lun': u'1', u'arrayWwpn': u'20210002AC00C312'}]},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 6,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 2:2-b",
                    "requestedMbps": "2500",
                    "wwnn": "10:00:a6:5e:00:d0:00:0b",
                    "wwpn": "10:00:a6:5e:00:d0:00:0a",
                    "networkUri": "FCOE:FCoE-2",
                    "boot": {u'priority': u'Secondary', u'bootVolumeSource': u'ManagedVolume', u'targets': [{u'lun': u'1', u'arrayWwpn': u'20220002AC00C312'}]},
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
                    "volumeUri": "SVOL:22-1_vol22",
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
        "name": "CF-3",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:CN751302CF, bay 3",
        "enclosureUri": "ENC:CN751302CF",
        "enclosureGroupUri": "EG:EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "RHEL 7.4",
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
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1132",
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
                    "portId": "Mezz 3:2-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1132",
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
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1133",
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
                    "portId": "Mezz 3:2-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1133",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 5,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 20000,
                    "name": "FCoE-1",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": "10:00:a6:5e:00:d0:00:01",
                    "wwpn": "10:00:a6:5e:00:d0:00:00",
                    "networkUri": "FCOE:FCoE-1",
                    "boot": {u'priority': u'Primary', u'bootVolumeSource': u'ManagedVolume', u'targets': [{u'lun': u'1', u'arrayWwpn': u'21210002AC00C312'}]},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 6,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 20000,
                    "name": "fcoe-2",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "wwnn": "10:00:a6:5e:00:d0:00:03",
                    "wwpn": "10:00:a6:5e:00:d0:00:02",
                    "networkUri": "FCOE:FCoE-2",
                    "boot": {u'priority': u'Secondary', u'bootVolumeSource': u'ManagedVolume', u'targets': [{u'lun': u'1', u'arrayWwpn': u'21220002AC00C312'}]},
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
                    "volumeUri": "SVOL:win 2016",
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
    },
    {
        "name": "CF-1",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:CN751302CF, bay 1",
        "enclosureUri": "ENC:CN751302CF",
        "enclosureGroupUri": "EG:EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "win 2016",
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
                    "networkUri": "ETH:Eth_1132",
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
                    "networkUri": "ETH:Eth_1132",
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
                    "networkUri": "ETH:Eth_1133",
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
                    "networkUri": "ETH:Eth_1133",
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
                    "wwnn": "10:00:a6:5e:00:d0:00:1f",
                    "wwpn": "10:00:a6:5e:00:d0:00:1e",
                    "networkUri": "FC:FC-1",
                    "boot": {u'priority': u'Primary', u'bootVolumeSource': u'ManagedVolume', u'targets': [{u'lun': u'1', u'arrayWwpn': u'20110002AC00C312'}]},
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
                    "wwnn": "10:00:a6:5e:00:d0:00:21",
                    "wwpn": "10:00:a6:5e:00:d0:00:20",
                    "networkUri": "FC:FC-2",
                    "boot": {u'priority': u'Secondary', u'bootVolumeSource': u'ManagedVolume', u'targets': [{u'lun': u'1', u'arrayWwpn': u'20120002AC00C312'}]},
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
                    "volumeUri": "SVOL:wiin 2016-fc",
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
        "name": "CF-8",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:CN751302CF, bay 8",
        "enclosureUri": "ENC:CN751302CF",
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
                    "networkUri": "ETH:Eth_1132",
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
                    "networkUri": "ETH:Eth_1132",
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
                    "networkUri": "ETH:Eth_1133",
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
                    "networkUri": "ETH:Eth_1133",
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
                    "wwnn": "10:00:a6:5e:00:d0:00:1b",
                    "wwpn": "10:00:a6:5e:00:d0:00:1a",
                    "networkUri": "FCOE:FCoE-1",
                    "boot": {u'priority': u'Primary', u'bootVolumeSource': u'ManagedVolume', u'targets': [{u'lun': u'1', u'arrayWwpn': u'20210002AC00C312'}]},
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
                    "wwnn": "10:00:a6:5e:00:d0:00:1d",
                    "wwpn": "10:00:a6:5e:00:d0:00:1c",
                    "networkUri": "FCOE:FCoE-2",
                    "boot": {u'priority': u'Secondary', u'bootVolumeSource': u'ManagedVolume', u'targets': [{u'lun': u'1', u'arrayWwpn': u'20220002AC00C312'}]},
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
                    "volumeUri": "SVOL:postup_priv_vol_edit",
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
        "name": "22-3",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:CN75450622, bay 3",
        "enclosureUri": "ENC:CN75450622",
        "enclosureGroupUri": "EG:EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "SLES 12 Sp3",
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
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1132",
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
                    "portId": "Mezz 3:2-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1132",
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
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1133",
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
                    "portId": "Mezz 3:2-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1133",
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
                    "wwnn": "10:00:a6:5e:00:d0:00:0d",
                    "wwpn": "10:00:a6:5e:00:d0:00:0c",
                    "networkUri": "FC:FC-1",
                    "boot": {u'priority': u'Primary', u'bootVolumeSource': u'ManagedVolume', u'targets': [{u'lun': u'1', u'arrayWwpn': u'21110002AC00C312'}]},
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
                    "wwnn": "10:00:a6:5e:00:d0:00:0f",
                    "wwpn": "10:00:a6:5e:00:d0:00:0e",
                    "networkUri": "FC:FC-2",
                    "boot": {u'priority': u'Secondary', u'bootVolumeSource': u'ManagedVolume', u'targets': [{u'lun': u'1', u'arrayWwpn': u'21120002AC00C312'}]},
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
                    "volumeUri": "SVOL:22-3_vol23",
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
        "name": "20-8",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:CN75450620, bay 8",
        "enclosureUri": "ENC:CN75450620",
        "enclosureGroupUri": "EG:EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "win 2012 r2",
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
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1132",
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
                    "portId": "Mezz 3:2-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1132",
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
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1133",
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
                    "networkUri": "ETH:Eth_1133",
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
                    "wwnn": "10:00:a6:5e:00:d0:00:11",
                    "wwpn": "10:00:a6:5e:00:d0:00:10",
                    "networkUri": "FC:FC-1",
                    "boot": {u'priority': u'Primary', u'bootVolumeSource': u'ManagedVolume', u'targets': [{u'lun': u'1', u'arrayWwpn': u'20110002AC00C312'}, {u'lun': u'1', u'arrayWwpn': u'21110002AC00C312'}]},
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
                    "requestedMbps": "Auto",
                    "wwnn": "10:00:a6:5e:00:d0:00:15",
                    "wwpn": "10:00:a6:5e:00:d0:00:14",
                    "networkUri": "FC:FC-2",
                    "boot": {u'priority': u'Secondary', u'bootVolumeSource': u'ManagedVolume', u'targets': [{u'lun': u'1', u'arrayWwpn': u'21120002AC00C312'}, {u'lun': u'1', u'arrayWwpn': u'20120002AC00C312'}]},
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
                    "volumeUri": "SVOL:win 2012 r2",
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
        "name": "20-6",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:CN75450620, bay 6",
        "enclosureUri": "ENC:CN75450620",
        "enclosureGroupUri": "EG:EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "win 2016",
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
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1132",
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
                    "portId": "Mezz 3:2-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1132",
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
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1133",
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
                    "networkUri": "ETH:Eth_1133",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 5,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 16000,
                    "name": "f1",
                    "portId": "Mezz 1:1",
                    "requestedMbps": "Auto",
                    "wwnn": "10:00:a6:5e:00:d0:00:05",
                    "wwpn": "10:00:a6:5e:00:d0:00:04",
                    "networkUri": "FC:FC-1",
                    "boot": {u'priority': u'Primary', u'bootVolumeSource': u'ManagedVolume', u'targets': [{u'lun': u'1', u'arrayWwpn': u'20110002AC00C312'}]},
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
                    "requestedMbps": "Auto",
                    "wwnn": "10:00:a6:5e:00:d0:00:07",
                    "wwpn": "10:00:a6:5e:00:d0:00:06",
                    "networkUri": "FC:FC-2",
                    "boot": {u'priority': u'Secondary', u'bootVolumeSource': u'ManagedVolume', u'targets': [{u'lun': u'1', u'arrayWwpn': u'20120002AC00C312'}]},
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
            "hostOSType": "RHE Virtualization 7.x",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:RHEL 7.4",
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
    }
]
expected_server_profile_with_storage = [
    {
        "uri": "SP:22-1",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9 5:2:Synergy 3820C 10/20Gb CNA:3:Synergy 3820C 10/20Gb CNA",
        "name": "22-1",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:CN75450622, bay 1",
        "enclosureUri": "ENC:CN75450622",
        "enclosureGroupUri": "EG:EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "esxi-6.5u2",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 2:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1132",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 2:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1132",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1133",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1133",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 5,
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 2:1-b",
                    "requestedMbps": "2500",
                    "wwnn": "10:00:a6:5e:00:d0:00:09",
                    "wwpn": "10:00:a6:5e:00:d0:00:08",
                    "networkUri": "FCOE:FCoE-1",
                    "boot": {u'priority': u'Primary', u'bootVolumeSource': u'ManagedVolume', u'targets': [{u'lun': u'1', u'arrayWwpn': u'20210002AC00C312'}]},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 6,
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 2:2-b",
                    "requestedMbps": "2500",
                    "wwnn": "10:00:a6:5e:00:d0:00:0b",
                    "wwpn": "10:00:a6:5e:00:d0:00:0a",
                    "networkUri": "FCOE:FCoE-2",
                    "boot": {u'priority': u'Secondary', u'bootVolumeSource': u'ManagedVolume', u'targets': [{u'lun': u'1', u'arrayWwpn': u'20220002AC00C312'}]},
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
                    "volumeUri": "SVOL:22-1_vol22",
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
        "uri": "SP:CF-3",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9 1:3:Synergy 3820C 10/20Gb CNA",
        "name": "CF-3",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:CN751302CF, bay 3",
        "enclosureUri": "ENC:CN751302CF",
        "enclosureGroupUri": "EG:EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "RHEL 7.4",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1132",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:2-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1132",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1133",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:2-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1133",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 5,
                    "maximumMbps": 20000,
                    "name": "FCoE-1",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "wwnn": "10:00:a6:5e:00:d0:00:01",
                    "wwpn": "10:00:a6:5e:00:d0:00:00",
                    "networkUri": "FCOE:FCoE-1",
                    "boot": {u'priority': u'Primary', u'bootVolumeSource': u'ManagedVolume', u'targets': [{u'lun': u'1', u'arrayWwpn': u'21210002AC00C312'}]},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 6,
                    "maximumMbps": 20000,
                    "name": "fcoe-2",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "wwnn": "10:00:a6:5e:00:d0:00:03",
                    "wwpn": "10:00:a6:5e:00:d0:00:02",
                    "networkUri": "FCOE:FCoE-2",
                    "boot": {u'priority': u'Secondary', u'bootVolumeSource': u'ManagedVolume', u'targets': [{u'lun': u'1', u'arrayWwpn': u'21220002AC00C312'}]},
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
                    "volumeUri": "SVOL:win 2016",
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
    },
    {
        "uri": "SP:CF-1",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen10 1:1:HPE Smart Array P416ie-m SR G10:3:Synergy 3820C 10/20Gb CNA",
        "name": "CF-1",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:CN751302CF, bay 1",
        "enclosureUri": "ENC:CN751302CF",
        "enclosureGroupUri": "EG:EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "win 2016",
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
                    "networkUri": "ETH:Eth_1132",
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
                    "networkUri": "ETH:Eth_1132",
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
                    "networkUri": "ETH:Eth_1133",
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
                    "networkUri": "ETH:Eth_1133",
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
                    "wwnn": "10:00:a6:5e:00:d0:00:1f",
                    "wwpn": "10:00:a6:5e:00:d0:00:1e",
                    "networkUri": "FC:FC-1",
                    "boot": {u'priority': u'Primary', u'bootVolumeSource': u'ManagedVolume', u'targets': [{u'lun': u'1', u'arrayWwpn': u'20110002AC00C312'}]},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 6,
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "wwnn": "10:00:a6:5e:00:d0:00:21",
                    "wwpn": "10:00:a6:5e:00:d0:00:20",
                    "networkUri": "FC:FC-2",
                    "boot": {u'priority': u'Secondary', u'bootVolumeSource': u'ManagedVolume', u'targets': [{u'lun': u'1', u'arrayWwpn': u'20120002AC00C312'}]},
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
                    "volumeUri": "SVOL:wiin 2016-fc",
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
        "uri": "SP:CF-8",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen10 1:1:HPE Smart Array P416ie-m SR G10:3:Synergy 3820C 10/20Gb CNA",
        "name": "CF-8",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:CN751302CF, bay 8",
        "enclosureUri": "ENC:CN751302CF",
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
                    "networkUri": "ETH:Eth_1132",
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
                    "networkUri": "ETH:Eth_1132",
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
                    "networkUri": "ETH:Eth_1133",
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
                    "networkUri": "ETH:Eth_1133",
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
                    "wwnn": "10:00:a6:5e:00:d0:00:1b",
                    "wwpn": "10:00:a6:5e:00:d0:00:1a",
                    "networkUri": "FCOE:FCoE-1",
                    "boot": {u'priority': u'Primary', u'bootVolumeSource': u'ManagedVolume', u'targets': [{u'lun': u'1', u'arrayWwpn': u'20210002AC00C312'}]},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 6,
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "wwnn": "10:00:a6:5e:00:d0:00:1d",
                    "wwpn": "10:00:a6:5e:00:d0:00:1c",
                    "networkUri": "FCOE:FCoE-2",
                    "boot": {u'priority': u'Secondary', u'bootVolumeSource': u'ManagedVolume', u'targets': [{u'lun': u'1', u'arrayWwpn': u'20220002AC00C312'}]},
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
                    "volumeUri": "SVOL:postup_priv_vol_edit",
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
        "uri": "SP:22-3",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen10 3:3:Synergy 3820C 10/20Gb CNA",
        "name": "22-3",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:CN75450622, bay 3",
        "enclosureUri": "ENC:CN75450622",
        "enclosureGroupUri": "EG:EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "SLES 12 Sp3",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1132",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:2-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1132",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1133",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 4,
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:2-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1133",
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
                    "wwnn": "10:00:a6:5e:00:d0:00:0d",
                    "wwpn": "10:00:a6:5e:00:d0:00:0c",
                    "networkUri": "FC:FC-1",
                    "boot": {u'priority': u'Primary', u'bootVolumeSource': u'ManagedVolume', u'targets': [{u'lun': u'1', u'arrayWwpn': u'21110002AC00C312'}]},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 6,
                    "maximumMbps": 20000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "wwnn": "10:00:a6:5e:00:d0:00:0f",
                    "wwpn": "10:00:a6:5e:00:d0:00:0e",
                    "networkUri": "FC:FC-2",
                    "boot": {u'priority': u'Secondary', u'bootVolumeSource': u'ManagedVolume', u'targets': [{u'lun': u'1', u'arrayWwpn': u'21120002AC00C312'}]},
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
                    "volumeUri": "SVOL:22-3_vol23",
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
        "uri": "SP:20-8",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen10 2:1:Synergy 3830C 16G FC HBA:3:Synergy 3820C 10/20Gb CNA",
        "name": "20-8",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:CN75450620, bay 8",
        "enclosureUri": "ENC:CN75450620",
        "enclosureGroupUri": "EG:EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "win 2012 r2",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1132",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1132",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1133",
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
                    "networkUri": "ETH:Eth_1133",
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
                    "wwnn": "10:00:a6:5e:00:d0:00:11",
                    "wwpn": "10:00:a6:5e:00:d0:00:10",
                    "networkUri": "FC:FC-1",
                    "boot": {u'priority': u'Primary', u'bootVolumeSource': u'ManagedVolume', u'targets': [{u'lun': u'1', u'arrayWwpn': u'20110002AC00C312'}, {u'lun': u'1', u'arrayWwpn': u'21110002AC00C312'}]},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 6,
                    "maximumMbps": 16000,
                    "name": "",
                    "portId": "Mezz 1:2",
                    "requestedMbps": "Auto",
                    "wwnn": "10:00:a6:5e:00:d0:00:15",
                    "wwpn": "10:00:a6:5e:00:d0:00:14",
                    "networkUri": "FC:FC-2",
                    "boot": {u'priority': u'Secondary', u'bootVolumeSource': u'ManagedVolume', u'targets': [{u'lun': u'1', u'arrayWwpn': u'21120002AC00C312'}, {u'lun': u'1', u'arrayWwpn': u'20120002AC00C312'}]},
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
                    "volumeUri": "SVOL:win 2012 r2",
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
        "uri": "SP:20-6",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 660 Gen9 2:1:Synergy 3530C 16G HBA:3:Synergy 3820C 10/20Gb CNA:4:Synergy 3830C 16G FC HBA:6:Synergy 3820C 10/20Gb CNA",
        "name": "20-6",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:CN75450620, bay 6",
        "enclosureUri": "ENC:CN75450620",
        "enclosureGroupUri": "EG:EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "win 2016",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1132",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1132",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1133",
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
                    "networkUri": "ETH:Eth_1133",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 5,
                    "maximumMbps": 16000,
                    "name": "f1",
                    "portId": "Mezz 1:1",
                    "requestedMbps": "Auto",
                    "wwnn": "10:00:a6:5e:00:d0:00:05",
                    "wwpn": "10:00:a6:5e:00:d0:00:04",
                    "networkUri": "FC:FC-1",
                    "boot": {u'priority': u'Primary', u'bootVolumeSource': u'ManagedVolume', u'targets': [{u'lun': u'1', u'arrayWwpn': u'20110002AC00C312'}]},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 6,
                    "maximumMbps": 16000,
                    "name": "",
                    "portId": "Mezz 1:2",
                    "requestedMbps": "Auto",
                    "wwnn": "10:00:a6:5e:00:d0:00:07",
                    "wwpn": "10:00:a6:5e:00:d0:00:06",
                    "networkUri": "FC:FC-2",
                    "boot": {u'priority': u'Secondary', u'bootVolumeSource': u'ManagedVolume', u'targets': [{u'lun': u'1', u'arrayWwpn': u'20120002AC00C312'}]},
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
            "hostOSType": "RHE Virtualization 7.x",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:RHEL 7.4",
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
    }
]

configured_enclosures = [
    {
        "name": "CN75450622",
        "state": "Configured",
        "serialNumber": "CN75450622",
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
        "name": "CN751302CF",
        "state": "Configured",
        "serialNumber": "CN751302CF",
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
                "devicePresence": "Subsumed"
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
        "name": "CN75450620",
        "state": "Configured",
        "serialNumber": "CN75450620",
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

servers = [
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 65536,
        "model": "Synergy 480 Gen9",
        "mpFirmwareVersion": "2.60 May 23 2018",
        "mpModel": "iLO4",
        "name": "CN75450620, bay 4",
        "partNumber": "732350-B21",
        "position": 4,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 14,
        "processorCount": 2,
        "processorSpeedMhz": 2000,
        "processorType": "Intel(R) Xeon(R) CPU E5-2660 v4 @ 2.00GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v2.60 (05/21/2018)",
        "serialNumber": "MXQ72003RL",
        "shortModel": "SY 480 Gen9",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "FullHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 16384,
        "model": "Synergy 660 Gen9",
        "mpFirmwareVersion": "2.55 Aug 16 2017",
        "mpModel": "iLO4",
        "name": "CN751302CF, bay 6",
        "partNumber": "777072-001",
        "position": 6,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 10,
        "processorCount": 2,
        "processorSpeedMhz": 1700,
        "processorType": "Intel(R) Xeon(R) CPU E5-4610 v3 @ 1.70GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I39 v2.60 (05/21/2018)",
        "serialNumber": "CN754606X0",
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
        "model": "Synergy 480 Gen10",
        "mpFirmwareVersion": "1.22 Mar 06 2018",
        "mpModel": "iLO5",
        "name": "CN75450620, bay 8",
        "partNumber": "871946-B21",
        "position": 8,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 6,
        "processorCount": 2,
        "processorSpeedMhz": 1700,
        "processorType": "Intel(R) Xeon(R) Bronze 3104 CPU @ 1.70GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v1.36 (02/14/2018)",
        "serialNumber": "MXQ749058X",
        "shortModel": "SY 480 Gen10",
        "state": "ProfileApplied",
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
        "name": "CN75450620, bay 6",
        "partNumber": "826958-B21",
        "position": 6,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 10,
        "processorCount": 2,
        "processorSpeedMhz": 1800,
        "processorType": "Intel(R) Xeon(R) CPU E5-4610 v4 @ 1.80GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I39 v2.60 (05/21/2018)",
        "serialNumber": "MXQ733085N",
        "shortModel": "SY 660 Gen9",
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
        "name": "CN751302CF, bay 1",
        "partNumber": "871946-B21",
        "position": 1,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 6,
        "processorCount": 2,
        "processorSpeedMhz": 1700,
        "processorType": "Intel(R) Xeon(R) Bronze 3104 CPU @ 1.70GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v1.36 (02/14/2018)",
        "serialNumber": "MXQ750059J",
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
        "model": "Synergy 480 Gen9",
        "mpFirmwareVersion": "2.55 Aug 16 2017",
        "mpModel": "iLO4",
        "name": "CN751302CF, bay 3",
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
        "serialNumber": "CN754606ZD",
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
        "model": "Synergy 480 Gen9",
        "mpFirmwareVersion": "2.55 Aug 16 2017",
        "mpModel": "iLO4",
        "name": "CN751302CF, bay 4",
        "partNumber": "754683-001",
        "position": 4,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 16,
        "processorCount": 2,
        "processorSpeedMhz": 2600,
        "processorType": "Intel(R) Xeon(R) CPU E5-2697A v4 @ 2.60GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v2.60 (05/21/2018)",
        "serialNumber": "CN7602080V",
        "shortModel": "SY 480 Gen9",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "Warning",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 32768,
        "model": "Synergy 480 Gen10",
        "mpFirmwareVersion": "1.22 Mar 06 2018",
        "mpModel": "iLO5",
        "name": "CN751302CF, bay 8",
        "partNumber": "871945-B21",
        "position": 8,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 12,
        "processorCount": 2,
        "processorSpeedMhz": 2300,
        "processorType": "Intel(R) Xeon(R) Gold 5118 CPU @ 2.30GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v1.36 (02/14/2018)",
        "serialNumber": "MXQ819037B",
        "shortModel": "SY 480 Gen10",
        "state": "ProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "FullHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 131072,
        "model": "Synergy 660 Gen10",
        "mpFirmwareVersion": "1.30 May 31 2018",
        "mpModel": "iLO5",
        "name": "CN751302CF, bay 5",
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
        "serialNumber": "MXQ734046L",
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
        "model": "Synergy 480 Gen9",
        "mpFirmwareVersion": "2.60 May 23 2018",
        "mpModel": "iLO4",
        "name": "CN75450622, bay 4",
        "partNumber": "754683-001",
        "position": 4,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 6,
        "processorCount": 2,
        "processorSpeedMhz": 1600,
        "processorType": "Intel(R) Xeon(R) CPU E5-2603 v3 @ 1.60GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v2.60 (05/21/2018)",
        "serialNumber": "CN754606ZX",
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
        "model": "Synergy 480 Gen9",
        "mpFirmwareVersion": "2.55 Aug 16 2017",
        "mpModel": "iLO4",
        "name": "CN75450622, bay 7",
        "partNumber": "754683-001",
        "position": 7,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 6,
        "processorCount": 2,
        "processorSpeedMhz": 1600,
        "processorType": "Intel(R) Xeon(R) CPU E5-2603 v3 @ 1.60GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v2.60 (05/21/2018)",
        "serialNumber": "CN754606YM",
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
        "mpFirmwareVersion": "1.22 Mar 06 2018",
        "mpModel": "iLO5",
        "name": "CN75450622, bay 3",
        "partNumber": "871946-B21",
        "position": 3,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 6,
        "processorCount": 2,
        "processorSpeedMhz": 1700,
        "processorType": "Intel(R) Xeon(R) Bronze 3104 CPU @ 1.70GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v1.36 (02/14/2018)",
        "serialNumber": "MXQ74904NG",
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
        "model": "Synergy 480 Gen9",
        "mpFirmwareVersion": "2.55 Aug 16 2017",
        "mpModel": "iLO4",
        "name": "CN75450622, bay 1",
        "partNumber": "754683-001",
        "position": 1,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 6,
        "processorCount": 2,
        "processorSpeedMhz": 1600,
        "processorType": "Intel(R) Xeon(R) CPU E5-2603 v3 @ 1.60GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v2.60 (05/21/2018)",
        "serialNumber": "CN75460700",
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
        "name": "CN75450622, bay 2",
        "partNumber": "754683-001",
        "position": 2,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 10,
        "processorCount": 2,
        "processorSpeedMhz": 2200,
        "processorType": "Intel(R) Xeon(R) CPU E5-2630 v4 @ 2.20GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v2.60 (05/21/2018)",
        "serialNumber": "MXQ70804QJ",
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
        "mpFirmwareVersion": "2.55 Aug 16 2017",
        "mpModel": "iLO4",
        "name": "CN75450622, bay 8",
        "partNumber": "754683-001",
        "position": 8,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 6,
        "processorCount": 2,
        "processorSpeedMhz": 1600,
        "processorType": "Intel(R) Xeon(R) CPU E5-2603 v3 @ 1.60GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v2.52 (10/25/2017)",
        "serialNumber": "CN7546071Y",
        "shortModel": "SY 480 Gen9",
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
        "name": "CN75450622, bay 10",
        "partNumber": "871945-B21",
        "position": 10,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 12,
        "processorCount": 2,
        "processorSpeedMhz": 2300,
        "processorType": "Intel(R) Xeon(R) Gold 5118 CPU @ 2.30GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v1.36 (02/14/2018)",
        "serialNumber": "MXQ8190378",
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
        "mpFirmwareVersion": "1.30 May 31 2018",
        "mpModel": "iLO5",
        "name": "CN75450620, bay 3",
        "partNumber": "871946-B21",
        "position": 3,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 6,
        "processorCount": 2,
        "processorSpeedMhz": 1700,
        "processorType": "Intel(R) Xeon(R) Bronze 3104 CPU @ 1.70GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v1.42 (06/20/2018)",
        "serialNumber": "MXQ75005B2",
        "shortModel": "SY 480 Gen10",
        "state": "Unmanaged",
        "stateReason": "Unconfigured",
        "status": "Critical",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "FullHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 131072,
        "model": "Synergy 660 Gen10",
        "mpFirmwareVersion": "1.22 Mar 06 2018",
        "mpModel": "iLO5",
        "name": "CN75450620, bay 5",
        "partNumber": "871933-B21",
        "position": 5,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 18,
        "processorCount": 2,
        "processorSpeedMhz": 2300,
        "processorType": "Intel(R) Xeon(R) Gold 6140 CPU @ 2.30GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I43 v1.36 (02/14/2018)",
        "serialNumber": "MXQ734046P",
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
        "model": "Synergy 480 Gen9",
        "mpFirmwareVersion": "2.60 May 23 2018",
        "mpModel": "iLO4",
        "name": "CN751302CF, bay 2",
        "partNumber": "754683-001",
        "position": 2,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 6,
        "processorCount": 2,
        "processorSpeedMhz": 1600,
        "processorType": "Intel(R) Xeon(R) CPU E5-2603 v3 @ 1.60GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v2.60 (05/21/2018)",
        "serialNumber": "CN754606YQ",
        "shortModel": "SY 480 Gen9",
        "state": "ProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-10"
    }
]

#!/usr/bin/env python

admin_credentials = {'userName': 'Administrator', 'password': 'Cosmos123'}
timeandlocale = {'localeDisplayName': 'English (United States)', 'locale': 'en_US.UTF-8',
                 'dateTime': '2018-09-05T17:17:14.284Z', 'ntpServers': [], 'timezone': 'UTC', 'type': 'TimeAndLocale'}
licenses = [
]

appliance = {
    'type': "ApplianceNetworkConfigurationV2",
    'applianceNetworks':
    [{
        "device": "bond0",
        "macAddress": "9c:b6:54:98:76:98",
        "interfaceName": "Appliance",
        "activeNode": 1,
        "unconfigure": False,
        "ipv4Type": "STATIC",
        "ipv4Subnet": "255.255.0.0",
        "ipv4Gateway": "10.152.0.1",
        "ipv4NameServers": [u'10.120.0.10'],
        "app1Ipv4Addr": "10.152.1.16",
        "ipv6Type": "UNCONFIGURE",
        "hostname": "CSTGS11.dom1152.lab",
        "confOneNode": False,
        "domainName": "dom1152.lab",
        "aliasDisabled": False
    }
    ]}

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
        'startAddress': "9A:2F:AC:60:00:00",
        'endAddress': "9A:2F:AC:6F:FF:FF",
        'enabled': True
    },
    {
        'type': "Range",
        'name': "VWWN",
        'category': "id-range-VWWN",
        'rangeCategory': "Generated",
        'startAddress': "10:00:7e:1f:30:00:00:00",
        'endAddress': "10:00:7e:1f:30:0f:ff:ff",
        'enabled': True
    },
    {
        'type': "Range",
        'name': "VSN",
        'category': "id-range-VSN",
        'rangeCategory': "Generated",
        'startAddress': "VCGJ27M000",
        'endAddress': "VCGJ27MZZZ",
        'enabled': True
    }
]

deployment_server = [
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
    },
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
    }
]
expected_san_managers = [
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
                "value": ""
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
        "name": "Eth_1156",
        "privateNetwork": False,
        "purpose": "Management",
        "smartLink": True,
        "vlanId": 1156
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth_1157",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1157
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth_1158",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1158
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth_1155",
        "privateNetwork": False,
        "purpose": "Management",
        "smartLink": True,
        "vlanId": 1155
    }
]
expected_ethernet_networks = [
    {
        "uri": "ETH:Eth_1156",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth_1156",
        "privateNetwork": False,
        "purpose": "Management",
        "smartLink": True,
        "vlanId": 1156
    },
    {
        "uri": "ETH:Eth_1157",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth_1157",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1157
    },
    {
        "uri": "ETH:Eth_1158",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth_1158",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1158
    },
    {
        "uri": "ETH:Eth_1155",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth_1155",
        "privateNetwork": False,
        "purpose": "Management",
        "smartLink": True,
        "vlanId": 1155
    }
]

fc_networks = [
    {
        "type": "fc-networkV4",
        "name": "FC-B",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:RIST-R1-SN6600B-SW2"
    },
    {
        "type": "fc-networkV4",
        "name": "FC-A",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:RIST-R1-SN6600B-SW1"
    }
]
expected_fc_networks = [
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
        "managedSanUri": "FCSan:RIST-R1-SN6600B-SW2"
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
        "managedSanUri": "FCSan:RIST-R1-SN6600B-SW1"
    }
]

fcoe_networks = [
    {
        "name": "FCOE3802",
        "type": "fcoe-networkV4",
        "vlanId": 3802,
        "managedSanUri": "FCSan:VSAN3802"
    },
    {
        "name": "FCOE3801",
        "type": "fcoe-networkV4",
        "vlanId": 3801,
        "managedSanUri": "FCSan:VSAN3801"
    }
]
expected_fcoe_networks = [
    {
        "uri": "FCOE:FCOE3802",
        "state": "Active",
        "status": "OK",
        "name": "FCOE3802",
        "type": "fcoe-networkV4",
        "vlanId": 3802,
        "managedSanUri": "FCSan:VSAN3802"
    },
    {
        "uri": "FCOE:FCOE3801",
        "state": "Active",
        "status": "OK",
        "name": "FCOE3801",
        "type": "fcoe-networkV4",
        "vlanId": 3801,
        "managedSanUri": "FCSan:VSAN3801"
    }
]

networksets = [
    {
        "type": "network-setV4",
        "name": "Networkset",
        "nativeNetworkUri": None,
        "networkUris": [
            "Eth_1155",
            "Eth_1156"
        ]
    }
]
expected_networksets = [
    {
        "category": "network-sets",
        "state": "Active",
        "description": None,
        "uri": "NS:Networkset",
        "status": "OK",
        "type": "network-setV4",
        "name": "Networkset",
        "nativeNetworkUri": "None",
        "networkUris": [
            "ETH:Eth_1155",
            "ETH:Eth_1156"
        ]
    }
]

storage_systems_with_pools = [
    {
        "credentials": {'username': 'cosmos', 'password': 'Insight7'},
        "name": "RIST-R1-3PAR",
        "family": "StoreServ",
        "hostname": "10.120.1.81",
        "deviceSpecificAttributes": {
            "managedDomain": "NO DOMAIN",
            "managedPools": [{'domain': 'NO DOMAIN', 'name': 'FC_r1', 'raidLevel': 'RAID1', 'state': 'Managed', 'deviceType': 'FC', 'freeCapacity': '1511828488192', 'totalCapacity': '2753074036736', 'uuid': 'd5aed6dd-6ea8-4ac5-ae51-72112a7bc43a'}, {'domain': 'NO DOMAIN', 'name': 'FC_r5', 'raidLevel': 'RAID5', 'state': 'Managed', 'deviceType': 'FC', 'freeCapacity': '1326071152640', 'totalCapacity': '1377610760192', 'uuid': 'd991ad64-3cf2-459b-886c-d63deb4c3737'}, {'domain': 'NO DOMAIN', 'name': 'FC_r6', 'raidLevel': 'RAID6', 'state': 'Managed', 'deviceType': 'FC', 'freeCapacity': '1060588486656', 'totalCapacity': '1111993876480', 'uuid': '9f3043ce-5dc2-4a48-9d5f-d1fc393d5c57'}],
            "discoveredPools": [],

        }
    }
]
expected_storage_systems_with_pools = [
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
    {
        "name": "Volume Template Raid 1",
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
                "default": "FC_r1",
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
                "default": "FC_r1",
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
        "name": "Volume Template Raid 5",
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
        "name": "Volume Template Raid 6",
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
                "default": "FC_r6",
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
                "default": "FC_r6",
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
        "uri": "SVT:Volume Template Raid 1",
        "status": "OK",
        "name": "Volume Template Raid 1",
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
                "default": "SPOOL:FC_r1",
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
                "default": "SPOOL:FC_r1",
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
        "uri": "SVT:Volume Template Raid 5",
        "status": "OK",
        "name": "Volume Template Raid 5",
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
        "uri": "SVT:Volume Template Raid 6",
        "status": "OK",
        "name": "Volume Template Raid 6",
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
                "default": "SPOOL:FC_r6",
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
                "default": "SPOOL:FC_r6",
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
        "templateUri": "Volume Template Raid 1",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "27K_bay4_Expo_Win16",
            "provisioningType": "Thin",
            "size": 53687091200,
            "storagePool": "FC_r1"
        },
    },
    {
        "templateUri": "Volume Template Raid 5",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "27K_bay1_FC_esxi65",
            "provisioningType": "Thin",
            "size": 53687091200,
            "storagePool": "FC_r5"
        },
    },
    {
        "templateUri": "Volume Template Raid 1",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "27K_bay2_FC_Win16",
            "provisioningType": "Thin",
            "size": 53687091200,
            "storagePool": "FC_r1"
        },
    },
    {
        "templateUri": "Volume Template Raid 6",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "27K_bay3_Quadium_ESXi65",
            "provisioningType": "Thin",
            "size": 53687091200,
            "storagePool": "FC_r6"
        },
    },
    {
        "templateUri": "Volume Template Raid 1",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "27K_bay12_Expo_ESXi65u1",
            "provisioningType": "Thin",
            "size": 53687091200,
            "storagePool": "FC_r1"
        },
    },
    {
        "templateUri": "Volume Template Raid 1",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "27K_bay7_Electron_esxi65u1",
            "provisioningType": "Thin",
            "size": 53687091200,
            "storagePool": "FC_r1"
        },
    },
    {
        "templateUri": "Volume Template Raid 1",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "27K_bay8_Quartz_esxi65u1",
            "provisioningType": "Thin",
            "size": 53687091200,
            "storagePool": "FC_r1"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "Add_Quadium 1",
            "provisioningType": "Thin",
            "size": 10737418240,
            "storagePool": "FC_r1"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "Add_Quadium 2",
            "provisioningType": "Thin",
            "size": 10737418240,
            "storagePool": "FC_r1"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "Add_Quadium 3",
            "provisioningType": "Thin",
            "size": 10737418240,
            "storagePool": "FC_r1"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "Add_Quadium 4",
            "provisioningType": "Thin",
            "size": 10737418240,
            "storagePool": "FC_r1"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "Add_Quadium 5",
            "provisioningType": "Thin",
            "size": 10737418240,
            "storagePool": "FC_r1"
        },
    },
    {
        "templateUri": "Volume Template Raid 1",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "27K_bay9_Electron_Win16",
            "provisioningType": "Thin",
            "size": 53687091200,
            "storagePool": "FC_r1"
        }
    }
]
expected_storage_volumes = [
    {
        "status": "OK",
        "uri": "SVOL:27K_bay4_Expo_Win16",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "27K_bay4_Expo_Win16",
            "provisioningType": "Thin",
            "size": 53687091200,
            "storagePoolUri": "SPOOL:FC_r1"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:27K_bay1_FC_esxi65",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "27K_bay1_FC_esxi65",
            "provisioningType": "Thin",
            "size": 53687091200,
            "storagePoolUri": "SPOOL:FC_r5"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:27K_bay2_FC_Win16",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "27K_bay2_FC_Win16",
            "provisioningType": "Thin",
            "size": 53687091200,
            "storagePoolUri": "SPOOL:FC_r1"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:27K_bay3_Quadium_ESXi65",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "27K_bay3_Quadium_ESXi65",
            "provisioningType": "Thin",
            "size": 53687091200,
            "storagePoolUri": "SPOOL:FC_r6"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:27K_bay12_Expo_ESXi65u1",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "27K_bay12_Expo_ESXi65u1",
            "provisioningType": "Thin",
            "size": 53687091200,
            "storagePoolUri": "SPOOL:FC_r1"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:27K_bay7_Electron_esxi65u1",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "27K_bay7_Electron_esxi65u1",
            "provisioningType": "Thin",
            "size": 53687091200,
            "storagePoolUri": "SPOOL:FC_r1"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:27K_bay8_Quartz_esxi65u1",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "27K_bay8_Quartz_esxi65u1",
            "provisioningType": "Thin",
            "size": 53687091200,
            "storagePoolUri": "SPOOL:FC_r1"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:Add_Quadium 1",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "Add_Quadium 1",
            "provisioningType": "Thin",
            "size": 10737418240,
            "storagePoolUri": "SPOOL:FC_r1"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:Add_Quadium 2",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "Add_Quadium 2",
            "provisioningType": "Thin",
            "size": 10737418240,
            "storagePoolUri": "SPOOL:FC_r1"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:Add_Quadium 3",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "Add_Quadium 3",
            "provisioningType": "Thin",
            "size": 10737418240,
            "storagePoolUri": "SPOOL:FC_r1"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:Add_Quadium 4",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "Add_Quadium 4",
            "provisioningType": "Thin",
            "size": 10737418240,
            "storagePoolUri": "SPOOL:FC_r1"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:Add_Quadium 5",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "Add_Quadium 5",
            "provisioningType": "Thin",
            "size": 10737418240,
            "storagePoolUri": "SPOOL:FC_r1"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:27K_bay9_Electron_Win16",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "27K_bay9_Electron_Win16",
            "provisioningType": "Thin",
            "size": 53687091200,
            "storagePoolUri": "SPOOL:FC_r1"
        }
    }
]

sas_lig = [
]
expected_sas_lig = [
]

ligs = [
    {
        "name": "LIGcarbon",
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
                "type": "Virtual Connect SE 32Gb FC Module for Synergy"
            },
            {
                "enclosureIndex": -1,
                "enclosure": -1,
                "bay": 2,
                "type": "Virtual Connect SE 32Gb FC Module for Synergy"
            }

        ],
        "interconnectBaySet": 2,
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
                        "port": "1",
                        "enclosure": "-1",
                        "bay": "2"
                    },
                    {
                        "speed": "Auto",
                        "port": "2",
                        "enclosure": "-1",
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
            },
            {
                "ethernetNetworkType": "NotApplicable",
                "lacpTimer": None,
                "logicalPortConfigInfos": [
                    {
                        "speed": "Auto",
                        "port": "1",
                        "enclosure": "-1",
                        "bay": "5"
                    },
                    {
                        "speed": "Auto",
                        "port": "2",
                        "enclosure": "-1",
                        "bay": "5"
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
        "name": "LIGPotash",
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
                "type": "Synergy 10Gb Interconnect Link Module"
            },
            {
                "enclosureIndex": 1,
                "enclosure": 1,
                "bay": 3,
                "type": "Virtual Connect SE 40Gb F8 Module for Synergy"
            },
            {
                "enclosureIndex": 2,
                "bay": 3,
                "enclosure": 2,
                "type": "Synergy 10Gb Interconnect Link Module"
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
                "ethernetNetworkType": "Tagged",
                "lacpTimer": "Short",
                "logicalPortConfigInfos": [
                    {
                        "speed": "Auto",
                        "enclosure": "2",
                        "port": "Q3",
                        "bay": "6"
                    }
                ],
                "mode": "Auto",
                "name": "FCoE 3802",
                "nativeNetworkUri": None,
                "networkType": "Ethernet",
                "networkUris": [
                    "FCOE3802"
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
                        "port": "71"
                    }
                ],
                "mode": "Auto",
                "name": "FCoE 3801",
                "nativeNetworkUri": None,
                "networkType": "Ethernet",
                "networkUris": [
                    "FCOE3801"
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
                        "port": "61",
                        "enclosure": "1",
                        "bay": "3"
                    }
                ],
                "mode": "Auto",
                "name": "EthUL",
                "nativeNetworkUri": None,
                "networkType": "Ethernet",
                "networkUris": [
                    "Eth_1155",
                    "Eth_1156"
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
        "uri": "LIG:LIGcarbon",
        "status": None,
        "stackingHealth": None,
        "category": "logical-interconnect-groups",
        "state": "Active",
        "internalNetworkUris": "[]",
        "stackingMode": None,
        "description": None,
        "name": "LIGcarbon",
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
        "uri": "LIG:LIGPotash",
        "status": None,
        "stackingHealth": None,
        "category": "logical-interconnect-groups",
        "state": "Active",
        "internalNetworkUris": "[]",
        "stackingMode": None,
        "description": None,
        "name": "LIGPotash",
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
                "logicalInterconnectGroupUri": "LIG:LIGcarbon",
                "enclosureIndex": 2
            },
            {
                "interconnectBay": 3,
                "logicalInterconnectGroupUri": "LIG:LIGPotash",

            },
            {
                "interconnectBay": 5,
                "logicalInterconnectGroupUri": "LIG:LIGcarbon",
                "enclosureIndex": 2
            },
            {
                "interconnectBay": 6,
                "logicalInterconnectGroupUri": "LIG:LIGPotash",

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
        "associatedLogicalInterconnectGroups": [u'LIG:LIGcarbon', u'LIG:LIGPotash'],
        "name": "EG",
        "type": "EnclosureGroupV7",
        "enclosureTypeUri": "/rest/enclosure-types/SY12000",
        "stackingMode": "Enclosure",
        "name": "EG",
        "interconnectBayMappingCount": "4",
        "interconnectBayMappings": [
            {
                "interconnectBay": 2,
                "logicalInterconnectGroupUri": "LIG:LIGcarbon",

            },
            {
                "interconnectBay": 3,
                "logicalInterconnectGroupUri": "LIG:LIGPotash",

            },
            {
                "interconnectBay": 5,
                "logicalInterconnectGroupUri": "LIG:LIGcarbon",

            },
            {
                "interconnectBay": 6,
                "logicalInterconnectGroupUri": "LIG:LIGPotash",

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
            "ENC:MXQ807027K",
            "ENC:MXQ807027N"
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
            "ENC:MXQ807027K",
            "ENC:MXQ807027N"
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
        "name": "27K_bay8_Quartz_esxi65u1",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:MXQ807027K, bay 8",
        "enclosureUri": "ENC:MXQ807027K",
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
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1156",
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
                    "networkUri": "ETH:Eth_1156",
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
                    "portId": "Mezz 2:1",
                    "requestedMbps": "Auto",
                    "wwnn": "10:00:7e:1f:30:00:00:1d",
                    "wwpn": "10:00:7e:1f:30:00:00:1c",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'Primary', u'bootVolumeSource': u'ManagedVolume'},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 16000,
                    "name": "",
                    "portId": "Mezz 2:2",
                    "requestedMbps": "Auto",
                    "wwnn": "10:00:7e:1f:30:00:00:1f",
                    "wwpn": "10:00:7e:1f:30:00:00:1e",
                    "networkUri": "FC:FC-B",
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
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:27K_bay8_Quartz_esxi65u1",
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
        "name": "27k_bay9_Electron_Win16",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:MXQ807027K, bay 9",
        "enclosureUri": "ENC:MXQ807027K",
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
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1156",
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
                    "portId": "Mezz 3:2-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1156",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": -2000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": -2000,
                    "name": "",
                    "portId": "Mezz 2:1",
                    "requestedMbps": "Auto",
                    "wwnn": "10:00:7e:1f:30:00:00:21",
                    "wwpn": "10:00:7e:1f:30:00:00:20",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'Primary', u'bootVolumeSource': u'ManagedVolume'},
                },
                {
                    "allocatedMbps": -2000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": -2000,
                    "name": "",
                    "portId": "Mezz 2:2",
                    "requestedMbps": "Auto",
                    "wwnn": "10:00:7e:1f:30:00:00:23",
                    "wwpn": "10:00:7e:1f:30:00:00:22",
                    "networkUri": "FC:FC-B",
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
                    "volumeUri": "SVOL:27K_bay9_Electron_Win16",
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
        "name": "27K_bay2_Quadium_Win16",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:MXQ807027K, bay 2",
        "enclosureUri": "ENC:MXQ807027K",
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
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1155",
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
                    "networkUri": "ETH:Eth_1155",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": -2000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": -2000,
                    "name": "",
                    "portId": "Mezz 2:1",
                    "requestedMbps": "Auto",
                    "wwnn": "10:00:7e:1f:30:00:00:0d",
                    "wwpn": "10:00:7e:1f:30:00:00:0c",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'Primary', u'bootVolumeSource': u'ManagedVolume'},
                },
                {
                    "allocatedMbps": -2000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": -2000,
                    "name": "",
                    "portId": "Mezz 2:2",
                    "requestedMbps": "Auto",
                    "wwnn": "10:00:7e:1f:30:00:00:0f",
                    "wwpn": "10:00:7e:1f:30:00:00:0e",
                    "networkUri": "FC:FC-B",
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
            "firmwareBaselineUri": "/rest/firmware-drivers/bp-2018-08-23-02",
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
            "hostOSType": "Windows Server 2016",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:27K_bay2_FC_Win16",
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
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:Add_Quadium 1",
                    "bootVolumePriority": "NotBootable",
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
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:Add_Quadium 2",
                    "bootVolumePriority": "NotBootable",
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
                },
                {
                    "id": 4,
                    "volumeUri": "SVOL:Add_Quadium 3",
                    "bootVolumePriority": "NotBootable",
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
                },
                {
                    "id": 5,
                    "volumeUri": "SVOL:Add_Quadium 4",
                    "bootVolumePriority": "NotBootable",
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
                },
                {
                    "id": 6,
                    "volumeUri": "SVOL:Add_Quadium 5",
                    "bootVolumePriority": "NotBootable",
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
        "name": "27K_bay1_FC_esxi65",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:MXQ807027K, bay 1",
        "enclosureUri": "ENC:MXQ807027K",
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
                    "networkUri": "ETH:Eth_1155",
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
                    "networkUri": "ETH:Eth_1155",
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
                    "networkUri": "ETH:Eth_1156",
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
                    "networkUri": "ETH:Eth_1156",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": -2000,
                    "functionType": "FibreChannel",
                    "id": 5,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": -2000,
                    "name": "",
                    "portId": "Mezz 2:1",
                    "requestedMbps": "Auto",
                    "wwnn": "10:00:7e:1f:30:00:00:09",
                    "wwpn": "10:00:7e:1f:30:00:00:08",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'Primary', u'bootVolumeSource': u'ManagedVolume'},
                },
                {
                    "allocatedMbps": -2000,
                    "functionType": "FibreChannel",
                    "id": 6,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": -2000,
                    "name": "",
                    "portId": "Mezz 2:2",
                    "requestedMbps": "Auto",
                    "wwnn": "10:00:7e:1f:30:00:00:0b",
                    "wwpn": "10:00:7e:1f:30:00:00:0a",
                    "networkUri": "FC:FC-B",
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
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:27K_bay1_FC_esxi65",
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
        "name": "27K_bay7_Quartz_esxi65u1",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:MXQ807027K, bay 7",
        "enclosureUri": "ENC:MXQ807027K",
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
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1156",
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
                    "networkUri": "ETH:Eth_1156",
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
                    "portId": "Mezz 2:1",
                    "requestedMbps": "Auto",
                    "wwnn": "10:00:7e:1f:30:00:00:19",
                    "wwpn": "10:00:7e:1f:30:00:00:18",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'Primary', u'bootVolumeSource': u'ManagedVolume'},
                },
                {
                    "allocatedMbps": -2000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": -2000,
                    "name": "",
                    "portId": "Mezz 2:2",
                    "requestedMbps": "Auto",
                    "wwnn": "10:00:7e:1f:30:00:00:1b",
                    "wwpn": "10:00:7e:1f:30:00:00:1a",
                    "networkUri": "FC:FC-B",
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
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:27K_bay7_Electron_esxi65u1",
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
        "name": "27K_bay3_Quadium_ESXi65",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:MXQ807027K, bay 3",
        "enclosureUri": "ENC:MXQ807027K",
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
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1155",
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
                    "networkUri": "ETH:Eth_1155",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 32000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 32000,
                    "name": "",
                    "portId": "Mezz 2:1",
                    "requestedMbps": "Auto",
                    "wwnn": "10:00:7e:1f:30:00:00:11",
                    "wwpn": "10:00:7e:1f:30:00:00:10",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'Primary', u'bootVolumeSource': u'ManagedVolume'},
                },
                {
                    "allocatedMbps": -2000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": -2000,
                    "name": "",
                    "portId": "Mezz 2:2",
                    "requestedMbps": "Auto",
                    "wwnn": "10:00:7e:1f:30:00:00:13",
                    "wwpn": "10:00:7e:1f:30:00:00:12",
                    "networkUri": "FC:FC-B",
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
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:27K_bay3_Quadium_ESXi65",
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
        "name": "27K_bay4_Expo_Win16",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:MXQ807027K, bay 4",
        "enclosureUri": "ENC:MXQ807027K",
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
                    "allocatedMbps": 32000,
                    "functionType": "FibreChannel",
                    "id": 5,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 32000,
                    "name": "",
                    "portId": "Mezz 2:1",
                    "requestedMbps": "Auto",
                    "wwnn": "10:00:7e:1f:30:00:00:01",
                    "wwpn": "10:00:7e:1f:30:00:00:00",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'Primary', u'bootVolumeSource': u'ManagedVolume'},
                },
                {
                    "allocatedMbps": -2000,
                    "functionType": "FibreChannel",
                    "id": 6,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": -2000,
                    "name": "",
                    "portId": "Mezz 2:2",
                    "requestedMbps": "Auto",
                    "wwnn": "10:00:7e:1f:30:00:00:03",
                    "wwpn": "10:00:7e:1f:30:00:00:02",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'Secondary', u'bootVolumeSource': u'ManagedVolume'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 7,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1156",
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
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1156",
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
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows Server 2016",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:27K_bay4_Expo_Win16",
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
        "name": "27K_bay12_Expo_ESXi65u1",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:MXQ807027K, bay 12",
        "enclosureUri": "ENC:MXQ807027K",
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
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1155",
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
                    "networkUri": "ETH:Eth_1155",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 32000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": 32000,
                    "name": "",
                    "portId": "Mezz 2:1",
                    "requestedMbps": "Auto",
                    "wwnn": "10:00:7e:1f:30:00:00:15",
                    "wwpn": "10:00:7e:1f:30:00:00:14",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'Primary', u'bootVolumeSource': u'ManagedVolume'},
                },
                {
                    "allocatedMbps": -2000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "mac": "",
                    "macType": "Virtual",
                    "maximumMbps": -2000,
                    "name": "",
                    "portId": "Mezz 2:2",
                    "requestedMbps": "Auto",
                    "wwnn": "10:00:7e:1f:30:00:00:17",
                    "wwpn": "10:00:7e:1f:30:00:00:16",
                    "networkUri": "FC:FC-B",
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
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:27K_bay12_Expo_ESXi65u1",
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
    }
]
expected_server_profile_with_storage = [
    {
        "uri": "SP:27K_bay8_Quartz_esxi65u1",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen10 2:2:Synergy 3830C 16G FC HBA:3:Synergy 3820C 10/20Gb CNA",
        "name": "27K_bay8_Quartz_esxi65u1",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:MXQ807027K, bay 8",
        "enclosureUri": "ENC:MXQ807027K",
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
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1156",
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
                    "networkUri": "ETH:Eth_1156",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "maximumMbps": 16000,
                    "name": "",
                    "portId": "Mezz 2:1",
                    "requestedMbps": "Auto",
                    "wwnn": "10:00:7e:1f:30:00:00:1d",
                    "wwpn": "10:00:7e:1f:30:00:00:1c",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'Primary', u'bootVolumeSource': u'ManagedVolume'},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": 16000,
                    "name": "",
                    "portId": "Mezz 2:2",
                    "requestedMbps": "Auto",
                    "wwnn": "10:00:7e:1f:30:00:00:1f",
                    "wwpn": "10:00:7e:1f:30:00:00:1e",
                    "networkUri": "FC:FC-B",
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
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:27K_bay8_Quartz_esxi65u1",
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
        "uri": "SP:27k_bay9_Electron_Win16",
        "state": "Normal",
        "status": "Critical",
        "serverHardwareTypeUri": "SHT:SY 480 Gen10 4:2:Synergy 3530C 16G HBA:3:Synergy 3820C 10/20Gb CNA",
        "name": "27k_bay9_Electron_Win16",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:MXQ807027K, bay 9",
        "enclosureUri": "ENC:MXQ807027K",
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
                    "portId": "Mezz 3:1-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1156",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-d",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1156",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": -2000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "maximumMbps": -2000,
                    "name": "",
                    "portId": "Mezz 2:1",
                    "requestedMbps": "Auto",
                    "wwnn": "10:00:7e:1f:30:00:00:21",
                    "wwpn": "10:00:7e:1f:30:00:00:20",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'Primary', u'bootVolumeSource': u'ManagedVolume'},
                },
                {
                    "allocatedMbps": -2000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": -2000,
                    "name": "",
                    "portId": "Mezz 2:2",
                    "requestedMbps": "Auto",
                    "wwnn": "10:00:7e:1f:30:00:00:23",
                    "wwpn": "10:00:7e:1f:30:00:00:22",
                    "networkUri": "FC:FC-B",
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
                    "volumeUri": "SVOL:27K_bay9_Electron_Win16",
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
        "uri": "SP:27K_bay2_Quadium_Win16",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen10 1:2:Synergy 5830C 32G FC HBA:3:Synergy 3820C 10/20Gb CNA",
        "name": "27K_bay2_Quadium_Win16",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:MXQ807027K, bay 2",
        "enclosureUri": "ENC:MXQ807027K",
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
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1155",
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
                    "networkUri": "ETH:Eth_1155",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": -2000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "maximumMbps": -2000,
                    "name": "",
                    "portId": "Mezz 2:1",
                    "requestedMbps": "Auto",
                    "wwnn": "10:00:7e:1f:30:00:00:0d",
                    "wwpn": "10:00:7e:1f:30:00:00:0c",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'Primary', u'bootVolumeSource': u'ManagedVolume'},
                },
                {
                    "allocatedMbps": -2000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": -2000,
                    "name": "",
                    "portId": "Mezz 2:2",
                    "requestedMbps": "Auto",
                    "wwnn": "10:00:7e:1f:30:00:00:0f",
                    "wwpn": "10:00:7e:1f:30:00:00:0e",
                    "networkUri": "FC:FC-B",
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
            "firmwareBaselineUri": "/rest/firmware-drivers/bp-2018-08-23-02",
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
            "hostOSType": "Windows Server 2016",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:27K_bay2_FC_Win16",
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
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:Add_Quadium 1",
                    "bootVolumePriority": "NotBootable",
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
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:Add_Quadium 2",
                    "bootVolumePriority": "NotBootable",
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
                },
                {
                    "id": 4,
                    "volumeUri": "SVOL:Add_Quadium 3",
                    "bootVolumePriority": "NotBootable",
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
                },
                {
                    "id": 5,
                    "volumeUri": "SVOL:Add_Quadium 4",
                    "bootVolumePriority": "NotBootable",
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
                },
                {
                    "id": 6,
                    "volumeUri": "SVOL:Add_Quadium 5",
                    "bootVolumePriority": "NotBootable",
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
        "uri": "SP:27K_bay1_FC_esxi65",
        "state": "Normal",
        "status": "Critical",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9 2:2:Synergy 3530C 16G HBA:3:Synergy 2820C 10Gb CNA",
        "name": "27K_bay1_FC_esxi65",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:MXQ807027K, bay 1",
        "enclosureUri": "ENC:MXQ807027K",
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
                    "networkUri": "ETH:Eth_1155",
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
                    "networkUri": "ETH:Eth_1155",
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
                    "networkUri": "ETH:Eth_1156",
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
                    "networkUri": "ETH:Eth_1156",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": -2000,
                    "functionType": "FibreChannel",
                    "id": 5,
                    "maximumMbps": -2000,
                    "name": "",
                    "portId": "Mezz 2:1",
                    "requestedMbps": "Auto",
                    "wwnn": "10:00:7e:1f:30:00:00:09",
                    "wwpn": "10:00:7e:1f:30:00:00:08",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'Primary', u'bootVolumeSource': u'ManagedVolume'},
                },
                {
                    "allocatedMbps": -2000,
                    "functionType": "FibreChannel",
                    "id": 6,
                    "maximumMbps": -2000,
                    "name": "",
                    "portId": "Mezz 2:2",
                    "requestedMbps": "Auto",
                    "wwnn": "10:00:7e:1f:30:00:00:0b",
                    "wwpn": "10:00:7e:1f:30:00:00:0a",
                    "networkUri": "FC:FC-B",
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
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:27K_bay1_FC_esxi65",
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
        "uri": "SP:27K_bay7_Quartz_esxi65u1",
        "state": "Normal",
        "status": "Critical",
        "serverHardwareTypeUri": "SHT:SY 480 Gen10 2:2:Synergy 3830C 16G FC HBA:3:Synergy 3820C 10/20Gb CNA",
        "name": "27K_bay7_Quartz_esxi65u1",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:MXQ807027K, bay 7",
        "enclosureUri": "ENC:MXQ807027K",
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
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1156",
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
                    "networkUri": "ETH:Eth_1156",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "maximumMbps": 16000,
                    "name": "",
                    "portId": "Mezz 2:1",
                    "requestedMbps": "Auto",
                    "wwnn": "10:00:7e:1f:30:00:00:19",
                    "wwpn": "10:00:7e:1f:30:00:00:18",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'Primary', u'bootVolumeSource': u'ManagedVolume'},
                },
                {
                    "allocatedMbps": -2000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": -2000,
                    "name": "",
                    "portId": "Mezz 2:2",
                    "requestedMbps": "Auto",
                    "wwnn": "10:00:7e:1f:30:00:00:1b",
                    "wwpn": "10:00:7e:1f:30:00:00:1a",
                    "networkUri": "FC:FC-B",
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
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:27K_bay7_Electron_esxi65u1",
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
        "uri": "SP:27K_bay3_Quadium_ESXi65",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen10 1:2:Synergy 5830C 32G FC HBA:3:Synergy 3820C 10/20Gb CNA",
        "name": "27K_bay3_Quadium_ESXi65",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:MXQ807027K, bay 3",
        "enclosureUri": "ENC:MXQ807027K",
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
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1155",
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
                    "networkUri": "ETH:Eth_1155",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 32000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "maximumMbps": 32000,
                    "name": "",
                    "portId": "Mezz 2:1",
                    "requestedMbps": "Auto",
                    "wwnn": "10:00:7e:1f:30:00:00:11",
                    "wwpn": "10:00:7e:1f:30:00:00:10",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'Primary', u'bootVolumeSource': u'ManagedVolume'},
                },
                {
                    "allocatedMbps": -2000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": -2000,
                    "name": "",
                    "portId": "Mezz 2:2",
                    "requestedMbps": "Auto",
                    "wwnn": "10:00:7e:1f:30:00:00:13",
                    "wwpn": "10:00:7e:1f:30:00:00:12",
                    "networkUri": "FC:FC-B",
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
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:27K_bay3_Quadium_ESXi65",
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
        "uri": "SP:27K_bay4_Expo_Win16",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen10 3:2:Synergy 5330C 32Gb FC HBA:3:Synergy 3820C 10/20Gb CNA",
        "name": "27K_bay4_Expo_Win16",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:MXQ807027K, bay 4",
        "enclosureUri": "ENC:MXQ807027K",
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
                    "allocatedMbps": 32000,
                    "functionType": "FibreChannel",
                    "id": 5,
                    "maximumMbps": 32000,
                    "name": "",
                    "portId": "Mezz 2:1",
                    "requestedMbps": "Auto",
                    "wwnn": "10:00:7e:1f:30:00:00:01",
                    "wwpn": "10:00:7e:1f:30:00:00:00",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'Primary', u'bootVolumeSource': u'ManagedVolume'},
                },
                {
                    "allocatedMbps": -2000,
                    "functionType": "FibreChannel",
                    "id": 6,
                    "maximumMbps": -2000,
                    "name": "",
                    "portId": "Mezz 2:2",
                    "requestedMbps": "Auto",
                    "wwnn": "10:00:7e:1f:30:00:00:03",
                    "wwpn": "10:00:7e:1f:30:00:00:02",
                    "networkUri": "FC:FC-B",
                    "boot": {u'priority': u'Secondary', u'bootVolumeSource': u'ManagedVolume'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 7,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1156",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 8,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1156",
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
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows Server 2016",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:27K_bay4_Expo_Win16",
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
        "uri": "SP:27K_bay12_Expo_ESXi65u1",
        "state": "Normal",
        "status": "OK",
        "serverHardwareTypeUri": "SHT:SY 480 Gen10 3:2:Synergy 5330C 32Gb FC HBA:3:Synergy 3820C 10/20Gb CNA",
        "name": "27K_bay12_Expo_ESXi65u1",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:MXQ807027K, bay 12",
        "enclosureUri": "ENC:MXQ807027K",
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
                    "portId": "Mezz 3:1-c",
                    "requestedMbps": "2500",
                    "wwnn": None,
                    "wwpn": None,
                    "networkUri": "ETH:Eth_1155",
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
                    "networkUri": "ETH:Eth_1155",
                    "boot": {u'priority': u'NotBootable'},
                },
                {
                    "allocatedMbps": 32000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "maximumMbps": 32000,
                    "name": "",
                    "portId": "Mezz 2:1",
                    "requestedMbps": "Auto",
                    "wwnn": "10:00:7e:1f:30:00:00:15",
                    "wwpn": "10:00:7e:1f:30:00:00:14",
                    "networkUri": "FC:FC-A",
                    "boot": {u'priority': u'Primary', u'bootVolumeSource': u'ManagedVolume'},
                },
                {
                    "allocatedMbps": -2000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": -2000,
                    "name": "",
                    "portId": "Mezz 2:2",
                    "requestedMbps": "Auto",
                    "wwnn": "10:00:7e:1f:30:00:00:17",
                    "wwpn": "10:00:7e:1f:30:00:00:16",
                    "networkUri": "FC:FC-B",
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
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:27K_bay12_Expo_ESXi65u1",
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
    }
]

servers = [
    {
        "formFactor": "FullHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 32768,
        "model": "Synergy 660 Gen9",
        "mpFirmwareVersion": "2.61 Jul 16 2018",
        "mpModel": "iLO4",
        "name": "MXQ807027N, bay 5",
        "partNumber": "732360-B21",
        "position": 5,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 10,
        "processorCount": 4,
        "processorSpeedMhz": 1800,
        "processorType": "Intel(R) Xeon(R) CPU E5-4610 v4 @ 1.80GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I39 v2.60 (05/21/2018)",
        "serialNumber": "MXQ75107SL",
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
        "model": "Synergy 480 Gen9",
        "mpFirmwareVersion": "2.61 Jul 16 2018",
        "mpModel": "iLO4",
        "name": "MXQ807027N, bay 2",
        "partNumber": "826953-B21",
        "position": 2,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 10,
        "processorCount": 2,
        "processorSpeedMhz": 2200,
        "processorType": "Intel(R) Xeon(R) CPU E5-2630 v4 @ 2.20GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v2.60 (05/21/2018)",
        "serialNumber": "MXQ748048J",
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
        "mpFirmwareVersion": "2.61 Jul 16 2018",
        "mpModel": "iLO4",
        "name": "MXQ807027N, bay 4",
        "partNumber": "826953-B21",
        "position": 4,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 10,
        "processorCount": 2,
        "processorSpeedMhz": 2200,
        "processorType": "Intel(R) Xeon(R) CPU E5-2630 v4 @ 2.20GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v2.60 (05/21/2018)",
        "serialNumber": "MXQ748048F",
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
        "mpFirmwareVersion": "2.61 Jul 16 2018",
        "mpModel": "iLO4",
        "name": "MXQ807027N, bay 1",
        "partNumber": "826953-B21",
        "position": 1,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 10,
        "processorCount": 2,
        "processorSpeedMhz": 2200,
        "processorType": "Intel(R) Xeon(R) CPU E5-2630 v4 @ 2.20GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v2.60 (05/21/2018)",
        "serialNumber": "MXQ7480480",
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
        "mpFirmwareVersion": "2.61 Jul 16 2018",
        "mpModel": "iLO4",
        "name": "MXQ807027K, bay 1",
        "partNumber": "826953-B21",
        "position": 1,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 10,
        "processorCount": 2,
        "processorSpeedMhz": 2200,
        "processorType": "Intel(R) Xeon(R) CPU E5-2630 v4 @ 2.20GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v2.60 (05/21/2018)",
        "serialNumber": "MXQ7480486",
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
        "mpFirmwareVersion": "2.61 Jul 16 2018",
        "mpModel": "iLO4",
        "name": "MXQ807027K, bay 5",
        "partNumber": "732360-B21",
        "position": 5,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 10,
        "processorCount": 4,
        "processorSpeedMhz": 1800,
        "processorType": "Intel(R) Xeon(R) CPU E5-4610 v4 @ 1.80GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I39 v2.60 (05/21/2018)",
        "serialNumber": "MXQ75107SK",
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
        "mpFirmwareVersion": "1.35 Jul 17 2018",
        "mpModel": "iLO5",
        "name": "MXQ807027K, bay 4",
        "partNumber": "871946-B21",
        "position": 4,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 6,
        "processorCount": 2,
        "processorSpeedMhz": 1700,
        "processorType": "Intel(R) Xeon(R) Bronze 3104 CPU @ 1.70GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v2.00 (08/07/2018)",
        "serialNumber": "MXQ81103JT",
        "shortModel": "SY 480 Gen10",
        "state": "ProfileApplied",
        "stateReason": "NotApplicable",
        "status": "Warning",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 16384,
        "model": "Synergy 480 Gen10",
        "mpFirmwareVersion": "1.35 Jul 17 2018",
        "mpModel": "iLO5",
        "name": "MXQ807027K, bay 7",
        "partNumber": "871946-B21",
        "position": 7,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 6,
        "processorCount": 2,
        "processorSpeedMhz": 1700,
        "processorType": "Intel(R) Xeon(R) Bronze 3104 CPU @ 1.70GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v2.00 (08/07/2018)",
        "serialNumber": "MXQ81103K0",
        "shortModel": "SY 480 Gen10",
        "state": "ProfileApplied",
        "stateReason": "NotApplicable",
        "status": "Warning",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 16384,
        "model": "Synergy 480 Gen10",
        "mpFirmwareVersion": "1.35 Jul 17 2018",
        "mpModel": "iLO5",
        "name": "MXQ807027K, bay 8",
        "partNumber": "871946-B21",
        "position": 8,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 6,
        "processorCount": 2,
        "processorSpeedMhz": 1700,
        "processorType": "Intel(R) Xeon(R) Bronze 3104 CPU @ 1.70GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v2.00 (08/07/2018)",
        "serialNumber": "MXQ81103JN",
        "shortModel": "SY 480 Gen10",
        "state": "ProfileApplied",
        "stateReason": "NotApplicable",
        "status": "Warning",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 32768,
        "model": "Synergy 480 Gen10",
        "mpFirmwareVersion": "1.35 Jul 17 2018",
        "mpModel": "iLO5",
        "name": "MXQ807027K, bay 9",
        "partNumber": "871945-B21",
        "position": 9,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 12,
        "processorCount": 2,
        "processorSpeedMhz": 2300,
        "processorType": "Intel(R) Xeon(R) Gold 5118 CPU @ 2.30GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v2.00 (08/07/2018)",
        "serialNumber": "MXQ8190379",
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
        "mpFirmwareVersion": "1.35 Jul 17 2018",
        "mpModel": "iLO5",
        "name": "MXQ807027K, bay 10",
        "partNumber": "871946-B21",
        "position": 10,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 6,
        "processorCount": 2,
        "processorSpeedMhz": 1700,
        "processorType": "Intel(R) Xeon(R) Bronze 3104 CPU @ 1.70GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v2.00 (08/07/2018)",
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
        "mpFirmwareVersion": "1.35 Jul 17 2018",
        "mpModel": "iLO5",
        "name": "MXQ807027K, bay 12",
        "partNumber": "871946-B21",
        "position": 12,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 6,
        "processorCount": 2,
        "processorSpeedMhz": 1700,
        "processorType": "Intel(R) Xeon(R) Bronze 3104 CPU @ 1.70GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v2.00 (08/07/2018)",
        "serialNumber": "MXQ74904NJ",
        "shortModel": "SY 480 Gen10",
        "state": "ProfileApplied",
        "stateReason": "NotApplicable",
        "status": "Critical",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 16384,
        "model": "Synergy 480 Gen10",
        "mpFirmwareVersion": "1.35 Jul 17 2018",
        "mpModel": "iLO5",
        "name": "MXQ807027K, bay 3",
        "partNumber": "871946-B21",
        "position": 3,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 6,
        "processorCount": 2,
        "processorSpeedMhz": 1700,
        "processorType": "Intel(R) Xeon(R) Bronze 3104 CPU @ 1.70GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v2.00 (08/07/2018)",
        "serialNumber": "MXQ81103JG",
        "shortModel": "SY 480 Gen10",
        "state": "ProfileApplied",
        "stateReason": "NotApplicable",
        "status": "Warning",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 16384,
        "model": "Synergy 480 Gen10",
        "mpFirmwareVersion": "1.35 Jul 17 2018",
        "mpModel": "iLO5",
        "name": "MXQ807027K, bay 2",
        "partNumber": "871946-B21",
        "position": 2,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 18,
        "processorCount": 2,
        "processorSpeedMhz": 2200,
        "processorType": "Intel(R) Xeon(R) Gold 5220 CPU @ 2.20GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I42 v2.00 (08/07/2018)",
        "serialNumber": "MXQ81103JZ",
        "shortModel": "SY 480 Gen10",
        "state": "ProfileApplied",
        "stateReason": "NotApplicable",
        "status": "Critical",
        "type": "server-hardware-10"
    }
]

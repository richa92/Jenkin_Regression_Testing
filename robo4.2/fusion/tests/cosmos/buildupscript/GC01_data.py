#!/usr/bin/env python

admin_credentials = {'userName': 'Administrator', 'password': 'Cosmos123'}
timeandlocale = {'localeDisplayName': 'English (United States)', 'locale': 'en_US.UTF-8', 'dateTime': '2018-09-11T07:39:51.555Z', 'ntpServers': [], 'timezone': 'UTC', 'type': 'TimeAndLocale'}
licenses = [
]

appliance = {
    'type': "ApplianceNetworkConfigurationV2",
    'applianceNetworks':
    [{
        "device": "eth0",
        "macAddress": "00:50:56:a1:8d:fb",
        "interfaceName": "Appliance",
        "activeNode": 1,
        "unconfigure": False,
        "ipv4Type": "STATIC",
        "ipv4Subnet": "255.255.255.0",
        "ipv4Gateway": "172.25.26.1",
        "ipv4NameServers": [],
        "app1Ipv4Addr": "172.25.26.140",
        "ipv6Type": "UNCONFIGURE",
        "hostname": "ci-005056a18dfb.com",
        "confOneNode": True,
        "domainName": "",
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
                "value": "172.25.9.22"
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
                "value": "172.25.9.21"
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
                "value": "172.25.9.127"
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
                "value": "administrator"
            }
        ]
    }
]
expected_san_managers = [
    {
        "uri": "SAN:172.25.9.22",
        "name": "172.25.9.22",
        "type": "FCDeviceManagerV2",
        "category": "fc-device-managers",
        "state": "Managed",
        "description": "HPE 5900AF-48XG-4QSFP+ Switch",
        "deviceManagerVersion": "7.1.045 Release 2422P03",
        "isInternal": "False",
        "providerDisplayName": "HPE",
        "refreshState": "Stable",
        "status": "OK",
        "connectionInfo": [
            {
                "name": "Host",
                "value": "172.25.9.22"
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
        "uri": "SAN:172.25.9.21",
        "name": "172.25.9.21",
        "type": "FCDeviceManagerV2",
        "category": "fc-device-managers",
        "state": "Managed",
        "description": "HP 5900AF-48XG-4QSFP+ Switch",
        "deviceManagerVersion": "7.1.045 Release 2416",
        "isInternal": "False",
        "providerDisplayName": "HPE",
        "refreshState": "Stable",
        "status": "OK",
        "connectionInfo": [
            {
                "name": "Host",
                "value": "172.25.9.21"
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
        "uri": "SAN:172.25.9.127",
        "name": "172.25.9.127",
        "type": "FCDeviceManagerV2",
        "category": "fc-device-managers",
        "state": "Managed",
        "description": "Brocade Network Advisor",
        "deviceManagerVersion": "14.0.1.170",
        "isInternal": "False",
        "providerDisplayName": "Brocade Network Advisor",
        "refreshState": "Stable",
        "status": "OK",
        "connectionInfo": [
            {
                "name": "Host",
                "value": "172.25.9.127"
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
                "value": "administrator"
            }
        ]
    }
]

ethernet_networks = [
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth5-iSCSI-VSA",
        "privateNetwork": False,
        "purpose": "ISCSI",
        "smartLink": True,
        "vlanId": 1009
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth4",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1057
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth6-iSCSI-VSA",
        "privateNetwork": False,
        "purpose": "ISCSI",
        "smartLink": True,
        "vlanId": 1009
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "iSCSI2",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1009
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth3",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1057
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "iSCSI1",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1009
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth2",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1056
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth1",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1056
    }
]
expected_ethernet_networks = [
    {
        "uri": "ETH:Eth5-iSCSI-VSA",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth5-iSCSI-VSA",
        "privateNetwork": False,
        "purpose": "ISCSI",
        "smartLink": True,
        "vlanId": 1009
    },
    {
        "uri": "ETH:Eth4",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth4",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1057
    },
    {
        "uri": "ETH:Eth6-iSCSI-VSA",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth6-iSCSI-VSA",
        "privateNetwork": False,
        "purpose": "ISCSI",
        "smartLink": True,
        "vlanId": 1009
    },
    {
        "uri": "ETH:iSCSI2",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "iSCSI2",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1009
    },
    {
        "uri": "ETH:Eth3",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth3",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1057
    },
    {
        "uri": "ETH:iSCSI1",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "iSCSI1",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1009
    },
    {
        "uri": "ETH:Eth2",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth2",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1056
    },
    {
        "uri": "ETH:Eth1",
        "category": "ethernet-networks",
        "state": "Active",
        "subnetUri": None,
        "description": None,
        "status": "OK",
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Eth1",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 1056
    }
]

fc_networks = [
    {
        "type": "fc-networkV4",
        "name": "DAS1",
        "fabricType": "DirectAttach",
        "linkStabilityTime": 0,
        "autoLoginRedistribution": False,
        "managedSanUri": None
    },
    {
        "type": "fc-networkV4",
        "name": "FC2",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:NFV-BNA-SW2"
    },
    {
        "type": "fc-networkV4",
        "name": "DAS2",
        "fabricType": "DirectAttach",
        "linkStabilityTime": 0,
        "autoLoginRedistribution": False,
        "managedSanUri": None
    },
    {
        "type": "fc-networkV4",
        "name": "FC1",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:NFV-BNA-SW1"
    }
]
expected_fc_networks = [
    {
        "category": "fc-networks",
        "state": "Active",
        "description": None,
        "uri": "FC:DAS1",
        "status": "OK",
        "type": "fc-networkV4",
        "name": "DAS1",
        "fabricType": "DirectAttach",
        "linkStabilityTime": 0,
        "autoLoginRedistribution": False,
        "managedSanUri": None
    },
    {
        "category": "fc-networks",
        "state": "Active",
        "description": None,
        "uri": "FC:FC2",
        "status": "OK",
        "type": "fc-networkV4",
        "name": "FC2",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:NFV-BNA-SW2"
    },
    {
        "category": "fc-networks",
        "state": "Active",
        "description": None,
        "uri": "FC:DAS2",
        "status": "OK",
        "type": "fc-networkV4",
        "name": "DAS2",
        "fabricType": "DirectAttach",
        "linkStabilityTime": 0,
        "autoLoginRedistribution": False,
        "managedSanUri": None
    },
    {
        "category": "fc-networks",
        "state": "Active",
        "description": None,
        "uri": "FC:FC1",
        "status": "OK",
        "type": "fc-networkV4",
        "name": "FC1",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:NFV-BNA-SW1"
    }
]

fcoe_networks = [
    {
        "name": "FCoE2",
        "type": "fcoe-networkV4",
        "vlanId": 1022,
        "managedSanUri": "FCSan:VSAN1022"
    },
    {
        "name": "FCoE1",
        "type": "fcoe-networkV4",
        "vlanId": 1021,
        "managedSanUri": "FCSan:VSAN1021"
    }
]
expected_fcoe_networks = [
    {
        "uri": "FCOE:FCoE2",
        "state": "Active",
        "status": "OK",
        "name": "FCoE2",
        "type": "fcoe-networkV4",
        "vlanId": 1022,
        "managedSanUri": "FCSan:VSAN1022"
    },
    {
        "uri": "FCOE:FCoE1",
        "state": "Active",
        "status": "OK",
        "name": "FCoE1",
        "type": "fcoe-networkV4",
        "vlanId": 1021,
        "managedSanUri": "FCSan:VSAN1021"
    }
]

networksets = [
]
expected_networksets = [
]

storage_systems_with_pools = [
    {
        "credentials": {'username': 'cosmos', 'password': 'Nextgen9'},
        "name": "COSMOS-7400-9.125",
        "family": "StoreServ",
        "hostname": "172.25.9.125",
        "deviceSpecificAttributes": {
            "managedDomain": "Cosmos-MainStream",
            "managedPools": [{'domain': 'Cosmos-MainStream', 'name': 'MainStream-CPG', 'raidLevel': 'RAID5', 'state': 'Managed', 'deviceType': 'FC', 'freeCapacity': '400505700352', 'totalCapacity': '1099511627776', 'uuid': '63c15e24-d9f3-48b4-a416-7f65d94884c4'}],
            "discoveredPools": [],

        },
    },
    {
        "credentials": {'username': 'admin', 'password': 'Cosmos123'},
        "name": "Cosmos_Cluster",
        "family": "StoreVirtual",
        "hostname": "172.25.16.4"
    }
]
expected_storage_systems_with_pools = [
    {
        "uri": "SSYS:COSMOS-7400-9.125",
        "type": "StorageSystemV5",
        "state": "Managed",
        "category": "storage-systems",
        "status": "OK",
        "name": "COSMOS-7400-9.125",
        "family": "StoreServ",
        "hostname": "172.25.9.125",
        "deviceSpecificAttributes": {
            "managedDomain": "Cosmos-MainStream",
            "serialNumber": "1615657"
        },
    },
    {
        "uri": "SSYS:Cosmos_Cluster",
        "type": "StorageSystemV5",
        "state": "Managed",
        "category": "storage-systems",
        "status": "OK",
        "name": "Cosmos_Cluster",
        "family": "StoreVirtual",
        "hostname": "172.25.16.4"
    }
]

storage_pools_toedit = [
    {
        "storageSystemUri": "Cosmos_Cluster",
        "name": "Cosmos_Cluster",
        "isManaged": True,
    },
    {
        "storageSystemUri": "COSMOS-7400-9.125",
        "name": "MainStream-CPG",
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
            "name": "Case128_RHEL6.9",
            "provisioningType": "Thin",
            "size": 53687091200,
            "storagePool": "MainStream-CPG"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "Case114_Bay10",
            "provisioningType": "Thin",
            "size": 53687091200,
            "storagePool": "MainStream-CPG"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "Case114_Bay10_RHEL6.9",
            "provisioningType": "Thin",
            "size": 53687091200,
            "storagePool": "MainStream-CPG"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "Case141_Bay9_SLES12P3_Prim",
            "provisioningType": "Thin",
            "size": 53687091200,
            "storagePool": "MainStream-CPG"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "Case141_Bay9_SLES12P3_2",
            "provisioningType": "Thin",
            "size": 53687091200,
            "storagePool": "MainStream-CPG"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "Case45_Issue Retest_SLES12 SP3",
            "provisioningType": "Thin",
            "size": 53687091200,
            "storagePool": "MainStream-CPG"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "Case45_Issue Retest",
            "provisioningType": "Thin",
            "size": 53687091200,
            "storagePool": "MainStream-CPG"
        },
    },
    {
        "templateUri": "ROOT",
        "isPermanent": True,
        "properties": {
            "description": "",
            "isShareable": True,
            "name": "Test_Vol",
            "provisioningType": "Thin",
            "size": 268435456,
            "storagePool": "MainStream-CPG"
        },
    },
    {
        "templateUri": "ROOT",
        "isPermanent": True,
        "properties": {
            "description": "",
            "isShareable": True,
            "name": "Test_Vol_2",
            "provisioningType": "Thin",
            "size": 268435456,
            "storagePool": "MainStream-CPG"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "Case110_Bay10_1",
            "provisioningType": "Thin",
            "size": 53687091200,
            "storagePool": "MainStream-CPG"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "Case59_Issue Restest_SLES12 SP2",
            "provisioningType": "Thin",
            "size": 53687091200,
            "storagePool": "MainStream-CPG"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "Case115_Bay10_1",
            "provisioningType": "Thin",
            "size": 53687091200,
            "storagePool": "MainStream-CPG"
        }
    }
]
expected_storage_volumes = [
    {
        "status": "OK",
        "uri": "SVOL:Case128_RHEL6.9",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "Case128_RHEL6.9",
            "provisioningType": "Thin",
            "size": 53687091200,
            "storagePoolUri": "SPOOL:MainStream-CPG"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:Case114_Bay10",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "Case114_Bay10",
            "provisioningType": "Thin",
            "size": 53687091200,
            "storagePoolUri": "SPOOL:MainStream-CPG"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:Case114_Bay10_RHEL6.9",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "Case114_Bay10_RHEL6.9",
            "provisioningType": "Thin",
            "size": 53687091200,
            "storagePoolUri": "SPOOL:MainStream-CPG"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:Case141_Bay9_SLES12P3_Prim",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "Case141_Bay9_SLES12P3_Prim",
            "provisioningType": "Thin",
            "size": 53687091200,
            "storagePoolUri": "SPOOL:MainStream-CPG"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:Case141_Bay9_SLES12P3_2",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "Case141_Bay9_SLES12P3_2",
            "provisioningType": "Thin",
            "size": 53687091200,
            "storagePoolUri": "SPOOL:MainStream-CPG"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:Case45_Issue Retest_SLES12 SP3",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "Case45_Issue Retest_SLES12 SP3",
            "provisioningType": "Thin",
            "size": 53687091200,
            "storagePoolUri": "SPOOL:MainStream-CPG"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:Case45_Issue Retest",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "Case45_Issue Retest",
            "provisioningType": "Thin",
            "size": 53687091200,
            "storagePoolUri": "SPOOL:MainStream-CPG"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:Test_Vol",
        "isPermanent": True,
        "properties": {
            "description": "",
            "isShareable": True,
            "name": "Test_Vol",
            "provisioningType": "Thin",
            "size": 268435456,
            "storagePoolUri": "SPOOL:MainStream-CPG"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:Test_Vol_2",
        "isPermanent": True,
        "properties": {
            "description": "",
            "isShareable": True,
            "name": "Test_Vol_2",
            "provisioningType": "Thin",
            "size": 268435456,
            "storagePoolUri": "SPOOL:MainStream-CPG"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:Case110_Bay10_1",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "Case110_Bay10_1",
            "provisioningType": "Thin",
            "size": 53687091200,
            "storagePoolUri": "SPOOL:MainStream-CPG"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:Case59_Issue Restest_SLES12 SP2",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "Case59_Issue Restest_SLES12 SP2",
            "provisioningType": "Thin",
            "size": 53687091200,
            "storagePoolUri": "SPOOL:MainStream-CPG"
        },
    },
    {
        "status": "OK",
        "uri": "SVOL:Case115_Bay10_1",
        "properties": {
            "description": "",
            "isShareable": False,
            "name": "Case115_Bay10_1",
            "provisioningType": "Thin",
            "size": 53687091200,
            "storagePoolUri": "SPOOL:MainStream-CPG"
        }
    }
]

sas_lig = [
]
expected_sas_lig = [
]

ligs = [
    {
        "name": "LIG-3",
        "type": "logical-interconnect-groupV6",
        "enclosureType": "C7000",
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
                "type": "HP VC 16Gb 24-Port FC Module"
            },
            {
                "enclosureIndex": 1,
                "bay": 4,
                "enclosure": 1,
                "type": "HP VC 16Gb 24-Port FC Module"
            }

        ],
        "interconnectBaySet": None,
        "redundancyType": None,
        "telemetryConfiguration": {
            "enableTelemetry": True,
            "sampleCount": 12,
            "sampleInterval": 300
        },
        "uplinkSets": [
        ],
        "qosConfiguration": {
            "activeQosConfig": {u'category': u'qos-aggregated-configuration', u'status': None, u'description': None, u'created': None, u'uri': None, u'modified': None, u'configType': u'Passthrough', u'state': None, u'eTag': None, u'downlinkClassificationType': None, u'uplinkClassificationType': None, u'qosTrafficClassifiers': [], u'type': u'QosConfiguration', u'name': None},
            "inactiveFCoEQosConfig": None,
            "inactiveNonFCoEQosConfig": None,
            "name": None,
            "type": "qos-aggregated-configuration"
        },
        "enclosureIndexes": [1]
    },
    {
        "name": "LIG2",
        "type": "logical-interconnect-groupV6",
        "enclosureType": "C7000",
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
                "type": "HP VC FlexFabric-20/40 F8 Module"
            },
            {
                "enclosureIndex": 1,
                "bay": 4,
                "enclosure": 1,
                "type": "HP VC FlexFabric-20/40 F8 Module"
            }

        ],
        "interconnectBaySet": None,
        "redundancyType": None,
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
                    "port": "X4",
                    "bay": "4"
                }
            ],
            "mode": "Auto",
            "name": "iSCSI2",
            "nativeNetworkUri": None,
            "networkType": "Ethernet",
            "networkUris": [
                "iSCSI2"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "NotApplicable",
            "lacpTimer": None,
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "enclosure": "1",
                    "port": "X3",
                    "bay": "4"
                }
            ],
            "mode": "Auto",
            "name": "FC2",
            "nativeNetworkUri": None,
            "networkType": "FibreChannel",
            "networkUris": [
                "FC2"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "NotApplicable",
            "lacpTimer": None,
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "enclosure": "1",
                    "port": "X3",
                    "bay": "3"
                }
            ],
            "mode": "Auto",
            "name": "FC1",
            "nativeNetworkUri": None,
            "networkType": "FibreChannel",
            "networkUris": [
                "FC1"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "Tagged",
            "lacpTimer": "Short",
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "enclosure": "1",
                    "port": "X1",
                    "bay": "4"
                }
            ],
            "mode": "Auto",
            "name": "FCoE2",
            "nativeNetworkUri": None,
            "networkType": "Ethernet",
            "networkUris": [
                "FCoE2"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "Tagged",
            "lacpTimer": "Short",
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "enclosure": "1",
                    "port": "X1",
                    "bay": "3"
                }
            ],
            "mode": "Auto",
            "name": "FCoE1",
            "nativeNetworkUri": None,
            "networkType": "Ethernet",
            "networkUris": [
                "FCoE1"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "NotApplicable",
            "lacpTimer": None,
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "enclosure": "1",
                    "port": "X2",
                    "bay": "4"
                }
            ],
            "mode": "Auto",
            "name": "DAS2",
            "nativeNetworkUri": None,
            "networkType": "FibreChannel",
            "networkUris": [
                "DAS2"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "NotApplicable",
            "lacpTimer": None,
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "enclosure": "1",
                    "port": "X2",
                    "bay": "3"
                }
            ],
            "mode": "Auto",
            "name": "DAS1",
            "nativeNetworkUri": None,
            "networkType": "FibreChannel",
            "networkUris": [
                "DAS1"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "Tagged",
            "lacpTimer": "Short",
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "enclosure": "1",
                    "port": "X4",
                    "bay": "3"
                }
            ],
            "mode": "Auto",
            "name": "iSCSI1",
            "nativeNetworkUri": None,
            "networkType": "Ethernet",
            "networkUris": [
                "iSCSI1"
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
    },
    {
        "name": "LIG1",
        "type": "logical-interconnect-groupV6",
        "enclosureType": "C7000",
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
                "bay": 1,
                "enclosure": 1,
                "type": "HP VC FlexFabric 10Gb/24-Port Module"
            },
            {
                "enclosureIndex": 1,
                "bay": 2,
                "enclosure": 1,
                "type": "HP VC FlexFabric 10Gb/24-Port Module"
            }

        ],
        "interconnectBaySet": None,
        "redundancyType": None,
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
                    "port": "X3",
                    "bay": "2"
                }
            ],
            "mode": "Auto",
            "name": "FC2",
            "nativeNetworkUri": None,
            "networkType": "FibreChannel",
            "networkUris": [
                "FC2"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "Tagged",
            "lacpTimer": "Short",
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "enclosure": "1",
                    "port": "X1",
                    "bay": "2"
                }
            ],
            "mode": "Auto",
            "name": "FCoE2",
            "nativeNetworkUri": None,
            "networkType": "Ethernet",
            "networkUris": [
                "FCoE2"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "Tagged",
            "lacpTimer": "Short",
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "enclosure": "1",
                    "port": "X5",
                    "bay": "2"
                }
            ],
            "mode": "Auto",
            "name": "Eth2",
            "nativeNetworkUri": None,
            "networkType": "Ethernet",
            "networkUris": [
                "Eth6-iSCSI-VSA",
                "Eth4",
                "Eth2"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "Tagged",
            "lacpTimer": "Short",
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "enclosure": "1",
                    "port": "X1",
                    "bay": "1"
                }
            ],
            "mode": "Auto",
            "name": "FCoE1",
            "nativeNetworkUri": None,
            "networkType": "Ethernet",
            "networkUris": [
                "FCoE1"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "NotApplicable",
            "lacpTimer": None,
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "enclosure": "1",
                    "port": "X3",
                    "bay": "1"
                }
            ],
            "mode": "Auto",
            "name": "FC1",
            "nativeNetworkUri": None,
            "networkType": "FibreChannel",
            "networkUris": [
                "FC1"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "Tagged",
            "lacpTimer": "Short",
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "enclosure": "1",
                    "port": "X4",
                    "bay": "2"
                }
            ],
            "mode": "Auto",
            "name": "iSCSI2",
            "nativeNetworkUri": None,
            "networkType": "Ethernet",
            "networkUris": [
                "iSCSI2"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "Tagged",
            "lacpTimer": "Short",
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "enclosure": "1",
                    "port": "X4",
                    "bay": "1"
                }
            ],
            "mode": "Auto",
            "name": "iSCSI1",
            "nativeNetworkUri": None,
            "networkType": "Ethernet",
            "networkUris": [
                "iSCSI1"
            ],
            "primaryPort": None
        }, {
            "ethernetNetworkType": "Tagged",
            "lacpTimer": "Short",
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "enclosure": "1",
                    "port": "X5",
                    "bay": "1"
                }
            ],
            "mode": "Auto",
            "name": "Eth1",
            "nativeNetworkUri": None,
            "networkType": "Ethernet",
            "networkUris": [
                "Eth5-iSCSI-VSA",
                "Eth1",
                "Eth3"
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
        "uri": "LIG:LIG-3",
        "status": None,
        "stackingHealth": None,
        "category": "logical-interconnect-groups",
        "state": "Active",
        "internalNetworkUris": "[]",
        "stackingMode": None,
        "description": None,
        "name": "LIG-3",
        "type": "logical-interconnect-groupV6",
        "enclosureType": "C7000",
        "ethernetSettings": {
            "enableFastMacCacheFailover": True,
            "enableIgmpSnooping": False,
            "enableNetworkLoopProtection": True,
            "enablePauseFloodProtection": True,
            "igmpIdleTimeoutInterval": 260,
            "interconnectType": "Ethernet",
            "macRefreshInterval": 5
        },
        "interconnectBaySet": None,
        "redundancyType": None,
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
    },
    {
        "uri": "LIG:LIG2",
        "status": None,
        "stackingHealth": None,
        "category": "logical-interconnect-groups",
        "state": "Active",
        "internalNetworkUris": "[]",
        "stackingMode": None,
        "description": None,
        "name": "LIG2",
        "type": "logical-interconnect-groupV6",
        "enclosureType": "C7000",
        "ethernetSettings": {
            "enableFastMacCacheFailover": True,
            "enableIgmpSnooping": False,
            "enableNetworkLoopProtection": True,
            "enablePauseFloodProtection": True,
            "igmpIdleTimeoutInterval": 260,
            "interconnectType": "Ethernet",
            "macRefreshInterval": 5
        },
        "interconnectBaySet": None,
        "redundancyType": None,
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
    },
    {
        "uri": "LIG:LIG1",
        "status": None,
        "stackingHealth": None,
        "category": "logical-interconnect-groups",
        "state": "Active",
        "internalNetworkUris": "[]",
        "stackingMode": None,
        "description": None,
        "name": "LIG1",
        "type": "logical-interconnect-groupV6",
        "enclosureType": "C7000",
        "ethernetSettings": {
            "enableFastMacCacheFailover": True,
            "enableIgmpSnooping": False,
            "enableNetworkLoopProtection": True,
            "enablePauseFloodProtection": True,
            "igmpIdleTimeoutInterval": 260,
            "interconnectType": "Ethernet",
            "macRefreshInterval": 5
        },
        "interconnectBaySet": None,
        "redundancyType": None,
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

encgroups_add = [
    {
        "name": "EG1",
        "interconnectBayMappings": [
            {
                "interconnectBay": 1,
                "logicalInterconnectGroupUri": "LIG:LIG1",

            },
            {
                "interconnectBay": 2,
                "logicalInterconnectGroupUri": "LIG:LIG1",

            },
            {
                "interconnectBay": 3,
                "logicalInterconnectGroupUri": "LIG:LIG-3",

            },
            {
                "interconnectBay": 4,
                "logicalInterconnectGroupUri": "LIG:LIG-3",

            }
        ],
        "ipAddressingMode": "External",
        "enclosureCount": 1
    }
]
expected_encgroups_add = [
    {
        "uri": "EG:EG1",
        "description": None,
        "category": "enclosure-groups",
        "state": "Normal",
        "status": "OK",
        "powerMode": None,
        "portMappingCount": 8,
        "portMappings": [{u'midplanePort': 1, u'interconnectBay': 1}, {u'midplanePort': 2, u'interconnectBay': 2}, {u'midplanePort': 3, u'interconnectBay': 3}, {u'midplanePort': 4, u'interconnectBay': 4}, {u'midplanePort': 5, u'interconnectBay': 5}, {u'midplanePort': 6, u'interconnectBay': 6}, {u'midplanePort': 7, u'interconnectBay': 7}, {u'midplanePort': 8, u'interconnectBay': 8}],
        "ipRangeUris": [],
        "associatedLogicalInterconnectGroups": [u'LIG:LIG-3', u'LIG:LIG1'],
        "name": "EG1",
        "type": "EnclosureGroupV7",
        "enclosureTypeUri": "/rest/enclosure-types/c7000",
        "stackingMode": "Enclosure",
        "name": "EG1",
        "interconnectBayMappingCount": "4",
        "interconnectBayMappings": [
            {
                "interconnectBay": 1,
                "logicalInterconnectGroupUri": "LIG:LIG1",
            },
            {
                "interconnectBay": 2,
                "logicalInterconnectGroupUri": "LIG:LIG1",
            },
            {
                "interconnectBay": 3,
                "logicalInterconnectGroupUri": "LIG:LIG-3",
            },
            {
                "interconnectBay": 4,
                "logicalInterconnectGroupUri": "LIG:LIG-3",
            }
        ],
        "ipAddressingMode": "External",
        "enclosureCount": 1
    }
]

logical_enclosure = [
    {
        "name": "enc-1",
        "enclosureUris": [
            "ENC:MS11_C01-E1"
        ],
        "enclosureGroupUri": "EG:EG1"
    }
]
expected_logical_enclosure = [
    {
        "type": "LogicalEnclosureV4",
        "uri": "enc-1",
        "status": "OK",
        "name": "enc-1",
        "enclosureUris": [
            "ENC:MS11_C01-E1"
        ],
        "enclosureGroupUri": "EG:EG1"
    }
]

enclosures = [
    {
        "username": "Admin",
        "name": "MS11_C01-E1",
        "password": "Insight7",
        "force": True,
        "hostname": "172.25.11.11",
        "enclosureGroupUri": "EG:EG1",
        "forceInstallFirmware": True,
        "licensingIntent": "OneViewNoiLO",
    }
]
expected_enclosures = [
    {
        "name": "MS11_C01-E1",
        'state': 'Configured',
        'status': 'OK',
        "enclosureGroupUri": "EG:EG1",
        'logicalEnclosureUri': 'LE:enc-1',
        "licensingIntent": "OneViewNoiLO"
    }
]
servers = [
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "OneViewNoiLO",
        "memoryMb": 8192,
        "model": "ProLiant BL460c Gen9",
        "mpFirmwareVersion": "2.60 May 23 2018",
        "mpModel": "iLO4",
        "name": "MS11_C01-E1, bay 2",
        "partNumber": "727026-B21",
        "position": 2,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 6,
        "processorCount": 1,
        "processorSpeedMhz": 1900,
        "processorType": "Intel(R) Xeon(R) CPU E5-2609 v3 @ 1.90GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I36 v2.60 (05/21/2018)",
        "serialNumber": "2M260901NH",
        "shortModel": "BL460c Gen9",
        "state": "Unmanaged",
        "stateReason": "NotOwner",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "OneViewNoiLO",
        "memoryMb": 131072,
        "model": "ProLiant BL460c Gen9",
        "mpFirmwareVersion": "2.60 May 23 2018",
        "mpModel": "iLO4",
        "name": "MS11_C01-E1, bay 9",
        "partNumber": "779803-S01",
        "position": 9,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 12,
        "processorCount": 2,
        "processorSpeedMhz": 2600,
        "processorType": "Intel(R) Xeon(R) CPU E5-2690 v3 @ 2.60GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I36 v2.60 (05/21/2018)",
        "serialNumber": "2M25450CS1",
        "shortModel": "BL460c Gen9",
        "state": "Unmanaged",
        "stateReason": "NotOwner",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "OneViewNoiLO",
        "memoryMb": 32768,
        "model": "ProLiant BL460c Gen9",
        "mpFirmwareVersion": "2.60 May 23 2018",
        "mpModel": "iLO4",
        "name": "MS11_C01-E1, bay 7",
        "partNumber": "727027-B21",
        "position": 7,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 6,
        "processorCount": 1,
        "processorSpeedMhz": 2400,
        "processorType": "Intel(R) Xeon(R) CPU E5-2620 v3 @ 2.40GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I36 v2.60 (05/21/2018)",
        "serialNumber": "2M260804TP",
        "shortModel": "BL460c Gen9",
        "state": "Unmanaged",
        "stateReason": "NotOwner",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "OneViewNoiLO",
        "memoryMb": 16384,
        "model": "ProLiant BL460c Gen9",
        "mpFirmwareVersion": "2.60 May 23 2018",
        "mpModel": "iLO4",
        "name": "MS11_C01-E1, bay 1",
        "partNumber": "727027-B21",
        "position": 1,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 6,
        "processorCount": 1,
        "processorSpeedMhz": 2400,
        "processorType": "Intel(R) Xeon(R) CPU E5-2620 v3 @ 2.40GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I36 v2.60 (05/21/2018)",
        "serialNumber": "2M2550035J",
        "shortModel": "BL460c Gen9",
        "state": "Unmanaged",
        "stateReason": "NotOwner",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "OneViewNoiLO",
        "memoryMb": 16384,
        "model": "ProLiant BL460c Gen9",
        "mpFirmwareVersion": "2.61 Jul 27 2018",
        "mpModel": "iLO4",
        "name": "MS11_C01-E1, bay 16",
        "partNumber": "727027-B21",
        "position": 16,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 6,
        "processorCount": 1,
        "processorSpeedMhz": 2400,
        "processorType": "Intel(R) Xeon(R) CPU E5-2620 v3 @ 2.40GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I36 v2.60 (05/21/2018)",
        "serialNumber": "2M2550035C",
        "shortModel": "BL460c Gen9",
        "state": "Unmanaged",
        "stateReason": "NotOwner",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "OneViewNoiLO",
        "memoryMb": 262144,
        "model": "ProLiant BL460c Gen9",
        "mpFirmwareVersion": "2.60 May 23 2018",
        "mpModel": "iLO4",
        "name": "MS11_C01-E1, bay 10",
        "partNumber": "727021-B21",
        "position": 10,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 8,
        "processorCount": 2,
        "processorSpeedMhz": 2600,
        "processorType": "Intel(R) Xeon(R) CPU E5-2640 v3 @ 2.60GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I36 v2.60 (05/21/2018)",
        "serialNumber": "USE449FRET",
        "shortModel": "BL460c Gen9",
        "state": "Unmanaged",
        "stateReason": "NotOwner",
        "status": "OK",
        "type": "server-hardware-10"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "OneViewNoiLO",
        "memoryMb": 16384,
        "model": "ProLiant BL460c Gen9",
        "mpFirmwareVersion": "2.60 May 23 2018",
        "mpModel": "iLO4",
        "name": "MS11_C01-E1, bay 11",
        "partNumber": "779806-S01",
        "position": 11,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 6,
        "processorCount": 1,
        "processorSpeedMhz": 2400,
        "processorType": "Intel(R) Xeon(R) CPU E5-2620 v3 @ 2.40GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I36 v2.60 (05/21/2018)",
        "serialNumber": "2M252614FY",
        "shortModel": "BL460c Gen9",
        "state": "Unmanaged",
        "stateReason": "NotOwner",
        "status": "OK",
        "type": "server-hardware-10"
    }
]

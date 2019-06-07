def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}
login_details = {'userName': 'Administrator', 'password': 'hpvse123'}
network_admin = {'userName': 'network', 'password': 'networkadmin'}
storage_admin = {'userName': 'storage', 'password': 'storageadmin'}
backup_admin = {'userName': 'backup', 'password': 'backupadmin'}
server_admin = {'userName': 'server', 'password': 'serveradmin'}
read_only = {'userName': 'readonly', 'password': 'readonly'}

FileBeatLocation = 'http://192.168.146.236/ELK/'

upgrade_firmware_path = '/rest/firmware-drivers/Cust-K130-46-EM202-prod-G10'
downgrade_firmware_path = '/rest/firmware-drivers/Cust-K130-44-EM202-prod-G10'

LIG_Version = 'logical-interconnect-groupV4'
ENC1 = 'SGH721WSR0'
eth_network_Version = 'ethernet-networkV4'
fcoe_network_version = 'fcoe-networkV4'
fc_network_version = 'fc-networkV4'

icm_name = 'SGH721WSR0, interconnect 3'
HafniumModule1 = 'SGH721WSR0, interconnect 3'
HafniumModule2 = 'SGH721WSR0, interconnect 6'

users = [{'userName': 'server', 'password': 'serveradmin', 'fullName': 'Sarah', 'roles': ['Server administrator'], 'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'network', 'password': 'networkadmin', 'fullName': 'Nat', 'roles': ['Network administrator'], 'emailAddress': 'nat@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'backup', 'password': 'backupadmin', 'fullName': 'Backup', 'roles': ['Backup administrator'], 'emailAddress': 'backup@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'readonly', 'password': 'readonly', 'fullName': 'Rheid', 'roles': ['Read only'], 'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'storage', 'password': 'storageadmin', 'fullName': 'Rheid', 'roles': ['Storage administrator'], 'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'}
         ]

icmap_ME = [{'enclosure': 1, 'bay': 3, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
            {'enclosure': 1, 'bay': 6, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1}
            ]
sflow_lig_static = {"type": LIG_Version,
                    "ethernetSettings": {"type": 'EthernetInterconnectSettingsV4', "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
                    "description": None,
                    "name": "LIG_STATIC_t",
                    "interconnectMapTemplate": icmap_ME,
                    "enclosureType": "SY12000",
                    "enclosureIndexes": [1],
                    "interconnectBaySet": "3",
                    "redundancyType": "Redundant",
                    "internalNetworkUris": [],
                    "snmpConfiguration": None,
                    "qosConfiguration": None,
                    "sflowConfiguration": {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "net_200"},
                                           "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": "20.20.20.1", "maxDatagramSize": "1400", "maxHeaderSize": "128", "port": "6343", "collectorId": 1}],
                                           "sflowAgents": [{"ipMode": "Static"}],
                                           "sflowPorts": [{"portName": "Q1:1", "collectorId": "1", "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 3,
                                                           "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": "20", "pollingEnabled": True},
                                                                                                            {"configurationMode": "Sampling", "direction": "BOTH", "samplingRate": "256", "samplingEnabled": True}]},
                                                          {"portName": "Q1:1", "collectorId": "1", "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 6,
                                                           "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": "20", "pollingEnabled": True},
                                                                                                            {"configurationMode": "Sampling", "direction": "BOTH", "samplingRate": "256", "samplingEnabled": True}]},
                                                          {"portName": "Q2:1", "collectorId": "2", "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 3,
                                                           "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": "20", "pollingEnabled": True},
                                                                                                            {"configurationMode": "Sampling", "direction": "BOTH", "samplingRate": "256", "samplingEnabled": True}]},
                                                          {"portName": "d1", "collectorId": "3", "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 3,
                                                           "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": "20", "pollingEnabled": True},
                                                                                                            {"configurationMode": "Sampling", "direction": "BOTH", "samplingRate": "256", "samplingEnabled": True}]},
                                                          {"portName": "d1", "collectorId": "3", "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 6,
                                                           "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": "20", "pollingEnabled": True},
                                                                                                            {"configurationMode": "Sampling", "direction": "BOTH", "samplingRate": "256", "samplingEnabled": True}]},
                                                          ]
                                           },
                    "uplinkSets": [
                        {'name': 'us1_eth100', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ["net_200"], 'primaryPort': None, 'nativeNetworkUri': None, 'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': 'Q2.1', 'speed': 'Auto'}]}
                    ]}

sflow_eg = [{'name': 'EG',
             'ipAddressingMode': "External",
             'enclosureCount': 1,
             'configurationScript': None,
             'interconnectBayMappings': [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                                         {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                                         {'interconnectBay': 3, 'logicalInterconnectGroupUri': "LIG:LIG"},
                                         {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                                         {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                                         {'interconnectBay': 6, 'logicalInterconnectGroupUri': "LIG:LIG"}
                                         ]}]

sflow_le = [{'name': 'LE',
             'enclosureUris': ['ENC:' + ENC1],
             'enclosureGroupUri': 'EG:EG',
             'firmwareBaselineUri': None,
             'forceInstallFirmware': False
             }]

edit_li_edit_collector_ip = {'sflowconfiguration': {
    "type": "sflow-configuration",
    "category": "sflow-configuration",
    "enabled": True,
    "sflowAgents": [{
        "ipMode": "Static",
        "ipAddr": "192.168.145.43",
        "subnetMask": "255.255.255.0"
    }],
    "sflowNetwork": {
        "name": "Ethernet_1000",
        "uri": ' '
    },
    "sflowCollectors": [{
        "name": "C1",
        "collectorEnabled": True,
        "ipAddress": "192.168.147.210",
        "maxDatagramSize": "400",
        "maxHeaderSize": "128",
        "port": "6343",
        "collectorId": 1
    }],
    "sflowPorts": [{
        "portName": "Q2:1",
        "collectorId": "1",
        "icmName": "SGH721WSR0, interconnect 3",
        "bayNumber": 3,
        "enclosureIndex": 1,
        "sflowConfigurationModes": [{
            "configurationMode": "Polling",
            "pollingInterval": "20"
        },
            {
            "configurationMode": "Sampling",
            "direction": "BOTH",
            "samplingRate": "330"
        }]
    },
        {
        "portName": "Q1:1",
        "collectorId": 1,
        "icmName": "SGH721WSR0, interconnect 3",
        "bayNumber": 3,
        "enclosureIndex": 1,
        "sflowConfigurationModes": [{
            "configurationMode": "Polling",
            "pollingInterval": "20"
        },
            {
            "configurationMode": "Sampling",
            "direction": "BOTH",
            "samplingRate": "300"
        }]
    }]
}}

edit_li_add_3collector_ip = {'sflowconfiguration': {
    "type": "sflow-configuration",
    "category": "sflow-configuration",
    "enabled": True,
    "sflowAgents": [{
        "ipMode": "Static",
        "ipAddr": "192.168.147.43",
        "subnetMask": "255.255.248.0"
    }],
    "sflowNetwork": {
        "name": "Ethernet_Vlan_1",
        "uri": ' '
    },
    "sflowCollectors": [{
        "name": "C1",
        "collectorEnabled": True,
        "ipAddress": "192.168.147.210",
        "maxDatagramSize": "400",
        "maxHeaderSize": "128",
        "port": "6343",
        "collectorId": 1
    },
        {
        "name": "C2",
        "collectorEnabled": True,
        "ipAddress": "192.168.147.190",
        "maxDatagramSize": "410",
        "maxHeaderSize": "128",
        "port": "6343",
        "collectorId": 2
    },
        {
        "name": "C3",
        "collectorEnabled": True,
        "ipAddress": "192.168.146.109",
        "maxDatagramSize": "420",
        "maxHeaderSize": "128",
        "port": "6343",
        "collectorId": 3
    }],
    "sflowPorts": [{
        "portName": "Q2:1",
        "collectorId": "1",
        "icmName": "SGH721WSR0, interconnect 3",
        "bayNumber": 3,
        "enclosureIndex": 1,
        "sflowConfigurationModes": [{
            "configurationMode": "Polling",
            "pollingInterval": "20"
        },
            {
            "configurationMode": "Sampling",
            "direction": "BOTH",
            "samplingRate": "330"
        }]
    },
        {
        "portName": "Q1:1",
        "collectorId": 1,
        "icmName": "SGH721WSR0, interconnect 3",
        "bayNumber": 3,
        "enclosureIndex": 1,
        "sflowConfigurationModes": [{
            "configurationMode": "Polling",
            "pollingInterval": "20"
        },
            {
            "configurationMode": "Sampling",
            "direction": "BOTH",
            "samplingRate": "300"
        }]
    }]
}}

edit_li_add_more_uplinkports = {'sflowconfiguration': {
    "type": "sflow-configuration",
    "category": "sflow-configuration",
    "enabled": True,
    "sflowAgents": [{
        "ipMode": "Static",
        "ipAddr": "192.168.145.43",
        "subnetMask": "255.255.248.0"
    }],
    "sflowNetwork": {
        "name": "Ethernet_1000",
        "uri": ' '
    },
    "sflowCollectors": [{
        "name": "C1",
        "collectorEnabled": True,
        "ipAddress": "192.168.147.210",
        "maxDatagramSize": "1400",
        "maxHeaderSize": "128",
        "port": "6343",
        "collectorId": 1
    },
        {
        "name": "C2",
        "collectorEnabled": True,
        "ipAddress": "192.168.147.211",
        "maxDatagramSize": "1400",
        "maxHeaderSize": "128",
        "port": "6343",
        "collectorId": 2
    },
        {
        "name": "C3",
        "collectorEnabled": True,
        "ipAddress": "192.168.147.212",
        "maxDatagramSize": "1400",
        "maxHeaderSize": "128",
        "port": "6343",
        "collectorId": 3
    }],
    "sflowPorts": [{
        "portName": "Q2:1",
        "collectorId": "1",
        "icmName": "SGH721WSR0, interconnect 3",
        "bayNumber": 3,
        "enclosureIndex": 1,
        "sflowConfigurationModes": [{
            "configurationMode": "Polling",
            "pollingInterval": "20"
        },
            {
            "configurationMode": "Sampling",
            "direction": "BOTH",
            "samplingRate": "330"
        }]
    },
        {
        "portName": "Q2:1",
        "collectorId": "2",
        "icmName": "SGH721WSR0, interconnect 6",
        "bayNumber": 6,
        "enclosureIndex": 1,
        "sflowConfigurationModes": [{
            "configurationMode": "Polling",
            "pollingInterval": "20"
        },
            {
            "configurationMode": "Sampling",
            "direction": "BOTH",
            "samplingRate": "330"
        }]
    },
        {
        "portName": "Q3:1",
        "collectorId": "1",
        "icmName": "SGH721WSR0, interconnect 3",
        "bayNumber": 3,
        "enclosureIndex": 1,
        "sflowConfigurationModes": [{
            "configurationMode": "Polling",
            "pollingInterval": "20"
        },
            {
            "configurationMode": "Sampling",
            "direction": "BOTH",
            "samplingRate": "330"
        }]
    },
        {
        "portName": "Q4:1",
        "collectorId": "1",
        "icmName": "SGH721WSR0, interconnect 3",
        "bayNumber": 3,
        "enclosureIndex": 1,
        "sflowConfigurationModes": [{
            "configurationMode": "Polling",
            "pollingInterval": "20"
        },
            {
            "configurationMode": "Sampling",
            "direction": "BOTH",
            "samplingRate": "330"
        }]
    },
        {
        "portName": "Q1:1",
        "collectorId": "1",
        "icmName": "SGH721WSR0, interconnect 3",
        "bayNumber": 3,
        "enclosureIndex": 1,
        "sflowConfigurationModes": [{
            "configurationMode": "Polling",
            "pollingInterval": "20"
        },
            {
            "configurationMode": "Sampling",
            "direction": "BOTH",
            "samplingRate": "300"
        }]
    },
        {
        "portName": "Q1:1",
        "collectorId": "2",
        "icmName": "SGH721WSR0, interconnect 6",
        "bayNumber": 6,
        "enclosureIndex": 1,
        "sflowConfigurationModes": [{
            "configurationMode": "Polling",
            "pollingInterval": "20"
        },
            {
            "configurationMode": "Sampling",
            "direction": "BOTH",
            "samplingRate": "300"
        }]
    }
    ]
}}

edit_li_change_collectorid = {'sflowconfiguration': {
    "type": "sflow-configuration",
    "category": "sflow-configuration",
    "enabled": True,
    "sflowAgents": [{
        "ipMode": "Static",
        "ipAddr": "192.168.145.43",
        "subnetMask": "255.255.248.0"
    }],
    "sflowNetwork": {
        "name": "Ethernet_1000",
        "uri": ' '
    },
    "sflowCollectors": [{
        "name": "C1",
        "collectorEnabled": True,
        "ipAddress": "192.168.147.210",
        "maxDatagramSize": "1400",
        "maxHeaderSize": "128",
        "port": "6343",
        "collectorId": 1
    },
        {
        "name": "C2",
        "collectorEnabled": True,
        "ipAddress": "192.168.147.211",
        "maxDatagramSize": "1400",
        "maxHeaderSize": "128",
        "port": "6343",
        "collectorId": 2
    },
        {
        "name": "C3",
        "collectorEnabled": True,
        "ipAddress": "192.168.147.212",
        "maxDatagramSize": "1400",
        "maxHeaderSize": "128",
        "port": "6343",
        "collectorId": 3
    }],
    "sflowPorts": [{
        "portName": "Q2:1",
        "collectorId": "2",
        "icmName": "SGH721WSR0, interconnect 3",
        "bayNumber": 3,
        "enclosureIndex": 1,
        "sflowConfigurationModes": [{
            "configurationMode": "Polling",
            "pollingInterval": "20"
        },
            {
            "configurationMode": "Sampling",
            "direction": "BOTH",
            "samplingRate": "330"
        }]
    },
        {
        "portName": "Q2:1",
        "collectorId": "1",
        "icmName": "SGH721WSR0, interconnect 6",
        "bayNumber": 6,
        "enclosureIndex": 1,
        "sflowConfigurationModes": [{
            "configurationMode": "Polling",
            "pollingInterval": "20"
        },
            {
            "configurationMode": "Sampling",
            "direction": "BOTH",
            "samplingRate": "330"
        }]
    },
        {
        "portName": "Q1:1",
        "collectorId": "1",
        "icmName": "SGH721WSR0, interconnect 3",
        "bayNumber": 3,
        "enclosureIndex": 1,
        "sflowConfigurationModes": [{
            "configurationMode": "Polling",
            "pollingInterval": "20"
        },
            {
            "configurationMode": "Sampling",
            "direction": "BOTH",
            "samplingRate": "300"
        }]
    },
        {
        "portName": "Q1:1",
        "collectorId": "2",
        "icmName": "SGH721WSR0, interconnect 6",
        "bayNumber": 6,
        "enclosureIndex": 1,
        "sflowConfigurationModes": [{
            "configurationMode": "Polling",
            "pollingInterval": "20"
        },
            {
            "configurationMode": "Sampling",
            "direction": "BOTH",
            "samplingRate": "300"
        }]
    }
    ]
}}

edit_li_disable_collector = {'sflowconfiguration': {
    "type": "sflow-configuration",
    "category": "sflow-configuration",
    "enabled": True,
    "sflowAgents": [{
        "ipMode": "Static",
        "ipAddr": "192.168.145.43",
        "subnetMask": "255.255.248.0"
    }],
    "sflowNetwork": {
        "name": "Ethernet_1000",
        "uri": ' '
    },
    "sflowCollectors": [{
        "name": "C1",
        "collectorEnabled": False,
        "ipAddress": "192.168.147.210",
        "maxDatagramSize": "1400",
        "maxHeaderSize": "128",
        "port": "6343",
        "collectorId": 1
    },
        {
        "name": "C2",
        "collectorEnabled": True,
        "ipAddress": "192.168.147.211",
        "maxDatagramSize": "1400",
        "maxHeaderSize": "128",
        "port": "6343",
        "collectorId": 2
    },
        {
        "name": "C3",
        "collectorEnabled": False,
        "ipAddress": "192.168.147.212",
        "maxDatagramSize": "1400",
        "maxHeaderSize": "128",
        "port": "6343",
        "collectorId": 3
    }],
    "sflowPorts": [{
        "portName": "Q2:1",
        "collectorId": "2",
        "icmName": "SGH721WSR0, interconnect 3",
        "bayNumber": 3,
        "enclosureIndex": 1,
        "sflowConfigurationModes": [{
            "configurationMode": "Polling",
            "pollingInterval": "20"
        },
            {
            "configurationMode": "Sampling",
            "direction": "BOTH",
            "samplingRate": "330"
        }]
    },
        {
        "portName": "Q1:1",
        "collectorId": 1,
        "icmName": "SGH721WSR0, interconnect 3",
        "bayNumber": 3,
        "enclosureIndex": 1,
        "sflowConfigurationModes": [{
            "configurationMode": "Polling",
            "pollingInterval": "20"
        },
            {
            "configurationMode": "Sampling",
            "direction": "BOTH",
            "samplingRate": "300"
        }]
    }]
}}

edit_li_max_datagramsize = {'sflowconfiguration': {
    "type": "sflow-configuration",
    "category": "sflow-configuration",
    "enabled": True,
    "sflowAgents": [{
        "ipMode": "Static",
        "ipAddr": "192.168.145.43",
        "subnetMask": "255.255.248.0"
    }],
    "sflowNetwork": {
        "name": "Ethernet_1000",
        "uri": ' '
    },
    "sflowCollectors": [{
        "name": "C1",
        "collectorEnabled": False,
        "ipAddress": "192.168.147.210",
        "maxDatagramSize": "5000",
        "maxHeaderSize": "128",
        "port": "6343",
        "collectorId": 1
    },
        {
        "name": "C2",
        "collectorEnabled": True,
        "ipAddress": "192.168.147.211",
        "maxDatagramSize": "9000",
        "maxHeaderSize": "128",
        "port": "6343",
        "collectorId": 2
    },
        {
        "name": "C3",
        "collectorEnabled": False,
        "ipAddress": "192.168.147.212",
        "maxDatagramSize": "3800",
        "maxHeaderSize": "128",
        "port": "6343",
        "collectorId": 3
    }],
    "sflowPorts": [{
        "portName": "Q2:1",
        "collectorId": "2",
        "icmName": "SGH721WSR0, interconnect 3",
        "bayNumber": 3,
        "enclosureIndex": 1,
        "sflowConfigurationModes": [{
            "configurationMode": "Polling",
            "pollingInterval": "20"
        },
            {
            "configurationMode": "Sampling",
            "direction": "BOTH",
            "samplingRate": "330"
        }]
    },
        {
        "portName": "Q1:1",
        "collectorId": 1,
        "icmName": "SGH721WSR0, interconnect 3",
        "bayNumber": 3,
        "enclosureIndex": 1,
        "sflowConfigurationModes": [{
            "configurationMode": "Polling",
            "pollingInterval": "20"
        },
            {
            "configurationMode": "Sampling",
            "direction": "BOTH",
            "samplingRate": "300"
        }]
    }]
}}

edit_li_max_headersize = {'sflowconfiguration': {
    "type": "sflow-configuration",
    "category": "sflow-configuration",
    "enabled": True,
    "sflowAgents": [{
        "ipMode": "Static",
        "ipAddr": "192.168.145.43",
        "subnetMask": "255.255.248.0"
    }],
    "sflowNetwork": {
        "name": "Ethernet_1000",
        "uri": ' '
    },
    "sflowCollectors": [{
        "name": "C1",
        "collectorEnabled": False,
        "ipAddress": "192.168.147.210",
        "maxDatagramSize": "5000",
        "maxHeaderSize": "256",
        "port": "6343",
        "collectorId": 1
    },
        {
        "name": "C2",
        "collectorEnabled": True,
        "ipAddress": "192.168.147.211",
        "maxDatagramSize": "9000",
        "maxHeaderSize": "1024",
        "port": "6343",
        "collectorId": 2
    },
        {
        "name": "C3",
        "collectorEnabled": False,
        "ipAddress": "192.168.147.212",
        "maxDatagramSize": "3800",
        "maxHeaderSize": "128",
        "port": "6343",
        "collectorId": 3
    }],
    "sflowPorts": [{
        "portName": "Q2:1",
        "collectorId": 2,
        "icmName": "SGH721WSR0, interconnect 3",
        "bayNumber": 3,
        "enclosureIndex": 1,
        "sflowConfigurationModes": [{
            "configurationMode": "Polling",
            "pollingInterval": 20
        },
            {
            "configurationMode": "Sampling",
            "direction": "BOTH",
            "samplingRate": 330
        }]
    },
        {
        "portName": "Q1:1",
        "collectorId": 1,
        "icmName": "SGH721WSR0, interconnect 3",
        "bayNumber": 3,
        "enclosureIndex": 1,
        "sflowConfigurationModes": [{
            "configurationMode": "Polling",
            "pollingInterval": 20
        },
            {
            "configurationMode": "Sampling",
            "direction": "BOTH",
            "samplingRate": 300
        }]
    }]
}}

edit_li_enable_one_collector = {'sflowconfiguration': {
    "type": "sflow-configuration",
    "category": "sflow-configuration",
    "enabled": True,
    "sflowAgents": [{
        "ipMode": "Static",
        "ipAddr": "192.168.145.43",
        "subnetMask": "255.255.248.0"
    }],
    "sflowNetwork": {
        "name": "Ethernet_1000",
        "uri": ' '
    },
    "sflowCollectors": [{
        "name": "C1",
        "collectorEnabled": False,
        "ipAddress": "192.168.147.210",
        "maxDatagramSize": "5000",
        "maxHeaderSize": "256",
        "port": "6343",
        "collectorId": 1
    },
        {
        "name": "C2",
        "collectorEnabled": True,
        "ipAddress": "192.168.147.211",
        "maxDatagramSize": "9000",
        "maxHeaderSize": "1024",
        "port": "6343",
        "collectorId": 2
    },
        {
        "name": "C3",
        "collectorEnabled": False,
        "ipAddress": "192.168.147.212",
        "maxDatagramSize": "3800",
        "maxHeaderSize": "128",
        "port": "6343",
        "collectorId": 3
    }],
    "sflowPorts": [{
        "portName": "Q2:1",
        "collectorId": "2",
        "icmName": "SGH721WSR0, interconnect 3",
        "bayNumber": 3,
        "enclosureIndex": 1,
        "sflowConfigurationModes": [{
            "configurationMode": "Polling",
            "pollingInterval": "20"
        },
            {
            "configurationMode": "Sampling",
            "direction": "BOTH",
            "samplingRate": "330"
        }]
    },
        {
        "portName": "Q1:1",
        "collectorId": 1,
        "icmName": "SGH721WSR0, interconnect 3",
        "bayNumber": 3,
        "enclosureIndex": 1,
        "sflowConfigurationModes": [{
            "configurationMode": "Polling",
            "pollingInterval": "20"
        },
            {
            "configurationMode": "Sampling",
            "direction": "BOTH",
            "samplingRate": "300"
        }]
    }]
}}

edit_li_disabled_collectors = {'sflowconfiguration': {
    "type": "sflow-configuration",
    "category": "sflow-configuration",
    "enabled": True,
    "sflowAgents": [{
        "ipMode": "Static",
        "ipAddr": "192.168.145.43",
        "subnetMask": "255.255.248.0"
    }],
    "sflowNetwork": {
        "name": "Ethernet_1000",
        "uri": ' '
    },
    "sflowCollectors": [{
        "name": "C1",
        "collectorEnabled": False,
        "ipAddress": "192.168.147.210",
        "maxDatagramSize": "5000",
        "maxHeaderSize": "256",
        "port": "6343",
        "collectorId": 1
    },
        {
        "name": "C2",
        "collectorEnabled": False,
        "ipAddress": "192.168.147.211",
        "maxDatagramSize": "9000",
        "maxHeaderSize": "1024",
        "port": "6343",
        "collectorId": 2
    },
        {
        "name": "C3",
        "collectorEnabled": False,
        "ipAddress": "192.168.147.212",
        "maxDatagramSize": "3800",
        "maxHeaderSize": "128",
        "port": "6343",
        "collectorId": 3
    }],
    "sflowPorts": [{
        "portName": "Q2:1",
        "collectorId": "2",
        "icmName": "SGH721WSR0, interconnect 3",
        "bayNumber": 3,
        "enclosureIndex": 1,
        "sflowConfigurationModes": [{
            "configurationMode": "Polling",
            "pollingInterval": "20"
        },
            {
            "configurationMode": "Sampling",
            "direction": "BOTH",
            "samplingRate": "330"
        }]
    },
        {
        "portName": "Q1:1",
        "collectorId": 1,
        "icmName": "SGH721WSR0, interconnect 3",
        "bayNumber": 3,
        "enclosureIndex": 1,
        "sflowConfigurationModes": [{
            "configurationMode": "Polling",
            "pollingInterval": "20"
        },
            {
            "configurationMode": "Sampling",
            "direction": "BOTH",
            "samplingRate": "300"
        }]
    }]
}}

edit_li_polling_collector = {'sflowconfiguration': {
    "type": "sflow-configuration",
    "category": "sflow-configuration",
    "enabled": True,
    "sflowAgents": [{
        "ipMode": "Static",
        "ipAddr": "192.168.145.43",
        "subnetMask": "255.255.248.0"
    }],
    "sflowNetwork": {
        "name": "Ethernet_1000",
        "uri": ' '
    },
    "sflowCollectors": [{
        "name": "C1",
        "collectorEnabled": True,
        "ipAddress": "192.168.147.210",
        "maxDatagramSize": "5000",
        "maxHeaderSize": "256",
        "port": "6343",
        "collectorId": 1
    }
    ],
    "sflowPorts": [{
        "portName": "Q2:1",
        "collectorId": "1",
        "icmName": "SGH721WSR0, interconnect 3",
        "bayNumber": 3,
        "enclosureIndex": 1,
        "sflowConfigurationModes": [
            {
                "configurationMode": "Polling",
                "pollingInterval": "20"
            }]
    }]
}}

edit_li_polling_changing_ip_of_collector = {'sflowconfiguration': {
    "type": "sflow-configuration",
    "category": "sflow-configuration",
    "enabled": True,
    "sflowAgents": [{
        "ipMode": "Static",
        "ipAddr": "192.168.145.43",
        "subnetMask": "255.255.248.0"
    }],
    "sflowNetwork": {
        "name": "Ethernet_1000",
        "uri": ' '
    },
    "sflowCollectors": [{
        "name": "C1",
        "collectorEnabled": False,
        "ipAddress": "192.168.147.213",
        "maxDatagramSize": 5000,
        "maxHeaderSize": 256,
        "port": 6343,
        "collectorId": 1
    }
    ],
    "sflowPorts": [{
        "portName": "Q2:1",
        "collectorId": 1,
        "icmName": "SGH721WSR0, interconnect 3",
        "bayNumber": 3,
        "enclosureIndex": 1,
        "sflowConfigurationModes": [
            {
                "configurationMode": "Polling",
                "pollingInterval": "20"
            }]
    }]
}}

edit_li_sampling_collector = {'sflowconfiguration': {
    "type": "sflow-configuration",
    "category": "sflow-configuration",
    "enabled": True,
    "sflowAgents": [{
        "ipMode": "Static",
        "ipAddr": "192.168.145.43",
        "subnetMask": "255.255.248.0"
    }],
    "sflowNetwork": {
        "name": "Ethernet_1000",
        "uri": ' '
    },
    "sflowCollectors": [{
        "name": "C2",
        "collectorEnabled": False,
        "ipAddress": "192.168.147.190",
        "maxDatagramSize": 9000,
        "maxHeaderSize": 128,
        "port": 6343,
        "collectorId": 2
    }
    ],
    "sflowPorts": [{
        "portName": "Q2:1",
        "collectorId": 2,
        "icmName": "SGH721WSR0, interconnect 3",
        "bayNumber": 3,
        "enclosureIndex": 1,
        "sflowConfigurationModes": [
            {
                "configurationMode": "Sampling",
                "direction": "BOTH",
                "samplingRate": 256
            }]
    }]
}}


edit_li_sampling_changing_ip_of_collector = {'sflowconfiguration': {
    "type": "sflow-configuration",
    "category": "sflow-configuration",
    "enabled": True,
    "sflowAgents": [{
        "ipMode": "Static",
        "ipAddr": "192.168.145.43",
        "subnetMask": "255.255.248.0"
    }],
    "sflowNetwork": {
        "name": "Ethernet_1000",
        "uri": ' '
    },
    "sflowCollectors": [{
        "name": "C1",
        "collectorEnabled": False,
        "ipAddress": "192.168.147.215",
        "maxDatagramSize": "5000",
        "maxHeaderSize": "256",
        "port": "6343",
        "collectorId": 1
    }
    ],
    "sflowPorts": [{
        "portName": "Q2:1",
        "collectorId": "1",
        "icmName": "SGH721WSR0, interconnect 3",
        "bayNumber": 3,
        "enclosureIndex": 1,
        "sflowConfigurationModes": [
            {
                "configurationMode": "Sampling",
                "direction": "BOTH",
                "samplingRate": "300"
            }]
    }]
}}

edit_li_sampling_changing_port_of_collector = {'sflowconfiguration': {
    "type": "sflow-configuration",
    "category": "sflow-configuration",
    "enabled": True,
    "sflowAgents": [{
        "ipMode": "Static",
        "ipAddr": "192.168.145.43",
        "subnetMask": "255.255.248.0"
    }],
    "sflowNetwork": {
        "name": "Ethernet_1000",
        "uri": ' '
    },
    "sflowCollectors": [{
        "name": "C1",
        "collectorEnabled": False,
        "ipAddress": "192.168.147.215",
        "maxDatagramSize": "5000",
        "maxHeaderSize": "256",
        "port": "49155",
        "collectorId": 1
    },
        {
        "name": "C2",
        "collectorEnabled": False,
        "ipAddress": "192.168.147.217",
        "maxDatagramSize": "5000",
        "maxHeaderSize": "256",
        "port": "49155",
        "collectorId": 2
    }
    ],
    "sflowPorts": [{
        "portName": "Q2:1",
        "collectorId": "1",
        "icmName": "SGH721WSR0, interconnect 3",
        "bayNumber": 3,
        "enclosureIndex": 1,
        "sflowConfigurationModes": [
            {
                "configurationMode": "Sampling",
                "direction": "BOTH",
                "samplingRate": "300"
            }]
    }]
}}

edit_li_removing_collector = {'sflowconfiguration': {
    "type": "sflow-configuration",
    "category": "sflow-configuration",
    "enabled": True,
    "sflowAgents": [{
        "ipMode": "Static",
        "ipAddr": "192.168.145.43",
        "subnetMask": "255.255.248.0"
    }],
    "sflowNetwork": {
        "name": "Ethernet_1000",
        "uri": ' '
    },
    "sflowCollectors": [{
        "name": "C2",
        "collectorEnabled": False,
        "ipAddress": "192.168.147.215",
        "maxDatagramSize": "5000",
        "maxHeaderSize": "256",
        "port": "49155",
        "collectorId": 2
    }
    ],
    "sflowPorts": [{
        "portName": "Q2:1",
        "collectorId": "1",
        "icmName": "SGH721WSR0, interconnect 3",
        "bayNumber": 3,
        "enclosureIndex": 1,
        "sflowConfigurationModes": [
            {
                "configurationMode": "Sampling",
                "direction": "BOTH",
                "samplingRate": "300"
            }]
    }]
}}

edit_li_changing_mode_of_sflow = {'sflowconfiguration': {
    "type": "sflow-configuration",
    "category": "sflow-configuration",
    "enabled": True,
    "sflowAgents": [{
        "ipMode": "DHCP"
    }],
    "sflowNetwork": {
        "name": "Ethernet_1000",
        "uri": ' '
    },
    "sflowCollectors": [{
        "name": "C1",
        "collectorEnabled": False,
        "ipAddress": "192.168.147.215",
        "maxDatagramSize": "5000",
        "maxHeaderSize": "256",
        "port": "49155",
        "collectorId": 1
    },
        {
        "name": "C2",
        "collectorEnabled": False,
        "ipAddress": "192.168.147.217",
        "maxDatagramSize": "5000",
        "maxHeaderSize": "256",
        "port": "49155",
        "collectorId": 2
    }
    ],
    "sflowPorts": [{
        "portName": "Q2:1",
        "collectorId": "1",
        "icmName": "SGH721WSR0, interconnect 3",
        "bayNumber": 3,
        "enclosureIndex": 1,
        "sflowConfigurationModes": [
            {
                "configurationMode": "Sampling",
                "direction": "BOTH",
                "samplingRate": "300"
            }]
    }]
}}

edit_li_adding_tunnel_nw = {'sflowconfiguration': {
    "type": "sflow-configuration",
    "category": "sflow-configuration",
    "enabled": True,
    "sflowAgents": [{
        "ipMode": "DHCP"
    }],
    "sflowNetwork": {
        "name": "tunnel_nw",
        "uri": ' '
    },
    "sflowCollectors": [{
        "name": "C1",
        "collectorEnabled": False,
        "ipAddress": "192.168.147.215",
        "maxDatagramSize": "5000",
        "maxHeaderSize": "256",
        "port": "49155",
        "collectorId": 1
    },
        {
        "name": "C2",
        "collectorEnabled": False,
        "ipAddress": "192.168.147.217",
        "maxDatagramSize": "5000",
        "maxHeaderSize": "256",
        "port": "49155",
        "collectorId": 2
    }
    ],
    "sflowPorts": [{
        "portName": "Q2:1",
        "collectorId": "1",
        "icmName": "SGH721WSR0, interconnect 3",
        "bayNumber": 3,
        "enclosureIndex": 1,
        "sflowConfigurationModes": [
            {
                "configurationMode": "Sampling",
                "direction": "BOTH",
                "samplingRate": "300"
            }]
    }]
}}

edit_li_without_sampling_interval = {'sflowconfiguration': {
    "type": "sflow-configuration",
    "category": "sflow-configuration",
    "enabled": True,
    "sflowAgents": [{
        "ipMode": "DHCP"
    }],
    "sflowNetwork": {
        "name": "Ethernet_1000",
        "uri": ' '
    },
    "sflowCollectors": [{
        "name": "C1",
        "collectorEnabled": False,
        "ipAddress": "192.168.147.215",
        "maxDatagramSize": "5000",
        "maxHeaderSize": "256",
        "port": "49155",
        "collectorId": 1
    },
        {
        "name": "C2",
        "collectorEnabled": False,
        "ipAddress": "192.168.147.217",
        "maxDatagramSize": "5000",
        "maxHeaderSize": "256",
        "port": "49155",
        "collectorId": 2
    }
    ],
    "sflowPorts": [{
        "portName": "Q2:1",
        "collectorId": "1",
        "icmName": "SGH721WSR0, interconnect 3",
        "bayNumber": 3,
        "enclosureIndex": 1,
        "sflowConfigurationModes": [
            {
                "configurationMode": "Sampling",
                "direction": "BOTH"
            }]
    }]
}}

edit_li_without_polling_interval = {'sflowconfiguration': {
    "type": "sflow-configuration",
    "category": "sflow-configuration",
    "enabled": True,
    "sflowAgents": [{
        "ipMode": "DHCP"
    }],
    "sflowNetwork": {
        "name": "Ethernet_1000",
        "uri": ' '
    },
    "sflowCollectors": [{
        "name": "C1",
        "collectorEnabled": False,
        "ipAddress": "192.168.147.215",
        "maxDatagramSize": "5000",
        "maxHeaderSize": "256",
        "port": "49155",
        "collectorId": 1
    },
        {
        "name": "C2",
        "collectorEnabled": False,
        "ipAddress": "192.168.147.217",
        "maxDatagramSize": "5000",
        "maxHeaderSize": "256",
        "port": "49155",
        "collectorId": 2
    }
    ],
    "sflowPorts": [{
        "portName": "Q2:1",
        "collectorId": "1",
        "icmName": "SGH721WSR0, interconnect 3",
        "bayNumber": 3,
        "enclosureIndex": 1,
        "sflowConfigurationModes": [{
            "configurationMode": "Polling"
        }]
    }]
}}

edit_li_duplicate_collectorname = {'sflowconfiguration': {
    "type": "sflow-configuration",
    "category": "sflow-configuration",
    "enabled": True,
    "sflowAgents": [{
        "ipMode": "Static",
        "ipAddr": "192.168.145.43",
        "subnetMask": "255.255.248.0"
    }],
    "sflowNetwork": {
        "name": "Ethernet_1000",
        "uri": ' '
    },
    "sflowCollectors": [{
        "name": "C1",
        "collectorEnabled": False,
        "ipAddress": "192.168.147.215",
        "maxDatagramSize": "5000",
        "maxHeaderSize": "256",
        "port": "49155",
        "collectorId": 1
    },
        {
        "name": "C1",
        "collectorEnabled": False,
        "ipAddress": "192.168.147.217",
        "maxDatagramSize": "5000",
        "maxHeaderSize": "256",
        "port": "49155",
        "collectorId": 2
    }
    ],
    "sflowPorts": [{
        "portName": "Q2:1",
        "collectorId": "1",
        "icmName": "SGH721WSR0, interconnect 3",
        "bayNumber": 3,
        "enclosureIndex": 1,
        "sflowConfigurationModes": [
            {
                "configurationMode": "Sampling",
                "direction": "BOTH",
                "samplingRate": "300"
            }]
    }]
}}


edit_li_invalid_static_ip = {'sflowconfiguration': {
    "type": "sflow-configuration",
    "category": "sflow-configuration",
    "enabled": True,
    "sflowAgents": [{
        "ipMode": "Static",
        "ipAddr": "192.168.145.43.12",
        "subnetMask": "255.255.248.0"
    }],
    "sflowNetwork": {
        "name": "Ethernet_1000",
        "uri": ' '
    },
    "sflowCollectors": [{
        "name": "C1",
        "collectorEnabled": True,
        "ipAddress": "192.168.147.210",
        "maxDatagramSize": "1400",
        "maxHeaderSize": "128",
        "port": "6343",
        "collectorId": 1
    }],
    "sflowPorts": [{
        "portName": "Q2:1",
        "collectorId": "1",
        "icmName": "SGH721WSR0, interconnect 3",
        "bayNumber": 3,
        "enclosureIndex": 1,
        "sflowConfigurationModes": [{
            "configurationMode": "Polling",
            "pollingInterval": "20"
        },
            {
            "configurationMode": "Sampling",
            "direction": "BOTH",
            "samplingRate": "330"
        }]
    },
        {
        "portName": "Q1:1",
        "collectorId": 1,
        "icmName": "SGH721WSR0, interconnect 3",
        "bayNumber": 3,
        "enclosureIndex": 1,
        "sflowConfigurationModes": [{
            "configurationMode": "Polling",
            "pollingInterval": "20"
        },
            {
            "configurationMode": "Sampling",
            "direction": "BOTH",
            "samplingRate": "300"
        }]
    }]
}}

edit_li_invalid_sampling_interval = {'sflowconfiguration': {
    "type": "sflow-configuration",
    "category": "sflow-configuration",
    "enabled": True,
    "sflowAgents": [{
        "ipMode": "DHCP"
    }],
    "sflowNetwork": {
        "name": "Ethernet_1000",
        "uri": ' '
    },
    "sflowCollectors": [{
        "name": "C1",
        "collectorEnabled": False,
        "ipAddress": "192.168.147.215",
        "maxDatagramSize": "5000",
        "maxHeaderSize": "256",
        "port": "49155",
        "collectorId": 1
    },
        {
        "name": "C2",
        "collectorEnabled": False,
        "ipAddress": "192.168.147.217",
        "maxDatagramSize": "5000",
        "maxHeaderSize": "256",
        "port": "49155",
        "collectorId": 2
    }
    ],
    "sflowPorts": [{
        "portName": "Q2:1",
        "collectorId": "1",
        "icmName": "SGH721WSR0, interconnect 3",
        "bayNumber": 3,
        "enclosureIndex": 1,
        "sflowConfigurationModes": [
            {
                "configurationMode": "Sampling",
                "direction": "BOTH",
                "samplingRate": "16777217"
            }]
    }]
}}

edit_li_invalid_polling_interval = {'sflowconfiguration': {
    "type": "sflow-configuration",
    "category": "sflow-configuration",
    "enabled": True,
    "sflowAgents": [{
        "ipMode": "DHCP"
    }],
    "sflowNetwork": {
        "name": "Ethernet_1000",
        "uri": ' '
    },
    "sflowCollectors": [{
        "name": "C1",
        "collectorEnabled": False,
        "ipAddress": "192.168.147.215",
        "maxDatagramSize": "5000",
        "maxHeaderSize": "256",
        "port": "49155",
        "collectorId": 1
    },
        {
        "name": "C2",
        "collectorEnabled": False,
        "ipAddress": "192.168.147.217",
        "maxDatagramSize": "5000",
        "maxHeaderSize": "256",
        "port": "49155",
        "collectorId": 2
    }
    ],
    "sflowPorts": [{
        "portName": "Q2:1",
        "collectorId": "1",
        "icmName": "SGH721WSR0, interconnect 3",
        "bayNumber": 3,
        "enclosureIndex": 1,
        "sflowConfigurationModes": [{
            "configurationMode": "Polling",
            "pollingInterval": "11"
        }]
    }]
}}

edit_li_only_ingress_packets = {'sflowconfiguration': {
    "type": "sflow-configuration",
    "category": "sflow-configuration",
    "enabled": True,
    "sflowAgents": [{
        "ipMode": "Static",
        "ipAddr": "192.168.145.43",
        "subnetMask": "255.255.248.0"
    }],
    "sflowNetwork": {
        "name": "Ethernet_1000",
        "uri": ' '
    },
    "sflowCollectors": [{
        "name": "C1",
        "collectorEnabled": True,
        "ipAddress": "192.168.147.210",
        "maxDatagramSize": "1400",
        "maxHeaderSize": "128",
        "port": "6343",
        "collectorId": 1
    },
        {
        "name": "C2",
        "collectorEnabled": True,
        "ipAddress": "192.168.147.211",
        "maxDatagramSize": "1400",
        "maxHeaderSize": "128",
        "port": "6343",
        "collectorId": 2
    },
        {
        "name": "C3",
        "collectorEnabled": True,
        "ipAddress": "192.168.147.212",
        "maxDatagramSize": "1400",
        "maxHeaderSize": "128",
        "port": "6343",
        "collectorId": 3
    }],
    "sflowPorts": [
        {
            "portName": "Q1:1",
            "collectorId": 1,
            "icmName": "SGH721WSR0, interconnect 3",
            "bayNumber": 3,
            "enclosureIndex": 1,
            "sflowConfigurationModes": [{
                "configurationMode": "Polling",
                "pollingInterval": "20"
            },
                {
                "configurationMode": "Sampling",
                "direction": "INGRESS",
                "samplingRate": "5000"
            }]
        }]
}}

edit_li_only_egress_packets = {'sflowconfiguration': {
    "type": "sflow-configuration",
    "category": "sflow-configuration",
    "enabled": True,
    "sflowAgents": [{
        "ipMode": "Static",
        "ipAddr": "192.168.145.43",
        "subnetMask": "255.255.248.0"
    }],
    "sflowNetwork": {
        "name": "Ethernet_1000",
        "uri": ' '
    },
    "sflowCollectors": [{
        "name": "C1",
        "collectorEnabled": True,
        "ipAddress": "192.168.147.210",
        "maxDatagramSize": "1400",
        "maxHeaderSize": "128",
        "port": "6343",
        "collectorId": 1
    },
        {
        "name": "C2",
        "collectorEnabled": True,
        "ipAddress": "192.168.147.211",
        "maxDatagramSize": "1400",
        "maxHeaderSize": "128",
        "port": "6343",
        "collectorId": 2
    },
        {
        "name": "C3",
        "collectorEnabled": True,
        "ipAddress": "192.168.147.212",
        "maxDatagramSize": "1400",
        "maxHeaderSize": "128",
        "port": "6343",
        "collectorId": 3
    }],
    "sflowPorts": [
        {
            "portName": "Q1:1",
            "collectorId": 1,
            "icmName": "SGH721WSR0, interconnect 3",
            "bayNumber": 3,
            "enclosureIndex": 1,
            "sflowConfigurationModes": [{
                "configurationMode": "Polling",
                "pollingInterval": "20"
            },
                {
                "configurationMode": "Sampling",
                "direction": "EGRESS",
                "samplingRate": "5000"
            }]
        }]
}}

edit_li_modify_ingress_rate = {'sflowconfiguration': {
    "type": "sflow-configuration",
    "category": "sflow-configuration",
    "enabled": True,
    "sflowAgents": [{
        "ipMode": "Static",
        "ipAddr": "192.168.145.43",
        "subnetMask": "255.255.248.0"
    }],
    "sflowNetwork": {
        "name": "Ethernet_1000",
        "uri": ' '
    },
    "sflowCollectors": [{
        "name": "C1",
        "collectorEnabled": True,
        "ipAddress": "192.168.147.210",
        "maxDatagramSize": "1400",
        "maxHeaderSize": "128",
        "port": "6343",
        "collectorId": 1
    },
        {
        "name": "C2",
        "collectorEnabled": True,
        "ipAddress": "192.168.147.211",
        "maxDatagramSize": "1400",
        "maxHeaderSize": "128",
        "port": "6343",
        "collectorId": 2
    },
        {
        "name": "C3",
        "collectorEnabled": True,
        "ipAddress": "192.168.147.212",
        "maxDatagramSize": "1400",
        "maxHeaderSize": "128",
        "port": "6343",
        "collectorId": 3
    }],
    "sflowPorts": [
        {
            "portName": "Q1:1",
            "collectorId": 1,
            "icmName": "SGH721WSR0, interconnect 3",
            "bayNumber": 3,
            "enclosureIndex": 1,
            "sflowConfigurationModes": [{
                "configurationMode": "Polling",
                "pollingInterval": "20"
            },
                {
                "configurationMode": "Sampling",
                "direction": "INGRESS",
                "samplingRate": "3000"
            }]
        }]
}}

edit_li_modify_egress_rate = {'sflowconfiguration': {
    "type": "sflow-configuration",
    "category": "sflow-configuration",
    "enabled": True,
    "sflowAgents": [{
        "ipMode": "Static",
        "ipAddr": "192.168.145.43",
        "subnetMask": "255.255.248.0"
    }],
    "sflowNetwork": {
        "name": "Ethernet_1000",
        "uri": ' '
    },
    "sflowCollectors": [{
        "name": "C1",
        "collectorEnabled": True,
        "ipAddress": "192.168.147.210",
        "maxDatagramSize": "1400",
        "maxHeaderSize": "128",
        "port": "6343",
        "collectorId": 1
    },
        {
        "name": "C2",
        "collectorEnabled": True,
        "ipAddress": "192.168.147.211",
        "maxDatagramSize": "1400",
        "maxHeaderSize": "128",
        "port": "6343",
        "collectorId": 2
    },
        {
        "name": "C3",
        "collectorEnabled": True,
        "ipAddress": "192.168.147.212",
        "maxDatagramSize": "1400",
        "maxHeaderSize": "128",
        "port": "6343",
        "collectorId": 3
    }],
    "sflowPorts": [
        {
            "portName": "Q1:1",
            "collectorId": 1,
            "icmName": "SGH721WSR0, interconnect 3",
            "bayNumber": 3,
            "enclosureIndex": 1,
            "sflowConfigurationModes": [{
                "configurationMode": "Polling",
                "pollingInterval": "20"
            },
                {
                "configurationMode": "Sampling",
                "direction": "EGRESS",
                "samplingRate": "1500"
            }]
        }]
}}

edit_li_add_morethan_3collector_ips = {'sflowconfiguration': {
    "type": "sflow-configuration",
    "category": "sflow-configuration",
    "enabled": True,
    "sflowAgents": [{
        "ipMode": "Static",
        "ipAddr": "192.168.145.43",
        "subnetMask": "255.255.248.0"
    }],
    "sflowNetwork": {
        "name": "Ethernet_1000",
        "uri": ' '
    },
    "sflowCollectors": [{
        "name": "C1",
        "collectorEnabled": True,
        "ipAddress": "192.168.147.210",
        "maxDatagramSize": "1400",
        "maxHeaderSize": "128",
        "port": "6343",
        "collectorId": 1
    },
        {
        "name": "C2",
        "collectorEnabled": True,
        "ipAddress": "192.168.147.211",
        "maxDatagramSize": "1400",
        "maxHeaderSize": "128",
        "port": "6343",
        "collectorId": 2
    },
        {
        "name": "C3",
        "collectorEnabled": True,
        "ipAddress": "192.168.147.212",
        "maxDatagramSize": "1400",
        "maxHeaderSize": "128",
        "port": "6343",
        "collectorId": 3
    },
        {
        "name": "C4",
        "collectorEnabled": True,
        "ipAddress": "192.168.147.213",
        "maxDatagramSize": "1400",
        "maxHeaderSize": "128",
        "port": "6343",
        "collectorId": 4
    }],
    "sflowPorts": [{
        "portName": "Q2:1",
        "collectorId": "1",
        "icmName": "SGH721WSR0, interconnect 3",
        "bayNumber": 3,
        "enclosureIndex": 1,
        "sflowConfigurationModes": [{
            "configurationMode": "Polling",
            "pollingInterval": "20"
        },
            {
            "configurationMode": "Sampling",
            "direction": "BOTH",
            "samplingRate": "330"
        }]
    },
        {
        "portName": "Q1:1",
        "collectorId": 1,
        "icmName": "SGH721WSR0, interconnect 3",
        "bayNumber": 3,
        "enclosureIndex": 1,
        "sflowConfigurationModes": [{
            "configurationMode": "Polling",
            "pollingInterval": "20"
        },
            {
            "configurationMode": "Sampling",
            "direction": "BOTH",
            "samplingRate": "300"
        }]
    }]
}}

edit_li_valid_ip_pool = {'sflowconfiguration': {
    "type": "sflow-configuration",
    "category": "sflow-configuration",
    "enabled": True,
    "sflowAgents": [{
        "ipMode": "IpPool"
    }],
    "sflowNetwork": {
        "name": "Ethernet_111",
        "uri": ' '
    },
    "sflowCollectors": [{
        "name": "C1",
        "collectorEnabled": True,
        "ipAddress": "192.168.147.210",
        "maxDatagramSize": "1400",
        "maxHeaderSize": "128",
        "port": "6343",
        "collectorId": 1
    }],
    "sflowPorts": [{
        "portName": "Q2:1",
        "collectorId": "1",
        "icmName": "SGH721WSR0, interconnect 3",
        "bayNumber": 3,
        "enclosureIndex": 1,
        "sflowConfigurationModes": [{
            "configurationMode": "Polling",
            "pollingInterval": "20"
        },
            {
            "configurationMode": "Sampling",
            "direction": "BOTH",
            "samplingRate": "330"
        }]
    },
        {
        "portName": "Q1:1",
        "collectorId": 1,
        "icmName": "SGH721WSR0, interconnect 3",
        "bayNumber": 3,
        "enclosureIndex": 1,
        "sflowConfigurationModes": [{
            "configurationMode": "Polling",
            "pollingInterval": "20"
        },
            {
            "configurationMode": "Sampling",
            "direction": "BOTH",
            "samplingRate": "300"
        }]
    }]
}}

sflow_lig = {"type": LIG_Version,
             "ethernetSettings": {"type": 'EthernetInterconnectSettingsV4', "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
             "description": None,
             "name": "LIG",
             "interconnectMapTemplate": icmap_ME,
             "enclosureType": "SY12000",
             "enclosureIndexes": [1],
             "interconnectBaySet": "3",
             "redundancyType": "Redundant",
             "internalNetworkUris": [],
             "snmpConfiguration": None,
             "qosConfiguration": None,
             "sflowConfiguration": {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "Ethernet_Vlan_1"},
                                    "sflowCollectors": [{"name": "C1", "collectorEnabled": True, "ipAddress": "192.168.147.210", "maxDatagramSize": "410", "maxHeaderSize": "128", "port": "6343", "collectorId": 1},
                                                        {"name": "C2", "collectorEnabled": True, "ipAddress": "192.168.147.190", "maxDatagramSize": "420", "maxHeaderSize": "128", "port": "6343", "collectorId": 2},
                                                        {"name": "C3", "collectorEnabled": True, "ipAddress": "192.168.146.109", "maxDatagramSize": "430", "maxHeaderSize": "128", "port": "6343", "collectorId": 3}],
                                    "sflowAgents": [{"ipMode": "Static"}],
                                    "sflowPorts": [{"portName": "Q1:1", "collectorId": "1", "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 3,
                                                    "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": "20", "pollingEnabled": True},
                                                                                                     {"configurationMode": "Sampling", "direction": "BOTH", "samplingRate": "256", "samplingEnabled": True}]},
                                                   {"portName": "Q1:1", "collectorId": "1", "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 6,
                                                    "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": "20", "pollingEnabled": True},
                                                                                                     {"configurationMode": "Sampling", "direction": "BOTH", "samplingRate": "256", "samplingEnabled": True}]},
                                                   {"portName": "Q2:1", "collectorId": "2", "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 3,
                                                    "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": "20", "pollingEnabled": True},
                                                                                                     {"configurationMode": "Sampling", "direction": "BOTH", "samplingRate": "256", "samplingEnabled": True}]},
                                                   {"portName": "Q2:1", "collectorId": "2", "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 6,
                                                    "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": "20", "pollingEnabled": True},
                                                                                                     {"configurationMode": "Sampling", "direction": "BOTH", "samplingRate": "256", "samplingEnabled": True}]},
                                                   {"portName": "d1", "collectorId": "3", "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 3,
                                                    "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": "20", "pollingEnabled": True},
                                                                                                     {"configurationMode": "Sampling", "direction": "BOTH", "samplingRate": "256", "samplingEnabled": True}]},
                                                   {"portName": "d1", "collectorId": "3", "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 6,
                                                    "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": "20", "pollingEnabled": True},
                                                                                                     {"configurationMode": "Sampling", "direction": "BOTH", "samplingRate": "256", "samplingEnabled": True}]},
                                                   ]
                                    },
             "uplinkSets": [{'name': 'us1', 'ethernetNetworkType': 'Untagged', 'networkType': 'Ethernet', 'networkUris': ["Untagged"], 'primaryPort': None, 'nativeNetworkUri': None, 'mode': 'Auto',
                             'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': 'Q1.1', 'speed': 'Auto'},
                                                        {'bay': '6', 'enclosure': '1', 'port': 'Q1.1', 'speed': 'Auto'}, ]},
                            {'name': 'us2', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ["Ethernet_1000", "Ethernet_Vlan_1", "Ethernet_111"], 'primaryPort': None, 'nativeNetworkUri': None, 'mode': 'Auto',
                             'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': 'Q2.1', 'speed': 'Auto'},
                                                        {'bay': '6', 'enclosure': '1', 'port': 'Q2.1', 'speed': 'Auto'}]}
                            ]}


sflow_lig_temp = {"type": LIG_Version,
                  "ethernetSettings": {"type": 'EthernetInterconnectSettingsV4', "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
                  "description": None,
                  "name": "LIG_1",
                  "interconnectMapTemplate": icmap_ME,
                  "enclosureType": "SY12000",
                  "enclosureIndexes": [1],
                  "interconnectBaySet": "3",
                  "redundancyType": "Redundant",
                  "internalNetworkUris": [],
                  "snmpConfiguration": None,
                  "qosConfiguration": None,
                  "sflowConfiguration": {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "Ethernet_111"},
                                         "sflowCollectors": [{"name": "C1", "collectorEnabled": True, "ipAddress": "192.168.147.210", "maxDatagramSize": "410", "maxHeaderSize": "128", "port": "6343", "collectorId": 1},
                                                             {"name": "C2", "collectorEnabled": True, "ipAddress": "192.168.147.190", "maxDatagramSize": "420", "maxHeaderSize": "128", "port": "6343", "collectorId": 2},
                                                             {"name": "C3", "collectorEnabled": True, "ipAddress": "192.168.146.109", "maxDatagramSize": "430", "maxHeaderSize": "128", "port": "6343", "collectorId": 3}],
                                         "sflowAgents": [{"ipMode": "IpPool"}],
                                         "sflowPorts": [{"portName": "Q1:1", "collectorId": "1", "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 3,
                                                         "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": "20", "pollingEnabled": True},
                                                                                                          {"configurationMode": "Sampling", "direction": "BOTH", "samplingRate": "256", "samplingEnabled": True}]},
                                                        {"portName": "Q1:1", "collectorId": "1", "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 6,
                                                         "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": "20", "pollingEnabled": True},
                                                                                                          {"configurationMode": "Sampling", "direction": "BOTH", "samplingRate": "256", "samplingEnabled": True}]},
                                                        {"portName": "Q2:1", "collectorId": "2", "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 3,
                                                         "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": "20", "pollingEnabled": True},
                                                                                                          {"configurationMode": "Sampling", "direction": "BOTH", "samplingRate": "256", "samplingEnabled": True}]},
                                                        {"portName": "Q2:1", "collectorId": "2", "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 6,
                                                         "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": "20", "pollingEnabled": True},
                                                                                                          {"configurationMode": "Sampling", "direction": "BOTH", "samplingRate": "256", "samplingEnabled": True}]},
                                                        {"portName": "d1", "collectorId": "3", "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 3,
                                                         "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": "20", "pollingEnabled": True},
                                                                                                          {"configurationMode": "Sampling", "direction": "BOTH", "samplingRate": "256", "samplingEnabled": True}]},
                                                        {"portName": "d1", "collectorId": "3", "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 6,
                                                         "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": "20", "pollingEnabled": True},
                                                                                                          {"configurationMode": "Sampling", "direction": "BOTH", "samplingRate": "256", "samplingEnabled": True}]},
                                                        ]
                                         },
                  "uplinkSets": [{'name': 'us1', 'ethernetNetworkType': 'Untagged', 'networkType': 'Ethernet', 'networkUris': ["Untagged"], 'primaryPort': None, 'nativeNetworkUri': None, 'mode': 'Auto',
                                    'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': 'Q1.1', 'speed': 'Auto'},
                                                               {'bay': '6', 'enclosure': '1', 'port': 'Q1.1', 'speed': 'Auto'}, ]},
                                 {'name': 'us2', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ["Ethernet_1000", "Ethernet_Vlan_1", "Ethernet_111"], 'primaryPort': None, 'nativeNetworkUri': None, 'mode': 'Auto',
                                  'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': 'Q2.1', 'speed': 'Auto'},
                                                             {'bay': '6', 'enclosure': '1', 'port': 'Q2.1', 'speed': 'Auto'}]}
                                 ]}

sflow_server = [{'name': 'server1', 'type': 'ServerProfileV9', 'serverHardwareUri': 'SH:SGH721WSR0, bay 1', 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Physical', 'iscsiInitiatorNameType': 'AutoGenerated', 'macType': 'Physical', 'wwnType': 'Physical', 'description': 'Updated Profile', 'affinity': 'Bay',
                 'boot': {'manageBoot': False},
                 'bootMode': {'manageMode': False},
                 'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                 'bios': {'manageBios': False, 'overriddenSettings': []},
                 'hideUnusedFlexNics': True, 'iscsiInitiatorName': '', 'osDeploymentSettings': None,
                 'localStorage': None,
                 'sanStorage': None,
                 'connectionSettings': {'connections': [{'id': 1, 'name': 'Connection 1', 'functionType': 'Ethernet', 'portId': 'Auto',
                                                         'requestedMbps': '2500', 'networkUri': 'ETH:Untagged',
                                                         'mac': None, 'wwpn': '', 'wwnn': ''},
                                                        {'id': 2, 'name': 'Connection 2', 'functionType': 'Ethernet', 'portId': 'Auto',
                                                         'requestedMbps': '2500', 'networkUri': 'ETH:Ethernet_1000',
                                                         'mac': None, 'wwpn': '', 'wwnn': ''},
                                                        ]},
                 }]

eth_networks = [{"vlanId": "100", "ethernetNetworkType": "Tagged", "subnetUri": None, "purpose": "General", "name": "net_100", "smartLink": 'true', "privateNetwork": 'false', "connectionTemplateUri": None, "type": eth_network_Version},
                {"vlanId": "101", "ethernetNetworkType": "Tagged", "subnetUri": None, "purpose": "General", "name": "net_200", "smartLink": 'true', "privateNetwork": 'false', "connectionTemplateUri": None, "type": eth_network_Version},
                {"vlanId": "102", "ethernetNetworkType": "Tagged", "subnetUri": None, "purpose": "General", "name": "net_300", "smartLink": 'true', "privateNetwork": 'false', "connectionTemplateUri": None, "type": eth_network_Version},
                {"vlanId": "1", "ethernetNetworkType": "Tunnel", "subnetUri": None, "purpose": "General", "name": "tunnel_nw", "smartLink": 'true', "privateNetwork": 'false', "connectionTemplateUri": None, "type": eth_network_Version}]


eth_networks_1 = [{"vlanId": "1000", "ethernetNetworkType": "Tagged", "subnetUri": None, "purpose": "General", "name": "Ethernet_1000", "smartLink": 'true', "privateNetwork": 'false', "connectionTemplateUri": None, "type": eth_network_Version},
                  {"vlanId": "1001", "ethernetNetworkType": "Tagged", "subnetUri": None, "purpose": "General", "name": "Ethernet_1001", "smartLink": 'true', "privateNetwork": 'false', "connectionTemplateUri": None, "type": eth_network_Version},
                  {"vlanId": "102", "ethernetNetworkType": "Untagged", "subnetUri": None, "purpose": "General", "name": "Untagged", "smartLink": 'true', "privateNetwork": 'false', "connectionTemplateUri": None, "type": eth_network_Version},
                  {"vlanId": "1002", "ethernetNetworkType": "Tunnel", "subnetUri": None, "purpose": "General", "name": "Ethernet_1002", "smartLink": 'true', "privateNetwork": 'false', "connectionTemplateUri": None, "type": eth_network_Version},
                  {"vlanId": "111", "ethernetNetworkType": "Tagged", "subnetUri": None, "purpose": "General", "name": "Ethernet_111", "smartLink": 'true', "privateNetwork": 'false', "connectionTemplateUri": None, "type": eth_network_Version},
                  {"vlanId": "1", "ethernetNetworkType": "Tagged", "subnetUri": None, "purpose": "General", "name": "Ethernet_Vlan_1", "smartLink": 'true', "privateNetwork": 'false', "connectionTemplateUri": None, "type": eth_network_Version}]

eth_networks_subnet_id = [{"vlanId": "110", "ethernetNetworkType": "Tagged", "subnetUri": "192.168.146.0", "purpose": "General",
                           "name": "Ethernet_110", "smartLink": 'true', "privateNetwork": 'false', "connectionTemplateUri": None,
                           "type": eth_network_Version}]

sflow_eg = [{'name': 'EG',
             'ipAddressingMode': "External",
             'enclosureCount': 1,
             'configurationScript': None,
             'interconnectBayMappings': [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                                         {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                                         {'interconnectBay': 3, 'logicalInterconnectGroupUri': "LIG:LIG"},
                                         {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                                         {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                                         {'interconnectBay': 6, 'logicalInterconnectGroupUri': "LIG:LIG"}
                                         ]}]

sflow_le = [{'name': 'LE',
             'enclosureUris': ['ENC:' + ENC1],
             'enclosureGroupUri': 'EG:EG',
             'firmwareBaselineUri': None,
             'forceInstallFirmware': False
             }]

ipv4_subnet = [{"type": "Subnet", "networkId": "192.168.146.0", "subnetmask": "255.255.255.0", "gateway": "192.168.146.1",
                "dnsServers": ["16.110.135.51", "16.110.135.52"], "domain": "ind.hp.com"}]

ipv4_range = [{"type": "Range", "startAddress": "192.168.146.2", "endAddress": "192.168.146.9", "name": "sflow",
               "subnetUri": "192.168.146.0", "associatedResources": []}]

InterfaceName = "Ten-GigabitEthernet0/0/1:1"
InterfaceName1 = "Ten-GigabitEthernet1/0/1:1"
InterfaceName2 = "TwentyGigE0/1/1"
InterfaceName3 = "Ten-GigabitEthernet1/0/2:1"

interfaceDetails = {"InterfaceName": "Ten-GigabitEthernet0/0/1:1", "InterfacePrefix": "Ten-GigabitEthernet"}

# Receiver details
sFlowRcvrOwner1 = ".enterprises.14706.1.1.4.1.2.1"
sFlowRcvrOwner2 = ".enterprises.14706.1.1.4.1.2.2"
sFlowRcvrOwner3 = ".enterprises.14706.1.1.4.1.2.3"

sFlowRcvrTimeout = ".enterprises.14706.1.1.4.1.3.1"
# Receiver Datagram
sFlowRcvrMaximumDatagramSize1 = ".enterprises.14706.1.1.4.1.4.1"
sFlowRcvrMaximumDatagramSize2 = ".enterprises.14706.1.1.4.1.4.2"
sFlowRcvrMaximumDatagramSize3 = ".enterprises.14706.1.1.4.1.4.3"

sFlowRcvrAddressType = ".enterprises.14706.1.1.4.1.5.1"

# Receiver Address
sFlowRcvrAddress1 = ".enterprises.14706.1.1.4.1.6.1"
sFlowRcvrAddress2 = ".enterprises.14706.1.1.4.1.6.2"
sFlowRcvrAddress3 = ".enterprises.14706.1.1.4.1.6.2"

# Receiver Status
sFlowRcvrStatus = ".enterprises.11.5.7.5.8.2.2.115.1.1.1.5"  # value 1 - Enabled, 2- Disabled

# Receiver Ports
sFlowRcvrPort1 = ".enterprises.14706.1.1.4.1.7.1"
sFlowRcvrPort2 = ".enterprises.14706.1.1.4.1.7.2"
sFlowRcvrPort3 = ".enterprises.14706.1.1.4.1.7.3"

sFlowRcvrDatagramVersion = ".enterprises.14706.1.1.4.1.8.1"

sFlowFsReceiver = ".enterprises.14706.1.1.5.1.3.11.1.3.6.1.2.1.2.2.1.1.98.1"
sFlowFsPacketSamplingRate = ".enterprises.14706.1.1.5.1.4.11.1.3.6.1.2.1.2.2.1.1.98.1"
sFlowFsMaximumHeaderSize = ".enterprises.14706.1.1.5.1.5.11.1.3.6.1.2.1.2.2.1.1.98.1"

sFlowCpReceiver = ".enterprises.14706.1.1.6.1.3.11.1.3.6.1.2.1.2.2.1.1.98.1"
sFlowCpInterval = ".enterprises.14706.1.1.6.1.4.11.1.3.6.1.2.1.2.2.1.1.98.1"

sFlowCounterPollerInterval1 = ".enterprises.14706.1.1.6.1.4.11.1.3.6.1.2.1.2.2.1.1.2.1"
sFlowCounterPollerInterval2 = ".enterprises.14706.1.1.6.1.4.11.1.3.6.1.2.1.2.2.1.1.2.2"
sFlowCounterPollerInterval3 = ".enterprises.14706.1.1.6.1.4.11.1.3.6.1.2.1.2.2.1.1.2.3"

sFlowInterfaceCounterPollerStatus = ".enterprises.11.5.7.5.8.2.2.115.2.1.1.6.11.1.3.6.1.2.1.2.2.1.1"
sFlowInterfaceSamplingStatus = ".enterprises.11.5.7.5.8.2.2.115.15.1.1.7.11.1.3.6.1.2.1.2.2.1.1"


sFlowAgentIpAddr = ".enterprises.14706.1.1.3.0"
sFlowAgentStatus = ".enterprises.11.5.7.5.8.2.2.115.4.0"    # value 1 - Enabled, 2- Disabled
sFlowSubnet = ".enterprises.11.5.7.5.8.1.27.1.5.1.3.326"

# Interface SNMP MIBS
InterfaceSamplingReceiver = ".enterprises.14706.1.1.5.1.3.11.1.3.6.1.2.1.2.2.1.1"
InterfacePollingReceiver = ".enterprises.14706.1.1.6.1.3.11.1.3.6.1.2.1.2.2.1.1"
interfacePollerInterval = ".enterprises.14706.1.1.6.1.4.11.1.3.6.1.2.1.2.2.1.1"
interfaceSamplingHeaderSize = ".enterprises.14706.1.1.5.1.5.11.1.3.6.1.2.1.2.2.1.1"
interfaceIngressSamplingRate = ".enterprises.14706.1.1.5.1.4.11.1.3.6.1.2.1.2.2.1.1"
interfaceEgressSamplingRate = ".enterprises.14706.1.1.5.1.4.11.1.3.6.1.2.1.2.2.1.1"
interfaceSamplingDirection = ".enterprises.11.5.7.5.8.2.2.115.15.1.1.2.11.1.3.6.1.2.1.2.2.1.1"  # 3 - BOTH, 2 - Egress , 1 - Ingress


# To get interface list
hafniumInterfaceList = "1.3.6.1.2.1.31.1.1.1.1"
# or
# hafniumInterfaceList =      "ifName"

sFlowRcvrOwner = ".enterprises.14706.1.1.4.1.2"
sFlowRcvrAddress = ".enterprises.14706.1.1.4.1.6"
sFlowRcvrPort = ".enterprises.14706.1.1.4.1.7"
sFlowRcvrMaximumDatagramSize = ".enterprises.14706.1.1.4.1.4"

sflowStaticIPMessage = 'The sFlow configuration is disabled because a static IP address has not been specified for the sFlow agent*'
LI_fw_update_Hafnium = {"path": "/firmware", 'command': 'UPDATE', 'ethernetActivationDelay': 0, 'ethernetActivationType': 'Parallel', "fcActivationDelay": 0, "fcActivationType": "Parallel", 'force': False, 'sppUri': upgrade_firmware_path, "validationType": "None"}
LI_fw_downgrade_Hafnium = {"path": "/firmware", 'command': 'UPDATE', 'ethernetActivationDelay': 0, 'ethernetActivationType': 'Parallel', "fcActivationDelay": 0, "fcActivationType": "Parallel", 'force': True, 'sppUri': downgrade_firmware_path, "validationType": "None"}


# ------------------- New lines ####################

edit_li_max_headersize_temp = {'sflowconfiguration': {
    "type": "sflow-configuration",
    "category": "sflow-configuration",
    "enabled": True,
    "sflowAgents": [{
        "ipMode": "Static",
        "ipAddr": "192.168.145.43",
        "subnetMask": "255.255.248.0"
    }],
    "sflowNetwork": {
        "name": "Ethernet_1000",
        "uri": ' '
    },
    "sflowCollectors": [{
        "name": "C1",
        "collectorEnabled": False,
        "ipAddress": "192.168.147.210",
        "maxDatagramSize": "5000",
        "maxHeaderSize": "256",
        "port": "6343",
        "collectorId": 1
    },
        {
        "name": "C2",
        "collectorEnabled": True,
        "ipAddress": "192.168.147.211",
        "maxDatagramSize": "5000",
        "maxHeaderSize": "1024",
        "port": "6343",
        "collectorId": 2
    },
        {
        "name": "C3",
        "collectorEnabled": False,
        "ipAddress": "192.168.147.212",
        "maxDatagramSize": "3800",
        "maxHeaderSize": "128",
        "port": "6343",
        "collectorId": 3
    }],
    "sflowPorts": [{
        "portName": "Q2:1",
        "collectorId": 2,
        "icmName": "SGH721WSR0, interconnect 3",
        "bayNumber": 3,
        "enclosureIndex": 1,
        "sflowConfigurationModes": [{
            "configurationMode": "Polling",
            "pollingInterval": 20
        },
            {
            "configurationMode": "Sampling",
            "direction": "BOTH",
            "samplingRate": 330
        }]
    },
        {
        "portName": "Q1:1",
        "collectorId": 1,
        "icmName": "SGH721WSR0, interconnect 3",
        "bayNumber": 3,
        "enclosureIndex": 1,
        "sflowConfigurationModes": [{
            "configurationMode": "Polling",
            "pollingInterval": 20
        },
            {
            "configurationMode": "Sampling",
            "direction": "BOTH",
            "samplingRate": 300
        }]
    }]
}}

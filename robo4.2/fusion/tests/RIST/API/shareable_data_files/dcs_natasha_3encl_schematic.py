admin_credentials = {'userName': 'administrator', 'password': 'wpsthpvse1'}

users = [
    {'userName': 'backup', 'password': 'backupadmin', 'roles': ['Backup administrator'], 'emailAddress':'backup@hp.com', 'officePhone':'970-666-1919', 'mobilePhone':'970-600-1919', 'type': 'UserAndPermissions'},
    {'userName': 'network', 'password': 'networkadmin', 'roles': ['Network administrator'], 'emailAddress':'network@hp.com', 'officePhone':'970-555-0001', 'mobilePhone':'970-500-0001', 'type': 'UserAndPermissions'},
    {'userName': 'readonly', 'password': 'readonly', 'roles': ['Read only'], 'emailAddress':'readonly@hp.com', 'officePhone':'970-666-1919', 'mobilePhone':'970-600-1919', 'type': 'UserAndPermissions'},
    {'userName': 'server', 'password': 'serveradmin', 'roles': ['Server administrator'], 'emailAddress':'server@hp.com', 'officePhone':'970-555-0001', 'mobilePhone':'970-500-0001', 'type': 'UserAndPermissions'},
    {'userName': 'software', 'password': 'softwareadmin', 'roles': ['Software administrator'], 'emailAddress':'software@hp.com', 'officePhone':'970-555-0001', 'mobilePhone':'970-500-0001', 'type': 'UserAndPermissions'},
    {'userName': 'storage', 'password': 'storageadmin', 'roles': ['Storage administrator'], 'emailAddress':'storage@hp.com', 'officePhone':'970-555-0001', 'mobilePhone':'970-500-0001', 'type': 'UserAndPermissions'},
]

# Removed attributes
# *uri
# created
# modified
# eTag
# state
# stateReason
# powerState
# *wwid
# uidState
# temperature
sas_interconnects = [
    {
        "type": "sas-interconnect",
        "firmwareVersion": "0.1.7.31",
        "partNumber": "755985-B21",
        "model": "Synergy 12Gb SAS Connection Module",
        "interconnectLocation": {
                "locationEntries": [
                    {
                        "value": "2302",
                        "type": "Port"
                    },
                    {
                        "value": "/rest/enclosures/0000000000A66103",
                        "type": "Enclosure"
                    },
                    {
                        "value": "fe80::2:0:8:5%eth2",
                        "type": "Ip"
                    },
                    {
                        "value": "1",
                        "type": "Bay"
                    }
                ]
        },
        "portCount": 12,
        "productName": "Synergy 12Gb SAS Connection Module",
        "interconnectIP": "fe80::2:0:8:5%eth2",
        "enclosureName": "0000A66103",
        "sasPorts": [
            {
                "type": "sas-port",
                "portName": "7",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "7",
                "portLocation": "7",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "7",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "11",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "11",
                "portLocation": "11",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "11",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "9",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "9",
                "portLocation": "9",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "9",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "2",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "2",
                "portLocation": "2",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "2",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "4",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "4",
                "portLocation": "4",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "4",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "3",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "3",
                "portLocation": "3",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "3",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "8",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "8",
                "portLocation": "8",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "8",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "10",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "10",
                "portLocation": "10",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "10",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "1",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "1",
                "portLocation": "1",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "1",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "12",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "12",
                "portLocation": "12",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "12",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "5",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "5",
                "portLocation": "5",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "5",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "6",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "6",
                "portLocation": "6",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "6",
                "category": "sas-ports",
            }
        ],
        "sasWWN": "500143801000005",
        "hardResetState": "Normal",
        "softResetState": "Normal",
        "serialNumber": "2M220104SL",
        "refreshState": "NotRefreshing",
        "description": None,
        "status": "OK",
        "name": "0000A66103, interconnect 1",
        "category": "sas-interconnects",
    },
    {
        "type": "sas-interconnect",
        "firmwareVersion": "0.1.7.31",
        "partNumber": "755985-B21",
        "model": "Synergy 12Gb SAS Connection Module",
        "interconnectLocation": {
                "locationEntries": [
                    {
                        "value": "2302",
                        "type": "Port"
                    },
                    {
                        "value": "/rest/enclosures/0000000000A66102",
                        "type": "Enclosure"
                    },
                    {
                        "value": "4",
                        "type": "Bay"
                    },
                    {
                        "value": "fe80::2:0:8:4%eth2",
                        "type": "Ip"
                    }
                ]
        },
        "portCount": 12,
        "productName": "Synergy 12Gb SAS Connection Module",
        "interconnectIP": "fe80::2:0:8:4%eth2",
        "enclosureName": "0000A66102",
        "sasPorts": [
            {
                "type": "sas-port",
                "portName": "4",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "4",
                "portLocation": "4",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "4",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "3",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "3",
                "portLocation": "3",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "3",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "1",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "1",
                "portLocation": "1",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "1",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "11",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "11",
                "portLocation": "11",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "11",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "12",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "12",
                "portLocation": "12",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "12",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "10",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "10",
                "portLocation": "10",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "10",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "2",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "2",
                "portLocation": "2",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "2",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "6",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "6",
                "portLocation": "6",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "6",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "9",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "9",
                "portLocation": "9",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "9",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "7",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "7",
                "portLocation": "7",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "7",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "8",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "8",
                "portLocation": "8",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "8",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "5",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "5",
                "portLocation": "5",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "5",
                "category": "sas-ports",
            }
        ],
        "sasWWN": "500143801000004",
        "hardResetState": "Normal",
        "softResetState": "Normal",
        "serialNumber": "2M220103SL",
        "refreshState": "NotRefreshing",
        "description": None,
        "status": "OK",
        "name": "0000A66102, interconnect 4",
        "category": "sas-interconnects",
    },
    {
        "type": "sas-interconnect",
        "firmwareVersion": "0.1.7.31",
        "partNumber": "755985-B21",
        "model": "Synergy 12Gb SAS Connection Module",
        "interconnectLocation": {
                "locationEntries": [
                    {
                        "value": "fe80::2:0:8:2%eth2",
                        "type": "Ip"
                    },
                    {
                        "value": "2302",
                        "type": "Port"
                    },
                    {
                        "value": "4",
                        "type": "Bay"
                    },
                    {
                        "value": "/rest/enclosures/0000000000A66101",
                        "type": "Enclosure"
                    }
                ]
        },
        "portCount": 12,
        "productName": "Synergy 12Gb SAS Connection Module",
        "interconnectIP": "fe80::2:0:8:2%eth2",
        "enclosureName": "0000A66101",
        "sasPorts": [
            {
                "type": "sas-port",
                "portName": "9",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "9",
                "portLocation": "9",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "9",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "1",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "1",
                "portLocation": "1",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "1",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "3",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "3",
                "portLocation": "3",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "3",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "4",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "4",
                "portLocation": "4",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "4",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "10",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "10",
                "portLocation": "10",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "10",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "6",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "6",
                "portLocation": "6",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "6",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "11",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "11",
                "portLocation": "11",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "11",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "12",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "12",
                "portLocation": "12",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "12",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "5",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "5",
                "portLocation": "5",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "5",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "8",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "8",
                "portLocation": "8",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "8",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "7",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "7",
                "portLocation": "7",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "7",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "2",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "2",
                "portLocation": "2",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "2",
                "category": "sas-ports",
            }
        ],
        "sasWWN": "500143801000002",
        "hardResetState": "Normal",
        "softResetState": "Normal",
        "serialNumber": "2M220101SL",
        "refreshState": "NotRefreshing",
        "description": None,
        "status": "OK",
        "name": "0000A66101, interconnect 4",
        "category": "sas-interconnects",
    },
    {
        "type": "sas-interconnect",
        "firmwareVersion": "0.1.7.31",
        "partNumber": "755985-B21",
        "model": "Synergy 12Gb SAS Connection Module",
        "interconnectLocation": {
                "locationEntries": [
                    {
                        "value": "2302",
                        "type": "Port"
                    },
                    {
                        "value": "/rest/enclosures/0000000000A66102",
                        "type": "Enclosure"
                    },
                    {
                        "value": "1",
                        "type": "Bay"
                    },
                    {
                        "value": "fe80::2:0:8:3%eth2",
                        "type": "Ip"
                    }
                ]
        },
        "portCount": 12,
        "productName": "Synergy 12Gb SAS Connection Module",
        "interconnectIP": "fe80::2:0:8:3%eth2",
        "enclosureName": "0000A66102",
        "sasPorts": [
            {
                "type": "sas-port",
                "portName": "10",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "10",
                "portLocation": "10",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "10",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "4",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "4",
                "portLocation": "4",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "4",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "6",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "6",
                "portLocation": "6",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "6",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "5",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "5",
                "portLocation": "5",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "5",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "9",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "9",
                "portLocation": "9",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "9",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "8",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "8",
                "portLocation": "8",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "8",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "11",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "11",
                "portLocation": "11",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "11",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "1",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "1",
                "portLocation": "1",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "1",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "2",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "2",
                "portLocation": "2",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "2",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "7",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "7",
                "portLocation": "7",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "7",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "3",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "3",
                "portLocation": "3",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "3",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "12",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "12",
                "portLocation": "12",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "12",
                "category": "sas-ports",
            }
        ],
        "sasWWN": "500143801000003",
        "hardResetState": "Normal",
        "softResetState": "Normal",
        "serialNumber": "2M220102SL",
        "refreshState": "NotRefreshing",
        "description": None,
        "status": "OK",
        "name": "0000A66102, interconnect 1",
        "category": "sas-interconnects",
    },
    {
        "type": "sas-interconnect",
        "firmwareVersion": "0.1.7.31",
        "partNumber": "755985-B21",
        "model": "Synergy 12Gb SAS Connection Module",
        "interconnectLocation": {
                "locationEntries": [
                    {
                        "value": "2302",
                        "type": "Port"
                    },
                    {
                        "value": "/rest/enclosures/0000000000A66103",
                        "type": "Enclosure"
                    },
                    {
                        "value": "4",
                        "type": "Bay"
                    },
                    {
                        "value": "fe80::2:0:8:6%eth2",
                        "type": "Ip"
                    }
                ]
        },
        "portCount": 12,
        "productName": "Synergy 12Gb SAS Connection Module",
        "interconnectIP": "fe80::2:0:8:6%eth2",
        "enclosureName": "0000A66103",
        "sasPorts": [
            {
                "type": "sas-port",
                "portName": "8",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "8",
                "portLocation": "8",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "8",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "5",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "5",
                "portLocation": "5",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "5",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "4",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "4",
                "portLocation": "4",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "4",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "9",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "9",
                "portLocation": "9",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "9",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "7",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "7",
                "portLocation": "7",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "7",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "2",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "2",
                "portLocation": "2",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "2",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "11",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "11",
                "portLocation": "11",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "11",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "3",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "3",
                "portLocation": "3",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "3",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "10",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "10",
                "portLocation": "10",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "10",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "1",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "1",
                "portLocation": "1",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "1",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "12",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "12",
                "portLocation": "12",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "12",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "6",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "6",
                "portLocation": "6",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "6",
                "category": "sas-ports",
            }
        ],
        "sasWWN": "500143801000006",
        "hardResetState": "Normal",
        "softResetState": "Normal",
        "serialNumber": "2M220105SL",
        "refreshState": "NotRefreshing",
        "description": None,
        "status": "OK",
        "name": "0000A66103, interconnect 4",
        "category": "sas-interconnects",
    },
    {
        "type": "sas-interconnect",
        "firmwareVersion": "0.1.7.31",
        "partNumber": "755985-B21",
        "model": "Synergy 12Gb SAS Connection Module",
        "interconnectLocation": {
                "locationEntries": [
                    {
                        "value": "2302",
                        "type": "Port"
                    },
                    {
                        "value": "1",
                        "type": "Bay"
                    },
                    {
                        "value": "/rest/enclosures/0000000000A66101",
                        "type": "Enclosure"
                    },
                    {
                        "value": "fe80::2:0:8:1%eth2",
                        "type": "Ip"
                    }
                ]
        },
        "portCount": 12,
        "productName": "Synergy 12Gb SAS Connection Module",
        "interconnectIP": "fe80::2:0:8:1%eth2",
        "enclosureName": "0000A66101",
        "sasPorts": [
            {
                "type": "sas-port",
                "portName": "4",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "4",
                "portLocation": "4",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "4",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "10",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "10",
                "portLocation": "10",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "10",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "12",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "12",
                "portLocation": "12",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "12",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "2",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "2",
                "portLocation": "2",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "2",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "1",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "1",
                "portLocation": "1",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "1",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "3",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "3",
                "portLocation": "3",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "3",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "5",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "5",
                "portLocation": "5",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "5",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "11",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "11",
                "portLocation": "11",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "11",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "8",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "8",
                "portLocation": "8",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "8",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "9",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "9",
                "portLocation": "9",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "9",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "7",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "7",
                "portLocation": "7",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "7",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "6",
                "portType": "Downlink",
                "portStatusReason": "None",
                "portIdentifier": "6",
                "portLocation": "6",
                "phyCount": 4,
                "enabled": True,
                "description": None,
                "status": "OK",
                "name": "6",
                "category": "sas-ports",
            }
        ],
        "sasWWN": "5001438010000001",
        "hardResetState": "Normal",
        "softResetState": "Normal",
        "serialNumber": "2M220100SL",
        "refreshState": "NotRefreshing",
        "description": None,
        "status": "OK",
        "name": "0000A66101, interconnect 1",
        "category": "sas-interconnects",
    }
]

drive_enclosures = [
    {
        "type": "drive-enclosure",
        "firmwareVersion": "0.18",
        "partNumber": "755984-B21",
        "model": "Synergy D3940 Storage Module",
        "productName": "Storage Enclosure 500143803110029D",
        "enclosureName": "0000A66101",
        "interconnectBaySet": 1,
        "manufacturer": "HPE",
        "driveEnclosureLocation": {
            "locationEntries": [
                {
                    "value": "1",
                    "type": "Bay"
                },
                {
                    "value": "/rest/enclosures/0000000000A66101",
                    "type": "Enclosure"
                },
                {
                    "value": "1",
                    "type": "SasPort"
                }
            ]
        },
        "driveBayCount": 40,
        "wwid": "500143803110029D",
        "bay": 1,
        "driveBays": [
            {
                "type": "drive-bay",
                "model": "SAS 2048",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "1",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610000",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610000",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "1:1:1"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "1",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710000J4524YPT",
                    "capacity": "2048",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 1",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 1",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 2048",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "2",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610001",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610001",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "1:1:2"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "2",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710001J4524YPT",
                    "capacity": "2048",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 2",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 2",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 500",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "3",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610002",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610002",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "1:1:3"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "3",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710002J4524YPT",
                    "capacity": "500",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 3",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 3",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 500",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "4",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610003",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610003",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "1:1:4"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "4",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710003J4524YPT",
                    "capacity": "500",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 4",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 4",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 500",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "5",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610004",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610004",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "1:1:5"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "5",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710004J4524YPT",
                    "capacity": "500",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 5",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 5",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 500",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "6",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610005",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610005",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "1:1:6"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "6",
                                "type": "Bay"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710005J4524YPT",
                    "capacity": "500",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 6",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 6",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 500",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "7",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610006",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610006",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "1:1:7"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "Bay"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710006J4524YPT",
                    "capacity": "500",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 7",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 7",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 80",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "8",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610007",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610007",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "1:1:8"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "8",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710007J4524YPT",
                    "capacity": "80",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 8",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 8",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 80",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "9",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610008",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610008",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "1:1:9"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "9",
                                "type": "Bay"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710008J4524YPT",
                    "capacity": "80",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 9",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 9",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 80",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "10",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610009",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610009",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "1:1:10"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            },
                            {
                                "value": "10",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710009J4524YPT",
                    "capacity": "80",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 10",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 10",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 80",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "11",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610010",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610010",
                    "deviceInterface": "SAS",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "1:1:11"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "11",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710010J4524YPT",
                    "capacity": "80",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 11",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 11",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "12",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610011",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610011",
                    "deviceInterface": "SAS",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "1:1:12"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "12",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710011J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 12",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 12",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "13",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610012",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610012",
                    "deviceInterface": "SAS",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "1:1:13"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "13",
                                "type": "Bay"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710012J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 13",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 13",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "14",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610013",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610013",
                    "deviceInterface": "SAS",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "1:1:14"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "14",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710013J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 14",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 14",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "15",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610014",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610014",
                    "deviceInterface": "SAS",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "1:1:15"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "15",
                                "type": "Bay"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710014J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 15",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 15",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "16",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610015",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610015",
                    "deviceInterface": "SAS",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "1:1:16"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "16",
                                "type": "Bay"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710015J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 16",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 16",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "17",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610016",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610016",
                    "deviceInterface": "SAS",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "1:1:17"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "17",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710016J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 17",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 17",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "18",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610017",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610017",
                    "deviceInterface": "SAS",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "1:1:18"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "18",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710017J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 18",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 18",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "19",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610018",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610018",
                    "deviceInterface": "SAS",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "1:1:19"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "19",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710018J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 19",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 19",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "20",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610019",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610019",
                    "deviceInterface": "SAS",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "1:1:20"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "20",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710019J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 20",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 20",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "21",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610020",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610020",
                    "deviceInterface": "SATA",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "1:1:21"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "21",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710020J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 21",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 21",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "22",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610021",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610021",
                    "deviceInterface": "SATA",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "1:1:22"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            },
                            {
                                "value": "22",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710021J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 22",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 22",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "23",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610022",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610022",
                    "deviceInterface": "SATA",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "1:1:23"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            },
                            {
                                "value": "23",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710022J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 23",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 23",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 500",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "24",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610023",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610023",
                    "deviceInterface": "SATA",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "1:1:24"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "24",
                                "type": "Bay"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710023J4524YPT",
                    "capacity": "500",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 24",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 24",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 500",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "25",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610024",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610024",
                    "deviceInterface": "SATA",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "1:1:25"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "25",
                                "type": "Bay"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710024J4524YPT",
                    "capacity": "500",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 25",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 25",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 500",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "26",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610025",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610025",
                    "deviceInterface": "SATA",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "1:1:26"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "26",
                                "type": "Bay"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710025J4524YPT",
                    "capacity": "500",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 26",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 26",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 500",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "27",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610026",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610026",
                    "deviceInterface": "SATA",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "1:1:27"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "27",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710026J4524YPT",
                    "capacity": "500",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 27",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 27",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 500",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "28",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610027",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610027",
                    "deviceInterface": "SATA",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "1:1:28"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "28",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710027J4524YPT",
                    "capacity": "500",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 28",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 28",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 500",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "29",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610028",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610028",
                    "deviceInterface": "SATA",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "1:1:29"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "29",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710028J4524YPT",
                    "capacity": "500",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 29",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 29",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 500",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "30",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610029",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610029",
                    "deviceInterface": "SATA",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "1:1:30"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "30",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710029J4524YPT",
                    "capacity": "500",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 30",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 30",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 80",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "31",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610030",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610030",
                    "deviceInterface": "SATA",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "1:1:31"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "31",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710030J4524YPT",
                    "capacity": "80",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 31",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 31",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 80",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "32",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610031",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610031",
                    "deviceInterface": "SATA",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "1:1:32"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "32",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710031J4524YPT",
                    "capacity": "80",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 32",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 32",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 80",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "33",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610032",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610032",
                    "deviceInterface": "SATA",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "1:1:33"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "33",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710032J4524YPT",
                    "capacity": "80",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 33",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 33",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 80",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "34",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610033",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610033",
                    "deviceInterface": "SATA",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "1:1:34"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "34",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710033J4524YPT",
                    "capacity": "80",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 34",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 34",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "35",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610034",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610034",
                    "deviceInterface": "SATA",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "1:1:35"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "35",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710034J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 35",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 35",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "36",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610035",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610035",
                    "deviceInterface": "SATA",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "1:1:36"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "36",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710035J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 36",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 36",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "37",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610036",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610036",
                    "deviceInterface": "SATA",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "1:1:37"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "37",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710036J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 37",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 37",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "38",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610037",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610037",
                    "deviceInterface": "SATA",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "1:1:38"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "38",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710037J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 38",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 38",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 6144",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "39",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610038",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610038",
                    "deviceInterface": "SATA",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "1:1:39"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "39",
                                "type": "Bay"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710038J4524YPT",
                    "capacity": "6144",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 39",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 39",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 6144",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "40",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610039",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610039",
                    "deviceInterface": "SATA",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "1:1:40"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            },
                            {
                                "value": "40",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710039J4524YPT",
                    "capacity": "6144",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 40",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 40",
                "description": None,
                "status": None,
                "category": "drive-bays",
            }
        ],
        "driveEnclosurePortMap": {
            "deviceSlots": [
                {
                    "deviceName": None,
                    "slotNumber": "1",
                    "physicalPorts": [
                        {
                            "interconnectName": "0000A66101, interconnect 4",
                            "interconnectPortNumber": "1",
                            "physicalInterconnectName": "0000A66101, interconnect 4",
                            "physicalInterconnectPortNumber": "1",
                            "type": "SAS"
                        },
                        {
                            "interconnectName": "0000A66101, interconnect 4",
                            "interconnectPortNumber": "2",
                            "physicalInterconnectName": "0000A66101, interconnect 4",
                            "physicalInterconnectPortNumber": "2",
                            "type": "SAS"
                        }
                    ],
                    "location": "IO Adapter"
                },
                {
                    "deviceName": None,
                    "slotNumber": "2",
                    "physicalPorts": [
                        {
                            "interconnectName": "0000A66101, interconnect 4",
                            "interconnectPortNumber": "1",
                            "physicalInterconnectName": "0000A66101, interconnect 4",
                            "physicalInterconnectPortNumber": "1",
                            "type": "SAS"
                        },
                        {
                            "interconnectName": "0000A66101, interconnect 4",
                            "interconnectPortNumber": "2",
                            "physicalInterconnectName": "0000A66101, interconnect 4",
                            "physicalInterconnectPortNumber": "2",
                            "type": "SAS"
                        }
                    ],
                    "location": "IO Adapter"
                }
            ],
            "type": "DriveEnclosurePortMap"
        },
        "hardResetState": "Normal",
        "ioAdapters": [
            {
                "type": "drive-enclosure-ioadapter",
                "firmwareVersion": "0.50",
                "partNumber": "755872-001",
                "ports": [
                    {
                        "type": "sas-port",
                        "portName": "2",
                        "portType": "Downlink",
                        "portStatusReason": "None",
                        "portIdentifier": "2",
                        "portLocation": "2",
                        "phyCount": 4,
                        "enabled": True,
                        "description": None,
                        "status": "OK",
                        "name": "2",
                        "category": "sas-ports",
                    },
                    {
                        "type": "sas-port",
                        "portName": "1",
                        "portType": "Downlink",
                        "portStatusReason": "None",
                        "portIdentifier": "1",
                        "portLocation": "1",
                        "phyCount": 4,
                        "enabled": True,
                        "description": None,
                        "status": "OK",
                        "name": "1",
                        "category": "sas-ports",
                    }
                ],
                "model": "Synergy D3940 Storage Module IO Adapter",
                "portCount": 2,
                "manufacturer": "HPE",
                "wwid": "5001438031100201",
                "redundantIoModule": "Installed",
                "ioAdapterLocation": {
                        "locationEntries": [
                            {
                                "value": "2",
                                "type": "Slot"
                            }
                        ]
                },
                "serialNumber": "50454e5445305101",
                "description": "",
                "status": "OK",
                "name": None,
                "category": "",
            },
            {
                "type": "drive-enclosure-ioadapter",
                "firmwareVersion": "0.50",
                "partNumber": "755872-001",
                "ports": [
                    {
                        "type": "sas-port",
                        "portName": "2",
                        "portType": "Downlink",
                        "portStatusReason": "None",
                        "portIdentifier": "2",
                        "portLocation": "2",
                        "phyCount": 4,
                        "enabled": True,
                        "description": None,
                        "status": "OK",
                        "name": "2",
                        "category": "sas-ports",
                    },
                    {
                        "type": "sas-port",
                        "portName": "1",
                        "portType": "Downlink",
                        "portStatusReason": "None",
                        "portIdentifier": "1",
                        "portLocation": "1",
                        "phyCount": 4,
                        "enabled": True,
                        "description": None,
                        "status": "OK",
                        "name": "1",
                        "category": "sas-ports",
                    }
                ],
                "model": "Synergy D3940 Storage Module IO Adapter",
                "portCount": 2,
                "manufacturer": "HPE",
                "wwid": "5001438031100200",
                "redundantIoModule": "Installed",
                "ioAdapterLocation": {
                        "locationEntries": [
                            {
                                "value": "1",
                                "type": "Slot"
                            }
                        ]
                },
                "serialNumber": "50454e5445305100",
                "description": "",
                "status": "OK",
                "name": None,
                "category": "",
            }
        ],
        "ioAdapterCount": 2,
        "serialNumber": "SN123100",
        "refreshState": None,
        "description": "",
        "status": "OK",
        "name": "0000A66101, bay 1",
        "category": "drive-enclosures",
    },
    {
        "type": "drive-enclosure",
        "firmwareVersion": "0.18",
        "partNumber": "755984-B21",
        "model": "Synergy D3940 Storage Module",
        "productName": "Storage Enclosure 500143803110529D",
        "enclosureName": "0000A66103",
        "interconnectBaySet": 1,
        "manufacturer": "HPE",
        "driveEnclosureLocation": {
                "locationEntries": [
                    {
                        "value": "7",
                        "type": "SasPort"
                    },
                    {
                        "value": "7",
                        "type": "Bay"
                    },
                    {
                        "value": "/rest/enclosures/0000000000A66103",
                        "type": "Enclosure"
                    }
                ]
        },
        "driveBayCount": 40,
        "wwid": "500143803110529D",
        "bay": 7,
        "driveBays": [
            {
                "type": "drive-bay",
                "model": "SAS 2048",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "1",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610176",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610176",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "7:4:1"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "1",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710176J4524YPT",
                    "capacity": "2048",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 1",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 1",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 2048",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "2",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610177",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610177",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "7:4:2"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "2",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710177J4524YPT",
                    "capacity": "2048",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 2",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 2",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "3",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610178",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610178",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "7:4:3"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "3",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710178J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 3",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 3",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "4",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610179",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610179",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "7:4:4"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "4",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710179J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 4",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 4",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "5",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610181",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610181",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "7:4:6"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "5",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710181J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 5",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 5",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "6",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610182",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610182",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "7:4:7"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "6",
                                "type": "Bay"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710182J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 6",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 6",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 500",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "7",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610183",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610183",
                    "deviceInterface": "SAS",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "7:4:8"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "7",
                                "type": "Bay"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710183J4524YPT",
                    "capacity": "500",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 7",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 7",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 500",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "8",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610184",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610184",
                    "deviceInterface": "SAS",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "7:4:9"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "8",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710184J4524YPT",
                    "capacity": "500",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 8",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 8",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 500",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "9",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610185",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610185",
                    "deviceInterface": "SAS",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "7:4:10"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "9",
                                "type": "Bay"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710185J4524YPT",
                    "capacity": "500",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 9",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 9",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 500",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "10",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610186",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610186",
                    "deviceInterface": "SAS",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "7:4:11"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "10",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710186J4524YPT",
                    "capacity": "500",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 10",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 10",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 80",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "11",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610187",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610187",
                    "deviceInterface": "SAS",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "7:4:12"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "11",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710187J4524YPT",
                    "capacity": "80",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 11",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 11",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 80",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "12",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610188",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610188",
                    "deviceInterface": "SAS",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "7:4:13"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "12",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710188J4524YPT",
                    "capacity": "80",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 12",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 12",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 80",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "13",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610189",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610189",
                    "deviceInterface": "SAS",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "7:4:14"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "13",
                                "type": "Bay"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710189J4524YPT",
                    "capacity": "80",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 13",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 13",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 80",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "14",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610190",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610190",
                    "deviceInterface": "SATA",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "7:4:15"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "14",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710190J4524YPT",
                    "capacity": "80",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 14",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 14",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 600",
                "driveBayLocation": {
                        "locationEntries": [
                            {
                                "value": "15",
                                "type": "Bay"
                            }
                        ]
                },
                "attachedDeviceWWID": "5000CCA03C610191",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610191",
                    "deviceInterface": "SATA",
                    "driveMedia": "HDD",
                    "drivePaths": [
                            "7:4:16"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "15",
                                "type": "Bay"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710191J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 15",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 15",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 600",
                "driveBayLocation": {
                        "locationEntries": [
                            {
                                "value": "16",
                                "type": "Bay"
                            }
                        ]
                },
                "attachedDeviceWWID": "5000CCA03C610192",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610192",
                    "deviceInterface": "SATA",
                    "driveMedia": "HDD",
                    "drivePaths": [
                            "7:4:17"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "16",
                                "type": "Bay"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710192J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 16",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 16",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 600",
                "driveBayLocation": {
                        "locationEntries": [
                            {
                                "value": "17",
                                "type": "Bay"
                            }
                        ]
                },
                "attachedDeviceWWID": "5000CCA03C610193",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610193",
                    "deviceInterface": "SATA",
                    "driveMedia": "HDD",
                    "drivePaths": [
                            "7:4:18"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "17",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710193J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 17",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 17",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 600",
                "driveBayLocation": {
                        "locationEntries": [
                            {
                                "value": "18",
                                "type": "Bay"
                            }
                        ]
                },
                "attachedDeviceWWID": "5000CCA03C610194",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610194",
                    "deviceInterface": "SATA",
                    "driveMedia": "HDD",
                    "drivePaths": [
                            "7:4:19"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "18",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710194J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 18",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 18",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 600",
                "driveBayLocation": {
                        "locationEntries": [
                            {
                                "value": "19",
                                "type": "Bay"
                            }
                        ]
                },
                "attachedDeviceWWID": "5000CCA03C610195",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610195",
                    "deviceInterface": "SATA",
                    "driveMedia": "HDD",
                    "drivePaths": [
                            "7:4:20"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "19",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710195J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 19",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 19",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 600",
                "driveBayLocation": {
                        "locationEntries": [
                            {
                                "value": "20",
                                "type": "Bay"
                            }
                        ]
                },
                "attachedDeviceWWID": "5000CCA03C610196",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610196",
                    "deviceInterface": "SATA",
                    "driveMedia": "HDD",
                    "drivePaths": [
                            "7:4:21"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "20",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710196J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 20",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 20",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 600",
                "driveBayLocation": {
                        "locationEntries": [
                            {
                                "value": "21",
                                "type": "Bay"
                            }
                        ]
                },
                "attachedDeviceWWID": "5000CCA03C610197",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610197",
                    "deviceInterface": "SATA",
                    "driveMedia": "SSD",
                    "drivePaths": [
                            "7:4:22"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "21",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710197J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 21",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 21",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 600",
                "driveBayLocation": {
                        "locationEntries": [
                            {
                                "value": "22",
                                "type": "Bay"
                            }
                        ]
                },
                "attachedDeviceWWID": "5000CCA03C610198",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610198",
                    "deviceInterface": "SATA",
                    "driveMedia": "SSD",
                    "drivePaths": [
                            "7:4:23"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "22",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710198J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 22",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 22",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 600",
                "driveBayLocation": {
                        "locationEntries": [
                            {
                                "value": "23",
                                "type": "Bay"
                            }
                        ]
                },
                "attachedDeviceWWID": "5000CCA03C610199",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610199",
                    "deviceInterface": "SATA",
                    "driveMedia": "SSD",
                    "drivePaths": [
                            "7:4:24"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "23",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710199J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 23",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 23",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 600",
                "driveBayLocation": {
                        "locationEntries": [
                            {
                                "value": "24",
                                "type": "Bay"
                            }
                        ]
                },
                "attachedDeviceWWID": "5000CCA03C610200",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610200",
                    "deviceInterface": "SATA",
                    "driveMedia": "SSD",
                    "drivePaths": [
                            "7:4:25"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "24",
                                "type": "Bay"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710200J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 24",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 24",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 600",
                "driveBayLocation": {
                        "locationEntries": [
                            {
                                "value": "25",
                                "type": "Bay"
                            }
                        ]
                },
                "attachedDeviceWWID": "5000CCA03C610201",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610201",
                    "deviceInterface": "SATA",
                    "driveMedia": "SSD",
                    "drivePaths": [
                            "7:4:26"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "25",
                                "type": "Bay"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710201J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 25",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 25",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 600",
                "driveBayLocation": {
                        "locationEntries": [
                            {
                                "value": "26",
                                "type": "Bay"
                            }
                        ]
                },
                "attachedDeviceWWID": "5000CCA03C610202",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610202",
                    "deviceInterface": "SATA",
                    "driveMedia": "SSD",
                    "drivePaths": [
                            "7:4:27"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "26",
                                "type": "Bay"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710202J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 26",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 26",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 6144",
                "driveBayLocation": {
                        "locationEntries": [
                            {
                                "value": "27",
                                "type": "Bay"
                            }
                        ]
                },
                "attachedDeviceWWID": "5000CCA03C610203",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610203",
                    "deviceInterface": "SATA",
                    "driveMedia": "SSD",
                    "drivePaths": [
                            "7:4:28"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "27",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710203J4524YPT",
                    "capacity": "6144",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 27",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 27",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 6144",
                "driveBayLocation": {
                        "locationEntries": [
                            {
                                "value": "28",
                                "type": "Bay"
                            }
                        ]
                },
                "attachedDeviceWWID": "5000CCA03C610204",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610204",
                    "deviceInterface": "SATA",
                    "driveMedia": "SSD",
                    "drivePaths": [
                            "7:4:29"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "28",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710204J4524YPT",
                    "capacity": "6144",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 28",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 28",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                        "locationEntries": [
                            {
                                "value": "29",
                                "type": "Bay"
                            }
                        ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "Drive Bay 29",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                        "locationEntries": [
                            {
                                "value": "30",
                                "type": "Bay"
                            }
                        ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "Drive Bay 30",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                        "locationEntries": [
                            {
                                "value": "31",
                                "type": "Bay"
                            }
                        ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "Drive Bay 31",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                        "locationEntries": [
                            {
                                "value": "32",
                                "type": "Bay"
                            }
                        ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "Drive Bay 32",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                        "locationEntries": [
                            {
                                "value": "33",
                                "type": "Bay"
                            }
                        ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "Drive Bay 33",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                        "locationEntries": [
                            {
                                "value": "34",
                                "type": "Bay"
                            }
                        ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "Drive Bay 34",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                        "locationEntries": [
                            {
                                "value": "35",
                                "type": "Bay"
                            }
                        ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "Drive Bay 35",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                        "locationEntries": [
                            {
                                "value": "36",
                                "type": "Bay"
                            }
                        ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "Drive Bay 36",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                        "locationEntries": [
                            {
                                "value": "37",
                                "type": "Bay"
                            }
                        ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "Drive Bay 37",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                        "locationEntries": [
                            {
                                "value": "38",
                                "type": "Bay"
                            }
                        ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "Drive Bay 38",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                        "locationEntries": [
                            {
                                "value": "39",
                                "type": "Bay"
                            }
                        ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "Drive Bay 39",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                        "locationEntries": [
                            {
                                "value": "40",
                                "type": "Bay"
                            }
                        ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "Drive Bay 40",
                "description": None,
                "status": None,
                "category": "drive-bays",
            }
        ],
        "driveEnclosurePortMap": {
            "deviceSlots": [
                {
                    "deviceName": None,
                    "slotNumber": "1",
                    "physicalPorts": [
                        {
                            "interconnectName": "0000A66103, interconnect 4",
                            "interconnectPortNumber": "7",
                            "physicalInterconnectName": "0000A66103, interconnect 4",
                            "physicalInterconnectPortNumber": "7",
                            "type": "SAS"
                        },
                        {
                            "interconnectName": "0000A66103, interconnect 4",
                            "interconnectPortNumber": "8",
                            "physicalInterconnectName": "0000A66103, interconnect 4",
                            "physicalInterconnectPortNumber": "8",
                            "type": "SAS"
                        }
                    ],
                    "location": "IO Adapter"
                },
                {
                    "deviceName": None,
                    "slotNumber": "2",
                    "physicalPorts": [
                        {
                            "interconnectName": "0000A66103, interconnect 4",
                            "interconnectPortNumber": "7",
                            "physicalInterconnectName": "0000A66103, interconnect 4",
                            "physicalInterconnectPortNumber": "7",
                            "type": "SAS"
                        },
                        {
                            "interconnectName": "0000A66103, interconnect 4",
                            "interconnectPortNumber": "8",
                            "physicalInterconnectName": "0000A66103, interconnect 4",
                            "physicalInterconnectPortNumber": "8",
                            "type": "SAS"
                        }
                    ],
                    "location": "IO Adapter"
                }
            ],
            "type": "DriveEnclosurePortMap"
        },
        "hardResetState": "Normal",
        "ioAdapters": [
            {
                "type": "drive-enclosure-ioadapter",
                "firmwareVersion": "0.50",
                "partNumber": "755872-001",
                "ports": [
                    {
                        "type": "sas-port",
                        "portName": "2",
                        "portType": "Downlink",
                        "portStatusReason": "None",
                        "portIdentifier": "2",
                        "portLocation": "2",
                        "phyCount": 4,
                        "enabled": True,
                        "description": None,
                        "status": "OK",
                        "name": "2",
                        "category": "sas-ports",
                    },
                    {
                        "type": "sas-port",
                        "portName": "1",
                        "portType": "Downlink",
                        "portStatusReason": "None",
                        "portIdentifier": "1",
                        "portLocation": "1",
                        "phyCount": 4,
                        "enabled": True,
                        "description": None,
                        "status": "OK",
                        "name": "1",
                        "category": "sas-ports",
                    }
                ],
                "model": "Synergy D3940 Storage Module IO Adapter",
                "portCount": 2,
                "manufacturer": "HPE",
                "wwid": "5001438031105210",
                "redundantIoModule": "Installed",
                "ioAdapterLocation": {
                        "locationEntries": [
                            {
                                "value": "1",
                                "type": "Slot"
                            }
                        ]
                },
                "serialNumber": "50454e5445305110",
                "description": "",
                "status": "OK",
                "name": None,
                "category": "",
            },
            {
                "type": "drive-enclosure-ioadapter",
                "firmwareVersion": "0.50",
                "partNumber": "755872-001",
                "ports": [
                    {
                        "type": "sas-port",
                        "portName": "2",
                        "portType": "Downlink",
                        "portStatusReason": "None",
                        "portIdentifier": "2",
                        "portLocation": "2",
                        "phyCount": 4,
                        "enabled": True,
                        "description": None,
                        "status": "OK",
                        "name": "2",
                        "category": "sas-ports",
                    },
                    {
                        "type": "sas-port",
                        "portName": "1",
                        "portType": "Downlink",
                        "portStatusReason": "None",
                        "portIdentifier": "1",
                        "portLocation": "1",
                        "phyCount": 4,
                        "enabled": True,
                        "description": None,
                        "status": "OK",
                        "name": "1",
                        "category": "sas-ports",
                    }
                ],
                "model": "Synergy D3940 Storage Module IO Adapter",
                "portCount": 2,
                "manufacturer": "HPE",
                "wwid": "5001438031105211",
                "redundantIoModule": "Installed",
                "ioAdapterLocation": {
                        "locationEntries": [
                            {
                                "value": "2",
                                "type": "Slot"
                            }
                        ]
                },
                "serialNumber": "50454e5445305111",
                "description": "",
                "status": "OK",
                "name": None,
                "category": "",
            }
        ],
        "ioAdapterCount": 2,
        "serialNumber": "SN123105",
        "refreshState": None,
        "description": "",
        "status": "OK",
        "name": "0000A66103, bay 7",
        "category": "drive-enclosures",
    },
    {
        "type": "drive-enclosure",
        "firmwareVersion": "0.18",
        "partNumber": "755984-B21",
        "model": "Synergy D3940 Storage Module",
        "productName": "Storage Enclosure 500143803110429D",
        "enclosureName": "0000A66103",
        "interconnectBaySet": 1,
        "manufacturer": "HPE",
        "driveEnclosureLocation": {
                "locationEntries": [
                    {
                        "value": "/rest/enclosures/0000000000A66103",
                        "type": "Enclosure"
                    },
                    {
                        "value": "1",
                        "type": "Bay"
                    },
                    {
                        "value": "1",
                        "type": "SasPort"
                    }
                ]
        },
        "driveBayCount": 40,
        "wwid": "500143803110429D",
        "bay": 1,
        "driveBays": [
            {
                "type": "drive-bay",
                "model": "SAS 2048",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "1",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610136",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610136",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "1:1:1"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "1",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710136J4524YPT",
                    "capacity": "2048",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 1",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 1",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 2048",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "2",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610137",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610137",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "1:1:2"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "2",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710137J4524YPT",
                    "capacity": "2048",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 2",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 2",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 500",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "3",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610138",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610138",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "1:1:3"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "3",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710138J4524YPT",
                    "capacity": "500",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 3",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 3",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 500",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "4",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610139",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610139",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "1:1:4"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "4",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710139J4524YPT",
                    "capacity": "500",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 4",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 4",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 80",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "5",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610141",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610141",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "1:1:6"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "5",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710141J4524YPT",
                    "capacity": "80",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 5",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 5",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 80",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "6",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610142",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610142",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "1:1:7"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "6",
                                "type": "Bay"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710142J4524YPT",
                    "capacity": "80",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 6",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 6",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 80",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "7",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610143",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610143",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "1:1:8"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "Bay"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710143J4524YPT",
                    "capacity": "80",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 7",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 7",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 80",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "8",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610144",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610144",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "1:1:9"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "8",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710144J4524YPT",
                    "capacity": "80",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 8",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 8",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 80",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "9",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610145",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610145",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "1:1:10"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "9",
                                "type": "Bay"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710145J4524YPT",
                    "capacity": "80",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 9",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 9",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 80",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "10",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610146",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610146",
                    "deviceInterface": "SAS",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "1:1:11"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            },
                            {
                                "value": "10",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710146J4524YPT",
                    "capacity": "80",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 10",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 10",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "11",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610147",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610147",
                    "deviceInterface": "SAS",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "1:1:12"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "11",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710147J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 11",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 11",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "12",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610148",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610148",
                    "deviceInterface": "SAS",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "1:1:13"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "12",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710148J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 12",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 12",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "13",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610149",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610149",
                    "deviceInterface": "SAS",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "1:1:14"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "13",
                                "type": "Bay"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710149J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 13",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 13",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "14",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610150",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610150",
                    "deviceInterface": "SAS",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "1:1:15"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "14",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710150J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 14",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 14",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "15",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610151",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610151",
                    "deviceInterface": "SAS",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "1:1:16"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "15",
                                "type": "Bay"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710151J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 15",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 15",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "16",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610152",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610152",
                    "deviceInterface": "SAS",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "1:1:17"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "16",
                                "type": "Bay"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710152J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 16",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 16",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "17",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610153",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610153",
                    "deviceInterface": "SAS",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "1:1:18"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "17",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710153J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 17",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 17",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "18",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610154",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610154",
                    "deviceInterface": "SAS",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "1:1:19"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "18",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710154J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 18",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 18",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "19",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610155",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610155",
                    "deviceInterface": "SAS",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "1:1:20"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "19",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710155J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 19",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 19",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "20",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610156",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610156",
                    "deviceInterface": "SATA",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "1:1:21"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "20",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710156J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 20",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 20",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "21",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610157",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610157",
                    "deviceInterface": "SATA",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "1:1:22"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "21",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710157J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 21",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 21",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 500",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "22",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610158",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610158",
                    "deviceInterface": "SATA",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "1:1:23"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            },
                            {
                                "value": "22",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710158J4524YPT",
                    "capacity": "500",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 22",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 22",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 500",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "23",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610159",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610159",
                    "deviceInterface": "SATA",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "1:1:24"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            },
                            {
                                "value": "23",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710159J4524YPT",
                    "capacity": "500",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 23",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 23",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 500",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "24",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610160",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610160",
                    "deviceInterface": "SATA",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "1:1:25"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "24",
                                "type": "Bay"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710160J4524YPT",
                    "capacity": "500",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 24",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 24",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 500",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "25",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610161",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610161",
                    "deviceInterface": "SATA",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "1:1:26"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "25",
                                "type": "Bay"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710161J4524YPT",
                    "capacity": "500",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 25",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 25",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 500",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "26",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610162",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610162",
                    "deviceInterface": "SATA",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "1:1:27"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "26",
                                "type": "Bay"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710162J4524YPT",
                    "capacity": "500",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 26",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 26",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 500",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "27",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610163",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610163",
                    "deviceInterface": "SATA",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "1:1:28"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "27",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710163J4524YPT",
                    "capacity": "500",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 27",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 27",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 500",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "28",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610164",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610164",
                    "deviceInterface": "SATA",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "1:1:29"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "28",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710164J4524YPT",
                    "capacity": "500",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 28",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 28",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 80",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "29",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610165",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610165",
                    "deviceInterface": "SATA",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "1:1:30"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "29",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710165J4524YPT",
                    "capacity": "80",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 29",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 29",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 80",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "30",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610166",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610166",
                    "deviceInterface": "SATA",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "1:1:31"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "30",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710166J4524YPT",
                    "capacity": "80",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 30",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 30",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 80",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "31",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610167",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610167",
                    "deviceInterface": "SATA",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "1:1:32"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "31",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710167J4524YPT",
                    "capacity": "80",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 31",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 31",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 80",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "32",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610168",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610168",
                    "deviceInterface": "SATA",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "1:1:33"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "32",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710168J4524YPT",
                    "capacity": "80",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 32",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 32",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "33",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610169",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610169",
                    "deviceInterface": "SATA",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "1:1:34"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "33",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710169J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 33",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 33",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "34",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610170",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610170",
                    "deviceInterface": "SATA",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "1:1:35"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "34",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710170J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 34",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 34",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "35",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610171",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610171",
                    "deviceInterface": "SATA",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "1:1:36"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "35",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710171J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 35",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 35",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "36",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610172",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610172",
                    "deviceInterface": "SATA",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "1:1:37"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "36",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710172J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 36",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 36",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "37",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610173",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610173",
                    "deviceInterface": "SATA",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "1:1:38"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "37",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710173J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 37",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 37",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 6144",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "38",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610174",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610174",
                    "deviceInterface": "SATA",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "1:1:39"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "38",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710174J4524YPT",
                    "capacity": "6144",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 38",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 38",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 6144",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "39",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610175",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610175",
                    "deviceInterface": "SATA",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "1:1:40"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "39",
                                "type": "Bay"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710175J4524YPT",
                    "capacity": "6144",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 39",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 39",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "40",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610180",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610180",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "7:4:5"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            },
                            {
                                "value": "40",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710180J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 40",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 40",
                "description": None,
                "status": None,
                "category": "drive-bays",
            }
        ],
        "driveEnclosurePortMap": {
            "deviceSlots": [
                {
                    "deviceName": None,
                    "slotNumber": "1",
                    "physicalPorts": [
                        {
                            "interconnectName": "0000A66103, interconnect 4",
                            "interconnectPortNumber": "1",
                            "physicalInterconnectName": "0000A66103, interconnect 4",
                            "physicalInterconnectPortNumber": "1",
                            "type": "SAS"
                        },
                        {
                            "interconnectName": "0000A66103, interconnect 4",
                            "interconnectPortNumber": "2",
                            "physicalInterconnectName": "0000A66103, interconnect 4",
                            "physicalInterconnectPortNumber": "2",
                            "type": "SAS"
                        }
                    ],
                    "location": "IO Adapter"
                },
                {
                    "deviceName": None,
                    "slotNumber": "2",
                    "physicalPorts": [
                        {
                            "interconnectName": "0000A66103, interconnect 4",
                            "interconnectPortNumber": "1",
                            "physicalInterconnectName": "0000A66103, interconnect 4",
                            "physicalInterconnectPortNumber": "1",
                            "type": "SAS"
                        },
                        {
                            "interconnectName": "0000A66103, interconnect 4",
                            "interconnectPortNumber": "2",
                            "physicalInterconnectName": "0000A66103, interconnect 4",
                            "physicalInterconnectPortNumber": "2",
                            "type": "SAS"
                        }
                    ],
                    "location": "IO Adapter"
                }
            ],
            "type": "DriveEnclosurePortMap"
        },
        "hardResetState": "Normal",
        "ioAdapters": [
            {
                "type": "drive-enclosure-ioadapter",
                "firmwareVersion": "0.50",
                "partNumber": "755872-001",
                "ports": [
                    {
                        "type": "sas-port",
                        "portName": "2",
                        "portType": "Downlink",
                        "portStatusReason": "None",
                        "portIdentifier": "2",
                        "portLocation": "2",
                        "phyCount": 4,
                        "enabled": True,
                        "description": None,
                        "status": "OK",
                        "name": "2",
                        "category": "sas-ports",
                    },
                    {
                        "type": "sas-port",
                        "portName": "1",
                        "portType": "Downlink",
                        "portStatusReason": "None",
                        "portIdentifier": "1",
                        "portLocation": "1",
                        "phyCount": 4,
                        "enabled": True,
                        "description": None,
                        "status": "OK",
                        "name": "1",
                        "category": "sas-ports",
                    }
                ],
                "model": "Synergy D3940 Storage Module IO Adapter",
                "portCount": 2,
                "manufacturer": "HPE",
                "wwid": "5001438031104209",
                "redundantIoModule": "Installed",
                "ioAdapterLocation": {
                        "locationEntries": [
                            {
                                "value": "2",
                                "type": "Slot"
                            }
                        ]
                },
                "serialNumber": "50454e5445305109",
                "description": "",
                "status": "OK",
                "name": None,
                "category": "",
            },
            {
                "type": "drive-enclosure-ioadapter",
                "firmwareVersion": "0.50",
                "partNumber": "755872-001",
                "ports": [
                    {
                        "type": "sas-port",
                        "portName": "2",
                        "portType": "Downlink",
                        "portStatusReason": "None",
                        "portIdentifier": "2",
                        "portLocation": "2",
                        "phyCount": 4,
                        "enabled": True,
                        "description": None,
                        "status": "OK",
                        "name": "2",
                        "category": "sas-ports",
                    },
                    {
                        "type": "sas-port",
                        "portName": "1",
                        "portType": "Downlink",
                        "portStatusReason": "None",
                        "portIdentifier": "1",
                        "portLocation": "1",
                        "phyCount": 4,
                        "enabled": True,
                        "description": None,
                        "status": "OK",
                        "name": "1",
                        "category": "sas-ports",
                    }
                ],
                "model": "Synergy D3940 Storage Module IO Adapter",
                "portCount": 2,
                "manufacturer": "HPE",
                "wwid": "5001438031104208",
                "redundantIoModule": "Installed",
                "ioAdapterLocation": {
                        "locationEntries": [
                            {
                                "value": "1",
                                "type": "Slot"
                            }
                        ]
                },
                "serialNumber": "50454e5445305108",
                "description": "",
                "status": "OK",
                "name": None,
                "category": "",
            }
        ],
        "ioAdapterCount": 2,
        "serialNumber": "SN123104",
        "refreshState": None,
        "description": "",
        "status": "OK",
        "name": "0000A66103, bay 1",
        "category": "drive-enclosures",
    },
    {
        "type": "drive-enclosure",
        "firmwareVersion": "0.18",
        "partNumber": "755984-B21",
        "model": "Synergy D3940 Storage Module",
        "productName": "Storage Enclosure 500143803110229D",
        "enclosureName": "0000A66102",
        "interconnectBaySet": 1,
        "manufacturer": "HPE",
        "driveEnclosureLocation": {
                "locationEntries": [
                    {
                        "value": "/rest/enclosures/0000000000A66102",
                        "type": "Enclosure"
                    },
                    {
                        "value": "1",
                        "type": "Bay"
                    },
                    {
                        "value": "1",
                        "type": "SasPort"
                    }
                ]
        },
        "driveBayCount": 40,
        "wwid": "500143803110229D",
        "bay": 1,
        "driveBays": [
            {
                "type": "drive-bay",
                "model": "SAS 2048",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "1",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610068",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610068",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "1:1:1"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "1",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710068J4524YPT",
                    "capacity": "2048",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 1",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 1",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 2048",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "2",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610069",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610069",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "1:1:2"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "2",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710069J4524YPT",
                    "capacity": "2048",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 2",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 2",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 500",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "3",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610070",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610070",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "1:1:3"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "3",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710070J4524YPT",
                    "capacity": "500",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 3",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 3",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 500",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "4",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610071",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610071",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "1:1:4"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "4",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710071J4524YPT",
                    "capacity": "500",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 4",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 4",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 500",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "5",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610072",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610072",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "1:1:5"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "5",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710072J4524YPT",
                    "capacity": "500",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 5",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 5",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 500",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "6",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610073",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610073",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "1:1:6"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "6",
                                "type": "Bay"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710073J4524YPT",
                    "capacity": "500",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 6",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 6",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 500",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "7",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610074",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610074",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "1:1:7"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "Bay"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710074J4524YPT",
                    "capacity": "500",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 7",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 7",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 80",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "8",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610075",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610075",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "1:1:8"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "8",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710075J4524YPT",
                    "capacity": "80",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 8",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 8",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 80",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "9",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610076",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610076",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "1:1:9"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "9",
                                "type": "Bay"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710076J4524YPT",
                    "capacity": "80",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 9",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 9",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 80",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "10",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610077",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610077",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "1:1:10"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            },
                            {
                                "value": "10",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710077J4524YPT",
                    "capacity": "80",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 10",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 10",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 80",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "11",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610078",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610078",
                    "deviceInterface": "SAS",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "1:1:11"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "11",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710078J4524YPT",
                    "capacity": "80",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 11",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 11",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "12",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610079",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610079",
                    "deviceInterface": "SAS",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "1:1:12"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "12",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710079J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 12",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 12",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "13",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610080",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610080",
                    "deviceInterface": "SAS",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "1:1:13"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "13",
                                "type": "Bay"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710080J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 13",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 13",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "14",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610081",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610081",
                    "deviceInterface": "SAS",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "1:1:14"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "14",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710081J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 14",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 14",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "15",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610082",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610082",
                    "deviceInterface": "SAS",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "1:1:15"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "15",
                                "type": "Bay"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710082J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 15",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 15",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "16",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610083",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610083",
                    "deviceInterface": "SAS",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "1:1:16"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "16",
                                "type": "Bay"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710083J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 16",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 16",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "17",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610084",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610084",
                    "deviceInterface": "SAS",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "1:1:17"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "17",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710084J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 17",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 17",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "18",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610085",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610085",
                    "deviceInterface": "SAS",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "1:1:18"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "18",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710085J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 18",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 18",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "19",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610086",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610086",
                    "deviceInterface": "SAS",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "1:1:19"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "19",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710086J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 19",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 19",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "20",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610087",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610087",
                    "deviceInterface": "SAS",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "1:1:20"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "20",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710087J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 20",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 20",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "21",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610089",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610089",
                    "deviceInterface": "SATA",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "1:1:22"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "21",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710089J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 21",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 21",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "22",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610090",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610090",
                    "deviceInterface": "SATA",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "1:1:23"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            },
                            {
                                "value": "22",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710090J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 22",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 22",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 500",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "23",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610091",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610091",
                    "deviceInterface": "SATA",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "1:1:24"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            },
                            {
                                "value": "23",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710091J4524YPT",
                    "capacity": "500",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 23",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 23",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 500",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "24",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610092",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610092",
                    "deviceInterface": "SATA",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "1:1:25"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "24",
                                "type": "Bay"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710092J4524YPT",
                    "capacity": "500",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 24",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 24",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 500",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "25",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610093",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610093",
                    "deviceInterface": "SATA",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "1:1:26"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "25",
                                "type": "Bay"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710093J4524YPT",
                    "capacity": "500",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 25",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 25",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 500",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "26",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610094",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610094",
                    "deviceInterface": "SATA",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "1:1:27"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "26",
                                "type": "Bay"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710094J4524YPT",
                    "capacity": "500",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 26",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 26",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 80",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "27",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610095",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610095",
                    "deviceInterface": "SATA",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "1:1:28"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "27",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710095J4524YPT",
                    "capacity": "80",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 27",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 27",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 80",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "28",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610096",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610096",
                    "deviceInterface": "SATA",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "1:1:29"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "28",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710096J4524YPT",
                    "capacity": "80",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 28",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 28",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 80",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "29",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610097",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610097",
                    "deviceInterface": "SATA",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "1:1:30"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "29",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710097J4524YPT",
                    "capacity": "80",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 29",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 29",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 80",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "30",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610098",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610098",
                    "deviceInterface": "SATA",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "1:1:31"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "30",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710098J4524YPT",
                    "capacity": "80",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 30",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 30",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 80",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "31",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610099",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610099",
                    "deviceInterface": "SATA",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "1:1:32"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "31",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710099J4524YPT",
                    "capacity": "80",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 31",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 31",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 80",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "32",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610100",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610100",
                    "deviceInterface": "SATA",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "1:1:33"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "32",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710100J4524YPT",
                    "capacity": "80",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 32",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 32",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 80",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "33",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610101",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610101",
                    "deviceInterface": "SATA",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "1:1:34"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "33",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710101J4524YPT",
                    "capacity": "80",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 33",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 33",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "34",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610102",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610102",
                    "deviceInterface": "SATA",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "1:1:35"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "34",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710102J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 34",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 34",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "35",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610103",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610103",
                    "deviceInterface": "SATA",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "1:1:36"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "35",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710103J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 35",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 35",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "36",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610104",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610104",
                    "deviceInterface": "SATA",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "1:1:37"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "36",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710104J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 36",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 36",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "37",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610105",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610105",
                    "deviceInterface": "SATA",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "1:1:38"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "37",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710105J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 37",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 37",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 6144",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "38",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610106",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610106",
                    "deviceInterface": "SATA",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "1:1:39"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "38",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710106J4524YPT",
                    "capacity": "6144",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 38",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 38",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 6144",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "39",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610107",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610107",
                    "deviceInterface": "SATA",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "1:1:40"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "39",
                                "type": "Bay"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710107J4524YPT",
                    "capacity": "6144",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 39",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 39",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "40",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610112",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610112",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "7:4:5"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "1",
                                "type": "SasPort"
                            },
                            {
                                "value": "40",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710112J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 40",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 40",
                "description": None,
                "status": None,
                "category": "drive-bays",
            }
        ],
        "driveEnclosurePortMap": {
            "deviceSlots": [
                {
                    "deviceName": None,
                    "slotNumber": "1",
                    "physicalPorts": [
                        {
                            "interconnectName": "0000A66102, interconnect 4",
                            "interconnectPortNumber": "1",
                            "physicalInterconnectName": "0000A66102, interconnect 4",
                            "physicalInterconnectPortNumber": "1",
                            "type": "SAS"
                        },
                        {
                            "interconnectName": "0000A66102, interconnect 4",
                            "interconnectPortNumber": "2",
                            "physicalInterconnectName": "0000A66102, interconnect 4",
                            "physicalInterconnectPortNumber": "2",
                            "type": "SAS"
                        }
                    ],
                    "location": "IO Adapter"
                },
                {
                    "deviceName": None,
                    "slotNumber": "2",
                    "physicalPorts": [
                        {
                            "interconnectName": "0000A66102, interconnect 4",
                            "interconnectPortNumber": "1",
                            "physicalInterconnectName": "0000A66102, interconnect 4",
                            "physicalInterconnectPortNumber": "1",
                            "type": "SAS"
                        },
                        {
                            "interconnectName": "0000A66102, interconnect 4",
                            "interconnectPortNumber": "2",
                            "physicalInterconnectName": "0000A66102, interconnect 4",
                            "physicalInterconnectPortNumber": "2",
                            "type": "SAS"
                        }
                    ],
                    "location": "IO Adapter"
                }
            ],
            "type": "DriveEnclosurePortMap"
        },
        "hardResetState": "Normal",
        "ioAdapters": [
            {
                "type": "drive-enclosure-ioadapter",
                "firmwareVersion": "0.50",
                "partNumber": "755872-001",
                "ports": [
                    {
                        "type": "sas-port",
                        "portName": "1",
                        "portType": "Downlink",
                        "portStatusReason": "None",
                        "portIdentifier": "1",
                        "portLocation": "1",
                        "phyCount": 4,
                        "enabled": True,
                        "description": None,
                        "status": "OK",
                        "name": "1",
                        "category": "sas-ports",
                    },
                    {
                        "type": "sas-port",
                        "portName": "2",
                        "portType": "Downlink",
                        "portStatusReason": "None",
                        "portIdentifier": "2",
                        "portLocation": "2",
                        "phyCount": 4,
                        "enabled": True,
                        "description": None,
                        "status": "OK",
                        "name": "2",
                        "category": "sas-ports",
                    }
                ],
                "model": "Synergy D3940 Storage Module IO Adapter",
                "portCount": 2,
                "manufacturer": "HPE",
                "wwid": "5001438031102204",
                "redundantIoModule": "Installed",
                "ioAdapterLocation": {
                        "locationEntries": [
                            {
                                "value": "1",
                                "type": "Slot"
                            }
                        ]
                },
                "serialNumber": "50454e5445305104",
                "description": "",
                "status": "OK",
                "name": None,
                "category": "",
            },
            {
                "type": "drive-enclosure-ioadapter",
                "firmwareVersion": "0.50",
                "partNumber": "755872-001",
                "ports": [
                    {
                        "type": "sas-port",
                        "portName": "2",
                        "portType": "Downlink",
                        "portStatusReason": "None",
                        "portIdentifier": "2",
                        "portLocation": "2",
                        "phyCount": 4,
                        "enabled": True,
                        "description": None,
                        "status": "OK",
                        "name": "2",
                        "category": "sas-ports",
                    },
                    {
                        "type": "sas-port",
                        "portName": "1",
                        "portType": "Downlink",
                        "portStatusReason": "None",
                        "portIdentifier": "1",
                        "portLocation": "1",
                        "phyCount": 4,
                        "enabled": True,
                        "description": None,
                        "status": "OK",
                        "name": "1",
                        "category": "sas-ports",
                    }
                ],
                "model": "Synergy D3940 Storage Module IO Adapter",
                "portCount": 2,
                "manufacturer": "HPE",
                "wwid": "5001438031102205",
                "redundantIoModule": "Installed",
                "ioAdapterLocation": {
                        "locationEntries": [
                            {
                                "value": "2",
                                "type": "Slot"
                            }
                        ]
                },
                "serialNumber": "50454e5445305105",
                "description": "",
                "status": "OK",
                "name": None,
                "category": "",
            }
        ],
        "ioAdapterCount": 2,
        "serialNumber": "SN123102",
        "refreshState": None,
        "description": "",
        "status": "OK",
        "name": "0000A66102, bay 1",
        "category": "drive-enclosures",
    },
    {
        "type": "drive-enclosure",
        "firmwareVersion": "0.18",
        "partNumber": "755984-B21",
        "model": "Synergy D3940 Storage Module",
        "productName": "Storage Enclosure 500143803110329D",
        "enclosureName": "0000A66102",
        "interconnectBaySet": 1,
        "manufacturer": "HPE",
        "driveEnclosureLocation": {
                "locationEntries": [
                    {
                        "value": "7",
                        "type": "SasPort"
                    },
                    {
                        "value": "7",
                        "type": "Bay"
                    },
                    {
                        "value": "/rest/enclosures/0000000000A66102",
                        "type": "Enclosure"
                    }
                ]
        },
        "driveBayCount": 40,
        "wwid": "500143803110329D",
        "bay": 7,
        "driveBays": [
            {
                "type": "drive-bay",
                "model": "SAS 2048",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "1",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610108",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610108",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "7:4:1"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "1",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710108J4524YPT",
                    "capacity": "2048",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 1",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 1",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 2048",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "2",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610109",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610109",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "7:4:2"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "2",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710109J4524YPT",
                    "capacity": "2048",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 2",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 2",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "3",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610110",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610110",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "7:4:3"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "3",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710110J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 3",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 3",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "4",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610111",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610111",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "7:4:4"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "4",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710111J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 4",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 4",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "5",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610113",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610113",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "7:4:6"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "5",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710113J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 5",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 5",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "6",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610114",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610114",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "7:4:7"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "6",
                                "type": "Bay"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710114J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 6",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 6",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 500",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "7",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610115",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610115",
                    "deviceInterface": "SAS",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "7:4:8"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "7",
                                "type": "Bay"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710115J4524YPT",
                    "capacity": "500",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 7",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 7",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 500",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "8",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610116",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610116",
                    "deviceInterface": "SAS",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "7:4:9"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "8",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710116J4524YPT",
                    "capacity": "500",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 8",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 8",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 500",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "9",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610117",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610117",
                    "deviceInterface": "SAS",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "7:4:10"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "9",
                                "type": "Bay"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710117J4524YPT",
                    "capacity": "500",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 9",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 9",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 500",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "10",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610118",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610118",
                    "deviceInterface": "SAS",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "7:4:11"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "10",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710118J4524YPT",
                    "capacity": "500",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 10",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 10",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 80",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "11",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610119",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610119",
                    "deviceInterface": "SAS",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "7:4:12"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "11",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710119J4524YPT",
                    "capacity": "80",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 11",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 11",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 80",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "12",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610120",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610120",
                    "deviceInterface": "SAS",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "7:4:13"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "12",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710120J4524YPT",
                    "capacity": "80",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 12",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 12",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 80",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "13",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610121",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610121",
                    "deviceInterface": "SAS",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "7:4:14"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "13",
                                "type": "Bay"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710121J4524YPT",
                    "capacity": "80",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 13",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 13",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 80",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "14",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610122",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610122",
                    "deviceInterface": "SATA",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "7:4:15"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "14",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710122J4524YPT",
                    "capacity": "80",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 14",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 14",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 80",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "15",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610123",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610123",
                    "deviceInterface": "SATA",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "7:4:16"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "15",
                                "type": "Bay"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710123J4524YPT",
                    "capacity": "80",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 15",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 15",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "16",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610124",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610124",
                    "deviceInterface": "SATA",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "7:4:17"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "16",
                                "type": "Bay"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710124J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 16",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 16",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "17",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610125",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610125",
                    "deviceInterface": "SATA",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "7:4:18"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "17",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710125J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 17",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 17",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "18",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610126",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610126",
                    "deviceInterface": "SATA",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "7:4:19"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "18",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710126J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 18",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 18",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "19",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610127",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610127",
                    "deviceInterface": "SATA",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "7:4:20"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "19",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710127J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 19",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 19",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "20",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610128",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610128",
                    "deviceInterface": "SATA",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "7:4:21"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "20",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710128J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 20",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 20",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "21",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610129",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610129",
                    "deviceInterface": "SATA",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "7:4:22"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "21",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710129J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 21",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 21",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "22",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610130",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610130",
                    "deviceInterface": "SATA",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "7:4:23"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "22",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710130J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 22",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 22",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "23",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610131",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610131",
                    "deviceInterface": "SATA",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "7:4:24"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "23",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710131J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 23",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 23",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "24",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610132",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610132",
                    "deviceInterface": "SATA",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "7:4:25"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "24",
                                "type": "Bay"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710132J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 24",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 24",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "25",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610133",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610133",
                    "deviceInterface": "SATA",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "7:4:26"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "25",
                                "type": "Bay"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710133J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 25",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 25",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 6144",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "26",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610134",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610134",
                    "deviceInterface": "SATA",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "7:4:27"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "26",
                                "type": "Bay"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710134J4524YPT",
                    "capacity": "6144",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 26",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 26",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 6144",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "27",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610135",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610135",
                    "deviceInterface": "SATA",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "7:4:28"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "27",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710135J4524YPT",
                    "capacity": "6144",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 27",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 27",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 80",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "28",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610140",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610140",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "1:1:5"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "28",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710140J4524YPT",
                    "capacity": "80",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 28",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 28",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "29",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "Drive Bay 29",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "30",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "Drive Bay 30",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "31",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "Drive Bay 31",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "32",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "Drive Bay 32",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "33",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "Drive Bay 33",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "34",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "Drive Bay 34",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "35",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "Drive Bay 35",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "36",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "Drive Bay 36",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "37",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "Drive Bay 37",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "38",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "Drive Bay 38",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "39",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "Drive Bay 39",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "40",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "Drive Bay 40",
                "description": None,
                "status": None,
                "category": "drive-bays",
            }
        ],
        "driveEnclosurePortMap": {
            "deviceSlots": [
                {
                    "deviceName": None,
                    "slotNumber": "1",
                    "physicalPorts": [
                        {
                            "interconnectName": "0000A66102, interconnect 4",
                            "interconnectPortNumber": "7",
                            "physicalInterconnectName": "0000A66102, interconnect 4",
                            "physicalInterconnectPortNumber": "7",
                            "type": "SAS"
                        },
                        {
                            "interconnectName": "0000A66102, interconnect 4",
                            "interconnectPortNumber": "8",
                            "physicalInterconnectName": "0000A66102, interconnect 4",
                            "physicalInterconnectPortNumber": "8",
                            "type": "SAS"
                        }
                    ],
                    "location": "IO Adapter"
                },
                {
                    "deviceName": None,
                    "slotNumber": "2",
                    "physicalPorts": [
                        {
                            "interconnectName": "0000A66102, interconnect 4",
                            "interconnectPortNumber": "7",
                            "physicalInterconnectName": "0000A66102, interconnect 4",
                            "physicalInterconnectPortNumber": "7",
                            "type": "SAS"
                        },
                        {
                            "interconnectName": "0000A66102, interconnect 4",
                            "interconnectPortNumber": "8",
                            "physicalInterconnectName": "0000A66102, interconnect 4",
                            "physicalInterconnectPortNumber": "8",
                            "type": "SAS"
                        }
                    ],
                    "location": "IO Adapter"
                }
            ],
            "type": "DriveEnclosurePortMap"
        },
        "hardResetState": "Normal",
        "ioAdapters": [
            {
                "type": "drive-enclosure-ioadapter",
                "firmwareVersion": "0.50",
                "partNumber": "755872-001",
                "ports": [
                    {
                        "type": "sas-port",
                        "portName": "2",
                        "portType": "Downlink",
                        "portStatusReason": "None",
                        "portIdentifier": "2",
                        "portLocation": "2",
                        "phyCount": 4,
                        "enabled": True,
                        "description": None,
                        "status": "OK",
                        "name": "2",
                        "category": "sas-ports",
                    },
                    {
                        "type": "sas-port",
                        "portName": "1",
                        "portType": "Downlink",
                        "portStatusReason": "None",
                        "portIdentifier": "1",
                        "portLocation": "1",
                        "phyCount": 4,
                        "enabled": True,
                        "description": None,
                        "status": "OK",
                        "name": "1",
                        "category": "sas-ports",
                    }
                ],
                "model": "Synergy D3940 Storage Module IO Adapter",
                "portCount": 2,
                "manufacturer": "HPE",
                "wwid": "5001438031103207",
                "redundantIoModule": "Installed",
                "ioAdapterLocation": {
                        "locationEntries": [
                            {
                                "value": "2",
                                "type": "Slot"
                            }
                        ]
                },
                "serialNumber": "50454e5445305107",
                "description": "",
                "status": "OK",
                "name": None,
                "category": "",
            },
            {
                "type": "drive-enclosure-ioadapter",
                "firmwareVersion": "0.50",
                "partNumber": "755872-001",
                "ports": [
                    {
                        "type": "sas-port",
                        "portName": "1",
                        "portType": "Downlink",
                        "portStatusReason": "None",
                        "portIdentifier": "1",
                        "portLocation": "1",
                        "phyCount": 4,
                        "enabled": True,
                        "description": None,
                        "status": "OK",
                        "name": "1",
                        "category": "sas-ports",
                    },
                    {
                        "type": "sas-port",
                        "portName": "2",
                        "portType": "Downlink",
                        "portStatusReason": "None",
                        "portIdentifier": "2",
                        "portLocation": "2",
                        "phyCount": 4,
                        "enabled": True,
                        "description": None,
                        "status": "OK",
                        "name": "2",
                        "category": "sas-ports",
                    }
                ],
                "model": "Synergy D3940 Storage Module IO Adapter",
                "portCount": 2,
                "manufacturer": "HPE",
                "wwid": "5001438031103206",
                "redundantIoModule": "Installed",
                "ioAdapterLocation": {
                        "locationEntries": [
                            {
                                "value": "1",
                                "type": "Slot"
                            }
                        ]
                },
                "serialNumber": "50454e5445305106",
                "description": "",
                "status": "OK",
                "name": None,
                "category": "",
            }
        ],
        "ioAdapterCount": 2,
        "serialNumber": "SN123103",
        "refreshState": None,
        "description": "",
        "status": "OK",
        "name": "0000A66102, bay 7",
        "category": "drive-enclosures",
    },
    {
        "type": "drive-enclosure",
        "firmwareVersion": "0.18",
        "partNumber": "755984-B21",
        "model": "Synergy D3940 Storage Module",
        "productName": "Storage Enclosure 500143803110129D",
        "enclosureName": "0000A66101",
        "interconnectBaySet": 1,
        "manufacturer": "HPE",
        "driveEnclosureLocation": {
                "locationEntries": [
                    {
                        "value": "7",
                        "type": "SasPort"
                    },
                    {
                        "value": "7",
                        "type": "Bay"
                    },
                    {
                        "value": "/rest/enclosures/0000000000A66101",
                        "type": "Enclosure"
                    }
                ]
        },
        "driveBayCount": 40,
        "wwid": "500143803110129D",
        "bay": 7,
        "driveBays": [
            {
                "type": "drive-bay",
                "model": "SAS 2048",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "1",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610040",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610040",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "7:4:1"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "1",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710040J4524YPT",
                    "capacity": "2048",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 1",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 1",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 2048",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "2",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610041",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610041",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "7:4:2"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "2",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710041J4524YPT",
                    "capacity": "2048",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 2",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 2",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "3",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610042",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610042",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "7:4:3"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "3",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710042J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 3",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 3",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "4",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610043",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610043",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "7:4:4"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "4",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710043J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 4",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 4",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "5",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610044",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610044",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "7:4:5"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "5",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710044J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 5",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 5",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "6",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610045",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610045",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "7:4:6"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "6",
                                "type": "Bay"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710045J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 6",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 6",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "7",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610046",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610046",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "7:4:7"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "7",
                                "type": "Bay"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710046J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 7",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 7",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 500",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "8",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610047",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610047",
                    "deviceInterface": "SAS",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "7:4:8"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "8",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710047J4524YPT",
                    "capacity": "500",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 8",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 8",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 500",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "9",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610048",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610048",
                    "deviceInterface": "SAS",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "7:4:9"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "9",
                                "type": "Bay"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710048J4524YPT",
                    "capacity": "500",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 9",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 9",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 500",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "10",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610049",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610049",
                    "deviceInterface": "SAS",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "7:4:10"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "10",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710049J4524YPT",
                    "capacity": "500",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 10",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 10",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 500",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "11",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610050",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610050",
                    "deviceInterface": "SAS",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "7:4:11"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "11",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710050J4524YPT",
                    "capacity": "500",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 11",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 11",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 80",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "12",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610051",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610051",
                    "deviceInterface": "SAS",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "7:4:12"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "12",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710051J4524YPT",
                    "capacity": "80",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 12",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 12",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 80",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "13",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610052",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610052",
                    "deviceInterface": "SAS",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "7:4:13"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "13",
                                "type": "Bay"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710052J4524YPT",
                    "capacity": "80",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 13",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 13",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 80",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "14",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610053",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610053",
                    "deviceInterface": "SAS",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "7:4:14"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "14",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710053J4524YPT",
                    "capacity": "80",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 14",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "Drive Bay 14",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 80",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "15",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610054",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610054",
                    "deviceInterface": "SATA",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "7:4:15"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "15",
                                "type": "Bay"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710054J4524YPT",
                    "capacity": "80",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 15",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 15",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "16",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610055",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610055",
                    "deviceInterface": "SATA",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "7:4:16"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "16",
                                "type": "Bay"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710055J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 16",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 16",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "17",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610056",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610056",
                    "deviceInterface": "SATA",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "7:4:17"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "17",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710056J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 17",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 17",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 80",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "18",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610057",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610057",
                    "deviceInterface": "SATA",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "7:4:18"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "18",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710057J4524YPT",
                    "capacity": "80",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 18",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 18",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "19",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610058",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610058",
                    "deviceInterface": "SATA",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "7:4:19"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "19",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710058J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 19",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 19",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "20",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610059",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610059",
                    "deviceInterface": "SATA",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "7:4:20"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "20",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710059J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 20",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 20",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "21",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610060",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610060",
                    "deviceInterface": "SATA",
                    "driveMedia": "HDD",
                    "drivePaths": [
                        "7:4:21"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "21",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710060J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 21",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 21",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "22",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610061",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610061",
                    "deviceInterface": "SATA",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "7:4:22"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "22",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710061J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 22",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 22",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "23",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610062",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610062",
                    "deviceInterface": "SATA",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "7:4:23"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "23",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710062J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 23",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 23",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "24",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610063",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610063",
                    "deviceInterface": "SATA",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "7:4:24"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "24",
                                "type": "Bay"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710063J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 24",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 24",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "25",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610064",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610064",
                    "deviceInterface": "SATA",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "7:4:25"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "25",
                                "type": "Bay"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710064J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 25",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 25",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 600",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "26",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610065",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610065",
                    "deviceInterface": "SATA",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "7:4:26"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "26",
                                "type": "Bay"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710065J4524YPT",
                    "capacity": "600",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 26",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 26",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 6144",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "27",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610066",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610066",
                    "deviceInterface": "SATA",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "7:4:27"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "27",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710066J4524YPT",
                    "capacity": "6144",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 27",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 27",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SATA 6144",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "28",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA03C610067",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HP01",
                    "model": "MM2000JEFRC",
                    "blockSize": 512,
                    "wwid": "5000CCA03C610067",
                    "deviceInterface": "SATA",
                    "driveMedia": "SSD",
                    "drivePaths": [
                        "7:4:28"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "7",
                                "type": "SasPort"
                            },
                            {
                                "value": "4",
                                "type": "Box"
                            },
                            {
                                "value": "28",
                                "type": "Bay"
                            }
                        ]
                    },
                    "rotationalRpms": 7200,
                    "linkRateInGbs": 6,
                    "authentic": "yes",
                    "serialNumber": "S46016710067J4524YPT",
                    "capacity": "6144",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "Drive 28",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SATA",
                "name": "Drive Bay 28",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "29",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "Drive Bay 29",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "30",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "Drive Bay 30",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "31",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "Drive Bay 31",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "32",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "Drive Bay 32",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "33",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "Drive Bay 33",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "34",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "Drive Bay 34",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "35",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "Drive Bay 35",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "36",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "Drive Bay 36",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "37",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "Drive Bay 37",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "38",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "Drive Bay 38",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "39",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "Drive Bay 39",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "40",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "Drive Bay 40",
                "description": None,
                "status": None,
                "category": "drive-bays",
            }
        ],
        "driveEnclosurePortMap": {
            "deviceSlots": [
                {
                    "deviceName": None,
                    "slotNumber": "1",
                    "physicalPorts": [
                        {
                            "interconnectName": "0000A66101, interconnect 4",
                            "interconnectPortNumber": "7",
                            "physicalInterconnectName": "0000A66101, interconnect 4",
                            "physicalInterconnectPortNumber": "7",
                            "type": "SAS"
                        },
                        {
                            "interconnectName": "0000A66101, interconnect 4",
                            "interconnectPortNumber": "8",
                            "physicalInterconnectName": "0000A66101, interconnect 4",
                            "physicalInterconnectPortNumber": "8",
                            "type": "SAS"
                        }
                    ],
                    "location": "IO Adapter"
                },
                {
                    "deviceName": None,
                    "slotNumber": "2",
                    "physicalPorts": [
                        {
                            "interconnectName": "0000A66101, interconnect 4",
                            "interconnectPortNumber": "7",
                            "physicalInterconnectName": "0000A66101, interconnect 4",
                            "physicalInterconnectPortNumber": "7",
                            "type": "SAS"
                        },
                        {
                            "interconnectName": "0000A66101, interconnect 4",
                            "interconnectPortNumber": "8",
                            "physicalInterconnectName": "0000A66101, interconnect 4",
                            "physicalInterconnectPortNumber": "8",
                            "type": "SAS"
                        }
                    ],
                    "location": "IO Adapter"
                }
            ],
            "type": "DriveEnclosurePortMap"
        },
        "hardResetState": "Normal",
        "ioAdapters": [
            {
                "type": "drive-enclosure-ioadapter",
                "firmwareVersion": "0.50",
                "partNumber": "755872-001",
                "ports": [
                    {
                        "type": "sas-port",
                        "portName": "2",
                        "portType": "Downlink",
                        "portStatusReason": "None",
                        "portIdentifier": "2",
                        "portLocation": "2",
                        "phyCount": 4,
                        "enabled": True,
                        "description": None,
                        "status": "OK",
                        "name": "2",
                        "category": "sas-ports",
                    },
                    {
                        "type": "sas-port",
                        "portName": "1",
                        "portType": "Downlink",
                        "portStatusReason": "None",
                        "portIdentifier": "1",
                        "portLocation": "1",
                        "phyCount": 4,
                        "enabled": True,
                        "description": None,
                        "status": "OK",
                        "name": "1",
                        "category": "sas-ports",
                    }
                ],
                "model": "Synergy D3940 Storage Module IO Adapter",
                "portCount": 2,
                "manufacturer": "HPE",
                "wwid": "5001438031101202",
                "redundantIoModule": "Installed",
                "ioAdapterLocation": {
                        "locationEntries": [
                            {
                                "value": "1",
                                "type": "Slot"
                            }
                        ]
                },
                "serialNumber": "50454e5445305102",
                "description": "",
                "status": "OK",
                "name": None,
                "category": "",
            },
            {
                "type": "drive-enclosure-ioadapter",
                "firmwareVersion": "0.50",
                "partNumber": "755872-001",
                "ports": [
                    {
                        "type": "sas-port",
                        "portName": "2",
                        "portType": "Downlink",
                        "portStatusReason": "None",
                        "portIdentifier": "2",
                        "portLocation": "2",
                        "phyCount": 4,
                        "enabled": True,
                        "description": None,
                        "status": "OK",
                        "name": "2",
                        "category": "sas-ports",
                    },
                    {
                        "type": "sas-port",
                        "portName": "1",
                        "portType": "Downlink",
                        "portStatusReason": "None",
                        "portIdentifier": "1",
                        "portLocation": "1",
                        "phyCount": 4,
                        "enabled": True,
                        "description": None,
                        "status": "OK",
                        "name": "1",
                        "category": "sas-ports",
                    }
                ],
                "model": "Synergy D3940 Storage Module IO Adapter",
                "portCount": 2,
                "manufacturer": "HPE",
                "wwid": "5001438031101203",
                "redundantIoModule": "Installed",
                "ioAdapterLocation": {
                        "locationEntries": [
                            {
                                "value": "2",
                                "type": "Slot"
                            }
                        ]
                },
                "serialNumber": "50454e5445305103",
                "description": "",
                "status": "OK",
                "name": None,
                "category": "",
            }
        ],
        "ioAdapterCount": 2,
        "serialNumber": "SN123101",
        "refreshState": None,
        "description": "",
        "status": "OK",
        "name": "0000A66101, bay 7",
        "category": "drive-enclosures",
    }
]

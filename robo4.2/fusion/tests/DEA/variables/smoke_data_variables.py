from robot.libraries.BuiltIn import BuiltIn
from dea_variables import default_variables


######################################
# Request body variables
######################################

ethernet_networks = [{"vlanId": BuiltIn().get_variable_value("${Ethernet_vlanID}"),
                    "ethernetNetworkType": "Tagged",
                    "purpose": "General",
                    "name": BuiltIn().get_variable_value("${Ethernet_Name}"),
                    "smartLink": True,
                    "privateNetwork": False,
                    "connectionTemplateUri": None,
                    "type": "ethernet-networkV300"}]

fc_networks = [{"name": BuiltIn().get_variable_value("${FC_Name1}"),
                       "connectionTemplateUri": None,
                       "linkStabilityTime": "30",
                       "autoLoginRedistribution": True,
                       "fabricType": "FabricAttach",
                       "managedSanUri": None,
                       "type": "fc-networkV300"}
               ]

fcoe_networks = [{"name": BuiltIn().get_variable_value("${FCOE_Name}"),
                         "vlanId": "200",
                         "connectionTemplateUri": None,
                         "managedSanUri": None,
                         "type": "fcoe-networkV300"}]

uplink_sets = [{"networkUris": [BuiltIn().get_variable_value("${Ethernet_Name}"), BuiltIn().get_variable_value("${FCOE_Name}")],
                                     "mode": "Auto",
                                     "lacpTimer": "Short",
                                     "logicalPortConfigInfos": [{'enclosure': '1', 'bay': int(BuiltIn().get_variable_value("${ICM_Bay}")), 'port': 'Q1', 'speed': 'Auto'}],
                                     "networkType": "Ethernet",
                                     "ethernetNetworkType": "Tagged",
                                     "name": "Up_Link"}]

uplink_sets_fc = [{"networkUris":[BuiltIn().get_variable_value("${FC_Name1}")],
                                    "mode":"Auto",
                                    "lacpTimer":"Short",
                                    "logicalPortConfigInfos":[{'enclosure': '-1', 'bay': int(BuiltIn().get_variable_value("${ICM_Bay_FC1}")), 'port': '1', 'speed': 'Auto'}],
                                    "networkType":"FibreChannel",
                                    "ethernetNetworkType":None,
                                    "name":"Up_LinkFC1"}
                  ]

lig = {"type": "logical-interconnect-groupV300",
                      "fcoeSettings": {"fcoeMode": "FcfNpv"},
                      "ethernetSettings": {"type": "EthernetInterconnectSettingsV201",
                                          "interconnectType": "Ethernet",
                                          "enableFastMacCacheFailover": True,
                                          "macRefreshInterval": 5,
                                          "enableIgmpSnooping": False,
                                          "igmpIdleTimeoutInterval": 260,
                                          "enableNetworkLoopProtection": True,
                                          "enableRichTLV": False,
                                          "enablePauseFloodProtection": True,
                                          "name": "defaultEthernetSwitchSettings",
                                          "id": "9b7f81ae-5e62-4953-9807-34386cf6d1b4",
                                          "uri": "/ethernetSettings"},
                      "name": BuiltIn().get_variable_value("${LIG_Name}"),
                      'interconnectMapTemplate': [{'bay': int(BuiltIn().get_variable_value("${ICM_Bay}")), 'enclosure': 1, 'type': BuiltIn().get_variable_value("${ICM_Model_Potash}"), 'enclosureIndex': 1}],
                      "uplinkSets": uplink_sets,
                      "enclosureType": "SY12000",
                      "enclosureIndexes": [1],
                      "interconnectBaySet": int(BuiltIn().get_variable_value("${ICM_Bay}")),
                      "redundancyType": "NonRedundantASide",
                      "internalNetworkUris": [],
                      "snmpConfiguration": {"type": "snmp-configuration",
                                           "readCommunity": "public",
                                           "systemContact": "",
                                           "enabled": True,
                                           "category": "snmp-configuration",
                                           },
                      }

lig_fc = {"type":"logical-interconnect-groupV300",
                    "ethernetSettings":{"type":"EthernetInterconnectSettingsV201",
                                        "enableIgmpSnooping":False,
                                        "igmpIdleTimeoutInterval":260,
                                        "enableFastMacCacheFailover":True,
                                        "macRefreshInterval":5,
                                        "enableNetworkLoopProtection":True,
                                        "enablePauseFloodProtection":True,
                                        "enableRichTLV":False,
                                        "enableTaggedLldp":False,
                                        "interconnectType":"Ethernet",
                                        "dependentResourceUri":None,
                                        "name":"defaultEthernetSwitchSettings",
                                        "id":"9b7f81ae-5e62-4953-9807-34386cf6d1b4",
                                        "uri":"/ethernetSettings"},
                    "name":BuiltIn().get_variable_value("${LIG_Name_FC}"),
                    "interconnectMapTemplate":[{'bay': int(BuiltIn().get_variable_value("${ICM_Bay_FC1}")), 'enclosure': '-1', 'type': BuiltIn().get_variable_value("${ICM_Model_Carbon}"), 'enclosureIndex': -1}
                                               ],
                    "uplinkSets": uplink_sets_fc,
                    "enclosureType":"SY12000",
                    "enclosureIndexes":[-1],
                    "interconnectBaySet":int(BuiltIn().get_variable_value("${ICM_Bay_FC1}")),
                    "redundancyType": "NonRedundantASide",
                    "internalNetworkUris":[],
                    "snmpConfiguration":{"type":"snmp-configuration",
                                         "readCommunity":"public",
                                         "systemContact":"",
                                         "enabled":True,
                                         "category":"snmp-configuration"}
          }

trapDestinations = None

snmp = {'snmpAccess': None,
        'trapDestinations': trapDestinations}

encl_group = {"type": "EnclosureGroupV400",
                       "name": BuiltIn().get_variable_value("${Encl_Grp_Name}"),
                       "interconnectBayMappings": [{"interconnectBay": int(BuiltIn().get_variable_value("${ICM_Bay}")),"logicalInterconnectGroupUri": "LIG:" + BuiltIn().get_variable_value("${LIG_Name}")}
                                                   ],
                       "interconnectBayMappingCount": 1,
                       "stackingMode": "Enclosure",
                       "configurationScript": "",
                       "uri": None,
                       "powerMode": "RedundantPowerFeed",
                       "ipAddressingMode": "DHCP",
                       "ipRangeUris": [],
                       "enclosureCount": 1,
                       "osDeploymentSettings": {"manageOSDeployment": False,
                                               "deploymentModeSettings": None},
                       "enclosureTypeUri": "/rest/enclosure-types/SY12000"}

encl_group_fc = {"type": "EnclosureGroupV400",
                       "name": BuiltIn().get_variable_value("${Encl_Grp_Name}"),
                       "interconnectBayMappings": [{"interconnectBay": int(BuiltIn().get_variable_value("${ICM_Bay}")), "logicalInterconnectGroupUri" : "LIG:" + BuiltIn().get_variable_value("${LIG_Name}")},
                                                   {"interconnectBay": int(BuiltIn().get_variable_value("${ICM_Bay_FC1}")), "enclosureIndex":1, "logicalInterconnectGroupUri": "LIG:" + BuiltIn().get_variable_value("${LIG_Name_FC}")}
                                                   ],
                       "interconnectBayMappingCount": 2,
                       "stackingMode": "Enclosure",
                       "configurationScript": "",
                       "uri": None,
                       "powerMode": "RedundantPowerFeed",
                       "ipAddressingMode": "DHCP",
                       "ipRangeUris": [],
                       "enclosureCount": 1,
                       "osDeploymentSettings": {"manageOSDeployment": False,
                                               "deploymentModeSettings": None},
                       "enclosureTypeUri": "/rest/enclosure-types/SY12000"}

logical_encl = {"name": BuiltIn().get_variable_value("${Logical_Encl_Name}"),
                         "enclosureUris": ["ENC:" + BuiltIn().get_variable_value("${Enclosures}")],
                         "enclosureGroupUri": "EG:" + BuiltIn().get_variable_value("${Encl_Grp_Name}"),
                         "firmwareBaselineUri": None,
                         "forceInstallFirmware": False}

enet_connection = [{"id": 1,"name": "Connection Bay Ethernet","functionType": "Ethernet", "portId": "Auto",
                   "requestedMbps": "2500","networkUri": "ETH:" + BuiltIn().get_variable_value("${Ethernet_Name}"),
                    "mac": None,"wwpn": "","wwnn": "","requestedVFs": "Auto"}]

fcoe_connection = [{"id": 2,"name": "Connection Bay FCoE","functionType": "FibreChannel", "portId": "Auto",
                    "requestedMbps": "2500","networkUri": "FCOE:" + BuiltIn().get_variable_value("${FCOE_Name}"),
                    "boot": {"priority":"Primary","bootVolumeSource":"UserDefined","targets":[{"arrayWwpn":BuiltIn().get_variable_value("${FCoE_WWPN}"),"lun":"0"}]},
                    "mac": None,"wwpn": "","wwnn": ""}]

fc_connection = [{"id": 2,"name": "Connection Bay FC","functionType": "FibreChannel", "portId": "Auto",
                    "requestedMbps": "Auto","networkUri": "FC:" + BuiltIn().get_variable_value("${FC_Name1}"),
                    "boot": {"priority":"Primary","bootVolumeSource":"UserDefined","targets":[{"arrayWwpn":BuiltIn().get_variable_value("${FC_WWPN}"),"lun":"0"}]},
                    "mac": None,"wwpn": "","wwnn": ""}]

bootmode_uefi = {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"}

boot_order_uefi = {"manageBoot": True,"order": ["HardDisk"]}

bootmode_legacy = {"manageMode": True,"mode":"BIOS"}

boot_order_legacy = {"manageBoot":True,"order":["CD","USB","HardDisk","PXE"]}

bootmode_uefioptimized = {"manageMode": True, "mode": "UEFIOptimized", "pxeBootPolicy": "Auto"} 

server_profiles_enet_fcoe = [{"type": "ServerProfileV6",
                              "serverHardwareUri": "CN7544043Z, bay 1",
                              "serverHardwareTypeUri": "",
                              'enclosureUri': 'ENC:' + BuiltIn().get_variable_value("${Enclosures}"),
                              "enclosureGroupUri": "EG:" + BuiltIn().get_variable_value("${Encl_Grp_Name}"),
                              "serialNumberType": "Physical",
                              "iscsiInitiatorNameType": "AutoGenerated",
                              "macType": "Physical",
                              "wwnType": "Physical",
                              "name": "Bay01",
                              "description": "",
                              "affinity": "Bay",
                              "connections": [enet_connection[0], fcoe_connection[0]],
                              "boot": boot_order_legacy,
                              "bootMode": bootmode_legacy,
                              "firmware": {"manageFirmware": False,"firmwareBaselineUri": "","forceInstallFirmware": False,"firmwareInstallType": None},
                              "bios": {"manageBios": False,"overriddenSettings": []},
                              "hideUnusedFlexNics": True,
                              "localStorage": {},
                              "sanStorage": None}]

server_profiles_enet_fc = [{"type": "ServerProfileV6",
                              "serverHardwareUri": "CN7544043Z, bay 1",
                              "serverHardwareTypeUri": "",
                              'enclosureUri': 'ENC:' + BuiltIn().get_variable_value("${Enclosures}"),
                              "enclosureGroupUri": "EG:" + BuiltIn().get_variable_value("${Encl_Grp_Name}"),
                              "serialNumberType": "Physical",
                              "iscsiInitiatorNameType": "AutoGenerated",
                              "macType": "Physical",
                              "wwnType": "Physical",
                              "name": "Bay01",
                              "description": "",
                              "affinity": "Bay",
                              "connections": [enet_connection[0], fc_connection[0]],
                              "boot": boot_order_uefi,
                              "bootMode": bootmode_uefi,
                              "firmware": {"manageFirmware": False,"firmwareBaselineUri": "","forceInstallFirmware": False,"firmwareInstallType": None},
                              "bios": {"manageBios": False,"overriddenSettings": []},
                              "hideUnusedFlexNics": True,
                              "localStorage": {},
                              "sanStorage": None}]

###########################################
# TEST DATA USES IN BOTH PRE-REQ and SMOKE TESTS
###########################################
storage_system_fcoe_310 = [{
        "type" : "StorageSystemV4",
        "name" : BuiltIn().get_variable_value("${3PAR_Name}"),
        "family" : "StoreServ",
        "hostname" : BuiltIn().get_variable_value("${3PAR_IP}"),
        "credentials" : {
            "username" : BuiltIn().get_variable_value("${3PAR_Uname}"),
            "password" : BuiltIn().get_variable_value("${3PAR_Pwd}")
        },
        "ports" : [{
                "name" : BuiltIn().get_variable_value("${3PAR_portName_FCoE}"),
                "expectedNetworkUri" : "FCOE:" + BuiltIn().get_variable_value("${FCOE_Name}"),
                "mode": "Managed"
            }
        ]
    }
]

storage_system_fc_310 = [{
        "type" : "StorageSystemV4",
        "name" : BuiltIn().get_variable_value("${3PAR_Name}"),
        "family" : "StoreServ",
        "hostname" : BuiltIn().get_variable_value("${3PAR_IP}"),
        "credentials" : {
            "username" : BuiltIn().get_variable_value("${3PAR_Uname}"),
            "password" : BuiltIn().get_variable_value("${3PAR_Pwd}")
        },
        "ports" : [{
                "name" : BuiltIn().get_variable_value("${3PAR_portName_FC}"),
                "expectedNetworkUri" : "FC:" + BuiltIn().get_variable_value("${FC_Name1}"),
                "mode": "Managed"
            }
        ]
    }
]

storage_pools = [{"storageSystemUri": BuiltIn().get_variable_value("${3PAR_Name}"),
                  "name": BuiltIn().get_variable_value("${3PAR_poolName}"),
                  "type": "StoragePoolV3",
                  "isManaged": True}]

enet_connection = [{"id": 1,"name": "Connection Bay Ethernet","functionType": "Ethernet", "portId": "Auto",
                   "requestedMbps": "2500","networkUri": "ETH:" + BuiltIn().get_variable_value("${Ethernet_Name}"),
                    "mac": None,"wwpn": "","wwnn": "","requestedVFs": "Auto"}]

storage_volumes_templates = [{
    "name": BuiltIn().get_variable_value("${3PAR_vol_template_name}"),
    "description": "",
    "rootTemplateUri": "/rest/storage-volume-templates/96c8145e-6850-4a2d-9b2e-a6da017d2177",
    "properties": {
        "name": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Volume name",
            "required": True,
            "maxLength": 100,
            "minLength": 1,
            "description": "A volume name between 1 and 100 characters"
        },
        "size": {
            "meta": {
                "locked": False,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": BuiltIn().get_variable_value("${volumeCapacity}"),
            "maximum": 17592186044416,
            "minimum": 1073741824,
            "required": True,
            "description": "The capacity of the volume in bytes"
        },
        "description": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Description",
            "default": "",
            "maxLength": 2000,
            "minLength": 0,
            "description": "A description for the volume"
        },
        "isShareable": {
            "meta": {
                "locked": False
            },
            "type": "boolean",
            "title": "Is Shareable",
            "default": False,
            "description": "The shareability of the volume"
        },
        "storagePool": {
            "meta": {
                "locked": False,
                "createOnly": True,
                "semanticType": "device-storage-pool"
            },
            "type": "string",
            "title": "Storage Pool",
            "format": "x-uri-reference",
            "required": True,
            "description": "A common provisioning group URI reference",
            "default": BuiltIn().get_variable_value("${3PAR_poolName}")
        },
        "snapshotPool": {
            "meta": {
                "locked": True,
                "semanticType": "device-snapshot-storage-pool"
            },
            "type": "string",
            "title": "Snapshot Pool",
            "format": "x-uri-reference",
            "default": BuiltIn().get_variable_value("${3PAR_poolName}"),
            "description": "A URI reference to the common provisioning group used to create snapshots"
        },
        "provisioningType": {
            "enum": ["Thin",
                "Full"
            ],
            "meta": {
                "locked": True,
                "createOnly": True
            },
            "type": "string",
            "title": "Provisioning Type",
            "default": "Thin",
            "description": "The provisioning type for the volume"
        }
    }
}]

storage_volumes = [{
    "properties": {
        "name": BuiltIn().get_variable_value("${3PAR_Vol_Bay7}"),
        "description": "",
        "storagePool": BuiltIn().get_variable_value("${3PAR_poolName}"),
        "size": BuiltIn().get_variable_value("${volumeCapacity}"),
        "provisioningType": "Thin",
        "isShareable": False
    },
    "templateUri": BuiltIn().get_variable_value("${3PAR_Vol_Template_Name}"),
    "isPermanent": True,
},]

fc_connection = [{"id": 2,"name": "Connection Bay FC","functionType": "FibreChannel", "portId": "Auto",
                    "requestedMbps": "Auto","networkUri": "FC:" + BuiltIn().get_variable_value("${FC_Name1}"),
                    "boot": {"priority":"Primary","bootVolumeSource":"UserDefined","targets":[{"arrayWwpn":BuiltIn().get_variable_value("${FC_WWPN}"),"lun":"0"}]},
                    "mac": None,"wwpn": "","wwnn": ""}]

enet_connection_primary_pxe = [{
    "id": 1,
    "name": BuiltIn().get_variable_value("${Eth_Port_Conn_Name}"),
    "functionType": "Ethernet",
    "portId": "Auto",
    "requestedMbps": "2500",
    "networkUri": "ETH:" + BuiltIn().get_variable_value("${Ethernet_Name}"),
    "boot": {
        "priority": "Primary"
    },
    "mac": None,
    "wwpn": "",
    "wwnn": "",
    "requestedVFs": "Auto"
}]

fcoe_connection = [{
    "id": 2,
    "name": BuiltIn().get_variable_value("${FCoE_Port_Conn_Name}"),
    "functionType": "FibreChannel",
    "portId": "Auto",
    "requestedMbps": "2500",
    "networkUri": "FCOE:" + BuiltIn().get_variable_value("${FCOE_Name}"),
    "boot": {
        "priority": "Primary",
        "bootVolumeSource": "UserDefined",
        "targets": [{
            "arrayWwpn": BuiltIn().get_variable_value("${FCoE_WWPN}"),
            "lun": "0"
        }]
    },
    "mac": None,
    "wwpn": "",
    "wwnn": ""
}]

pxe_enet_fcoe_connection = [enet_connection_primary_pxe[0], fcoe_connection[0]]
pxe_enet_fc_connection = [enet_connection_primary_pxe[0], fc_connection[0]]
enet_fcoe_connection = [enet_connection[0], fcoe_connection[0]]
enet_fc_connection = [enet_connection[0], fc_connection[0]]
bootmode_uefi = {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "IPv4"}
boot_order_uefi = {"manageBoot": True,"order": ["HardDisk"]}
boot_order_uefi_pxe = {"manageBoot": True,"order": ["PXE"]}
bootmode_legacy = {"manageMode": True,"mode":"BIOS"}
boot_order_legacy = {"manageBoot":True,"order":["CD","USB","HardDisk","PXE"]}
boot_order_legacy_pxe = {"manageBoot":True,"order":["PXE","USB","HardDisk","CD"]}

server_profiles_3par = [{
         "type": "ServerProfileV7",
         "serverHardwareUri": BuiltIn().get_variable_value("${Enclosures}") + ", bay "  +  BuiltIn().get_variable_value("${Adapter_Bay}"), 
         "serverHardwareTypeUri": "",
         "enclosureUri": "ENC:" + BuiltIn().get_variable_value("${Enclosures}"),
         "enclosureGroupUri": "EG:Encl_Grp",
         "serialNumberType": "Physical",
         "iscsiInitiatorNameType": "AutoGenerated",
         "macType": "Physical",
         "wwnType": "Physical",
         "name": "Bay_07",
         "description": "",
         "affinity": "Bay",
         "connections": [{
                 "id": 1,
                 "name": BuiltIn().get_variable_value("${Eth_Port_Conn_Name}"),
                 "functionType": "Ethernet",
                 "portId": "Auto",
                 "requestedMbps": "2500",
                 "networkUri": "ETH:" + BuiltIn().get_variable_value("${Ethernet_Name}"),
                 "boot": {
                     "priority": "Primary"
                 },
                 "mac": None,
                 "wwpn": "",
                 "wwnn": "",
                 "requestedVFs": "Auto"
             }, {
                 "id": 2,
                 "name": BuiltIn().get_variable_value("${FCoE_Port_Conn_Name}"),
                 "functionType": "FibreChannel",
                 "portId": "Auto",
                 "requestedMbps": "2500",
                 "networkUri": "FCOE:" + BuiltIn().get_variable_value("${FCOE_Name}"),
                 "boot": {
                     "priority": "Primary",
                     "bootVolumeSource": "UserDefined",
                     "targets": [{
                             "arrayWwpn": BuiltIn().get_variable_value("${FCoE_WWPN}"),
                             "lun": "0"
                         }
                     ]
                 },
                 "mac": None,
                 "wwpn": "",
                 "wwnn": ""
             }
         ],
         "boot": {
             "manageBoot": True,
             "order": ["CD", "USB", "HardDisk", "PXE"]
         },
         "bootMode": {
             "manageMode": True,
             "mode": "BIOS"
         },
         "firmware": {
             "manageFirmware": False,
             "firmwareBaselineUri": "",
             "forceInstallFirmware": False,
             "firmwareInstallType": None
         },
         "bios": {
             "manageBios": False,
             "overriddenSettings": []
         },
         "hideUnusedFlexNics": True,
         "localStorage": {},
         "sanStorage": {
             "hostOSType": "Windows 2012 / WS2012 R2",
             "manageSanStorage": True,
             "volumeAttachments": [{
                     "id": 1,
                     "volumeUri": None,
                     "isBootVolume": False,
                     "lunType": "Auto",
                     "lun": None,
                     "storagePaths": [{
                             "isEnabled": True,
                             "connectionId": 2,
                             "targetSelector": "Auto",
                             "targets": []
                         }
                     ],
                     "volumeName": BuiltIn().get_variable_value("${3PAR_Vol_bay7}"),
                     "volumeDescription": "",
                     "volumeStoragePoolUri": BuiltIn().get_variable_value("${3PAR_poolName}"),
                     "volumeStorageSystemUri": BuiltIn().get_variable_value("${3PAR_StorageURI}"),
                     "volumeProvisionType": "Thin",
                     "volumeProvisionedCapacityBytes": "42949672960",
                     "volumeShareable": False,
                     "permanent": False
                 }
             ]
         }
     }
 ]


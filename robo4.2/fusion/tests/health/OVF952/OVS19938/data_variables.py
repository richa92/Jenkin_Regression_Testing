FUSION_SSH_USERNAME = "root"
FUSION_SSH_PASSWORD = "hpvse1"
ilo_credentials = {"UserName": "Administrator", "Password": "password"}
admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}
LIG_Data = {
    "type": "logical-interconnect-groupV4",
    "uri": None,
    "category": None,
    "eTag": None,
    "created": None,
    "modified": None,
    "ethernetSettings": {
    },
    "description": None,
    "state": None,
    "status": None,
    "name": "lig",
    "telemetryConfiguration": {
    },
    'interconnectMapTemplate': [{'bay': 3, 'enclosure': 1, 'type': "Virtual Connect SE 40Gb F8 Module for Synergy", 'enclosureIndex': 1},
                                {'bay': 6, 'enclosure': 1, 'type': "Virtual Connect SE 40Gb F8 Module for Synergy", 'enclosureIndex': 1}],
    "uplinkSets": [],
    "enclosureType": "SY12000",
    "enclosureIndexes": [1],
    "interconnectBaySet": "3",
    "redundancyType": "Redundant",
    "internalNetworkUris": [],
    "snmpConfiguration": {
    },
    "qosConfiguration": {
    },
    "initialScopeUris": []
}
iLO_REDFISH_SESSION_URI = "/redfish/v1/Sessions/"
iLO_REDFISH_VERSION = "4.0"
eg = {"name": "eg", "interconnectBayMappings": [{"interconnectBay": 3, "logicalInterconnectGroupUri": 'LIG:lig'}, {"interconnectBay": 6, "logicalInterconnectGroupUri": 'LIG:lig'}],
      "ipAddressingMode": "External", "ipRangeUris": [], "enclosureCount": 1,
      "osDeploymentSettings": {"manageOSDeployment": False, "deploymentModeSettings": {"deploymentMode": "None", "deploymentNetworkUri": None}},
      "powerMode": "RedundantPowerFeed", "ambientTemperatureMode": "Standard", "initialScopeUris": []}
le = {"name": "LE", "enclosureUris": ['ENC:MXQ807027M'], "enclosureGroupUri": "EG:eg",
      "firmwareBaselineUri": None, "forceInstallFirmware": False, "initialScopeUris": []}

# ########## C7K data ##################
c7k_enclosures_monitored = [{"username": "Administrator",
                             "password": "HPHPHPHP",
                             "enclosureGroupUri": None,
                             "firmwareBaselineUri": None,
                             "updateFirmwareOn": None,
                             "force": False,
                             "forceInstallFirmware": False,
                             "licensingIntent": "OneViewStandard",
                             "initialScopeUris": [],
                             "hostname": "16.83.10.26",
                             "state": "Monitored"
                             }]
c7k_enc_groups = {"name": "c7k_eg",
                  "interconnectBayMappings": [],
                  "ipRangeUris": [],
                  "enclosureCount": 1,
                  "osDeploymentSettings": None,
                  "configurationScript": "",
                  "powerMode": None,
                  "ambientTemperatureMode": "Standard",
                  "initialScopeUris": []
                  }
c7k_enclosures_managed = [{"username": "Administrator",
                           "password": "HPHPHPHP",
                           "enclosureGroupUri": "EG:c7k_eg",
                           "firmwareBaselineUri": None,
                           "updateFirmwareOn": None,
                           "force": False,
                           "forceInstallFirmware": False,
                           "licensingIntent": "OneViewNoiLO",
                           "initialScopeUris": [],
                           "hostname": "16.83.10.26"}]

# ######### DL data ####################
servers_monitored = [{"name": "ILOCN68130P0M.lr.eml.lab",
                      "hostname": "16.83.14.232",
                      "username": "Administrator",
                      "password": "password",
                      "force": False,
                      "licensingIntent": "OneViewStandard",
                      "configurationState": "Monitored",
                      "initialScopeUris": []
                      },
                     {"name": "ILO7CE712P2MF.lr.eml.lab",
                      "hostname": "16.83.13.48",
                      "username": "Administrator",
                      "password": "password",
                      "force": False,
                      "licensingIntent": "OneViewStandard",
                      "configurationState": "Monitored",
                      "initialScopeUris": []
                      },
                     {"name": "ILOCN764302G9.serverenabled.com",
                      "hostname": "ILOCN764302G9",
                      "username": "Administrator",
                      "password": "password",
                      "force": False,
                      "licensingIntent": "OneViewStandard",
                      "configurationState": "Monitored",
                      "initialScopeUris": []
                      },
                     ]
servers_managed = [{"name": "ILOCN68130P0M.lr.eml.lab",
                    "hostname": "16.83.14.232",
                    "username": "Administrator",
                    "password": "password",
                    "force": False,
                    "licensingIntent": "OneViewStandard",
                    "configurationState": "Managed",
                    "initialScopeUris": []
                    },
                   {"name": "ILO7CE712P2MF.lr.eml.lab",
                    "hostname": "16.83.13.48",
                    "username": "Administrator",
                    "password": "password",
                    "force": False,
                    "licensingIntent": "OneViewStandard",
                    "configurationState": "Managed",
                    "initialScopeUris": []
                    },
                   {"name": "ILOCN764302G9.serverenabled.com",
                    "hostname": "16.83.13.247",
                    "username": "Administrator",
                    "password": "password",
                    "force": False,
                    "licensingIntent": "OneViewStandard",
                    "configurationState": "Managed",
                    "initialScopeUris": []
                    },
                   ]

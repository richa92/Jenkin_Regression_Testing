admin_credentials = {'userName': 'Administrator','password': 'wpsthpvse1'}

oa_credentials = {'username': 'Administrator','password': 'hpvse14'}

ilo_credentials = {'username': 'Administrator','password': 'hpvse1-ilo'}

# LIGs and EGs
LIG_NAME = 'LIG1'
EG_NAME = 'EG1'

# Enclosures
ENC1 = 'wpst11'
ENC1_OA1 = "Wpst11-oa1.vse.rdlabs.hpecorp.net"

# Interconnects
ENC1ICBAY1 = '%s, interconnect 1' % ENC1
ENC1ICBAY2 = '%s, interconnect 2' % ENC1
ENC1ICBAY3 = '%s, interconnect 3' % ENC1
ENC1ICBAY4 = '%s, interconnect 4' % ENC1
ENC1ICBAY5 = '%s, interconnect 5' % ENC1
ENC1ICBAY6 = '%s, interconnect 6' % ENC1
ENC1ICBAY7 = '%s, interconnect 7' % ENC1
ENC1ICBAY8 = '%s, interconnect 8' % ENC1

# Server Hardware
ENC1SHBAY1  = '%s, bay 1' % ENC1
ENC1SHBAY2  = '%s, bay 2' % ENC1
ENC1SHBAY3  = '%s, bay 3' % ENC1
ENC1SHBAY4  = '%s, bay 4' % ENC1
ENC1SHBAY7  = '%s, bay 7' % ENC1
ENC1SHBAY8  = '%s, bay 8' % ENC1
ENC1SHBAY9  = '%s, bay 9' % ENC1


# Profile name
BAY1_PROFILE1_NAME = "wpst11-bay1"
BAY4_PROFILE1_NAME = "wpst11-bay4"

ethernet_networks = [{'name': 'network-tagged',
                      'type': 'ethernet-networkV300',
                      'vlanId': 100,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Ethernet'}]

ligs = [{'name': LIG_NAME,
         'type': 'logical-interconnect-groupV3',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC 8Gb 24-Port FC Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC 8Gb 24-Port FC Module'},
                                     ],
         'uplinkSets': [{'name': 'us-tagged',
                         'ethernetNetworkType': 'Ethernet',
                         'networkType': 'Ethernet',
                         'networkUris': ['network-tagged'],
                         'nativeNetworkUri': None,
                         'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '1', 'port': 'X5', 'speed': 'Auto'}]}],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None},
        ]

enc_groups = [{'name': EG_NAME,
               'type': 'EnclosureGroupV300',
               'enclosureTypeUri': '/rest/enclosure-types/c7000',
               'stackingMode': 'Enclosure',
               'interconnectBayMappingCount': 8,
               'configurationScript': None,
               'interconnectBayMappings':
                   [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:' +LIG_NAME},
                    {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:' +LIG_NAME},
                    {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:' +LIG_NAME},
                    {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:' +LIG_NAME},
                    {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:' +LIG_NAME},
                    {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:' +LIG_NAME},
                    {'interconnectBay': 7, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}]
               },
              ]

encs = [{'hostname': ENC1_OA1, 'username': oa_credentials['username'], 'password': oa_credentials['password'], 'enclosureGroupUri': 'EG:'+ EG_NAME,
         'force': True, 'licensingIntent': 'OneViewNoiLO'},
        ]
# ports
DownLinkPort = '1'
UpLinkPort = 'X5'

flex_IC_on = [{ "name": ENC1ICBAY1,"uri": "IC:" + ENC1ICBAY1, "powerState": "On"}]
flex_IC_off = [{ "name": ENC1ICBAY1, "uri": "IC:" + ENC1ICBAY1, "powerState": "Off"}]

disable_uplink = {
    "associatedUplinkSetUri": "us-tagged",
    "interconnectName": ENC1ICBAY1,
    "portType": "Uplink",
    "portId": "X1",
    "portHealthStatus": "Normal",
    "capability": ["EnetFcoe","Ethernet","FibreChannel"],
    "configPortTypes": ["EnetFcoe","Ethernet"],
    "enabled": False,
    "portName": UpLinkPort,
    "portStatus": "Linked",
    "type": "port"
}

enable_uplink = {
    "associatedUplinkSetUri": "us-tagged",
    "interconnectName": ENC1ICBAY1,
    "portType": "Uplink",
    "portId": "X1",
    "portHealthStatus": "Normal",
    "capability": ["EnetFcoe","Ethernet","FibreChannel"],
    "configPortTypes": ["EnetFcoe","Ethernet"],
    "enabled": True,
    "portName": UpLinkPort,
    "portStatus": "Linked",
    "type": "port"
}

profile_with_DownlinkPort_down = {
      "type": "ServerProfileV7",
      "serverHardwareUri":'SH:'+ ENC1SHBAY1,
      "enclosureGroupUri":"EG:"+ EG_NAME,
      "serialNumberType": "Virtual",
      "iscsiInitiatorNameType": "AutoGenerated",
      "macType": "Virtual",
      "wwnType": "Virtual",
      "name": BAY1_PROFILE1_NAME,
      "description": "",
      "affinity": "Bay",
      "connections": [{"id": 1, "name": "1", "functionType": "Ethernet", "portId": "Auto",
	                   "requestedMbps": "2500", "networkUri": 'ETH:network-tagged', "ipv4": {}}],
      "boot": {"manageBoot": False}, "bootMode": None,
      "firmware": {"manageFirmware": False, "firmwareBaselineUri": "", "forceInstallFirmware": False,
      "firmwareInstallType": None, "firmwareScheduleDateTime": ""},
      "bios": {"manageBios": False,"overriddenSettings": []},
      "hideUnusedFlexNics": True,
      "iscsiInitiatorName": "",
      "osDeploymentSettings": None,
      "localStorage": {"sasLogicalJBODs": [ ],"controllers": []},
      "sanStorage": None
     }

bay4_profile = {
      "type": "ServerProfileV7",
      "serverHardwareUri":'SH:'+ ENC1SHBAY4,
      "enclosureGroupUri":"EG:"+ EG_NAME,
      "serialNumberType": "Virtual",
      "iscsiInitiatorNameType": "AutoGenerated",
      "macType": "Virtual",
      "wwnType": "Virtual",
      "name": BAY4_PROFILE1_NAME,
      "description": "",
      "affinity": "Bay",
      "connections": [{"id": 1, "name": "1", "functionType": "Ethernet", "portId": "Auto",
	                    "requestedMbps": "2500", "networkUri": 'ETH:network-tagged', "ipv4": {}}],
      "boot": {"manageBoot": False}, "bootMode": None,
      "firmware": {"manageFirmware": False, "firmwareBaselineUri": "", "forceInstallFirmware": False,
      "firmwareInstallType": None, "firmwareScheduleDateTime": ""},
      "bios": {"manageBios": False,"overriddenSettings": []},
      "hideUnusedFlexNics": True,
      "iscsiInitiatorName": "",
      "osDeploymentSettings": None,
      "localStorage": {"sasLogicalJBODs": [ ],"controllers": []},
      "sanStorage": None
     }


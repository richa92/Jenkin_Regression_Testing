import os
import sys

cwd = os.getcwd()
download_to_path = cwd

def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist

SSH_PASS = 'hpvse1'

APPLIANCE_IP = '15.199.229.232'

appliance_cred = ['root', 'hpvse1']

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

serveradmin = {'userName': 'Serveradmin', 'password': 'Serveradmin'}

network_admin = {'userName': 'Networkadmin', 'password': 'Networkadmin'}

backup_admin = {'userName': 'Backupadmin', 'password': 'Backupadmin'}

readonly_user = {'userName': 'readonly', 'password': 'readonly'}

vcenter = {'server': '15.199.230.130', 'user': 'GopalK', 'password': 'hpvse1'}

users = [{'userName': 'Serveradmin', 'password': 'Serveradmin', 'fullName': 'Serveradmin', 'roles': ['Server administrator','Backup administrator'], 'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'}]


loggerlevel = r'INFO'   # use INFO|DEBUG

fcnets = [{"type": "fc-networkV300",
           "name": "FC_1",
           "fabricType": "FabricAttach",
           "linkStabilityTime": 30,
           "autoLoginRedistribution": True
           }]

ethernet_network = [{"vlanId" : "401",
                    "purpose" : "Management",
                    "name" : "fvt4network1",
                    "smartLink" : False,
                    "privateNetwork" : False,
                    "connectionTemplateUri" : None,
                    "ethernetNetworkType" : "Tagged",
                    "type" : "ethernet-networkV300"},
                    {"vlanId" : "402",
                    "purpose" : "Management",
                    "name" : "fvt4network2",
                    "smartLink" : False,
                    "privateNetwork" : False,
                    "connectionTemplateUri" : None,
                    "ethernetNetworkType" : "Tagged",
                    "type" : "ethernet-networkV300"},
                    {"vlanId" : "403",
                    "purpose" : "Management",
                    "name" : "fvt4network3",
                    "smartLink" : False,
                    "privateNetwork" : False,
                    "connectionTemplateUri" : None,
                    "ethernetNetworkType" : "Tagged",
                    "type" : "ethernet-networkV300"},
                    {"vlanId" : "404",
                    "purpose" : "Management",
                    "name" : "fvt4network4",
                    "smartLink" : False,
                    "privateNetwork" : False,
                    "connectionTemplateUri" : None,
                    "ethernetNetworkType" : "Tagged",
                    "type" : "ethernet-networkV300"},
                    {"vlanId" : "405",
                    "purpose" : "Management",
                    "name" : "fvt4network5",
                    "smartLink" : False,
                    "privateNetwork" : False,
                    "connectionTemplateUri" : None,
                    "ethernetNetworkType" : "Tagged",
                    "type" : "ethernet-networkV300"},
                    {"vlanId" : "406",
                    "purpose" : "Management",
                    "name" : "fvt4network6",
                    "smartLink" : False,
                    "privateNetwork" : False,
                    "connectionTemplateUri" : None,
                    "ethernetNetworkType" : "Tagged",
                    "type" : "ethernet-networkV300"},
                    {"vlanId" : "407",
                    "purpose" : "Management",
                    "name" : "fvt4network7",
                    "smartLink" : False,
                    "privateNetwork" : False,
                    "connectionTemplateUri" : None,
                    "ethernetNetworkType" : "Tagged",
                    "type" : "ethernet-networkV300"}]


POTASH = "Virtual Connect SE 40Gb F8 Module for Synergy"
CHLORIDE10 = "Synergy 10Gb Interconnect Link Module"

LIG1 = 'lig_tbird'
LIGB = 'lig_tbird_B'
redundancyType= 'HighlyAvailable'

EG = '2enc-DUS-EG'

               
enc_groups = [{'name': EG,
               'type': 'EnclosureGroupV300',
               'enclosureCount': 2,
               'enclosureTypeUri': '/rest/enclosure-types/SY12000',
               'stackingMode': 'Enclosure',
               'interconnectBayMappingCount': 6,
               'configurationScript': None,
               'interconnectBayMappings':
               [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:' + LIG1},
                {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:' + LIG1},
                {'interconnectBay': 5, 'logicalInterconnectGroupUri': None}],
               'ipAddressingMode': "External",
               'ipRangeUris': [],
               'powerMode': "RedundantPowerFeed"
               }]

enc_groups_aside = [{'name': EG,
               'type': 'EnclosureGroupV300',
               'enclosureCount': 2,
               'enclosureTypeUri': '/rest/enclosure-types/SY12000',
               'stackingMode': 'Enclosure',
               'interconnectBayMappingCount': 6,
               'configurationScript': None,
               'interconnectBayMappings':
               [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:' + LIG1},
                {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 6, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 5, 'logicalInterconnectGroupUri': None}],
               'ipAddressingMode': "External",
               'ipRangeUris': [],
               'powerMode': "RedundantPowerFeed"
               }]
               
enc_groups_bside = [{'name': EG,
               'type': 'EnclosureGroupV300',
               'enclosureCount': 2,
               'enclosureTypeUri': '/rest/enclosure-types/SY12000',
               'stackingMode': 'Enclosure',
               'interconnectBayMappingCount': 6,
               'configurationScript': None,
               'interconnectBayMappings':
               [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:' + LIG1},
                {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:' + LIGB},
                {'interconnectBay': 5, 'logicalInterconnectGroupUri': None}],
               'ipAddressingMode': "External",
               'ipRangeUris': [],
               'powerMode': "RedundantPowerFeed"
               }]

ENC1 = 'CN754406W4'
ENC2 = 'CN7545084F'
BAY = 3
LE = '2enc-cl10-le'
#LI creation for both A side and HA
LI = LE+'-'+LIG1
# Bside Configuration script
LIB = LE+'-'+LIGB

les = [{'name': LE,
        'enclosureUris': ['ENC:' + ENC1, 'ENC:' + ENC2],
        'enclosureGroupUri': 'EG:'+EG,
        'firmwareBaselineUri': None,
        'forceInstallFirmware': False
        }]                                           
                           
us = {'us-eth': {'name': 'us-eth',
                            'ethernetNetworkType': 'Tagged',
                            'networkType': 'Ethernet',
                            'networkUris': ['fvt4network8'],
                            'fcNetworkUris': [],
                            'fcoeNetworkUris': [],
                            'lacpTimer': 'Short',
                            'logicalInterconnectUri': None,
                            'primaryPortLocation': None,
                            'manualLoginRedistributionState': 'NotSupported',
                            'connectionMode': 'Auto',
                            'nativeNetworkUri': None,
                          'portConfigInfos': [{'enclosure': ENC1, 'bay': '3', 'port': 'Q2.3', 'desiredSpeed': 'Auto'}]}}
                                              
                                              


#'Virtual Connect SE 40Gb F8 Module for Synergy - 794502-B23':
port_map = {'Q1': '61', 'Q1.1': '62', 'Q1.2': '63', 'Q1.3': '64', 'Q1.4': '65',
  'Q2': '66', 'Q2.1': '67', 'Q2.2': '68', 'Q2.3': '69', 'Q2.4': '70',
  'Q3': '71', 'Q3.1': '72', 'Q3.2': '73', 'Q3.3': '74', 'Q3.4': '75',
  'Q4': '76', 'Q4.1': '77', 'Q4.2': '78', 'Q4.3': '79', 'Q4.4': '80',
  'Q5': '81', 'Q5.1': '82', 'Q5.2': '83', 'Q5.3': '84', 'Q5.4': '85',
  'Q6': '86', 'Q6.1': '87', 'Q6.2': '88', 'Q6.3': '89', 'Q6.4': '90',
  'Q7': '91', 'Q7.1': '92', 'Q7.2': '93', 'Q7.3': '94', 'Q7.4': '95',
  'Q8': '96', 'Q8.1': '97', 'Q8.2': '98', 'Q8.3': '99', 'Q8.4': '100',
  'Q1:1': '62', 'Q1:2': '63', 'Q1:3': '64', 'Q1:4': '65',
  'Q2:1': '67', 'Q2:2': '68', 'Q2:3': '69', 'Q2:4': '70',
  'Q3:1': '72', 'Q3:2': '73', 'Q3:3': '74', 'Q3:4': '75',
  'Q4:1': '77', 'Q4:2': '78', 'Q4:3': '79', 'Q4:4': '80',
  'Q5:1': '82', 'Q5:2': '83', 'Q5:3': '84', 'Q5:4': '85',
  'Q6:1': '87', 'Q6:2': '88', 'Q6:3': '89', 'Q6:4': '90',
  'Q7:1': '92', 'Q7:2': '93', 'Q7:3': '94', 'Q7:4': '95',
  'Q8:1': '97', 'Q8:2': '98', 'Q8:3': '99', 'Q8:4': '100'
  }

lig_tbird_2enc = {"type": "logical-interconnect-groupV300",
                  "ethernetSettings": {"type": "EthernetInterconnectSettingsV201", "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
                  "description": None,
                  "name": "lig_tbird",
                  "interconnectMapTemplate":
                  {"interconnectMapEntryTemplates": [
                      {"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 3}, {"type": "Enclosure", "relativeValue": 1}]}, "permittedInterconnectTypeUri": "Virtual Connect SE 40Gb F8 Module for Synergy - 794502-B23", "enclosureIndex": 1},
                      {"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 6}, {"type": "Enclosure", "relativeValue": 2}]}, "permittedInterconnectTypeUri": "Virtual Connect SE 40Gb F8 Module for Synergy - 794502-B23", "enclosureIndex": 2},
                      {"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 6}, {"type": "Enclosure", "relativeValue": 1}]}, "permittedInterconnectTypeUri": "Synergy 10Gb Interconnect Link Module", "enclosureIndex": 1},
                      {"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 3}, {"type": "Enclosure", "relativeValue": 2}]}, "permittedInterconnectTypeUri": "Synergy 10Gb Interconnect Link Module", "enclosureIndex": 2}]},
                  "enclosureType": "SY12000",
                  "enclosureIndexes": [1, 2],
                  "interconnectBaySet": "3",
                  "redundancyType": "HighlyAvailable",
                  "internalNetworkUris": [],
                  "snmpConfiguration": {"type": "snmp-configuration", "readCommunity": "public", "systemContact": "", "trapDestinations": None, "snmpAccess": None, "enabled": True, "description": None, "name": None, "state": None, "category": "snmp-configuration"},
                  "qosConfiguration": None,
                  #"uplinkSets": [{"networkUris":["/rest/ethernet-networks/48ee7ab1-2733-4fee-8110-9acbdf4e351d"],"lacpTimer":"Long","name":"bay3-enet4x-us","networkType":"Ethernet","ethernetNetworkType":"Tagged","primaryPort":None,"logicalPortConfigInfos":[{"desiredSpeed":"Auto","logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":3},{"type":"Port","relativeValue":67},{"type":"Enclosure","relativeValue":1}]}}],"mode":"Auto"}]
				  "uplinkSets": [
						{"networkUris":["fvt4network1","fvt4network2"],
						"lacpTimer":"Long",
						"name":"bay3-enet4x-us",
						"networkType":"Ethernet",
						"ethernetNetworkType":"Tagged",
						"primaryPort":None,
						"logicalPortConfigInfos":[
						{"desiredSpeed":"Auto","logicalLocation":
							{"locationEntries":[{"type":"Bay","relativeValue":3},
												{"type":"Port","relativeValue":67},
												{"type":"Enclosure","relativeValue":1}]
							}},
							{"desiredSpeed":"Auto","logicalLocation":
							{"locationEntries":[{"type":"Bay","relativeValue":3},
												{"type":"Port","relativeValue":68},
												{"type":"Enclosure","relativeValue":1}]
							}}
							],"mode":"Auto"},
							
						{"networkUris":["FC_1"],
						"mode":"Auto",
						"lacpTimer":"Short",
						"primaryPort":None,
						"logicalPortConfigInfos":[{"desiredSpeed":"Auto","logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":3},{"type":"Port","relativeValue":62},{"type":"Enclosure","relativeValue":1}]}}],
						"networkType":"FibreChannel",
						"ethernetNetworkType":None,
						"name":"US_FC"},

							
						{"networkUris":["fvt4network3"],
						"lacpTimer":"Long",
						"name":"bay3-enetQ-us",
						"networkType":"Ethernet",
						"ethernetNetworkType":"Tagged",
						"primaryPort":None,
						"logicalPortConfigInfos":[
						{"desiredSpeed":"Auto","logicalLocation":
							{"locationEntries":[{"type":"Bay","relativeValue":3},
												{"type":"Port","relativeValue":71},
												{"type":"Enclosure","relativeValue":1}]
							}},
							],"mode":"Auto"},
						
						{"networkUris":["fvt4network4","fvt4network6","fvt4network7"],
						"lacpTimer":"Long",
						"name":"bay6-enet4x-us",
						"networkType":"Ethernet",
						"ethernetNetworkType":"Tagged",
						"primaryPort":None,
						"logicalPortConfigInfos":[
						{"desiredSpeed":"Auto","logicalLocation":
							{"locationEntries":[{"type":"Bay","relativeValue":6},
												{"type":"Port","relativeValue":67},
												{"type":"Enclosure","relativeValue":2}]
							}},
							{"desiredSpeed":"Auto","logicalLocation":
							{"locationEntries":[{"type":"Bay","relativeValue":6},
												{"type":"Port","relativeValue":68},
												{"type":"Enclosure","relativeValue":2}]
							}},
							{"desiredSpeed":"Auto","logicalLocation":
							{"locationEntries":[{"type":"Bay","relativeValue":6},
												{"type":"Port","relativeValue":69},
												{"type":"Enclosure","relativeValue":2}]
							}},
							{"desiredSpeed":"Auto","logicalLocation":
							{"locationEntries":[{"type":"Bay","relativeValue":6},
												{"type":"Port","relativeValue":70},
												{"type":"Enclosure","relativeValue":2}]
							}}
							
							],"mode":"Auto"},
						{"networkUris":["fvt4network5"],
						"lacpTimer":"Long",
						"name":"bay6-enetQ-us",
						"networkType":"Ethernet",
						"ethernetNetworkType":"Tagged",
						"primaryPort":None,
						"logicalPortConfigInfos":[
						{"desiredSpeed":"Auto","logicalLocation":
							{"locationEntries":[{"type":"Bay","relativeValue":6},
												{"type":"Port","relativeValue":76},
												{"type":"Enclosure","relativeValue":2}]
							}},
							],"mode":"Auto"},
							]
					}
                    
Lig_tbird_Aside = {"type": "logical-interconnect-groupV300",
        "ethernetSettings": {"type": "EthernetInterconnectSettingsV201", "enableIgmpSnooping":False,"igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5,"enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},"description": None,"name": LIG1,"interconnectMapTemplate":{"interconnectMapEntryTemplates":[{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":3},{"type":"Enclosure","relativeValue":1}]},"logicalDownlinkUri":None,"permittedInterconnectTypeUri":"Virtual Connect SE 40Gb F8 Module for Synergy - 794502-B23","enclosureIndex":1},      {"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":3},{"type":"Enclosure","relativeValue":2}]},"logicalDownlinkUri":None,"permittedInterconnectTypeUri":"Synergy 10Gb Interconnect Link Module","enclosureIndex":2}]},
        "enclosureType": "SY12000","enclosureIndexes": [1, 2],"interconnectBaySet": "3","redundancyType": "NonRedundantASide",      "internalNetworkUris": [],"snmpConfiguration": {"type": "snmp-configuration", "readCommunity": "public", "systemContact": "", "trapDestinations": None, "snmpAccess": None, "enabled": True, "description": None, "name": None, "state": None, "category": "snmp-configuration"},"qosConfiguration": None,"uplinkSets": [
            {"networkUris":["fvt4network1","fvt4network2"],"lacpTimer":"Long","name":"bay3-enet4x-us-Aside","networkType":"Ethernet",
            "ethernetNetworkType":"Tagged", "primaryPort":None,
            "logicalPortConfigInfos":[
            {"desiredSpeed":"Auto","logicalLocation":
                {"locationEntries":[{"type":"Bay","relativeValue":3},
                                    {"type":"Port","relativeValue":67},
                                    {"type":"Enclosure","relativeValue":1}]
                }},
                {"desiredSpeed":"Auto","logicalLocation":
                {"locationEntries":[{"type":"Bay","relativeValue":3},
                                    {"type":"Port","relativeValue":68},
                                    {"type":"Enclosure","relativeValue":1}]
                }}
                
                ],"mode":"Auto"},	
            {"networkUris":["FC_1"], "mode":"Auto","lacpTimer":"Short","primaryPort":None,"logicalPortConfigInfos":[{"desiredSpeed":"Auto","logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":3},{"type":"Port","relativeValue":62},{"type":"Enclosure","relativeValue":1}]}}],
            "networkType":"FibreChannel","ethernetNetworkType":None,"name":"US_FC"},{"networkUris":["fvt4network3"],
            "lacpTimer":"Long","name":"bay3-enetQ-us","networkType":"Ethernet","ethernetNetworkType":"Tagged","primaryPort":None,
            "logicalPortConfigInfos":[
            {"desiredSpeed":"Auto","logicalLocation":
                {"locationEntries":[{"type":"Bay","relativeValue":3},
                                    {"type":"Port","relativeValue":71},
                                    {"type":"Enclosure","relativeValue":1}]
                }},
                ],"mode":"Auto"},]
        }


Lig_tbird_Bside = {"type": "logical-interconnect-groupV300",
        "ethernetSettings": {"type": "EthernetInterconnectSettingsV201", "enableIgmpSnooping":False,"igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5,"enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},"description": None,"name": LIGB,"interconnectMapTemplate":{"interconnectMapEntryTemplates":[
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":6},{"type":"Enclosure","relativeValue":1}]},"logicalDownlinkUri":None,"permittedInterconnectTypeUri":"Synergy 10Gb Interconnect Link Module","enclosureIndex":1},{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":6},{"type":"Enclosure","relativeValue":2}]},"logicalDownlinkUri":None,"permittedInterconnectTypeUri":"Virtual Connect SE 40Gb F8 Module for Synergy - 794502-B23","enclosureIndex":2}]},
        "enclosureType": "SY12000","enclosureIndexes": [1, 2],"interconnectBaySet": "3","redundancyType": "NonRedundantBSide",      "internalNetworkUris": [],"snmpConfiguration": {"type": "snmp-configuration", "readCommunity": "public", "systemContact": "", "trapDestinations": None, "snmpAccess": None, "enabled": True, "description": None, "name": None, "state": None, "category": "snmp-configuration"},"qosConfiguration": None,"uplinkSets": [
            {"networkUris":["fvt4network1","fvt4network2"],"lacpTimer":"Long","name":"bay3-enet4x-us-Bside","networkType":"Ethernet",
            "ethernetNetworkType":"Tagged", "primaryPort":None,
            "logicalPortConfigInfos":[
            {"desiredSpeed":"Auto","logicalLocation":
                {"locationEntries":[{"type":"Bay","relativeValue":6},
                                    {"type":"Port","relativeValue":67},
                                    {"type":"Enclosure","relativeValue":2}]
                }},
                {"desiredSpeed":"Auto","logicalLocation":
                {"locationEntries":[{"type":"Bay","relativeValue":6},
                                    {"type":"Port","relativeValue":68},
                                    {"type":"Enclosure","relativeValue":2}]
                }}
                
                ],"mode":"Auto"},	
            {"networkUris":["FC_1"], "mode":"Auto","lacpTimer":"Short","primaryPort":None,"logicalPortConfigInfos":[{"desiredSpeed":"Auto","logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":6},{"type":"Port","relativeValue":62},{"type":"Enclosure","relativeValue":2}]}}],
            "networkType":"FibreChannel","ethernetNetworkType":None,"name":"US_FC"},{"networkUris":["fvt4network3"],
            "lacpTimer":"Long","name":"bay3-enetQ-us","networkType":"Ethernet","ethernetNetworkType":"Tagged","primaryPort":None,
            "logicalPortConfigInfos":[
            {"desiredSpeed":"Auto","logicalLocation":
                {"locationEntries":[{"type":"Bay","relativeValue":6},
                                    {"type":"Port","relativeValue":71},
                                    {"type":"Enclosure","relativeValue":2}]
                }},
                ],"mode":"Auto"},]
        }

'''
#HA second Profile details
{'type': 'ServerProfileV6', 'serverHardwareUri': ENC2 + ', bay 2',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC2, 'enclosureGroupUri': 'EG:'+EG, 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'Enc2'+ENC2 + '-bay-2', 'description': '', 'affinity': 'Bay',
                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'connections': [{'id': 1, 'name': 'conAA', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:fvt4network1', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 2, 'name': 'conAB', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:fvt4network5', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    #{'id': 3, 'name': 'connBA', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', #'networkUri': 'ETH:fvt4network3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 4, 'name': 'connBB', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '2500', 'networkUri': 'ETH:fvt4network4', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                    ]}
'''

server_profiles = [{'type': 'ServerProfileV6', 'serverHardwareUri': ENC1 + ', bay 2',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:'+EG, 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'Enc1'+ENC1 + '-bay-2', 'description': '', 'affinity': 'Bay',
                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'connections': [{'id': 1, 'name': 'conAA', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:fvt4network1', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 2, 'name': 'conAB', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:fvt4network5', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 3, 'name': 'connBA', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:fvt4network3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 4, 'name': 'connBB', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '2500', 'networkUri': 'ETH:fvt4network4', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                    ]},
					{'type': 'ServerProfileV6', 'serverHardwareUri': ENC2 + ', bay 2',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC2, 'enclosureGroupUri': 'EG:'+EG, 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'Enc2'+ENC2 + '-bay-2', 'description': '', 'affinity': 'Bay',
                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'connections': [{'id': 1, 'name': 'conAA', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:fvt4network1', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 2, 'name': 'conAB', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:fvt4network5', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 3, 'name': 'connBA', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:fvt4network3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 4, 'name': 'connBB', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '2500', 'networkUri': 'ETH:fvt4network4', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                    ]}
                   ]

'''
ASide 2nd Profile 
                    {'type': 'ServerProfileV6', 'serverHardwareUri': ENC2 + ', bay 2',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC2, 'enclosureGroupUri': 'EG:'+EG, 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'Enc2'+ENC2 + '-bay-2', 'description': '', 'affinity': 'Bay',
                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'connections': [{'id': 1, 'name': 'conAA', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:fvt4network1', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 2, 'name': 'conAB', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:fvt4network2', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    #{'id': 3, 'name': 'connBA', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', #'networkUri': 'ETH:fvt4network3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    #{'id': 4, 'name': 'connBB', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '2500', 'networkUri': 'ETH:fvt4network3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                    ]},

'''
                   
server_profiles_Aside = [{'type': 'ServerProfileV6', 'serverHardwareUri': ENC1 + ', bay 2',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:'+EG, 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'Enc1'+ENC1 + '-bay-2', 'description': '', 'affinity': 'Bay',
                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'connections': [{'id': 1, 'name': 'conAA', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:fvt4network1', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 2, 'name': 'conAB', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:fvt4network2', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    #{'id': 3, 'name': 'connBA', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', #'networkUri': 'ETH:fvt4network3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    #{'id': 4, 'name': 'connBB', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '2500', 'networkUri': 'ETH:fvt4network3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                    ]},
                    
                   ]
server_profiles_Bside = [{'type': 'ServerProfileV6', 'serverHardwareUri': ENC2 + ', bay 2',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC2, 'enclosureGroupUri': 'EG:'+EG, 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'Enc2'+ENC2 + '-bay-2', 'description': '', 'affinity': 'Bay',
                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'connections': [{'id': 1, 'name': 'conAA', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:fvt4network1', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 2, 'name': 'conAB', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:fvt4network2', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    #{'id': 3, 'name': 'connBA', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', #'networkUri': 'ETH:fvt4network3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    #{'id': 4, 'name': 'connBB', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '2500', 'networkUri': 'ETH:fvt4network3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                    ]},
                    
                   ]
interconnects = [ENC1+', interconnect 3', ENC2+', interconnect 6']
analyzer_port = "Q2:3"
analyzer_dport = "d2"
used_uplink_port = "Q2:2"
fc_uplink_port = "Q1:1"
stacking_port = "Q7"
analyzer_port_2 = "Q6"
analyzer_port_3 = "Q2:4"
# Timer for configuring the Port monitoring
pm_timer = 400
# Timer for Configuring the Port Monitoring When switched from Port Q3.3 to Q5
pm_timer_q5 = 800
# Logical enclosure Create timer
le_timer = 0
bay_no=3
li_portmonitor = {"type": "port-monitor",
                  "enablePortMonitor": 'true',
                  "analyzerPort": {"portMonitorConfigInfo": "AnalyzerPort",
                                   "portUri": "UplinkportUri"},
                  "monitoredPorts": [{"portMonitorConfigInfo": "MonitoredBoth",
                                      "portUri": "DownlinkportUri"}]
                  }
import paramiko
import re
import sys
import os


def make_range_list(vrange):
    rlist = []
    for x in xrange(vrange['start'], (vrange['end'] + 1)):
        rlist.append(vrange['prefix'] + str(x) + vrange['suffix'])
    return rlist


def convert_unicode_to_string(String):
    res = String.encode("utf-8")
    return res

APPLIANCE_IP = '15.245.133.139'
ENCLOSURE_IP = '15.245.129.11'
Enclosure_Name = 'WPST-PAAU56-EN2'
LE = 'WPST-PAAU56-EN2'
admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
Server_power_on_sleep_time = '900'

FC_Switch_IP = '15.245.128.50'
FC_Switch_USERNAME = 'root'
FC_Switch_PASSWORD = 'wpsthpvse1'

Switch_ports = ['1', '2', '3', '4', '6', '7']
exp_output_speed = ['N4Gbps', 'N2Gbps', 'N8Gbps', 'N8Gbps', 'N2Gbps', 'N4Gbps']

linux_details = {"hostip": "15.199.235.170", "username": "root", "password": "hpvse123", "dir_location": "/root/", "python_cmd": "python2.7"}
oa_details = {"oa_ip": ENCLOSURE_IP, "username": "Administrator", "password": "wpsthpvse1"}
win_server_details = {"username": "Administrator", "password": "Wpsthpvse1"}
linux_server_details = {"username": "root", "password": "wpsthpvse1"}
bfs_server_details = {"username": "root", "password": "hpvse123"}

Fc_body = {"name": "", "connectionTemplateUri": None, "linkStabilityTime": "30", "autoLoginRedistribution": True, "fabricType": "", "type": "fc-networkV4"}

Fc_body1 = {"name": "", "connectionTemplateUri": None, "linkStabilityTime": "60", "autoLoginRedistribution": True, "fabricType": "", "type": "fc-networkV4"}

Enet_body = {"purpose": "General", "name": "Enet_untagged", "smartLink": False, "privateNetwork": False, "connectionTemplateUri": None, "ethernetNetworkType": "Untagged", "type": "ethernet-networkV4"}

Preview_uri = '/rest/enclosure-preview'

Preview_body = {"hostname": ENCLOSURE_IP, "username": oa_details['username'], "password": oa_details['password'], "ligPrefix": "LIG_A", "force": True, "logicalInterconnectGroupNeeded": True}

Server_bays = ['1', '2', '3', '4']
Supershaw_DA = {'bay_num': '1', 'Act_ports': ['X1', 'X2', 'X3'], 'rel_ports': ['33', '34', '35']}
Supershaw_FA = {'bay_num': '2', 'Act_ports': ['X1', 'X2', 'X3'], 'rel_ports': ['33', '34', '35']}
Sheppard_DA = {'bay_num': '3', 'Act_ports': ['X1', 'X2', 'X3'], 'rel_ports': ['17', '18', '19']}
Sheppard_FA = {'bay_num': '4', 'Act_ports': ['X1', 'X2', 'X3'], 'rel_ports': ['17', '18', '19']}
Enet_connection = {'bay_num': '1', 'Act_ports': 'Q2.1', 'rel_ports': '17'}

Server_bay_num = '4'
interconnect5 = '5'
fc_connection = {'sp1': [1, 4], 'sp2': [2, 5], 'sp3': [3, 6]}

lig_body1 = {"name": "LIG_A",
             "type": "logical-interconnect-groupV4",
             "enclosureType": "C7000",
             "interconnectMapTemplate": {},
             "internalNetworkUris": [],
             "uplinkSets": "",
             "stackingMode": "Enclosure",
             "ethernetSettings": None,
             "state": "Active",
             "telemetryConfiguration": None,
             "snmpConfiguration": None,
             "qosConfiguration": None}

lig_us_body1 = [{"networkType": "Ethernet",
                 "ethernetNetworkType": "Untagged",
                 "networkUris": [],
                 "nativeNetworkUri":None,
                 "lacpTimer":"Short",
                 "primaryPort":None,
                 "logicalPortConfigInfos":[{"logicalLocation": {"locationEntries": [{"relativeValue": Enet_connection['bay_num'], "type":"Bay"}, {"relativeValue": Enet_connection['rel_ports'], "type":"Port"}, {"relativeValue": 1, "type": "Enclosure"}]}, "desiredSpeed": "Auto"}],
                 "reachability": None,
                 "mode": "Auto",
                 "name": "US_enet"},
                {"networkUris": [],
                 "mode":"Auto",
                 "lacpTimer":"Short",
                 "primaryPort":None,
                 "logicalPortConfigInfos":[{"desiredSpeed": "Speed2G", "logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": Supershaw_DA['bay_num']}, {"type": "Port", "relativeValue": Supershaw_DA['rel_ports'][0]}, {"type": "Enclosure", "relativeValue": 1}]}}],
                 "networkType": "FibreChannel",
                 "ethernetNetworkType": None,
                 "nativeNetworkUri": None,
                 "name": "US_da1"},

                {"networkUris": [],
                 "mode":"Auto",
                 "lacpTimer":"Short",
                 "primaryPort":None,
                 "logicalPortConfigInfos":[{"desiredSpeed": "Speed4G", "logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": Supershaw_DA['bay_num']}, {"type": "Port", "relativeValue": Supershaw_DA['rel_ports'][1]}, {"type": "Enclosure", "relativeValue": 1}]}}],
                 "networkType": "FibreChannel",
                 "ethernetNetworkType": None,
                 "nativeNetworkUri": None,
                 "name": "US_da2"},

                {"networkUris": [],
                 "mode":"Auto",
                 "lacpTimer":"Short",
                 "primaryPort":None,
                 "logicalPortConfigInfos":[{"desiredSpeed": "Speed8G", "logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": Supershaw_DA['bay_num']}, {"type": "Port", "relativeValue": Supershaw_DA['rel_ports'][2]}, {"type": "Enclosure", "relativeValue": 1}]}}],
                 "networkType": "FibreChannel",
                 "ethernetNetworkType": None,
                 "nativeNetworkUri": None,
                 "name": "US_da3"},

                {"networkUris": [],
                 "mode":"Auto",
                 "lacpTimer":"Short",
                 "primaryPort":None,
                 "logicalPortConfigInfos":[{"desiredSpeed": "Speed2G", "logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": Sheppard_DA['bay_num']}, {"type": "Port", "relativeValue": Sheppard_DA['rel_ports'][0]}, {"type": "Enclosure", "relativeValue": 1}]}}],
                 "networkType": "FibreChannel",
                 "ethernetNetworkType": None,
                 "nativeNetworkUri": None,
                 "name": "US_da4"},

                {"networkUris": [],
                 "mode":"Auto",
                 "lacpTimer":"Short",
                 "primaryPort":None,
                 "logicalPortConfigInfos":[{"desiredSpeed": "Speed4G", "logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": Sheppard_DA['bay_num']}, {"type": "Port", "relativeValue": Sheppard_DA['rel_ports'][1]}, {"type": "Enclosure", "relativeValue": 1}]}}],
                 "networkType": "FibreChannel",
                 "ethernetNetworkType": None,
                 "nativeNetworkUri": None,
                 "name": "US_da5"},

                {"networkUris": [],
                 "mode":"Auto",
                 "lacpTimer":"Short",
                 "primaryPort":None,
                 "logicalPortConfigInfos":[{"desiredSpeed": "Speed8G", "logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": Sheppard_DA['bay_num']}, {"type": "Port", "relativeValue": Sheppard_DA['rel_ports'][2]}, {"type": "Enclosure", "relativeValue": 1}]}}],
                 "networkType": "FibreChannel",
                 "ethernetNetworkType": None,
                 "nativeNetworkUri": None,
                 "name": "US_da6"},


                {"networkUris": [],
                 "mode":"Auto",
                 "lacpTimer":"Short",
                 "primaryPort":None,
                 "logicalPortConfigInfos":[{"desiredSpeed": "Speed2G", "logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": Supershaw_FA['bay_num']}, {"type": "Port", "relativeValue": Supershaw_FA['rel_ports'][0]}, {"type": "Enclosure", "relativeValue": 1}]}}],
                 "networkType": "FibreChannel",
                 "ethernetNetworkType": None,
                 "nativeNetworkUri": None,
                 "name": "US_fa1"},

                {"networkUris": [],
                 "mode":"Auto",
                 "lacpTimer":"Short",
                 "primaryPort":None,
                 "logicalPortConfigInfos":[{"desiredSpeed": "Speed4G", "logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": Supershaw_FA['bay_num']}, {"type": "Port", "relativeValue": Supershaw_FA['rel_ports'][1]}, {"type": "Enclosure", "relativeValue": 1}]}}],
                 "networkType": "FibreChannel",
                 "ethernetNetworkType": None,
                 "nativeNetworkUri": None,
                 "name": "US_fa2"},

                {"networkUris": [],
                 "mode":"Auto",
                 "lacpTimer":"Short",
                 "primaryPort":None,
                 "logicalPortConfigInfos":[{"desiredSpeed": "Speed8G", "logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": Supershaw_FA['bay_num']}, {"type": "Port", "relativeValue": Supershaw_FA['rel_ports'][2]}, {"type": "Enclosure", "relativeValue": 1}]}}],
                 "networkType": "FibreChannel",
                 "ethernetNetworkType": None,
                 "nativeNetworkUri": None,
                 "name": "US_fa3"},

                {"networkUris": [],
                 "mode":"Auto",
                 "lacpTimer":"Short",
                 "primaryPort":None,
                 "logicalPortConfigInfos":[{"desiredSpeed": "Speed2G", "logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": Sheppard_FA['bay_num']}, {"type": "Port", "relativeValue": Sheppard_FA['rel_ports'][0]}, {"type": "Enclosure", "relativeValue": 1}]}}],
                 "networkType": "FibreChannel",
                 "ethernetNetworkType": None,
                 "nativeNetworkUri": None,
                 "name": "US_fa4"},

                {"networkUris": [],
                 "mode":"Auto",
                 "lacpTimer":"Short",
                 "primaryPort":None,
                 "logicalPortConfigInfos":[{"desiredSpeed": "Speed4G", "logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": Sheppard_FA['bay_num']}, {"type": "Port", "relativeValue": Sheppard_FA['rel_ports'][1]}, {"type": "Enclosure", "relativeValue": 1}]}}],
                 "networkType": "FibreChannel",
                 "ethernetNetworkType": None,
                 "nativeNetworkUri": None,
                 "name": "US_fa5"},

                {"networkUris": [],
                 "mode":"Auto",
                 "lacpTimer":"Short",
                 "primaryPort":None,
                 "logicalPortConfigInfos":[{"desiredSpeed": "Speed8G", "logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": Sheppard_FA['bay_num']}, {"type": "Port", "relativeValue": Sheppard_FA['rel_ports'][2]}, {"type": "Enclosure", "relativeValue": 1}]}}],
                 "networkType": "FibreChannel",
                 "ethernetNetworkType": None,
                 "nativeNetworkUri": None,
                 "name": "US_fa6"}
                ]


eg_body1 = {'name': 'EG_A',
            'configurationScript': None,
            'interconnectBayMappings':
            [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
             {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
             {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
             {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
             {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
             {'interconnectBay': 6, 'logicalInterconnectGroupUri': None},
             {'interconnectBay': 7, 'logicalInterconnectGroupUri': None},
             {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}],
            'ipRangeUris': [],
            'enclosureCount': 1,
            'powerMode': None,
            'ambientTemperatureMode': 'Standard'}

enc_body1 = {'hostname': ENCLOSURE_IP, "username": oa_details['username'], "password": oa_details['password'], 'enclosureGroupUri': '', 'force': False, 'licensingIntent': 'OneViewNoiLO'}

SP_body1 = {"type": "ServerProfileV8",
            "serverHardwareUri": "",
            "serverHardwareTypeUri": "",
            "enclosureGroupUri": "",
            "serialNumberType": "Virtual",
            "iscsiInitiatorNameType": "AutoGenerated",
            "macType": "Physical",
            "wwnType": "Physical",
            "name": "",
            "description": "",
            "affinity": "Bay",
            "connections": [{"id": 1, "name": "connection1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2000", "networkUri": "", "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
                            {"id": 2, "name": "connection2", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2000", "networkUri": "", "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
                            {"id": 3, "name": "connection3", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2000", "networkUri": "", "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
                            {"id": 4, "name": "connection4", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2000", "networkUri": "", "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
                            {"id": 5, "name": "connection5", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2000", "networkUri": "", "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}}
                            ],
            "boot": {"manageBoot": True, "order": ["CD", "Floppy", "USB", "HardDisk", "PXE"]},
            "bootMode": None,
            "firmware": {"manageFirmware": False, "firmwareBaselineUri": "", "forceInstallFirmware": False, "firmwareInstallType": None, "firmwareScheduleDateTime": ""},
            "bios": {"manageBios": False, "overriddenSettings": []},
            "hideUnusedFlexNics": True,
            "iscsiInitiatorName": "",
            "osDeploymentSettings": None,
            "localStorage": {"sasLogicalJBODs": [], "controllers": []},
            "sanStorage": None}


FCnets_bfs = ["FC_da1", "FC_fa1", "FC_da4", "FC_fa4"]

arrayWwpn = ["20240002AC003644", "20110002AC003644", "20220002AC003644", "21110002AC003644"]


SP_body2 = {"type": "ServerProfileV8",
            "serverHardwareUri": "",
            "serverHardwareTypeUri": "",
            "enclosureGroupUri": "",
            "serialNumberType": "Virtual",
            "iscsiInitiatorNameType": "AutoGenerated",
            "macType": "Physical",
            "wwnType": "Physical",
            "name": "",
            "description": "",
            "affinity": "Bay",
            "connections": [
                           {"id": 1,
                            "name": "connection1",
                            "functionType": "FibreChannel",
                            "portId": "Auto",
                            "requestedMbps": "2500",
                            "networkUri": "",
                            "mac": None,
                            "wwpn": None,
                            "wwnn": None,
                            "ipv4": {},
                            "boot": {"priority": "Primary",
                                     "bootVolumeSource": "UserDefined",
                                     "targets": [{"arrayWwpn": "20240002AC003644", "lun": "0"}], "iscsi": {}}}],
            "boot": {"manageBoot": True, "order": ["CD", "Floppy", "USB", "HardDisk", "PXE"]},
            "bootMode": None,
            "firmware": {"manageFirmware": False, "firmwareBaselineUri": "", "forceInstallFirmware": False, "firmwareInstallType": None, "firmwareScheduleDateTime": ""},
            "bios": {"manageBios": False, "overriddenSettings": []},
            "hideUnusedFlexNics": True,
            "iscsiInitiatorName": "",
            "osDeploymentSettings": None,
            "osDeploymentSettings": None,
            "localStorage": {"sasLogicalJBODs": [], "controllers": []},
            "sanStorage": None}

li_body4 = [{"type": "uplink-setV4",
             "name": "us13", "networkUris": [],
             "portConfigInfos":[{"desiredSpeed": "Auto",
                                 "location": {"locationEntries": [{"value": "X7", "type": "Port"},
                                                                  {"value": 5, "type": "Bay"},
                                                                  {"value": "/rest/enclosures/09USE121ALJW", "type": "Enclosure"}]}}],
             "networkType": "FibreChannel",
             "primaryPortLocation": None,
             "reachability": None,
             "manualLoginRedistributionState": "Supported",
             "logicalInterconnectUri": [],
             "connectionMode":"Auto",
             "lacpTimer":"Short",
             "nativeNetworkUri":None,
             "fcNetworkUris":[],
             "fcoeNetworkUris":[],
             "state":None,
             "description":None,
             "status":None,
             "uri":None,
             "category":None,
             "modified":None,
             "created":None,
             "eTag":None},

            {"type": "uplink-setV4", "name": "us14", "networkUris": [],
             "portConfigInfos":[{"desiredSpeed": "Auto",
                                 "location": {"locationEntries": [{"value": "X8", "type": "Port"},
                                                                  {"value": 5, "type": "Bay"},
                                                                  {"value": "/rest/enclosures/09USE121ALJW", "type": "Enclosure"}]}}],
             "networkType": "FibreChannel",
             "primaryPortLocation": None,
             "reachability": None,
             "manualLoginRedistributionState": "Supported",
             "logicalInterconnectUri": [],
             "connectionMode":"Auto",
             "lacpTimer":"Short",
             "nativeNetworkUri":None,
             "fcNetworkUris":[],
             "fcoeNetworkUris":[],
             "state":None,
             "description":None,
             "status":None,
             "uri":None,
             "category":None,
             "modified":None,
             "created":None,
             "eTag":None}]

ic_disable_body = [{"associatedUplinkSetUri": "", "interconnectName": "", "portType": "Uplink", "portId": "", "portHealthStatus": "Normal", "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes":["FibreChannel"], "enabled":False, "portName":"", "portStatus":"Linked", "type":"port"}]

ic_enable_body = [{"associatedUplinkSetUri": "", "interconnectName": "", "portType": "Uplink", "portId": "", "portHealthStatus": "Normal", "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes":["FibreChannel"], "enabled":True, "portName":"", "portStatus":"Linked", "type":"port"}]

connections_edit_add1 = [{"id": 1, "name": "connection1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2000", "networkUri": "", "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
                         {"id": 2, "name": "connection2", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2000", "networkUri": "", "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
                         {"id": 3, "name": "connection3", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2000", "networkUri": "", "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
                         {"id": 4, "name": "connection4", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2000", "networkUri": "", "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
                         {"id": 5, "name": "connection5", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2000", "networkUri": "", "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}}
                         ]

connections_edit_add2 = [{"id": 1, "name": "connection1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2000", "networkUri": "", "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
                         {"id": 2, "name": "connection2", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2000", "networkUri": "", "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
                         {"id": 3, "name": "connection3", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2000", "networkUri": "", "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
                         {"id": 4, "name": "connection4", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2000", "networkUri": "", "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
                         {"id": 5, "name": "connection5", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2000", "networkUri": "", "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}}
                         ]

connections_edit_add3 = [{"id": 1, "name": "connection1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2000", "networkUri": "", "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
                         {"id": 2, "name": "connection2", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2000", "networkUri": "", "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
                         {"id": 3, "name": "connection3", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2000", "networkUri": "", "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
                         {"id": 4, "name": "connection4", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2000", "networkUri": "", "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
                         {"id": 5, "name": "connection5", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2000", "networkUri": "", "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}}
                         ]

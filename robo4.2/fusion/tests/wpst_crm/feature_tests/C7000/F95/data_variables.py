import os
import sys

cwd = os.getcwd()
download_to_path = cwd


def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist

APPLIANCE_IP = '15.245.133.179'
ENCLOSURE_IP = '15.245.129.74'
Enclosure_Name = 'WPST-PABA58-EN1'

appliance_cred = ['root', 'hpvse1']

admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}

enclosure_credentials = {'userName': 'Administrator', 'password': 'hpvse1'}

Bulk_enet_body = {"vlanIdRange": "1-4094", "purpose": "General", "namePrefix": "NETG", "smartLink": False, "privateNetwork": False, "bandwidth": {"maximumBandwidth": 10000, "typicalBandwidth": 2000}, "type": "bulk-ethernet-networkV1"}

Fcoe_body = {"name": "NET", "vlanId": "1001", "connectionTemplateUri": None, "type": "fcoe-networkV4"}

Enet_body = {"vlanId": 10, "purpose": "General", "name": "Enet", "smartLink": False, "privateNetwork": False, "connectionTemplateUri": None, "ethernetNetworkType": "Tagged", "type": "ethernet-networkV4"}

Fc_body = {"name": "fc", "connectionTemplateUri": None, "linkStabilityTime": "30", "autoLoginRedistribution": True, "fabricType": "FabricAttach", "type": "fc-networkV4"}

empty_variable = ''

bay_f95 = '1'
server_f95 = '1'

relative_ports_f95 = ['17', '21']
normal_ports_f95 = ['X4']
Tagged_VLAN = '115'
Server_power_on_sleep_time = '500s'

error_msg_1 = 'Ethernet network Enet cannot be created because the maximum number of networks (8192) exists.'

error_msg_2 = 'FCoE network FCOE_NET cannot be created because the maximum number of networks (8192) exists.'

error_msg_3 = 'FC network fc cannot be created because the maximum number NPIV values are allocated.'

error_msg_4 = 'Internal networks can contain no more than 1000 Ethernet networks. The requested configuration will result in 1001 networks.'

error_msg_5 = 'An uplink set can contain no more than 1000 Ethernet networks. The requested configuration will result in 1001 networks.'

error_msg_6 = 'Port is not available for analyzer port configuration.'

lig_inet_uri = '/rest/logical-interconnect-groups/internal-network-groups/validator'

Preview_uri = '/rest/enclosure-preview'

Preview_body = {"hostname": ENCLOSURE_IP, "username": enclosure_credentials['userName'], "password": enclosure_credentials['password'], "ligPrefix": "LIG_1", "force": True, "logicalInterconnectGroupNeeded": True}

lig_body1 = {"name": "LIG_1",
             "type": "logical-interconnect-groupV4",
             "enclosureType": "C7000",
             "interconnectMapTemplate": {},
             "internalNetworkUris": [],
             "uplinkSets": [],
             "stackingMode": "Enclosure",
             "ethernetSettings": None,
             "state": "Active",
             "telemetryConfiguration": None,
             "snmpConfiguration": None,
             "qosConfiguration": None}

eg_body1 = enc_group1 = {'name': 'EG1', "interconnectBayMappings":
                         [{"interconnectBay": 1, "logicalInterconnectGroupUri": 'LIG_1'},
                          {"interconnectBay": 2, "logicalInterconnectGroupUri": 'LIG_1'},
                             {"interconnectBay": 3, "logicalInterconnectGroupUri": 'LIG_1'},
                             {"interconnectBay": 4, "logicalInterconnectGroupUri": 'LIG_1'},
                             {"interconnectBay": 5, "logicalInterconnectGroupUri": 'LIG_1'},
                             {"interconnectBay": 6, "logicalInterconnectGroupUri": 'LIG_1'},
                             {"interconnectBay": 7, "logicalInterconnectGroupUri": 'LIG_1'},
                             {"interconnectBay": 8, "logicalInterconnectGroupUri": None}],
                         "ipRangeUris": [],
                         "enclosureCount": 1,
                         "osDeploymentSettings": None,
                         "configurationScript": None,
                         "powerMode": None,
                         "ambientTemperatureMode": "Standard"}

enc_body1 = {'hostname': ENCLOSURE_IP, 'username': enclosure_credentials['userName'], 'password': enclosure_credentials['password'], 'enclosureGroupUri': '', 'force': False, 'licensingIntent': 'OneViewNoiLO'}

lig_inet_body = {"internalNetworkUris": "", "type": "lite-network-logical-interconnect-group", "enclosureType": "C7000"}

lig_us_body1 = {"networkType": "Ethernet", "ethernetNetworkType": "Tagged", "networkUris": [], "nativeNetworkUri": None, "lacpTimer": "Short", "primaryPort": None, "logicalPortConfigInfos": [{"logicalLocation": {"locationEntries": [{"relativeValue": bay_f95, "type": "Bay"}, {"relativeValue": relative_ports_f95[0], "type":"Port"}, {"relativeValue": 1, "type": "Enclosure"}]}, "desiredSpeed": "Auto"}], "reachability": None, "mode": "Auto", "name": "US1"}

li_us_body1 = {"type": "uplink-setV4", "name": "US1", "networkUris": [], "portConfigInfos": [{"desiredSpeed": "Auto", "location": {"locationEntries": [{"value": normal_ports_f95[0], "type":"Port"}, {"value": bay_f95, "type": "Bay"}, {"value": "", "type": "Enclosure"}]}}], "networkType": "Ethernet", "primaryPortLocation": None, "reachability": None, "manualLoginRedistributionState": "NotSupported", "logicalInterconnectUri": "", "connectionMode": "Auto", "lacpTimer": "Short", "nativeNetworkUri": None, "fcNetworkUris": [], "fcoeNetworkUris": [], "state": None, "description": None, "status": None, "uri": None, "category": None, "modified": None, "created": None, "eTag": None, "ethernetNetworkType": "Tagged"}

SP_body1 = {"type": "ServerProfileV8", "serverHardwareUri": "", "serverHardwareTypeUri": "", "enclosureGroupUri": "", "serialNumberType": "Virtual", "iscsiInitiatorNameType": "AutoGenerated", "macType": "Virtual", "wwnType": "Virtual", "name": "SP1", "description": "", "affinity": "Bay", "connections": [{"id": 1, "name": "", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2000", "networkUri": "", "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}}], "boot": {"manageBoot": True, "order": ["CD", "Floppy", "USB", "HardDisk", "PXE"]}, "bootMode": None, "firmware": {"manageFirmware": False, "firmwareBaselineUri": "", "forceInstallFirmware": False, "firmwareInstallType": None, "firmwareScheduleDateTime": ""}, "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True, "iscsiInitiatorName": "", "osDeploymentSettings": None, "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": None}

pmoni_body1 = {"type": "port-monitor", "enablePortMonitor": True, "analyzerPort": {"portMonitorConfigInfo": "AnalyzerPort", "portUri": ""}, "monitoredPorts": [{"portMonitorConfigInfo": "MonitoredBoth", "portUri": ""}]}

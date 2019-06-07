import paramiko
import re
import sys
import os


def make_range_list(vrange):
    rlist = []
    for x in xrange(vrange['start'], (vrange['end'] + 1)):
        rlist.append(vrange['prefix'] + str(x) + vrange['suffix'])
    return rlist


def rlist(start, end, prefix='net_', suffix=''):
    tlist = []
    for x in xrange(start, end + 1):
        tlist.append(prefix + str(x) + suffix)
    return tlist


def convert_unicode_to_string(String):
    res = String.encode("utf-8")
    return res

APPLIANCE_IP = '15.186.14.96'
ENCLOSURE_IP = '15.186.19.77'
Enclosure_Name = ['enc2']

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}
oa_details = {"oa_ip": ENCLOSURE_IP, "username": "Administrator", "password": "compaq"}
Preview_uri = '/rest/enclosure-preview'

Preview_body = {"hostname": ENCLOSURE_IP, "username": oa_details['username'], "password": oa_details['password'], "ligPrefix": "LIG_A", "force": True, "logicalInterconnectGroupNeeded": True}

Trunking_Bays = ['5', '6']

FC_switch_details = {'ip': '15.186.16.231', 'userName': 'admin', 'password': 'password'}

interconnect_details = [{'ip': '15.186.19.118', 'userName': 'root', 'password': 'fibranne'}, {'ip': '15.186.18.153', 'userName': 'root', 'password': 'R4RVY96Y'}]

Trunk_Commands = ['porttrunkarea --show enabled', 'portdisable', 'porttrunkarea --disable', 'portcfgtrunkport', 'portenable', 'porttrunkarea --enable', 'portCfgPersistentEnable']

no_trunk_message = 'No ports have Trunk Area enabled'

root_info = '\nExecution Succeeded. See vcsu-hill.log for more information.'

FC_switch_ports = {'segment1': [0, 1, 2, 3, 4, 5, 6, 7], 'segment2': [8, 9, 10]}

desiredSpeeds = ['Auto', 'Speed4G', 'Speed8G', 'Speed16G']

fcmodes = ['TRUNK', 'NONE']

empty_list = []
alert_message = "Trunking is enabled for uplink set us1 but no trunks have formed."
power_state_value = ['poweroff', 'poweron']

interconnect_state = ['OFF', 'ON']

US_details = [{'bay': Trunking_Bays[0], 'Act_ports': ['1', '2', '3', '4', '5', '6', '7', '8'], 'rel_ports':['17', '18', '19', '20', '21', '22', '23', '24'], 'name':'us1'}, {'bay': Trunking_Bays[1], 'Act_ports': ['1', '2', '3'], 'rel_ports':['17', '18', '19'], 'name':'us2'}]

ic_firmwareVersion_old = '4.00'
ic_firmwareVersion_new = '3.08'
SPP_bundle = 'SPPGen10Snap2.2017_1026.37.iso'
INTERCONNECTS = ['enc2, interconnect 5', 'enc2, interconnect 6']
Fc_body = {"name": "",
           "connectionTemplateUri": None,
           "linkStabilityTime": "30",
           "autoLoginRedistribution": True,
           "fabricType": "",
           "type": "fc-networkV4"}

lig_body1 = {"name": "lig",
             "type": "logical-interconnect-groupV5",
             "enclosureType": "C7000",
             "interconnectMapTemplate": {},
             "internalNetworkUris": [],
             "uplinkSets": [{'name': 'us1',
                             'networkType': 'FibreChannel',
                             'networkUris': [],
                             'fcMode': 'TRUNK',
                             'nativeNetworkUri': None,
                             'mode': 'Auto',
                             'logicalPortConfigInfos': [{"desiredSpeed": "Auto", "logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 5}, {"type": "Port", "relativeValue": 17}, {"type": "Enclosure", "relativeValue": 1}]}},
                                                        {"desiredSpeed": "Auto", "logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 5}, {"type": "Port", "relativeValue": 18}, {"type": "Enclosure", "relativeValue": 1}]}},
                                                        {"desiredSpeed": "Auto", "logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 5}, {"type": "Port", "relativeValue": 19}, {"type": "Enclosure", "relativeValue": 1}]}},
                                                        {"desiredSpeed": "Auto", "logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 5}, {"type": "Port", "relativeValue": 20}, {"type": "Enclosure", "relativeValue": 1}]}},
                                                        {"desiredSpeed": "Auto", "logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 5}, {"type": "Port", "relativeValue": 21}, {"type": "Enclosure", "relativeValue": 1}]}},
                                                        {"desiredSpeed": "Auto", "logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 5}, {"type": "Port", "relativeValue": 22}, {"type": "Enclosure", "relativeValue": 1}]}},
                                                        {"desiredSpeed": "Auto", "logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 5}, {"type": "Port", "relativeValue": 23}, {"type": "Enclosure", "relativeValue": 1}]}},
                                                        {"desiredSpeed": "Auto", "logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 5}, {"type": "Port", "relativeValue": 24}, {"type": "Enclosure", "relativeValue": 1}]}}]
                             }],
             "stackingMode": "Enclosure",
             "ethernetSettings": None,
             "state": "Active",
             "telemetryConfiguration": None,
             "snmpConfiguration": None,
             "qosConfiguration": None}

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

logicalPortConfigInfos = [{"desiredSpeed": "", "logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": ""},
                                                                                       {"type": "Port", "relativeValue": ""},
                                                                                       {"type": "Enclosure", "relativeValue": 1}]}},
                          {"desiredSpeed": "", "logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": ""},
                                                                                       {"type": "Port", "relativeValue": ""},
                                                                                       {"type": "Enclosure", "relativeValue": 1}]}},
                          {"desiredSpeed": "", "logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": ""},
                                                                                       {"type": "Port", "relativeValue": ""},
                                                                                       {"type": "Enclosure", "relativeValue": 1}]}},
                          {"desiredSpeed": "", "logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": ""},
                                                                                       {"type": "Port", "relativeValue": ""},
                                                                                       {"type": "Enclosure", "relativeValue": 1}]}},
                          {"desiredSpeed": "", "logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": ""},
                                                                                       {"type": "Port", "relativeValue": ""},
                                                                                       {"type": "Enclosure", "relativeValue": 1}]}},
                          {"desiredSpeed": "", "logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": ""},
                                                                                       {"type": "Port", "relativeValue": ""},
                                                                                       {"type": "Enclosure", "relativeValue": 1}]}},
                          {"desiredSpeed": "", "logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": ""},
                                                                                       {"type": "Port", "relativeValue": ""},
                                                                                       {"type": "Enclosure", "relativeValue": 1}]}},
                          {"desiredSpeed": "", "logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": ""},
                                                                                       {"type": "Port", "relativeValue": ""},
                                                                                       {"type": "Enclosure", "relativeValue": 1}]}}]

portConfigInfos = [{"desiredSpeed": "", "location": {"locationEntries": [{"value": "", "type": "Port"}, {"value": "", "type": "Bay"}, {"value": "", "type": "Enclosure"}]}},
                   {"desiredSpeed": "", "location": {"locationEntries": [{"value": "", "type": "Port"}, {"value": "", "type": "Bay"}, {"value": "", "type": "Enclosure"}]}},
                   {"desiredSpeed": "", "location": {"locationEntries": [{"value": "", "type": "Port"}, {"value": "", "type": "Bay"}, {"value": "", "type": "Enclosure"}]}},
                   {"desiredSpeed": "", "location": {"locationEntries": [{"value": "", "type": "Port"}, {"value": "", "type": "Bay"}, {"value": "", "type": "Enclosure"}]}},
                   {"desiredSpeed": "", "location": {"locationEntries": [{"value": "", "type": "Port"}, {"value": "", "type": "Bay"}, {"value": "", "type": "Enclosure"}]}},
                   {"desiredSpeed": "", "location": {"locationEntries": [{"value": "", "type": "Port"}, {"value": "", "type": "Bay"}, {"value": "", "type": "Enclosure"}]}},
                   {"desiredSpeed": "", "location": {"locationEntries": [{"value": "", "type": "Port"}, {"value": "", "type": "Bay"}, {"value": "", "type": "Enclosure"}]}},
                   {"desiredSpeed": "", "location": {"locationEntries": [{"value": "", "type": "Port"}, {"value": "", "type": "Bay"}, {"value": "", "type": "Enclosure"}]}}]

li_upsbody = [{"type": "uplink-setV4",
               "name": "",
               "fcMode": "",
               "networkUris": [],
               "portConfigInfos":"",
               "networkType":"FibreChannel",
               "primaryPortLocation":None,
               "reachability":None,
               "manualLoginRedistributionState":"Supported",
               "logicalInterconnectUri":"",
               "connectionMode":"Auto",
               "fcoeNetworkUris":[],
               "fcNetworkUris":[]}]

lig_uls_body1 = {"networkUris": [],
                 "mode": "Auto",
                 "name": "",
                 "lacpTimer": "Short",
                 "primaryPort": None,
                 "logicalPortConfigInfos": "",
                 "networkType": "FibreChannel",
                 "ethernetNetworkType": None,
                 "nativeNetworkUri": None,
                 }
liupdate_body = {"sppUri": '',
                 "command": "UPDATE",
                 "force": False,
                 "ethernetActivationType": "Parallel",
                 "ethernetActivationDelay": "0",
                 "fcActivationType": "Parallel",
                 "fcActivationDelay": "0",
                 "validationType": "None"}

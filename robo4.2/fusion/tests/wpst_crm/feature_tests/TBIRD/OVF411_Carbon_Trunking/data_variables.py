from copy import deepcopy


def make_range_list(start, end, prefix='net_', suffix=''):
    tlist = []
    for x in xrange(start, end + 1):
        tlist.append(prefix + str(x) + suffix)
    return tlist


def rlist(start, end, prefix='net_', suffix=''):
    tlist = []
    for x in xrange(start, end + 1):
        tlist.append(prefix + str(x) + suffix)
    return tlist


def convert_unicode_to_string(String):
    res = String.encode("utf-8")
    return res

enclosureCount = 1
Enclosure_Name = ['CN751302K0']

# values should be either 'Redundant' or 'NonRedundantASide' or 'NonRedundantBSide'
Enc_bay_type = {'enc1': 'Redundant'}

IC_bay_set = 1
IC_bay_set_pair = IC_bay_set + 3
# Enc_bay_spec = {'enc1':{'ic_'IC_bay_set:'Redundant','ic_'IC_bay_set_pair:'Redundant'},'enc2':{'ic_'IC_bay_set:'Redundant','ic_'IC_bay_set_pair:'Redundant'},'enc3':{'ic_'IC_bay_set:'Redundant','ic_'IC_bay_set_pair:'Redundant'},'enc4':{'ic_'IC_bay_set:'Redundant','ic_'IC_bay_set_pair:'Redundant'},'enc5':{'ic_'IC_bay_set:'Redundant','ic_'IC_bay_set_pair:'Redundant'}}

APPLIANCE_IP = '15.186.9.21'
admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}
root_credntials = {'userName': 'root', 'password': 'hpvse1'}
FC_switch_details = {'ip': '15.186.24.76', 'userName': 'admin', 'password': 'password'}
Trunk_Commands = ['porttrunkarea --show enabled', 'portdisable', 'porttrunkarea --disable', 'portcfgtrunkport', 'portenable', 'porttrunkarea --enable', 'portCfgPersistentEnable']
no_trunk_message = 'No ports have Trunk Area enabled'
FC_switch_ports = {'segment1': [4, 5, 6, 7], 'segment2': [8, 9, 10, 11], 'segment3': [16, 17, 18, 19, 20, 21, 22, 23]}

IC_model_name = "Virtual Connect SE 16Gb FC Module for Synergy"
IC_powerstate_body = [{'op': 'replace', 'path': '/powerState', 'value': ''}]
empty_list = []
alert_message = "Trunking is enabled for uplink set us3 but no trunks have formed."
neg_ports = ['1', '2', 'Q2:3', 'Q2:4']

icmap_Redundant = {"interconnectMapEntryTemplates": [{"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": IC_bay_set},
                                                                                              {"type": "Enclosure", "relativeValue": -1}]}, "logicalDownlinkUri": None, "permittedInterconnectTypeUri": "", "enclosureIndex": -1},
                                                     {"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": IC_bay_set_pair},
                                                                                              {"type": "Enclosure", "relativeValue": -1}]}, "logicalDownlinkUri": None, "permittedInterconnectTypeUri": "", "enclosureIndex": -1}]}

icmap_NonRedundantASide = {"interconnectMapEntryTemplates": [{"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": IC_bay_set},
                                                                                                      {"type": "Enclosure", "relativeValue": -1}]}, "logicalDownlinkUri": None, "permittedInterconnectTypeUri": "", "enclosureIndex": -1}]}

icmap_NonRedundantBSide = {"interconnectMapEntryTemplates": [{"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": IC_bay_set_pair},
                                                                                                      {"type": "Enclosure", "relativeValue": -1}]}, "logicalDownlinkUri": None, "permittedInterconnectTypeUri": "", "enclosureIndex": -1}]}

desiredSpeeds = ['Auto', 'Speed4G', 'Speed8G', 'Speed16G']

fcmodes = ['TRUNK', 'NONE']

power_state_value = ['On', 'Off']

Action_ICM = ['EFuseOff', 'EFuseOn']

logicalPortConfigInfos = [{"desiredSpeed": "", "logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": ""},
                                                                                       {"type": "Port", "relativeValue": ""},
                                                                                       {"type": "Enclosure", "relativeValue": -1}]}},
                          {"desiredSpeed": "", "logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": ""},
                                                                                       {"type": "Port", "relativeValue": ""},
                                                                                       {"type": "Enclosure", "relativeValue": -1}]}},
                          {"desiredSpeed": "", "logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": ""},
                                                                                       {"type": "Port", "relativeValue": ""},
                                                                                       {"type": "Enclosure", "relativeValue": -1}]}},
                          {"desiredSpeed": "", "logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": ""},
                                                                                       {"type": "Port", "relativeValue": ""},
                                                                                       {"type": "Enclosure", "relativeValue": -1}]}},
                          {"desiredSpeed": "", "logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": ""},
                                                                                       {"type": "Port", "relativeValue": ""},
                                                                                       {"type": "Enclosure", "relativeValue": -1}]}},
                          {"desiredSpeed": "", "logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": ""},
                                                                                       {"type": "Port", "relativeValue": ""},
                                                                                       {"type": "Enclosure", "relativeValue": -1}]}},
                          {"desiredSpeed": "", "logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": ""},
                                                                                       {"type": "Port", "relativeValue": ""},
                                                                                       {"type": "Enclosure", "relativeValue": -1}]}},
                          {"desiredSpeed": "", "logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": ""},
                                                                                       {"type": "Port", "relativeValue": ""},
                                                                                       {"type": "Enclosure", "relativeValue": -1}]}}]


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


US_details = [{'bay': IC_bay_set, 'Act_ports': ['1', '2', '3', '4'], 'rel_ports':['13', '14', '15', '16'], 'name':'us1'}, {'bay': IC_bay_set_pair, 'Act_ports': ['1', '2', '3', '4'], 'rel_ports':['13', '14', '15', '16'], 'name':'us2'}, {'bay': IC_bay_set, 'Act_ports': ['Q1:1', 'Q1:2', 'Q1:3', 'Q1:4', 'Q2:1', 'Q2:2', 'Q2:3', 'Q2:4'], 'rel_ports':['21', '22', '23', '24', '25', '26', '27', '28'], 'name':'us3'}]

# LIG_name_list=['LIG_enc1_Redundant']

Fc_body = {"name": "",
           "connectionTemplateUri": None,
           "linkStabilityTime": "30",
           "autoLoginRedistribution": True,
           "fabricType": "",
           "type": "fc-networkV4"}

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


uri = '/rest/logical-interconnect-groups/b6677136-8e29-4146-b1b8-2353edc6971a'
LIG_body = {"type": "logical-interconnect-groupV4",
            "ethernetSettings": None,
            "name": "",
            "telemetryConfiguration": None,
            "interconnectMapTemplate": "",
            "uplinkSets": [],
            "enclosureType": "SY12000",
            "enclosureIndexes": [-1],
            "interconnectBaySet": IC_bay_set,
            "redundancyType": "",
            "internalNetworkUris": [],
            "snmpConfiguration": None,
            "qosConfiguration": None}

interconnectBayMappings = [{"interconnectBay": IC_bay_set, "enclosureIndex": 1, "logicalInterconnectGroupUri": ""},
                           {"interconnectBay": IC_bay_set_pair, "enclosureIndex": 1, "logicalInterconnectGroupUri": ""},
                           {"interconnectBay": IC_bay_set, "enclosureIndex": 2, "logicalInterconnectGroupUri": ""},
                           {"interconnectBay": IC_bay_set_pair, "enclosureIndex": 2, "logicalInterconnectGroupUri": ""},
                           {"interconnectBay": IC_bay_set, "enclosureIndex": 3, "logicalInterconnectGroupUri": ""},
                           {"interconnectBay": IC_bay_set_pair, "enclosureIndex": 3, "logicalInterconnectGroupUri": ""},
                           {"interconnectBay": IC_bay_set, "enclosureIndex": 4, "logicalInterconnectGroupUri": ""},
                           {"interconnectBay": IC_bay_set_pair, "enclosureIndex": 4, "logicalInterconnectGroupUri": ""},
                           {"interconnectBay": IC_bay_set, "enclosureIndex": 5, "logicalInterconnectGroupUri": ""},
                           {"interconnectBay": IC_bay_set_pair, "enclosureIndex": 5, "logicalInterconnectGroupUri": ""}]

EG_body = {"name": "",
           "interconnectBayMappings": interconnectBayMappings,
           "ipAddressingMode": "DHCP",
           "ipRangeUris": [],
                   "enclosureCount": enclosureCount}
les = [{'name': 'LE_1',
        'enclosureUris': [],
        'enclosureGroupUri': '',
        'firmwareBaselineUri': None,
        'forceInstallFirmware': False
        }]

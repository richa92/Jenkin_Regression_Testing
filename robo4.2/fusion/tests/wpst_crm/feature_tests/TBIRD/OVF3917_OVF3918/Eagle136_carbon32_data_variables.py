import os
import sys

APPLIANCE_IP = '15.186.9.136'
state = 'Ok'
admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}
appliance_cred = ['root', 'hpvse1']
IC_bay_set = 1
IC_bay_set_pair = IC_bay_set + 3
Enclosure_Name = ['MXQ734024N']
enclosureCount = 1
ENC1 = 'MXQ734024N'
ENC2 = 'MXQ734024N'
INTERCONNECTS_dto = {'name': 'MXQ734024N, interconnect 1'}, {'name': 'MXQ734024N, interconnect 4'}
IC_NAMES = ['MXQ734024N, interconnect 1', 'MXQ734024N, interconnect 4']
IC_model_name = 'Virtual Connect SE 32Gb FC Module for Synergy'
IC_models = ['Virtual Connect SE 32Gb FC Module for Synergy', 'Virtual Connect SE 16Gb FC TAA Module for Synergy', 'Virtual Connect SE 16Gb FC Module for Synergy']

Enc_bay_type = {'enc1': 'Redundant', 'enc2': 'Redundant'}
FUSION_IP = APPLIANCE_IP
FUSION_SSH_USERNAME = "root"
FUSION_SSH_PASSWORD = "hpvse1"
FUSION_PROMPT = '#'
FUSION_TIMEOUT = 180
IC_SSH_USERNAME = "root"
IC_TIMEOUT = 100
IC_PROMPT = '>'
time = 300

LIG = ['LIG1', 'LIG2']
uplinkset_names = ['UplinkSet_1', 'UplinkSet_2', 'UplinkSet_3', 'UplinkSet_4']
icmap_Redundant = {"interconnectMapEntryTemplates": [{"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": IC_bay_set},
                                                                                              {"type": "Enclosure", "relativeValue": -1}]}, "logicalDownlinkUri": None, "permittedInterconnectTypeUri": "", "enclosureIndex": -1},
                                                     {"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": IC_bay_set_pair},
                                                                                              {"type": "Enclosure", "relativeValue": -1}]}, "logicalDownlinkUri": None, "permittedInterconnectTypeUri": "", "enclosureIndex": -1}]}

icmap_NonRedundantASide = {"interconnectMapEntryTemplates": [{"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": IC_bay_set},
                                                                                                      {"type": "Enclosure", "relativeValue": -1}]}, "logicalDownlinkUri": None, "permittedInterconnectTypeUri": "", "enclosureIndex": -1}]}

icmap_NonRedundantBSide = {"interconnectMapEntryTemplates": [{"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": IC_bay_set_pair},
                                                                                                      {"type": "Enclosure", "relativeValue": -1}]}, "logicalDownlinkUri": None, "permittedInterconnectTypeUri": "", "enclosureIndex": -1}]}

enc_count = 1


ENC2 = 'XXXXXXXXXX'
ENC3 = 'XXXXXXXXXX'
ENC4 = 'XXXXXXXXXX'
ENC5 = 'XXXXXXXXXX'

Enc1Map = \
    [
        {'bay': 1, 'enclosure': -1, 'type': 'Virtual Connect SE 32Gb FC Module for Synergy', 'enclosureIndex': -1},
        {'bay': 4, 'enclosure': -1, 'type': 'Virtual Connect SE 32Gb FC Module for Synergy', 'enclosureIndex': -1}
    ]


LIG_body = {"type": "logical-interconnect-groupV6",
            "ethernetSettings": None,
            "name": "",
            "telemetryConfiguration": None,
            "interconnectMapTemplate": "",
            "uplinkSets": [],
            "enclosureType": "SY12000",
            "enclosureIndexes": [-1],
            "enclosureIndexes": [-1],
            "interconnectBaySet": IC_bay_set,
            "redundancyType": "",
            "internalNetworkUris": [],
            "snmpConfiguration": None,
            "qosConfiguration": None}

LIG_new = {
    'name': 'LIG1',
    'interconnectMapTemplate': Enc1Map,
    'enclosureIndexes': [-1],
    'interconnectBaySet': 1,
    'redundancyType': 'Redundant',
    'uplinkSets': []}

enc_groups = {'name': 'EG1',
              'enclosureCount': 1,
              'ipAddressingMode': 'DHCP',
              'interconnectBayMappings':
              [{'interconnectBay': 1, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
               {'interconnectBay': 4, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': 'LIG:LIG1'}
               ],
              'ipRangeUris': [],
              'powerMode': 'RedundantPowerFeed'
              }

les = {'name': 'LE1',
       'enclosureUris': ['ENC:' + ENC1],
       'enclosureGroupUri': 'EG:EG1',
       'firmwareBaselineUri': None,
       'forceInstallFirmware': False
       }

LES_name = 'LE1'

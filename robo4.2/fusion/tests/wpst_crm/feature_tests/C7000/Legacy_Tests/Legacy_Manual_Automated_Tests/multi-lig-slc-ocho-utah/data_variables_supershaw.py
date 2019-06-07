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


APPLIANCE_IP = '15.186.14.17'

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}
# Enclosure IP
ENCLOSURE_IP = '15.186.2.227'

oa_details = {"oa_ip": ENCLOSURE_IP, "username": "Administrator", "password": "Compaq123"}

OA_USER = 'Administrator'

OA_PASS = 'Compaq123'

users = [{'type': 'UserAndPermissions', 'userName': 'nat', 'fullName': 'Networkadmin', 'password': 'hpvse123', 'enabled': True,
          'permissions': [{'roleName': 'Network administrator', 'scopeUri': None}]},
         {'type': 'UserAndPermissions', 'userName': 'sarah', 'fullName': 'Serveradmin', 'password': 'hpvse123', 'enabled': True,
          'permissions': [{'roleName': 'Server administrator', 'scopeUri': None}]}]


network_credentials = {'userName': 'nat', 'password': 'hpvse123'}

server_credentials = {'userName': 'sarah', 'password': 'hpvse123'}

network_user = {'type': 'UserAndPermissions', 'userName': 'nat', 'fullName': 'Networkadmin', 'password': 'hpvse123', 'enabled': True,
                'permissions': [{'roleName': 'Network administrator', 'scopeUri': None}]}

serveradmin = {'type': 'UserAndPermissions', 'userName': 'sarah', 'fullName': 'Serveradmin', 'password': 'hpvse123', 'enabled': True,
               'permissions': [{'roleName': 'Server administrator', 'scopeUri': None}]}

ENC1 = 'aus-c7000-188'

LI = [ENC1 + '-' + 'LIG-COMP-OU1', ENC1 + '-' + 'LIG-COMP-OU2']

LIG1 = 'LIG-COMP-OU1'

LIG2 = 'LIG-COMP-OU2'

ligs = {'lig1':
        {'name': 'LIG-COMP-OU1',
         'type': 'logical-interconnect-groupV6',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric-20/40 F8 Module'}],
         "internalNetworkUris": [],
            "uplinkSets": [],
            "stackingMode": "Enclosure",
            "ethernetSettings": None,
            "state": "Active",
            "telemetryConfiguration": None,
            "snmpConfiguration": None,
            "qosConfiguration": None},
        'lig2':
        {'name': 'LIG-COMP-OU2',
         'type': 'logical-interconnect-groupV6',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC Flex-10/10D Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC Flex-10/10D Module'}],
         "internalNetworkUris": [],
            "uplinkSets": [],
            "stackingMode": "Enclosure",
            "ethernetSettings": None,
            "state": "Active",
            "telemetryConfiguration": None,
            "snmpConfiguration": None,
            "qosConfiguration": None}
        }

enc_group = {'name': 'config1-group',
             'interconnectBayMappings':
             [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:LIG-COMP-OU1'},
                 {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:LIG-COMP-OU1'},
                 {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG-COMP-OU2'},
                 {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:LIG-COMP-OU2'},
                 {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                 {'interconnectBay': 6, 'logicalInterconnectGroupUri': None},
                 {'interconnectBay': 7, 'logicalInterconnectGroupUri': None},
                 {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}],
             'ipRangeUris': [],
             'enclosureCount': 1,
             'osDeploymentSettings': None,
             'configurationScript': None,
             'powerMode': None,
             'ambientTemperatureMode': 'Standard'}


enc_body1 = [{'hostname': '15.186.2.227', 'username': 'Administrator', 'password': 'Compaq123', 'enclosureGroupUri': 'EG:config1-group', 'licensingIntent': 'OneViewNoiLO'}]

enc_body2 = [{'hostname': '15.186.2.227', 'username': 'Administrator', 'password': 'Compaq123', 'enclosureGroupUri': 'EG:config1-group_3', 'licensingIntent': 'OneViewNoiLO'}]

enc_unmanaged = [{'hostname': '15.186.2.227', 'username': 'Administrator', 'password': 'Compaq123', 'enclosureGroupUri': 'EG:config1-group_1', 'licensingIntent': 'OneViewNoiLO'}]

enc_inventory = [{'hostname': '15.186.2.227', 'username': 'Administrator', 'password': 'Compaq123', 'enclosureGroupUri': 'EG:config1-group_2', 'licensingIntent': 'OneViewNoiLO'}]

INTERCONNECTS_enc1 = [ENC1 + ', interconnect 1', ENC1 + ', interconnect 2', ENC1 + ', interconnect 3', ENC1 + ', interconnect 4']

interconnect_bay = ['3', '4']

interconnect_bay1 = ['2', '4']

INTERCONNECTS_Int1 = ['1', '2']

INTERCONNECTS_Int2 = ['3', '4']

INTERCONNECTS_Int3 = ['1', '3']

INTERCONNECTS_Int4 = ['2', '4']

edit_lig = {'lig1':
            {'name': 'LIG-COMP-OU1',
             'type': 'logical-interconnect-groupV6',
             'enclosureType': 'C7000',
             'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                                         {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric-20/40 F8 Module'}],
             "internalNetworkUris": [],
             "uplinkSets": [],
             "stackingMode": "Enclosure",
             "ethernetSettings": None,
             "state": "Active",
             "telemetryConfiguration": None,
             "snmpConfiguration": None,
             "qosConfiguration": None},
            'lig2':
            {'name': 'LIG-COMP-OU2',
                'type': 'logical-interconnect-groupV6',
                'enclosureType': 'C7000',
                'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'}],
                "internalNetworkUris": [],
                "uplinkSets": [],
                "stackingMode": "Enclosure",
                "ethernetSettings": None,
                "state": "Active",
                "telemetryConfiguration": None,
                "snmpConfiguration": None,
                "qosConfiguration": None}
            }

edit_eg = {'name': 'config1-group_1',
           'interconnectBayMappings':
           [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:LIG-COMP-OU1'},
            {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:LIG-COMP-OU1'},
            {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG-COMP-OU2'},
            {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:LIG-COMP-OU2'},
            {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
            {'interconnectBay': 6, 'logicalInterconnectGroupUri': None},
            {'interconnectBay': 7, 'logicalInterconnectGroupUri': None},
            {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}],
           'ipRangeUris': [],
           'enclosureCount': 1,
           'osDeploymentSettings': None,
           'configurationScript': None,
           'powerMode': None,
           'ambientTemperatureMode': 'Standard'}

edit_lig1 = {'lig1':
             {'name': 'LIG-COMP-OU1',
              'type': 'logical-interconnect-groupV6',
              'enclosureType': 'C7000',
              'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric-20/40 F8 Module'}],
              "internalNetworkUris": [],
              "uplinkSets": [],
              "stackingMode": "Enclosure",
              "ethernetSettings": None,
              "state": "Active",
              "telemetryConfiguration": None,
              "snmpConfiguration": None,
              "qosConfiguration": None},
             'lig2':
             {'name': 'LIG-COMP-OU2',
                 'type': 'logical-interconnect-groupV6',
                 'enclosureType': 'C7000',
                 'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC Flex-10/10D Module'}],
                 "internalNetworkUris": [],
                 "uplinkSets": [],
                 "stackingMode": "Enclosure",
                 "ethernetSettings": None,
                 "state": "Active",
                 "telemetryConfiguration": None,
                 "snmpConfiguration": None,
                 "qosConfiguration": None}
             }

edit_eg1 = {'name': 'config1-group_2',
            'interconnectBayMappings':
                [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:LIG-COMP-OU1'},
                 {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                 {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG-COMP-OU2'},
                 {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                 {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                 {'interconnectBay': 6, 'logicalInterconnectGroupUri': None},
                 {'interconnectBay': 7, 'logicalInterconnectGroupUri': None},
                 {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}],
            'ipRangeUris': [],
            'enclosureCount': 1,
            'osDeploymentSettings': None,
            'configurationScript': None,
            'powerMode': None,
            'ambientTemperatureMode': 'Standard'}


edit_lig2 = {'lig1':
             {'name': 'LIG-COMP-OU1',
              'type': 'logical-interconnect-groupV6',
              'enclosureType': 'C7000',
              'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                                          {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric-20/40 F8 Module'}],
              "internalNetworkUris": [],
              "uplinkSets": [],
              "stackingMode": "Enclosure",
              "ethernetSettings": None,
              "state": "Active",
              "telemetryConfiguration": None,
              "snmpConfiguration": None,
              "qosConfiguration": None},
             'lig2':
             {'name': 'LIG-COMP-OU2',
                 'type': 'logical-interconnect-groupV6',
                 'enclosureType': 'C7000',
                 'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC Flex-10/10D Module'},
                                             {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC Flex-10/10D Module'}],
                 "internalNetworkUris": [],
                 "uplinkSets": [],
                 "stackingMode": "Enclosure",
                 "ethernetSettings": None,
                 "state": "Active",
                 "telemetryConfiguration": None,
                 "snmpConfiguration": None,
                 "qosConfiguration": None}
             }

edit_eg2 = {'name': 'config1-group_3',
            'interconnectBayMappings':
                [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:LIG-COMP-OU1'},
                 {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:LIG-COMP-OU1'},
                 {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG-COMP-OU2'},
                 {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:LIG-COMP-OU2'},
                 {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                 {'interconnectBay': 6, 'logicalInterconnectGroupUri': None},
                 {'interconnectBay': 7, 'logicalInterconnectGroupUri': None},
                 {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}],
            'ipRangeUris': [],
            'enclosureCount': 1,
            'osDeploymentSettings': None,
            'configurationScript': None,
            'powerMode': None,
            'ambientTemperatureMode': 'Standard'}

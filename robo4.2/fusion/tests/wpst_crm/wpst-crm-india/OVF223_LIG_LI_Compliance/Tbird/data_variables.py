import os
import sys
import paramiko
import os.path
import tarfile
import time
import re
import string

cwd = os.getcwd()
download_to_path = cwd


def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist


def convert_unicode_to_string(String):
    res = String.encode('utf-8')
    return res


def include_thousand_sep(str1):
    res = format(str1, ',')
    return res


def replace_string(string1, str):
    str = string.replace(string1, 'XXX', str)
    return str


def replace_multi_string(string1, count, str):
    str = string.replace(string1, count, str)
    return str

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}
ENC_1 = '0000A66101'
ENC_2 = '0000A66102'
ENC_3 = '0000A66103'
System_Contact = 'Administrator'
IC_Configured = 'Configured'
Expected_Consistency_Status = 'CONSISTENT'
Expected_Non_Consistency_Status = 'NOT_CONSISTENT'
Non_Reduntant_A = 'NonRedundantASide'
Non_Reduntant_B = 'NonRedundantBSide'
Uplinkset_A = 'US_A'
Uplinkset_B = 'US_B'
LIGname = 'LIG1'
LIG_A = 'LIGA'
LIG_B = 'LIGB'
frame = 3
enc_list = ['ENC:' + ENC_1, 'ENC:' + ENC_2, 'ENC:' + ENC_3]
Public = 'public'
Sample_interval = 400
Sample_interval_2 = 500
Snmp_True = True
Snmp_False = False
None_Value = None
Qos_Enable = True
Qos_Disable = False
Igmp_enable = True
Igmp_disable = False
IC_Configured = 'Configured'
Expected_Consistency_Status = 'CONSISTENT'
Expected_Non_Consistency_Status = 'NOT_CONSISTENT'
Non_Reduntant_A = 'NonRedundantASide'
Non_Reduntant_B = 'NonRedundantBSide'
Interconnect_1 = '0000A66101, interconnect 3'
Interconnect_2 = '0000A66102, interconnect 6'
Fibrechannel = 'FibreChannel'
Us_name = 'US1'
Us_Rename = 'US_Renamed'
relative_value = '72'
Internal_networks = []
SNMP_Access_add = ['192.168.0.1/24']
SNMP_Access_edit = ['192.168.0.2/24']
Compliance_list = ['uplinkSets', 'snmp']
Multi_one_Compliance_list = ['qualityOfService', 'snmp', 'uplinkSets']
Multi_two_Compliance_list = ['interconnectSettings', 'utilizationSampling', 'internalNetworks']
Multi_three_compliance_list = ['qualityOfService', 'snmp', 'uplinkSets', 'interconnectSettings', 'utilizationSampling', 'internalNetworks', 'sFlow']
Multi_three_compliance_list_switch = ['qualityOfService', 'snmp', 'uplinkSets', 'interconnectSettings', 'utilizationSampling', 'internalNetworks', 'switchMap']
Multi_count = ['1', '2', '3']

Snmpuser_add_1 = [{'snmpV3UserName': 'User1', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'}]
Snmpuser_add_2 = [{'snmpV3UserName': 'User2', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'}]
Snmpuser_add_3 = [{'snmpV3UserName': 'User3', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'}]
Snmpuser_Edit_Auth_Credentials = [{'snmpV3UserName': 'User2', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'}, {'snmpV3UserName': 'User3', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password1234', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'}]

TrapDestinations_1 = [{'trapDestination': '10.10.0.1', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'User1', 'inform':False, 'communityString':'', 'port':'162'}]
TrapDestinations_2 = [{'trapDestination': '10.10.0.2', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'User2', 'inform':False, 'communityString':'', 'port':'162'}]
TrapDestinations_3 = [{'trapDestination': '10.10.0.3', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'User3', 'inform':False, 'communityString':'', 'port':'162'}]

TrapDestinations = [{'trapDestination': '10.10.0.2', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'User2', 'inform':False, 'communityString':'', 'port':'162', 'engineId':None},
                    {'trapDestination': '10.10.0.3', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'User3', 'inform':False, 'communityString':'', 'port':'162', 'engineId':None}]


Enc3MapBaysetA = [{'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
                  {'bay': 3, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
                  {'bay': 3, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3}
                  ]

Enc3MapBaysetB = [{'bay': 6, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
                  {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
                  {'bay': 6, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3}
                  ]

icmap_ME_Multi_LIG1 = [
    {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy'},
    {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'Synergy 20Gb Interconnect Link Module'},
    {'enclosure': 2, 'enclosureIndex': 2, 'bay': 6, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy'},
    {'enclosure': 2, 'enclosureIndex': 2, 'bay': 3, 'type': 'Synergy 20Gb Interconnect Link Module'},
    {'enclosure': 3, 'enclosureIndex': 3, 'bay': 6, 'type': 'Synergy 20Gb Interconnect Link Module'},
    {'enclosure': 3, 'enclosureIndex': 3, 'bay': 3, 'type': 'Synergy 20Gb Interconnect Link Module'}
]
Alert = ['Active', 'Locked']
Consistency_State = ['CONSISTENT', 'NOT_CONSISTENT']
edit_li_with_internal_network = {'snmpConfiguration':
                                 {'type': 'snmp-configuration',
                                  'readCommunity': 'public',

                                  'snmpUsers': [],
                                  'systemContact': 'None',
                                  'v3Enabled': True,
                                  'trapDestinations': [],
                                  'snmpAccess': [],
                                  'enabled': False,
                                  'category': 'snmp-configuration',
                                  'uri': None}}
COMPLAINCE_ALERT = 'The logical interconnect is inconsistent with the logical interconnect group ' + LIGname
netwrks = []
varTrue = True
varFalse = False

logicalPortConfigInfos = [{'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 62}, {'type': 'Enclosure', 'relativeValue': 1}]}}]
logicalPortConfigInfos_2 = [{'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 67}, {'type': 'Enclosure', 'relativeValue': 1}]}}]
logicalPortConfigInfos_LI = [{'desiredSpeed': 'Auto', 'location': {'locationEntries': [{'type': 'Bay', 'value': 3}, {'type': 'Port', 'value': 'Q1:1'}, {'type': 'Enclosure', 'value': '/rest/enclosures/0000000000A66101'}]}}]
logicalPortConfigInfos_2_LI = [{'desiredSpeed': 'Auto', 'location': {'locationEntries': [{'type': 'Bay', 'value': 3}, {'type': 'Port', 'value': 'Q3:1'}, {'type': 'Enclosure', 'value': '/rest/enclosures/0000000000A66101'}]}}]
logicalport = []

icmap_SE_Multi_LIG1 = [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy'},
                       {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy'}

                       ]

enet_name = 'Net_5'
enet_name_prev = 'Net_1'
ethnets = [{'name': 'Net_5',
            'vlanId': '10',
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged',
                      'type': 'ethernet-networkV4'}]
key = 'If-Match'
value = '*'
ligs_tbird_SE_Multi_LIG_All_Users = {'name': 'LIG1',
                                     'type': 'logical-interconnect-groupV5',
                                     'enclosureType': 'SY12000',
                                     'enclosureIndexes': [1, 2, 3],
                                     'interconnectMapTemplate': icmap_SE_Multi_LIG1,
                                     'uplinkSets': [],
                                     'interconnectBaySet': 3,
                                     'redundancyType': 'HighlyAvailable',
                                     'ethernetSettings': None,
                                     'state': 'Active',
                                     'telemetryConfiguration': None,
                                     'snmpConfiguration': None}

ligs_tbird_SE_Multi_LIG_All_Users_1 = {'name': 'LIG1',
                                       'type': 'logical-interconnect-groupV5',
                                       'enclosureType': 'SY12000',
                                       'enclosureIndexes': [1, 2, 3],
                                       'interconnectMapTemplate': icmap_SE_Multi_LIG1,
                                       'uplinkSets': [],
                                       'interconnectBaySet': 3,
                                       'redundancyType': 'HighlyAvailable',
                                       'ethernetSettings': None,
                                       'state': 'Active',
                                       'telemetryConfiguration': None,
                                       'snmpConfiguration': None}

Edit_Lig_Snmpv1_v2 = {'type': 'logical-interconnect-groupV5',
                      'uplinkSets': [],
                      'telemetryConfiguration': None,
                      'snmpConfiguration': {'type': 'snmp-configuration',
                                            'uri': None,
                                            'category': 'snmp-configuration',
                                            'eTag': None,
                                            'created': None,
                                            'modified': None,
                                            'enabled': False,
                                            'v3Enabled': True,
                                            'systemContact': '',
                                            'readCommunity': '',
                                            'snmpUsers': [],
                                            'trapDestinations': [],
                                            'snmpAccess': [],
                                            'description': None,
                                            'name': None,
                                            'state': None,
                                            'status': None},
                      'enclosureType': 'SY12000',
                      'qosConfiguration': None,
                      'interconnectMapTemplate': None,
                      'enclosureIndexes': [1, 2, 3],
                      'fabricUri': None,
                      'interconnectBaySet': 3,
                      'redundancyType': 'HighlyAvailable',
                      'ethernetSettings': None,
                      'internalNetworkUris': [],
                      'stackingHealth': None,
                      'stackingMode': None,
                      'scopesUri': None,
                      'description': None,
                      'name': 'LIG1',
                      'state': 'Active',
                      'status': None,
                      'created': '',
                      'eTag': '',
                      'modified': '',
                      'category': 'logical-interconnect-groups',
                      'uri': ''}

SNMP_Config = {'type': 'snmp-configuration',
               'readCommunity': 'public',
               'systemContact': '',
               'v3Enabled': True,
               'snmpUsers': [],
               'trapDestinations': [],
               'snmpAccess': [],
               'enabled': False,
               'description': None,
               'name': None,
               'state': None,
               'status': None,
               'created': None,
               'modified': None,
               'eTag': None,
               'category': 'snmp-configuration',
               'uri': None}

edit_Li_snmpv1_v2_Enabled = {'snmpConfiguration': {'type': 'snmp-configuration',
                                                   'readCommunity': 'None',
                                                   'systemContact': 'Administrator',
                                                   'v3Enabled': True,
                                                   'snmpUsers': [{'snmpV3UserName': 'User2', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'}, {'snmpV3UserName': 'User3', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password1234', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'}],
                                                   'trapDestinations': [{'trapDestination': '10.10.0.3', 'trapFormat': 'SNMPv3', 'trapSeverities': ["Critical"], 'vcmTrapCategories':["Legacy"], 'enetTrapCategories':["Other"], 'fcTrapCategories':["Other"], 'userName':'User3', 'inform':False, 'communityString':'', 'port':'162'},
                                                                        {'trapDestination': '10.10.0.2', 'trapFormat': 'SNMPv3', 'trapSeverities': ["Critical"], 'vcmTrapCategories':["Legacy"], 'enetTrapCategories':["Other"], 'fcTrapCategories':["Other"], 'userName':'User2', 'inform':False, 'communityString':'', 'port':'162'}],
                                                   'snmpAccess': [],
                                                   'enabled': True,
                                                   'description': None,
                                                   'category': 'snmp-configuration',
                                                   'uri': None}
                             }


edit_Li_snmpv1_v2_Enabled_tbird = {'snmpConfiguration': {'type': 'snmp-configuration',
                                                         'readCommunity': 'None',
                                                         'systemContact': '',
                                                         'v3Enabled': True,
                                                         'snmpUsers': [],
                                                         'trapDestinations': [],
                                                         'snmpAccess': [],
                                                         'enabled': True,
                                                         'description': None,
                                                         'category': 'snmp-configuration',
                                                         'uri': None}
                                   }

edit_Li_snmpv1_v2_Disabled_tbird = {'snmpConfiguration': {'type': 'snmp-configuration',
                                                          'readCommunity': '',
                                                          'systemContact': '',
                                                          'v3Enabled': True,
                                                          'snmpUsers': [],
                                                          'trapDestinations': [],
                                                          'snmpAccess': [],
                                                          'enabled': False,
                                                          'description': None,
                                                          'category': 'snmp-configuration',
                                                          'uri': None}
                                    }

edit_Li_snmp_config = {'type': 'snmp-configuration',
                       'readCommunity': '',
                       'systemContact': '',
                       'v3Enabled': True,
                       'snmpUsers': [],
                       'trapDestinations': [],
                       'snmpAccess': [],
                       'enabled': False,
                       'description': None,
                       'category': 'snmp-configuration',
                       'uri': None}

Delete_Li_snmp_user = {'type': 'snmp-configuration',
                       'readCommunity': '',
                       'systemContact': '',
                       'v3Enabled': True,
                       'snmpUsers': [{'snmpV3UserName': 'User2', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'}],
                       'trapDestinations': [{'trapDestination': '10.10.0.2', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'User2', 'inform':False, 'communityString':'', 'port':'162'}],
                       'snmpAccess': [],
                       'enabled': False,
                       'description': None,
                       'category': 'snmp-configuration',
                       'uri': None}

Snmp_V1_V2 = {'type': 'snmp-configuration',
              'uri': None,
              'category': 'snmp-configuration',
              'eTag': None,
              'created': None,
              'modified': None,
              'enabled': False,
              'v3Enabled': True,
              'systemContact': '',
              'readCommunity': '',
              'snmpUsers': [],
              'trapDestinations': [],
              'snmpAccess': [],
              'description': None,
              'name': None,
              'state': None,
              'status': None}

ligs = {'LIG1':
        {'name': 'LIG',
                 'type': 'logical-interconnect-groupV5',
                 'enclosureType': 'SY12000',
                 'interconnectMapTemplate': icmap_SE_Multi_LIG1,
                 'enclosureIndexes': [1, 2, 3],
                 'interconnectBaySet': 3,
                 'redundancyType': 'HighlyAvailable',
                 'uplinkSets': [],
                 'ethernetSettings': [{'type': 'EthernetInterconnectSettingsV4', 'interconnectType': 'Ethernet', 'enablePauseFloodProtection': True, 'enableIgmpSnooping': False, 'igmpIdleTimeoutInterval': 260, 'enableFastMacCacheFailover': True, 'macRefreshInterval': 5, 'enableNetworkLoopProtection': True, 'enableTaggedLldp': False, 'enableRichTLV': False}],
                 'ethernetSettings': None,
                 'state': 'Active',
                 'telemetryConfiguration': None,
                 'snmpConfiguration': None},
        'lig1':
        {'name': 'LIG',
                 'type': 'logical-interconnect-groupV5',
                 'enclosureType': 'SY12000',
                 'interconnectMapTemplate': icmap_SE_Multi_LIG1,
                 'enclosureIndexes': [1, 2, 3],
                 'interconnectBaySet': 3,
                 'redundancyType': 'HighlyAvailable',
                 'internalNetworkUris': ['net1'],
                 'uplinkSets': [],
                 'ethernetSettings': None,
                 'state': 'Active',
                 'telemetryConfiguration': None,
                 'snmpConfiguration': None},

        'lig2':
        {'name': 'LIG',
                 'type': 'logical-interconnect-groupV5',
                 'enclosureType': 'SY12000',
                 'interconnectMapTemplate': icmap_SE_Multi_LIG1,
                 'enclosureIndexes': [1, 2, 3],
                 'interconnectBaySet': 3,
                 'redundancyType': 'HighlyAvailable',
                 'internalNetworkUris': ['Net1', 'Net2'],
                 'uplinkSets': [],
                 'ethernetSettings': None,
                 'state': 'Active',
                 'telemetryConfiguration': None,
                 'snmpConfiguration': None, },
        'lig3':
        {'name': 'LIG',
                 'type': 'logical-interconnect-groupV5',
                 'enclosureType': 'SY12000',
                 'interconnectMapTemplate': icmap_SE_Multi_LIG1,
                 'enclosureIndexes': [1, 2, 3],
                 'interconnectBaySet': 3,
                 'redundancyType': 'HighlyAvailable',
                 'internalNetworkUris': [],
                 'uplinkSets': [],
                 'ethernetSettings': None,
                 'state': 'Active',
                 'telemetryConfiguration': None,
                 'snmpConfiguration': None},

        }

lig_body2_tbird = {'type': 'logical-interconnect-groupV5',
                   'uplinkSets': [],
                   'telemetryConfiguration': None,
                   'snmpConfiguration': None,
                   'enclosureType': 'SY12000',
                   'qosConfiguration': None,
                   'interconnectMapTemplate': None,
                   'enclosureIndexes': [1, 2, 3],
                   'fabricUri': None,
                   'interconnectBaySet': 3,
                   'redundancyType': 'HighlyAvailable',
                   'ethernetSettings': None,
                   'internalNetworkUris': [],
                   'stackingHealth': None,
                   'stackingMode': None,
                   'scopesUri': None,
                   'description': None,
                   'name': 'LIG1',
                   'state': 'Active',
                   'status': None,
                   'created': '',
                   'eTag': '',
                   'modified': '',
                   'category': 'logical-interconnect-groups',
                   'uri': ''}

lig_body1_tbird = {'type': 'logical-interconnect-groupV5',
                   'uri': '',
                   'category': 'logical-interconnect-groups',
                   'eTag': '',
                   'created': '',
                   'modified': '',
                   'scopesUri': '',
                   'uplinkSets': [],
                   'interconnectMapTemplate': None,
                   'stackingMode': None,
                   'stackingHealth': None,
                   'ethernetSettings': {'type': 'EthernetInterconnectSettingsV4',
                                        'uri': '',
                                        'category': None,
                                        'eTag': None,
                                        'created': '2017-12-10T02:55:25.936Z',
                                        'modified': '2017-12-12T05:33:37.736Z',
                                        'id': '0e514ac3-2fd7-4cc3-8fb6-a6fe1ad7f6ef',
                                        'name': 'name-647683970-1512874525936',
                                        'interconnectType': 'Ethernet',
                                        'enableIgmpSnooping': False,
                                        'igmpIdleTimeoutInterval': 260,
                                        'igmpSnoopingVlanIds': '',
                                        'enableFastMacCacheFailover': True,
                                        'macRefreshInterval': 5,
                                        'enableNetworkLoopProtection': True,
                                        'dependentResourceUri': '/rest/logical-interconnect-groups/a6c91411-d8bf-42b3-a337-3c833c311f8b',
                                        'enablePauseFloodProtection': True,
                                        'enableRichTLV': False,
                                        'enableTaggedLldp': False,
                                        'lldpIpv4Address': '',
                                        'lldpIpv6Address': '',
                                        'lldpIpAddressMode': 'IPV4',
                                        'enableStormControl': False,
                                        'stormControlThreshold': 0,
                                        'stormControlPollingInterval': 10,
                                        'description': None,
                                        'state': None,
                                        'status': None},
                   'telemetryConfiguration': {'type': 'telemetry-configuration', 'uri': None, 'category': 'telemetry-configuration', 'eTag': None, 'created': '2017-12-12T05:25:50.988Z', 'modified': '2017-12-12T05:25:50.988Z', 'enableTelemetry': True, 'sampleInterval': 300, 'sampleCount': 12, 'description': None, 'state': None, 'status': None, 'name': None},
                   'snmpConfiguration': {'type': 'snmp-configuration', 'uri': None, 'category': 'snmp-configuration', 'eTag': None, 'created': '2017-12-10T02:55:25.940Z', 'modified': '2017-12-10T02:55:25.940Z', 'enabled': False, 'v3Enabled': True, 'systemContact': '', 'readCommunity': '', 'trapDestinations': [], 'snmpAccess': [], 'description': None, 'state': None, 'status': None, 'name': None, 'snmpUsers': []},
                   'enclosureType': 'SY12000',
                   'internalNetworkUris': ['/rest/ethernet-networks/9596efb4-cb27-4b3e-bd33-745842e9d6e1'],
                   'fabricUri': '',
                   'enclosureIndexes': [1, 2, 3],
                   'interconnectBaySet': 3,
                   'redundancyType': 'HighlyAvailable',
                   'qosConfiguration': {'activeQosConfig': {'type': 'QosConfiguration', 'uri': None, 'category': 'qos-aggregated-configuration', 'eTag': None, 'created': None, 'modified': None, 'configType': 'Passthrough', 'uplinkClassificationType': None, 'downlinkClassificationType': None, 'qosTrafficClassifiers': None, 'description': None, 'state': None, 'status': None, 'name': None}, 'inactiveFCoEQosConfig': None, 'inactiveNonFCoEQosConfig': None, 'type': 'qos-aggregated-configuration', 'name': None, 'state': None, 'status': None, 'eTag': None, 'modified': None, 'created': None, 'category': 'qos-aggregated-configuration', 'uri': None},
                   'description': None, 'state': 'Active', 'status': None, 'name': 'LIG1'}

ligs_tbird_SE_Multi_LIG = {'snmpConfiguration':

                           {'type': 'snmp-configuration', 'snmpUsers': [{'snmpV3UserName': 'User1', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'NA'},
                                                                        {'snmpV3UserName': 'User2', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA384', 'v3PrivacyProtocol': 'AES128'},
                                                                        {'snmpV3UserName': 'User3', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA512', 'v3PrivacyProtocol': 'AES192'},
                                                                        {'snmpV3UserName': 'User4', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES256'},
                                                                        {'snmpV3UserName': 'User5', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'TDEA'},
                                                                        {'snmpV3UserName': 'User6', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA512', 'v3PrivacyProtocol': 'TDEA'},
                                                                        {'snmpV3UserName': 'User7', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'}],
                            'readCommunity': 'public',
                            'systemContact': '',
                            'trapDestinations': [],
                            'snmpAccess': [],
                            'v3Enabled': True,
                            'enabled': False,
                            'description': None,
                            'name': None,
                            'state': None,
                            'status': None,
                            'eTag': None,
                            'category': 'snmp-configuration',
                            'uri': None

                            }
                           }

LIGS_TB_Non_Redundant_A = {'name': 'LIGA',
                           'type': 'logical-interconnect-groupV5',
                           'enclosureType': 'SY12000',
                           "ethernetSettings": {"type": "EthernetInterconnectSettingsV4", "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "enableTaggedLldp": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
                           'uplinkSets': [],
                           'interconnectMapTemplate': Enc3MapBaysetA,
                           'internalNetworkUris': [],
                           'interconnectBaySet': 3,
                           'redundancyType': 'NonRedundantASide',
                           'enclosureIndexes': [1, 2, 3],
                           'qosConfiguration': {'activeQosConfig': {'type': 'QosConfiguration', 'configType': 'Passthrough', 'downlinkClassificationType': None, 'uplinkClassificationType': None, 'qosTrafficClassifiers': None, 'description': None, 'status': None, 'name': None, 'state': None, 'category': 'qos-aggregated-configuration', 'created': None, 'modified': None, 'eTag': None, 'uri': None}, 'inactiveFCoEQosConfig': None, 'inactiveNonFCoEQosConfig': None, 'type': 'qos-aggregated-configuration', 'name': None, 'state': None, 'status': None, 'eTag': None, 'modified': None, 'created': None, 'category': 'qos-aggregated-configuration', 'uri': None}
                           }

LIGS_TB_Non_Redundant_B = {'name': 'LIGB',
                           'type': 'logical-interconnect-groupV5',
                           'enclosureType': 'SY12000',
                           "ethernetSettings": {"type": "EthernetInterconnectSettingsV4", "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "enableTaggedLldp": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
                           'uplinkSets': [],
                           'interconnectMapTemplate': Enc3MapBaysetB,
                           'internalNetworkUris': [],
                           'interconnectBaySet': 3,
                           'redundancyType': 'NonRedundantBSide',
                           'enclosureIndexes': [1, 2, 3],
                           'qosConfiguration': {'activeQosConfig': {'type': 'QosConfiguration', 'configType': 'Passthrough', 'downlinkClassificationType': None, 'uplinkClassificationType': None, 'qosTrafficClassifiers': None, 'description': None, 'status': None, 'name': None, 'state': None, 'category': 'qos-aggregated-configuration', 'created': None, 'modified': None, 'eTag': None, 'uri': None}, 'inactiveFCoEQosConfig': None, 'inactiveNonFCoEQosConfig': None, 'type': 'qos-aggregated-configuration', 'name': None, 'state': None, 'status': None, 'eTag': None, 'modified': None, 'created': None, 'category': 'qos-aggregated-configuration', 'uri': None}
                           }


Enc_group = [{'name': 'EG1',
              'interconnectBayMappings': [{'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
                                          {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG1'}],
              'ipAddressingMode': 'DHCP',
              'ipRangeUris': None,
              'enclosureCount': 3,
              'osDeploymentSettings': {'manageOSDeployment': False, 'deploymentModeSettings': {'deploymentMode': 'None', 'deploymentNetworkUri': None}},
              'powerMode': 'RedundantPowerFeed'}]

Edit_Enc_group = {"type": "EnclosureGroupV7",
                  "uri": None,
                  "category": "enclosure-groups",
                  "name": "EG1",
                  "created": None,
                  "modified": None,
                  "eTag": None,
                  "status": "OK",
                  "state": "Normal",
                  "enclosureTypeUri": "/rest/enclosure-types/SY12000",
                  "stackingMode": "Enclosure",
                  "portMappingCount": 8,
                  "portMappings": [{"midplanePort": 1, "interconnectBay": 1}, {"midplanePort": 2, "interconnectBay": 2}, {"midplanePort": 3, "interconnectBay": 3}, {"midplanePort": 4, "interconnectBay": 4}, {"midplanePort": 5, "interconnectBay": 5}, {"midplanePort": 6, "interconnectBay": 6}, {"midplanePort": 7, "interconnectBay": 7}, {"midplanePort": 8, "interconnectBay": 8}], "interconnectBayMappingCount": 2,
                  "interconnectBayMappings": [{'interconnectBay': 3, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': 'LIG:LIGA'},
                                              {'interconnectBay': 3, 'enclosureIndex': 2, 'logicalInterconnectGroupUri': 'LIG:LIGA'},
                                              {'interconnectBay': 3, 'enclosureIndex': 3, 'logicalInterconnectGroupUri': 'LIG:LIGA'},
                                              {'interconnectBay': 6, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': 'LIG:LIGB'},
                                              {'interconnectBay': 6, 'enclosureIndex': 2, 'logicalInterconnectGroupUri': 'LIG:LIGB'},
                                              {'interconnectBay': 6, 'enclosureIndex': 3, 'logicalInterconnectGroupUri': 'LIG:LIGB'}], "ipAddressingMode": "DHCP", "ipRangeUris": [], "powerMode": "RedundantPowerFeed", "description": None, "osDeploymentSettings": {"manageOSDeployment": False,
                                                                                                                                                                                                                                                                       "deploymentModeSettings": {"deploymentMode": "None",
                                                                                                                                                                                                                                                                                                  "deploymentNetworkUri": None}},
                  "ambientTemperatureMode": "Standard",
                  "enclosureCount": 3,
                  "associatedLogicalInterconnectGroups": ["/rest/logical-interconnect-groups/a6c91411-d8bf-42b3-a337-3c833c311f8b"],
                  "scopesUri": "/rest/scopes/resources/rest/enclosure-groups/6b3ab430-813e-4aa2-9b76-dd37a031d470", "configurationScript": "",
                  "enclosureType": "TClass"}


LIG_INTERNAL = 'LIG1'
LIG_New = 'LIG_New'
timeandlocale = {'type': 'TimeAndLocale', 'dateTime': None, 'timezone': 'UTC', 'ntpServers': ['ntp.hpecorp.net'], 'locale': 'en_US.UTF-8'}

uplink_sets = {'us1': {'name': 'us1',
                       'ethernetNetworkType': 'Tunnel',
                       'networkType': 'Ethernet',
                       'networkUris': ['eth-100'],
                       'primaryPort': None,
                       'nativeNetworkUri': None,
                       'mode': 'Auto',
                       'logicalPortConfigInfos': [{'bay': '1', 'port': 'X1', 'speed': 'Auto'},
                                                  {'bay': '1', 'port': 'X2', 'speed': 'Auto'},
                                                  ]},
               'us2': {'name': 'us2',
                       'ethernetNetworkType': 'Tunnel',
                       'networkType': 'Ethernet',
                       'networkUris': ['eth-101'],
                       'primaryPort': None,
                       'nativeNetworkUri': None,
                       'mode': 'Auto',
                       'logicalPortConfigInfos': [{'bay': '2', 'port': 'X1', 'speed': 'Auto'},
                                                  {'bay': '2', 'port': 'X2', 'speed': 'Auto'},
                                                  ]},

               'us12': {'name': 'US',
                        'ethernetNetworkType': 'Tagged',
                        'networkType': 'Ethernet',
                        'networkUris': ['Net_1'],
                        'nativeNetworkUri': None,
                        'logicalPortConfigInfos': []}
               }


ligs_tbird_SE_Multi_LIG_All_Users_uplink = {'name': 'LIG1',
                                            'type': 'logical-interconnect-groupV5',
                                            'enclosureType': 'SY12000',
                                            'enclosureIndexes': [1, 2, 3],
                                            'interconnectMapTemplate': icmap_ME_Multi_LIG1,
                                            'uplinkSets': [uplink_sets['us12']],
                                            'interconnectBaySet': 3,
                                            'redundancyType': 'HighlyAvailable',
                                            'ethernetSettings': None,
                                            'state': 'Active',
                                            'telemetryConfiguration': None,
                                            'snmpConfiguration': None}


icmap_SE_Multi_LIG = [
    {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy'},
    {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'Synergy 20Gb Interconnect Link Module'},
    {'enclosure': 2, 'enclosureIndex': 2, 'bay': 6, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy'},
    {'enclosure': 2, 'enclosureIndex': 2, 'bay': 3, 'type': 'Synergy 20Gb Interconnect Link Module'}
]

icmap_ME_Multi_LIG = [
    {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy'},
    {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'Synergy 20Gb Interconnect Link Module'},
    {'enclosure': 2, 'enclosureIndex': 2, 'bay': 6, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy'},
    {'enclosure': 2, 'enclosureIndex': 2, 'bay': 3, 'type': 'Synergy 20Gb Interconnect Link Module'},
    {'enclosure': 3, 'enclosureIndex': 3, 'bay': 6, 'type': 'Synergy 20Gb Interconnect Link Module'},
    {'enclosure': 3, 'enclosureIndex': 3, 'bay': 3, 'type': 'Synergy 20Gb Interconnect Link Module'}
]

icmap_ME_Multi_LIG_chnage = [
    {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy'},
    {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'Synergy 10Gb Interconnect Link Module'},
    {'enclosure': 2, 'enclosureIndex': 2, 'bay': 6, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy'},
    {'enclosure': 2, 'enclosureIndex': 2, 'bay': 3, 'type': 'Synergy 10Gb Interconnect Link Module'},
    {'enclosure': 3, 'enclosureIndex': 3, 'bay': 3, 'type': 'Synergy 10Gb Interconnect Link Module'},
    {'enclosure': 3, 'enclosureIndex': 3, 'bay': 6, 'type': 'Synergy 10Gb Interconnect Link Module'}
]

Enc1MapBayset3 = [
    {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
    {'bay': 6, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
    {'bay': 3, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
    {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
    {'bay': 3, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3},
    {'bay': 6, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3}
]
ethernet_networks = [{'name': 'Vlan10',
                      'type': 'ethernet-networkV4',
                      'vlanId': 10,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'}]

Ethernet = [{
    'vlanId': 10,
    'purpose': 'General',
    'name': 'Net_1',
    'smartLink': True,
    'privateNetwork': False,
    'connectionTemplateUri': None,
    'ethernetNetworkType': 'Tagged',
    'type': 'ethernet-networkV4'},
    {
    'vlanId': 15,
    'purpose': 'General',
    'name': 'Net_2',
    'smartLink': True,
    'privateNetwork': False,
    'ethernetNetworkType': 'Tagged',
    'connectionTemplateUri': None,
    'type': 'ethernet-networkV4'},
    {
    'vlanId': 20,
    'purpose': 'General',
    'name': 'Net_3',
    'smartLink': True,
    'privateNetwork': False,
    'connectionTemplateUri': None,
    'ethernetNetworkType': 'Tagged',
    'type': 'ethernet-networkV4'},
    {
    'vlanId': 40,
    'purpose': 'General',
    'name': 'Net_4',
    'smartLink': True,
    'privateNetwork': False,
    'connectionTemplateUri': None,
    'ethernetNetworkType': 'Tagged',
    'type': 'ethernet-networkV4'},
    {'name': 'Vlan10',
     'type': 'ethernet-networkV4',
     'vlanId': 10,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged'}]

Logical_Enclosure = [{'name': 'LE',
                      'enclosureUris': enc_list[0:frame],
                      'enclosureGroupUri': 'EG:EG1',
                      'firmwareBaselineUri': None,
                      'forceInstallFirmware': False}]


LIGS_TB = {'ligsup': [{'name': 'LIG1',
                       'type': 'logical-interconnect-groupV5',
                       'enclosureType': 'SY12000',
                       'interconnectMapTemplate': icmap_ME_Multi_LIG,
                       'enclosureIndexes': [1, 2],
                       'interconnectBaySet': 3,
                       'redundancyType': 'HighlyAvailable',
                       'uplinkSets': [],
                       'internalNetworkUris':[],
                       'ethernetSettings': None,
                       'state': 'Active',
                       'telemetryConfiguration': None,
                       'snmpConfiguration': None}]}


Enet_1 = [{
    'vlanId': 10,
    'purpose': 'General',
    'name': 'Vlan10',
    'smartLink': True,
    'privateNetwork': True,
    'ethernetNetworkType': 'Tagged',
    'connectionTemplateUri': None,
    'type': 'ethernet-networkV4'}]

uplink_sets = {'us1_1': {'name': 'upset1',
                         'ethernetNetworkType': 'Tagged',
                         'networkType': 'Ethernet',
                         'networkUris': ['Vlan10'],
                         'nativeNetworkUri': None,
                         'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q1.1', 'speed': 'Auto'}, {'enclosure': '1', 'bay': '6', 'port': 'Q1.1', 'speed': 'Auto'}]
                         },
               'us1': {'name': 'upset1',
                       'ethernetNetworkType': 'Tagged',
                       'networkType': 'Ethernet',
                       'networkUris': ['Net_1'],
                       'nativeNetworkUri': None,
                       'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q1.1', 'speed': 'Auto'}, {'enclosure': '1', 'bay': '3', 'port': 'Q2.1', 'speed': 'Auto'}, {'enclosure': '2', 'bay': '6', 'port': 'Q1.1', 'speed': 'Auto'}, {'enclosure': '2', 'bay': '6', 'port': 'Q2.1', 'speed': 'Auto'}]
                       },

               }

edit_ligs_tbird_switch = {'lig_E_IGMP':
                          {'name': 'LIG1',
                           'type': 'logical-interconnect-groupV5',
                           'enclosureType': 'SY12000',
                           'interconnectMapTemplate': icmap_ME_Multi_LIG_chnage,
                           'enclosureIndexes': [1, 2, 3],
                           'interconnectBaySet': 3,
                           'redundancyType': 'HighlyAvailable',
                           'uplinkSets': [],
                           'ethernetSettings': None,
                              'state': 'Active',
                              'telemetryConfiguration': None,
                              'snmpConfiguration': None}}

edit_ligs_tbird_disable_US = {'ligDU':
                              {'name': 'LIG1',
                               'type': 'logical-interconnect-groupV5',
                               'enclosureType': 'SY12000',
                               'interconnectMapTemplate': icmap_ME_Multi_LIG,
                               'enclosureIndexes': [1, 2, 3],
                               'interconnectBaySet': 3,
                               'redundancyType': 'HighlyAvailable',
                               'uplinkSets': [],
                               'ethernetSettings': None,
                               'state': 'Active',
                               'telemetryConfiguration': {'type': 'telemetry-configuration', 'sampleCount': 12, 'sampleInterval': 300, 'enableTelemetry': False, 'category': 'telemetry-configuration'},
                               'snmpConfiguration': None}}

edit_ligs_tbird_enable_US_interval = {'ligEU':
                                      {'name': 'LIG1',
                                       'type': 'logical-interconnect-groupV5',
                                       'enclosureType': 'SY12000',
                                       'interconnectMapTemplate': icmap_ME_Multi_LIG,
                                       'enclosureIndexes': [1, 2, 3],
                                       'interconnectBaySet': 3,
                                       'redundancyType': 'HighlyAvailable',
                                       'uplinkSets': [],
                                       'ethernetSettings': None,
                                       'state': 'Active',
                                       'telemetryConfiguration': {'type': 'telemetry-configuration', 'sampleCount': 16, 'sampleInterval': 306, 'enableTelemetry': True, 'category': 'telemetry-configuration'},
                                       'snmpConfiguration': None}}

edit_ligs_tbird_enable_US = {'ligEU':
                             {'name': 'LIG1',
                              'type': 'logical-interconnect-groupV5',
                              'enclosureType': 'SY12000',
                              'interconnectMapTemplate': icmap_ME_Multi_LIG,
                              'enclosureIndexes': [1, 2, 3],
                              'interconnectBaySet': 3,
                              'redundancyType': 'HighlyAvailable',
                              'uplinkSets': [],
                              'ethernetSettings': None,
                              'state': 'Active',
                              'telemetryConfiguration': {'type': 'telemetry-configuration', 'sampleCount': 12, 'sampleInterval': 300, 'enableTelemetry': True, 'category': 'telemetry-configuration'},
                              'snmpConfiguration': None}}


edit_ligs_tbird_enable_Igmp = {'lig_E_IGMP':
                               {'name': 'LIG1',
                                'type': 'logical-interconnect-groupV5',
                                'enclosureType': 'SY12000',
                                'interconnectMapTemplate': icmap_ME_Multi_LIG,
                                'enclosureIndexes': [1, 2, 3],
                                'interconnectBaySet': 3,
                                'redundancyType': 'HighlyAvailable',
                                'uplinkSets': [uplink_sets['us1'].copy()],
                                'ethernetSettings': {'type': 'EthernetInterconnectSettingsV4', 'enableIgmpSnooping': True, 'interconnectType': 'Ethernet'},
                                'state': 'Active',
                                'telemetryConfiguration': None,
                                'snmpConfiguration': None}}

edit_ligs_tbird_disable_Igmp = {'lig_D_IGMP':
                                {'name': 'LIG1',
                                 'type': 'logical-interconnect-groupV5',
                                 'enclosureType': 'SY12000',
                                 'interconnectMapTemplate': icmap_ME_Multi_LIG,
                                 'enclosureIndexes': [1, 2, 3],
                                 'interconnectBaySet': 3,
                                 'redundancyType': 'HighlyAvailable',
                                 'uplinkSets': [uplink_sets['us1'].copy()],
                                 'ethernetSettings': {'type': 'EthernetInterconnectSettingsV4', 'enableIgmpSnooping': False, 'interconnectType': 'Ethernet', 'enableTaggedLldp': False, 'enableStormControl': False},
                                 'state': 'Active',
                                 'telemetryConfiguration': None,
                                 'snmpConfiguration': None}}


edit_ligs_tbird_enable_vlan_Igmp = {'lig_E_vlan_IGMP':
                                    {'name': 'LIG1',
                                     'type': 'logical-interconnect-groupV5',
                                     'enclosureType': 'SY12000',
                                     'interconnectMapTemplate': icmap_ME_Multi_LIG,
                                     'enclosureIndexes': [1, 2, 3],
                                     'interconnectBaySet': 3,
                                     'redundancyType': 'HighlyAvailable',
                                     'uplinkSets': [uplink_sets['us1'].copy()],
                                     'ethernetSettings': {'type': 'EthernetInterconnectSettingsV4', 'enableIgmpSnooping': True, 'igmpSnoopingVlanIds': 10, 'igmpIdleTimeoutInterval': 260, 'enableTaggedLldp': False, 'enableStormControl': False, 'lldpIpAddressMode': 'IPV4', 'interconnectType': 'Ethernet'},
                                     'state': 'Active',
                                     'telemetryConfiguration': None,
                                     'snmpConfiguration': None}}

edit_ligs_tbird_enable_Igmp_lldp = {'lig_E_IGMP_LLDP':
                                    {'name': 'LIG1',
                                     'type': 'logical-interconnect-groupV5',
                                     'enclosureType': 'SY12000',
                                     'interconnectMapTemplate': icmap_ME_Multi_LIG,
                                     'enclosureIndexes': [1, 2, 3],
                                     'interconnectBaySet': 3,
                                     'redundancyType': 'HighlyAvailable',
                                     'uplinkSets': [uplink_sets['us1'].copy()],
                                     'ethernetSettings': {'type': 'EthernetInterconnectSettingsV4', 'enableIgmpSnooping': True, 'igmpIdleTimeoutInterval': 261, 'enableTaggedLldp': True, 'enableStormControl': True, 'stormControlThreshold': 10, 'stormControlPollingInterval': 10, 'lldpIpAddressMode': 'IPV4', 'interconnectType': 'Ethernet'},
                                     'state': 'Active',
                                     'telemetryConfiguration': None,
                                     'snmpConfiguration': None}}

edit_ligs_tbird_enable_Igmp_lldp_Dis_storm_loop = {'lig_E_IGMP_LLDP_D_storm_loop':
                                                   {'name': 'LIG1',
                                                    'type': 'logical-interconnect-groupV5',
                                                    'enclosureType': 'SY12000',
                                                    'interconnectMapTemplate': icmap_ME_Multi_LIG,
                                                    'enclosureIndexes': [1, 2, 3],
                                                       'interconnectBaySet': 3,
                                                       'redundancyType': 'HighlyAvailable',
                                                       'uplinkSets': [uplink_sets['us1'].copy()],
                                                    'ethernetSettings': {'type': 'EthernetInterconnectSettingsV4', 'enableIgmpSnooping': True, 'igmpIdleTimeoutInterval': 260, 'enableNetworkLoopProtection': False, 'enableTaggedLldp': True, 'enableStormControl': False, 'lldpIpAddressMode': 'IPV4', 'enablePauseFloodProtection': True, 'interconnectType': 'Ethernet'},
                                                       'state': 'Active',
                                                       'telemetryConfiguration': None,
                                                       'snmpConfiguration': None}}

edit_ligs_tbird_disable_Igmp_lldp_enable_storm_loop = {'lig_D_IGMP_LLDP_E_storm_loop':
                                                       {'name': 'LIG1',
                                                        'type': 'logical-interconnect-groupV5',
                                                        'enclosureType': 'SY12000',
                                                        'interconnectMapTemplate': icmap_ME_Multi_LIG,
                                                        'enclosureIndexes': [1, 2, 3],
                                                           'interconnectBaySet': 3,
                                                           'redundancyType': 'HighlyAvailable',
                                                           'uplinkSets': [uplink_sets['us1'].copy()],
                                                        'ethernetSettings': {'type': 'EthernetInterconnectSettingsV4', 'enableIgmpSnooping': False, 'igmpIdleTimeoutInterval': 261, 'enableNetworkLoopProtection': True, 'enableTaggedLldp': False, 'enableStormControl': True, 'stormControlThreshold': 10, 'stormControlPollingInterval': 10, 'enablePauseFloodProtection': False, 'lldpIpAddressMode': 'IPV6', 'interconnectType': 'Ethernet'},
                                                           'state': 'Active',
                                                           'telemetryConfiguration': None,
                                                           'snmpConfiguration': None}}


edit_ligs_tbird_enableVlan_Igmp_lldpIPV6 = {'lig_EVlan_IGMP_LLDPV6':
                                            {'name': 'LIG1',
                                             'type': 'logical-interconnect-groupV5',
                                             'enclosureType': 'SY12000',
                                             'interconnectMapTemplate': icmap_ME_Multi_LIG,
                                             'enclosureIndexes': [1, 2, 3],
                                             'interconnectBaySet': 3,
                                             'redundancyType': 'HighlyAvailable',
                                             'uplinkSets': [uplink_sets['us1'].copy()],
                                             'ethernetSettings': {'type': 'EthernetInterconnectSettingsV4', 'enableIgmpSnooping': True, 'igmpSnoopingVlanIds': 10, 'igmpIdleTimeoutInterval': 261, 'enableTaggedLldp': True, 'enableStormControl': True, 'stormControlThreshold': 10, 'stormControlPollingInterval': 10, 'lldpIpAddressMode': 'IPV6', 'interconnectType': 'Ethernet'},
                                                'state': 'Active',
                                                'telemetryConfiguration': None,
                                                'snmpConfiguration': None}}


li_enable_igmp = {'type': 'EthernetInterconnectSettingsV4', 'enableIgmpSnooping': True, 'enableTaggedLldp': False, 'enableStormControl': False, 'lldpIpAddressMode': 'IPV4', 'interconnectType': 'Ethernet'}

li_disable_igmp = {'type': 'EthernetInterconnectSettingsV4', 'enableIgmpSnooping': False, 'enableTaggedLldp': False, 'enableStormControl': False, 'lldpIpAddressMode': 'IPV4', 'interconnectType': 'Ethernet'}

li_enable_Vlan_igmp = {'type': 'EthernetInterconnectSettingsV4', 'enableIgmpSnooping': True, 'igmpSnoopingVlanIds': 10, 'igmpIdleTimeoutInterval': 260, 'enableTaggedLldp': False, 'enableStormControl': False, 'lldpIpAddressMode': 'IPV4', 'interconnectType': 'Ethernet'}

li_enable_lldp_storm_igmp = {'type': 'EthernetInterconnectSettingsV4', 'enableIgmpSnooping': True, 'igmpIdleTimeoutInterval': 261, 'enableTaggedLldp': True, 'enableStormControl': True, 'stormControlThreshold': 10, 'stormControlPollingInterval': 10, 'lldpIpAddressMode': 'IPV4', 'interconnectType': 'Ethernet'}

li_enable_vlan_lldp_storm_ipv6 = {'type': 'EthernetInterconnectSettingsV4', 'enableIgmpSnooping': True, 'igmpSnoopingVlanIds': 10, 'igmpIdleTimeoutInterval': 261, 'enableTaggedLldp': True, 'enableStormControl': True, 'stormControlThreshold': 10, 'stormControlPollingInterval': 10, 'lldpIpAddressMode': 'IPV6', 'interconnectType': 'Ethernet'}

li_D_IGMP_LLDP_E_storm_loop = {'type': 'EthernetInterconnectSettingsV4', 'enableIgmpSnooping': False, 'igmpIdleTimeoutInterval': 261, 'enableNetworkLoopProtection': True, 'enableTaggedLldp': False, 'enableStormControl': True, 'stormControlThreshold': 10, 'stormControlPollingInterval': 10, 'enablePauseFloodProtection': False, 'lldpIpAddressMode': 'IPV6', 'interconnectType': 'Ethernet'}

li_E_IGMP_LLDP_D_storm_loop = {'type': 'EthernetInterconnectSettingsV4', 'enableIgmpSnooping': True, 'igmpIdleTimeoutInterval': 260, 'enableNetworkLoopProtection': False, 'enableTaggedLldp': True, 'enableStormControl': False, 'lldpIpAddressMode': 'IPV4', 'enablePauseFloodProtection': True, 'interconnectType': 'Ethernet'}

li_Tel_F = {'type': 'telemetry-configuration',
            'enableTelemetry': False,
            'sampleInterval': 300, 'sampleCount': 12}

li_Tel_T = {'type': 'telemetry-configuration',
            'enableTelemetry': True,
            'sampleInterval': 302, 'sampleCount': 14}

li_Tel_T_def = {'type': 'telemetry-configuration',
                'enableTelemetry': True,
                'sampleInterval': 300, 'sampleCount': 12}

li_Tel_T_changeInt = {'type': 'telemetry-configuration',
                      'enableTelemetry': True,
                      'sampleInterval': 306, 'sampleCount': 16}

US_valT = 'True'
US_valF = 'False'

LE = 'LE'
LIG_1 = 'LIG1'
IGMP_valT = 'True'
IGMP_valF = 'False'

CustomNoFcoe = 'CustomNoFCoE'
DOT1P = 'DOT1P'
DSCP = 'DSCP'
DOT1P_DSCP = 'DOT1P_AND_DSCP'
IC_Configured = 'Configured'
Expected_Consistency_Status = 'CONSISTENT'
Expected_Non_Consistency_Status = 'NOT_CONSISTENT'
Class_Name_msg = ['"Class1"', '"Class2"', '"Class3"', '"Class4"', '"Class5"', '"Best effort"', '"FCoE lossless"', '"Medium"', '"Real time"']
Class_Name = ['Class1', 'Class2', 'Class3', 'Class4', 'Class5', 'Medium', 'Real time']
Medium = 'Medium'
Real_time = 'Real time'
Fcoe_lossless = 'FCoE lossless'
Bestefforts = 'Best effort'
Band_Width_qos = 'bandwidthShare'
Class_Name_qos = 'className'
Egress_Dot1p_Value_qos = 'egressDot1pValue'
Enabled_qos = 'enabled'
Max_Band_qos = 'maxBandwidth'
Real_Time_qos = 'realTime'
Best_Effort = 74
Share = 30
Medium_share = 55
Real_time_share = 40
All_traffic_share = 5
All_traffic_band = 70
Total_band = 35
Dot1p_value = 1
egressDot1p_value = 2
egressDot1p_value_realtime = 5
Dot1p_effort = '3'
Default_total_band = '65'


LIGS_TB_HA = {'name': 'LIG1',
              'type': 'logical-interconnect-groupV5',
              'enclosureType': 'SY12000',
              'interconnectMapTemplate': Enc1MapBayset3,
              'enclosureIndexes': [1, 2, 3],
              'interconnectBaySet': 3,
              'redundancyType': 'HighlyAvailable',
              'uplinkSets': [],
              'internalNetworkUris': [],
              'ethernetSettings': None,
              'state': 'Active',
                       'telemetryConfiguration': None,
                       'snmpConfiguration': None}

Edit_Lig = {'type': 'logical-interconnect-groupV5',
            'uplinkSets': [{'networkUris': [''],
                            'mode':'Auto',
                            'lacpTimer':'Short',
                            'primaryPort':None,
                            'logicalPortConfigInfos':[],
                            'networkType':'Ethernet',
                            'ethernetNetworkType':'Tagged',
                            'nativeNetworkUri':None,
                            'name':'US'}],
            'telemetryConfiguration': None,
            'snmpConfiguration': {'type': 'snmp-configuration',
                                  'uri': None,
                                  'category': 'snmp-configuration',
                                  'eTag': None,
                                  'created': None,
                                  'modified': None,
                                  'enabled': False,
                                  'v3Enabled': True,
                                  'systemContact': '',
                                  'readCommunity': '',
                                  'snmpUsers': [],
                                  'trapDestinations': [],
                                  'snmpAccess': [],
                                  'description': None,
                                  'name': None,
                                  'state': None,
                                  'status': None},
            'enclosureType': 'SY12000',
            'qosConfiguration': None,
            'interconnectMapTemplate': None,
            'enclosureIndexes': [1, 2, 3],
            'fabricUri': '/rest/fabrics/04f3e40f-5a46-4676-aac0-5847030a2f3f',
            'interconnectBaySet': 3,
            'redundancyType': 'HighlyAvailable',
            'ethernetSettings': None,
            'internalNetworkUris': [],
            'stackingHealth': None,
            'stackingMode': None,
            'scopesUri': '',
            'description': None,
            'name': 'LIG1',
            'state': 'Active',
            'status': None,
            'created': '',
            'eTag': '',
            'modified': '',
            'category': 'logical-interconnect-groups',
            'uri': ''}

Qos_config = {'type': 'logical-interconnect-groupV5',
              'uplinkSets': [],
              'telemetryConfiguration': None,
              'snmpConfiguration': {'type': 'snmp-configuration',
                                    'uri': None,
                                    'category': 'snmp-configuration',
                                    'eTag': None,
                                    'created': None,
                                    'modified': None,
                                    'enabled': False,
                                    'v3Enabled': True,
                                    'systemContact': '',
                                    'readCommunity': '',
                                    'snmpUsers': [],
                                    'trapDestinations': [],
                                    'snmpAccess': [],
                                    'description': None,
                                    'name': None,
                                    'state': None,
                                    'status': None},
              'enclosureType': 'SY12000',
              'qosConfiguration': None,
              'interconnectMapTemplate': None,
              'enclosureIndexes': [1, 2, 3],
              'fabricUri': None,
              'interconnectBaySet': 3,
              'redundancyType': 'HighlyAvailable',
              'ethernetSettings': None,
              'internalNetworkUris': [],
              'stackingHealth': None,
              'stackingMode': None,
              'scopesUri': None,
              'description': None,
              'name': 'LIG1',
              'state': 'Active',
              'status': None,
              'created': '',
              'eTag': '',
              'modified': '',
              'category': 'logical-interconnect-groups',
              'uri': ''}

Qos_NoFcoe = {'activeQosConfig': {'type': 'QosConfiguration',
                                  'uri': None,
                                  'category': 'qos-aggregated-configuration',
                                  'eTag': None,
                                  'created': None,
                                  'modified': None,
                                  'configType': 'CustomNoFCoE',
                                  'uplinkClassificationType': 'DOT1P',
                                  'downlinkClassificationType': 'DOT1P_AND_DSCP',
                                  'qosTrafficClassifiers': [{'qosTrafficClass': {'className': 'Best effort',
                                                                                 'realTime': False,
                                                                                 'bandwidthShare': '65',
                                                                                 'maxBandwidth': 100,
                                                                                 'enabled': True,
                                                                                 'egressDot1pValue': 0},
                                                                'qosClassificationMapping': {'dot1pClassMapping': [1, 0],
                                                                                             'dscpClassMapping':['DSCP 10, AF11', 'DSCP 12, AF12', 'DSCP 14, AF13', 'DSCP 8, CS1', 'DSCP 0, CS0']}},
                                                            {'qosTrafficClass': {'className': 'Class1',
                                                                                 'realTime': False,
                                                                                 'bandwidthShare': '0',
                                                                                 'maxBandwidth': 100,
                                                                                 'enabled': False, 'egressDot1pValue': 0},
                                                             'qosClassificationMapping': None},
                                                            {'qosTrafficClass': {'className': 'Class2',
                                                                                 'realTime': False,
                                                                                 'bandwidthShare': '0',
                                                                                 'maxBandwidth': 100,
                                                                                 'enabled': False,
                                                                                 'egressDot1pValue': 0},
                                                             'qosClassificationMapping': None},
                                                            {'qosTrafficClass': {'className': 'Class3',
                                                                                 'realTime': False,
                                                                                 'bandwidthShare': '0',
                                                                                 'maxBandwidth': 100,
                                                                                 'enabled': False,
                                                                                 'egressDot1pValue': 0},
                                                             'qosClassificationMapping': None},
                                                            {'qosTrafficClass': {'className': 'Class4',
                                                                                 'realTime': False,
                                                                                 'bandwidthShare': '0',
                                                                                 'maxBandwidth': 100,
                                                                                 'enabled': False,
                                                                                 'egressDot1pValue': 0},
                                                             'qosClassificationMapping': None},
                                                            {'qosTrafficClass': {'className': 'Class5',
                                                                                 'realTime': False,
                                                                                 'bandwidthShare': '0',
                                                                                 'maxBandwidth': 100,
                                                                                 'enabled': False,
                                                                                 'egressDot1pValue': 0},
                                                             'qosClassificationMapping': None},
                                                            {'qosTrafficClass': {'className': 'Medium',
                                                                                 'realTime': False,
                                                                                 'bandwidthShare': '25',
                                                                                 'maxBandwidth': 100,
                                                                                 'enabled': True,
                                                                                 'egressDot1pValue': 2},
                                                             'qosClassificationMapping': {'dot1pClassMapping': [4, 3, 2], 'dscpClassMapping':['DSCP 18, AF21', 'DSCP 20, AF22', 'DSCP 22, AF23', 'DSCP 26, AF31', 'DSCP 28, AF32', 'DSCP 30, AF33', 'DSCP 34, AF41', 'DSCP 36, AF42', 'DSCP 38, AF43', 'DSCP 16, CS2', 'DSCP 24, CS3', 'DSCP 32, CS4']}},
                                                            {'qosTrafficClass': {'className': 'Real time',
                                                                                 'realTime': True,
                                                                                 'bandwidthShare': '10',
                                                                                 'maxBandwidth': 10,
                                                                                 'enabled': True,
                                                                                 'egressDot1pValue': 5},
                                                             'qosClassificationMapping': {'dot1pClassMapping': [5, 6, 7], 'dscpClassMapping':['DSCP 46, EF', 'DSCP 40, CS5', 'DSCP 48, CS6', 'DSCP 56, CS7']}}],
                                  'description': None,
                                  'name': None,
                                  'state': None,
                                  'status': None},
              'inactiveFCoEQosConfig': None,
              'inactiveNonFCoEQosConfig': None,
              'type': 'qos-aggregated-configuration',
              'name': None,
              'state': None,
              'status': None,
              'eTag': None,
              'modified': None,
              'created': None,
              'category': 'qos-aggregated-configuration', 'uri': None}

Qos_classifiers = [{'qosTrafficClass': {'className': 'Best effort',
                                        'realTime': False,
                                        'bandwidthShare': '70',
                                        'maxBandwidth': 74, 'enabled': True,
                                        'egressDot1pValue': 0},
                    'qosClassificationMapping': {'dot1pClassMapping': [1, 0],
                                                 'dscpClassMapping':['DSCP 10, AF11', 'DSCP 12, AF12', 'DSCP 14, AF13', 'DSCP 8, CS1', 'DSCP 0, CS0']}},
                   {'qosTrafficClass': {'className': 'Class1',
                                        'realTime': False,
                                        'bandwidthShare': '5',
                                        'maxBandwidth': 100,
                                        'enabled': True,
                                        'egressDot1pValue': 1},
                    'qosClassificationMapping': None},
                   {'qosTrafficClass': {'className': 'Class2',
                                        'realTime': False,
                                        'bandwidthShare': '5',
                                        'maxBandwidth': 100,
                                        'enabled': True,
                                        'egressDot1pValue': 2},
                    'qosClassificationMapping': None},
                   {'qosTrafficClass': {'className': 'Class3',
                                        'realTime': False,
                                        'bandwidthShare': '5',
                                        'maxBandwidth': 100,
                                        'enabled': True, 'egressDot1pValue': 3},
                    'qosClassificationMapping': None},
                   {'qosTrafficClass': {'className': 'Class4',
                                        'realTime': False,
                                        'bandwidthShare': '5',
                                        'maxBandwidth': 100,
                                        'enabled': True,
                                        'egressDot1pValue': 4},
                    'qosClassificationMapping': None},
                   {'qosTrafficClass': {'className': 'FCoE lossless',
                                        'realTime': False,
                                        'bandwidthShare': 'Share is based on the profile configuration connection',
                                        'maxBandwidth': 100,
                                        'enabled': True,
                                        'egressDot1pValue': 5},
                    'qosClassificationMapping': {'dot1pClassMapping': [3], 'dscpClassMapping':[]}},
                   {'qosTrafficClass': {'className': 'Medium',
                                        'realTime': False,
                                        'bandwidthShare': '5',
                                        'maxBandwidth': 100,
                                        'enabled': True,
                                        'egressDot1pValue': 6},
                    'qosClassificationMapping': {'dot1pClassMapping': [4, 3, 2], 'dscpClassMapping':['DSCP 18, AF21', 'DSCP 20, AF22', 'DSCP 22, AF23', 'DSCP 26, AF31', 'DSCP 28, AF32', 'DSCP 30, AF33', 'DSCP 34, AF41', 'DSCP 36, AF42', 'DSCP 38, AF43', 'DSCP 16, CS2', 'DSCP 24, CS3', 'DSCP 32, CS4']}},
                   {'qosTrafficClass': {'className': 'Real time',
                                        'realTime': True,
                                        'bandwidthShare': '5',
                                        'maxBandwidth': 5,
                                        'enabled': True,
                                        'egressDot1pValue': 7},
                    'qosClassificationMapping': {'dot1pClassMapping': [5, 6, 7], 'dscpClassMapping':['DSCP 46, EF', 'DSCP 40, CS5', 'DSCP 48, CS6', 'DSCP 56, CS7']}}]
Qos_classifiers_wofcoe = [{'qosTrafficClass': {'className': 'Best effort',
                                               'realTime': False,
                                               'bandwidthShare': '65',
                                               'maxBandwidth': 74, 'enabled': True,
                                               'egressDot1pValue': 0},
                           'qosClassificationMapping': {'dot1pClassMapping': [1, 0],
                                                        'dscpClassMapping':['DSCP 10, AF11', 'DSCP 12, AF12', 'DSCP 14, AF13', 'DSCP 8, CS1', 'DSCP 0, CS0']}},
                          {'qosTrafficClass': {'className': 'Class1',
                                               'realTime': False,
                                               'bandwidthShare': '5',
                                               'maxBandwidth': 100,
                                               'enabled': True,
                                               'egressDot1pValue': 1},
                           'qosClassificationMapping': None},
                          {'qosTrafficClass': {'className': 'Class2',
                                               'realTime': False,
                                               'bandwidthShare': '5',
                                               'maxBandwidth': 100,
                                               'enabled': True,
                                               'egressDot1pValue': 2},
                           'qosClassificationMapping': None},
                          {'qosTrafficClass': {'className': 'Class3',
                                               'realTime': False,
                                               'bandwidthShare': '5',
                                               'maxBandwidth': 100,
                                               'enabled': True, 'egressDot1pValue': 3},
                           'qosClassificationMapping': None},
                          {'qosTrafficClass': {'className': 'Class4',
                                               'realTime': False,
                                               'bandwidthShare': '5',
                                               'maxBandwidth': 100,
                                               'enabled': True,
                                               'egressDot1pValue': 4},
                           'qosClassificationMapping': None},
                          {'qosTrafficClass': {'className': 'Class5',
                                               'realTime': False,
                                               'bandwidthShare': '5',
                                               'maxBandwidth': 100,
                                               'enabled': True,
                                               'egressDot1pValue': 5},
                           'qosClassificationMapping': None},
                          {'qosTrafficClass': {'className': 'Medium',
                                               'realTime': False,
                                               'bandwidthShare': '5',
                                               'maxBandwidth': 100,
                                               'enabled': True,
                                               'egressDot1pValue': 6},
                           'qosClassificationMapping': {'dot1pClassMapping': [4, 3, 2], 'dscpClassMapping':['DSCP 18, AF21', 'DSCP 20, AF22', 'DSCP 22, AF23', 'DSCP 26, AF31', 'DSCP 28, AF32', 'DSCP 30, AF33', 'DSCP 34, AF41', 'DSCP 36, AF42', 'DSCP 38, AF43', 'DSCP 16, CS2', 'DSCP 24, CS3', 'DSCP 32, CS4']}},
                          {'qosTrafficClass': {'className': 'Real time',
                                               'realTime': True,
                                               'bandwidthShare': '5',
                                               'maxBandwidth': 5,
                                               'enabled': True,
                                               'egressDot1pValue': 7},
                           'qosClassificationMapping': {'dot1pClassMapping': [5, 6, 7], 'dscpClassMapping':['DSCP 46, EF', 'DSCP 40, CS5', 'DSCP 48, CS6', 'DSCP 56, CS7']}}]
Class_Value = {'qosTrafficClass': {'className': 'Class5',
                                   'realTime': False,
                                   'bandwidthShare': '5',
                                   'maxBandwidth': 100,
                                   'enabled': True,
                                   'egressDot1pValue': 5},
               'qosClassificationMapping': None}

SNMP_Config_public = {'type': 'snmp-configuration',
                      'readCommunity': 'public',
                      'systemContact': '',
                      'v3Enabled': True,
                      'snmpUsers': [],
                      'trapDestinations': [],
                      'snmpAccess': [],
                      'enabled': False,
                      'description': None,
                      'name': None,
                      'state': None,
                      'status': None,
                      'created': None,
                      'modified': None,
                      'eTag': None,
                      'category': 'snmp-configuration',
                      'uri': None}

Qos_Passthrough = {'activeQosConfig': {'type': 'QosConfiguration',
                                       'uri': None,
                                       'category': 'qos-aggregated-configuration',
                                       'eTag': None,
                                       'created': None,
                                       'modified': None,
                                       'configType': 'Passthrough',
                                       'uplinkClassificationType': None,
                                       'downlinkClassificationType': None,
                                       'qosTrafficClassifiers': None,
                                       'description': None,
                                       'state': None,
                                       'status': None, 'name': None},
                   'inactiveFCoEQosConfig': None,
                   'inactiveNonFCoEQosConfig': None,
                   'type': 'qos-aggregated-configuration',
                   'name': None,
                   'state': None,
                   'status': None,
                   'eTag': None,
                   'modified': None,
                   'created': None,
                   'category': 'qos-aggregated-configuration',
                   'uri': None}

LIGS_TBird = {'name': 'LIG1',
              'type': 'logical-interconnect-groupV5',
              'enclosureType': 'SY12000',
              "ethernetSettings": {"type": "EthernetInterconnectSettingsV4", "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "enableTaggedLldp": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
              'uplinkSets': [],
              'interconnectMapTemplate': [{'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
                                          {'bay': 6, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
                                          {'bay': 3, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
                                          {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
                                          {'bay': 3, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3},
                                          {'bay': 6, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3}],
              'internalNetworkUris': [],
              'interconnectBaySet': 3,
              'redundancyType': 'HighlyAvailable',
              'enclosureIndexes': [1, 2, 3],
              'qosConfiguration': {'activeQosConfig': {'type': 'QosConfiguration', 'configType': 'Passthrough', 'downlinkClassificationType': None, 'uplinkClassificationType': None, 'qosTrafficClassifiers': None, 'description': None, 'status': None, 'name': None, 'state': None, 'category': 'qos-aggregated-configuration', 'created': None, 'modified': None, 'eTag': None, 'uri': None}, 'inactiveFCoEQosConfig': None, 'inactiveNonFCoEQosConfig': None, 'type': 'qos-aggregated-configuration', 'name': None, 'state': None, 'status': None, 'eTag': None, 'modified': None, 'created': None, 'category': 'qos-aggregated-configuration', 'uri': None}
              }


Logiacl_Enclosure_Tbird = {'name': 'LE', 'enclosureUris': ['ENC:0000A66101', 'ENC:0000A66102', 'ENC:0000A66103'], 'enclosureGroupUri': 'EG:EG1', 'firmwareBaselineUri': None,
                           'forceInstallFirmware': False}

LIGS_TB1 = {'name': 'LIG1',
            'type': 'logical-interconnect-groupV4',
            'enclosureType': 'SY12000',
            'interconnectMapTemplate': Enc1MapBayset3,
            'enclosureIndexes': [1, 2, 3],
            'interconnectBaySet': 3,
            'redundancyType': 'HighlyAvaiable',
            'uplinkSets': [],
            'internalNetworkUris': [],
            'ethernetSettings': None,
            'state': 'Active',
            'telemetryConfiguration': None,
            'snmpConfiguration': None}

LIGS_TB = {'name': 'LIG1',
           'type': 'logical-interconnect-groupV5',
           'enclosureType': 'SY12000',
           'interconnectMapTemplate': Enc1MapBayset3,
           'enclosureIndexes': [1, 2, 3],
           'interconnectBaySet': 3,
           'redundancyType': 'HighlyAvaiable',
           'uplinkSets': [],
           'internalNetworkUris': [],
           'ethernetSettings': None,
           'state': 'Active',
           'telemetryConfiguration': None,
           'snmpConfiguration': None}


Edit_Lig = {'type': 'logical-interconnect-groupV5',
            'uri': '',
            'category': 'logical-interconnect-groups',
            'eTag': '',
            'created': '',
            'modified': '',
            'scopesUri': '',
            'uplinkSets': [{'networkUris': [''],
                            'mode':'Auto',
                            'lacpTimer':'Short',
                            'primaryPort':None,
                            'logicalPortConfigInfos':[],
                            'networkType':'Ethernet',
                            'ethernetNetworkType':'Tagged',
                            'nativeNetworkUri':None,
                            'name':'US'}],
            'interconnectMapTemplate': None,
            'stackingMode': None,
            'stackingHealth': None,
            'ethernetSettings': {'type': 'EthernetInterconnectSettingsV4', 'uri': '/rest/logical-interconnect-groups/6b6995d9-badd-48ba-a4c2-1a1bee525599/ethernetSettings', 'category': None, 'eTag': None, 'created': '2017-11-29T19:16:52.335Z', 'modified': '2017-12-05T05:01:30.791Z', 'id': '39c58731-998a-4b6b-96ed-b22b7edda937', 'name': 'name-1986346659-1511983012335', 'interconnectType': 'Ethernet', 'enableIgmpSnooping': False, 'igmpIdleTimeoutInterval': 260, 'igmpSnoopingVlanIds': '', 'enableFastMacCacheFailover': True, 'macRefreshInterval': 5, 'enableNetworkLoopProtection': True, 'dependentResourceUri': '/rest/logical-interconnect-groups/6b6995d9-badd-48ba-a4c2-1a1bee525599', 'enablePauseFloodProtection': True, 'enableRichTLV': False, 'enableTaggedLldp': False, 'lldpIpv4Address': '', 'lldpIpv6Address': '', 'lldpIpAddressMode': 'IPV4', 'enableStormControl': False, 'stormControlThreshold': 0, 'stormControlPollingInterval': 10, 'description': None, 'state': None, 'status': None},
            'telemetryConfiguration': {'type': 'telemetry-configuration', 'uri': None, 'category': 'telemetry-configuration', 'eTag': None, 'created': '2017-11-29T19:53:08.450Z', 'modified': '2017-11-29T19:53:08.450Z', 'enableTelemetry': True, 'sampleInterval': 300, 'sampleCount': 12, 'description': None, 'state': None, 'name': None, 'status': None},
            'snmpConfiguration': {'type': 'snmp-configuration', 'uri': None, 'category': 'snmp-configuration', 'eTag': None, 'created': '2017-11-29T19:16:52.339Z', 'modified': '2017-11-29T19:16:52.339Z', 'enabled': False, 'v3Enabled': True, 'systemContact': '', 'readCommunity': '', 'trapDestinations': [], 'snmpAccess': [], 'description': None, 'state': None, 'name': None, 'status': None, 'snmpUsers': []},
            'enclosureType': 'SY12000',
            'internalNetworkUris': [],
            'fabricUri': '/rest/fabrics/d4f3c4ba-b411-4558-824f-6cf1f04c900c',
            'enclosureIndexes': [1, 2, 3],
            'interconnectBaySet': 3,
            'redundancyType': 'HighlyAvailable',
            'qosConfiguration': {'activeQosConfig': {'type': 'QosConfiguration', 'uri': None, 'category': 'qos-aggregated-configuration', 'eTag': None, 'created': None, 'modified': None, 'configType': 'Passthrough', 'uplinkClassificationType': None, 'downlinkClassificationType': None, 'qosTrafficClassifiers': None, 'description': None, 'state': None, 'name': None, 'status': None}, 'inactiveFCoEQosConfig': None, 'inactiveNonFCoEQosConfig': None, 'type': 'qos-aggregated-configuration', 'name': None, 'state': None, 'status': None, 'eTag': None, 'modified': None, 'created': None, 'category': 'qos-aggregated-configuration', 'uri': None},
            'description': None,
            'state': 'Active',
            'name': 'LIG1',
            'status': None}
Edit_Lig_US1 = {'type': 'logical-interconnect-groupV5',
                'uri': '',
                'category': 'logical-interconnect-groups',
                'eTag': '',
                'created': '',
                'modified': '',
                'scopesUri': '',
                'uplinkSets': [{'networkUris': [],
                                'mode':'Auto',
                                'lacpTimer':'Short',
                                'primaryPort':None,
                                'logicalPortConfigInfos':[{'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 62}, {'type': 'Enclosure', 'relativeValue': 1}]}}],
                                'networkType': 'Ethernet',
                                'ethernetNetworkType': 'Tagged',
                                'nativeNetworkUri': None,
                                'name': 'US'},
                               {'networkUris': [],
                                'mode':'Auto',
                                'lacpTimer':'Short',
                                'primaryPort':None,
                                'logicalPortConfigInfos':[{'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 67}, {'type': 'Enclosure', 'relativeValue': 1}]}}],
                                'networkType': 'Ethernet',
                                'ethernetNetworkType': 'Tagged',
                                'nativeNetworkUri': None,
                                'name': 'US1'}],
                'interconnectMapTemplate': None,
                'stackingMode': None,
                'stackingHealth': None,
                'ethernetSettings': {'type': 'EthernetInterconnectSettingsV4', 'uri': '/rest/logical-interconnect-groups/56183c82-a043-456a-89ae-64b682125492/ethernetSettings', 'category': None, 'eTag': None, 'created': '2017-11-29T04:42:10.033Z', 'modified': '2017-11-29T04:42:10.033Z', 'id': '2eedda52-4e10-4a6c-a9c2-28851bfeb724', 'name': 'name1708820585-1511930530033', 'interconnectType': 'Ethernet', 'enableIgmpSnooping': False, 'igmpIdleTimeoutInterval': 260, 'igmpSnoopingVlanIds': '', 'enableFastMacCacheFailover': True, 'macRefreshInterval': 5, 'enableNetworkLoopProtection': True, 'dependentResourceUri': '/rest/logical-interconnect-groups/56183c82-a043-456a-89ae-64b682125492', 'enablePauseFloodProtection': True, 'enableRichTLV': False, 'enableTaggedLldp': False, 'lldpIpv4Address': '', 'lldpIpv6Address': '', 'lldpIpAddressMode': 'IPV4', 'enableStormControl': False, 'stormControlThreshold': 0, 'stormControlPollingInterval': 10, 'description': None, 'state': None, 'status': None},
                'telemetryConfiguration': {'type': 'telemetry-configuration', 'uri': None, 'category': 'telemetry-configuration', 'eTag': None, 'created': '2017-11-29T04:42:10.258Z', 'modified': '2017-11-29T04:42:10.258Z', 'enableTelemetry': True, 'sampleInterval': 300, 'sampleCount': 12, 'description': None, 'state': None, 'status': None, 'name': None},
                'snmpConfiguration': {'type': 'snmp-configuration', 'uri': None, 'category': 'snmp-configuration', 'eTag': None, 'created': '2017-11-29T04:42:10.039Z', 'modified': '2017-11-29T04:42:10.039Z', 'enabled': False, 'v3Enabled': True, 'systemContact': '', 'readCommunity': '', 'trapDestinations': [], 'snmpAccess': [], 'description': None, 'state': None, 'status': None, 'name': None, 'snmpUsers': []},
                'enclosureType': 'SY12000',
                'internalNetworkUris': [],
                'fabricUri': '/rest/fabrics/114f9010-0e04-434e-a6a7-8b4abdc30ed5',
                'enclosureIndexes': [1, 2, 3],
                'interconnectBaySet': 3,
                'redundancyType': 'HighlyAvailable',
                'qosConfiguration': {'activeQosConfig': {'type': 'QosConfiguration', 'uri': None, 'category': 'qos-aggregated-configuration', 'eTag': None, 'created': None, 'modified': None, 'configType': 'Passthrough', 'uplinkClassificationType': None, 'downlinkClassificationType': None, 'qosTrafficClassifiers': None, 'description': None, 'state': None, 'status': None, 'name': None},
                                     'inactiveFCoEQosConfig': None, 'inactiveNonFCoEQosConfig': None, 'type': 'qos-aggregated-configuration', 'name': None, 'state': None, 'status': None, 'eTag': None, 'modified': None, 'created': None, 'category': 'qos-aggregated-configuration', 'uri': None},
                'description': None,
                'state': 'Active',
                'status': None,
                'name': 'LIG1'}

Edit_Lig_US2 = {'type': 'logical-interconnect-groupV5',
                'uri': '',
                'category': 'logical-interconnect-groups',
                'eTag': '32578a1f-ceba-4ee4-a0a7-542fb6ea63c7',
                'created': '2017-11-29T04:42:10.033Z',
                'modified': '2017-11-29T04:42:10.288Z',
                'scopesUri': '',
                'uplinkSets': [{'networkUris': [''],
                                'mode':'Auto',
                                'lacpTimer':'Short',
                                'primaryPort':None,
                                'logicalPortConfigInfos':[{'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 62}, {'type': 'Enclosure', 'relativeValue': 1}]}}],
                                'networkType': 'Ethernet',
                                'ethernetNetworkType': 'Tagged',
                                'nativeNetworkUri': None,
                                'name': 'US'},
                               {'networkUris': [''],
                                'mode':'Auto',
                                'lacpTimer':'Short',
                                'primaryPort':None,
                                'logicalPortConfigInfos':[{'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 67}, {'type': 'Enclosure', 'relativeValue': 1}]}}],
                                'networkType': 'Ethernet',
                                'ethernetNetworkType': 'Tagged',
                                'nativeNetworkUri': None,
                                'name': 'US1'},
                               {'networkUris': [''],
                                'mode':'Auto',
                                'lacpTimer':'Short',
                                'primaryPort':None,
                                'logicalPortConfigInfos':[{'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 77}, {'type': 'Enclosure', 'relativeValue': 1}]}}],
                                'networkType': 'FibreChannel',
                                'ethernetNetworkType': None,
                                'nativeNetworkUri': None,
                                'name': 'US2'}],
                'interconnectMapTemplate': None,
                'stackingMode': None,
                'stackingHealth': None,
                'ethernetSettings': {'type': 'EthernetInterconnectSettingsV4', 'uri': '/rest/logical-interconnect-groups/56183c82-a043-456a-89ae-64b682125492/ethernetSettings', 'category': None, 'eTag': None, 'created': '2017-11-29T04:42:10.033Z', 'modified': '2017-11-29T04:42:10.033Z', 'id': '2eedda52-4e10-4a6c-a9c2-28851bfeb724', 'name': 'name1708820585-1511930530033', 'interconnectType': 'Ethernet', 'enableIgmpSnooping': False, 'igmpIdleTimeoutInterval': 260, 'igmpSnoopingVlanIds': '', 'enableFastMacCacheFailover': True, 'macRefreshInterval': 5, 'enableNetworkLoopProtection': True, 'dependentResourceUri': '/rest/logical-interconnect-groups/56183c82-a043-456a-89ae-64b682125492', 'enablePauseFloodProtection': True, 'enableRichTLV': False, 'enableTaggedLldp': False, 'lldpIpv4Address': '', 'lldpIpv6Address': '', 'lldpIpAddressMode': 'IPV4', 'enableStormControl': False, 'stormControlThreshold': 0, 'stormControlPollingInterval': 10, 'description': None, 'state': None, 'status': None},
                'telemetryConfiguration': {'type': 'telemetry-configuration', 'uri': None, 'category': 'telemetry-configuration', 'eTag': None, 'created': '2017-11-29T04:42:10.258Z', 'modified': '2017-11-29T04:42:10.258Z', 'enableTelemetry': True, 'sampleInterval': 300, 'sampleCount': 12, 'description': None, 'state': None, 'status': None, 'name': None},
                'snmpConfiguration': {'type': 'snmp-configuration', 'uri': None, 'category': 'snmp-configuration', 'eTag': None, 'created': '2017-11-29T04:42:10.039Z', 'modified': '2017-11-29T04:42:10.039Z', 'enabled': False, 'v3Enabled': True, 'systemContact': '', 'readCommunity': '', 'trapDestinations': [], 'snmpAccess': [], 'description': None, 'state': None, 'status': None, 'name': None, 'snmpUsers': []},
                'enclosureType': 'SY12000',
                'internalNetworkUris': [],
                'fabricUri': '/rest/fabrics/114f9010-0e04-434e-a6a7-8b4abdc30ed5',
                'enclosureIndexes': [1, 2, 3],
                'interconnectBaySet': 3,
                'redundancyType': 'HighlyAvailable',
                'qosConfiguration': {'activeQosConfig': {'type': 'QosConfiguration', 'uri': None, 'category': 'qos-aggregated-configuration', 'eTag': None, 'created': None, 'modified': None, 'configType': 'Passthrough', 'uplinkClassificationType': None, 'downlinkClassificationType': None, 'qosTrafficClassifiers': None, 'description': None, 'state': None, 'status': None, 'name': None},
                                     'inactiveFCoEQosConfig': None, 'inactiveNonFCoEQosConfig': None, 'type': 'qos-aggregated-configuration', 'name': None, 'state': None, 'status': None, 'eTag': None, 'modified': None, 'created': None, 'category': 'qos-aggregated-configuration', 'uri': None},
                'description': None,
                'state': 'Active',
                'status': None,
                'name': 'LIG1'}

Edit_Lig_US3 = {'type': 'logical-interconnect-groupV5',
                'uri': '',
                'category': 'logical-interconnect-groups',
                'eTag': '',
                'created': '',
                'modified': '',
                'scopesUri': '',
                'uplinkSets': [{'networkUris': [''],
                                'mode':'Auto',
                                'lacpTimer':'Short',
                                'primaryPort':None,
                                'logicalPortConfigInfos':[],
                                'networkType':'Ethernet',
                                'ethernetNetworkType':'Tagged',
                                'nativeNetworkUri':None,
                                'name':'US'},
                               {'networkUris': [''],
                                'mode':'Auto',
                                'lacpTimer':'Short',
                                'primaryPort':None,
                                'logicalPortConfigInfos':[{'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 67}, {'type': 'Enclosure', 'relativeValue': 1}]}}],
                                'networkType': 'Ethernet',
                                'ethernetNetworkType': 'Tagged',
                                'nativeNetworkUri': None,
                                'name': 'US1'},
                               {'networkUris': [''],
                                'mode':'Auto',
                                'lacpTimer':'Short',
                                'primaryPort':None,
                                'logicalPortConfigInfos':[{'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 77}, {'type': 'Enclosure', 'relativeValue': 1}]}}],
                                'networkType': 'FibreChannel',
                                'ethernetNetworkType': None,
                                'nativeNetworkUri': None,
                                'name': 'US2'},
                               {'networkUris': [''],
                                'mode':'Auto',
                                'lacpTimer':'Short',
                                'primaryPort':None,
                                'logicalPortConfigInfos':[],
                                'networkType':'Ethernet',
                                'ethernetNetworkType':'Tagged',
                                'nativeNetworkUri':None,
                                'name':'US3'}],
                'interconnectMapTemplate': None,
                'stackingMode': None,
                'stackingHealth': None,
                'ethernetSettings': {'type': 'EthernetInterconnectSettingsV4', 'uri': '/rest/logical-interconnect-groups/56183c82-a043-456a-89ae-64b682125492/ethernetSettings', 'category': None, 'eTag': None, 'created': '2017-11-29T04:42:10.033Z', 'modified': '2017-11-29T04:42:10.033Z', 'id': '2eedda52-4e10-4a6c-a9c2-28851bfeb724', 'name': 'name1708820585-1511930530033', 'interconnectType': 'Ethernet', 'enableIgmpSnooping': False, 'igmpIdleTimeoutInterval': 260, 'igmpSnoopingVlanIds': '', 'enableFastMacCacheFailover': True, 'macRefreshInterval': 5, 'enableNetworkLoopProtection': True, 'dependentResourceUri': '/rest/logical-interconnect-groups/56183c82-a043-456a-89ae-64b682125492', 'enablePauseFloodProtection': True, 'enableRichTLV': False, 'enableTaggedLldp': False, 'lldpIpv4Address': '', 'lldpIpv6Address': '', 'lldpIpAddressMode': 'IPV4', 'enableStormControl': False, 'stormControlThreshold': 0, 'stormControlPollingInterval': 10, 'description': None, 'state': None, 'status': None},
                'telemetryConfiguration': {'type': 'telemetry-configuration', 'uri': None, 'category': 'telemetry-configuration', 'eTag': None, 'created': '2017-11-29T04:42:10.258Z', 'modified': '2017-11-29T04:42:10.258Z', 'enableTelemetry': True, 'sampleInterval': 300, 'sampleCount': 12, 'description': None, 'state': None, 'status': None, 'name': None},
                'snmpConfiguration': {'type': 'snmp-configuration', 'uri': None, 'category': 'snmp-configuration', 'eTag': None, 'created': '2017-11-29T04:42:10.039Z', 'modified': '2017-11-29T04:42:10.039Z', 'enabled': False, 'v3Enabled': True, 'systemContact': '', 'readCommunity': '', 'trapDestinations': [], 'snmpAccess': [], 'description': None, 'state': None, 'status': None, 'name': None, 'snmpUsers': []},
                'enclosureType': 'SY12000',
                'internalNetworkUris': [],
                'fabricUri': '/rest/fabrics/114f9010-0e04-434e-a6a7-8b4abdc30ed5',
                'enclosureIndexes': [1, 2, 3],
                'interconnectBaySet': 3,
                'redundancyType': 'HighlyAvailable',
                'qosConfiguration': {'activeQosConfig': {'type': 'QosConfiguration', 'uri': None, 'category': 'qos-aggregated-configuration', 'eTag': None, 'created': None, 'modified': None, 'configType': 'Passthrough', 'uplinkClassificationType': None, 'downlinkClassificationType': None, 'qosTrafficClassifiers': None, 'description': None, 'state': None, 'status': None, 'name': None},
                                     'inactiveFCoEQosConfig': None, 'inactiveNonFCoEQosConfig': None, 'type': 'qos-aggregated-configuration', 'name': None, 'state': None, 'status': None, 'eTag': None, 'modified': None, 'created': None, 'category': 'qos-aggregated-configuration', 'uri': None},
                'description': None,
                'state': 'Active',
                'status': None,
                'name': 'LIG1'}

Edit_Lig_US4_5 = {'type': 'logical-interconnect-groupV5',
                  'uri': '',
                  'category': 'logical-interconnect-groups',
                  'eTag': '',
                  'created': '',
                  'modified': '',
                  'scopesUri': '',
                  'uplinkSets': [{'networkUris': [''],
                                  'mode':'Auto',
                                  'lacpTimer':'Short',
                                  'primaryPort':None,
                                  'logicalPortConfigInfos':[],
                                  'networkType':'Ethernet',
                                  'ethernetNetworkType':'Tagged',
                                  'nativeNetworkUri':None,
                                  'name':'US'},
                                 {'networkUris': [''],
                                  'mode':'Auto',
                                  'lacpTimer':'Short',
                                  'primaryPort':None,
                                  'logicalPortConfigInfos':[{'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 67}, {'type': 'Enclosure', 'relativeValue': 1}]}}],
                                  'networkType': 'Ethernet',
                                  'ethernetNetworkType': 'Tagged',
                                  'nativeNetworkUri': None,
                                  'name': 'US1'},
                                 {'networkUris': [''],
                                  'mode':'Auto',
                                  'lacpTimer':'Short',
                                  'primaryPort':None,
                                  'logicalPortConfigInfos':[{'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 77}, {'type': 'Enclosure', 'relativeValue': 1}]}}],
                                  'networkType': 'FibreChannel',
                                  'ethernetNetworkType': None,
                                  'nativeNetworkUri': None,
                                  'name': 'US2'},
                                 {'networkUris': [''],
                                  'mode':'Auto',
                                  'lacpTimer':'Short',
                                  'primaryPort':None,
                                  'logicalPortConfigInfos':[],
                                  'networkType':'Ethernet',
                                  'ethernetNetworkType':'Tagged',
                                  'nativeNetworkUri':None,
                                  'name':'US3'},
                                 {'networkUris': [''],
                                  'mode':'Auto',
                                  'lacpTimer':'Short',
                                  'primaryPort':None,
                                  'logicalPortConfigInfos':[],
                                  'networkType':'Ethernet',
                                  'ethernetNetworkType':'Tagged',
                                  'nativeNetworkUri':None,
                                  'name':'US4'},
                                 {'networkUris': [''],
                                  'mode':'Auto',
                                  'lacpTimer':'Short',
                                  'primaryPort':None,
                                  'logicalPortConfigInfos':[],
                                  'networkType':'FibreChannel',
                                  'ethernetNetworkType':None,
                                  'nativeNetworkUri':None,
                                  'name':'US5'}],
                  'interconnectMapTemplate': None,
                  'stackingMode': None,
                  'stackingHealth': None,
                  'ethernetSettings': {'type': 'EthernetInterconnectSettingsV4', 'uri': '/rest/logical-interconnect-groups/56183c82-a043-456a-89ae-64b682125492/ethernetSettings', 'category': None, 'eTag': None, 'created': '2017-11-29T04:42:10.033Z', 'modified': '2017-11-29T04:42:10.033Z', 'id': '2eedda52-4e10-4a6c-a9c2-28851bfeb724', 'name': 'name1708820585-1511930530033', 'interconnectType': 'Ethernet', 'enableIgmpSnooping': False, 'igmpIdleTimeoutInterval': 260, 'igmpSnoopingVlanIds': '', 'enableFastMacCacheFailover': True, 'macRefreshInterval': 5, 'enableNetworkLoopProtection': True, 'dependentResourceUri': '/rest/logical-interconnect-groups/56183c82-a043-456a-89ae-64b682125492', 'enablePauseFloodProtection': True, 'enableRichTLV': False, 'enableTaggedLldp': False, 'lldpIpv4Address': '', 'lldpIpv6Address': '', 'lldpIpAddressMode': 'IPV4', 'enableStormControl': False, 'stormControlThreshold': 0, 'stormControlPollingInterval': 10, 'description': None, 'state': None, 'status': None},
                  'telemetryConfiguration': {'type': 'telemetry-configuration', 'uri': None, 'category': 'telemetry-configuration', 'eTag': None, 'created': '2017-11-29T04:42:10.258Z', 'modified': '2017-11-29T04:42:10.258Z', 'enableTelemetry': True, 'sampleInterval': 300, 'sampleCount': 12, 'description': None, 'state': None, 'status': None, 'name': None},
                  'snmpConfiguration': {'type': 'snmp-configuration', 'uri': None, 'category': 'snmp-configuration', 'eTag': None, 'created': '2017-11-29T04:42:10.039Z', 'modified': '2017-11-29T04:42:10.039Z', 'enabled': False, 'v3Enabled': True, 'systemContact': '', 'readCommunity': '', 'trapDestinations': [], 'snmpAccess': [], 'description': None, 'state': None, 'status': None, 'name': None, 'snmpUsers': []},
                  'enclosureType': 'SY12000',
                  'internalNetworkUris': [],
                  'fabricUri': '',
                  'enclosureIndexes': [1, 2, 3],
                  'interconnectBaySet': 3,
                  'redundancyType': 'HighlyAvailable',
                  'qosConfiguration': {'activeQosConfig': {'type': 'QosConfiguration', 'uri': None, 'category': 'qos-aggregated-configuration', 'eTag': None, 'created': None, 'modified': None, 'configType': 'Passthrough', 'uplinkClassificationType': None, 'downlinkClassificationType': None, 'qosTrafficClassifiers': None, 'description': None, 'state': None, 'status': None, 'name': None},
                                       'inactiveFCoEQosConfig': None, 'inactiveNonFCoEQosConfig': None, 'type': 'qos-aggregated-configuration', 'name': None, 'state': None, 'status': None, 'eTag': None, 'modified': None, 'created': None, 'category': 'qos-aggregated-configuration', 'uri': None},
                  'description': None,
                  'state': 'Active',
                  'status': None,
                  'name': 'LIG1'}

Edit_Lig_1 = {'type': 'logical-interconnect-groupV5',
              'uplinkSets': [{'networkUris': [],
                              'mode':'Auto',
                              'lacpTimer':'Short',
                              'primaryPort':None,
                              'logicalPortConfigInfos':[],
                              'networkType':'Ethernet',
                              'ethernetNetworkType':'Tagged',
                              'nativeNetworkUri':None,
                              'name':'US'}],
              'telemetryConfiguration': None,
              'snmpConfiguration': None,
              'enclosureType': 'SY12000',
              'qosConfiguration': None,
              'interconnectMapTemplate': None,
              'enclosureIndexes': [1, 2, 3],
              'fabricUri': '',
              'interconnectBaySet': 3,
              'redundancyType': 'HighlyAvaiable',
              'ethernetSettings': None,
              'internalNetworkUris': [],
              'stackingHealth': None,
              'stackingMode': None,
              'scopesUri': None,
              'description': None,
              'name': 'LIG1',
              'state': 'Active',
              'status': None,
              'created': '',
              'eTag': '',
              'modified': '',
              'category': 'logical-interconnect-groups',
              'uri': ''}

Edit_LI_US = {'type': 'uplink-setV4',
              'name': 'US',
              'networkUris': [],
              'portConfigInfos': [],
              'networkType': 'Ethernet',
              'primaryPortLocation': None,
              'reachability': None,
              'manualLoginRedistributionState': 'NotSupported',
              'logicalInterconnectUri': None,
              'connectionMode': 'Auto',
              'lacpTimer': 'Short',
              'nativeNetworkUri': None,
              'fcNetworkUris': [],
              'fcoeNetworkUris': [],
              'state': None,
              'description': None,
              'status': None,
              'uri': None,
              'category': None,
              'modified': None,
              'created': None,
              'eTag': None,
              'ethernetNetworkType': 'Tagged'}

Edit_LI_US_2 = {'type': 'uplink-setV4',
                'name': 'US1',
                'networkUris': [],
                'portConfigInfos': [],
                'networkType': 'FibreChannel',
                'primaryPortLocation': None,
                'reachability': None,
                'manualLoginRedistributionState': 'Supported',
                'logicalInterconnectUri': None,
                'connectionMode': 'Auto',
                'lacpTimer': 'Short',
                'nativeNetworkUri': None,
                'fcNetworkUris': [],
                'fcoeNetworkUris': [],
                'state': None,
                'description': None,
                'status': None,
                'uri': None,
                'category': None,
                'modified': None,
                'created': None,
                'eTag': None}

Edit_LIG_FC = {'type': 'logical-interconnect-groupV5',
               'uplinkSets': [{'networkUris': [''],
                               'mode':'Auto',
                               'lacpTimer':'Short',
                               'primaryPort':None,
                               'logicalPortConfigInfos':[],
                               'networkType':'Ethernet',
                               'ethernetNetworkType':'Tagged',
                               'nativeNetworkUri':None,
                               'name':'US'},
                              {'networkUris': [''],
                               'mode':'Auto',
                               'lacpTimer':'Short',
                               'primaryPort':None,
                               'logicalPortConfigInfos':[],
                               'networkType':'FibreChannel',
                               'ethernetNetworkType':None,
                               'nativeNetworkUri':None,
                               'name':'US1'}],
               'telemetryConfiguration': None,
               'snmpConfiguration': None,
               'enclosureType': 'SY12000',
               'qosConfiguration': None,
               'interconnectMapTemplate': None,
               'enclosureIndexes': [1, 2, 3],
               'fabricUri': '',
               'interconnectBaySet': 3,
               'redundancyType': 'HighlyAvaiable',
               'ethernetSettings': None,
               'internalNetworkUris': [],
               'stackingHealth': None,
               'stackingMode': None,
               'scopesUri': '',
               'description': None,
               'name': 'LIG1',
               'state': 'Active',
               'status': None,
               'created': '',
               'eTag': '',
               'modified': '',
               'category': 'logical-interconnect-groups',
               'uri': ''}

Edit_Lig_Snmp = {'type': 'logical-interconnect-groupV5',
                 'uplinkSets': [],
                 'telemetryConfiguration': None,
                 'snmpConfiguration': {'type': 'snmp-configuration',
                                       'readCommunity': 'public',
                                       'systemContact': '',
                                       'v3Enabled': False,
                                       'snmpUsers': [],
                                       'trapDestinations': [],
                                       'snmpAccess': [],
                                       'enabled': True,
                                       'description': None,
                                       'status': None,
                                       'name': None,
                                       'state': None,
                                       'eTag': None,
                                       'modified': '',
                                       'created': '',
                                       'category': 'snmp-configuration',
                                       'uri': None},
                 'enclosureType': 'SY12000',
                 'qosConfiguration': None,
                 'interconnectMapTemplate': None,
                 'enclosureIndexes': [1, 2, 3],
                 'fabricUri': None,
                 'interconnectBaySet': 3,
                 'redundancyType': 'HighlyAvaiable',
                 'ethernetSettings': None,
                 'internalNetworkUris': [],
                 'stackingHealth': None,
                 'stackingMode': None,
                 'scopesUri': None,
                 'description': None,
                 'name': 'LIG1',
                 'state': 'Active',
                 'status': None,
                 'created': '',
                 'eTag': '',
                 'modified': '',
                 'category': 'logical-interconnect-groups',
                 'uri': ''}

Enc_group = {'name': 'EG1',
             'configurationScript': None,
             'powerMode': 'HighlyAvaiablePowerFeed',
             'ipAddressingMode': 'DHCP',
             'ipRangeUris': [],
             'enclosureCount': frame,
             'osDeploymentSettings': {'manageOSDeployment': False, 'deploymentModeSettings': {'deploymentMode': 'None', 'deploymentNetworkUri': None}},
             'interconnectBayMappings':
             [{'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG1'}
              ]}

enc_group_Tbird = {'name': 'EG1',
                   'enclosureCount': 3,
                   'interconnectBayMappings': [
                       {'interconnectBay': 3, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': "LIG:LIG1"},
                       {'interconnectBay': 6, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': "LIG:LIG1"},
                       {'interconnectBay': 3, 'enclosureIndex': 2, 'logicalInterconnectGroupUri': "LIG:LIG1"},
                       {'interconnectBay': 6, 'enclosureIndex': 2, 'logicalInterconnectGroupUri': "LIG:LIG1"},
                       {'interconnectBay': 3, 'enclosureIndex': 3, 'logicalInterconnectGroupUri': "LIG:LIG1"},
                       {'interconnectBay': 6, 'enclosureIndex': 3, 'logicalInterconnectGroupUri': "LIG:LIG1"}
                   ],
                   'ipAddressingMode': 'DHCP',
                   'powerMode': 'RedundantPowerFeed'}


Logical_Enclosure = [{'name': LE,
                      'enclosureUris': enc_list[0:frame],
                      'enclosureGroupUri': 'EG:EG1',
                      'firmwareBaselineUri': None,
                      'forceInstallFirmware': False}]

Edit_Lig_no_us = {'type': 'logical-interconnect-groupV5',
                  'uplinkSets': [],
                  'telemetryConfiguration': {'type': 'telemetry-configuration',
                                             'sampleCount': 12,
                                             'sampleInterval': 300,
                                             'enableTelemetry': True,
                                             'category': 'telemetry-configuration'},
                  'snmpConfiguration': {'type': 'snmp-configuration',
                                        'uri': None,
                                        'category': 'snmp-configuration',
                                        'eTag': None,
                                        'created': None,
                                        'modified': None,
                                        'enabled': False,
                                        'v3Enabled': True,
                                        'systemContact': '',
                                        'readCommunity': '',
                                        'snmpUsers': [],
                                        'trapDestinations': [],
                                        'snmpAccess': [],
                                        'description': None,
                                        'name': None,
                                        'state': None,
                                        'status': None},
                  'enclosureType': 'SY12000',
                  'qosConfiguration': None,
                  'interconnectMapTemplate': None,
                  'enclosureIndexes': [1, 2, 3],
                  'fabricUri': '',
                  'interconnectBaySet': 3,
                  'redundancyType': 'HighlyAvailable',
                  'ethernetSettings': {'type': 'EthernetInterconnectSettingsV4',
                                       'enableIgmpSnooping': False,
                                       'igmpSnoopingVlanIds': '',
                                       'interconnectType': 'Ethernet'},
                  'internalNetworkUris': [],
                  'stackingHealth': None,
                  'stackingMode': None,
                  'scopesUri': '',
                  'description': None,
                  'name': 'LIG1',
                  'state': 'Active',
                  'status': None,
                  'created': '',
                  'eTag': '',
                  'modified': '',
                  'category': 'logical-interconnect-groups',
                  'uri': ''}

Edit_Lig = {'type': 'logical-interconnect-groupV5',
            'uplinkSets': [{'networkUris': [''],
                            'mode':'Auto',
                            'lacpTimer':'Short',
                            'primaryPort':None,
                            'logicalPortConfigInfos':[],
                            'networkType':'Ethernet',
                            'ethernetNetworkType':'Tagged',
                            'nativeNetworkUri':None,
                            'name':'US'}],
            'telemetryConfiguration': None,
            'snmpConfiguration': {'type': 'snmp-configuration',
                                  'uri': None,
                                  'category': 'snmp-configuration',
                                  'eTag': None,
                                  'created': None,
                                  'modified': None,
                                  'enabled': False,
                                  'v3Enabled': True,
                                  'systemContact': '',
                                  'readCommunity': '',
                                  'snmpUsers': [],
                                  'trapDestinations': [],
                                  'snmpAccess': [],
                                  'description': None,
                                  'name': None,
                                  'state': None,
                                  'status': None},
            'enclosureType': 'SY12000',
            'qosConfiguration': None,
            'interconnectMapTemplate': None,
            'enclosureIndexes': [1, 2, 3],
            'fabricUri': '',
            'interconnectBaySet': 3,
            'redundancyType': 'HighlyAvailable',
            'ethernetSettings': None,
            'internalNetworkUris': [],
            'stackingHealth': None,
            'stackingMode': None,
            'scopesUri': '',
            'description': None,
            'name': 'LIG1',
            'state': 'Active',
            'status': None,
            'created': '',
            'eTag': '',
            'modified': '',
            'category': 'logical-interconnect-groups',
            'uri': ''}

Qos_Fcoe = {'activeQosConfig': {'type': 'QosConfiguration',
                                'uri': None,
                                'category': 'qos-aggregated-configuration',
                                'eTag': None,
                                'created': None,
                                'modified': None,
                                'configType': 'CustomWithFCoE',
                                'uplinkClassificationType': 'DOT1P',
                                'downlinkClassificationType': 'DOT1P_AND_DSCP',
                                'qosTrafficClassifiers': [{'qosTrafficClass': {'className': 'Best effort',
                                                                               'realTime': False,
                                                                               'bandwidthShare': '65',
                                                                               'maxBandwidth': 100, 'enabled': True,
                                                                               'egressDot1pValue': 0},
                                                           'qosClassificationMapping': {'dot1pClassMapping': [1, 0],
                                                                                        'dscpClassMapping':['DSCP 10, AF11', 'DSCP 12, AF12', 'DSCP 14, AF13', 'DSCP 8, CS1', 'DSCP 0, CS0']}},
                                                          {'qosTrafficClass': {'className': 'Class1',
                                                                               'realTime': False,
                                                                               'bandwidthShare': '0',
                                                                               'maxBandwidth': 100,
                                                                               'enabled': False,
                                                                               'egressDot1pValue': 0},
                                                           'qosClassificationMapping': None},
                                                          {'qosTrafficClass': {'className': 'Class2',
                                                                               'realTime': False,
                                                                               'bandwidthShare': '0',
                                                                               'maxBandwidth': 100,
                                                                               'enabled': False,
                                                                               'egressDot1pValue': 0},
                                                           'qosClassificationMapping': None},
                                                          {'qosTrafficClass': {'className': 'Class3',
                                                                               'realTime': False,
                                                                               'bandwidthShare': '0',
                                                                               'maxBandwidth': 100,
                                                                               'enabled': False, 'egressDot1pValue': 0},
                                                           'qosClassificationMapping': None},
                                                          {'qosTrafficClass': {'className': 'Class4',
                                                                               'realTime': False,
                                                                               'bandwidthShare': '0',
                                                                               'maxBandwidth': 100,
                                                                               'enabled': False,
                                                                               'egressDot1pValue': 0},
                                                           'qosClassificationMapping': None},
                                                          {'qosTrafficClass': {'className': 'FCoE lossless',
                                                                               'realTime': False,
                                                                               'bandwidthShare': 'Share is based on the profile configuration connection',
                                                                               'maxBandwidth': 100,
                                                                               'enabled': True,
                                                                               'egressDot1pValue': 3},
                                                           'qosClassificationMapping': {'dot1pClassMapping': [3], 'dscpClassMapping':[]}},
                                                          {'qosTrafficClass': {'className': 'Medium',
                                                                               'realTime': False,
                                                                               'bandwidthShare': '25',
                                                                               'maxBandwidth': 100,
                                                                               'enabled': True,
                                                                               'egressDot1pValue': 2},
                                                           'qosClassificationMapping': {'dot1pClassMapping': [4, 3, 2], 'dscpClassMapping':['DSCP 18, AF21', 'DSCP 20, AF22', 'DSCP 22, AF23', 'DSCP 26, AF31', 'DSCP 28, AF32', 'DSCP 30, AF33', 'DSCP 34, AF41', 'DSCP 36, AF42', 'DSCP 38, AF43', 'DSCP 16, CS2', 'DSCP 24, CS3', 'DSCP 32, CS4']}},
                                                          {'qosTrafficClass': {'className': 'Real time',
                                                                               'realTime': True,
                                                                               'bandwidthShare': '10',
                                                                               'maxBandwidth': 10,
                                                                               'enabled': True,
                                                                               'egressDot1pValue': 5},
                                                           'qosClassificationMapping': {'dot1pClassMapping': [5, 6, 7], 'dscpClassMapping':['DSCP 46, EF', 'DSCP 40, CS5', 'DSCP 48, CS6', 'DSCP 56, CS7']}}],
                                'description': None,
                                'name': None,
                                'state': None,
                                'status': None},
            'inactiveFCoEQosConfig': None,
            'inactiveNonFCoEQosConfig': None,
            'type': 'qos-aggregated-configuration',
                    'name': None,
                    'state': None,
                    'status': None,
                    'eTag': None,
                    'modified': None,
                    'created': None,
                    'category': 'qos-aggregated-configuration',
                    'uri': None}

Ethernet_settings = {'ethernetSettings': {'type': 'EthernetInterconnectSettingsV4',
                                          'uri': '',
                                          'category': None,
                                          'eTag': None,
                                          'created': '',
                                          'modified': '',
                                          'id': '',
                                          'name': '',
                                          'interconnectType': 'Ethernet',
                                          'enableIgmpSnooping': False,
                                          'igmpIdleTimeoutInterval': 260,
                                          'igmpSnoopingVlanIds': '',
                                          'enableFastMacCacheFailover': True,
                                          'macRefreshInterval': 5,
                                          'enableNetworkLoopProtection': True,
                                          'dependentResourceUri': '',
                                          'enablePauseFloodProtection': True,
                                          'enableRichTLV': False,
                                          'enableTaggedLldp': False,
                                          'lldpIpv4Address': '',
                                          'lldpIpv6Address': '',
                                          'lldpIpAddressMode': 'IPV4',
                                          'enableStormControl': False,
                                          'stormControlThreshold': 0,
                                          'stormControlPollingInterval': 10,
                                          'description': None,
                                          'state': None,
                                          'status': None}
                     }
Ethernet_settings_2 = {'ethernetSettings': {'type': 'EthernetInterconnectSettingsV4',
                                            'enableIgmpSnooping': False,
                                            'igmpSnoopingVlanIds': '',
                                            'interconnectType': 'Ethernet'}
                       }

Utilization_sampling_2 = {'telemetryConfiguration': {'type': 'telemetry-configuration',
                                                     'sampleCount': 12,
                                                     'sampleInterval': 300,
                                                     'enableTelemetry': True,
                                                     'category': 'telemetry-configuration'}

                          }


Utilization_sampling = {'telemetryConfiguration': {'type': 'telemetry-configuration',
                                                   'uri': None,
                                                   'category': 'telemetry-configuration',
                                                   'eTag': None,
                                                   'created': '',
                                                   'modified': '',
                                                   'enableTelemetry': True,
                                                   'sampleInterval': 300,
                                                   'sampleCount': 12,
                                                   'description': None,
                                                   'state': None,
                                                   'status': None,
                                                   'name': None}
                        }

Edit_LI_Fc = {'type': 'uplink-setV4',
              'name': 'US2',
              'networkUris': [],
              'portConfigInfos': [],
              'networkType': 'FibreChannel',
              'primaryPortLocation': None,
              'reachability': None,
              'manualLoginRedistributionState': 'Supported',
              'logicalInterconnectUri': None,
              'connectionMode': 'Auto',
              'lacpTimer': 'Short',
              'nativeNetworkUri': None,
              'fcNetworkUris': [],
              'fcoeNetworkUris': [],
              'state': None,
              'description': None,
              'status': None,
              'uri': None,
              'category': None,
              'modified': None,
              'created': None,
              'eTag': None}


# ### sFlow ###

sFlow_valT = True
sFlow_valF = False

ethnets = [{'name': 'Net1',
            'vlanId': '10',
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'subnetUri': '',
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged',
                      'type': 'ethernet-networkV4'}]
subnet = [{'type': 'Subnet',
           'gateway': '15.212.136.1',
           'networkId': '15.212.136.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [],
           'domain': 'hpe.com'}]

ipv4range = [{'type': 'Range',
              'startAddress': '15.212.136.3',
              'endAddress': '15.212.136.11',
              'name': 'Test',
              'subnetUri': ' '}]

ipMode = ["DHCP", "Static", 'IpPool']
sFlow_net = 'Net1'
sFlow_LIG_Name = 'LIG1'
uplink_sets_sFlow = {'us1_1': {'name': 'upset1',
                               'ethernetNetworkType': 'Tagged',
                               'networkType': 'Ethernet',
                               'networkUris': ['Net1'],
                               'nativeNetworkUri': None,
                               'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q1.1', 'speed': 'Auto'}, ]
                               }, }

sflowCollectors_initial = []
sflowPorts_initial = []

sampling_direction = ['Egress', 'Both', 'Ingress']


sflow_add_collector = [{"name": "collector1", "collectorEnabled": True, "ipAddress": "123.12.12.1", "maxDatagramSize": "1400", "maxHeaderSize": "128", "port": "6343", "collectorId": 1}]

sflow_edit_collector_name = [{"name": "collector2", "collectorEnabled": True, "ipAddress": "123.12.12.1", "maxDatagramSize": "1400", "maxHeaderSize": "128", "port": "6343", "collectorId": 1}]

sflow_edit_collector_disable = [{"name": "collector1", "collectorEnabled": False, "ipAddress": "123.12.12.1", "maxDatagramSize": "1400", "maxHeaderSize": "128", "port": "6343", "collectorId": 1}]
sflow_edit_collector_enable = [{"name": "collector1", "collectorEnabled": True, "ipAddress": "123.12.12.1", "maxDatagramSize": "1400", "maxHeaderSize": "128", "port": "6343", "collectorId": 1}]
sflow_edit_collector_datagram = [{"name": "collector1", "collectorEnabled": True, "ipAddress": "123.12.12.1", "maxDatagramSize": "500", "maxHeaderSize": "128", "port": "6343", "collectorId": 1}]

sflow_edit_collector_port_edit = [{"name": "collector1", "collectorEnabled": True, "ipAddress": "123.12.12.1", "maxDatagramSize": "1400", "maxHeaderSize": "128", "port": "49155", "collectorId": 1}]
sflow_add_2nd_collector = [{"name": "collector1", "collectorEnabled": True, "ipAddress": "123.12.12.1", "maxDatagramSize": "1400", "maxHeaderSize": "128", "port": "6343", "collectorId": 1}, {"name": "collector2", "collectorEnabled": True, "ipAddress": "123.12.12.2", "maxDatagramSize": "1400", "maxHeaderSize": "128", "port": "6343", "collectorId": 2}]

sflow_ports_add = [{"portName": "Q1:4", "collectorId": "1", "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 3, "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Sampling", "direction": "Both", "samplingRate": "4096"}, {"configurationMode": "Polling", "pollingInterval": "20"}]}]

sflow_ports_collector2 = [{"portName": "Q1:4", "collectorId": "2", "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 3, "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Sampling", "direction": "Ingress", "samplingRate": "4096"}, {"configurationMode": "Polling", "pollingInterval": "20"}]}]

sflow_ports_sampling_egress = [{"portName": "Q1:4", "collectorId": "1", "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 3, "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Sampling", "direction": "Egress", "samplingRate": "4096"}, {"configurationMode": "Polling", "pollingInterval": "20"}]}]

sflow_ports_sampling_ingress = [{"portName": "Q1:4", "collectorId": "1", "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 3, "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Sampling", "direction": "Ingress", "samplingRate": "4096"}, {"configurationMode": "Polling", "pollingInterval": "20"}]}]

sflow_ports_sampling_disable = [{"portName": "Q1:4", "collectorId": "1", "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 3, "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": "20"}]}]

sflow_ports_sampling_rate_edit = [{"portName": "Q1:4", "collectorId": "1", "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 3, "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Sampling", "direction": "Ingress", "samplingRate": "4097"}, {"configurationMode": "Polling", "pollingInterval": "20"}]}]

sflow_ports_polling_disable = [{"portName": "Q1:4", "collectorId": "1", "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 3, "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Sampling", "direction": "Ingress", "samplingRate": "4096"}]}]

sflow_ports_single_port_add = [{"portName": "Q1:4", "collectorId": "1", "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 3, "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Sampling", "direction": "Ingress", "samplingRate": "4096"}, {"configurationMode": "Polling", "pollingInterval": "20"}]},
                               {"portName": "Q2:4", "collectorId": "1", "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 3, "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Sampling", "direction": "Ingress", "samplingRate": "4096"}, {"configurationMode": "Polling", "pollingInterval": "20"}]}]

sflow_ports_multiple_port_add = [{"portName": "Q1:4", "collectorId": "1", "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 3, "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Sampling", "direction": "Ingress", "samplingRate": "4096"}, {"configurationMode": "Polling", "pollingInterval": "20"}]},
                                 {"portName": "Q2:4", "collectorId": "1", "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 3, "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Sampling", "direction": "Ingress", "samplingRate": "4096"}, {"configurationMode": "Polling", "pollingInterval": "20"}]}, {"portName": "Q1:1", "collectorId": "1", "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 3, "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Sampling", "direction": "Ingress", "samplingRate": "4096"}, {"configurationMode": "Polling", "pollingInterval": "20"}]}]

sflowCollectors_header_256 = [{
    'name': 'collector1',
    'ipAddress': '123.12.12.1',
    'port': 6343,
    'maxHeaderSize': '256',
    'maxDatagramSize': 1400,
    'collectorEnabled': True,
    'collectorId': 1}]
sflowCollectors_header_128 = [{
    'name': 'collector1',
    'ipAddress': '123.12.12.1',
    'port': 6343,
    'maxHeaderSize': '128',
    'maxDatagramSize': 1400,
    'collectorEnabled': True,
    'collectorId': 1}]
sflowCollectors_header_512 = [{
    'name': 'collector1',
    'ipAddress': '123.12.12.1',
    'port': 6343,
    'maxHeaderSize': '512',
    'maxDatagramSize': 1400,
    'collectorEnabled': True,
    'collectorId': 1}]
sflowCollectors_header_1024 = [{
    'name': 'collector1',
    'ipAddress': '123.12.12.1',
    'port': 6343,
    'maxHeaderSize': '1024',
    'maxDatagramSize': 1400,
    'collectorEnabled': True,
    'collectorId': 1}]

ip_mode_static = [{"ipMode": "Static", "ipAddr": "15.212.136.5", "subnetMask": "255.255.255.0"}]

sFlow_data = {"enabled": True,
              "type": "sflow-configuration",
              "sflowNetwork": {"name": "Net1", "uri": ""},
              "sflowCollectors": [],
              "sflowAgents": [{"ipMode": ""}],
              "sflowPorts": []}

sFlow_data_static = {"enabled": True,
                     "type": "sflow-configuration",
                     "sflowNetwork": {"name": "Net1", "uri": ""},
                     "sflowCollectors": [],
                     "sflowAgents": ip_mode_static,
                     "sflowPorts": []}

LIG_sFlow = {'lig_sFlow_setup':
             {'name': sFlow_LIG_Name,
              'type': 'logical-interconnect-groupV5',
              'enclosureType': 'SY12000',
              'interconnectMapTemplate': icmap_ME_Multi_LIG,
              'enclosureIndexes': [1, 2, 3],
              'interconnectBaySet': 3,
              'redundancyType': 'HighlyAvailable',
                                'uplinkSets': [uplink_sets_sFlow['us1_1'].copy()],
                                'ethernetSettings': None,
                                'state': 'Active',
                                'telemetryConfiguration': None,
                                'snmpConfiguration': None,
                                # 'sflowConfiguration':sFlow_data
              }}

Edit_LIG_sFlow_enabled = {'lig_E_sFlow':
                          {'name': sFlow_LIG_Name,
                           'type': 'logical-interconnect-groupV5',
                           'enclosureType': 'SY12000',
                           'interconnectMapTemplate': icmap_ME_Multi_LIG,
                           'enclosureIndexes': [1, 2, 3],
                           'interconnectBaySet': 3,
                           'redundancyType': 'HighlyAvailable',
                           'uplinkSets': [uplink_sets_sFlow['us1_1'].copy()],
                           'ethernetSettings': None,
                           'state': 'Active',
                           'telemetryConfiguration': None,
                           'snmpConfiguration': None,
                           # 'sflowConfiguration':sFlow_data
                           }}

Edit_LIG_sFlow_LI_initial_setup = {'lig_sFlow':
                                   {'name': sFlow_LIG_Name,
                                    'type': 'logical-interconnect-groupV5',
                                    'enclosureType': 'SY12000',
                                    'interconnectMapTemplate': icmap_ME_Multi_LIG,
                                    'enclosureIndexes': [1, 2, 3],
                                    'interconnectBaySet': 3,
                                    'redundancyType': 'HighlyAvailable',
                                    'uplinkSets': [uplink_sets_sFlow['us1_1'].copy()],
                                    'ethernetSettings': None,
                                    'state': 'Active',
                                    'telemetryConfiguration': None,
                                    'snmpConfiguration': None,
                                    'sflowConfiguration': sFlow_data
                                    }}

def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist


tor_switch_ip = "192.168.144.118"
server_ip = "25.25.26.4"
encic3 = "WPSTENC100, interconnect 3"
encic6 = "WPSTENC100, interconnect 6"
POTASH = "Virtual Connect SE 40Gb F8 Module for Synergy"
CHLORIDE20 = "Synergy 20Gb Interconnect Link Module"
split_unsplit_msg = "An uplink set may not contain both split and un-split uplink ports."
split_recomaction = "Specify only split or only un-split ports in an uplink set."
invalid_speed_errorcode = "INVALID_JSON_DATA_TYPE"
inval_spd_resol = "Correct the content of the JSON and try the request again."
LI = "LE_1Enc-LIG-bay3-1enc_f1682"
msg105 = "For uplink set Uplink1, uplink ports WPSTENC100, interconnect 3 :Q1 are non operational."
msg107 = "For uplink set Uplink1, uplink ports WPSTENC100, interconnect 3 :Q2 are non operational."
msg101 = "For uplink set Uplink1, uplink ports WPSTENC100, interconnect 3 :Q3 are non operational."
msg102 = "For uplink set Uplink1, uplink ports WPSTENC100, interconnect 3 :Q3 are non operational."
EM_SN = "WPSTENC100"


admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}
network_admin = {'userName': 'network', 'password': 'networkadmin'}
storage_admin = {'userName': 'storage', 'password': 'storageadmin'}
backup_admin = {'userName': 'backup', 'password': 'backupadmin'}
server_admin = {'userName': 'server', 'password': 'serveradmin'}
read_only = {'userName': 'readonly', 'password': 'readonly'}

users = [{'userName': 'server', 'password': 'serveradmin', 'fullName': 'Sarah', 'roles': ['Server administrator'], 'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'network', 'password': 'networkadmin', 'fullName': 'Nat', 'roles': ['Network administrator'], 'emailAddress': 'nat@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'backup', 'password': 'backupadmin', 'fullName': 'Backup', 'roles': ['Backup administrator'], 'emailAddress': 'backup@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'readonly', 'password': 'readonly', 'fullName': 'Rheid', 'roles': ['Read only'], 'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'storage', 'password': 'storageadmin', 'fullName': 'Rheid', 'roles': ['Storage administrator'], 'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'}
         ]

licenses_1 = [{'key': 'YB2C D9MA H9PA 8HU3 V2B4 HWWV Y9JL KMPL B89H MZVU GR4S JHWE 9QSP XFR8 CMRG HPMR UFVU A5K9 MWHC 9K4K HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'},
              {'key': 'ABSE D9MA H9P9 CHUZ V2B4 HWWV Y9JL KMPL B89H MZVU GR4S JHWE 9FQP XN5W CMRG HPMR UFVU A5K9 MWHC 9K4K HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'}
              ]
licenses_2 = [{'key': 'YBCG D9MA H9PA GHUY V2B4 HWWV Y9JL KMPL B89H MZVU GR4S JHWE JVSH XV5S CMRG HPMR UFVU A5K9 MWHC 9K4K HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'}]

ethernet_networks = [{'name': 'eth-10', 'type': 'ethernet-networkV300', 'vlanId': 10, 'purpose': 'General', 'smartLink': True,
                      'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tagged'},
                     {'name': 'eth-11', 'type': 'ethernet-networkV300', 'vlanId': 11, 'purpose': 'General',
                      'smartLink': True, 'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tagged'},
                     {'name': 'eth-12', 'type': 'ethernet-networkV300', 'vlanId': 12, 'purpose': 'General',
                      'smartLink': True, 'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Untagged'},
                     {'name': 'eth-13', 'type': 'ethernet-networkV300', 'vlanId': 13, 'purpose': 'General',
                      'smartLink': True, 'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tunnel'}

                     ]

# enc

fcoe_networks = [{'name': 'FCOE-100', 'type': 'fcoe-networkV300', 'vlanId': 100},
                 {'name': 'FCOE-101', 'type': 'fcoe-networkV300', 'vlanId': 101},
                 {'name': 'FCOE-114', 'type': 'fcoe-networkV300', 'vlanId': 114},
                 {'name': 'FCOE-115', 'type': 'fcoe-networkV300', 'vlanId': 115}
                 ]

fc_networks = [{'type': 'fc-networkV300', 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
                'name': 'SAN-1-A', 'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'},
               {'type': 'fc-networkV300', 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
                'name': 'SAN-2-A', 'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'}]


lig_tbird_f1682 = [{'type': 'logical-interconnect-groupV300',
                    'ethernetSettings': {'type': 'EthernetInterconnectSettingsV201', 'enableIgmpSnooping': False,
                                         'igmpIdleTimeoutInterval': 260, 'enableFastMacCacheFailover': True,
                                         'macRefreshInterval': 5, 'enableNetworkLoopProtection': True,
                                         'enablePauseFloodProtection': True, 'enableRichTLV': False,
                                         'interconnectType': 'Ethernet', 'dependentResourceUri': None,
                                         'name': 'defaultEthernetSwitchSettings', 'category': None, 'uri': '/ethernetSettings'},
                    'description': None, 'name': 'LIG-bay3-1enc_f1682',
                    'interconnectMapTemplate':
                    {'interconnectMapEntryTemplates': [
                        {'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Enclosure', 'relativeValue': 1}]}, 'permittedInterconnectTypeUri': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1}]},
                    'enclosureType': 'SY12000', 'enclosureIndexes': [1], 'interconnectBaySet': '3',
                    'redundancyType': 'NonRedundantASide', 'internalNetworkUris': [],
                    'snmpConfiguration': {'type': 'snmp-configuration', 'readCommunity': 'public', 'systemContact': '', 'trapDestinations': None, 'snmpAccess': None, 'enabled': True, 'description': None, 'name': None, 'state': None, 'category': 'snmp-configuration'},
                    'qosConfiguration': None,
                    'uplinkSets': [
                        {'networkUris': ['eth-10'], 'mode':'Auto', 'lacpTimer':'Short', 'primaryPort':None,
                         'logicalPortConfigInfos':[{'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 61}, {'type': 'Enclosure', 'relativeValue': 1}]}}],
                         'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'name': 'Uplink1'},
                        {'networkUris': ['eth-11'], 'mode':'Auto', 'lacpTimer':'Short', 'primaryPort':None,
                            'logicalPortConfigInfos':[{'desiredSpeed': 'Speed40G', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 66}, {'type': 'Enclosure', 'relativeValue': 1}]}}],
                            'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'name': 'Uplink2'},
                        {'networkUris': ['SAN-1-A'], 'mode':'Auto', 'lacpTimer':'Short', 'primaryPort':None,
                            'logicalPortConfigInfos':[{'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 72}, {'type': 'Enclosure', 'relativeValue': 1}]}}],
                            'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'name': 'SAN-1-A'},
                        {'networkUris': ['FCOE-100'], 'mode':'Auto', 'lacpTimer':'Short', 'primaryPort':None,
                            'logicalPortConfigInfos':[{'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 76}, {'type': 'Enclosure', 'relativeValue': 1}]}}],
                            'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'name': 'FCOE-100'}
                    ]}]

lig_tbird_f1682_1 = [{'type': 'logical-interconnect-groupV300',
                      'ethernetSettings': {'type': 'EthernetInterconnectSettingsV201', 'enableIgmpSnooping': False, 'igmpIdleTimeoutInterval': 260, 'enableFastMacCacheFailover': True, 'macRefreshInterval': 5, 'enableNetworkLoopProtection': True, 'enablePauseFloodProtection': True, 'enableRichTLV': False, 'interconnectType': 'Ethernet', 'dependentResourceUri': None, 'name': 'defaultEthernetSwitchSettings', 'category': None, 'uri': '/ethernetSettings'},
                      'description': None, 'name': 'LIG-bay3-1enc_f16821',
                      'interconnectMapTemplate':
                      {'interconnectMapEntryTemplates': [
                          {'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Enclosure', 'relativeValue': 1}]}, 'permittedInterconnectTypeUri': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
                          {'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 6}, {'type': 'Enclosure', 'relativeValue': 1}]}, 'permittedInterconnectTypeUri': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1}]},
                      'enclosureType': 'SY12000', 'enclosureIndexes': [1], 'interconnectBaySet': '3',
                      'redundancyType': 'Redundant', 'internalNetworkUris': [],
                      'snmpConfiguration': {'type': 'snmp-configuration', 'readCommunity': 'public', 'systemContact': '', 'trapDestinations': None, 'snmpAccess': None, 'enabled': True, 'description': None, 'name': None, 'state': None, 'category': 'snmp-configuration'},
                      'qosConfiguration': None,
                      'uplinkSets': [
                          {'networkUris': ['eth-10'], 'mode':'Auto', 'lacpTimer':'Short', 'primaryPort':None,
                           'logicalPortConfigInfos':[{'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 61}, {'type': 'Enclosure', 'relativeValue': 1}]}}],
                           'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'name': 'Uplink1'},
                          {'networkUris': ['eth-11'], 'mode':'Auto', 'lacpTimer':'Short', 'primaryPort':None,
                           'logicalPortConfigInfos':[{'desiredSpeed': 'Speed40G', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 66}, {'type': 'Enclosure', 'relativeValue': 1}]}}],
                           'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'name': 'Uplink2'},
                          {'networkUris': ['SAN-1-A'], 'mode':'Auto', 'lacpTimer':'Short', 'primaryPort':None,
                           'logicalPortConfigInfos':[{'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 72}, {'type': 'Enclosure', 'relativeValue': 1}]}}],
                           'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'name': 'SAN-1-A'},
                          {'networkUris': ['FCOE-100'], 'mode':'Auto', 'lacpTimer':'Short', 'primaryPort':None,
                           'logicalPortConfigInfos':[{'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 76}, {'type': 'Enclosure', 'relativeValue': 1}]}}],
                           'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'name': 'FCOE-100'}
                      ]}]


uplinkSets_782 = [{'networkUris': ['eth-11'], 'mode':'Auto', 'lacpTimer':'Short', 'primaryPort':None,
                   'logicalPortConfigInfos':[{'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 62}, {'type': 'Enclosure', 'relativeValue': 1}]}},
                                             {'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 63}, {'type': 'Enclosure', 'relativeValue': 1}]}},
                                             {'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 64}, {'type': 'Enclosure', 'relativeValue': 1}]}},
                                             {'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 65}, {'type': 'Enclosure', 'relativeValue': 1}]}}],
                   'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'name': 'Uplink1'}]


uplinkSets_60 = [{'networkUris': ['eth-10'], 'mode':'Auto', 'lacpTimer':'Short', 'primaryPort':None,
                  'logicalPortConfigInfos':[{'desiredSpeed': 'Speed40G', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 61}, {'type': 'Enclosure', 'relativeValue': 1}]}}],
                  'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'name': 'Uplink1'},
                 {'networkUris': ['eth-11'], 'mode':'Auto', 'lacpTimer':'Short', 'primaryPort':None,
                  'logicalPortConfigInfos':[{'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 67}, {'type': 'Enclosure', 'relativeValue': 1}]}},
                                            {'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 68}, {'type': 'Enclosure', 'relativeValue': 1}]}}],
                  'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'name': 'Uplink2'}]


uplinkSets_61 = [{'networkUris': ['eth-10'], 'mode':'Auto', 'lacpTimer':'Short', 'primaryPort':None,
                  'logicalPortConfigInfos':[{'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 67}, {'type': 'Enclosure', 'relativeValue': 1}]}}],
                  'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'name': 'Uplink1'},
                 {'networkUris': ['eth-11'], 'mode':'Auto', 'lacpTimer':'Short', 'primaryPort':None,
                  'logicalPortConfigInfos':[{'desiredSpeed': 'Speed40G', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 66}, {'type': 'Enclosure', 'relativeValue': 1}]}},
                                            {'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 62}, {'type': 'Enclosure', 'relativeValue': 1}]}}],
                  'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'name': 'Uplink2'}]


uplinkSets_611 = [{'networkUris': ['eth-10'], 'mode':'Auto', 'lacpTimer':'Short', 'primaryPort':None,
                   'logicalPortConfigInfos':[{'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 61}, {'type': 'Enclosure', 'relativeValue': 1}]}},
                                             {'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 64}, {'type': 'Enclosure', 'relativeValue': 1}]}}],
                   'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'name': 'Uplink1'},
                  ]


uplinkSets_62 = [{'networkUris': ['eth-10'], 'mode':'Auto', 'lacpTimer':'Short', 'primaryPort':None,
                  'logicalPortConfigInfos':[{'desiredSpeed': 'Speed40G', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 61}, {'type': 'Enclosure', 'relativeValue': 1}]}}],
                  'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'name': 'Uplink1'},
                 {'networkUris': ['eth-11'], 'mode':'Auto', 'lacpTimer':'Short', 'primaryPort':None,
                  'logicalPortConfigInfos':[{'desiredSpeed': 'Speed40G', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 66}, {'type': 'Enclosure', 'relativeValue': 1}]}}],
                  'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'name': 'Uplink2'}]

uplinkSets_63 = [{'networkUris': ['eth-11'], 'mode':'Auto', 'lacpTimer':'Short', 'primaryPort':None,
                  'logicalPortConfigInfos':[{'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 67}, {'type': 'Enclosure', 'relativeValue': 1}]}},
                                            {'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 72}, {'type': 'Enclosure', 'relativeValue': 1}]}},
                                            {'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 77}, {'type': 'Enclosure', 'relativeValue': 1}]}},
                                            {'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 62}, {'type': 'Enclosure', 'relativeValue': 1}]}}],
                  'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'name': 'Uplink1'}]

uplinkSets_64 = [{'networkUris': ['eth-11'], 'mode':'Auto', 'lacpTimer':'Short', 'primaryPort':None,
                  'logicalPortConfigInfos':[{'desiredSpeed': 'semiAuto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 67}, {'type': 'Enclosure', 'relativeValue': 1}]}},
                                            ], 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'name': 'Uplink1'},
                 ]

uplinkSets_641 = [{'networkUris': ['eth-11'], 'mode':'Auto', 'lacpTimer':'Short', 'primaryPort':None,
                   'logicalPortConfigInfos':[{'desiredSpeed': ' Auto ', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 67}, {'type': 'Enclosure', 'relativeValue': 1}]}},
                                             ], 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'name': 'Uplink1'},
                  ]

uplinkSets_642 = [{'networkUris': ['eth-11'], 'mode':'Auto', 'lacpTimer':'Short', 'primaryPort':None,
                   'logicalPortConfigInfos':[{'desiredSpeed': 'speed40g', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 67}, {'type': 'Enclosure', 'relativeValue': 1}]}},
                                             ], 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'name': 'Uplink1'},
                  ]

uplinkSets_643 = [{'networkUris': ['eth-11'], 'mode':'Auto', 'lacpTimer':'Short', 'primaryPort':None,
                   'logicalPortConfigInfos':[{'desiredSpeed': 'auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 67}, {'type': 'Enclosure', 'relativeValue': 1}]}},
                                             ], 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'name': 'Uplink1'},
                  ]
uplinkSets_55 = [{'networkUris': ['eth-10'], 'mode':'Auto', 'lacpTimer':'Short', 'primaryPort':None,
                  'logicalPortConfigInfos':[{'desiredSpeed': 'Speed40G', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 61}, {'type': 'Enclosure', 'relativeValue': 1}]}},
                                            {'desiredSpeed': 'Speed40G', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 66}, {'type': 'Enclosure', 'relativeValue': 1}]}},
                                            {'desiredSpeed': 'Speed40G', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 71}, {'type': 'Enclosure', 'relativeValue': 1}]}},
                                            {'desiredSpeed': 'Speed40G', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 76}, {'type': 'Enclosure', 'relativeValue': 1}]}}],
                  'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'name': 'Uplink1'},
                 {'networkUris': ['eth-11'], 'mode':'Auto', 'lacpTimer':'Short', 'primaryPort':None,
                  'logicalPortConfigInfos':[{'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 6}, {'type': 'Port', 'relativeValue': 61}, {'type': 'Enclosure', 'relativeValue': 1}]}},
                                            {'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 6}, {'type': 'Port', 'relativeValue': 66}, {'type': 'Enclosure', 'relativeValue': 1}]}},
                                            {'desiredSpeed': 'Speed40G', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 6}, {'type': 'Port', 'relativeValue': 71}, {'type': 'Enclosure', 'relativeValue': 1}]}},
                                            {'desiredSpeed': 'Speed40G', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 6}, {'type': 'Port', 'relativeValue': 76}, {'type': 'Enclosure', 'relativeValue': 1}]}}],
                  'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'name': 'Uplink2'}]


uplinkSets_56 = [{'networkUris': ['eth-10'], 'mode':'Auto', 'lacpTimer':'Short', 'primaryPort':None,
                  'logicalPortConfigInfos':[{'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 62}, {'type': 'Enclosure', 'relativeValue': 1}]}},
                                            {'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 65}, {'type': 'Enclosure', 'relativeValue': 1}]}},
                                            {'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 67}, {'type': 'Enclosure', 'relativeValue': 1}]}},
                                            {'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 70}, {'type': 'Enclosure', 'relativeValue': 1}]}},
                                            {'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 72}, {'type': 'Enclosure', 'relativeValue': 1}]}},
                                            {'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 75}, {'type': 'Enclosure', 'relativeValue': 1}]}}

                                            ],
                  'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'name': 'Uplink1'},
                 {'networkUris': ['eth-11'], 'mode':'Auto', 'lacpTimer':'Short', 'primaryPort':None,
                  'logicalPortConfigInfos':[{'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 6}, {'type': 'Port', 'relativeValue': 77}, {'type': 'Enclosure', 'relativeValue': 1}]}},
                                            {'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 6}, {'type': 'Port', 'relativeValue': 80}, {'type': 'Enclosure', 'relativeValue': 1}]}},
                                            ],
                  'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'name': 'Uplink2'}]

uplinkSets_backup = [{'networkUris': ['eth-10'], 'mode':'Auto', 'lacpTimer':'Short', 'primaryPort':None,
                      'logicalPortConfigInfos':[{'desiredSpeed': 'Speed40G', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 61}, {'type': 'Enclosure', 'relativeValue': 1}]}},
                                                {'desiredSpeed': 'Speed40G', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 66}, {'type': 'Enclosure', 'relativeValue': 1}]}},
                                                ],
                      'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'name': 'Uplink1'},
                     {'networkUris': ['eth-11'], 'mode':'Auto', 'lacpTimer':'Short', 'primaryPort':None,
                      'logicalPortConfigInfos':[{'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 6}, {'type': 'Port', 'relativeValue': 72}, {'type': 'Enclosure', 'relativeValue': 1}]}},
                                                {'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 6}, {'type': 'Port', 'relativeValue': 73}, {'type': 'Enclosure', 'relativeValue': 1}]}}],
                      'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'name': 'Uplink2'}]

uplinkSets_backup2 = [{"type": "uplink-setV300", "name": "Uplink2",
                       "networkUris": ["eth-10"], "portConfigInfos":[{"desiredSpeed": "Speed40G", "location":
                                                                      {"locationEntries": [{"value": "Q3", "type": "Port"}, {"value": "3", "type": "Bay"},
                                                                                           {"value": "/rest/enclosures/000000WPSTENC100", "type": "Enclosure"}]}},
                                                                     ],
                       "networkType": "Ethernet", "primaryPortLocation": None, "reachability": None, "manualLoginRedistributionState": "NotSupported",
                       "logicalInterconnectUri": "LE_1Enc-LIG-bay3-1enc_f1682", "connectionMode": "Auto", "lacpTimer": "Short", "nativeNetworkUri": None, "fcNetworkUris": [],
                       "fcoeNetworkUris":[], "state":None, "description":None,
                       "uri":None, "category":"logical-interconnects", "ethernetNetworkType":"Tagged"}]


uplinkSets_52 = [
    {'networkUris': ['eth-10'], 'mode':'Auto', 'lacpTimer':'Short', 'primaryPort':None,
     'logicalPortConfigInfos':[{'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 61}, {'type': 'Enclosure', 'relativeValue': 1}]}},

                               {'desiredSpeed': 'Speed40G', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 66}, {'type': 'Enclosure', 'relativeValue': 1}]}}],
     'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'name': 'Uplink1'}]


uplinkSets_53 = [{"type": "uplink-setV300", "name": "Uplink3",
                  "networkUris": ["eth-10"], "portConfigInfos":[{"desiredSpeed": "Auto", "location":
                                                                 {"locationEntries": [{"value": "Q3", "type": "Port"}, {"value": "3", "type": "Bay"},
                                                                                      {"value": "/rest/enclosures/000000WPSTENC100", "type": "Enclosure"}]}},
                                                                {"desiredSpeed": "Auto", "location": {"locationEntries": [{"value": "Q4:1", "type": "Port"},
                                                                                                                          {"value": "3", "type": "Bay"},
                                                                                                                          {"value": "/rest/enclosures/000000WPSTENC100", "type": "Enclosure"}]}},
                                                                {"desiredSpeed": "Auto", "location": {"locationEntries": [{"value": "Q4:2", "type": "Port"},
                                                                                                                          {"value": "3", "type": "Bay"},
                                                                                                                          {"value": "/rest/enclosures/000000WPSTENC100", "type": "Enclosure"}]}}
                                                                ],
                  "networkType": "Ethernet", "primaryPortLocation": None, "reachability": None, "manualLoginRedistributionState": "NotSupported",
                  "logicalInterconnectUri": "LE_1Enc-LIG-bay3-1enc_f1682", "connectionMode": "Auto", "lacpTimer": "Short", "nativeNetworkUri": None, "fcNetworkUris": [],
                  "fcoeNetworkUris":[], "state":None, "description":None,
                  "uri":None, "category":"logical-interconnects", "ethernetNetworkType":"Tagged"}]


uplinkSets_78 = [{"type": "uplink-setV300", "name": "Uplink11",
                  "networkUris": ["eth-10"], "portConfigInfos":[{"desiredSpeed": "Autos", "location":
                                                                 {"locationEntries": [{"value": "Q5", "type": "Port"}, {"value": "3", "type": "Bay"},
                                                                                      {"value": "/rest/enclosures/000000WPSTENC100", "type": "Enclosure"}]}},
                                                                ],
                  "networkType": "Ethernet", "primaryPortLocation": None, "reachability": None, "manualLoginRedistributionState": "NotSupported",
                  "logicalInterconnectUri": "LE_1Enc-LIG-bay3-1enc_f1682", "connectionMode": "Auto", "lacpTimer": "Short", "nativeNetworkUri": None, "fcNetworkUris": [],
                  "fcoeNetworkUris":[], "state":None, "description":None,
                  "uri":None, "category":"logical-interconnects", "ethernetNetworkType":"Tagged"}]


uplinkSets_791 = [{"type": "uplink-setV300", "name": "Uplink11",
                   "networkUris": ["eth-10"], "portConfigInfos":[{"desiredSpeed": "Speed4G", "location":
                                                                  {"locationEntries": [{"value": "Q6:1", "type": "Port"}, {"value": "6", "type": "Bay"},
                                                                                       {"value": "/rest/enclosures/000000WPSTENC100", "type": "Enclosure"}]}},
                                                                 {"desiredSpeed": "Speed10G", "location":
                                                                  {"locationEntries": [{"value": "Q6:2", "type": "Port"}, {"value": "3", "type": "Bay"},
                                                                                       {"value": "/rest/enclosures/000000WPSTENC100", "type": "Enclosure"}]}},
                                                                 {"desiredSpeed": "Speed7G", "location":
                                                                  {"locationEntries": [{"value": "Q5", "type": "Port"}, {"value": "3", "type": "Bay"},
                                                                                       {"value": "/rest/enclosures/000000WPSTENC100", "type": "Enclosure"}]}},

                                                                 ],
                   "networkType": "Ethernet", "primaryPortLocation": None, "reachability": None, "manualLoginRedistributionState": "NotSupported",
                   "logicalInterconnectUri": "LE_1Enc-LIG-bay3-1enc_f1682", "connectionMode": "Auto", "lacpTimer": "Short", "nativeNetworkUri": None, "fcNetworkUris": [],
                   "fcoeNetworkUris":[], "state":None, "description":None,
                   "uri":None, "category":"logical-interconnects", "ethernetNetworkType":"Tagged"}]


uplinkSets_792_lig = [
    {'networkUris': ['eth-10'], 'mode':'Auto', 'lacpTimer':'Short', 'primaryPort':None,
     'logicalPortConfigInfos':[{'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 61}, {'type': 'Enclosure', 'relativeValue': 1}]}},
                               {'desiredSpeed': 'Speed40G', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 66}, {'type': 'Enclosure', 'relativeValue': 1}]}}
                               ],
     'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'name': 'Uplink1'},
]

uplinkSets_792_lig1 = [
    {'networkUris': ['eth-10'], 'mode':'Auto', 'lacpTimer':'Short', 'primaryPort':None,
     'logicalPortConfigInfos':[{'desiredSpeed': 'Speed40G', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 61}, {'type': 'Enclosure', 'relativeValue': 1}]}},
                               {'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 66}, {'type': 'Enclosure', 'relativeValue': 1}]}}
                               ],
     'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'name': 'Uplink1'},
]

uplinkSets_792_li = [{"type": "uplink-setV300", "name": "Uplink1",
                      "networkUris": ["eth-10"], "portConfigInfos":[{"desiredSpeed": "Speed40G", "location":
                                                                     {"locationEntries": [{"value": "Q1", "type": "Port"}, {"value": "3", "type": "Bay"},
                                                                                          {"value": "/rest/enclosures/000000WPSTENC100", "type": "Enclosure"}]}},
                                                                    {"desiredSpeed": "Speed40G", "location":
                                                                     {"locationEntries": [{"value": "Q2", "type": "Port"}, {"value": "3", "type": "Bay"},
                                                                                          {"value": "/rest/enclosures/000000WPSTENC100", "type": "Enclosure"}]}}
                                                                    ],
                      "networkType": "Ethernet", "primaryPortLocation": None, "reachability": None, "manualLoginRedistributionState": "NotSupported",
                      "logicalInterconnectUri": "LE_1Enc-LIG-bay3-1enc_f1682", "connectionMode": "Auto", "lacpTimer": "Short", "nativeNetworkUri": None, "fcNetworkUris": [],
                      "fcoeNetworkUris":[], "state":None, "description":None,
                      "uri":None, "category":"logical-interconnects", "ethernetNetworkType":"Tagged"}]


uplinkSets_531 = [{"type": "uplink-setV300", "name": "Uplink1",
                   "networkUris": ["eth-10"], "portConfigInfos":[{"desiredSpeed": "Auto", "location":
                                                                  {"locationEntries": [{"value": "Q1", "type": "Port"}, {"value": "3", "type": "Bay"},
                                                                                       {"value": "/rest/enclosures/000000WPSTENC100", "type": "Enclosure"}]}},
                                                                 {"desiredSpeed": "Speed40G", "location": {"locationEntries": [{"value": "Q2", "type": "Port"},
                                                                                                                               {"value": "3", "type": "Bay"},
                                                                                                                               {"value": "/rest/enclosures/000000WPSTENC100", "type": "Enclosure"}]}},
                                                                 {"desiredSpeed": "Speed40G", "location": {"locationEntries": [{"value": "Q3", "type": "Port"},
                                                                                                                               {"value": "3", "type": "Bay"},
                                                                                                                               {"value": "/rest/enclosures/000000WPSTENC100", "type": "Enclosure"}]}}

                                                                 ],
                   "networkType": "Ethernet", "primaryPortLocation": None, "reachability": None, "manualLoginRedistributionState": "NotSupported",
                   "logicalInterconnectUri": "LE_1Enc-LIG-bay3-1enc_f1682", "connectionMode": "Auto", "lacpTimer": "Short", "nativeNetworkUri": None, "fcNetworkUris": [],
                   "fcoeNetworkUris":[], "state":None, "description":None,
                   "uri":None, "category":"logical-interconnects", "ethernetNetworkType":"Tagged"}]


uplinkSets_691 = [{"type": "uplink-setV300", "name": "Uplink1",
                   "networkUris": ["eth-10"], "portConfigInfos":[{"desiredSpeed": "Speed40G", "location":
                                                                  {"locationEntries": [{"value": "Q1", "type": "Port"}, {"value": "3", "type": "Bay"},
                                                                                       {"value": "/rest/enclosures/000000WPSTENC100", "type": "Enclosure"}]}},
                                                                 ],
                   "networkType": "Ethernet", "primaryPortLocation": None, "reachability": None, "manualLoginRedistributionState": "NotSupported",
                   "logicalInterconnectUri": "LE_1Enc-LIG-bay3-1enc_f1682", "connectionMode": "Auto", "lacpTimer": "Short", "nativeNetworkUri": None, "fcNetworkUris": [],
                   "fcoeNetworkUris":[], "state":None, "description":None,
                   "uri":None, "category":"logical-interconnects", "ethernetNetworkType":"Tagged"},

                  {"type": "uplink-setV300", "name": "Uplink2",
                   "networkUris": ["eth-12"], "portConfigInfos":[{"desiredSpeed": "Auto", "location":
                                                                  {"locationEntries": [{"value": "Q2", "type": "Port"}, {"value": "3", "type": "Bay"},
                                                                                       {"value": "/rest/enclosures/000000WPSTENC100", "type": "Enclosure"}]}}],
                   "networkType": "Ethernet", "primaryPortLocation": None, "reachability": None, "manualLoginRedistributionState": "NotSupported",
                   "logicalInterconnectUri": "LE_1Enc-LIG-bay3-1enc_f1682", "connectionMode": "Auto", "lacpTimer": "Short", "nativeNetworkUri": None, "fcNetworkUris": [],
                   "fcoeNetworkUris":[], "state":None, "description":None,
                   "uri":None, "category":"logical-interconnects", "ethernetNetworkType":"Untagged"}]


uplinkSets_691_lig1 = [
    {'networkUris': ['eth-10'], 'mode':'Auto', 'lacpTimer':'Short', 'primaryPort':None,
     'logicalPortConfigInfos':[{'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 62}, {'type': 'Enclosure', 'relativeValue': 1}]}},

                               ],
     'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'name': 'Uplink1'},
    {'networkUris': ['eth-11'], 'mode':'Auto', 'lacpTimer':'Short', 'primaryPort':None,
     'logicalPortConfigInfos':[{'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 68}, {'type': 'Enclosure', 'relativeValue': 1}]}},
                               ],
     'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'name': 'Uplink2'},
]

uplinkSets_692_lig1 = [
    {'networkUris': ['eth-10'], 'mode':'Auto', 'lacpTimer':'Short', 'primaryPort':None,
     'logicalPortConfigInfos':[{'desiredSpeed': 'Speed40G', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 61}, {'type': 'Enclosure', 'relativeValue': 1}]}},

                               ],
     'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'name': 'Uplink1'},
    {'networkUris': ['eth-11'], 'mode':'Auto', 'lacpTimer':'Short', 'primaryPort':None,
     'logicalPortConfigInfos':[{'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 66}, {'type': 'Enclosure', 'relativeValue': 1}]}},
                               ],
     'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'name': 'Uplink2'},
]


uplinkSets_54 = [{"type": "uplink-setV300", "name": "Uplink1",
                  "networkUris": ["eth-10"], "portConfigInfos":[{"desiredSpeed": "Speed40G", "location":
                                                                 {"locationEntries": [{"value": "Q1", "type": "Port"}, {"value": "3", "type": "Bay"},
                                                                                      {"value": "/rest/enclosures/000000WPSTENC100", "type": "Enclosure"}]}},
                                                                {"desiredSpeed": "Speed40G", "location": {"locationEntries": [{"value": "Q2", "type": "Port"},
                                                                                                                              {"value": "3", "type": "Bay"},
                                                                                                                              {"value": "/rest/enclosures/000000WPSTENC100", "type": "Enclosure"}]}}],
                  "networkType": "Ethernet", "primaryPortLocation": None, "reachability": None, "manualLoginRedistributionState": "NotSupported",
                  "logicalInterconnectUri": "LE_1Enc-LIG-bay3-1enc_f1682", "connectionMode": "Auto", "lacpTimer": "Short", "nativeNetworkUri": None, "fcNetworkUris": [],
                  "fcoeNetworkUris":[], "state":None, "description":None,
                  "uri":None, "category":"logical-interconnects", "ethernetNetworkType":"Tagged"},
                 {"type": "uplink-setV300", "name": "Uplink2",
                  "networkUris": ["eth-12"], "portConfigInfos":[{"desiredSpeed": "Auto", "location":
                                                                 {"locationEntries": [{"value": "Q3:2", "type": "Port"}, {"value": "3", "type": "Bay"},
                                                                                      {"value": "/rest/enclosures/000000WPSTENC100", "type": "Enclosure"}]}}],
                  "networkType": "Ethernet", "primaryPortLocation": None, "reachability": None, "manualLoginRedistributionState": "NotSupported",
                  "logicalInterconnectUri": "LE_1Enc-LIG-bay3-1enc_f1682", "connectionMode": "Auto", "lacpTimer": "Short", "nativeNetworkUri": None, "fcNetworkUris": [],
                  "fcoeNetworkUris":[], "state":None, "description":None,
                  "uri":None, "category":"logical-interconnects", "ethernetNetworkType":"Untagged"}
                 ]


uplinkSets_541 = [{"type": "uplink-setV300", "name": "Uplink1",
                   "networkUris": ["eth-10"], "portConfigInfos":[{"desiredSpeed": "Speed40G", "location":
                                                                  {"locationEntries": [{"value": "Q1", "type": "Port"}, {"value": "3", "type": "Bay"},
                                                                                       {"value": "/rest/enclosures/000000WPSTENC100", "type": "Enclosure"}]}},
                                                                 {"desiredSpeed": "Speed40G", "location": {"locationEntries": [{"value": "Q2", "type": "Port"},
                                                                                                                               {"value": "3", "type": "Bay"},
                                                                                                                               {"value": "/rest/enclosures/000000WPSTENC100", "type": "Enclosure"}]}},

                                                                 {"desiredSpeed": "Speed40G", "location": {"locationEntries": [{"value": "Q4", "type": "Port"},
                                                                                                                               {"value": "3", "type": "Bay"},
                                                                                                                               {"value": "/rest/enclosures/000000WPSTENC100", "type": "Enclosure"}]}},
                                                                 {"desiredSpeed": "Speed40G", "location": {"locationEntries": [{"value": "Q3", "type": "Port"},
                                                                                                                               {"value": "3", "type": "Bay"},
                                                                                                                               {"value": "/rest/enclosures/000000WPSTENC100", "type": "Enclosure"}]}}
                                                                 ],
                   "networkType": "Ethernet", "primaryPortLocation": None, "reachability": None, "manualLoginRedistributionState": "NotSupported",
                   "logicalInterconnectUri": "LE_1Enc-LIG-bay3-1enc_f1682", "connectionMode": "Auto", "lacpTimer": "Short", "nativeNetworkUri": None, "fcNetworkUris": [],
                   "fcoeNetworkUris":[], "state":None, "description":None,
                   "uri":None, "category":"logical-interconnects", "ethernetNetworkType":"Tagged"},


                  ]

uplinkSets_541_bay6 = [{"type": "uplink-setV300", "name": "Uplink1",
                        "networkUris": ["eth-10"], "portConfigInfos":[{"desiredSpeed": "Speed40G", "location":
                                                                       {"locationEntries": [{"value": "Q1", "type": "Port"}, {"value": "3", "type": "Bay"},
                                                                                            {"value": "/rest/enclosures/000000WPSTENC100", "type": "Enclosure"}]}},
                                                                      {"desiredSpeed": "Speed40G", "location": {"locationEntries": [{"value": "Q2", "type": "Port"},
                                                                                                                                    {"value": "3", "type": "Bay"},
                                                                                                                                    {"value": "/rest/enclosures/000000WPSTENC100", "type": "Enclosure"}]}},

                                                                      {"desiredSpeed": "Speed40G", "location": {"locationEntries": [{"value": "Q4", "type": "Port"},
                                                                                                                                    {"value": "3", "type": "Bay"},
                                                                                                                                    {"value": "/rest/enclosures/000000WPSTENC100", "type": "Enclosure"}]}},
                                                                      {"desiredSpeed": "Speed40G", "location": {"locationEntries": [{"value": "Q3", "type": "Port"},
                                                                                                                                    {"value": "3", "type": "Bay"},
                                                                                                                                    {"value": "/rest/enclosures/000000WPSTENC100", "type": "Enclosure"}]}}
                                                                      ],
                        "networkType": "Ethernet", "primaryPortLocation": None, "reachability": None, "manualLoginRedistributionState": "NotSupported",
                        "logicalInterconnectUri": "LE_1Enc-LIG-bay3-1enc_f1682", "connectionMode": "Auto", "lacpTimer": "Short", "nativeNetworkUri": None, "fcNetworkUris": [],
                        "fcoeNetworkUris":[], "state":None, "description":None,
                        "uri":None, "category":"logical-interconnects", "ethernetNetworkType":"Tagged"},

                       {"type": "uplink-setV300", "name": "Uplink2",
                        "networkUris": ["eth-12"], "portConfigInfos":[{"desiredSpeed": "Speed40G", "location":
                                                                       {"locationEntries": [{"value": "Q1", "type": "Port"}, {"value": "6", "type": "Bay"},
                                                                                            {"value": "/rest/enclosures/000000WPSTENC100", "type": "Enclosure"}]}},
                                                                      {"desiredSpeed": "Speed40G", "location":
                                                                       {"locationEntries": [{"value": "Q2", "type": "Port"}, {"value": "6", "type": "Bay"},
                                                                                            {"value": "/rest/enclosures/000000WPSTENC100", "type": "Enclosure"}]}},
                                                                      {"desiredSpeed": "Speed40G", "location":
                                                                       {"locationEntries": [{"value": "Q3", "type": "Port"}, {"value": "6", "type": "Bay"},
                                                                                            {"value": "/rest/enclosures/000000WPSTENC100", "type": "Enclosure"}]}},
                                                                      {"desiredSpeed": "Speed40G", "location":
                                                                       {"locationEntries": [{"value": "Q4", "type": "Port"}, {"value": "6", "type": "Bay"},
                                                                                            {"value": "/rest/enclosures/000000WPSTENC100", "type": "Enclosure"}]}}
                                                                      ],
                        "networkType": "Ethernet", "primaryPortLocation": None, "reachability": None, "manualLoginRedistributionState": "NotSupported",
                        "logicalInterconnectUri": "LE_1Enc-LIG-bay3-1enc_f1682", "connectionMode": "Auto", "lacpTimer": "Short", "nativeNetworkUri": None, "fcNetworkUris": [],
                        "fcoeNetworkUris":[], "state":None, "description":None,
                        "uri":None, "category":"logical-interconnects", "ethernetNetworkType":"Untagged"}
                       ]


uplinkSets_77 = [{"type": "uplink-setV300", "name": "Uplink1",
                  "networkUris": ["eth-10"], "portConfigInfos":[
                      {"desiredSpeed": "Auto", "location":
                       {"locationEntries": [{"value": "Q1:1", "type": "Port"}, {"value": "3", "type": "Bay"},
                                            {"value": "/rest/enclosures/000000WPSTENC100", "type": "Enclosure"}]}},
                      {"desiredSpeed": "Auto", "location": {"locationEntries": [{"value": "Q1:4", "type": "Port"},
                                                                                {"value": "3", "type": "Bay"},
                                                                                {"value": "/rest/enclosures/000000WPSTENC100", "type": "Enclosure"}]}},

                      {"desiredSpeed": "Auto", "location": {"locationEntries": [{"value": "Q2:1", "type": "Port"},
                                                                                {"value": "3", "type": "Bay"},
                                                                                {"value": "/rest/enclosures/000000WPSTENC100", "type": "Enclosure"}]}},
                      {"desiredSpeed": "Auto", "location": {"locationEntries": [{"value": "Q2:4", "type": "Port"},
                                                                                {"value": "3", "type": "Bay"},
                                                                                {"value": "/rest/enclosures/000000WPSTENC100", "type": "Enclosure"}]}},
                      {"desiredSpeed": "Auto", "location":
                       {"locationEntries": [{"value": "Q3:1", "type": "Port"}, {"value": "3", "type": "Bay"},
                                            {"value": "/rest/enclosures/000000WPSTENC100", "type": "Enclosure"}]}},
                      {"desiredSpeed": "Auto", "location":
                       {"locationEntries": [{"value": "Q3:4", "type": "Port"}, {"value": "3", "type": "Bay"},
                                            {"value": "/rest/enclosures/000000WPSTENC100", "type": "Enclosure"}]}},
                      {"desiredSpeed": "Auto", "location":
                       {"locationEntries": [{"value": "Q4:1", "type": "Port"}, {"value": "3", "type": "Bay"},
                                            {"value": "/rest/enclosures/000000WPSTENC100", "type": "Enclosure"}]}},
                      {"desiredSpeed": "Auto", "location":
                       {"locationEntries": [{"value": "Q4:4", "type": "Port"}, {"value": "3", "type": "Bay"},
                                            {"value": "/rest/enclosures/000000WPSTENC100", "type": "Enclosure"}]}}

                  ],
                  "networkType": "Ethernet", "primaryPortLocation": None, "reachability": None, "manualLoginRedistributionState": "NotSupported",
                  "logicalInterconnectUri": "LE_1Enc-LIG-bay3-1enc_f1682", "connectionMode": "Auto", "lacpTimer": "Short", "nativeNetworkUri": "eth-10", "fcNetworkUris": [],
                  "fcoeNetworkUris":[], "state":None, "description":None,
                  "uri":None, "category":"logical-interconnects", "ethernetNetworkType":"Tagged"},


                 ]
uplinkSets_77_bay6 = [{"type": "uplink-setV300", "name": "Uplink1",
                       "networkUris": ["eth-10"], "portConfigInfos":[
                           {"desiredSpeed": "Auto", "location":
                            {"locationEntries": [{"value": "Q1:1", "type": "Port"}, {"value": "3", "type": "Bay"},
                                                 {"value": "/rest/enclosures/000000WPSTENC100", "type": "Enclosure"}]}},
                           {"desiredSpeed": "Auto", "location": {"locationEntries": [{"value": "Q1:4", "type": "Port"},
                                                                                     {"value": "3", "type": "Bay"},
                                                                                     {"value": "/rest/enclosures/000000WPSTENC100", "type": "Enclosure"}]}},

                           {"desiredSpeed": "Auto", "location": {"locationEntries": [{"value": "Q2:1", "type": "Port"},
                                                                                     {"value": "3", "type": "Bay"},
                                                                                     {"value": "/rest/enclosures/000000WPSTENC100", "type": "Enclosure"}]}},
                           {"desiredSpeed": "Auto", "location": {"locationEntries": [{"value": "Q2:4", "type": "Port"},
                                                                                     {"value": "3", "type": "Bay"},
                                                                                     {"value": "/rest/enclosures/000000WPSTENC100", "type": "Enclosure"}]}},
                           {"desiredSpeed": "Auto", "location":
                            {"locationEntries": [{"value": "Q3:1", "type": "Port"}, {"value": "3", "type": "Bay"},
                                                 {"value": "/rest/enclosures/000000WPSTENC100", "type": "Enclosure"}]}},
                           {"desiredSpeed": "Auto", "location":
                            {"locationEntries": [{"value": "Q3:4", "type": "Port"}, {"value": "3", "type": "Bay"},
                                                 {"value": "/rest/enclosures/000000WPSTENC100", "type": "Enclosure"}]}},
                           {"desiredSpeed": "Auto", "location":
                            {"locationEntries": [{"value": "Q4:1", "type": "Port"}, {"value": "6", "type": "Bay"},
                                                 {"value": "/rest/enclosures/000000WPSTENC100", "type": "Enclosure"}]}},
                           {"desiredSpeed": "Auto", "location":
                            {"locationEntries": [{"value": "Q4:4", "type": "Port"}, {"value": "6", "type": "Bay"},
                                                 {"value": "/rest/enclosures/000000WPSTENC100", "type": "Enclosure"}]}}

                       ],
                       "networkType": "Ethernet", "primaryPortLocation": None, "reachability": None, "manualLoginRedistributionState": "NotSupported",
                       "logicalInterconnectUri": "LE_1Enc-LIG-bay3-1enc_f1682", "connectionMode": "Auto", "lacpTimer": "Short", "nativeNetworkUri": "eth-10", "fcNetworkUris": [],
                       "fcoeNetworkUris":[], "state":None, "description":None,
                       "uri":None, "category":"logical-interconnects", "ethernetNetworkType":"Tagged"},


                      ]

uls_Q1_HPCR4 = [{"type": "uplink-setV300", "name": "Uplink1",
                 "networkUris": ["eth-10"], "portConfigInfos":[{"desiredSpeed": "Auto", "location":
                                                                {"locationEntries": [{"value": "Q1", "type": "Port"}, {"value": "3", "type": "Bay"},
                                                                                     {"value": "/rest/enclosures/000000WPSTENC100", "type": "Enclosure"}]}}],
                 "networkType": "Ethernet", "primaryPortLocation": None, "reachability": None, "manualLoginRedistributionState": "NotSupported",
                 "logicalInterconnectUri": "LE_1Enc-LIG-bay3-1enc_f1682", "connectionMode": "Auto", "lacpTimer": "Short", "nativeNetworkUri": "eth-10", "fcNetworkUris": [],
                 "fcoeNetworkUris":[], "state":None, "description":None,
                 "uri":None, "category":"logical-interconnects", "ethernetNetworkType":"Tagged"}]

uls_Q1_HPCR4_1 = [{"type": "uplink-setV300", "name": "Uplink1",
                   "networkUris": ["eth-10"], "portConfigInfos":[{"desiredSpeed": "Speed40G", "location":
                                                                  {"locationEntries": [{"value": "Q1", "type": "Port"}, {"value": "3", "type": "Bay"},
                                                                                       {"value": "/rest/enclosures/000000WPSTENC100", "type": "Enclosure"}]}}],
                   "networkType": "Ethernet", "primaryPortLocation": None, "reachability": None, "manualLoginRedistributionState": "NotSupported",
                   "logicalInterconnectUri": "LE_1Enc-LIG-bay3-1enc_f1682", "connectionMode": "Auto", "lacpTimer": "Short", "nativeNetworkUri": "eth-10", "fcNetworkUris": [],
                   "fcoeNetworkUris":[], "state":None, "description":None,
                   "uri":None, "category":"logical-interconnects", "ethernetNetworkType":"Tagged"}]

uls_Q2_AOC = [{"type": "uplink-setV300", "name": "Uplink1",
               "networkUris": ["eth-10"], "portConfigInfos":[{"desiredSpeed": "Auto", "location":
                                                              {"locationEntries": [{"value": "Q2", "type": "Port"}, {"value": "3", "type": "Bay"},
                                                                                   {"value": "/rest/enclosures/000000WPSTENC100", "type": "Enclosure"}]}}],
               "networkType": "Ethernet", "primaryPortLocation": None, "reachability": None, "manualLoginRedistributionState": "NotSupported",
               "logicalInterconnectUri": "LE_1Enc-LIG-bay3-1enc_f1682", "connectionMode": "Auto", "lacpTimer": "Short", "nativeNetworkUri": "eth-10", "fcNetworkUris": [],
               "fcoeNetworkUris":[], "state":None, "description":None,
               "uri":None, "category":"logical-interconnects", "ethernetNetworkType":"Tagged"}]

uls_Q2_AOC_1 = [{"type": "uplink-setV300", "name": "Uplink1",
                 "networkUris": ["eth-10"], "portConfigInfos":[{"desiredSpeed": "Speed40G", "location":
                                                                {"locationEntries": [{"value": "Q2", "type": "Port"}, {"value": "3", "type": "Bay"},
                                                                                     {"value": "/rest/enclosures/000000WPSTENC100", "type": "Enclosure"}]}}],
                 "networkType": "Ethernet", "primaryPortLocation": None, "reachability": None, "manualLoginRedistributionState": "NotSupported",
                 "logicalInterconnectUri": "LE_1Enc-LIG-bay3-1enc_f1682", "connectionMode": "Auto", "lacpTimer": "Short", "nativeNetworkUri": "eth-10", "fcNetworkUris": [],
                 "fcoeNetworkUris":[], "state":None, "description":None,
                 "uri":None, "category":"logical-interconnects", "ethernetNetworkType":"Tagged"}]

uls_Q3_ACU = [{"type": "uplink-setV300", "name": "Uplink1",
               "networkUris": ["eth-10"], "portConfigInfos":[{"desiredSpeed": "Auto", "location":
                                                              {"locationEntries": [{"value": "Q3", "type": "Port"}, {"value": "3", "type": "Bay"},
                                                                                   {"value": "/rest/enclosures/000000WPSTENC100", "type": "Enclosure"}]}}],
               "networkType": "Ethernet", "primaryPortLocation": None, "reachability": None, "manualLoginRedistributionState": "NotSupported",
               "logicalInterconnectUri": "LE_1Enc-LIG-bay3-1enc_f1682", "connectionMode": "Auto", "lacpTimer": "Short", "nativeNetworkUri": "eth-10", "fcNetworkUris": [],
               "fcoeNetworkUris":[], "state":None, "description":None,
               "uri":None, "category":"logical-interconnects", "ethernetNetworkType":"Tagged"}]

uls_Q3_ACU_1 = [{"type": "uplink-setV300", "name": "Uplink1",
                 "networkUris": ["eth-10"], "portConfigInfos":[{"desiredSpeed": "Speed40G", "location":
                                                                {"locationEntries": [{"value": "Q3", "type": "Port"}, {"value": "3", "type": "Bay"},
                                                                                     {"value": "/rest/enclosures/000000WPSTENC100", "type": "Enclosure"}]}}],
                 "networkType": "Ethernet", "primaryPortLocation": None, "reachability": None, "manualLoginRedistributionState": "NotSupported",
                 "logicalInterconnectUri": "LE_1Enc-LIG-bay3-1enc_f1682", "connectionMode": "Auto", "lacpTimer": "Short", "nativeNetworkUri": "eth-10", "fcNetworkUris": [],
                 "fcoeNetworkUris":[], "state":None, "description":None,
                 "uri":None, "category":"logical-interconnects", "ethernetNetworkType":"Tagged"}]

uls_Q4_ciscosplit = [{"type": "uplink-setV300", "name": "Uplink1",
                      "networkUris": ["eth-10"], "portConfigInfos":[{"desiredSpeed": "Auto", "location":
                                                                     {"locationEntries": [{"value": "Q4", "type": "Port"}, {"value": "3", "type": "Bay"},
                                                                                          {"value": "/rest/enclosures/000000WPSTENC100", "type": "Enclosure"}]}}],
                      "networkType": "Ethernet", "primaryPortLocation": None, "reachability": None, "manualLoginRedistributionState": "NotSupported",
                      "logicalInterconnectUri": "LE_1Enc-LIG-bay3-1enc_f1682", "connectionMode": "Auto", "lacpTimer": "Short", "nativeNetworkUri": "eth-10", "fcNetworkUris": [],
                      "fcoeNetworkUris":[], "state":None, "description":None,
                      "uri":None, "category":"logical-interconnects", "ethernetNetworkType":"Tagged"}]

uls_Q4_ciscosplit_1 = [{"type": "uplink-setV300", "name": "Uplink1",
                        "networkUris": ["eth-10"], "portConfigInfos":[{"desiredSpeed": "Speed40G", "location":
                                                                       {"locationEntries": [{"value": "Q4", "type": "Port"}, {"value": "3", "type": "Bay"},
                                                                                            {"value": "/rest/enclosures/000000WPSTENC100", "type": "Enclosure"}]}}],
                        "networkType": "Ethernet", "primaryPortLocation": None, "reachability": None, "manualLoginRedistributionState": "NotSupported",
                        "logicalInterconnectUri": "LE_1Enc-LIG-bay3-1enc_f1682", "connectionMode": "Auto", "lacpTimer": "Short", "nativeNetworkUri": "eth-10", "fcNetworkUris": [],
                        "fcoeNetworkUris":[], "state":None, "description":None,
                        "uri":None, "category":"logical-interconnects", "ethernetNetworkType":"Tagged"}]

uls_Q3_ciscosplit_2 = [{"type": "uplink-setV300", "name": "Uplink1",
                        "networkUris": ["eth-10"], "portConfigInfos":[{"desiredSpeed": "Auto", "location":
                                                                       {"locationEntries": [{"value": "Q4:1", "type": "Port"}, {"value": "3", "type": "Bay"},
                                                                                            {"value": "/rest/enclosures/000000WPSTENC100", "type": "Enclosure"}]}}],
                        "networkType": "Ethernet", "primaryPortLocation": None, "reachability": None, "manualLoginRedistributionState": "NotSupported",
                        "logicalInterconnectUri": "LE_1Enc-LIG-bay3-1enc_f1682", "connectionMode": "Auto", "lacpTimer": "Short", "nativeNetworkUri": "eth-10", "fcNetworkUris": [],
                        "fcoeNetworkUris":[], "state":None, "description":None,
                        "uri":None, "category":"logical-interconnects", "ethernetNetworkType":"Tagged"}]

uls_Q5_HPJS = [{"type": "uplink-setV300", "name": "Uplink1",
                "networkUris": ["eth-10"], "portConfigInfos":[{"desiredSpeed": "Auto", "location":
                                                               {"locationEntries": [{"value": "Q5", "type": "Port"}, {"value": "3", "type": "Bay"},
                                                                                    {"value": "/rest/enclosures/000000WPSTENC100", "type": "Enclosure"}]}}],
                "networkType": "Ethernet", "primaryPortLocation": None, "reachability": None, "manualLoginRedistributionState": "NotSupported",
                "logicalInterconnectUri": "LE_1Enc-LIG-bay3-1enc_f1682", "connectionMode": "Auto", "lacpTimer": "Short", "nativeNetworkUri": "eth-10", "fcNetworkUris": [],
                "fcoeNetworkUris":[], "state":None, "description":None,
                "uri":None, "category":"logical-interconnects", "ethernetNetworkType":"Tagged"}]

uls_Q5_HPJS_1 = [{"type": "uplink-setV300", "name": "Uplink1",
                  "networkUris": ["eth-10"], "portConfigInfos":[{"desiredSpeed": "Speed40G", "location":
                                                                 {"locationEntries": [{"value": "Q5", "type": "Port"}, {"value": "3", "type": "Bay"},
                                                                                      {"value": "/rest/enclosures/000000WPSTENC100", "type": "Enclosure"}]}}],
                  "networkType": "Ethernet", "primaryPortLocation": None, "reachability": None, "manualLoginRedistributionState": "NotSupported",
                  "logicalInterconnectUri": "LE_1Enc-LIG-bay3-1enc_f1682", "connectionMode": "Auto", "lacpTimer": "Short", "nativeNetworkUri": "eth-10", "fcNetworkUris": [],
                  "fcoeNetworkUris":[], "state":None, "description":None,
                  "uri":None, "category":"logical-interconnects", "ethernetNetworkType":"Tagged"}]


uls_Q6_CU = [{"type": "uplink-setV300", "name": "Uplink1",
              "networkUris": ["eth-10"], "portConfigInfos":[{"desiredSpeed": "Auto", "location":
                                                             {"locationEntries": [{"value": "Q6", "type": "Port"}, {"value": "3", "type": "Bay"},
                                                                                  {"value": "/rest/enclosures/000000WPSTENC100", "type": "Enclosure"}]}}],
              "networkType": "Ethernet", "primaryPortLocation": None, "reachability": None, "manualLoginRedistributionState": "NotSupported",
              "logicalInterconnectUri": "LE_1Enc-LIG-bay3-1enc_f1682", "connectionMode": "Auto", "lacpTimer": "Short", "nativeNetworkUri": "eth-10", "fcNetworkUris": [],
              "fcoeNetworkUris":[], "state":None, "description":None,
              "uri":None, "category":"logical-interconnects", "ethernetNetworkType":"Tagged"}]

uls_Q6_CU_1 = [{"type": "uplink-setV300", "name": "Uplink1",
                "networkUris": ["eth-10"], "portConfigInfos":[{"desiredSpeed": "Speed40G", "location":
                                                               {"locationEntries": [{"value": "Q6", "type": "Port"}, {"value": "3", "type": "Bay"},
                                                                                    {"value": "/rest/enclosures/000000WPSTENC100", "type": "Enclosure"}]}}],
                "networkType": "Ethernet", "primaryPortLocation": None, "reachability": None, "manualLoginRedistributionState": "NotSupported",
                "logicalInterconnectUri": "LE_1Enc-LIG-bay3-1enc_f1682", "connectionMode": "Auto", "lacpTimer": "Short", "nativeNetworkUri": "eth-10", "fcNetworkUris": [],
                "fcoeNetworkUris":[], "state":None, "description":None,
                "uri":None, "category":"logical-interconnects", "ethernetNetworkType":"Tagged"}]

uls_117_HPCR4 = [{"type": "uplink-setV300", "name": "Uplink1",
                  "networkUris": ["eth-10"], "portConfigInfos":[{"desiredSpeed": "Auto", "location":
                                                                 {"locationEntries": [{"value": "Q1", "type": "Port"}, {"value": "3", "type": "Bay"},
                                                                                      {"value": "/rest/enclosures/000000WPSTENC100", "type": "Enclosure"}]}}],
                  "networkType": "Ethernet", "primaryPortLocation": None, "reachability": None, "manualLoginRedistributionState": "NotSupported",
                  "logicalInterconnectUri": "LE_1Enc-LIG-bay3-1enc_f1682", "connectionMode": "Auto", "lacpTimer": "Short", "nativeNetworkUri": "eth-10", "fcNetworkUris": [],
                  "fcoeNetworkUris":[], "state":None, "description":None,
                  "uri":None, "category":"logical-interconnects", "ethernetNetworkType":"Tagged"}]


li_intents_36_val = [["WPSTENC100, interconnect 3, Q1", "40 Gb/s", "10 Gb/s", "Disabled", "Linked"],
                     ["WPSTENC100, interconnect 3, Q2", "Auto", "40 Gb/s", "Enabled", "Linked"],
                     ["WPSTENC100, interconnect 3, Q4:1", "Auto", "0 Gb/s", "n/a", "Unlinked"]]


li_1enc = {'name': 'LE_1Enc-LIG-bay3-1enc'}

enc_groups_1enc = [{'name': 'EG_1Enc_Bay3',
                    'type': 'EnclosureGroupV400',
                    'enclosureTypeUri': '/rest/enclosure-types/SY12000',
                    'stackingMode': 'Enclosure',
                    'ipAddressingMode': 'External',
                    'interconnectBayMappingCount': 0,
                    'enclosureCount': 1,
                    'configurationScript': None,
                    'interconnectBayMappings':
                    [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                     {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                     {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG-bay3-1enc_f1682'},
                     {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                     {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                     {'interconnectBay': 6, 'logicalInterconnectGroupUri': None}
                     ]}]

les_potash_1enc = {'name': 'LE_1Enc', 'enclosureUris': ['ENC:WPSTENC100'],
                   'enclosureGroupUri': 'EG:EG_1Enc_Bay3',
                   'firmwareBaselineUri': None,
                   'forceInstallFirmware': False
                   }

ICM_powercycle = [{'op': 'replace', 'path': '/deviceResetState', 'value': 'Reset'}]
potash_poweroff = [{'op': 'replace', 'path': '/powerState', 'value': 'Off'}]
potash_poweron = [{'op': 'replace', 'path': '/powerState', 'value': 'On'}]

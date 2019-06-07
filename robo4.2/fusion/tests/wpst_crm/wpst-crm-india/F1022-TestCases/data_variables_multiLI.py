def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist


admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}
network_admin = {'userName': 'network', 'password': 'networkadmin'}
storage_admin = {'userName': 'storage', 'password': 'storageadmin'}
backup_admin = {'userName': 'backup', 'password': 'backupadmin'}
server_admin = {'userName': 'server', 'password': 'serveradmin'}

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
licenses_expired = [{'key': 'QBSG A9MA H9PA KHUZ V2B4 HWWV Y9JL KMPL KDND PCJQ 6RMS KHWE JLQ8 7FUK CMRG HPMR UFVU A5K9 EFHC 9SRJ HKDU LWWP 3TPW L9YM QSQM 47AC 9XKR JZ53 P2ZV RHMQ 54ZF BGWB BKTS X5VC LL4U R4WA V886 FCY3 HQT5 6CAD 3WJY YLJ6 CCUG 2EQ7 "24R2-02192-002 T1111A FC_License J4E8IAMANEON"'}]
licenses_invalid = [{'key': 'D9MA H9PA GHUY V2B4 HWWV KMPL B89H MZVU GR4S JHWE JVSH XV5S CMRG HPMR UFVU A5K9 MWHC 9K4K HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'}]


ethernet_networks = [{'name': 'eth-100', 'type': 'ethernet-networkV300', 'vlanId': 100, 'purpose': 'General', 'smartLink': True,
                      'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tagged'},
                     {'name': 'eth-101', 'type': 'ethernet-networkV300', 'vlanId': 102, 'purpose': 'General',
                      'smartLink': True, 'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tagged'}]

fcoe_networks = [{'name': 'FCOE-10', 'type': 'fcoe-networkV300', 'vlanId': 10},
                 {'name': 'FCOE-100', 'type': 'fcoe-networkV300', 'vlanId': 10},
                 {'name': 'FCOE-101', 'type': 'fcoe-networkV300', 'vlanId': 101}]

fc_networks = [{'type': 'fc-networkV300', 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
                'name': 'SAN-1-A', 'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'},
               {'type': 'fc-networkV300', 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
                'name': 'SAN-2-A', 'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'}]

lig_tbird_1enc = {'type': 'logical-interconnect-groupV300',
                  'ethernetSettings': {'type': 'EthernetInterconnectSettingsV201', 'enableIgmpSnooping': False, 'igmpIdleTimeoutInterval': 260, 'enableFastMacCacheFailover': True, 'macRefreshInterval': 5, 'enableNetworkLoopProtection': True, 'enablePauseFloodProtection': True, 'enableRichTLV': False, 'interconnectType': 'Ethernet', 'dependentResourceUri': None, 'name': 'defaultEthernetSwitchSettings', 'category': None, 'uri': '/ethernetSettings'},
                  'description': None,
                  'name': 'LIG-bay3-1enc',
                  'interconnectMapTemplate':
                  {'interconnectMapEntryTemplates': [
                      {'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Enclosure', 'relativeValue': 1}]}, 'permittedInterconnectTypeUri': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
                      {'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 6}, {'type': 'Enclosure', 'relativeValue': 1}]}, 'permittedInterconnectTypeUri': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1}]},
                  'enclosureType': 'SY12000', 'enclosureIndexes': [1], 'interconnectBaySet': '3',
                  'redundancyType': 'Redundant', 'internalNetworkUris': [],
                  'snmpConfiguration': {'type': 'snmp-configuration', 'readCommunity': 'public', 'systemContact': '', 'trapDestinations': None, 'snmpAccess': None, 'enabled': True, 'description': None, 'name': None, 'state': None, 'category': 'snmp-configuration'},
                  'qosConfiguration': None,
                  'uplinkSets': [
                      {'networkUris': ['eth-100'], 'mode':'Auto', 'lacpTimer':'Short', 'primaryPort':None,
                       'logicalPortConfigInfos':[{'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 61}, {'type': 'Enclosure', 'relativeValue': 1}]}}],
                       'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'name': 'eth-100'},
                      {'networkUris': ['SAN-1-A'], 'mode':'Auto', 'lacpTimer':'Short', 'primaryPort':None,
                       'logicalPortConfigInfos':[{'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 72}, {'type': 'Enclosure', 'relativeValue': 1}]}}],
                       'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'name': 'SAN-1-A'},
                      {'networkUris': ['FCOE-100'], 'mode':'Auto', 'lacpTimer':'Short', 'primaryPort':None,
                       'logicalPortConfigInfos':[{'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 66}, {'type': 'Enclosure', 'relativeValue': 1}]}}],
                       'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'name': 'FCOE-100'}
                  ]}

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
                     {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG-bay3-1enc'},
                     {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                     {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                     {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG-bay3-1enc'}
                     ]}]

les_potash_1enc = {'name': 'LE_1Enc', 'enclosureUris': ['ENC:EM1FFFF500'],
                   'enclosureGroupUri': 'EG:EG_1Enc_Bay3',
                   'firmwareBaselineUri': None,
                   'forceInstallFirmware': False
                   }

ICM_powercycle = [{'op': 'replace', 'path': '/deviceResetState', 'value': 'Reset'}]
lig_tbird_1enc_Aside = {'type': 'logical-interconnect-groupV300',
                        'ethernetSettings': {'type': 'EthernetInterconnectSettingsV201', 'enableIgmpSnooping': False, 'igmpIdleTimeoutInterval': 260, 'enableFastMacCacheFailover': True, 'macRefreshInterval': 5, 'enableNetworkLoopProtection': True, 'enablePauseFloodProtection': True, 'enableRichTLV': False, 'interconnectType': 'Ethernet', 'dependentResourceUri': None, 'name': 'defaultEthernetSwitchSettings', 'category': None, 'uri': '/ethernetSettings'},
                        'description': None,
                        'name': 'LIG-bay3-1enc_A',
                        'interconnectMapTemplate':
                        {'interconnectMapEntryTemplates': [
                            {'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Enclosure', 'relativeValue': 1}]}, 'permittedInterconnectTypeUri': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1}]},
                            'enclosureType': 'SY12000', 'enclosureIndexes': [1], 'interconnectBaySet': '3',
                            'redundancyType': 'NonRedundantASide', 'internalNetworkUris': [],
                            'snmpConfiguration': {'type': 'snmp-configuration', 'readCommunity': 'public', 'systemContact': '', 'trapDestinations': None, 'snmpAccess': None, 'enabled': True, 'description': None, 'name': None, 'state': None, 'category': 'snmp-configuration'},
                            'qosConfiguration': None,
                            'uplinkSets': [
                            {'networkUris': ['eth-100'], 'mode':'Auto', 'lacpTimer':'Short', 'primaryPort':None,
                             'logicalPortConfigInfos':[{'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 61}, {'type': 'Enclosure', 'relativeValue': 1}]}}],
                             'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'name': 'eth-100'},
                            {'networkUris': ['SAN-1-A'], 'mode':'Auto', 'lacpTimer':'Short', 'primaryPort':None,
                             'logicalPortConfigInfos':[{'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 72}, {'type': 'Enclosure', 'relativeValue': 1}]}}],
                             'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'name': 'SAN-1-A'},
                            {'networkUris': ['FCOE-100'], 'mode':'Auto', 'lacpTimer':'Short', 'primaryPort':None,
                             'logicalPortConfigInfos':[{'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 66}, {'type': 'Enclosure', 'relativeValue': 1}]}}],
                             'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'name': 'FCOE-100'}
                        ]}

lig_tbird_1enc_Bside = {'type': 'logical-interconnect-groupV300',
                        'ethernetSettings': {'type': 'EthernetInterconnectSettingsV201', 'enableIgmpSnooping': False, 'igmpIdleTimeoutInterval': 260, 'enableFastMacCacheFailover': True, 'macRefreshInterval': 5, 'enableNetworkLoopProtection': True, 'enablePauseFloodProtection': True, 'enableRichTLV': False, 'interconnectType': 'Ethernet', 'dependentResourceUri': None, 'name': 'defaultEthernetSwitchSettings', 'category': None, 'uri': '/ethernetSettings'},
                        'description': None,
                        'name': 'LIG-bay3-1enc_B',
                        'interconnectMapTemplate':
                        {'interconnectMapEntryTemplates': [
                            {'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 6}, {'type': 'Enclosure', 'relativeValue': 1}]}, 'permittedInterconnectTypeUri': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1}]},
                        'enclosureType': 'SY12000', 'enclosureIndexes': [1], 'interconnectBaySet': '3',
                                                    'redundancyType': 'NonRedundantBSide', 'internalNetworkUris': [],
                                                    'snmpConfiguration': {'type': 'snmp-configuration', 'readCommunity': 'public', 'systemContact': '', 'trapDestinations': None, 'snmpAccess': None, 'enabled': True, 'description': None, 'name': None, 'state': None, 'category': 'snmp-configuration'},
                                                    'qosConfiguration': None,
                                                    'uplinkSets': [
                                                    {'networkUris': ['eth-101'], 'mode':'Auto', 'lacpTimer':'Short', 'primaryPort':None,
                                                     'logicalPortConfigInfos':[{'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 6}, {'type': 'Port', 'relativeValue': 61}, {'type': 'Enclosure', 'relativeValue': 1}]}}],
                                                     'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'name': 'eth-101'},
                                                    {'networkUris': ['SAN-2-A'], 'mode':'Auto', 'lacpTimer':'Short', 'primaryPort':None,
                                                     'logicalPortConfigInfos':[{'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 6}, {'type': 'Port', 'relativeValue': 72}, {'type': 'Enclosure', 'relativeValue': 1}]}}],
                                                     'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'name': 'SAN-2-A'},
                                                    {'networkUris': ['FCOE-101'], 'mode':'Auto', 'lacpTimer':'Short', 'primaryPort':None,
                                                     'logicalPortConfigInfos':[{'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 6}, {'type': 'Port', 'relativeValue': 66}, {'type': 'Enclosure', 'relativeValue': 1}]}}],
                                                     'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'name': 'FCOE-101'}
                        ]
                        }


enc_groups_1enc_Multi = [{'name': 'EG_1Enc_Bay3_Multi',
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
                           {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG-bay3-1enc_A'},
                           {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                           {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                           {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG-bay3-1enc_B'}
                           ]}]

li_1enc_A = {'name': 'LE_1Enc-LIG-bay3-1enc_A'}
li_1enc_B = {'name': 'LE_1Enc-LIG-bay3-1enc_B'}


les_potash_1enc_Multi = {'name': 'LE_1Enc',
                         'enclosureUris': ['ENC:EM1FFFF500'],
                         'enclosureGroupUri': 'EG:EG_1Enc_Bay3_Multi',
                         'firmwareBaselineUri': None,
                         'forceInstallFirmware': False
                         }

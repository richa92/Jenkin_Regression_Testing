def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist

lig1_ethernetsettings = {'type': 'EthernetInterconnectSettingsV3','enableRichTLV': True,'interconnectType': 'Ethernet'}

login_details = {'userName': 'Administrator', 'password': 'hpvse123'}
network_login_details = {'userName': 'network', 'password': 'hpvse123'}
server_login_details = {'userName': 'server', 'password': 'hpvse123'}
storage_login_details = {'userName': 'storage', 'password': 'hpvse123'}
software_login_details = {'userName': 'software', 'password': 'hpvse123'}
backup_login_details = {'userName': 'backup', 'password': 'hpvse123'}

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}
network_admin = {'userName': 'network', 'password': 'networkadmin'}
storage_admin = {'userName': 'storage', 'password': 'storageadmin'}
backup_admin = {'userName': 'backup', 'password': 'backupadmin'}
server_admin = {'userName': 'server', 'password': 'serveradmin'}
read_only = {'userName': 'readonly', 'password': 'readonly'}

upgrade_firmware_path = '/rest/firmware-drivers/SPPgen9snap6_2016_0517_107'
downgrade_firmware_path = '/rest/firmware-drivers/CAR-26-Snap6-bp-Hf115-C26-CLSyl-101-2016-03-09-01'
enclosure_name = ''
server_name = ''

users = [{'userName': 'server', 'password': 'serveradmin', 'fullName': 'Sarah', 'roles': ['Server administrator'], 'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'network', 'password': 'networkadmin', 'fullName': 'Nat', 'roles': ['Network administrator'], 'emailAddress': 'nat@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'backup', 'password': 'backupadmin', 'fullName': 'Backup', 'roles': ['Backup administrator'], 'emailAddress': 'backup@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'readonly', 'password': 'readonly', 'fullName': 'Rheid', 'roles': ['Read only'], 'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'storage', 'password': 'storageadmin', 'fullName': 'Rheid', 'roles': ['Storage administrator'], 'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'}
         ]

licenses_1 = [{'key':'YB2C D9MA H9PA 8HU3 V2B4 HWWV Y9JL KMPL B89H MZVU GR4S JHWE 9QSP XFR8 CMRG HPMR UFVU A5K9 MWHC 9K4K HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'},
            {'key': 'ABSE D9MA H9P9 CHUZ V2B4 HWWV Y9JL KMPL B89H MZVU GR4S JHWE 9FQP XN5W CMRG HPMR UFVU A5K9 MWHC 9K4K HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'}
            ]

licenses_2 = [{'key':'YBCG D9MA H9PA GHUY V2B4 HWWV Y9JL KMPL B89H MZVU GR4S JHWE JVSH XV5S CMRG HPMR UFVU A5K9 MWHC 9K4K HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'},{'key':'YBKA D9MA H9P9 8HX3 V2B4 HWWV Y9JL KMPL B89H MZVU GR4S JHWE J2SP XNZ8 CMRG HPMR UFVU A5K9 MWHC 9K4K HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'}]

licenses_expired=[{'key':'QBSG A9MA H9PA KHUZ V2B4 HWWV Y9JL KMPL KDND PCJQ 6RMS KHWE JLQ8 7FUK CMRG HPMR UFVU A5K9 EFHC 9SRJ HKDU LWWP 3TPW L9YM QSQM 47AC 9XKR JZ53 P2ZV RHMQ 54ZF BGWB BKTS X5VC LL4U R4WA V886 FCY3 HQT5 6CAD 3WJY YLJ6 CCUG 2EQ7 "24R2-02192-002 T1111A FC_License J4E8IAMANEON"'}]


licenses_invalid =[{'key':'D9MA H9PA GHUY V2B4 HWWV KMPL B89H MZVU GR4S JHWE JVSH XV5S CMRG HPMR UFVU A5K9 MWHC 9K4K HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'}]


ethernet_networks_TBird = [{'name': 'eth-100',
                      'type': 'ethernet-networkV300',
                      'vlanId': 100,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'},
                           
                      {'name': 'eth-102',
                      'type': 'ethernet-networkV300',
                      'vlanId': 102,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'} ]
                     
fcoe_networks = {'FCOE-10': {'name': 'FCOE-10', 'type': 'fcoe-networkV300', 'vlanId': 10},
                 'FCOE-100': {'name': 'FCOE-100', 'type': 'fcoe-networkV300', 'vlanId': 10},
                 'FCOE-101': {'name': 'FCOE-101', 'type': 'fcoe-networkV300', 'vlanId': 101},
                 'FCOE-2000': {'name': 'FCOE-2000', 'type': 'fcoe-networkV300', 'vlanId': 2000},
                 'FCOE-4095': {'name': 'FCOE-4095', 'type': 'fcoe-networkV300', 'vlanId': 4095}}



fc_networks = [{'type': 'fc-networkV300',
                'linkStabilityTime': 30,
                'autoLoginRedistribution': True,
                'name': 'SAN-1-A',
                'connectionTemplateUri': None,
                'managedSanUri': None,
                'fabricType': 'FabricAttach'},
               
               {'type': 'fc-networkV300',
                'linkStabilityTime': 30,
                'autoLoginRedistribution': True,
                'name': 'SAN-2-A',
                'connectionTemplateUri': None,
                'managedSanUri': None,
                'fabricType': 'FabricAttach'},    
               
               {'type': 'fc-networkV300',
                'linkStabilityTime': 30,
                'autoLoginRedistribution': True,
                'name': 'SAN-11-A',
                'connectionTemplateUri': None,
                'managedSanUri': None,
                'fabricType': 'FabricAttach'},
               
               {'type': 'fc-networkV300',
                'linkStabilityTime': 30,
                'autoLoginRedistribution': True,
                'name': 'SAN-21-A',
                'connectionTemplateUri': None,
                'managedSanUri': None,
                'fabricType': 'FabricAttach'}
                          
               
               ]                     

carbon_fc_networks = [{'type': 'fc-networkV300',
                'linkStabilityTime': 30,
                'autoLoginRedistribution': True,
                'name': 'FC_FA_1',
                'connectionTemplateUri': None,
                'managedSanUri': None,
                'fabricType': 'FabricAttach'},
               
               {'type': 'fc-networkV300',
                'linkStabilityTime': 30,
                'autoLoginRedistribution': True,
                'name': 'FC_FA_2',
                'connectionTemplateUri': None,
                'managedSanUri': None,
                'fabricType': 'FabricAttach'},    
               
               {'type': 'fc-networkV300',
                'linkStabilityTime': 30,
                'autoLoginRedistribution': True,
                'name': 'FC_FA_4',
                'connectionTemplateUri': None,
                'managedSanUri': None,
                'fabricType': 'FabricAttach'},
               
               {'type': 'fc-networkV300',
                'linkStabilityTime': 30,
                'autoLoginRedistribution': True,
                'name': 'FC_FA_5',
                'connectionTemplateUri': None,
                'managedSanUri': None,
                'fabricType': 'FabricAttach'}
               ]                     


LE_edit_intent_yes = {
           "type":"LogicalEnclosureV300",
           "enclosureGroupUri":"enc_groups_potash",
           "enclosureUris":["/rest/enclosures/0000000000A66101", "/rest/enclosures/0000000000A66102", "/rest/enclosures/0000000000A66103"],
           "enclosures":{"/rest/enclosures/0000000000A66101":{"interconnectBays":[{"bayNumber":1,"licenseIntent":"No"}, 
            {
                "bayNumber":2,"licenseIntent":"Yes"}, {
                "bayNumber":3,"licenseIntent":"No"}, {
                "bayNumber":4,"licenseIntent":"No"}, {
                "bayNumber":5,"licenseIntent":"No"}, {
                "bayNumber":6,"licenseIntent":"No"}],
            "enclosureUri":"/rest/enclosures/0000000000A66101"},
                         "/rest/enclosures/0000000000A66102":{"interconnectBays":[{"bayNumber":1,"licenseIntent":"No"}, {
                "bayNumber":2,"licenseIntent":"No"}, {
                "bayNumber":3,"licenseIntent":"No"}, {
                "bayNumber":4,"licenseIntent":"No"}, {
                "bayNumber":5,"licenseIntent":"Yes"}, {
                "bayNumber":6,"licenseIntent":"No"}],
            "enclosureUri":"/rest/enclosures/0000000000A66102"},
        "/rest/enclosures/0000000000A66103":{"interconnectBays":[{"bayNumber":1,"licenseIntent":"No"}, {
                "bayNumber":2,"licenseIntent":"No"}, {
                "bayNumber":3,"licenseIntent":"No"}, {
                "bayNumber":4,"licenseIntent":"No"}, {
                "bayNumber":5,"licenseIntent":"No"}, {
                "bayNumber":6,"licenseIntent":"No"}],
            "enclosureUri":"/rest/enclosures/0000000000A66103"}
    },
    "logicalInterconnectUris":[],"ipAddressingMode":"External","ipv4Ranges":[],"powerMode":"RedundantPowerFeed",
    "firmware":{"firmwareBaselineUri":None,"firmwareUpdateOn":None,"forceInstallFirmware":False,"logicalInterconnectUpdateMode":"Parallel","validateIfLIFirmwareUpdateIsNonDisruptive":False,"updateFirmwareOnUnmanagedInterconnect":False},
    "scalingState":"NotScaling",
    "name":"LE",
    "state":"Consistent",
    "uri":"LE",
    "category":"logical-enclosures"
    }


LE_edit_intent_no = {
           "type":"LogicalEnclosureV300",
           "enclosureGroupUri":"enc_groups_potash",
           "enclosureUris":["/rest/enclosures/0000000000A66101", "/rest/enclosures/0000000000A66102", "/rest/enclosures/0000000000A66103"],
           "enclosures":{"/rest/enclosures/0000000000A66101":{"interconnectBays":[{"bayNumber":1,"licenseIntent":"No"}, 
            {
                "bayNumber":2,"licenseIntent":"No"}, {
                "bayNumber":3,"licenseIntent":"No"}, {
                "bayNumber":4,"licenseIntent":"No"}, {
                "bayNumber":5,"licenseIntent":"No"}, {
                "bayNumber":6,"licenseIntent":"No"}],
            "enclosureUri":"/rest/enclosures/0000000000A66101"},
                         "/rest/enclosures/0000000000A66102":{"interconnectBays":[{"bayNumber":1,"licenseIntent":"No"}, {
                "bayNumber":2,"licenseIntent":"No"}, {
                "bayNumber":3,"licenseIntent":"No"}, {
                "bayNumber":4,"licenseIntent":"No"}, {
                "bayNumber":5,"licenseIntent":"No"}, {
                "bayNumber":6,"licenseIntent":"No"}],
            "enclosureUri":"/rest/enclosures/0000000000A66102"},
        "/rest/enclosures/0000000000A66103":{"interconnectBays":[{"bayNumber":1,"licenseIntent":"No"}, {
                "bayNumber":2,"licenseIntent":"No"}, {
                "bayNumber":3,"licenseIntent":"No"}, {
                "bayNumber":4,"licenseIntent":"No"}, {
                "bayNumber":5,"licenseIntent":"No"}, {
                "bayNumber":6,"licenseIntent":"No"}],
            "enclosureUri":"/rest/enclosures/0000000000A66103"}
    },
    "logicalInterconnectUris":[],"ipAddressingMode":"External","ipv4Ranges":[],"powerMode":"RedundantPowerFeed",
    "firmware":{"firmwareBaselineUri":None,"firmwareUpdateOn":None,"forceInstallFirmware":False,"logicalInterconnectUpdateMode":"Parallel","validateIfLIFirmwareUpdateIsNonDisruptive":False,"updateFirmwareOnUnmanagedInterconnect":False},
    "scalingState":"NotScaling",
    "name":"LE",
    "state":"Consistent",
    "uri":"LE",
    "category":"logical-enclosures"
    }





enc_groups_potash_3enc = [{'name': 'enc_groups_potash',
               'type': 'EnclosureGroupV300',
               'enclosureTypeUri': '/rest/enclosure-types/SY12000',
               'stackingMode': 'Enclosure',
               'ipAddressingMode': "External",
               'interconnectBayMappingCount': 0,
               'enclosureCount': 3,
               'configurationScript': None,
               'interconnectBayMappings':
                    [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 3, 'logicalInterconnectGroupUri': "LIG:lig_tbird21"},
                    {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 6, 'logicalInterconnectGroupUri': "LIG:lig_tbird21"}
                    ]}]


enc_groups_potash_2enc = [{'name': 'enc_groups_potash',
               'type': 'EnclosureGroupV300',
               'enclosureTypeUri': '/rest/enclosure-types/SY12000',
               'stackingMode': 'Enclosure',
               'ipAddressingMode': "External",
               'interconnectBayMappingCount': 0,
               'enclosureCount': 2,
               'configurationScript': None,
               'interconnectBayMappings':
                    [{'interconnectBay': 1, "enclosureIndex":1, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 2, "enclosureIndex":1, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 3, "enclosureIndex":1, 'logicalInterconnectGroupUri': "LIG:lig_tbird21"},
                    {'interconnectBay': 4, "enclosureIndex":1, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 5, "enclosureIndex":1, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 6, "enclosureIndex":1, 'logicalInterconnectGroupUri': "LIG:lig_tbird21"}
                    ]}]

enc_groups_carbon_a1 = [{'name': 'enc_groups_carbon_a_1',
               'type': 'EnclosureGroupV300',
               'enclosureTypeUri': '/rest/enclosure-types/SY12000',
               'stackingMode': 'Enclosure',
               'ipAddressingMode': "External",
               'interconnectBayMappingCount': 0,
               'enclosureCount': 1,
               'configurationScript': None,
               'interconnectBayMappings':
                    [{'interconnectBay': 1, "enclosureIndex":1, 'logicalInterconnectGroupUri': "LIG:lig_a_1"},
                    {'interconnectBay': 2, "enclosureIndex":1, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 3, "enclosureIndex":1, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 4, "enclosureIndex":1, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 5, "enclosureIndex":1, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 6, "enclosureIndex":1, 'logicalInterconnectGroupUri': None}
                    ]}]

enc_groups_carbon_b4 = [{'name': 'enc_groups_carbon_b_4',
               'type': 'EnclosureGroupV300',
               'enclosureTypeUri': '/rest/enclosure-types/SY12000',
               'stackingMode': 'Enclosure',
               'ipAddressingMode': "External",
               'interconnectBayMappingCount': 0,
               'enclosureCount': 1,
               'configurationScript': None,
               'interconnectBayMappings':
                    [{'interconnectBay': 1, "enclosureIndex":1, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 2, "enclosureIndex":1, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 3, "enclosureIndex":1, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 4, "enclosureIndex":1, 'logicalInterconnectGroupUri': "LIG:lig_b_4"},
                    {'interconnectBay': 5, "enclosureIndex":1, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 6, "enclosureIndex":1, 'logicalInterconnectGroupUri': None}
                    ]}]

enc_groups_carbon_1_4 = [{'name': 'enc_groups_carbon_1_4',
               'type': 'EnclosureGroupV300',
               'enclosureTypeUri': '/rest/enclosure-types/SY12000',
               'stackingMode': 'Enclosure',
               'ipAddressingMode': "External",
               'interconnectBayMappingCount': 0,
               'enclosureCount': 1,
               'configurationScript': None,
               'interconnectBayMappings':
                    [{'interconnectBay': 1, "enclosureIndex":1, 'logicalInterconnectGroupUri': "LIG:lig_1_4"},
                    {'interconnectBay': 2, "enclosureIndex":1, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 3, "enclosureIndex":1, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 4, "enclosureIndex":1, 'logicalInterconnectGroupUri': "LIG:lig_1_4"},
                    {'interconnectBay': 5, "enclosureIndex":1, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 6, "enclosureIndex":1, 'logicalInterconnectGroupUri': None}
                    ]}]

enc_groups_carbon_a2 = [{'name': 'enc_groups_carbon_a_2',
               'type': 'EnclosureGroupV300',
               'enclosureTypeUri': '/rest/enclosure-types/SY12000',
               'stackingMode': 'Enclosure',
               'ipAddressingMode': "External",
               'interconnectBayMappingCount': 0,
               'enclosureCount': 1,
               'configurationScript': None,
               'interconnectBayMappings':
                    [{'interconnectBay': 1, "enclosureIndex":1, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 2, "enclosureIndex":1, 'logicalInterconnectGroupUri': "LIG:lig_a_2"},
                    {'interconnectBay': 3, "enclosureIndex":1, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 4, "enclosureIndex":1, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 5, "enclosureIndex":1, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 6, "enclosureIndex":1, 'logicalInterconnectGroupUri': None}
                    ]}]

enc_groups_carbon_b5 = [{'name': 'enc_groups_carbon_b_5',
               'type': 'EnclosureGroupV300',
               'enclosureTypeUri': '/rest/enclosure-types/SY12000',
               'stackingMode': 'Enclosure',
               'ipAddressingMode': "External",
               'interconnectBayMappingCount': 0,
               'enclosureCount': 1,
               'configurationScript': None,
               'interconnectBayMappings':
                    [{'interconnectBay': 1, "enclosureIndex":1, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 2, "enclosureIndex":1, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 3, "enclosureIndex":1, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 4, "enclosureIndex":1, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 5, "enclosureIndex":1, 'logicalInterconnectGroupUri': "LIG:lig_b_5"},
                    {'interconnectBay': 6, "enclosureIndex":1, 'logicalInterconnectGroupUri': None}
                    ]}]

enc_groups_carbon_2_5 = [{'name': 'enc_groups_carbon_2_5',
               'type': 'EnclosureGroupV300',
               'enclosureTypeUri': '/rest/enclosure-types/SY12000',
               'stackingMode': 'Enclosure',
               'ipAddressingMode': "External",
               'interconnectBayMappingCount': 0,
               'enclosureCount': 1,
               'configurationScript': None,
               'interconnectBayMappings':
                    [{'interconnectBay': 1, "enclosureIndex":1, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 2, "enclosureIndex":1, 'logicalInterconnectGroupUri': "LIG:lig_2_5"},
                    {'interconnectBay': 3, "enclosureIndex":1, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 4, "enclosureIndex":1, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 5, "enclosureIndex":1, 'logicalInterconnectGroupUri': "LIG:lig_2_5"},
                    {'interconnectBay': 6, "enclosureIndex":1, 'logicalInterconnectGroupUri': None}
                    ]}]


uplink_sets_Licensing = [{"type":"uplink-setV300",
                         "name":"SAN-1-A","networkUris":[],
                         "portConfigInfos":[{"desiredSpeed":"Auto",
                                             "location":{"locationEntries":[{"value":"Q1:3","type":"Port"},
                                                                            {"value":3,"type":"Bay"},
                                                                            {"value":"/rest/enclosures/000000FVTVP30001","type":"Enclosure"}]}}],
                         "networkType":"FibreChannel",
                         "primaryPortLocation":None,
                         "reachability":None,
                         "manualLoginRedistributionState":"Supported",
                         "logicalInterconnectUri":"LE_POTASH-lig_tbird21",
                         "connectionMode":"Auto","lacpTimer":"Short","nativeNetworkUri":None,
                         "fcNetworkUris":['SAN-1-A'],
                         "fcoeNetworkUris":[]},
                         
                         {"type":"uplink-setV300",
                         "name":"SAN-11-A","networkUris":[],
                         "portConfigInfos":[{"desiredSpeed":"Auto",
                                             "location":{"locationEntries":[{"value":"Q2:2","type":"Port"},
                                                                            {"value":3,"type":"Bay"},
                                                                            {"value":"/rest/enclosures/000000FVTVP30001","type":"Enclosure"}]}}],
                         "networkType":"FibreChannel",
                         "primaryPortLocation":None,
                         "reachability":None,
                         "manualLoginRedistributionState":"Supported",
                         "logicalInterconnectUri":"LE_POTASH-lig_tbird21",
                         "connectionMode":"Auto","lacpTimer":"Short","nativeNetworkUri":None,
                         "fcNetworkUris":['SAN-11-A'],
                         "fcoeNetworkUris":[]}
                         ]
                         
uplink_sets_Licensing_2 =  [{"type":"uplink-setV300",
                         "name":"SAN-2-A","networkUris":[],
                         "portConfigInfos":[{"desiredSpeed":"Auto",
                                             "location":{"locationEntries":[{"value":"Q1:2","type":"Port"},
                                                                            {"value":2,"type":"Bay"},
                                                                            {"value":"/rest/enclosures/000000FVTVP30001","type":"Enclosure"}]}}],
                         "networkType":"FibreChannel",
                         "primaryPortLocation":None,
                         "reachability":None,
                         "manualLoginRedistributionState":"Supported",
                         "logicalInterconnectUri":"LE_POTASH-lig_tbird_bayset2",
                         "connectionMode":"Auto","lacpTimer":"Short","nativeNetworkUri":None,
                         "fcNetworkUris":['SAN-2-A'],
                         "fcoeNetworkUris":[]},
                         
                         
                         {"type":"uplink-setV300",
                         "name":"SAN-21-A","networkUris":[],
                         "portConfigInfos":[{"desiredSpeed":"Auto",
                                             "location":{"locationEntries":[{"value":"Q2:2","type":"Port"},
                                                                            {"value":2,"type":"Bay"},
                                                                            {"value":"/rest/enclosures/000000FVTVP30001","type":"Enclosure"}]}}],
                         "networkType":"FibreChannel",
                         "primaryPortLocation":None,
                         "reachability":None,
                         "manualLoginRedistributionState":"Supported",
                         "logicalInterconnectUri":"LE_POTASH-lig_tbird_bayset2",
                         "connectionMode":"Auto","lacpTimer":"Short","nativeNetworkUri":None,
                         "fcNetworkUris":['SAN-21-A'],
                         "fcoeNetworkUris":[]}
                         
                         ]


carbon_fc_uplink_sets = [{"type":"uplink-setV300",
                         "name":"CAR_SAN-A1","networkUris":[],
                         "portConfigInfos":[{"desiredSpeed":"Auto",
                                             "location":{"locationEntries":[{"value":"X1","type":"Port"},
                                                                            {"value":1,"type":"Bay"},
                                                                            {"value":"/rest/enclosures/0000000000A66101","type":"Enclosure"}]}}],
                         "networkType":"FibreChannel",
                         "primaryPortLocation":None,
                         "reachability":None,
                         "manualLoginRedistributionState":"Supported",
                         "logicalInterconnectUri":"lig_1_4",
                         "connectionMode":"Auto","lacpTimer":"Short","nativeNetworkUri":None,
                         "fcNetworkUris":['SAN-1-A'],
                         "fcoeNetworkUris":[]},
                         
                         {"type":"uplink-setV300",
                         "name":"SAN-11-A","networkUris":[],
                         "portConfigInfos":[{"desiredSpeed":"Auto",
                                             "location":{"locationEntries":[{"value":"X2","type":"Port"},
                                                                            {"value":2,"type":"Bay"},
                                                                            {"value":"/rest/enclosures/0000000000A66101","type":"Enclosure"}]}}],
                         "networkType":"FibreChannel",
                         "primaryPortLocation":None,
                         "reachability":None,
                         "manualLoginRedistributionState":"Supported",
                         "logicalInterconnectUri":"lig_1_4",
                         "connectionMode":"Auto","lacpTimer":"Short","nativeNetworkUri":None,
                         "fcNetworkUris":['SAN-11-A'],
                         "fcoeNetworkUris":[]}
                         ]


les_potash= {'name': 'LE_POTASH',
        #'enclosureUris': ['ENC:HD345r'],   #REAL
        'enclosureUris': ['ENC:0000A66101','ENC:0000A66102','ENC:0000A66103'],  # DCS
        'enclosureGroupUri': 'EG:enc_groups_potash',
        'firmwareBaselineUri': None,
        'forceInstallFirmware': False
        }


les_potash_1enc= {'name': 'LE_POTASH',
        #'enclosureUris': ['ENC:HD345r'],   #REAL
        'enclosureUris': ['ENC:0000A66101'],  # DCS
        'enclosureGroupUri': 'EG:enc_groups_potash',
        'firmwareBaselineUri': None,
        'forceInstallFirmware': False
        }

les_potash_2enc= {'name': 'LE_POTASH',
        
        'enclosureUris': ['ENC:FVTVP30001','ENC:FVTVP30002'],  # REAL
        'enclosureGroupUri': 'EG:enc_groups_potash',
        'firmwareBaselineUri': None,
        'forceInstallFirmware': False
        }

lig_tbird_1enc = {"type":"logical-interconnect-groupV300",
"ethernetSettings":{"type":"EthernetInterconnectSettingsV201","enableIgmpSnooping":False,"igmpIdleTimeoutInterval":260,"enableFastMacCacheFailover":True,"macRefreshInterval":5,"enableNetworkLoopProtection":True,"enablePauseFloodProtection":True,"enableRichTLV":False,"interconnectType":"Ethernet","dependentResourceUri":None,"name":"defaultEthernetSwitchSettings","category":None,"uri":"/ethernetSettings"},
"description":None,
"name":"lig_tbird21",
"interconnectMapTemplate":
{"interconnectMapEntryTemplates":[
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":3},{"type":"Enclosure","relativeValue":1}]},"permittedInterconnectTypeUri":"Virtual Connect SE 40Gb F8 Module for Synergy - 794502-B23","enclosureIndex":1},
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":6},{"type":"Enclosure","relativeValue":1}]},"permittedInterconnectTypeUri":"Virtual Connect SE 40Gb F8 Module for Synergy - 794502-B23","enclosureIndex":1}
]},
"enclosureType":"SY12000",
"enclosureIndexes":[1],
"interconnectBaySet":"3",
"redundancyType":"Redundant",
"internalNetworkUris":[],
"snmpConfiguration":{"type":"snmp-configuration","readCommunity":"public","systemContact":"","trapDestinations":None,"snmpAccess":None,"enabled":True,"description":None,"name":None,"state":None,"category":"snmp-configuration"},
"qosConfiguration":None,
"uplinkSets":[
{"networkUris":["eth-100"],"mode":"Auto","lacpTimer":"Short","primaryPort":None,
"logicalPortConfigInfos":[{"desiredSpeed":"Auto","logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":3},{"type":"Port","relativeValue":62},{"type":"Enclosure","relativeValue":1}]}}],
"networkType":"Ethernet","ethernetNetworkType":"Tagged","name":"eth-100"},
 {"networkUris":["FCOE-100"],"mode":"Auto","lacpTimer":"Short","primaryPort":None,
"logicalPortConfigInfos":[{"desiredSpeed":"Auto","logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":3},{"type":"Port","relativeValue":63},{"type":"Enclosure","relativeValue":1}]}}],
"networkType":"Ethernet","ethernetNetworkType":"Tagged","name":"FCOE-100"}            
 ]
 }

lig_tbird_a_1 = {"type":"logical-interconnect-groupV300",
"ethernetSettings":{"type":"EthernetInterconnectSettingsV201","enableIgmpSnooping":False,"igmpIdleTimeoutInterval":260,"enableFastMacCacheFailover":True,"macRefreshInterval":5,"enableNetworkLoopProtection":True,"enablePauseFloodProtection":True,"enableRichTLV":False,"interconnectType":"Ethernet","dependentResourceUri":None,"name":"defaultEthernetSwitchSettings","category":None,"uri":"/ethernetSettings"},
"description":None,
"name":"lig_a_1",
"interconnectMapTemplate":
{"interconnectMapEntryTemplates":[
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":1},{"type":"Enclosure","relativeValue":1}]},"permittedInterconnectTypeUri":"Virtual Connect SE 16Gb FC Module for Synergy","enclosureIndex":-1}
]},
"enclosureType":"SY12000",
"enclosureIndexes":[-1],
"interconnectBaySet":"1",
"redundancyType":"NonRedundantASide",
"internalNetworkUris":[],
"snmpConfiguration":{"type":"snmp-configuration","readCommunity":"public","systemContact":"","trapDestinations":None,"snmpAccess":None,"enabled":True,"description":None,"name":None,"state":None,"category":"snmp-configuration"},
"qosConfiguration":None,
"uplinkSets":[]
 }

lig_tbird_a_1_upl = {"type":"logical-interconnect-groupV300",
"ethernetSettings":{"type":"EthernetInterconnectSettingsV201","enableIgmpSnooping":False,"igmpIdleTimeoutInterval":260,"enableFastMacCacheFailover":True,"macRefreshInterval":5,"enableNetworkLoopProtection":True,"enablePauseFloodProtection":True,"enableRichTLV":False,"interconnectType":"Ethernet","dependentResourceUri":None,"name":"defaultEthernetSwitchSettings","category":None,"uri":"/ethernetSettings"},
"description":None,
"name":"lig_a_1",
"interconnectMapTemplate":
{"interconnectMapEntryTemplates":[
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":1},{"type":"Enclosure","relativeValue":-1}]},"permittedInterconnectTypeUri":"Virtual Connect SE 16Gb FC Module for Synergy","enclosureIndex":-1}
]},
"enclosureType":"SY12000",
"enclosureIndexes":[-1],
"interconnectBaySet":"1",
"redundancyType":"NonRedundantASide",
"internalNetworkUris":[],
"snmpConfiguration":{"type":"snmp-configuration","readCommunity":"public","systemContact":"","trapDestinations":None,"snmpAccess":None,"enabled":True,"description":None,"name":None,"state":None,"category":"snmp-configuration"},
"qosConfiguration":None,
"uplinkSets":[
 {"networkUris":["SAN-1-A"],"mode":"Auto","lacpTimer":"Short","primaryPort":None,
  "logicalPortConfigInfos":[{"desiredSpeed":"Auto","logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":1},{"type":"Port","relativeValue":26},{"type":"Enclosure","relativeValue":-1}]}}],
  "networkType":"FibreChannel","ethernetNetworkType":None,"name":"FC-a-1"}
 ]
 }


lig_tbird_a_2 = {"type":"logical-interconnect-groupV300",
"ethernetSettings":{"type":"EthernetInterconnectSettingsV201","enableIgmpSnooping":False,"igmpIdleTimeoutInterval":260,"enableFastMacCacheFailover":True,"macRefreshInterval":5,"enableNetworkLoopProtection":True,"enablePauseFloodProtection":True,"enableRichTLV":False,"interconnectType":"Ethernet","dependentResourceUri":None,"name":"defaultEthernetSwitchSettings","category":None,"uri":"/ethernetSettings"},
"description":None,
"name":"lig_a_2",
"interconnectMapTemplate":
{"interconnectMapEntryTemplates":[
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":2},{"type":"Enclosure","relativeValue":1}]},"permittedInterconnectTypeUri":"Virtual Connect SE 16Gb FC Module for Synergy","enclosureIndex":-1}
]},
"enclosureType":"SY12000",
"enclosureIndexes":[-1],
"interconnectBaySet":"2",
"redundancyType":"NonRedundantASide",
"internalNetworkUris":[],
"snmpConfiguration":{"type":"snmp-configuration","readCommunity":"public","systemContact":"","trapDestinations":None,"snmpAccess":None,"enabled":True,"description":None,"name":None,"state":None,"category":"snmp-configuration"},
"qosConfiguration":None,
"uplinkSets":[]
 }

lig_tbird_1_4 = {"type":"logical-interconnect-groupV300",
"ethernetSettings":{"type":"EthernetInterconnectSettingsV201","enableIgmpSnooping":False,"igmpIdleTimeoutInterval":260,"enableFastMacCacheFailover":True,"macRefreshInterval":5,"enableNetworkLoopProtection":True,"enablePauseFloodProtection":True,"enableRichTLV":False,"interconnectType":"Ethernet","dependentResourceUri":None,"name":"defaultEthernetSwitchSettings","category":None,"uri":"/ethernetSettings"},
"description":None,
"name":"lig_1_4",
"interconnectMapTemplate":
{"interconnectMapEntryTemplates":[
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":1},{"type":"Enclosure","relativeValue":1}]},"permittedInterconnectTypeUri":"Virtual Connect SE 16Gb FC Module for Synergy","enclosureIndex":-1},
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":4},{"type":"Enclosure","relativeValue":4}]},"permittedInterconnectTypeUri":"Virtual Connect SE 16Gb FC Module for Synergy","enclosureIndex":-1}
]},
"enclosureType":"SY12000",
"enclosureIndexes":[-1],
"interconnectBaySet":"1",
"redundancyType":"Redundant",
"internalNetworkUris":[],
"snmpConfiguration":{"type":"snmp-configuration","readCommunity":"public","systemContact":"","trapDestinations":None,"snmpAccess":None,"enabled":True,"description":None,"name":None,"state":None,"category":"snmp-configuration"},
"qosConfiguration":None,
"uplinkSets":[]
 }
lig_tbird_upl_1_4 = {"type":"logical-interconnect-groupV300",
"ethernetSettings":{"type":"EthernetInterconnectSettingsV201","enableIgmpSnooping":False,"igmpIdleTimeoutInterval":260,"enableFastMacCacheFailover":True,"macRefreshInterval":5,"enableNetworkLoopProtection":True,"enablePauseFloodProtection":True,"enableRichTLV":False,"interconnectType":"Ethernet","dependentResourceUri":None,"name":"defaultEthernetSwitchSettings","category":None,"uri":"/ethernetSettings"},
"description":None,
"name":"lig_1_4",
"interconnectMapTemplate":
{"interconnectMapEntryTemplates":[
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":1},{"type":"Enclosure","relativeValue":1}]},"permittedInterconnectTypeUri":"Virtual Connect SE 16Gb FC Module for Synergy","enclosureIndex":-1},
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":4},{"type":"Enclosure","relativeValue":4}]},"permittedInterconnectTypeUri":"Virtual Connect SE 16Gb FC Module for Synergy","enclosureIndex":-1}
]},
"enclosureType":"SY12000",
"enclosureIndexes":[-1],
"interconnectBaySet":"1",
"redundancyType":"Redundant",
"internalNetworkUris":[],
"snmpConfiguration":{"type":"snmp-configuration","readCommunity":"public","systemContact":"","trapDestinations":None,"snmpAccess":None,"enabled":True,"description":None,"name":None,"state":None,"category":"snmp-configuration"},
"qosConfiguration":None,
"uplinkSets":[
 {"networkUris":["FC-FA-1"],"mode":"Auto","lacpTimer":"Short","primaryPort":None,
  "logicalPortConfigInfos":[{"desiredSpeed":"Auto","logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":1},{"type":"Port","relativeValue":13},{"type":"Enclosure","relativeValue":-1}]}}],
  "networkType":"FibreChannel","ethernetNetworkType":None,"name":"FC-UPL-1"},
 {"networkUris":["FC-FA-2"],"mode":"Auto","lacpTimer":"Short","primaryPort":None,
  "logicalPortConfigInfos":[{"desiredSpeed":"Auto","logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":4},{"type":"Port","relativeValue":13},{"type":"Enclosure","relativeValue":-1}]}}],
  "networkType":"FibreChannel","ethernetNetworkType":None,"name":"FC-UPL-2"}

 ]
 }

lig_tbird_upl_1_4_1_upl = {"type":"logical-interconnect-groupV300",
"ethernetSettings":{"type":"EthernetInterconnectSettingsV201","enableIgmpSnooping":False,"igmpIdleTimeoutInterval":260,"enableFastMacCacheFailover":True,"macRefreshInterval":5,"enableNetworkLoopProtection":True,"enablePauseFloodProtection":True,"enableRichTLV":False,"interconnectType":"Ethernet","dependentResourceUri":None,"name":"defaultEthernetSwitchSettings","category":None,"uri":"/ethernetSettings"},
"description":None,
"name":"lig_1_4",
"interconnectMapTemplate":
{"interconnectMapEntryTemplates":[
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":1},{"type":"Enclosure","relativeValue":1}]},"permittedInterconnectTypeUri":"Virtual Connect SE 16Gb FC Module for Synergy","enclosureIndex":-1},
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":4},{"type":"Enclosure","relativeValue":4}]},"permittedInterconnectTypeUri":"Virtual Connect SE 16Gb FC Module for Synergy","enclosureIndex":-1}
]},
"enclosureType":"SY12000",
"enclosureIndexes":[-1],
"interconnectBaySet":"1",
"redundancyType":"Redundant",
"internalNetworkUris":[],
"snmpConfiguration":{"type":"snmp-configuration","readCommunity":"public","systemContact":"","trapDestinations":None,"snmpAccess":None,"enabled":True,"description":None,"name":None,"state":None,"category":"snmp-configuration"},
"qosConfiguration":None,
"uplinkSets":[
 {"networkUris":[],"mode":"Auto","lacpTimer":"Short","primaryPort":None,
  "logicalPortConfigInfos":[{"desiredSpeed":"Auto","logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":1},{"type":"Port","relativeValue":13},{"type":"Enclosure","relativeValue":-1}]}}],
  "networkType":"FibreChannel","ethernetNetworkType":None,"name":"FC-UPL-1"}
 ]
 }

lig_tbird_upl_1_4_remove_net_upl2 = {"type":"logical-interconnect-groupV300",
"ethernetSettings":{"type":"EthernetInterconnectSettingsV201","enableIgmpSnooping":False,"igmpIdleTimeoutInterval":260,"enableFastMacCacheFailover":True,"macRefreshInterval":5,"enableNetworkLoopProtection":True,"enablePauseFloodProtection":True,"enableRichTLV":False,"interconnectType":"Ethernet","dependentResourceUri":None,"name":"defaultEthernetSwitchSettings","category":None,"uri":"/ethernetSettings"},
"description":None,
"name":"lig_1_4",
"interconnectMapTemplate":
{"interconnectMapEntryTemplates":[
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":1},{"type":"Enclosure","relativeValue":1}]},"permittedInterconnectTypeUri":"Virtual Connect SE 16Gb FC Module for Synergy","enclosureIndex":-1},
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":4},{"type":"Enclosure","relativeValue":4}]},"permittedInterconnectTypeUri":"Virtual Connect SE 16Gb FC Module for Synergy","enclosureIndex":-1}
]},
"enclosureType":"SY12000",
"enclosureIndexes":[-1],
"interconnectBaySet":"1",
"redundancyType":"Redundant",
"internalNetworkUris":[],
"snmpConfiguration":{"type":"snmp-configuration","readCommunity":"public","systemContact":"","trapDestinations":None,"snmpAccess":None,"enabled":True,"description":None,"name":None,"state":None,"category":"snmp-configuration"},
"qosConfiguration":None,
"uplinkSets":[
 {"networkUris":["FC-FA-1"],"mode":"Auto","lacpTimer":"Short","primaryPort":None,
  "logicalPortConfigInfos":[{"desiredSpeed":"Auto","logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":1},{"type":"Port","relativeValue":13},{"type":"Enclosure","relativeValue":-1}]}}],
  "networkType":"FibreChannel","ethernetNetworkType":None,"name":"FC-UPL-1"},
 {"networkUris":[],"mode":"Auto","lacpTimer":"Short","primaryPort":None,
  "logicalPortConfigInfos":[{"desiredSpeed":"Auto","logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":4},{"type":"Port","relativeValue":13},{"type":"Enclosure","relativeValue":-1}]}}],
  "networkType":"FibreChannel","ethernetNetworkType":None,"name":"FC-UPL-2"}

 ]
 }

lig_tbird_upl_1_4_test = {"type":"logical-interconnect-groupV300",
"ethernetSettings":{"type":"EthernetInterconnectSettingsV201","enableIgmpSnooping":False,"igmpIdleTimeoutInterval":260,"enableFastMacCacheFailover":True,"macRefreshInterval":5,"enableNetworkLoopProtection":True,"enablePauseFloodProtection":True,"enableRichTLV":False,"interconnectType":"Ethernet","dependentResourceUri":None,"name":"defaultEthernetSwitchSettings","category":None,"uri":"/ethernetSettings"},
"description":None,
"name":"lig_1_4",
"interconnectMapTemplate":
{"interconnectMapEntryTemplates":[
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":1},{"type":"Enclosure","relativeValue":1}]},"permittedInterconnectTypeUri":"Virtual Connect SE 16Gb FC Module for Synergy","enclosureIndex":-1},
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":4},{"type":"Enclosure","relativeValue":4}]},"permittedInterconnectTypeUri":"Virtual Connect SE 16Gb FC Module for Synergy","enclosureIndex":-1}
]},
"enclosureType":"SY12000",
"enclosureIndexes":[-1],
"interconnectBaySet":"1",
"redundancyType":"Redundant",
"internalNetworkUris":[],
"snmpConfiguration":{"type":"snmp-configuration","readCommunity":"public","systemContact":"","trapDestinations":None,"snmpAccess":None,"enabled":True,"description":None,"name":None,"state":None,"category":"snmp-configuration"},
"qosConfiguration":None,
"uplinkSets":[
 {"networkUris":["FC-FA-1"],"mode":"Auto","lacpTimer":"Short","primaryPort":None,
  "logicalPortConfigInfos":[{"desiredSpeed":"Auto","logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":1},{"type":"Port","relativeValue":13},{"type":"Enclosure","relativeValue":-1}]}}],
  "networkType":"FibreChannel","ethernetNetworkType":None,"name":"FC-UPL-1"},
 {"networkUris":["FC-FA-2"],"mode":"Auto","lacpTimer":"Short","primaryPort":None,
  "logicalPortConfigInfos":[{"desiredSpeed":"Auto","logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":4},{"type":"Port","relativeValue":13},{"type":"Enclosure","relativeValue":-1}]}}],
  "networkType":"FibreChannel","ethernetNetworkType":None,"name":"FC-UPL-2"}

 ]
 }

lig_tbird_b_4 = {"type":"logical-interconnect-groupV300",
"ethernetSettings":{"type":"EthernetInterconnectSettingsV201","enableIgmpSnooping":False,"igmpIdleTimeoutInterval":260,"enableFastMacCacheFailover":True,"macRefreshInterval":5,"enableNetworkLoopProtection":True,"enablePauseFloodProtection":True,"enableRichTLV":False,"interconnectType":"Ethernet","dependentResourceUri":None,"name":"defaultEthernetSwitchSettings","category":None,"uri":"/ethernetSettings"},
"description":None,
"name":"lig_b_4",
"interconnectMapTemplate":
{"interconnectMapEntryTemplates":[
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":4},{"type":"Enclosure","relativeValue":1}]},"permittedInterconnectTypeUri":"Virtual Connect SE 16Gb FC Module for Synergy","enclosureIndex":-1}
]},
"enclosureType":"SY12000",
"enclosureIndexes":[-1],
"interconnectBaySet":"1",
"redundancyType":"NonRedundantBSide",
"internalNetworkUris":[],
"snmpConfiguration":{"type":"snmp-configuration","readCommunity":"public","systemContact":"","trapDestinations":None,"snmpAccess":None,"enabled":True,"description":None,"name":None,"state":None,"category":"snmp-configuration"},
"qosConfiguration":None,
"uplinkSets":[]
 }

lig_tbird_b_5 = {"type":"logical-interconnect-groupV300",
"ethernetSettings":{"type":"EthernetInterconnectSettingsV201","enableIgmpSnooping":False,"igmpIdleTimeoutInterval":260,"enableFastMacCacheFailover":True,"macRefreshInterval":5,"enableNetworkLoopProtection":True,"enablePauseFloodProtection":True,"enableRichTLV":False,"interconnectType":"Ethernet","dependentResourceUri":None,"name":"defaultEthernetSwitchSettings","category":None,"uri":"/ethernetSettings"},
"description":None,
"name":"lig_b_5",
"interconnectMapTemplate":
{"interconnectMapEntryTemplates":[
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":5},{"type":"Enclosure","relativeValue":1}]},"permittedInterconnectTypeUri":"Virtual Connect SE 16Gb FC Module for Synergy","enclosureIndex":-1}
]},
"enclosureType":"SY12000",
"enclosureIndexes":[-1],
"interconnectBaySet":"2",
"redundancyType":"NonRedundantBSide",
"internalNetworkUris":[],
"snmpConfiguration":{"type":"snmp-configuration","readCommunity":"public","systemContact":"","trapDestinations":None,"snmpAccess":None,"enabled":True,"description":None,"name":None,"state":None,"category":"snmp-configuration"},
"qosConfiguration":None,
"uplinkSets":[]
 }
lig_tbird_2_5 = {"type":"logical-interconnect-groupV300",
"ethernetSettings":{"type":"EthernetInterconnectSettingsV201","enableIgmpSnooping":False,"igmpIdleTimeoutInterval":260,"enableFastMacCacheFailover":True,"macRefreshInterval":5,"enableNetworkLoopProtection":True,"enablePauseFloodProtection":True,"enableRichTLV":False,"interconnectType":"Ethernet","dependentResourceUri":None,"name":"defaultEthernetSwitchSettings","category":None,"uri":"/ethernetSettings"},
"description":None,
"name":"lig_2_5",
"interconnectMapTemplate":
{"interconnectMapEntryTemplates":[
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":2},{"type":"Enclosure","relativeValue":2}]},"permittedInterconnectTypeUri":"Virtual Connect SE 16Gb FC Module for Synergy","enclosureIndex":-1},
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":5},{"type":"Enclosure","relativeValue":5}]},"permittedInterconnectTypeUri":"Virtual Connect SE 16Gb FC Module for Synergy","enclosureIndex":-1}
]},
"enclosureType":"SY12000",
"enclosureIndexes":[-1],
"interconnectBaySet":"2",
"redundancyType":"Redundant",
"internalNetworkUris":[],
"snmpConfiguration":{"type":"snmp-configuration","readCommunity":"public","systemContact":"","trapDestinations":None,"snmpAccess":None,"enabled":True,"description":None,"name":None,"state":None,"category":"snmp-configuration"},
"qosConfiguration":None,
"uplinkSets":[]
 }

ligs_tbird = [{'name': 'LIG-Tbird',
         'type': 'logical-interconnect-groupV300',
         'enclosureType': 'SY12000',
         #'interconnectMapTemplate': None,
         'interconnectMapTemplate': [
                {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
                {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
                {'bay': 6, 'enclosure': 1, 'type': 'HP Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
                {'bay': 3, 'enclosure': 2, 'type': 'HP Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
                {'bay': 6, 'enclosure': 3, 'type': 'HP Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3},
                {'bay': 3, 'enclosure': 3, 'type': 'HP Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3}],
         'enclosureIndexes': [1,2,3],
         'interconnectBaySet': 3,
         'redundancyType': 'HighlyAvailable',
         #'redundancyType': 'NonRedundantASide',
         'fcoeSettings': {'fcoeMode': 'FcfNpv'},
         
         #'uplinkSets': [],
         'uplinkSets': ['SAN-1-A'],
         
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None},
        ]
     

lig_tbird = {"type":"logical-interconnect-groupV300",
"ethernetSettings":{"type":"EthernetInterconnectSettingsV201","enableIgmpSnooping":False,"igmpIdleTimeoutInterval":260,"enableFastMacCacheFailover":True,"macRefreshInterval":5,"enableNetworkLoopProtection":True,"enablePauseFloodProtection":True,"enableRichTLV":False,"interconnectType":"Ethernet","dependentResourceUri":None,"name":"defaultEthernetSwitchSettings","category":None,"uri":"/ethernetSettings"},
"description":None,
"name":"lig_tbird21",
"interconnectMapTemplate":
{"interconnectMapEntryTemplates":[
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":3},{"type":"Enclosure","relativeValue":1}]},"permittedInterconnectTypeUri":"Virtual Connect SE 40Gb F8 Module for Synergy - 794502-B23","enclosureIndex":1},
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":6},{"type":"Enclosure","relativeValue":2}]},"permittedInterconnectTypeUri":"Virtual Connect SE 40Gb F8 Module for Synergy - 794502-B23","enclosureIndex":2},
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":6},{"type":"Enclosure","relativeValue":1}]},"permittedInterconnectTypeUri":"Synergy 20Gb Interconnect Link Module","enclosureIndex":1},
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":3},{"type":"Enclosure","relativeValue":2}]},"permittedInterconnectTypeUri":"Synergy 20Gb Interconnect Link Module","enclosureIndex":2},
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":3},{"type":"Enclosure","relativeValue":3}]},"permittedInterconnectTypeUri":"Synergy 20Gb Interconnect Link Module","enclosureIndex":3},
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":6},{"type":"Enclosure","relativeValue":3}]},"permittedInterconnectTypeUri":"Synergy 20Gb Interconnect Link Module","enclosureIndex":3}]},
"enclosureType":"SY12000",
"enclosureIndexes":[1,2,3],
"interconnectBaySet":"3",
"redundancyType":"HighlyAvailable",
"internalNetworkUris":[],
"snmpConfiguration":{"type":"snmp-configuration","readCommunity":"public","systemContact":"","trapDestinations":None,"snmpAccess":None,"enabled":True,"description":None,"name":None,"state":None,"category":"snmp-configuration"},
"qosConfiguration":None,
"uplinkSets":[
{"networkUris":["eth-100"],"mode":"Auto","lacpTimer":"Short","primaryPort":None,
"logicalPortConfigInfos":[{"desiredSpeed":"Auto","logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":3},{"type":"Port","relativeValue":62},{"type":"Enclosure","relativeValue":1}]}}],
"networkType":"Ethernet","ethernetNetworkType":"Tagged","name":"eth-100"},
 {"networkUris":["SAN-1-A"],"mode":"Auto","lacpTimer":"Short","primaryPort":None,
  "logicalPortConfigInfos":[{"desiredSpeed":"Auto","logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":3},{"type":"Port","relativeValue":64},{"type":"Enclosure","relativeValue":1}]}}],
  "networkType":"FibreChannel","ethernetNetworkType":None,"name":"SAN-1-A"},
 {"networkUris":["FCOE-100"],"mode":"Auto","lacpTimer":"Short","primaryPort":None,
"logicalPortConfigInfos":[{"desiredSpeed":"Auto","logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":3},{"type":"Port","relativeValue":63},{"type":"Enclosure","relativeValue":1}]}}],
"networkType":"Ethernet","ethernetNetworkType":"Tagged","name":"FCOE-100"}            
 ]
 }

lig_tbird_2enc = {"type":"logical-interconnect-groupV300",
"ethernetSettings":{"type":"EthernetInterconnectSettingsV201","enableIgmpSnooping":False,"igmpIdleTimeoutInterval":260,"enableFastMacCacheFailover":True,"macRefreshInterval":5,"enableNetworkLoopProtection":True,"enablePauseFloodProtection":True,"enableRichTLV":False,"interconnectType":"Ethernet","dependentResourceUri":None,"name":"defaultEthernetSwitchSettings","category":None,"uri":"/ethernetSettings"},
"description":None,
"name":"lig_tbird21",
"interconnectMapTemplate":
{"interconnectMapEntryTemplates":[
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":3},{"type":"Enclosure","relativeValue":1}]},"permittedInterconnectTypeUri":"Virtual Connect SE 40Gb F8 Module for Synergy - 794502-B23","enclosureIndex":1},
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":6},{"type":"Enclosure","relativeValue":2}]},"permittedInterconnectTypeUri":"Virtual Connect SE 40Gb F8 Module for Synergy - 794502-B23","enclosureIndex":2},
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":6},{"type":"Enclosure","relativeValue":1}]},"permittedInterconnectTypeUri":"Synergy 20Gb Interconnect Link Module","enclosureIndex":1},
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":3},{"type":"Enclosure","relativeValue":2}]},"permittedInterconnectTypeUri":"Synergy 20Gb Interconnect Link Module","enclosureIndex":2}]},
"enclosureType":"SY12000",
"enclosureIndexes":[1,2],
"interconnectBaySet":"3",
"redundancyType":"HighlyAvailable",
"internalNetworkUris":[],
"snmpConfiguration":{"type":"snmp-configuration","readCommunity":"public","systemContact":"","trapDestinations":None,"snmpAccess":None,"enabled":True,"description":None,"name":None,"state":None,"category":"snmp-configuration"},
"qosConfiguration":None,
"uplinkSets":[
{"networkUris":["eth-100"],"mode":"Auto","lacpTimer":"Short","primaryPort":None,
"logicalPortConfigInfos":[{"desiredSpeed":"Auto","logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":3},{"type":"Port","relativeValue":62},{"type":"Enclosure","relativeValue":1}]}}],
"networkType":"Ethernet","ethernetNetworkType":"Tagged","name":"eth-100"},
 {"networkUris":["SAN-1-A"],"mode":"Auto","lacpTimer":"Short","primaryPort":None,
  "logicalPortConfigInfos":[{"desiredSpeed":"Auto","logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":3},{"type":"Port","relativeValue":64},{"type":"Enclosure","relativeValue":1}]}}],
  "networkType":"FibreChannel","ethernetNetworkType":None,"name":"SAN-1-A"},
 {"networkUris":["FCOE-100"],"mode":"Auto","lacpTimer":"Short","primaryPort":None,
"logicalPortConfigInfos":[{"desiredSpeed":"Auto","logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":3},{"type":"Port","relativeValue":63},{"type":"Enclosure","relativeValue":1}]}}],
"networkType":"Ethernet","ethernetNetworkType":"Tagged","name":"FCOE-100"}            
 ]
 }

lig_tbird_lig = {"type":"logical-interconnect-groupV300",
"ethernetSettings":{"type":"EthernetInterconnectSettingsV201","enableIgmpSnooping":False,"igmpIdleTimeoutInterval":260,"enableFastMacCacheFailover":True,"macRefreshInterval":5,"enableNetworkLoopProtection":True,"enablePauseFloodProtection":True,"enableRichTLV":False,"interconnectType":"Ethernet","dependentResourceUri":None,"name":"defaultEthernetSwitchSettings","category":None,"uri":"/ethernetSettings"},
"description":None,
"name":"lig_tbird21",
"interconnectMapTemplate":
{"interconnectMapEntryTemplates":[
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":1},{"type":"Enclosure","relativeValue":1}]},"permittedInterconnectTypeUri":"Virtual Connect SE 16Gb FC Module for Synergy","enclosureIndex":1},
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":4},{"type":"Enclosure","relativeValue":2}]},"permittedInterconnectTypeUri":"Virtual Connect SE 16Gb FC Module for Synergy","enclosureIndex":1}]},
"enclosureType":"SY12000",
"enclosureIndexes":[1],
"interconnectBaySet":"1",
"redundancyType":"HighlyAvailable",
"internalNetworkUris":[],
"snmpConfiguration":{"type":"snmp-configuration","readCommunity":"public","systemContact":"","trapDestinations":None,"snmpAccess":None,"enabled":True,"description":None,"name":None,"state":None,"category":"snmp-configuration"},
"qosConfiguration":None,
"uplinkSets":[]
 }


lig_tbird_uplinkset1= [
{"networkUris":["eth-100"],"mode":"Auto","lacpTimer":"Short","primaryPort":None,
"logicalPortConfigInfos":[{"desiredSpeed":"Auto","logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":3},{"type":"Port","relativeValue":62},{"type":"Enclosure","relativeValue":1}]}}],
"networkType":"Ethernet","ethernetNetworkType":"Tagged","name":"eth-100"},
 {"networkUris":["FCOE-100"],"mode":"Auto","lacpTimer":"Short","primaryPort":None,
"logicalPortConfigInfos":[{"desiredSpeed":"Auto","logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":3},{"type":"Port","relativeValue":63},{"type":"Enclosure","relativeValue":1}]}}],
"networkType":"Ethernet","ethernetNetworkType":"Tagged","name":"FCOE-100"}            
 ]

lig_tbird_uplinkset2= [{"networkUris":["eth-100"],"mode":"Auto","lacpTimer":"Short","primaryPort":None,
"logicalPortConfigInfos":[{"desiredSpeed":"Auto","logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":3},{"type":"Port","relativeValue":62},{"type":"Enclosure","relativeValue":1}]}}],
"networkType":"Ethernet","ethernetNetworkType":"Tagged","name":"eth-100"},
{"networkUris":["SAN-1-A"],"mode":"Auto","lacpTimer":"Short","primaryPort":None,
  "logicalPortConfigInfos":[{"desiredSpeed":"Auto","logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":3},{"type":"Port","relativeValue":64},{"type":"Enclosure","relativeValue":1}]}}],
  "networkType":"FibreChannel","ethernetNetworkType":None,"name":"SAN-1-A"},
{"networkUris":["FCOE-100"],"mode":"Auto","lacpTimer":"Short","primaryPort":None,
"logicalPortConfigInfos":[{"desiredSpeed":"Auto","logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":3},{"type":"Port","relativeValue":63},{"type":"Enclosure","relativeValue":1}]}}],
"networkType":"Ethernet","ethernetNetworkType":"Tagged","name":"FCOE-100"},            
 ]

lig_tbird_uplinkset3=[{"networkUris":["eth-100"],"mode":"Auto","lacpTimer":"Short","primaryPort":None,
"logicalPortConfigInfos":[{"desiredSpeed":"Auto","logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":3},{"type":"Port","relativeValue":62},{"type":"Enclosure","relativeValue":1}]}}],
"networkType":"Ethernet","ethernetNetworkType":"Tagged","name":"eth-100"},
 {"networkUris":["SAN-1-A"],"mode":"Auto","lacpTimer":"Short","primaryPort":None,
  "logicalPortConfigInfos":[{"desiredSpeed":"Auto","logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":3},{"type":"Port","relativeValue":64},{"type":"Enclosure","relativeValue":1}]}}],
  "networkType":"FibreChannel","ethernetNetworkType":None,"name":"SAN-1-A"},
{"networkUris":["SAN-11-A"],"mode":"Auto","lacpTimer":"Short","primaryPort":None,
  "logicalPortConfigInfos":[{"desiredSpeed":"Auto","logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":3},{"type":"Port","relativeValue":67},{"type":"Enclosure","relativeValue":1}]}}],
  "networkType":"FibreChannel","ethernetNetworkType":None,"name":"SAN-11-A"},
 {"networkUris":["FCOE-100"],"mode":"Auto","lacpTimer":"Short","primaryPort":None,
"logicalPortConfigInfos":[{"desiredSpeed":"Auto","logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":3},{"type":"Port","relativeValue":63},{"type":"Enclosure","relativeValue":1}]}}],
"networkType":"Ethernet","ethernetNetworkType":"Tagged","name":"FCOE-100"},            
 ]


lig_tbird_bayset2 = {"type":"logical-interconnect-groupV300",
"ethernetSettings":{"type":"EthernetInterconnectSettingsV201","enableIgmpSnooping":False,"igmpIdleTimeoutInterval":260,"enableFastMacCacheFailover":True,"macRefreshInterval":5,"enableNetworkLoopProtection":True,"enablePauseFloodProtection":True,"enableRichTLV":False,"interconnectType":"Ethernet","dependentResourceUri":None,"name":"defaultEthernetSwitchSettings","category":None,"uri":"/ethernetSettings"},
"description":None,
"name":"lig_tbird_bayset2",
"interconnectMapTemplate":
{"interconnectMapEntryTemplates":[
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":2},{"type":"Enclosure","relativeValue":1}]},"permittedInterconnectTypeUri":"Virtual Connect SE 40Gb F8 Module for Synergy - 794502-B23","enclosureIndex":1},
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":5},{"type":"Enclosure","relativeValue":2}]},"permittedInterconnectTypeUri":"Virtual Connect SE 40Gb F8 Module for Synergy - 794502-B23","enclosureIndex":2},
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":5},{"type":"Enclosure","relativeValue":1}]},"permittedInterconnectTypeUri":"Synergy 20Gb Interconnect Link Module","enclosureIndex":1},
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":2},{"type":"Enclosure","relativeValue":2}]},"permittedInterconnectTypeUri":"Synergy 20Gb Interconnect Link Module","enclosureIndex":2},
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":2},{"type":"Enclosure","relativeValue":3}]},"permittedInterconnectTypeUri":"Synergy 20Gb Interconnect Link Module","enclosureIndex":3},
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":5},{"type":"Enclosure","relativeValue":3}]},"permittedInterconnectTypeUri":"Synergy 20Gb Interconnect Link Module","enclosureIndex":3}]},
"enclosureType":"SY12000",
"enclosureIndexes":[1,2,3],
"interconnectBaySet":"2",
"redundancyType":"HighlyAvailable",
"internalNetworkUris":[],
"snmpConfiguration":{"type":"snmp-configuration","readCommunity":"public","systemContact":"","trapDestinations":None,"snmpAccess":None,"enabled":True,"description":None,"name":None,"state":None,"category":"snmp-configuration"},
"qosConfiguration":None,
"uplinkSets":[
{"networkUris":["eth-102"],"mode":"Auto","lacpTimer":"Short","primaryPort":None,
"logicalPortConfigInfos":[{"desiredSpeed":"Auto","logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":2},{"type":"Port","relativeValue":62},{"type":"Enclosure","relativeValue":1}]}}],
"networkType":"Ethernet","ethernetNetworkType":"Tagged","name":"eth-102"},
 {"networkUris":["FCOE-101"],"mode":"Auto","lacpTimer":"Short","primaryPort":None,
"logicalPortConfigInfos":[{"desiredSpeed":"Auto","logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":2},{"type":"Port","relativeValue":63},{"type":"Enclosure","relativeValue":1}]}}],
"networkType":"Ethernet","ethernetNetworkType":"Tagged","name":"FCOE-101"}            
 ]
 }


lig_tbird_fconly = {"type":"logical-interconnect-groupV300",
"ethernetSettings":{"type":"EthernetInterconnectSettingsV201","enableIgmpSnooping":False,"igmpIdleTimeoutInterval":260,"enableFastMacCacheFailover":True,"macRefreshInterval":5,"enableNetworkLoopProtection":True,"enablePauseFloodProtection":True,"enableRichTLV":False,"interconnectType":"Ethernet","dependentResourceUri":None,"name":"defaultEthernetSwitchSettings","category":None,"uri":"/ethernetSettings"},
"description":None,
"name":"lig_tbird21",
"interconnectMapTemplate":
{"interconnectMapEntryTemplates":[
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":3},{"type":"Enclosure","relativeValue":1}]},"permittedInterconnectTypeUri":"Virtual Connect SE 40Gb F8 Module for Synergy - 794502-B23","enclosureIndex":1},
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":6},{"type":"Enclosure","relativeValue":2}]},"permittedInterconnectTypeUri":"Virtual Connect SE 40Gb F8 Module for Synergy - 794502-B23","enclosureIndex":2},
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":6},{"type":"Enclosure","relativeValue":1}]},"permittedInterconnectTypeUri":"Synergy 20Gb Interconnect Link Module","enclosureIndex":1},
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":3},{"type":"Enclosure","relativeValue":2}]},"permittedInterconnectTypeUri":"Synergy 20Gb Interconnect Link Module","enclosureIndex":2},
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":3},{"type":"Enclosure","relativeValue":3}]},"permittedInterconnectTypeUri":"Synergy 20Gb Interconnect Link Module","enclosureIndex":3},
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":6},{"type":"Enclosure","relativeValue":3}]},"permittedInterconnectTypeUri":"Synergy 20Gb Interconnect Link Module","enclosureIndex":3}]},
"enclosureType":"SY12000",
"enclosureIndexes":[1,2,3],
"interconnectBaySet":"3",
"redundancyType":"HighlyAvailable",
"internalNetworkUris":[],
"snmpConfiguration":{"type":"snmp-configuration","readCommunity":"public","systemContact":"","trapDestinations":None,"snmpAccess":None,"enabled":True,"description":None,"name":None,"state":None,"category":"snmp-configuration"},
"qosConfiguration":None,
"uplinkSets":[
 {"networkUris":["SAN-1-A"],"mode":"Auto","lacpTimer":"Short","primaryPort":None,
  "logicalPortConfigInfos":[{"desiredSpeed":"Auto","logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":3},{"type":"Port","relativeValue":64},{"type":"Enclosure","relativeValue":1}]}}],
  "networkType":"FibreChannel","ethernetNetworkType":None,"name":"SAN-1-A"}
 ]
 }

lig_tbird_carbon_fc = {"type":"logical-interconnect-groupV300",
"ethernetSettings":{"type":"EthernetInterconnectSettingsV201","enableIgmpSnooping":False,"igmpIdleTimeoutInterval":260,"enableFastMacCacheFailover":True,"macRefreshInterval":5,"enableNetworkLoopProtection":True,"enablePauseFloodProtection":True,"enableRichTLV":False,"interconnectType":"Ethernet","dependentResourceUri":None,"name":"defaultEthernetSwitchSettings","category":None,"uri":"/ethernetSettings"},
"description":None,
"name":"lig_1_4",
"interconnectMapTemplate":
{"interconnectMapEntryTemplates":[
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":3},{"type":"Enclosure","relativeValue":1}]},"permittedInterconnectTypeUri":"Virtual Connect SE 40Gb F8 Module for Synergy - 794502-B23","enclosureIndex":1},
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":6},{"type":"Enclosure","relativeValue":2}]},"permittedInterconnectTypeUri":"Virtual Connect SE 40Gb F8 Module for Synergy - 794502-B23","enclosureIndex":2},
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":6},{"type":"Enclosure","relativeValue":1}]},"permittedInterconnectTypeUri":"Synergy 20Gb Interconnect Link Module","enclosureIndex":1},
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":3},{"type":"Enclosure","relativeValue":2}]},"permittedInterconnectTypeUri":"Synergy 20Gb Interconnect Link Module","enclosureIndex":2},
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":3},{"type":"Enclosure","relativeValue":3}]},"permittedInterconnectTypeUri":"Synergy 20Gb Interconnect Link Module","enclosureIndex":3},
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":6},{"type":"Enclosure","relativeValue":3}]},"permittedInterconnectTypeUri":"Synergy 20Gb Interconnect Link Module","enclosureIndex":3}]},
"enclosureType":"SY12000",
"enclosureIndexes":[1,2,3],
"interconnectBaySet":"3",
"redundancyType":"HighlyAvailable",
"internalNetworkUris":[],
"snmpConfiguration":{"type":"snmp-configuration","readCommunity":"public","systemContact":"","trapDestinations":None,"snmpAccess":None,"enabled":True,"description":None,"name":None,"state":None,"category":"snmp-configuration"},
"qosConfiguration":None,
"uplinkSets":[
 {"networkUris":["SAN-1-A"],"mode":"Auto","lacpTimer":"Short","primaryPort":None,
  "logicalPortConfigInfos":[{"desiredSpeed":"Auto","logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":3},{"type":"Port","relativeValue":64},{"type":"Enclosure","relativeValue":1}]}}],
  "networkType":"FibreChannel","ethernetNetworkType":None,"name":"SAN-1-A"}
 ]
 }


lig_tbird_edit_noFCuplink = {"type":"logical-interconnect-groupV300",
"ethernetSettings":{"type":"EthernetInterconnectSettingsV201","enableIgmpSnooping":False,"igmpIdleTimeoutInterval":260,"enableFastMacCacheFailover":True,"macRefreshInterval":5,"enableNetworkLoopProtection":True,"enablePauseFloodProtection":True,"enableRichTLV":False,"interconnectType":"Ethernet","dependentResourceUri":None,"name":"defaultEthernetSwitchSettings","category":None,"uri":"/ethernetSettings"},
"description":None,
"name":"lig_tbird21",
"interconnectMapTemplate":
{"interconnectMapEntryTemplates":[
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":3},{"type":"Enclosure","relativeValue":1}]},"permittedInterconnectTypeUri":"Virtual Connect SE 40Gb F8 Module for Synergy - 794502-B23","enclosureIndex":1},
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":6},{"type":"Enclosure","relativeValue":2}]},"permittedInterconnectTypeUri":"Virtual Connect SE 40Gb F8 Module for Synergy - 794502-B23","enclosureIndex":2},
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":6},{"type":"Enclosure","relativeValue":1}]},"permittedInterconnectTypeUri":"Synergy 20Gb Interconnect Link Module","enclosureIndex":1},
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":3},{"type":"Enclosure","relativeValue":2}]},"permittedInterconnectTypeUri":"Synergy 20Gb Interconnect Link Module","enclosureIndex":2},
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":3},{"type":"Enclosure","relativeValue":3}]},"permittedInterconnectTypeUri":"Synergy 20Gb Interconnect Link Module","enclosureIndex":3},
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":6},{"type":"Enclosure","relativeValue":3}]},"permittedInterconnectTypeUri":"Synergy 20Gb Interconnect Link Module","enclosureIndex":3}]},
"enclosureType":"SY12000",
"enclosureIndexes":[1,2,3],
"interconnectBaySet":"3",
"redundancyType":"HighlyAvailable",
"internalNetworkUris":[],
"snmpConfiguration":{"type":"snmp-configuration","readCommunity":"public","systemContact":"","trapDestinations":None,"snmpAccess":None,"enabled":True,"description":None,"name":None,"state":None,"category":"snmp-configuration"},
"qosConfiguration":None,
"uplinkSets":[
{"networkUris":["eth-100"],"mode":"Auto","lacpTimer":"Short","primaryPort":None,
"logicalPortConfigInfos":[{"desiredSpeed":"Auto","logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":3},{"type":"Port","relativeValue":62},{"type":"Enclosure","relativeValue":1}]}}],
"networkType":"Ethernet","ethernetNetworkType":"Tagged","name":"eth-100"},
{"networkUris":["FCOE-100"],"mode":"Auto","lacpTimer":"Short","primaryPort":None,
"logicalPortConfigInfos":[{"desiredSpeed":"Auto","logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":3},{"type":"Port","relativeValue":63},{"type":"Enclosure","relativeValue":1}]}}],
"networkType":"Ethernet","ethernetNetworkType":"Tagged","name":"FCOE-100"}
            
    ]
   }


lig_tbird_nouplink = {"type":"logical-interconnect-groupV300",
"ethernetSettings":{"type":"EthernetInterconnectSettingsV201","enableIgmpSnooping":False,"igmpIdleTimeoutInterval":260,"enableFastMacCacheFailover":True,"macRefreshInterval":5,"enableNetworkLoopProtection":True,"enablePauseFloodProtection":True,"enableRichTLV":False,"interconnectType":"Ethernet","dependentResourceUri":None,"name":"defaultEthernetSwitchSettings","category":None,"uri":"/ethernetSettings"},
"description":None,
"name":"lig_tbird21",
"interconnectMapTemplate":
{"interconnectMapEntryTemplates":[
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":3},{"type":"Enclosure","relativeValue":1}]},"permittedInterconnectTypeUri":"Virtual Connect SE 40Gb F8 Module for Synergy - 794502-B23","enclosureIndex":1},
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":6},{"type":"Enclosure","relativeValue":2}]},"permittedInterconnectTypeUri":"Virtual Connect SE 40Gb F8 Module for Synergy - 794502-B23","enclosureIndex":2},
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":6},{"type":"Enclosure","relativeValue":1}]},"permittedInterconnectTypeUri":"Synergy 20Gb Interconnect Link Module","enclosureIndex":1},
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":3},{"type":"Enclosure","relativeValue":2}]},"permittedInterconnectTypeUri":"Synergy 20Gb Interconnect Link Module","enclosureIndex":2},
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":3},{"type":"Enclosure","relativeValue":3}]},"permittedInterconnectTypeUri":"Synergy 20Gb Interconnect Link Module","enclosureIndex":3},
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":6},{"type":"Enclosure","relativeValue":3}]},"permittedInterconnectTypeUri":"Synergy 20Gb Interconnect Link Module","enclosureIndex":3}]},
"enclosureType":"SY12000",
"enclosureIndexes":[1,2,3],
"interconnectBaySet":"3",
"redundancyType":"HighlyAvailable",
"internalNetworkUris":[],
"snmpConfiguration":{"type":"snmp-configuration","readCommunity":"public","systemContact":"","trapDestinations":None,"snmpAccess":None,"enabled":True,"description":None,"name":None,"state":None,"category":"snmp-configuration"},
"qosConfiguration":None,
"uplinkSets":[]
   }



lig_tbird_Potassium = {"type":"logical-interconnect-groupV300",
"ethernetSettings":{"type":"EthernetInterconnectSettingsV201","enableIgmpSnooping":False,"igmpIdleTimeoutInterval":260,"enableFastMacCacheFailover":True,"macRefreshInterval":5,"enableNetworkLoopProtection":True,"enablePauseFloodProtection":True,"enableRichTLV":False,"interconnectType":"Ethernet","dependentResourceUri":None,"name":"defaultEthernetSwitchSettings","category":None,"uri":"/ethernetSettings"},
"description":None,
"name":"lig_tbird21",
"interconnectMapTemplate":
{"interconnectMapEntryTemplates":[
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":3},{"type":"Enclosure","relativeValue":1}]},"permittedInterconnectTypeUri":"Virtual Connect SE 40Gb F8 Module for Synergy","enclosureIndex":1},
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":6},{"type":"Enclosure","relativeValue":2}]},"permittedInterconnectTypeUri":"Virtual Connect SE 40Gb F8 Module for Synergy","enclosureIndex":2},
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":6},{"type":"Enclosure","relativeValue":1}]},"permittedInterconnectTypeUri":"Synergy 20Gb Interconnect Link Module","enclosureIndex":1},
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":3},{"type":"Enclosure","relativeValue":2}]},"permittedInterconnectTypeUri":"Synergy 20Gb Interconnect Link Module","enclosureIndex":2},
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":3},{"type":"Enclosure","relativeValue":3}]},"permittedInterconnectTypeUri":"Synergy 20Gb Interconnect Link Module","enclosureIndex":3},
{"logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":6},{"type":"Enclosure","relativeValue":3}]},"permittedInterconnectTypeUri":"Synergy 20Gb Interconnect Link Module","enclosureIndex":3}]},
"enclosureType":"SY12000",
"enclosureIndexes":[1,2,3],
"interconnectBaySet":"3",
"redundancyType":"HighlyAvailable",
"internalNetworkUris":[],
"snmpConfiguration":{"type":"snmp-configuration","readCommunity":"public","systemContact":"","trapDestinations":None,"snmpAccess":None,"enabled":True,"description":None,"name":None,"state":None,"category":"snmp-configuration"},
"qosConfiguration":None,
"uplinkSets": []
   }





telemetry = {'enableTelemetry': True, 'sampleInterval': 400, 'sampleCount': 20}

trapDestinations = [{'trapSeverities': ['Major'],
                     'enetTrapCategories': ['Other'],
                     'fcTrapCategories': ['Other'],
                     'vcmTrapCategories': ['Legacy'],
                     'trapFormat': 'SNMPv1',
                     'trapDestination': '192.168.99.99',
                     'communityString': 'public'}]

snmp = {'snmpAccess': ['192.168.1.0/24'],
        'trapDestinations': trapDestinations}

enet = {'enableFastMacCacheFailover': False}

"""
profile1 = {'type': 'ServerProfileV5', 'serverHardwareUri': 'WPST-PABA58-EN1, bay 1',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:WPST-PABA58-EN1', 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'WPST-PABA58-EN1_Bay1-BFS', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
                    'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:eth-102', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Flb 1:1-b', 'requestedMbps': '2500', 'networkUri': 'FCOE:fcoe-1002', 'boot': {'priority': 'Primary', 'targets': [{'arrayWwpn': '21110002AC003655', 'lun': '0'}]}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    ]}

profile2 = {'type': 'ServerProfileV5', 'serverHardwareUri': 'WPST-PABA58-EN1, bay 2',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:WPST-PABA58-EN1', 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'WPST-PABA58-EN1_Bay2', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
                    'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:eth-102', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                   ]}

server_profiles = [profile1.copy(), profile2.copy()]

"""
server_profiles = [{'type': 'ServerProfileV5', 'serverHardwareUri': 'SGH411DFYA, bay 6',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:SGH411DFYA', 'enclosureGroupUri': 'EG:EGLldp', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'Sp_APIC', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': False},
                    'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:eth-100', 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-b', 'requestedMbps': '2500', 'networkUri': 'ETH:eth-101', 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    ]},                  
                   ]

server_profiles1 = [{'type': 'ServerProfileV5', 'serverHardwareUri': 'SGH411DFYA, bay 3',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:SGH411DFYA', 'enclosureGroupUri': 'EG:EGLldp', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'Sp_APIC', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
                    'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:APIC1', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-b', 'requestedMbps': '2500', 'networkUri': 'ETH:APIC2', 'boot': {'priority': 'Primary', 'targets': [{'arrayWwpn': '21110002AC003655', 'lun': '0'}]}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    ]},
                   
                   ]

# server_profile_fc = [{'name':'ServerBay4', 'type':'ServerProfileV6', 'serverHardwareUri':'SH:0000000010, bay 4', 'enclosureGroupUri': 'EG:TB_CAR_EG_1_4','serialNumberType':'Physical', 'iscsiInitiatorNameType':'AutoGenerated', 'macType':'Physical', 'wwnType':'Physical', 'description':'Updated Profile', 'affinity':'Bay',
server_profile_fc = [{'name':'ServerBay4', 'type':'ServerProfileV6', 'serverHardwareUri':'SH:{0}, bay 4'.format(server_name), 'enclosureGroupUri': 'EG:TB_CAR_EG_1_4','serialNumberType':'Physical', 'iscsiInitiatorNameType':'AutoGenerated', 'macType':'Physical', 'wwnType':'Physical', 'description':'Updated Profile', 'affinity':'Bay',
                        'connections':[],
                        'boot':{'manageBoot':False},
                        'bootMode':{'manageMode':False},
                        'firmware':{'manageFirmware':False, 'firmwareBaselineUri':'', 'forceInstallFirmware':False, 'firmwareInstallType':None},
                        'bios':{'manageBios':False, 'overriddenSettings':[]},
                        'hideUnusedFlexNics':True, 'iscsiInitiatorName':'', 'osDeploymentSettings':None,
                        'localStorage':None,
                        'sanStorage':None,
                        'connections': [{'id': 1, 'name': '1', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_FA_1', 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_FA_2', 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    ]},                  

                 ]

LI_fwupdate_carbon = {"path":"/firmware",'command':'UPDATE','ethernetActivationDelay':'5','ethernetActivationType':'Parallel','force': True,'sppUri':upgrade_firmware_path}

LE_fw_update_Carbon_sharedinfra = {"op":"replace","path":"/firmware","firmwareBaselineUri":upgrade_firmware_path,"firmwareUpdateOn":"SharedInfrastructureOnly","forceInstallFirmware":False,"validateIfLIFirmwareUpdateIsNonDisruptive":False,"logicalInterconnectUpdateMode":"Parallel","updateFirmwareOnUnmanagedInterconnect":False}
LE_fw_update_Carbon_sharedinfra_force = {"op":"replace","path":"/firmware","firmwareBaselineUri":upgrade_firmware_path,"firmwareUpdateOn":"SharedInfrastructureOnly","forceInstallFirmware":True,"validateIfLIFirmwareUpdateIsNonDisruptive":False,"logicalInterconnectUpdateMode":"Parallel","updateFirmwareOnUnmanagedInterconnect":False}
LE_fw_downgrade_Carbon_sharedinfra = {"op":"replace","path":"/firmware","firmwareBaselineUri":downgrade_firmware_path,"firmwareUpdateOn":"SharedInfrastructureOnly","forceInstallFirmware":True,"validateIfLIFirmwareUpdateIsNonDisruptive":False,"logicalInterconnectUpdateMode":"Parallel","updateFirmwareOnUnmanagedInterconnect":False}
LE_fw_update_Carbon_sharedInfra_parallel = {"op":"replace","path":"/firmware","firmwareBaselineUri":upgrade_firmware_path,"firmwareUpdateOn":"SharedInfrastructureOnly","forceInstallFirmware":False,"validateIfLIFirmwareUpdateIsNonDisruptive":False,"logicalInterconnectUpdateMode":"Parallel","updateFirmwareOnUnmanagedInterconnect":False}
LE_fw_update_Carbon_EMOnly = {"op":"replace","path":"/firmware","firmwareBaselineUri":upgrade_firmware_path,"firmwareUpdateOn":"EnclosureOnly","forceInstallFirmware":False,"validateIfLIFirmwareUpdateIsNonDisruptive":False,"logicalInterconnectUpdateMode":"Parallel","updateFirmwareOnUnmanagedInterconnect":False}
LE_fw_update_Carbon_SharedProfile = {"op":"replace","path":"/firmware","firmwareBaselineUri":upgrade_firmware_path,"firmwareUpdateOn":"SharedInfrastructureAndServerProfiles","forceInstallFirmware":False,"validateIfLIFirmwareUpdateIsNonDisruptive":False,"logicalInterconnectUpdateMode":"Parallel","updateFirmwareOnUnmanagedInterconnect":False}

LI_fw_update_Carbon = {"path":"firmware","command": "Stage","ethernetActivationDelay": "5","ethernetActivationType": "OddEven","fcActivationDelay": "5","fcActivationType":"Serial","force": False,"sppUri": upgrade_firmware_path}

LI_fwupdate_carbon = {'command':'UPDATE','ethernetActivationDelay':'5','ethernetActivationType':'Parallel','force': True,'sppUri':upgrade_firmware_path}
LI_fw_update_Carbon = {"path":"/firmware","command": "Stage","ethernetActivationDelay": "5","ethernetActivationType": "OddEven","fcActivationDelay": "5","fcActivationType":"Serial","force": False,"sppUri": upgrade_firmware_path}
LI_fwdowngrade_carbon_parallel = {"path":"/firmware",'command':'Update','ethernetActivationDelay':'5','ethernetActivationType':'Parallel',"fcActivationDelay": "5","fcActivationType":"Parallel",'force': True,'sppUri':downgrade_firmware_path}
LI_fwdowngrade_carbon_orchestrated = {"path":"/firmware",'command':'Update','ethernetActivationDelay':'5','ethernetActivationType':'PairProtect',"fcActivationDelay": "5","fcActivationType":"Serial",'force': True,'sppUri':downgrade_firmware_path}

LI_fw_update_Carbon_orchestrated = {"path":"/firmware","sppUri":upgrade_firmware_path,"command":"Update","force":False,"ethernetActivationType":"PairProtect","ethernetActivationDelay":"0","fcActivationType":"PairProtect","fcActivationDelay":"0","validationType":"ValidateBestEffort"}

LI_fw_update_Carbon_orchestrated_stage_activate_comp = {"path":"/firmware","sppUri":upgrade_firmware_path,"command":"Update","force":True,"ethernetActivationType":"PairProtect","ethernetActivationDelay":"0","fcActivationType":"PairProtect","fcActivationDelay":"0","validationType":"ValidateBestEffort"}
LI_fw_update_Carbon_orchestrated_stage_activate_incomp = {"path":"/firmware","sppUri":upgrade_firmware_path,"command":"Update","force":False,"ethernetActivationType":"PairProtect","ethernetActivationDelay":"0","fcActivationType":"PairProtect","fcActivationDelay":"0","validationType":"ValidateBestEffort"}

LI_fw_update_Carbon_orchestrated = {"path":"/firmware","sppUri":upgrade_firmware_path,"command":"Update","force":False,"ethernetActivationType":"PairProtect","ethernetActivationDelay":"0","fcActivationType":"PairProtect","fcActivationDelay":"5","validationType":"ValidateBestEffort"}
LI_fw_update_Carbon_parallel = {"path":"/firmware","sppUri":upgrade_firmware_path,"command":"Update","force":True,"ethernetActivationType":"Parallel","ethernetActivationDelay":"0","fcActivationType":"Parallel","fcActivationDelay":"5","validationType":"None"}

LE_fw_downgrade_Carbon_sharedInfra_parallel = {"op":"replace","path":"/firmware","firmwareBaselineUri":downgrade_firmware_path,"firmwareUpdateOn":"SharedInfrastructureOnly","forceInstallFirmware":True,"validateIfLIFirmwareUpdateIsNonDisruptive":False,"logicalInterconnectUpdateMode":"Parallel","updateFirmwareOnUnmanagedInterconnect":False}
LE_fw_downgrade_Carbon_sharedInfra_orchestrated = {"op":"replace","path":"/firmware","firmwareBaselineUri":downgrade_firmware_path,"firmwareUpdateOn":"SharedInfrastructureOnly","forceInstallFirmware":True,"validateIfLIFirmwareUpdateIsNonDisruptive":False,"logicalInterconnectUpdateMode":"PairProtect","updateFirmwareOnUnmanagedInterconnect":False}

LE_fw_downgrade_Carbon_sharedInfra_orchestrated_noforce = {"op":"replace","path":"/firmware","firmwareBaselineUri":downgrade_firmware_path,"firmwareUpdateOn":"SharedInfrastructureOnly","forceInstallFirmware":True,"validateIfLIFirmwareUpdateIsNonDisruptive":False,"logicalInterconnectUpdateMode":"Parallel","updateFirmwareOnUnmanagedInterconnect":False}


#LE_fw_update_Carbon_sharedinfra = {"op":"replace","path":"/firmware","firmwareBaselineUri":"/rest/firmware-drivers/SPPgen9snap6_2016_0128_64","firmwareUpdateOn":"SharedInfrastructureOnly","forceInstallFirmware":False,"validateIfLIFirmwareUpdateIsNonDisruptive":False,"logicalInterconnectUpdateMode":"Parallel","updateFirmwareOnUnmanagedInterconnect":False}
#LE_fw_update_Carbon_sharedinfra = {"op":"replace","path":"/firmware","firmwareBaselineUri":"/rest/firmware-drivers/SPPgen9snap6_2016_0128_64","firmwareUpdateOn":"SharedInfrastructureOnly","forceInstallFirmware":False,"validateIfLIFirmwareUpdateIsNonDisruptive":False,"logicalInterconnectUpdateMode":"Parallel","updateFirmwareOnUnmanagedInterconnect":False}

LE_create_update_fw_force = {"firmwareBaselineUri":downgrade_firmware_path,"forceInstallFirmware":True}
LE_create_update_fw_noforce = {"firmwareBaselineUri":upgrade_firmware_path,"forceInstallFirmware":False}

LE_fw_negative_test = {"op":"replace","path":"/firmware","firmwareBaselineUri":upgrade_firmware_path,"firmwareUpdateOn":"SharedInfrastructureOnly","forceInstallFirmware":True,"validateIfLIFirmwareUpdateIsNonDisruptive":False,"logicalInterconnectUpdateMode":"Parallel","updateFirmwareOnUnmanagedInterconnect":False}

#LI_fw_update_Carbon_orchestrated_stage = {"path":"/firmware","sppUri":"/rest/firmware-drivers/CAR-26-Snap6-bp-Hf115-C26-CLSyl-101-2016-03-09-01","command":"Stage","force":False,"ethernetActivationType":"PairProtect","ethernetActivationDelay":"0","fcActivationType":"PairProtect","fcActivationDelay":"0","validationType":"ValidateBestEffort"}
LI_fw_update_Carbon_orchestrated_stage = {"path":"/firmware",'command':'Stage','ethernetActivationDelay':'5','ethernetActivationType':'Parallel',"fcActivationDelay": "5","fcActivationType":"Parallel",'force': True,'sppUri':upgrade_firmware_path,"validationType":"ValidateBestEffort"}
LI_fw_update_Carbon_orchestrated_stage_old = {"path":"/firmware",'command':'Stage','ethernetActivationDelay':'5','ethernetActivationType':'Parallel',"fcActivationDelay": "5","fcActivationType":"Parallel",'force': True,'sppUri':upgrade_firmware_path,"validationType":"ValidateBestEffort"} 
#LI_fw_update_Carbon_orchestrated_activate = {"path":"/firmware","sppUri":"/rest/firmware-drivers/CAR-26-Snap6-bp-Hf115-C26-CLSyl-101-2016-03-09-01","command":"Activate","force":False,"ethernetActivationType":"PairProtect","ethernetActivationDelay":"0","fcActivationType":"PairProtect","fcActivationDelay":"0","validationType":"ValidateBestEffort"}
LI_fw_update_Carbon_orchestrated_activate = {"path":"/firmware",'command':'Activate','ethernetActivationDelay':'5','ethernetActivationType':'Parallel',"fcActivationDelay": "5","fcActivationType":"Parallel",'force': True,'sppUri':upgrade_firmware_path,"validationType":"ValidateBestEffort"}


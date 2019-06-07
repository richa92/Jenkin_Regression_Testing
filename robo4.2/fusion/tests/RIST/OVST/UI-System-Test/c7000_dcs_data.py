ONEVIEW_SSH_USERNAME = 'root'  # SSH Username
ONEVIEW_SSH_PASSWORD = 'hponeview'  # SSH Password

appliance = {'type': 'ApplianceNetworkConfiguration',
             'applianceNetworks':
             [{'device': 'eth0',
               'macAddress': None,
               'interfaceName': 'OVAQual',
               'activeNode': '1',
               'unconfigure': False,
               'ipv4Type': 'STATIC',
               'ipv4Subnet': '255.255.0.0',
               'ipv4Gateway': '10.2.0.1',
               'ipv4NameServers': ['10.2.0.11'],
               'app1Ipv4Addr': '10.2.12.6',
               'ipv6Type': 'UNCONFIGURE',
               'hostname': 'ci-ovaQual-dcs2.dom1002.net',
               'confOneNode': True,
               'domainName': 'dom1002.net',
               'aliasDisabled': True,
               }],
             }

"""
This is the time and locale settings used during FTS.
"""
timeandlocale = {'type': 'TimeAndLocale', 'dateTime': None, 'timezone': 'UTC', 'ntpServers': ['ntp.hp.net'], 'locale': 'en_US.UTF-8'}

credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}

licenses = [{'key': 'YCDG B9MA H9P9 8HV3 V7B5 HWWB Y9JL KMPL P4SA 6EZA DXAU 2CSM GHTG L762 GFD6 W9JM KJVT D5KM EFVW DT5J JQM8 M2S2 9K2P 3E22 DKAG 3UFR TZZX MB5X 82Z5 WHEF D9ED 3RUX BJS2 XFXC T84U R42A 58S5 XA2D WXAP GMTQ 4YLB MM2S CZU7 2E4X E8EW BGB5 BWPD CAAR YT9J 4NUG 2NJN J9UF "424669585 HPOV-NFR1 HP_OneView_16_Seat_NFR JJ72AYTJ2U9Y"_3JJL2-DHCDC-X5RM4-T85XX-SM962'},
            {'key': 'QCLE C9MA H9PA 8HV3 V7B5 HWWB Y9JL KMPL D4KG MEZA DXAU 2CSM GHTG L762 B57Z GLJM KJVT D5KM EFRW DS5R DQEM 7ZS2 9K2P 3E22 LKAG LUVR TZZP MB5X 82Z5 WHEF D9ED 3RUX BJS2 XFXC T84U R42A 58S5 XA2D WXAP GMTQ 4YLB MM2S CZU7 2E4X E8EW BGB5 BWPD CAAR YT9J 4NUG 2NJN J9UF "424669494 HPOV-NFR1 HP_OneView_16_Seat_NFR ADEJAYTJC7YC"_3JJKW-KM6WK-KZ45Y-V6789-9Q5J6'},
            {'key': 'QCLE A9MA H9PY KHV2 U7B5 HWW5 Y9JL KMPL R42E NFJA DXAU 2CSM GHTG L762 WFH4 G9J4 KJVT D5KM EFVW DT5J RQUK 42C2 9K2P 3E22 DKAG 3UFR TZZH AB6X 82Z5 WHEF D9ED 3RUX BJS2 XFXC T84U R42A 58S5 XA2D WXAP GMTQ 4YLB MM2S CZU7 2E4X E8EW BGB5 BWPD CAAR 2T9J MNEG 2NJN J9UF "424669587 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR 66CAAYTJCJA7"'},
            {'key': 'YC3G A9MA H9P9 KHW3 U7B5 HWW5 Y9JL KMPL F42C PEJA DXAU 2CSM GHTG L762 AB36 XJZU KJVT D5KM EFRW DS5R FQU9 6ZC2 9K2P 3E22 LKAG LUVR TZZX MB5X 82Z5 WHEF D9ED 3RUX BJS2 XFXC T84U R42A 58S5 XA2D WXAP GMTQ 4YLB MM2S CZU7 2E4X E8EW BGB5 BWPD CAAR 2T9J MNEG 2NJN J9UF "424669495 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR 3GJ9AYTJ275U"'}]

users = [{'userName': 'appliance', 'password': 'Cosmos123', 'roles': ['Infrastructure administrator'], 'emailAddress':'appliance@hp.com', 'officePhone':'970-898-2222', 'mobilePhone':'970-898-0022', 'type': 'UserAndRoles'},
         {'userName': 'backup', 'password': 'backupadmin', 'roles': ['Backup administrator'], 'emailAddress':'backup@hp.com', 'officePhone':'970-666-1919', 'mobilePhone':'970-600-1919', 'type': 'UserAndRoles'},
         {'userName': 'readonly', 'password': 'readonly', 'roles': ['Read only'], 'emailAddress':'readonly@hp.com', 'officePhone':'970-666-1919', 'mobilePhone':'970-600-1919', 'type': 'UserAndRoles'}]

expected_users = [{'type': 'UserAndRoles', 'roles': ['Infrastructure administrator'], 'userName':'administrator', 'fullName':'Default appliance administrator', 'emailAddress':'', 'officePhone':'', 'mobilePhone':'', 'enabled':True, 'uri':'/rest/users/administrator', 'description':None, 'name':None, 'state':None, 'status':None, 'category':'users'},
                  {'type': 'UserAndRoles', 'roles': ['Infrastructure administrator'], 'userName':'appliance', 'fullName':'', 'emailAddress':'appliance@hp.com', 'officePhone':'970-898-2222', 'mobilePhone':'970-898-0022', 'enabled':True, 'uri':'/rest/users/appliance', 'description':None, 'name':None, 'state':None, 'status':None, 'category':'users'},
                  {'type': 'UserAndRoles', 'roles': ['Backup administrator'], 'userName':'backup', 'fullName':'', 'emailAddress':'backup@hp.com', 'officePhone':'970-666-1919', 'mobilePhone':'970-600-1919', 'enabled':True, 'uri':'/rest/users/backup', 'description':None, 'name':None, 'state':None, 'status':None, 'category':'users'},
                  {'type': 'UserAndRoles', 'roles': ['Read only'], 'userName':'readonly', 'fullName':'', 'emailAddress':'readonly@hp.com', 'officePhone':'970-666-1919', 'mobilePhone':'970-600-1919', 'enabled':True, 'uri':'/rest/users/readonly', 'description':None, 'name':None, 'state':None, 'status':None, 'category':'users'}]

san_managers = [{'connectionInfo': [{'name': 'Type', 'value': 'Cisco'},
                                    {'name': 'Host', 'value': '172.18.20.1'},
                                    {'name': 'SnmpPort', 'value': 161},
                                    {'name': 'SnmpUserName', 'value': 'dcs-SHA'},
                                    {'name': 'SnmpAuthString', 'value': 'dcsdcsdcs'},
                                    {'name': 'SnmpAuthLevel','value': 'AUTHNOPRIV'},
                                    {'name': 'SnmpAuthProtocol', 'value': 'SHA'}]},

                {'connectionInfo': [{'name': 'Type', 'value': 'Cisco'},
                                    {'name': 'Host', 'value': '172.18.20.2'},
                                    {'name': 'SnmpPort', 'value': 161},
                                    {'name': 'SnmpUserName', 'value': 'dcs-SHA'},
                                    {'name': 'SnmpAuthString', 'value': 'dcsdcsdcs'},
                                    {'name': 'SnmpAuthLevel','value': 'AUTHNOPRIV'},
                                    {'name': 'SnmpAuthProtocol', 'value': 'SHA'}]}]

expected_san_managers = [{'uri': 'SAN:172.18.20.1', 'name': '172.18.20.1', 'type': 'FCDeviceManagerV2',
                          'state': 'Managed', 'status': 'OK', 'category': 'fc-device-managers',
                          'connectionInfo': [{'name': 'Host', 'displayName': 'Host', 'required': False, 'value': '172.18.20.1', 'valueFormat': 'IPAddressOrHostname', 'valueType': 'String'},
                                    {'name': 'SnmpPort', 'displayName': 'SnmpPort', 'required': False, 'value': 161, 'valueFormat': 'None', 'valueType': 'Integer'},
                                    {'name': 'SnmpUserName', 'displayName': 'SnmpUserName', 'required': False, 'value': 'dcs-SHA', 'valueFormat': 'None', 'valueType': 'String'},
                                    {'name': 'SnmpAuthString', 'displayName': 'SnmpAuthString', 'required': False, 'value': '', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'},
                                    {'name': 'SnmpAuthLevel', 'displayName': 'SnmpAuthLevel', 'required': False, 'value': 'AUTHNOPRIV', 'valueFormat': 'None', 'valueType': 'String'},
                                    {'name': 'SnmpAuthProtocol', 'displayName': 'SnmpAuthProtocol', 'required': False, 'value': 'SHA', 'valueFormat': 'None', 'valueType': 'String'},
                                    {'name': 'SnmpPrivProtocol', 'displayName': 'SnmpPrivProtocol', 'required': False, 'value': '', 'valueFormat': 'None', 'valueType': 'String'},
                                    {'name': 'SnmpPrivString', 'displayName': 'SnmpPrivString', 'required': False, 'value': '', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                          'description': 'MDS 9250i 40 FC 2 IPS 8 FCoE (1 Slot) Chassis',
                          'deviceManagerVersion': '6.2(5)',
                          'isInternal': False,
                          'providerDisplayName': 'Cisco',
                          'refreshState': 'Stable'},

                         {'uri': 'SAN:172.18.20.2', 'name': '172.18.20.2', 'type': 'FCDeviceManagerV2',
                          'state': 'Managed', 'status': 'OK', 'category': 'fc-device-managers',
                          'connectionInfo': [{'name': 'Host', 'displayName': 'Host', 'required': False, 'value': '172.18.20.2', 'valueFormat': 'IPAddressOrHostname', 'valueType': 'String'},
                                    {'name': 'SnmpPort', 'displayName': 'SnmpPort', 'required': False, 'value': 161, 'valueFormat': 'None', 'valueType': 'Integer'},
                                    {'name': 'SnmpUserName', 'displayName': 'SnmpUserName', 'required': False, 'value': 'dcs-SHA', 'valueFormat': 'None', 'valueType': 'String'},
                                    {'name': 'SnmpAuthString', 'displayName': 'SnmpAuthString', 'required': False, 'value': '', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'},
                                    {'name': 'SnmpAuthLevel', 'displayName': 'SnmpAuthLevel', 'required': False, 'value': 'AUTHNOPRIV', 'valueFormat': 'None', 'valueType': 'String'},
                                    {'name': 'SnmpAuthProtocol', 'displayName': 'SnmpAuthProtocol', 'required': False, 'value': 'SHA', 'valueFormat': 'None', 'valueType': 'String'},
                                    {'name': 'SnmpPrivProtocol', 'displayName': 'SnmpPrivProtocol', 'required': False, 'value': '', 'valueFormat': 'None', 'valueType': 'String'},
                                    {'name': 'SnmpPrivString', 'displayName': 'SnmpPrivString', 'required': False, 'value': '', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                          'description': 'MDS 9250i 40 FC 2 IPS 8 FCoE (1 Slot) Chassis',
                          'deviceManagerVersion': '6.2(5)',
                          'isInternal': False,
                          'providerDisplayName': 'Cisco',
                          'refreshState': 'Stable'}]

ethernet_networks = [{'name': 'net10', 'vlanId': '10', 'purpose': 'General', 'smartLink': 'false', 'privateNetwork': 'false', 'ethernetNetworkType': 'Tagged', 'type': 'ethernet-networkV300', 'connectionTemplateUri': None},
                     {'name': 'net11', 'vlanId': '11', 'purpose': 'Management', 'smartLink': 'false', 'privateNetwork': 'false', 'ethernetNetworkType': 'Tagged', 'type': 'ethernet-networkV300', 'connectionTemplateUri': None},
                     {'name': 'net12', 'vlanId': '12', 'purpose': 'Management', 'smartLink': 'false', 'privateNetwork': 'false', 'ethernetNetworkType': 'Tagged', 'type': 'ethernet-networkV300', 'connectionTemplateUri': None},
                     {'name': 'net13', 'vlanId': '13', 'purpose': 'Management', 'smartLink': 'false', 'privateNetwork': 'false', 'ethernetNetworkType': 'Tagged', 'type': 'ethernet-networkV300', 'connectionTemplateUri': None},
                     {'name': 'net14', 'vlanId': '14', 'purpose': 'Management', 'smartLink': 'false', 'privateNetwork': 'false', 'ethernetNetworkType': 'Tagged', 'type': 'ethernet-networkV300', 'connectionTemplateUri': None},
                     {'name': 'net15', 'vlanId': '15', 'purpose': 'General', 'smartLink': 'false', 'privateNetwork': 'false', 'ethernetNetworkType': 'Tagged', 'type': 'ethernet-networkV300', 'connectionTemplateUri': None}]

expected_ethernet_networks = [{'name': 'net10', 'type': 'ethernet-networkV300', 'ethernetNetworkType': 'Tagged', 'vlanId': '10', 'smartLink': 'False', 'purpose': 'General', 'privateNetwork': 'False', 'subnetUri': None, 'description': None, 'status': 'OK', 'state': 'Active', 'category': 'ethernet-networks', 'uri': 'ETH:net10'},
                              {'name': 'net11', 'type': 'ethernet-networkV300', 'ethernetNetworkType': 'Tagged', 'vlanId': '11', 'smartLink': 'False', 'purpose': 'Management', 'privateNetwork': 'False', 'subnetUri': None, 'description': None, 'status': 'OK', 'state': 'Active', 'category': 'ethernet-networks', 'uri': 'ETH:net11'},
                              {'name': 'net12', 'type': 'ethernet-networkV300', 'ethernetNetworkType': 'Tagged', 'vlanId': '12', 'smartLink': 'False', 'purpose': 'Management', 'privateNetwork': 'False', 'subnetUri': None, 'description': None, 'status': 'OK', 'state': 'Active', 'category': 'ethernet-networks', 'uri': 'ETH:net12'},
                              {'name': 'net13', 'type': 'ethernet-networkV300', 'ethernetNetworkType': 'Tagged', 'vlanId': '13', 'smartLink': 'False', 'purpose': 'Management', 'privateNetwork': 'False', 'subnetUri': None, 'description': None, 'status': 'OK', 'state': 'Active', 'category': 'ethernet-networks', 'uri': 'ETH:net13'},
                              {'name': 'net14', 'type': 'ethernet-networkV300', 'ethernetNetworkType': 'Tagged', 'vlanId': '14', 'smartLink': 'False', 'purpose': 'Management', 'privateNetwork': 'False', 'subnetUri': None, 'description': None, 'status': 'OK', 'state': 'Active', 'category': 'ethernet-networks', 'uri': 'ETH:net14'},
                              {'name': 'net15', 'type': 'ethernet-networkV300', 'ethernetNetworkType': 'Tagged', 'vlanId': '15', 'smartLink': 'False', 'purpose': 'General', 'privateNetwork': 'False', 'subnetUri': None, 'description': None, 'status': 'OK', 'state': 'Active', 'category': 'ethernet-networks', 'uri': 'ETH:net15'}]

fc_networks = [{'name': 'fa-switch1', 'autoLoginRedistribution': 'true', 'type': 'fc-networkV300', 'linkStabilityTime': '30', 'fabricType': 'FabricAttach', 'connectionTemplateUri': None, 'managedSanUri': 'FCSan:SAN1_0'},
               {'name': 'fa-switch2', 'autoLoginRedistribution': 'true', 'type': 'fc-networkV300', 'linkStabilityTime': '30', 'fabricType': 'FabricAttach', 'connectionTemplateUri': None, 'managedSanUri': 'FCSan:SAN1_1'},
               {'name': 'da-3par1-a', 'autoLoginRedistribution': 'false', 'type': 'fc-networkV300', 'linkStabilityTime': '0', 'fabricType': 'DirectAttach', 'connectionTemplateUri': None, 'managedSanUri': None},
               {'name': 'da-3par1-b', 'autoLoginRedistribution': 'true', 'type': 'fc-networkV300', 'linkStabilityTime': '0', 'fabricType': 'DirectAttach', 'connectionTemplateUri': None, 'managedSanUri': None}]

expected_fc_networks = [{'name': 'fa-switch1', 'type': 'fc-networkV300', 'fabricType': 'FabricAttach', 'linkStabilityTime': '30', 'managedSanUri': 'FCSan:SAN1_0', 'autoLoginRedistribution': 'True', 'description': None, 'status': 'OK', 'state': 'Active', 'category': 'fc-networks', 'uri': 'FC:fa-switch1'},
                        {'name': 'fa-switch2', 'type': 'fc-networkV300', 'fabricType': 'FabricAttach', 'linkStabilityTime': '30', 'managedSanUri': 'FCSan:SAN1_1', 'autoLoginRedistribution': 'True', 'description': None, 'status': 'OK', 'state': 'Active', 'category': 'fc-networks', 'uri': 'FC:fa-switch2'},
                        {'name': 'da-3par1-a', 'type': 'fc-networkV300', 'fabricType': 'DirectAttach', 'linkStabilityTime': '0', 'managedSanUri': None, 'autoLoginRedistribution': 'False', 'description': None, 'status': 'OK', 'state': 'Active', 'category': 'fc-networks', 'uri': 'FC:da-3par1-a'},
                        {'name': 'da-3par1-b', 'type': 'fc-networkV300', 'fabricType': 'DirectAttach', 'linkStabilityTime': '0', 'managedSanUri': None, 'autoLoginRedistribution': 'False', 'description': None, 'status': 'OK', 'state': 'Active', 'category': 'fc-networks', 'uri': 'FC:da-3par1-b'}]

networksets = [{'name': 'netset1', 'nativeNetworkUri': 'net10', 'type': 'network-setV300', 'networkUris': ['net10', 'net11', 'net12']},
               {'name': 'netset2', 'nativeNetworkUri': 'net13', 'type': 'network-setV300', 'networkUris': ['net13', 'net14', 'net15']}]

expected_networksets = [{'name': 'netset1', 'type': 'network-setV300', 'networkUris': ['ETH:net10', 'ETH:net11', 'ETH:net12'], 'nativeNetworkUri':'ETH:net10', 'description':None, 'status':'OK', 'state':'Active', 'category':'network-sets', 'uri':'NS:netset1'},
                        {'name': 'netset2', 'type': 'network-setV300', 'networkUris': ['ETH:net13', 'ETH:net14', 'ETH:net15'], 'nativeNetworkUri':'ETH:net13', 'description':None, 'status':'OK', 'state':'Active', 'category':'network-sets', 'uri':'NS:netset2'}]

uplink_sets = {'lig1-enet': {'name': 'lig1-enet', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['net10', 'net11', 'net12', 'net13', 'net14', 'net15'], 'mode': 'Auto',
                             'logicalPortConfigInfos': [{'bay': '1', 'port': 'X1', 'speed': 'Auto'},
                                                        {'bay': '1', 'port': 'X2', 'speed': 'Auto'},
                                                        {'bay': '2', 'port': 'X1', 'speed': 'Auto'},
                                                        {'bay': '2', 'port': 'X2', 'speed': 'Auto'}]},

               'lig1-fa-switch1': {'name': 'lig1-fa-switch1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'name': 'lig1-fa-switch1', 'networkUris': ['fa-switch1'], 'mode': 'Auto',
                                   'logicalPortConfigInfos': [{'bay': '1', 'port': 'X7', 'speed': 'Auto'}]},

               'lig1-fa-switch2': {'name': 'lig1-fa-switch2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'name': 'lig1-fa-switch2', 'networkUris': ['fa-switch2'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                   'logicalPortConfigInfos': [{'bay': '2', 'port': 'X7', 'speed': 'Auto'}]},

               'lig1-da-3par1-a': {'name': 'lig1-da-3par1-a', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'name': 'lig1-da-3par1-a', 'networkUris': ['da-3par1-a'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                   'logicalPortConfigInfos': [{'bay': '1', 'port': 'X3', 'speed': 'Auto'}]},

               'lig1-da-3par1-b': {'name': 'lig1-da-3par1-b', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'name': 'lig1-da-3par1-b', 'networkUris': ['da-3par1-b'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                   'logicalPortConfigInfos': [{'bay': '2', 'port': 'X3', 'speed': 'Auto'}]},
               }

ligs = [{"name": "lig_dcs_2", "type": "logical-interconnect-groupV300", "internalNetworkUris": [], "enclosureType": "C7000", "status": None,
         "ethernetSettings": None, "description": None, "state": None, "category": None, "created": None, "modified": None, "eTag": None, "uri": None,
         "uplinkSets": [uplink_sets['lig1-enet'].copy(),
                        uplink_sets['lig1-fa-switch1'].copy(),
                        uplink_sets['lig1-fa-switch2'].copy(),
                        uplink_sets['lig1-da-3par1-a'].copy(),
                        uplink_sets['lig1-da-3par1-b'].copy()],
         'interconnectMapTemplate': [{'bay': 1, 'enclosure': 1, 'type': 'HP VC FlexFabric-20/40 F8 Module', 'enclosureIndex': 1},
                                     {'bay': 2, 'enclosure': 1, 'type': 'HP VC FlexFabric-20/40 F8 Module', 'enclosureIndex': 1}],
         "qosConfiguration": {"activeQosConfig": {"type": "QosConfiguration", "configType": "Passthrough", "downlinkClassificationType": None, "uplinkClassificationType": None, "qosTrafficClassifiers": None, "description": None, "status": None, "name": None, "state": None, "category": "qos-aggregated-configuration", "created": None, "modified": None, "eTag": None, "uri": None}, "inactiveFCoEQosConfig": None, "inactiveNonFCoEQosConfig": None, "type": "qos-aggregated-configuration", "name": None, "state": None, "status": None, "eTag": None, "modified": None, "created": None, "category": "qos-aggregated-configuration", "uri": None}}]

expected_lig = [{"type": "logical-interconnect-groupV300",
                 "enclosureType": "C7000",
#                "uplink_sets"=[]
                 "qosConfiguration": {"type": "qos-aggregated-configuration","inactiveFCoEQosConfig": None,"inactiveNonFCoEQosConfig": None,
                                      "activeQosConfig": {"type": "QosConfiguration","qosTrafficClassifiers": [],
                                                          "uplinkClassificationType": None,"downlinkClassificationType": None,"configType": "Passthrough","description": None,"name": None,
                                                          "state": None,"status": None,"created":None,"modified": None,"eTag": None,
                                                          "category": "qos-aggregated-configuration","uri": None},"description": None,"name": None,
                                                          "state": None,"status": None,"eTag": None,"category": "qos-aggregated-configuration","uri": None},"internalNetworkUris": [],"enclosureIndexes": [1],"redundancyType": None,
                 "stackingHealth": None,
                 "interconnectBaySet": None,"stackingMode": None,"scopeUris": [],"description": None,
                 "name": "lig_dcs_2","state": "Active","status": None,
                 "category": "logical-interconnect-groups","uri":"LIG:lig_dcs_2"}]

encgroups_add = [{'name': 'encgrp1', 'type': 'EnclosureGroupV400', 'interconnectBayMappings': [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:lig_dcs_2'}, {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:lig_dcs_2'}], "interconnectBayMappingCount": 2, "stackingMode": "Enclosure", "configurationScript": "", "uri": None, "powerMode": None, "ipRangeUris": [], "enclosureCount":1, "osDeploymentSettings":None, "enclosureTypeUri":"/rest/enclosure-types/c7000"}]

expected_encgroups_add = [{'type': 'EnclosureGroupV400', 'uri': 'EG:encgrp1', 'category': 'enclosure-groups', 'name': 'encgrp1', 'status': 'OK', 'state': 'Normal', 'enclosureTypeUri': '/rest/enclosure-types/c7000', 'stackingMode': 'Enclosure', 'portMappingCount': 8, 'interconnectBayMappingCount': 2, 'interconnectBayMappings': [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:lig_dcs_2'}, {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:lig_dcs_2'}], 'ipAddressingMode': 'External', 'ipRangeUris': [], 'powerMode':None, 'description':None, 'osDeploymentSettings':None, 'enclosureCount':1, 'associatedLogicalInterconnectGroups':['LIG:lig_dcs_2']}]

rackservers = [{"name": "172.18.6.15", "hostname": "172.18.6.15", "username": "dcs", "password": "dcs", "force": False, "licensingIntent": "OneViewNoiLO", "configurationState": "Managed"}]

expected_rackservers = [{"type": "server-hardware-6", "name": "172.18.6.15", "state": "NoProfileApplied", "stateReason": "NotApplicable", "assetTag": "[Unknown]", "formFactor": "1U", "intelligentProvisioningVersion": "Unknown", "licensingIntent": "OneViewNoiLO", "locationUri": None, "memoryMb": 262144, "migrationState": "Unknown", "model": "ProLiant DL360p Gen8", "mpFirmwareVersion": "2.20 Nov 01 2014", "mpHostInfo": {"mpHostName": "172.18.6.15", "mpIpAddresses": [{"address": "172.18.6.15","type": "DHCP"},{"address": "fe80:0:0:0:2:ff:fe03:7","type": "LinkLocal"}]}, "mpModel": "iLO4", "mpState": "OK", "partNumber": "603718-F21", "portMap": None, "position": 0, "powerLock": False, "powerState": "Off", "processorCoreCount": 8, "processorCount": 2, "processorSpeedMhz": 2600, "processorType": "Intel(R) Xeon(R) CPU E5-2650L 0 @ 1.80GHz", "refreshState": "NotRefreshing","romVersion": "P71 09/30/2011", "scopeUris": [], "serialNumber":"MXQ1000207", "serverGroupUri":None, "serverHardwareTypeUri":"SHT:DL360p Gen8 1", "serverProfileUri":None, "serverSettings":None, "shortModel": "DL360p Gen8", "signature": None, "status": "OK", "uidState": "Unsupported", "uri": "SH:172.18.6.15", "uuid": "37333036-3831-584D-5131-303030323037", "virtualSerialNumber": None, "virtualUuid": None}]

enclosures = [{"name": "Encl1", "hostname": "172.18.1.11", "username": "dcs", "password": "dcs", "enclosureGroupUri": "EG:encgrp1", "firmwareBaselineUri": None, "updateFirmwareOn": None, "force": True, "forceInstallFirmware": False, "licensingIntent": "OneViewNoiLO"},
              {"name": "Encl2", "hostname": "172.18.1.13", "username": "dcs", "password": "dcs", "enclosureGroupUri": "EG:encgrp2", "firmwareBaselineUri": None, "updateFirmwareOn": None, "force": True, "forceInstallFirmware": False, "licensingIntent": "OneViewNoiLO"}]

expected_enclosures = [{'name': 'Encl1', 'type': 'EnclosureV400', 'supportState': 'Disabled',
                        'remoteSupportSettings': {'remoteSupportCurrentState': 'Unregistered', 'destination': ''},
                        'supportDataCollectionType': None, 'supportDataCollectionState': None, 'serialNumber': 'SGH100X6J1', 'enclosureType': 'C7000', 'licensingIntent': 'OneViewNoiLO',
                        'interconnectBays': [{'bayNumber': 1, 'interconnectUri': 'IC:Encl1, interconnect 1', 'logicalInterconnectUri': 'LI:Encl1-lig_dcs_2', 'interconnectModel': 'HP VC FlexFabric-20/40 F8 Module', 'ipv4Setting': None, 'serialNumber': 'WECFSED100', 'changeState': 'None', 'bayPowerState': 'Unknown', 'interconnectBayType': 'C7000InterconnectBay'},
                                             {'bayNumber': 2, 'interconnectUri': 'IC:Encl1, interconnect 2', 'logicalInterconnectUri': 'LI:Encl1-lig_dcs_2', 'interconnectModel': 'HP VC FlexFabric-20/40 F8 Module', 'ipv4Setting': None, 'serialNumber': 'WECFSED101', 'changeState': 'None', 'bayPowerState': 'Unknown', 'interconnectBayType': 'C7000InterconnectBay'},
                                             {'bayNumber': 3, 'interconnectUri': None, 'logicalInterconnectUri': None, 'interconnectModel': None, 'ipv4Setting': None, 'serialNumber': None, 'changeState': 'None', 'bayPowerState': 'Unknown', 'interconnectBayType': 'C7000InterconnectBay'},
                                             {'bayNumber': 4, 'interconnectUri': None, 'logicalInterconnectUri': None, 'interconnectModel': None, 'ipv4Setting': None, 'serialNumber': None, 'changeState': 'None', 'bayPowerState': 'Unknown', 'interconnectBayType': 'C7000InterconnectBay'},
                                             {'bayNumber': 5, 'interconnectUri': None, 'logicalInterconnectUri': None, 'interconnectModel': None, 'ipv4Setting': None, 'serialNumber': None, 'changeState': 'None', 'bayPowerState': 'Unknown', 'interconnectBayType': 'C7000InterconnectBay'},
                                             {'bayNumber': 6, 'interconnectUri': None, 'logicalInterconnectUri': None, 'interconnectModel': None, 'ipv4Setting': None, 'serialNumber': None, 'changeState': 'None', 'bayPowerState': 'Unknown', 'interconnectBayType': 'C7000InterconnectBay'},
                                             {'bayNumber': 7, 'interconnectUri': None, 'logicalInterconnectUri': None, 'interconnectModel': None, 'ipv4Setting': None, 'serialNumber': None, 'changeState': 'None', 'bayPowerState': 'Unknown', 'interconnectBayType': 'C7000InterconnectBay'},
                                             {'bayNumber': 8, 'interconnectUri': None, 'logicalInterconnectUri': None, 'interconnectModel': None, 'ipv4Setting': None, 'serialNumber': None, 'changeState': 'None', 'bayPowerState': 'Unknown', 'interconnectBayType': 'C7000InterconnectBay'}],
                        'managerBays': [{'role': 'Active', 'ipAddress': '172.18.1.11', 'bayNumber': 1, 'changeState': 'None', 'fwVersion': '4.01', 'devicePresence': 'Present', 'uidState': None, 'bayPowerState': 'Unknown', 'managerType': 'OA', 'fwBuildDate': 'April 01 2013', 'dhcpIpv6Enable': False, 'ipv6Addresses': [], 'fqdnHostName':'172.18.1.11', 'dhcpEnable':True},
                                        {'role': 'Standby', 'ipAddress': '172.18.1.12', 'bayNumber': 2, 'changeState': 'None', 'fwVersion': '4.01', 'devicePresence': 'Present', 'uidState': None, 'bayPowerState': 'Unknown', 'managerType': 'OA', 'fwBuildDate': 'April 01 2013', 'dhcpIpv6Enable': False, 'ipv6Addresses': [], 'fqdnHostName':'172.18.1.12', 'dhcpEnable':True}],
                        'enclosureTypeUri':'/rest/enclosure-types/c7000', 'interconnectBayCount':8, 'uidState':None, 'enclosureGroupUri':'EG:encgrp1',
                        'deviceBays':[{'type': 'DeviceBayV300', 'bayNumber': 1, 'model': None, 'devicePresence': 'Present', 'profileUri': None, 'deviceUri': 'SH:Encl1, bay 1', 'deviceBayType': 'C7000DeviceBay', 'deviceFormFactor': 'DoubleHeightSingleWide'},
                                      {'type': 'DeviceBayV300', 'bayNumber': 2, 'model': None, 'devicePresence': 'Present', 'profileUri': None, 'deviceUri': 'SH:Encl1, bay 2', 'coveredByProfile': None, 'deviceBayType': 'C7000DeviceBay', 'deviceFormFactor': 'DoubleHeightSingleWide'},
                                      {'type': 'DeviceBayV300', 'bayNumber': 3, 'model': None, 'devicePresence': 'Present', 'profileUri': None, 'deviceUri': 'SH:Encl1, bay 3', 'deviceFormFactor': 'SingleHeightSingleWide'},
                                      {'type': 'DeviceBayV300', 'bayNumber': 4, 'model': None, 'devicePresence': 'Present', 'profileUri': None, 'deviceUri': 'SH:Encl1, bay 4', 'deviceFormFactor': 'SingleHeightSingleWide'},
                                      {'type': 'DeviceBayV300', 'bayNumber': 5, 'model': None, 'devicePresence': 'Present', 'profileUri': None, 'deviceUri': 'SH:Encl1, bay 5', 'deviceFormFactor': 'SingleHeightSingleWide'},
                                      {'type': 'DeviceBayV300', 'bayNumber': 6, 'model': None, 'devicePresence': 'Present', 'profileUri': None, 'deviceUri': 'SH:Encl1, bay 6', 'deviceFormFactor': 'SingleHeightSingleWide'},
                                      {'type': 'DeviceBayV300', 'bayNumber': 7, 'model': None, 'devicePresence': 'Present', 'profileUri': None, 'deviceUri': 'SH:Encl1, bay 7', 'deviceFormFactor': 'SingleHeightSingleWide'},
                                      {'type': 'DeviceBayV300', 'bayNumber': 8, 'model': None, 'devicePresence': 'Present', 'profileUri': None, 'deviceUri': 'SH:Encl1, bay 8', 'deviceFormFactor': 'SingleHeightSingleWide'},
                                      {'type': 'DeviceBayV300', 'bayNumber': 9, 'model': None, 'devicePresence': 'Subsumed', 'profileUri': None, 'deviceUri': None, 'deviceFormFactor': 'DoubleHeightSingleWide'},
                                      {'type': 'DeviceBayV300', 'bayNumber': 10, 'model': None, 'devicePresence': 'Subsumed', 'profileUri': None, 'deviceUri': None, 'deviceFormFactor': 'DoubleHeightSingleWide'},
                                      {'type': 'DeviceBayV300', 'bayNumber': 11, 'model': None, 'devicePresence': 'Present', 'profileUri': None, 'deviceUri': 'SH:Encl1, bay 11', 'deviceFormFactor': 'SingleHeightSingleWide'},
                                      {'type': 'DeviceBayV300', 'bayNumber': 12, 'model': None, 'devicePresence': 'Present', 'profileUri': None, 'deviceUri': 'SH:Encl1, bay 12', 'deviceFormFactor': 'SingleHeightSingleWide'},
                                      {'type': 'DeviceBayV300', 'bayNumber': 13, 'model': None, 'devicePresence': 'Present', 'profileUri': None, 'deviceUri': 'SH:Encl1, bay 13', 'deviceFormFactor': 'SingleHeightSingleWide'},
                                      {'type': 'DeviceBayV300', 'bayNumber': 14, 'model': None, 'devicePresence': 'Present', 'profileUri': None, 'deviceUri': 'SH:Encl1, bay 14', 'deviceFormFactor': 'SingleHeightSingleWide'},
                                      {'type': 'DeviceBayV300', 'bayNumber': 15, 'model': None, 'devicePresence': 'Present', 'profileUri': None, 'deviceUri': 'SH:Encl1, bay 15', 'deviceFormFactor': 'SingleHeightSingleWide'},
                                      {'type': 'DeviceBayV300', 'bayNumber': 16, 'model': None, 'devicePresence': 'Present', 'profileUri': None, 'deviceUri': 'SH:Encl1, bay 16', 'deviceFormFactor': 'SingleHeightSingleWide'}],
                        'uuid': '09SGH100X6J1', 'fwBaselineUri': None, 'logicalEnclosureUri': 'LE:Encl1', 'partNumber': '507019-B21', 'deviceBayCount': 16, 'isFwManaged': False,
                        'powerSupplyBays': [{'bayNumber': 1, 'devicePresence': 'Present', 'status': 'OK', 'model': 'HP 2400W HE PSU', 'serialNumber': '5AGUD100L2V2LZ', 'partNumber': '499253-B21', 'sparePartNumber': '500242-001', 'changeState': 'None', 'powerSupplyBayType': 'C7000PowerSupplyBay'},
                                            {'bayNumber': 2, 'devicePresence': 'Present', 'status': 'OK', 'model': 'HP 2400W HE PSU', 'serialNumber': '5AGUD101L2V2LZ', 'partNumber': '499253-B21', 'sparePartNumber': '500242-001', 'changeState': 'None', 'powerSupplyBayType': 'C7000PowerSupplyBay'},
                                            {'bayNumber': 3, 'devicePresence': 'Present', 'status': 'OK', 'model': 'HP 2400W HE PSU', 'serialNumber': '5AGUD102L2V2LZ', 'partNumber': '499253-B21', 'sparePartNumber': '500242-001', 'changeState': 'None', 'powerSupplyBayType': 'C7000PowerSupplyBay'},
                                            {'bayNumber': 4, 'devicePresence': 'Present', 'status': 'OK', 'model': 'HP 2400W HE PSU', 'serialNumber': '5AGUD103L2V2LZ', 'partNumber': '499253-B21', 'sparePartNumber': '500242-001', 'changeState': 'None', 'powerSupplyBayType': 'C7000PowerSupplyBay'},
                                            {'bayNumber': 5, 'devicePresence': 'Present', 'status': 'OK', 'model': 'HP 2400W HE PSU', 'serialNumber': '5AGUD104L2V2LZ', 'partNumber': '499253-B21', 'sparePartNumber': '500242-001', 'changeState': 'None', 'powerSupplyBayType': 'C7000PowerSupplyBay'},
                                            {'bayNumber': 6, 'devicePresence': 'Present', 'status': 'OK', 'model': 'HP 2400W HE PSU', 'serialNumber': '5AGUD105L2V2LZ', 'partNumber': '499253-B21', 'sparePartNumber': '500242-001', 'changeState': 'None', 'powerSupplyBayType': 'C7000PowerSupplyBay'}],
                        'fanBays': [{'bayNumber': 1, 'devicePresence': 'Present', 'deviceRequired': False, 'status': 'OK', 'model': 'Fan', 'partNumber': '412140-B21', 'sparePartNumber': '413996-001', 'changeState': 'None', 'fanBayType': 'C7000FanBay', 'state': 'OK'},
                                    {'bayNumber': 2, 'devicePresence': 'Present', 'deviceRequired': False, 'status': 'OK', 'model': 'Fan', 'partNumber': '412140-B21', 'sparePartNumber': '413996-001', 'changeState': 'None', 'fanBayType': 'C7000FanBay', 'state': 'OK'},
                                    {'bayNumber': 3, 'devicePresence': 'Present', 'deviceRequired': True, 'status': 'OK', 'model': 'Fan', 'partNumber': '412140-B21', 'sparePartNumber': '413996-001', 'changeState': 'None', 'fanBayType': 'C7000FanBay', 'state': 'OK'},
                                    {'bayNumber': 4, 'devicePresence': 'Present', 'deviceRequired': True, 'status': 'OK', 'model': 'Fan', 'partNumber': '412140-B21', 'sparePartNumber': '413996-001', 'changeState': 'None', 'fanBayType': 'C7000FanBay', 'state': 'OK'},
                                    {'bayNumber': 5, 'devicePresence': 'Present', 'deviceRequired': True, 'status': 'OK', 'model': 'Fan', 'partNumber': '412140-B21', 'sparePartNumber': '413996-001', 'changeState': 'None', 'fanBayType': 'C7000FanBay', 'state': 'OK'},
                                    {'bayNumber': 6, 'devicePresence': 'Present', 'deviceRequired': False, 'status': 'OK', 'model': 'Fan', 'partNumber': '412140-B21', 'sparePartNumber': '413996-001', 'changeState': 'None', 'fanBayType': 'C7000FanBay', 'state': 'OK'},
                                    {'bayNumber': 7, 'devicePresence': 'Present', 'deviceRequired': False, 'status': 'OK', 'model': 'Fan', 'partNumber': '412140-B21', 'sparePartNumber': '413996-001', 'changeState': 'None', 'fanBayType': 'C7000FanBay', 'state': 'OK'},
                                    {'bayNumber': 8, 'devicePresence': 'Present', 'deviceRequired': True, 'status': 'OK', 'model': 'Fan', 'partNumber': '412140-B21', 'sparePartNumber': '413996-001', 'changeState': 'None', 'fanBayType': 'C7000FanBay', 'state': 'OK'},
                                    {'bayNumber': 9, 'devicePresence': 'Present', 'deviceRequired': True, 'status': 'OK', 'model': 'Fan', 'partNumber': '412140-B21', 'sparePartNumber': '413996-001', 'changeState': 'None', 'fanBayType': 'C7000FanBay', 'state': 'OK'},
                                    {'bayNumber': 10, 'devicePresence': 'Present', 'deviceRequired': True, 'status': 'OK', 'model': 'Fan', 'partNumber': '412140-B21', 'sparePartNumber': '413996-001', 'changeState': 'None', 'fanBayType': 'C7000FanBay', 'state': 'OK'}],
                        'fwBaselineName': None, 'reconfigurationState': 'NotReapplyingConfiguration', 'forceInstallFirmware': False, 'fanBayCount': 10, 'powerSupplyBayCount': 6, 'enclosureModel': 'BladeSystem c7000 Enclosure G3', 'refreshState': 'NotRefreshing',
                        'status': 'OK', 'uri': 'ENC:Encl1', 'stateReason': 'None', 'description': None, 'category': 'enclosures',
                        'standbyOaPreferredIP': '172.18.1.12', 'activeOaPreferredIP': '172.18.1.11', 'assetTag': '', 'rackName': 'Rack-221', 'vcmDomainName': 'OneViewDomain', 'oaBays': 2, 'migrationState': 'NotApplicable'},

                       {'name': 'Encl2', 'type': 'EnclosureV400', 'scopeUris': [], 'supportState':'Disabled',
                        'remoteSupportSettings':{'remoteSupportCurrentState': 'Unregistered', 'destination': ''},
                        'supportDataCollectionType': None, 'supportDataCollectionState': None, 'serialNumber': 'SGH102X6J1', 'enclosureType': 'C7000', 'licensingIntent': 'OneViewNoiLO',
                        'interconnectBays': [{'bayNumber': 1, 'interconnectUri': 'IC:Encl2, interconnect 1', 'logicalInterconnectUri': 'LI:Encl2-lig_dcs_2', 'interconnectModel': 'HP VC FlexFabric-20/40 F8 Module', 'ipv4Setting': None, 'serialNumber': 'WECFSED102', 'changeState': 'None', 'bayPowerState': 'Unknown', 'interconnectBayType': 'C7000InterconnectBay'},
                                             {'bayNumber': 2, 'interconnectUri': 'IC:Encl2, interconnect 2', 'logicalInterconnectUri': 'LI:Encl2-lig_dcs_2', 'interconnectModel': 'HP VC FlexFabric-20/40 F8 Module', 'ipv4Setting': None, 'serialNumber': 'WECFSED103', 'changeState': 'None', 'bayPowerState': 'Unknown', 'interconnectBayType': 'C7000InterconnectBay'},
                                             {'bayNumber': 3, 'interconnectUri': None, 'logicalInterconnectUri': None, 'interconnectModel': None, 'ipv4Setting': None, 'serialNumber': None, 'changeState': 'None', 'bayPowerState': 'Unknown', 'interconnectBayType': 'C7000InterconnectBay'},
                                             {'bayNumber': 4, 'interconnectUri': None, 'logicalInterconnectUri': None, 'interconnectModel': None, 'ipv4Setting': None, 'serialNumber': None, 'changeState': 'None', 'bayPowerState': 'Unknown', 'interconnectBayType': 'C7000InterconnectBay'},
                                             {'bayNumber': 5, 'interconnectUri': None, 'logicalInterconnectUri': None, 'interconnectModel': None, 'ipv4Setting': None, 'serialNumber': None, 'changeState': 'None', 'bayPowerState': 'Unknown', 'interconnectBayType': 'C7000InterconnectBay'},
                                             {'bayNumber': 6, 'interconnectUri': None, 'logicalInterconnectUri': None, 'interconnectModel': None, 'ipv4Setting': None, 'serialNumber': None, 'changeState': 'None', 'bayPowerState': 'Unknown', 'interconnectBayType': 'C7000InterconnectBay'},
                                             {'bayNumber': 7, 'interconnectUri': None, 'logicalInterconnectUri': None, 'interconnectModel': None, 'ipv4Setting': None, 'serialNumber': None, 'changeState': 'None', 'bayPowerState': 'Unknown', 'interconnectBayType': 'C7000InterconnectBay'},
                                             {'bayNumber': 8, 'interconnectUri': None, 'logicalInterconnectUri': None, 'interconnectModel': None, 'ipv4Setting': None, 'serialNumber': None, 'changeState': 'None', 'bayPowerState': 'Unknown', 'interconnectBayType': 'C7000InterconnectBay'}],
                        'managerBays': [{'role': 'Active', 'ipAddress': '172.18.1.13', 'bayNumber': 1, 'changeState': 'None', 'fwVersion': '4.01', 'devicePresence': 'Present', 'uidState': None, 'bayPowerState': 'Unknown', 'managerType': 'OA', 'fwBuildDate': 'April 01 2013', 'dhcpIpv6Enable': False, 'ipv6Addresses': [], 'fqdnHostName':'172.18.1.13', 'dhcpEnable':True},
                                        {'role': 'Standby', 'ipAddress': '172.18.1.14', 'bayNumber': 2, 'changeState': 'None', 'fwVersion': '4.01', 'devicePresence': 'Present', 'uidState': None, 'bayPowerState': 'Unknown', 'managerType': 'OA', 'fwBuildDate': 'April 01 2013', 'dhcpIpv6Enable': False, 'ipv6Addresses': [], 'fqdnHostName':'172.18.1.14', 'dhcpEnable':True}],
                        'enclosureTypeUri':'/rest/enclosure-types/c7000', 'interconnectBayCount':8, 'uidState':None, 'enclosureGroupUri':'EG:encgrp1',
                        'deviceBays':[{'type': 'DeviceBayV300', 'bayNumber': 1, 'model': None, 'devicePresence': 'Present', 'profileUri': None, 'deviceUri': 'SH:Encl2, bay 1', 'deviceFormFactor': 'DoubleHeightSingleWide'},
                                      {'type': 'DeviceBayV300', 'bayNumber': 2, 'model': None, 'devicePresence': 'Present', 'profileUri': None, 'deviceUri': 'SH:Encl2, bay 2', 'deviceFormFactor': 'DoubleHeightSingleWide'},
                                      {'type': 'DeviceBayV300', 'bayNumber': 3, 'model': None, 'devicePresence': 'Present', 'profileUri': None, 'deviceUri': 'SH:Encl2, bay 3', 'deviceFormFactor': 'SingleHeightSingleWide'},
                                      {'type': 'DeviceBayV300', 'bayNumber': 4, 'model': None, 'devicePresence': 'Present', 'profileUri': None, 'deviceUri': 'SH:Encl2, bay 4', 'deviceFormFactor': 'SingleHeightSingleWide'},
                                      {'type': 'DeviceBayV300', 'bayNumber': 5, 'model': None, 'devicePresence': 'Present', 'profileUri': None, 'deviceUri': 'SH:Encl2, bay 5', 'deviceFormFactor': 'SingleHeightSingleWide'},
                                      {'type': 'DeviceBayV300', 'bayNumber': 6, 'model': None, 'devicePresence': 'Present', 'profileUri': None, 'deviceUri': 'SH:Encl2, bay 6', 'deviceFormFactor': 'SingleHeightSingleWide'},
                                      {'type': 'DeviceBayV300', 'bayNumber': 7, 'model': None, 'devicePresence': 'Present', 'profileUri': None, 'deviceUri': 'SH:Encl2, bay 7', 'deviceFormFactor': 'SingleHeightSingleWide'},
                                      {'type': 'DeviceBayV300', 'bayNumber': 8, 'model': None, 'devicePresence': 'Present', 'profileUri': None, 'deviceUri': 'SH:Encl2, bay 8', 'deviceFormFactor': 'SingleHeightSingleWide'},
                                      {'type': 'DeviceBayV300', 'bayNumber': 9, 'model': None, 'devicePresence': 'Subsumed', 'profileUri': None, 'deviceUri': None, 'deviceFormFactor': 'DoubleHeightSingleWide'},
                                      {'type': 'DeviceBayV300', 'bayNumber': 10, 'model': None, 'devicePresence': 'Subsumed', 'profileUri': None, 'deviceUri': None, 'deviceFormFactor': 'DoubleHeightSingleWide'},
                                      {'type': 'DeviceBayV300', 'bayNumber': 11, 'model': None, 'devicePresence': 'Present', 'profileUri': None, 'deviceUri': 'SH:Encl2, bay 11', 'deviceFormFactor': 'SingleHeightSingleWide'},
                                      {'type': 'DeviceBayV300', 'bayNumber': 12, 'model': None, 'devicePresence': 'Present', 'profileUri': None, 'deviceUri': 'SH:Encl2, bay 12', 'deviceFormFactor': 'SingleHeightSingleWide'},
                                      {'type': 'DeviceBayV300', 'bayNumber': 13, 'model': None, 'devicePresence': 'Present', 'profileUri': None, 'deviceUri': 'SH:Encl2, bay 13', 'deviceFormFactor': 'SingleHeightSingleWide'},
                                      {'type': 'DeviceBayV300', 'bayNumber': 14, 'model': None, 'devicePresence': 'Present', 'profileUri': None, 'deviceUri': 'SH:Encl2, bay 14', 'deviceFormFactor': 'SingleHeightSingleWide'},
                                      {'type': 'DeviceBayV300', 'bayNumber': 15, 'model': None, 'devicePresence': 'Present', 'profileUri': None, 'deviceUri': 'SH:Encl2, bay 15', 'deviceFormFactor': 'SingleHeightSingleWide'},
                                      {'type': 'DeviceBayV300', 'bayNumber': 16, 'model': None, 'devicePresence': 'Present', 'profileUri': None, 'deviceUri': 'SH:Encl2, bay 16', 'deviceFormFactor': 'SingleHeightSingleWide'}],
                        'uuid': '09SGH102X6J1', 'fwBaselineUri': None, 'logicalEnclosureUri': 'LE:Encl2', 'partNumber': '507019-B21', 'deviceBayCount': 16, 'isFwManaged': False,
                        'powerSupplyBays': [{'bayNumber': 1, 'devicePresence': 'Present', 'status': 'OK', 'model': 'HP 2400W HE PSU', 'serialNumber': '5AGUD106L2V2LZ', 'partNumber': '499253-B21', 'sparePartNumber': '500242-001', 'changeState': 'None', 'powerSupplyBayType': 'C7000PowerSupplyBay'},
                                            {'bayNumber': 2, 'devicePresence': 'Present', 'status': 'OK', 'model': 'HP 2400W HE PSU', 'serialNumber': '5AGUD107L2V2LZ', 'partNumber': '499253-B21', 'sparePartNumber': '500242-001', 'changeState': 'None', 'powerSupplyBayType': 'C7000PowerSupplyBay'},
                                            {'bayNumber': 3, 'devicePresence': 'Present', 'status': 'OK', 'model': 'HP 2400W HE PSU', 'serialNumber': '5AGUD108L2V2LZ', 'partNumber': '499253-B21', 'sparePartNumber': '500242-001', 'changeState': 'None', 'powerSupplyBayType': 'C7000PowerSupplyBay'},
                                            {'bayNumber': 4, 'devicePresence': 'Present', 'status': 'OK', 'model': 'HP 2400W HE PSU', 'serialNumber': '5AGUD109L2V2LZ', 'partNumber': '499253-B21', 'sparePartNumber': '500242-001', 'changeState': 'None', 'powerSupplyBayType': 'C7000PowerSupplyBay'},
                                            {'bayNumber': 5, 'devicePresence': 'Present', 'status': 'OK', 'model': 'HP 2400W HE PSU', 'serialNumber': '5AGUD110L2V2LZ', 'partNumber': '499253-B21', 'sparePartNumber': '500242-001', 'changeState': 'None', 'powerSupplyBayType': 'C7000PowerSupplyBay'},
                                            {'bayNumber': 6, 'devicePresence': 'Present', 'status': 'OK', 'model': 'HP 2400W HE PSU', 'serialNumber': '5AGUD111L2V2LZ', 'partNumber': '499253-B21', 'sparePartNumber': '500242-001', 'changeState': 'None', 'powerSupplyBayType': 'C7000PowerSupplyBay'}],
                        'fanBays': [{'bayNumber': 1, 'devicePresence': 'Present', 'deviceRequired': False, 'status': 'OK', 'model': 'Fan', 'partNumber': '412140-B21', 'sparePartNumber': '413996-001', 'changeState': 'None', 'fanBayType': 'C7000FanBay', 'state': 'OK'},
                                    {'bayNumber': 2, 'devicePresence': 'Present', 'deviceRequired': False, 'status': 'OK', 'model': 'Fan', 'partNumber': '412140-B21', 'sparePartNumber': '413996-001', 'changeState': 'None', 'fanBayType': 'C7000FanBay', 'state': 'OK'},
                                    {'bayNumber': 3, 'devicePresence': 'Present', 'deviceRequired': True, 'status': 'OK', 'model': 'Fan', 'partNumber': '412140-B21', 'sparePartNumber': '413996-001', 'changeState': 'None', 'fanBayType': 'C7000FanBay', 'state': 'OK'},
                                    {'bayNumber': 4, 'devicePresence': 'Present', 'deviceRequired': True, 'status': 'OK', 'model': 'Fan', 'partNumber': '412140-B21', 'sparePartNumber': '413996-001', 'changeState': 'None', 'fanBayType': 'C7000FanBay', 'state': 'OK'},
                                    {'bayNumber': 5, 'devicePresence': 'Present', 'deviceRequired': True, 'status': 'OK', 'model': 'Fan', 'partNumber': '412140-B21', 'sparePartNumber': '413996-001', 'changeState': 'None', 'fanBayType': 'C7000FanBay', 'state': 'OK'},
                                    {'bayNumber': 6, 'devicePresence': 'Present', 'deviceRequired': False, 'status': 'OK', 'model': 'Fan', 'partNumber': '412140-B21', 'sparePartNumber': '413996-001', 'changeState': 'None', 'fanBayType': 'C7000FanBay', 'state': 'OK'},
                                    {'bayNumber': 7, 'devicePresence': 'Present', 'deviceRequired': False, 'status': 'OK', 'model': 'Fan', 'partNumber': '412140-B21', 'sparePartNumber': '413996-001', 'changeState': 'None', 'fanBayType': 'C7000FanBay', 'state': 'OK'},
                                    {'bayNumber': 8, 'devicePresence': 'Present', 'deviceRequired': True, 'status': 'OK', 'model': 'Fan', 'partNumber': '412140-B21', 'sparePartNumber': '413996-001', 'changeState': 'None', 'fanBayType': 'C7000FanBay', 'state': 'OK'},
                                    {'bayNumber': 9, 'devicePresence': 'Present', 'deviceRequired': True, 'status': 'OK', 'model': 'Fan', 'partNumber': '412140-B21', 'sparePartNumber': '413996-001', 'changeState': 'None', 'fanBayType': 'C7000FanBay', 'state': 'OK'},
                                    {'bayNumber': 10, 'devicePresence': 'Present', 'deviceRequired': True, 'status': 'OK', 'model': 'Fan', 'partNumber': '412140-B21', 'sparePartNumber': '413996-001', 'changeState': 'None', 'fanBayType': 'C7000FanBay', 'state': 'OK'}],
                        'fwBaselineName': None, 'reconfigurationState': 'NotReapplyingConfiguration', 'forceInstallFirmware': False, 'fanBayCount': 10, 'powerSupplyBayCount': 6, 'enclosureModel': 'BladeSystem c7000 Enclosure G3', 'refreshState': 'NotRefreshing',
                        'status': 'OK', 'uri': 'ENC:Encl2', 'stateReason': 'None', 'description': None, 'category': 'enclosures',
                        'standbyOaPreferredIP': '172.18.1.14', 'activeOaPreferredIP': '172.18.1.13', 'assetTag': '', 'rackName': 'Rack-221', 'vcmDomainName': 'OneViewDomain', 'vcmMode': True, 'oaBays': 2, 'migrationState': 'NotApplicable'}]

storage_systems_with_pools = [{'name':'ThreePAR-1', 'family':'StoreServ',"hostname":"172.18.11.11",
                               "credentials":{"username":"dcs", "password": "dcs"},"serialNumber":"TXQ1000307",
                               'deviceSpecificAttributes':{'managedDomain':'TestDomain', 'managedPools': []}}]

expected_storage_systems_with_pools = [{'type':'StorageSystemV4', 'name': 'ThreePAR-1','uri':'SSYS:ThreePAR-1', 'state':'Managed',
                                        'deviceSpecificAttributes':{"managedDomain": 'TestDomain',"serialNumber": "TXQ1000307"},
                                        'status':'OK', 'category':'storage-systems'}]

storage_pools_toedit = [{"storageSystemUri": 'ThreePAR-1', "name": 'FST_CPG1', "isManaged": True},
                        {"storageSystemUri": 'ThreePAR-1', "name": 'FST_CPG2', "isManaged": True}]

storage_volume_templates = [{"name":"ova-private-thin","description":"", "rootTemplateUri":"SVT:ova-private-thin", "description":"private non-boot volume template",
                             "properties": {"name": {"title": "Volume name", "description":"A volume name between 1 and 100 characters", "type":"string","minLength":1,"maxLength":100,"required":True, "meta":{"locked":False}},
                                            "description":{"title":"Description","description":"A description for the volume", "type":"string","minLength":0,"maxLength":2000,"default":"", "meta":{"locked":False}},
                                            "storagePool":{"title":"Storage Pool","description":"A common provisioning group URI reference", "type":"string","required":True,"format":"x-uri-reference", "meta":{"locked":False,"createOnly":True,"semanticType":"device-storage-pool"}, "default": "FST_CPG1"},
                                            "size":{"title":"Capacity","description":"The capacity of the volume in bytes", "type":"integer","required":True,"minimum":1073741824,"maximum":17592186044416, "meta":{"locked":False,"semanticType":"capacity"}, "default":1073741824,},
                                            "isShareable":{"title":"Is Shareable","description":"The shareability of the volume", "type":"boolean","meta":{"locked":False}, "default":False,},
                                            "provisioningType":{"title":"Provisioning Type","description":"The provisioning type for the volume", "type":"string","enum":["Thin","Full"],"meta":{"locked":True,"createOnly":True}, "default":"Thin"},
                                            "snapshotPool":{"title":"FC_wpst16_r1","description":"A URI referenceto the common provisioning group used to create snapshots", "type":"string","format":"x-uri-reference","meta":{"locked":True,"semanticType":"device-snapshot-storage-pool"}, "default": "FST_CPG1"}}}]

expected_storage_volume_templates = [{"category": "storage-volume-templates", "name": "ova-private-thin", "status": "OK",
                                      "state": "Configured", "type": "StorageVolumeTemplateV4", "uri": "SVT:ova-private-thin",
                                      "properties": {"name": {"title": "Volume name", "description":"A volume name between 1 and 100 characters", "type":"string","minLength":1,"maxLength":100,"required":True, "meta":{"locked":False}},
                                                     "description":{"title":"Description","description":"A description for the volume", "type":"string","minLength":0,"maxLength":2000,"default":"", "meta":{"locked":False}},
                                                     "storagePool":{"title":"Storage Pool","description":"A common provisioning group URI reference", "type":"string","required":True,"format":"x-uri-reference", "meta":{"locked":False,"createOnly":True,"semanticType":"device-storage-pool"}, "default": "SPOOL:FST_CPG1"},
                                                     "size":{"title":"Capacity","description":"The capacity of the volume in bytes", "type":"integer","required":True,"minimum":1073741824,"maximum":17592186044416, "meta":{"locked":False,"semanticType":"capacity"}, "default":1073741824,},
                                                     "isShareable":{"title":"Is Shareable","description":"The shareability of the volume", "type":"boolean","meta":{"locked":False}, "default":False,},
                                                     "provisioningType":{"title":"Provisioning Type","description":"The provisioning type for the volume", "type":"string","enum":["Thin","Full"],"meta":{"locked":True,"createOnly":True}, "default":"Thin"},
                                                     "snapshotPool":{"title":"FC_wpst16_r1","description":"A URI referenceto the common provisioning group used to create snapshots", "type":"string","format":"x-uri-reference","meta":{"locked":True,"semanticType":"device-snapshot-storage-pool"}, "default": "SPOOL:FST_CPG1"}}}]

storage_volumes = [ # new private no template
                   {"properties": {"description": "non-boot private volume", "isShareable": False, "name": "enc2bay1priv", "provisioningType": "Full", "size": 5368709120, "storagePool": "FST_CPG1"}, "templateUri": "ROOT"},
                   {"properties": {"description": "non-boot private volume", "isShareable": False, "name": "enc2bay2priv", "provisioningType": "Full", "size": 5368709120, "storagePool": "FST_CPG1"}, "templateUri": "ROOT"},
                   {"properties": {"description": "non-boot private volume", "isShareable": False, "name": "enc2bay3priv", "provisioningType": "Full", "size": 5368709120, "storagePool": "FST_CPG1"}, "templateUri": "ROOT"},
                   {"properties": {"description": "non-boot private volume", "isShareable": False, "name": "enc2bay4priv", "provisioningType": "Full", "size": 5368709120, "storagePool": "FST_CPG1"}, "templateUri": "ROOT"},
                    # new private with template
                   {"properties": {"description": "non-boot private volume", "isShareable": False, "name": "enc2bay7priv", "size": 5368709120, "storagePool": "FST_CPG1"}, "templateUri": "ova-private-thin"},
                   {"properties": {"description": "non-boot private volume", "isShareable": False, "name": "enc2bay8priv", "size": 5368709120, "storagePool": "FST_CPG1"}, "templateUri": "ova-private-thin"},
                   {"properties": {"description": "non-boot private volume", "isShareable": False, "name": "enc2bay9priv", "size": 5368709120, "storagePool": "FST_CPG1"}, "templateUri": "ova-private-thin"},
                   {"properties": {"description": "non-boot private volume", "isShareable": False, "name": "enc2bay10priv", "size": 5368709120, "storagePool": "FST_CPG1"}, "templateUri": "ova-private-thin"},
                    # shared volume
                   {"properties": {"description": "shared volume", "isShareable": True, "name": "ovacluster", "provisioningType": "Full", "size": 5368709120, "storagePool": "FST_CPG1"}, "templateUri": "ROOT"}]

expected_storage_volumes = [{'isShareable': False, 'name': 'enc2bay1priv','state': 'Managed', 'status': 'OK', 'storagePoolUri': 'SPOOL:FST_CPG1', 'type': 'StorageVolumeV4'},
                            {'isShareable': False, 'name': 'enc2bay2priv','state': 'Managed', 'status': 'OK', 'storagePoolUri': 'SPOOL:FST_CPG1', 'type': 'StorageVolumeV4'},
                            {'isShareable': False, 'name': 'enc2bay3priv','state': 'Managed', 'status': 'OK', 'storagePoolUri': 'SPOOL:FST_CPG1', 'type': 'StorageVolumeV4'},
                            {'isShareable': False, 'name': 'enc2bay4priv','state': 'Managed', 'status': 'OK', 'storagePoolUri': 'SPOOL:FST_CPG1', 'type': 'StorageVolumeV4'},

                            {'isShareable': False, 'name': 'enc2bay7priv','state': 'Managed', 'status': 'OK', 'storagePoolUri': 'SPOOL:FST_CPG1', 'type': 'StorageVolumeV4'},
                            {'isShareable': False, 'name': 'enc2bay8priv','state': 'Managed', 'status': 'OK', 'storagePoolUri': 'SPOOL:FST_CPG1', 'type': 'StorageVolumeV4'},
                            {'isShareable': False, 'name': 'enc2bay9priv','state': 'Managed', 'status': 'OK', 'storagePoolUri': 'SPOOL:FST_CPG1', 'type': 'StorageVolumeV4'},
                            {'isShareable': False, 'name': 'enc2bay10priv','state': 'Managed', 'status': 'OK', 'storagePoolUri': 'SPOOL:FST_CPG1', 'type': 'StorageVolumeV4'},

                            {'isShareable': True, 'name': 'ovacluster','state': 'Managed', 'status': 'OK', 'storagePoolUri': 'SPOOL:FST_CPG1', 'type': 'StorageVolumeV4'}]

server_profiles = [# BL Servers with connections (network set)
                          {'name': 'Encl1bay1', 'type': 'ServerProfileV7', 'serverHardwareUri': 'SH:Encl1, bay 1', 'serverHardwareTypeUri': '', 'enclosureGroupUri': '', 'serialNumberType': 'Virtual', 'iscsiInitiatorNameType': 'AutoGenerated', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                          'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500', 'networkUri': 'NS:netset1', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                          {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500', 'networkUri': 'NS:netset2', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}],
                          'boot': {'manageBoot': True, 'order': ['HardDisk']},
                          'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                          'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                          'bios': {'manageBios': False, 'overriddenSettings': []}, 'hideUnusedFlexNics':True, 'iscsiInitiatorName':'', 'osDeploymentSettings':None,
                          'localStorage':{'sasLogicalJBODs': [], 'controllers':[]}, 'sanStorage':None},

                          {'name': 'Encl2bay3', 'type': 'ServerProfileV7', 'serverHardwareUri': 'SH:Encl2, bay 3', 'serverHardwareTypeUri': '', 'enclosureGroupUri': '', 'serialNumberType': 'Virtual', 'iscsiInitiatorNameType': 'AutoGenerated', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                          'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:net10', 'mac': None, 'wwpn': '', 'wwnn': ''},
                                          {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:net11', 'mac': None, 'wwpn': '', 'wwnn': ''},
                                          {'id': 3, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:net12', 'mac': None, 'wwpn': '', 'wwnn': ''},
                                          {'id': 4, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-d', 'requestedMbps': '2500', 'networkUri': 'ETH:net13', 'mac': None, 'wwpn': '', 'wwnn': ''},
                                          {'id': 6, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:net10', 'mac': None, 'wwpn': '', 'wwnn': ''},
                                          {'id': 7, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-b', 'requestedMbps': '2500', 'networkUri': 'ETH:net11', 'mac': None, 'wwpn': '', 'wwnn': ''},
                                          {'id': 8, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-c', 'requestedMbps': '2500', 'networkUri': 'ETH:net12', 'mac': None, 'wwpn': '', 'wwnn': ''},
                                          {'id': 9, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-d', 'requestedMbps': '2500', 'networkUri': 'ETH:net13', 'mac': None, 'wwpn': '', 'wwnn': ''}],
                          'boot': None,
                          'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                          'bios': {'manageBios': False, 'overriddenSettings': []}, 'hideUnusedFlexNics':True, 'iscsiInitiatorName':'', 'osDeploymentSettings':None,
                          'localStorage':{'sasLogicalJBODs': [], 'controllers':[]}, 'sanStorage':None}]

expected_server_profiles = [{"name": "Encl2bay3","type": "ServerProfileV7","uri": "SP:Encl2bay3","description": "",
                                    "serverProfileTemplateUri": None,"templateCompliance": "Unknown",
                                    "serverHardwareUri": "SH:Encl2, bay 3","serverHardwareTypeUri": "SHT:BL460c Gen8:Flb1:HP FlexFabric 10Gb 2-port 554FLB Adapter","enclosureGroupUri": "EG:encgrp1",
                                    "enclosureUri": "ENC:Encl2","enclosureBay": 3,"affinity": "Bay","associatedServer": None,
                                    "hideUnusedFlexNics": True,"firmware": {"firmwareInstallType": None,"forceInstallFirmware": False,"firmwareBaselineUri": None,"manageFirmware": False},
                                    "macType": "Virtual","wwnType": "Virtual","serialNumberType": "Virtual","category": "server-profiles",
                                    "status": "OK","state": "Normal","inProgress": False,"connections": [{"id": 1,"name": "","functionType": "Ethernet","networkUri": "ETH:net10","portId": "Flb 1:1-a","requestedVFs":"Auto","allocatedVFs": None,"macType": "Virtual","wwpnType": "Virtual","requestedMbps": "2500","allocatedMbps": 2500,"maximumMbps": 10000,"boot": {"priority": "NotBootable"}},
                                                                                                         {"id": 2,"name": "","functionType": "Ethernet","networkUri": "ETH:net11","portId": "Flb 1:1-b","requestedVFs":"Auto","allocatedVFs": None,"macType": "Virtual","wwpnType": "Virtual","requestedMbps": "2500","allocatedMbps": 2500,"maximumMbps": 10000,"boot": {"priority": "NotBootable"}},
                                                                                                         {"id": 3,"name": "","functionType": "Ethernet","networkUri": "ETH:net12","portId": "Flb 1:1-c","requestedVFs":"Auto","allocatedVFs": None,"macType": "Virtual","wwpnType": "Virtual","requestedMbps": "2500","allocatedMbps": 2500,"maximumMbps": 10000,"boot": {"priority": "NotBootable"}},
                                                                                                         {"id": 4,"name": "","functionType": "Ethernet","networkUri": "ETH:net13","portId": "Flb 1:1-d","requestedVFs":"Auto","allocatedVFs": None,"macType": "Virtual","wwpnType": "Virtual","requestedMbps": "2500","allocatedMbps": 2500,"maximumMbps": 10000,"boot": {"priority": "NotBootable"}},
                                                                                                         {"id": 6,"name": "","functionType": "Ethernet","networkUri": "ETH:net10","portId": "Flb 1:2-a","requestedVFs":"Auto","allocatedVFs": None,"macType": "Virtual","wwpnType": "Virtual","requestedMbps": "2500","allocatedMbps": 2500,"maximumMbps": 10000,"boot": {"priority": "NotBootable"}},
                                                                                                         {"id": 7,"name": "","functionType": "Ethernet","networkUri": "ETH:net11","portId": "Flb 1:2-b","requestedVFs":"Auto","allocatedVFs": None,"macType": "Virtual","wwpnType": "Virtual","requestedMbps": "2500","allocatedMbps": 2500,"maximumMbps": 10000,"boot": {"priority": "NotBootable"}},
                                                                                                         {"id": 8,"name": "","functionType": "Ethernet","networkUri": "ETH:net12","portId": "Flb 1:2-c","requestedVFs":"Auto","allocatedVFs": None,"macType": "Virtual","wwpnType": "Virtual","requestedMbps": "2500","allocatedMbps": 2500,"maximumMbps": 10000,"boot": {"priority": "NotBootable"}},
                                                                                                         {"id": 9,"name": "","functionType": "Ethernet","networkUri": "ETH:net13","portId": "Flb 1:2-d","requestedVFs":"Auto","allocatedVFs": None,"macType": "Virtual","wwpnType": "Virtual","requestedMbps": "2500","allocatedMbps": 2500,"maximumMbps": 10000,"boot": {"priority": "NotBootable"}}],
                                    "bootMode": None, "boot": {"manageBoot": True,"order": ["CD","Floppy","USB","HardDisk","PXE"]},
                                    "bios": {"overriddenSettings": [],"manageBios": False},
                                    "localStorage": {"sasLogicalJBODs": [],"controllers": []},"sanStorage": {"volumeAttachments": [],"manageSanStorage": False},"osDeploymentSettings": None,},

                                   {"name": "Encl1bay1","type": "ServerProfileV7","uri": "SP:Encl1bay1","description": "",
                                    "serverProfileTemplateUri": None,"templateCompliance": "Unknown",
                                    "serverHardwareUri": "SH:Encl1, bay 1","serverHardwareTypeUri": "SHT:BL660c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter","enclosureGroupUri": "EG:encgrp1",
                                    "enclosureUri": "ENC:Encl1","enclosureBay": 1,"affinity": "Bay","associatedServer": None,
                                    "hideUnusedFlexNics": True,"firmware": {"firmwareInstallType": None,"forceInstallFirmware": False,"firmwareBaselineUri": None,"manageFirmware": False},
                                    "macType": "Virtual","wwnType": "Virtual","serialNumberType": "Virtual","category": "server-profiles",
                                    "status": "OK","state": "Normal","inProgress": False,"connections": [{"id": 1,"name": "","functionType": "Ethernet","networkUri": "NS:netset1","portId": "Flb 1:1-a","requestedVFs":"Auto","allocatedVFs": None,"macType": "Virtual","wwpnType": "Virtual","requestedMbps": "2500","allocatedMbps": 2500,"maximumMbps": 10000,"boot": {"priority": "NotBootable"}},
                                                                                                         {"id": 2,"name": "","functionType": "Ethernet","networkUri": "NS:netset2","portId": "Flb 1:2-a","requestedVFs":"Auto","allocatedVFs": None,"macType": "Virtual","wwpnType": "Virtual","requestedMbps": "2500","allocatedMbps": 2500,"maximumMbps": 10000,"boot": {"priority": "NotBootable"}}],
                                    "bootMode": {"pxeBootPolicy": 'Auto',"manageMode": True,"mode": "UEFI"},
                                    "boot": {"manageBoot": True,"order": ["HardDisk"]},
                                    "bios": {"overriddenSettings": [],"manageBios": False},
                                    "localStorage": {"sasLogicalJBODs": [],"controllers": []},"sanStorage": {"volumeAttachments": [],"manageSanStorage": False},"osDeploymentSettings": None,}]

server_profile_with_storage = [{'name': 'Encl2bay2', 'type': 'ServerProfileV7', 'serverHardwareUri': 'SH:Encl2, bay 2', 'serverHardwareTypeUri': '', 'enclosureGroupUri': '', 'serialNumberType': 'Physical', 'iscsiInitiatorNameType': 'AutoGenerated', 'macType': 'Physical', 'wwnType': 'Physical', 'description': '', 'affinity': 'Bay',
                                'connections': [{'id': 1, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Flb 1:1-b', 'requestedMbps': '2500', 'networkUri': 'FC:da-3par1-a', 'mac': None, 'wwpn': '', 'wwnn': '',
                                                        'boot':{'priority':'Primary', 'bootVolumeSource':'UserDefined', 'targets':[{'arrayWwpn':'21210002AC01AB7E', 'lun':'1'}]}},
                                                {'id': 2, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Flb 1:2-b', 'requestedMbps': '8000', 'networkUri': 'FC:da-3par1-b', 'mac': None, 'wwpn': '', 'wwnn': '',
                                                        'boot':{'priority':'Secondary', 'bootVolumeSource':'UserDefined', 'targets':[{'arrayWwpn':'20010002AC01AB7E', 'lun':'2'}]}}],
                                "boot": {"manageBoot": True,"order": ["HardDisk"]}, "bootMode": {"pxeBootPolicy": None,"manageMode": True,"mode": "BIOS"},
                                'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                'bios': {'manageBios': False, 'overriddenSettings': []}, 'hideUnusedFlexNics':True, 'iscsiInitiatorName':'', 'osDeploymentSettings':None,
                                'localStorage':{'sasLogicalJBODs': [], 'controllers':[]},
                                'sanStorage':{'hostOSType': 'RHE Linux (5.x, 6.x)', 'manageSanStorage': True,
                                              'volumeAttachments': [{'id': 1, 'volumeUri': 'SVOL:enc2bay2priv', 'isBootVolume': False, 'lunType': 'Manual', 'lun': 1,
                                                                     'storagePaths': [{'isEnabled': True, 'connectionId': 2, 'targetSelector': 'Auto', 'targets': []}]}]}}]

expected_server_profile_with_storage = [{"name": "Encl2bay2","type": "ServerProfileV7","uri": "SP:Encl2bay2","description": "",
                                         "serverProfileTemplateUri": None,"templateCompliance": "Unknown",
                                         "serverHardwareUri": "SH:Encl2, bay 2","serverHardwareTypeUri": "SHT:BL660c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter","enclosureGroupUri": "EG:encgrp1",
                                         "enclosureUri": "ENC:Encl2","enclosureBay": 2,"affinity": "Bay","associatedServer": None,
                                         "hideUnusedFlexNics": True,"firmware": {"firmwareInstallType": None,"forceInstallFirmware": False,"firmwareBaselineUri": None,"manageFirmware": False},
                                         "macType": "Physical","wwnType": "Physical","serialNumberType": "Physical","category": "server-profiles",
                                         "status": "OK","state": "Normal","inProgress": False,
                                         "connections": [{"id": 1,"name": "","functionType": "FibreChannel","state": "Deployed","status":"OK","networkUri": "FC:da-3par1-a",
                                                          "portId": "Flb 1:1-b","requestedVFs": None,"allocatedVFs": None,"macType": "Physical",
                                                          "wwpnType": "Physical", "requestedMbps": "2500","allocatedMbps": 2500,"maximumMbps": 10000,"boot": {"priority": "Primary","targets": [{"arrayWwpn": "21210002AC01AB7E","lun": "1"}],}},
                                                         {"id": 2,"name": "","functionType": "FibreChannel","state": "Deployed","status":"OK","networkUri": "FC:da-3par1-b",
                                                          "portId": "Flb 1:2-b","requestedVFs": None,"allocatedVFs": None,"macType": "Physical",
                                                          "wwpnType": "Physical","requestedMbps": "8000","allocatedMbps": 8000,"maximumMbps": 10000,"boot": {"priority": "Secondary","targets": [{"arrayWwpn": "20010002AC01AB7E","lun": "2"}],}}],
                                         "bootMode": {"pxeBootPolicy": None,"manageMode": True,"mode": "BIOS"}, "boot": {"manageBoot": True,"order": ["HardDisk","CD","USB","PXE"]},
                                         "bios": {"overriddenSettings": [],"manageBios": False}, "localStorage": {"sasLogicalJBODs": [],"controllers": []},
                                         "sanStorage": {"volumeAttachments": [{"storagePaths": [{"targetSelector": "Auto","targets": [{'name':"20:00:00:02:AC:00:08:DB"}],"connectionId": 2,"isEnabled": True,"status": "OK"}],"isBootVolume": False,"state": "Attached","lun": "1",
                                                                               "volumeStoragePoolUri": "SPOOL:FST_CPG1","volumeStorageSystemUri": "SYS:ThreePAR-1","lunType": "Manual","volumeUri": "SVOL:enc2bay2priv","status": "OK","id": 1},],
                                                        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)","manageSanStorage": True},"osDeploymentSettings": None,}]

server_profile_templates = [{'name': 'SPT-ENCL1-BAY1', 'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL660c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter',
                             'enclosureGroupUri': 'EG:encgrp1', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': { "manageConnections": True,
                                                    'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:net10', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:net11', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Flb 1:1-b', 'requestedMbps': '2500', 'networkUri': 'FC:da-3par1-a', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 4, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Flb 1:2-b', 'requestedMbps': '2500', 'networkUri': 'FC:da-3par1-b', 'boot': {'priority': 'NotBootable'}}]},
                             'boot': {'manageBoot': True, 'order': ['HardDisk']},
                             'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics':True, 'iscsiInitiatorNameType':'AutoGenerated',
                             'localStorage':{'sasLogicalJBODs': [], 'controllers':[]}, 'sanStorage':None}]

expected_server_profile_templates = [{'type': 'ServerProfileTemplateV3', 'uri': 'SPT:SPT-ENCL1-BAY1', 'name': 'SPT-ENCL1-BAY1', 'description': '', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL660c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter', 'enclosureGroupUri': 'EG:encgrp1', 'affinity': 'Bay', 'hideUnusedFlexNics': True, 'macType': 'Virtual', 'wwnType': 'Virtual', 'serialNumberType': 'Virtual', 'iscsiInitiatorNameType': 'AutoGenerated',
                                      'firmware': {'manageFirmware': False, 'forceInstallFirmware': False},
                                      'connectionSettings': { "manageConnections": True,
                                                    'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:net10', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:net11', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Flb 1:1-b', 'requestedMbps': '2500', 'networkUri': 'FC:da-3par1-a', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 4, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Flb 1:2-b', 'requestedMbps': '2500', 'networkUri': 'FC:da-3par1-b', 'boot': {'priority': 'NotBootable'}}]},
                                      'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                      'boot': {'manageBoot': True, 'order': ['HardDisk']}, 'bios':{'manageBios': False, 'overriddenSettings': []},
                                      'localStorage':{'sasLogicalJBODs': [], 'controllers':[]}, 'sanStorage':{'manageSanStorage': False, 'volumeAttachments': []},
                                      'category':'server-profile-templates', 'status':'OK', 'state':None}]

server_profiles_from_spt = [{'name': 'Encl1bay2', 'type': 'ServerProfileV7', 'serverHardwareUri': 'Encl1, bay 2', 'serverHardwareTypeUri': 'SHT:BL660c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter', 'enclosureGroupUri': 'EG:encgrp1', 'serialNumberType': 'Virtual', 'iscsiInitiatorNameType': 'AutoGenerated', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:net10', 'boot': {'priority': 'NotBootable'}},
                                             {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:net11', 'boot': {'priority': 'NotBootable'}},
                                             {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Flb 1:1-b', 'requestedMbps': '2500', 'networkUri': 'FC:da-3par1-a', 'boot': {'priority': 'NotBootable'}},
                                             {'id': 4, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Flb 1:2-b', 'requestedMbps': '2500', 'networkUri': 'FC:da-3par1-b', 'boot': {'priority': 'NotBootable'}}],
                             'boot': {'manageBoot': True, 'order': ['HardDisk']}, 'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []}, 'hideUnusedFlexNics':True, 'iscsiInitiatorName':'',
                             'serverProfileTemplateUri':'SPT:SPT-ENCL1-BAY1', 'osDeploymentSettings':None,
                             'localStorage':{'sasLogicalJBODs': [], 'controllers':[]}, 'sanStorage':None}]

expected_server_profiles_from_spt = [{'name': 'Encl1bay2', 'type': 'ServerProfileV7', 'serverHardwareUri': 'SH:Encl1, bay 2', 'serverHardwareTypeUri': 'SHT:BL660c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter', 'enclosureGroupUri': 'EG:encgrp1', 'serialNumberType': 'Virtual', 'iscsiInitiatorNameType': 'AutoGenerated', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                      'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:net10', 'boot': {'priority': 'NotBootable'}},
                                                      {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:net11', 'boot': {'priority': 'NotBootable'}},
                                                      {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Flb 1:1-b', 'requestedMbps': '2500', 'networkUri': 'FC:da-3par1-a', 'boot': {'priority': 'NotBootable'}},
                                                      {'id': 4, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Flb 1:2-b', 'requestedMbps': '2500', 'networkUri': 'FC:da-3par1-b', 'boot': {'priority': 'NotBootable'}}],
                                      'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                      'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                      'firmware': {'manageFirmware': False, 'forceInstallFirmware': False},
                                      'bios': {'manageBios': False, 'overriddenSettings': []},
                                      'hideUnusedFlexNics':True,
                                      'serverProfileTemplateUri':'SPT:SPT-ENCL1-BAY1', 'osDeploymentSettings':None,
                                      'localStorage':{'sasLogicalJBODs': [], 'controllers':[]}, 'sanStorage':{'manageSanStorage': False, 'volumeAttachments': []}}]

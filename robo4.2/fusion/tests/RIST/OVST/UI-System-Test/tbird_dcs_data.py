ONEVIEW_SSH_USERNAME = 'root'  # SSH Username
ONEVIEW_SSH_PASSWORD = 'hponeview'  # SSH Password

appliance = {'type': 'ApplianceNetworkConfigurationV2',
             'applianceNetworks': [{
                                    'macAddress':None,
                                    'ipv4NameServers': ['16.125.25.82'],
                                     "virtIpv4Addr":'16.114.219.35',
                                    'interfaceName': 'Appliance',
                                    'overrideIpv4DhcpDnsServers': False,
                                    'activeNode': '1',
                                    'confOneNode': True,
                                    'ipv4Type': 'STATIC',
                                    'ipv4Subnet': '255.255.240.0',
                                    'device': 'eth0',
                                    'ipv6Type': 'UNCONFIGURE',
                                    'unconfigure': False,
                                    'aliasDisabled': False,
                                    'ipv4Gateway': '16.114.208.1',
                                    'hostname': 'DCSTbird.vse.rdlabs.hpecorp.net',
                                    'searchDomains': ['vse.rdlabs.hpecorp.net'],
                                    'domainName': 'vse.rdlabs.hpecorp.net',
                                    }]}

"""
This is the time and locale settings used during FTS.
"""
timeandlocale = {'type': 'TimeAndLocale', 'dateTime': None, 'timezone': 'UTC', 'ntpServers': ['ntp.hp.net'], 'locale': 'en_US.UTF-8'}

credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}

licenses = [{'key': 'YCDG B9MA H9P9 8HV3 V7B5 HWWB Y9JL KMPL P4SA 6EZA DXAU 2CSM GHTG L762 GFD6 W9JM KJVT D5KM EFVW DT5J JQM8 M2S2 9K2P 3E22 DKAG 3UFR TZZX MB5X 82Z5 WHEF D9ED 3RUX BJS2 XFXC T84U R42A 58S5 XA2D WXAP GMTQ 4YLB MM2S CZU7 2E4X E8EW BGB5 BWPD CAAR YT9J 4NUG 2NJN J9UF "424669585 HPOV-NFR1 HP_OneView_16_Seat_NFR JJ72AYTJ2U9Y"_3JJL2-DHCDC-X5RM4-T85XX-SM962'},
            {'key': 'QCLE C9MA H9PA 8HV3 V7B5 HWWB Y9JL KMPL D4KG MEZA DXAU 2CSM GHTG L762 B57Z GLJM KJVT D5KM EFRW DS5R DQEM 7ZS2 9K2P 3E22 LKAG LUVR TZZP MB5X 82Z5 WHEF D9ED 3RUX BJS2 XFXC T84U R42A 58S5 XA2D WXAP GMTQ 4YLB MM2S CZU7 2E4X E8EW BGB5 BWPD CAAR YT9J 4NUG 2NJN J9UF "424669494 HPOV-NFR1 HP_OneView_16_Seat_NFR ADEJAYTJC7YC"_3JJKW-KM6WK-KZ45Y-V6789-9Q5J6'},
            {'key': 'QCLE A9MA H9PY KHV2 U7B5 HWW5 Y9JL KMPL R42E NFJA DXAU 2CSM GHTG L762 WFH4 G9J4 KJVT D5KM EFVW DT5J RQUK 42C2 9K2P 3E22 DKAG 3UFR TZZH AB6X 82Z5 WHEF D9ED 3RUX BJS2 XFXC T84U R42A 58S5 XA2D WXAP GMTQ 4YLB MM2S CZU7 2E4X E8EW BGB5 BWPD CAAR 2T9J MNEG 2NJN J9UF "424669587 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR 66CAAYTJCJA7"'},
            {'key': 'YC3G A9MA H9P9 KHW3 U7B5 HWW5 Y9JL KMPL F42C PEJA DXAU 2CSM GHTG L762 AB36 XJZU KJVT D5KM EFRW DS5R FQU9 6ZC2 9K2P 3E22 LKAG LUVR TZZX MB5X 82Z5 WHEF D9ED 3RUX BJS2 XFXC T84U R42A 58S5 XA2D WXAP GMTQ 4YLB MM2S CZU7 2E4X E8EW BGB5 BWPD CAAR 2T9J MNEG 2NJN J9UF "424669495 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR 3GJ9AYTJ275U"'},
            {'key': '9B2G D9MA H9PA CHVZ V2B4 HWWV Y9JL KMPL B89H MZVU 6RMS 9HWE 92R6 3FZ3 CMRG HPMR MFVU A5K9 MHGK EKX9 HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'},
            {'key': 'YBKA D9MA H9P9 8HX3 V2B4 HWWV Y9JL KMPL B89H MZVU GR4S JHWE J2SP XNZ8 CMRG HPMR UFVU A5K9 MWHC 9K4K HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'}]

users = [{'userName': 'appliance', 'password': 'wpsthpvse1', 'roles': ['Infrastructure administrator'], 'emailAddress':'appliance@hp.com', 'officePhone':'970-898-2222', 'mobilePhone':'970-898-0022', 'type': 'UserAndRoles'},
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

fc_networks = [{'name': 'fa-san-1', 'autoLoginRedistribution': 'true', 'type': 'fc-networkV300', 'linkStabilityTime': '30', 'fabricType': 'FabricAttach', 'connectionTemplateUri': None, 'managedSanUri': 'FCSan:VSAN20'},
               {'name': 'fa-san-2', 'autoLoginRedistribution': 'true', 'type': 'fc-networkV300', 'linkStabilityTime': '30', 'fabricType': 'FabricAttach', 'connectionTemplateUri': None, 'managedSanUri': 'FCSan:VSAN21'},
               {'name': '3par-a', 'autoLoginRedistribution': 'false', 'type': 'fc-networkV300', 'linkStabilityTime': '0', 'fabricType': 'DirectAttach', 'connectionTemplateUri': None, 'managedSanUri': None},
               {'name': '3par-b', 'autoLoginRedistribution': 'true', 'type': 'fc-networkV300', 'linkStabilityTime': '0', 'fabricType': 'DirectAttach', 'connectionTemplateUri': None, 'managedSanUri': None}]

expected_fc_networks = [{'name': 'fa-san-1', 'type': 'fc-networkV300', 'fabricType': 'FabricAttach', 'linkStabilityTime': '30', 'managedSanUri': 'FCSan:VSAN20', 'autoLoginRedistribution': 'True', 'description': None, 'status': 'OK', 'state': 'Active', 'category': 'fc-networks', 'uri': 'FC:fa-san-1'},
                        {'name': 'fa-san-2', 'type': 'fc-networkV300', 'fabricType': 'FabricAttach', 'linkStabilityTime': '30', 'managedSanUri': 'FCSan:VSAN21', 'autoLoginRedistribution': 'True', 'description': None, 'status': 'OK', 'state': 'Active', 'category': 'fc-networks', 'uri': 'FC:fa-san-2'},
                        {'name': '3par-a', 'type': 'fc-networkV300', 'fabricType': 'DirectAttach', 'linkStabilityTime': '0', 'managedSanUri': None, 'autoLoginRedistribution': 'False', 'description': None, 'status': 'OK', 'state': 'Active', 'category': 'fc-networks', 'uri': 'FC:3par-a'},
                        {'name': '3par-b', 'type': 'fc-networkV300', 'fabricType': 'DirectAttach', 'linkStabilityTime': '0', 'managedSanUri': None, 'autoLoginRedistribution': 'False', 'description': None, 'status': 'OK', 'state': 'Active', 'category': 'fc-networks', 'uri': 'FC:3par-b'}]

networksets = [{'name': 'netset1', 'nativeNetworkUri': 'net10', 'type': 'network-setV300', 'networkUris': ['net10', 'net11', 'net12', 'net13']},
               {'name': 'netset2', 'nativeNetworkUri': 'net14', 'type': 'network-setV300', 'networkUris': ['net14', 'net15', 'net16', 'net17']}]

expected_networksets = [{'name': 'netset1', 'type': 'network-setV300', 'networkUris': ['ETH:net10', 'ETH:net11', 'ETH:net12', 'ETH:net13'], 'nativeNetworkUri':'ETH:net10', 'description':None, 'status':'OK', 'state':'Active', 'category':'network-sets', 'uri':'NS:netset1'},
                        {'name': 'netset2', 'type': 'network-setV300', 'networkUris': ['ETH:net14', 'ETH:net15', 'ETH:net16', 'ETH:net17'], 'nativeNetworkUri':'ETH:net14', 'description':None, 'status':'OK', 'state':'Active', 'category':'network-sets', 'uri':'NS:netset2'}]

uplink_sets = {'lig1-enet': {'name': 'lig1-enet', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['net10', 'net11', 'net12', 'net13'], 'mode': 'Auto',
                             'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q1.1', 'speed': 'Auto'},
                                                        {'enclosure': '2', 'bay': '6', 'port': 'Q1.1', 'speed': 'Auto'}]},

               'lig1-fa-san-1': {'name': 'lig1-fa-san-1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fa-san-1'],
                                 'mode': 'Auto', 'logicalPortConfigInfos': [{'bay': '3', 'port': 'Q1.2', 'speed': 'Auto'}]},

               'lig1-fa-san-2': {'name': 'lig1-fa-san-2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fa-san-2'],
                                 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None, 'logicalPortConfigInfos': [{'bay': '3', 'port': 'Q1.3', 'speed': 'Auto'}]}}

ligs = [{"name": "LIG_DCS_2", "type": "logical-interconnect-groupV300", "enclosureType": "SY12000",
         "ethernetSettings": {'enableIgmpSnooping': True, 'igmpIdleTimeoutInterval': 240, 'enableFastMacCacheFailover': False, 'macRefreshInterval': 15,
                              'enableNetworkLoopProtection': False, 'enablePauseFloodProtection': False},
         "description": None, "status": None, "state": None, "category": None, "created": None, "modified": None, "eTag": None, "uri": None,
         "uplinkSets": [uplink_sets['lig1-enet'].copy(),
                        uplink_sets['lig1-fa-san-1'].copy(),
                        uplink_sets['lig1-fa-san-2'].copy()],
         'interconnectMapTemplate': [{'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
                                     {'bay': 6, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
                                     {'bay': 3, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
                                     {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
                                     {'bay': 3, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3},
                                     {'bay': 6, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3}],
         "internalNetworkUris": [], 'interconnectBaySet': 3, 'redundancyType': 'HighlyAvailable', 'enclosureIndexes': [1, 2, 3],
         "qosConfiguration": {"activeQosConfig": {"type": "QosConfiguration", "configType": "Passthrough", "downlinkClassificationType": None, "uplinkClassificationType": None, "qosTrafficClassifiers": None, "description": None, "status": None, "name": None, "state": None, "category": "qos-aggregated-configuration", "created": None, "modified": None, "eTag": None, "uri": None}, "inactiveFCoEQosConfig": None, "inactiveNonFCoEQosConfig": None, "type": "qos-aggregated-configuration", "name": None, "state": None, "status": None, "eTag": None, "modified": None, "created": None, "category": "qos-aggregated-configuration", "uri": None}}]

expected_lig = [{"name": "LIG_DCS_2", "type": "logical-interconnect-groupV300", "enclosureType": "SY12000",
                 "qosConfiguration": {"type": "qos-aggregated-configuration",
                                      "activeQosConfig": {"type": "QosConfiguration", "configType": "Passthrough", "downlinkClassificationType": None,
                                                          "uplinkClassificationType": None, "qosTrafficClassifiers": [], "description": None,
                                                          "name": None, "state": None, "status": None, "created": None,
                                                          "eTag": None, "modified": None, "category": "qos-aggregated-configuration", "uri": None},
                                      "inactiveFCoEQosConfig": None, "inactiveNonFCoEQosConfig": None, "description": None, "name": None, "state": None,
                                      "status": None, },
                 "stackingHealth": None, "internalNetworkUris": [], "enclosureIndexes": [1, 2, 3], "redundancyType": "HighlyAvailable",
                 "interconnectBaySet": 3, "stackingMode": None, "scopeUris": [], "description": None, "state": "Active", "status": None,
                 "category": "logical-interconnect-groups", "uri": "LIG:LIG_DCS_2"}]

sas_lig = [{"name": "dd-Natasha", "type": "sas-logical-interconnect-group", "enclosureType": "SY12000",
            "description": None, "status": None, "state": None, "category": None, "created": None, "modified": None, "eTag": None, "uri": None,
            'interconnectMapTemplate': [{'bay': 1, 'enclosure': 1, 'type': 'Synergy 12Gb SAS Connection Module', 'enclosureIndex': 1},
                                     {'bay': 4, 'enclosure': 1, 'type': 'Synergy 12Gb SAS Connection Module', 'enclosureIndex': 1}],
            'interconnectBaySet': 1, 'enclosureIndexes': [1]}]

expected_sas_lig = [{"name": "dd-Natasha", "type": "sas-logical-interconnect-group", "enclosureType": "SY12000", "description": None,
                     "status": 'OK', "state": 'Active', "uri": 'SASLIG:dd-Natasha',
                     'interconnectBaySet': 1, 'enclosureIndexes': [1]}]

encgroups_add = [{'name': 'ISO-EG', 'type': 'EnclosureGroupV400',
                  'interconnectBayMappings': [{'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG_DCS_2'},
                                              {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG_DCS_2'},
                                              {'interconnectBay': 1, 'logicalInterconnectGroupUri': 'SASLIG:dd-Natasha'},
                                              {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'SASLIG:dd-Natasha'}],
                  'interconnectBayMappingCount': 2, 'stackingMode': 'Enclosure', 'configurationScript': '', 'uri': 'ISO-EG', 'powerMode': 'RedundantPowerFeed',
                  'ipAddressingMode': 'External', 'ipRangeUris': [], 'enclosureCount': 3, 'osDeploymentSettings': None, 'enclosureTypeUri': 'SY12000'}]

expected_encgroups_add = [{"type": "EnclosureGroupV400", "uri": "EG:ISO-EG", "category": "enclosure-groups", "name": "ISO-EG",
                           "status": "OK", "state": "Normal", "enclosureTypeUri": "/rest/enclosure-types/SY12000",
                           "stackingMode": "Enclosure", "portMappingCount": 8, "portMappings": [{"midplanePort": 1, "interconnectBay": 1},
                                                                                                {"midplanePort": 2, "interconnectBay": 2},
                                                                                                {"midplanePort": 3, "interconnectBay": 3},
                                                                                                {"midplanePort": 4, "interconnectBay": 4},
                                                                                                {"midplanePort": 5, "interconnectBay": 5},
                                                                                                {"midplanePort": 6, "interconnectBay": 6},
                                                                                                {"midplanePort": 7, "interconnectBay": 7},
                                                                                                {"midplanePort": 8, "interconnectBay": 8}],
                           "interconnectBayMappingCount": 4, "interconnectBayMappings": [{"interconnectBay": 3, "logicalInterconnectGroupUri": "LIG:LIG_DCS_2"},
                                                                                         {"interconnectBay": 6, "logicalInterconnectGroupUri": "LIG:LIG_DCS_2"},
                                                                                         {'interconnectBay': 1, 'logicalInterconnectGroupUri': "SASLIG:dd-Natasha"},
                                                                                         {'interconnectBay': 4, 'logicalInterconnectGroupUri': "SASLIG:dd-Natasha"}],
                           "ipAddressingMode": "External", "ipRangeUris": [], "powerMode": "RedundantPowerFeed", "description": None,
                           "associatedLogicalInterconnectGroups": ["LIG:LIG_DCS_2","SASLIG:dd-Natasha"], "enclosureCount": 3}]

logical_enclosure= [{'name': 'DCS_LE', 'enclosureUris': ['ENC:0000A66101','ENC:0000A66102','ENC:0000A66103'], 'enclosureGroupUri': 'EG:ISO-EG'}]

expected_logical_enclosure = [{'type': 'LogicalEnclosureV400', 'name': 'DCS_LE', 'status': 'OK', 'enclosureUris': ['ENC:0000A66101', 'ENC:0000A66102', 'ENC:0000A66103'], 'enclosureGroupUri': 'EG:ISO-EG'}]

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
                   {"properties": {"description": "shared volume", "isShareable": True, "name": "dd-shared", "provisioningType": "Full", "size": 5368709120, "storagePool": "FST_CPG1"}, "templateUri": "ROOT", "isPermanent": True}]

expected_storage_volumes = [{'isShareable': False, 'name': 'enc2bay1priv','state': 'Managed', 'status': 'OK', 'storagePoolUri': 'SPOOL:FST_CPG1', 'type': 'StorageVolumeV4'},
                            {'isShareable': False, 'name': 'enc2bay2priv','state': 'Managed', 'status': 'OK', 'storagePoolUri': 'SPOOL:FST_CPG1', 'type': 'StorageVolumeV4'},
                            {'isShareable': False, 'name': 'enc2bay3priv','state': 'Managed', 'status': 'OK', 'storagePoolUri': 'SPOOL:FST_CPG1', 'type': 'StorageVolumeV4'},
                            {'isShareable': False, 'name': 'enc2bay4priv','state': 'Managed', 'status': 'OK', 'storagePoolUri': 'SPOOL:FST_CPG1', 'type': 'StorageVolumeV4'},

                            {'isShareable': False, 'name': 'enc2bay7priv','state': 'Managed', 'status': 'OK', 'storagePoolUri': 'SPOOL:FST_CPG1', 'type': 'StorageVolumeV4'},
                            {'isShareable': False, 'name': 'enc2bay8priv','state': 'Managed', 'status': 'OK', 'storagePoolUri': 'SPOOL:FST_CPG1', 'type': 'StorageVolumeV4'},
                            {'isShareable': False, 'name': 'enc2bay9priv','state': 'Managed', 'status': 'OK', 'storagePoolUri': 'SPOOL:FST_CPG1', 'type': 'StorageVolumeV4'},
                            {'isShareable': False, 'name': 'enc2bay10priv','state': 'Managed', 'status': 'OK', 'storagePoolUri': 'SPOOL:FST_CPG1', 'type': 'StorageVolumeV4'},

                            {'isShareable': True, 'name': 'dd-shared','state': 'Managed', 'status': 'OK', 'storagePoolUri': 'SPOOL:FST_CPG1', 'type': 'StorageVolumeV4'}]

server_profiles = [{'type': 'ServerProfileV7', 'serverHardwareUri': 'SH:0000A66101, bay 3', 'serverHardwareTypeUri': '', 'enclosureGroupUri': '',
                    'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': '0000A66101, bay 3', 'description': '',
                    'affinity': 'Bay', 'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'}, 'boot':{'manageBoot': False},
                    'connections': [{'id': 1, 'name': 'Mezz 3:1-a', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:net10', 'functionType': 'Ethernet'},
                                    {'id': 2, 'name': 'Mezz 3:1-b', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:net11', 'functionType': 'Ethernet'},
                                    {'id': 3, 'name': 'Mezz 3:1-c', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:net12', 'functionType': 'Ethernet'}]},
                   {'type': 'ServerProfileV7', 'serverHardwareUri': 'SH:0000A66101, bay 4', 'serverHardwareTypeUri': '', 'enclosureGroupUri': '',
                    'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': '0000A66101, bay 4', 'description': '', 'affinity': 'Bay',
                    'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'}, 'boot':{'manageBoot': False},
                    'connections': [{'id': 1, 'name': 'Mezz 3:1-a', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:net10', 'functionType': 'Ethernet'},
                                    {'id': 2, 'name': 'Mezz 3:1-b', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:net11', 'functionType': 'Ethernet'},
                                    {'id': 3, 'name': 'Mezz 3:1-c', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:net12', 'functionType': 'Ethernet'},
                                    {'id': 4, 'name': 'Mezz 3:1-d', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'ETH:net13', 'functionType': 'Ethernet'}]}]

expected_server_profiles = [{'type': 'ServerProfileV7', 'serverHardwareUri': 'SH:0000A66101, bay 3',
                             'serverHardwareTypeUri': 'SHT:SY 660 Gen9:1:Smart Array P542D Controller:2:HPE Synergy 3530C 16G Host Bus Adapter:3:HPE Synergy 3820C 10/20Gb Converged Network Adapter',
                             'enclosureGroupUri': 'EG:ISO-EG', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                             'name': '0000A66101, bay 3', 'description': '', 'affinity': 'Bay', 'status':'OK','state':'Normal',
                             'connections': [{'id': 1, 'name': 'Mezz 3:1-a', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:net10', 'functionType': 'Ethernet'},
                                             {'id': 2, 'name': 'Mezz 3:1-b', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:net11', 'functionType': 'Ethernet'},
                                             {'id': 3, 'name': 'Mezz 3:1-c', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:net12', 'functionType': 'Ethernet'}]},
                            {'type': 'ServerProfileV7', 'serverHardwareUri': 'SH:0000A66101, bay 4',
                             'serverHardwareTypeUri': 'SHT:SY 660 Gen9:2:HPE Synergy 3830C 16G Fibre Channel Host Bus Adapter:3:HPE Synergy 3820C 10/20Gb Converged Network Adapter',
                             'enclosureGroupUri': 'EG:ISO-EG', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                             'name': '0000A66101, bay 4', 'description': '', 'affinity': 'Bay', 'status':'OK','state':'Normal',
                             'connections': [{'id': 1, 'name': 'Mezz 3:1-a', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:net10', 'functionType': 'Ethernet'},
                                             {'id': 2, 'name': 'Mezz 3:1-b', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:net11', 'functionType': 'Ethernet'},
                                             {'id': 3, 'name': 'Mezz 3:1-c', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:net12', 'functionType': 'Ethernet'},
                                             {'id': 4, 'name': 'Mezz 3:1-d', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'ETH:net13', 'functionType': 'Ethernet'}]}]

server_profile_with_storage = [{'name': 'Encl1bay5', 'type': 'ServerProfileV7', 'serverHardwareUri': 'SH:0000A66101, bay 5', 'serverHardwareTypeUri': '', 'enclosureGroupUri': '', 'serialNumberType': 'Virtual', 'iscsiInitiatorNameType': 'AutoGenerated', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:net10', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                {'id': 2, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b', 'requestedMbps': '4000', 'networkUri': 'FC:fa-san-1', 'mac': None, 'wwpn': '', 'wwnn': '',
                                                 'boot':{'priority':'Primary', 'bootVolumeSource':'UserDefined', 'targets':[{'arrayWwpn':'20000002AC0008DE', 'lun':'1'}]}}],
                                "boot": {"manageBoot": True,"order": ["HardDisk"]}, "bootMode": {"pxeBootPolicy": None,"manageMode": True,"mode": "BIOS"},
                                'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                'bios': {'manageBios': False, 'overriddenSettings': []}, 'hideUnusedFlexNics':True, 'iscsiInitiatorName':'', 'osDeploymentSettings':None,
                                'localStorage':{'sasLogicalJBODs': [], 'controllers':[]},
                                'sanStorage':{'hostOSType': 'RHE Linux (5.x, 6.x)', 'manageSanStorage': True,
                                              'volumeAttachments': [{'id': 1, 'volumeUri': 'SVOL:enc2bay7priv', 'isBootVolume': False, 'lunType': 'Manual', 'lun': 1,
                                                                     'storagePaths': [{'isEnabled': True, 'connectionId': 2, 'targetSelector': 'Auto', 'targets': []}]},]}}]

expected_server_profile_with_storage = [{"name": "Encl1bay5","type": "ServerProfileV7","uri": "SP:Encl1bay5","description": "",
                                         "serverProfileTemplateUri": None,"templateCompliance": "Unknown",
                                         "serverHardwareUri": "SH:0000A66101, bay 5","serverHardwareTypeUri": "SHT:SY 480 Gen9:1:Smart Array P542D Controller:3:HPE Synergy 3820C 10/20Gb Converged Network Adapter","enclosureGroupUri": "EG:ISO-EG",
                                         "enclosureUri": "ENC:0000A66101","enclosureBay": 5,"affinity": "Bay","associatedServer": None,
                                         "hideUnusedFlexNics": True,"firmware": {"firmwareInstallType": None,"forceInstallFirmware": False,"firmwareBaselineUri": None,"manageFirmware": False},
                                         "macType": "Virtual","wwnType": "Virtual","serialNumberType": "Virtual","category": "server-profiles",
                                         "status": "OK","state": "Normal","inProgress": False,
                                         "connections": [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:net10', 'boot': {'priority': 'NotBootable'} },
                                                         {"id": 2, 'name': '', "functionType": "FibreChannel", "networkUri": "FC:fa-san-1",
                                                          "portId": "Mezz 3:1-b","requestedVFs": None,"allocatedVFs": None,"macType": "Virtual",
                                                          "wwpnType": "Virtual","requestedMbps": "4000","allocatedMbps": 4000,"maximumMbps": 10000,"boot": {"priority": "Primary","targets": [{"arrayWwpn": "20000002AC0008DE","lun": "1"}],}}],
                                         "bootMode": {"pxeBootPolicy": None,"manageMode": True,"mode": "BIOS"}, "boot": {"manageBoot": True,"order": ["HardDisk","CD","USB","PXE"]},
                                         "bios": {"overriddenSettings": [],"manageBios": False}, "localStorage": {"sasLogicalJBODs": [],"controllers": []},
                                         "sanStorage": {"volumeAttachments": [{"storagePaths": [{"targetSelector": "Auto","targets": [{'name':"20:00:00:02:AC:00:08:E2"},{'name':"20:00:00:02:AC:00:08:DE"}],"connectionId": 2,"isEnabled": True,"status": "OK"}],"isBootVolume": False,"state": "Attached","lun": "1",
                                                                               "volumeStoragePoolUri": "SPOOL:FST_CPG1","volumeStorageSystemUri": "SYS:ThreePAR-1","lunType": "Manual","volumeUri": "SVOL:enc2bay7priv","status": "OK","id": 1},],
                                                        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)","manageSanStorage": True},"osDeploymentSettings": None,},]

server_profile_templates = [{'name': 'SPT-ENCL1-BAY3', 'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:SY 660 Gen9:1:Smart Array P542D Controller:2:HPE Synergy 3530C 16G Host Bus Adapter:3:HPE Synergy 3820C 10/20Gb Converged Network Adapter', 'enclosureGroupUri': 'EG:ISO-EG', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             "connectionSettings": { "manageConnections": True,
                                                    'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:net10', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:net11', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'FC:fa-san-1', 'boot': {'priority': 'NotBootable'}}],},
                             'boot': {'manageBoot': True, 'order': ['HardDisk']}, 'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []}, 'hideUnusedFlexNics':True, 'iscsiInitiatorNameType':'AutoGenerated',
                             'localStorage':{'sasLogicalJBODs': [], 'controllers':[]}, 'sanStorage':None}]

expected_server_profile_templates = [{'type': 'ServerProfileTemplateV3', 'uri': 'SPT:SPT-ENCL1-BAY3', 'name': 'SPT-ENCL1-BAY3', 'description': '', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:SY 660 Gen9:1:Smart Array P542D Controller:2:HPE Synergy 3530C 16G Host Bus Adapter:3:HPE Synergy 3820C 10/20Gb Converged Network Adapter', 'enclosureGroupUri': 'EG:ISO-EG', 'affinity': 'Bay', 'hideUnusedFlexNics': True, 'macType': 'Virtual', 'wwnType': 'Virtual', 'serialNumberType': 'Virtual', 'iscsiInitiatorNameType': 'AutoGenerated',
                                      'firmware': {'manageFirmware': False, 'forceInstallFirmware': False},
                                      "connectionSettings": { "manageConnections": True,
                                                             'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:net10', 'boot': {'priority': 'NotBootable'}},
                                                                             {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:net11', 'boot': {'priority': 'NotBootable'}},
                                                                             {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'FC:fa-san-1', 'boot': {'priority': 'NotBootable'}}],},
                                      'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                      'boot': {'manageBoot': True,
                                               'order': ['HardDisk']}, 'bios':{'manageBios': False, 'overriddenSettings': []},
                                      'localStorage':{'sasLogicalJBODs': [], 'controllers':[]},
                                      'sanStorage':{'manageSanStorage': False, 'volumeAttachments': []},
                                      'category':'server-profile-templates', 'status':'OK', 'state':None}]

server_profiles_from_spt = [{'name': 'Encl1bay3', 'type': 'ServerProfileV7', 'serverHardwareUri': '0000A66102, bay 3', 'serverHardwareTypeUri': 'SHT:SY 660 Gen9:1:Smart Array P542D Controller:2:HPE Synergy 3530C 16G Host Bus Adapter:3:HPE Synergy 3820C 10/20Gb Converged Network Adapter', 'enclosureGroupUri': 'EG:ISO-EG', 'serialNumberType': 'Virtual', 'iscsiInitiatorNameType': 'AutoGenerated', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:net10', 'boot': {'priority': 'NotBootable'}},
                                             {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:net11', 'boot': {'priority': 'NotBootable'}},
                                             {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'FC:fa-san-1', 'boot': {'priority': 'NotBootable'}}],
                             'boot': {'manageBoot': True, 'order': ['HardDisk']}, 'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []}, 'hideUnusedFlexNics':True, 'iscsiInitiatorName':'',
                             'serverProfileTemplateUri':'SPT:SPT-ENCL1-BAY3', 'osDeploymentSettings':None,
                             'localStorage':{'sasLogicalJBODs': [], 'controllers':[]}, 'sanStorage':None}]

expected_server_profiles_from_spt = [{'name': 'Encl1bay3', 'type': 'ServerProfileV7', 'serverHardwareUri': 'SH:0000A66102, bay 3', 'serverHardwareTypeUri': 'SHT:SY 660 Gen9:1:Smart Array P542D Controller:2:HPE Synergy 3530C 16G Host Bus Adapter:3:HPE Synergy 3820C 10/20Gb Converged Network Adapter', 'enclosureGroupUri': 'EG:ISO-EG', 'serialNumberType': 'Virtual', 'iscsiInitiatorNameType': 'AutoGenerated', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:net10', 'boot': {'priority': 'NotBootable'}},
                                             {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:net11', 'boot': {'priority': 'NotBootable'}},
                                             {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'FC:fa-san-1', 'boot': {'priority': 'NotBootable'}}],
                             'boot': {'manageBoot': True, 'order': ['HardDisk']}, 'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                             'firmware': {'manageFirmware': False, 'forceInstallFirmware': False},
                             'bios': {'manageBios': False, 'overriddenSettings': []}, 'hideUnusedFlexNics':True,
                             'serverProfileTemplateUri':'SPT:SPT-ENCL1-BAY3', 'osDeploymentSettings':None,
                             'localStorage':{'sasLogicalJBODs': [], 'controllers':[]}, 'sanStorage':{'manageSanStorage': False, 'volumeAttachments': [], 'sanSystemCredentials': []}}]

configured_enclosures = [{'name': '0000A66101', 'type': 'EnclosureV400', 'enclosureType': 'SY12000', 'serialNumber': '0000A66101',
                         'refreshState': 'NotRefreshing', 'state': 'Configured',
                         'deviceBays': [{'bayNumber': 1, 'devicePresence': 'Present'}, {'bayNumber': 2, 'devicePresence': 'Subsumed'}, {'bayNumber': 3, 'devicePresence': 'Present'},
                                        {'bayNumber': 4, 'devicePresence': 'Present'}, {'bayNumber': 5, 'devicePresence': 'Present'}, {'bayNumber': 6, 'devicePresence': 'Present'},
                                        {'bayNumber': 7, 'devicePresence': 'Present'}, {'bayNumber': 8, 'devicePresence': 'Present'}, {'bayNumber': 9, 'devicePresence': 'Subsumed'}, {'bayNumber': 10, 'devicePresence': 'Subsumed'}, {'bayNumber': 11, 'devicePresence': 'Present'}, {'bayNumber': 12, 'devicePresence': 'Present'}],
                         'interconnectBays': [{'bayNumber': 1, 'bayPowerState': 'Unknown'}, {'bayNumber': 2, 'bayPowerState': 'Unknown'},
                                              {'bayNumber': 3, 'bayPowerState': 'Unknown'}, {'bayNumber': 4, 'bayPowerState': 'Unknown'},
                                              {'bayNumber': 5, 'bayPowerState': 'Unknown'}, {'bayNumber': 6, 'bayPowerState': 'Unknown'}],
                         'fanBays': [{'bayNumber': 1, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 2, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 3, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 4, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 5, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 6, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 7, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 8, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 9, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 10, 'status': 'OK', 'devicePresence': 'Present'}],
                         'powerSupplyBays': [{'bayNumber': 1, 'status': 'OK', 'devicePresence': 'Present'},
                                             {'bayNumber': 2, 'status': 'OK', 'devicePresence': 'Present'},
                                             {'bayNumber': 3, 'status': 'OK', 'devicePresence': 'Present'},
                                             {'bayNumber': 4, 'status': 'OK', 'devicePresence': 'Present'},
                                             {'bayNumber': 5, 'status': 'OK', 'devicePresence': 'Present'},
                                             {'bayNumber': 6, 'status': 'OK', 'devicePresence': 'Present'}],
                         'applianceBays': [{'bayNumber': 1, 'status': 'OK', 'devicePresence': 'Present'},
                                           {'bayNumber': 2, 'status': None, 'devicePresence': 'Absent'}],
                         'managerBays': [{'bayNumber': 1, 'status': 'OK', 'devicePresence': 'Present', 'mgmtPortStatus': 'OK'},
                                         {'bayNumber': 2, 'status': 'OK', 'devicePresence': 'Present', 'mgmtPortStatus': 'OK'}]},
                        {'name': '0000A66102', 'type': 'EnclosureV400', 'enclosureType': 'SY12000', 'serialNumber': '0000A66102',
                         'refreshState': 'NotRefreshing', 'state': 'Configured',
                         'deviceBays': [{'bayNumber': 1, 'devicePresence': 'Present'}, {'bayNumber': 2, 'devicePresence': 'Subsumed'}, {'bayNumber': 3, 'devicePresence': 'Present'},
                                        {'bayNumber': 4, 'devicePresence': 'Present'}, {'bayNumber': 5, 'devicePresence': 'Present'}, {'bayNumber': 6, 'devicePresence': 'Present'},
                                        {'bayNumber': 7, 'devicePresence': 'Present'}, {'bayNumber': 8, 'devicePresence': 'Present'}, {'bayNumber': 9, 'devicePresence': 'Subsumed'}, {'bayNumber': 10, 'devicePresence': 'Subsumed'}, {'bayNumber': 11, 'devicePresence': 'Present'}, {'bayNumber': 12, 'devicePresence': 'Present'}],
                         'interconnectBays': [{'bayNumber': 1, 'bayPowerState': 'Unknown'}, {'bayNumber': 2, 'bayPowerState': 'Unknown'},
                                              {'bayNumber': 3, 'bayPowerState': 'Unknown'}, {'bayNumber': 4, 'bayPowerState': 'Unknown'},
                                              {'bayNumber': 5, 'bayPowerState': 'Unknown'}, {'bayNumber': 6, 'bayPowerState': 'Unknown'}],
                         'fanBays': [{'bayNumber': 1, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 2, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 3, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 4, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 5, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 6, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 7, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 8, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 9, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 10, 'status': 'OK', 'devicePresence': 'Present'}],
                         'powerSupplyBays': [{'bayNumber': 1, 'status': 'OK', 'devicePresence': 'Present'},
                                             {'bayNumber': 2, 'status': 'OK', 'devicePresence': 'Present'},
                                             {'bayNumber': 3, 'status': 'OK', 'devicePresence': 'Present'},
                                             {'bayNumber': 4, 'status': 'OK', 'devicePresence': 'Present'},
                                             {'bayNumber': 5, 'status': 'OK', 'devicePresence': 'Present'},
                                             {'bayNumber': 6, 'status': 'OK', 'devicePresence': 'Present'}],
                         'applianceBays': [{'bayNumber': 1, 'status': 'OK', 'devicePresence': 'Present'},
                                           {'bayNumber': 2, 'status': 'OK', 'devicePresence': 'Present'}],
                         'managerBays': [{'bayNumber': 1, 'status': 'OK', 'devicePresence': 'Present', 'mgmtPortStatus': None},
                                         {'bayNumber': 2, 'status': 'OK', 'devicePresence': 'Present', 'mgmtPortStatus': None}]},
                        {'name': '0000A66103', 'type': 'EnclosureV400', 'enclosureType': 'SY12000', 'serialNumber': '0000A66103',
                         'refreshState': 'NotRefreshing', 'state': 'Configured',
                         'deviceBays': [{'bayNumber': 1, 'devicePresence': 'Present'}, {'bayNumber': 2, 'devicePresence': 'Subsumed'}, {'bayNumber': 3, 'devicePresence': 'Present'},
                                        {'bayNumber': 4, 'devicePresence': 'Present'}, {'bayNumber': 5, 'devicePresence': 'Present'}, {'bayNumber': 6, 'devicePresence': 'Present'},
                                        {'bayNumber': 7, 'devicePresence': 'Present'}, {'bayNumber': 8, 'devicePresence': 'Present'}, {'bayNumber': 9, 'devicePresence': 'Subsumed'}, {'bayNumber': 10, 'devicePresence': 'Subsumed'}, {'bayNumber': 11, 'devicePresence': 'Present'}, {'bayNumber': 12, 'devicePresence': 'Present'}],
                         'interconnectBays': [{'bayNumber': 1, 'bayPowerState': 'Unknown'}, {'bayNumber': 2, 'bayPowerState': 'Unknown'},
                                              {'bayNumber': 3, 'bayPowerState': 'Unknown'}, {'bayNumber': 4, 'bayPowerState': 'Unknown'},
                                              {'bayNumber': 5, 'bayPowerState': 'Unknown'}, {'bayNumber': 6, 'bayPowerState': 'Unknown'}],
                         'fanBays': [{'bayNumber': 1, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 2, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 3, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 4, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 5, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 6, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 7, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 8, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 9, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 10, 'status': 'OK', 'devicePresence': 'Present'}],
                         'powerSupplyBays': [{'bayNumber': 1, 'status': 'OK', 'devicePresence': 'Present'},
                                             {'bayNumber': 2, 'status': 'OK', 'devicePresence': 'Present'},
                                             {'bayNumber': 3, 'status': 'OK', 'devicePresence': 'Present'},
                                             {'bayNumber': 4, 'status': 'OK', 'devicePresence': 'Present'},
                                             {'bayNumber': 5, 'status': 'OK', 'devicePresence': 'Present'},
                                             {'bayNumber': 6, 'status': 'OK', 'devicePresence': 'Present'}],
                         'applianceBays': [{'bayNumber': 1, 'status': None, 'devicePresence': 'Absent'},
                                           {'bayNumber': 2, 'status': 'OK', 'devicePresence': 'Present'}],
                         'managerBays': [{'bayNumber': 1, 'status': 'OK', 'devicePresence': 'Present', 'mgmtPortStatus': None},
                                         {'bayNumber': 2, 'status': 'OK', 'devicePresence': 'Present', 'mgmtPortStatus': None}]}]

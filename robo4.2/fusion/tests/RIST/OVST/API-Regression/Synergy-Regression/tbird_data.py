from DynamicData import DynamicData

DD = DynamicData()

ONEVIEW_SSH_USERNAME = 'root'  # SSH Username
ONEVIEW_SSH_PASSWORD = 'hponeview'  # SSH Password

appliance = {'type': 'ApplianceNetworkConfigurationV2',
             'applianceNetworks': [{
                 'macAddress': None,
                 'ipv4NameServers': ['10.93.0.11'],
                 'virtIpv4Addr': '10.93.1.15',
                 'interfaceName': 'Appliance',
                 'overrideIpv4DhcpDnsServers': False,
                 'activeNode': '1',
                 'confOneNode': True,
                 'ipv4Type': 'STATIC',
                 'ipv4Subnet': '255.255.0.0',
                 'device': 'eth0',
                 'ipv6Type': 'UNCONFIGURE',
                 'unconfigure': False,
                 'aliasDisabled': False,
                 'ipv4Gateway': '10.93.0.1',
                 'hostname': 'cypress.dom1093.net',
                 'searchDomains': None,
                 'domainName': '',
             }]}

'''
This is the time and locale settings used during FTS.
'''
timeandlocale = {'type': 'TimeAndLocale', 'dateTime': None, 'timezone': 'UTC', 'ntpServers': ['ntp.hp.net'], 'locale': 'en_US.UTF-8'}

admin_credentials = {'userName': 'Administrator', 'password': 'Cosmos123'}

licenses = [{'key': 'ACLA C9MA H9P9 CHUZ V7B5 HWWB Y9JL KMPL 5R2H 6DRM DXAU 2CSM GHTG L762 BCV6 EEFY KJVT D5KM EFVW DT5J 69UM NY2G 9K2P 3E22 MKQU 3UFZ TZZX AB6X 82Z5 WHEF D9ED 3RUX BJS2 XFXC T84U R42A 58S5 XA2D WXAP GMTQ 4YLB MM2S CZU7 2E4X E8EW BGB5 BWPD CAAR YT9J 4NUG 2NJN J9UF "424863919 HPOV-NFR1 HP_OneView_16_Seat_NFR H592ADTYDJJD"_3PXQT-HWSHJ-7RBW9-ZW3WG-XC2W2'},
            {'key': 'YCLE B9MA H9PY GHU3 U7B5 HWW5 Y9JL KMPL NRSF 4ERM DXAU 2CSM GHTG L762 DK5Y HHF9 KJVT D5KM EFVW DT5J 89MK PZ2G 9K2P 3E22 MKYU 3UFZ TZZ7 9B5X 82Z5 WHEF D9ED 3RUX BJS2 XFXC T84U R42A 58S5 XA2D WXAP GMTQ 4YLB MM2S CZU7 2E4X E8EW BGB5 BWPD CAAR 2T9J MNEG 2NJN J9UF "424863952 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR YHUAADTYEC5H"'},
            {'key': 'QCLA A9MA H9PA KHW3 V7B5 HWWB Y9JL KMPL BRKD 8FBM DXAU 2CSM GHTG L762 XKJ3 VBF4 KJVT D5KM EFRW DS5R A9E9 52KG 9K2P 3E22 UKYU 3UFZ TZZ7 MB5X 82Z5 WHEF D9ED 3RUX BJS2 XFXC T84U R42A 58S5 XA2D WXAP GMTQ 4YLB MM2S CZU7 2E4X E8EW BGB5 BWPD CAAR YT9J 4NUG 2NJN J9UF "424863966 HPOV-NFR1 HP_OneView_16_Seat_NFR 7EA7ADTYED49"_3Q7Z5-2HDVR-CC6R8-6BJQM-9S84B'},
            {'key': 'YCLC C9MA H9P9 8HW3 U7B5 HWW5 Y9JL KMPL LRGB 7ABQ DXAU 2CSM GHTG L762 QGFZ EEZM KJVT D5KM EFRW DS5R M94M N5KG 9K2P 3E22 AKYU LUV5 TZZX 9B5X 82Z5 WHEF D9ED 3RUX BJS2 XFXC T84U R42A 58S5 XA2D WXAP GMTQ 4YLB MM2S CZU7 2E4X E8EW BGB5 BWPD CAAR 2T9J MNEG 2NJN J9UF "424864041 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR HY95ADTYTCHT"'},
            {'key': '9B2G D9MA H9PA CHVZ V2B4 HWWV Y9JL KMPL B89H MZVU 6RMS 9HWE 92R6 3FZ3 CMRG HPMR MFVU A5K9 MHGK EKX9 HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'},
            {'key': 'YBKA D9MA H9P9 8HX3 V2B4 HWWV Y9JL KMPL B89H MZVU GR4S JHWE J2SP XNZ8 CMRG HPMR UFVU A5K9 MWHC 9K4K HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'}]

users = [{'userName': 'appliance', 'password': 'wpsthpvse1', 'permissions': [{'roleName': 'Infrastructure administrator', 'scopeUri': None}], 'emailAddress': 'appliance@hp.com', 'officePhone': '970-898-2222', 'mobilePhone': '970-898-0022', 'type': 'UserAndPermissions'},
         {'userName': 'backup', 'password': 'backupadmin', 'permissions': [{'roleName': 'Backup administrator', 'scopeUri': None}], 'emailAddress': 'backup@hp.com', 'officePhone': '970-666-1919', 'mobilePhone': '970-600-1919', 'type': 'UserAndPermissions'},
         {'userName': 'network', 'password': 'networkadmin', 'permissions': [{'roleName': 'Network administrator', 'scopeUri': None}], 'emailAddress': 'network@hp.com', 'officePhone': '970-555-0001', 'mobilePhone': '970-500-0001', 'type': 'UserAndPermissions'},
         {'userName': 'readonly', 'password': 'readonly', 'permissions': [{'roleName': 'Read only', 'scopeUri': None}], 'emailAddress': 'readonly@hp.com', 'officePhone': '970-666-1919', 'mobilePhone': '970-600-1919', 'type': 'UserAndPermissions'},
         {'userName': 'server', 'password': 'serveradmin', 'permissions': [{'roleName': 'Server administrator', 'scopeUri': None}], 'emailAddress': 'server@hp.com', 'officePhone': '970-555-0001', 'mobilePhone': '970-500-0001', 'type': 'UserAndPermissions'},
         {'userName': 'storage', 'password': 'storageadmin', 'permissions': [{'roleName': 'Storage administrator', 'scopeUri': None}], 'emailAddress': 'storage@hp.com', 'officePhone': '970-555-0001', 'mobilePhone': '970-500-0001', 'type': 'UserAndPermissions'},
         {'userName': 'oneview', 'password': 'oneviewadmin', 'permissions': [{'roleName': 'Infrastructure administrator', 'scopeUri': None}], 'emailAddress': 'oneview@hp.com', 'officePhone': '970-555-0001', 'mobilePhone': '970-500-0001', 'type': 'UserAndPermissions'},
         {'userName': 'networkserver', 'password': 'networkserveradmin', 'permissions': [{'roleName': 'Network administrator', 'scopeUri': None}, {'roleName': 'Server administrator', 'scopeUri': None}], 'emailAddress': 'networkserver@hp.com', 'officePhone': '970-555-0001', 'mobilePhone': '970-500-0001', 'type': 'UserAndPermissions'},
         {'userName': 'backupstorage', 'password': 'backupstorageadmin', 'permissions': [{'roleName': 'Backup administrator', 'scopeUri': None}, {'roleName': 'Storage administrator', 'scopeUri': None}], 'emailAddress': 'backupstorage@hp.com', 'officePhone': '970-555-0001', 'mobilePhone': '970-500-0001', 'type': 'UserAndPermissions'},
         {'userName': 'networkserverstorage', 'password': 'wpsthpvse1', 'permissions': [{'roleName': 'Network administrator', 'scopeUri': None}, {'roleName': 'Server administrator', 'scopeUri': None}, {'roleName': 'Storage administrator', 'scopeUri': None}], 'emailAddress': 'networkserverstorage@hp.com', 'officePhone': '970-555-0001', 'mobilePhone': '970-500-0001', 'type': 'UserAndPermissions'}]

expected_users = [{'type': 'UserAndPermissions', 'permissions': [{'roleName': 'Infrastructure administrator', 'scopeUri': None}], 'userName': 'administrator', 'fullName': 'Default appliance administrator', 'emailAddress': '', 'officePhone': '', 'mobilePhone': '', 'enabled': True, 'uri': '/rest/users/administrator', 'name': None, 'category': 'users'},
                  {'type': 'UserAndPermissions', 'permissions': [{'roleName': 'Infrastructure administrator', 'scopeUri': None}], 'userName': 'appliance', 'fullName': '', 'emailAddress': 'appliance@hp.com', 'officePhone': '970-898-2222', 'mobilePhone': '970-898-0022', 'enabled': True, 'uri': '/rest/users/appliance', 'name': None, 'category': 'users'},
                  {'type': 'UserAndPermissions', 'permissions': [{'roleName': 'Backup administrator', 'scopeUri': None}], 'userName': 'backup', 'fullName': '', 'emailAddress': 'backup@hp.com', 'officePhone': '970-666-1919', 'mobilePhone': '970-600-1919', 'enabled': True, 'uri': '/rest/users/backup', 'name': None, 'category': 'users'},
                  {'type': 'UserAndPermissions', 'permissions': [{'roleName': 'Network administrator', 'scopeUri': None}], 'userName': 'network', 'fullName': '', 'emailAddress': 'network@hp.com', 'officePhone': '970-555-0001', 'mobilePhone': '970-500-0001', 'enabled': True, 'uri': '/rest/users/network', 'name': None, 'category': 'users'},
                  {'type': 'UserAndPermissions', 'permissions': [{'roleName': 'Read only', 'scopeUri': None}], 'userName': 'readonly', 'fullName': '', 'emailAddress': 'readonly@hp.com', 'officePhone': '970-666-1919', 'mobilePhone': '970-600-1919', 'enabled': True, 'uri': '/rest/users/readonly', 'name': None, 'category': 'users'},
                  {'type': 'UserAndPermissions', 'permissions': [{'roleName': 'Server administrator', 'scopeUri': None}], 'userName': 'server', 'fullName': '', 'emailAddress': 'server@hp.com', 'officePhone': '970-555-0001', 'mobilePhone': '970-500-0001', 'enabled': True, 'uri': '/rest/users/server', 'name': None, 'category': 'users'},
                  {'type': 'UserAndPermissions', 'permissions': [{'roleName': 'Storage administrator', 'scopeUri': None}], 'userName': 'storage', 'fullName': '', 'emailAddress': 'storage@hp.com', 'officePhone': '970-555-0001', 'mobilePhone': '970-500-0001', 'enabled': True, 'uri': '/rest/users/storage', 'name': None, 'category': 'users'},
                  {'type': 'UserAndPermissions', 'permissions': [{'roleName': 'Infrastructure administrator', 'scopeUri': None}], 'userName': 'oneview', 'fullName': '', 'emailAddress': 'oneview@hp.com', 'officePhone': '970-555-0001', 'mobilePhone': '970-500-0001', 'enabled': True, 'uri': '/rest/users/oneview', 'name': None, 'category': 'users'},
                  {'type': 'UserAndPermissions', 'permissions': [{'roleName': 'Network administrator', 'scopeUri': None}, {'roleName': 'Server administrator', 'scopeUri': None}], 'userName': 'networkserver', 'fullName': '', 'emailAddress': 'networkserver@hp.com', 'officePhone': '970-555-0001', 'mobilePhone': '970-500-0001', 'enabled': True, 'uri': '/rest/users/networkserver', 'name': None, 'category': 'users'},
                  {'type': 'UserAndPermissions', 'permissions': [{'roleName': 'Backup administrator', 'scopeUri': None}, {'roleName': 'Storage administrator', 'scopeUri': None}], 'userName': 'backupstorage', 'fullName': '', 'emailAddress': 'backupstorage@hp.com', 'officePhone': '970-555-0001', 'mobilePhone': '970-500-0001', 'enabled': True, 'uri': '/rest/users/backupstorage', 'name': None, 'category': 'users'},
                  {'type': 'UserAndPermissions', 'permissions': [{'roleName': 'Network administrator', 'scopeUri': None}, {'roleName': 'Server administrator', 'scopeUri': None}, {'roleName': 'Storage administrator', 'scopeUri': None}], 'userName': 'networkserverstorage', 'fullName': '', 'emailAddress': 'networkserverstorage@hp.com', 'officePhone': '970-555-0001', 'mobilePhone': '970-500-0001', 'enabled': True, 'uri': '/rest/users/networkserverstorage', 'name': None, 'category': 'users'}]

san_managers = [{'connectionInfo': [{'name': 'Type', 'value': 'HPE'},
                                    {'name': 'Host', 'value': '10.0.1.58'},
                                    {'name': 'SnmpPort', 'value': 161},
                                    {'name': 'SnmpUserName', 'value': 'defaultUser'},
                                    {'name': 'SnmpAuthString', 'value': 'authPass123'},
                                    {'name': 'SnmpAuthLevel', 'value': 'authpriv'},
                                    {'name': 'SnmpAuthProtocol', 'value': 'MD5'},
                                    {'name': 'SnmpPrivProtocol', 'value': 'aes'},
                                    {'name': 'SnmpPrivString', 'value': 'privPass123'}]}]

expected_san_managers = [{'uri': 'SAN:10.0.1.58', 'name': '10.0.1.58', 'type': 'FCDeviceManagerV2',
                          'state': 'Managed', 'status': 'OK', 'category': 'fc-device-managers',
                          'connectionInfo': [{'name': 'Host', 'displayName': 'Host', 'required': False, 'value': '10.0.1.58', 'valueFormat': 'IPAddressOrHostname', 'valueType': 'String'},
                                             {'name': 'SnmpPort', 'displayName': 'SnmpPort', 'required': False, 'value': 161, 'valueFormat': 'None', 'valueType': 'Integer'},
                                             {'name': 'SnmpUserName', 'displayName': 'SnmpUserName', 'required': False, 'value': 'defaultUser', 'valueFormat': 'None', 'valueType': 'String'},
                                             {'name': 'SnmpAuthLevel', 'displayName': 'SnmpAuthLevel', 'required': False, 'value': 'authpriv', 'valueFormat': 'None', 'valueType': 'String'},
                                             {'name': 'SnmpAuthProtocol', 'displayName': 'SnmpAuthProtocol', 'required': False, 'value': 'MD5', 'valueFormat': 'None', 'valueType': 'String'},
                                             {'name': 'SnmpAuthString', 'displayName': 'SnmpAuthString', 'required': False, 'value': '', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'},
                                             {'name': 'SnmpPrivProtocol', 'displayName': 'SnmpPrivProtocol', 'required': False, 'value': 'aes', 'valueFormat': 'None', 'valueType': 'String'},
                                             {'name': 'SnmpPrivString', 'displayName': 'SnmpPrivString', 'required': False, 'value': '', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, ],
                          'description': 'HP FF 5930-4Slot Switch',
                          'deviceManagerVersion': '7.1.045 Release 2418P01',
                          'isInternal': False,
                          'providerDisplayName': 'HPE',
                          'refreshState': 'Stable'}
                         ]

ethernet_networks = [{'name': 'net10', 'vlanId': '1070', 'purpose': 'General', 'smartLink': 'false', 'privateNetwork': 'false', 'ethernetNetworkType': 'Tagged', 'type': 'ethernet-networkV4', 'connectionTemplateUri': None},
                     {'name': 'net11', 'vlanId': '1071', 'purpose': 'Management', 'smartLink': 'false', 'privateNetwork': 'false', 'ethernetNetworkType': 'Tagged', 'type': 'ethernet-networkV4', 'connectionTemplateUri': None},
                     {'name': 'net12', 'vlanId': '1072', 'purpose': 'Management', 'smartLink': 'false', 'privateNetwork': 'false', 'ethernetNetworkType': 'Tagged', 'type': 'ethernet-networkV4', 'connectionTemplateUri': None},
                     {'name': 'net13', 'vlanId': '1073', 'purpose': 'Management', 'smartLink': 'false', 'privateNetwork': 'false', 'ethernetNetworkType': 'Tagged', 'type': 'ethernet-networkV4', 'connectionTemplateUri': None},
                     {'name': 'net14', 'vlanId': '1074', 'purpose': 'Management', 'smartLink': 'false', 'privateNetwork': 'false', 'ethernetNetworkType': 'Tagged', 'type': 'ethernet-networkV4', 'connectionTemplateUri': None},
                     {'name': 'net15', 'vlanId': '1075', 'purpose': 'General', 'smartLink': 'false', 'privateNetwork': 'false', 'ethernetNetworkType': 'Tagged', 'type': 'ethernet-networkV4', 'connectionTemplateUri': None},
                     {'name': 'net16', 'vlanId': '1076', 'purpose': 'General', 'smartLink': 'false', 'privateNetwork': 'false', 'ethernetNetworkType': 'Tagged', 'type': 'ethernet-networkV4', 'connectionTemplateUri': None},
                     {'name': 'net17', 'vlanId': '1077', 'purpose': 'VMMigration', 'smartLink': 'false', 'privateNetwork': 'false', 'ethernetNetworkType': 'Tagged', 'type': 'ethernet-networkV4', 'connectionTemplateUri': None},
                     {'name': 'net18', 'vlanId': '1078', 'purpose': 'General', 'smartLink': 'false', 'privateNetwork': 'false', 'ethernetNetworkType': 'Tagged', 'type': 'ethernet-networkV4', 'connectionTemplateUri': None},
                     {'name': 'net19', 'vlanId': '1079', 'purpose': 'General', 'smartLink': 'false', 'privateNetwork': 'false', 'ethernetNetworkType': 'Tagged', 'type': 'ethernet-networkV4', 'connectionTemplateUri': None},
                     {'name': 'net20', 'vlanId': '1080', 'purpose': 'General', 'smartLink': 'false', 'privateNetwork': 'false', 'ethernetNetworkType': 'Tagged', 'type': 'ethernet-networkV4', 'connectionTemplateUri': None},
                     {'name': 'net21', 'vlanId': '1081', 'purpose': 'General', 'smartLink': 'false', 'privateNetwork': 'false', 'ethernetNetworkType': 'Tagged', 'type': 'ethernet-networkV4', 'connectionTemplateUri': None},
                     {'name': 'net22', 'vlanId': '1082', 'purpose': 'General', 'smartLink': 'false', 'privateNetwork': 'false', 'ethernetNetworkType': 'Tagged', 'type': 'ethernet-networkV4', 'connectionTemplateUri': None},
                     {'name': 'net23', 'vlanId': '1083', 'purpose': 'General', 'smartLink': 'false', 'privateNetwork': 'false', 'ethernetNetworkType': 'Tagged', 'type': 'ethernet-networkV4', 'connectionTemplateUri': None},
                     {'name': 'net24', 'vlanId': '1084', 'purpose': 'General', 'smartLink': 'false', 'privateNetwork': 'false', 'ethernetNetworkType': 'Tagged', 'type': 'ethernet-networkV4', 'connectionTemplateUri': None},
                     {'name': 'net25', 'vlanId': '1085', 'purpose': 'General', 'smartLink': 'false', 'privateNetwork': 'false', 'ethernetNetworkType': 'Tagged', 'type': 'ethernet-networkV4', 'connectionTemplateUri': None},
                     {'name': 'net300', 'vlanId': '1086', 'purpose': 'General', 'smartLink': 'false', 'privateNetwork': 'false', 'ethernetNetworkType': 'Tagged', 'type': 'ethernet-networkV4', 'connectionTemplateUri': None}
                     ]

expected_ethernet_networks = [{'name': 'net10', 'type': 'ethernet-networkV4', 'ethernetNetworkType': 'Tagged', 'vlanId': '1070', 'smartLink': 'False', 'purpose': 'General', 'privateNetwork': 'False', 'subnetUri': None, 'description': None, 'status': 'OK', 'state': 'Active', 'category': 'ethernet-networks', 'uri': 'ETH:net10'},
                              {'name': 'net11', 'type': 'ethernet-networkV4', 'ethernetNetworkType': 'Tagged', 'vlanId': '1071', 'smartLink': 'False', 'purpose': 'Management', 'privateNetwork': 'False', 'subnetUri': None, 'description': None, 'status': 'OK', 'state': 'Active', 'category': 'ethernet-networks', 'uri': 'ETH:net11'},
                              {'name': 'net12', 'type': 'ethernet-networkV4', 'ethernetNetworkType': 'Tagged', 'vlanId': '1072', 'smartLink': 'False', 'purpose': 'Management', 'privateNetwork': 'False', 'subnetUri': None, 'description': None, 'status': 'OK', 'state': 'Active', 'category': 'ethernet-networks', 'uri': 'ETH:net12'},
                              {'name': 'net13', 'type': 'ethernet-networkV4', 'ethernetNetworkType': 'Tagged', 'vlanId': '1073', 'smartLink': 'False', 'purpose': 'Management', 'privateNetwork': 'False', 'subnetUri': None, 'description': None, 'status': 'OK', 'state': 'Active', 'category': 'ethernet-networks', 'uri': 'ETH:net13'},
                              {'name': 'net14', 'type': 'ethernet-networkV4', 'ethernetNetworkType': 'Tagged', 'vlanId': '1074', 'smartLink': 'False', 'purpose': 'Management', 'privateNetwork': 'False', 'subnetUri': None, 'description': None, 'status': 'OK', 'state': 'Active', 'category': 'ethernet-networks', 'uri': 'ETH:net14'},
                              {'name': 'net15', 'type': 'ethernet-networkV4', 'ethernetNetworkType': 'Tagged', 'vlanId': '1075', 'smartLink': 'False', 'purpose': 'General', 'privateNetwork': 'False', 'subnetUri': None, 'description': None, 'status': 'OK', 'state': 'Active', 'category': 'ethernet-networks', 'uri': 'ETH:net15'},
                              {'name': 'net16', 'type': 'ethernet-networkV4', 'ethernetNetworkType': 'Tagged', 'vlanId': '1076', 'smartLink': 'False', 'purpose': 'General', 'privateNetwork': 'False', 'subnetUri': None, 'description': None, 'status': 'OK', 'state': 'Active', 'category': 'ethernet-networks', 'uri': 'ETH:net16'},
                              {'name': 'net17', 'type': 'ethernet-networkV4', 'ethernetNetworkType': 'Tagged', 'vlanId': '1077', 'smartLink': 'False', 'purpose': 'VMMigration', 'privateNetwork': 'False', 'subnetUri': None, 'description': None, 'status': 'OK', 'state': 'Active', 'category': 'ethernet-networks', 'uri': 'ETH:net17'},
                              {'name': 'net18', 'type': 'ethernet-networkV4', 'ethernetNetworkType': 'Tagged', 'vlanId': '1078', 'smartLink': 'False', 'purpose': 'General', 'privateNetwork': 'False', 'subnetUri': None, 'description': None, 'status': 'OK', 'state': 'Active', 'category': 'ethernet-networks', 'uri': 'ETH:net18'},
                              {'name': 'net19', 'type': 'ethernet-networkV4', 'ethernetNetworkType': 'Tagged', 'vlanId': '1079', 'smartLink': 'False', 'purpose': 'General', 'privateNetwork': 'False', 'subnetUri': None, 'description': None, 'status': 'OK', 'state': 'Active', 'category': 'ethernet-networks', 'uri': 'ETH:net19'},
                              {'name': 'net20', 'type': 'ethernet-networkV4', 'ethernetNetworkType': 'Tagged', 'vlanId': '1080', 'smartLink': 'False', 'purpose': 'General', 'privateNetwork': 'False', 'subnetUri': None, 'description': None, 'status': 'OK', 'state': 'Active', 'category': 'ethernet-networks', 'uri': 'ETH:net20'},
                              {'name': 'net21', 'type': 'ethernet-networkV4', 'ethernetNetworkType': 'Tagged', 'vlanId': '1081', 'smartLink': 'False', 'purpose': 'General', 'privateNetwork': 'False', 'subnetUri': None, 'description': None, 'status': 'OK', 'state': 'Active', 'category': 'ethernet-networks', 'uri': 'ETH:net21'},
                              {'name': 'net22', 'type': 'ethernet-networkV4', 'ethernetNetworkType': 'Tagged', 'vlanId': '1082', 'smartLink': 'False', 'purpose': 'General', 'privateNetwork': 'False', 'subnetUri': None, 'description': None, 'status': 'OK', 'state': 'Active', 'category': 'ethernet-networks', 'uri': 'ETH:net22'},
                              {'name': 'net23', 'type': 'ethernet-networkV4', 'ethernetNetworkType': 'Tagged', 'vlanId': '1083', 'smartLink': 'False', 'purpose': 'General', 'privateNetwork': 'False', 'subnetUri': None, 'description': None, 'status': 'OK', 'state': 'Active', 'category': 'ethernet-networks', 'uri': 'ETH:net23'},
                              {'name': 'net24', 'type': 'ethernet-networkV4', 'ethernetNetworkType': 'Tagged', 'vlanId': '1084', 'smartLink': 'False', 'purpose': 'General', 'privateNetwork': 'False', 'subnetUri': None, 'description': None, 'status': 'OK', 'state': 'Active', 'category': 'ethernet-networks', 'uri': 'ETH:net24'},
                              {'name': 'net25', 'type': 'ethernet-networkV4', 'ethernetNetworkType': 'Tagged', 'vlanId': '1085', 'smartLink': 'False', 'purpose': 'General', 'privateNetwork': 'False', 'subnetUri': None, 'description': None, 'status': 'OK', 'state': 'Active', 'category': 'ethernet-networks', 'uri': 'ETH:net25'},
                              {'name': 'net300', 'type': 'ethernet-networkV4', 'ethernetNetworkType': 'Tagged', 'vlanId': '1086', 'smartLink': 'False', 'purpose': 'General', 'privateNetwork': 'False', 'subnetUri': None, 'description': None, 'status': 'OK', 'state': 'Active', 'category': 'ethernet-networks', 'uri': 'ETH:net300'}
                              ]

fc_networks = [{'name': 'wpstsan10-a', 'autoLoginRedistribution': 'true', 'type': 'fc-networkV4', 'linkStabilityTime': '30', 'fabricType': 'FabricAttach', 'connectionTemplateUri': None, 'managedSanUri': 'FCSan:VSAN3505'},
               {'name': 'wpstsan10-b', 'autoLoginRedistribution': 'true', 'type': 'fc-networkV4', 'linkStabilityTime': '30', 'fabricType': 'FabricAttach', 'connectionTemplateUri': None, 'managedSanUri': 'FCSan:VSAN3506'},
               {'name': '3par-a', 'autoLoginRedistribution': 'false', 'type': 'fc-networkV4', 'linkStabilityTime': '0', 'fabricType': 'DirectAttach', 'connectionTemplateUri': None, 'managedSanUri': None},
               {'name': '3par-b', 'autoLoginRedistribution': 'true', 'type': 'fc-networkV4', 'linkStabilityTime': '0', 'fabricType': 'DirectAttach', 'connectionTemplateUri': None, 'managedSanUri': None}]

expected_fc_networks = [{'name': 'wpstsan10-a', 'type': 'fc-networkV4', 'fabricType': 'FabricAttach', 'linkStabilityTime': '30', 'managedSanUri': 'FCSan:VSAN3505', 'autoLoginRedistribution': 'True', 'description': None, 'status': 'OK', 'state': 'Active', 'category': 'fc-networks', 'uri': 'FC:wpstsan10-a'},
                        {'name': 'wpstsan10-b', 'type': 'fc-networkV4', 'fabricType': 'FabricAttach', 'linkStabilityTime': '30', 'managedSanUri': 'FCSan:VSAN3506', 'autoLoginRedistribution': 'True', 'description': None, 'status': 'OK', 'state': 'Active', 'category': 'fc-networks', 'uri': 'FC:wpstsan10-b'},
                        {'name': '3par-a', 'type': 'fc-networkV4', 'fabricType': 'DirectAttach', 'linkStabilityTime': '0', 'managedSanUri': None, 'autoLoginRedistribution': 'False', 'description': None, 'status': 'OK', 'state': 'Active', 'category': 'fc-networks', 'uri': 'FC:3par-a'},
                        {'name': '3par-b', 'type': 'fc-networkV4', 'fabricType': 'DirectAttach', 'linkStabilityTime': '0', 'managedSanUri': None, 'autoLoginRedistribution': 'False', 'description': None, 'status': 'OK', 'state': 'Active', 'category': 'fc-networks', 'uri': 'FC:3par-b'}]

networksets = [{'name': 'netset1', 'nativeNetworkUri': 'net10', 'type': 'network-setV4', 'networkUris': ['net10', 'net11', 'net12', 'net13']},
               {'name': 'netset2', 'nativeNetworkUri': 'net14', 'type': 'network-setV4', 'networkUris': ['net14', 'net15', 'net16', 'net17']},
               {'name': 'netset3', 'nativeNetworkUri': 'net18', 'type': 'network-setV4', 'networkUris': ['net18', 'net19', 'net20', 'net21']},
               {'name': 'netset4', 'nativeNetworkUri': 'net22', 'type': 'network-setV4', 'networkUris': ['net22', 'net23', 'net24', 'net25']}
               ]

expected_networksets = [{'name': 'netset1', 'type': 'network-setV4', 'networkUris': ['ETH:net10', 'ETH:net11', 'ETH:net12', 'ETH:net13'], 'nativeNetworkUri':'ETH:net10', 'description':None, 'status':'OK', 'state':'Active', 'category':'network-sets', 'uri':'NS:netset1'},
                        {'name': 'netset2', 'type': 'network-setV4', 'networkUris': ['ETH:net14', 'ETH:net15', 'ETH:net16', 'ETH:net17'], 'nativeNetworkUri':'ETH:net14', 'description':None, 'status':'OK', 'state':'Active', 'category':'network-sets', 'uri':'NS:netset2'},
                        {'name': 'netset3', 'type': 'network-setV4', 'networkUris': ['ETH:net18', 'ETH:net19', 'ETH:net20', 'ETH:net21'], 'nativeNetworkUri':'ETH:net18', 'description':None, 'status':'OK', 'state':'Active', 'category':'network-sets', 'uri':'NS:netset3'},
                        {'name': 'netset4', 'type': 'network-setV4', 'networkUris': ['ETH:net22', 'ETH:net23', 'ETH:net24', 'ETH:net25'], 'nativeNetworkUri':'ETH:net22', 'description':None, 'status':'OK', 'state':'Active', 'category':'network-sets', 'uri':'NS:netset4'}
                        ]

uplink_sets = {'lig1-enet': {'name': 'LIG-net', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['net10', 'net11', 'net12', 'net13', 'net14', 'net15', 'net16', 'net17', 'net18',
                                                                                                                            'net19', 'net20', 'net21', 'net22', 'net23', 'net24', 'net25', 'net300'], 'mode': 'Auto',
                             'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q1', 'speed': 'Auto'},
                                                        {'enclosure': '1', 'bay': '3', 'port': 'Q2', 'speed': 'Auto'},
                                                        {'enclosure': '2', 'bay': '6', 'port': 'Q1', 'speed': 'Auto'},
                                                        {'enclosure': '2', 'bay': '6', 'port': 'Q2', 'speed': 'Auto'}
                                                        ]}}

ligs = [{'name': 'LIG_3Enc_Ring',
         'type': 'logical-interconnect-groupV4',
         'enclosureType': 'SY12000',
         'ethernetSettings': {'enableIgmpSnooping': True, 'igmpIdleTimeoutInterval': 240, 'enableFastMacCacheFailover': False, 'macRefreshInterval': 15,
                              'enableNetworkLoopProtection': False, 'enablePauseFloodProtection': False},
         'description': None,
         'status': None,
         'state': None,
         'category': None,
         'created': None,
         'modified': None,
         'eTag': None,
         'uri': None,
         'uplinkSets': [uplink_sets['lig1-enet'].copy()],
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
         'qosConfiguration': {'activeQosConfig': {'type': 'QosConfiguration', 'configType': 'Passthrough', 'downlinkClassificationType': None, 'uplinkClassificationType': None, 'qosTrafficClassifiers': None, 'description': None, 'status': None, 'name': None, 'state': None, 'category': 'qos-aggregated-configuration', 'created': None, 'modified': None, 'eTag': None, 'uri': None}, 'inactiveFCoEQosConfig': None, 'inactiveNonFCoEQosConfig': None, 'type': 'qos-aggregated-configuration', 'name': None, 'state': None, 'status': None, 'eTag': None, 'modified': None, 'created': None, 'category': 'qos-aggregated-configuration', 'uri': None}},
        ]

expected_lig = [{'name': 'LIG_3Enc_Ring', 'type': 'logical-interconnect-groupV4', 'enclosureType': 'SY12000',
                 # ==============================================================
                 # 'uplinkSets': [{'lig1-enet': {'name': 'LIG-net', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['net10', 'net11', 'net12', 'net13', 'net14', 'net15', 'net16', 'net17', 'net18',
                 #                                                                                                             'net19', 'net20', 'net21', 'net22', 'net23', 'net24', 'net25', 'net300'], 'mode': 'Auto',
                 #             'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q1', 'speed': 'Auto'},
                 #                                        {'enclosure': '1', 'bay': '3', 'port': 'Q2', 'speed': 'Auto'},
                 #                                        {'enclosure': '2', 'bay': '6', 'port': 'Q1', 'speed': 'Auto'},
                 #                                        {'enclosure': '2', 'bay': '6', 'port': 'Q2', 'speed': 'Auto'}
                 #                                        ]}}],
                 # ==============================================================
                 'qosConfiguration': {'type': 'qos-aggregated-configuration', 'activeQosConfig': {'type': 'QosConfiguration', 'configType': 'Passthrough', 'downlinkClassificationType': None, 'uplinkClassificationType': None, 'qosTrafficClassifiers': '[]',
                                                                                                  'description': None, 'name': None, 'state': None, 'status': None, 'created': None, 'eTag': None, 'modified': None, 'category': 'qos-aggregated-configuration', 'uri': None},
                                      'inactiveFCoEQosConfig': None, 'inactiveNonFCoEQosConfig': None, 'description': None, 'name': None, 'state': None, 'status': None},
                 'stackingHealth': None,
                 #                  'interconnectMapTemplate': {'interconnectMapEntryTemplates': [{'enclosureIndex': 2, 'logicalLocation': {'locationEntries': [{'relativeValue': 3, 'type': 'Bay'}, {'relativeValue': 2, 'type': 'Enclosure'}]}, },
                 #                                                                                {'enclosureIndex': 2, 'logicalLocation': {'locationEntries': [{'relativeValue': 2, 'type': 'Enclosure'}, {'relativeValue': 6, 'type': 'Bay'}]}, },
                 #                                                                                {'enclosureIndex': 1, 'logicalLocation': {'locationEntries': [{'relativeValue': 1, 'type': 'Enclosure'}, {'relativeValue': 6, 'type': 'Bay'}]}, },
                 #                                                                                {'enclosureIndex': 3, 'logicalLocation': {'locationEntries': [{'relativeValue': 3, 'type': 'Bay'}, {'relativeValue': 3, 'type': 'Enclosure'}]}, },
                 #                                                                                {'enclosureIndex': 1, 'logicalLocation': {'locationEntries': [{'relativeValue': 1, 'type': 'Enclosure'}, {'relativeValue': 3, 'type': 'Bay'}]}, },
                 #                                                                                {'enclosureIndex': 3, 'logicalLocation': {'locationEntries': [{'relativeValue': 3, 'type': 'Enclosure'}, {'relativeValue': 6, 'type': 'Bay'}]}, }]},
                 # TO-DO interconnectMapTemplate verification looking for a particular order each time, need to fix it
                 'internalNetworkUris': [], 'enclosureIndexes': [1, 2, 3], 'redundancyType': 'HighlyAvailable',
                 'interconnectBaySet': 3, 'stackingMode': None, 'scopeUris': [], 'description': None, 'state': 'Active', 'status': None,
                 'category': 'logical-interconnect-groups', 'uri': 'LIG:LIG_3Enc_Ring'}]

sas_lig = [{'name': 'dd-Natasha',
            'type': 'sas-logical-interconnect-groupV2',
            'enclosureType': 'SY12000',
            'description': None,
            'status': None,
            'state': None,
            'category': None,
            'created': None,
            'modified': None,
            'eTag': None,
            'uri': None,
            'interconnectMapTemplate': [{'bay': 1, 'enclosure': 1, 'type': 'Synergy 12Gb SAS Connection Module', 'enclosureIndex': 1},
                                        {'bay': 4, 'enclosure': 1, 'type': 'Synergy 12Gb SAS Connection Module', 'enclosureIndex': 1}],
            'interconnectBaySet': 1,
            'enclosureIndexes': [1]}
           ]

expected_sas_lig = [{'name': 'dd-Natasha',
                     'type': 'sas-logical-interconnect-groupV2',
                     'enclosureType': 'SY12000',
                     'description': None,
                     'status': 'OK',
                     'state': 'Active',
                     'uri': 'SASLIG:dd-Natasha',
                     #         'interconnectMapTemplate': [{'bay': 1, 'enclosure': 1, 'type': 'Synergy 12Gb SAS Connection Module', 'enclosureIndex': 1},
                     #                                     {'bay': 4, 'enclosure': 1, 'type': 'Synergy 12Gb SAS Connection Module', 'enclosureIndex': 1}],
                     'interconnectBaySet': 1,
                     'enclosureIndexes': [1]}]

encgroups_add = [{'name': 'EG_Ring',
                  'interconnectBayMappings': [{'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG_3Enc_Ring'},
                                              {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG_3Enc_Ring'}],
                  'enclosureCount': 3,
                  'ipAddressingMode': 'External'}]

expected_encgroups_add = [{'type': 'EnclosureGroupV7', 'uri': 'EG:EG_Ring', 'category': 'enclosure-groups', 'name': 'EG_Ring',
                           'status': 'OK', 'state': 'Normal', 'enclosureTypeUri': '/rest/enclosure-types/SY12000',
                           'stackingMode': 'Enclosure', 'portMappingCount': 8, 'portMappings': [{'midplanePort': 1, 'interconnectBay': 1},
                                                                                                {'midplanePort': 2, 'interconnectBay': 2},
                                                                                                {'midplanePort': 3, 'interconnectBay': 3},
                                                                                                {'midplanePort': 4, 'interconnectBay': 4},
                                                                                                {'midplanePort': 5, 'interconnectBay': 5},
                                                                                                {'midplanePort': 6, 'interconnectBay': 6},
                                                                                                {'midplanePort': 7, 'interconnectBay': 7},
                                                                                                {'midplanePort': 8, 'interconnectBay': 8}],
                           'interconnectBayMappingCount': 2, 'interconnectBayMappings': [{'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG_3Enc_Ring'},
                                                                                         {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG_3Enc_Ring'}, ],
                           'ipAddressingMode': 'External', 'ipRangeUris': [], 'powerMode': 'RedundantPowerFeed', 'description': None,
                           'associatedLogicalInterconnectGroups': ['LIG:LIG_3Enc_Ring'], 'enclosureCount': 3}]

edit_enclosure_group = {'type': 'EnclosureGroupV7', 'name': 'EG_Ring',
                        'interconnectBayMappings': [{'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG_3Enc_Ring'},
                                                    {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG_3Enc_Ring'}],
                        'interconnectBayMappingCount': 2, 'stackingMode': 'Enclosure', 'configurationScript': '',
                        'uri': 'EG_Ring', 'powerMode': 'RedundantPowerFeed', 'ipAddressingMode': 'External', 'ipRangeUris': [], 'enclosureCount': 3, 'osDeploymentSettings': None,
                        'enclosureTypeUri': '/rest/enclosure-types/SY12000'}

logical_enclosure = [{'name': 'LE_3Enc_Ring', 'enclosureUris': ['ENC:MXQ70700G4', 'ENC:MXQ708021V', 'ENC:MXQ708030N'], 'enclosureGroupUri': 'EG:EG_Ring'}]

expected_logical_enclosure = [{'type': 'LogicalEnclosureV4', 'name': 'LE_3Enc_Ring', 'status': 'OK', 'enclosureUris': ['ENC:MXQ70700G4', 'ENC:MXQ708021V', 'ENC:MXQ708030N'], 'enclosureGroupUri': 'EG:EG_Ring'}]
update_logical_enclosure_from_group = {'name': 'LE_3Enc_Ring'}

edit_li_telemetry_config = {'name': 'LE_3Enc_Ring-LIG_3Enc_Ring', 'type': 'telemetry-configuration', 'enableTelemetry': True, 'sampleCount': 20, 'sampleInterval': 200,
                            'description': None, 'status': None, 'state': None, 'category': 'telemetry-configurations',
                            'uri': '/rest/logical-interconnects'}

update_logical_interconnect_from_group = {'name': 'LE_3Enc_Ring-LIG_3Enc_Ring'}

li_state = {'name': 'LE_3Enc_Ring-LIG_3Enc_Ring'}

li_state_after_update = {'name': 'LE_3Enc_Ring-LIG_3Enc_Ring_update2'}

storage_systems_with_pools = [{'name': 'cosmos-cho', 'family': 'StoreServ', 'hostname': '16.95.208.238',
                               'credentials': {'username': 'cosmos', 'password': 'Insight7'}, 'serialNumber': '1649903',
                               'deviceSpecificAttributes': {'managedDomain': 'CHO', 'managedPools': []}}]

expected_storage_systems_with_pools = [{'type': 'StorageSystemV4', 'name': 'cosmos-cho', 'uri': 'SSYS:cosmos-cho', 'state': 'Managed',
                                        'deviceSpecificAttributes': {'managedDomain': 'CHO', 'serialNumber': '1649903'},
                                        'status': 'OK', 'category': 'storage-systems'}]

storage_pools_toedit = [{'storageSystemUri': 'cosmos-cho', 'name': 'CHO-FC-Raid5', 'isManaged': True}]

storage_volume_templates = [{'name': 'ova-private-thin', 'description': '', 'rootTemplateUri': 'SVT:ova-private-thin', 'description': 'private non-boot volume template',
                             'properties': {'name': {'title': 'Volume name', 'description': 'A volume name between 1 and 100 characters',
                                                     'type': 'string', 'minLength': 1, 'maxLength': 100, 'required': True, 'meta': {'locked': False}},
                                            'description': {'title': 'Description', 'description': 'A description for the volume',
                                                            'type': 'string', 'minLength': 0, 'maxLength': 2000, 'default': '', 'meta': {'locked': False}},
                                            'storagePool': {'title': 'Storage Pool', 'description': 'A common provisioning group URI reference',
                                                            'type': 'string', 'required': True, 'format': 'x-uri-reference',
                                                            'meta': {'locked': False, 'createOnly': True, 'semanticType': 'device-storage-pool'},
                                                            'default': 'CHO-FC-Raid5'},
                                            'size': {'title': 'Capacity', 'description': 'The capacity of the volume in bytes',
                                                     'type': 'integer', 'required': True, 'minimum': 1073741824, 'maximum': 17592186044416,
                                                     'meta': {'locked': False, 'semanticType': 'capacity'}, 'default': 1073741824, },
                                            'isShareable': {'title': 'Is Shareable', 'description': 'The shareability of the volume',
                                                            'type': 'boolean', 'meta': {'locked': False}, 'default': False, },
                                            'provisioningType': {'title': 'Provisioning Type', 'description': 'The provisioning type for the volume',
                                                                 'type': 'string', 'enum': ['Thin', 'Full'], 'meta':{'locked': True, 'createOnly': True},
                                                                 'default': 'Thin'},
                                            'snapshotPool': {'title': 'FC_wpst16_r1', 'description': 'A URI referenceto the common provisioning group used to create snapshots',
                                                             'type': 'string', 'format': 'x-uri-reference', 'meta': {'locked': True, 'semanticType': 'device-snapshot-storage-pool'},
                                                             'default': 'CHO-FC-Raid5'}}}]

expected_storage_volume_templates = [{'category': 'storage-volume-templates', 'name': 'ova-private-thin', 'status': 'OK',
                                      'state': 'Configured', 'type': 'StorageVolumeTemplateV5 ', 'uri': 'SVT:ova-private-thin',
                                      'properties': {'name': {'title': 'Volume name', 'description': 'A volume name between 1 and 100 characters',
                                                              'type': 'string', 'minLength': 1, 'maxLength': 100, 'required': True, 'meta': {'locked': False}},
                                                     'description': {'title': 'Description', 'description': 'A description for the volume',
                                                                     'type': 'string', 'minLength': 0, 'maxLength': 2000, 'default': '', 'meta': {'locked': False}},
                                                     'storagePool': {'title': 'Storage Pool', 'description': 'A common provisioning group URI reference',
                                                                     'type': 'string', 'required': True, 'format': 'x-uri-reference',
                                                                     'meta': {'locked': False, 'createOnly': True, 'semanticType': 'device-storage-pool'},
                                                                     'default': 'SPOOL:CHO-FC-Raid5'},
                                                     'size': {'title': 'Capacity', 'description': 'The capacity of the volume in bytes',
                                                              'type': 'integer', 'required': True, 'minimum': 1073741824, 'maximum': 17592186044416,
                                                              'meta': {'locked': False, 'semanticType': 'capacity'}, 'default': 1073741824, },
                                                     'isShareable': {'title': 'Is Shareable', 'description': 'The shareability of the volume',
                                                                     'type': 'boolean', 'meta': {'locked': False}, 'default': False, },
                                                     'provisioningType': {'title': 'Provisioning Type', 'description': 'The provisioning type for the volume',
                                                                          'type': 'string', 'enum': ['Thin', 'Full'], 'meta':{'locked': True, 'createOnly': True},
                                                                          'default': 'Thin'},
                                                     'snapshotPool': {'title': 'FC_wpst16_r1', 'description': 'A URI referenceto the common provisioning group used to create snapshots',
                                                                      'type': 'string', 'format': 'x-uri-reference', 'meta': {'locked': True, 'semanticType': 'device-snapshot-storage-pool'},
                                                                      'default': 'SPOOL:CHO-FC-Raid5'}}}]

storage_volumes = [  # new private no template
    {'properties': {'description': 'non-boot private volume', 'isShareable': False, 'name': 'enc2bay1priv',
                                   'provisioningType': 'Full', 'size': 5368709120, 'storagePool': 'CHO-FC-Raid5'}, 'templateUri': 'ROOT'},
    {'properties': {'description': 'non-boot private volume', 'isShareable': False, 'name': 'enc2bay2priv',
                                   'provisioningType': 'Full', 'size': 5368709120, 'storagePool': 'CHO-FC-Raid5'}, 'templateUri': 'ROOT'},
    {'properties': {'description': 'non-boot private volume', 'isShareable': False, 'name': 'enc2bay3priv',
                                   'provisioningType': 'Full', 'size': 5368709120, 'storagePool': 'CHO-FC-Raid5'}, 'templateUri': 'ROOT'},
    {'properties': {'description': 'non-boot private volume', 'isShareable': False, 'name': 'enc2bay4priv',
                                   'provisioningType': 'Full', 'size': 5368709120, 'storagePool': 'CHO-FC-Raid5'}, 'templateUri': 'ROOT'},
    # new private with template
    {'properties': {'description': 'non-boot private volume', 'isShareable': False, 'name': 'enc2bay7priv',
                                   'size': 5368709120, 'storagePool': 'CHO-FC-Raid5'}, 'templateUri': 'ova-private-thin'},
    {'properties': {'description': 'non-boot private volume', 'isShareable': False, 'name': 'enc2bay8priv',
                                   'size': 5368709120, 'storagePool': 'CHO-FC-Raid5'}, 'templateUri': 'ova-private-thin'},
    {'properties': {'description': 'non-boot private volume', 'isShareable': False, 'name': 'enc2bay9priv',
                                   'size': 5368709120, 'storagePool': 'CHO-FC-Raid5'}, 'templateUri': 'ova-private-thin'},
    {'properties': {'description': 'non-boot private volume', 'isShareable': False, 'name': 'enc2bay10priv',
                                   'size': 5368709120, 'storagePool': 'CHO-FC-Raid5'}, 'templateUri': 'ova-private-thin'},

    {'properties': {'description': 'non-boot private volume', 'isShareable': False, 'name': 'enc2-bay1-bfsDoNotDelfrom3PAR',
                                   'provisioningType': 'Full', 'size': 5368709120, 'storagePool': 'CHO-FC-Raid5'}, 'templateUri': 'ROOT'},
    {'properties': {'description': 'non-boot private volume', 'isShareable': False, 'name': 'enc2-bay2-bfsDoNotDelfrom3PAR',
                                   'provisioningType': 'Full', 'size': 5368709120, 'storagePool': 'CHO-FC-Raid5'}, 'templateUri': 'ROOT'},
    {'properties': {'description': 'non-boot private volume', 'isShareable': False, 'name': 'enc2-bay3-bfsDoNotDelfrom3PAR',
                                   'provisioningType': 'Full', 'size': 5368709120, 'storagePool': 'CHO-FC-Raid5'}, 'templateUri': 'ROOT'},
    {'properties': {'description': 'non-boot private volume', 'isShareable': False, 'name': 'enc2-bay4-bfsDoNotDelfrom3PAR',
                                   'provisioningType': 'Full', 'size': 5368709120, 'storagePool': 'CHO-FC-Raid5'}, 'templateUri': 'ROOT'},
    {'properties': {'description': 'non-boot private volume', 'isShareable': False, 'name': 'enc2-bay7-bfsDoNotDelfrom3PAR',
                                   'provisioningType': 'Full', 'size': 5368709120, 'storagePool': 'CHO-FC-Raid5'}, 'templateUri': 'ROOT'},
    {'properties': {'description': 'non-boot private volume', 'isShareable': False, 'name': 'enc2-bay8-bfsDoNotDelfrom3PAR',
                                   'provisioningType': 'Full', 'size': 5368709120, 'storagePool': 'CHO-FC-Raid5'}, 'templateUri': 'ROOT'},
    {'properties': {'description': 'non-boot private volume', 'isShareable': False, 'name': 'enc2-bay9-bfsDoNotDelfrom3PAR',
                                   'provisioningType': 'Full', 'size': 5368709120, 'storagePool': 'CHO-FC-Raid5'}, 'templateUri': 'ROOT'},
    {'properties': {'description': 'non-boot private volume', 'isShareable': False, 'name': 'enc2-bay10-bfsDoNotDelfrom3PAR',
                                   'provisioningType': 'Full', 'size': 5368709120, 'storagePool': 'CHO-FC-Raid5'}, 'templateUri': 'ROOT'},

    # shared volume
    {'properties': {'description': 'shared volume', 'isShareable': True, 'name': 'dd-shared',
                                   'provisioningType': 'Full', 'size': 5368709120, 'storagePool': 'CHO-FC-Raid5'}, 'templateUri': 'ROOT', 'isPermanent': True}]

expected_storage_volumes = [{'isShareable': False, 'name': 'enc2bay1priv', 'state': 'Managed', 'status': 'OK', 'storagePoolUri': 'SPOOL:CHO-FC-Raid5', 'type': 'StorageVolumeV5'},
                            {'isShareable': False, 'name': 'enc2bay2priv', 'state': 'Managed', 'status': 'OK', 'storagePoolUri': 'SPOOL:CHO-FC-Raid5', 'type': 'StorageVolumeV5'},
                            {'isShareable': False, 'name': 'enc2bay3priv', 'state': 'Managed', 'status': 'OK', 'storagePoolUri': 'SPOOL:CHO-FC-Raid5', 'type': 'StorageVolumeV5'},
                            {'isShareable': False, 'name': 'enc2bay4priv', 'state': 'Managed', 'status': 'OK', 'storagePoolUri': 'SPOOL:CHO-FC-Raid5', 'type': 'StorageVolumeV5'},

                            {'isShareable': False, 'name': 'enc2bay7priv', 'state': 'Managed', 'status': 'OK', 'storagePoolUri': 'SPOOL:CHO-FC-Raid5', 'type': 'StorageVolumeV5'},
                            {'isShareable': False, 'name': 'enc2bay8priv', 'state': 'Managed', 'status': 'OK', 'storagePoolUri': 'SPOOL:CHO-FC-Raid5', 'type': 'StorageVolumeV5'},
                            {'isShareable': False, 'name': 'enc2bay9priv', 'state': 'Managed', 'status': 'OK', 'storagePoolUri': 'SPOOL:CHO-FC-Raid5', 'type': 'StorageVolumeV5'},
                            {'isShareable': False, 'name': 'enc2bay10priv', 'state': 'Managed', 'status': 'OK', 'storagePoolUri': 'SPOOL:CHO-FC-Raid5', 'type': 'StorageVolumeV5'},

                            {'isShareable': False, 'name': 'enc2-bay1-bfsDoNotDelfrom3PAR', 'state': 'Managed', 'status': 'OK', 'storagePoolUri': 'SPOOL:CHO-FC-Raid5', 'type': 'StorageVolumeV5'},
                            {'isShareable': False, 'name': 'enc2-bay2-bfsDoNotDelfrom3PAR', 'state': 'Managed', 'status': 'OK', 'storagePoolUri': 'SPOOL:CHO-FC-Raid5', 'type': 'StorageVolumeV5'},
                            {'isShareable': False, 'name': 'enc2-bay3-bfsDoNotDelfrom3PAR', 'state': 'Managed', 'status': 'OK', 'storagePoolUri': 'SPOOL:CHO-FC-Raid5', 'type': 'StorageVolumeV5'},
                            {'isShareable': False, 'name': 'enc2-bay4-bfsDoNotDelfrom3PAR', 'state': 'Managed', 'status': 'OK', 'storagePoolUri': 'SPOOL:CHO-FC-Raid5', 'type': 'StorageVolumeV5'},
                            {'isShareable': False, 'name': 'enc2-bay7-bfsDoNotDelfrom3PAR', 'state': 'Managed', 'status': 'OK', 'storagePoolUri': 'SPOOL:CHO-FC-Raid5', 'type': 'StorageVolumeV5'},
                            {'isShareable': False, 'name': 'enc2-bay8-bfsDoNotDelfrom3PAR', 'state': 'Managed', 'status': 'OK', 'storagePoolUri': 'SPOOL:CHO-FC-Raid5', 'type': 'StorageVolumeV5'},
                            {'isShareable': False, 'name': 'enc2-bay9-bfsDoNotDelfrom3PAR', 'state': 'Managed', 'status': 'OK', 'storagePoolUri': 'SPOOL:CHO-FC-Raid5', 'type': 'StorageVolumeV5'},
                            {'isShareable': False, 'name': 'enc2-bay10-bfsDoNotDelfrom3PAR', 'state': 'Managed', 'status': 'OK', 'storagePoolUri': 'SPOOL:CHO-FC-Raid5', 'type': 'StorageVolumeV5'},

                            {'isShareable': True, 'name': 'dd-shared', 'state': 'Managed', 'status': 'OK', 'storagePoolUri': 'SPOOL:CHO-FC-Raid5', 'type': 'StorageVolumeV5'}]

delete_storage_volumes_from_DCS = [{'type': 'AddStorageVolumeV3', 'name': 'enc2-bay1-bfsDoNotDelfrom3PAR', 'description': '', 'storageSystemUri': 'ThreePAR-1', 'storageSystemVolumeName': 'enc2-bay1-bfsDoNotDelfrom3PAR', 'provisioningParameters': {'shareable': False}},
                                   {'type': 'AddStorageVolumeV3', 'name': 'enc2-bay2-bfsDoNotDelfrom3PAR', 'description': '', 'storageSystemUri': 'ThreePAR-1', 'storageSystemVolumeName': 'enc2-bay2-bfsDoNotDelfrom3PAR', 'provisioningParameters': {'shareable': False}},
                                   {'type': 'AddStorageVolumeV3', 'name': 'enc2-bay3-bfsDoNotDelfrom3PAR', 'description': '', 'storageSystemUri': 'ThreePAR-1', 'storageSystemVolumeName': 'enc2-bay3-bfsDoNotDelfrom3PAR', 'provisioningParameters': {'shareable': False}},
                                   {'type': 'AddStorageVolumeV3', 'name': 'enc2-bay4-bfsDoNotDelfrom3PAR', 'description': '', 'storageSystemUri': 'ThreePAR-1', 'storageSystemVolumeName': 'enc2-bay4-bfsDoNotDelfrom3PAR', 'provisioningParameters': {'shareable': False}},
                                   {'type': 'AddStorageVolumeV3', 'name': 'enc2-bay7-bfsDoNotDelfrom3PAR', 'description': '', 'storageSystemUri': 'ThreePAR-1', 'storageSystemVolumeName': 'enc2-bay7-bfsDoNotDelfrom3PAR', 'provisioningParameters': {'shareable': False}},
                                   {'type': 'AddStorageVolumeV3', 'name': 'enc2-bay8-bfsDoNotDelfrom3PAR', 'description': '', 'storageSystemUri': 'ThreePAR-1', 'storageSystemVolumeName': 'enc2-bay8-bfsDoNotDelfrom3PAR', 'provisioningParameters': {'shareable': False}},
                                   {'type': 'AddStorageVolumeV3', 'name': 'enc2-bay9-bfsDoNotDelfrom3PAR', 'description': '', 'storageSystemUri': 'ThreePAR-1', 'storageSystemVolumeName': 'enc2-bay9-bfsDoNotDelfrom3PAR', 'provisioningParameters': {'shareable': False}},
                                   {'type': 'AddStorageVolumeV3', 'name': 'enc2-bay10-bfsDoNotDelfrom3PAR', 'description': '', 'storageSystemUri': 'ThreePAR-1', 'storageSystemVolumeName': 'enc2-bay10-bfsDoNotDelfrom3PAR', 'provisioningParameters': {'shareable': False}}]

add_existing_storage_volumes = [{'storageSystemUri': 'ThreePAR-1', 'deviceVolumeName': 'enc2-bay1-bfsDoNotDelfrom3PAR',
                                 'name': 'enc2-bay1-bfsDoNotDelfrom3PAR', 'isShareable': False},
                                {'storageSystemUri': 'ThreePAR-1', 'deviceVolumeName': 'enc2-bay2-bfsDoNotDelfrom3PAR',
                                 'name': 'enc2-bay2-bfsDoNotDelfrom3PAR', 'isShareable': False},
                                {'storageSystemUri': 'ThreePAR-1', 'deviceVolumeName': 'enc2-bay3-bfsDoNotDelfrom3PAR',
                                 'name': 'enc2-bay3-bfsDoNotDelfrom3PAR', 'isShareable': False},
                                {'storageSystemUri': 'ThreePAR-1', 'deviceVolumeName': 'enc2-bay4-bfsDoNotDelfrom3PAR',
                                 'name': 'enc2-bay4-bfsDoNotDelfrom3PAR', 'isShareable': False},
                                {'storageSystemUri': 'ThreePAR-1', 'deviceVolumeName': 'enc2-bay7-bfsDoNotDelfrom3PAR',
                                 'name': 'enc2-bay7-bfsDoNotDelfrom3PAR', 'isShareable': False},
                                {'storageSystemUri': 'ThreePAR-1', 'deviceVolumeName': 'enc2-bay8-bfsDoNotDelfrom3PAR',
                                 'name': 'enc2-bay8-bfsDoNotDelfrom3PAR', 'isShareable': False},
                                {'storageSystemUri': 'ThreePAR-1', 'deviceVolumeName': 'enc2-bay9-bfsDoNotDelfrom3PAR',
                                 'name': 'enc2-bay9-bfsDoNotDelfrom3PAR', 'isShareable': False},
                                {'storageSystemUri': 'ThreePAR-1', 'deviceVolumeName': 'enc2-bay10-bfsDoNotDelfrom3PAR',
                                 'name': 'enc2-bay10-bfsDoNotDelfrom3PAR', 'isShareable': False}]

expected_existing_storage_volumes = [{'isShareable': False, 'name': 'enc2-bay1-bfsDoNotDelfrom3PAR', 'state': 'Managed', 'status': 'OK', 'storagePoolUri': 'SPOOL:CHO-FC-Raid5', 'type': 'StorageVolumeV5'},
                                     {'isShareable': False, 'name': 'enc2-bay2-bfsDoNotDelfrom3PAR', 'state': 'Managed', 'status': 'OK', 'storagePoolUri': 'SPOOL:CHO-FC-Raid5', 'type': 'StorageVolumeV5'},
                                     {'isShareable': False, 'name': 'enc2-bay3-bfsDoNotDelfrom3PAR', 'state': 'Managed', 'status': 'OK', 'storagePoolUri': 'SPOOL:CHO-FC-Raid5', 'type': 'StorageVolumeV5'},
                                     {'isShareable': False, 'name': 'enc2-bay4-bfsDoNotDelfrom3PAR', 'state': 'Managed', 'status': 'OK', 'storagePoolUri': 'SPOOL:CHO-FC-Raid5', 'type': 'StorageVolumeV5'},
                                     {'isShareable': False, 'name': 'enc2-bay7-bfsDoNotDelfrom3PAR', 'state': 'Managed', 'status': 'OK', 'storagePoolUri': 'SPOOL:CHO-FC-Raid5', 'type': 'StorageVolumeV5'},
                                     {'isShareable': False, 'name': 'enc2-bay8-bfsDoNotDelfrom3PAR', 'state': 'Managed', 'status': 'OK', 'storagePoolUri': 'SPOOL:CHO-FC-Raid5', 'type': 'StorageVolumeV5'},
                                     {'isShareable': False, 'name': 'enc2-bay9-bfsDoNotDelfrom3PAR', 'state': 'Managed', 'status': 'OK', 'storagePoolUri': 'SPOOL:CHO-FC-Raid5', 'type': 'StorageVolumeV5'},
                                     {'isShareable': False, 'name': 'enc2-bay10-bfsDoNotDelfrom3PAR', 'state': 'Managed', 'status': 'OK', 'storagePoolUri': 'SPOOL:CHO-FC-Raid5', 'type': 'StorageVolumeV5'}]

delete_storage_volumes_from_OV_only = [{'type': 'AddStorageVolumeV3', 'name': 'enc2-bay1-bfsDoNotDelfrom3PAR', 'description': '', 'storageSystemUri': 'ThreePAR-1', 'storageSystemVolumeName': 'enc2-bay1-bfsDoNotDelfrom3PAR', 'provisioningParameters': {'shareable': False}},
                                       {'type': 'AddStorageVolumeV3', 'name': 'enc2-bay2-bfsDoNotDelfrom3PAR', 'description': '', 'storageSystemUri': 'ThreePAR-1', 'storageSystemVolumeName': 'enc2-bay2-bfsDoNotDelfrom3PAR', 'provisioningParameters': {'shareable': False}},
                                       {'type': 'AddStorageVolumeV3', 'name': 'enc2-bay3-bfsDoNotDelfrom3PAR', 'description': '', 'storageSystemUri': 'ThreePAR-1', 'storageSystemVolumeName': 'enc2-bay3-bfsDoNotDelfrom3PAR', 'provisioningParameters': {'shareable': False}},
                                       {'type': 'AddStorageVolumeV3', 'name': 'enc2-bay4-bfsDoNotDelfrom3PAR', 'description': '', 'storageSystemUri': 'ThreePAR-1', 'storageSystemVolumeName': 'enc2-bay4-bfsDoNotDelfrom3PAR', 'provisioningParameters': {'shareable': False}},
                                       {'type': 'AddStorageVolumeV3', 'name': 'enc2-bay7-bfsDoNotDelfrom3PAR', 'description': '', 'storageSystemUri': 'ThreePAR-1', 'storageSystemVolumeName': 'enc2-bay7-bfsDoNotDelfrom3PAR', 'provisioningParameters': {'shareable': False}},
                                       {'type': 'AddStorageVolumeV3', 'name': 'enc2-bay8-bfsDoNotDelfrom3PAR', 'description': '', 'storageSystemUri': 'ThreePAR-1', 'storageSystemVolumeName': 'enc2-bay8-bfsDoNotDelfrom3PAR', 'provisioningParameters': {'shareable': False}},
                                       {'type': 'AddStorageVolumeV3', 'name': 'enc2-bay9-bfsDoNotDelfrom3PAR', 'description': '', 'storageSystemUri': 'ThreePAR-1', 'storageSystemVolumeName': 'enc2-bay9-bfsDoNotDelfrom3PAR', 'provisioningParameters': {'shareable': False}},
                                       {'type': 'AddStorageVolumeV3', 'name': 'enc2-bay10-bfsDoNotDelfrom3PAR', 'description': '', 'storageSystemUri': 'ThreePAR-1', 'storageSystemVolumeName': 'enc2-bay10-bfsDoNotDelfrom3PAR', 'provisioningParameters': {'shareable': False}}]

storage_volumes_to_delete = [{'name': 'enc2bay1priv', 'storageSystemVolumeName': 'ThreePAR-1'},
                             {'name': 'enc2bay2priv', 'storageSystemVolumeName': 'ThreePAR-1'},
                             {'name': 'enc2bay3priv', 'storageSystemVolumeName': 'ThreePAR-1'},
                             {'name': 'enc2bay4priv', 'storageSystemVolumeName': 'ThreePAR-1'},
                             {'name': 'enc2bay7priv', 'storageSystemVolumeName': 'ThreePAR-1'},
                             {'name': 'enc2bay8priv', 'storageSystemVolumeName': 'ThreePAR-1'},
                             {'name': 'enc2bay9priv', 'storageSystemVolumeName': 'ThreePAR-1'},
                             {'name': 'enc2bay10priv', 'storageSystemVolumeName': 'ThreePAR-1'},
                             {'name': 'dd-shared', 'storageSystemVolumeName': 'ThreePAR-1'}]

server_profiles = [{'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ70700G4, bay 1',
                    'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1:3:Synergy 3820C 10/20Gb CNA', 'enclosureGroupUri': 'EG:EG_Ring',
                    'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'MXQ70700G4Bay1-to-Bay9', 'description': 'Created server profile from SP Transform DTO', 'affinity': 'Bay',
                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                    'boot': {'manageBoot': True, 'order': ['PXE']},
                    'bios': {'manageBios': True, 'overriddenSettings': [{'id': 'AdminName', 'value': 'WPST Tester1'}, {'id': 'AdminPhone', 'value': '111-111-1111'}]},
                    'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                    'connectionSettings': {'connections': [{'id': 1, 'name': 'Mezz 3:1-a', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:net10', 'functionType': 'Ethernet'}]}}]

expected_server_profiles = [{'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ70700G4, bay 1',
                             'status': 'OK', 'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1:3:Synergy 3820C 10/20Gb CNA', 'enclosureGroupUri': 'EG:EG_Ring',
                             'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                             'name': 'MXQ70700G4Bay1-to-Bay9', 'description': 'Created server profile from SP Transform DTO', 'affinity': 'Bay',
                             'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                             'boot': {'manageBoot': True, 'order': ['PXE']},
                             'bios': {'manageBios': True, 'overriddenSettings': [{'id': 'AdminName', 'value': 'WPST Tester1'}, {'id': 'AdminPhone', 'value': '111-111-1111'}]},
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                             'connectionSettings': {'connections': [{'id': 1, 'name': 'Mezz 3:1-a', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:net10', 'functionType': 'Ethernet'}]}}]

server_profile_with_storage = [{'name': 'Encl1bay7', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ70700G4, bay 7', 'serverHardwareTypeUri': '', 'enclosureGroupUri': '', 'serialNumberType': 'Virtual', 'iscsiInitiatorNameType': 'AutoGenerated', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:net10', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                                       {'id': 2, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b', 'requestedMbps': '4000', 'networkUri': 'FC:wpstsan10-a', 'mac': None, 'wwpn': '', 'wwnn': '',
                                                                        'boot': {'priority': 'Primary', 'bootVolumeSource': 'UserDefined', 'targets': [{'arrayWwpn': '20000002AC0008DE', 'lun': '1'}]}}]},
                                'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                'bootMode': {'pxeBootPolicy': None, 'manageMode': True, 'mode': 'BIOS'},
                                'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                'bios': {'manageBios': False, 'overriddenSettings': []},
                                'hideUnusedFlexNics':True, 'iscsiInitiatorName':'', 'osDeploymentSettings':None,
                                'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                'sanStorage': {'hostOSType': 'RHE Linux (5.x, 6.x)', 'manageSanStorage': True,
                                               'volumeAttachments': [{'id': 1, 'volumeUri': 'SVOL:enc2bay4priv', 'isBootVolume': False, 'lunType': 'Manual', 'lun': 1,
                                                                      'storagePaths': [{'isEnabled': True, 'connectionId': 2, 'targetSelector': 'Auto', 'targets': []}]}, ]}},

                               {'name': 'Encl1bay8', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ70700G4, bay 8', 'serverHardwareTypeUri': '', 'enclosureGroupUri': '', 'serialNumberType': 'Virtual', 'iscsiInitiatorNameType': 'AutoGenerated', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:net10', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                                       {'id': 2, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b', 'requestedMbps': '4000', 'networkUri': 'FC:wpstsan10-a', 'mac': None, 'wwpn': '', 'wwnn': '',
                                                                        'boot': {'priority': 'Primary', 'bootVolumeSource': 'UserDefined', 'targets': [{'arrayWwpn': '20000002AC0008DE', 'lun': '1'}]}}]},
                                'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                'bootMode': {'pxeBootPolicy': None, 'manageMode': True, 'mode': 'BIOS'},
                                'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                'bios': {'manageBios': False, 'overriddenSettings': []},
                                'hideUnusedFlexNics':True, 'iscsiInitiatorName':'', 'osDeploymentSettings':None,
                                'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                'sanStorage': {'hostOSType': 'RHE Linux (5.x, 6.x)', 'manageSanStorage': True,
                                               'volumeAttachments': [{'id': 1, 'volumeUri': 'SVOL:enc2bay7priv', 'isBootVolume': False, 'lunType': 'Manual', 'lun': 1,
                                                                      'storagePaths': [{'isEnabled': True, 'connectionId': 2, 'targetSelector': 'Auto', 'targets': []}]}, ]}}]

expected_server_profile_with_storage = [{'name': 'Encl1bay7', 'type': 'ServerProfileV8', 'uri': 'SP:Encl1bay7', 'description': '',
                                         'serverProfileTemplateUri': None, 'templateCompliance': 'Unknown',
                                         'serverHardwareUri': 'SH:MXQ70700G4, bay 7', 'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1:3:Synergy 3820C 10/20Gb CNA', 'enclosureGroupUri': 'EG:EG_Ring',
                                         'enclosureUri': 'ENC:MXQ70700G4', 'enclosureBay': 7, 'affinity': 'Bay', 'associatedServer': None,
                                         'hideUnusedFlexNics': True, 'firmware': {'firmwareInstallType': None, 'forceInstallFirmware': False, 'firmwareBaselineUri': None, 'manageFirmware': False},
                                         'macType': 'Virtual', 'wwnType': 'Virtual', 'serialNumberType': 'Virtual', 'category': 'server-profiles',
                                         'status': 'OK', 'state': 'Normal', 'inProgress': False,
                                         'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:net10', 'boot': {'priority': 'NotBootable'}},
                                                                                {'id': 2, 'name': '', 'functionType': 'FibreChannel', 'networkUri': 'FC:wpstsan10-a',
                                                                                 'portId': 'Mezz 3:1-b', 'requestedVFs': None, 'allocatedVFs': None, 'macType': 'Virtual',
                                                                                 'wwpnType': 'Virtual', 'requestedMbps': '4000', 'allocatedMbps': 4000, 'maximumMbps': 10000, 'boot': {'priority': 'Primary', 'targets': [{'arrayWwpn': '20000002AC0008DE', 'lun': '1'}], }}]},
                                         'bootMode': {'pxeBootPolicy': None, 'manageMode': True, 'mode': 'BIOS'},
                                         'boot': {'manageBoot': True, 'order': ['HardDisk', 'CD', 'USB', 'PXE']},
                                         'bios': {'overriddenSettings': [], 'manageBios': False},
                                         'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                                         'sanStorage': {'volumeAttachments': [{'storagePaths': [{'targetSelector': 'Auto', 'targets': [{'name': '20:00:00:02:AC:00:08:E2'}, {'name': '20:00:00:02:AC:00:08:DE'}], 'connectionId': 2, 'isEnabled': True, 'status': 'OK'}], 'isBootVolume': False, 'state': 'Attached', 'lun': '1',
                                                                               'volumeStoragePoolUri': 'SPOOL:CHO-FC-Raid5', 'volumeStorageSystemUri': 'SYS:ThreePAR-1', 'lunType': 'Manual', 'volumeUri': 'SVOL:enc2bay4priv', 'status': 'OK', 'id': 1}, ],
                                                        'hostOSType': 'RHE Linux (5.x, 6.x, 7.x)', 'manageSanStorage': True}, 'osDeploymentSettings': None, },

                                        {'name': 'Encl1bay8', 'type': 'ServerProfileV8', 'uri': 'SP:Encl1bay8', 'description': '',
                                         'serverProfileTemplateUri': None, 'templateCompliance': 'Unknown',
                                         'serverHardwareUri': 'SH:MXQ70700G4, bay 8', 'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1:3:Synergy 3820C 10/20Gb CNA', 'enclosureGroupUri': 'EG:EG_Ring',
                                         'enclosureUri': 'ENC:MXQ70700G4', 'enclosureBay': 8, 'affinity': 'Bay', 'associatedServer': None,
                                         'hideUnusedFlexNics': True, 'firmware': {'firmwareInstallType': None, 'forceInstallFirmware': False, 'firmwareBaselineUri': None, 'manageFirmware': False},
                                         'macType': 'Virtual', 'wwnType': 'Virtual', 'serialNumberType': 'Virtual', 'category': 'server-profiles',
                                         'status': 'OK', 'state': 'Normal', 'inProgress': False,
                                         'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:net10', 'boot': {'priority': 'NotBootable'}},
                                                                                {'id': 2, 'name': '', 'functionType': 'FibreChannel', 'networkUri': 'FC:wpstsan10-a',
                                                                                 'portId': 'Mezz 3:1-b', 'requestedVFs': None, 'allocatedVFs': None, 'macType': 'Virtual',
                                                                                 'wwpnType': 'Virtual', 'requestedMbps': '4000', 'allocatedMbps': 4000, 'maximumMbps': 10000, 'boot': {'priority': 'Primary', 'targets': [{'arrayWwpn': '20000002AC0008DE', 'lun': '1'}], }}]},
                                         'bootMode': {'pxeBootPolicy': None, 'manageMode': True, 'mode': 'BIOS'},
                                         'boot': {'manageBoot': True, 'order': ['HardDisk', 'CD', 'USB', 'PXE']},
                                         'bios': {'overriddenSettings': [], 'manageBios': False},
                                         'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                                         'sanStorage': {'volumeAttachments': [{'storagePaths': [{'targetSelector': 'Auto', 'targets': [{'name': '20:00:00:02:AC:00:08:E2'}, {'name': '20:00:00:02:AC:00:08:DE'}], 'connectionId': 2, 'isEnabled': True, 'status': 'OK'}], 'isBootVolume': False, 'state': 'Attached', 'lun': '1',
                                                                               'volumeStoragePoolUri': 'SPOOL:CHO-FC-Raid5', 'volumeStorageSystemUri': 'SYS:ThreePAR-1', 'lunType': 'Manual', 'volumeUri': 'SVOL:enc2bay7priv', 'status': 'OK', 'id': 1}, ],
                                                        'hostOSType': 'RHE Linux (5.x, 6.x, 7.x)', 'manageSanStorage': True}, 'osDeploymentSettings': None, }, ]

server_profile_templates = [{'name': 'SPT-ENCL1-BAY3', 'type': 'ServerProfileTemplateV4', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1:3:Synergy 3820C 10/20Gb CNA', 'enclosureGroupUri': 'EG:EG_Ring', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:net10', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:net11', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'FC:wpstsan10-a', 'boot': {'priority': 'NotBootable'}}], },
                             'boot': {'manageBoot': True, 'order': ['HardDisk']},
                             'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics':True, 'iscsiInitiatorNameType':'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage':None}]

expected_server_profile_templates = [{'type': 'ServerProfileTemplateV4', 'uri': 'SPT:SPT-ENCL1-BAY3', 'name': 'SPT-ENCL1-BAY3', 'description': '', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:SY 660 Gen9:1:Smart Array P542D Controller:2:HPE Synergy 3530C 16G Host Bus Adapter:3:HPE Synergy 3820C 10/20Gb Converged Network Adapter', 'enclosureGroupUri': 'EG:EG_Ring', 'affinity': 'Bay', 'hideUnusedFlexNics': True, 'macType': 'Virtual', 'wwnType': 'Virtual', 'serialNumberType': 'Virtual', 'iscsiInitiatorNameType': 'AutoGenerated',
                                      'firmware': {'manageFirmware': False, 'forceInstallFirmware': False},
                                      'connectionSettings': {'manageConnections': True,
                                                             'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:net10', 'boot': {'priority': 'NotBootable'}},
                                                                             {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:net11', 'boot': {'priority': 'NotBootable'}},
                                                                             {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'FC:wpstsan10-a', 'boot': {'priority': 'NotBootable'}}], },
                                      'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                      'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                      'bios': {'manageBios': False, 'overriddenSettings': []},
                                      'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                                      'sanStorage': {'manageSanStorage': False, 'volumeAttachments': []},
                                      'category': 'server-profile-templates',
                                      'status': 'OK', 'state': None}]

server_profiles_from_spt = [{'name': 'Encl1bay3', 'type': 'ServerProfileV8', 'serverHardwareUri': '0000A66101, bay 3', 'serverHardwareTypeUri': 'SHT:SY 660 Gen9:1:Smart Array P542D Controller:2:HPE Synergy 3530C 16G Host Bus Adapter:3:HPE Synergy 3820C 10/20Gb Converged Network Adapter', 'enclosureGroupUri': 'EG:EG_Ring', 'serialNumberType': 'Virtual', 'iscsiInitiatorNameType': 'AutoGenerated', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:net10', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:net11', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'FC:wpstsan10-a', 'boot': {'priority': 'NotBootable'}}]},
                             'boot': {'manageBoot': True, 'order': ['HardDisk']},
                             'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorName': '',
                             'serverProfileTemplateUri':'SPT:SPT-ENCL1-BAY3', 'osDeploymentSettings':None,
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage':None}]

expected_server_profiles_from_spt = [{'name': 'Encl1bay3', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:0000A66101, bay 3', 'serverHardwareTypeUri': 'SHT:SY 660 Gen9:1:Smart Array P542D Controller:2:HPE Synergy 3530C 16G Host Bus Adapter:3:HPE Synergy 3820C 10/20Gb Converged Network Adapter', 'enclosureGroupUri': 'EG:EG_Ring', 'serialNumberType': 'Virtual', 'iscsiInitiatorNameType': 'AutoGenerated', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                      'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:net10', 'boot': {'priority': 'NotBootable'}},
                                                                             {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:net11', 'boot': {'priority': 'NotBootable'}},
                                                                             {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'FC:wpstsan10-a', 'boot': {'priority': 'NotBootable'}}]},
                                      'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                      'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                      'firmware': {'manageFirmware': False, 'forceInstallFirmware': False},
                                      'bios': {'manageBios': False, 'overriddenSettings': []},
                                      'hideUnusedFlexNics': True,
                                      'serverProfileTemplateUri':'SPT:SPT-ENCL1-BAY3', 'osDeploymentSettings':None,
                                      'localStorage':{'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage':{'manageSanStorage': False, 'volumeAttachments': [], 'sanSystemCredentials': []}}]

monitored_enclosures = [{'name': 'MXQ70700G4', 'type': 'EnclosureV7', 'enclosureType': 'SY12000', 'serialNumber': 'MXQ70700G4',
                         'refreshState': 'NotRefreshing', 'state': 'Monitored',
                         'deviceBays': [{'bayNumber': 1, 'devicePresence': 'Present'}, {'bayNumber': 2, 'devicePresence': 'Present'}, {'bayNumber': 3, 'devicePresence': 'Present'},
                                        {'bayNumber': 4, 'devicePresence': 'Absent'}, {'bayNumber': 5, 'devicePresence': 'Absent'}, {'bayNumber': 6, 'devicePresence': 'Absent'},
                                        {'bayNumber': 7, 'devicePresence': 'Present'}, {'bayNumber': 8, 'devicePresence': 'Present'}, {'bayNumber': 9, 'devicePresence': 'Present'}, {'bayNumber': 10, 'devicePresence': 'Absent'}, {'bayNumber': 11, 'devicePresence': 'Absent'}, {'bayNumber': 12, 'devicePresence': 'Absent'}],
                         'interconnectBays': [{'bayNumber': 1, 'bayPowerState': 'Unknown'}, {'bayNumber': 2, 'bayPowerState': 'Unknown'}, {'bayNumber': 3, 'bayPowerState': 'Unknown'},
                                              {'bayNumber': 4, 'bayPowerState': 'Unknown'}, {'bayNumber': 5, 'bayPowerState': 'Unknown'}, {'bayNumber': 6, 'bayPowerState': 'Unknown'}],
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
                        {'name': 'MXQ708021V', 'type': 'EnclosureV7', 'enclosureType': 'SY12000', 'serialNumber': 'MXQ708021V',
                         'refreshState': 'NotRefreshing', 'state': 'Monitored',
                         'deviceBays': [{'bayNumber': 1, 'devicePresence': 'Present'}, {'bayNumber': 2, 'devicePresence': 'Present'}, {'bayNumber': 3, 'devicePresence': 'Present'},
                                        {'bayNumber': 4, 'devicePresence': 'Present'}, {'bayNumber': 5, 'devicePresence': 'Present'}, {'bayNumber': 6, 'devicePresence': 'Absent'},
                                        {'bayNumber': 7, 'devicePresence': 'Present'}, {'bayNumber': 8, 'devicePresence': 'Present'}, {'bayNumber': 9, 'devicePresence': 'Present'}, {'bayNumber': 10, 'devicePresence': 'Absent'}, {'bayNumber': 11, 'devicePresence': 'Subsumed'}, {'bayNumber': 12, 'devicePresence': 'Absent'}],
                         'interconnectBays': [{'bayNumber': 1, 'bayPowerState': 'Unknown'}, {'bayNumber': 2, 'bayPowerState': 'Unknown'}, {'bayNumber': 3, 'bayPowerState': 'Unknown'},
                                              {'bayNumber': 4, 'bayPowerState': 'Unknown'}, {'bayNumber': 5, 'bayPowerState': 'Unknown'}, {'bayNumber': 6, 'bayPowerState': 'Unknown'}],

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
                         'managerBays': [{'bayNumber': 1, 'status': 'OK', 'devicePresence': 'Present', 'mgmtPortStatus': 'OK'},
                                         {'bayNumber': 2, 'status': 'OK', 'devicePresence': 'Present', 'mgmtPortStatus': 'OK'}]},
                        {'name': 'MXQ708030N', 'type': 'EnclosureV7', 'enclosureType': 'SY12000', 'serialNumber': 'MXQ708030N',
                         'refreshState': 'NotRefreshing', 'state': 'Monitored',
                         'deviceBays': [{'bayNumber': 1, 'devicePresence': 'Present'}, {'bayNumber': 2, 'devicePresence': 'Present'}, {'bayNumber': 3, 'devicePresence': 'Present'},
                                        {'bayNumber': 4, 'devicePresence': 'Absent'}, {'bayNumber': 5, 'devicePresence': 'Absent'}, {'bayNumber': 6, 'devicePresence': 'Absent'},
                                        {'bayNumber': 7, 'devicePresence': 'Present'}, {'bayNumber': 8, 'devicePresence': 'Present'}, {'bayNumber': 9, 'devicePresence': 'Present'}, {'bayNumber': 10, 'devicePresence': 'Absent'}, {'bayNumber': 11, 'devicePresence': 'Absent'}, {'bayNumber': 12, 'devicePresence': 'Absent'}],
                         'interconnectBays': [{'bayNumber': 1, 'bayPowerState': 'Unknown'}, {'bayNumber': 2, 'bayPowerState': 'Unknown'}, {'bayNumber': 3, 'bayPowerState': 'Unknown'},
                                              {'bayNumber': 4, 'bayPowerState': 'Unknown'}, {'bayNumber': 5, 'bayPowerState': 'Unknown'}, {'bayNumber': 6, 'bayPowerState': 'Unknown'}],
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
                                           {'bayNumber': 2, 'status': None, 'devicePresence': 'Absent'}],
                         'managerBays': [{'bayNumber': 1, 'status': 'OK', 'devicePresence': 'Present', 'mgmtPortStatus': 'OK'},
                                         {'bayNumber': 2, 'status': 'OK', 'devicePresence': 'Present', 'mgmtPortStatus': 'OK'}]}]

expected_monitored_enclosures = [{'name': 'MXQ70700G4', 'type': 'EnclosureV7', 'enclosureType': 'SY12000', 'serialNumber': 'MXQ70700G4',
                                  'refreshState': 'NotRefreshing', 'state': 'Monitored',
                                  'deviceBays': [{'bayNumber': 1, 'devicePresence': 'Present'}, {'bayNumber': 2, 'devicePresence': 'Present'}, {'bayNumber': 3, 'devicePresence': 'Present'},
                                                 {'bayNumber': 4, 'devicePresence': 'Absent'}, {'bayNumber': 5, 'devicePresence': 'Absent'}, {'bayNumber': 6, 'devicePresence': 'Absent'},
                                                 {'bayNumber': 7, 'devicePresence': 'Present'}, {'bayNumber': 8, 'devicePresence': 'Present'}, {'bayNumber': 9, 'devicePresence': 'Present'}, {'bayNumber': 10, 'devicePresence': 'Absent'}, {'bayNumber': 11, 'devicePresence': 'Absent'}, {'bayNumber': 12, 'devicePresence': 'Absent'}],
                                  'interconnectBays': [{'bayNumber': 1, 'bayPowerState': 'Unknown'}, {'bayNumber': 2, 'bayPowerState': 'Unknown'}, {'bayNumber': 3, 'bayPowerState': 'Unknown'},
                                                       {'bayNumber': 4, 'bayPowerState': 'Unknown'}, {'bayNumber': 5, 'bayPowerState': 'Unknown'}, {'bayNumber': 6, 'bayPowerState': 'Unknown'}],
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
                                 {'name': 'MXQ708021V', 'type': 'EnclosureV7', 'enclosureType': 'SY12000', 'serialNumber': 'MXQ708021V',
                                  'refreshState': 'NotRefreshing', 'state': 'Monitored',
                                  'deviceBays': [{'bayNumber': 1, 'devicePresence': 'Present'}, {'bayNumber': 2, 'devicePresence': 'Present'}, {'bayNumber': 3, 'devicePresence': 'Present'},
                                                 {'bayNumber': 4, 'devicePresence': 'Present'}, {'bayNumber': 5, 'devicePresence': 'Present'}, {'bayNumber': 6, 'devicePresence': 'Absent'},
                                                 {'bayNumber': 7, 'devicePresence': 'Present'}, {'bayNumber': 8, 'devicePresence': 'Present'}, {'bayNumber': 9, 'devicePresence': 'Present'}, {'bayNumber': 10, 'devicePresence': 'Absent'}, {'bayNumber': 11, 'devicePresence': 'Subsumed'}, {'bayNumber': 12, 'devicePresence': 'Absent'}],
                                  'interconnectBays': [{'bayNumber': 1, 'bayPowerState': 'Unknown'}, {'bayNumber': 2, 'bayPowerState': 'Unknown'}, {'bayNumber': 3, 'bayPowerState': 'Unknown'},
                                                       {'bayNumber': 4, 'bayPowerState': 'Unknown'}, {'bayNumber': 5, 'bayPowerState': 'Unknown'}, {'bayNumber': 6, 'bayPowerState': 'Unknown'}],

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
                                  'managerBays': [{'bayNumber': 1, 'status': 'OK', 'devicePresence': 'Present', 'mgmtPortStatus': 'OK'},
                                                  {'bayNumber': 2, 'status': 'OK', 'devicePresence': 'Present', 'mgmtPortStatus': 'OK'}]},
                                 {'name': 'MXQ708030N', 'type': 'EnclosureV7', 'enclosureType': 'SY12000', 'serialNumber': 'MXQ708030N',
                                  'refreshState': 'NotRefreshing', 'state': 'Monitored',
                                  'deviceBays': [{'bayNumber': 1, 'devicePresence': 'Present'}, {'bayNumber': 2, 'devicePresence': 'Present'}, {'bayNumber': 3, 'devicePresence': 'Present'},
                                                 {'bayNumber': 4, 'devicePresence': 'Absent'}, {'bayNumber': 5, 'devicePresence': 'Absent'}, {'bayNumber': 6, 'devicePresence': 'Absent'},
                                                 {'bayNumber': 7, 'devicePresence': 'Present'}, {'bayNumber': 8, 'devicePresence': 'Present'}, {'bayNumber': 9, 'devicePresence': 'Present'}, {'bayNumber': 10, 'devicePresence': 'Absent'}, {'bayNumber': 11, 'devicePresence': 'Absent'}, {'bayNumber': 12, 'devicePresence': 'Absent'}],
                                  'interconnectBays': [{'bayNumber': 1, 'bayPowerState': 'Unknown'}, {'bayNumber': 2, 'bayPowerState': 'Unknown'}, {'bayNumber': 3, 'bayPowerState': 'Unknown'},
                                                       {'bayNumber': 4, 'bayPowerState': 'Unknown'}, {'bayNumber': 5, 'bayPowerState': 'Unknown'}, {'bayNumber': 6, 'bayPowerState': 'Unknown'}],
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
                                                    {'bayNumber': 2, 'status': None, 'devicePresence': 'Absent'}],
                                  'managerBays': [{'bayNumber': 1, 'status': 'OK', 'devicePresence': 'Present', 'mgmtPortStatus': 'OK'},
                                                  {'bayNumber': 2, 'status': 'OK', 'devicePresence': 'Present', 'mgmtPortStatus': 'OK'}]}]

configured_enclosures = [{'name': 'MXQ70700G4', 'type': 'EnclosureV7', 'enclosureType': 'SY12000', 'serialNumber': 'MXQ70700G4',
                          'refreshState': 'NotRefreshing', 'state': 'Configured',
                          'deviceBays': [{'bayNumber': 1, 'devicePresence': 'Present'}, {'bayNumber': 2, 'devicePresence': 'Present'}, {'bayNumber': 3, 'devicePresence': 'Present'},
                                         {'bayNumber': 4, 'devicePresence': 'Absent'}, {'bayNumber': 5, 'devicePresence': 'Absent'}, {'bayNumber': 6, 'devicePresence': 'Absent'},
                                         {'bayNumber': 7, 'devicePresence': 'Present'}, {'bayNumber': 8, 'devicePresence': 'Present'}, {'bayNumber': 9, 'devicePresence': 'Present'}, {'bayNumber': 10, 'devicePresence': 'Absent'}, {'bayNumber': 11, 'devicePresence': 'Absent'}, {'bayNumber': 12, 'devicePresence': 'Absent'}],
                          'interconnectBays': [{'bayNumber': 1, 'bayPowerState': 'Unknown'}, {'bayNumber': 2, 'bayPowerState': 'Unknown'}, {'bayNumber': 3, 'bayPowerState': 'Unknown'},
                                               {'bayNumber': 4, 'bayPowerState': 'Unknown'}, {'bayNumber': 5, 'bayPowerState': 'Unknown'}, {'bayNumber': 6, 'bayPowerState': 'Unknown'}],
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
                         {'name': 'MXQ708021V', 'type': 'EnclosureV7', 'enclosureType': 'SY12000', 'serialNumber': 'MXQ708021V',
                          'refreshState': 'NotRefreshing', 'state': 'Configured',
                          'deviceBays': [{'bayNumber': 1, 'devicePresence': 'Present'}, {'bayNumber': 2, 'devicePresence': 'Present'}, {'bayNumber': 3, 'devicePresence': 'Present'},
                                         {'bayNumber': 4, 'devicePresence': 'Present'}, {'bayNumber': 5, 'devicePresence': 'Present'}, {'bayNumber': 6, 'devicePresence': 'Absent'},
                                         {'bayNumber': 7, 'devicePresence': 'Present'}, {'bayNumber': 8, 'devicePresence': 'Present'}, {'bayNumber': 9, 'devicePresence': 'Present'}, {'bayNumber': 10, 'devicePresence': 'Absent'}, {'bayNumber': 11, 'devicePresence': 'Subsumed'}, {'bayNumber': 12, 'devicePresence': 'Absent'}],
                          'interconnectBays': [{'bayNumber': 1, 'bayPowerState': 'Unknown'}, {'bayNumber': 2, 'bayPowerState': 'Unknown'}, {'bayNumber': 3, 'bayPowerState': 'Unknown'},
                                               {'bayNumber': 4, 'bayPowerState': 'Unknown'}, {'bayNumber': 5, 'bayPowerState': 'Unknown'}, {'bayNumber': 6, 'bayPowerState': 'Unknown'}],

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
                          'managerBays': [{'bayNumber': 1, 'status': 'OK', 'devicePresence': 'Present', 'mgmtPortStatus': 'OK'},
                                          {'bayNumber': 2, 'status': 'OK', 'devicePresence': 'Present', 'mgmtPortStatus': 'OK'}]},
                         {'name': 'MXQ708030N', 'type': 'EnclosureV7', 'enclosureType': 'SY12000', 'serialNumber': 'MXQ708030N',
                          'refreshState': 'NotRefreshing', 'state': 'Configured',
                          'deviceBays': [{'bayNumber': 1, 'devicePresence': 'Present'}, {'bayNumber': 2, 'devicePresence': 'Present'}, {'bayNumber': 3, 'devicePresence': 'Present'},
                                         {'bayNumber': 4, 'devicePresence': 'Absent'}, {'bayNumber': 5, 'devicePresence': 'Absent'}, {'bayNumber': 6, 'devicePresence': 'Absent'},
                                         {'bayNumber': 7, 'devicePresence': 'Present'}, {'bayNumber': 8, 'devicePresence': 'Present'}, {'bayNumber': 9, 'devicePresence': 'Present'}, {'bayNumber': 10, 'devicePresence': 'Absent'}, {'bayNumber': 11, 'devicePresence': 'Absent'}, {'bayNumber': 12, 'devicePresence': 'Absent'}],
                          'interconnectBays': [{'bayNumber': 1, 'bayPowerState': 'Unknown'}, {'bayNumber': 2, 'bayPowerState': 'Unknown'}, {'bayNumber': 3, 'bayPowerState': 'Unknown'},
                                               {'bayNumber': 4, 'bayPowerState': 'Unknown'}, {'bayNumber': 5, 'bayPowerState': 'Unknown'}, {'bayNumber': 6, 'bayPowerState': 'Unknown'}],
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
                                            {'bayNumber': 2, 'status': None, 'devicePresence': 'Absent'}],
                          'managerBays': [{'bayNumber': 1, 'status': 'OK', 'devicePresence': 'Present', 'mgmtPortStatus': 'OK'},
                                          {'bayNumber': 2, 'status': 'OK', 'devicePresence': 'Present', 'mgmtPortStatus': 'OK'}]}]

expected_configured_enclosures = [{'name': 'MXQ70700G4', 'type': 'EnclosureV7', 'enclosureType': 'SY12000', 'serialNumber': 'MXQ70700G4',
                                   'refreshState': 'NotRefreshing', 'state': 'Configured',
                                   'deviceBays': [{'bayNumber': 1, 'devicePresence': 'Present'}, {'bayNumber': 2, 'devicePresence': 'Present'}, {'bayNumber': 3, 'devicePresence': 'Present'},
                                                  {'bayNumber': 4, 'devicePresence': 'Absent'}, {'bayNumber': 5, 'devicePresence': 'Absent'}, {'bayNumber': 6, 'devicePresence': 'Absent'},
                                                  {'bayNumber': 7, 'devicePresence': 'Present'}, {'bayNumber': 8, 'devicePresence': 'Present'}, {'bayNumber': 9, 'devicePresence': 'Present'}, {'bayNumber': 10, 'devicePresence': 'Absent'}, {'bayNumber': 11, 'devicePresence': 'Absent'}, {'bayNumber': 12, 'devicePresence': 'Absent'}],
                                   'interconnectBays': [{'bayNumber': 1, 'bayPowerState': 'Unknown'}, {'bayNumber': 2, 'bayPowerState': 'Unknown'}, {'bayNumber': 3, 'bayPowerState': 'Unknown'},
                                                        {'bayNumber': 4, 'bayPowerState': 'Unknown'}, {'bayNumber': 5, 'bayPowerState': 'Unknown'}, {'bayNumber': 6, 'bayPowerState': 'Unknown'}],
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
                                                       {'bayNumber': 5, 'status': 'OK', 'devicePresence': 'Present'}],

                                   'applianceBays': [{'bayNumber': 1, 'status': 'OK', 'devicePresence': 'Present'},
                                                     {'bayNumber': 2, 'status': None, 'devicePresence': 'Absent'}],
                                   'managerBays': [{'bayNumber': 1, 'status': 'OK', 'devicePresence': 'Present', 'mgmtPortStatus': 'OK'},
                                                   {'bayNumber': 2, 'status': 'OK', 'devicePresence': 'Present', 'mgmtPortStatus': 'OK'}]},
                                  {'name': 'MXQ708021V', 'type': 'EnclosureV7', 'enclosureType': 'SY12000', 'serialNumber': 'MXQ708021V',
                                   'refreshState': 'NotRefreshing', 'state': 'Configured',
                                   'deviceBays': [{'bayNumber': 1, 'devicePresence': 'Present'}, {'bayNumber': 2, 'devicePresence': 'Present'}, {'bayNumber': 3, 'devicePresence': 'Present'},
                                                  {'bayNumber': 4, 'devicePresence': 'Present'}, {'bayNumber': 5, 'devicePresence': 'Present'}, {'bayNumber': 6, 'devicePresence': 'Absent'},
                                                  {'bayNumber': 7, 'devicePresence': 'Present'}, {'bayNumber': 8, 'devicePresence': 'Present'}, {'bayNumber': 9, 'devicePresence': 'Present'}, {'bayNumber': 10, 'devicePresence': 'Absent'}, {'bayNumber': 11, 'devicePresence': 'Subsumed'}, {'bayNumber': 12, 'devicePresence': 'Absent'}],
                                   'interconnectBays': [{'bayNumber': 1, 'bayPowerState': 'Unknown'}, {'bayNumber': 2, 'bayPowerState': 'Unknown'}, {'bayNumber': 3, 'bayPowerState': 'Unknown'},
                                                        {'bayNumber': 4, 'bayPowerState': 'Unknown'}, {'bayNumber': 5, 'bayPowerState': 'Unknown'}, {'bayNumber': 6, 'bayPowerState': 'Unknown'}],

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
                                                       {'bayNumber': 5, 'status': 'OK', 'devicePresence': 'Present'}],

                                   'applianceBays': [{'bayNumber': 1, 'status': None, 'devicePresence': 'Absent'},
                                                     {'bayNumber': 2, 'status': 'OK', 'devicePresence': 'Present'}],
                                   'managerBays': [{'bayNumber': 1, 'status': 'OK', 'devicePresence': 'Present', 'mgmtPortStatus': 'OK'},
                                                   {'bayNumber': 2, 'status': 'OK', 'devicePresence': 'Present', 'mgmtPortStatus': 'OK'}]},
                                  {'name': 'MXQ708030N', 'type': 'EnclosureV7', 'enclosureType': 'SY12000', 'serialNumber': 'MXQ708030N',
                                   'refreshState': 'NotRefreshing', 'state': 'Configured',
                                   'deviceBays': [{'bayNumber': 1, 'devicePresence': 'Present'}, {'bayNumber': 2, 'devicePresence': 'Present'}, {'bayNumber': 3, 'devicePresence': 'Present'},
                                                  {'bayNumber': 4, 'devicePresence': 'Absent'}, {'bayNumber': 5, 'devicePresence': 'Absent'}, {'bayNumber': 6, 'devicePresence': 'Absent'},
                                                  {'bayNumber': 7, 'devicePresence': 'Present'}, {'bayNumber': 8, 'devicePresence': 'Present'}, {'bayNumber': 9, 'devicePresence': 'Present'}, {'bayNumber': 10, 'devicePresence': 'Absent'}, {'bayNumber': 11, 'devicePresence': 'Absent'}, {'bayNumber': 12, 'devicePresence': 'Absent'}],
                                   'interconnectBays': [{'bayNumber': 1, 'bayPowerState': 'Unknown'}, {'bayNumber': 2, 'bayPowerState': 'Unknown'}, {'bayNumber': 3, 'bayPowerState': 'Unknown'},
                                                        {'bayNumber': 4, 'bayPowerState': 'Unknown'}, {'bayNumber': 5, 'bayPowerState': 'Unknown'}, {'bayNumber': 6, 'bayPowerState': 'Unknown'}],
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
                                                     {'bayNumber': 2, 'status': None, 'devicePresence': 'Absent'}],
                                   'managerBays': [{'bayNumber': 1, 'status': 'OK', 'devicePresence': 'Present', 'mgmtPortStatus': 'OK'},
                                                   {'bayNumber': 2, 'status': 'OK', 'devicePresence': 'Present', 'mgmtPortStatus': 'OK'}]}]

support_dump = [{'errorCode': 'CI', 'encrypt': True}]

le_support_dump = [{'name': 'DCS_LE', 'errorCode': 'LESD1', 'encrypt': True, 'excludeApplianceDump': False}]

transformation_sp = [{'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ70700G4, bay 9',
                      'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1:3:Synergy 3820C 10/20Gb CNA', 'enclosureGroupUri': 'EG:EG_Ring',
                      'name': 'MXQ70700G4Bay1-to-Bay9', 'description': 'Created server profile from SP Transform DTO', 'affinity': 'Bay',
                      'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                      'boot': {'manageBoot': True, 'order': ['PXE']},
                      'bios': {'manageBios': True, 'overriddenSettings': [{'id': 'AdminName', 'value': 'WPST Tester1'}, {'id': 'AdminPhone', 'value': '111-111-1111'}]},
                      'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                      'sanStorage': {'volumeAttachments': [], 'sanSystemCredentials': [], 'manageSanStorage': False},
                      'connectionSettings': {'connections': [{'id': 1, 'name': 'Mezz 3:1-a', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:net10', 'functionType': 'Ethernet',
                                                              'requestedVFs': 'Auto', 'allocatedVFs': 64, 'macType': 'Physical', 'wwpnType': 'Physical', 'requestedMbps': '2500', 'allocatedMbps': 2500,
                                                              'maximumMbps': 10000, 'ipv4': None, 'boot': {'priority': 'NotBootable'}}]}}]

expected_transformation_sp = [{'type': 'ServerProfileV8',
                               'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1:3:Synergy 3820C 10/20Gb CNA',
                               'enclosureGroupUri': 'EG:EG_Ring', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                               'name': 'MXQ70700G4Bay1-to-Bay9', 'description': 'Created server profile from SP Transform DTO', 'affinity': 'Bay',
                               'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                               'boot': {'manageBoot': True, 'order': ['PXE']},
                               'bios': {'manageBios': True, 'overriddenSettings': [{'id': 'AdminName', 'value': 'WPST Tester1'}, {'id': 'AdminPhone', 'value': '111-111-1111'}]},
                               'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                               'sanStorage': {'volumeAttachments': [], 'sanSystemCredentials': [], 'manageSanStorage': False},
                               'connectionSettings': {'connections': [{'id': 1, 'name': 'Mezz 3:1-a', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:net10', 'functionType': 'Ethernet',
                                                                       'requestedVFs': 'Auto', 'allocatedVFs': 64, 'macType': 'Physical', 'wwpnType': 'Physical', 'requestedMbps': '2500', 'allocatedMbps': 2500,
                                                                       'maximumMbps': 10000, 'ipv4': None, 'boot': {'priority': 'NotBootable'}}]}}]

sp_from_transform_dto = [{'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ70700G4, bay 9',
                          'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1:3:Synergy 3820C 10/20Gb CNA', 'enclosureGroupUri': 'EG:EG_Ring',
                          'name': 'MXQ70700G4Bay1-to-Bay9', 'description': 'Created server profile from SP Transform DTO', 'affinity': 'Bay',
                          'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                          'boot': {'manageBoot': False},
                          'connectionSettings': {'connections': [{'id': 1, 'name': 'Mezz 3:1-a', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:net10', 'functionType': 'Ethernet'},
                                                                 {'id': 2, 'name': 'Mezz 3:1-b', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:net11', 'functionType': 'Ethernet'},
                                                                 {'id': 3, 'name': 'Mezz 3:1-c', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:net12', 'functionType': 'Ethernet'}]}}]

expected_sp_from_transform_dto = [{'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ70700G4, bay 9',
                                   'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1:3:Synergy 3820C 10/20Gb CNA',
                                   'enclosureGroupUri': 'EG:EG_Ring',
                                   'name': 'MXQ70700G4Bay1-to-Bay9', 'description': 'Created server profile from SP Transform DTO', 'affinity': 'Bay',
                                   'status': 'OK', 'state': 'Normal',
                                   'connectionSettings': {'connections': [{'id': 1, 'name': 'Mezz 3:1-a', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:net10', 'functionType': 'Ethernet'},
                                                                          {'id': 2, 'name': 'Mezz 3:1-b', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:net11', 'functionType': 'Ethernet'},
                                                                          {'id': 3, 'name': 'Mezz 3:1-c', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:net12', 'functionType': 'Ethernet'}]}}]


edit_sp_transform = [{'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ70700G4, bay 9',
                      'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1:3:Synergy 3820C 10/20Gb CNA', 'enclosureGroupUri': 'EG:EG_Ring',
                      'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                      'name': 'MXQ70700G4Bay1-to-Bay9', 'description': 'Created server profile from SP Transform DTO', 'affinity': 'Bay',
                      'bootMode': {'manageMode': True, 'mode': 'BIOS'},
                      'boot': {'manageBoot': True, 'order': ['PXE', 'HardDisk', 'CD', 'USB']},
                      'bios': {'manageBios': True, 'overriddenSettings': [{'id': 'AdminName', 'value': 'WPST Tester2'}, {'id': 'AdminPhone', 'value': '222-222-2222'}]},
                      'connectionSettings': {'connections': [{'id': 1, 'name': 'Mezz 3:1-a', 'portId': 'Mezz 3:1-a', 'requestedMbps': '4000', 'networkUri': 'ETH:net10', 'functionType': 'Ethernet'}]},
                      'localStorage': {'sasLogicalJBODs': [], 'controllers': []}}]

expected_edit_sp_transform = [{'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ70700G4, bay 9',
                               'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1:3:Synergy 3820C 10/20Gb CNA',
                               'enclosureGroupUri': 'EG:EG_Ring', 'serialNumberType': 'Physical',
                               'macType': 'Physical', 'wwnType': 'Physical',
                               'bootMode': {'manageMode': True, 'mode': 'BIOS'},
                               'boot': {'manageBoot': True, 'order': ['PXE', 'HardDisk', 'CD', 'USB']},
                               'bios': {'manageBios': True, 'overriddenSettings': [{'id': 'AdminName', 'value': 'WPST Tester2'}, {'id': 'AdminPhone', 'value': '222-222-2222'}]},
                               'name': 'MXQ70700G4Bay1-to-Bay9', 'description': 'Created server profile from SP Transform DTO', 'affinity': 'Bay',
                               'status': 'OK', 'state': 'Normal',
                               'connectionSettings': {'connections': [{'id': 1, 'name': 'Mezz 3:1-a', 'portId': 'Mezz 3:1-a', 'requestedMbps': '4000', 'networkUri': 'ETH:net10', 'functionType': 'Ethernet'}]},
                               'localStorage': {'sasLogicalJBODs': [], 'controllers': []}}]

spp_local_path = 'C:/SPP/Gen9Snap6_191.iso'
spp_bundle = 'Gen9Snap6_191.iso'

enclosure = [{'serialNumber': 'MXQ70700G4', 'name': 'MXQ70700G4',
              'interconnectBays': [{'bayNumber': 3, 'interconnectUri': 'IC:MXQ70700G4, interconnect 3', 'interconnectModel': 'Synergy 20Gb Interconnect Link Module', 'serialNumber': '2TV703004T', 'bayPowerState': 'Unknown', 'interconnectBayType': 'SY12000InterconnectBay'},
                                   {'bayNumber': 6, 'interconnectUri': 'IC:MXQ70700G4, interconnect 6', 'interconnectModel': 'Synergy 20Gb Interconnect Link Module', 'serialNumber': '7C970300S6', 'bayPowerState': 'Unknown', 'interconnectBayType': 'SY12000InterconnectBay'}],
              'deviceBays': [{'type': 'DeviceBayV400', 'bayNumber': 1, 'model': None, 'devicePresence': 'Present', 'profileUri': None, 'deviceUri': 'MXQ70700G4, bay 1', 'deviceBayType': 'SY12000DeviceBay', 'deviceFormFactor': 'SingleHeightSingleWide', 'category': 'device-bays'},
                             {'type': 'DeviceBayV400', 'bayNumber': 2, 'model': None, 'devicePresence': 'Present', 'profileUri': None, 'deviceUri': 'MXQ70700G4, bay 2', 'deviceBayType': 'SY12000DeviceBay', 'deviceFormFactor': 'SingleHeightSingleWide', 'category': 'device-bays'}]}]


uid_on_data = DD.update_enclosure(enclosure, 'uidState', 'on', 'UID on')
uid_off_data = DD.update_enclosure(enclosure, 'uidState', 'off', 'UID off')
em_bay1_uid_on = DD.update_enclosure(enclosure, 'managerBays/1/uidState', 'on', 'Link module 1 UID on')
em_bay2_uid_on = DD.update_enclosure(enclosure, 'managerBays/2/uidState', 'on', 'Link module 2 UID on')
em_bay1_uid_off = DD.update_enclosure(enclosure, 'managerBays/1/uidState', 'off', 'Link module 1 UID off')
em_bay2_uid_off = DD.update_enclosure(enclosure, 'managerBays/2/uidState', 'off', 'Link module 2 UID off')
dev_bay1_reset = DD.update_enclosure(enclosure, 'deviceBays/1/bayPowerState', 'Reset', 'Reset management processor')
dev_bay2_reset = DD.update_enclosure(enclosure, 'deviceBays/2/bayPowerState', 'Reset', 'Reset management processor')
efuse_bay3 = DD.update_enclosure(enclosure, 'interconnectBays/3/bayPowerState', 'E-Fuse', 'E-fuse interconnect bay 3')
efuse_bay6 = DD.update_enclosure(enclosure, 'interconnectBays/6/bayPowerState', 'E-Fuse', 'E-fuse interconnect bay 6')
efuse_bay1_blade = DD.update_enclosure(enclosure, 'deviceBays/1/bayPowerState', 'E-Fuse', 'E-fuse device bay 1')
efuse_bay2_blade = DD.update_enclosure(enclosure, 'deviceBays/2/bayPowerState', 'E-Fuse', 'E-fuse device bay 2')
failover_bay1_em = DD.update_enclosure(enclosure, 'managerBays/1/role', 'Active', 'Update')
failover_bay2_em = DD.update_enclosure(enclosure, 'managerBays/2/role', 'Active', 'Update')
efuse_em_bay1 = DD.update_enclosure(enclosure, 'managerBays/1/bayPowerState', 'E-Fuse', 'E-fuse Synergy Frame Link Module bay 1')
efuse_em_bay2 = DD.update_enclosure(enclosure, 'managerBays/2/bayPowerState', 'E-Fuse', 'E-fuse Synergy Frame Link Module bay 2')
reset_em_bay1 = DD.update_enclosure(enclosure, 'managerBays/1/bayPowerState', 'Reset', 'Reset Synergy Frame Link Module')
reset_em_bay2 = DD.update_enclosure(enclosure, 'managerBays/2/bayPowerState', 'Reset', 'Reset Synergy Frame Link Module')


server = {'name': 'MXQ70700G4, bay 2', 'uri': '/rest/server-hardware/39363238-3435-584D-5136-343530344A58'}
reset_srv_expected_msg = 'Reset iLO'
uid_srv_expected_msg = 'UID on'
uid_off_srv_expected_msg = 'UID off'

# Data for Profile tests for Enclosures 1

server_profile_raid0 = [{'name': 'enc1_bay1', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ70700G4, bay 1', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                         'connectionSettings': {'connections': []},
                         'boot': {'manageBoot': True, 'order': ['PXE']},
                         'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                         'localStorage': {'controllers': [{u'deviceSlot': u'Embedded', u'initialize': True, u'mode': u'RAID', u'importConfiguration': False, u'logicalDrives': [{u'name': u'LD0', u'bootable': False, u'raidLevel': u'RAID0', u'sasLogicalJBODId': None, u'driveTechnology': u'SasHdd', u'numPhysicalDrives': 1, u'driveNumber': None}]}],
                                          'sasLogicalJBODs': []}, }]


expected_server_profile_raid0 = [{'name': 'enc1_bay1', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ70700G4, bay 1', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                  'connectionSettings': {'connections': []},
                                  'boot': {'manageBoot': True, 'order': ['PXE']},
                                  'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                                  'localStorage': {'controllers': [{u'deviceSlot': u'Embedded', u'initialize': False, u'mode': u'RAID', u'importConfiguration': False, u'logicalDrives': [{u'name': u'LD0', u'bootable': False, u'raidLevel': u'RAID0', u'sasLogicalJBODId': None, u'driveTechnology': u'SasHdd', u'numPhysicalDrives': 1, u'driveNumber': None}]}],
                                                   'sasLogicalJBODs': []},
                                  'status': 'OK'}]

server_profile_hba = [{'name': 'enc1_bay1', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ70700G4, bay 1', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                       'connectionSettings': {'connections': []},
                       'boot': {'manageBoot': True, 'order': ['PXE']},
                       'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                       'localStorage': {'controllers': [{u'deviceSlot': u'Embedded', u'initialize': True, u'mode': u'HBA', u'importConfiguration': False}],
                                        'sasLogicalJBODs': []}, }]

expected_server_profile_hba = [{'name': 'enc1_bay1', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ70700G4, bay 1', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                'connectionSettings': {'connections': []},
                                'boot': {'manageBoot': True, 'order': ['PXE']},
                                'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                                'localStorage': {'controllers': [{u'deviceSlot': u'Embedded', u'initialize': False, u'mode': u'HBA', u'importConfiguration': False}],
                                                 'sasLogicalJBODs': []},
                                'status': 'OK'}]


server_profile_raid1 = [{'name': 'enc1_bay1', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ70700G4, bay 1', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                         'connectionSettings': {'connections': []},
                         'boot': {'manageBoot': True, 'order': ['PXE']},
                         'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                         'localStorage': {'controllers': [{u'deviceSlot': u'Embedded', u'initialize': True, u'mode': u'RAID', u'importConfiguration': False, u'logicalDrives': [{u'name': u'LD1', u'bootable': False, u'raidLevel': u'RAID0', u'sasLogicalJBODId': None, u'driveTechnology': u'SasHdd', u'numPhysicalDrives': 1, u'driveNumber': None}]}],
                                          'sasLogicalJBODs': []}, }]

expected_server_profile_raid1 = [{'name': 'enc1_bay1', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ70700G4, bay 1', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                  'connectionSettings': {'connections': []},
                                  'boot': {'manageBoot': True, 'order': ['PXE']},
                                  'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                                  'localStorage': {'controllers': [{u'deviceSlot': u'Embedded', u'initialize': False, u'mode': u'RAID', u'importConfiguration': False, u'logicalDrives': [{u'name': u'LD1', u'bootable': False, u'raidLevel': u'RAID0', u'sasLogicalJBODId': None, u'driveTechnology': u'SasHdd', u'numPhysicalDrives': 1, u'driveNumber': None}]}],
                                                   'sasLogicalJBODs': []},
                                  'status': 'OK'}]

server_profile_raid_no_initialize = [{'name': 'enc1_bay1', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ70700G4, bay 1', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                      'connectionSettings': {'connections': []},
                                      'boot': {'manageBoot': True, 'order': ['PXE']},
                                      'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                                      'localStorage': {'controllers': [{u'deviceSlot': u'Embedded', u'initialize': False, u'mode': u'RAID', u'importConfiguration': False}],
                                                       'sasLogicalJBODs': []},
                                      }]

expected_server_profile_raid_no_initialize = [{'name': 'enc1_bay1', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ70700G4, bay 1', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                               'connectionSettings': {'connections': []},
                                               'boot': {'manageBoot': True, 'order': ['PXE']},
                                               'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                                               'localStorage': {'controllers': [{u'deviceSlot': u'Embedded', u'initialize': False, u'mode': u'RAID', u'importConfiguration': False}],
                                                                'sasLogicalJBODs': []},
                                               'status': 'OK'}]

server_profile_templates = [{'name': 'Enclosure1Template', 'type': 'ServerProfileTemplateV4', 'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1:3:Synergy 3820C 10/20Gb CNA', 'enclosureGroupUri': 'EG:EG_Ring', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 1, 'name': 'ETH', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2000', 'networkUri': 'ETH:net10'}]}, },
                            {'name': 'Enc1 Bios and local storage with connections', 'type': 'ServerProfileTemplateV4', 'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1:3:Synergy 3820C 10/20Gb CNA', 'enclosureGroupUri': 'EG:EG_Ring', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 1, 'name': 'ETH', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2000', 'networkUri': 'ETH:net10'}]},
                             'bios': {'manageBios': True,
                                      'overriddenSettings': [{u'id': u'AdminName', u'value': u'Sylvester McSweggins'}]},
                             'localStorage': {'sasLogicalJBODs': [],
                                              'controllers': [{u'deviceSlot': u'Embedded', u'initialize': True, u'mode': u'RAID', u'logicalDrives': [{u'name': u'raid', u'bootable': False, u'raidLevel': u'RAID0', u'sasLogicalJBODId': None, u'driveTechnology': None, u'numPhysicalDrives': 1}]}]}}]


expected_server_profile_templates = [{'name': 'Enclosure1Template', 'uri': 'SPT:Enclosure1Template', 'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1:3:Synergy 3820C 10/20Gb CNA', 'enclosureGroupUri': 'EG:EG_Ring', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'affinity': 'Bay',
                                      'connectionSettings': {'manageConnections': True,
                                                             'connections': [{'id': 1, 'name': 'ETH', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2000', 'networkUri': 'ETH:net10'}]},
                                      'status': 'OK'},
                                     {'name': 'Enc1 Bios and local storage with connections', 'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1:3:Synergy 3820C 10/20Gb CNA', 'enclosureGroupUri': 'EG:EG_Ring', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'affinity': 'Bay',
                                      'connectionSettings': {'manageConnections': True,
                                                             'connections': [{'id': 1, 'name': 'ETH', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2000', 'networkUri': 'ETH:net10'}]},
                                      'bios': {'manageBios': True,
                                               'overriddenSettings': [{u'id': u'AdminName', u'value': u'Sylvester McSweggins'}]},
                                      'localStorage': {'sasLogicalJBODs': [],
                                                       'controllers': [{u'deviceSlot': u'Embedded', u'initialize': True, u'mode': u'RAID', u'logicalDrives': [{u'name': u'raid', u'bootable': False, u'raidLevel': u'RAID0', u'sasLogicalJBODId': None, u'driveTechnology': None, u'numPhysicalDrives': 1}]}]},
                                      'status': 'OK'}]

server_profiles_from_spt = [{'name': 'wpst-tbird1-Bay1', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ70700G4, bay 1', 'serialNumberType': 'Virtual',
                             'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1:3:Synergy 3820C 10/20Gb CNA', 'serverProfileTemplateUri': 'SPT:Enclosure1Template'}]

expected_server_profiles_from_spt = [{'status': 'OK', 'type': 'ServerProfileV8', 'name': 'wpst-tbird1-Bay1', 'serverHardwareUri': 'SH:MXQ70700G4, bay 1', 'serialNumberType': 'Virtual',
                                      'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1:3:Synergy 3820C 10/20Gb CNA', 'serverProfileTemplateUri': 'SPT:Enclosure1Template'}]

server_profile_many_conn = [{'name': 'enc1_bay2_fail', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ70700G4, bay 2', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': 'Should fail, too many connections.', 'affinity': 'Bay',
                             'connectionSettings': {'connections': [{'id': 1, 'name': 'net10', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net10', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:01', 'boot': {'priority': 'Primary'}},
                                                                    {'id': 2, 'name': 'net11', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net11', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:02', 'requestedVFs': '3'},
                                                                    {'id': 3, 'name': 'net12', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net12', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:03'},
                                                                    {'id': 4, 'name': 'net13', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net13', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:04'},
                                                                    {'id': 5, 'name': 'net14', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net14', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:05', 'requestedVFs': '3'},
                                                                    {'id': 6, 'name': 'net15', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net15', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:06'},
                                                                    {'id': 7, 'name': 'net16', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net16', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:07'},
                                                                    {'id': 8, 'name': 'net17', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net17', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:08', 'requestedVFs': '3'},
                                                                    {'id': 9, 'name': 'net18', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net300', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:09'},
                                                                    {'id': 10, 'name': 'net19', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net17', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:10'},
                                                                    {'id': 11, 'name': 'net20', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net17', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:11'},
                                                                    {'id': 12, 'name': 'net21', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net17', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:12'},
                                                                    {'id': 13, 'name': 'net22', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net17', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:13'},
                                                                    {'id': 14, 'name': 'net23', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net17', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:14'},
                                                                    {'id': 15, 'name': 'net24', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net17', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:15'},
                                                                    {'id': 16, 'name': 'net25', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net17', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:10'},
                                                                    {'id': 17, 'name': 'net26', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net17', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:11'},
                                                                    {'id': 18, 'name': 'net27', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net17', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:12'},
                                                                    {'id': 19, 'name': 'net28', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net17', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:13'},
                                                                    {'id': 20, 'name': 'net29', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net17', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:14'},
                                                                    {'id': 21, 'name': 'net30', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net17', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:09'},
                                                                    {'id': 22, 'name': 'net31', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net17', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:10'},
                                                                    {'id': 23, 'name': 'net32', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net17', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:11'},
                                                                    {'id': 24, 'name': 'net33', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net17', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:12'},
                                                                    {'id': 25, 'name': 'net34', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net17', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:13'},
                                                                    {'id': 26, 'name': 'net35', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net17', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:14'}]},
                             'boot': {'manageBoot': True, 'order': ['PXE']},
                             'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'}}]
errormessage = 'No additional port available to support network'

server_profile_diff_conn = [{'name': 'enc1_bay2', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ70700G4, bay 2', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'affinity': 'Bay',
                             'boot': {'manageBoot': True, 'order': ['PXE']},
                             'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                             'connectionSettings': {'connections': [{'id': 1, 'name': 'net14', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net14', 'boot': {'priority': 'Primary'}},
                                                                    {'id': 2, 'name': 'net15', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net15'},
                                                                    {'id': 3, 'name': 'net16', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net16'},
                                                                    {'id': 4, 'name': 'net17', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net17'}]}}]


expected_server_profile_diff_conn = [{'name': 'enc1_bay2', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ70700G4, bay 2', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'affinity': 'Bay',
                                      'boot': {'manageBoot': True, 'order': ['PXE']},
                                      'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                      'connectionSettings': {'connections': [{'id': 1, 'name': 'net14', 'functionType': 'Ethernet', 'networkUri': 'ETH:net14', 'boot': {'priority': 'Primary'}},
                                                                             {'id': 2, 'name': 'net15', 'functionType': 'Ethernet', 'networkUri': 'ETH:net15'},
                                                                             {'id': 3, 'name': 'net16', 'functionType': 'Ethernet', 'networkUri': 'ETH:net16'},
                                                                             {'id': 4, 'name': 'net17', 'functionType': 'Ethernet', 'networkUri': 'ETH:net17'}]},
                                      'status': 'OK'}]

server_profile_three_conn = [{'name': 'enc1_bay2', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ70700G4, bay 2', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'affinity': 'Bay',
                              'boot': {'manageBoot': True, 'order': ['PXE']},
                              'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                              'connectionSettings': {'connections': [{'id': 1, 'name': 'net10', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net10', 'boot': {'priority': 'Primary'}},
                                                                     {'id': 2, 'name': 'net11', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net11'},
                                                                     {'id': 3, 'name': 'net12', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net12'},
                                                                     {'id': 4, 'name': 'net13', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net13'}]}}]

expected_server_profile_three_conn = [{'name': 'enc1_bay2', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ70700G4, bay 2', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'affinity': 'Bay',
                                       'boot': {'manageBoot': True, 'order': ['PXE']},
                                       'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                                       'connectionSettings': {'connections': [{'id': 1, 'name': 'net14', 'functionType': 'Ethernet', 'networkUri': 'ETH:net10', 'boot': {'priority': 'Primary'}},
                                                                              {'id': 2, 'name': 'net15', 'functionType': 'Ethernet', 'networkUri': 'ETH:net11'},
                                                                              {'id': 3, 'name': 'net16', 'functionType': 'Ethernet', 'networkUri': 'ETH:net12'},
                                                                              {'id': 4, 'name': 'net17', 'functionType': 'Ethernet', 'networkUri': 'ETH:net13'}]},
                                       'status': 'OK'}]

# Data for Profile tests for Enclosures 2
server_profile_templates_enc2 = [{'name': 'Enclosure2Template', 'type': 'ServerProfileTemplateV4', 'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1:3:Synergy 3820C 10/20Gb CNA', 'enclosureGroupUri': 'EG:EG_Ring', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'affinity': 'Bay',
                                  'connectionSettings': {'manageConnections': True,
                                                         'connections': [{'id': 1, 'name': 'ETH', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2000', 'networkUri': 'ETH:net10'}]}, },
                                 {'name': 'Enc2 Bios and local storage with connections', 'type': 'ServerProfileTemplateV4', 'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1:3:Synergy 3820C 10/20Gb CNA', 'enclosureGroupUri': 'EG:EG_Ring', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'affinity': 'Bay',
                                  'connectionSettings': {'manageConnections': True,
                                                         'connections': [{'id': 1, 'name': 'ETH', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2000', 'networkUri': 'ETH:net10'}]},
                                  'bios': {'manageBios': True,
                                           'overriddenSettings': [{u'id': u'AdminName', u'value': u'Sylvester McSweggins'}]},
                                  'localStorage': {'sasLogicalJBODs': [],
                                                   'controllers': [{u'deviceSlot': u'Embedded', u'initialize': True, u'mode': u'RAID', u'logicalDrives': [{u'name': u'raid', u'bootable': False, u'raidLevel': u'RAID0', u'sasLogicalJBODId': None, u'driveTechnology': None, u'numPhysicalDrives': 1}]}]}}]


expected_server_profile_templates_enc2 = [{'name': 'Enclosure2Template', 'uri': 'SPT:Enclosure2Template', 'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1:3:Synergy 3820C 10/20Gb CNA', 'enclosureGroupUri': 'EG:EG_Ring', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'affinity': 'Bay',
                                           'connectionSettings': {'manageConnections': True,
                                                                  'connections': [{'id': 1, 'name': 'ETH', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2000', 'networkUri': 'ETH:net10'}]},
                                           'status': 'OK'},
                                          {'name': 'Enc2 Bios and local storage with connections', 'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1:3:Synergy 3820C 10/20Gb CNA', 'enclosureGroupUri': 'EG:EG_Ring', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'affinity': 'Bay',
                                           'connectionSettings': {'manageConnections': True,
                                                                  'connections': [{'id': 1, 'name': 'ETH', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2000', 'networkUri': 'ETH:net10'}]},
                                           'bios': {'manageBios': True,
                                                    'overriddenSettings': [{u'id': u'AdminName', u'value': u'Sylvester McSweggins'}]},
                                           'localStorage': {'sasLogicalJBODs': [],
                                                            'controllers': [{u'deviceSlot': u'Embedded', u'initialize': True, u'mode': u'RAID', u'logicalDrives': [{u'name': u'raid', u'bootable': False, u'raidLevel': u'RAID0', u'sasLogicalJBODId': None, u'driveTechnology': None, u'numPhysicalDrives': 1}]}]},
                                           'status': 'OK'}]

server_profiles_from_spt_enc2 = [{'name': 'wpst-tbird2-Bay1', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ708021V, bay 1', 'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1:3:Synergy 3820C 10/20Gb CNA',
                                  'serialNumberType': 'Virtual', 'serverProfileTemplateUri': 'SPT:Enclosure2Template'}]

expected_server_profiles_from_spt_enc2 = [{'name': 'wpst-tbird2-Bay1', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ708021V, bay 1', 'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1:3:Synergy 3820C 10/20Gb CNA',
                                           'serialNumberType': 'Virtual', 'serverProfileTemplateUri': 'SPT:Enclosure2Template', 'status': 'OK'}]

server_profile_raid0_enc2 = [{'name': 'enc2_bay1', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ708021V, bay 1', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                              'connectionSettings': {'connections': []},
                              'boot': {'manageBoot': True, 'order': ['PXE']},
                              'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                              'localStorage': {'controllers': [{u'deviceSlot': u'Embedded', u'initialize': True, u'mode': u'RAID', u'importConfiguration': False, u'logicalDrives': [{u'name': u'LD0', u'bootable': False, u'raidLevel': u'RAID0', u'sasLogicalJBODId': None, u'driveTechnology': u'SasHdd', u'numPhysicalDrives': 1, u'driveNumber': None}]}],
                                               'sasLogicalJBODs': []}, }]

expected_server_profile_raid0_enc2 = [{'name': 'enc2_bay1', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ708021V, bay 1', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                       'connectionSettings': {'connections': []},
                                       'boot': {'manageBoot': True, 'order': ['PXE']},
                                       'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                                       'localStorage': {'controllers': [{u'deviceSlot': u'Embedded', u'initialize': False, u'mode': u'RAID', u'importConfiguration': False, u'logicalDrives': [{u'name': u'LD0', u'bootable': False, u'raidLevel': u'RAID0', u'sasLogicalJBODId': None, u'driveTechnology': u'SasHdd', u'numPhysicalDrives': 1, u'driveNumber': None}]}],
                                                        'sasLogicalJBODs': []},
                                       'status': 'OK'}]

server_profile_hba_enc2 = [{'name': 'enc2_bay1', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ708021V, bay 1', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                            'connectionSettings': {'connections': []},
                            'boot': {'manageBoot': True, 'order': ['PXE']},
                            'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                            'localStorage': {'controllers': [{u'deviceSlot': u'Embedded', u'initialize': True, u'mode': u'HBA', u'importConfiguration': False}],
                                             'sasLogicalJBODs': []}, }]

expected_server_profile_hba_enc2 = [{'name': 'enc2_bay1', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ708021V, bay 1', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                     'connectionSettings': {'connections': []},
                                     'boot': {'manageBoot': True, 'order': ['PXE']},
                                     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                                     'localStorage': {'controllers': [{u'deviceSlot': u'Embedded', u'initialize': False, u'mode': u'HBA', u'importConfiguration': False}],
                                                      'sasLogicalJBODs': []},
                                     'status': 'OK'}]


server_profile_raid1_enc2 = [{'name': 'enc2_bay1', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ708021V, bay 1', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                              'connectionSettings': {'connections': []},
                              'boot': {'manageBoot': True, 'order': ['PXE']},
                              'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                              'localStorage': {'controllers': [{u'deviceSlot': u'Embedded', u'initialize': True, u'mode': u'RAID', u'importConfiguration': False, u'logicalDrives': [{u'name': u'LD1', u'bootable': False, u'raidLevel': u'RAID0', u'sasLogicalJBODId': None, u'driveTechnology': u'SasHdd', u'numPhysicalDrives': 1, u'driveNumber': None}]}],
                                               'sasLogicalJBODs': []}, }]

expected_server_profile_raid1_enc2 = [{'name': 'enc2_bay1', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ708021V, bay 1', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                       'connectionSettings': {'connections': []},
                                       'boot': {'manageBoot': True, 'order': ['PXE']},
                                       'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                                       'localStorage': {'controllers': [{u'deviceSlot': u'Embedded', u'initialize': False, u'mode': u'RAID', u'importConfiguration': False, u'logicalDrives': [{u'name': u'LD1', u'bootable': False, u'raidLevel': u'RAID0', u'sasLogicalJBODId': None, u'driveTechnology': u'SasHdd', u'numPhysicalDrives': 1, u'driveNumber': None}]}],
                                                        'sasLogicalJBODs': []}, 'status': 'OK'}]

server_profile_raid_no_initialize_enc2 = [{'name': 'enc2_bay1', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ708021V, bay 1', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                           'connectionSettings': {'connections': []},
                                           'boot': {'manageBoot': True, 'order': ['PXE']},
                                           'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                                           'localStorage': {'controllers': [{u'deviceSlot': u'Embedded', u'initialize': False, u'mode': u'RAID', u'importConfiguration': False}],
                                                            'sasLogicalJBODs': []}, }]

expected_server_profile_raid_no_initialize_enc2 = [{'name': 'enc2_bay1', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ708021V, bay 1', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                                    'connectionSettings': {'connections': []},
                                                    'boot': {'manageBoot': True, 'order': ['PXE']},
                                                    'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                                                    'localStorage': {'controllers': [{u'deviceSlot': u'Embedded', u'initialize': False, u'mode': u'RAID', u'importConfiguration': False}],
                                                                     'sasLogicalJBODs': []},
                                                    'status': 'OK'}]

server_profile_many_conn_enc2 = [{'name': 'enc2_bay2_fail', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ708021V, bay 2', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': 'Should fail, too many connections.', 'affinity': 'Bay',
                                  'connectionSettings': {'connections': [{'id': 1, 'name': 'net10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'networkUri': 'ETH:net10', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:10', 'boot': {'priority': 'Primary'}},
                                                                         {'id': 2, 'name': 'net11', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'networkUri': 'ETH:net11', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:11', 'requestedVFs': '3'},
                                                                         {'id': 3, 'name': 'net12', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'networkUri': 'ETH:net12', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:12'},
                                                                         {'id': 4, 'name': 'net13', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'networkUri': 'ETH:net13', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:13'},
                                                                         {'id': 5, 'name': 'net14', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'networkUri': 'ETH:net14', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:14', 'requestedVFs': '3'},
                                                                         {'id': 6, 'name': 'net15', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b', 'networkUri': 'ETH:net15', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:15'},
                                                                         {'id': 7, 'name': 'net16', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'networkUri': 'ETH:net16', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:16'},
                                                                         {'id': 8, 'name': 'net17', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'networkUri': 'ETH:net17', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:17', 'requestedVFs': '3'},
                                                                         {'id': 9, 'name': 'net18', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net18', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:18'}]},
                                  'boot': {'manageBoot': True, 'order': ['PXE']},
                                  'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'}}]

server_profile_diff_conn_enc2 = [{'name': 'enc2_bay2', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ708021V, bay 2', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'affinity': 'Bay',
                                  'boot': {'manageBoot': True, 'order': ['PXE']},
                                  'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                  'connectionSettings': {'connections': [{'id': 1, 'name': 'net14', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net14', 'boot': {'priority': 'Primary'}},
                                                                         {'id': 2, 'name': 'net15', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net15'},
                                                                         {'id': 3, 'name': 'net16', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net16'},
                                                                         {'id': 4, 'name': 'net17', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net17'}]}, }]

expected_server_profile_diff_conn_enc2 = [{'name': 'enc2_bay2', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ708021V, bay 2', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'affinity': 'Bay',
                                           'boot': {'manageBoot': True, 'order': ['PXE']},
                                           'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                           'connectionSettings': {'connections': [{'id': 1, 'name': 'net14', 'functionType': 'Ethernet', 'networkUri': 'ETH:net14', 'boot': {'priority': 'Primary'}},
                                                                                  {'id': 2, 'name': 'net15', 'functionType': 'Ethernet', 'networkUri': 'ETH:net15'},
                                                                                  {'id': 3, 'name': 'net16', 'functionType': 'Ethernet', 'networkUri': 'ETH:net16'},
                                                                                  {'id': 4, 'name': 'net17', 'functionType': 'Ethernet', 'networkUri': 'ETH:net17'}]},
                                           'status': 'OK'}]

server_profile_three_conn_enc2 = [{'name': 'enc2_bay2', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ708021V, bay 2', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'affinity': 'Bay',
                                   'boot': {'manageBoot': True, 'order': ['PXE']},
                                   'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                                   'connectionSettings': {'connections': [{'id': 1, 'name': 'net10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'networkUri': 'ETH:net10', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:10', 'boot': {'priority': 'Primary'}},
                                                                          {'id': 2, 'name': 'net11', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'networkUri': 'ETH:net11', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:11', 'requestedVFs': '3'},
                                                                          {'id': 3, 'name': 'net12', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'networkUri': 'ETH:net12', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:12'},
                                                                          {'id': 4, 'name': 'net13', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'networkUri': 'ETH:net13', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:13'}]}, }]

expected_server_profile_three_conn_enc2 = [{'name': 'enc2_bay2', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ708021V, bay 2', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'affinity': 'Bay',
                                            'boot': {'manageBoot': True, 'order': ['PXE']},
                                            'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                                            'connectionSettings': {'connections': [{'id': 1, 'name': 'net10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'networkUri': 'ETH:net10', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:10', 'boot': {'priority': 'Primary'}},
                                                                                   {'id': 2, 'name': 'net11', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'networkUri': 'ETH:net11', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:11', 'requestedVFs': '3'},
                                                                                   {'id': 3, 'name': 'net12', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'networkUri': 'ETH:net12', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:12'},
                                                                                   {'id': 4, 'name': 'net13', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'networkUri': 'ETH:net13', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:13'}]},
                                            'status': 'OK'}]
# Data for Profile tests for Enclosures 3
server_profile_templates_enc3 = [{'name': 'Enclosure3Template', 'type': 'ServerProfileTemplateV4', 'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1:3:Synergy 3820C 10/20Gb CNA', 'enclosureGroupUri': 'EG:EG_Ring', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'affinity': 'Bay',
                                  'connectionSettings': {'manageConnections': True,
                                                         'connections': [{'id': 1, 'name': 'ETH', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2000', 'networkUri': 'ETH:net10'}]}, },

                                 {'name': 'Enc3 Bios and local storage with connections', 'type': 'ServerProfileTemplateV4', 'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1:3:Synergy 3820C 10/20Gb CNA', 'enclosureGroupUri': 'EG:EG_Ring', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'affinity': 'Bay',
                                  'connectionSettings': {'manageConnections': True,
                                                         'connections': [{'id': 1, 'name': 'ETH', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2000', 'networkUri': 'ETH:net10'}]},
                                  'bios': {'manageBios': True,
                                           'overriddenSettings': [{u'id': u'AdminName', u'value': u'Sylvester McSweggins'}]},
                                  'localStorage': {'sasLogicalJBODs': [],
                                                   'controllers': [{u'deviceSlot': u'Embedded', u'initialize': True, u'mode': u'RAID', u'logicalDrives': [{u'name': u'raid', u'bootable': False, u'raidLevel': u'RAID0', u'sasLogicalJBODId': None, u'driveTechnology': None, u'numPhysicalDrives': 1}]}]}}]

expected_server_profile_templates_enc3 = [{'name': 'Enclosure3Template', 'uri': 'SPT:Enclosure3Template', 'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1:3:Synergy 3820C 10/20Gb CNA', 'enclosureGroupUri': 'EG:EG_Ring', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'affinity': 'Bay',
                                           'connectionSettings': {'manageConnections': True,
                                                                  'connections': [{'id': 1, 'name': 'ETH', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2000', 'networkUri': 'ETH:net10'}]},
                                           'status': 'OK'},
                                          {'name': 'Enc3 Bios and local storage with connections', 'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1:3:Synergy 3820C 10/20Gb CNA', 'enclosureGroupUri': 'EG:EG_Ring', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'affinity': 'Bay',
                                           'connectionSettings': {'manageConnections': True,
                                                                  'connections': [{'id': 1, 'name': 'ETH', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2000', 'networkUri': 'ETH:net10'}]},
                                           'bios': {'manageBios': True,
                                                    'overriddenSettings': [{u'id': u'AdminName', u'value': u'Sylvester McSweggins'}]},
                                           'localStorage': {'sasLogicalJBODs': [],
                                                            'controllers': [{u'deviceSlot': u'Embedded', u'initialize': True, u'mode': u'RAID', u'logicalDrives': [{u'name': u'raid', u'bootable': False, u'raidLevel': u'RAID0', u'sasLogicalJBODId': None, u'driveTechnology': None, u'numPhysicalDrives': 1}]}]},
                                           'status': 'OK'}]

server_profiles_from_spt_enc3 = [{'name': 'wpst-tbird3-Bay1', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ708030N, bay 1', 'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1:3:Synergy 3820C 10/20Gb CNA',
                                  'serialNumberType': 'Virtual', 'serverProfileTemplateUri': 'SPT:Enclosure3Template'}]

expected_server_profiles_from_spt_enc3 = [{'status': 'OK', 'name': 'wpst-tbird3-Bay1', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ708030N, bay 1', 'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1:3:Synergy 3820C 10/20Gb CNA',
                                           'serialNumberType': 'Virtual', 'serverProfileTemplateUri': 'SPT:Enclosure3Template'}]

server_profile_raid0_enc3 = [{'name': 'enc3_bay1', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ708030N, bay 7', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                              'connectionSettings': {'connections': []},
                              'boot': {'manageBoot': True, 'order': ['PXE']},
                              'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                              'localStorage': {'controllers': [{u'deviceSlot': u'Embedded', u'initialize': True, u'mode': u'RAID', u'importConfiguration': False, u'logicalDrives': [{u'name': u'LD0', u'bootable': False, u'raidLevel': u'RAID0', u'sasLogicalJBODId': None, u'driveTechnology': u'SasHdd', u'numPhysicalDrives': 1, u'driveNumber': None}]}],
                                               'sasLogicalJBODs': []}, }]

expected_server_profile_raid0_enc3 = [{'name': 'enc3_bay1', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ708030N, bay 7', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                       'connectionSettings': {'connections': []},
                                       'boot': {'manageBoot': True, 'order': ['PXE']},
                                       'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                                       'localStorage': {'controllers': [{u'deviceSlot': u'Embedded', u'initialize': False, u'mode': u'RAID', u'importConfiguration': False, u'logicalDrives': [{u'name': u'LD0', u'bootable': False, u'raidLevel': u'RAID0', u'sasLogicalJBODId': None, u'driveTechnology': u'SasHdd', u'numPhysicalDrives': 1, u'driveNumber': None}]}],
                                                        'sasLogicalJBODs': []},
                                       'status': 'OK'}]

server_profile_hba_enc3 = [{'name': 'enc3_bay1', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ708030N, bay 7', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                            'connectionSettings': {'connections': []},
                            'boot': {'manageBoot': True, 'order': ['PXE']},
                            'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                            'localStorage': {'controllers': [{u'deviceSlot': u'Embedded', u'initialize': True, u'mode': u'HBA', u'importConfiguration': False}],
                                             'sasLogicalJBODs': []}, }]

expected_server_profile_hba_enc3 = [{'name': 'enc3_bay1', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ708030N, bay 7', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                     'connectionSettings': {'connections': []},
                                     'boot': {'manageBoot': True, 'order': ['PXE']},
                                     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                                     'localStorage': {'controllers': [{u'deviceSlot': u'Embedded', u'initialize': False, u'mode': u'HBA', u'importConfiguration': False}],
                                                      'sasLogicalJBODs': []},
                                     'status': 'OK'}]

server_profile_raid1_enc3 = [{'name': 'enc3_bay1', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ708030N, bay 7', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                              'connectionSettings': {'connections': []},
                              'boot': {'manageBoot': True, 'order': ['PXE']},
                              'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                              'localStorage': {'controllers': [{u'deviceSlot': u'Embedded', u'initialize': True, u'mode': u'RAID', u'importConfiguration': False, u'logicalDrives': [{u'name': u'LD1', u'bootable': False, u'raidLevel': u'RAID0', u'sasLogicalJBODId': None, u'driveTechnology': u'SasHdd', u'numPhysicalDrives': 1, u'driveNumber': None}]}],
                                               'sasLogicalJBODs': []}, }]

expected_server_profile_raid1_enc3 = [{'name': 'enc3_bay1', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ708030N, bay 7', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                       'connectionSettings': {'connections': []},
                                       'boot': {'manageBoot': True, 'order': ['PXE']},
                                       'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                                       'localStorage': {'controllers': [{u'deviceSlot': u'Embedded', u'initialize': False, u'mode': u'RAID', u'importConfiguration': False, u'logicalDrives': [{u'name': u'LD1', u'bootable': False, u'raidLevel': u'RAID0', u'sasLogicalJBODId': None, u'driveTechnology': u'SasHdd', u'numPhysicalDrives': 1, u'driveNumber': None}]}],
                                                        'sasLogicalJBODs': []},
                                       'status': 'OK'}]

server_profile_raid_no_initialize_enc3 = [{'name': 'enc3_bay1', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ708030N, bay 7', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                           'connectionSettings': {'connections': []},
                                           'boot': {'manageBoot': True, 'order': ['PXE']},
                                           'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                                           'localStorage': {'controllers': [{u'deviceSlot': u'Embedded', u'initialize': False, u'mode': u'RAID', u'importConfiguration': False}],
                                                            'sasLogicalJBODs': []}, }]

expected_server_profile_raid_no_initialize_enc3 = [{'name': 'enc3_bay1', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ708030N, bay 7', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                                    'connectionSettings': {'connections': []},
                                                    'boot': {'manageBoot': True, 'order': ['PXE']},
                                                    'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                                                    'localStorage': {'controllers': [{u'deviceSlot': u'Embedded', u'initialize': False, u'mode': u'RAID', u'importConfiguration': False}],
                                                                     'sasLogicalJBODs': []},
                                                    'status': 'OK'}]

server_profile_many_conn_enc3 = [{'name': 'enc3_bay5_fail', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ708030N, bay 3', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': 'Should fail, too many connections.', 'affinity': 'Bay',
                                  'connectionSettings': {'connections': [{'id': 1, 'name': 'net10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'networkUri': 'ETH:net10', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:01', 'boot': {'priority': 'Primary'}},
                                                                         {'id': 2, 'name': 'net11', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'networkUri': 'ETH:net11', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:02', 'requestedVFs': '3'},
                                                                         {'id': 3, 'name': 'net12', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'networkUri': 'ETH:net12', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:03'},
                                                                         {'id': 4, 'name': 'net13', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'networkUri': 'ETH:net13', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:04'},
                                                                         {'id': 5, 'name': 'net14', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'networkUri': 'ETH:net14', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:05', 'requestedVFs': '3'},
                                                                         {'id': 6, 'name': 'net15', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b', 'networkUri': 'ETH:net15', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:06'},
                                                                         {'id': 7, 'name': 'net16', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'networkUri': 'ETH:net16', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:07'},
                                                                         {'id': 8, 'name': 'net17', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'networkUri': 'ETH:net17', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:08', 'requestedVFs': '3'},
                                                                         {'id': 9, 'name': 'net18', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net18', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:09'}]},
                                  'boot': {'manageBoot': True, 'order': ['PXE']},
                                  'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'}}]

server_profile_diff_conn_enc3 = [{'name': 'enc3_bay5', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ708030N, bay 3', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'affinity': 'Bay',
                                  'boot': {'manageBoot': True, 'order': ['PXE']},
                                  'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                  'connectionSettings': {'connections': [{'id': 5, 'name': 'net14', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'networkUri': 'ETH:net14', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:14', 'boot': {'priority': 'Primary'}},
                                                                         {'id': 6, 'name': 'net15', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b', 'networkUri': 'ETH:net15', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:15', 'requestedVFs': '3'},
                                                                         {'id': 7, 'name': 'net16', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'networkUri': 'ETH:net16', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:16'},
                                                                         {'id': 8, 'name': 'net17', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'networkUri': 'ETH:net17', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:17'}]}, }]

expected_server_profile_diff_conn_enc3 = [{'name': 'enc3_bay5', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ708030N, bay 3', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'affinity': 'Bay',
                                           'boot': {'manageBoot': True, 'order': ['PXE']},
                                           'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                           'connectionSettings': {'connections': [{'id': 5, 'name': 'net14', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'networkUri': 'ETH:net14', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:14', 'boot': {'priority': 'Primary'}},
                                                                                  {'id': 6, 'name': 'net15', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b', 'networkUri': 'ETH:net15', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:15', 'requestedVFs': '3'},
                                                                                  {'id': 7, 'name': 'net16', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'networkUri': 'ETH:net16', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:16'},
                                                                                  {'id': 8, 'name': 'net17', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'networkUri': 'ETH:net17', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:17'}]},
                                           'status': 'OK'}]

server_profile_three_conn_enc3 = [{'name': 'enc3_bay5', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ708030N, bay 3', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'affinity': 'Bay',
                                   'boot': {'manageBoot': True, 'order': ['PXE']},
                                   'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                                   'connectionSettings': {'connections': [{'id': 1, 'name': 'net10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'networkUri': 'ETH:net10', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:01', 'boot': {'priority': 'Primary'}},
                                                                          {'id': 2, 'name': 'net11', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'networkUri': 'ETH:net11', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:02', 'requestedVFs': '3'},
                                                                          {'id': 3, 'name': 'net12', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'networkUri': 'ETH:net12', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:03'},
                                                                          {'id': 4, 'name': 'net13', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'networkUri': 'ETH:net13', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:04'}]}, }]

expected_server_profile_three_conn_enc3 = [{'name': 'enc3_bay5', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ708030N, bay 3', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'affinity': 'Bay',
                                            'boot': {'manageBoot': True, 'order': ['PXE']},
                                            'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                                            'connectionSettings': {'connections': [{'id': 1, 'name': 'net10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'networkUri': 'ETH:net10', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:01', 'boot': {'priority': 'Primary'}},
                                                                                   {'id': 2, 'name': 'net11', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'networkUri': 'ETH:net11', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:02', 'requestedVFs': '3'},
                                                                                   {'id': 3, 'name': 'net12', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'networkUri': 'ETH:net12', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:03'},
                                                                                   {'id': 4, 'name': 'net13', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'networkUri': 'ETH:net13', 'macType': 'UserDefined', 'mac': 'AA:BB:65:80:00:04'}]},
                                            'status': 'OK'}]


server_profile_local_storage = [{'name': 'MXQ70700G4bay3', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ70700G4, bay 3', 'enclosureGroupUri': 'EG_Ring', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                 'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                 'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                 'firmware': {'firmwareScheduleDateTime': None, 'firmwareActivationType': None, 'firmwareInstallType': None, 'forceInstallFirmware': False, 'manageFirmware': False, 'firmwareBaselineUri': None, },
                                 'connectionSettings': {'connections': [{'id': 1, 'name': None, 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:net10', 'functionType': 'Ethernet', 'boot': {'priority': 'NotBootable'}, }]},
                                 'sanStorage': {'manageSanStorage': False, 'volumeAttachments': []},
                                 'bios': {'manageBios': True, 'overriddenSettings': [{'id': 'AdminName', 'value': 'WPST Tester1'}, {'id': 'AdminPhone', 'value': '111-111-1111'}]},
                                 'localStorage': {'controllers': [{'deviceSlot': 'Embedded', 'mode': 'RAID', 'initialize': True, 'importConfiguration': False,
                                                                   'logicalDrives': [{'name': 'LD1', 'raidLevel': 'RAID0', 'bootable': True, 'numPhysicalDrives': 1, 'driveTechnology': 'SasHdd', 'sasLogicalJBODId': None, }], }]}, }]

expected_server_profile_local_storage = [{'status': 'OK', 'name': 'MXQ70700G4bay3', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ70700G4, bay 3', 'enclosureGroupUri': 'EG_Ring', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                          'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                          'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                          'firmware': {'firmwareScheduleDateTime': None, 'firmwareActivationType': None, 'firmwareInstallType': None, 'forceInstallFirmware': False, 'manageFirmware': False, 'firmwareBaselineUri': None, },
                                          'connectionSettings': {'connections': [{'id': 1, 'name': None, 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:net10', 'functionType': 'Ethernet', 'boot': {'priority': 'NotBootable'}, }]},
                                          'sanStorage': {'manageSanStorage': False, 'volumeAttachments': []},
                                          'bios': {'manageBios': True, 'overriddenSettings': [{'id': 'AdminName', 'value': 'WPST Tester1'}, {'id': 'AdminPhone', 'value': '111-111-1111'}]},
                                          'localStorage': {'controllers': [{'deviceSlot': 'Embedded', 'mode': 'RAID', 'initialize': False, 'importConfiguration': False,
                                                                            'logicalDrives': [{'name': 'LD1', 'raidLevel': 'RAID0', 'bootable': True, 'numPhysicalDrives': 1, 'driveTechnology': 'SasHdd', 'sasLogicalJBODId': None, }], }]}, }]


edit_serverprofile_hba = [{'name': 'MXQ70700G4bay3', 'status': 'OK', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ70700G4, bay 3', 'enclosureGroupUri': 'EG_Ring', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                           'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                           'boot': {'manageBoot': True, 'order': ['HardDisk']},
                           'firmware': {'firmwareScheduleDateTime': None, 'firmwareActivationType': None, 'firmwareInstallType': None, 'forceInstallFirmware': False, 'manageFirmware': False, 'firmwareBaselineUri': None, },
                           'connectionSettings': {'connections': [{'id': 1, 'name': None, 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:net10', 'functionType': 'Ethernet', 'boot': {'priority': 'NotBootable'}, }]},
                           'bios': {'manageBios': True, 'overriddenSettings': [{'id': 'AdminName', 'value': 'WPST Tester1'}, {'id': 'AdminPhone', 'value': '111-111-1111'}]},
                           'localStorage': {'sasLogicalJBODs': [], 'controllers': [{'deviceSlot': 'Embedded', 'mode': 'HBA', 'initialize': True, 'importConfiguration': False, }]}, }]


expected_serverprofile_hba = edit_serverprofile_hba = [{'name': 'MXQ70700G4bay3', 'status': 'OK', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ70700G4, bay 3', 'enclosureGroupUri': 'EG_Ring', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                                        'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                                        'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                                        'firmware': {'firmwareScheduleDateTime': None, 'firmwareActivationType': None, 'firmwareInstallType': None, 'forceInstallFirmware': False, 'manageFirmware': False, 'firmwareBaselineUri': None, },
                                                        'connectionSettings': {'connections': [{'id': 1, 'name': None, 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:net10', 'functionType': 'Ethernet', 'boot': {'priority': 'NotBootable'}, }]},
                                                        'bios': {'manageBios': True, 'overriddenSettings': [{'id': 'AdminName', 'value': 'WPST Tester1'}, {'id': 'AdminPhone', 'value': '111-111-1111'}]},
                                                        'localStorage': {'sasLogicalJBODs': [], 'controllers': [{'deviceSlot': 'Embedded', 'mode': 'HBA', 'initialize': False, 'importConfiguration': False, }]}, }]

edit_serverprofile_raid = [{'name': 'MXQ70700G4bay3', 'status': 'OK', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ70700G4, bay 3', 'enclosureGroupUri': 'EG_Ring', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                            'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                            'boot': {'manageBoot': True, 'order': ['HardDisk']},
                            'firmware': {'firmwareScheduleDateTime': None, 'firmwareActivationType': None, 'firmwareInstallType': None, 'forceInstallFirmware': False, 'manageFirmware': False, 'firmwareBaselineUri': None, },
                            'connectionSettings': {'connections': [{'id': 1, 'name': None, 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:net10', 'functionType': 'Ethernet', 'boot': {'priority': 'NotBootable'}, }]},
                            'sanStorage': {'manageSanStorage': False, 'volumeAttachments': []},
                            'bios': {'manageBios': True, 'overriddenSettings': [{'id': 'AdminName', 'value': 'WPST Tester1'}, {'id': 'AdminPhone', 'value': '111-111-1111'}]},
                            'localStorage': {'controllers': [{'deviceSlot': 'Embedded', 'mode': 'RAID', 'initialize': True, 'importConfiguration': False,
                                                              'logicalDrives': [{'name': 'LD3', 'raidLevel': 'RAID0', 'bootable': True, 'numPhysicalDrives': 1, 'driveTechnology': 'SasHdd', 'sasLogicalJBODId': None, }], }]}, }]


expected_serverprofile_raid = [{'name': 'MXQ70700G4bay3', 'status': 'OK', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ70700G4, bay 3', 'enclosureGroupUri': 'EG_Ring', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                'firmware': {'firmwareScheduleDateTime': None, 'firmwareActivationType': None, 'firmwareInstallType': None, 'forceInstallFirmware': False, 'manageFirmware': False, 'firmwareBaselineUri': None, },
                                'connectionSettings': {'connections': [{'id': 1, 'name': None, 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:net10', 'functionType': 'Ethernet', 'boot': {'priority': 'NotBootable'}, }]},
                                'sanStorage': {'manageSanStorage': False, 'volumeAttachments': []},
                                'bios': {'manageBios': True, 'overriddenSettings': [{'id': 'AdminName', 'value': 'WPST Tester1'}, {'id': 'AdminPhone', 'value': '111-111-1111'}]},
                                'localStorage': {'controllers': [{'deviceSlot': 'Embedded', 'mode': 'RAID', 'initialize': False, 'importConfiguration': False,
                                                                  'logicalDrives': [{'name': 'LD3', 'raidLevel': 'RAID0', 'bootable': True, 'numPhysicalDrives': 1, 'driveTechnology': 'SasHdd', 'sasLogicalJBODId': None, }], }]}, }]

health_status = {'enc_serial': 'MXQ70700G4', 'efuse_bay_number': 3, 'efuse_action': 'EFuseReset'}

efuse_server_profile = [{'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ70700G4, bay 3',
                         'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1:3:Synergy 3820C 10/20Gb CNA', 'enclosureGroupUri': 'EG:EG_Ring',
                         'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                         'name': 'MXQ70700G4bay3', 'description': '', 'affinity': 'Bay',
                         'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                         'boot': {'manageBoot': True, 'order': ['PXE']},
                         'bios': {'manageBios': True, 'overriddenSettings': [{'id': 'AdminName', 'value': 'WPST Tester1'}, {'id': 'AdminPhone', 'value': '111-111-1111'}]},
                         'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                         'connectionSettings': {'connections': [{'id': 1, 'name': 'Mezz 3:1-a', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:net10', 'functionType': 'Ethernet'}]}}]

expected_efuse_server_profile = [{'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ70700G4, bay 3',
                                  'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1:3:Synergy 3820C 10/20Gb CNA', 'enclosureGroupUri': 'EG:EG_Ring',
                                  'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                  'name': 'MXQ70700G4bay3', 'description': '', 'affinity': 'Bay',
                                  'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                                  'boot': {'manageBoot': True, 'order': ['PXE']}, 'status': 'OK',
                                  'bios': {'manageBios': True, 'overriddenSettings': [{'id': 'AdminName', 'value': 'WPST Tester1'}, {'id': 'AdminPhone', 'value': '111-111-1111'}]},
                                  'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                                  'connectionSettings': {'connections': [{'id': 1, 'name': 'Mezz 3:1-a', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:net10', 'functionType': 'Ethernet'}]}}]


fan_failures = [{'enc_serial': 'MXQ70700G4', 'fan_action': 'FanFaultInjection', 'fan_bay_number': 1, 'fan_fault_type': 'Fan1', 'inject_failure': 'true', 'filter': '/rest/v1/Fan/1'},
                {'enc_serial': 'MXQ70700G4', 'fan_action': 'FanFaultInjection', 'fan_bay_number': 1, 'fan_fault_type': 'Fan1', 'inject_failure': 'false', 'filter': '/rest/v1/Fan/1'}]

power_failures = [{'enc_serial': 'MXQ70700G4', 'power_action': 'PSFaultInjection', 'power_bay_number': 2, 'power_fault_type': 'PS_OK', 'inject_failure': 'true', 'filter': '/rest/v1/PowerSupply/2'},
                  {'enc_serial': 'MXQ70700G4', 'power_action': 'PSFaultInjection', 'power_bay_number': 2, 'power_fault_type': 'PS_OK', 'inject_failure': 'false', 'filter': '/rest/v1/PowerSupply/2'}]

snmp_trap = [{'trap_tool_path': 'C:\\Users\\Administrator\\Desktop\\sendSnmpTrap.exe', 'source_server_hardware_name': 'MXQ708021V, bay 1', 'source_server_hardware': '10.93.12.13', 'trap_name': 'cpqHeResilientMemLockStepMemoryEngaged', 'trap_value': 'cpqHoTrapFlags 1'},
             {'trap_tool_path': 'C:\\Users\\Administrator\\Desktop\\sendSnmpTrap.exe', 'source_server_hardware_name': 'MXQ708021V, bay 1', 'source_server_hardware': '10.93.12.13', 'trap_name': 'cpqHe4FltTolPowerSupplyFailed',
              'trap_value': 'cpqHeFltTolPowerSupplyChassis 2' + ' -v ' + 'cpqHeFltTolPowerSupplyBay 3' + ' -v ' + 'cpqHeFltTolPowerSupplyStatus 13' + ' -v ' + 'cpqHeFltTolPowerSupplyModel 5' + ' -v ' + 'cpqHeFltTolPowerSupplySerialNumber 6' + ' -v ' + 'cpqHeFltTolPowerSupplyAutoRev 7' +
              ' -v ' + 'cpqHeFltTolPowerSupplyFirmwareRev 8' + ' -v ' + 'cpqHeFltTolPowerSupplySparePartNum 9' + ' -v ' + 'cpqSiServerSystemId 10'}]

snmp_server_profile = [{'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ708021V, bay 1',
                        'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1:3:Synergy 3820C 10/20Gb CNA', 'enclosureGroupUri': 'EG:EG_Ring',
                        'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                        'name': 'MXQ708021Vbay1', 'description': '', 'affinity': 'Bay',
                        'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                        'boot': {'manageBoot': True, 'order': ['PXE']},
                        'bios': {'manageBios': True, 'overriddenSettings': [{'id': 'AdminName', 'value': 'WPST Tester1'}, {'id': 'AdminPhone', 'value': '111-111-1111'}]},
                        'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                        'connectionSettings': {'connections': [{'id': 1, 'name': 'Mezz 3:1-a', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:net10', 'functionType': 'Ethernet'}]}}]

expected_snmp_server_profile = [{'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:MXQ708021V, bay 1',
                                 'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1:3:Synergy 3820C 10/20Gb CNA', 'enclosureGroupUri': 'EG:EG_Ring',
                                 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                 'name': 'MXQ708021Vbay1', 'description': '', 'affinity': 'Bay',
                                 'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                                 'boot': {'manageBoot': True, 'order': ['PXE']}, 'status': 'OK',
                                 'bios': {'manageBios': True, 'overriddenSettings': [{'id': 'AdminName', 'value': 'WPST Tester1'}, {'id': 'AdminPhone', 'value': '111-111-1111'}]},
                                 'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                                 'connectionSettings': {'connections': [{'id': 1, 'name': 'Mezz 3:1-a', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:net10', 'functionType': 'Ethernet'}]}}]

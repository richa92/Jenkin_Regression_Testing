
admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

ilo_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

licenses = [{'key': 'YBLG B99A H9PQ 8HVZ U7B5 HWW5 Y9JL KMPL VAWA 8CBE DXAU 2CSM GHTG L762 5NW5 HDV4 KJVT D5KM EFVW DT5J VXP8 4XK2 GNSL 9F82 7JKT QVXB XZKH ABB4 NV2C LHXU KN7U 5NA6 BKRK 35QB D8UW R42A X3BN LQ6M 5V9A PM6Q 4MN9 9GGS EZU7 GEMX VUJW CDB5 JVRX 8HEN 2J98 ACPB "TKOPREN HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR JJADJJEDATCA'},
            {'key': '9B3C A99A H9P9 GHUZ U7B5 HWW5 Y9JL KMPL 5AWA 8CBE DXAU 2CSM GHTG L762 7NGZ GDV4 KJVT D5KM EFRW DS5R 5XP8 4XK2 GNSL 9F82 7JKT QVXB XZKH ABB4 NV2C LHXU KN7U 5NA6 BKRK 35QB D8UW R42A X3BN LQ6M 5V9A PM6Q 4MN9 9GGS EZU7 GEMX VUJW CDB5 JVRX 8HEN 2J98 ACPB "TKOPREN HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR ATJUJJEDAT2Y'},
            {'key': '9CDC C9MA H9P9 CHV2 V7B5 HWWB Y9JL KMPL MACB 8ERQ DXAU 2CSM GHTG L762 X4Z2 WPJQ KJVT D5KM EFVW DT5J NX7N 4R2K 9K2P 3EW2 FJAW XUNF TZZH MB5X 82Z5 WHEF GE4C LUE3 BKT8 WXDG NK6Y C4GA HZL4 XBE7 3VJ6 2MSU 4ZU9 9WGG CZU7 WE4X YN44 CH55 KZLG 2F4N A8RJ UKEC 3F9V JQY5 "424446983 HPOV-NFR1 HP_OneView_16_Seat_NFR 7D2HJJEUD5AC"_3QMTJ-Q4HBV-H7DMB-TP7GX-ZJDZH'},
            {'key': 'ACDC C9MA H9PA GHXZ V7B5 HWWB Y9JL KMPL UACF 4EBQ DXAU 2CSM GHTG L762 B456 VPZY KJVT D5KM EFVW DV5J XX7J PRKK 9K2P 3EW2 FJAW XUNF TZZP MB5X 82Z5 WHEF GE4C LUE3 BKT8 WXDG NK6Y C4GA HZL4 XBE7 3VJ6 2MSU 4ZU9 9WGG CZU7 WE4X YN44 CH55 KZLG 2F4N A8RJ UKEC 3F9V JQY5 "424446984 HPOV-NFR1 HP_OneView_16_Seat_NFR JCECJJEU35YD"_3QMTD-3YCMM-QRB6Z-V6Y76-7LP22'}
            ]

users = [{'userName': 'administrator', 'password': 'wpsthpvse1', 'roles': ['Administrator'], 'emailAddress':'admin@hp.com', 'officePhone':'970-555-0003', 'mobilePhone':'970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'appliance', 'password': 'wpsthpvse1', 'roles': ['Infrastructure administrator'], 'emailAddress':'appliance@hp.com', 'officePhone':'970-898-2222', 'mobilePhone':'970-898-0022', 'type': 'UserAndRoles'},
         {'userName': 'backup', 'password': 'backupadmin', 'roles': ['Backup administrator'], 'emailAddress':'backup@hp.com', 'officePhone':'970-666-1919', 'mobilePhone':'970-600-1919', 'type': 'UserAndRoles'},
         {'userName': 'network', 'password': 'networkadmin', 'roles': ['Network administrator'], 'emailAddress':'network@hp.com', 'officePhone':'970-555-0001', 'mobilePhone':'970-500-0001', 'type': 'UserAndRoles'},
         {'userName': 'readonly', 'password': 'readonly', 'roles': ['Read only'], 'emailAddress':'readonly@hp.com', 'officePhone':'970-666-1919', 'mobilePhone':'970-600-1919', 'type': 'UserAndRoles'},
         {'userName': 'server', 'password': 'serveradmin', 'roles': ['Server administrator'], 'emailAddress':'server@hp.com', 'officePhone':'970-555-0001', 'mobilePhone':'970-500-0001', 'type': 'UserAndRoles'},
         {'userName': 'storage', 'password': 'storageadmin', 'roles': ['Storage administrator'], 'emailAddress':'storage@hp.com', 'officePhone':'970-555-0001', 'mobilePhone':'970-500-0001', 'type': 'UserAndRoles'},
         {'userName': 'oneview', 'password': 'oneviewadmin', 'roles': ['Infrastructure administrator'], 'emailAddress':'oneview@hp.com', 'officePhone':'970-555-0001', 'mobilePhone':'970-500-0001', 'type': 'UserAndRoles'},
         {'userName': 'networkserver', 'password': 'networkserveradmin', 'roles': ['Network administrator', 'Server administrator'], 'emailAddress':'networkserver@hp.com', 'officePhone':'970-555-0001', 'mobilePhone':'970-500-0001', 'type': 'UserAndRoles'},
         {'userName': 'backupstorage', 'password': 'backupstorageadmin', 'roles': ['Backup administrator', 'Storage administrator'], 'emailAddress':'backupstorage@hp.com', 'officePhone':'970-555-0001', 'mobilePhone':'970-500-0001', 'type': 'UserAndRoles'},
         {'userName': 'networkserverstorage', 'password': 'wpsthpvse1', 'roles': ['Network administrator', 'Server administrator', 'Storage administrator'], 'emailAddress':'networkserverstorage@hp.com', 'officePhone':'970-555-0001', 'mobilePhone':'970-500-0001', 'type': 'UserAndRoles'}
         ]

san_managers = [{'connectionInfo': [{'name': 'Type', 'value': 'HPE'},
                                    {'name': 'Host', 'value': '10.0.1.10'},
                                    {'name': 'SnmpPort', 'value': 161},
                                    {'name': 'SnmpUserName', 'value': 'defaultUser'},
                                    {'name': 'SnmpAuthLevel', 'value': 'authpriv'},
                                    {'name': 'SnmpAuthProtocol', 'value': 'md5'},
                                    {'name': 'SnmpAuthString', 'value': 'authPass123'},
                                    {'name': 'SnmpPrivProtocol', 'value': 'aes'},
                                    {'name': 'SnmpPrivString', 'value': 'privPass123'}]
                 },
                {'connectionInfo': [{'name': 'Type', 'value': 'HPE'},
                                    {'name': 'Host', 'value': '10.0.1.14'},
                                    {'name': 'SnmpPort', 'value': 161},
                                    {'name': 'SnmpUserName', 'value': 'defaultUser'},
                                    {'name': 'SnmpAuthLevel', 'value': 'authpriv'},
                                    {'name': 'SnmpAuthProtocol', 'value': 'md5'},
                                    {'name': 'SnmpAuthString', 'value': 'authPass123'},
                                    {'name': 'SnmpPrivProtocol', 'value': 'aes'},
                                    {'name': 'SnmpPrivString', 'value': 'privPass123'}]
                 }
                ]

expected_san_managers = [{'name': '10.0.1.10',
                          'type': 'FCDeviceManagerV2',
                          'state': 'Managed',
                          'status': 'OK',
                          'category': 'fc-device-managers',
                          'connectionInfo': [{'valueFormat': 'IPAddressOrHostname', 'displayName': 'Host', 'name': 'Host', 'valueType': 'String', 'required': False, 'value': '10.0.1.10'},
                                             {'valueFormat': 'None', 'displayName': 'SnmpPort', 'name': 'SnmpPort', 'valueType': 'Integer', 'required': False, 'value': 161},
                                             {'valueFormat': 'None', 'displayName': 'SnmpUserName', 'name': 'SnmpUserName', 'valueType': 'String', 'required': False, 'value': 'defaultUser'},
                                             {'valueFormat': 'None', 'displayName': 'SnmpAuthLevel', 'name': 'SnmpAuthLevel', 'valueType': 'String', 'required': False, 'value': 'authpriv'},
                                             {'valueFormat': 'None', 'displayName': 'SnmpAuthProtocol', 'name': 'SnmpAuthProtocol', 'valueType': 'String', 'required': False, 'value': 'md5'},
                                             {'valueFormat': 'SecuritySensitive', 'displayName': 'SnmpAuthString', 'name': 'SnmpAuthString', 'valueType': 'String', 'required': False, 'value': ''},
                                             {'valueFormat': 'None', 'displayName': 'SnmpPrivProtocol', 'name': 'SnmpPrivProtocol', 'valueType': 'String', 'required': False, 'value': 'aes'},
                                             {'valueFormat': 'SecuritySensitive', 'displayName': 'SnmpPrivString', 'name': 'SnmpPrivString', 'valueType': 'String', 'required': False, 'value': ''},
                                             {'valueFormat': 'None', 'displayName': 'Type', 'name': 'Type', 'valueType': 'String', 'required': False, 'value': 'HPE'}],
                          'description': 'HP 5900AF-48G-4XG-2QSFP+ Switch',
                          'deviceManagerVersion': '7.1.045 Release 2416',
                          'deviceManagerUrl': '10.0.1.10',
                          'providerDisplayName': 'HPE',
                          'providerUri': 'FCPROV:HPE San Plugin',
                          'uri': 'SAN:10.0.1.10'
                          },
                         {'name': '10.0.1.14',
                          'type': 'FCDeviceManagerV2',
                          'state': 'Managed',
                          'status': 'OK',
                          'category': 'fc-device-managers',
                          'connectionInfo': [{'valueFormat': 'IPAddressOrHostname', 'displayName': 'Host', 'name': 'Host', 'valueType': 'String', 'required': False, 'value': '10.0.1.14'},
                                             {'valueFormat': 'None', 'displayName': 'SnmpPort', 'name': 'SnmpPort', 'valueType': 'Integer', 'required': False, 'value': 161},
                                             {'valueFormat': 'None', 'displayName': 'SnmpUserName', 'name': 'SnmpUserName', 'valueType': 'String', 'required': False, 'value': 'defaultUser'},
                                             {'valueFormat': 'None', 'displayName': 'SnmpAuthLevel', 'name': 'SnmpAuthLevel', 'valueType': 'String', 'required': False, 'value': 'authpriv'},
                                             {'valueFormat': 'None', 'displayName': 'SnmpAuthProtocol', 'name': 'SnmpAuthProtocol', 'valueType': 'String', 'required': False, 'value': 'md5'},
                                             {'valueFormat': 'SecuritySensitive', 'displayName': 'SnmpAuthString', 'name': 'SnmpAuthString', 'valueType': 'String', 'required': False, 'value': ''},
                                             {'valueFormat': 'None', 'displayName': 'SnmpPrivProtocol', 'name': 'SnmpPrivProtocol', 'valueType': 'String', 'required': False, 'value': 'aes'},
                                             {'valueFormat': 'SecuritySensitive', 'displayName': 'SnmpPrivString', 'name': 'SnmpPrivString', 'valueType': 'String', 'required': False, 'value': ''},
                                             {'valueFormat': 'None', 'displayName': 'Type', 'name': 'Type', 'valueType': 'String', 'required': False, 'value': 'HPE'}],
                          'description': 'HP 5900AF-48G-4XG-2QSFP+ Switch',
                          'deviceManagerVersion': '7.1.045 Release 2416',
                          'deviceManagerUrl': '10.0.1.14',
                          'providerDisplayName': 'HPE',
                          'providerUri': 'FCPROV:HPE San Plugin',
                          'uri': 'SAN:10.0.1.14'
                          }
                         ]

ethernet_networks = [{'name': 'net1036-a', 'vlanId': '1036', 'purpose': 'Management', 'smartLink': 'false', 'privateNetwork': 'false', 'ethernetNetworkType': 'Tagged', 'type': 'ethernet-networkV300', 'connectionTemplateUri': None},
                     {'name': 'net1036-b', 'vlanId': '1036', 'purpose': 'General', 'smartLink': 'false', 'privateNetwork': 'false', 'ethernetNetworkType': 'Tagged', 'type': 'ethernet-networkV300', 'connectionTemplateUri': None},
                     {'name': 'net1037-a', 'vlanId': '1037', 'purpose': 'Management', 'smartLink': 'false', 'privateNetwork': 'false', 'ethernetNetworkType': 'Tagged', 'type': 'ethernet-networkV300', 'connectionTemplateUri': None},
                     {'name': 'net1037-b', 'vlanId': '1037', 'purpose': 'General', 'smartLink': 'false', 'privateNetwork': 'false', 'ethernetNetworkType': 'Tagged', 'type': 'ethernet-networkV300', 'connectionTemplateUri': None},
                     {'name': 'net1038-a', 'vlanId': '1038', 'purpose': 'Management', 'smartLink': 'false', 'privateNetwork': 'false', 'ethernetNetworkType': 'Tagged', 'type': 'ethernet-networkV300', 'connectionTemplateUri': None},
                     {'name': 'net1038-b', 'vlanId': '1038', 'purpose': 'General', 'smartLink': 'false', 'privateNetwork': 'false', 'ethernetNetworkType': 'Tagged', 'type': 'ethernet-networkV300', 'connectionTemplateUri': None},
                     {'name': 'net1039-a', 'vlanId': '1039', 'purpose': 'Management', 'smartLink': 'false', 'privateNetwork': 'false', 'ethernetNetworkType': 'Tagged', 'type': 'ethernet-networkV300', 'connectionTemplateUri': None},
                     {'name': 'net1039-b', 'vlanId': '1039', 'purpose': 'General', 'smartLink': 'false', 'privateNetwork': 'false', 'ethernetNetworkType': 'Tagged', 'type': 'ethernet-networkV300', 'connectionTemplateUri': None},
                     {'name': 'net1040-a', 'vlanId': '1040', 'purpose': 'Management', 'smartLink': 'false', 'privateNetwork': 'false', 'ethernetNetworkType': 'Tagged', 'type': 'ethernet-networkV300', 'connectionTemplateUri': None},
                     {'name': 'net1040-b', 'vlanId': '1040', 'purpose': 'General', 'smartLink': 'false', 'privateNetwork': 'false', 'ethernetNetworkType': 'Tagged', 'type': 'ethernet-networkV300', 'connectionTemplateUri': None},
                     ]

expected_ethernet_networks = [{'name': 'net1036-a', 'type': 'ethernet-networkV300', 'ethernetNetworkType': 'Tagged', 'vlanId': '1036', 'smartLink': 'False', 'purpose': 'Management', 'privateNetwork': 'False', 'subnetUri': None, 'description': None, 'status': 'OK', 'state': 'Active', 'category': 'ethernet-networks', 'uri': 'ETH:net1036-a'},
                              {'name': 'net1036-b', 'type': 'ethernet-networkV300', 'ethernetNetworkType': 'Tagged', 'vlanId': '1036', 'smartLink': 'False', 'purpose': 'General', 'privateNetwork': 'False', 'subnetUri': None, 'description': None, 'status': 'OK', 'state': 'Active', 'category': 'ethernet-networks', 'uri': 'ETH:net1036-b'},
                              {'name': 'net1037-a', 'type': 'ethernet-networkV300', 'ethernetNetworkType': 'Tagged', 'vlanId': '1037', 'smartLink': 'False', 'purpose': 'Management', 'privateNetwork': 'False', 'subnetUri': None, 'description': None, 'status': 'OK', 'state': 'Active', 'category': 'ethernet-networks', 'uri': 'ETH:net1037-a'},
                              {'name': 'net1037-b', 'type': 'ethernet-networkV300', 'ethernetNetworkType': 'Tagged', 'vlanId': '1037', 'smartLink': 'False', 'purpose': 'General', 'privateNetwork': 'False', 'subnetUri': None, 'description': None, 'status': 'OK', 'state': 'Active', 'category': 'ethernet-networks', 'uri': 'ETH:net1037-b'},
                              {'name': 'net1038-a', 'type': 'ethernet-networkV300', 'ethernetNetworkType': 'Tagged', 'vlanId': '1038', 'smartLink': 'False', 'purpose': 'Management', 'privateNetwork': 'False', 'subnetUri': None, 'description': None, 'status': 'OK', 'state': 'Active', 'category': 'ethernet-networks', 'uri': 'ETH:net1038-a'},
                              {'name': 'net1038-b', 'type': 'ethernet-networkV300', 'ethernetNetworkType': 'Tagged', 'vlanId': '1038', 'smartLink': 'False', 'purpose': 'General', 'privateNetwork': 'False', 'subnetUri': None, 'description': None, 'status': 'OK', 'state': 'Active', 'category': 'ethernet-networks', 'uri': 'ETH:net1038-b'},
                              {'name': 'net1039-a', 'type': 'ethernet-networkV300', 'ethernetNetworkType': 'Tagged', 'vlanId': '1039', 'smartLink': 'False', 'purpose': 'Management', 'privateNetwork': 'False', 'subnetUri': None, 'description': None, 'status': 'OK', 'state': 'Active', 'category': 'ethernet-networks', 'uri': 'ETH:net1039-a'},
                              {'name': 'net1039-b', 'type': 'ethernet-networkV300', 'ethernetNetworkType': 'Tagged', 'vlanId': '1039', 'smartLink': 'False', 'purpose': 'General', 'privateNetwork': 'False', 'subnetUri': None, 'description': None, 'status': 'OK', 'state': 'Active', 'category': 'ethernet-networks', 'uri': 'ETH:net1039-b'},
                              {'name': 'net1040-a', 'type': 'ethernet-networkV300', 'ethernetNetworkType': 'Tagged', 'vlanId': '1040', 'smartLink': 'False', 'purpose': 'Management', 'privateNetwork': 'False', 'subnetUri': None, 'description': None, 'status': 'OK', 'state': 'Active', 'category': 'ethernet-networks', 'uri': 'ETH:net1040-a'},
                              {'name': 'net1040-b', 'type': 'ethernet-networkV300', 'ethernetNetworkType': 'Tagged', 'vlanId': '1040', 'smartLink': 'False', 'purpose': 'General', 'privateNetwork': 'False', 'subnetUri': None, 'description': None, 'status': 'OK', 'state': 'Active', 'category': 'ethernet-networks', 'uri': 'ETH:net1040-b'},
                              ]

fc_networks = [{'name': 'fa-switch1', 'autoLoginRedistribution': 'true', 'type': 'fc-networkV300', 'linkStabilityTime': '30', 'fabricType': 'FabricAttach', 'connectionTemplateUri': None, 'managedSanUri': None},
               {'name': 'fa-switch2', 'autoLoginRedistribution': 'true', 'type': 'fc-networkV300', 'linkStabilityTime': '30', 'fabricType': 'FabricAttach', 'connectionTemplateUri': None, 'managedSanUri': None},
               {'name': 'da-3par1-a', 'autoLoginRedistribution': 'false', 'type': 'fc-networkV300', 'linkStabilityTime': '0', 'fabricType': 'DirectAttach', 'connectionTemplateUri': None, 'managedSanUri': None},
               {'name': 'da-3par1-b', 'autoLoginRedistribution': 'true', 'type': 'fc-networkV300', 'linkStabilityTime': '0', 'fabricType': 'DirectAttach', 'connectionTemplateUri': None, 'managedSanUri': None}
               ]

expected_fc_networks = [{'name': 'fa-switch1', 'type': 'fc-networkV300', 'fabricType': 'FabricAttach', 'linkStabilityTime': '30', 'managedSanUri': None, 'autoLoginRedistribution': 'True', 'description': None, 'status': 'OK', 'state': 'Active', 'category': 'fc-networks', 'uri': 'FC:fa-switch1'},
                        {'name': 'fa-switch2', 'type': 'fc-networkV300', 'fabricType': 'FabricAttach', 'linkStabilityTime': '30', 'managedSanUri': None, 'autoLoginRedistribution': 'True', 'description': None, 'status': 'OK', 'state': 'Active', 'category': 'fc-networks', 'uri': 'FC:fa-switch2'},
                        {'name': 'da-3par1-a', 'type': 'fc-networkV300', 'fabricType': 'DirectAttach', 'linkStabilityTime': '0', 'managedSanUri': None, 'autoLoginRedistribution': 'False', 'description': None, 'status': 'OK', 'state': 'Active', 'category': 'fc-networks', 'uri': 'FC:da-3par1-a'},
                        {'name': 'da-3par1-b', 'type': 'fc-networkV300', 'fabricType': 'DirectAttach', 'linkStabilityTime': '0', 'managedSanUri': None, 'autoLoginRedistribution': 'False', 'description': None, 'status': 'OK', 'state': 'Active', 'category': 'fc-networks', 'uri': 'FC:da-3par1-b'}
                        ]

fcoe_networks = [{"name": "FCOE1", "vlanId": "1084", "managedSanUri": "FCSan:VSAN1084", "type": "fcoe-networkV300"},
                 {"name": "FCOE2", "vlanId": "1085", "managedSanUri": "FCSan:VSAN1085", "type": "fcoe-networkV300"}
                 ]

expected_fcoe_networks = [{"name": "FCOE1", "vlanId": "1084", "managedSanUri": "FCSan:VSAN1084", "type": "fcoe-networkV300", "state": "Active", "description": None, "status": "OK", "category": "fcoe-networks", "uri": "FCOE:FCOE1"},
                          {"name": "FCOE2", "vlanId": "1085", "managedSanUri": "FCSan:VSAN1085", "type": "fcoe-networkV300", "state": "Active", "description": None, "status": "OK", "category": "fcoe-networks", "uri": "FCOE:FCOE2"}
                          ]


networksets = [{'name': 'netset1a', 'nativeNetworkUri': 'net1038-a', 'type': 'network-setV300', 'networkUris': ['net1036-a', 'net1037-a', 'net1038-a', 'net1039-a', 'net1040-a']},
               {'name': 'netset1b', 'nativeNetworkUri': 'net1038-b', 'type': 'network-setV300', 'networkUris': ['net1036-b', 'net1037-b', 'net1038-b', 'net1039-b', 'net1040-b']},
               ]

expected_networksets = [{'name': 'netset1a', 'type': 'network-setV300', 'networkUris': ['ETH:net1036-a', 'ETH:net1037-a', 'ETH:net1038-a', 'ETH:net1039-a', 'ETH:net1040-a'], 'nativeNetworkUri':'ETH:net1038-a', 'description':None, 'status':'OK', 'state':'Active', 'category':'network-sets', 'uri':'NS:netset1a'},
                        {'name': 'netset1b', 'type': 'network-setV300', 'networkUris': ['ETH:net1036-b', 'ETH:net1037-b', 'ETH:net1038-b', 'ETH:net1039-b', 'ETH:net1040-b'], 'nativeNetworkUri':'ETH:net1038-b', 'description':None, 'status':'OK', 'state':'Active', 'category':'network-sets', 'uri':'NS:netset1b'},
                        ]

storage_systems = [{'type': 'StorageSystemV3', 'serialNumber': '1649938', 'name': 'tbr13par', 'uri': 'SSYS:tbr13par', 'managedDomain': 'TB4',
                    'credentials': {'ip_hostname': '16.95.208.237', 'username': 'cosmos', 'password': 'Insight7'},
                    'managedPorts': [{'type': 'StorageTargetPortV3', 'name': '1:2:2', 'portName': '1:2:2', 'portWwn': '21:22:00:02:AC:00:C3:12', 'expectedNetworkUri': 'FCSan:VSAN1085', 'actualNetworkUri': 'FCOE:FCOE2', 'actualNetworkSanUri': 'VSAN1085', 'groupName': 'Auto', 'protocolType': 'FCoE', 'label': 'TBR3-5900AF-P50'},
                                     {'type': 'StorageTargetPortV3', 'name': '1:2:1', 'portName': '1:2:1', 'portWwn': '21:21:00:02:AC:00:C3:12', 'expectedNetworkUri': 'FCSan:VSAN1084', 'actualNetworkUri': 'FCOE:FCOE1', 'actualNetworkSanUri': 'VSAN1084', 'groupName': 'Auto', 'protocolType': 'FCoE', 'label': 'TBR1-5900AF-P50'},
                                     {'type': 'StorageTargetPortV3', 'name': '0:2:2', 'portName': '0:2:2', 'portWwn': '20:22:00:02:AC:00:C3:12', 'expectedNetworkUri': 'FCSan:VSAN1085', 'actualNetworkUri': 'FCOE:FCOE2', 'actualNetworkSanUri': 'VSAN1085', 'groupName': 'Auto', 'protocolType': 'FCoE', 'label': 'TBR3-5900AF-P49'},
                                     {'type': 'StorageTargetPortV3', 'name': '0:2:1', 'portName': '0:2:1', 'portWwn': '20:21:00:02:AC:00:C3:12', 'expectedNetworkUri': 'FCSan:VSAN1084', 'actualNetworkUri': 'FCOE:FCOE1', 'actualNetworkSanUri': 'VSAN1084', 'groupName': 'Auto', 'protocolType': 'FCoE', 'label': 'TBR1-5900AF-P49'}],
                    'unmanagedPorts': [],
                    'managedPools':[{'type': 'StoragePool', 'domain': 'TB4', 'name': 'TB4-Raid5-FC', 'deviceType': 'FC'}]
                    }]

expected_storage_systems = [{'type': 'StorageSystemV3', 'serialNumber': '1649938', 'name': 'tbr13par', 'uri': 'SSYS:tbr13par', 'managedDomain': 'TB4', 'firmware': '3.2.2.290', 'wwn': '2F:F7:00:02:AC:00:C3:12', 'state': 'Configured', 'model': 'HP_3PAR 7200c', 'refreshState': 'NotRefreshing', 'stateReason': 'None', 'description': '1649938', 'status': 'OK', 'state': 'Configured', 'category': 'storage-systems',
                             'credentials': {'ip_hostname': '16.95.208.237', 'username': 'cosmos'},
                             'managedPorts': [{'type': 'StorageTargetPortV3', 'name': '1:2:2', 'portName': '1:2:2', 'partnerPort': '0:2:2', 'refreshState': 'NotRefreshing', 'stateReason': 'None', 'status': 'OK', 'state': 'Configured', 'expectedNetworkName': 'VSAN1085', 'category': 'storage-target-ports', 'portWwn': '21:22:00:02:AC:00:C3:12', 'expectedNetworkUri': 'FCSan:VSAN1085', 'actualNetworkUri': 'FCOE:FCOE2', 'actualNetworkSanUri': 'FCSan:VSAN1085', 'groupName': 'Auto', 'protocolType': 'FCoE', 'label': 'TBR3-5900AF-P50'},
                                              {'type': 'StorageTargetPortV3', 'name': '1:2:1', 'portName': '1:2:1', 'partnerPort': '0:2:1', 'refreshState': 'NotRefreshing', 'stateReason': 'None', 'status': 'OK', 'state': 'Configured', 'expectedNetworkName': 'VSAN1084', 'category': 'storage-target-ports', 'portWwn': '21:21:00:02:AC:00:C3:12', 'expectedNetworkUri': 'FCSan:VSAN1084', 'actualNetworkUri': 'FCOE:FCOE1', 'actualNetworkSanUri': 'FCSan:VSAN1084', 'groupName': 'Auto', 'protocolType': 'FCoE', 'label': 'TBR1-5900AF-P50'},
                                              {'type': 'StorageTargetPortV3', 'name': '0:2:2', 'portName': '0:2:2', 'partnerPort': '1:2:2', 'refreshState': 'NotRefreshing', 'stateReason': 'None', 'status': 'OK', 'state': 'Configured', 'expectedNetworkName': 'VSAN1085', 'category': 'storage-target-ports', 'portWwn': '20:22:00:02:AC:00:C3:12', 'expectedNetworkUri': 'FCSan:VSAN1085', 'actualNetworkUri': 'FCOE:FCOE2', 'actualNetworkSanUri': 'FCSan:VSAN1085', 'groupName': 'Auto', 'protocolType': 'FCoE', 'label': 'TBR3-5900AF-P49'},
                                              {'type': 'StorageTargetPortV3', 'name': '0:2:1', 'portName': '0:2:1', 'partnerPort': '1:2:1', 'refreshState': 'NotRefreshing', 'stateReason': 'None', 'status': 'OK', 'state': 'Configured', 'expectedNetworkName': 'VSAN1084', 'category': 'storage-target-ports', 'portWwn': '20:21:00:02:AC:00:C3:12', 'expectedNetworkUri': 'FCSan:VSAN1084', 'actualNetworkUri': 'FCOE:FCOE1', 'actualNetworkSanUri': 'FCSan:VSAN1084', 'groupName': 'Auto', 'protocolType': 'FCoE', 'label': 'TBR1-5900AF-P49'}],
                             'managedPools': [{'type': 'StoragePoolV2', 'domain': 'TB4', 'name': 'TB4-Raid5-FC', 'deviceType': 'FC', 'supportedRAIDLevel': 'RAID5', 'deviceSpeed': 'Default', 'totalCapacity': '8640400457728', 'refreshState': 'NotRefreshing', 'stateReason': 'None', 'status': 'OK', 'state': 'Configured'}]
                             }]

uplink_sets = {'UplinkSetEthernet': {'name': 'UplinkSetEthernet', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['net1036-a', 'net1037-a', 'net1038-a', 'net1039-a', 'net1040-a'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                     'logicalPortConfigInfos': [{'bay': '3', 'port': 'Q1', 'enclosure': '1', 'speed': 'Auto'},
                                                                {'bay': '6', 'port': 'Q1', 'enclosure': '2', 'speed': 'Auto'}]},

               'UplinkFCOE1': {'name': 'UplinkFCOE1', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['FCOE1'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                               'logicalPortConfigInfos': [{'bay': '3', 'port': 'Q2', 'enclosure': '1', 'speed': 'Auto'}]},

               'UplinkFCOE2': {'name': 'UplinkFCOE2', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['FCOE2'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                               'logicalPortConfigInfos': [{'bay': '6', 'port': 'Q2', 'enclosure': '2', 'speed': 'Auto'}]},
               }

ligs = [{'name': 'CHO-ME-LIG',
         'type': 'logical-interconnect-groupV300',
         'enclosureType': 'SY12000',
         "uplinkSets": [uplink_sets['UplinkSetEthernet'].copy(),
                        uplink_sets['UplinkFCOE1'].copy(),
                        uplink_sets['UplinkFCOE2'].copy()
                        ],
         'interconnectMapTemplate': [{'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy - 794502-B23', 'enclosureIndex': 1},
                                     {'bay': 6, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
                                     {'bay': 3, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
                                     {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy - 794502-B23', 'enclosureIndex': 2}],
         'internalNetworkUris': [],
         'interconnectBaySet': 3,
         'redundancyType': 'HighlyAvailable',
         'enclosureIndexes': [1, 2],
         'qosConfiguration': {'activeQosConfig': {'type': 'QosConfiguration', 'configType': 'Passthrough', 'downlinkClassificationType': None, 'uplinkClassificationType': None, 'qosTrafficClassifiers': None, 'description': None, 'status': None, 'name': None, 'state': None, 'category': 'qos-aggregated-configuration', 'created': None, 'modified': None, 'eTag': None, 'uri': None}, 'inactiveFCoEQosConfig': None, 'inactiveNonFCoEQosConfig': None, 'type': 'qos-aggregated-configuration', 'name': None, 'state': None, 'status': None, 'eTag': None, 'modified': None, 'created': None, 'category': 'qos-aggregated-configuration', 'uri': None}
         }
        ]

encgroups_add = [{'name': 'CHO-ME-EG', 'type': 'EnclosureGroupV300', 'interconnectBayMappings': [{'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:CHO-ME-LIG'}, {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:CHO-ME-LIG'}], "interconnectBayMappingCount": 2, "stackingMode": "Enclosure", "configurationScript": "", "uri": None, "powerMode": 'RedundantPowerSupply', 'ipAddressingMode': 'External', "ipRangeUris": [], "enclosureCount":2, "osDeploymentSettings":None, "enclosureTypeUri":"/rest/enclosure-types/SY12000"}
                 ]

expected_encgroups_add = [{'type': 'EnclosureGroupV300', 'uri': 'EG:CHO-ME-EG', 'category': 'enclosure-groups', 'name': 'CHO-ME-EG', 'status': 'OK', 'state': 'Normal', 'enclosureTypeUri': '/rest/enclosure-types/SY12000', 'stackingMode': 'Enclosure', 'portMappingCount': 8, 'interconnectBayMappingCount': 2, 'interconnectBayMappings': [{'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:CHO-ME-LIG'}, {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:CHO-ME-LIG'}], 'ipAddressingMode': 'External', 'ipRangeUris': [], 'powerMode':'RedundantPowerSupply', 'description':None, 'osDeploymentSettings':None, 'enclosureCount':2, 'associatedLogicalInterconnectGroups':['LIG:CHO-ME-LIG']}
                          ]

logical_enclosures = {'name': 'CHO-ME-LE', 'enclosureGroupUri': 'EG:CHO-ME-EG', 'enclosureUris': ['ENC:CN751302CG', 'ENC:CN750163KV'], 'firmwareBaselineUri': None, 'forceInstallFirmware': False}

expected_logical_enclosures = [{'name': 'CHO-ME-LE',
                                'type': 'LogicalEnclosureV300',
                                'description': None,
                                'category': 'logical-enclosures',
                                'scalingState': 'NotScaling',
                                'status': 'OK',
                                'state': 'Consistent',
                                'powerMode': 'RedundantPowerSupply',
                                'ipAddressingMode': 'External',
                                'uri': 'LE:CHO-ME-LE',
                                'deleteFailed': False,
                                'logicalInterconnectUris': ['LI:CHO-ME-LE-CHO-ME-LIG'],
                                'enclosureGroupUri': 'EG:CHO-ME-EG',
                                'firmware': {'firmwareBaselineUri': None, 'firmwareUpdateOn': None, 'forceInstallFirmware': False, 'logicalInterconnectUpdateMode': 'Parallel', 'validateIfLIFirmwareUpdateIsNonDisruptive': False, 'updateFirmwareOnUnmanagedInterconnect': False},
                                'deploymentManagerSettings': None,
                                'enclosureUris': ['ENC:CN751302CG', 'ENC:CN750163KV']
                                }]

expected_logical_interconnects = [{'type': 'logical-interconnectV300',
                                   'snmpConfiguration': {'type': 'snmp-configuration', 'readCommunity': 'public', 'enabled': True, 'category': 'snmp-configuration'},
                                   'qosConfiguration': {'type': 'qos-aggregated-configuration', 'activeQosConfig': {'type': 'QosConfiguration', 'configType': 'Passthrough', 'category': 'qos-aggregated-configuration'}, 'category': 'qos-aggregated-configuration'},
                                   'interconnectMap': {'interconnectMapEntries': [{'enclosureIndex': 1, 'permittedInterconnectTypeUri': 'ICTYPE:Virtual Connect SE 40Gb F8 Module for Synergy - 794502-B23', 'interconnectUri': 'IC:CN751302CG, interconnect 3', 'location': {'locationEntries': [{'value': '3', 'type': 'Bay'}, {'value': 'ENC:CN751302CG', 'type': 'Enclosure'}]}},
                                                                                  {'enclosureIndex': 1, 'permittedInterconnectTypeUri': 'ICTYPE:Synergy 20Gb Interconnect Link Module', 'interconnectUri': 'IC:CN751302CG, interconnect 6', 'location': {'locationEntries': [{'value': '6', 'type': 'Bay'}, {'value': 'ENC:CN751302CG', 'type': 'Enclosure'}]}},
                                                                                  {'enclosureIndex': 2, 'permittedInterconnectTypeUri': 'ICTYPE:Synergy 20Gb Interconnect Link Module', 'interconnectUri': 'IC:CN750163KV, interconnect 3', 'location': {'locationEntries': [{'value': '3', 'type': 'Bay'}, {'value': 'ENC:CN750163KV', 'type': 'Enclosure'}]}},
                                                                                  {'enclosureIndex': 2, 'permittedInterconnectTypeUri': 'ICTYPE:Virtual Connect SE 40Gb F8 Module for Synergy - 794502-B23', 'interconnectUri': 'IC:CN750163KV, interconnect 6', 'location': {'locationEntries': [{'value': '6', 'type': 'Bay'}, {'value': 'ENC:CN750163KV', 'type': 'Enclosure'}]}}]},
                                   'enclosureType': 'SY12000',
                                   'logicalInterconnectGroupUri': '',
                                   'consistencyStatus': 'CONSISTENT',
                                   'stackingHealth': 'BiConnected',
                                   'enclosureUris': ['ENC:CN751302CG', 'ENC:CN750163KV'],
                                   'interconnects':['IC:CN751302CG, interconnect 3', 'IC:CN751302CG, interconnect 6', 'IC:CN750163KV, interconnect 3', 'IC:CN750163KV, interconnect 6'],
                                   'name': 'CHO-ME-LE-CHO-ME-LIG',
                                   'state': 'Unknown',
                                   'status': 'OK'
                                   }]

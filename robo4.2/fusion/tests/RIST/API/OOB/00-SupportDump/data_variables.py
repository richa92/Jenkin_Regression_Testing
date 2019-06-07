######################################
admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}

######################################
add_enclosure_uri = '/rest/enclosures'
add_enclosure_body = {"username": "dcs", "password": "dcs",
                      "enclosureGroupUri": '/rest/enclosure-groups/5477f919-71a3-48bf-88ab-bc3cef2190aa',
                      "firmwareBaselineUri": None, "updateFirmwareOn": None, "force": False,
                      "forceInstallFirmware": False, "licensingIntent": "OneView", "hostname": "172.18.1.11"}

######################################
enclosure_sht_import_uri = '/rest/enclosures/importSHT'
enclosure_sht_import_body = {'hostname': '172.18.1.11', 'username': 'dcs', 'password': 'dcs'}

######################################
users = [
    {'userName': 'Serveradmin', 'password': 'Serveradmin', 'fullName': 'Serveradmin', 'roles': ['Server administrator'],
     'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
     'type': 'UserAndRoles'},
    {'userName': 'Networkadmin', 'password': 'Networkadmin', 'fullName': 'Networkadmin',
     'roles': ['Network administrator'], 'emailAddress': 'nat@hp.com', 'officePhone': '970-555-0003',
     'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
    {'userName': 'Backupadmin', 'password': 'Backupadmin', 'fullName': 'Backupadmin', 'roles': ['Backup administrator'],
     'emailAddress': 'backup@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
     'type': 'UserAndRoles'},
    {'userName': 'Noprivledge', 'password': 'Noprivledge', 'fullName': 'Noprivledge', 'roles': ['Read only'],
     'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
     'type': 'UserAndRoles'}
]

ethernet_networks = [{'name': 'IC',
                      'type': 'ethernet-networkV3',
                      'vlanId': 1001,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'},
                     {'name': 'Untagged',
                      'type': 'ethernet-networkV3',
                      'vlanId': None,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Untagged'},
                     {'name': 'Tunnel',
                      'type': 'ethernet-networkV3',
                      'vlanId': None,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tunnel'}]

expected_ethernet_networks = [{'name': 'IC', 'type': 'ethernet-networkV3',
                               'vlanId': 1001,
                               'purpose': 'General',
                               'smartLink': True,
                               'privateNetwork': False,
                               'ethernetNetworkType': 'Tagged'},
                              {'name': 'Untagged',
                               'type': 'ethernet-networkV3', 'vlanId': 0,
                               'purpose': 'General',
                               'smartLink': True,
                               'privateNetwork': False,
                               'ethernetNetworkType': 'Untagged'},
                              {'name': 'Tunnel', 'type': 'ethernet-networkV3',
                               'vlanId': 0,
                               'purpose': 'General',
                               'smartLink': True,
                               'privateNetwork': False,
                               'ethernetNetworkType': 'Tunnel'}]


######################################

licenses = [{'product': 'HPE OneView Advanced', 'key': 'AA9C DQAA H9PA GHX3 U7B5 HWW5 Y9JL KMPL SR6C MHJU DXAU 2CSM GHTG L762 9AVY WXJY KJVT D5KM EFVW DT5J TFQ9 74C8 SPS9 YG66 Z99R MWSN 6Z84 46XT WZJT HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTVG LS8T XU4E "EVAL-HPOV-NFR2 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR 9G6UAEJGUA4U"'},
            {'product': 'HPE OneView Advanced w/o iLO', 'key': '9A9C DQAA H9PY CHV2 V7B5 HWWB Y9JL KMPL DJKD 5FFM DXAU 2CSM GHTG L762 TT66 VZRY KJVT D5KM EFVW DT5J EBE9 M2CC SPS9 YG66 Z99R MWSN 6Z84 46XT WZJL HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTFG LS8T XU4E "EVAL-HPOV-NFR1 HPOV-NFR1 HP_OneView_16_Seat_NFR 7T36AEJG7JJ9"_3MBSY-CJZY2-LDVV4-92DQT-L6TTW'}]

######################################
lic = 'AA9C DQAA H9PA GHX3 U7B5 HWW5 Y9JL KMPL SR6C MHJU DXAU 2CSM GHTG L762 9AVY WXJY KJVT D5KM EFVW DT5J TFQ9 74C8 SPS9 YG66 Z99R MWSN 6Z84 46XT WZJT HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTVG LS8T XU4E "EVAL-HPOV-NFR2 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR 9G6UAEJGUA4U"'


######################################
expected_licenses = [{"productDescription": "HP OneView 16 Seat NFR",
                      "product": "HPE OneView Advanced",
                      "licenseType": "Evaluation",
                      "category": "licenses",
                      "totalCapacity": 16,
                      "key": "9A9C DQAA H9PY CHV2 V7B5 HWWB Y9JL KMPL DJKD 5FFM DXAU 2CSM GHTG L762 TT66 VZRY KJVT D5KM EFVW DT5J EBE9 M2CC SPS9 YG66 Z99R MWSN 6Z84 46XT WZJL HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTFG LS8T XU4E \"EVAL-HPOV-NFR1 HPOV-NFR1 HP_OneView_16_Seat_NFR 7T36AEJG7JJ9\"_3MBSY-CJZY2-LDVV4-92DQT-L6TTW",
                      "type": "LicenseV2"},
                     {"productDescription": "HP OneView w/o iLO 16 Seat NFR",
                      "product": "HPE OneView Advanced w/o iLO",
                      "licenseType": "Evaluation",
                      "category": "licenses",
                      "totalCapacity": 16,
                      "key": "AA9C DQAA H9PA GHX3 U7B5 HWW5 Y9JL KMPL SR6C MHJU DXAU 2CSM GHTG L762 9AVY WXJY KJVT D5KM EFVW DT5J TFQ9 74C8 SPS9 YG66 Z99R MWSN 6Z84 46XT WZJT HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTVG LS8T XU4E \"EVAL-HPOV-NFR2 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR 9G6UAEJGUA4U\"",
                      "type": "LicenseV2"}]

create_support_dump = [{"encrypt": True, "errorCode": "CI", "userName": "administrator", "password": "wpsthpvse1"},
                       {"encrypt": True, "errorCode": "CI", "userName": "backup", "password": "password"},
                       {"encrypt": True, "errorCode": "CI", "userName": "server", "password": "password"}]

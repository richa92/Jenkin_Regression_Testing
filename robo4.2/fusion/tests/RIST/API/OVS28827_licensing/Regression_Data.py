admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
oa_credentials = {'username': 'Administrator', 'password': 'hpvse14'}
ilo_credentials = {'username': 'Administrator', 'password': 'hpvse123'}
ssh_credentials = {'userName': 'root', 'password': 'hpvse1'}
FUSION_PROMPT = '#'               # Fusion Appliance Prompt
FUSION_TIMEOUT = 120

# Resource types for X-API-Version=800
APPLIANCE_NETWORK_CONFIGURATION_TYPE = 'ApplianceNetworkConfigurationV2'
TIME_AND_LOCALE_TYPE = 'TimeAndLocale'
USER_AND_PERMISSION_TYPE = 'UserAndPermissions'
ETHERNET_NETWORK_TYPE = 'ethernet-networkV4'
NETWORK_SET_TYPE = 'network-setV4'
FCOE_NETWORK_TYPE = 'fcoe-networkV4'
FC_NETWORK_TYPE = 'fc-networkV4'
LOGICAL_INTERCONNECT_GROUP_TYPE = 'logical-interconnect-groupV4'
INTERCONNECT_TYPE = 'InterconnectV4'
ENCLOSURE_TYPE = 'EnclosureV7'
ENCLOSURE_GROUP_TYPE = 'EnclosureGroupV7'
SERVER_HARDWARE_TYPE = 'server-hardware-8'
STORAGE_SYSTEM_TYPE = 'StorageSystemV4'
STORAGE_POOL_TYPE = 'StoragePoolV4'
STORAGE_VOLUME_TEMPLATE_TYPE = 'StorageTemplateV4'
STORAGE_VOLUME_TYPE = 'StorageVolumeV4'
SERVER_PROFILE_TEMPLATE_TYPE = 'ServerProfileTemplateV5'
SERVER_PROFILE_TYPE = 'ServerProfileV9'
SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE = 'ServerProfileCompliancePreviewV1'

# DL
DL120_name = 'FBTilodns'
DL120_IP = '16.114.212.91'
DL160_name = 'fvtdl93-ilo'
DL160_IP = '16.114.212.93'
DL180_name = 'ILO7CE651P1TU'
DL180_IP = '16.114.212.95'
DL360_name = 'ILOCN763807XQ'
DL360_IP = '16.125.78.155'
DL380_name = 'fvtdl43-ilo'
DL380_IP = '16.125.78.155'
# DL580_name = 'ILOCN771702NK'
# DL580_IP = '16.114.212.96'
DL180_2_IP = '16.114.212.94'

Gen10_DLs_with_profiles = [DL180_name]
Gen10_DLs_names = [DL120_name, DL160_name, DL180_name, DL360_name, DL380_name]

Gen10_DLs = [
    {'name': DL160_name,
     'hostname': DL160_IP,
     'licensingIntent': 'OneViewNoiLO',
     'username': 'Administrator',
     'password': 'hpvse123',
     'force': True,
     'configurationState': 'Managed'
     },
    {'name': DL180_name,
     'hostname': DL180_IP,
     'licensingIntent': 'OneViewNoiLO',
     'username': 'Administrator',
     'password': 'hpvse123',
     'force': True,
     'configurationState': 'Managed'
     },
]
licensesWithoutIlo = [{'key': 'YAAE DQAA H9P9 GHV3 U7B5 HWW5 Y9JL KMPL CRKE 6AJU DXAU 2CSM GHTG L762 H9Z2 WUZY KJVT D5KM EFVW DT5J FFAK N5C8 SPS9 YG66 Z99R MWSN 6Z84 46XT WZJT HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTVG LS8T XU4E "EVAL-HPOV-NFR2 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR 9G6UAEJGUA4U"'}]

licensesWithIlo = [
    {'key':
        '9A9C DQAA H9PY CHV2 V7B5 HWWB Y9JL KMPL DJKD 5FFM DXAU 2CSM GHTG L762 TT66 VZRY KJVT D5KM EFVW DT5J EBE9 M2CC SPS9 YG66 Z99R MWSN 6Z84 46XT WZJL HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTFG LS8T XU4E "EVAL-HPOV-NFR1 HPOV-NFR1 HP_OneView_16_Seat_NFR 7T36AEJG7JJ9"_3MBSY-CJZY2-LDVV4-92DQT-L6TTW'}]

ENC20 = 'wpst20'
ENC20_OA1 = "16.125.76.89"
EG20_NAME = "EG20"
LIG20_NAME = 'LIG20'

Enc = [{'name': ENC20}]
enclosureMonitored = [{'hostname': ENC20_OA1,
                       'username': oa_credentials['username'],
                       'password': oa_credentials['password'],
                       'enclosureGroupUri': None, 'force': True,
                       'firmwareBaselineUri': None,
                       'licensingIntent': 'OneViewStandard',
                       'state': 'Monitored'}]
enclosureWithOutIlo = [
    {'hostname': ENC20_OA1, 'username': oa_credentials['username'], 'password': oa_credentials['password'], 'enclosureGroupUri': 'EG:' + EG20_NAME,
     'force': True, 'licensingIntent': 'OneViewNoiLO', 'firmwareBaselineUri': None, }]

enclosureWithIlo = [
    {'hostname': ENC20_OA1, 'username': oa_credentials['username'], 'password': oa_credentials['password'], 'enclosureGroupUri': 'EG:' + EG20_NAME,
     'force': True, 'licensingIntent': 'OneView', 'firmwareBaselineUri': None, }]

# Interconnects
ENC20ICBAY1 = '%s, interconnect 1' % ENC20
ENC20ICBAY2 = '%s, interconnect 2' % ENC20
ENC20ICBAY3 = '%s, interconnect 3' % ENC20
ENC20ICBAY4 = '%s, interconnect 4' % ENC20
ENC20ICBAY5 = '%s, interconnect 5' % ENC20
ENC20ICBAY6 = '%s, interconnect 6' % ENC20

# Server Hardware
ENC20SHBAY1 = '%s, bay 1' % ENC20    # BL460c Gen8
ENC20SHBAY2 = '%s, bay 2' % ENC20    # BL465c Gen8
ENC20SHBAY3 = '%s, bay 3' % ENC20    # BL460c Gen8
ENC20SHBAY4 = '%s, bay 4' % ENC20    # BL460c Gen8
ENC20SHBAY6 = '%s, bay 6' % ENC20    # BL460c Gen9
ENC20SHBAY8 = '%s, bay 8' % ENC20    # BL660c Gen8

servers_IPs_keys = [{'server': 'ENC20SHBAY1', 'IP': '16.125.73.165', 'key': '35R74-PHZB2-VYBV6-W7SRY-YR6QH'},
                    {'server': 'ENC20SHBAY2', 'IP': '16.125.73.163', 'key': '32Q6W-PQWTB-H7XYL-39968-RR53R'},
                    {'server': 'ENC20SHBAY3', 'IP': '16.125.69.133', 'key': '332Q6-5QL28-7XHP3-NJZQT-7Y48W'},
                    {'server': 'ENC20SHBAY4', 'IP': '16.125.78.186', 'key': '32Q6W-PQWTB-H7XYL-39968-RR53R'},
                    {'server': 'ENC20SHBAY6', 'IP': '16.125.77.220', 'key': '32Q6W-PQWTB-H7XYL-39968-RR53R'},
                    {'server': 'ENC20SHBAY8', 'IP': '16.125.78.155', 'key': '3Q7Z5-2HDVR-CC6R8-6BJQM-9S84B'}]


sh_standard = [
    {'type': 'server-hardware-8', 'name': ENC20SHBAY1, 'licensingIntent': 'OneViewStandard'},
    {'type': 'server-hardware-8', 'name': ENC20SHBAY2, 'licensingIntent': 'OneViewStandard'},
    {'type': 'server-hardware-8', 'name': ENC20SHBAY3, 'licensingIntent': 'OneViewStandard'},
    {'type': 'server-hardware-8', 'name': ENC20SHBAY4, 'licensingIntent': 'OneViewStandard'},
    {'type': 'server-hardware-8', 'name': ENC20SHBAY6, 'licensingIntent': 'OneViewStandard'},
    {'type': 'server-hardware-8', 'name': ENC20SHBAY8, 'licensingIntent': 'OneViewStandard'}]

sh_wo_ilo = [
    {'type': 'server-hardware-8', 'name': ENC20SHBAY1, 'licensingIntent': 'OneViewNoiLO'},
    {'type': 'server-hardware-8', 'name': ENC20SHBAY2, 'licensingIntent': 'OneViewNoiLO'},
    {'type': 'server-hardware-8', 'name': ENC20SHBAY3, 'licensingIntent': 'OneViewNoiLO'},
    {'type': 'server-hardware-8', 'name': ENC20SHBAY4, 'licensingIntent': 'OneViewNoiLO'},
    {'type': 'server-hardware-8', 'name': ENC20SHBAY6, 'licensingIntent': 'OneViewNoiLO'},
    {'type': 'server-hardware-8', 'name': ENC20SHBAY8, 'licensingIntent': 'OneViewNoiLO'}]
sh_w_ilo = [
    {'type': 'server-hardware-8', 'name': ENC20SHBAY1, 'licensingIntent': 'OneView'},
    {'type': 'server-hardware-8', 'name': ENC20SHBAY2, 'licensingIntent': 'OneViewNoiLO'},
    {'type': 'server-hardware-8', 'name': ENC20SHBAY3, 'licensingIntent': 'OneViewNoiLO'},
    {'type': 'server-hardware-8', 'name': ENC20SHBAY4, 'licensingIntent': 'OneViewNoiLO'},
    {'type': 'server-hardware-8', 'name': ENC20SHBAY6, 'licensingIntent': 'OneViewNoiLO'},
    {'type': 'server-hardware-8', 'name': ENC20SHBAY8, 'licensingIntent': 'OneView'}]

ligs = [{'name': LIG20_NAME,
         'type': LOGICAL_INTERCONNECT_GROUP_TYPE,
         'enclosureType': 'C7000',
         'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                     {'enclosure': 1,
                                      'enclosureIndex': 1,
                                      'bay': 2,
                                      'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                     {'enclosure': 1,
                                      'enclosureIndex': 1,
                                      'bay': 3,
                                      'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                     {'enclosure': 1,
                                      'enclosureIndex': 1,
                                      'bay': 4,
                                      'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                     {'enclosure': 1,
                                      'enclosureIndex': 1,
                                      'bay': 5,
                                      'type': 'HP VC 8Gb 20-Port FC Module'},
                                     {'enclosure': 1,
                                      'enclosureIndex': 1,
                                      'bay': 6,
                                      'type': 'HP VC 8Gb 20-Port FC Module'},
                                     ],
         'uplinkSets': [],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None}]

enc_groups = [{'name': EG20_NAME,
               'configurationScript': None,
               'interconnectBayMappings':
                   [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:' + LIG20_NAME},
                    {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:' + LIG20_NAME},
                    {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:' + LIG20_NAME},
                    {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:' + LIG20_NAME},
                    {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:' + LIG20_NAME},
                    {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:' + LIG20_NAME},
                    {'interconnectBay': 7, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}]
               }]

patch_server_task_bay3 = [
    {'keyword': 'Patch Server Hardware2',
     'argument': ENC20SHBAY3,
     'taskState': 'Error',
     'timeout': '120',
     'interval': '5',
     'errorMessage': 'SERVER_ALREADY_LICENSED_ILO'}]
patch_server_task_bay8 = [
    {'keyword': 'Patch Server Hardware2',
     'argument': ENC20SHBAY8,
     'taskState': 'Error',
     'timeout': '120',
     'interval': '5',
     'errorMessage': 'SERVER_ALREADY_LICENSED_ILO'}]

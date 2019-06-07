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

Gen10_DLs_With_ilo = [
    {'name': DL160_name,
     'hostname': DL160_IP,
     'licensingIntent': 'OneView',
     'username': 'Administrator',
     'password': 'hpvse123',
     'force': True,
     'configurationState': 'Managed'
     },
    {'name': DL180_name,
     'hostname': DL180_IP,
     'licensingIntent': 'OneView',
     'username': 'Administrator',
     'password': 'hpvse123',
     'force': True,
     'configurationState': 'Managed'
     },
]
Gen10_DLs_Without_ilo = [
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
licensesWithoutIlo = [{'key': 'AA9C DQAA H9PA GHX3 U7B5 HWW5 Y9JL KMPL SR6C MHJU DXAU 2CSM GHTG L762 9AVY WXJY KJVT D5KM EFVW DT5J TFQ9 74C8 SPS9 YG66 Z99R MWSN 6Z84 46XT WZJT HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTVG LS8T XU4E "EVAL-HPOV-NFR2 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR 9G6UAEJGUA4U"'}]

licensesWithIlo = [
    {'key':
        '9A9C DQAA H9PY CHV2 V7B5 HWWB Y9JL KMPL DJKD 5FFM DXAU 2CSM GHTG L762 TT66 VZRY KJVT D5KM EFVW DT5J EBE9 M2CC SPS9 YG66 Z99R MWSN 6Z84 46XT WZJL HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTFG LS8T XU4E "EVAL-HPOV-NFR1 HPOV-NFR1 HP_OneView_16_Seat_NFR 7T36AEJG7JJ9"_3MBSY-CJZY2-LDVV4-92DQT-L6TTW'}]


dl_servers_IPs_keys = [{'server': DL160_name, 'IP': DL160_IP, 'key': '3Q7Z5-2HDVR-CC6R8-6BJQM-9S84B'},
                       {'server': DL180_name, 'IP': DL180_IP, 'key': '3Q7Z5-2HDVR-CC6R8-6BJQM-9S84B'}]

patch_dl_server_task = [
    {'keyword': 'Set Server License with OneView',
     'argument': DL180_name,
     'taskState': 'Error',
     'timeout': '120',
     'interval': '5',
     'errorMessage': 'SERVER_ALREADY_LICENSED_NONE_AVAILABLE'}]

patch_dl_server_task2 = [
    {'keyword': 'Set Server License with OneView',
     'argument': DL180_name,
     'taskState': 'Error',
     'timeout': '120',
     'interval': '5',
     'errorMessage': 'SERVER_ALREADY_LICENSED_PERMANENT'}]

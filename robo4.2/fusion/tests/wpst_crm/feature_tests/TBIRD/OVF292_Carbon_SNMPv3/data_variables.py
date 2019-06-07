
def make_range_list(vrange):
    rlist = []
    for x in xrange(vrange['start'], (vrange['end'] + 1)):
        rlist.append(vrange['prefix'] + str(x) + vrange['suffix'])
    return rlist

SSH_PASS = 'hpvse1'

FUSION_USERNAME = 'Administrator'    # Fusion Appliance Username
FUSION_PASSWORD = 'hpvse123'         # Fusion Appliance Password
FUSION_SSH_USERNAME = 'root'             # Fusion SSH Username
FUSION_SSH_PASSWORD = 'hpvse1'        # Fusion SSH Password
FUSION_PROMPT = '#'               # Fusion Appliance Prompt
FUSION_TIMEOUT = 180              # Timeout.  Move this out???
FUSION_NIC = 'bond0'            # Fusion Appliance Primary NIC
FUSION_NIC_SUFFIX = '%' + FUSION_NIC
FUSION_IP = '15.186.9.20'
IC_SSH_USERNAME = 'root'
IC_TIMEOUT = 100
IC_PROMPT = '>'
APPLIANCE_IP = '15.186.9.20'
admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}
appliance_cred = ['root', 'hpvse1']
ICM_MODEL1 = 'Virtual Connect SE 16Gb FC TAA Module for Synergy'
ICM_MODEL2 = 'Virtual Connect SE 16Gb FC Module for Synergy'
INTERCONNECTS = ['CN750160YS, interconnect 1', 'CN750160YS, interconnect 4']
type = 'IPV4'
OA_USER = 'Administrator'
OA_PASS = 'compaq'
IO_BAY = '5'
V3_host = '15.186.13.8'

V3_user = 'root'
V3_pass = 'password@123'

icm_bays = ['1', '4']

LE1 = 'LE1'
LIG1 = 'LIG1'


time = 300
tm = 300
ic_bay = '1'
Trap_details = 'noPriv\n\nSNMPv3'
Users_details = 'Trap/Inform'

Trap_dest = '15.186.13.8'
Trap_usr = '162\\n Trap User: '
Trap_name = '\\n'

user_left = '\\n'
Users = 'User 1 (rw):'
User = '\\n\\tAuth'
trap = '\nTRAP..'
split_trap = 'Trap Entry'
name = [' ', '1 (rw): ', '2 (rw): ', '3 (rw): ', '4 (ro): ', '5 (ro): ', '6 (ro): ']
Engine_match = ']'
temp_engine_id = '00:00:00:00:00:00:00:00:00'

match = '\\n\\nSNMPv3 \']'

split_password = 'root'
snmpv1_trap_split = 'Community'
trap_ip1 = '15.186.13.8'
var = ''
enc_count = 1

ENC1 = 'CN750160YS'
ENC2 = 'XXXXXXXXXX'
ENC3 = 'XXXXXXXXXX'
ENC4 = 'XXXXXXXXXX'
ENC5 = 'XXXXXXXXXX'

Enc1Map = \
    [
        {'bay': 1, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1},
        {'bay': 4, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1}
    ]

Enc1MapASide = \
    [
        {'bay': 1, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1}
    ]

Enc1MapBSide = \
    [
        {'bay': 4, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1}
    ]

###
# Interconnect bays configurations
# 2 Enclosures, Fabric 3
###

Enc2Map = \
    [
        {'bay': 1, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1},
        {'bay': 4, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1},
        {'bay': 1, 'enclosure': -2, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -2},
        {'bay': 4, 'enclosure': -2, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -2}
    ]

Enc2MapASide = \
    [
        {'bay': 1, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1},
        {'bay': 1, 'enclosure': -2, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -2},
    ]

Enc2MapBSide = \
    [
        {'bay': 4, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1},
        {'bay': 4, 'enclosure': -2, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -2}
    ]

###
# Interconnect bays configurations
# 3 Enclosures, Fabric 3
###

Enc3bay3ICMMap = \
    [
        {'bay': 1, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1},
        {'bay': 4, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1},
        {'bay': 1, 'enclosure': -2, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -2},
        {'bay': 4, 'enclosure': -2, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -2},
        {'bay': 1, 'enclosure': -3, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -3},
        {'bay': 4, 'enclosure': -3, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -3}
    ]

Enc3MapASide = \
    [
        {'bay': 1, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1},
        {'bay': 1, 'enclosure': -2, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -2},
        {'bay': 1, 'enclosure': -3, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -3}

    ]

Enc3MapBSide = \
    [
        {'bay': 4, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1},
        {'bay': 4, 'enclosure': -2, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -2},
        {'bay': 4, 'enclosure': -3, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -3}
    ]

###
# Interconnect bays configurations
# 4 Enclosures, Fabric 3
###

Enc4Map = \
    [
        {'bay': 1, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1},
        {'bay': 4, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -2},
        {'bay': 1, 'enclosure': -2, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1},
        {'bay': 4, 'enclosure': -2, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -2},
        {'bay': 1, 'enclosure': -3, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -3},
        {'bay': 4, 'enclosure': -3, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -3},
        {'bay': 1, 'enclosure': -4, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -4},
        {'bay': 4, 'enclosure': -4, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -4}
    ]

###
# Interconnect bays configurations
# 5 Enclosures, Fabric 3
###

Enc5Map = \
    [
        {'bay': 1, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1},
        {'bay': 4, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -2},
        {'bay': 1, 'enclosure': -2, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1},
        {'bay': 4, 'enclosure': -2, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -2},
        {'bay': 1, 'enclosure': -3, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -3},
        {'bay': 4, 'enclosure': -3, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -3},
        {'bay': 1, 'enclosure': -4, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -4},
        {'bay': 4, 'enclosure': -4, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -4},
        {'bay': 1, 'enclosure': -5, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -5},
        {'bay': 4, 'enclosure': -5, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -5}
    ]

uplink_sets = {'UplinkSet_1': {'name': 'UplinkSet_1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_1'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                               'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': 'Q1:1', 'speed': 'Auto'}]},
               'UplinkSet_2': {'name': 'UplinkSet_2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_2'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                               'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '-1', 'port': '1', 'speed': 'Speed16G'}]}}

LIG_new = {
    'name': 'LIG1',
    'interconnectMapTemplate': Enc1Map,
    'enclosureIndexes': [-1],
    'interconnectBaySet': 1,
    'redundancyType': 'Redundant',
    'uplinkSets': [uplink_sets['UplinkSet_1'].copy(), uplink_sets['UplinkSet_2'].copy()],
}

LIG_2_enc = {'name': 'LIG_2_enc',
             'interconnectMapTemplate': Enc2Map,
             'enclosureIndexes': [-1, -2],
             'interconnectBaySet': 1,
             'redundancyType': 'Redundant',
             'uplinkSets': []}

LIG_3_enc = {'name': 'LIG_3_enc',
             'interconnectMapTemplate': Enc3bay3ICMMap,
             'enclosureIndexes': [-1, -2, -3],
             'interconnectBaySet': 3,
             'redundancyType': 'Redundant',
             'uplinkSets': [],
             }

LIG_4_enc = {
    'name': 'LIG_4_enc',
    'interconnectMapTemplate': Enc4Map,
    'enclosureIndexes': [-1, -2, -3, -4],
    'interconnectBaySet': 3,
    'redundancyType': 'Redundant',
    'uplinkSets': [],
}


Edit_Uplink_Port = {'associatedUplinkSetUri': '',
                    'interconnectName': '',
                    'portType': 'Uplink',
                    'portId': '',
                    'portHealthStatus': '',
                    'capability': ['FibreChannel'],
                    'configPortTypes': ['FibreChannel'],
                    'enabled': '',
                    'portName': '',
                    'portStatus': '',
                    'type': 'port'}

downlink_port_disable = {'interconnectName': '',
                         'portType': 'Downlink',
                         'portId': '',
                         'capability': ['FibreChannel'],
                         'configPortTypes': ['FibreChannel'],
                         'enabled': '',
                         'portName': '',
                         'portStatus': '',
                         'type': 'port'}

power_value = ['Off', 'On']
edit_power_body = {'op': 'replace',
                   'path': '/powerState',
                   'value': ''}

valDict = {'status_code': 200,
           'taskState': 'Completed'}


###
# Linked_Uplink_port_id = ['32', '32']
# Linked_Uplink_port = ['Q1:1', 'Q1:1']
###

Linked_Uplink_port = ['1', '1']
Linked_Uplink_port_id = ['25', '25']
Linked_downlink_port = ['d1', 'd1', 'd2']
Linked_downlink_port_id = ['1', '1']

edit_SNMPv1_body = {'readCommunity': 'public',
                    'enabled': '',
                    'systemContact': '',
                    'snmpAccess': [],
                    'trapDestinations': [
                        {'enetTrapCategories': ['PortStatus'],
                         'vcmTrapCategories': ['Legacy'],
                         'trapSeverities': ['Normal', 'Info', 'Warning'],
                         'communityString': 'public',
                         'fcTrapCategories': ['PortStatus'],
                         'trapDestination': 'dest',
                         'trapFormat': 'SNMPv1'
                         }],
                    'type': 'snmp-configuration'
                    }


snmp_config = 'snmp-configuration'
invalid_password = 'talent@123'

SNMPV3_LI_body_md5_des = {'category': 'snmp-configuration',
                          'enabled': 'false',
                          'readCommunity': 'public',
                          'snmpAccess': [],
                          'snmpUsers': [{'snmpV3UserName': 'e20sysadminmd5des',
                                         'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword',
                                                              'value': 'password',
                                                              'valueFormat': 'SecuritySensitive',
                                                              'valueType': 'String'},
                                                             {'propertyName': 'SnmpV3PrivacyPassword',
                                                              'value': 'password',
                                                              'valueFormat': 'SecuritySensitive',
                                                              'valueType': 'String'}],
                                         'v3AuthProtocol': 'MD5',
                                         'v3PrivacyProtocol': 'DES56'}],
                          'trapDestinations': [{'communityString': '',
                                                'enetTrapCategories': [],
                                                'fcTrapCategories': [],
                                                'inform': 'false',
                                                'port': '162',
                                                'trapDestination': '15.186.13.8',
                                                'trapFormat': 'SNMPv3',
                                                'trapSeverities': [],
                                                'userName': 'e20sysadminmd5des',
                                                'vcmTrapCategories': []}],
                          'type': 'snmp-configuration',
                          'uri': '',
                          'v3Enabled': 'true'}

SNMPV3_LI_body_149_md5_des = {'category': 'snmp-configuration',
                              'enabled': 'false',
                              'readCommunity': 'public',
                              'snmpAccess': [],
                              'snmpUsers': [{'snmpV3UserName': 'e20149sysadminmd5des',
                                             'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword',
                                                                  'value': 'challenge',
                                                                  'valueFormat': 'SecuritySensitive',
                                                                  'valueType': 'String'},
                                                                 {'propertyName': 'SnmpV3PrivacyPassword',
                                                                  'value': 'challenge',
                                                                  'valueFormat': 'SecuritySensitive',
                                                                  'valueType': 'String'}],
                                             'v3AuthProtocol': 'MD5',
                                             'v3PrivacyProtocol': 'DES56'}],
                              'trapDestinations': [{'communityString': '',
                                                    'enetTrapCategories': [],
                                                    'fcTrapCategories': [],
                                                    'inform': 'false',
                                                    'port': '162',
                                                    'trapDestination': '15.186.21.149',
                                                    'trapFormat': 'SNMPv3',
                                                    'trapSeverities': [],
                                                    'userName': 'e20149sysadminmd5des',
                                                    'vcmTrapCategories': []}],
                              'type': 'snmp-configuration',
                              'uri': '',
                              'v3Enabled': 'true'}


SNMPV3_LI_body_md5_aes = {'category': 'snmp-configuration',
                          'enabled': 'false',
                          'readCommunity': 'public',
                          'snmpAccess': [],
                          'snmpUsers': [{'snmpV3UserName': 'e20sysadminmd5aes',
                                         'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword',
                                                              'value': 'password',
                                                              'valueFormat': 'SecuritySensitive',
                                                              'valueType': 'String'},
                                                             {'propertyName': 'SnmpV3PrivacyPassword',
                                                              'value': 'password',
                                                              'valueFormat': 'SecuritySensitive',
                                                              'valueType': 'String'}],
                                         'v3AuthProtocol': 'MD5',
                                         'v3PrivacyProtocol': 'AES128'}],
                          'trapDestinations': [{'communityString': '',
                                                'enetTrapCategories': [],
                                                'fcTrapCategories': [],
                                                'inform': 'true',
                                                'port': '162',
                                                'engineId': '0x80001F888071F26C0ED6B8E15800000000',
                                                'trapDestination': '15.186.13.8',
                                                'trapFormat': 'SNMPv3',
                                                'trapSeverities': [],
                                                'userName': 'e20sysadminmd5aes',
                                                'vcmTrapCategories': []}],
                          'type': 'snmp-configuration',
                          'uri': '',
                          'v3Enabled': 'true'}

v1_trap = {'communityString': 'public', 'enetTrapCategories': [], 'fcTrapCategories': [], 'port': '162',
           'trapDestination': '15.186.13.8', 'trapFormat': 'SNMPv1', 'trapSeverities': [], 'vcmTrapCategories': []}

v1_trap_list = [{'communityString': 'public', 'enetTrapCategories': [], 'fcTrapCategories':[], 'port':'162',
                 'trapDestination':'15.186.13.8', 'trapFormat': 'SNMPv1', 'trapSeverities':[], 'vcmTrapCategories':[]}]
true = 'true'
alternate_trap_ip = '15.186.21.149'

SNMPV3_LI_body_all_users = {'category': 'snmp-configuration',
                            'enabled': 'false',
                            'readCommunity': 'public',
                            'snmpAccess': [],
                            'snmpUsers': [{'snmpV3UserName': 'e20sysadminnone',
                                           'userCredentials': [],
                                           'v3AuthProtocol': 'NA', 'v3PrivacyProtocol': 'NA'},
                                          {'snmpV3UserName': 'e20sysadminshaaes',
                                           'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                                'valueFormat': 'SecuritySensitive', 'valueType': 'String'},
                                                               {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password',
                                                                'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                           'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'},
                                          {'snmpV3UserName': 'e20sysadminmd5aes',
                                           'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                                'valueFormat': 'SecuritySensitive', 'valueType': 'String'},
                                                               {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password',
                                                                'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                           'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'},
                                          {'snmpV3UserName': 'e20sysadminmd5des',
                                           'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                                'valueFormat': 'SecuritySensitive', 'valueType': 'String'},
                                                               {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password',
                                                                'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                           'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                                          {'snmpV3UserName': 'e20sysadminshades',
                                           'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                                'valueFormat': 'SecuritySensitive', 'valueType': 'String'},
                                                               {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password',
                                                                'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                           'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                          {'snmpV3UserName': 'e20sysadminsha',
                                           'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                                'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                           'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'}],
                            'trapDestinations': [{'communityString': '',
                                                  'enetTrapCategories': [],
                                                  'fcTrapCategories': [],
                                                  'inform': 'false',
                                                  'port': '162',
                                                  'trapDestination': '15.186.13.8',
                                                  'trapFormat': 'SNMPv3',
                                                  'trapSeverities': [],
                                                  'userName': 'e20sysadminmd5des',
                                                  'vcmTrapCategories': []}],
                            'type': 'snmp-configuration',
                            'uri': '',
                            'v3Enabled': 'true'}

trap_users_list = ['e20sysadminshaaes', 'e20sysadminsha', 'e20sysadminmd5aes', 'e20sysadminnone']

invalid_userCredentials = [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'HPEoneview',
                            'valueFormat': 'SecuritySensitive', 'valueType': 'String'},
                           {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'HPEoneview',
                            'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]

LI_consistent = 'CONSISTENT'
LI_Inconsistent = 'NOT_CONSISTENT'
IC_state = 'Configured'

engine_id = '0x80001F888071F26C0ED6B8E15800000000'
engine_id1 = '0x80000634B2100000110A00D1D9'
invalid_engine_id = '888071F26C0ED6B'

SNMPV3_LI_body_7_users = {'category': 'snmp-configuration',
                          'enabled': 'false',
                          'readCommunity': 'public',
                          'snmpAccess': [],
                          'snmpUsers': [{'snmpV3UserName': 'e20sysadminnone',
                                         'userCredentials': [],
                                         'v3AuthProtocol': 'NA', 'v3PrivacyProtocol': 'NA'},
                                        {'snmpV3UserName': 'e20sysadminshaaes',
                                         'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                              'valueFormat': 'SecuritySensitive', 'valueType': 'String'},
                                                             {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password',
                                                              'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                         'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'},
                                        {'snmpV3UserName': 'e20sysadminmd5aes',
                                         'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                              'valueFormat': 'SecuritySensitive', 'valueType': 'String'},
                                                             {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password',
                                                              'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                         'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'},
                                        {'snmpV3UserName': 'e20sysadminmd5des',
                                         'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                              'valueFormat': 'SecuritySensitive', 'valueType': 'String'},
                                                             {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password',
                                                              'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                         'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                                        {'snmpV3UserName': 'e20sysadminshades',
                                         'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                              'valueFormat': 'SecuritySensitive', 'valueType': 'String'},
                                                             {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password',
                                                              'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                         'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                        {'snmpV3UserName': 'e20sysadminsha',
                                         'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                              'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                         'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                                        {'snmpV3UserName': 'e20sysadminmd5',
                                         'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                              'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                         'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'NA'}],
                          'trapDestinations': [{'communityString': '',
                                                'enetTrapCategories': [],
                                                'fcTrapCategories': [],
                                                'inform': 'false',
                                                'port': '162',
                                                'trapDestination': '15.186.13.8',
                                                'trapFormat': 'SNMPv3',
                                                'trapSeverities': [],
                                                'userName': 'e20sysadminmd5des',
                                                'vcmTrapCategories': []}],
                          'type': 'snmp-configuration',
                          'uri': '',
                          'v3Enabled': 'true'}


SNMPV3_LI_body_sha_aes = {'category': 'snmp-configuration',
                          'enabled': 'false',
                          'readCommunity': 'public',
                          'snmpAccess': [],
                          'snmpUsers': [{'snmpV3UserName': 'e20sysadminshaaes',
                                         'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword',
                                                              'value': 'password',
                                                              'valueFormat': 'SecuritySensitive',
                                                              'valueType': 'String'},
                                                             {'propertyName': 'SnmpV3PrivacyPassword',
                                                              'value': 'password',
                                                              'valueFormat': 'SecuritySensitive',
                                                              'valueType': 'String'}],
                                         'v3AuthProtocol': 'SHA',
                                         'v3PrivacyProtocol': 'AES128'}],
                          'trapDestinations': [{'communityString': '',
                                                'enetTrapCategories': [],
                                                'fcTrapCategories': [],
                                                'inform': 'false',
                                                'port': '162',
                                                'trapDestination': '15.186.13.8',
                                                'trapFormat': 'SNMPv3',
                                                'trapSeverities': [],
                                                'userName': 'e20sysadminshaaes',
                                                'vcmTrapCategories': []}],
                          'type': 'snmp-configuration',
                          'uri': '',
                          'v3Enabled': 'true'}

SNMPV1_LIG_body = {'category': 'snmp-configuration',
                   'enabled': 'true',
                   'readCommunity': 'public',
                   'snmpAccess': [],
                   'snmpUsers': [],
                   'trapDestinations': [{'communityString': 'Public',
                                         'enetTrapCategories': [],
                                         'fcTrapCategories': [],
                                         'inform': 'false',
                                         'port': '162',
                                         'trapDestination': '15.186.13.8',
                                         'trapFormat': 'SNMPv1',
                                         'trapSeverities': [],
                                         'vcmTrapCategories': []}],
                   'type': 'snmp-configuration',
                   'uri': '',
                   'v3Enabled': 'false'}


SNMPV3_LI_body_sha_des = {'category': 'snmp-configuration',
                          'enabled': 'false',
                          'readCommunity': 'public',
                          'snmpAccess': [],
                          'snmpUsers': [{'snmpV3UserName': 'e20sysadminshades',
                                         'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword',
                                                              'value': 'password',
                                                              'valueFormat': 'SecuritySensitive',
                                                              'valueType': 'String'},
                                                             {'propertyName': 'SnmpV3PrivacyPassword',
                                                              'value': 'password',
                                                              'valueFormat': 'SecuritySensitive',
                                                              'valueType': 'String'}],
                                         'v3AuthProtocol': 'SHA',
                                         'v3PrivacyProtocol': 'DES56'}],
                          'trapDestinations': [{'communityString': '',
                                                'enetTrapCategories': [],
                                                'fcTrapCategories': [],
                                                'inform': 'false',
                                                'port': '162',
                                                'trapDestination': '15.186.13.8',
                                                'trapFormat': 'SNMPv3',
                                                'trapSeverities': [],
                                                'userName': 'e20sysadminshades',
                                                'vcmTrapCategories': []}],
                          'type': 'snmp-configuration',
                          'uri': '',
                          'v3Enabled': 'true'}


SNMPV3_LI_body_md5 = {'category': 'snmp-configuration',
                      'enabled': 'false',
                      'readCommunity': 'public',
                      'snmpAccess': [],
                      'snmpUsers': [{'snmpV3UserName': 'e20sysadminmd5',
                                     'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword',
                                                          'value': 'password',
                                                          'valueFormat': 'SecuritySensitive',
                                                          'valueType': 'String'}],
                                     'v3AuthProtocol': 'MD5',
                                     'v3PrivacyProtocol': 'NA'}],
                      'trapDestinations': [{'communityString': '',
                                            'enetTrapCategories': [],
                                            'fcTrapCategories': [],
                                            'inform': 'false',
                                            'port': '162',
                                            'trapDestination': '15.186.13.8',
                                            'trapFormat': 'SNMPv3',
                                            'trapSeverities': [],
                                            'userName': 'e20sysadminmd5',
                                            'vcmTrapCategories': []}],
                      'type': 'snmp-configuration',
                      'uri': '',
                      'v3Enabled': 'true'}

li_invalid_trap_body = [{'communityString': '',
                         'enetTrapCategories': [],
                         'fcTrapCategories': [],
                         'inform': 'false',
                         'port': '162',
                         'trapDestination': '15.186.13.8',
                         'trapFormat': 'SNMPv3',
                         'trapSeverities': [],
                         'userName': 'e20sysadminmd5',
                         'vcmTrapCategories': []},
                        {'communityString': '',
                         'enetTrapCategories': [],
                         'fcTrapCategories': [],
                         'inform': 'false',
                         'port': '162',
                         'trapDestination': '15.186.13.8',
                         'trapFormat': 'SNMPv3',
                         'trapSeverities': [],
                         'userName': 'e20sysadminshaaes',
                         'vcmTrapCategories': []
                         }]

lig_duplicate_trap_ip = [{'communityString': '',
                          'enetTrapCategories': [],
                          'fcTrapCategories': [],
                          'inform': 'false',
                          'port': '162',
                          'trapDestination': '15.186.13.8',
                          'trapFormat': 'SNMPv3',
                          'trapSeverities': [],
                          'userName': 'e20sysadminmd5aes',
                          'vcmTrapCategories': []},
                         {'communityString': '',
                          'enetTrapCategories': [],
                          'fcTrapCategories': [],
                          'inform': 'false',
                          'port': '162',
                          'trapDestination': '15.186.13.8',
                          'trapFormat': 'SNMPv3',
                          'trapSeverities': [],
                          'userName': 'e20sysadminsha',
                          'vcmTrapCategories': []
                          }]


lig_invalid_trap_body = [{'communityString': '',
                          'enetTrapCategories': [],
                          'fcTrapCategories': [],
                          'inform': 'false',
                          'port': '162',
                          'trapDestination': '15.186.13.8',
                          'trapFormat': 'SNMPv3',
                          'trapSeverities': [],
                          'userName': 'e20sysadminsha',
                          'vcmTrapCategories': []},
                         {'communityString': '',
                          'enetTrapCategories': [],
                          'fcTrapCategories': [],
                          'inform': 'false',
                          'port': '162',
                          'trapDestination': '15.186.13.8',
                          'trapFormat': 'SNMPv3',
                          'trapSeverities': [],
                          'userName': 'e20sysadminsha',
                          'vcmTrapCategories': []
                          }]

lig_duplicate_trap_user = {'communityString': '',
                           'enetTrapCategories': [],
                           'fcTrapCategories': [],
                           'inform': 'false',
                           'port': '162',
                           'trapDestination': '15.186.13.8',
                           'trapFormat': 'SNMPv3',
                           'trapSeverities': [],
                           'userName': 'e20sysadminshades',
                           'vcmTrapCategories': []
                           }

SNMPV3_LI_body_6_trap = {'category': 'snmp-configuration',
                         'enabled': 'false',
                         'readCommunity': 'public',
                         'snmpAccess': [],
                         'snmpUsers': [{'snmpV3UserName': 'e20sysadminshaaes',
                                        'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                             'valueFormat': 'SecuritySensitive', 'valueType': 'String'},
                                                            {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password',
                                                             'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                        'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}],
                         'trapDestinations': [{'communityString': '',
                                               'enetTrapCategories': [],
                                               'fcTrapCategories': [],
                                               'inform': 'false',
                                               'port': '162',
                                               'trapDestination': '15.186.13.1',
                                               'trapFormat': 'SNMPv3',
                                               'trapSeverities': [],
                                               'userName': 'e20sysadminshaaes',
                                               'vcmTrapCategories': []},
                                              {'communityString': '',
                                               'enetTrapCategories': [],
                                               'fcTrapCategories': [],
                                               'inform': 'false',
                                               'port': '162',
                                               'trapDestination': '15.186.13.2',
                                               'trapFormat': 'SNMPv3',
                                               'trapSeverities': [],
                                               'userName': 'e20sysadminshaaes',
                                               'vcmTrapCategories': []},
                                              {'communityString': '',
                                               'enetTrapCategories': [],
                                               'fcTrapCategories': [],
                                               'inform': 'false',
                                               'port': '162',
                                               'trapDestination': '15.186.13.3',
                                               'trapFormat': 'SNMPv3',
                                               'trapSeverities': [],
                                               'userName': 'e20sysadminshaaes',
                                               'vcmTrapCategories': []},
                                              {'communityString': '',
                                               'enetTrapCategories': [],
                                               'fcTrapCategories': [],
                                               'inform': 'false',
                                               'port': '162',
                                               'trapDestination': '15.186.13.4',
                                               'trapFormat': 'SNMPv3',
                                               'trapSeverities': [],
                                               'userName': 'e20sysadminshaaes',
                                               'vcmTrapCategories': []},
                                              {'communityString': '',
                                               'enetTrapCategories': [],
                                               'fcTrapCategories': [],
                                               'inform': 'false',
                                               'port': '162',
                                               'trapDestination': '15.186.13.5',
                                               'trapFormat': 'SNMPv3',
                                               'trapSeverities': [],
                                               'userName': 'e20sysadminshaaes',
                                               'vcmTrapCategories': []},
                                              {'communityString': '',
                                               'enetTrapCategories': [],
                                               'fcTrapCategories': [],
                                               'inform': 'false',
                                               'port': '162',
                                               'trapDestination': '15.186.13.6',
                                               'trapFormat': 'SNMPv3',
                                               'trapSeverities': [],
                                               'userName': 'e20sysadminshaaes',
                                               'vcmTrapCategories': []}],
                         'type': 'snmp-configuration',
                         'uri': '',
                         'v3Enabled': 'true'}

SNMPV3_LI_body_invalid_trap_user = {'category': 'snmp-configuration',
                                    'enabled': 'false',
                                    'readCommunity': 'public',
                                    'snmpAccess': [],
                                    'snmpUsers': [{'snmpV3UserName': 'e20sysadminshaaes',
                                                   'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                                        'valueFormat': 'SecuritySensitive', 'valueType': 'String'},
                                                                       {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password',
                                                                        'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                                   'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}],
                                    'trapDestinations': [{'communityString': '',
                                                          'enetTrapCategories': [],
                                                          'fcTrapCategories': [],
                                                          'inform': 'false',
                                                          'port': '162',
                                                          'trapDestination': '15.186.13.1',
                                                          'trapFormat': 'SNMPv3',
                                                          'trapSeverities': [],
                                                          'userName': 'e20sysadminmd5',
                                                          'vcmTrapCategories': []}],
                                    'type': 'snmp-configuration',
                                    'uri': '',
                                    'v3Enabled': 'true'}

snmpv3_li_body_6_users_7_traps = {'category': 'snmp-configuration',
                                  'enabled': 'false',
                                  'readCommunity': 'public',
                                  'snmpAccess': [],
                                  'snmpUsers': [{'snmpV3UserName': 'e20sysadminshaaes',
                                                 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                                      'valueFormat': 'SecuritySensitive', 'valueType': 'String'},
                                                                     {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password',
                                                                      'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                                 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'},
                                                {'snmpV3UserName': 'e20sysadminmd5aes',
                                                 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                                      'valueFormat': 'SecuritySensitive', 'valueType': 'String'},
                                                                     {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password',
                                                                      'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                                 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'},
                                                {'snmpV3UserName': 'e20sysadminmd5des',
                                                 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                                      'valueFormat': 'SecuritySensitive', 'valueType': 'String'},
                                                                     {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password',
                                                                      'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                                 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                                                {'snmpV3UserName': 'e20sysadminshades',
                                                 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                                      'valueFormat': 'SecuritySensitive', 'valueType': 'String'},
                                                                     {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password',
                                                                      'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                                 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                                {'snmpV3UserName': 'e20sysadminsha',
                                                 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                                      'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                                 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                                                {'snmpV3UserName': 'e20sysadminmd5',
                                                 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                                      'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                                 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'NA'}],
                                  'trapDestinations': [{'communityString': '',
                                                        'enetTrapCategories': [],
                                                        'fcTrapCategories': [],
                                                        'inform': 'false',
                                                        'port': '162',
                                                        'trapDestination': '15.186.13.1',
                                                        'trapFormat': 'SNMPv3',
                                                        'trapSeverities': [],
                                                        'userName': 'e20sysadminshaaes',
                                                        'vcmTrapCategories': []},
                                                       {'communityString': '',
                                                        'enetTrapCategories': [],
                                                        'fcTrapCategories': [],
                                                        'inform': 'false',
                                                        'port': '162',
                                                        'trapDestination': '15.186.13.2',
                                                        'trapFormat': 'SNMPv3',
                                                        'trapSeverities': [],
                                                        'userName': 'e20sysadminshades',
                                                        'vcmTrapCategories': []},
                                                       {'communityString': '',
                                                        'enetTrapCategories': [],
                                                        'fcTrapCategories': [],
                                                        'inform': 'false',
                                                        'port': '162',
                                                        'trapDestination': '15.186.13.3',
                                                        'trapFormat': 'SNMPv3',
                                                        'trapSeverities': [],
                                                        'userName': 'e20sysadminmd5aes',
                                                        'vcmTrapCategories': []},
                                                       {'communityString': '',
                                                        'enetTrapCategories': [],
                                                        'fcTrapCategories': [],
                                                        'inform': 'false',
                                                        'port': '162',
                                                        'trapDestination': '15.186.13.4',
                                                        'trapFormat': 'SNMPv3',
                                                        'trapSeverities': [],
                                                        'userName': 'e20sysadminmd5des',
                                                        'vcmTrapCategories': []},
                                                       {'communityString': '',
                                                        'enetTrapCategories': [],
                                                        'fcTrapCategories': [],
                                                        'inform': 'false',
                                                        'port': '162',
                                                        'trapDestination': '15.186.13.5',
                                                        'trapFormat': 'SNMPv3',
                                                        'trapSeverities': [],
                                                        'userName': 'e20sysadminsha',
                                                        'vcmTrapCategories': []},
                                                       {'communityString': '',
                                                        'enetTrapCategories': [],
                                                        'fcTrapCategories': [],
                                                        'inform': 'false',
                                                        'port': '162',
                                                        'trapDestination': '15.186.13.6',
                                                        'trapFormat': 'SNMPv3',
                                                        'trapSeverities': [],
                                                        'userName': 'e20sysadminmd5',
                                                        'vcmTrapCategories': []},
                                                       {'communityString': '',
                                                        'enetTrapCategories': [],
                                                        'fcTrapCategories': [],
                                                        'inform': 'false',
                                                        'port': '162',
                                                        'trapDestination': '15.186.13.6',
                                                        'trapFormat': 'SNMPv3',
                                                        'trapSeverities': [],
                                                        'userName': 'e20sysadminshaaes',
                                                        'vcmTrapCategories': []}],
                                  'type': 'snmp-configuration',
                                  'uri': '',
                                  'v3Enabled': 'true'}


snmpv1_li_body_6_traps = {'category': 'snmp-configuration',
                          'enabled': 'false',
                          'readCommunity': 'public',
                          'snmpAccess': [],
                          'snmpUsers': [],
                          'trapDestinations': [{'communityString': '',
                                                'enetTrapCategories': [],
                                                'fcTrapCategories': [],
                                                'inform': 'false',
                                                'port': '162',
                                                'trapDestination': '15.186.13.1',
                                                'trapFormat': 'SNMPv1',
                                                'trapSeverities': [],
                                                'userName': 'e20sysadminshaaes',
                                                'vcmTrapCategories': []},
                                               {'communityString': '',
                                                'enetTrapCategories': [],
                                                'fcTrapCategories': [],
                                                'inform': 'false',
                                                'port': '162',
                                                'trapDestination': '15.186.13.2',
                                                'trapFormat': 'SNMPv1',
                                                'trapSeverities': [],
                                                'userName': 'e20sysadminshades',
                                                'vcmTrapCategories': []},
                                               {'communityString': '',
                                                'enetTrapCategories': [],
                                                'fcTrapCategories': [],
                                                'inform': 'false',
                                                'port': '162',
                                                'trapDestination': '15.186.13.3',
                                                'trapFormat': 'SNMPv1',
                                                'trapSeverities': [],
                                                'userName': 'e20sysadminmd5aes',
                                                'vcmTrapCategories': []},
                                               {'communityString': '',
                                                'enetTrapCategories': [],
                                                'fcTrapCategories': [],
                                                'inform': 'false',
                                                'port': '162',
                                                'trapDestination': '15.186.13.4',
                                                'trapFormat': 'SNMPv1',
                                                'trapSeverities': [],
                                                'userName': 'e20sysadminmd5des',
                                                'vcmTrapCategories': []},
                                               {'communityString': '',
                                                'enetTrapCategories': [],
                                                'fcTrapCategories': [],
                                                'inform': 'false',
                                                'port': '162',
                                                'trapDestination': '15.186.13.5',
                                                'trapFormat': 'SNMPv1',
                                                'trapSeverities': [],
                                                'userName': 'e20sysadminsha',
                                                'vcmTrapCategories': []},
                                               {'communityString': '',
                                                'enetTrapCategories': [],
                                                'fcTrapCategories': [],
                                                'inform': 'false',
                                                'port': '162',
                                                'trapDestination': '15.186.13.6',
                                                'trapFormat': 'SNMPv1',
                                                'trapSeverities': [],
                                                'userName': 'e20sysadminmd5',
                                                'vcmTrapCategories': []}],
                          'type': 'snmp-configuration',
                          'uri': '',
                          'v3Enabled': 'true'}

snmpv1_li_body_6snmpv3traps_5snmpv1traps = {'category': 'snmp-configuration',
                                            'enabled': 'false',
                                            'readCommunity': 'public',
                                            'snmpAccess': [],
                                            'snmpUsers': [{'snmpV3UserName': 'e20sysadminshaaes',
                                                           'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                                                'valueFormat': 'SecuritySensitive', 'valueType': 'String'},
                                                                               {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password',
                                                                                'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                                           'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'},
                                                          {'snmpV3UserName': 'e20sysadminmd5aes',
                                                           'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                                                'valueFormat': 'SecuritySensitive', 'valueType': 'String'},
                                                                               {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password',
                                                                                'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                                           'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'},
                                                          {'snmpV3UserName': 'e20sysadminmd5des',
                                                           'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                                                'valueFormat': 'SecuritySensitive', 'valueType': 'String'},
                                                                               {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password',
                                                                                'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                                           'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                                                          {'snmpV3UserName': 'e20sysadminshades',
                                                           'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                                                'valueFormat': 'SecuritySensitive', 'valueType': 'String'},
                                                                               {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password',
                                                                                'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                                           'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                                          {'snmpV3UserName': 'e20sysadminsha',
                                                           'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                                                'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                                           'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                                                          {'snmpV3UserName': 'e20sysadminmd5',
                                                           'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                                                'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                                           'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'NA'}],
                                            'trapDestinations': [{'communityString': '',
                                                                  'enetTrapCategories': [],
                                                                  'fcTrapCategories': [],
                                                                  'inform': 'false',
                                                                  'port': '162',
                                                                  'trapDestination': '15.186.13.2',
                                                                  'trapFormat': 'SNMPv3',
                                                                  'trapSeverities': [],
                                                                  'userName': 'e20sysadminshades',
                                                                  'vcmTrapCategories': []},
                                                                 {'communityString': '',
                                                                  'enetTrapCategories': [],
                                                                  'fcTrapCategories': [],
                                                                  'inform': 'false',
                                                                  'port': '162',
                                                                  'trapDestination': '15.186.13.3',
                                                                  'trapFormat': 'SNMPv3',
                                                                  'trapSeverities': [],
                                                                  'userName': 'e20sysadminmd5aes',
                                                                  'vcmTrapCategories': []},
                                                                 {'communityString': '',
                                                                  'enetTrapCategories': [],
                                                                  'fcTrapCategories': [],
                                                                  'inform': 'false',
                                                                  'port': '162',
                                                                  'trapDestination': '15.186.13.4',
                                                                  'trapFormat': 'SNMPv3',
                                                                  'trapSeverities': [],
                                                                  'userName': 'e20sysadminmd5des',
                                                                  'vcmTrapCategories': []},
                                                                 {'communityString': '',
                                                                  'enetTrapCategories': [],
                                                                  'fcTrapCategories': [],
                                                                  'inform': 'false',
                                                                  'port': '162',
                                                                  'trapDestination': '15.186.13.5',
                                                                  'trapFormat': 'SNMPv3',
                                                                  'trapSeverities': [],
                                                                  'userName': 'e20sysadminsha',
                                                                  'vcmTrapCategories': []},
                                                                 {'communityString': '',
                                                                  'enetTrapCategories': [],
                                                                  'fcTrapCategories': [],
                                                                  'inform': 'false',
                                                                  'port': '162',
                                                                  'trapDestination': '15.186.13.6',
                                                                  'trapFormat': 'SNMPv3',
                                                                  'trapSeverities': [],
                                                                  'userName': 'e20sysadminmd5',
                                                                  'vcmTrapCategories': []},
                                                                 {'communityString': '',
                                                                  'enetTrapCategories': [],
                                                                  'fcTrapCategories': [],
                                                                  'inform': 'false',
                                                                  'port': '162',
                                                                  'trapDestination': '15.186.13.7',
                                                                  'trapFormat': 'SNMPv3',
                                                                  'trapSeverities': [],
                                                                  'userName': 'e20sysadminshaaes',
                                                                  'vcmTrapCategories': []},
                                                                 {'communityString': '',
                                                                  'enetTrapCategories': [],
                                                                  'fcTrapCategories': [],
                                                                  'inform': 'false',
                                                                  'port': '162',
                                                                  'trapDestination': '15.186.13.1',
                                                                  'trapFormat': 'SNMPv1',
                                                                  'trapSeverities': [],
                                                                  'userName': 'e20sysadminshaaes',
                                                                  'vcmTrapCategories': []},
                                                                 {'communityString': '',
                                                                  'enetTrapCategories': [],
                                                                  'fcTrapCategories': [],
                                                                  'inform': 'false',
                                                                  'port': '162',
                                                                  'trapDestination': '15.186.13.2',
                                                                  'trapFormat': 'SNMPv1',
                                                                  'trapSeverities': [],
                                                                  'userName': 'e20sysadminshades',
                                                                  'vcmTrapCategories': []},
                                                                 {'communityString': '',
                                                                  'enetTrapCategories': [],
                                                                  'fcTrapCategories': [],
                                                                  'inform': 'false',
                                                                  'port': '162',
                                                                  'trapDestination': '15.186.13.3',
                                                                  'trapFormat': 'SNMPv1',
                                                                  'trapSeverities': [],
                                                                  'userName': 'e20sysadminmd5aes',
                                                                  'vcmTrapCategories': []},
                                                                 {'communityString': '',
                                                                  'enetTrapCategories': [],
                                                                  'fcTrapCategories': [],
                                                                  'inform': 'false',
                                                                  'port': '162',
                                                                  'trapDestination': '15.186.13.4',
                                                                  'trapFormat': 'SNMPv1',
                                                                  'trapSeverities': [],
                                                                  'userName': 'e20sysadminmd5des',
                                                                  'vcmTrapCategories': []},
                                                                 {'communityString': '',
                                                                  'enetTrapCategories': [],
                                                                  'fcTrapCategories': [],
                                                                  'inform': 'false',
                                                                  'port': '162',
                                                                  'trapDestination': '15.186.13.5',
                                                                  'trapFormat': 'SNMPv1',
                                                                  'trapSeverities': [],
                                                                  'userName': 'e20sysadminsha',
                                                                  'vcmTrapCategories': []},
                                                                 ],
                                            'type': 'snmp-configuration',
                                            'uri': '',
                                            'v3Enabled': 'true'}


snmpv3_li_body_duplicate_user = {'category': 'snmp-configuration',
                                 'enabled': 'false',
                                 'readCommunity': 'public',
                                 'snmpAccess': [],
                                 'snmpUsers': [{'snmpV3UserName': 'e20sysadminshaaes',
                                                'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                                     'valueFormat': 'SecuritySensitive', 'valueType': 'String'},
                                                                    {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password',
                                                                     'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                                'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'},
                                               {'snmpV3UserName': 'e20sysadminshaaes',
                                                'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                                     'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                                'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'NA'}],
                                 'trapDestinations': [],
                                 'type': 'snmp-configuration',
                                 'uri': '',
                                 'v3Enabled': 'true'}

SNMPV3_LI_body_md5_des_duplicate = {'category': 'snmp-configuration',
                                    'enabled': 'false',
                                    'readCommunity': 'public',
                                    'snmpAccess': [],
                                    'snmpUsers': [{'snmpV3UserName': 'e20sysadminmd5des',
                                                   'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword',
                                                                        'value': 'password',
                                                                        'valueFormat': 'SecuritySensitive',
                                                                        'valueType': 'String'},
                                                                       {'propertyName': 'SnmpV3PrivacyPassword',
                                                                        'value': 'password',
                                                                        'valueFormat': 'SecuritySensitive',
                                                                        'valueType': 'String'}],
                                                   'v3AuthProtocol': 'MD5',
                                                   'v3PrivacyProtocol': 'DES56'}],
                                    'trapDestinations': [],
                                    'type': 'snmp-configuration',
                                    'uri': '',
                                    'v3Enabled': 'true'}

port = '162'
inavlid_snmp_usernames = ['talent@123', '        ', 'Change$!#']
max_length_username = ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', '']
valid_snmp_username = ['snmpusernmae', '12345678', 'password123', 'change_1234', 'ABCDEFGH', 'AbCdEfGh']
invalid_auth_passwords = '       '
valid_auth_username = ['snmpusernmae', '12345678', 'change_1234', 'AbCdEfGh']
min_length_auth_password = 'hello'

SNMPV3_LI_body_sha_inform = {'category': 'snmp-configuration',
                             'enabled': 'false',
                             'readCommunity': 'public',
                             'snmpAccess': [],
                             'snmpUsers': [{'snmpV3UserName': 'e20sysadminsha',
                                            'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                                 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                            'v3AuthProtocol': 'SHA',
                                            'v3PrivacyProtocol': 'NA'}],
                             'trapDestinations': [{'communityString': '',
                                                   'enetTrapCategories': [],
                                                   'fcTrapCategories': [],
                                                   'inform': 'true',
                                                   'engineId': '0x80001F888071F26C0ED6B8E15800000000',
                                                   'port': '162',
                                                   'trapDestination': '15.186.13.8',
                                                   'trapFormat': 'SNMPv3',
                                                   'trapSeverities': [],
                                                   'userName': 'e20sysadminsha',
                                                   'vcmTrapCategories': []}],
                             'type': 'snmp-configuration',
                             'uri': '',
                             'v3Enabled': 'true'}

SNMPV3_LI_body_md5_wrong_password = {'category': 'snmp-configuration',
                                     'enabled': 'false',
                                     'readCommunity': 'public',
                                     'snmpAccess': [],
                                     'snmpUsers': [{'snmpV3UserName': 'e20sysadminmd5',
                                                    'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword',
                                                                         'value': 'default',
                                                                         'valueFormat': 'SecuritySensitive',
                                                                         'valueType': 'String'}],
                                                    'v3AuthProtocol': 'MD5',
                                                    'v3PrivacyProtocol': 'NA'}],
                                     'trapDestinations': [{'communityString': '',
                                                           'enetTrapCategories': [],
                                                           'fcTrapCategories': [],
                                                           'inform': 'false',
                                                           'port': '162',
                                                           'trapDestination': '15.186.13.8',
                                                           'trapFormat': 'SNMPv3',
                                                           'trapSeverities': [],
                                                           'userName': 'e20sysadminmd5',
                                                           'vcmTrapCategories': []}],
                                     'type': 'snmp-configuration',
                                     'uri': '',
                                     'v3Enabled': 'true'}

SNMPV3_LI_body_sha_aes_wrong_password = {'category': 'snmp-configuration',
                                         'enabled': 'false',
                                         'readCommunity': 'public',
                                         'snmpAccess': [],
                                         'snmpUsers': [{'snmpV3UserName': 'e20sysadminshaaees',
                                                        'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword',
                                                                             'value': 'default@123',
                                                                             'valueFormat': 'SecuritySensitive',
                                                                             'valueType': 'String'},
                                                                            {'propertyName': 'SnmpV3PrivacyPassword',
                                                                             'value': 'default@123',
                                                                             'valueFormat': 'SecuritySensitive',
                                                                             'valueType': 'String'}],
                                                        'v3AuthProtocol': 'SHA',
                                                        'v3PrivacyProtocol': 'AES128'}],
                                         'trapDestinations': [{'communityString': '',
                                                               'enetTrapCategories': [],
                                                               'fcTrapCategories': [],
                                                               'inform': 'true',
                                                               'port': '162',
                                                               'engineId': '0x80001F888071F26C0ED6B8E15800000000',
                                                               'trapDestination': '15.186.13.8',
                                                               'trapFormat': 'SNMPv3',
                                                               'trapSeverities': [],
                                                               'userName': 'e20sysadminshaaes',
                                                               'vcmTrapCategories': []}],
                                         'type': 'snmp-configuration',
                                         'uri': '',
                                         'v3Enabled': 'true'}

invalid_trap_ip = '15.20.30'
valid_trap_ip = ['15.186.13.8', '']


LIG_TB = {'name': 'LIG1',
          'type': 'logical-interconnect-groupV4',
          'enclosureType': 'SY12000',
          'enclosureIndexes': [-1],
          'interconnectMapTemplate': [],
          'interconnectBaySet': 1,
          'redundancyType': 'Redundant',
          'uplinkSets': [],
          'internalNetworkUris': [],
          'stackingMode': 'Enclosure',
          'ethernetSettings': None,
          'state': 'Active',
          'telemetryConfiguration': None,
          'snmpConfiguration': {'category': 'snmp-configuration',
                                'enabled': 'false',
                                'readCommunity': 'public',
                                'snmpAccess': [],
                                'snmpUsers': [{'snmpV3UserName': 'e20sysadminmd5des',
                                               'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword',
                                                                    'value': 'password',
                                                                    'valueFormat': 'SecuritySensitive',
                                                                    'valueType': 'String'},
                                                                   {'propertyName': 'SnmpV3PrivacyPassword',
                                                                    'value': 'password',
                                                                    'valueFormat': 'SecuritySensitive',
                                                                    'valueType': 'String'}],
                                               'v3AuthProtocol': 'MD5',
                                               'v3PrivacyProtocol': 'DES56'}],
                                'trapDestinations': [{'communityString': 'public',
                                                      'enetTrapCategories': [],
                                                      'fcTrapCategories': [],
                                                      'inform': 'false',
                                                      'port': '162',
                                                      'trapDestination': '15.186.13.8',
                                                      'trapFormat': 'SNMPv3',
                                                      'trapSeverities': [],
                                                      'userName': 'e20sysadminmd5des',
                                                      'vcmTrapCategories': []}],
                                'type': 'snmp-configuration',
                                'uri': '',
                                'v3Enabled': 'true'}}


users_list = [{'userName': 'Serveradmin', 'password': 'Serveradmin', 'permissions': [{'roleName': 'Server administrator'}], 'fullName': 'Serveradmin', 'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions'},
              {'userName': 'Networkadmin', 'password': 'Networkadmin', 'permissions': [{'roleName': 'Network administrator'}], 'fullName': 'Networkadmin', 'emailAddress': 'nat@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions'},
              {'userName': 'Backupadmin', 'password': 'Backupadmin', 'permissions': [{'roleName': 'Backup administrator'}], 'fullName': 'Backupadmin', 'emailAddress': 'backup@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions'},
              {'userName': 'readonly', 'password': 'readonly', 'fullName': 'readonly', 'permissions': [{'roleName': 'Read only'}], 'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions'}
              ]

serveradmin_credentials = {'userName': 'Serveradmin', 'password': 'Serveradmin'}

network_admin = {'userName': 'Networkadmin', 'password': 'Networkadmin'}

backup_admin = {'userName': 'Backupadmin', 'password': 'Backupadmin'}

readonly_user = {'userName': 'readonly', 'password': 'readonly'}

li_usernames_edit = ['md5des_1', 'md5aes_1', 'sha_1_aes', 'sha_d_des', 'shA1', 'Md5_none']


uplink_sets = {'UplinkSet_1': {'name': 'UplinkSet_1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_1'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                               'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': 'Q1:1', 'speed': 'Auto'}]},
               'UplinkSet_2': {'name': 'UplinkSet_2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_2'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                               'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '-1', 'port': '1', 'speed': 'Speed16G'}]},
               'UplinkSet_3': {'name': 'UplinkSet_3', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_3'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                               'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': '2', 'speed': 'Speed8G'}]},
               'UplinkSet_4': {'name': 'UplinkSet_4', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_4'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                               'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '-1', 'port': '2', 'speed': 'Speed4G'}]},
               'UplinkSet_20464': {'name': 'UplinkSet_4', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_2'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                   'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '-1', 'port': '1', 'speed': 'Speed4G'}]},
               'UplinkSet1_20580': {'name': 'UplinkSet_1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_1'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                    'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': 'Q1:1', 'speed': 'Speed4G'}]},
               'UplinkSet2_20580': {'name': 'UplinkSet_2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_2'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                    'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '-1', 'port': '1', 'speed': 'Speed4G'}]},
               'UplinkSet1_20581': {'name': 'UplinkSet_1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_1'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                    'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': 'Q1:1', 'speed': 'Speed8G'}]},
               'UplinkSet2_20581': {'name': 'UplinkSet_2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_2'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                    'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '-1', 'port': '1', 'speed': 'Speed8G'}]},
               'UplinkSet_20970_1': {'name': 'UplinkSet_20970_1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_1'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                     'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': 'Q1:1', 'speed': 'Speed8G'}]},
               'UplinkSet_20970_2': {'name': 'UplinkSet_20970_2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_2'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                     'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '-1', 'port': '1', 'speed': 'Speed4G'}]},
               'UplinkSet_20635': {'name': 'UplinkSet_1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_20635'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                   'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': 'Q1:1', 'speed': 'Speed4G'}]},
               'UplinkSet_failover': {'name': 'UplinkSet_1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_1'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                      'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': 'Q1:1', 'speed': 'Auto'},
                                                                 {'bay': '1', 'enclosure': '-1', 'port': 'Q1:2', 'speed': 'Auto'}]}
               }

fcnets = [{"type": "fc-networkV4",
           "name": "FC_1",
           "fabricType": "FabricAttach",
           "linkStabilityTime": 30,
           "autoLoginRedistribution": True
           },
          {"type": "fc-networkV4",
           "name": "FC_2",
           "fabricType": "FabricAttach",
           "linkStabilityTime": 30,
           "autoLoginRedistribution": True
           },
          {"type": "fc-networkV4",
           "name": "FC_3",
           "fabricType": "FabricAttach",
           "linkStabilityTime": 30,
           "autoLoginRedistribution": True
           },
          {"type": "fc-networkV4",
           "name": "FC_4",
           "fabricType": "FabricAttach",
           "linkStabilityTime": 30,
           "autoLoginRedistribution": True
           }
          ]

ligs = {'name': 'LIG1',
        'type': 'logical-interconnect-groupV400',
        'enclosureType': 'SY12000',
        'interconnectMapTemplate': [{'bay': 1, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1},
                                    {'bay': 4, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1}
                                    ],
        'enclosureIndexes': [-1],
        'interconnectBaySet': 1,
        'redundancyType': 'Redundant',
        'uplinkSets': [uplink_sets['UplinkSet_1'].copy(), uplink_sets['UplinkSet_2'].copy()],
        'internalNetworkUris': [],
        'stackingMode': 'Enclosure',
        'ethernetSettings': None,
        'state': 'Active',
        'telemetryConfiguration': None,
        'snmpConfiguration': None
        }

EG1 = 'EG1'

enc_groups = {'name': 'EG1',
              'enclosureCount': 1,
              'ipAddressingMode': 'DHCP',
              'interconnectBayMappings':
              [{'interconnectBay': 1, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
               {'interconnectBay': 4, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': 'LIG:LIG1'}
               ],
              'ipRangeUris': [],
              'powerMode': 'RedundantPowerFeed'
              }

les = {'name': 'LE1',
       'enclosureUris': ['ENC:' + ENC1],
       'enclosureGroupUri': 'EG:EG1',
       'firmwareBaselineUri': None,
       'forceInstallFirmware': False
       }

PROFILE2 = 'CN750160YS_Bay2-Carbon'

server_profile2 = [{'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 2',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG1', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': PROFILE2, 'description': 'Server using Carbon', 'affinity': 'Bay',
                    'bootMode': {"manageMode": True, "mode": "BIOS"},
                    'boot': {"manageBoot": True, "order": ["CD", "USB", "HardDisk"]},
                    'connections': [{'id': 1, 'name': 'Downlink_1', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_1', "wwpnType": "UserDefined", "wwpn": "10:00:00:90:fa:5d:34:56", "wwnn": "20:00:00:90:fa:5d:34:56", "boot": {"priority": "NotBootable", "iscsi": {}}},
                                    {'id': 2, 'name': 'Downlink_2', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '16000', 'networkUri': 'FC:FC_2', "wwpnType": "UserDefined", "wwpn": "10:00:00:90:fa:5d:34:57", "wwnn": "20:00:00:90:fa:5d:34:57", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}}
                                    ]}
                   ]
server_profiles3 = [{'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 3',
                     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + EG1, 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                     'name': 'LUNS_ELX_LGCY', 'description': '', 'affinity': 'Bay',
                     'bootMode': {"manageMode": True, "mode": "BIOS"},
                     'boot': {"manageBoot": True, "order": ["CD", "USB", "HardDisk"]},
                     'connections': [{'id': 1, 'name': 'BAY1', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_1', "wwpnType": "UserDefined", "wwpn": "10:00:00:90:fa:5d:34:56", "wwnn": "20:00:00:90:fa:5d:34:56", "boot": {"priority": "NotBootable", "iscsi": {}}},
                                     {'id': 2, 'name': 'BAY4', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '16000', 'networkUri': 'FC:FC_2', "wwpnType": "UserDefined", "wwpn": "10:00:00:90:fa:5d:34:57", "wwnn": "20:00:00:90:fa:5d:34:57", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
                                     ]}]

server_profiles1 = [{'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 1',
                     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + EG1, 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                     'name': 'BFS_QLGC_LEGACY', 'description': '', 'affinity': 'Bay',
                     'bootMode': {"manageMode": True, "mode": "BIOS"},
                     'boot': {"manageBoot": True, "order": ["CD", "USB", "HardDisk"]},
                     'connections': [{'id': 1, 'name': 'Downlink_1', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_1', "wwpnType": "UserDefined", "wwpn": "10:00:00:90:fa:5d:34:52", "wwnn": "20:00:00:90:fa:5d:34:52", "boot": {"priority": "Primary", "bootVolumeSource": "UserDefined", "targets": [{"arrayWwpn": "10:00:00:90:fa:5d:34:52", "lun": "0"}], "iscsi": {}}},
                                     {'id': 2, 'name': 'Downlink_2', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '16000', 'networkUri': 'FC:FC_2', "wwpnType": "UserDefined", "wwpn": "10:00:00:90:fa:5d:34:53", "wwnn": "20:00:00:90:fa:5d:34:53", "ipv4": {}, "boot": {"priority": "Secondary", "bootVolumeSource": "UserDefined", "targets": [{"arrayWwpn": "10:00:00:90:fa:5d:34:53", "lun": "0"}], "iscsi": {}}},
                                     ]}]
server_profiles2 = [{'type': 'ServerProfileV7', 'serverHardwareUri': ENC1 + ', bay 2',
                     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + EG1, 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                     'name': 'BFS_QLGC_LEGACY2', 'description': '', 'affinity': 'Bay',
                     'bootMode': {"manageMode": True, "mode": "BIOS"},
                     'boot': {"manageBoot": True, "order": ["CD", "USB", "HardDisk"]},
                     'connections': [{'id': 1, 'name': 'Downlink_1', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_1', "wwpnType": "UserDefined", "wwpn": "10:00:9a:69:37:00:00:08", "wwnn": "20:00:9a:69:37:00:00:08", "boot": {"priority": "Primary", "bootVolumeSource": "UserDefined", "targets": [{"arrayWwpn": "10:00:9a:69:37:00:00:08", "lun": "1"}], "iscsi": {}}},
                                     {'id': 2, 'name': 'Downlink_2', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '16000', 'networkUri': 'FC:FC_2', "wwpnType": "UserDefined", "wwpn": "10:00:9a:69:37:00:00:10", "wwnn": "20:00:9a:69:37:00:00:10", "ipv4": {}, "boot": {"priority": "Secondary", "bootVolumeSource": "UserDefined", "targets": [{"arrayWwpn": "20:00:9a:69:37:00:00:10", "lun": "0"}], "iscsi": {}}},
                                     ]}
                    ]

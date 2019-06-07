from robot.libraries.BuiltIn import BuiltIn

# Credentials
admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
oa_credentials = {'username': 'Administrator', 'password': 'hpvse14'}
ilo_credentials = {'username': 'Administrator', 'password': 'hpvse1-ilo'}
cliq_credentials = {'mgmt_ip': '16.71.149.173', 'username': 'admin', 'password': 'admin'}

# Resource types for X-API-Version=800
ENCLOSURE_TYPE = 'EnclosureV7'
SERVER_PROFILE_TYPE = 'ServerProfileV9'

# Enclosures, Interconnects, Server Hardware, Networks, ULS, LIG, and EG
# Enclosures
ENC1 = 'wpst22'
ENC1_OA1 = "16.125.77.71"
ENC2 = 'wpst23'
ENC2_OA1 = "16.125.77.80"
ENC3 = 'wpst26'
ENC3_OA1 = "16.125.79.45"
# Interconnects
ENC1ICBAY1 = '%s, interconnect 1' % ENC1
ENC1ICBAY2 = '%s, interconnect 2' % ENC1
ENC1ICBAY3 = '%s, interconnect 3' % ENC1
ENC1ICBAY4 = '%s, interconnect 4' % ENC1
ENC1ICBAY5 = '%s, interconnect 5' % ENC1
ENC1ICBAY6 = '%s, interconnect 6' % ENC1
ENC2ICBAY1 = '%s, interconnect 1' % ENC2
ENC2ICBAY2 = '%s, interconnect 2' % ENC2
ENC2ICBAY3 = '%s, interconnect 3' % ENC2
ENC2ICBAY4 = '%s, interconnect 4' % ENC2
ENC2ICBAY5 = '%s, interconnect 5' % ENC2
ENC2ICBAY6 = '%s, interconnect 6' % ENC2
ENC3ICBAY1 = '%s, interconnect 1' % ENC3
ENC3ICBAY2 = '%s, interconnect 2' % ENC3
ENC3ICBAY3 = '%s, interconnect 3' % ENC3
ENC3ICBAY4 = '%s, interconnect 4' % ENC3
ENC3ICBAY5 = '%s, interconnect 5' % ENC3
ENC3ICBAY6 = '%s, interconnect 6' % ENC3
# Server Hardware
ENC1SHBAY1 = '%s, bay 1' % ENC1    # BL465c Gen8
ENC1SHBAY2 = '%s, bay 2' % ENC1    # BL465c Gen8
ENC1SHBAY3 = '%s, bay 3' % ENC1    # BL465c Gen8
ENC1SHBAY4 = '%s, bay 4' % ENC1    # BL420c Gen8
ENC1SHBAY5 = '%s, bay 5' % ENC1    # BL460c Gen9
ENC1SHBAY6 = '%s, bay 6' % ENC1    # BL460c G6
ENC1SHBAY8 = '%s, bay 7' % ENC1    # BL495c G5
ENC1SHBAY14 = '%s, bay 14' % ENC1  # BL460c Gen10
ENC1SHBAY16 = '%s, bay 16' % ENC1  # BL460c Gen10
ENC2SHBAY1 = '%s, bay 1' % ENC2    # BL465c Gen8
ENC2SHBAY2 = '%s, bay 2' % ENC2    # BL465c Gen8
ENC2SHBAY3 = '%s, bay 3' % ENC2    # BL465c Gen8
ENC2SHBAY4 = '%s, bay 4' % ENC2    # BL420c Gen8
ENC2SHBAY5 = '%s, bay 5' % ENC2    # BL460c Gen9
ENC2SHBAY6 = '%s, bay 6' % ENC2    # BL460c G6
ENC2SHBAY7 = '%s, bay 7' % ENC2    # BL2x220c G5
ENC2SHBAY10 = '%s, bay 10' % ENC2  # BL460c Gen10
ENC2SHBAY16 = '%s, bay 16' % ENC2  # BL460c Gen10
ENC3SHBAY1 = '%s, bay 1' % ENC3    # BL465c Gen8
ENC3SHBAY2 = '%s, bay 2' % ENC3    # BL465c Gen8
ENC3SHBAY3 = '%s, bay 3' % ENC3    # BL465c Gen8
ENC3SHBAY4 = '%s, bay 4' % ENC3    # BL420c Gen8
ENC3SHBAY5 = '%s, bay 5' % ENC3    # BL460c Gen9
ENC3SHBAY7 = '%s, bay 7' % ENC3    # BL660c Gen9
ENC3SHBAY8 = '%s, bay 8' % ENC3    # BL660c Gen8
ENC3SHBAY9 = '%s, bay 9' % ENC3    # BL460c G7
ENC3SHBAY10 = '%s, bay 10' % ENC3  # BL465c G7
# LIGs and EGs
LIG1_NAME = 'LIG22'
EG1_NAME = 'EG22'
LIG2_NAME = 'LIG23'
EG2_NAME = 'EG23'
LIG3_NAME = 'LIG26'
EG3_NAME = 'EG26'

enclosures_expected = [
    {"type": ENCLOSURE_TYPE, "name": "wpst22", "state": "Configured"},
    {"type": ENCLOSURE_TYPE, "name": "wpst23", "state": "Configured"},
    {"type": ENCLOSURE_TYPE, "name": "wpst23", "state": "Configured"},
]

# OVF1061
OVF1061_SERVER1 = ENC1SHBAY14
OVF1061_SERVER1_SERVER_NAME_1 = "wpst22bay14-1"
OVF1061_SERVER1_SERVER_NAME_2 = "wpst22bay14-2"
OVF1061_SERVER1_SERVER_NAME_3 = "WPST22BAY14-OS"
OVF1061_SERVER2 = ENC2SHBAY2
OVF1061_SERVER2_SERVER_NAME_1 = "wpst23bay2-1"
OVF1061_SERVER2_SERVER_NAME_2 = "wpst23bay2-2"
OVF1061_SERVER2_SERVER_NAME_3 = "wpst23bay2-os"

server_settings_1 = [
    {'name': OVF1061_SERVER1, 'ilo': '16.125.73.236', 'server_name': OVF1061_SERVER1_SERVER_NAME_1},
    {'name': OVF1061_SERVER2, 'ilo': '16.125.77.205', 'server_name': OVF1061_SERVER2_SERVER_NAME_1},
]

server_settings_2 = [
    {'name': OVF1061_SERVER1, 'server_name': OVF1061_SERVER1_SERVER_NAME_2},
    {'name': OVF1061_SERVER2, 'server_name': OVF1061_SERVER2_SERVER_NAME_2},
]

server_settings_3 = [
    {'name': OVF1061_SERVER1, 'server_name': OVF1061_SERVER1_SERVER_NAME_3},
    {'name': OVF1061_SERVER2, 'server_name': OVF1061_SERVER2_SERVER_NAME_3},
]

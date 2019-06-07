from dto import *
from env_variables import *

# Credentials
oa_credentials = {'username': 'Administrator', 'password': 'hpvse14'}
cliq_credentials = {'mgmt_ip': '16.71.149.173', 'username': 'admin', 'password': 'admin'}
ssh_credentials = {'username': 'root', 'password': 'hpvse1'}

# Enclosures, Interconnects, Server Hardware, LIG, EG, and LE
# Potash and Chloride
ENC1ICBAY3 = '%s, interconnect 3' % ENC1  # Potash
ENC1ICBAY6 = '%s, interconnect 6' % ENC1
ENC2ICBAY3 = '%s, interconnect 3' % ENC2  # Potash
ENC2ICBAY6 = '%s, interconnect 6' % ENC2
ENC3ICBAY3 = '%s, interconnect 3' % ENC3
ENC3ICBAY6 = '%s, interconnect 6' % ENC3
# Natasha SAS interconnects
ENC1SASICBAY1 = '%s, interconnect 1' % ENC1
ENC1SASICBAY4 = '%s, interconnect 4' % ENC1
# Drive Enclosures (Bigbird)
ENC1DEBAY1 = '%s, bay 1' % ENC1
# Server Hardware
ENC1SHBAY3 = '%s, bay 3' % ENC1  # SY680 Gen9
ENC1SHBAY5 = '%s, bay 5' % ENC1  # SY660 Gen9
ENC1SHBAY6 = '%s, bay 6' % ENC1  # SY480 Gen10
ENC1SHBAY7 = '%s, bay 7' % ENC1  # SY480 Gen9
ENC1SHBAY8 = '%s, bay 8' % ENC1  # SY480 Gen10
ENC2SHBAY1 = '%s, bay 1' % ENC2  # SY480 Gen9
ENC2SHBAY5 = '%s, bay 5' % ENC2  # SY660 Gen9
ENC2SHBAY7 = '%s, bay 7' % ENC2  # SY480 Gen10
ENC2SHBAY8 = '%s, bay 8' % ENC2  # SY480 Gen10
ENC3SHBAY1 = '%s, bay 1' % ENC3  # SY480 Gen9
ENC3SHBAY5 = '%s, bay 5' % ENC3  # SY680 Gen9

# OVF1061
OVF1061_SERVER1 = ENC3SHBAY1
OVF1061_SERVER1_SERVER_NAME_1 = "tbird18bay1-1"
OVF1061_SERVER1_SERVER_NAME_2 = "tbird18bay1-os"
OVF1061_SERVER2 = ENC2SHBAY7
OVF1061_SERVER2_SERVER_NAME_1 = "tbird17bay7-1"
OVF1061_SERVER2_SERVER_NAME_2 = "TBIRD17BAY7-OS"

server_settings_1 = [
    {'name': OVF1061_SERVER1, 'server_name': OVF1061_SERVER1_SERVER_NAME_1},
    {'name': OVF1061_SERVER2, 'server_name': OVF1061_SERVER2_SERVER_NAME_1},
]

server_settings_2 = [
    {'name': OVF1061_SERVER1, 'server_name': OVF1061_SERVER1_SERVER_NAME_2},
    {'name': OVF1061_SERVER2, 'server_name': OVF1061_SERVER2_SERVER_NAME_2},
]

server_settings_3 = [
    {'name': OVF1061_SERVER1, 'server_name': OVF1061_SERVER1_SERVER_NAME_2},
]

NAME_PREFIX = 'Synergy-Ring1-OVF1061-'
PROFILE_NAME_PREFIX = NAME_PREFIX
PROFILE1_NAME = PROFILE_NAME_PREFIX + 'profile1'
PROFILE1_SERVER = OVF1061_SERVER1
PROFILE1_EG = EG_NAME
PROFILE1_ENC = ENC3
PROFILE2_NAME = PROFILE_NAME_PREFIX + 'profile2'
PROFILE2_SERVER = OVF1061_SERVER2
PROFILE2_EG = EG_NAME
PROFILE2_ENC = ENC2
profile1 = {
    "type": SERVER_PROFILE_TYPE, "name": PROFILE1_NAME,
    "description": "", "iscsiInitiatorName": None, "iscsiInitiatorNameType": "AutoGenerated",
    "serverHardwareUri": 'SH:' + PROFILE1_SERVER, "enclosureGroupUri": "EG:" + PROFILE1_EG,
    'enclosureUri': 'ENC:' + PROFILE1_ENC,
    "hideUnusedFlexNics": True, "affinity": "Bay", "macType": "Physical", "wwnType": "Physical",
    "serialNumberType": "Physical",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": True, "order": ["HardDisk"]},
    "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
    "firmware": {
        "manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None
    },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
}

profile2 = {
    "type": SERVER_PROFILE_TYPE, "name": PROFILE2_NAME,
    "description": "", "iscsiInitiatorName": None, "iscsiInitiatorNameType": "AutoGenerated",
    "serverHardwareUri": 'SH:' + PROFILE2_SERVER, "enclosureGroupUri": "EG:" + PROFILE2_EG,
    'enclosureUri': 'ENC:' + PROFILE2_ENC,
    "hideUnusedFlexNics": True, "affinity": "Bay", "macType": "Physical", "wwnType": "Physical",
    "serialNumberType": "Physical",
    "connectionSettings": {"connections": []},
    "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
    "boot": {"manageBoot": True, "order": ["HardDisk"]},
    "firmware": {
        "manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None
    },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
}

suite_setup_profiles = [profile1.copy(), profile2.copy()]
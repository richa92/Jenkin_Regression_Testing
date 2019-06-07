# Credentials
admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
oa_credentials = {'username': 'Administrator', 'password': 'hpvse14'}
ilo_credentials = {'username': 'Administrator', 'password': 'hpvse123'}
cliq_credentials = {
    'mgmt_ip': '16.71.149.173',
    'username': 'admin',
    'password': 'admin'}
ssh_credentials = {'username': 'root', 'password': 'hpvse1'}

# Resource types for X-API-Version=1000
SERVER_PROFILE_TEMPLATE_TYPE = 'ServerProfileTemplateV6'
SERVER_PROFILE_TYPE = 'ServerProfileV10'
SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE = 'ServerProfileCompliancePreviewV1'

# Enclosures, Interconnects, Server Hardware, LIG, EG, and LE
# Enclosures
ENC1 = 'CN754406XL'
ENC2 = 'CN754404R6'
ENC3 = 'CN754406WB'
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
ENC1SHBAY3 = '%s, bay 3' % ENC1    # SY680 Gen9
ENC1SHBAY5 = '%s, bay 5' % ENC1    # SY660 Gen9
ENC1SHBAY6 = '%s, bay 6' % ENC1    # SY480 Gen10
ENC1SHBAY7 = '%s, bay 7' % ENC1    # SY480 Gen9
ENC1SHBAY8 = '%s, bay 8' % ENC1    # SY480 Gen10
ENC2SHBAY1 = '%s, bay 1' % ENC2    # SY480 Gen9
ENC2SHBAY5 = '%s, bay 5' % ENC2    # SY660 Gen9
ENC2SHBAY7 = '%s, bay 7' % ENC2    # SY480 Gen10
ENC2SHBAY8 = '%s, bay 8' % ENC2    # SY480 Gen10
ENC3SHBAY1 = '%s, bay 1' % ENC3    # SY480 Gen9
ENC3SHBAY5 = '%s, bay 5' % ENC3    # SY680 Gen9
# LIG, EG and LE
LIG_NAME = 'LIG1'
SASLIG_NAME = 'SASLIG1'
EG_NAME = 'EG1'
LE_NAME = 'LE1'

# Name prefixes
NAME_PREFIX = 'Synergy-Ring1-OVF2972-'
SPT_NAME_PREFIX = NAME_PREFIX
PROFILE_NAME_PREFIX = NAME_PREFIX
# SH
SERVER1 = ENC1SHBAY7            # SY480c Gen9
SERVER2 = ENC1SHBAY6            # SY480c Gen10
# SHT
SHT_SERVER1 = 'SH:' + SERVER1
SHT_SERVER2 = 'SH:' + SERVER2
# Suite Setup
SUITE_SETUP_SP1_NAME = PROFILE_NAME_PREFIX + 'suite-setup-profile1'
SUITE_SETUP_SP1_SH = SERVER1
SUITE_SETUP_SP1_EG = EG_NAME
SUITE_SETUP_SP2_NAME = PROFILE_NAME_PREFIX + 'suite-setup-profile2'
SUITE_SETUP_SP2_SH = SERVER2
SUITE_SETUP_SP2_EG = EG_NAME
# NTS1 create SPT to fail validation
NTS1_SPT1_NAME = SPT_NAME_PREFIX + 'nts1-spt1'
NTS1_SPT2_NAME = SPT_NAME_PREFIX + 'nts1-spt2'
NTS1_SPT3_NAME = SPT_NAME_PREFIX + 'nts1-spt3'
NTS1_SPT4_NAME = SPT_NAME_PREFIX + 'nts1-spt4'
NTS1_SPT5_NAME = SPT_NAME_PREFIX + 'nts1-spt5'
NTS1_SPT6_NAME = SPT_NAME_PREFIX + 'nts1-spt6'
NTS1_SPT_EG = EG_NAME
# NTS2 edit SPT to fail validation
NTS2_SPT_NAME = SPT_NAME_PREFIX + 'nts2-spt'
NTS2_SPT_EG = EG_NAME
# NTS3 create SP to fail validation
NTS3_PROFILE1_NAME = PROFILE_NAME_PREFIX + 'nts3-profile1'
NTS3_PROFILE2_NAME = PROFILE_NAME_PREFIX + 'nts3-profile2'
NTS3_PROFILE3_NAME = PROFILE_NAME_PREFIX + 'nts3-profile3'
NTS3_PROFILE4_NAME = PROFILE_NAME_PREFIX + 'nts3-profile4'
NTS3_PROFILE5_NAME = PROFILE_NAME_PREFIX + 'nts3-profile5'
NTS3_PROFILE6_NAME = PROFILE_NAME_PREFIX + 'nts3-profile6'
NTS3_PROFILE_EG = EG_NAME
# NTS4 edit SP to fail validation
NTS4_PROFILE_NAME = PROFILE_NAME_PREFIX + 'nts4-profile'
NTS4_PROFILE_EG = EG_NAME
# PTS1 create and edit SP
PTS1_PROFILE1_NAME = PROFILE_NAME_PREFIX + 'pts1-profile1'
PTS1_PROFILE1_SERVER = SERVER1
PTS1_PROFILE1_EG = EG_NAME
PTS1_PROFILE2_NAME = PROFILE_NAME_PREFIX + 'pts1-profile2'
PTS1_PROFILE2_SERVER = SERVER2
PTS1_PROFILE2_EG = EG_NAME
PTS1_CREATE_USER = 'Birch'
PTS1_CREATE_USER_PASSWORD = 'hpvse123'
PTS1_EDIT_USER = 'Cherry'
PTS1_EDIT_USER_PASSWORD = 'hpvse12345'
# PTS2 non-compliance on user count
PTS2_SPT1_NAME = SPT_NAME_PREFIX + 'pts2-spt1'
PTS2_SPT1_SHT = SHT_SERVER1
PTS2_SPT1_EG = EG_NAME
PTS2_PROFILE1_NAME = PROFILE_NAME_PREFIX + 'pts2-profile1'
PTS2_PROFILE1_SERVER = SERVER1
PTS2_PROFILE1_EG = EG_NAME
PTS2_SPT2_NAME = SPT_NAME_PREFIX + 'pts2-spt2'
PTS2_SPT2_SHT = SHT_SERVER2
PTS2_SPT2_EG = EG_NAME
PTS2_PROFILE2_NAME = PROFILE_NAME_PREFIX + 'pts2-profile2'
PTS2_PROFILE2_SERVER = SERVER2
PTS2_PROFILE2_EG = EG_NAME
# PTS3 non-compliance on user priv
PTS3_SPT1_NAME = SPT_NAME_PREFIX + 'pts3-spt1'
PTS3_SPT1_SHT = SHT_SERVER1
PTS3_SPT1_EG = EG_NAME
PTS3_PROFILE1_NAME = PROFILE_NAME_PREFIX + 'pts3-profile1'
PTS3_PROFILE1_SERVER = SERVER1
PTS3_PROFILE1_EG = EG_NAME
PTS3_SPT2_NAME = SPT_NAME_PREFIX + 'pts3-spt2'
PTS3_SPT2_SHT = SHT_SERVER2
PTS3_SPT2_EG = EG_NAME
PTS3_PROFILE2_NAME = PROFILE_NAME_PREFIX + 'pts3-profile2'
PTS3_PROFILE2_SERVER = SERVER2
PTS3_PROFILE2_EG = EG_NAME
# PTS4 create SPT from SP
PTS4_PROFILE1_NAME = PROFILE_NAME_PREFIX + 'pts4-profile1'
PTS4_PROFILE1_SERVER = SERVER1
PTS4_PROFILE1_EG = EG_NAME
PTS4_PROFILE2_NAME = PROFILE_NAME_PREFIX + 'pts4-profile2'
PTS4_PROFILE2_SERVER = SERVER2
PTS4_PROFILE2_EG = EG_NAME
PTS4_SPT1_NAME = SPT_NAME_PREFIX + 'pts4-spt1'
PTS4_SPT1_SHT = SHT_SERVER1
PTS4_SPT1_EG = EG_NAME
PTS4_SPT2_NAME = SPT_NAME_PREFIX + 'pts4-spt2'
PTS4_SPT2_SHT = SHT_SERVER2
PTS4_SPT2_EG = EG_NAME
# PTS5 manageMp
PTS5_PROFILE1_NAME = PROFILE_NAME_PREFIX + 'pts5-profile1'
PTS5_PROFILE1_SERVER = SERVER1
PTS5_PROFILE1_EG = EG_NAME
PTS5_PROFILE2_NAME = PROFILE_NAME_PREFIX + 'pts5-profile2'
PTS5_PROFILE2_SERVER = SERVER2
PTS5_PROFILE2_EG = EG_NAME
# PTS6 unassign and assign profile
PTS6_PROFILE1_NAME = PROFILE_NAME_PREFIX + 'pts6-profile1'
PTS6_PROFILE1_SHT = SHT_SERVER1
PTS6_PROFILE1_SERVER = SERVER1
PTS6_PROFILE1_EG = EG_NAME
PTS6_PROFILE2_NAME = PROFILE_NAME_PREFIX + 'pts6-profile2'
PTS6_PROFILE2_SHT = SHT_SERVER2
PTS6_PROFILE2_SERVER = SERVER2
PTS6_PROFILE2_EG = EG_NAME
# PTS7 move profile
PTS7_PROFILE_NAME = PROFILE_NAME_PREFIX + 'pts7-profile'
PTS7_PROFILE_SERVER = SERVER1
PTS7_PROFILE_SHT = SHT_SERVER1
PTS7_PROFILE_EG = EG_NAME
PTS7_PROFILE_MOVE_SERVER = SERVER2
PTS7_PROFILE_MOVE_SHT = SHT_SERVER2
PTS7_PROFILE_MOVE_EG = EG_NAME
# PTS8 B/R
PTS8_SPT1_NAME = SPT_NAME_PREFIX + 'pts8-spt1'
PTS8_SPT1_SHT = SHT_SERVER1
PTS8_SPT1_EG = EG_NAME
PTS8_PROFILE1_NAME = PROFILE_NAME_PREFIX + 'pts8-profile1'
PTS8_PROFILE1_SHT = SHT_SERVER1
PTS8_PROFILE1_SERVER = SERVER1
PTS8_PROFILE1_EG = EG_NAME
PTS8_SPT2_NAME = SPT_NAME_PREFIX + 'pts8-spt2'
PTS8_SPT2_SHT = SHT_SERVER2
PTS8_SPT2_EG = EG_NAME
PTS8_PROFILE2_NAME = PROFILE_NAME_PREFIX + 'pts8-profile2'
PTS8_PROFILE2_SHT = SHT_SERVER2
PTS8_PROFILE2_SERVER = SERVER2
PTS8_PROFILE2_EG = EG_NAME

# suite setup
suite_setup_profile1 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": SUITE_SETUP_SP1_NAME,
    "serverHardwareUri": 'SH:' + SUITE_SETUP_SP1_SH,
    "enclosureGroupUri": 'EG:' + SUITE_SETUP_SP1_EG,
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": []
    },
    "managementProcessor": {
        "manageMp": False,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {"localAccounts": []}
        }]
    },
}

suite_setup_profile2 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": SUITE_SETUP_SP2_NAME,
    "serverHardwareUri": 'SH:' + SUITE_SETUP_SP2_SH,
    "enclosureGroupUri": 'EG:' + SUITE_SETUP_SP2_EG,
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": []
    },
    "managementProcessor": {
        "manageMp": False,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {"localAccounts": []}
        }]
    },
}

# NTS1 create SPT to fail validation
# userName=ADMINISTRATOR
nts1_negative_spt1 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": NTS1_SPT1_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT_SERVER1,
    "enclosureGroupUri": 'EG:' + NTS1_SPT_EG,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "iscsiInitiatorNameType": "AutoGenerated",
    "connectionSettings": {
        "connections": [],
        "manageConnections": False
    },
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "ADMINISTRATOR",
                    "displayName": "ADMINISTRATOR",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True
                },
                ]
            }
        }]
    },
}

# userName=_HPOneViewAdmin
nts1_negative_spt2 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": NTS1_SPT2_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT_SERVER1,
    "enclosureGroupUri": 'EG:' + NTS1_SPT_EG,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "iscsiInitiatorNameType": "AutoGenerated",
    "connectionSettings": {
        "connections": [],
        "manageConnections": False
    },
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "_HPOneViewAdmin",
                    "displayName": "ONeView Administrator",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True
                },
                ]
            }
        }]
    },
}

# priv=recoverySet
nts1_negative_spt3 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": NTS1_SPT3_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT_SERVER2,
    "enclosureGroupUri": 'EG:' + NTS1_SPT_EG,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "iscsiInitiatorNameType": "AutoGenerated",
    "connectionSettings": {
        "connections": [],
        "manageConnections": False
    },
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "Pine",
                    "displayName": "Pine",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True,
                    "loginPriv": True,
                    "hostBIOSConfigPriv": True,
                    "hostNICConfigPriv": True,
                    "hostStorageConfigPriv": True,
                    "recoverySet": True
                },
                ]
            }
        }]
    },
}

# iLO5 priv on iLO4 server
nts1_negative_spt4 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": NTS1_SPT4_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT_SERVER1,
    "enclosureGroupUri": 'EG:' + NTS1_SPT_EG,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "iscsiInitiatorNameType": "AutoGenerated",
    "connectionSettings": {
        "connections": [],
        "manageConnections": False
    },
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "Pine",
                    "displayName": "Pine",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True,
                    "loginPriv": True,
                    "hostBIOSConfigPriv": True,
                    "hostNICConfigPriv": True,
                    "hostStorageConfigPriv": True,
                },
                ]
            }
        }]
    },
}

# >max 8 user account
nts1_negative_spt5 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": NTS1_SPT5_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT_SERVER1,
    "enclosureGroupUri": 'EG:' + NTS1_SPT_EG,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "iscsiInitiatorNameType": "AutoGenerated",
    "connectionSettings": {
        "connections": [],
        "manageConnections": False
    },
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [
                    {
                        "userName": "Pine1",
                        "displayName": "Pine1",
                        "password": "hpvse123",
                        "userConfigPriv": True,
                        "remoteConsolePriv": True,
                        "virtualMediaPriv": True,
                        "virtualPowerAndResetPriv": True,
                        "iLOConfigPriv": True
                    },
                    {
                        "userName": "Pine2",
                        "displayName": "Pine2",
                        "password": "hpvse123",
                        "userConfigPriv": True,
                        "remoteConsolePriv": True,
                        "virtualMediaPriv": True,
                        "virtualPowerAndResetPriv": True,
                        "iLOConfigPriv": True
                    },
                    {
                        "userName": "Pine3",
                        "displayName": "Pine3",
                        "password": "hpvse123",
                        "userConfigPriv": True,
                        "remoteConsolePriv": True,
                        "virtualMediaPriv": True,
                        "virtualPowerAndResetPriv": True,
                        "iLOConfigPriv": True
                    },
                    {
                        "userName": "Pine4",
                        "displayName": "Pine4",
                        "password": "hpvse123",
                        "userConfigPriv": True,
                        "remoteConsolePriv": True,
                        "virtualMediaPriv": True,
                        "virtualPowerAndResetPriv": True,
                        "iLOConfigPriv": True
                    },
                    {
                        "userName": "Pine5",
                        "displayName": "Pine5",
                        "password": "hpvse123",
                        "userConfigPriv": True,
                        "remoteConsolePriv": True,
                        "virtualMediaPriv": True,
                        "virtualPowerAndResetPriv": True,
                        "iLOConfigPriv": True
                    },
                    {
                        "userName": "Pine6",
                        "displayName": "Pine6",
                        "password": "hpvse123",
                        "userConfigPriv": True,
                        "remoteConsolePriv": True,
                        "virtualMediaPriv": True,
                        "virtualPowerAndResetPriv": True,
                        "iLOConfigPriv": True
                    },
                    {
                        "userName": "Pine7",
                        "displayName": "Pine7",
                        "password": "hpvse123",
                        "userConfigPriv": True,
                        "remoteConsolePriv": True,
                        "virtualMediaPriv": True,
                        "virtualPowerAndResetPriv": True,
                        "iLOConfigPriv": True
                    },
                    {
                        "userName": "Pine8",
                        "displayName": "Pine8",
                        "password": "hpvse123",
                        "userConfigPriv": True,
                        "remoteConsolePriv": True,
                        "virtualMediaPriv": True,
                        "virtualPowerAndResetPriv": True,
                        "iLOConfigPriv": True
                    },
                    {
                        "userName": "Pine9",
                        "displayName": "Pine9",
                        "password": "hpvse123",
                        "userConfigPriv": True,
                        "remoteConsolePriv": True,
                        "virtualMediaPriv": True,
                        "virtualPowerAndResetPriv": True,
                        "iLOConfigPriv": True
                    },
                ]
            }
        }]
    },
}

nts1_negative_spt_tasks = [
    {
        'keyword': 'Add Server Profile Template',
        'argument': nts1_negative_spt1.copy(),
        'taskState': 'Error',
        'errorMessage': 'ILO_CONFIG_LOCAL_ACCOUNT_INVALID_USERNAME'
    },
    {
        'keyword': 'Add Server Profile Template',
        'argument': nts1_negative_spt2.copy(),
        'taskState': 'Error',
        'errorMessage': 'ILO_CONFIG_LOCAL_ACCOUNT_INVALID_USERNAME'
    },
    {
        'keyword': 'Add Server Profile Template',
        'argument': nts1_negative_spt3.copy(),
        'taskState': 'Error',
        'errorMessage': 'ILO_CONFIG_LOCAL_ACCOUNT_IVALID_SETTING'
    },
    {
        'keyword': 'Add Server Profile Template',
        'argument': nts1_negative_spt4.copy(),
        'taskState': 'Error',
        'errorMessage': 'ILO_CONFIG_LOCAL_ACCOUNT_IVALID_SETTING'
    },
    {
        'keyword': 'Add Server Profile Template',
        'argument': nts1_negative_spt5.copy(),
        'taskState': 'Error',
        'errorMessage': 'ILO_CONFIG_LOCAL_ACCOUNT_EXCEED_MAX'
    },
]

# NTS2 edit SPT to fail validation
nts2_spt_create = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": NTS2_SPT_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT_SERVER1,
    "enclosureGroupUri": 'EG:' + NTS2_SPT_EG,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "iscsiInitiatorNameType": "AutoGenerated",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [],
        "manageConnections": False
    },
    "managementProcessor": {
        "manageMp": False,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {"localAccounts": []}
        }]
    },
}

# userName=ADMINISTRATOR
nts2_spt_edit1 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": NTS2_SPT_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT_SERVER1,
    "enclosureGroupUri": 'EG:' + NTS1_SPT_EG,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "description": "",
    "affinity": "Bay",
    "iscsiInitiatorNameType": "AutoGenerated",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [],
        "manageConnections": False
    },
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "ADMINISTRATOR",
                    "displayName": "ADMINISTRATOR",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True
                },
                ]
            }
        }]
    },
}


# userName=_HPOneViewAdmin
nts2_spt_edit2 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": NTS2_SPT_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT_SERVER1,
    "enclosureGroupUri": 'EG:' + NTS2_SPT_EG,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "iscsiInitiatorNameType": "AutoGenerated",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [],
        "manageConnections": False
    },
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "_HPOneViewAdmin",
                    "displayName": "ONeView Administrator",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True
                },
                ]
            }
        }]
    },
}

# priv=recoverySet
nts2_spt_edit3 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": NTS2_SPT_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT_SERVER2,
    "enclosureGroupUri": 'EG:' + NTS2_SPT_EG,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "description": "",
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "iscsiInitiatorNameType": "AutoGenerated",
    "connectionSettings": {
        "connections": [],
        "manageConnections": False
    },
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "Pine",
                    "displayName": "Pine",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True,
                    "loginPriv": True,
                    "hostBIOSConfigPriv": True,
                    "hostNICConfigPriv": True,
                    "hostStorageConfigPriv": True,
                    "recoverySet": True
                },
                ]
            }
        }]
    },
}

# iLO5 priv on iLO4 server
nts2_spt_edit4 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": NTS2_SPT_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT_SERVER1,
    "enclosureGroupUri": 'EG:' + NTS2_SPT_EG,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "iscsiInitiatorNameType": "AutoGenerated",
    "connectionSettings": {
        "connections": [],
        "manageConnections": False
    },
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "Pine",
                    "displayName": "Pine",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True,
                    "loginPriv": True,
                    "hostBIOSConfigPriv": True,
                    "hostNICConfigPriv": True,
                    "hostStorageConfigPriv": True,
                },
                ]
            }
        }]
    },
}

# > max 8 user accounts
nts2_spt_edit5 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": NTS2_SPT_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT_SERVER1,
    "enclosureGroupUri": 'EG:' + NTS2_SPT_EG,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "description": "",
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "iscsiInitiatorNameType": "AutoGenerated",
    "connectionSettings": {
        "connections": [],
        "manageConnections": False
    },
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "Pine1",
                    "displayName": "Pine1",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True
                },
                    {
                    "userName": "Pine2",
                    "displayName": "Pine2",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True
                },
                    {
                    "userName": "Pine3",
                    "displayName": "Pine3",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True
                },
                    {
                    "userName": "Pine4",
                    "displayName": "Pine4",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True
                },
                    {
                    "userName": "Pine5",
                    "displayName": "Pine5",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True
                },
                    {
                    "userName": "Pine6",
                    "displayName": "Pine6",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True
                },
                    {
                    "userName": "Pine7",
                    "displayName": "Pine7",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True
                },
                    {
                    "userName": "Pine8",
                    "displayName": "Pine8",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True
                },
                    {
                    "userName": "Pine9",
                    "displayName": "Pine9",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True
                },
                ]
            }
        }]
    },
}

nts2_spts_create = [
    nts2_spt_create.copy(),
]

nts2_negative_spt_tasks = [
    {
        'keyword': 'Edit Server Profile Template',
        'argument': nts2_spt_edit1.copy(),
        'taskState': 'Error',
        'errorMessage': 'ILO_CONFIG_LOCAL_ACCOUNT_INVALID_USERNAME'
    },
    {
        'keyword': 'Edit Server Profile Template',
        'argument': nts2_spt_edit2.copy(),
        'taskState': 'Error',
        'errorMessage': 'ILO_CONFIG_LOCAL_ACCOUNT_INVALID_USERNAME'
    },
    {
        'keyword': 'Edit Server Profile Template',
        'argument': nts2_spt_edit3.copy(),
        'taskState': 'Error',
        'errorMessage': 'ILO_CONFIG_LOCAL_ACCOUNT_IVALID_SETTING'
    },
    {
        'keyword': 'Edit Server Profile Template',
        'argument': nts2_spt_edit4.copy(),
        'taskState': 'Error',
        'errorMessage': 'ILO_CONFIG_LOCAL_ACCOUNT_IVALID_SETTING'
    },
    {
        'keyword': 'Edit Server Profile Template',
        'argument': nts2_spt_edit5.copy(),
        'taskState': 'Error',
        'errorMessage': 'ILO_CONFIG_LOCAL_ACCOUNT_EXCEED_MAX'
    },
]

# NTS3 create SP to fail validation
# userName=administrator
nts3_negative_profile1 = {
    "type": SERVER_PROFILE_TYPE,
    "name": NTS3_PROFILE1_NAME,
    "serverHardwareUri": 'SH:' + SERVER1,
    "enclosureGroupUri": 'EG:' + NTS3_PROFILE_EG,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "iscsiInitiatorNameType": "AutoGenerated",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": []
    },
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "administrator",
                    "displayName": "administrator",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True
                },
                ]
            }
        }]
    },
}

# userName=_HPOneViewAdmin
nts3_negative_profile2 = {
    "type": SERVER_PROFILE_TYPE,
    "name": NTS3_PROFILE2_NAME,
    "serverHardwareUri": 'SH:' + SERVER1,
    "enclosureGroupUri": 'EG:' + NTS3_PROFILE_EG,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "iscsiInitiatorNameType": "AutoGenerated",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": []
    },
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "_HPOneViewAdmin",
                    "displayName": "ONeView Administrator",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True
                },
                ]
            }
        }]
    },
}

# priv=recoverySet
nts3_negative_profile3 = {
    "type": SERVER_PROFILE_TYPE,
    "name": NTS3_PROFILE3_NAME,
    "serverHardwareUri": 'SH:' + SERVER2,
    "enclosureGroupUri": 'EG:' + NTS3_PROFILE_EG,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "iscsiInitiatorNameType": "AutoGenerated",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": []
    },
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "Pine",
                    "displayName": "Pine",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True,
                    "loginPriv": True,
                    "hostBIOSConfigPriv": True,
                    "hostNICConfigPriv": True,
                    "hostStorageConfigPriv": True,
                    "recoverySet": True
                },
                ]
            }
        }]
    },
}

# iLO5 priv on iLO4 server
nts3_negative_profile4 = {
    "type": SERVER_PROFILE_TYPE,
    "name": NTS3_PROFILE4_NAME,
    "serverHardwareUri": 'SH:' + SERVER1,
    "enclosureGroupUri": 'EG:' + NTS3_PROFILE_EG,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "iscsiInitiatorNameType": "AutoGenerated",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": []
    },
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "Pine",
                    "displayName": "Pine",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True,
                    "loginPriv": True,
                    "hostBIOSConfigPriv": True,
                    "hostNICConfigPriv": True,
                    "hostStorageConfigPriv": True,
                },
                ]
            }
        }]
    },
}

# > max 8 user accounts
nts3_negative_profile5 = {
    "type": SERVER_PROFILE_TYPE,
    "name": NTS3_PROFILE5_NAME,
    "serverHardwareUri": 'SH:' + SERVER1,
    "enclosureGroupUri": 'EG:' + NTS3_PROFILE_EG,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "iscsiInitiatorNameType": "AutoGenerated",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": []
    },
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [
                    {
                        "userName": "Pine1",
                        "displayName": "Pine1",
                        "password": "hpvse123",
                        "userConfigPriv": True,
                        "remoteConsolePriv": True,
                        "virtualMediaPriv": True,
                        "virtualPowerAndResetPriv": True,
                        "iLOConfigPriv": True
                    },
                    {
                        "userName": "Pine2",
                        "displayName": "Pine2",
                        "password": "hpvse123",
                        "userConfigPriv": True,
                        "remoteConsolePriv": True,
                        "virtualMediaPriv": True,
                        "virtualPowerAndResetPriv": True,
                        "iLOConfigPriv": True
                    },
                    {
                        "userName": "Pine3",
                        "displayName": "Pine3",
                        "password": "hpvse123",
                        "userConfigPriv": True,
                        "remoteConsolePriv": True,
                        "virtualMediaPriv": True,
                        "virtualPowerAndResetPriv": True,
                        "iLOConfigPriv": True
                    },
                    {
                        "userName": "Pine4",
                        "displayName": "Pine4",
                        "password": "hpvse123",
                        "userConfigPriv": True,
                        "remoteConsolePriv": True,
                        "virtualMediaPriv": True,
                        "virtualPowerAndResetPriv": True,
                        "iLOConfigPriv": True
                    },
                    {
                        "userName": "Pine5",
                        "displayName": "Pine5",
                        "password": "hpvse123",
                        "userConfigPriv": True,
                        "remoteConsolePriv": True,
                        "virtualMediaPriv": True,
                        "virtualPowerAndResetPriv": True,
                        "iLOConfigPriv": True
                    },
                    {
                        "userName": "Pine6",
                        "displayName": "Pine6",
                        "password": "hpvse123",
                        "userConfigPriv": True,
                        "remoteConsolePriv": True,
                        "virtualMediaPriv": True,
                        "virtualPowerAndResetPriv": True,
                        "iLOConfigPriv": True
                    },
                    {
                        "userName": "Pine7",
                        "displayName": "Pine7",
                        "password": "hpvse123",
                        "userConfigPriv": True,
                        "remoteConsolePriv": True,
                        "virtualMediaPriv": True,
                        "virtualPowerAndResetPriv": True,
                        "iLOConfigPriv": True
                    },
                    {
                        "userName": "Pine8",
                        "displayName": "Pine8",
                        "password": "hpvse123",
                        "userConfigPriv": True,
                        "remoteConsolePriv": True,
                        "virtualMediaPriv": True,
                        "virtualPowerAndResetPriv": True,
                        "iLOConfigPriv": True
                    },
                    {
                        "userName": "Pine9",
                        "displayName": "Pine9",
                        "password": "hpvse123",
                        "userConfigPriv": True,
                        "remoteConsolePriv": True,
                        "virtualMediaPriv": True,
                        "virtualPowerAndResetPriv": True,
                        "iLOConfigPriv": True
                    },
                ]
            }
        }]
    },
}

nts3_negative_profile_tasks = [
    {
        'keyword': 'Add Server Profile',
        'argument': nts3_negative_profile1.copy(),
        'taskState': 'Error',
        'errorMessage': 'ILO_CONFIG_LOCAL_ACCOUNT_INVALID_USERNAME'},
    {
        'keyword': 'Add Server Profile',
        'argument': nts3_negative_profile2.copy(),
        'taskState': 'Error',
        'errorMessage': 'ILO_CONFIG_LOCAL_ACCOUNT_INVALID_USERNAME'},
    {
        'keyword': 'Add Server Profile',
        'argument': nts3_negative_profile3.copy(),
        'taskState': 'Error',
        'errorMessage': 'ILO_CONFIG_LOCAL_ACCOUNT_IVALID_SETTING'},
    {
        'keyword': 'Add Server Profile',
        'argument': nts3_negative_profile4.copy(),
        'taskState': 'Error',
        'errorMessage': 'ILO_CONFIG_LOCAL_ACCOUNT_IVALID_SETTING'},
    {
        'keyword': 'Add Server Profile',
        'argument': nts3_negative_profile5.copy(),
        'taskState': 'Error',
        'errorMessage': 'ILO_CONFIG_LOCAL_ACCOUNT_EXCEED_MAX'},
]

# NTS4 edit SP to fail validation
nts4_profile_create = {
    "type": SERVER_PROFILE_TYPE,
    "name": NTS4_PROFILE_NAME,
    "serverHardwareUri": 'SH:' + SERVER1,
    "enclosureGroupUri": 'EG:' + NTS4_PROFILE_EG,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "iscsiInitiatorNameType": "AutoGenerated",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": []
    },
}

# userName=administrator
nts4_profile_edit1 = {
    "type": SERVER_PROFILE_TYPE,
    "name": NTS4_PROFILE_NAME,
    "serverHardwareUri": 'SH:' + SERVER1,
    "enclosureGroupUri": 'EG:' + NTS4_PROFILE_EG,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "iscsiInitiatorNameType": "AutoGenerated",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": []
    },
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "administrator",
                    "displayName": "administrator",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True
                },
                ]
            }
        }]
    },
}

# userName=_HPOneViewAdmin
nts4_profile_edit2 = {
    "type": SERVER_PROFILE_TYPE,
    "name": NTS4_PROFILE_NAME,
    "serverHardwareUri": 'SH:' + SERVER1,
    "enclosureGroupUri": 'EG:' + NTS4_PROFILE_EG,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "iscsiInitiatorNameType": "AutoGenerated",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": []
    },
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "_HPOneViewAdmin",
                    "displayName": "ONeView Administrator",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True
                },
                ]
            }
        }]
    },
}

# priv=recoverySet
nts4_profile_edit3 = {
    "type": SERVER_PROFILE_TYPE,
    "name": NTS4_PROFILE_NAME,
    "serverHardwareUri": 'SH:' + SERVER2,
    "enclosureGroupUri": 'EG:' + NTS4_PROFILE_EG,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "iscsiInitiatorNameType": "AutoGenerated",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": []
    },
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "Pine",
                    "displayName": "Pine",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True,
                    "loginPriv": True,
                    "hostBIOSConfigPriv": True,
                    "hostNICConfigPriv": True,
                    "hostStorageConfigPriv": True,
                    "recoverySet": True
                },
                ]
            }
        }]
    },
}

# iLO5 priv on iLO4 server
nts4_profile_edit4 = {
    "type": SERVER_PROFILE_TYPE,
    "name": NTS4_PROFILE_NAME,
    "serverHardwareUri": 'SH:' + SERVER1,
    "enclosureGroupUri": 'EG:' + NTS4_PROFILE_EG,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "iscsiInitiatorNameType": "AutoGenerated",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": []
    },
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "Pine",
                    "displayName": "Pine",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True,
                    "loginPriv": True,
                    "hostBIOSConfigPriv": True,
                    "hostNICConfigPriv": True,
                    "hostStorageConfigPriv": True,
                },
                ]
            }
        }]
    },
}

# > max 8 user accounts
nts4_profile_edit5 = {
    "type": SERVER_PROFILE_TYPE,
    "name": NTS4_PROFILE_NAME,
    "serverHardwareUri": 'SH:' + SERVER1,
    "enclosureGroupUri": 'EG:' + NTS4_PROFILE_EG,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "iscsiInitiatorNameType": "AutoGenerated",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": []
    },
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [
                    {
                        "userName": "Pine1",
                        "displayName": "Pine1",
                        "password": "hpvse123",
                        "userConfigPriv": True,
                        "remoteConsolePriv": True,
                        "virtualMediaPriv": True,
                        "virtualPowerAndResetPriv": True,
                        "iLOConfigPriv": True
                    },
                    {
                        "userName": "Pine2",
                        "displayName": "Pine2",
                        "password": "hpvse123",
                        "userConfigPriv": True,
                        "remoteConsolePriv": True,
                        "virtualMediaPriv": True,
                        "virtualPowerAndResetPriv": True,
                        "iLOConfigPriv": True
                    },
                    {
                        "userName": "Pine3",
                        "displayName": "Pine3",
                        "password": "hpvse123",
                        "userConfigPriv": True,
                        "remoteConsolePriv": True,
                        "virtualMediaPriv": True,
                        "virtualPowerAndResetPriv": True,
                        "iLOConfigPriv": True
                    },
                    {
                        "userName": "Pine4",
                        "displayName": "Pine4",
                        "password": "hpvse123",
                        "userConfigPriv": True,
                        "remoteConsolePriv": True,
                        "virtualMediaPriv": True,
                        "virtualPowerAndResetPriv": True,
                        "iLOConfigPriv": True
                    },
                    {
                        "userName": "Pine5",
                        "displayName": "Pine5",
                        "password": "hpvse123",
                        "userConfigPriv": True,
                        "remoteConsolePriv": True,
                        "virtualMediaPriv": True,
                        "virtualPowerAndResetPriv": True,
                        "iLOConfigPriv": True
                    },
                    {
                        "userName": "Pine6",
                        "displayName": "Pine6",
                        "password": "hpvse123",
                        "userConfigPriv": True,
                        "remoteConsolePriv": True,
                        "virtualMediaPriv": True,
                        "virtualPowerAndResetPriv": True,
                        "iLOConfigPriv": True
                    },
                    {
                        "userName": "Pine7",
                        "displayName": "Pine7",
                        "password": "hpvse123",
                        "userConfigPriv": True,
                        "remoteConsolePriv": True,
                        "virtualMediaPriv": True,
                        "virtualPowerAndResetPriv": True,
                        "iLOConfigPriv": True
                    },
                    {
                        "userName": "Pine8",
                        "displayName": "Pine8",
                        "password": "hpvse123",
                        "userConfigPriv": True,
                        "remoteConsolePriv": True,
                        "virtualMediaPriv": True,
                        "virtualPowerAndResetPriv": True,
                        "iLOConfigPriv": True
                    },
                    {
                        "userName": "Pine9",
                        "displayName": "Pine9",
                        "password": "hpvse123",
                        "userConfigPriv": True,
                        "remoteConsolePriv": True,
                        "virtualMediaPriv": True,
                        "virtualPowerAndResetPriv": True,
                        "iLOConfigPriv": True
                    },
                ]
            }
        }]
    },
}

nts4_profiles_create = [
    nts4_profile_create.copy(),
]

nts4_negative_profile_tasks = [
    {
        'keyword': 'Edit Server Profile',
        'argument': nts4_profile_edit1.copy(),
        'taskState': 'Error',
        'errorMessage': 'ILO_CONFIG_LOCAL_ACCOUNT_INVALID_USERNAME'},
    {
        'keyword': 'Edit Server Profile',
        'argument': nts4_profile_edit2.copy(),
        'taskState': 'Error',
        'errorMessage': 'ILO_CONFIG_LOCAL_ACCOUNT_INVALID_USERNAME'},
    {
        'keyword': 'Edit Server Profile',
        'argument': nts4_profile_edit3.copy(),
        'taskState': 'Error',
        'errorMessage': 'ILO_CONFIG_LOCAL_ACCOUNT_IVALID_SETTING'},
    {
        'keyword': 'Edit Server Profile',
        'argument': nts4_profile_edit4.copy(),
        'taskState': 'Error',
        'errorMessage': 'ILO_CONFIG_LOCAL_ACCOUNT_IVALID_SETTING'},
    {
        'keyword': 'Edit Server Profile',
        'argument': nts4_profile_edit5.copy(),
        'taskState': 'Error',
        'errorMessage': 'ILO_CONFIG_LOCAL_ACCOUNT_EXCEED_MAX'},
]

# PTS1 create and edit SP and validate the password
pts1_profile1_create = {
    "type": SERVER_PROFILE_TYPE,
    "name": PTS1_PROFILE1_NAME,
    "serverHardwareUri": 'SH:' + PTS1_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + PTS1_PROFILE1_EG,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "iscsiInitiatorNameType": "AutoGenerated",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": []
    },
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "Birch",
                    "displayName": PTS1_CREATE_USER,
                    "password": PTS1_CREATE_USER_PASSWORD,
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True
                },
                ]
            }
        }]
    },
}

pts1_profile1_edit = {
    "type": SERVER_PROFILE_TYPE,
    "name": PTS1_PROFILE1_NAME,
    "serverHardwareUri": 'SH:' + PTS1_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + PTS1_PROFILE1_EG,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "iscsiInitiatorNameType": "AutoGenerated",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": []
    },
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "Cherry",
                    "displayName": PTS1_EDIT_USER,
                    "password": PTS1_EDIT_USER_PASSWORD,
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True
                },
                ]
            }
        }]
    },
}

pts1_profile2_create = {
    "type": SERVER_PROFILE_TYPE,
    "name": PTS1_PROFILE2_NAME,
    "serverHardwareUri": 'SH:' + PTS1_PROFILE2_SERVER,
    "enclosureGroupUri": 'EG:' + PTS1_PROFILE2_EG,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "iscsiInitiatorNameType": "AutoGenerated",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": []
    },
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "Birch",
                    "displayName": PTS1_CREATE_USER,
                    "password": PTS1_CREATE_USER_PASSWORD,
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True,
                    "loginPriv": True,
                    "hostBIOSConfigPriv": True,
                    "hostNICConfigPriv": True,
                    "hostStorageConfigPriv": True
                },
                ]
            }
        }]
    },
}

pts1_profile2_edit = {
    "type": SERVER_PROFILE_TYPE,
    "name": PTS1_PROFILE2_NAME,
    "serverHardwareUri": 'SH:' + PTS1_PROFILE2_SERVER,
    "enclosureGroupUri": 'EG:' + PTS1_PROFILE2_EG,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "iscsiInitiatorNameType": "AutoGenerated",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": []
    },
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "Cherry",
                    "displayName": PTS1_EDIT_USER,
                    "password": PTS1_EDIT_USER_PASSWORD,
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True,
                    "loginPriv": True,
                    "hostBIOSConfigPriv": True,
                    "hostNICConfigPriv": True,
                    "hostStorageConfigPriv": True
                },
                ]
            }
        }]
    },
}

pts1_profiles_create = [
    pts1_profile1_create.copy(),
    pts1_profile2_create.copy()]

pts1_profiles_edit = [pts1_profile1_edit.copy(), pts1_profile2_edit.copy()]

# PTS2 edit SP to create non-compliance
pts2_spt1_create = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": PTS2_SPT1_NAME,
    "serverHardwareTypeUri": 'SHT:' + PTS2_SPT1_SHT,
    "enclosureGroupUri": 'EG:' + PTS2_SPT1_EG,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "iscsiInitiatorNameType": "AutoGenerated",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [],
        "manageConnections": False
    },
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "Alder",
                    "displayName": "Alder",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True
                }]
            }
        }]
    },
}

pts2_spt2_create = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": PTS2_SPT2_NAME,
    "serverHardwareTypeUri": 'SHT:' + PTS2_SPT2_SHT,
    "enclosureGroupUri": 'EG:' + PTS2_SPT2_EG,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "iscsiInitiatorNameType": "AutoGenerated",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [],
        "manageConnections": False
    },
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "Alder",
                    "displayName": "Alder",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True,
                    "loginPriv": True,
                    "hostBIOSConfigPriv": True,
                    "hostNICConfigPriv": True,
                    "hostStorageConfigPriv": True
                }]
            }
        }]
    },
}

pts2_profile1_create = {
    "type": SERVER_PROFILE_TYPE,
    "name": PTS2_PROFILE1_NAME,
    "serverHardwareUri": 'SH:' + PTS2_PROFILE1_SERVER,
    "serverProfileTemplateUri": "SPT:" + PTS2_SPT1_NAME,
}

pts2_profile1_create_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": PTS2_PROFILE1_NAME,
    "serverHardwareUri": 'SH:' + PTS2_PROFILE1_SERVER,
    "serverProfileTemplateUri": "SPT:" + PTS2_SPT1_NAME,
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "Alder",
                    "displayName": "Alder",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True
                }]
            }
        }]
    },
}

# profile compliance
pts2_profile1_compliance = {
    "name": PTS2_PROFILE1_NAME,
    "compliance-preview":
    {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "isOnlineUpdate": None,
        "automaticUpdates": [],
        "manualUpdates": [],
    }
}

pts2_profile1_edit = {
    "type": SERVER_PROFILE_TYPE,
    "name": PTS2_PROFILE1_NAME,
    "serverHardwareUri": 'SH:' + PTS2_PROFILE1_SERVER,
    "serverProfileTemplateUri": "SPT:" + PTS2_SPT1_NAME,
    "enclosureGroupUri": 'EG:' + PTS2_PROFILE1_EG,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "iscsiInitiatorNameType": "AutoGenerated",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": []
    },
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "Alder",
                    "displayName": "Alder",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True
                },
                    {
                    "userName": "Aspen",
                    "displayName": "Aspen",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True
                },
                ]
            }
        }]
    },
}

# profile non compliance
pts2_profile1_non_compliance = {
    "name": PTS2_PROFILE1_NAME,
    "compliance-preview":
    {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "isOnlineUpdate": True,
        "automaticUpdates": ["Modify Management Processor LocalAccounts to match template."],
        "manualUpdates": [],
    }
}

pts2_profile2_create = {
    "type": SERVER_PROFILE_TYPE,
    "name": PTS2_PROFILE2_NAME,
    "serverHardwareUri": 'SH:' + PTS2_PROFILE2_SERVER,
    "serverProfileTemplateUri": "SPT:" + PTS2_SPT2_NAME,
}

pts2_profile2_create_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": PTS2_PROFILE2_NAME,
    "serverHardwareUri": 'SH:' + PTS2_PROFILE2_SERVER,
    "serverProfileTemplateUri": "SPT:" + PTS2_SPT2_NAME,
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "Alder",
                    "displayName": "Alder",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True,
                    "loginPriv": True,
                    "hostBIOSConfigPriv": True,
                    "hostNICConfigPriv": True,
                    "hostStorageConfigPriv": True
                }]
            }
        }]
    },
}

# profile compliance
pts2_profile2_compliance = {
    "name": PTS2_PROFILE2_NAME,
    "compliance-preview":
    {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "isOnlineUpdate": None,
        "automaticUpdates": [],
        "manualUpdates": [],
    }
}

pts2_profile2_edit = {
    "type": SERVER_PROFILE_TYPE,
    "name": PTS2_PROFILE2_NAME,
    "serverHardwareUri": 'SH:' + PTS2_PROFILE2_SERVER,
    "serverProfileTemplateUri": "SPT:" + PTS2_SPT2_NAME,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "iscsiInitiatorNameType": "AutoGenerated",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": []
    },
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "Alder",
                    "displayName": "Alder",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True,
                    "loginPriv": True,
                    "hostBIOSConfigPriv": True,
                    "hostNICConfigPriv": True,
                    "hostStorageConfigPriv": True
                },
                    {
                    "userName": "Aspen",
                    "displayName": "Aspen",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True,
                    "loginPriv": True,
                    "hostBIOSConfigPriv": True,
                    "hostNICConfigPriv": True,
                    "hostStorageConfigPriv": True
                },
                ]
            }
        }]
    },
}

# profile non compliance
pts2_profile2_non_compliance = {
    "name": PTS2_PROFILE2_NAME,
    "compliance-preview":
    {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "isOnlineUpdate": True,
        "automaticUpdates": ["Modify Management Processor LocalAccounts to match template."],
        "manualUpdates": [],
    }
}


pts2_spts_create = [pts2_spt1_create.copy(), pts2_spt2_create.copy()]

pts2_profiles_create = [
    pts2_profile1_create.copy(),
    pts2_profile2_create.copy()]

pts2_profiles_create_expected = [
    pts2_profile1_create_expected,
    pts2_profile2_create_expected]

pts2_profiles_compliance = [pts2_profile1_compliance, pts2_profile2_compliance]

pts2_profiles_edit = [pts2_profile1_edit.copy(), pts2_profile2_edit.copy()]

pts2_profiles_non_compliance = [
    pts2_profile1_non_compliance,
    pts2_profile2_non_compliance]

# PTS3 edit SPT to create non-compliance
pts3_spt1_create = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": PTS3_SPT1_NAME,
    "serverHardwareTypeUri": 'SHT:' + PTS3_SPT1_SHT,
    "enclosureGroupUri": 'EG:' + PTS3_SPT1_EG,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "iscsiInitiatorNameType": "AutoGenerated",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [],
        "manageConnections": False
    },
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "Maple",
                    "displayName": "Maple",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True
                }]
            }
        }]
    },
}

pts3_spt1_edit = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": PTS3_SPT1_NAME,
    "serverHardwareTypeUri": 'SHT:' + PTS3_SPT1_SHT,
    "enclosureGroupUri": 'EG:' + PTS3_SPT1_EG,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "iscsiInitiatorNameType": "AutoGenerated",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [],
        "manageConnections": False
    },
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "Maple",
                    "displayName": "Maple",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": False
                }]
            }
        }]
    },
}

pts3_spt2_create = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": PTS3_SPT2_NAME,
    "serverHardwareTypeUri": 'SHT:' + PTS3_SPT2_SHT,
    "enclosureGroupUri": 'EG:' + PTS3_SPT2_EG,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "iscsiInitiatorNameType": "AutoGenerated",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [],
        "manageConnections": False
    },
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "Maple",
                    "displayName": "Maple",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True,
                    "loginPriv": True,
                    "hostBIOSConfigPriv": True,
                    "hostNICConfigPriv": True,
                    "hostStorageConfigPriv": True
                }]
            }
        }]
    },
}

pts3_spt2_edit = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": PTS3_SPT2_NAME,
    "serverHardwareTypeUri": 'SHT:' + PTS3_SPT2_SHT,
    "enclosureGroupUri": 'EG:' + PTS3_SPT2_EG,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "iscsiInitiatorNameType": "AutoGenerated",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [],
        "manageConnections": False
    },
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "Maple",
                    "displayName": "Maple",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": False,
                    "loginPriv": True,
                    "hostBIOSConfigPriv": True,
                    "hostNICConfigPriv": True,
                    "hostStorageConfigPriv": True
                }]
            }
        }]
    },
}

pts3_profile1_create = {
    "type": SERVER_PROFILE_TYPE,
    "name": PTS3_PROFILE1_NAME,
    "serverHardwareUri": 'SH:' + PTS3_PROFILE1_SERVER,
    "serverProfileTemplateUri": "SPT:" + PTS3_SPT1_NAME,
}

pts3_profile1_create_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": PTS3_PROFILE1_NAME,
    "serverHardwareUri": 'SH:' + PTS3_PROFILE1_SERVER,
    "serverProfileTemplateUri": "SPT:" + PTS3_SPT1_NAME,
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "Maple",
                    "displayName": "Maple",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True
                }]
            }
        }]
    },
}

# profile compliance
pts3_profile1_compliance = {
    "name": PTS3_PROFILE1_NAME,
    "compliance-preview":
    {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "isOnlineUpdate": None,
        "automaticUpdates": [],
        "manualUpdates": [],
    }
}

# profile non compliance
pts3_profile1_non_compliance = {
    "name": PTS3_PROFILE1_NAME,
    "compliance-preview":
    {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "isOnlineUpdate": True,
        "automaticUpdates": ["Modify Management Processor LocalAccounts to match template."],
        "manualUpdates": [],
    }
}

pts3_profile1_patch_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": PTS3_PROFILE1_NAME,
    "serverHardwareUri": 'SH:' + PTS3_PROFILE1_SERVER,
    "serverProfileTemplateUri": "SPT:" + PTS3_SPT1_NAME,
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "Maple",
                    "displayName": "Maple",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": False
                }]
            }
        }]
    },
}

pts3_profile2_create = {
    "type": SERVER_PROFILE_TYPE,
    "name": PTS3_PROFILE2_NAME,
    "serverHardwareUri": 'SH:' + PTS3_PROFILE2_SERVER,
    "serverProfileTemplateUri": "SPT:" + PTS3_SPT2_NAME,
}

pts3_profile2_create_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": PTS3_PROFILE2_NAME,
    "serverHardwareUri": 'SH:' + PTS3_PROFILE2_SERVER,
    "serverProfileTemplateUri": "SPT:" + PTS3_SPT2_NAME,
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "Maple",
                    "displayName": "Maple",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True,
                    "loginPriv": True,
                    "hostBIOSConfigPriv": True,
                    "hostNICConfigPriv": True,
                    "hostStorageConfigPriv": True
                }]
            }
        }]
    },
}

# profile compliance
pts3_profile2_compliance = {
    "name": PTS3_PROFILE2_NAME,
    "compliance-preview":
    {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "isOnlineUpdate": None,
        "automaticUpdates": [],
        "manualUpdates": [],
    }
}

# profile compliance
pts3_profile2_non_compliance = {
    "name": PTS3_PROFILE2_NAME,
    "compliance-preview":
    {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "isOnlineUpdate": True,
        "automaticUpdates": ["Modify Management Processor LocalAccounts to match template."],
        "manualUpdates": [],
    }
}


pts3_profile2_patch_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": PTS3_PROFILE2_NAME,
    "serverHardwareUri": 'SH:' + PTS3_PROFILE2_SERVER,
    "serverProfileTemplateUri": "SPT:" + PTS3_SPT2_NAME,
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "Maple",
                    "displayName": "Maple",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": False,
                    "loginPriv": True,
                    "hostBIOSConfigPriv": True,
                    "hostNICConfigPriv": True,
                    "hostStorageConfigPriv": True
                }]
            }
        }]
    },
}

pts3_spts_create = [pts3_spt1_create.copy(), pts3_spt2_create.copy()]

pts3_spts_edit = [pts3_spt1_edit.copy(), pts3_spt2_edit.copy()]

pts3_profiles_create = [
    pts3_profile1_create.copy(),
    pts3_profile2_create.copy()]

pts3_profiles_create_expected = [
    pts3_profile1_create_expected,
    pts3_profile2_create_expected]

pts3_profiles_compliance = [pts3_profile1_compliance, pts3_profile2_compliance]

pts3_profiles_non_compliance = [
    pts3_profile1_non_compliance,
    pts3_profile2_non_compliance]

pts3_profiles_patch_expected = [
    pts3_profile1_patch_expected,
    pts3_profile2_patch_expected]

# PTS4 create SPT from SP
# PTS1 create and edit SP and validate the password
pts4_profile1_create = {
    "type": SERVER_PROFILE_TYPE,
    "name": PTS4_PROFILE1_NAME,
    "serverHardwareUri": 'SH:' + PTS4_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + PTS4_PROFILE1_EG,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "iscsiInitiatorNameType": "AutoGenerated",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": []
    },
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "Oak",
                    "displayName": "Oak",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True
                },
                ]
            }
        }]
    },
}

pts4_profile2_create = {
    "type": SERVER_PROFILE_TYPE,
    "name": PTS4_PROFILE2_NAME,
    "serverHardwareUri": 'SH:' + PTS4_PROFILE2_SERVER,
    "enclosureGroupUri": 'EG:' + PTS4_PROFILE2_EG,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "iscsiInitiatorNameType": "AutoGenerated",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": []
    },
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "Oak",
                    "displayName": "Oak",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True,
                    "loginPriv": True,
                    "hostBIOSConfigPriv": True,
                    "hostNICConfigPriv": True,
                    "hostStorageConfigPriv": True
                },
                ]
            }
        }]
    },
}

pts4_spt1_create_expected = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE, "name": PTS4_SPT1_NAME,
    "serverHardwareTypeUri": 'SHT:' + PTS4_SPT1_SHT, "enclosureGroupUri": 'EG:' + PTS4_SPT1_EG,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "iscsiInitiatorNameType": "AutoGenerated",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [],
        "manageConnections": True
    },
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "Oak",
                    "displayName": "Oak",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True
                },
                ]
            }
        }]
    },
}

pts4_spt2_create_expected = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE, "name": PTS4_SPT2_NAME,
    "serverHardwareTypeUri": 'SHT:' + PTS4_SPT2_SHT, "enclosureGroupUri": 'EG:' + PTS4_SPT2_EG,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "iscsiInitiatorNameType": "AutoGenerated",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [],
        "manageConnections": True
    },
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "Oak",
                    "displayName": "Oak",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True,
                    "loginPriv": True,
                    "hostBIOSConfigPriv": True,
                    "hostNICConfigPriv": True,
                    "hostStorageConfigPriv": True
                },
                ]
            }
        }]
    },
}

pts4_profiles_create = [
    pts4_profile1_create.copy(),
    pts4_profile2_create.copy()]

pts4_spts_create_expected = [
    pts4_spt1_create_expected,
    pts4_spt2_create_expected]

# PTS5 manageMp
pts5_profile1_create = {
    "type": SERVER_PROFILE_TYPE,
    "name": PTS5_PROFILE1_NAME,
    "serverHardwareUri": 'SH:' + PTS5_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + PTS5_PROFILE1_EG,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "iscsiInitiatorNameType": "AutoGenerated",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": []
    },
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "Spruce",
                    "displayName": "Spruce",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True
                },
                ]
            }
        }]
    },
}

pts5_profile1_edit = {
    "type": SERVER_PROFILE_TYPE,
    "name": PTS5_PROFILE1_NAME,
    "serverHardwareUri": 'SH:' + PTS5_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + PTS5_PROFILE1_EG,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "iscsiInitiatorNameType": "AutoGenerated",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": []
    },
    "managementProcessor": {
        "manageMp": False,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "Spruce",
                    "displayName": "Spruce",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True
                },
                ]
            }
        }]
    },
}

pts5_profile2_create = {
    "type": SERVER_PROFILE_TYPE,
    "name": PTS5_PROFILE2_NAME,
    "serverHardwareUri": 'SH:' + PTS5_PROFILE2_SERVER,
    "enclosureGroupUri": 'EG:' + PTS5_PROFILE2_EG,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "iscsiInitiatorNameType": "AutoGenerated",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": []
    },
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "Spruce",
                    "displayName": "Spruce",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True,
                    "loginPriv": True,
                    "hostBIOSConfigPriv": True,
                    "hostNICConfigPriv": True,
                    "hostStorageConfigPriv": True
                },
                ]
            }
        }]
    },
}

pts5_profile2_edit = {
    "type": SERVER_PROFILE_TYPE,
    "name": PTS5_PROFILE2_NAME,
    "serverHardwareUri": 'SH:' + PTS5_PROFILE2_SERVER,
    "enclosureGroupUri": 'EG:' + PTS5_PROFILE2_EG,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "iscsiInitiatorNameType": "AutoGenerated",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": []
    },
    "managementProcessor": {
        "manageMp": False,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "Spruce",
                    "displayName": "Spruce",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True,
                    "loginPriv": True,
                    "hostBIOSConfigPriv": True,
                    "hostNICConfigPriv": True,
                    "hostStorageConfigPriv": True
                },
                ]
            }
        }]
    },
}

pts5_profiles_create = [
    pts5_profile1_create.copy(),
    pts5_profile2_create.copy()]

pts5_profiles_edit = [pts5_profile1_edit.copy(), pts5_profile2_edit.copy()]

# PTS6 unaissgn and assign profile
pts6_profile1_create = {
    "type": SERVER_PROFILE_TYPE,
    "name": PTS6_PROFILE1_NAME,
    "serverHardwareUri": 'SH:' + PTS6_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + PTS6_PROFILE1_EG,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "iscsiInitiatorNameType": "AutoGenerated",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": []
    },
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "Cedar1",
                    "displayName": "Cedar1",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True
                },
                    {
                    "userName": "Cedar2",
                    "displayName": "Cedar2",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True
                },
                    {
                    "userName": "Cedar3",
                    "displayName": "Cedar3",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True
                },
                ]
            }
        }]
    },
}

pts6_profile1_unassign = {
    "type": SERVER_PROFILE_TYPE,
    "name": PTS6_PROFILE1_NAME,
    "serverHardwareUri": '',
    "serverHardwareTypeUri": 'SHT:' + PTS6_PROFILE1_SHT,
    "enclosureGroupUri": 'EG:' + PTS6_PROFILE1_EG,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "iscsiInitiatorNameType": "AutoGenerated",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": []
    },
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "Cedar1",
                    "displayName": "Cedar1",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True
                },
                    {
                    "userName": "Cedar2",
                    "displayName": "Cedar2",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True
                },
                    {
                    "userName": "Cedar3",
                    "displayName": "Cedar3",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True
                },
                ]
            }
        }]
    },
}

pts6_profile1_reassign = {
    "type": SERVER_PROFILE_TYPE,
    "name": PTS6_PROFILE1_NAME,
    "serverHardwareUri": 'SH:' + PTS6_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + PTS6_PROFILE1_EG,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "iscsiInitiatorNameType": "AutoGenerated",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": []
    },
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "Cedar1",
                    "displayName": "Cedar1",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True
                },
                    {
                    "userName": "Cedar2",
                    "displayName": "Cedar2",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True
                },
                ]
            }
        }]
    },
}

pts6_profile2_create = {
    "type": SERVER_PROFILE_TYPE,
    "name": PTS6_PROFILE2_NAME,
    "serverHardwareUri": 'SH:' + PTS6_PROFILE2_SERVER,
    "enclosureGroupUri": 'EG:' + PTS6_PROFILE2_EG,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "iscsiInitiatorNameType": "AutoGenerated",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": []
    },
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "Cedar1",
                    "displayName": "Cedar1",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True,
                    "loginPriv": True,
                    "hostBIOSConfigPriv": True,
                    "hostNICConfigPriv": True,
                    "hostStorageConfigPriv": True
                },
                    {
                    "userName": "Cedar2",
                    "displayName": "Cedar2",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True,
                    "loginPriv": True,
                    "hostBIOSConfigPriv": True,
                    "hostNICConfigPriv": True,
                    "hostStorageConfigPriv": True
                },
                    {
                    "userName": "Cedar3",
                    "displayName": "Cedar3",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True,
                    "loginPriv": True,
                    "hostBIOSConfigPriv": True,
                    "hostNICConfigPriv": True,
                    "hostStorageConfigPriv": True
                },
                ]
            }
        }]
    },
}

pts6_profile2_unassign = {
    "type": SERVER_PROFILE_TYPE,
    "name": PTS6_PROFILE2_NAME,
    "serverHardwareUri": '',
    "serverHardwareTypeUri": 'SHT:' + PTS6_PROFILE2_SHT,
    "enclosureGroupUri": 'EG:' + PTS6_PROFILE2_EG,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "iscsiInitiatorNameType": "AutoGenerated",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": []
    },
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "Cedar1",
                    "displayName": "Cedar1",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True,
                    "loginPriv": True,
                    "hostBIOSConfigPriv": True,
                    "hostNICConfigPriv": True,
                    "hostStorageConfigPriv": True
                },
                    {
                    "userName": "Cedar2",
                    "displayName": "Cedar2",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True,
                    "loginPriv": True,
                    "hostBIOSConfigPriv": True,
                    "hostNICConfigPriv": True,
                    "hostStorageConfigPriv": True
                },
                    {
                    "userName": "Cedar3",
                    "displayName": "Cedar3",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True,
                    "loginPriv": True,
                    "hostBIOSConfigPriv": True,
                    "hostNICConfigPriv": True,
                    "hostStorageConfigPriv": True
                },
                ]
            }
        }]
    },
}

pts6_profile2_reassign = {
    "type": SERVER_PROFILE_TYPE,
    "name": PTS6_PROFILE2_NAME,
    "serverHardwareUri": 'SH:' + PTS6_PROFILE2_SERVER,
    "enclosureGroupUri": 'EG:' + PTS6_PROFILE2_EG,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "iscsiInitiatorNameType": "AutoGenerated",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": []
    },
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "Cedar1",
                    "displayName": "Cedar1",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True,
                    "loginPriv": True,
                    "hostBIOSConfigPriv": True,
                    "hostNICConfigPriv": True,
                    "hostStorageConfigPriv": True
                },
                    {
                    "userName": "Cedar2",
                    "displayName": "Cedar2",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True,
                    "loginPriv": True,
                    "hostBIOSConfigPriv": True,
                    "hostNICConfigPriv": True,
                    "hostStorageConfigPriv": True
                },
                ]
            }
        }]
    },
}

pts6_profiles_create = [
    pts6_profile1_create.copy(),
    pts6_profile2_create.copy()]

pts6_profiles_unassign = [
    pts6_profile1_unassign.copy(),
    pts6_profile2_unassign.copy()]

pts6_profiles_reassign = [
    pts6_profile1_reassign.copy(),
    pts6_profile2_reassign.copy()]

# PTS7 move profile
pts7_profile_create = {
    "type": SERVER_PROFILE_TYPE,
    "name": PTS7_PROFILE_NAME,
    "serverHardwareUri": 'SH:' + PTS7_PROFILE_SERVER,
    "enclosureGroupUri": 'EG:' + PTS7_PROFILE_EG,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "iscsiInitiatorNameType": "AutoGenerated",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": []
    },
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "Acacia1",
                    "displayName": "Acacia1",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True
                },
                    {
                    "userName": "Acacia2",
                    "displayName": "Acacia2",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True
                },
                    {
                    "userName": "Acacia3",
                    "displayName": "Acacia3",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True
                },
                    {
                    "userName": "Acacia4",
                    "displayName": "Acacia4",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True
                },
                    {
                    "userName": "Acacia5",
                    "displayName": "Acacia5",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True
                },
                ]
            }
        }]
    },
}

pts7_profile_create_expected = pts7_profile_create.copy()

pts7_profile_gen9_to_gen10_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": PTS7_PROFILE_NAME,
    "serverHardwareTypeUri": 'SHT:' + PTS7_PROFILE_MOVE_SHT,
    "enclosureGroupUri": 'EG:' + PTS7_PROFILE_MOVE_EG,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "iscsiInitiatorNameType": "AutoGenerated",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": []
    },
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "Acacia1",
                    "displayName": "Acacia1",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True,
                    "loginPriv": False,
                    "hostBIOSConfigPriv": False,
                    "hostNICConfigPriv": False,
                    "hostStorageConfigPriv": False,

                },
                    {
                    "userName": "Acacia2",
                    "displayName": "Acacia2",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True,
                    "loginPriv": False,
                    "hostBIOSConfigPriv": False,
                    "hostNICConfigPriv": False,
                    "hostStorageConfigPriv": False,
                },
                    {
                    "userName": "Acacia3",
                    "displayName": "Acacia3",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True,
                    "loginPriv": False,
                    "hostBIOSConfigPriv": False,
                    "hostNICConfigPriv": False,
                    "hostStorageConfigPriv": False,
                },
                    {
                    "userName": "Acacia4",
                    "displayName": "Acacia4",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True,
                    "loginPriv": False,
                    "hostBIOSConfigPriv": False,
                    "hostNICConfigPriv": False,
                    "hostStorageConfigPriv": False,
                },
                    {
                    "userName": "Acacia5",
                    "displayName": "Acacia5",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True,
                    "loginPriv": False,
                    "hostBIOSConfigPriv": False,
                    "hostNICConfigPriv": False,
                    "hostStorageConfigPriv": False,
                },
                ]
            }
        }]
    },
}

pts7_profile_move = {
    "type": SERVER_PROFILE_TYPE,
    "name": PTS7_PROFILE_NAME,
    "serverHardwareUri": 'SH:' + PTS7_PROFILE_MOVE_SERVER,
    "enclosureGroupUri": 'EG:' + PTS7_PROFILE_MOVE_EG,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "iscsiInitiatorNameType": "AutoGenerated",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": []
    },
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "Acacia1",
                    "displayName": "Acacia1",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True,
                    "loginPriv": True,
                    "hostBIOSConfigPriv": True,
                    "hostNICConfigPriv": True,
                    "hostStorageConfigPriv": True
                },
                    {
                    "userName": "Acacia2",
                    "displayName": "Acacia2",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True,
                    "loginPriv": True,
                    "hostBIOSConfigPriv": True,
                    "hostNICConfigPriv": True,
                    "hostStorageConfigPriv": True
                },
                    {
                    "userName": "Acacia3",
                    "displayName": "Acacia3",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True,
                    "loginPriv": True,
                    "hostBIOSConfigPriv": True,
                    "hostNICConfigPriv": True,
                    "hostStorageConfigPriv": True
                },
                    {
                    "userName": "Acacia4",
                    "displayName": "Acacia4",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True,
                    "loginPriv": True,
                    "hostBIOSConfigPriv": True,
                    "hostNICConfigPriv": True,
                    "hostStorageConfigPriv": True
                },
                ]
            }
        }]
    },
}

pts7_profile_move_expected = pts7_profile_move.copy()

pts7_profile_gen10_to_gen9_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": PTS7_PROFILE_NAME,
    "serverHardwareTypeUri": 'SHT:' + PTS7_PROFILE_SHT,
    "enclosureGroupUri": 'EG:' + PTS7_PROFILE_EG,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "iscsiInitiatorNameType": "AutoGenerated",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": []
    },
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "Acacia1",
                    "displayName": "Acacia1",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True,
                },
                    {
                    "userName": "Acacia2",
                    "displayName": "Acacia2",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True,
                },
                    {
                    "userName": "Acacia3",
                    "displayName": "Acacia3",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True,
                },
                    {
                    "userName": "Acacia4",
                    "displayName": "Acacia4",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True,
                },
                ]
            }
        }]
    },
}

pts7_profile_move_back = {
    "type": SERVER_PROFILE_TYPE,
    "name": PTS7_PROFILE_NAME,
    "serverHardwareUri": 'SH:' + PTS7_PROFILE_SERVER,
    "enclosureGroupUri": 'EG:' + PTS7_PROFILE_EG,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "iscsiInitiatorNameType": "AutoGenerated",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": []
    },
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "Acacia1",
                    "displayName": "Acacia1",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True
                },
                    {
                    "userName": "Acacia2",
                    "displayName": "Acacia2",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True
                },
                    {
                    "userName": "Acacia3",
                    "displayName": "Acacia3",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True
                },
                ]
            }
        }]
    },
}

pts7_profile_move_back_expected = pts7_profile_move_back.copy()

pts7_profiles_create = [pts7_profile_create.copy()]

pts7_profiles_move = [pts7_profile_move.copy()]

pts7_profiles_move_back = [pts7_profile_move_back.copy()]

# PTS8 B/R
pts8_spt1_create = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": PTS8_SPT1_NAME,
    "serverHardwareTypeUri": 'SHT:' + PTS8_SPT1_SHT,
    "enclosureGroupUri": 'EG:' + PTS8_SPT1_EG,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "iscsiInitiatorNameType": "AutoGenerated",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [],
        "manageConnections": False
    },
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "Willow",
                    "displayName": "Willow",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True
                }]
            }
        }]
    },
}

pts8_spt2_create = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": PTS8_SPT2_NAME,
    "serverHardwareTypeUri": 'SHT:' + PTS8_SPT2_SHT,
    "enclosureGroupUri": 'EG:' + PTS8_SPT2_EG,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "iscsiInitiatorNameType": "AutoGenerated",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [],
        "manageConnections": False
    },
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "Willow",
                    "displayName": "Willow",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True,
                    "loginPriv": True,
                    "hostBIOSConfigPriv": True,
                    "hostNICConfigPriv": True,
                    "hostStorageConfigPriv": True
                }]
            }
        }]
    },
}

pts8_profile1_create = {
    "type": SERVER_PROFILE_TYPE,
    "name": PTS8_PROFILE1_NAME,
    "serverHardwareUri": 'SH:' + PTS8_PROFILE1_SERVER,
    "serverProfileTemplateUri": "SPT:" + PTS8_SPT1_NAME,
}

pts8_profile1_create_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": PTS8_PROFILE1_NAME,
    "serverHardwareUri": 'SH:' + PTS8_PROFILE1_SERVER,
    "serverProfileTemplateUri": "SPT:" + PTS8_SPT1_NAME,
    "enclosureGroupUri": 'EG:' + PTS8_PROFILE1_EG,
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "Willow",
                    "displayName": "Willow",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True
                }]
            }
        }]
    },
}

pts8_profile1_unassign = {
    "type": SERVER_PROFILE_TYPE,
    "name": PTS8_PROFILE1_NAME,
    "serverHardwareUri": '',
    "serverHardwareTypeUri": 'SHT:' + PTS8_PROFILE1_SHT,
    "serverProfileTemplateUri": "SPT:" + PTS8_SPT1_NAME,
    "enclosureGroupUri": 'EG:' + PTS8_PROFILE1_EG,
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "Willow",
                    "displayName": "Willow",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True
                }]
            }
        }]
    },
}

pts8_profile1_reassign = {
    "type": SERVER_PROFILE_TYPE,
    "name": PTS8_PROFILE1_NAME,
    "serverHardwareUri": 'SH:' + PTS8_PROFILE1_SERVER,
    "serverProfileTemplateUri": "SPT:" + PTS8_SPT1_NAME,
    "enclosureGroupUri": 'EG:' + PTS8_PROFILE1_EG,
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "Willow",
                    "displayName": "Willow",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True
                }]
            }
        }]
    },
}

pts8_profile2_create = {
    "type": SERVER_PROFILE_TYPE,
    "name": PTS8_PROFILE2_NAME,
    "serverHardwareUri": 'SH:' + PTS8_PROFILE2_SERVER,
    "serverProfileTemplateUri": "SPT:" + PTS8_SPT2_NAME,
}

pts8_profile2_create_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": PTS8_PROFILE2_NAME,
    "serverHardwareUri": 'SH:' + PTS8_PROFILE2_SERVER,
    "serverProfileTemplateUri": "SPT:" + PTS8_SPT2_NAME,
    "enclosureGroupUri": 'EG:' + PTS8_PROFILE2_EG,
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "Willow",
                    "displayName": "Willow",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True,
                    "loginPriv": True,
                    "hostBIOSConfigPriv": True,
                    "hostNICConfigPriv": True,
                    "hostStorageConfigPriv": True
                }]
            }
        }]
    },
}

pts8_profile2_unassign = {
    "type": SERVER_PROFILE_TYPE,
    "name": PTS8_PROFILE2_NAME,
    "serverHardwareUri": '',
    "serverHardwareTypeUri": 'SHT:' + PTS8_PROFILE2_SHT,
    "serverProfileTemplateUri": "SPT:" + PTS8_SPT2_NAME,
    "enclosureGroupUri": 'EG:' + PTS8_PROFILE2_EG,
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "Willow",
                    "displayName": "Willow",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True,
                    "loginPriv": True,
                    "hostBIOSConfigPriv": True,
                    "hostNICConfigPriv": True,
                    "hostStorageConfigPriv": True
                }]
            }
        }]
    },
}

pts8_profile2_reassign = {
    "type": SERVER_PROFILE_TYPE,
    "name": PTS8_PROFILE2_NAME,
    "serverHardwareUri": 'SH:' + PTS8_PROFILE2_SERVER,
    "serverProfileTemplateUri": "SPT:" + PTS8_SPT2_NAME,
    "enclosureGroupUri": 'EG:' + PTS8_PROFILE2_EG,
    "managementProcessor": {
        "manageMp": True,
        "mpSettings": [{
            "settingType": "LocalAccounts",
            "args": {
                "localAccounts": [{
                    "userName": "Willow",
                    "displayName": "Willow",
                    "password": "hpvse123",
                    "userConfigPriv": True,
                    "remoteConsolePriv": True,
                    "virtualMediaPriv": True,
                    "virtualPowerAndResetPriv": True,
                    "iLOConfigPriv": True,
                    "loginPriv": True,
                    "hostBIOSConfigPriv": True,
                    "hostNICConfigPriv": True,
                    "hostStorageConfigPriv": True
                }]
            }
        }]
    },
}

pts8_spts_create = [pts8_spt1_create.copy(), pts8_spt2_create.copy()]

pts8_profiles_create = [
    pts8_profile1_create.copy(),
    pts8_profile2_create.copy()]

pts8_profiles_create_expected = [
    pts8_profile1_create_expected,
    pts8_profile2_create_expected]

pts8_profiles_unassign = [
    pts8_profile1_unassign.copy(),
    pts8_profile2_unassign.copy()]

pts8_profiles_reassign = [
    pts8_profile1_reassign.copy(),
    pts8_profile2_reassign.copy()]

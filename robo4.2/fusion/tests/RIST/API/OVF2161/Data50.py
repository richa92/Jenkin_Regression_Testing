from dto import *
from env_variables import *

# Credentials
oa_credentials = {'username': 'Administrator', 'password': 'hpvse14'}
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

# Name prefixes
NAME_PREFIX = 'Synergy-Ring1-OVF2161-'
SPT_NAME_PREFIX = NAME_PREFIX
PROFILE_NAME_PREFIX = NAME_PREFIX
# SHT
SHT_GEN10_SY480 = 'SH:' + ENC2SHBAY7
SHT_GEN10_SY660 = 'SH:' + ENC1SHBAY6
SHT_GEN9_SY480 = 'SH:' + ENC1SHBAY7
SHT_GEN9_SY660 = 'SH:' + ENC1SHBAY5
# SH
SHT_GEN10_SY480_SERVER1 = ENC2SHBAY7
SHT_GEN10_SY480_SERVER2 = ENC2SHBAY8
SHT_GEN10_SY660_SERVER1 = ENC1SHBAY6
SHT_GEN9_SY480_SERVER1 = ENC1SHBAY7
SHT_GEN9_SY660_SERVER1 = ENC1SHBAY5
# NTS1 SPT
NTS1_SPT1_NAME = SPT_NAME_PREFIX + 'nts1-spt1'
NTS1_SPT2_NAME = SPT_NAME_PREFIX + 'nts1-spt2'
NTS1_SPT3_NAME = SPT_NAME_PREFIX + 'nts1-spt3'
NTS1_SPT_EG = EG_NAME
# NTS2 SPT
NTS2_SPT_NAME = SPT_NAME_PREFIX + 'nts2-spt'
NTS2_SPT_EG = EG_NAME
# NTS3 Profile
NTS3_PROFILE1_NAME = PROFILE_NAME_PREFIX + 'nts3-profile1'
NTS3_PROFILE1_SERVER = SHT_GEN9_SY480_SERVER1
NTS3_PROFILE1_EG = EG_NAME
NTS3_PROFILE2_NAME = PROFILE_NAME_PREFIX + 'nts3-profile2'
NTS3_PROFILE2_SERVER = SHT_GEN10_SY480_SERVER1
NTS3_PROFILE2_EG = EG_NAME
NTS3_PROFILE3_NAME = PROFILE_NAME_PREFIX + 'nts3-profile3'
NTS3_PROFILE3_SERVER = SHT_GEN10_SY480_SERVER1
NTS3_PROFILE3_EG = EG_NAME
# NTS4 Profile
NTS4_PROFILE_NAME = PROFILE_NAME_PREFIX + 'nts4-profile'
NTS4_PROFILE_SERVER = SHT_GEN10_SY480_SERVER1
NTS4_PROFILE_EG = EG_NAME
NTS4_PROFILE_EDIT1_SERVER = SHT_GEN9_SY480_SERVER1
NTS4_PROFILE_EDIT1_EG = EG_NAME
# PTS1 SPT and Profile
PTS1_SPT1_NAME = SPT_NAME_PREFIX + 'pts1-spt1'
PTS1_SPT1_SHT = SHT_GEN10_SY480
PTS1_SPT1_EG = EG_NAME
PTS1_SPT1_PROFILE_NAME = PROFILE_NAME_PREFIX + 'pts1-spt1-profile'
PTS1_SPT1_PROFILE_SERVER = SHT_GEN10_SY480_SERVER1
PTS1_SPT1_PROFILE_EG = EG_NAME
PTS1_SPT2_NAME = SPT_NAME_PREFIX + 'pts1-spt2'
PTS1_SPT2_SHT = SHT_GEN10_SY660
PTS1_SPT2_EG = EG_NAME
PTS1_SPT2_PROFILE_NAME = PROFILE_NAME_PREFIX + 'pts1-spt2-profile'
PTS1_SPT2_PROFILE_SERVER = SHT_GEN10_SY660_SERVER1
PTS1_SPT2_PROFILE_EG = EG_NAME
# PTS2 SPT and Profile
PTS2_PROFILE_NAME = PROFILE_NAME_PREFIX + 'pts2-profile'
PTS2_PROFILE_SERVER = SHT_GEN10_SY480_SERVER1
PTS2_PROFILE_EG = EG_NAME
PTS2_SPT_FROM_SP_NAME = SPT_NAME_PREFIX + 'pts2-spt-from-sp'
PTS2_SPT_FROM_SP_SHT = SHT_GEN10_SY480
PTS2_SPT_FROM_SP_EG = EG_NAME
PTS2_SP_FROM_SPT_NAME = PROFILE_NAME_PREFIX + 'pts2-sp-from-spt'
PTS2_SP_FROM_SPT_SERVER = SHT_GEN10_SY480_SERVER2
PTS2_SP_FROM_SPT_EG = EG_NAME
# PTS3 Profile
PTS3_PROFILE_NAME = PROFILE_NAME_PREFIX + 'pts3-profile'
PTS3_PROFILE_SERVER = SHT_GEN10_SY480_SERVER1
PTS3_PROFILE_EG = EG_NAME
PTS3_PROFILE_MOVE_SERVER = SHT_GEN10_SY660_SERVER1
PTS3_PROFILE_MOVE_EG = EG_NAME
PTS3_PROFILE_EDIT_SERVER = SHT_GEN10_SY660_SERVER1
PTS3_PROFILE_EDIT_EG = EG_NAME
PTS3_PROFILE_MOVE_BACK_SERVER = SHT_GEN10_SY480_SERVER1
PTS3_PROFILE_MOVE_BACK_EG = EG_NAME
# PTS4 SPT and Profile
PTS4_SPT1_NAME = SPT_NAME_PREFIX + 'pts4-spt1'
PTS4_SPT1_EG = EG_NAME
PTS4_SPT1_SHT = SHT_GEN10_SY480
PTS4_SPT2_NAME = SPT_NAME_PREFIX + 'pts4-spt2'
PTS4_SPT2_EG = EG_NAME
PTS4_SPT2_SHT = SHT_GEN10_SY660
PTS4_PROFILE1_NAME = PROFILE_NAME_PREFIX + 'pts4-profile1'
PTS4_PROFILE1_SERVER = SHT_GEN10_SY480_SERVER1
PTS4_PROFILE1_EG = EG_NAME
PTS4_PROFILE2_NAME = PROFILE_NAME_PREFIX + 'pts4-profile2'
PTS4_PROFILE2_SERVER = SHT_GEN10_SY660_SERVER1
PTS4_PROFILE2_EG = EG_NAME
# Suite Setup and Teardown
PROFILE1_NAME = PROFILE_NAME_PREFIX + 'profile1'
PROFILE1_SERVER = SHT_GEN10_SY480_SERVER1
PROFILE1_EG = EG_NAME
PROFILE2_NAME = PROFILE_NAME_PREFIX + 'profile2'
PROFILE2_SERVER = SHT_GEN10_SY660_SERVER1
PROFILE2_EG = EG_NAME
PROFILE3_NAME = PROFILE_NAME_PREFIX + 'profile3'
PROFILE3_SERVER = SHT_GEN10_SY480_SERVER2
PROFILE3_EG = EG_NAME
# Profile complinace
COMPLIANCE_DISABLE_SECURE_BOOT_REGEX = 'REGEX:Change secure boot setting to Disabled.'
COMPLIANCE_ENABLE_SECURE_BOOT_REGEX = 'REGEX:Change secure boot setting to Enabled.'
# REGEX
RIS_SECURE_BOOT_CURRENT_BOOT_REGEX = 'REGEX:\w*'

# NTS1 create negative SPT
# unsupported SHT
nts1_negative_spt1 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE, "name": NTS1_SPT1_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT_GEN9_SY480, "enclosureGroupUri": 'EG:' + NTS1_SPT_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual",
    "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": [], "manageConnections": False},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": True, "mode": "UEFIOptimized", "secureBoot": "Enabled", "pxeBootPolicy": "Auto"},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
}

# unsupported SecureBoot value
nts1_negative_spt2 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE, "name": NTS1_SPT2_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT_GEN10_SY480, "enclosureGroupUri": 'EG:' + NTS1_SPT_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual",
    "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": [], "manageConnections": False},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": True, "mode": "UEFIOptimized", "secureBoot": "enabled", "pxeBootPolicy": "Auto"},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
}

# unsupported boot mode
nts1_negative_spt3 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE, "name": NTS1_SPT3_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT_GEN10_SY480, "enclosureGroupUri": 'EG:' + NTS1_SPT_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual",
    "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": [], "manageConnections": False},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": True, "mode": "UEFI", "secureBoot": "Enabled", "pxeBootPolicy": "Auto"},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
}

nts1_negative_spt_tasks = [
    {
        'keyword': 'Add Server Profile Template',
        'argument': nts1_negative_spt1.copy(),
        'taskState': 'Error',
        'errorMessage': 'SecureBoot_unsupported_SHT'
    },
    {
        'keyword': 'Add Server Profile Template',
        'argument': nts1_negative_spt2.copy(),
        'taskState': 'Error',
        'errorMessage': 'SecureBoot_invalid_value'
    },
    {
        'keyword': 'Add Server Profile Template',
        'argument': nts1_negative_spt3.copy(),
        'taskState': 'Error',
        'errorMessage': 'SecureBoot_unsupported_boot_mode'
    },
]

# NTS2 edit negative SPT
nts2_spt_create = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE, "name": NTS2_SPT_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT_GEN10_SY480, "enclosureGroupUri": 'EG:' + NTS2_SPT_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual",
    "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": [], "manageConnections": False},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": True, "mode": "UEFIOptimized", "secureBoot": "Enabled", "pxeBootPolicy": "Auto"},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
}

# unsupported SHT
nts2_spt_edit1 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE, "name": NTS2_SPT_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT_GEN9_SY480, "enclosureGroupUri": 'EG:' + NTS2_SPT_EG,
    "iscsiInitiatorNameType": "AutoGenerated",
    "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": [], "manageConnections": False},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": True, "mode": "UEFIOptimized", "secureBoot": "Enabled", "pxeBootPolicy": "Auto"},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
}

# unsupported SecureBoot value
nts2_spt_edit2 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE, "name": NTS2_SPT_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT_GEN10_SY480, "enclosureGroupUri": 'EG:' + NTS2_SPT_EG,
    "iscsiInitiatorNameType": "AutoGenerated",
    "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": [], "manageConnections": False},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": True, "mode": "UEFIOptimized", "secureBoot": "enabled", "pxeBootPolicy": "Auto"},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
}

# unsupported boot mode
nts2_spt_edit3 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE, "name": NTS2_SPT_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT_GEN10_SY480, "enclosureGroupUri": 'EG:' + NTS2_SPT_EG,
    "iscsiInitiatorNameType": "AutoGenerated",
    "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": [], "manageConnections": False},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": True, "mode": "UEFI", "secureBoot": "Enabled", "pxeBootPolicy": "Auto"},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
}

nts2_spts_create = [
    nts2_spt_create.copy(),
]

nts2_negative_spt_tasks = [
    {
        'keyword': 'Edit Server Profile Template',
        'argument': nts2_spt_edit1.copy(),
        'taskState': 'Error',
        'errorMessage': 'SecureBoot_unsupported_SHT'
    },
    {
        'keyword': 'Edit Server Profile Template',
        'argument': nts2_spt_edit2.copy(),
        'taskState': 'Error',
        'errorMessage': 'SecureBoot_invalid_value'
    },
    {
        'keyword': 'Edit Server Profile Template',
        'argument': nts2_spt_edit3.copy(),
        'taskState': 'Error',
        'errorMessage': 'SecureBoot_unsupported_boot_mode'
    },
]

# NTS3 create negative SP
nts3_negative_profile1 = {
    "type": SERVER_PROFILE_TYPE, "name": NTS3_PROFILE1_NAME,
    "serverHardwareUri": 'SH:' + NTS3_PROFILE1_SERVER, "enclosureGroupUri": 'EG:' + NTS3_PROFILE1_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual",
    "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "bootMode": {"manageMode": True, "mode": "UEFIOptimized", "pxeBootPolicy": "Auto", "secureBoot": "Enabled"},
    "boot": {"order": ["HardDisk"], "manageBoot": False},
    "firmware": {
        "firmwareScheduleDateTime": None, "firmwareActivationType": None, "firmwareInstallType": None,
        "forceInstallFirmware": False, "manageFirmware": False, "firmwareBaselineUri": None
    },
    "bios": {"overriddenSettings": [], "manageBios": False},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {"volumeAttachments": [], "sanSystemCredentials": [], "manageSanStorage": False},
    "hideUnusedFlexNics": True,
}

# unsupported SecureBoot value
nts3_negative_profile2 = {
    "type": SERVER_PROFILE_TYPE, "name": NTS3_PROFILE2_NAME,
    "serverHardwareUri": 'SH:' + NTS3_PROFILE2_SERVER, "enclosureGroupUri": 'EG:' + NTS3_PROFILE2_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual",
    "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "bootMode": {"manageMode": True, "mode": "UEFIOptimized", "pxeBootPolicy": "Auto", "secureBoot": "enabled"},
    "boot": {"order": ["HardDisk"], "manageBoot": False},
    "firmware": {
        "firmwareScheduleDateTime": None, "firmwareActivationType": None, "firmwareInstallType": None,
        "forceInstallFirmware": False, "manageFirmware": False, "firmwareBaselineUri": None
    },
    "bios": {"overriddenSettings": [], "manageBios": False},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {"volumeAttachments": [], "sanSystemCredentials": [], "manageSanStorage": False},
    "hideUnusedFlexNics": True,
}

# unsupported boot mode
nts3_negative_profile3 = {
    "type": SERVER_PROFILE_TYPE, "name": NTS3_PROFILE3_NAME,
    "serverHardwareUri": 'SH:' + NTS3_PROFILE3_SERVER, "enclosureGroupUri": 'EG:' + NTS3_PROFILE3_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual",
    "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto", "secureBoot": "Enabled"},
    "boot": {"order": ["HardDisk"], "manageBoot": False},
    "firmware": {
        "firmwareScheduleDateTime": None, "firmwareActivationType": None, "firmwareInstallType": None,
        "forceInstallFirmware": False, "manageFirmware": False, "firmwareBaselineUri": None
    },
    "bios": {"overriddenSettings": [], "manageBios": False},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {"volumeAttachments": [], "sanSystemCredentials": [], "manageSanStorage": False},
    "hideUnusedFlexNics": True,
}

nts3_negative_profile_tasks = [
    {
        'keyword': 'Add Server Profile',
        'argument': nts3_negative_profile1.copy(),
        'taskState': 'Error',
        'errorMessage': 'SecureBoot_unsupported_SHT'
    },
    {
        'keyword': 'Add Server Profile',
        'argument': nts3_negative_profile2.copy(),
        'taskState': 'Error',
        'errorMessage': 'SecureBoot_invalid_value'
    },
    {
        'keyword': 'Add Server Profile',
        'argument': nts3_negative_profile3.copy(),
        'taskState': 'Error',
        'errorMessage': 'SecureBoot_unsupported_boot_mode'
    },
]

# NTS4 edit negative SP
nts4_profile_create = {
    "type": SERVER_PROFILE_TYPE, "name": NTS4_PROFILE_NAME,
    "serverHardwareUri": 'SH:' + NTS4_PROFILE_SERVER, "enclosureGroupUri": 'EG:' + NTS4_PROFILE_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual",
    "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "bootMode": {"manageMode": True, "mode": "UEFIOptimized", "pxeBootPolicy": "Auto", "secureBoot": "Enabled"},
    "boot": {"order": ["HardDisk"], "manageBoot": False},
    "firmware": {
        "firmwareScheduleDateTime": None, "firmwareActivationType": None, "firmwareInstallType": None,
        "forceInstallFirmware": False, "manageFirmware": False, "firmwareBaselineUri": None
    },
    "bios": {"overriddenSettings": [], "manageBios": False},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {"volumeAttachments": [], "sanSystemCredentials": [], "manageSanStorage": False},
    "hideUnusedFlexNics": True,
}

# unsupported SHT
nts4_profile_edit1 = {
    "type": SERVER_PROFILE_TYPE, "name": NTS4_PROFILE_NAME,
    "serverHardwareUri": 'SH:' + NTS4_PROFILE_EDIT1_SERVER, "enclosureGroupUri": 'EG:' + NTS4_PROFILE_EDIT1_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual",
    "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "bootMode": {"manageMode": True, "mode": "UEFIOptimized", "pxeBootPolicy": "Auto", "secureBoot": "Enabled"},
    "boot": {"order": ["HardDisk"], "manageBoot": False},
    "firmware": {
        "firmwareScheduleDateTime": None, "firmwareActivationType": None, "firmwareInstallType": None,
        "forceInstallFirmware": False, "manageFirmware": False, "firmwareBaselineUri": None
    },
    "bios": {"overriddenSettings": [], "manageBios": False},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {"volumeAttachments": [], "sanSystemCredentials": [], "manageSanStorage": False},
    "hideUnusedFlexNics": True,
}

# unsupported SecureBoot value
nts4_profile_edit2 = {
    "type": SERVER_PROFILE_TYPE, "name": NTS4_PROFILE_NAME,
    "serverHardwareUri": 'SH:' + NTS4_PROFILE_SERVER, "enclosureGroupUri": 'EG:' + NTS4_PROFILE_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual",
    "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "bootMode": {"manageMode": True, "mode": "UEFIOptimized", "pxeBootPolicy": "Auto", "secureBoot": "enabled"},
    "boot": {"order": ["HardDisk"], "manageBoot": False},
    "firmware": {
        "firmwareScheduleDateTime": None, "firmwareActivationType": None, "firmwareInstallType": None,
        "forceInstallFirmware": False, "manageFirmware": False, "firmwareBaselineUri": None
    },
    "bios": {"overriddenSettings": [], "manageBios": False},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {"volumeAttachments": [], "sanSystemCredentials": [], "manageSanStorage": False},
    "hideUnusedFlexNics": True,
}

# unsupported boot mode
nts4_profile_edit3 = {
    "type": SERVER_PROFILE_TYPE, "name": NTS4_PROFILE_NAME,
    "serverHardwareUri": 'SH:' + NTS4_PROFILE_SERVER, "enclosureGroupUri": 'EG:' + NTS4_PROFILE_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual",
    "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto", "secureBoot": "Enabled"},
    "boot": {"order": ["HardDisk"], "manageBoot": False},
    "firmware": {
        "firmwareScheduleDateTime": None, "firmwareActivationType": None, "firmwareInstallType": None,
        "forceInstallFirmware": False, "manageFirmware": False, "firmwareBaselineUri": None
    },
    "bios": {"overriddenSettings": [], "manageBios": False},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {"volumeAttachments": [], "sanSystemCredentials": [], "manageSanStorage": False},
    "hideUnusedFlexNics": True,
}

nts4_profiles_create = [
    nts4_profile_create.copy(),
]

nts4_negative_profile_tasks = [
    {
        'keyword': 'Edit Server Profile',
        'argument': nts4_profile_edit1.copy(),
        'taskState': 'Error',
        'errorMessage': 'SecureBoot_unsupported_SHT'
    },
    {
        'keyword': 'Edit Server Profile',
        'argument': nts4_profile_edit2.copy(),
        'taskState': 'Error',
        'errorMessage': 'SecureBoot_invalid_value'
    },
    {
        'keyword': 'Edit Server Profile',
        'argument': nts4_profile_edit3.copy(),
        'taskState': 'Error',
        'errorMessage': 'SecureBoot_unsupported_boot_mode'
    },
]

pts1_spt1_create = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE, "name": PTS1_SPT1_NAME,
    "serverHardwareTypeUri": 'SHT:' + PTS1_SPT1_SHT, "enclosureGroupUri": 'EG:' + PTS1_SPT1_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual",
    "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": [], "manageConnections": False},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": True, "mode": "UEFIOptimized", "secureBoot": "Enabled", "pxeBootPolicy": "Auto"},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
}

pts1_spt1_edit = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE, "name": PTS1_SPT1_NAME,
    "serverHardwareTypeUri": 'SHT:' + PTS1_SPT1_SHT, "enclosureGroupUri": 'EG:' + PTS1_SPT1_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual",
    "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": [], "manageConnections": False},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": True, "mode": "UEFIOptimized", "secureBoot": "Disabled", "pxeBootPolicy": "Auto"},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
}

pts1_spt2_create = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE, "name": PTS1_SPT2_NAME,
    "serverHardwareTypeUri": 'SHT:' + PTS1_SPT2_SHT, "enclosureGroupUri": 'EG:' + PTS1_SPT2_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual",
    "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": [], "manageConnections": False},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": True, "mode": "UEFIOptimized", "secureBoot": "Disabled", "pxeBootPolicy": "Auto"},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
}

pts1_spt2_edit = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE, "name": PTS1_SPT2_NAME,
    "serverHardwareTypeUri": 'SHT:' + PTS1_SPT2_SHT, "enclosureGroupUri": 'EG:' + PTS1_SPT2_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual",
    "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": [], "manageConnections": False},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": True, "mode": "UEFIOptimized", "secureBoot": "Enabled", "pxeBootPolicy": "Auto"},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
}

pts1_spt1_profile_create = {
    "type": SERVER_PROFILE_TYPE, "name": PTS1_SPT1_PROFILE_NAME,
    "serverHardwareUri": 'SH:' + PTS1_SPT1_PROFILE_SERVER,
    "serverProfileTemplateUri": "SPT:" + PTS1_SPT1_NAME,
}

pts1_spt1_profile_create_expected = {
    "type": SERVER_PROFILE_TYPE, "name": PTS1_SPT1_PROFILE_NAME,
    "serverHardwareUri": 'SH:' + PTS1_SPT1_PROFILE_SERVER,
    "serverProfileTemplateUri": "SPT:" + PTS1_SPT1_NAME,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual",
    "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": True, "mode": "UEFIOptimized", "secureBoot": "Enabled", "pxeBootPolicy": "Auto"},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,

}

pts1_spt1_profile_compliant_compliance = {
    "name": PTS1_SPT1_PROFILE_NAME,
    "compliance-preview": {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "isOnlineUpdate": None,
        "automaticUpdates": [],
        "manualUpdates": []
    }
}

pts1_spt1_profile_edit_compliance = {
    "name": PTS1_SPT1_PROFILE_NAME,
    "compliance-preview": {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "isOnlineUpdate": False,
        "automaticUpdates":
            [
                COMPLIANCE_DISABLE_SECURE_BOOT_REGEX,
            ],
        "manualUpdates": []
    }
}

pts1_spt1_profile_patch_expected = {
    "type": SERVER_PROFILE_TYPE, "name": PTS1_SPT1_PROFILE_NAME,
    "serverHardwareUri": 'SH:' + PTS1_SPT1_PROFILE_SERVER,
    "serverProfileTemplateUri": "SPT:" + PTS1_SPT1_NAME,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual",
    "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": True, "mode": "UEFIOptimized", "secureBoot": "Disabled", "pxeBootPolicy": "Auto"},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,

}

pts1_spt2_profile_create = {
    "type": SERVER_PROFILE_TYPE, "name": PTS1_SPT2_PROFILE_NAME,
    "serverHardwareUri": 'SH:' + PTS1_SPT2_PROFILE_SERVER,
    "serverProfileTemplateUri": "SPT:" + PTS1_SPT2_NAME,
}

pts1_spt2_profile_create_expected = {
    "type": SERVER_PROFILE_TYPE, "name": PTS1_SPT2_PROFILE_NAME,
    "serverHardwareUri": 'SH:' + PTS1_SPT2_PROFILE_SERVER,
    "serverProfileTemplateUri": "SPT:" + PTS1_SPT2_NAME,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual",
    "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": True, "mode": "UEFIOptimized", "secureBoot": "Disabled", "pxeBootPolicy": "Auto"},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
}

pts1_spt2_profile_compliant_compliance = {
    "name": PTS1_SPT2_PROFILE_NAME,
    "compliance-preview": {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "isOnlineUpdate": None,
        "automaticUpdates": [],
        "manualUpdates": []
    }
}

pts1_spt2_profile_edit_compliance = {
    "name": PTS1_SPT2_PROFILE_NAME,
    "compliance-preview": {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "isOnlineUpdate": False,
        "automaticUpdates":
            [
                COMPLIANCE_ENABLE_SECURE_BOOT_REGEX,
            ],
        "manualUpdates": []
    }
}

pts1_spt2_profile_patch_expected = {
    "type": SERVER_PROFILE_TYPE, "name": PTS1_SPT2_PROFILE_NAME,
    "serverHardwareUri": 'SH:' + PTS1_SPT2_PROFILE_SERVER,
    "serverProfileTemplateUri": "SPT:" + PTS1_SPT2_NAME,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual",
    "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": True, "mode": "UEFIOptimized", "secureBoot": "Enabled", "pxeBootPolicy": "Auto"},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
}

pts2_profile_create = {
    "type": SERVER_PROFILE_TYPE, "name": PTS2_PROFILE_NAME,
    "serverHardwareUri": 'SH:' + PTS2_PROFILE_SERVER, "enclosureGroupUri": 'EG:' + PTS2_PROFILE_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual",
    "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "bootMode": {"manageMode": True, "mode": "UEFIOptimized", "pxeBootPolicy": "Auto", "secureBoot": "Enabled"},
    "boot": {"manageBoot": False, "order": [], },
    "firmware": {"manageFirmware": False, },
    "bios": {"overriddenSettings": [], "manageBios": False},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {"volumeAttachments": [], "sanSystemCredentials": [], "manageSanStorage": False},
    "hideUnusedFlexNics": True,
}

pts2_spt_from_sp_expected = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE, "name": PTS2_SPT_FROM_SP_NAME,
    "serverHardwareTypeUri": 'SHT:' + PTS2_SPT_FROM_SP_SHT, "enclosureGroupUri": 'EG:' + PTS2_SPT_FROM_SP_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual",
    "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": [], "manageConnections": True},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": True, "mode": "UEFIOptimized", "secureBoot": "Enabled", "pxeBootPolicy": "Auto"},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
}

pts2_sp_from_spt = {
    "type": SERVER_PROFILE_TYPE, "name": PTS2_SP_FROM_SPT_NAME,
    "serverHardwareUri": 'SH:' + PTS2_SP_FROM_SPT_SERVER,
    "serverProfileTemplateUri": "SPT:" + PTS2_SPT_FROM_SP_NAME,
}

pts2_sp_from_spt_expected = {
    "type": SERVER_PROFILE_TYPE, "name": PTS2_SP_FROM_SPT_NAME,
    "serverHardwareUri": 'SH:' + PTS2_SP_FROM_SPT_SERVER,
    "serverProfileTemplateUri": "SPT:" + PTS2_SPT_FROM_SP_NAME,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual",
    "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "bootMode": {"manageMode": True, "mode": "UEFIOptimized", "pxeBootPolicy": "Auto", "secureBoot": "Enabled"},
    "boot": {"manageBoot": False, "order": [], },
    "firmware": {"manageFirmware": False, },
    "bios": {"overriddenSettings": [], "manageBios": False},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {"volumeAttachments": [], "sanSystemCredentials": [], "manageSanStorage": False},
    "hideUnusedFlexNics": True,
}

pts3_profile_create = {
    "type": SERVER_PROFILE_TYPE, "name": PTS3_PROFILE_NAME,
    "serverHardwareUri": 'SH:' + PTS3_PROFILE_SERVER, "enclosureGroupUri": 'EG:' + PTS3_PROFILE_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual",
    "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "bootMode": {"manageMode": True, "mode": "UEFIOptimized", "pxeBootPolicy": "Auto", "secureBoot": "Enabled"},
    "boot": {"order": [], "manageBoot": False},
    "firmware": {"manageFirmware": False, },
    "bios": {"overriddenSettings": [], "manageBios": False},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {"volumeAttachments": [], "sanSystemCredentials": [], "manageSanStorage": False},
    "hideUnusedFlexNics": True,
}

pts3_profile_move = {
    "type": SERVER_PROFILE_TYPE, "name": PTS3_PROFILE_NAME,
    "serverHardwareUri": 'SH:' + PTS3_PROFILE_MOVE_SERVER, "enclosureGroupUri": 'EG:' + PTS3_PROFILE_MOVE_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual",
    "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "bootMode": {"manageMode": True, "mode": "UEFIOptimized", "pxeBootPolicy": "Auto", "secureBoot": "Enabled"},
    "boot": {"order": [], "manageBoot": False},
    "firmware": {"manageFirmware": False, },
    "bios": {"overriddenSettings": [], "manageBios": False},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {"volumeAttachments": [], "sanSystemCredentials": [], "manageSanStorage": False},
    "hideUnusedFlexNics": True,
}

pts3_profile_edit = {
    "type": SERVER_PROFILE_TYPE, "name": PTS3_PROFILE_NAME,
    "serverHardwareUri": 'SH:' + PTS3_PROFILE_EDIT_SERVER, "enclosureGroupUri": 'EG:' + PTS3_PROFILE_EDIT_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual",
    "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "bootMode": {"manageMode": True, "mode": "UEFIOptimized", "pxeBootPolicy": "Auto", "secureBoot": "Disabled"},
    "boot": {"order": [], "manageBoot": False},
    "firmware": {"manageFirmware": False, },
    "bios": {"overriddenSettings": [], "manageBios": False},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {"volumeAttachments": [], "sanSystemCredentials": [], "manageSanStorage": False},
    "hideUnusedFlexNics": True,
}

pts3_profile_move_back = {
    "type": SERVER_PROFILE_TYPE, "name": PTS3_PROFILE_NAME,
    "serverHardwareUri": 'SH:' + PTS3_PROFILE_MOVE_BACK_SERVER, "enclosureGroupUri": 'EG:' + PTS3_PROFILE_MOVE_BACK_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual",
    "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "bootMode": {"manageMode": True, "mode": "UEFIOptimized", "pxeBootPolicy": "Auto", "secureBoot": "Disabled"},
    "boot": {"order": [], "manageBoot": False},
    "firmware": {"manageFirmware": False, },
    "bios": {"overriddenSettings": [], "manageBios": False},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {"volumeAttachments": [], "sanSystemCredentials": [], "manageSanStorage": False},
    "hideUnusedFlexNics": True,
}

pts4_spt1_create = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE, "name": PTS4_SPT1_NAME,
    "serverHardwareTypeUri": 'SHT:' + PTS4_SPT1_SHT, "enclosureGroupUri": 'EG:' + PTS4_SPT1_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual",
    "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": [], "manageConnections": False},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": True, "mode": "UEFIOptimized", "secureBoot": "Enabled", "pxeBootPolicy": "Auto"},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
}

pts4_spt2_create = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE, "name": PTS4_SPT2_NAME,
    "serverHardwareTypeUri": 'SHT:' + PTS4_SPT2_SHT, "enclosureGroupUri": 'EG:' + PTS4_SPT2_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual",
    "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": [], "manageConnections": False},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": True, "mode": "UEFIOptimized", "secureBoot": "Disabled", "pxeBootPolicy": "Auto"},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
}

pts4_profile1_create = {
    "type": SERVER_PROFILE_TYPE, "name": PTS4_PROFILE1_NAME,
    "serverHardwareUri": 'SH:' + PTS4_PROFILE1_SERVER, "enclosureGroupUri": 'EG:' + PTS4_PROFILE1_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual",
    "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "bootMode": {"manageMode": True, "mode": "UEFIOptimized", "pxeBootPolicy": "Auto", "secureBoot": "Disabled"},
    "boot": {"order": [], "manageBoot": False},
    "firmware": {"manageFirmware": False, },
    "bios": {"overriddenSettings": [], "manageBios": False},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {"volumeAttachments": [], "sanSystemCredentials": [], "manageSanStorage": False},
    "hideUnusedFlexNics": True,
}

pts4_profile1_edit = {
    "type": SERVER_PROFILE_TYPE, "name": PTS4_PROFILE1_NAME,
    "serverHardwareUri": 'SH:' + PTS4_PROFILE1_SERVER, "enclosureGroupUri": 'EG:' + PTS4_PROFILE1_EG,
    "serverProfileTemplateUri": "SPT:" + PTS4_SPT1_NAME,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual",
    "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "bootMode": {"manageMode": True, "mode": "UEFIOptimized", "pxeBootPolicy": "Auto", "secureBoot": "Disabled"},
    "boot": {"order": [], "manageBoot": False},
    "firmware": {"manageFirmware": False, },
    "bios": {"overriddenSettings": [], "manageBios": False},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {"volumeAttachments": [], "sanSystemCredentials": [], "manageSanStorage": False},
    "hideUnusedFlexNics": True,
}

pts4_profile1_compliant_compliance = {
    "name": PTS4_PROFILE1_NAME,
    "compliance-preview": {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "isOnlineUpdate": None,
        "automaticUpdates": [],
        "manualUpdates": []
    }
}

pts4_profile1_edit_compliance = {
    "name": PTS4_PROFILE1_NAME,
    "compliance-preview": {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "isOnlineUpdate": False,
        "automaticUpdates":
            [
                COMPLIANCE_ENABLE_SECURE_BOOT_REGEX,
            ],
        "manualUpdates": []
    }
}

pts4_profile1_patch_expected = {
    "type": SERVER_PROFILE_TYPE, "name": PTS4_PROFILE1_NAME,
    "serverHardwareUri": 'SH:' + PTS4_PROFILE1_SERVER, "enclosureGroupUri": 'EG:' + PTS4_PROFILE1_EG,
    "serverProfileTemplateUri": "SPT:" + PTS4_SPT1_NAME,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual",
    "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "bootMode": {"manageMode": True, "mode": "UEFIOptimized", "pxeBootPolicy": "Auto", "secureBoot": "Enabled"},
    "boot": {"order": [], "manageBoot": False},
    "firmware": {"manageFirmware": False, },
    "bios": {"overriddenSettings": [], "manageBios": False},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {"volumeAttachments": [], "sanSystemCredentials": [], "manageSanStorage": False},
    "hideUnusedFlexNics": True,
}

pts4_profile2_create = {
    "type": SERVER_PROFILE_TYPE, "name": PTS4_PROFILE2_NAME,
    "serverHardwareUri": 'SH:' + PTS4_PROFILE2_SERVER, "enclosureGroupUri": 'EG:' + PTS4_PROFILE2_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual",
    "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "bootMode": {"manageMode": True, "mode": "UEFIOptimized", "pxeBootPolicy": "Auto", "secureBoot": "Enabled"},
    "boot": {"order": [], "manageBoot": False},
    "firmware": {"manageFirmware": False, },
    "bios": {"overriddenSettings": [], "manageBios": False},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {"volumeAttachments": [], "sanSystemCredentials": [], "manageSanStorage": False},
    "hideUnusedFlexNics": True,
}

pts4_profile2_edit = {
    "type": SERVER_PROFILE_TYPE, "name": PTS4_PROFILE2_NAME,
    "serverHardwareUri": 'SH:' + PTS4_PROFILE2_SERVER, "enclosureGroupUri": 'EG:' + PTS4_PROFILE2_EG,
    "serverProfileTemplateUri": "SPT:" + PTS4_SPT2_NAME,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual",
    "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "bootMode": {"manageMode": True, "mode": "UEFIOptimized", "pxeBootPolicy": "Auto", "secureBoot": "Enabled"},
    "boot": {"order": [], "manageBoot": False},
    "firmware": {"manageFirmware": False, },
    "bios": {"overriddenSettings": [], "manageBios": False},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {"volumeAttachments": [], "sanSystemCredentials": [], "manageSanStorage": False},
    "hideUnusedFlexNics": True,
}

pts4_profile2_compliant_compliance = {
    "name": PTS4_PROFILE2_NAME,
    "compliance-preview": {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "isOnlineUpdate": None,
        "automaticUpdates": [],
        "manualUpdates": []
    }
}

pts4_profile2_edit_compliance = {
    "name": PTS4_PROFILE2_NAME,
    "compliance-preview": {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "isOnlineUpdate": False,
        "automaticUpdates":
            [
                COMPLIANCE_DISABLE_SECURE_BOOT_REGEX,
            ],
        "manualUpdates": []
    }
}

pts4_profile2_patch_expected = {
    "type": SERVER_PROFILE_TYPE, "name": PTS4_PROFILE2_NAME,
    "serverHardwareUri": 'SH:' + PTS4_PROFILE2_SERVER, "enclosureGroupUri": 'EG:' + PTS4_PROFILE2_EG,
    "serverProfileTemplateUri": "SPT:" + PTS4_SPT2_NAME,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual",
    "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "bootMode": {"manageMode": True, "mode": "UEFIOptimized", "pxeBootPolicy": "Auto", "secureBoot": "Disabled"},
    "boot": {"order": [], "manageBoot": False},
    "firmware": {"manageFirmware": False, },
    "bios": {"overriddenSettings": [], "manageBios": False},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {"volumeAttachments": [], "sanSystemCredentials": [], "manageSanStorage": False},
    "hideUnusedFlexNics": True,
}

# Suite Setup and Teardown profiles
profile1_create = {
    "type": SERVER_PROFILE_TYPE, "name": PROFILE1_NAME,
    "serverHardwareUri": 'SH:' + PROFILE1_SERVER, "enclosureGroupUri": 'EG:' + PROFILE1_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual",
    "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "bootMode": {"manageMode": True, "mode": "UEFIOptimized", "pxeBootPolicy": "Auto", "secureBoot": "Disabled"},
    "boot": {"order": [], "manageBoot": False},
    "firmware": {"manageFirmware": False, },
    "bios": {"overriddenSettings": [], "manageBios": False},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {"volumeAttachments": [], "sanSystemCredentials": [], "manageSanStorage": False},
    "hideUnusedFlexNics": True,
}

profile2_create = {
    "type": SERVER_PROFILE_TYPE, "name": PROFILE2_NAME,
    "serverHardwareUri": 'SH:' + PROFILE2_SERVER, "enclosureGroupUri": 'EG:' + PROFILE2_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual",
    "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "bootMode": {"manageMode": True, "mode": "UEFIOptimized", "pxeBootPolicy": "Auto", "secureBoot": "Disabled"},
    "boot": {"order": [], "manageBoot": False},
    "firmware": {"manageFirmware": False, },
    "bios": {"overriddenSettings": [], "manageBios": False},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {"volumeAttachments": [], "sanSystemCredentials": [], "manageSanStorage": False},
    "hideUnusedFlexNics": True,
}

profile3_create = {
    "type": SERVER_PROFILE_TYPE, "name": PROFILE3_NAME,
    "serverHardwareUri": 'SH:' + PROFILE3_SERVER, "enclosureGroupUri": 'EG:' + PROFILE3_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual",
    "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "bootMode": {"manageMode": True, "mode": "UEFIOptimized", "pxeBootPolicy": "Auto", "secureBoot": "Disabled"},
    "boot": {"order": [], "manageBoot": False},
    "firmware": {"manageFirmware": False, },
    "bios": {"overriddenSettings": [], "manageBios": False},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {"volumeAttachments": [], "sanSystemCredentials": [], "manageSanStorage": False},
    "hideUnusedFlexNics": True,
}

# RIS nodes
ris_node_sht_gen10_sy480_server1_secure_boot_enabled = {
    "server": SHT_GEN10_SY480_SERVER1,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/SecureBoot",
    "validate": {
        "Id": "SecureBoot",
        "Name": "SecureBoot",
        "SecureBootCurrentBoot": RIS_SECURE_BOOT_CURRENT_BOOT_REGEX,
        "SecureBootEnable": True,
        "SecureBootMode": "UserMode"
    }
}

ris_node_sht_gen10_sy480_server1_secure_boot_enabled_power_on = {
    "server": SHT_GEN10_SY480_SERVER1,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/SecureBoot",
    "validate": {
        "Id": "SecureBoot",
        "Name": "SecureBoot",
        "SecureBootCurrentBoot": "Enabled",
        "SecureBootEnable": True,
        "SecureBootMode": "UserMode"
    }
}

ris_node_sht_gen10_sy480_server1_secure_boot_disabled = {
    "server": SHT_GEN10_SY480_SERVER1,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/SecureBoot",
    "validate": {
        "Id": "SecureBoot",
        "Name": "SecureBoot",
        "SecureBootCurrentBoot": RIS_SECURE_BOOT_CURRENT_BOOT_REGEX,
        "SecureBootEnable": False,
        "SecureBootMode": "UserMode"
    }
}

ris_node_sht_gen10_sy480_server1_secure_boot_disabled_power_on = {
    "server": SHT_GEN10_SY480_SERVER1,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/SecureBoot",
    "validate": {
        "Id": "SecureBoot",
        "Name": "SecureBoot",
        "SecureBootCurrentBoot": "Disabled",
        "SecureBootEnable": False,
        "SecureBootMode": "UserMode"
    }
}

ris_node_sht_gen10_sy480_server2_secure_boot_enabled = {
    "server": SHT_GEN10_SY480_SERVER2,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/SecureBoot",
    "validate": {
        "Id": "SecureBoot",
        "Name": "SecureBoot",
        "SecureBootCurrentBoot": RIS_SECURE_BOOT_CURRENT_BOOT_REGEX,
        "SecureBootEnable": True,
        "SecureBootMode": "UserMode"
    }
}

ris_node_sht_gen10_sy480_server2_secure_boot_enabled_power_on = {
    "server": SHT_GEN10_SY480_SERVER2,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/SecureBoot",
    "validate": {
        "Id": "SecureBoot",
        "Name": "SecureBoot",
        "SecureBootCurrentBoot": "Enabled",
        "SecureBootEnable": True,
        "SecureBootMode": "UserMode"
    }
}

ris_node_sht_gen10_sy480_server2_secure_boot_disabled = {
    "server": SHT_GEN10_SY480_SERVER2,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/SecureBoot",
    "validate": {
        "Id": "SecureBoot",
        "Name": "SecureBoot",
        "SecureBootCurrentBoot": RIS_SECURE_BOOT_CURRENT_BOOT_REGEX,
        "SecureBootEnable": False,
        "SecureBootMode": "UserMode"
    }
}

ris_node_sht_gen10_sy480_server2_secure_boot_disabled_power_on = {
    "server": SHT_GEN10_SY480_SERVER2,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/SecureBoot",
    "validate": {
        "Id": "SecureBoot",
        "Name": "SecureBoot",
        "SecureBootCurrentBoot": RIS_SECURE_BOOT_CURRENT_BOOT_REGEX,
        "SecureBootEnable": False,
        "SecureBootMode": "UserMode"
    }
}

ris_node_sht_gen10_sy660_server1_secure_boot_enabled = {
    "server": SHT_GEN10_SY660_SERVER1,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/SecureBoot",
    "validate": {
        "Id": "SecureBoot",
        "Name": "SecureBoot",
        "SecureBootCurrentBoot": RIS_SECURE_BOOT_CURRENT_BOOT_REGEX,
        "SecureBootEnable": True,
        "SecureBootMode": "UserMode"
    }
}

ris_node_sht_gen10_sy660_server1_secure_boot_enabled_power_on = {
    "server": SHT_GEN10_SY660_SERVER1,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/SecureBoot",
    "validate": {
        "Id": "SecureBoot",
        "Name": "SecureBoot",
        "SecureBootCurrentBoot": "Enabled",
        "SecureBootEnable": True,
        "SecureBootMode": "UserMode"
    }
}

ris_node_sht_gen10_sy660_server1_secure_boot_disabled = {
    "server": SHT_GEN10_SY660_SERVER1,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/SecureBoot",
    "validate": {
        "Id": "SecureBoot",
        "Name": "SecureBoot",
        "SecureBootCurrentBoot": RIS_SECURE_BOOT_CURRENT_BOOT_REGEX,
        "SecureBootEnable": False,
        "SecureBootMode": "UserMode"
    }
}

ris_node_sht_gen10_sy660_server1_secure_boot_disabled_power_on = {
    "server": SHT_GEN10_SY660_SERVER1,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/SecureBoot",
    "validate": {
        "Id": "SecureBoot",
        "Name": "SecureBoot",
        "SecureBootCurrentBoot": "Disabled",
        "SecureBootEnable": False,
        "SecureBootMode": "UserMode"
    }
}

pts1_spts_create = [pts1_spt1_create.copy(), pts1_spt2_create.copy()]

pts1_profiles_create = [pts1_spt1_profile_create.copy(), pts1_spt2_profile_create.copy()]

pts1_profiles_create_expected = [pts1_spt1_profile_create_expected, pts1_spt2_profile_create_expected]

pts1_spts_edit = [pts1_spt1_edit.copy(), pts1_spt2_edit.copy()]

pts1_profiles_compliant_compliance = [pts1_spt1_profile_compliant_compliance, pts1_spt2_profile_compliant_compliance]

pts1_profiles_edit_compliance = [pts1_spt1_profile_edit_compliance, pts1_spt2_profile_edit_compliance]

pts1_profiles_patch_expected = [pts1_spt1_profile_patch_expected, pts1_spt2_profile_patch_expected]

pts1_ris_nodes_after_create = [ris_node_sht_gen10_sy480_server1_secure_boot_enabled,
                               ris_node_sht_gen10_sy660_server1_secure_boot_disabled]

pts1_ris_nodes_after_power_on_after_create = [ris_node_sht_gen10_sy480_server1_secure_boot_enabled_power_on,
                                              ris_node_sht_gen10_sy660_server1_secure_boot_disabled_power_on]

pts1_ris_nodes_after_patch = [ris_node_sht_gen10_sy480_server1_secure_boot_disabled,
                              ris_node_sht_gen10_sy660_server1_secure_boot_enabled]

pts1_ris_nodes_after_power_on_after_patch = [ris_node_sht_gen10_sy480_server1_secure_boot_disabled_power_on,
                                             ris_node_sht_gen10_sy660_server1_secure_boot_enabled_power_on]

pts2_profiles_create = [pts2_profile_create.copy()]

pts2_profiles_sp_from_spt = [pts2_sp_from_spt.copy()]

pts2_profiles_delete = [pts2_profile_create.copy(), pts2_sp_from_spt.copy()]

pts3_profiles_create = [pts3_profile_create.copy()]

pts3_profiles_move = [pts3_profile_move.copy()]

pts3_profiles_edit = [pts3_profile_edit.copy()]

pts3_profiles_delete = [pts3_profile_move_back.copy()]

pts4_spts_create = [pts4_spt1_create.copy(), pts4_spt2_create.copy()]

pts4_profiles_create = [pts4_profile1_create.copy(), pts4_profile2_create.copy()]

pts4_profiles_edit = [pts4_profile1_edit.copy(), pts4_profile2_edit.copy()]

pts4_profiles_compliant_compliance = [pts4_profile1_compliant_compliance, pts4_profile2_compliant_compliance]

pts4_profiles_edit_compliance = [pts4_profile1_edit_compliance, pts4_profile2_edit_compliance]

pts4_profiles_patch_expected = [pts4_profile1_patch_expected, pts4_profile2_patch_expected]

pts4_ris_nodes_after_create = [ris_node_sht_gen10_sy480_server1_secure_boot_disabled,
                               ris_node_sht_gen10_sy660_server1_secure_boot_enabled]

pts4_ris_nodes_after_power_on_after_create = [ris_node_sht_gen10_sy480_server1_secure_boot_disabled_power_on,
                                              ris_node_sht_gen10_sy660_server1_secure_boot_enabled_power_on]

pts4_ris_nodes_after_edit = pts4_ris_nodes_after_create

pts4_ris_nodes_after_power_on_after_edit = pts4_ris_nodes_after_power_on_after_create

pts4_ris_nodes_after_patch = [ris_node_sht_gen10_sy480_server1_secure_boot_enabled,
                              ris_node_sht_gen10_sy660_server1_secure_boot_disabled]

pts4_ris_nodes_after_power_on_after_patch = [ris_node_sht_gen10_sy480_server1_secure_boot_enabled_power_on,
                                             ris_node_sht_gen10_sy660_server1_secure_boot_disabled_power_on]

suite_setup_profiles = [profile1_create.copy(), profile2_create.copy(), profile3_create.copy()]

suite_teardown_profiles = suite_setup_profiles

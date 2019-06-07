# Credentials
admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
ilo_credentials = {'username': 'Administrator', 'password': 'hpvse123'}
cliq_credentials = {
    'mgmt_ip': '16.71.149.173',
    'username': 'admin',
    'password': 'admin'}
ssh_credentials = {'username': 'root', 'password': 'hpvse1'}

# Resource types for X-API-Version=800
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
ENC2SHBAY6 = '%s, bay 6' % ENC2    # SY660 Gen10
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
NAME_PREFIX = 'Synergy-Ring1-OVF899-'
SPT_NAME_PREFIX = NAME_PREFIX
PROFILE_NAME_PREFIX = NAME_PREFIX
# SH
SERVER1 = ENC1SHBAY8
SERVER2 = ENC2SHBAY8
SERVER3 = ENC2SHBAY6  # missing two SAS HDD drives in drive bay 1 and 2
#
SHT_SERVER1 = 'SH:' + SERVER1
SHT_SERVER2 = 'SH:' + SERVER2
SHT_SERVER3 = 'SH:' + SERVER3
# NTS1
NTS1_PROFILE1_NAME = PROFILE_NAME_PREFIX + 'NTS1-PROFILE1'
NTS1_PROFILE1_SERVER = SERVER1
NTS1_PROFILE1_EG = EG_NAME
NTS1_PROFILE2_NAME = PROFILE_NAME_PREFIX + 'NTS1-PROFILE2'
NTS1_PROFILE2_SERVER = SERVER3
NTS1_PROFILE2_EG = EG_NAME
# PTS1 SPT and Profile
PTS1_SPT1_NAME = PROFILE_NAME_PREFIX + 'pts1-spt1'
PTS1_SPT1_SHT = SHT_SERVER1
PTS1_SPT1_EG = EG_NAME
PTS1_PROFILE1_NAME = PROFILE_NAME_PREFIX + 'pts1-profile1'
PTS1_PROFILE1_SERVER = SERVER1
PTS1_PROFILE1_EG = EG_NAME
PTS1_SPT2_NAME = PROFILE_NAME_PREFIX + 'pts1-spt2'
PTS1_SPT2_SHT = SHT_SERVER2
PTS1_SPT2_EG = EG_NAME
PTS1_PROFILE2_NAME = PROFILE_NAME_PREFIX + 'pts1-profile2'
PTS1_PROFILE2_SERVER = SERVER2
PTS1_PROFILE2_EG = EG_NAME
PTS1_SPT3_NAME = PROFILE_NAME_PREFIX + 'pts1-spt3'
PTS1_SPT3_SHT = SHT_SERVER3
PTS1_SPT3_EG = EG_NAME
PTS1_PROFILE3_NAME = PROFILE_NAME_PREFIX + 'pts1-profile3'
PTS1_PROFILE3_SERVER = SERVER3
PTS1_PROFILE3_EG = EG_NAME
# PTS2 SPT and Profile
PTS2_SPT1_NAME = PROFILE_NAME_PREFIX + 'pts2-spt1'
PTS2_SPT1_SHT = SHT_SERVER1
PTS2_SPT1_EG = EG_NAME
PTS2_PROFILE1_NAME = PROFILE_NAME_PREFIX + 'pts2-profile1'
PTS2_PROFILE1_SERVER = SERVER1
PTS2_PROFILE1_EG = EG_NAME
PTS2_UNASSIGN_PROFILE1_NAME = PROFILE_NAME_PREFIX + 'pts2-unassign-profile1'
PTS2_UNASSIGN_PROFILE1_SHT = SHT_SERVER1
PTS2_UNASSIGN_PROFILE1_EG = EG_NAME
PTS2_SPT2_NAME = PROFILE_NAME_PREFIX + 'pts2-spt2'
PTS2_SPT2_SHT = SHT_SERVER2
PTS2_SPT2_EG = EG_NAME
PTS2_PROFILE2_NAME = PROFILE_NAME_PREFIX + 'pts2-profile2'
PTS2_PROFILE2_SERVER = SERVER2
PTS2_PROFILE2_EG = EG_NAME
PTS2_UNASSIGN_PROFILE2_NAME = PROFILE_NAME_PREFIX + 'pts2-unassign-profile2'
PTS2_UNASSIGN_PROFILE2_SHT = SHT_SERVER2
PTS2_UNASSIGN_PROFILE2_EG = EG_NAME
PTS2_SPT3_NAME = PROFILE_NAME_PREFIX + 'pts2-spt3'
PTS2_SPT3_SHT = SHT_SERVER3
PTS2_SPT3_EG = EG_NAME
PTS2_PROFILE3_NAME = PROFILE_NAME_PREFIX + 'pts2-profile3'
PTS2_PROFILE3_SERVER = SERVER3
PTS2_PROFILE3_EG = EG_NAME
PTS2_UNASSIGN_PROFILE3_NAME = PROFILE_NAME_PREFIX + 'pts2-unassign-profile3'
PTS2_UNASSIGN_PROFILE3_SHT = SHT_SERVER3
PTS2_UNASSIGN_PROFILE3_EG = EG_NAME
# PTS3 Profile
PTS3_PROFILE1_NAME = PROFILE_NAME_PREFIX + 'pts3-profile1'
PTS3_PROFILE1_SERVER = SERVER1
PTS3_PROFILE1_EG = EG_NAME
PTS3_PROFILE2_NAME = PROFILE_NAME_PREFIX + 'pts3-profile2'
PTS3_PROFILE2_SERVER = SERVER2
PTS3_PROFILE2_EG = EG_NAME
PTS3_PROFILE3_NAME = PROFILE_NAME_PREFIX + 'pts3-profile3'
PTS3_PROFILE3_SERVER = SERVER3
PTS3_PROFILE3_EG = EG_NAME
# PTS4 Profile
PTS4_PROFILE1_NAME = PROFILE_NAME_PREFIX + 'pts4-profile1'
PTS4_PROFILE1_SERVER = SERVER1
PTS4_PROFILE1_EG = EG_NAME
PTS4_PROFILE2_NAME = PROFILE_NAME_PREFIX + 'pts4-profile2'
PTS4_PROFILE2_SERVER = SERVER2
PTS4_PROFILE2_EG = EG_NAME
PTS4_PROFILE3_NAME = PROFILE_NAME_PREFIX + 'pts4-profile3'
PTS4_PROFILE3_SERVER = SERVER3
PTS4_PROFILE3_EG = EG_NAME
# PTS5 Profile
PTS5_PROFILE1_NAME = PROFILE_NAME_PREFIX + 'pts5-profile1'
PTS5_PROFILE1_SERVER = SERVER1
PTS5_PROFILE1_EG = EG_NAME
PTS5_PROFILE2_NAME = PROFILE_NAME_PREFIX + 'pts5-profile2'
PTS5_PROFILE2_SERVER = SERVER2
PTS5_PROFILE2_EG = EG_NAME
PTS5_PROFILE3_NAME = PROFILE_NAME_PREFIX + 'pts5-profile3'
PTS5_PROFILE3_SERVER = SERVER3
PTS5_PROFILE3_EG = EG_NAME
# PTS6 Profile
PTS6_PROFILE_NAME = PROFILE_NAME_PREFIX + 'pts6-profile'
PTS6_PROFILE_SERVER = SERVER1
PTS6_PROFILE_EG = EG_NAME
PTS6_PROFILE_MOVE_SERVER = SERVER3
PTS6_PROFILE_MOVE_EG = EG_NAME
# PTS7 Profile
PTS7_PROFILE_NAME = PROFILE_NAME_PREFIX + 'pts7-profile'
PTS7_PROFILE_SERVER = SERVER2
PTS7_PROFILE_EG = EG_NAME
# PTS8 SPT and Profile
PTS8_SPT1_NAME = PROFILE_NAME_PREFIX + 'pts8-spt1'
PTS8_SPT1_SHT = SHT_SERVER1
PTS8_SPT1_EG = EG_NAME
PTS8_PROFILE1_NAME = PROFILE_NAME_PREFIX + 'pts8-profile1'
PTS8_PROFILE1_SERVER = SERVER1
PTS8_PROFILE1_EG = EG_NAME
PTS8_SPT2_NAME = PROFILE_NAME_PREFIX + 'pts8-spt2'
PTS8_SPT2_SHT = SHT_SERVER2
PTS8_SPT2_EG = EG_NAME
PTS8_PROFILE2_NAME = PROFILE_NAME_PREFIX + 'pts8-profile2'
PTS8_PROFILE2_SERVER = SERVER2
PTS8_PROFILE2_EG = EG_NAME
PTS8_SPT3_NAME = PROFILE_NAME_PREFIX + 'pts8-spt3'
PTS8_SPT3_SHT = SHT_SERVER3
PTS8_SPT3_EG = EG_NAME
PTS8_PROFILE3_NAME = PROFILE_NAME_PREFIX + 'pts8-profile3'
PTS8_PROFILE3_SERVER = SERVER3
PTS8_PROFILE3_EG = EG_NAME
# Suite Setup and Teardown
PROFILE1_NAME = PROFILE_NAME_PREFIX + 'suite-setup-profile1'
PROFILE1_SERVER = SERVER1
PROFILE1_EG = EG_NAME
PROFILE2_NAME = PROFILE_NAME_PREFIX + 'suite-setup-profile2'
PROFILE2_SERVER = SERVER2
PROFILE2_EG = EG_NAME
PROFILE3_NAME = PROFILE_NAME_PREFIX + 'suite-setup-profile3'
PROFILE3_SERVER = SERVER3
PROFILE3_EG = EG_NAME
# Profile complinace
COMPLIANCE_LS_REGEX = 'Modify local storage settings to match with the server profile template.'
# REGEX
RIS_SECURE_BOOT_CURRENT_BOOT_REGEX = 'REGEX:\w*'

# NTS1 profile1 CWC set and LDA set to IOBypass, but server has SASHDD
nts1_profile1_create = {
    "type": SERVER_PROFILE_TYPE, "name": NTS1_PROFILE1_NAME,
    "serverHardwareUri": 'SH:' + NTS1_PROFILE1_SERVER, "enclosureGroupUri": 'EG:' + NTS1_PROFILE1_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "pxeBootPolicy": None, "secureBoot": "Unmanaged"},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": False,
                "importConfiguration": False,
                "driveWriteCache": "Disabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID1",
                        "bootable": False,
                        "numPhysicalDrives": 2,
                        "driveTechnology": "Unknown",
                        "sasLogicalJBODId": None,
                        "accelerator": "IOBypass",
                    }
                ]
            }
        ]
    },
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
}

# NTS1 profile2 CWC set, LDA1 set to IOBypass and LDA1 set to
# ControllerCache, but server has SASHDD in bays 1&2 and SATASSD in bays
# 3&4
nts1_profile2_create = {
    "type": SERVER_PROFILE_TYPE, "name": NTS1_PROFILE2_NAME,
    "serverHardwareUri": 'SH:' + NTS1_PROFILE2_SERVER, "enclosureGroupUri": 'EG:' + NTS1_PROFILE2_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "pxeBootPolicy": None, "secureBoot": "Unmanaged"},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": False,
                "importConfiguration": False,
                "driveWriteCache": "Enabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID1",
                        "bootable": False,
                        "numPhysicalDrives": 2,
                        "driveTechnology": "Unknown",
                        "sasLogicalJBODId": None,
                        "accelerator": "IOBypass",
                    },
                ]
            }
        ]
    },
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
}

nts1_profiles = [nts1_profile1_create.copy(), nts1_profile2_create.copy(), ]

nts1_negative_profile_tasks = [
    {
        'keyword': 'Add Server Profile',
        'argument': nts1_profile1_create.copy(),
        'taskState': 'Error',
        'errorMessage': 'LDA_IOBYPASS_UNSUPPORTED'},
    {
        'keyword': 'Add Server Profile',
        'argument': nts1_profile2_create.copy(),
        'taskState': 'Error',
        'errorMessage': 'LDA_IOBYPASS_UNSUPPORTED'},
]

pts1_spt1_create = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE, "name": PTS1_SPT1_NAME,
    "serverHardwareTypeUri": 'SHT:' + PTS1_SPT1_SHT, "enclosureGroupUri": 'EG:' + PTS1_SPT1_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": [], "manageConnections": False},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": True,
                "driveWriteCache": "Disabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID1",
                        "bootable": False,
                        "numPhysicalDrives": 2,
                        "driveTechnology": "SasHdd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                    }
                ]
            }
        ]
    },
}

pts1_spt1_edit = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE, "name": PTS1_SPT1_NAME,
    "serverHardwareTypeUri": 'SHT:' + PTS1_SPT1_SHT, "enclosureGroupUri": 'EG:' + PTS1_SPT1_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": [], "manageConnections": False},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": True,
                "driveWriteCache": "Enabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID1",
                        "bootable": False,
                        "numPhysicalDrives": 2,
                        "driveTechnology": "SasHdd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                    }
                ]
            }
        ]
    },
}

pts1_profile1_create = {
    "type": SERVER_PROFILE_TYPE, "name": PTS1_PROFILE1_NAME,
    "serverHardwareUri": 'SH:' + PTS1_PROFILE1_SERVER,
    "serverProfileTemplateUri": "SPT:" + PTS1_SPT1_NAME,
}

pts1_profile1_create_expected = {
    "type": SERVER_PROFILE_TYPE, "name": PTS1_PROFILE1_NAME,
    "serverHardwareUri": 'SH:' + PTS1_PROFILE1_SERVER,
    "serverProfileTemplateUri": "SPT:" + PTS1_SPT1_NAME,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": False,
                "importConfiguration": False,
                "driveWriteCache": "Disabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID1",
                        "bootable": False,
                        "numPhysicalDrives": 2,
                        "driveTechnology": "SasHdd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                        "driveNumber": 1,
                    }
                ]
            }
        ]
    },
}

pts1_profile1_compliance = {
    "name": PTS1_PROFILE1_NAME,
    "compliance-preview": {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "isOnlineUpdate": None,
        "automaticUpdates": [],
        "manualUpdates": [],
    }
}

pts1_profile1_non_compliance = {
    "name": PTS1_PROFILE1_NAME,
    "compliance-preview": {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "isOnlineUpdate": None,
        "automaticUpdates": [],
        "manualUpdates": [COMPLIANCE_LS_REGEX, ]
    }
}

pts1_profile1_edit = {
    "type": SERVER_PROFILE_TYPE, "name": PTS1_PROFILE1_NAME,
    "serverHardwareUri": 'SH:' + PTS1_PROFILE1_SERVER,
    "serverProfileTemplateUri": "SPT:" + PTS1_SPT1_NAME,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": False,
                "importConfiguration": False,
                "driveWriteCache": "Enabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID1",
                        "bootable": False,
                        "numPhysicalDrives": 2,
                        "driveTechnology": "SasHdd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                        "driveNumber": 1,
                    }
                ]
            }
        ]
    },
}

pts1_spt2_create = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE, "name": PTS1_SPT2_NAME,
    "serverHardwareTypeUri": 'SHT:' + PTS1_SPT2_SHT, "enclosureGroupUri": 'EG:' + PTS1_SPT2_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": [], "manageConnections": False},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": True,
                "driveWriteCache": "Disabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "IOBypass",
                    },
                    {
                        "name": "LD2",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "IOBypass",
                    }
                ]
            }
        ]
    },
}

pts1_spt2_edit = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE, "name": PTS1_SPT2_NAME,
    "serverHardwareTypeUri": 'SHT:' + PTS1_SPT2_SHT, "enclosureGroupUri": 'EG:' + PTS1_SPT2_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": [], "manageConnections": False},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": True,
                "driveWriteCache": "Enabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "IOBypass",
                    },
                    {
                        "name": "LD2",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                    }
                ]
            }
        ]
    }
}

pts1_profile2_create = {
    "type": SERVER_PROFILE_TYPE, "name": PTS1_PROFILE2_NAME,
    "serverHardwareUri": 'SH:' + PTS1_PROFILE2_SERVER,
    "serverProfileTemplateUri": "SPT:" + PTS1_SPT2_NAME,
}

pts1_profile2_create_expected = {
    "type": SERVER_PROFILE_TYPE, "name": PTS1_PROFILE2_NAME,
    "serverHardwareUri": 'SH:' + PTS1_PROFILE2_SERVER,
    "serverProfileTemplateUri": "SPT:" + PTS1_SPT2_NAME,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": False,
                "importConfiguration": False,
                "driveWriteCache": "Disabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "IOBypass",
                        "driveNumber": 1,
                    },
                    {
                        "name": "LD2",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "IOBypass",
                        "driveNumber": 2,
                    }
                ]
            }
        ]
    },
}

pts1_profile2_compliance = {
    "name": PTS1_PROFILE2_NAME,
    "compliance-preview": {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "isOnlineUpdate": None,
        "automaticUpdates": [],
        "manualUpdates": [],
    }
}

pts1_profile2_non_compliance = {
    "name": PTS1_PROFILE2_NAME,
    "compliance-preview": {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "isOnlineUpdate": None,
        "automaticUpdates": [],
        "manualUpdates": [COMPLIANCE_LS_REGEX, ]
    }
}

pts1_profile2_edit = {
    "type": SERVER_PROFILE_TYPE, "name": PTS1_PROFILE2_NAME,
    "serverHardwareUri": 'SH:' + PTS1_PROFILE2_SERVER,
    "serverProfileTemplateUri": "SPT:" + PTS1_SPT2_NAME,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": False,
                "importConfiguration": False,
                "driveWriteCache": "Enabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "IOBypass",
                        "driveNumber": 1,
                    },
                    {
                        "name": "LD2",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                        "driveNumber": 2,
                    }
                ]
            }
        ]
    },
}

pts1_spt3_create = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE, "name": PTS1_SPT3_NAME,
    "serverHardwareTypeUri": 'SHT:' + PTS1_SPT3_SHT, "enclosureGroupUri": 'EG:' + PTS1_SPT3_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": [], "manageConnections": False},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": True,
                "driveWriteCache": "Disabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SasHdd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                    },
                    {
                        "name": "LD2",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SasHdd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                    },
                    {
                        "name": "LD3",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "IOBypass",
                    },
                    {
                        "name": "LD4",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "IOBypass",
                    }
                ]
            }
        ]
    },
}

pts1_spt3_edit = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE, "name": PTS1_SPT3_NAME,
    "serverHardwareTypeUri": 'SHT:' + PTS1_SPT3_SHT, "enclosureGroupUri": 'EG:' + PTS1_SPT3_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": [], "manageConnections": False},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": True,
                "driveWriteCache": "Enabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SasHdd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                    },
                    {
                        "name": "LD2",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SasHdd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                    },
                    {
                        "name": "LD3",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "IOBypass",
                    },
                    {
                        "name": "LD4",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                    }
                ]
            }
        ]
    },
}

pts1_profile3_create = {
    "type": SERVER_PROFILE_TYPE, "name": PTS1_PROFILE3_NAME,
    "serverHardwareUri": 'SH:' + PTS1_PROFILE3_SERVER,
    "serverProfileTemplateUri": "SPT:" + PTS1_SPT3_NAME,
}

pts1_profile3_create_expected = {
    "type": SERVER_PROFILE_TYPE, "name": PTS1_PROFILE3_NAME,
    "serverHardwareUri": 'SH:' + PTS1_PROFILE3_SERVER,
    "serverProfileTemplateUri": "SPT:" + PTS1_SPT3_NAME,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": False,
                "driveWriteCache": "Disabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SasHdd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                        "driveNumber": 1,
                    },
                    {
                        "name": "LD2",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SasHdd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                        "driveNumber": 2,
                    },
                    {
                        "name": "LD3",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "IOBypass",
                        "driveNumber": 3,
                    },
                    {
                        "name": "LD4",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "IOBypass",
                        "driveNumber": 4,
                    }
                ]
            }
        ]
    },
}

pts1_profile3_compliance = {
    "name": PTS1_PROFILE3_NAME,
    "compliance-preview": {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "isOnlineUpdate": None,
        "automaticUpdates": [],
        "manualUpdates": [],
    }
}

pts1_profile3_non_compliance = {
    "name": PTS1_PROFILE3_NAME,
    "compliance-preview": {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "isOnlineUpdate": None,
        "automaticUpdates": [],
        "manualUpdates": [COMPLIANCE_LS_REGEX]
    }
}

pts1_profile3_edit = {
    "type": SERVER_PROFILE_TYPE, "name": PTS1_PROFILE3_NAME,
    "serverHardwareUri": 'SH:' + PTS1_PROFILE3_SERVER,
    "serverProfileTemplateUri": "SPT:" + PTS1_SPT3_NAME,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": False,
                "driveWriteCache": "Enabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SasHdd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                        "driveNumber": 1,
                    },
                    {
                        "name": "LD2",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SasHdd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                        "driveNumber": 2,
                    },
                    {
                        "name": "LD3",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "IOBypass",
                        "driveNumber": 3,
                    },
                    {
                        "name": "LD4",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                        "driveNumber": 4,
                    }
                ]
            }
        ]
    },
}

pts2_profile1_create = {
    "type": SERVER_PROFILE_TYPE, "name": PTS2_PROFILE1_NAME,
    "serverHardwareUri": 'SH:' + PTS2_PROFILE1_SERVER, "enclosureGroupUri": 'EG:' + PTS2_PROFILE1_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": True,
                "importConfiguration": False,
                "driveWriteCache": "Disabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID1",
                        "bootable": False,
                        "numPhysicalDrives": 2,
                        "driveTechnology": "SasHdd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                    }
                ]
            }
        ]
    },
}

pts2_profile1_create_expected = {
    "type": SERVER_PROFILE_TYPE, "name": PTS2_PROFILE1_NAME,
    "serverHardwareUri": 'SH:' + PTS2_PROFILE1_SERVER, "enclosureGroupUri": 'EG:' + PTS2_PROFILE1_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": False,
                "importConfiguration": False,
                "driveWriteCache": "Disabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID1",
                        "bootable": False,
                        "numPhysicalDrives": 2,
                        "driveTechnology": "SasHdd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                    }
                ]
            }
        ]
    },
}

pts2_spt1_create_expected = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE, "name": PTS2_SPT1_NAME,
    "serverHardwareTypeUri": 'SHT:' + PTS2_SPT1_SHT, "enclosureGroupUri": 'EG:' + PTS2_SPT1_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": [], "manageConnections": True},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": False,
                "driveWriteCache": "Disabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID1",
                        "bootable": False,
                        "numPhysicalDrives": 2,
                        "driveTechnology": "SasHdd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                    }
                ]
            }
        ]
    },
}

pts2_unassign_profile1_create = {
    "type": SERVER_PROFILE_TYPE, "name": PTS2_UNASSIGN_PROFILE1_NAME,
    "serverHardwareUri": None,
    "serverProfileTemplateUri": "SPT:" + PTS2_SPT1_NAME,
}

pts2_unassign_profile1_create_expected = {
    "type": SERVER_PROFILE_TYPE, "name": PTS2_UNASSIGN_PROFILE1_NAME,
    "serverHardwareUri": None, "serverHardwareTypeUri": 'SHT:' + PTS2_UNASSIGN_PROFILE1_SHT, "enclosureGroupUri": 'EG:' + PTS2_UNASSIGN_PROFILE1_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": False,
                "importConfiguration": False,
                "driveWriteCache": "Disabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID1",
                        "bootable": False,
                        "numPhysicalDrives": 2,
                        "driveTechnology": "SasHdd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                    }
                ]
            }
        ]
    },
}

pts2_unassign_profile1_compliance = {
    "name": PTS2_UNASSIGN_PROFILE1_NAME,
    "compliance-preview": {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "isOnlineUpdate": None,
        "automaticUpdates": [],
        "manualUpdates": []
    }
}

pts2_profile2_create = {
    "type": SERVER_PROFILE_TYPE, "name": PTS2_PROFILE2_NAME,
    "serverHardwareUri": 'SH:' + PTS2_PROFILE2_SERVER, "enclosureGroupUri": 'EG:' + PTS2_PROFILE2_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": True,
                "importConfiguration": False,
                "driveWriteCache": "Disabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "IOBypass",
                    },
                    {
                        "name": "LD2",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                    }
                ]
            }
        ]
    },
}

pts2_profile2_create_expected = {
    "type": SERVER_PROFILE_TYPE, "name": PTS2_PROFILE2_NAME,
    "serverHardwareUri": 'SH:' + PTS2_PROFILE2_SERVER, "enclosureGroupUri": 'EG:' + PTS2_PROFILE2_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": False,
                "importConfiguration": False,
                "driveWriteCache": "Disabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "IOBypass",
                    },
                    {
                        "name": "LD2",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                    }
                ]
            }
        ]
    },
}

pts2_spt2_create_expected = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE, "name": PTS2_SPT2_NAME,
    "serverHardwareTypeUri": 'SHT:' + PTS2_SPT2_SHT, "enclosureGroupUri": 'EG:' + PTS2_SPT2_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": [], "manageConnections": True},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": False,
                "driveWriteCache": "Disabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "IOBypass",
                    },
                    {
                        "name": "LD2",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                    }
                ]
            }
        ]
    }
}

pts2_unassign_profile2_create = {
    "type": SERVER_PROFILE_TYPE, "name": PTS2_UNASSIGN_PROFILE2_NAME,
    "serverHardwareUri": None,
    "serverProfileTemplateUri": "SPT:" + PTS2_SPT2_NAME,
}

pts2_unassign_profile2_create_expected = {
    "type": SERVER_PROFILE_TYPE, "name": PTS2_UNASSIGN_PROFILE2_NAME,
    "serverHardwareUri": None, "serverHardwareTypeUri": 'SHT:' + PTS2_UNASSIGN_PROFILE2_SHT, "enclosureGroupUri": 'EG:' + PTS2_UNASSIGN_PROFILE2_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": False,
                "importConfiguration": False,
                "driveWriteCache": "Disabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "IOBypass",
                    },
                    {
                        "name": "LD2",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                    }
                ]
            }
        ]
    },
}

pts2_unassign_profile2_compliance = {
    "name": PTS2_UNASSIGN_PROFILE2_NAME,
    "compliance-preview": {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "isOnlineUpdate": None,
        "automaticUpdates": [],
        "manualUpdates": []
    }
}

pts2_profile3_create = {
    "type": SERVER_PROFILE_TYPE, "name": PTS2_PROFILE3_NAME,
    "serverHardwareUri": 'SH:' + PTS2_PROFILE3_SERVER, "enclosureGroupUri": 'EG:' + PTS2_PROFILE3_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": True,
                "driveWriteCache": "Disabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SasHdd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                    },
                    {
                        "name": "LD2",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SasHdd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                    },
                    {
                        "name": "LD3",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "IOBypass",
                    },
                    {
                        "name": "LD4",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                    }
                ]
            }
        ]
    },
}

pts2_profile3_create_expected = {
    "type": SERVER_PROFILE_TYPE, "name": PTS2_PROFILE3_NAME,
    "serverHardwareUri": 'SH:' + PTS2_PROFILE3_SERVER, "enclosureGroupUri": 'EG:' + PTS2_PROFILE3_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": False,
                "driveWriteCache": "Disabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SasHdd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                    },
                    {
                        "name": "LD2",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SasHdd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                    },
                    {
                        "name": "LD3",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "IOBypass",
                    },
                    {
                        "name": "LD4",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                    }
                ]
            }
        ]
    },
}

pts2_spt3_create_expected = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE, "name": PTS2_SPT3_NAME,
    "serverHardwareTypeUri": 'SHT:' + PTS2_SPT3_SHT, "enclosureGroupUri": 'EG:' + PTS2_SPT3_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": [], "manageConnections": True},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": False,
                "driveWriteCache": "Disabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SasHdd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                    },
                    {
                        "name": "LD2",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SasHdd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                    },
                    {
                        "name": "LD3",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "IOBypass",
                    },
                    {
                        "name": "LD4",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                    }
                ]
            }
        ]
    },
}

pts2_unassign_profile3_create = {
    "type": SERVER_PROFILE_TYPE, "name": PTS2_UNASSIGN_PROFILE3_NAME,
    "serverHardwareUri": None,
    "serverProfileTemplateUri": "SPT:" + PTS2_SPT3_NAME,
}


pts2_unassign_profile3_create_expected = {
    "type": SERVER_PROFILE_TYPE, "name": PTS2_UNASSIGN_PROFILE3_NAME,
    "serverHardwareUri": None, "serverHardwareTypeUri": 'SHT:' + PTS2_UNASSIGN_PROFILE3_SHT, "enclosureGroupUri": 'EG:' + PTS2_UNASSIGN_PROFILE3_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": False,
                "driveWriteCache": "Disabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SasHdd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                    },
                    {
                        "name": "LD2",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SasHdd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                    },
                    {
                        "name": "LD3",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "IOBypass",
                    },
                    {
                        "name": "LD4",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                    }
                ]
            }
        ]
    },
}

pts2_unassign_profile3_compliance = {
    "name": PTS2_UNASSIGN_PROFILE3_NAME,
    "compliance-preview": {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "isOnlineUpdate": None,
        "automaticUpdates": [],
        "manualUpdates": []
    }
}

pts3_profile1_create = {
    "type": SERVER_PROFILE_TYPE, "name": PTS3_PROFILE1_NAME,
    "serverHardwareUri": 'SH:' + PTS3_PROFILE1_SERVER, "enclosureGroupUri": 'EG:' + PTS3_PROFILE1_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": True,
                "importConfiguration": False,
                "driveWriteCache": "Disabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID1",
                        "bootable": False,
                        "numPhysicalDrives": 2,
                        "driveTechnology": "SasHdd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                    }
                ]
            }
        ]
    },
}

pts3_profile1_create_expected = {
    "type": SERVER_PROFILE_TYPE, "name": PTS3_PROFILE1_NAME,
    "serverHardwareUri": 'SH:' + PTS3_PROFILE1_SERVER, "enclosureGroupUri": 'EG:' + PTS3_PROFILE1_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": False,
                "importConfiguration": False,
                "driveWriteCache": "Disabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID1",
                        "bootable": False,
                        "numPhysicalDrives": 2,
                        "driveTechnology": "SasHdd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                        "driveNumber": 1,
                    }
                ]
            }
        ]
    },
}

pts3_profile1_import = {
    "type": SERVER_PROFILE_TYPE, "name": PTS3_PROFILE1_NAME,
    "serverHardwareUri": 'SH:' + PTS3_PROFILE1_SERVER, "enclosureGroupUri": 'EG:' + PTS3_PROFILE1_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": False,
                "importConfiguration": True,
                "logicalDrives": [],
            }
        ]
    },
}

pts3_profile1_import_expected = {
    "type": SERVER_PROFILE_TYPE, "name": PTS3_PROFILE1_NAME,
    "serverHardwareUri": 'SH:' + PTS3_PROFILE1_SERVER, "enclosureGroupUri": 'EG:' + PTS3_PROFILE1_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": False,
                "importConfiguration": False,
                "driveWriteCache": "Unmanaged",
                "logicalDrives": [
                    {
                        "name": "Logical Drive 1",
                        "raidLevel": "RAID1",
                        "bootable": False,
                        "numPhysicalDrives": 2,
                        "driveTechnology": None,
                        "sasLogicalJBODId": None,
                        "accelerator": "Unmanaged",
                        "driveNumber": 1,
                    }
                ]
            }
        ]
    },
}

pts3_profile1_edit = {
    "type": SERVER_PROFILE_TYPE, "name": PTS3_PROFILE1_NAME,
    "serverHardwareUri": 'SH:' + PTS3_PROFILE1_SERVER, "enclosureGroupUri": 'EG:' + PTS3_PROFILE1_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": False,
                "importConfiguration": False,
                "driveWriteCache": "Enabled",
                "logicalDrives": [
                    {
                        "name": "Logical Drive 1",
                        "raidLevel": "RAID1",
                        "bootable": False,
                        "numPhysicalDrives": 2,
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                        "driveNumber": 1,
                    }
                ]
            }
        ]
    },
}

pts3_profile2_create = {
    "type": SERVER_PROFILE_TYPE, "name": PTS3_PROFILE2_NAME,
    "serverHardwareUri": 'SH:' + PTS3_PROFILE2_SERVER, "enclosureGroupUri": 'EG:' + PTS3_PROFILE2_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": True,
                "importConfiguration": False,
                "driveWriteCache": "Disabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                    },
                    {
                        "name": "LD2",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                    }
                ]
            }
        ]
    },
}

pts3_profile2_create_expected = {
    "type": SERVER_PROFILE_TYPE, "name": PTS3_PROFILE2_NAME,
    "serverHardwareUri": 'SH:' + PTS3_PROFILE2_SERVER, "enclosureGroupUri": 'EG:' + PTS3_PROFILE2_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": False,
                "importConfiguration": False,
                "driveWriteCache": "Disabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                        "driveNumber": 1,
                    },
                    {
                        "name": "LD2",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                        "driveNumber": 2,
                    }
                ]
            }
        ]
    },
}

pts3_profile2_import = {
    "type": SERVER_PROFILE_TYPE, "name": PTS3_PROFILE2_NAME,
    "serverHardwareUri": 'SH:' + PTS3_PROFILE2_SERVER, "enclosureGroupUri": 'EG:' + PTS3_PROFILE2_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": False,
                "importConfiguration": True,
                "logicalDrives": [],
            }
        ]
    },
}

pts3_profile2_import_expected = {
    "type": SERVER_PROFILE_TYPE, "name": PTS3_PROFILE2_NAME,
    "serverHardwareUri": 'SH:' + PTS3_PROFILE2_SERVER, "enclosureGroupUri": 'EG:' + PTS3_PROFILE2_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": False,
                "importConfiguration": False,
                "driveWriteCache": "Unmanaged",
                "logicalDrives": [
                    {
                        "name": "Logical Drive 1",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": None,
                        "sasLogicalJBODId": None,
                        "accelerator": "Unmanaged",
                        "driveNumber": 1,
                    },
                    {
                        "name": "Logical Drive 2",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": None,
                        "sasLogicalJBODId": None,
                        "accelerator": "Unmanaged",
                        "driveNumber": 2,
                    }
                ]
            }
        ]
    },
}

pts3_profile2_edit = {
    "type": SERVER_PROFILE_TYPE, "name": PTS3_PROFILE2_NAME,
    "serverHardwareUri": 'SH:' + PTS3_PROFILE2_SERVER, "enclosureGroupUri": 'EG:' + PTS3_PROFILE2_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": False,
                "importConfiguration": False,
                "driveWriteCache": "Enabled",
                "logicalDrives": [
                    {
                        "name": "Logical Drive 1",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                        "driveNumber": 1,
                    },
                    {
                        "name": "Logical Drive 2",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                        "driveNumber": 2,
                    }
                ]
            }
        ]
    },
}

pts3_profile3_create = {
    "type": SERVER_PROFILE_TYPE, "name": PTS3_PROFILE3_NAME,
    "serverHardwareUri": 'SH:' + PTS3_PROFILE3_SERVER, "enclosureGroupUri": 'EG:' + PTS3_PROFILE3_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": True,
                "importConfiguration": False,
                "driveWriteCache": "Disabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SasHdd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                    },
                    {
                        "name": "LD2",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SasHdd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                    },
                    {
                        "name": "LD3",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                    },
                    {
                        "name": "LD4",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                    }
                ]
            }
        ]
    },
}

pts3_profile3_create_expected = {
    "type": SERVER_PROFILE_TYPE, "name": PTS3_PROFILE3_NAME,
    "serverHardwareUri": 'SH:' + PTS3_PROFILE3_SERVER, "enclosureGroupUri": 'EG:' + PTS3_PROFILE3_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": False,
                "importConfiguration": False,
                "driveWriteCache": "Disabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SasHdd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                        "driveNumber": 1,
                    },
                    {
                        "name": "LD2",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SasHdd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                        "driveNumber": 2,
                    },
                    {
                        "name": "LD3",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                        "driveNumber": 3,
                    },
                    {
                        "name": "LD4",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                        "driveNumber": 4,
                    }
                ]
            }
        ]
    },
}

pts3_profile3_import = {
    "type": SERVER_PROFILE_TYPE, "name": PTS3_PROFILE3_NAME,
    "serverHardwareUri": 'SH:' + PTS3_PROFILE3_SERVER, "enclosureGroupUri": 'EG:' + PTS3_PROFILE3_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": False,
                "importConfiguration": True,
                "logicalDrives": [],
            }
        ]
    },
}

pts3_profile3_import_expected = {
    "type": SERVER_PROFILE_TYPE, "name": PTS3_PROFILE3_NAME,
    "serverHardwareUri": 'SH:' + PTS3_PROFILE3_SERVER, "enclosureGroupUri": 'EG:' + PTS3_PROFILE3_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": False,
                "importConfiguration": False,
                "driveWriteCache": "Unmanaged",
                "logicalDrives": [
                    {
                        "name": "Logical Drive 1",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": None,
                        "sasLogicalJBODId": None,
                        "accelerator": "Unmanaged",
                        "driveNumber": 1,
                    },
                    {
                        "name": "Logical Drive 2",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": None,
                        "sasLogicalJBODId": None,
                        "accelerator": "Unmanaged",
                        "driveNumber": 2,
                    },
                    {
                        "name": "Logical Drive 3",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": None,
                        "sasLogicalJBODId": None,
                        "accelerator": "Unmanaged",
                        "driveNumber": 3,
                    },
                    {
                        "name": "Logical Drive 4",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": None,
                        "sasLogicalJBODId": None,
                        "accelerator": "Unmanaged",
                        "driveNumber": 4,
                    }
                ]
            }
        ]
    },
}


pts3_profile3_edit = {
    "type": SERVER_PROFILE_TYPE, "name": PTS3_PROFILE3_NAME,
    "serverHardwareUri": 'SH:' + PTS3_PROFILE3_SERVER, "enclosureGroupUri": 'EG:' + PTS3_PROFILE3_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": False,
                "importConfiguration": False,
                "driveWriteCache": "Enabled",
                "logicalDrives": [
                    {
                        "name": "Logical Drive 1",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                        "driveNumber": 1,
                    },
                    {
                        "name": "Logical Drive 2",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                        "driveNumber": 2,
                    },
                    {
                        "name": "Logical Drive 3",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                        "driveNumber": 3,
                    },
                    {
                        "name": "Logical Drive 4",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                        "driveNumber": 4,
                    }
                ]
            }
        ]
    },
}

pts4_profile1_create = {
    "type": SERVER_PROFILE_TYPE, "name": PTS4_PROFILE1_NAME,
    "serverHardwareUri": 'SH:' + PTS4_PROFILE1_SERVER, "enclosureGroupUri": 'EG:' + PTS4_PROFILE1_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": True,
                "importConfiguration": False,
                "driveWriteCache": "Enabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID1",
                        "bootable": False,
                        "numPhysicalDrives": 2,
                        "driveTechnology": "SasHdd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                    }
                ]
            }
        ]
    },
}

pts4_profile1_create_expected = {
    "type": SERVER_PROFILE_TYPE, "name": PTS4_PROFILE1_NAME,
    "serverHardwareUri": 'SH:' + PTS4_PROFILE1_SERVER, "enclosureGroupUri": 'EG:' + PTS4_PROFILE1_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": False,
                "importConfiguration": False,
                "driveWriteCache": "Enabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID1",
                        "bootable": False,
                        "numPhysicalDrives": 2,
                        "driveTechnology": "SasHdd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                        "driveNumber": 1,
                    }
                ]
            }
        ]
    },
}

pts4_profile1_edit1 = {
    "type": SERVER_PROFILE_TYPE, "name": PTS4_PROFILE1_NAME,
    "serverHardwareUri": 'SH:' + PTS4_PROFILE1_SERVER, "enclosureGroupUri": 'EG:' + PTS4_PROFILE1_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": False,
                "importConfiguration": False,
                "driveWriteCache": 'Unmanaged',
            }
        ]
    },
}

pts4_profile1_edit2 = {
    "type": SERVER_PROFILE_TYPE, "name": PTS4_PROFILE1_NAME,
    "serverHardwareUri": 'SH:' + PTS4_PROFILE1_SERVER, "enclosureGroupUri": 'EG:' + PTS4_PROFILE1_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": False,
                "importConfiguration": False,
                "driveWriteCache": "Enabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID1",
                        "bootable": False,
                        "numPhysicalDrives": 2,
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                    }
                ]
            }
        ]
    },
}

pts4_profile2_create = {
    "type": SERVER_PROFILE_TYPE, "name": PTS4_PROFILE2_NAME,
    "serverHardwareUri": 'SH:' + PTS4_PROFILE2_SERVER, "enclosureGroupUri": 'EG:' + PTS4_PROFILE2_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": True,
                "importConfiguration": False,
                "driveWriteCache": "Enabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "IOBypass",
                    },
                    {
                        "name": "LD2",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "IOBypass",
                    }
                ]
            }
        ]
    },
}

pts4_profile2_create_expected = {
    "type": SERVER_PROFILE_TYPE, "name": PTS4_PROFILE2_NAME,
    "serverHardwareUri": 'SH:' + PTS4_PROFILE2_SERVER, "enclosureGroupUri": 'EG:' + PTS4_PROFILE2_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": False,
                "importConfiguration": False,
                "driveWriteCache": "Enabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "IOBypass",
                        "driveNumber": 1,
                    },
                    {
                        "name": "LD2",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "IOBypass",
                        "driveNumber": 2,
                    }
                ]
            }
        ]
    },
}

pts4_profile2_edit1 = {
    "type": SERVER_PROFILE_TYPE, "name": PTS4_PROFILE2_NAME,
    "serverHardwareUri": 'SH:' + PTS4_PROFILE2_SERVER, "enclosureGroupUri": 'EG:' + PTS4_PROFILE2_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": False,
                "importConfiguration": False,
                "driveWriteCache": 'Unmanaged',
            }
        ]
    },
}

pts4_profile2_edit2 = {
    "type": SERVER_PROFILE_TYPE, "name": PTS4_PROFILE2_NAME,
    "serverHardwareUri": 'SH:' + PTS4_PROFILE2_SERVER, "enclosureGroupUri": 'EG:' + PTS4_PROFILE2_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": False,
                "importConfiguration": False,
                "driveWriteCache": "Enabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "IOBypass",
                    },
                    {
                        "name": "LD2",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "IOBypass",
                    }
                ]
            }
        ]
    },
}

pts4_profile3_create = {
    "type": SERVER_PROFILE_TYPE, "name": PTS4_PROFILE3_NAME,
    "serverHardwareUri": 'SH:' + PTS4_PROFILE3_SERVER, "enclosureGroupUri": 'EG:' + PTS4_PROFILE3_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": True,
                "importConfiguration": False,
                "driveWriteCache": "Enabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SasHdd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                    },
                    {
                        "name": "LD2",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SasHdd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                    },
                    {
                        "name": "LD3",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "IOBypass",
                    },
                    {
                        "name": "LD4",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "IOBypass",
                    }
                ]
            }
        ]
    },
}

pts4_profile3_create_expected = {
    "type": SERVER_PROFILE_TYPE, "name": PTS4_PROFILE3_NAME,
    "serverHardwareUri": 'SH:' + PTS4_PROFILE3_SERVER, "enclosureGroupUri": 'EG:' + PTS4_PROFILE3_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": False,
                "importConfiguration": False,
                "driveWriteCache": "Enabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SasHdd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                        "driveNumber": 1,
                    },
                    {
                        "name": "LD2",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SasHdd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                        "driveNumber": 2,
                    },
                    {
                        "name": "LD3",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "IOBypass",
                        "driveNumber": 3,
                    },
                    {
                        "name": "LD4",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "IOBypass",
                        "driveNumber": 4,
                    }
                ]
            }
        ]
    },
}

pts4_profile3_edit1 = {
    "type": SERVER_PROFILE_TYPE, "name": PTS4_PROFILE3_NAME,
    "serverHardwareUri": 'SH:' + PTS4_PROFILE3_SERVER, "enclosureGroupUri": 'EG:' + PTS4_PROFILE3_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": False,
                "importConfiguration": False,
                "driveWriteCache": 'Unmanaged',
            }
        ]
    },
}

pts4_profile3_edit2 = {
    "type": SERVER_PROFILE_TYPE, "name": PTS4_PROFILE3_NAME,
    "serverHardwareUri": 'SH:' + PTS4_PROFILE3_SERVER, "enclosureGroupUri": 'EG:' + PTS4_PROFILE3_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": False,
                "importConfiguration": False,
                "driveWriteCache": "Enabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SasHdd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                    },
                    {
                        "name": "LD2",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SasHdd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                    },
                    {
                        "name": "LD3",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "IOBypass",
                    },
                    {
                        "name": "LD4",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "IOBypass",
                    }
                ]
            }
        ]
    },
}

pts5_profile1_create = {
    "type": SERVER_PROFILE_TYPE, "name": PTS5_PROFILE1_NAME,
    "serverHardwareUri": 'SH:' + PTS5_PROFILE1_SERVER, "enclosureGroupUri": 'EG:' + PTS5_PROFILE1_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": True,
                "importConfiguration": False,
                "driveWriteCache": "Enabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID1",
                        "bootable": False,
                        "numPhysicalDrives": 2,
                        "driveTechnology": "SasHdd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                    }
                ]
            }
        ]
    },
}

pts5_profile1_create_expected = {
    "type": SERVER_PROFILE_TYPE, "name": PTS5_PROFILE1_NAME,
    "serverHardwareUri": 'SH:' + PTS5_PROFILE1_SERVER, "enclosureGroupUri": 'EG:' + PTS5_PROFILE1_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": False,
                "importConfiguration": False,
                "driveWriteCache": "Enabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID1",
                        "bootable": False,
                        "numPhysicalDrives": 2,
                        "driveTechnology": "SasHdd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                        "driveNumber": 1,
                    }
                ]
            }
        ]
    },
}

pts5_profile2_create = {
    "type": SERVER_PROFILE_TYPE, "name": PTS5_PROFILE2_NAME,
    "serverHardwareUri": 'SH:' + PTS5_PROFILE2_SERVER, "enclosureGroupUri": 'EG:' + PTS5_PROFILE2_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": True,
                "importConfiguration": False,
                "driveWriteCache": "Enabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "IOBypass",
                    },
                    {
                        "name": "LD2",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                    }
                ]
            }
        ]
    },
}

pts5_profile2_create_expected = {
    "type": SERVER_PROFILE_TYPE, "name": PTS5_PROFILE2_NAME,
    "serverHardwareUri": 'SH:' + PTS5_PROFILE2_SERVER, "enclosureGroupUri": 'EG:' + PTS5_PROFILE2_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": False,
                "importConfiguration": False,
                "driveWriteCache": "Enabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "IOBypass",
                        "driveNumber": 1,
                    },
                    {
                        "name": "LD2",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                        "driveNumber": 2,
                    }
                ]
            }
        ]
    },
}

pts5_profile3_create = {
    "type": SERVER_PROFILE_TYPE, "name": PTS5_PROFILE3_NAME,
    "serverHardwareUri": 'SH:' + PTS5_PROFILE3_SERVER, "enclosureGroupUri": 'EG:' + PTS5_PROFILE3_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": True,
                "importConfiguration": False,
                "driveWriteCache": "Enabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SasHdd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                    },
                    {
                        "name": "LD2",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SasHdd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                    },
                    {
                        "name": "LD3",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "IOBypass",
                    },
                    {
                        "name": "LD4",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                    }
                ]
            }
        ]
    },
}

pts5_profile3_create_expected = {
    "type": SERVER_PROFILE_TYPE, "name": PTS5_PROFILE3_NAME,
    "serverHardwareUri": 'SH:' + PTS5_PROFILE3_SERVER, "enclosureGroupUri": 'EG:' + PTS5_PROFILE3_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": False,
                "importConfiguration": False,
                "driveWriteCache": "Enabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SasHdd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                        "driveNumber": 1,
                    },
                    {
                        "name": "LD2",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SasHdd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                        "driveNumber": 2,
                    },
                    {
                        "name": "LD3",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "IOBypass",
                        "driveNumber": 3,
                    },
                    {
                        "name": "LD4",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                        "driveNumber": 4,
                    }
                ]
            }
        ]
    },
}


pts6_profile_create = {
    "type": SERVER_PROFILE_TYPE, "name": PTS6_PROFILE_NAME,
    "serverHardwareUri": 'SH:' + PTS6_PROFILE_SERVER, "enclosureGroupUri": 'EG:' + PTS6_PROFILE_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": True,
                "importConfiguration": False,
                "driveWriteCache": "Enabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID1",
                        "bootable": False,
                        "numPhysicalDrives": 2,
                        "driveTechnology": "SasHdd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                    }
                ]
            }
        ]
    },
}

pts6_profile_create_expected = {
    "type": SERVER_PROFILE_TYPE, "name": PTS6_PROFILE_NAME,
    "serverHardwareUri": 'SH:' + PTS6_PROFILE_SERVER, "enclosureGroupUri": 'EG:' + PTS6_PROFILE_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": False,
                "importConfiguration": False,
                "driveWriteCache": "Enabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID1",
                        "bootable": False,
                        "numPhysicalDrives": 2,
                        "driveTechnology": "SasHdd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                        "driveNumber": 1,
                    }
                ]
            }
        ]
    },
}

pts6_profile_move = {
    "type": SERVER_PROFILE_TYPE, "name": PTS6_PROFILE_NAME,
    "serverHardwareUri": 'SH:' + PTS6_PROFILE_MOVE_SERVER, "enclosureGroupUri": 'EG:' + PTS6_PROFILE_MOVE_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": True,
                "importConfiguration": False,
                "driveWriteCache": "Enabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID1",
                        "bootable": False,
                        "numPhysicalDrives": 2,
                        "driveTechnology": "SasHdd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                        "driveNumber": 1,
                    }
                ]
            }
        ]
    },
}

pts6_profile_move_expected = {
    "type": SERVER_PROFILE_TYPE, "name": PTS6_PROFILE_NAME,
    "serverHardwareUri": 'SH:' + PTS6_PROFILE_MOVE_SERVER, "enclosureGroupUri": 'EG:' + PTS6_PROFILE_MOVE_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": False,
                "importConfiguration": False,
                "driveWriteCache": "Enabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID1",
                        "bootable": False,
                        "numPhysicalDrives": 2,
                        "driveTechnology": "SasHdd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                        "driveNumber": 1,
                    }
                ]
            }
        ]
    },
}

pts7_profile_create = {
    "type": SERVER_PROFILE_TYPE, "name": PTS7_PROFILE_NAME,
    "serverHardwareUri": 'SH:' + PTS7_PROFILE_SERVER, "enclosureGroupUri": 'EG:' + PTS7_PROFILE_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": True,
                "importConfiguration": False,
                "driveWriteCache": "Enabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                    },
                    {
                        "name": "LD2",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                    }
                ]
            }
        ]
    },
}

pts7_profile_create_expected = {
    "type": SERVER_PROFILE_TYPE, "name": PTS7_PROFILE_NAME,
    "serverHardwareUri": 'SH:' + PTS7_PROFILE_SERVER, "enclosureGroupUri": 'EG:' + PTS7_PROFILE_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": False,
                "importConfiguration": False,
                "driveWriteCache": "Enabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                        "driveNumber": 1,
                    },
                    {
                        "name": "LD2",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                        "driveNumber": 2,
                    }
                ]
            }
        ]
    },
}

pts8_spt1_create = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE, "name": PTS8_SPT1_NAME,
    "serverHardwareTypeUri": 'SHT:' + PTS8_SPT1_SHT, "enclosureGroupUri": 'EG:' + PTS8_SPT1_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": [], "manageConnections": False},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": True,
                "driveWriteCache": "Enabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID1",
                        "bootable": False,
                        "numPhysicalDrives": 2,
                        "driveTechnology": "SasHdd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                    }
                ]
            }
        ]
    },
}

pts8_profile1_create = {
    "type": SERVER_PROFILE_TYPE, "name": PTS8_PROFILE1_NAME,
    "serverHardwareUri": 'SH:' + PTS8_PROFILE1_SERVER,
    "serverProfileTemplateUri": "SPT:" + PTS8_SPT1_NAME,
}

pts8_profile1_create_expected = {
    "type": SERVER_PROFILE_TYPE, "name": PTS8_PROFILE1_NAME,
    "serverHardwareUri": 'SH:' + PTS8_PROFILE1_SERVER, "enclosureGroupUri": 'EG:' + PTS8_PROFILE1_EG,
    "serverProfileTemplateUri": "SPT:" + PTS8_SPT1_NAME,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": False,
                "importConfiguration": False,
                "driveWriteCache": "Enabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID1",
                        "bootable": False,
                        "numPhysicalDrives": 2,
                        "driveTechnology": "SasHdd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                        "driveNumber": 1,
                    }
                ]
            }
        ]
    },
}

pts8_profile1_compliance = {
    "name": PTS8_PROFILE1_NAME,
    "compliance-preview": {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "isOnlineUpdate": None,
        "automaticUpdates": [],
        "manualUpdates": [],
    }
}

pts8_profile1_unassign = {
    "type": SERVER_PROFILE_TYPE, "name": PTS8_PROFILE1_NAME,
    "serverHardwareUri": None, "serverHardwareTypeUri": 'SHT:' + PTS8_SPT1_SHT, "enclosureGroupUri": 'EG:' + PTS8_PROFILE1_EG,
    "serverProfileTemplateUri": "SPT:" + PTS8_SPT1_NAME,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": False,
                "importConfiguration": False,
                "driveWriteCache": "Enabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID1",
                        "bootable": False,
                        "numPhysicalDrives": 2,
                        "driveTechnology": "SasHdd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                        "driveNumber": 1,
                    }
                ]
            }
        ]
    },
}

pts8_spt2_create = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE, "name": PTS8_SPT2_NAME,
    "serverHardwareTypeUri": 'SHT:' + PTS8_SPT2_SHT, "enclosureGroupUri": 'EG:' + PTS8_SPT2_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": [], "manageConnections": False},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": True,
                "driveWriteCache": "Enabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                    },
                    {
                        "name": "LD2",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                    }
                ]
            }
        ]
    },
}

pts8_profile2_create = {
    "type": SERVER_PROFILE_TYPE, "name": PTS8_PROFILE2_NAME,
    "serverHardwareUri": 'SH:' + PTS8_PROFILE2_SERVER,
    "serverProfileTemplateUri": "SPT:" + PTS8_SPT2_NAME,
}

pts8_profile2_create_expected = {
    "type": SERVER_PROFILE_TYPE, "name": PTS8_PROFILE2_NAME,
    "serverHardwareUri": 'SH:' + PTS8_PROFILE2_SERVER, "enclosureGroupUri": 'EG:' + PTS8_PROFILE2_EG,
    "serverProfileTemplateUri": "SPT:" + PTS8_SPT2_NAME,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": False,
                "importConfiguration": False,
                "driveWriteCache": "Enabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                        "driveNumber": 1,
                    },
                    {
                        "name": "LD2",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                        "driveNumber": 2,
                    }
                ]
            }
        ]
    },
}

pts8_profile2_compliance = {
    "name": PTS8_PROFILE2_NAME,
    "compliance-preview": {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "isOnlineUpdate": None,
        "automaticUpdates": [],
        "manualUpdates": [],
    }
}

pts8_profile2_unassign = {
    "type": SERVER_PROFILE_TYPE, "name": PTS8_PROFILE2_NAME,
    "serverHardwareUri": None, "serverHardwareTypeUri": 'SHT:' + PTS8_SPT2_SHT, "enclosureGroupUri": 'EG:' + PTS8_PROFILE2_EG,
    "serverProfileTemplateUri": "SPT:" + PTS8_SPT2_NAME,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": False,
                "importConfiguration": False,
                "driveWriteCache": "Enabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                        "driveNumber": 1,
                    },
                    {
                        "name": "LD2",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                        "driveNumber": 2,
                    }
                ]
            }
        ]
    },
}

pts8_spt3_create = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE, "name": PTS8_SPT3_NAME,
    "serverHardwareTypeUri": 'SHT:' + PTS8_SPT3_SHT, "enclosureGroupUri": 'EG:' + PTS8_SPT3_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": [], "manageConnections": False},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": True,
                "driveWriteCache": "Enabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SasHdd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                    },
                    {
                        "name": "LD2",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SasHdd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                    },
                    {
                        "name": "LD3",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                    },
                    {
                        "name": "LD4",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                    }
                ]
            }
        ]
    },
}

pts8_profile3_create = {
    "type": SERVER_PROFILE_TYPE, "name": PTS8_PROFILE3_NAME,
    "serverHardwareUri": 'SH:' + PTS8_PROFILE3_SERVER,
    "serverProfileTemplateUri": "SPT:" + PTS8_SPT3_NAME,
}

pts8_profile3_create_expected = {
    "type": SERVER_PROFILE_TYPE, "name": PTS8_PROFILE3_NAME,
    "serverHardwareUri": 'SH:' + PTS8_PROFILE3_SERVER, "enclosureGroupUri": 'EG:' + PTS8_PROFILE3_EG,
    "serverProfileTemplateUri": "SPT:" + PTS8_SPT3_NAME,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": False,
                "driveWriteCache": "Enabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SasHdd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                        "driveNumber": 1,
                    },
                    {
                        "name": "LD2",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SasHdd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                        "driveNumber": 2,
                    },
                    {
                        "name": "LD3",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                        "driveNumber": 3,
                    },
                    {
                        "name": "LD4",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                        "driveNumber": 4,
                    }
                ]
            }
        ]
    },
}

pts8_profile3_compliance = {
    "name": PTS8_PROFILE3_NAME,
    "compliance-preview": {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "isOnlineUpdate": None,
        "automaticUpdates": [],
        "manualUpdates": [],
    }
}

pts8_profile3_unassign = {
    "type": SERVER_PROFILE_TYPE, "name": PTS8_PROFILE3_NAME,
    "serverHardwareUri": None, "serverHardwareTypeUri": 'SHT:' + PTS8_SPT3_SHT, "enclosureGroupUri": 'EG:' + PTS8_PROFILE3_EG,
    "serverProfileTemplateUri": "SPT:" + PTS8_SPT3_NAME,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": False,
                "driveWriteCache": "Enabled",
                "logicalDrives": [
                    {
                        "name": "LD1",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SasHdd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                        "driveNumber": 1,
                    },
                    {
                        "name": "LD2",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SasHdd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                        "driveNumber": 2,
                    },
                    {
                        "name": "LD3",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                        "driveNumber": 3,
                    },
                    {
                        "name": "LD4",
                        "raidLevel": "RAID0",
                        "bootable": False,
                        "numPhysicalDrives": 1,
                        "driveTechnology": "SataSsd",
                        "sasLogicalJBODId": None,
                        "accelerator": "ControllerCache",
                        "driveNumber": 4,
                    }
                ]
            }
        ]
    },
}

# suite setup
profile1 = {
    "type": SERVER_PROFILE_TYPE, "name": PROFILE1_NAME,
    "serverHardwareUri": 'SH:' + PROFILE1_SERVER, "enclosureGroupUri": 'EG:' + PROFILE1_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": True,
                "importConfiguration": False,
                "driveWriteCache": None,
                "logicalDrives": []
            }
        ]
    },
}

profile2 = {
    "type": SERVER_PROFILE_TYPE, "name": PROFILE2_NAME,
    "serverHardwareUri": 'SH:' + PROFILE2_SERVER, "enclosureGroupUri": 'EG:' + PROFILE2_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": True,
                "importConfiguration": False,
                "driveWriteCache": None,
                "logicalDrives": []
            }
        ]
    },
}

profile3 = {
    "type": SERVER_PROFILE_TYPE, "name": PROFILE3_NAME,
    "serverHardwareUri": 'SH:' + PROFILE3_SERVER, "enclosureGroupUri": 'EG:' + PROFILE3_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": False, "mode": None, "secureBoot": "Unmanaged", "pxeBootPolicy": None},
    "firmware": {"manageFirmware": False, },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": True,
                "importConfiguration": False,
                "driveWriteCache": None,
                "logicalDrives": []
            }
        ]
    },
}

# RIS nodes
ris_node_server1_initial = {
    "server": SERVER1,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/smartstorageconfig",
    "validate": {
        "Id": "smartstorageconfig",
    }
}

ris_node_server1_dwc_enabled_lda_cc = {
    "server": SERVER1,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/smartstorageconfig",
    "validate": {
        "DriveWriteCache": "Enabled",
        "LogicalDrives": [
            {"Accelerator": "ControllerCache",
             "LogicalDriveNumber": 1,
             }
        ]
    }
}

ris_node_server1_dwc_disabled_lda_cc = {
    "server": SERVER1,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/smartstorageconfig",
    "validate": {
        "DriveWriteCache": "Disabled",
        "LogicalDrives": [
            {"Accelerator": "ControllerCache",
             "LogicalDriveNumber": 1,
             }
        ]
    }
}

# PTS4 after remove LDs
ris_node_server1_dwc_unmanaged = {
    "server": SERVER1,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/smartstorageconfig",
    "validate": {
        "DriveWriteCache": None,
        "LogicalDrives": []
    }
}

ris_node_server2_initial = {
    "server": SERVER2,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/smartstorageconfig",
    "validate": {
        "Id": "smartstorageconfig",
    }
}

ris_node_server2_dwc_enabled_lda1_io_lda2_io = {
    "server": SERVER2,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/smartstorageconfig",
    "validate": {
        "DriveWriteCache": "Enabled",
        "LogicalDrives": [
            {"Accelerator": "IOBypass",
             "LogicalDriveNumber": 1,
             },
            {"Accelerator": "IOBypass",
             "LogicalDriveNumber": 2,
             }
        ]
    }
}

ris_node_server2_dwc_enabled_lda1_io_lda2_cc = {
    "server": SERVER2,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/smartstorageconfig",
    "validate": {
        "DriveWriteCache": "Enabled",
        "LogicalDrives": [
            {"Accelerator": "IOBypass",
             "LogicalDriveNumber": 1,
             },
            {"Accelerator": "ControllerCache",
             "LogicalDriveNumber": 2,
             }
        ]
    }
}

ris_node_server2_dwc_enabled_lda1_cc_lda2_cc = {
    "server": SERVER2,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/smartstorageconfig",
    "validate": {
        "DriveWriteCache": "Enabled",
        "LogicalDrives": [
            {"Accelerator": "ControllerCache",
             "LogicalDriveNumber": 1,
             },
            {"Accelerator": "ControllerCache",
             "LogicalDriveNumber": 2,
             }
        ]
    }
}

ris_node_server2_dwc_disabled_lda1_io_lda2_io = {
    "server": SERVER2,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/smartstorageconfig",
    "validate": {
        "DriveWriteCache": "Disabled",
        "LogicalDrives": [
            {"Accelerator": "IOBypass",
             "LogicalDriveNumber": 1,
             },
            {"Accelerator": "IOBypass",
             "LogicalDriveNumber": 2,
             }
        ]
    }
}

ris_node_server2_dwc_disabled_lda1_io_lda2_cc = {
    "server": SERVER2,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/smartstorageconfig",
    "validate": {
        "DriveWriteCache": "Disabled",
        "LogicalDrives": [
            {"Accelerator": "IOBypass",
             "LogicalDriveNumber": 1,
             },
            {"Accelerator": "ControllerCache",
             "LogicalDriveNumber": 2,
             }
        ]
    }
}

ris_node_server2_dwc_disabled_lda1_cc_lda2_cc = {
    "server": SERVER2,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/smartstorageconfig",
    "validate": {
        "DriveWriteCache": "Disabled",
        "LogicalDrives": [
            {"Accelerator": "ControllerCache",
             "LogicalDriveNumber": 1,
             },
            {"Accelerator": "ControllerCache",
             "LogicalDriveNumber": 2,
             }
        ]
    }
}

# PTS4 after remove LDs
ris_node_server2_dwc_unmanaged = {
    "server": SERVER2,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/smartstorageconfig",
    "validate": {
        "DriveWriteCache": None,
        "LogicalDrives": []
    }
}


# PTS7 smartstorageconfig settings
ris_node_server2_settings_dwc_disabled_lda1_cc_lda2_cc = {
    "server": SERVER2,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/smartstorageconfig/settings",
    "validate": {
        "DriveWriteCache": "Disabled",
        "LogicalDrives": [
            {"Accelerator": "ControllerCache",
             "LogicalDriveNumber": 1,
             },
            {"Accelerator": "ControllerCache",
             "LogicalDriveNumber": 2,
             },
        ]
    }
}

ris_node_server3_initial = {
    "server": SERVER3,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/smartstorageconfig",
    "validate": {
        "Id": "smartstorageconfig",
    }
}

ris_node_server3_dwc_enabled_lda1_cc_lda2_cc_lda3_io_lda4_io = {
    "server": SERVER3,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/smartstorageconfig",
    "validate": {
        "DriveWriteCache": "Enabled",
        "LogicalDrives": [
            {"Accelerator": "ControllerCache",
             "LogicalDriveNumber": 1,
             },
            {"Accelerator": "ControllerCache",
             "LogicalDriveNumber": 2,
             },
            {"Accelerator": "IOBypass",
             "LogicalDriveNumber": 3,
             },
            {"Accelerator": "IOBypass",
             "LogicalDriveNumber": 4,
             },
        ]
    }
}

ris_node_server3_dwc_enabled_lda1_cc_lda2_cc_lda3_io_lda4_cc = {
    "server": SERVER3,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/smartstorageconfig",
    "validate": {
        "DriveWriteCache": "Enabled",
        "LogicalDrives": [
            {"Accelerator": "ControllerCache",
             "LogicalDriveNumber": 1,
             },
            {"Accelerator": "ControllerCache",
             "LogicalDriveNumber": 2,
             },
            {"Accelerator": "IOBypass",
             "LogicalDriveNumber": 3,
             },
            {"Accelerator": "ControllerCache",
             "LogicalDriveNumber": 4,
             },
        ]
    }
}

ris_node_server3_dwc_enabled_lda1_cc_lda2_cc_lda3_cc_lda4_cc = {
    "server": SERVER3,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/smartstorageconfig",
    "validate": {
        "DriveWriteCache": "Enabled",
        "LogicalDrives": [
            {"Accelerator": "ControllerCache",
             "LogicalDriveNumber": 1,
             },
            {"Accelerator": "ControllerCache",
             "LogicalDriveNumber": 2,
             },
            {"Accelerator": "ControllerCache",
             "LogicalDriveNumber": 3,
             },
            {"Accelerator": "ControllerCache",
             "LogicalDriveNumber": 4,
             },
        ]
    }
}

ris_node_server3_dwc_disabled_lda1_cc_lda2_cc_lda3_io_lda4_io = {
    "server": SERVER3,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/smartstorageconfig",
    "validate": {
        "DriveWriteCache": "Disabled",
        "LogicalDrives": [
            {"Accelerator": "ControllerCache",
             "LogicalDriveNumber": 1,
             },
            {"Accelerator": "ControllerCache",
             "LogicalDriveNumber": 2,
             },
            {"Accelerator": "IOBypass",
             "LogicalDriveNumber": 3,
             },
            {"Accelerator": "IOBypass",
             "LogicalDriveNumber": 4,
             },
        ]
    }
}

ris_node_server3_dwc_disabled_lda1_cc_lda2_cc_lda3_io_lda4_cc = {
    "server": SERVER3,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/smartstorageconfig",
    "validate": {
        "DriveWriteCache": "Disabled",
        "LogicalDrives": [
            {"Accelerator": "ControllerCache",
             "LogicalDriveNumber": 1,
             },
            {"Accelerator": "ControllerCache",
             "LogicalDriveNumber": 2,
             },
            {"Accelerator": "IOBypass",
             "LogicalDriveNumber": 3,
             },
            {"Accelerator": "ControllerCache",
             "LogicalDriveNumber": 4,
             },
        ]
    }
}

ris_node_server3_dwc_disabled_lda1_cc_lda2_cc_lda3_cc_lda4_cc = {
    "server": SERVER3,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/smartstorageconfig",
    "validate": {
        "DriveWriteCache": "Disabled",
        "LogicalDrives": [
            {"Accelerator": "ControllerCache",
             "LogicalDriveNumber": 1,
             },
            {"Accelerator": "ControllerCache",
             "LogicalDriveNumber": 2,
             },
            {"Accelerator": "ControllerCache",
             "LogicalDriveNumber": 3,
             },
            {"Accelerator": "ControllerCache",
             "LogicalDriveNumber": 4,
             },
        ]
    }
}

# PTS4 after remove LDs
ris_node_server3_dwc_unmanaged = {
    "server": SERVER3,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/smartstorageconfig",
    "validate": {
        "DriveWriteCache": None,
        "LogicalDrives": []
    }
}

# PTS6 move profile
ris_node_server3_dwc_enabled_lda_cc = {
    "server": SERVER3,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/smartstorageconfig",
    "validate": {
        "DriveWriteCache": "Enabled",
        "LogicalDrives": [
            {"Accelerator": "ControllerCache",
             "LogicalDriveNumber": 1,
             },
        ]
    }
}

pts1_spts_create = [
    pts1_spt1_create.copy(),
    pts1_spt2_create.copy(),
    pts1_spt3_create.copy()]

pts1_profiles_create = [
    pts1_profile1_create.copy(),
    pts1_profile2_create.copy(),
    pts1_profile3_create.copy()]

pts1_profiles_create_expected = [
    pts1_profile1_create_expected,
    pts1_profile2_create_expected,
    pts1_profile3_create_expected]

pts1_spts_edit = [
    pts1_spt1_edit.copy(),
    pts1_spt2_edit.copy(),
    pts1_spt3_edit.copy()]

pts1_profiles_edit = [
    pts1_profile1_edit.copy(),
    pts1_profile2_edit.copy(),
    pts1_profile3_edit.copy()]

pts1_profiles_compliance = [
    pts1_profile1_compliance,
    pts1_profile2_compliance,
    pts1_profile3_compliance]

pts1_profiles_non_compliance = [
    pts1_profile1_non_compliance,
    pts1_profile2_non_compliance,
    pts1_profile3_non_compliance]

pts1_ris_nodes_after_create = [
    ris_node_server1_dwc_disabled_lda_cc,
    ris_node_server2_dwc_disabled_lda1_io_lda2_io,
    ris_node_server3_dwc_disabled_lda1_cc_lda2_cc_lda3_io_lda4_io]

pts1_ris_nodes_after_edit = [
    ris_node_server1_dwc_enabled_lda_cc,
    ris_node_server2_dwc_enabled_lda1_io_lda2_cc,
    ris_node_server3_dwc_enabled_lda1_cc_lda2_cc_lda3_io_lda4_cc]

pts2_profiles_create = [
    pts2_profile1_create.copy(),
    pts2_profile2_create.copy(),
    pts2_profile3_create.copy()]

pts2_profiles_create_expected = [
    pts2_profile1_create_expected,
    pts2_profile2_create_expected,
    pts2_profile3_create_expected]

pts2_spts_create_expected = [
    pts2_spt1_create_expected,
    pts2_spt2_create_expected,
    pts2_spt3_create_expected]

pts2_unassign_profiles_create = [
    pts2_unassign_profile1_create.copy(),
    pts2_unassign_profile2_create.copy(),
    pts2_unassign_profile3_create.copy()]

pts2_unassign_profiles_create_expected = [
    pts2_unassign_profile1_create_expected,
    pts2_unassign_profile2_create_expected,
    pts2_unassign_profile3_create_expected]

pts2_unassign_profiles_compliance = [
    pts2_unassign_profile1_compliance,
    pts2_unassign_profile2_compliance,
    pts2_unassign_profile3_compliance]

pts2_ris_nodes_after_create = [
    ris_node_server1_dwc_disabled_lda_cc,
    ris_node_server2_dwc_disabled_lda1_io_lda2_cc,
    ris_node_server3_dwc_disabled_lda1_cc_lda2_cc_lda3_io_lda4_cc]

pts3_profiles_create = [
    pts3_profile1_create.copy(),
    pts3_profile2_create.copy(),
    pts3_profile3_create.copy()]

pts3_profiles_create_expected = [
    pts3_profile1_create_expected,
    pts3_profile2_create_expected,
    pts3_profile3_create_expected]

pts3_profiles_import = [
    pts3_profile1_import.copy(),
    pts3_profile2_import.copy(),
    pts3_profile3_import.copy()]

Pts3_profiles_import_expected = [
    pts3_profile1_import_expected,
    pts3_profile2_import_expected,
    pts3_profile3_import_expected]

pts3_profiles_edit = [
    pts3_profile1_edit.copy(),
    pts3_profile2_edit.copy(),
    pts3_profile3_edit.copy()]

pts3_ris_nodes_after_create = [
    ris_node_server1_dwc_disabled_lda_cc,
    ris_node_server2_dwc_disabled_lda1_cc_lda2_cc,
    ris_node_server3_dwc_disabled_lda1_cc_lda2_cc_lda3_cc_lda4_cc]

pts3_ris_nodes_after_edit = [
    ris_node_server1_dwc_enabled_lda_cc,
    ris_node_server2_dwc_enabled_lda1_cc_lda2_cc,
    ris_node_server3_dwc_enabled_lda1_cc_lda2_cc_lda3_cc_lda4_cc]

pts4_profiles_create = [
    pts4_profile1_create.copy(),
    pts4_profile2_create.copy(),
    pts4_profile3_create.copy()]

pts4_profiles_create_expected = [
    pts4_profile1_create_expected,
    pts4_profile2_create_expected,
    pts4_profile3_create_expected]

pts4_profiles_edit1 = [
    pts4_profile1_edit1.copy(),
    pts4_profile2_edit1.copy(),
    pts4_profile3_edit1.copy()]

pts4_profiles_edit2 = [
    pts4_profile1_edit2.copy(),
    pts4_profile2_edit2.copy(),
    pts4_profile3_edit2.copy()]

pts4_ris_nodes_after_create = [
    ris_node_server1_dwc_enabled_lda_cc,
    ris_node_server2_dwc_enabled_lda1_io_lda2_io,
    ris_node_server3_dwc_enabled_lda1_cc_lda2_cc_lda3_io_lda4_io]

pts4_ris_nodes_after_edit1 = [
    ris_node_server1_dwc_unmanaged,
    ris_node_server2_dwc_unmanaged,
    ris_node_server3_dwc_unmanaged]

pts4_ris_nodes_after_edit2 = pts4_ris_nodes_after_create

pts5_profiles_create = [
    pts5_profile1_create.copy(),
    pts5_profile2_create.copy(),
    pts5_profile3_create.copy()]

pts5_profiles_create_expected = [
    pts5_profile1_create_expected,
    pts5_profile2_create_expected,
    pts5_profile3_create_expected]

pts5_ris_nodes_after_create = [
    ris_node_server1_dwc_enabled_lda_cc,
    ris_node_server2_dwc_enabled_lda1_io_lda2_cc,
    ris_node_server3_dwc_enabled_lda1_cc_lda2_cc_lda3_io_lda4_cc]

pts6_profiles_create = [pts6_profile_create.copy(), ]

pts6_profiles_create_expected = [pts6_profile_create_expected, ]

pts6_profiles_move = [pts6_profile_move.copy()]

pts6_profiles_move_expected = [pts6_profile_move_expected]

pts6_ris_nodes_after_create = [ris_node_server1_dwc_enabled_lda_cc]

pts6_ris_nodes_after_move = [ris_node_server3_dwc_enabled_lda_cc]

pts7_profiles_create = [pts7_profile_create.copy(), ]

pts7_profiles_create_expected = [pts7_profile_create_expected]

pts7_ris_nodes_after_create = [ris_node_server2_dwc_enabled_lda1_cc_lda2_cc]

pts7_ris_nodes_after_update_on_ilo = [
    ris_node_server2_settings_dwc_disabled_lda1_cc_lda2_cc]

pts7_ris_nodes_after_server_reset = [
    ris_node_server2_dwc_disabled_lda1_cc_lda2_cc]

pts8_spts_create = [
    pts8_spt1_create.copy(),
    pts8_spt2_create.copy(),
    pts8_spt3_create.copy()]

pts8_profiles_create = [
    pts8_profile1_create.copy(),
    pts8_profile2_create.copy(),
    pts8_profile3_create.copy()]

pts8_profiles_create_expected = [
    pts8_profile1_create_expected,
    pts8_profile2_create_expected,
    pts8_profile3_create_expected]

pts8_profiles_unassign = [
    pts8_profile1_unassign.copy(),
    pts8_profile2_unassign.copy(),
    pts8_profile3_unassign.copy()]

pts8_profiles_reassign = [
    pts8_profile1_create_expected.copy(),
    pts8_profile2_create_expected.copy(),
    pts8_profile3_create_expected.copy()]

pts8_profiles_compliance = [
    pts8_profile1_compliance,
    pts8_profile2_compliance,
    pts8_profile3_compliance]

pts8_ris_nodes_after_create = [
    ris_node_server1_dwc_enabled_lda_cc,
    ris_node_server2_dwc_enabled_lda1_cc_lda2_cc,
    ris_node_server3_dwc_enabled_lda1_cc_lda2_cc_lda3_cc_lda4_cc]

suite_setup_profiles = [profile1.copy(), profile2.copy(), profile3.copy()]

suite_setup_ris_nodes = [
    ris_node_server1_initial,
    ris_node_server2_initial,
    ris_node_server3_initial]

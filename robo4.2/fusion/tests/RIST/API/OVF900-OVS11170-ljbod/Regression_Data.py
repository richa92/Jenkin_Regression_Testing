admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
ilo_credentials = {'username': 'Administrator', 'password': 'hpvse123'}

# Resource types for X-API-Version=800
APPLIANCE_NETWORK_CONFIGURATION_TYPE = 'ApplianceNetworkConfigurationV2'
TIME_AND_LOCALE_TYPE = 'TimeAndLocale'
USER_AND_PERMISSION_TYPE = 'UserAndPermissions'
ETHERNET_NETWORK_TYPE = 'ethernet-networkV4'
FCOE_NETWORK_TYPE = 'fcoe-networkV4'
FC_NETWORK_TYPE = 'fc-networkV4'
NETWORK_SET_TYPE = 'network-setV4'
LOGICAL_INTERCONNECT_GROUP_TYPE = 'logical-interconnect-groupV5'
SAS_LOGICAL_INTERCONNECT_GROUP_TYPE = 'sas-logical-interconnect-groupV2'
ENCLOSURE_GROUP_TYPE = 'EnclosureGroupV7'
INTERCONNECT_TYPE = 'InterconnectV4'
ENCLOSURE_TYPE = 'EnclosureV7'
STORAGE_SYSTEM_TYPE = 'StorageSystemV4'
SERVER_PROFILE_TEMPLATE_TYPE = 'ServerProfileTemplateV6'
SERVER_PROFILE_TYPE = 'ServerProfileV10'
SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE = 'ServerProfileCompliancePreviewV1'
SAS_LOGICAL_JBOD_TYPE = 'sas-logical-jbodV4'

# Enclosures
ENC1 = 'CN754406XL'
ENC2 = 'CN754404R6'
ENC3 = 'CN754406WB'

# LIG, SASLIG, AND LE
LIG_NAME = 'LIG1'
SASLIG_NAME = 'SASLIG1'
EG_NAME = 'EG1'
LE_NAME = 'LE1'

# Potash interconnects
ENC1ICBAY3 = '%s, interconnect 3' % ENC1
ENC2ICBAY6 = '%s, interconnect 6' % ENC2

# Natasha SAS interconnects
ENC1SASICBAY1 = '%s, interconnect 1' % ENC1
ENC1SASICBAY4 = '%s, interconnect 4' % ENC1

# Drive Enclosures (Bigbird)
ENC1DEBAY1 = '%s, bay 1' % ENC1

# Server Hardware
ENC1SHBAY1 = '%s, bay 1' % ENC1
ENC1SHBAY3 = '%s, bay 3' % ENC1
ENC1SHBAY5 = '%s, bay 5' % ENC1
ENC1SHBAY6 = '%s, bay 6' % ENC1
ENC1SHBAY7 = '%s, bay 7' % ENC1
ENC1SHBAY8 = '%s, bay 8' % ENC1
ENC2SHBAY1 = '%s, bay 1' % ENC2
ENC2SHBAY5 = '%s, bay 5' % ENC2
ENC2SHBAY7 = '%s, bay 7' % ENC2
ENC3SHBAY1 = '%s, bay 1' % ENC3
ENC3SHBAY5 = '%s, bay 5' % ENC3

enclosures = [
    {"type": "EnclosureV400", "name": ENC1, },
    {"type": "EnclosureV400", "name": ENC2, },
    {"type": "EnclosureV400", "name": ENC3, },
]

sasics = [
    {"name": ENC1SASICBAY1, },
    {"name": ENC1SASICBAY4, },
]

sasic_bay1 = [{"name": ENC1SASICBAY1, }, ]
sasic_bay4 = [{"name": ENC1SASICBAY4, }, ]
sasic1_dict = {"name": ENC1SASICBAY1, }
sasic4_dict = {"name": ENC1SASICBAY4, }

ics = [
    {"name": ENC1ICBAY3, },
    {"name": ENC2ICBAY6, },
]
gen9_ljb1 = 'XL-bay3-gen9-ljb1'
gen10_ljb1 = 'XL-bay8-gen10-ljb1'
gen9_ljb2 = 'XL-bay3-gen9-ljb2'
gen10_ljb2 = 'XL-bay8-gen10-ljb2'
gen9_new_ljb = 'XL-bay3-gen9-new-ljb'
gen10_new_ljb = 'XL-bay8-gen10-new-ljb'
spt_gen10_ljb = 'spt-gen10-ljb'
spt_gen9_ljb = 'spt-gen9-ljb'

SASLI = 'LE1-SASLIG1-1'

ljbs = [{"name": gen9_ljb1, "type": SAS_LOGICAL_JBOD_TYPE, "description": "",
         "sasLogicalInterconnectUri": SASLI, "initialScopeUris": [],
         "driveEnclosureUris": [ENC1DEBAY1], "numPhysicalDrives": 1, "minSizeGB": "100",
         "maxSizeGB": "146", "driveTechnology": {"deviceInterface": "SAS", "driveMedia": "HDD"},
         "eraseData": False},
        {"name": gen10_ljb1, "type": SAS_LOGICAL_JBOD_TYPE, "description": "",
         "sasLogicalInterconnectUri": SASLI, "initialScopeUris": [],
         "driveEnclosureUris": [ENC1DEBAY1], "numPhysicalDrives": 1, "minSizeGB": "100",
         "maxSizeGB": "146", "driveTechnology": {"deviceInterface": "SAS", "driveMedia": "HDD"},
         "eraseData": False},
        {"name": gen9_ljb2, "type": SAS_LOGICAL_JBOD_TYPE, "description": "",
         "sasLogicalInterconnectUri": SASLI, "initialScopeUris": [],
         "driveEnclosureUris": [ENC1DEBAY1], "numPhysicalDrives": 1, "minSizeGB": "100",
         "maxSizeGB": "146", "driveTechnology": {"deviceInterface": "SAS", "driveMedia": "HDD"},
         "eraseData": False},
        {"name": gen10_ljb2, "type": SAS_LOGICAL_JBOD_TYPE, "description": "",
         "sasLogicalInterconnectUri": SASLI, "initialScopeUris": [],
         "driveEnclosureUris": [ENC1DEBAY1], "numPhysicalDrives": 1, "minSizeGB": "100",
         "maxSizeGB": "146", "driveTechnology": {"deviceInterface": "SAS", "driveMedia": "HDD"},
         "eraseData": False}, ]

spt_ljbs = [{"name": spt_gen9_ljb, "type": SAS_LOGICAL_JBOD_TYPE, "description": "",
             "sasLogicalInterconnectUri": SASLI, "initialScopeUris": [],
             "driveEnclosureUris": [ENC1DEBAY1], "numPhysicalDrives": 1, "minSizeGB": "100",
             "maxSizeGB": "146", "driveTechnology": {"deviceInterface": "SAS", "driveMedia": "HDD"},
             "eraseData": False},
            {"name": spt_gen10_ljb, "type": SAS_LOGICAL_JBOD_TYPE, "description": "",
             "sasLogicalInterconnectUri": SASLI, "initialScopeUris": [],
             "driveEnclosureUris": [ENC1DEBAY1], "numPhysicalDrives": 1, "minSizeGB": "100",
             "maxSizeGB": "146", "driveTechnology": {"deviceInterface": "SAS", "driveMedia": "HDD"},
             "eraseData": False}, ]

profiles = [{"type": SERVER_PROFILE_TYPE,
             "serverHardwareUri": "SH:" + ENC1SHBAY3,
             "serverHardwareTypeUri": "SHT:SY 680 Gen9:1:Smart Array P542D Controller:3:HP Synergy 3820C 10/20Gb CNA",
             "enclosureGroupUri": "EG:" + EG_NAME,
             "serialNumberType": "Virtual",
             "iscsiInitiatorNameType": "AutoGenerated",
             "macType": "Virtual",
             "wwnType": "Virtual",
             "name": "OVF900-OVS11170-sp1",
             "description": "",
             "affinity": "Bay",
             "connectionSettings": {"connections": []},
             "boot": {"manageBoot": True, "order": ["HardDisk"]},
             "bootMode": {"manageMode": True, "mode": "UEFI", "secureBoot": "Disabled", "pxeBootPolicy": "Auto"},
             "firmware": {
                 "manageFirmware": False,
                 "firmwareBaselineUri": "",
                 "forceInstallFirmware": False,
                 "firmwareInstallType": None,
                 "firmwareScheduleDateTime": "",
                 "firmwareActivationType": "Immediate"
             },
             "bios": {
                 "manageBios": False,
                 "overriddenSettings": []
             },
             "managementProcessor": {
                 "manageMp": False,
                 "mpSettings": []
             },
             "hideUnusedFlexNics": True,
             "iscsiInitiatorName": "",
             "osDeploymentSettings": None,
             "localStorage": {
                 "sasLogicalJBODs": [{"id": 1,
                                      "deviceSlot": "Mezz 1",
                                      "name": gen9_ljb1,
                                      "numPhysicalDrives": 1,
                                      "driveMinSizeGB": 100,
                                      "driveMaxSizeGB": 146,
                                      "driveTechnology": "SasHdd",
                                      "eraseData": False,
                                      "persistent": True,
                                      "sasLogicalJBODUri": "SASLJBOD:" + gen9_ljb1,
                                      "status": None},
                                     {"id": 2,
                                      "deviceSlot": "Mezz 1",
                                      "name": gen9_new_ljb,
                                      "numPhysicalDrives": 1,
                                      "driveMinSizeGB": 100,
                                      "driveMaxSizeGB": 146,
                                      "driveTechnology": "SasHdd",
                                      "eraseData": False,
                                      "persistent": False,
                                      "status": None}],
                 "controllers": []},
             "sanStorage": None,
             "initialScopeUris": []
             },
            {"type": SERVER_PROFILE_TYPE,
             "serverHardwareUri": "SH:" + ENC1SHBAY8,
             "serverHardwareTypeUri": "SHT:SY 480 Gen10:1:HPE Smart Array P416ie-m SR G10:3:Synergy 3820C 10/20Gb CNA",
             "enclosureGroupUri": "EG:" + EG_NAME,
             "serialNumberType": "Virtual",
             "iscsiInitiatorNameType": "AutoGenerated",
             "macType": "Virtual",
             "wwnType": "Virtual",
             "name": "OVF900-OVS11170-sp2",
             "description": "",
             "affinity": "Bay",
             "connectionSettings": {"connections":
                                    [{"id": 1, "name": "", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                      "networkUri": "ETH:net100", "requestedVFs": "0",
                                      "ipv4": {"ipAddressSource": None, "subnetMask": None, "gateway": None}},
                                        {"id": 2, "name": "", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                         "networkUri": "ETH:net300", "requestedVFs": "0",
                                         "ipv4": {"ipAddressSource": None, "subnetMask": None, "gateway": None}}],
                                    },
             "boot": {"manageBoot": True, "order": ["HardDisk"]},
             "bootMode": {"manageMode": True, "mode": "UEFI", "secureBoot": "Disabled", "pxeBootPolicy": "Auto"},
             "firmware": {
                 "manageFirmware": False,
                 "firmwareBaselineUri": "",
                 "forceInstallFirmware": False,
                 "firmwareInstallType": None,
                 "firmwareScheduleDateTime": "",
                 "firmwareActivationType": "Immediate"
             },
             "bios": {
                 "manageBios": False,
                 "overriddenSettings": []
             },
             "managementProcessor": {
                 "manageMp": False,
                 "mpSettings": []
             },
             "hideUnusedFlexNics": True,
             "iscsiInitiatorName": "",
             "osDeploymentSettings": None,
             "localStorage": {
                 "sasLogicalJBODs": [{"id": 1,
                                      "deviceSlot": "Mezz 1",
                                      "name": gen10_ljb1,
                                      "numPhysicalDrives": 1,
                                      "driveMinSizeGB": 100,
                                      "driveMaxSizeGB": 146,
                                      "driveTechnology": "SasHdd",
                                      "eraseData": False,
                                      "persistent": False,
                                      "sasLogicalJBODUri": "SASLJBOD:" + gen10_ljb1,
                                      "status": None},
                                     {"id": 2,
                                      "deviceSlot": "Mezz 1",
                                      "name": gen10_new_ljb,
                                      "numPhysicalDrives": 1,
                                      "driveMinSizeGB": 100,
                                      "driveMaxSizeGB": 146,
                                      "driveTechnology": "SasHdd",
                                      "eraseData": False,
                                      "persistent": True,
                                      "status": None}],
                 "controllers": []},
             "sanStorage": None,
             "initialScopeUris": []
             }]

edit_profiles = [
    {"type": SERVER_PROFILE_TYPE,
     "serverHardwareUri": "SH:" + ENC1SHBAY3,
     "serverHardwareTypeUri": "SHT:SY 680 Gen9:1:Smart Array P542D Controller:3:HP Synergy 3820C 10/20Gb CNA",
     "enclosureGroupUri": "EG:" + EG_NAME,
     "serialNumberType": "Virtual",
     "iscsiInitiatorNameType": "AutoGenerated",
     "macType": "Virtual",
     "wwnType": "Virtual",
     "name": "OVF900-OVS11170-sp1",
             "description": "",
             "affinity": "Bay",
             "connectionSettings": {"connections": []},
             "boot": {"manageBoot": True, "order": ["HardDisk"]},
             "bootMode": {"manageMode": True, "mode": "UEFI", "secureBoot": "Disabled", "pxeBootPolicy": "Auto"},
             "firmware": {
                 "manageFirmware": False,
                 "firmwareBaselineUri": "",
                 "forceInstallFirmware": False,
                 "firmwareInstallType": None,
                 "firmwareScheduleDateTime": "",
                 "firmwareActivationType": "Immediate"
             },
     "bios": {
                 "manageBios": False,
                 "overriddenSettings": []
             },
     "managementProcessor": {
                 "manageMp": False,
                 "mpSettings": []
             },
     "hideUnusedFlexNics": True,
     "iscsiInitiatorName": "",
     "osDeploymentSettings": None,
     "localStorage": {
                 "sasLogicalJBODs": [{"id": 1,
                                      "deviceSlot": "Mezz 1",
                                      "name": gen9_ljb1,
                                      "numPhysicalDrives": 1,
                                      "driveMinSizeGB": 100,
                                      "driveMaxSizeGB": 146,
                                      "driveTechnology": "SasHdd",
                                      "eraseData": False,
                                      "persistent": True,
                                      "sasLogicalJBODUri": "SASLJBOD:" + gen9_ljb1,
                                      "status": "OK"},
                                     {"id": 2,
                                      "deviceSlot": "Mezz 1",
                                      "name": gen9_new_ljb,
                                      "numPhysicalDrives": 1,
                                      "driveMinSizeGB": 100,
                                      "driveMaxSizeGB": 146,
                                      "driveTechnology": "SasHdd",
                                      "eraseData": False,
                                      "persistent": False,
                                      "sasLogicalJBODUri": "SASLJBOD:" + gen9_new_ljb,
                                      "status": "OK"},
                                     {"id": 3,
                                      "deviceSlot": "Mezz 1",
                                      "name": gen9_ljb2,
                                      "numPhysicalDrives": 1,
                                      "driveMinSizeGB": 100,
                                      "driveMaxSizeGB": 146,
                                      "driveTechnology": "SasHdd",
                                      "eraseData": False,
                                      "persistent": True,
                                      "sasLogicalJBODUri": "SASLJBOD:" + gen9_ljb2,
                                      "status": None}],
                 "controllers": []},
     "sanStorage": None,
     "initialScopeUris": []
     },
    {"type": SERVER_PROFILE_TYPE,
     "serverHardwareUri": "SH:" + ENC1SHBAY8,
     "serverHardwareTypeUri": "SHT:SY 480 Gen10:1:HPE Smart Array P416ie-m SR G10:3:Synergy 3820C 10/20Gb CNA",
     "enclosureGroupUri": "EG:" + EG_NAME,
     "serialNumberType": "Virtual",
     "iscsiInitiatorNameType": "AutoGenerated",
     "macType": "Virtual",
     "wwnType": "Virtual",
     "name": "OVF900-OVS11170-sp2",
             "description": "",
             "affinity": "Bay",
             "connectionSettings": {"connections":
                                    [{"id": 1, "name": "", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                      "networkUri": "ETH:net100", "requestedVFs": "0",
                                      "ipv4": {"ipAddressSource": None, "subnetMask": None, "gateway": None}},
                                        {"id": 2, "name": "", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                         "networkUri": "ETH:net300", "requestedVFs": "0",
                                         "ipv4": {"ipAddressSource": None, "subnetMask": None, "gateway": None}}],
                                    },
     "boot": {"manageBoot": True, "order": ["HardDisk"]},
             "bootMode": {"manageMode": True, "mode": "UEFI", "secureBoot": "Disabled", "pxeBootPolicy": "Auto"},
             "firmware": {
                 "manageFirmware": False,
                 "firmwareBaselineUri": "",
                 "forceInstallFirmware": False,
                 "firmwareInstallType": None,
                 "firmwareScheduleDateTime": "",
                 "firmwareActivationType": "Immediate"
             },
     "bios": {
                 "manageBios": False,
                 "overriddenSettings": []
             },
     "managementProcessor": {
                 "manageMp": False,
                 "mpSettings": []
             },
     "hideUnusedFlexNics": True,
     "iscsiInitiatorName": "",
     "osDeploymentSettings": None,
     "localStorage": {
                 "sasLogicalJBODs": [{"id": 1,
                                      "deviceSlot": "Mezz 1",
                                      "name": gen10_ljb1,
                                      "numPhysicalDrives": 1,
                                      "driveMinSizeGB": 100,
                                      "driveMaxSizeGB": 146,
                                      "driveTechnology": "SasHdd",
                                      "eraseData": False,
                                      "persistent": False,
                                      "sasLogicalJBODUri": "SASLJBOD:" + gen10_ljb1,
                                      "status": "OK"},
                                     {"id": 2,
                                      "deviceSlot": "Mezz 1",
                                      "name": gen10_new_ljb,
                                      "numPhysicalDrives": 1,
                                      "driveMinSizeGB": 100,
                                      "driveMaxSizeGB": 146,
                                      "driveTechnology": "SasHdd",
                                      "eraseData": False,
                                      "persistent": True,
                                      "sasLogicalJBODUri": "SASLJBOD:" + gen10_new_ljb,
                                      "status": "OK"},
                                     {"id": 3,
                                      "deviceSlot": "Mezz 1",
                                      "name": gen10_ljb2,
                                      "numPhysicalDrives": 1,
                                      "driveMinSizeGB": 100,
                                      "driveMaxSizeGB": 146,
                                      "driveTechnology": "SasHdd",
                                      "eraseData": False,
                                      "persistent": True,
                                      "sasLogicalJBODUri": "SASLJBOD:" + gen10_ljb2,
                                      "status": None},
                                     {"id": 4,
                                      "deviceSlot": "Mezz 1",
                                      "name": "rd1",
                                      "numPhysicalDrives": 1,
                                      "driveMinSizeGB": 146,
                                      "driveMaxSizeGB": 146,
                                      "driveTechnology": "SasHdd",
                                      "eraseData": False,
                                      "persistent": False,
                                      "description": "",
                                      "sasLogicalJBODUri": None,
                                      "status": None}],
                 "controllers": [{"logicalDrives": [{
                                  "name": None,
                                  "raidLevel": "RAID0",
                                  "bootable": False,
                                  "numPhysicalDrives": None,
                                  "driveTechnology": None,
                                  "sasLogicalJBODId": 4,
                                  "driveNumber": None,
                                  "accelerator": "ControllerCache",
                                  "numSpareDrives": None}],
                                  "deviceSlot": "Mezz 1",
                                  "mode": "Mixed",
                                  "initialize": True,
                                  "importConfiguration": False,
                                  "driveWriteCache": "Unmanaged",
                                  "predictiveSpareRebuild": "Unmanaged"}]},
     "sanStorage": None,
     "initialScopeUris": []
     }]
profile_templates = [
    {
        "type": SERVER_PROFILE_TEMPLATE_TYPE,
        "serverProfileDescription": "",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9:1:Smart Array P542D Controller:3:HP Synergy 3820C 10/20Gb CNA",
        "enclosureGroupUri": "EG:" + EG_NAME,
        "serialNumberType": "Virtual",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "name": "gen9-spt",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [],
            "manageConnections": False,
        },
        "boot": {
            "manageBoot": True,
            "order": ["HardDisk"],
        },
        "bootMode": {
            "manageMode": True,
            "mode": "UEFI",
            "secureBoot": "Disabled",
            "pxeBootPolicy": "Auto",
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": "",
            "forceInstallFirmware": False,
            "firmwareInstallType": None,
            "firmwareActivationType": "Immediate",
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": [],
        },
        "managementProcessor": {
            "manageMp": False,
            "mpSettings": [],
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorNameType": "AutoGenerated",
        "localStorage": {
            "sasLogicalJBODs": [{
                "id": 1,
                "deviceSlot": "Mezz 1",
                "name": "ljb-g9",
                "numPhysicalDrives": 1,
                "driveMinSizeGB": 146,
                "driveMaxSizeGB": 146,
                "driveTechnology": "SasHdd",
                "eraseData": True,
                "persistent": True,
                "description": ""
            }],
            "controllers": [{
                "logicalDrives": [],
                "deviceSlot": "Mezz 1",
                "mode": "HBA",
                "initialize": False
            }],
        },
        "sanStorage": None,
        "osDeploymentSettings": None,
        "initialScopeUris": []
    }, {
        "type": SERVER_PROFILE_TEMPLATE_TYPE,
        "serverProfileDescription": "",
        "serverHardwareTypeUri": "SHT:SY 660 Gen10:1:HPE Smart Array P416ie-m SR G10:3:Synergy 3820C 10/20Gb CNA:4:HPE Smart Array P416ie-m SR G10",
        "enclosureGroupUri": "EG:" + EG_NAME,
        "serialNumberType": "Virtual",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "name": "gen10-spt",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [],
            "manageConnections": False,
        },
        "boot": {
            "manageBoot": True,
            "order": ["HardDisk"],
        },
        "bootMode": {
            "manageMode": True,
            "mode": "UEFI",
            "secureBoot": "Disabled",
            "pxeBootPolicy": "Auto",
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": "",
            "forceInstallFirmware": False,
            "firmwareInstallType": None,
            "firmwareActivationType": "Immediate",
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": [],
        },
        "managementProcessor": {
            "manageMp": False,
            "mpSettings": [],
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorNameType": "AutoGenerated",
        "localStorage": {
            "sasLogicalJBODs": [{
                "id": 1,
                "deviceSlot": "Mezz 4",
                "name": "ljb1",
                "numPhysicalDrives": 1,
                "driveMinSizeGB": 146,
                "driveMaxSizeGB": 146,
                "driveTechnology": "SasHdd",
                "eraseData": False,
                "persistent": False,
                "description": ""
            }, {
                "id": 2,
                "deviceSlot": "Mezz 4",
                "name": "ld1",
                "numPhysicalDrives": 1,
                "driveMinSizeGB": 146,
                "driveMaxSizeGB": 146,
                "driveTechnology": "SasHdd",
                "eraseData": False,
                "persistent": False,
                "description": ""
            }],
            "controllers": [{
                "logicalDrives": [{
                    "name": None,
                    "raidLevel": "RAID0",
                    "bootable": False,
                    "numPhysicalDrives": None,
                    "driveTechnology": None,
                    "sasLogicalJBODId": 2,
                    "accelerator": "Unmanaged",
                    "numSpareDrives": None
                }],
                "deviceSlot": "Mezz 4",
                "mode": "Mixed",
                "initialize": False,
                "driveWriteCache": "Enabled",
                "predictiveSpareRebuild": "Unmanaged"
            }],
        },
        "sanStorage": None,
        "osDeploymentSettings": None,
        "initialScopeUris": []
    }]

profiles_from_templates = [
    {
        "type": SERVER_PROFILE_TYPE,
        "serverHardwareUri": "SH:" + ENC1SHBAY7,
        "serverHardwareTypeUri": "SHT:SY 480 Gen9:1:Smart Array P542D Controller:3:HP Synergy 3820C 10/20Gb CNA",
        "enclosureGroupUri": "EG:" + EG_NAME,
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "name": "gen9-sp-from-spt",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": []
        },
        "boot": {
            "manageBoot": True,
            "order": ["HardDisk"]
        },
        "bootMode": {
            "manageMode": True,
            "mode": "UEFI",
            "secureBoot": "Disabled",
            "pxeBootPolicy": "Auto"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": "",
            "forceInstallFirmware": False,
            "firmwareInstallType": None,
            "firmwareScheduleDateTime": "",
            "firmwareActivationType": "Immediate"
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "managementProcessor": {
            "manageMp": False,
            "mpSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "serverProfileTemplateUri": "SPT:gen9-spt",
        "osDeploymentSettings": None,
        "localStorage": {
            "sasLogicalJBODs": [{
                "id": 1,
                "deviceSlot": "Mezz 1",
                "name": "ljb-g9",
                "numPhysicalDrives": 1,
                "driveMinSizeGB": 146,
                "driveMaxSizeGB": 146,
                "driveTechnology": "SasHdd",
                "eraseData": False,
                "persistent": True,
                "description": None,
                "status": "Unknown"
            }, {
                "id": 2,
                "deviceSlot": "Mezz 1",
                "name": "spt-gen9-ljb",
                "numPhysicalDrives": 1,
                "driveMinSizeGB": 100,
                "driveMaxSizeGB": 146,
                "driveTechnology": "SasHdd",
                "eraseData": False,
                "persistent": True,
                "sasLogicalJBODUri": "SASLJBOD:" + spt_gen9_ljb,
                "status": None
            }],
            "controllers": [{
                "logicalDrives": [],
                "deviceSlot": "Mezz 1",
                "mode": "HBA",
                "initialize": False,
                "importConfiguration": False
            }]
        },
        "sanStorage": None,
        "initialScopeUris": []
    },
    {
        "type": SERVER_PROFILE_TYPE,
        "serverHardwareUri": "SH:" + ENC1SHBAY6,
        "serverHardwareTypeUri": "SHT:SY 660 Gen10:1:HPE Smart Array P416ie-m SR G10:3:Synergy 3820C 10/20Gb CNA:4:HPE Smart Array P416ie-m SR G10",
        "enclosureGroupUri": "EG:" + EG_NAME,
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "name": "gen10-sp-from-spt",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": []
        },
        "boot": {
            "manageBoot": True,
            "order": ["HardDisk"]
        },
        "bootMode": {
            "manageMode": True,
            "mode": "UEFI",
            "secureBoot": "Disabled",
            "pxeBootPolicy": "Auto"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": "",
            "forceInstallFirmware": False,
            "firmwareInstallType": None,
            "firmwareScheduleDateTime": "",
            "firmwareActivationType": "Immediate"
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "managementProcessor": {
            "manageMp": False,
            "mpSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "serverProfileTemplateUri": "SPT:gen10-spt",
        "osDeploymentSettings": None,
        "localStorage": {
            "sasLogicalJBODs": [{
                "id": 1,
                "deviceSlot": "Mezz 4",
                "name": "ljb1",
                "numPhysicalDrives": 1,
                "driveMinSizeGB": 146,
                "driveMaxSizeGB": 146,
                "driveTechnology": "SasHdd",
                "eraseData": False,
                "persistent": False,
                "description": None,
                "status": "Unknown"
            }, {
                "id": 2,
                "deviceSlot": "Mezz 4",
                "name": "ld1",
                "numPhysicalDrives": 1,
                "driveMinSizeGB": 146,
                "driveMaxSizeGB": 146,
                "driveTechnology": "SasHdd",
                "eraseData": False,
                "persistent": False,
                "description": None,
                "status": "Unknown"
            }, {
                "id": 3,
                "deviceSlot": "Mezz 4",
                "name": "spt-gen10-ljb",
                "numPhysicalDrives": 1,
                "driveMinSizeGB": 100,
                "driveMaxSizeGB": 146,
                "driveTechnology": "SasHdd",
                "eraseData": False,
                "persistent": True,
                "sasLogicalJBODUri": "SASLJBOD:" + spt_gen10_ljb,
                "status": None
            }],
            "controllers": [{
                "logicalDrives": [{
                    "name": None,
                    "raidLevel": "RAID0",
                    "bootable": False,
                    "numPhysicalDrives": None,
                    "driveTechnology": None,
                    "sasLogicalJBODId": 2,
                    "driveNumber": None,
                    "accelerator": "Unmanaged",
                    "numSpareDrives": None
                }],
                "deviceSlot": "Mezz 4",
                "mode": "Mixed",
                "initialize": False,
                "importConfiguration": False,
                "driveWriteCache": "Enabled",
                "predictiveSpareRebuild": "Unmanaged"
            }]
        },
        "sanStorage": None,
        "initialScopeUris": []
    }, ]

del_ljb_task = {'keyword': 'Delete Logical JBOD',
                'argument': spt_gen10_ljb,
                'taskState': 'Error',
                'timeout': '120',
                'interval': '15',
                'status_code': 200,
                'errorMessage': 'DFRM_SAS_LOGICAL_JBOD_UNABLE_TO_DELETE_SP_EXISTS'}

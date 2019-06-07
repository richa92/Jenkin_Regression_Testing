""" HPE DFRM Varibles.py file for declaring common constants and Rest API JSON Payloads """
print "Developed By HP India"
FUSION_IP = r'15.112.86.12'  # HP One View Appliance IP
BROWSER = r'firefox'

FUSION_ADMIN_LOGIN = r'Administrator'        # Credentials for login to HP One View
FUSION_ADMIN_PASSWORD = r'hpvse123'


loggerlevel = r'INFO'   # use INFO|DEBUG

# below are the variable for Natasha_F175
enclosure_uri = r'/rest/enclosures'
sas_interconnect_uri = r'/rest/sas-interconnects'
drive_enclosure_uri = r'/rest/drive-enclosures'
sas_interconnect_state = r'Monitored'
drive_enclosure_state = r'Monitored'
enclosure_state = r'Monitored'
natasha_model = r'Synergy 12Gb SAS Connection Module'
big_Bird_model = r'Synergy D3940 Storage Module'
power_state = r'On'
task_create_status = r'Added SAS logical Interconnect group'
task_delete_status = r'Deleted sas-logical-interconnect-groups successfully'
task_create_status = r'None'
task_delete_status = r'None'
Delete_LIG_Status = r'None'
task_state = r'Completed'
lig_state = r'Active'
permittedInterconnectTypeUri = '/rest/sas-interconnect-types/Synergy12GbSASConnectionModule'


# below variables are for F176.txt
LIG_Names = ['RGLIG1', 'RGLIG4', 'RGLIG14']
bay_list = [[1], [4], [1, 4]]
baylistno = []

UI_LIG_name = 'RGLIGbay1updated'


# Variables for LE Creation New
EG_NAME = 'RGLE_EG'
LE_Name = 'RGLE1'
LE_Enc_Num = 3
logicalEnclosureUri = r'/rest/logical-enclosures'
enclosureGroupUri = r'/rest/enclosure-groups'


# variables for server profile creation
serverProfileUri = r'/rest/server-profiles/'
server_profile_create_status = r'Created server profile: RG_SP0.'
serverHardwareTypeUri = r'/rest/server-hardware-types'
Erase_flag = 0
Persist_flag = 0

# variables for sas-logical-jbod
LJbodminSizeGB = 1999
LJbodmaxSizeGB = 11446411
sasLogicalJbodType = r'sas-logical-jbod'
sasLogicalInterconnectUri = r'/rest/sas-logical-interconnects/'
sasLogicalJbodUri = r'/rest/sas-logical-jbods'
sasLogicalJbodAttachmentType = r'sas-logical-jbod-attachment'
LE_Create_task_status = r'None'  # r'Logical Enclosure Created successfully.'
sasLJbod_task_create_status = r'None'  # "SAS logical JBOD created successfully."
sasLJbod_task_delete_status = r'None'  # Removed SAS logical JBOD successfully."
numofServerProfiles = 1
# sasLJbodNumPerServerProfile = 1 #  sasLJbodNumPerLI/numofServerProfiles
sasLJbodNumPerLI = 1
num_Jbod_Drives = 1  # Number of Drives in each LJbod
sasLJbodAttachment_create_status = "SAS logical JBOD attachment created successfully."
sasLogicalJbodAttachmentUri = r'/rest/sas-logical-jbod-attachments'
logicalEnclosure_task_delete_status = "SAS logical interconnect deleted successfully."
serverProfileType = "ServerProfileV6"
serverHardwareUri = r'/rest/server-hardware'


# variables for F636
# sas_interconnect_CPU_Reset_status=r'SAS Interconnect CPU reset control request is completed.'
# sas_interconnect_Device_Reset_status=r'SAS Interconnect device reset control request is completed.'
# sas_interconnect_power_control_status=r'SAS Interconnect power control request is completed.'
# sas_interconnect_uid_light_control_status=r'SAS Interconnect UID light control request is completed.'
# drive_enc_device_reset_status=r'DriveEnclosure device reset control request is completed.'
# drive_enc_power_control_status=r'DriveEnclosure power control request is completed.'
# drive_enc_uid_light_control_status=r'DriveEnclosure UID light control request is completed.'

# variables for F636
sas_interconnect_CPU_Reset_status = r'None'
sas_interconnect_Device_Reset_status = r'None'
sas_interconnect_power_control_status = r'None'
sas_interconnect_uid_light_control_status = r'None'
drive_enc_device_reset_status = r'None'
drive_enc_power_control_status = r'None'
drive_enc_uid_light_control_status = r'None'
######################################################
hw_list = []
lists = []
SAS_HDD_List = []
lignamess = "LIG_dualDomain"
egnames = "EG1"
lenames = "le1"

sp1_index = 0
sp2_index = 1
sw_hw_1_index = 0
sw_hw_2_index = 1
server_index = 1

checkspdictionary = {
}
addone = 1
MezzCardPresent = 0
MaxLJBOD = "MAXLJBOD"
MaxDrives = "MAXDRIVES"
formezz = "Mezz 1"
fornull = "null"
forname = "ljbod"
letssay = "S"
sassmall = "Sas"
satasmall = "Sata"
capitalh = "H"
capitals = "Ss"
listtoaddljbods = []
listtoaddljbodss = []
zero = 1
taskstates = 'Completed'
advanceligpayload = {
    "type": "sas-logical-interconnect-groupV2",
    "description": None,
    "status": None,
    "state": None,
    "eTag": None,
    "created": None,
    "modified": None,
    "category": None,
    "uri": None,
    "interconnectMapTemplate": {
            "interconnectMapEntryTemplates": [{
                "logicalLocation": {
                    "locationEntries": [{
                        "type": "Bay",
                        "relativeValue": 1
                    }, {
                        "type": "Enclosure",
                        "relativeValue": 1
                    }]
                },
                "permittedInterconnectTypeUri": "/rest/sas-interconnect-types/Synergy12GbSASConnectionModule",
                "enclosureIndex": 1
            }, {
                "logicalLocation": {
                    "locationEntries": [{
                        "type": "Bay",
                        "relativeValue": 4
                    }, {
                        "type": "Enclosure",
                        "relativeValue": 1
                    }]
                },
                "permittedInterconnectTypeUri": "/rest/sas-interconnect-types/Synergy12GbSASConnectionModule",
                "enclosureIndex": 1
            }]
    },
    "name": "LIG_dualDomain",
    "enclosureType": "SY12000",
    "enclosureIndexes": [1],
    "interconnectBaySet": 1,
    "initialScopeUris": []
}

advancesingledomainligpayload = {
    "type": "sas-logical-interconnect-groupV2",
    "description": None,
    "status": None,
    "state": None,
    "eTag": None,
    "created": None,
    "modified": None,
    "category": None,
    "uri": None,
    "interconnectMapTemplate": {
            "interconnectMapEntryTemplates": [{
                "logicalLocation": {
                    "locationEntries": [{
                        "type": "Bay",
                        "relativeValue": 1
                    }, {
                        "type": "Enclosure",
                        "relativeValue": 1
                    }]
                },
                "permittedInterconnectTypeUri": "/rest/sas-interconnect-types/Synergy12GbSASConnectionModule",
                "enclosureIndex": 1
            }]
    },
    "name": "LIG-Single-Domain",
    "enclosureType": "SY12000",
    "enclosureIndexes": [1],
    "interconnectBaySet": 1,
    "initialScopeUris": []
}

advanceegpayload = {
    "name": "EG1",
    "interconnectBayMappings": [{
            "interconnectBay": 1,
        "enclosureIndex": 1,
        "logicalInterconnectGroupUri": "/rest/sas-logical-interconnect-groups/72eabe7a-d1fe-4ee0-b9d4-e3bb63aa3626"
    }, {
        "interconnectBay": 4,
        "enclosureIndex": 1,
        "logicalInterconnectGroupUri": "/rest/sas-logical-interconnect-groups/72eabe7a-d1fe-4ee0-b9d4-e3bb63aa3626"
    }],
    "ipAddressingMode": "External",
    "ipRangeUris": [],
    "enclosureCount": 1,
    "osDeploymentSettings": {
        "manageOSDeployment": False,
        "deploymentModeSettings": {
            "deploymentMode": "None",
            "deploymentNetworkUri": None
        }
    },
    "powerMode": "RedundantPowerFeed",
    "ambientTemperatureMode": "Standard",
    "initialScopeUris": []
}

advancelepayload = {
    "name": "le1",
    "enclosureUris": ["/rest/enclosures/0000000000A66101"],
    "enclosureGroupUri": "/rest/enclosure-groups/658683b2-abec-4dd3-8aa1-863d864ab37e",
    "firmwareBaselineUri": None,
    "forceInstallFirmware": False,
    "initialScopeUris": []
}

advancesppayload = {
    "type": "ServerProfileV10",
    # "serverHardwareUri": "/rest/server-hardware/30373737-3237-4D32-3230-313530314752",
    # "serverHardwareTypeUri": "/rest/server-hardware-types/FEF75493-4A44-406A-8835-EADF8248D8BE",
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": "sp6",
    "description": "",
    "affinity": "Bay",
    "connectionSettings": {
            "connections": []
    },
    "boot": None,
    "bootMode": {
        "manageMode": False
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
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None,
    "initialScopeUris": []
}


advancesp2payload = {
    "type": "ServerProfileV10",
    # "serverHardwareUri": "/rest/server-hardware/30373737-3237-4D32-3230-313530314752",
    # "serverHardwareTypeUri": "/rest/server-hardware-types/FEF75493-4A44-406A-8835-EADF8248D8BE",
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": "sp6",
    "description": "",
    "affinity": "Bay",
    "connectionSettings": {
            "connections": []
    },
    "boot": None,
    "bootMode": {
        "manageMode": False
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
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None,
    "initialScopeUris": []
}

payloadoflogicalenclosureupdatefromgroup = {}

supportpayload = {
    "errorCode": "LE", "encrypt": True

}
check = None
DiskSASHDD = "SASHDD"
DiskSASSSD = "SASSSD"
DiskSATAHDD = "SATAHDD"
DiskSATASSD = "SATASSD"
uriiii = "updateFromGroup"
supportdump = "/support-dumps"

advanceligpayloadforsingledomain = {
    "type": "sas-logical-interconnect-groupV2",
    "description": None,
    "status": None,
    "state": None,
    "eTag": None,
    "created": None,
    "modified": None,
    "category": None,
    "uri": None,
    "interconnectMapTemplate": {
        "interconnectMapEntryTemplates": [{
            "logicalLocation": {
                "locationEntries": [{
                    "type": "Bay",
                    "relativeValue": 1
                }, {
                    "type": "Enclosure",
                    "relativeValue": 1
                }]
            },
            "permittedInterconnectTypeUri": "/rest/sas-interconnect-types/Synergy12GbSASConnectionModule",
            "enclosureIndex": 1
        }]
    },
    "name": "lig1",
    "enclosureType": "SY12000",
    "enclosureIndexes": [1],
    "interconnectBaySet": 1,
    "initialScopeUris": []
}

unassignedhw = {
    "type": "ServerProfileV10",
    "description": "",
    "iscsiInitiatorName": None,
    "iscsiInitiatorNameType": "AutoGenerated",
    "serverProfileTemplateUri": None,
    "templateCompliance": "Unknown",
    "serverHardwareUri": None,
    "affinity": "Bay",
    "associatedServer": None,
    "hideUnusedFlexNics": True,
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": "",
        "forceInstallFirmware": False,
        "firmwareInstallType": None,
        "firmwareScheduleDateTime": "",
        "firmwareActivationType": "Immediate"
    },
    "macType": "Virtual",
    "wwnType": "Virtual",
    "serialNumberType": "Virtual",
    "category": "server-profiles",
    "created": "2018-04-03T16:46:09.678Z",
    "modified": "2018-04-03T16:47:49.551Z",
    "status": "OK",
    "state": "Normal",
    "serverHardwareReapplyState": "NotApplying",
    "inProgress": False,
    "taskUri": "/rest/tasks/DB709512-8C29-4F58-A459-C24F4529B251",
    "connectionSettings": {
        "connections": []
    },
    "bootMode": {
        "manageMode": False
    },
    "boot": None,
    "bios": {
        "manageBios": False,
        "overriddenSettings": []
    },
    "sanStorage": None,
    "osDeploymentSettings": None,
    "refreshState": "NotRefreshing"
}

bay_1 = 1
interconnect_poweroff = [{"op": "replace", "path": "/powerState", "value": "Off"}]
interconnect_poweron = [{"op": "replace", "path": "/powerState", "value": "On"}]
interconnect_softresets = [{"op": "replace", "path": "/cpuResetState", "value": "Reset"}]

interconnect_hardreset = [{"op": "replace", "path": "/deviceResetState", "value": "Reset"}]
statusv = "OK"
bay_4 = 4
listforalertindex = []
predefinedalertwhileefuseonbay1 = ['profilemgr.LocalStorage.PROFILEMGR_LJBOD_HEALTH_ERROR', 'dfrm.ioAdapter1.Interconnect', 'dfrm.ioAdapter2.Interconnect', 'dfrm.sasLi.dualDomain.icmMissing']
predefinedalertwhileefuseonbay4andbay1 = ['dfrm.ioAdapter2.Interconnect', 'dfrm.ioAdapter1.Interconnect', 'dfrm.sasLi.dualDomain.icmMissing']
predefinedalertwhileefuseoffbay1 = ['profilemgr.LocalStorage.PROFILEMGR_LJBOD_HEALTH_ERROR', 'dfrm.sasLi.dualDomain.icmMissing']
listofalertvalues = []

# Power ON/OFF SAS Interconnects Alerts
predefinedalertafterpoweringoffbay1 = ['dfrm.sasic.bay1.power.operations', 'profilemgr.LocalStorage.PROFILEMGR_LJBOD_HEALTH_ERROR']
predefinedalertafterpoweringoffbay1andbay4 = ['dfrm.sasic.bay4.power.operations', 'profilemgr.LocalStorage.PROFILEMGR_LJBOD_HEALTH_ERROR']
predefinedalertafterpoweringonbay1 = ['profilemgr.LocalStorage.PROFILEMGR_LJBOD_HEALTH_ERROR', 'dfrm.sasic.bay4.power.operations']

ExpectedDualDomainICMRemovalAlerts = ['hpris.HpSmartStorageSasSwitch.PartnerSwitchNotPresent', 'dfrm.sasLi.dualDomain.icmMissing']
ExpectedDomainConvertAlerts = ['dfrm.SasLiInconsistent', 'perm.InconsistentLogicalEnclosure']

# Pre defined Restore mismatch Alert on LI
ExpetedSPMisMatchRestoreAlert = ['dfrm.ljbod.configMismatchOnSASICM']
ExpetedLJBODMisMatchRestoreAlert = ['dfrm.ljbod.notConfiguredOnSASICM']

payloadforresetofdriveneclosure = [{
    "op": "replace",
    "path": "/deviceResetState",
    "value": "Reset"
}]
# Drive Enclosure Power off Alerts
DE_Serial_Num = ""
predefinedalertforpoweroffdriveenclosure = ['profilemgr.LocalStorage.PROFILEMGR_LJBOD_HEALTH_ERROR', 'dfrm.de.power.operations']

counterofbay = 0
counterofalerts = 0
stringvalue = "1"
sata = "SATA"
sas = "SAS"
refreshpayload = {"refreshState": "RefreshPending"}
index = "/rest/index/trees"

independentljbodpayload = {
    "name": "ljbod2",
    "initialScopeUris": [],
    "description": "",
    "numPhysicalDrives": 1,
    "driveTechnology": {
    },
    "eraseData": True,
    "type": "sas-logical-jbodV4"
}
editedjbodname = "newname"
eraseondata = "False"
description = "this is the description after edit"
editofindependentljbod = [{"op": "replace", "path": "/eraseData", "value": False}]
listforindependentljbod = []
disksfromfirstbay = []
disksfromsecondbay = []
drivebaseduri = {
    "name": "Test_MDB_1",
            "initialScopeUris": [],
            "description": "",
            "eraseData": False,
            "type": "sas-logical-jbodV4"
}
filename = None

payloadforrestore = {
    "type": "RESTORE",
    "uriOfBackupToRestore": "/rest/backups/Pegasus-ci-9cb654981190_backup_2018-05-15_081755"
}

sppayloadforlogicaldrives = {
    "type": "ServerProfileV10",
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": "SP-RAID",
    "description": "",
    "affinity": "Bay",
    "connectionSettings": {
            "connections": []
    },
    "boot": None,
    "bootMode": {
        "manageMode": False
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
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [{
            "logicalDrives": [{
                "name": None,
                "raidLevel": "RAID1",
                "bootable": False,
                "numPhysicalDrives": None,
                "driveTechnology": None,
                "sasLogicalJBODId": 1,
                "driveNumber": None,
                "accelerator": "Unmanaged",
                "numSpareDrives": None
            }],
            "deviceSlot": "Mezz 1",
            "mode": "RAID",
            "initialize": False,
            "importConfiguration": False,
            "driveWriteCache": "Unmanaged",
            "predictiveSpareRebuild": "Unmanaged"
        }]
    },
    "sanStorage": None,
    "initialScopeUris": []
}

EGPAYLOADSINGLEDOMAIN = {
    "type": "EnclosureGroupV7",
    "uri": "",
    "name": "EG1",
    "eTag": "",
    "enclosureTypeUri": "/rest/enclosure-types/SY12000",
    "stackingMode": "Enclosure",
    "interconnectBayMappingCount": 2,
    "interconnectBayMappings": [{
            "interconnectBay": 1,
            "enclosureIndex": 1,
            "logicalInterconnectGroupUri": "/rest/sas-logical-interconnect-groups/03486ad4-4445-48c1-9ce2-96c1c8979c52"
    }],
    "ipAddressingMode": "External",
    "ipRangeUris": [],
    "powerMode": "RedundantPowerFeed",
    "osDeploymentSettings": {
        "manageOSDeployment": False,
        "deploymentModeSettings": {
            "deploymentMode": "None",
            "deploymentNetworkUri": None
        }
    },
    "enclosureCount": 1,
    "associatedLogicalInterconnectGroups": ["/rest/sas-logical-interconnect-groups/16152529-2512-4690-bbb1-46c7ea86665e"],
    "scopesUri": "",
    "configurationScript": "",
    "enclosureType": "TClass"
}

EDITEGCOPYLIGPAYLOAD = {
    "type": "EnclosureGroupV7",
    "uri": "",
    "name": "EG1",
    "eTag": "",
    "enclosureTypeUri": "/rest/enclosure-types/SY12000",
    "stackingMode": "Enclosure",
    "interconnectBayMappingCount": 2,
    "interconnectBayMappings": [{
            "interconnectBay": 1,
            "enclosureIndex": 1,
            "logicalInterconnectGroupUri": "/rest/sas-logical-interconnect-groups/03486ad4-4445-48c1-9ce2-96c1c8979c52"
    }, {
        "interconnectBay": 4,
        "enclosureIndex": 1,
        "logicalInterconnectGroupUri": "/rest/sas-logical-interconnect-groups/03486ad4-4445-48c1-9ce2-96c1c8979c52"
    }],
    "ipAddressingMode": "External",
    "ipRangeUris": [],
    "powerMode": "RedundantPowerFeed",
    "osDeploymentSettings": {
        "manageOSDeployment": False,
        "deploymentModeSettings": {
            "deploymentMode": "None",
            "deploymentNetworkUri": None
        }
    },
    "enclosureCount": 1,
    "associatedLogicalInterconnectGroups": ["/rest/sas-logical-interconnect-groups/16152529-2512-4690-bbb1-46c7ea86665e"],
    "scopesUri": "",
    "configurationScript": "",
    "enclosureType": "TClass"
}

egpayloadfor3enclosure = {
    "name": "eg_3enclosure",
    "interconnectBayMappings": [{
            "interconnectBay": 1,
        "enclosureIndex": 1,
    }, {
        "interconnectBay": 4,
        "enclosureIndex": 1,
    }, {
        "interconnectBay": 1,
        "enclosureIndex": 2,
    }, {
        "interconnectBay": 4,
        "enclosureIndex": 2,
    }, {
        "interconnectBay": 1,
        "enclosureIndex": 3,
    }, {
        "interconnectBay": 4,
        "enclosureIndex": 3,
    }],
    "ipAddressingMode": "External",
    "ipRangeUris": [],
    "enclosureCount": 3,
    "osDeploymentSettings": {
        "manageOSDeployment": False,
        "deploymentModeSettings": {
            "deploymentMode": "None",
            "deploymentNetworkUri": None
        }
    },
    "powerMode": "RedundantPowerFeed",
    "ambientTemperatureMode": "Standard",
    "initialScopeUris": []
}

lepayloadfor3enclosure = {
    "name": "le_3Enclosure",
    "firmwareBaselineUri": None,
    "forceInstallFirmware": False,
    "initialScopeUris": []
}


#   --------------------  Multi Enclosure Drive Bay Selection Variables  ---------------------------- #
IndLJBODDriveBaySelPayload = {
    "type": "sas-logical-jbodV4",
    "name": "DB_Sel_Ljbod",
    "initialScopeUris": [],
    "sasLogicalInterconnectUri": None,
    "eraseData": False,
    "clearMetaData": True,
    "driveBayUris": []
}

SingleDE = 1
MultipleDE = 99
DriveTypeList = ['SASHDD', 'SASSSD', 'SATAHDD', 'SATASSD']
ERASE_ENABLE = 'Erase_true'
PERSIST_ENABLE = 'PERSIST_true'
NORMAL_BAY_SEL = 'NORMAL_BAY'
RANDOM_BAY_SEL = 'RANDOM_BAY'
INDENTICAL_SW_HW = 'IDENTICAL_SW_HW_PROF_MOBILITY'
LOGICAL_DRIVE = 'RAID_SP'
RAID_PHY_DRIVE = 2
CRYPTO_FIPS_MODE = 'FIPS'
CRYPTO_LEGACY_MODE = 'LEGACY'

CUSTOM_SPP_NAME = "custom_spp"
INTERNAL_FW_REPO = "Internal"
FW_PARALLEL_UPDT = "Parallel"
FW_ORCHESTRATE_UPDT = "Orchestrated"
FW_UPDT_FORCE_TRUE = "True"
FW_UPDT_FORCE_FALSE = "False"
FW_UPDT_STAGE = "Stage"
FW_UPDT_ACTIVATE = "Activate"
FW_UPDT_STAGE_ACTIVATE = "Update"
FW_VALIDATE_TYPE = "ValidateFailFast"
FW_STAGE_WAIT_TIME = "30min"
FW_ACTIVATE_WAIT_TIME = "60min"
FW_STAGE_ACT_WAIT_TIME = "90min"
FW_UPDT_WAIT_INTRVL = "15sec"
FW_LATEST_ISO_NAME = "bp_latest.iso"
FW_OLD_ISO_NAME = "bp_old.iso"

EXP_PAR_STAGE_TASKS = ['Stage firmware (force install).',
                       'Staging complete (force install).']
EXP_PAR_STAGE_ACT_TASKS = ['Stage firmware (force install).',
                           'Staging complete (force install).',
                           'Activate firmware (parallel).',
                           'Activation complete (parallel).',
                           'Refresh SAS interconnect(s).',
                           'Refresh drive enclosure(s).']
EXP_PAR_ACTIVATE_TASKS = ['Activate firmware (parallel).',
                          'Activation complete (parallel).',
                          'Refresh SAS interconnect(s).',
                          'Refresh drive enclosure(s).']

EXP_ORCH_STAGE_TASKS = ['Stage firmware (force install).',
                        'Staging complete (force install).']
EXP_ORCH_STAGE_ACT_TASKS = ['Stage firmware (force install).',
                            'Staging complete (force install).',
                            'Activate firmware (orchestrated).',
                            'Activation complete (orchestrated).',
                            'Refresh SAS interconnect(s).',
                            'Refresh drive enclosure(s).']
EXP_ORCH_ACTIVATE_TASKS = ['Activate firmware (orchestrated).',
                           'Activation complete (orchestrated).',
                           'Refresh SAS interconnect(s).',
                           'Refresh drive enclosure(s).']
FW_COMP_12GBSAS_MODULE_FW_NAME = "Smart Component for HPE Synergy 12Gb SAS Connection Module Firmware"
FW_COMP_D3940_STOR_MODULE_NAME = "Smart Component for HPE Synergy  D3940 Storage Module firmware"

FW_REPO_URL = "http://15.212.143.46/webdav/DFRM-AUTO/"
FW_REPO_NAME = "DFRM_REPO"
FW_REPO_LOGIN_NAME = "root"
FW_REPO_LOGIN_PASSWD = "hpvse123"

FW_REPOSITORY_PAYLOAD = {
    "repositoryName": FW_REPO_NAME,
    "repositoryURI": FW_REPO_URL,
    "userName": FW_REPO_LOGIN_NAME,
    "password": FW_REPO_LOGIN_PASSWD,
}

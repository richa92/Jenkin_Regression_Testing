admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

server_hardwares = [{"name": "ILO7CE712P2MF.lr.eml.lab", "hostname": "16.83.13.48", "username": "Administrator", "password": "password", "force": True, "licensingIntent": "OneViewNoiLO", "configurationState": "Managed"}]

host_name = 'ILO7CE712P2MF.lr.eml.lab'

sht = "DL380 Gen10 1"

ilo_credentials = {'username': 'Administrator', 'password': 'password'}

SP_1 = [{"type": "ServerProfileV10",
         "serverHardwareUri": "SH:" + host_name,
         "serverHardwareTypeUri": "SHT:" + sht,
         "serialNumberType": "Physical",
         "iscsiInitiatorNameType": "AutoGenerated",
         "macType": "Physical",
         "wwnType": "Physical",
         "name": "SP_1",
         "description": "",
         "affinity": None,
         "connectionSettings": {
             "connections": []},
         "boot": {
             "manageBoot": False},
         "bootMode": {
             "manageMode": True,
             "mode": "UEFIOptimized",
             "secureBoot": "Unmanaged",
             "pxeBootPolicy": "Auto"},
         "firmware": {
             "manageFirmware": False,
             "firmwareBaselineUri": "",
             "forceInstallFirmware": False,
             "firmwareInstallType": None,
             "firmwareScheduleDateTime": "",
             "firmwareActivationType": "Immediate"},
         "bios": {
             "manageBios": True,
             "overriddenSettings": [{"id": "WorkloadProfile",
                                     "value": "MissionCritical"},
                                    {"id": "DynamicPowerCapping",
                                     "value": "Auto"},
                                    {"id": "UsbControl",
                                     "value": "UsbEnabled"},
                                    {"id": "AdvancedMemProtection",
                                     "value": "FastFaultTolerantADDDC"},
                                    {"id": "MemRefreshRate",
                                     "value": "Refreshx2"},
                                    {"id": "ConfigurationEnabled",
                                     "value": "Disabled"},
                                    {"id": "PowerRegulator",
                                     "value": "StaticHighPerf"},
                                    {"id": "CollabPowerControl",
                                     "value": "Disabled"},
                                    {"id": "NumaGroupSizeOpt",
                                     "value": "Clustered"},
                                    {"id": "UncoreFreqScaling",
                                     "value": "Maximum"},
                                    {"id": "EnergyEfficientTurbo",
                                     "value": "Disabled"},
                                    {"id": "IntelUpiPowerManagement",
                                     "value": "Disabled"}]},
         "hideUnusedFlexNics": True,
         "iscsiInitiatorName": "",
         "osDeploymentSettings": None,
         "localStorage": {
             "sasLogicalJBODs": [],
             "controllers": []},
         "sanStorage": None,
         "initialScopeUris": []
         }]

SP_2 = [{"type": "ServerProfileV10",
         "serverHardwareUri": "SH:" + host_name,
         "serverHardwareTypeUri": "SHT:" + sht,
         "serialNumberType": "Physical",
         "iscsiInitiatorNameType": "AutoGenerated",
         "macType": "Physical",
         "wwnType": "Physical",
         "name": "SP_2",
         "description": "",
         "affinity": None,
         "connectionSettings": {
             "connections": []},
         "boot": {
             "manageBoot": False},
         "bootMode": {
             "manageMode": True,
             "mode": "UEFI",
             "secureBoot": "Unmanaged",
             "pxeBootPolicy": "Auto"},
         "firmware": {
             "manageFirmware": False,
             "firmwareBaselineUri": "",
             "forceInstallFirmware": False,
             "firmwareInstallType": None,
             "firmwareScheduleDateTime": "",
             "firmwareActivationType": "Immediate"},
         "bios": {
             "manageBios": True,
             "overriddenSettings": [{"id": "WorkloadProfile",
                                     "value": "MissionCritical"},
                                    {"id": "DynamicPowerCapping",
                                     "value": "Auto"},
                                    {"id": "UsbControl",
                                     "value": "UsbEnabled"},
                                    {"id": "AdvancedMemProtection",
                                     "value": "FastFaultTolerantADDDC"},
                                    {"id": "MemRefreshRate",
                                     "value": "Refreshx2"},
                                    {"id": "ConfigurationEnabled",
                                     "value": "Disabled"},
                                    {"id": "PowerRegulator",
                                     "value": "StaticHighPerf"},
                                    {"id": "CollabPowerControl",
                                     "value": "Disabled"},
                                    {"id": "NumaGroupSizeOpt",
                                     "value": "Clustered"},
                                    {"id": "UncoreFreqScaling",
                                     "value": "Maximum"},
                                    {"id": "EnergyEfficientTurbo",
                                     "value": "Disabled"},
                                    {"id": "IntelUpiPowerManagement",
                                     "value": "Disabled"}]},
         "hideUnusedFlexNics": True,
         "iscsiInitiatorName": "",
         "osDeploymentSettings": None,
         "localStorage": {
             "sasLogicalJBODs": [],
             "controllers": []},
         "sanStorage": None,
         "initialScopeUris": []
         }]

SP_3 = [{"type": "ServerProfileV10",
         "serverHardwareUri": "SH:" + host_name,
         "serverHardwareTypeUri": "SHT:" + sht,
         "serialNumberType": "Physical",
         "iscsiInitiatorNameType": "AutoGenerated",
         "macType": "Physical",
         "wwnType": "Physical",
         "name": "SP_3",
         "description": "",
         "affinity": None,
         "connectionSettings": {
             "connections": []},
         "boot": {
             "manageBoot": False},
         "bootMode": {
             "manageMode": True,
             "mode": "BIOS",
             "secureBoot": "Unmanaged",
             "pxeBootPolicy": "Auto"},
         "firmware": {
             "manageFirmware": False,
             "firmwareBaselineUri": "",
             "forceInstallFirmware": False,
             "firmwareInstallType": None,
             "firmwareScheduleDateTime": "",
             "firmwareActivationType": "Immediate"},
         "bios": {
             "manageBios": True,
             "overriddenSettings": [{"id": "WorkloadProfile",
                                     "value": "MissionCritical"},
                                    {"id": "DynamicPowerCapping",
                                     "value": "Auto"},
                                    {"id": "UsbControl",
                                     "value": "UsbEnabled"},
                                    {"id": "AdvancedMemProtection",
                                     "value": "FastFaultTolerantADDDC"},
                                    {"id": "MemRefreshRate",
                                     "value": "Refreshx2"},
                                    {"id": "ConfigurationEnabled",
                                     "value": "Disabled"},
                                    {"id": "PowerRegulator",
                                     "value": "StaticHighPerf"},
                                    {"id": "CollabPowerControl",
                                     "value": "Disabled"},
                                    {"id": "NumaGroupSizeOpt",
                                     "value": "Clustered"},
                                    {"id": "UncoreFreqScaling",
                                     "value": "Maximum"},
                                    {"id": "EnergyEfficientTurbo",
                                     "value": "Disabled"},
                                    {"id": "IntelUpiPowerManagement",
                                     "value": "Disabled"}]},
         "hideUnusedFlexNics": True,
         "iscsiInitiatorName": "",
         "osDeploymentSettings": None,
         "localStorage": {
             "sasLogicalJBODs": [],
             "controllers": []},
         "sanStorage": None,
         "initialScopeUris": []
         }]

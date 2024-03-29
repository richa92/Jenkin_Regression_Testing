"""User Input to perform Integrated CDP test on rack server"""

rack_api_version = '1000'
rack_fusion_ip = '16.83.15.93'   # OneView IP Address
rack_admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}
rack_fusion_ssh_credentials = {'userName': 'root', 'password': 'hpvse1'}
rack_server_generation = "Gen10"   # Example1 "Gen9" #Example2 "Gen8"
rack_server_ip = '16.83.14.185'   # Example "16.83.13.200"
rack_server_ilo_hostname = 'ILO2135430985.lr.eml.lab'   # Example 'ILOCN7642000Y.lr.eml.lab'
rack_server_credentials_username = 'Administrator'  # Example 'Administrator' {'userName': 'Administrator', 'password': 'password'}
rack_server_credentials_password = 'password'  # Example 'password'
rack_server_hardware_type = 'DL120 Gen10 1'
rack_server_profile_type = 'ServerProfileV10'
rack_server_firmware = '/rest/firmware-drivers/SPPGen10Snap4_2018_1120_48'

"""User Input Section rack server Ends"""

"""User Input to perform Integrated CDP test on Blade server """

''' Note : Keep the TestServer in the Managed Mode before testing '''
bl_api_version = '1000'
bl_fusion_ip = '16.83.14.88'   # OneView IP Address
bl_fusion_admin_credentials_username = 'Administrator'   # Example 'Administrator' Administrator'{'userName': 'Administrator', 'password': 'hpvse123'}
bl_fusion_admin_credentials_password = 'hpvse123'
bl_fusion_ssh_credentials_username = 'root'   # example 'root' {'userName': 'root', 'password': 'hpvse1'}
bl_fusion_ssh_credentials_password = 'hpvse1'   # example 'hpvse1'
bl_eg_name = "EG1"   # Enclosure Group Name
bl_server_genration = "Gen10"   # Example1 "Gen9" # Example2 "Gen8"
bl_server_ip = '172.18.31.8'   # Example "16.83.13.200"
bl_server_ilo_hostname = 'Encl3, bay 6'   # Example 'USE146KPNS, bay 13'
bl_server_credentials_username = 'Administrator'  # Example 'Administrator' {'userName': 'Administrator', 'password': 'password'}
bl_server_credentials_password = 'password'   # Example 'password'
bl_server_hardware_type = 'BL460c Gen10 1'
bl_server_firmware = '/rest/firmware-drivers/SPPGen10Snap4_2018_1120_48'
bl_server_profile_type = 'ServerProfileV10'

"""User Input Section for blade server Ends"""

"""User Input to perform Integrated CDP test on Blade server"""

''' Note : Keep the TestServer in the Managed Mode before testing '''
syn_api_version = '1000'
syn_frame_ip = "16.83.15.219"  # Synergy Frame IP
syn_fusion_ip = syn_frame_ip   # Usually the Frame IP and Fusion IP will be same, if changed please change it here
syn_fusion_admin_credentials_username = 'Administrator'  # Example 'Administrator' Administrator'{'userName': 'Administrator', 'password': 'hpvse123'}
syn_fusion_admin_credentials_password = 'hpvse123'
syn_fusion_ssh_credentials_username = 'root'  # example 'root' {'userName': 'root', 'password': 'hpvse1'}
syn_fusion_ssh_credentials_password = 'hpvse1'  # example 'hpvse1'
syn_lig_name = "LIG1"  # Logical Interconnect Group Name
syn_eg_name = "EG1"  # Enclosure Group Name
syn_server_genration = "Gen10"  # Example1 "Gen9" #Example2 "Gen8" # Example3 "Gen10"
syn_server_ip = '16.83.15.2'  # Example "16.83.13.200"
syn_server_ilo_hostname = '0000A66101, bay 6'  # Example 'CN744502CH, bay 1'
syn_server_credentials_username = 'Administrator'  # Example 'Administrator' {'userName': 'Administrator', 'password': 'password'}
syn_server_credentials_password = 'password'  # Example 'password'
syn_server_firmware = "/rest/firmware-drivers/SPPGen10Snap4_2018_1018_39"
syn_server_hardware_type = 'SY 660 Gen10 1'
syn_server_profile_type = 'ServerProfileV10'

"""User Input Section for Synergy server Ends"""

rack_server_add = [
    {
        'name': rack_server_ilo_hostname,
        'hostname': rack_server_ip,
        'licensingIntent': 'OneViewNoiLO',
        'username': rack_server_credentials_username,
        'password': rack_server_credentials_password,
        'force': True,
        'configurationState': 'Managed'}]

Server_profile = [{
    "name": "Testing with Script",
    "description": "Testing with Script Description",
    "type": rack_server_profile_type,
    "serverHardwareUri": "SH:" + rack_server_ilo_hostname,
    "serverHardwareTypeUri": "SHT:" + rack_server_hardware_type,
    "iscsiInitiatorName": None,
    "iscsiInitiatorNameType": "AutoGenerated",
    "affinity": None,
    "associatedServer": None,
    "hideUnusedFlexNics": None,
    "firmware": None,
    "macType": "Physical",
    "wwnType": "Physical",
    "serialNumberType": "Physical",
    "category": "server-profiles",
    "status": "OK",
    "state": "Normal",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": True, "mode": "UEFIOptimized", "pxeBootPolicy": "Auto", "secureBoot": "Unmanaged"},
    "bios": {"manageBios": True, "overriddenSettings": []},
    "localStorage": None,
    "sanStorage": None,
    "osDeploymentSettings": None,
    "initialScopeUris": []}]

rack_Server_edit_profile = [{
    "name": "Testing with Script",
    "description": "Testing with Script Description",
    "type": rack_server_profile_type,
    "serverHardwareUri": "SH:" + rack_server_ilo_hostname,
    "serverHardwareTypeUri": "SHT:" + rack_server_hardware_type,
    "serialNumberType": "Physical",
    "iscsiInitiatorName": None,
    "iscsiInitiatorNameType": "AutoGenerated",
    "affinity": None,
    "associatedServer": None,
    "hideUnusedFlexNics": None,
    "firmware": None,
    "macType": "Physical",
    "wwnType": "Physical",
    "serialNumberType": "Physical",
    "category": "server-profiles",
    "status": "OK",
    "state": "Normal",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": True, "order": ["CD", "USB", "HardDisk", "PXE"]},
    "bootMode": {"manageMode": True, "mode": "BIOS", "pxeBootPolicy": None, "secureBoot": "Disabled"},
    "bios": {"manageBios": True, "overriddenSettings": [{"id": "AsrTimeoutMinutes", "value": "Timeout15"}]},
    "localStorage": None,
    "sanStorage": None,
    "osDeploymentSettings": None,
    "initialScopeUris": []}]

rack_Server_edit_profile_with_firmware = [{
    "name": "Testing with Script",
    "description": "Testing with Script Description",
    "type": rack_server_profile_type,
    "serverHardwareUri": "SH:" + rack_server_ilo_hostname,
    "serverHardwareTypeUri": "SHT:" + rack_server_hardware_type,
    "serialNumberType": "Physical",
    "iscsiInitiatorName": None,
    "iscsiInitiatorNameType": "AutoGenerated",
    "affinity": None,
    "associatedServer": None,
    "hideUnusedFlexNics": None,
    "firmware": {
        "manageFirmware": True,
        "forceInstallFirmware": False,
        "firmwareInstallType": "FirmwareOnlyOfflineMode",
        "firmwareBaselineUri": rack_server_firmware},
    "macType": "Physical",
    "wwnType": "Physical",
    "serialNumberType": "Physical",
    "category": "server-profiles",
    "status": "OK",
    "state": "Normal",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": True, "order": ["CD", "USB", "HardDisk", "PXE"]},
    "bootMode": {"manageMode": True, "mode": "BIOS", "pxeBootPolicy": None, "secureBoot": "Disabled"},
    "bios": {"manageBios": True, "overriddenSettings": [{"id": "AsrTimeoutMinutes", "value": "Timeout15"}]},
    "localStorage": None,
    "sanStorage": None,
    "osDeploymentSettings": None,
    "initialScopeUris": []}]

"""Configurations below can be changed as per the requirement of testing"""

bl_admin_credentials = {'userName': bl_fusion_admin_credentials_username, 'password': bl_fusion_admin_credentials_password}

bl_Server_profile = [{
    "name": "Testing with Script",
    "description": "Testing with Script Description",
    "type": bl_server_profile_type,
    "serverHardwareUri": "SH:" + bl_server_ilo_hostname,
    "serverHardwareTypeUri": "SHT:" + bl_server_hardware_type,
    "iscsiInitiatorName": None,
    "iscsiInitiatorNameType": "AutoGenerated",
    "associatedServer": None,
    "hideUnusedFlexNics": None,
    "firmware": None,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "category": "server-profiles",
    "status": "OK",
    "state": "Normal",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": True, "mode": "UEFIOptimized", "pxeBootPolicy": "Auto", "secureBoot": "Unmanaged"},
    "bios": {"manageBios": True, "overriddenSettings": []},
    "localStorage": None,
    "sanStorage": None,
    "osDeploymentSettings": None,
    "initialScopeUris": []}]

bl_Server_edit_profile = [{
    "name": "Testing with Script",
    "description": "Testing with Script Description",
    "type": bl_server_profile_type,
    "serverHardwareUri": "SH:" + bl_server_ilo_hostname,
    "serverHardwareTypeUri": "SHT:" + bl_server_hardware_type,
    "serialNumberType": "Physical",
    "iscsiInitiatorName": None,
    "iscsiInitiatorNameType": "AutoGenerated",
    "associatedServer": None,
    "hideUnusedFlexNics": None,
    "firmware": None,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "category": "server-profiles",
    "status": "OK",
    "state": "Normal",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": True, "order": ["CD", "USB", "HardDisk", "PXE"]},
    "bootMode": {"manageMode": True, "mode": "BIOS", "pxeBootPolicy": None, "secureBoot": "Disabled"},
    "bios": {"manageBios": True, "overriddenSettings": [{"id": "AsrTimeoutMinutes", "value": "Timeout15"}]},
    "localStorage": None,
    "sanStorage": None,
    "osDeploymentSettings": None,
    "initialScopeUris": []}]

bl_Server_edit_profile_with_firmware = [{
    "name": "Testing with Script",
    "description": "Testing with Script Description",
    "type": bl_server_profile_type,
    "serverHardwareUri": "SH:" + bl_server_ilo_hostname,
    "serverHardwareTypeUri": "SHT:" + bl_server_hardware_type,
    "iscsiInitiatorName": None,
    "iscsiInitiatorNameType": "AutoGenerated",
    "associatedServer": None,
    "hideUnusedFlexNics": None,
    "firmware": {
        "manageFirmware": True,
        "forceInstallFirmware": False,
        "firmwareInstallType": "FirmwareOnlyOfflineMode",
        "firmwareBaselineUri": bl_server_firmware},
    "serialNumberType": "Virtual",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "category": "server-profiles",
    "status": "OK",
    "state": "Normal",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": True, "mode": "UEFIOptimized", "pxeBootPolicy": "Auto", "secureBoot": "Unmanaged"},
    "bios": {"manageBios": True, "overriddenSettings": []},
    "localStorage": None,
    "sanStorage": None,
    "osDeploymentSettings": None,
    "initialScopeUris": []}]

"""Configurations below can be changed as per the requirement of testing"""

syn_admin_credentials = {'userName': syn_fusion_admin_credentials_username, 'password': syn_fusion_admin_credentials_password}

syn_Server_profile = [{
    "name": "Testing with Script",
    "description": "Testing with Script Description",
    "type": syn_server_profile_type,
    "serverHardwareUri": "SH:" + syn_server_ilo_hostname,
    "serverHardwareTypeUri": "SHT:" + syn_server_hardware_type,
    "iscsiInitiatorName": None,
    "iscsiInitiatorNameType": "AutoGenerated",
    "associatedServer": None,
    "hideUnusedFlexNics": None,
    "firmware": None,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "category": "server-profiles",
    "status": "OK",
    "state": "Normal",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": True, "mode": "UEFIOptimized", "pxeBootPolicy": "Auto", "secureBoot": "Unmanaged"},
    "bios": {"manageBios": True, "overriddenSettings": []},
    "localStorage": None,
    "sanStorage": None,
    "osDeploymentSettings": None,
    "initialScopeUris": []}]

syn_Server_edit_profile = [{
    "name": "Testing with Script",
    "description": "Testing with Script Description",
    "type": syn_server_profile_type,
    "serverHardwareUri": "SH:" + syn_server_ilo_hostname,
    "serverHardwareTypeUri": "SHT:" + syn_server_hardware_type,
    "iscsiInitiatorName": None,
    "iscsiInitiatorNameType": "AutoGenerated",
    "associatedServer": None,
    "hideUnusedFlexNics": None,
    "firmware": None,
    "serialNumberType": "Virtual",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "category": "server-profiles",
    "status": "OK",
    "state": "Normal",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": True, "order": ["CD", "USB", "HardDisk", "PXE"]},
    "bootMode": {"manageMode": True, "mode": "BIOS", "pxeBootPolicy": None, "secureBoot": "Disabled"},
    "bios": {"manageBios": True, "overriddenSettings": [{"id": "AsrTimeoutMinutes", "value": "Timeout15"}]},
    "localStorage": None,
    "sanStorage": None,
    "osDeploymentSettings": None,
    "initialScopeUris": []}]

syn_Server_edit_profile_with_firmware = [{
    "name": "Testing with Script",
    "description": "Testing with Script Description",
    "type": syn_server_profile_type,
    "serverHardwareUri": "SH:" + syn_server_ilo_hostname,
    "serverHardwareTypeUri": "SHT:" + syn_server_hardware_type,
    "iscsiInitiatorName": None,
    "iscsiInitiatorNameType": "AutoGenerated",
    "associatedServer": None,
    "hideUnusedFlexNics": None,
    "firmware": {
        "manageFirmware": True,
        "forceInstallFirmware": False,
        "firmwareInstallType": "FirmwareOnlyOfflineMode",
        "firmwareBaselineUri": syn_server_firmware},
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "category": "server-profiles",
    "status": "OK",
    "state": "Normal",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": True, "mode": "UEFIOptimized", "pxeBootPolicy": "Auto", "secureBoot": "Unmanaged"},
    "localStorage": None,
    "sanStorage": None,
    "osDeploymentSettings": None,
    "initialScopeUris": []}]

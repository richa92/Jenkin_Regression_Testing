"""User Input Section Begins for Rack Servers Only"""

rack_api_version = '1000'
rack_fusion_ip = '16.83.13.190'  # OneView IP Address
rack_fusion_admin_credentials_username = 'Administrator'  # Example 'Administrator'
rack_fusion_admin_credentials_password = 'hpvse123'
rack_fusion_ssh_credentials_username = 'root'  # example 'root'
rack_fusion_ssh_credentials_password = 'hpvse1'  # example 'hpvse1'
rack_server_genration = 'Gen10'  # Example1 "Gen9" #Example2 "Gen8"
rack_server_ip = '172.18.8.58'  # Example "172.18.31.1"
rack_server_ilo_hostname = '172.18.8.58'  # Example 'ILOCN7642000Y.lr.eml.lab' or '172.18.31.1'
rack_server_credentials_username = 'dcs'  # Example 'dcs'
rack_server_credentials_password = 'dcs'  # Example 'dcs'
rack_firmware_iso_uploaded_into_OneView = 'SPPGen10Snap4_2018_1016_38.iso'  # Example 'SPPGen10Snap4_2018_1016_38.iso'

"""User Input Section Ends here for Rack Servers"""

"""User Input Section Begins for Blade Servers Only"""

bl_api_version = '1000'
bl_fusion_ip = '16.83.13.190'  # OneView IP Address
bl_fusion_admin_credentials_username = 'Administrator'  # Example 'Administrator'
bl_fusion_admin_credentials_password = 'hpvse123'
bl_fusion_ssh_credentials_username = 'root'  # example 'root'
bl_fusion_ssh_credentials_password = 'hpvse1'  # example 'hpvse1'
bl_eg_name = 'Eg1'  # Enclosure Group Name - Example : 'EG1'
bl_server_genration = 'Gen10'  # Example1 "Gen9" #Example2 "Gen8"
bl_server_ip = '172.18.31.6'  # Example '172.18.31.1'
bl_server_ilo_hostname = '0000A66101, bay 1'  # Example 'USE146KPNS, bay 13' or '172.18.31.1'
bl_server_credentials_username = 'dcs'  # Example 'dcs'
bl_server_credentials_password = 'dcs'  # Example 'dcs'
bl_firmware_iso_uploaded_into_OneView = 'SPPGen10Snap4_2018_1016_38.iso'  # Example 'SPPGen10Snap4_2018_1016_38.iso'

"""User Input Section Ends here for Blade Servers"""

"""User Input Section Begins here for Synergy Servers"""

syn_api_version = '1000'
syn_fusion_ip = '16.83.13.196'  # OneView IP Address
syn_fusion_admin_credentials_username = 'Administrator'  # Example 'Administrator'
syn_fusion_admin_credentials_password = 'hpvse123'
syn_fusion_ssh_credentials_username = 'root'  # example 'root'
syn_fusion_ssh_credentials_password = 'hpvse1'  # example 'hpvse1'
syn_eg_name = 'Eg1'  # Enclosure Group Name - Example : 'EG1'
syn_server_genration = 'Gen10'  # Example1 "Gen9" #Example2 "Gen8"
syn_server_ip = '172.18.31.1'  # Example '172.18.31.1'
syn_server_ilo_hostname = '0000A66101, bay 2'  # Example 'CN744502CH, bay 1', '0000A66101, bay 2'
syn_server_credentials_username = 'dcs'  # Example 'dcs'
syn_server_credentials_password = 'dcs'  # Example 'dcs'
syn_firmware_iso_uploaded_into_OneView = 'SPPGen10Snap4_2018_1106_44.iso'  # Example 'SPPGen10Snap4_2018_1106_44.iso'

"""User Input Section Ends here for Synergy Servers"""

"""Configurations below for Rack Servers can be changed as per the requirement of testing"""

rack_admin_credentials = {'userName': rack_fusion_admin_credentials_username, 'password': rack_fusion_admin_credentials_password}

rack_server_add = [
    {
        'name': rack_server_ilo_hostname,
        'hostname': rack_server_ip,
        'licensingIntent': 'OneViewNoiLO',
        'username': rack_server_credentials_username,
        'password': rack_server_credentials_password,
        'force': True,
        'configurationState': 'Managed'}]

rack_server_hardware_type = 'server-hardware-10'
rack_server_profile_template_type = 'ServerProfileTemplateV6'
rack_server_profile_type = 'ServerProfileV10'

""" Generation 8 Rack Server configuration variables below"""

rack_gen8_spt_overridden_setting = [
    {
        "id": "InternalSDCardSlot",
        "value": "Disabled"}]

rack_gen8_create_sp_overridden_setting = [
    {
        "id": "InternalSDCardSlot",
        "value": "Enabled"}]

rack_gen8_edit_sp_overridden_setting = [
    {
        "id": "InternalSDCardSlot",
        "value": "Disabled"}]

rack_gen8_create_specific_bios_overridden_setting = [
    # The Specific bios attributes for testing
    # Virtualization 158,
    # Hyperthreading 176,
    # Turbo Boost performance 181,
    # VTd 186
    {
        "id": "ProcHyperthreading",
        "value": "Disabled"
    },
    {
        "id": "ProcVirtualization",
        "value": "Disabled"
    },
    {
        "id": "ProcX2Apic",
        "value": "Disabled"
    },
    {
        "id": "IntelProcVtd",
        "value": "Disabled"
    }  # ,
    # {
    #    "id": "EnergyEfficientTurbo",
    #    "value": "Disabled"
    # },
    # {
    #    "id": "ProcTurbo",
    #    "value": "Disabled"
    # }
]

rack_gen8_edit_specific_bios_overridden_setting = [
    # The Specific bios attributes for testing
    # Virtualization 158,
    # Hyperthreading 176,
    # Turbo Boost performance 181,
    # VTd 186
    {
        "id": "ProcHyperthreading",
        "value": "Enabled"
    },
    {
        "id": "ProcVirtualization",
        "value": "Enabled"
    },
    {
        "id": "ProcX2Apic",
        "value": "Enabled"
    },
    {
        "id": "IntelProcVtd",
        "value": "Enabled"
    }  # ,
    # {
    #    "id": "EnergyEfficientTurbo",
    #    "value": "Enabled"
    # },
    # {
    #    "id": "ProcTurbo",
    #    "value": "Enabled"
    # }
]

rack_gen8_profile_templates = [
    {
        "name": "RackGen8TemplateName",
        "type": rack_server_profile_template_type,
        "description": "RackGen8TemplateDescription",
        "serverProfileDescription": 'RackGen8ServerProfileDescription',
        "enclosureGroupUri": "",
        "serialNumberType": "Physical",
        "macType": "Physical",
        "wwnType": "Physical",
        "affinity": None,
        "connectionSettings": {"manageConnections": False},
        "bios": {"manageBios": True, "overriddenSettings": rack_gen8_spt_overridden_setting},
        "hideUnusedFlexNics": True,
        "iscsiInitiatorNameType": "AutoGenerated",
        "localStorage": None,
        "sanStorage": None,
        "osDeploymentSettings": None,
        "initialScopeUris": []}]

rack_gen8_server_profile_bios_only = {
    "serverHardwareUri": "SH:" + rack_server_ilo_hostname,
    "bios": {"manageBios": True, "overriddenSettings": rack_gen8_create_sp_overridden_setting}}

rack_gen8_server_profile_bootmode_and_bios = {
    "serverHardwareUri": "SH:" + rack_server_ilo_hostname,
    "boot": {"manageBoot": True, "order": ["CD", "USB", "HardDisk", "PXE"]},
    "bootMode": {"manageMode": True, "mode": "BIOS", "secureBoot": "Unmanaged"},
    "bios": {"manageBios": True, "overriddenSettings": rack_gen8_create_sp_overridden_setting}}

rack_gen8_server_profile_firmware_and_bios = {
    "serverHardwareUri": "SH:" + rack_server_ilo_hostname,
    "firmware": {
        "manageFirmware": True,
        "forceInstallFirmware": False,
        "firmwareInstallType": "FirmwareOnlyOfflineMode"},
    "bios": {"manageBios": True, "overriddenSettings": rack_gen8_create_sp_overridden_setting}}

rack_gen8_server_profile_create_specific_bios = {
    "serverHardwareUri": "SH:" + rack_server_ilo_hostname,
    "bios": {"manageBios": True, "overriddenSettings": rack_gen8_create_specific_bios_overridden_setting}}

rack_gen8_server_profile_edit_specific_bios = {
    "serverHardwareUri": "SH:" + rack_server_ilo_hostname,
    "bios": {"manageBios": True, "overriddenSettings": rack_gen8_edit_specific_bios_overridden_setting}}

rack_gen8_server_profile_with_template_and_bios = {
    "serverProfileTemplateUri": "SPT:RackGen8TemplateName",
    "serverHardwareUri": "SH:" + rack_server_ilo_hostname,
    "bios": {"manageBios": True, "overriddenSettings": rack_gen8_create_sp_overridden_setting}}

rack_gen8_server_profile_unassign = {
    "serverProfileTemplateUri": "SPT:RackGen8TemplateName",
    "bios": {"manageBios": True, "overriddenSettings": rack_gen8_spt_overridden_setting}}

rack_gen8_server_profile_assign = {
    "serverProfileTemplateUri": "SPT:RackGen8TemplateName",
    "serverHardwareUri": "SH:" + rack_server_ilo_hostname,
    "bios": {"manageBios": True, "overriddenSettings": rack_gen8_spt_overridden_setting}}

rack_gen8_server_profile_unassign_defbios = {
    "serverProfileTemplateUri": "SPT:RackGen8TemplateName",
    "bios": {"manageBios": True, "overriddenSettings": []}}

rack_gen8_server_profile_assign_defbios = {
    "serverProfileTemplateUri": "SPT:RackGen8TemplateName",
    "serverHardwareUri": "SH:" + rack_server_ilo_hostname,
    "bios": {"manageBios": True, "overriddenSettings": []}}

rack_gen8_server_profile_edit_assign_defbios = {
    "serverProfileTemplateUri": "SPT:RackGen8TemplateName",
    "serverHardwareUri": "SH:" + rack_server_ilo_hostname,
    "bios": {"manageBios": True, "overriddenSettings": []}}

rack_gen8_server_profile_edit_bios_only = {
    "description": "RackGen8ServerProfileDescription edited",
    "serverHardwareUri": "SH:" + rack_server_ilo_hostname,
    "bios": {"manageBios": True, "overriddenSettings": rack_gen8_edit_sp_overridden_setting}}

rack_gen8_server_profiles = [
    {
        "name": "RackGen8ServerProfileName",
        "description": "RackGen8ServerProfileDescription",
        "type": rack_server_profile_type,
        "serialNumberType": "Physical",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Physical",
        "wwnType": "Physical",
        "affinity": None,
        "hideUnusedFlexNics": None,
        "osDeploymentSettings": None,
        "localStorage": None,
        "sanStorage": None,
        "initialScopeUris": []}]

""" Generation 9 Rack Server configuration variables below"""

rack_gen9_spt_overridden_setting = [
    {
        "id": "InternalSDCardSlot",
        "value": "Disabled"}]

rack_gen9_create_sp_overridden_setting = [
    {
        "id": "InternalSDCardSlot",
        "value": "Enabled"}]

rack_gen9_edit_sp_overridden_setting = [
    {
        "id": "InternalSDCardSlot",
        "value": "Disabled"}]

rack_gen9_create_specific_bios_overridden_setting = [
    # The Specific bios attributes for testing
    # Virtualization 158,
    # Hyperthreading 176,
    # Turbo Boost performance 181,
    # VTd 186
    {
        "id": "ProcHyperthreading",
        "value": "Disabled"
    },
    {
        "id": "ProcVirtualization",
        "value": "Disabled"
    },
    {
        "id": "ProcX2Apic",
        "value": "Disabled"
    },
    {
        "id": "IntelProcVtd",
        "value": "Disabled"
    }  # ,
    # {
    #    "id": "EnergyEfficientTurbo",
    #    "value": "Disabled"
    # },
    # {
    #    "id": "ProcTurbo",
    #    "value": "Disabled"
    # }  # Few servers doesn't support Turbo Boost hence few lines of code are commented, if server is supporting Turbo Boost, then the below can be enabled.
]

rack_gen9_edit_specific_bios_overridden_setting = [
    # The Specific bios attributes for testing
    # Virtualization 158,
    # Hyperthreading 176,
    # Turbo Boost performance 181,
    # VTd 186
    {
        "id": "ProcHyperthreading",
        "value": "Enabled"
    },
    {
        "id": "ProcVirtualization",
        "value": "Enabled"
    },
    {
        "id": "ProcX2Apic",
        "value": "Enabled"
    },
    {
        "id": "IntelProcVtd",
        "value": "Enabled"
    }  # ,
    # {
    #    "id": "EnergyEfficientTurbo",
    #    "value": "Enabled"
    # },
    # {
    #    "id": "ProcTurbo",
    #    "value": "Enabled"
    # }  # Few servers doesn't support Turbo Boost hence few lines of code are commented, if server is supporting Turbo Boost, then the below can be enabled.
]

rack_gen9_profile_templates = [
    {
        "name": "RackGen9TemplateName",
        "type": rack_server_profile_template_type,
        "description": "RackGen9TemplateDescription",
        "serverProfileDescription": 'RackGen9ServerProfileDescription',
        "enclosureGroupUri": "",
        "serialNumberType": "Physical",
        "macType": "Physical",
        "wwnType": "Physical",
        "affinity": None,
        "connectionSettings": {"manageConnections": False},
        "bios": {"manageBios": True, "overriddenSettings": rack_gen9_spt_overridden_setting},
        "hideUnusedFlexNics": True,
        "iscsiInitiatorNameType": "AutoGenerated",
        "localStorage": None,
        "sanStorage": None,
        "osDeploymentSettings": None,
        "initialScopeUris": []}]

rack_gen9_server_profile_bios_only = {
    "serverHardwareUri": "SH:" + rack_server_ilo_hostname,
    "bios": {"manageBios": True, "overriddenSettings": rack_gen9_create_sp_overridden_setting}}

rack_gen9_server_profile_bootmode_and_bios = {
    "serverHardwareUri": "SH:" + rack_server_ilo_hostname,
    "boot": {"manageBoot": True, "order": ["CD", "USB", "HardDisk", "PXE"]},
    "bootMode": {"manageMode": True, "mode": "BIOS", "secureBoot": "Unmanaged"},
    "bios": {"manageBios": True, "overriddenSettings": rack_gen9_create_sp_overridden_setting}}

rack_gen9_server_profile_firmware_and_bios = {
    "serverHardwareUri": "SH:" + rack_server_ilo_hostname,
    "firmware": {
        "manageFirmware": True,
        "forceInstallFirmware": False,
        "firmwareInstallType": "FirmwareOnlyOfflineMode"},
    "bios": {"manageBios": True, "overriddenSettings": rack_gen9_create_sp_overridden_setting}}

rack_gen9_server_profile_create_specific_bios = {
    "serverHardwareUri": "SH:" + rack_server_ilo_hostname,
    "bios": {"manageBios": True, "overriddenSettings": rack_gen9_create_specific_bios_overridden_setting}}

rack_gen9_server_profile_edit_specific_bios = {
    "serverHardwareUri": "SH:" + rack_server_ilo_hostname,
    "bios": {"manageBios": True, "overriddenSettings": rack_gen9_edit_specific_bios_overridden_setting}}

rack_gen9_server_profile_with_template_and_bios = {
    "serverProfileTemplateUri": "SPT:RackGen9TemplateName",
    "serverHardwareUri": "SH:" + rack_server_ilo_hostname,
    "bios": {"manageBios": True, "overriddenSettings": rack_gen9_create_sp_overridden_setting}}

rack_gen9_server_profile_unassign = {
    "serverProfileTemplateUri": "SPT:RackGen9TemplateName",
    "bios": {"manageBios": True, "overriddenSettings": rack_gen9_spt_overridden_setting}}

rack_gen9_server_profile_assign = {
    "serverProfileTemplateUri": "SPT:RackGen9TemplateName",
    "serverHardwareUri": "SH:" + rack_server_ilo_hostname,
    "bios": {"manageBios": True, "overriddenSettings": rack_gen9_spt_overridden_setting}}

rack_gen9_server_profile_unassign_defbios = {
    "serverProfileTemplateUri": "SPT:RackGen9TemplateName",
    "bios": {"manageBios": True, "overriddenSettings": []}}

rack_gen9_server_profile_assign_defbios = {
    "serverProfileTemplateUri": "SPT:RackGen9TemplateName",
    "serverHardwareUri": "SH:" + rack_server_ilo_hostname,
    "bios": {"manageBios": True, "overriddenSettings": []}}

rack_gen9_server_profile_edit_assign_defbios = {
    "serverProfileTemplateUri": "SPT:RackGen9TemplateName",
    "serverHardwareUri": "SH:" + rack_server_ilo_hostname,
    "bios": {"manageBios": True, "overriddenSettings": []}}

rack_gen9_server_profile_edit_bios_only = {
    "description": "RackGen9ServerProfileDescription edited",
    "serverHardwareUri": "SH:" + rack_server_ilo_hostname,
    "bios": {"manageBios": True, "overriddenSettings": rack_gen9_edit_sp_overridden_setting}}

rack_gen9_server_profiles = [
    {
        "name": "RackGen9ServerProfileName",
        "description": "RackGen9ServerProfileDescription",
        "type": rack_server_profile_type,
        "serialNumberType": "Physical",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Physical",
        "wwnType": "Physical",
        "affinity": None,
        "hideUnusedFlexNics": None,
        "osDeploymentSettings": None,
        "localStorage": None,
        "sanStorage": None,
        "initialScopeUris": []}]

""" Generation 10 Rack Server configuration variables below"""

rack_gen10_spt_overridden_setting = [
    {
        "id": "InternalSDCardSlot",
        "value": "Disabled"}]
rack_gen10_create_sp_overridden_setting = [
    {
        "id": "InternalSDCardSlot",
        "value": "Enabled"}]

rack_gen10_edit_sp_overridden_setting = [
    {
        "id": "InternalSDCardSlot",
        "value": "Disabled"}]

rack_gen10_create_specific_bios_overridden_setting = [
    # The Specific bios attributes for testing
    # Virtualization 158,
    # Hyperthreading 176,
    # Turbo Boost performance 181,
    # VTd 186
    {
        "id": "ProcHyperthreading",
        "value": "Disabled"
    },
    {
        "id": "ProcVirtualization",
        "value": "Disabled"
    },
    {
        "id": "ProcX2Apic",
        "value": "Disabled"
    },
    {
        "id": "IntelProcVtd",
        "value": "Disabled"
    }  # ,
    # {
    #    "id": "EnergyEfficientTurbo",
    #    "value": "Disabled"
    # },
    # {
    #    "id": "ProcTurbo",
    #    "value": "Disabled"
    # }  # Few servers doesn't support Turbo Boost hence few lines of code are commented, if server is supporting Turbo Boost, then the below can be enabled.
]

rack_gen10_edit_specific_bios_overridden_setting = [
    # The Specific bios attributes for testing
    # Virtualization 158,
    # Hyperthreading 176,
    # Turbo Boost performance 181,
    # VTd 186
    {
        "id": "ProcHyperthreading",
        "value": "Enabled"
    },
    {
        "id": "ProcVirtualization",
        "value": "Enabled"
    },
    {
        "id": "ProcX2Apic",
        "value": "Enabled"
    },
    {
        "id": "IntelProcVtd",
        "value": "Enabled"
    }  # ,
    # {
    #    "id": "EnergyEfficientTurbo",
    #    "value": "Enabled"
    # },
    # {
    #    "id": "ProcTurbo",
    #    "value": "Enabled"
    # }  # Few servers doesn't support Turbo Boost hence few lines of code are commented, if server is supporting Turbo Boost, then the below can be enabled.
]

rack_gen10_profile_templates = [
    {
        "name": "RackGen10TemplateName",
        "type": rack_server_profile_template_type,
        "description": "RackGen10TemplateDescription",
        "serverProfileDescription": 'RackGen10ServerProfileDescription',
        "enclosureGroupUri": "",
        "serialNumberType": "Physical",
        "macType": "Physical",
        "wwnType": "Physical",
        "affinity": None,
        "connectionSettings": {"manageConnections": False},
        "bios": {"manageBios": True, "overriddenSettings": rack_gen10_spt_overridden_setting},
        "hideUnusedFlexNics": True,
        "iscsiInitiatorNameType": "AutoGenerated",
        "localStorage": None,
        "sanStorage": None,
        "osDeploymentSettings": None,
        "initialScopeUris": []}]

rack_gen10_server_profile_bios_only = {
    "serverHardwareUri": "SH:" + rack_server_ilo_hostname,
    "bios": {"manageBios": True, "overriddenSettings": rack_gen10_create_sp_overridden_setting}}

rack_gen10_server_profile_bootmode_and_bios = {
    "serverHardwareUri": "SH:" + rack_server_ilo_hostname,
    "boot": {"manageBoot": True, "order": ["CD", "USB", "HardDisk", "PXE"]},
    "bootMode": {"manageMode": True, "mode": "BIOS", "secureBoot": "Unmanaged"},
    "bios": {"manageBios": True, "overriddenSettings": rack_gen10_create_sp_overridden_setting}}

rack_gen10_server_profile_firmware_and_bios = {
    "serverHardwareUri": "SH:" + rack_server_ilo_hostname,
    "firmware": {
        "manageFirmware": True,
        "forceInstallFirmware": False,
        "firmwareInstallType": "FirmwareOnlyOfflineMode"},
    "bios": {"manageBios": True, "overriddenSettings": rack_gen10_create_sp_overridden_setting}}

rack_gen10_server_profile_create_specific_bios = {
    "serverHardwareUri": "SH:" + rack_server_ilo_hostname,
    "bios": {"manageBios": True, "overriddenSettings": rack_gen10_create_specific_bios_overridden_setting}}

rack_gen10_server_profile_edit_specific_bios = {
    "serverHardwareUri": "SH:" + rack_server_ilo_hostname,
    "bios": {"manageBios": True, "overriddenSettings": rack_gen10_edit_specific_bios_overridden_setting}}

rack_gen10_server_profile_with_template_and_bios = {
    "serverProfileTemplateUri": "SPT:RackGen10TemplateName",
    "serverHardwareUri": "SH:" + rack_server_ilo_hostname,
    "bios": {"manageBios": True, "overriddenSettings": rack_gen10_create_sp_overridden_setting}}

rack_gen10_server_profile_unassign = {
    "serverProfileTemplateUri": "SPT:RackGen10TemplateName",
    "bios": {"manageBios": True, "overriddenSettings": rack_gen10_spt_overridden_setting}}

rack_gen10_server_profile_assign = {
    "serverProfileTemplateUri": "SPT:RackGen10TemplateName",
    "serverHardwareUri": "SH:" + rack_server_ilo_hostname,
    "bios": {"manageBios": True, "overriddenSettings": rack_gen10_spt_overridden_setting}}

rack_gen10_server_profile_unassign_defbios = {
    "serverProfileTemplateUri": "SPT:RackGen10TemplateName",
    "bios": {"manageBios": True, "overriddenSettings": []}}

rack_gen10_server_profile_assign_defbios = {
    "serverProfileTemplateUri": "SPT:RackGen10TemplateName",
    "serverHardwareUri": "SH:" + rack_server_ilo_hostname,
    "bios": {"manageBios": True, "overriddenSettings": []}}

rack_gen10_server_profile_edit_assign_defbios = {
    "serverProfileTemplateUri": "SPT:RackGen10TemplateName",
    "serverHardwareUri": "SH:" + rack_server_ilo_hostname,
    "bios": {"manageBios": True, "overriddenSettings": []}}

rack_gen10_server_profile_edit_bios_only = {
    "description": "RackGen10ServerProfileDescription edited",
    "serverHardwareUri": "SH:" + rack_server_ilo_hostname,
    "bios": {"manageBios": True, "overriddenSettings": rack_gen10_edit_sp_overridden_setting}}

rack_gen10_server_profiles = [
    {
        "name": "RackGen10ServerProfileName",
        "description": "RackGen10ServerProfileDescription",
        "type": rack_server_profile_type,
        "serialNumberType": "Physical",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Physical",
        "wwnType": "Physical",
        "affinity": None,
        "hideUnusedFlexNics": None,
        "osDeploymentSettings": None,
        "localStorage": None,
        "sanStorage": None,
        "initialScopeUris": []}]

''' Rack Servers Section Ends here  '''

"""Configurations below for Blade Servers can be changed as per the requirement of testing"""

''' Note : Keep the TestServer in the Managed Mode before testing '''

bl_admin_credentials = {'userName': bl_fusion_admin_credentials_username, 'password': bl_fusion_admin_credentials_password}

bl_server_hardware_type = 'server-hardware-10'
bl_server_profile_template_type = 'ServerProfileTemplateV6'
bl_server_profile_type = 'ServerProfileV10'

""" Generation 8 Blade Server configuration variables below"""

bl_gen8_spt_overridden_setting = [
    {
        "id": "InternalSDCardSlot",
        "value": "Disabled"}]

bl_gen8_create_sp_overridden_setting = [
    {
        "id": "InternalSDCardSlot",
        "value": "Enabled"}]

bl_gen8_edit_sp_overridden_setting = [
    {
        "id": "InternalSDCardSlot",
        "value": "Disabled"}]

bl_gen8_create_specific_bios_overridden_setting = [
    # The Specific bios attributes for testing
    # Virtualization 158,
    # Hyperthreading 176,
    # Turbo Boost performance 181,
    # VTd 186
    {
        "id": "ProcHyperthreading",
        "value": "Disabled"
    },
    {
        "id": "ProcVirtualization",
        "value": "Disabled"
    },
    {
        "id": "ProcX2Apic",
        "value": "Disabled"
    },
    {
        "id": "IntelProcVtd",
        "value": "Disabled"
    }  # ,
    # {
    #    "id": "EnergyEfficientTurbo",
    #    "value": "Disabled"
    # },
    # {
    #    "id": "ProcTurbo",
    #    "value": "Disabled"
    # }  # Few servers doesn't support Turbo Boost hence few lines of code are commented, if server is supporting Turbo Boost, then the below can be enabled.
]

bl_gen8_edit_specific_bios_overridden_setting = [
    # The Specific bios attributes for testing
    # Virtualization 158,
    # Hyperthreading 176,
    # Turbo Boost performance 181,
    # VTd 186
    {
        "id": "ProcHyperthreading",
        "value": "Enabled"
    },
    {
        "id": "ProcVirtualization",
        "value": "Enabled"
    },
    {
        "id": "ProcX2Apic",
        "value": "Enabled"
    },
    {
        "id": "IntelProcVtd",
        "value": "Enabled"
    }  # ,
    # {
    #    "id": "EnergyEfficientTurbo",
    #    "value": "Enabled"
    # },
    # {
    #    "id": "ProcTurbo",
    #    "value": "Enabled"
    # }  # Few servers doesn't support Turbo Boost hence few lines of code are commented, if server is supporting Turbo Boost, then the below can be enabled.
]

bl_gen8_profile_templates = [
    {
        "name": "BladeGen8TemplateName",
        "type": bl_server_profile_template_type,
        "description": "BladeGen8TemplateDescription",
        "serverProfileDescription": "BladeGen8ServerProfileDescription",
        "enclosureGroupUri": 'EG:' + bl_eg_name,
        "serialNumberType": "Virtual",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "affinity": "Bay",
        "connectionSettings": {"connections": [], "manageConnections": False},
        "bios": {"manageBios": True, "overriddenSettings": bl_gen8_spt_overridden_setting},
        "hideUnusedFlexNics": True,
        "iscsiInitiatorNameType": "AutoGenerated",
        "localStorage": None,
        "sanStorage": None,
        "osDeploymentSettings": None,
        "initialScopeUris": []}]

bl_gen8_server_profile_bios_only = {
    "serverHardwareUri": "SH:" + bl_server_ilo_hostname,
    "bios": {"manageBios": True, "overriddenSettings": bl_gen8_create_sp_overridden_setting}}

bl_gen8_server_profile_bootmode_and_bios = {
    "serverHardwareUri": "SH:" + bl_server_ilo_hostname,
    "boot": {"manageBoot": True, "order": ["CD", "USB", "HardDisk", "PXE"]},
    "bootMode": {"manageMode": True, "mode": "BIOS", "secureBoot": "Unmanaged"},
    "bios": {"manageBios": True, "overriddenSettings": bl_gen8_create_sp_overridden_setting}}

bl_gen8_server_profile_connection_and_bios = {
    "serverHardwareUri": "SH:" + bl_server_ilo_hostname,
    "connectionSettings": {"connections": []},
    "bios": {"manageBios": True, "overriddenSettings": bl_gen8_create_sp_overridden_setting}}

bl_gen8_server_profile_firmware_and_bios = {
    "serverHardwareUri": "SH:" + bl_server_ilo_hostname,
    "firmware": {
        "manageFirmware": True,
        "forceInstallFirmware": False,
        "firmwareInstallType": "FirmwareOnlyOfflineMode"},
    "bios": {"manageBios": True, "overriddenSettings": bl_gen8_create_sp_overridden_setting}}

bl_gen8_server_profile_with_template_and_bios = {
    "serverHardwareUri": "SH:" + bl_server_ilo_hostname,
    "serverProfileTemplateUri": "SPT:BladeGen8TemplateName",
    "bios": {"manageBios": True, "overriddenSettings": bl_gen8_create_sp_overridden_setting}}

bl_gen8_server_profile_create_specific_bios = {
    "serverHardwareUri": "SH:" + bl_server_ilo_hostname,
    "bios": {"manageBios": True, "overriddenSettings": bl_gen8_create_specific_bios_overridden_setting}}

bl_gen8_server_profile_edit_specific_bios = {
    "serverHardwareUri": "SH:" + bl_server_ilo_hostname,
    "bios": {"manageBios": True, "overriddenSettings": bl_gen8_edit_specific_bios_overridden_setting}}

bl_gen8_server_profile_with_template_and_bios = {
    "serverHardwareUri": "SH:" + bl_server_ilo_hostname,
    "serverProfileTemplateUri": "SPT:BladeGen8TemplateName",
    "bios": {"manageBios": True, "overriddenSettings": bl_gen8_create_sp_overridden_setting}}

bl_gen8_server_profile_unassign = {
    "serverProfileTemplateUri": "SPT:BladeGen8TemplateName",
    "bios": {"manageBios": True, "overriddenSettings": bl_gen8_spt_overridden_setting}}

bl_gen8_server_profile_assign = {
    "serverHardwareUri": "SH:" + bl_server_ilo_hostname,
    "serverProfileTemplateUri": "SPT:BladeGen8TemplateName",
    "bios": {"manageBios": True, "overriddenSettings": bl_gen8_spt_overridden_setting}}

bl_gen8_server_profile_unassign_defbios = {
    "serverProfileTemplateUri": "SPT:BladeGen8TemplateName",
    "bios": {"manageBios": True, "overriddenSettings": []}}

bl_gen8_server_profile_assign_defbios = {
    "serverProfileTemplateUri": "SPT:BladeGen8TemplateName",
    "serverHardwareUri": "SH:" + bl_server_ilo_hostname,
    "bios": {"manageBios": True, "overriddenSettings": []}}

bl_gen8_server_profile_edit_assign_defbios = {
    "serverProfileTemplateUri": "SPT:BladeGen8TemplateName",
    "serverHardwareUri": "SH:" + bl_server_ilo_hostname,
    "bios": {"manageBios": True, "overriddenSettings": []}}

bl_gen8_server_profile_edit_assigned_bios_only = {
    "serverHardwareUri": "SH:" + bl_server_ilo_hostname,
    "description": "BladeGen8ServerProfileDescription edited",
    "bios": {"manageBios": True, "overriddenSettings": bl_gen8_edit_sp_overridden_setting}}

bl_gen8_server_profiles = [
    {
        "name": "BLGen8ServerProfileName",
        "description": "BladeGen8ServerProfileDescription",
        "type": bl_server_profile_type,
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "affinity": "Bay",
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "localStorage": None,
        "sanStorage": None,
        "initialScopeUris": []}]

""" Generation 9 Blade Server configuration variables below"""

bl_gen9_spt_overridden_setting = [
    {
        "id": "InternalSDCardSlot",
        "value": "Disabled"}]

bl_gen9_create_sp_overridden_setting = [
    {
        "id": "InternalSDCardSlot",
        "value": "Enabled"}]

bl_gen9_edit_sp_overridden_setting = [
    {
        "id": "InternalSDCardSlot",
        "value": "Disabled"}]

bl_gen9_create_specific_bios_overridden_setting = [
    # The Specific bios attributes for testing
    # Virtualization 158,
    # Hyperthreading 176,
    # Turbo Boost performance 181,
    # VTd 186
    {
        "id": "ProcHyperthreading",
        "value": "Disabled"
    },
    {
        "id": "ProcVirtualization",
        "value": "Disabled"
    },
    {
        "id": "ProcX2Apic",
        "value": "Disabled"
    },
    {
        "id": "IntelProcVtd",
        "value": "Disabled"
    }  # ,
    # {
    #    "id": "EnergyEfficientTurbo",
    #    "value": "Disabled"
    # },
    # {
    #    "id": "ProcTurbo",
    #    "value": "Disabled"
    # }  # Few servers doesn't support Turbo Boost hence few lines of code are commented, if server is supporting Turbo Boost, then the below can be enabled.
]

bl_gen9_edit_specific_bios_overridden_setting = [
    # The Specific bios attributes for testing
    # Virtualization 158,
    # Hyperthreading 176,
    # Turbo Boost performance 181,
    # VTd 186
    {
        "id": "ProcHyperthreading",
        "value": "Enabled"
    },
    {
        "id": "ProcVirtualization",
        "value": "Enabled"
    },
    {
        "id": "ProcX2Apic",
        "value": "Enabled"
    },
    {
        "id": "IntelProcVtd",
        "value": "Enabled"
    }  # ,
    # {
    #    "id": "EnergyEfficientTurbo",
    #    "value": "Enabled"
    # },
    # {
    #    "id": "ProcTurbo",
    #    "value": "Enabled"
    # }  # Few servers doesn't support Turbo Boost hence few lines of code are commented, if server is supporting Turbo Boost, then the below can be enabled.
]

bl_gen9_profile_templates = [
    {
        "name": "BladeGen9TemplateName",
        "type": bl_server_profile_template_type,
        "description": "BladeGen9TemplateDescription",
        "serverProfileDescription": "BladeGen9ServerProfileDescription",
        "enclosureGroupUri": 'EG:' + bl_eg_name,
        "serialNumberType": "Virtual",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "affinity": "Bay",
        "connectionSettings": {"connections": [], "manageConnections": False},
        "bios": {"manageBios": True, "overriddenSettings": bl_gen9_spt_overridden_setting},
        "hideUnusedFlexNics": True,
        "iscsiInitiatorNameType": "AutoGenerated",
        "localStorage": None,
        "sanStorage": None,
        "osDeploymentSettings": None,
        "initialScopeUris": []}]

bl_gen9_server_profile_bios_only = {
    "serverHardwareUri": "SH:" + bl_server_ilo_hostname,
    "bios": {"manageBios": True, "overriddenSettings": bl_gen9_create_sp_overridden_setting}}

bl_gen9_server_profile_bootmode_and_bios = {
    "serverHardwareUri": "SH:" + bl_server_ilo_hostname,
    "boot": {"manageBoot": True, "order": ["CD", "USB", "HardDisk", "PXE"]},
    "bootMode": {"manageMode": True, "mode": "BIOS", "secureBoot": "Unmanaged"},
    "bios": {"manageBios": True, "overriddenSettings": bl_gen9_create_sp_overridden_setting}}

bl_gen9_server_profile_connection_and_bios = {
    "serverHardwareUri": "SH:" + bl_server_ilo_hostname,
    "connectionSettings": {"connections": []},
    "bios": {"manageBios": True, "overriddenSettings": bl_gen9_create_sp_overridden_setting}}

bl_gen9_server_profile_firmware_and_bios = {
    "serverHardwareUri": "SH:" + bl_server_ilo_hostname,
    "firmware": {
        "manageFirmware": True,
        "forceInstallFirmware": False,
        "firmwareInstallType": "FirmwareOnlyOfflineMode"},
    "bios": {"manageBios": True, "overriddenSettings": bl_gen9_create_sp_overridden_setting}}

bl_gen9_server_profile_with_template_and_bios = {
    "serverHardwareUri": "SH:" + bl_server_ilo_hostname,
    "serverProfileTemplateUri": "SPT:BladeGen9TemplateName",
    "bios": {"manageBios": True, "overriddenSettings": bl_gen9_create_sp_overridden_setting}}

bl_gen9_server_profile_create_specific_bios = {
    "serverHardwareUri": "SH:" + bl_server_ilo_hostname,
    "bios": {"manageBios": True, "overriddenSettings": bl_gen9_create_specific_bios_overridden_setting}}

bl_gen9_server_profile_edit_specific_bios = {
    "serverHardwareUri": "SH:" + bl_server_ilo_hostname,
    "bios": {"manageBios": True, "overriddenSettings": bl_gen9_edit_specific_bios_overridden_setting}}

bl_gen9_server_profile_with_template_and_bios = {
    "serverHardwareUri": "SH:" + bl_server_ilo_hostname,
    "serverProfileTemplateUri": "SPT:BladeGen9TemplateName",
    "bios": {"manageBios": True, "overriddenSettings": bl_gen9_create_sp_overridden_setting}}

bl_gen9_server_profile_unassign = {
    "serverProfileTemplateUri": "SPT:BladeGen9TemplateName",
    "bios": {"manageBios": True, "overriddenSettings": bl_gen9_spt_overridden_setting}}

bl_gen9_server_profile_assign = {
    "serverHardwareUri": "SH:" + bl_server_ilo_hostname,
    "serverProfileTemplateUri": "SPT:BladeGen9TemplateName",
    "bios": {"manageBios": True, "overriddenSettings": bl_gen9_spt_overridden_setting}}

bl_gen9_server_profile_unassign_defbios = {
    "serverProfileTemplateUri": "SPT:BladeGen9TemplateName",
    "bios": {"manageBios": True, "overriddenSettings": []}}

bl_gen9_server_profile_assign_defbios = {
    "serverProfileTemplateUri": "SPT:BladeGen9TemplateName",
    "serverHardwareUri": "SH:" + bl_server_ilo_hostname,
    "bios": {"manageBios": True, "overriddenSettings": []}}

bl_gen9_server_profile_edit_assign_defbios = {
    "serverProfileTemplateUri": "SPT:BladeGen9TemplateName",
    "serverHardwareUri": "SH:" + bl_server_ilo_hostname,
    "bios": {"manageBios": True, "overriddenSettings": []}}

bl_gen9_server_profile_edit_bios_only = {
    "serverHardwareUri": "SH:" + bl_server_ilo_hostname,
    "description": "BladeGen9ServerProfileDescription edited",
    "bios": {"manageBios": True, "overriddenSettings": bl_gen9_edit_sp_overridden_setting}}

bl_gen9_server_profiles = [
    {
        "name": "BLGen9ServerProfileName",
        "description": "BladeGen9ServerProfileDescription",
        "type": bl_server_profile_type,
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "affinity": "Bay",
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "localStorage": None,
        "sanStorage": None,
        "initialScopeUris": []}]

""" Generation 10 Blade Server configuration variables below"""

bl_gen10_spt_overridden_setting = [
    {
        "id": "InternalSDCardSlot",
        "value": "Disabled"}]

bl_gen10_create_sp_overridden_setting = [
    {
        "id": "InternalSDCardSlot",
        "value": "Enabled"}]

bl_gen10_edit_sp_overridden_setting = [
    {
        "id": "InternalSDCardSlot",
        "value": "Disabled"}]

bl_gen10_create_specific_bios_overridden_setting = [
    # The Specific bios attributes for testing
    # Virtualization 158,
    # Hyperthreading 176,
    # Turbo Boost performance 181,
    # VTd 186
    {
        "id": "ProcHyperthreading",
        "value": "Disabled"
    },
    {
        "id": "ProcVirtualization",
        "value": "Disabled"
    },
    {
        "id": "ProcX2Apic",
        "value": "Disabled"
    },
    {
        "id": "IntelProcVtd",
        "value": "Disabled"
    }  # ,
    # {
    #    "id": "EnergyEfficientTurbo",
    #    "value": "Disabled"
    # },
    # {
    #    "id": "ProcTurbo",
    #    "value": "Disabled"
    # }  # Few servers doesn't support Turbo Boost hence few lines of code are commented, if server is supporting Turbo Boost, then the below can be enabled.
]

bl_gen10_edit_specific_bios_overridden_setting = [
    # The Specific bios attributes for testing
    # Virtualization 158,
    # Hyperthreading 176,
    # Turbo Boost performance 181,
    # VTd 186
    {
        "id": "ProcHyperthreading",
        "value": "Enabled"
    },
    {
        "id": "ProcVirtualization",
        "value": "Enabled"
    },
    {
        "id": "ProcX2Apic",
        "value": "Enabled"
    },
    {
        "id": "IntelProcVtd",
        "value": "Enabled"
    }  # ,
    # {
    #    "id": "EnergyEfficientTurbo",
    #    "value": "Enabled"
    # },
    # {
    #    "id": "ProcTurbo",
    #    "value": "Enabled"
    # }  # Few servers doesn't support Turbo Boost hence few lines of code are commented, if server is supporting Turbo Boost, then the below can be enabled.
]

bl_gen10_profile_templates = [
    {
        "name": "BladeGen10TemplateName",
        "type": bl_server_profile_template_type,
        "description": "BladeGen10TemplateDescription",
        "serverProfileDescription": "BladeGen10ServerProfileDescription",
        "enclosureGroupUri": 'EG:' + bl_eg_name,
        "serialNumberType": "Virtual",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "affinity": "Bay",
        "connectionSettings": {"connections": [], "manageConnections": False},
        "bios": {"manageBios": True, "overriddenSettings": bl_gen10_spt_overridden_setting},
        "hideUnusedFlexNics": True,
        "iscsiInitiatorNameType": "AutoGenerated",
        "localStorage": None,
        "sanStorage": None,
        "osDeploymentSettings": None,
        "initialScopeUris": []}]

bl_gen10_server_profile_bios_only = {
    "serverHardwareUri": "SH:" + bl_server_ilo_hostname,
    "bios": {"manageBios": True, "overriddenSettings": bl_gen10_create_sp_overridden_setting}}

bl_gen10_server_profile_bootmode_and_bios = {
    "serverHardwareUri": "SH:" + bl_server_ilo_hostname,
    "boot": {"manageBoot": True, "order": ["CD", "USB", "HardDisk", "PXE"]},
    "bootMode": {"manageMode": True, "mode": "BIOS", "secureBoot": "Unmanaged"},
    "bios": {"manageBios": True, "overriddenSettings": bl_gen10_create_sp_overridden_setting}}

bl_gen10_server_profile_connection_and_bios = {
    "serverHardwareUri": "SH:" + bl_server_ilo_hostname,
    "connectionSettings": {"connections": []},
    "bios": {"manageBios": True, "overriddenSettings": bl_gen10_create_sp_overridden_setting}}

bl_gen10_server_profile_firmware_and_bios = {
    "serverHardwareUri": "SH:" + bl_server_ilo_hostname,
    "firmware": {
        "manageFirmware": True,
        "forceInstallFirmware": False,
        "firmwareInstallType": "FirmwareOnlyOfflineMode"},
    "bios": {"manageBios": True, "overriddenSettings": bl_gen10_create_sp_overridden_setting}}

bl_gen10_server_profile_with_template_and_bios = {
    "serverHardwareUri": "SH:" + bl_server_ilo_hostname,
    "serverProfileTemplateUri": "SPT:BladeGen10TemplateName",
    "bios": {"manageBios": True, "overriddenSettings": bl_gen10_create_sp_overridden_setting}}

bl_gen10_server_profile_create_specific_bios = {
    "serverHardwareUri": "SH:" + bl_server_ilo_hostname,
    "bios": {"manageBios": True, "overriddenSettings": bl_gen10_create_specific_bios_overridden_setting}}

bl_gen10_server_profile_edit_specific_bios = {
    "serverHardwareUri": "SH:" + bl_server_ilo_hostname,
    "bios": {"manageBios": True, "overriddenSettings": bl_gen10_edit_specific_bios_overridden_setting}}

bl_gen10_server_profile_with_template_and_bios = {
    "serverHardwareUri": "SH:" + bl_server_ilo_hostname,
    "serverProfileTemplateUri": "SPT:BladeGen10TemplateName",
    "bios": {"manageBios": True, "overriddenSettings": bl_gen10_create_sp_overridden_setting}}

bl_gen10_server_profile_unassign = {
    "serverProfileTemplateUri": "SPT:BladeGen10TemplateName",
    "bios": {"manageBios": True, "overriddenSettings": bl_gen10_spt_overridden_setting}}

bl_gen10_server_profile_assign = {
    "serverHardwareUri": "SH:" + bl_server_ilo_hostname,
    "serverProfileTemplateUri": "SPT:BladeGen10TemplateName",
    "bios": {"manageBios": True, "overriddenSettings": bl_gen10_spt_overridden_setting}}

bl_gen10_server_profile_unassign_defbios = {
    "serverProfileTemplateUri": "SPT:BladeGen10TemplateName",
    "bios": {"manageBios": True, "overriddenSettings": []}}

bl_gen10_server_profile_assign_defbios = {
    "serverProfileTemplateUri": "SPT:BladeGen10TemplateName",
    "serverHardwareUri": "SH:" + bl_server_ilo_hostname,
    "bios": {"manageBios": True, "overriddenSettings": []}}

bl_gen10_server_profile_edit_assign_defbios = {
    "serverProfileTemplateUri": "SPT:BladeGen10TemplateName",
    "serverHardwareUri": "SH:" + bl_server_ilo_hostname,
    "bios": {"manageBios": True, "overriddenSettings": []}}

bl_gen10_server_profile_edit_bios_only = {
    "serverHardwareUri": "SH:" + bl_server_ilo_hostname,
    "description": "BladeGen10ServerProfileDescription edited",
    "bios": {"manageBios": True, "overriddenSettings": bl_gen10_edit_sp_overridden_setting}}

bl_gen10_server_profiles = [
    {
        "name": "BLGen10ServerProfileName",
        "description": "BladeGen10ServerProfileDescription",
        "type": bl_server_profile_type,
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "affinity": "Bay",
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "localStorage": None,
        "sanStorage": None,
        "initialScopeUris": []}]

''' C7K Blade Section Ends Here '''

"""Configurations below for Synergy Servers can be changed as per the requirement of testing"""

''' Note : Keep the TestServer in the Managed Mode before testing '''

syn_admin_credentials = {'userName': syn_fusion_admin_credentials_username, 'password': syn_fusion_admin_credentials_password}

syn_server_hardware_type = 'server-hardware-10'
syn_server_profile_template_type = 'ServerProfileTemplateV6'
syn_server_profile_type = 'ServerProfileV10'

""" Generation 9 Synergy Server configuration variables below"""

syn_gen9_spt_overridden_setting = [
    {
        "id": "InternalSDCardSlot",
        "value": "Disabled"}]

syn_gen9_create_sp_overridden_setting = [
    {
        "id": "InternalSDCardSlot",
        "value": "Enabled"}]

syn_gen9_edit_sp_overridden_setting = [
    {
        "id": "InternalSDCardSlot",
        "value": "Disabled"}]

syn_gen9_create_specific_bios_overridden_setting = [
    # The Specific bios attributes for testing
    # Virtualization 158,
    # Hyperthreading 176,
    # Turbo Boost performance 181,
    # VTd 186
    {
        "id": "ProcHyperthreading",
        "value": "Disabled"
    },
    {
        "id": "ProcVirtualization",
        "value": "Disabled"
    },
    {
        "id": "ProcX2Apic",
        "value": "Disabled"
    },
    {
        "id": "IntelProcVtd",
        "value": "Disabled"
    }  # ,
    # {
    #    "id": "EnergyEfficientTurbo",
    #    "value": "Disabled"
    # },
    # {
    #    "id": "ProcTurbo",
    #    "value": "Disabled"
    # }  # Few servers doesn't support Turbo Boost hence few lines of code are commented, if server is supporting Turbo Boost, then the below can be enabled.
]

syn_gen9_edit_specific_bios_overridden_setting = [
    # The Specific bios attributes for testing
    # Virtualization 158,
    # Hyperthreading 176,
    # Turbo Boost performance 181,
    # VTd 186
    {
        "id": "ProcHyperthreading",
        "value": "Enabled"
    },
    {
        "id": "ProcVirtualization",
        "value": "Enabled"
    },
    {
        "id": "ProcX2Apic",
        "value": "Enabled"
    },
    {
        "id": "IntelProcVtd",
        "value": "Enabled"
    }  # ,
    # {
    #    "id": "EnergyEfficientTurbo",
    #    "value": "Enabled"
    # },
    # {
    #    "id": "ProcTurbo",
    #    "value": "Enabled"
    # }  # Few servers doesn't support Turbo Boost hence few lines of code are commented, if server is supporting Turbo Boost, then the below can be enabled.
]

syn_gen9_profile_templates = [
    {
        "name": "SynGen9TemplateName",
        "type": syn_server_profile_template_type,
        "description": "SynGen9TemplateDescription",
        "serverProfileDescription": "SynGen9ServerProfileDescription",
        "enclosureGroupUri": "EG:" + syn_eg_name,
        "serialNumberType": "Virtual",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "affinity": "Bay",
        "connectionSettings": {"connections": [], "manageConnections": False},
        "bios": {"manageBios": True, "overriddenSettings": syn_gen9_spt_overridden_setting},
        "hideUnusedFlexNics": True,
        "iscsiInitiatorNameType": "AutoGenerated",
        "localStorage": None,
        "sanStorage": None,
        "osDeploymentSettings": None}]

syn_gen9_server_profile_bios_only = {
    "serverHardwareUri": "SH:" + syn_server_ilo_hostname,
    "bios": {"manageBios": True, "overriddenSettings": syn_gen9_create_sp_overridden_setting}}

syn_gen9_server_profile_bootmode_and_bios = {
    "serverHardwareUri": "SH:" + syn_server_ilo_hostname,
    "boot": {"manageBoot": True, "order": ["CD", "USB", "HardDisk", "PXE"]},
    "bootMode": {"manageMode": True, "mode": "BIOS", "secureBoot": "Unmanaged"},
    "bios": {"manageBios": True, "overriddenSettings": syn_gen9_create_sp_overridden_setting}}

syn_gen9_server_profile_connection_and_bios = {
    "serverHardwareUri": "SH:" + syn_server_ilo_hostname,
    "connectionSettings": {"connections": []},
    "bios": {"manageBios": True, "overriddenSettings": syn_gen9_create_sp_overridden_setting}}

syn_gen9_server_profile_firmware_and_bios = {
    "serverHardwareUri": "SH:" + syn_server_ilo_hostname,
    "firmware": {
        "manageFirmware": True,
        "forceInstallFirmware": False,
        "firmwareInstallType": "FirmwareOnlyOfflineMode"},
    "bios": {"manageBios": True, "overriddenSettings": syn_gen9_create_sp_overridden_setting}}

syn_gen9_server_profile_create_specific_bios = {
    "serverHardwareUri": "SH:" + syn_server_ilo_hostname,
    "bios": {"manageBios": True, "overriddenSettings": syn_gen9_create_specific_bios_overridden_setting}}

syn_gen9_server_profile_edit_specific_bios = {
    "serverHardwareUri": "SH:" + syn_server_ilo_hostname,
    "bios": {"manageBios": True, "overriddenSettings": syn_gen9_edit_specific_bios_overridden_setting}}

syn_gen9_server_profile_with_template_and_bios = {
    "serverHardwareUri": "SH:" + syn_server_ilo_hostname,
    "serverProfileTemplateUri": "SPT:SynGen9TemplateName",
    "bios": {"manageBios": True, "overriddenSettings": syn_gen9_create_sp_overridden_setting}}

syn_gen9_server_profile_unassign = {
    "serverProfileTemplateUri": "SPT:SynGen9TemplateName",
    "bios": {"manageBios": True, "overriddenSettings": syn_gen9_spt_overridden_setting}}

syn_gen9_server_profile_assign = {
    "serverHardwareUri": "SH:" + syn_server_ilo_hostname,
    "serverProfileTemplateUri": "SPT:SynGen9TemplateName",
    "bios": {"manageBios": True, "overriddenSettings": syn_gen9_spt_overridden_setting}}

syn_gen9_server_profile_unassign_defbios = {
    "serverProfileTemplateUri": "SPT:SynGen9TemplateName",
    "bios": {"manageBios": True, "overriddenSettings": []}}

syn_gen9_server_profile_assign_defbios = {
    "serverProfileTemplateUri": "SPT:SynGen9TemplateName",
    "serverHardwareUri": "SH:" + syn_server_ilo_hostname,
    "bios": {"manageBios": True, "overriddenSettings": []}}

syn_gen9_server_profile_edit_assign_defbios = {
    "serverProfileTemplateUri": "SPT:SynGen9TemplateName",
    "serverHardwareUri": "SH:" + syn_server_ilo_hostname,
    "bios": {"manageBios": True, "overriddenSettings": []}}

syn_gen9_server_profile_edit_bios_only = {
    "serverHardwareUri": "SH:" + syn_server_ilo_hostname,
    "description": "SynGen9ServerProfileDescription edited",
    "bios": {"manageBios": True, "overriddenSettings": syn_gen9_edit_sp_overridden_setting}}

syn_gen9_server_profiles = [
    {
        "name": "SynGen9ServerProfileName",
        "description": "SynGen9ServerProfileDescription",
        "type": syn_server_profile_type,
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "affinity": "Bay",
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "localStorage": None,
        "sanStorage": None}]

""" Generation 10 Synergy Server configuration variables below"""

syn_gen10_spt_overridden_setting = [
    {
        "id": "InternalSDCardSlot",
        "value": "Disabled"}]

syn_gen10_create_sp_overridden_setting = [
    {
        "id": "InternalSDCardSlot",
        "value": "Enabled"}]

syn_gen10_edit_sp_overridden_setting = [
    {
        "id": "InternalSDCardSlot",
        "value": "Disabled"}]

syn_gen10_create_specific_bios_overridden_setting = [
    # The Specific bios attributes for testing
    # Virtualization 158,
    # Hyperthreading 176,
    # Turbo Boost performance 181,
    # VTd 186
    {
        "id": "ProcHyperthreading",
        "value": "Disabled"
    },
    {
        "id": "ProcVirtualization",
        "value": "Disabled"
    },
    {
        "id": "ProcX2Apic",
        "value": "Disabled"
    },
    {
        "id": "IntelProcVtd",
        "value": "Disabled"
    }  # ,
    # {
    #    "id": "EnergyEfficientTurbo",
    #    "value": "Disabled"
    # },
    # {
    #    "id": "ProcTurbo",
    #    "value": "Disabled"
    # }  # Few servers doesn't support Turbo Boost hence few lines of code are commented, if server is supporting Turbo Boost, then the below can be enabled.
]

syn_gen10_edit_specific_bios_overridden_setting = [
    # The Specific bios attributes for testing
    # Virtualization 158,
    # Hyperthreading 176,
    # Turbo Boost performance 181,
    # VTd 186
    {
        "id": "ProcHyperthreading",
        "value": "Enabled"
    },
    {
        "id": "ProcVirtualization",
        "value": "Enabled"
    },
    {
        "id": "ProcX2Apic",
        "value": "Enabled"
    },
    {
        "id": "IntelProcVtd",
        "value": "Enabled"
    }  # ,
    # {
    #    "id": "EnergyEfficientTurbo",
    #    "value": "Enabled"
    # },
    # {
    #    "id": "ProcTurbo",
    #    "value": "Enabled"
    # }  # Few servers doesn't support Turbo Boost hence few lines of code are commented, if server is supporting Turbo Boost, then the below can be enabled.
]

syn_gen10_profile_templates = [
    {
        "name": "SynGen10TemplateName",
        "type": syn_server_profile_template_type,
        "description": "SynGen10TemplateDescription",
        "serverProfileDescription": "SynGen10ServerProfileDescription",
        "enclosureGroupUri": "EG:" + syn_eg_name,
        "serialNumberType": "Virtual",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "affinity": "Bay",
        "connectionSettings": {"connections": [], "manageConnections": False},
        "bios": {"manageBios": True, "overriddenSettings": syn_gen10_spt_overridden_setting},
        "hideUnusedFlexNics": True,
        "iscsiInitiatorNameType": "AutoGenerated",
        "localStorage": None,
        "sanStorage": None,
        "osDeploymentSettings": None}]

syn_gen10_server_profile_bios_only = {
    "serverHardwareUri": "SH:" + syn_server_ilo_hostname,
    "bios": {"manageBios": True, "overriddenSettings": syn_gen10_create_sp_overridden_setting}}

syn_gen10_server_profile_bootmode_and_bios = {
    "serverHardwareUri": "SH:" + syn_server_ilo_hostname,
    "boot": {"manageBoot": True, "order": ["CD", "USB", "HardDisk", "PXE"]},
    "bootMode": {"manageMode": True, "mode": "BIOS", "secureBoot": "Unmanaged"},
    "bios": {"manageBios": True, "overriddenSettings": syn_gen10_create_sp_overridden_setting}}

syn_gen10_server_profile_connection_and_bios = {
    "serverHardwareUri": "SH:" + syn_server_ilo_hostname,
    "connectionSettings": {"connections": []},
    "bios": {"manageBios": True, "overriddenSettings": syn_gen10_create_sp_overridden_setting}}

syn_gen10_server_profile_firmware_and_bios = {
    "serverHardwareUri": "SH:" + syn_server_ilo_hostname,
    "firmware": {
        "manageFirmware": True,
        "forceInstallFirmware": False,
        "firmwareInstallType": "FirmwareOnlyOfflineMode"},
    "bios": {"manageBios": True, "overriddenSettings": syn_gen10_create_sp_overridden_setting}}

syn_gen10_server_profile_create_specific_bios = {
    "serverHardwareUri": "SH:" + syn_server_ilo_hostname,
    "bios": {"manageBios": True, "overriddenSettings": syn_gen10_create_specific_bios_overridden_setting}}

syn_gen10_server_profile_edit_specific_bios = {
    "serverHardwareUri": "SH:" + syn_server_ilo_hostname,
    "bios": {"manageBios": True, "overriddenSettings": syn_gen10_edit_specific_bios_overridden_setting}}

syn_gen10_server_profile_with_template_and_bios = {
    "serverHardwareUri": "SH:" + syn_server_ilo_hostname,
    "serverProfileTemplateUri": "SPT:SynGen10TemplateName",
    "bios": {"manageBios": True, "overriddenSettings": syn_gen10_create_sp_overridden_setting}}

syn_gen10_server_profile_unassign = {
    "serverProfileTemplateUri": "SPT:SynGen10TemplateName",
    "bios": {"manageBios": True, "overriddenSettings": syn_gen10_spt_overridden_setting}}

syn_gen10_server_profile_assign = {
    "serverHardwareUri": "SH:" + syn_server_ilo_hostname,
    "serverProfileTemplateUri": "SPT:SynGen10TemplateName",
    "bios": {"manageBios": True, "overriddenSettings": syn_gen10_spt_overridden_setting}}

syn_gen10_server_profile_unassign_defbios = {
    "serverProfileTemplateUri": "SPT:SynGen10TemplateName",
    "bios": {"manageBios": True, "overriddenSettings": []}}

syn_gen10_server_profile_assign_defbios = {
    "serverProfileTemplateUri": "SPT:SynGen10TemplateName",
    "serverHardwareUri": "SH:" + syn_server_ilo_hostname,
    "bios": {"manageBios": True, "overriddenSettings": []}}

syn_gen10_server_profile_edit_assign_defbios = {
    "serverProfileTemplateUri": "SPT:SynGen10TemplateName",
    "serverHardwareUri": "SH:" + syn_server_ilo_hostname,
    "bios": {"manageBios": True, "overriddenSettings": []}}

syn_gen10_server_profile_edit_bios_only = {
    "serverHardwareUri": "SH:" + syn_server_ilo_hostname,
    "description": "SynGen10ServerProfileDescription edited",
    "bios": {"manageBios": True, "overriddenSettings": syn_gen10_edit_sp_overridden_setting}}

syn_gen10_server_profiles = [
    {
        "name": "SynGen10ServerProfileName",
        "description": "SynGen10ServerProfileDescription",
        "type": syn_server_profile_type,
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "affinity": "Bay",
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "localStorage": None,
        "sanStorage": None}]

''' Synergy Section Ends Here'''

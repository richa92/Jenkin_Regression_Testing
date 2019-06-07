import copy

admin_credentials = {
    'userName': 'Administrator',
    'password': 'wpsthpvse1'
}

ilo_credentials = {
    'username': 'Administrator',
    'password': 'hpvse1-ilo'
}

# EG
EG_NAME = 'EG22'

# Enclosures
ENC1 = 'wpst22'

# Server Hardware
ENC1SHBAY4 = '%s, bay 5' % ENC1
ENC1SHBAY9 = '%s, bay 14' % ENC1
ENC1SHBAY1 = '%s, bay 1' % ENC1

# Server Hardware Types
SERVER_HARDWARE_TYPE1 = 'BL460c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 10Gb 2-port 534M Adapter:2:HP LPe1605 16Gb FC HBA for BladeSystem c-Class'
SERVER_HARDWARE_TYPE2 = 'BL460c Gen10:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter'

# Profiles
PROFILE1_NAME = 'SD Boot Gen9'
PROFILE1_SH = ENC1SHBAY4
PROFILE1_SHT = SERVER_HARDWARE_TYPE1
PROFILE2_NAME = 'SD Boot Gen10'
PROFILE2_SH = ENC1SHBAY9
PROFILE2_SHT = SERVER_HARDWARE_TYPE2
PROFILE3_NAME = 'SD_Boot_Gen9_2'
PROFILE3_SHT = SERVER_HARDWARE_TYPE1
PROFILE4_NAME = 'SD_Boot_Gen10_2'
PROFILE4_SHT = SERVER_HARDWARE_TYPE1
PROFILE1_GEN8_SH = ENC1SHBAY1
PROFILE1_GEN8_NAME = 'Gen8_SP'

PROFILE1_DL_SH = 'fvtdl43-ilo'
DL380_name = 'fvtdl43-ilo'
DL380_IP = '16.114.212.43'

Gen10_DLs = [
    {'name': DL380_name,
     'hostname': DL380_IP,
     'licensingIntent': 'OneViewNoiLO',
     'username': 'Administrator',
     'password': 'hpvse123',
     'force': True,
     'configurationState': 'Managed'
     }
]


# PROFILE DATA

# Create profile with SD Boot on Gen 9
create_profile_gen9 = {
    "type": "ServerProfileV9",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareUri': 'SH:' + PROFILE1_SH,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": ['SD'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "connections": []
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# Create profile with SD Boot on Gen 10
create_profile_gen10 = {
    "type": "ServerProfileV9",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareUri': 'SH:' + PROFILE2_SH,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE2_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": ['SD'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFIOptimized",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "connections": []
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# Edit profile and change boot order to hard disk on Gen 9
edit_profile_gen9 = {
    "type": "ServerProfileV9",
    'serverHardwareUri': 'SH:' + PROFILE1_SH,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "connections": []
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# Edit profile and change boot order to hard disk on Gen 10
edit_profile_gen10 = {
    "type": "ServerProfileV9",
    'serverHardwareUri': 'SH:' + PROFILE2_SH,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE2_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFIOptimized",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "connections": []
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# Edit profile and change boot order to SD on Gen 9
edit2_profile_gen9 = {
    "type": "ServerProfileV9",
    'serverHardwareUri': 'SH:' + PROFILE1_SH,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": ['SD'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "connections": []
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# Edit profile and change boot order to SD on Gen 10
edit2_profile_gen10 = {
    "type": "ServerProfileV9",
    'serverHardwareUri': 'SH:' + PROFILE2_SH,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE2_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": ['SD'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFIOptimized",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "connections": []
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# Move Profile with SD Boot from Gen9 to Gen10
move_profile_to_different_sht = {
    "type": "ServerProfileV9",
    'serverHardwareUri': 'SH:' + PROFILE2_SH,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": ['SD'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "connections": []
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# Create SPT with HD as boot device on Gen9
create_template_gen9 = {
    "type": "ServerProfileTemplateV5",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": False,
    },
    "boot": {
        "order": ['SD'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [],
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# Create SPT with SD as boot device on Gen9
create_template_gen9_2 = {
    "type": "ServerProfileTemplateV5",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE3_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE3_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": False,
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [],
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# Create SPT with HD as boot device on Gen10
create_template_gen10 = {
    "type": "ServerProfileTemplateV5",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE2_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE2_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": False,
    },
    "boot": {
        "order": ['SD'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFIOptimized",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [],
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# Create SPT with SD as boot device on Gen10
create_template_gen10_2 = {
    "type": "ServerProfileTemplateV5",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE4_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE4_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": False,
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFIOptimized",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [],
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# Edit SPT and change boot device to SD on Gen9
edit_template_gen9 = {
    "type": "ServerProfileTemplateV5",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": False,
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [],
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# Edit SPT and change boot device to HD on Gen9
edit_template_gen9_2 = {
    "type": "ServerProfileTemplateV5",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE3_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE3_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": False,
    },
    "boot": {
        "order": ['SD'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [],
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# Edit SPT and change boot device to SD on Gen10
edit_template_gen10 = {
    "type": "ServerProfileTemplateV5",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE2_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE2_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": False,
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFIOptimized",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [],
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# Edit SPT with SD Boot and change to Hard Disk on Gen10
edit_template_gen10_2 = {
    "type": "ServerProfileTemplateV5",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE2_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE4_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": False,
    },
    "boot": {
        "order": ['SD'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFIOptimized",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [],
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# Create profile with SD Boot from template on Gen 9
create_sp_from_spt_gen9 = {
    "type": "ServerProfileV9",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareUri': 'SH:' + PROFILE1_SH,
    'serverProfileTemplateUri': 'SPT:' + PROFILE1_NAME,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": ['SD'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "connections": []
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# Create profile with SD Boot from template on Gen 10
create_sp_from_spt_gen10 = {
    "type": "ServerProfileV9",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareUri': 'SH:' + PROFILE2_SH,
    'serverProfileTemplateUri': 'SPT:' + PROFILE2_NAME,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE2_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": ['SD'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFIOptimized",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "connections": []
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# Create non-compliant profile from template on Gen 9
create_noncompliant_sp_from_spt_gen9 = {
    "type": "ServerProfileV9",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareUri': 'SH:' + PROFILE1_SH,
    'serverProfileTemplateUri': 'SPT:' + PROFILE1_NAME,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "connections": []
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# Create non-compliant profile from template on Gen 10
create_noncompliant_sp_from_spt_gen10 = {
    "type": "ServerProfileV9",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareUri': 'SH:' + PROFILE2_SH,
    'serverProfileTemplateUri': 'SPT:' + PROFILE2_NAME,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE2_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFIOptimized",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "connections": []
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# RIS DATA

ts0_ris_after_create_pending_gen9 = {
    "server": PROFILE1_SH,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/bios/boot/settings",
    "validate": {
        'Name': 'Boot Order Pending Settings',
        'PersistentBootConfigOrder': [
            'HD.SD.1.1',
            'Generic.USB.1.1',
            'HD.Emb.1.2',
            'Unknown.Unknown.1',
            'NIC.Slot.1.1.IPv4',
            'NIC.Slot.1.2.IPv4',
            'NIC.Slot.1.1.IPv6',
            'NIC.Slot.1.2.IPv6',
            'NIC.FlexLOM.1.1.IPv4',
            'NIC.FlexLOM.1.2.IPv4',
            'NIC.FlexLOM.1.1.IPv6',
            'NIC.FlexLOM.1.2.IPv6'
        ],
    }
}

ts0_ris_after_create_pending_gen10 = {
    "server": PROFILE2_SH,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/bios/boot/settings",
    "validate": {
        'Name': 'Boot Order Pending Settings',
        'PersistentBootConfigOrder': [
            'HD.SD.1.2',
            'HD.EmbRAID.1.3',
            'HD.EmbRAID.1.2',
            'Generic.USB.1.1',
            'NIC.FlexLOM.1.1.Httpv4',
            'NIC.FlexLOM.1.1.IPv4',
            'NIC.FlexLOM.1.2.Httpv4',
            'NIC.FlexLOM.1.2.IPv4',
            'NIC.FlexLOM.1.1.Httpv6',
            'NIC.FlexLOM.1.1.IPv6',
            'NIC.FlexLOM.1.2.Httpv6',
            'NIC.FlexLOM.1.2.IPv6'
        ]
    }
}

ts0_ris_after_create_gen9 = {
    "server": PROFILE1_SH,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/bios/boot",
    "validate": {
        "BootSources": [
            {
                'BootString': 'Internal SD Card 1 : Generic Ultra Fast Media Reader',
                'CorrelatableID': 'PciRoot(0x0)/Pci(0x1D,0x0)/USB(0x0,0x0)/USB(0x2,0x0)/USB(0x0,0x0)',
                'StructuredBootString': 'HD.SD.1.1',
                'UEFIDevicePath': 'PciRoot(0x0)/Pci(0x1D,0x0)/USB(0x0,0x0)/USB(0x2,0x0)/USB(0x0,0x0)'},
            {
                'BootString': 'Generic USB Boot',
                'CorrelatableID': 'UsbClass(0xFFFF,0xFFFF,0xFF,0xFF,0xFF)',
                'StructuredBootString': 'Generic.USB.1.1',
                'UEFIDevicePath': 'UsbClass(0xFFFF,0xFFFF,0xFF,0xFF,0xFF)'
            },
            {
                'BootString': 'Embedded RAID 1 : Smart Array P244br Controller - 136.70 GiB, RAID 1 Logical Drive(Target:0, Lun:0)',
                'CorrelatableID': 'PciRoot(0x0)/Pci(0x2,0x2)/Pci(0x0,0x0)',
                'StructuredBootString': 'HD.Emb.1.2',
                'UEFIDevicePath': 'PciRoot(0x0)/Pci(0x2,0x2)/Pci(0x0,0x0)/Scsi(0x0,0x0)'
            },
            {
                'BootString': 'sles-secureboot',
                'CorrelatableID': 'HD(1,GPT,25BFB49C-8C2D-4FCE-BDFC-D9D01BA7531B,0x800,0x4E000)/\\EFI\\sles\\shim.efi',
                'StructuredBootString': 'Unknown.Unknown.1',
                'UEFIDevicePath': 'HD(1,GPT,25BFB49C-8C2D-4FCE-BDFC-D9D01BA7531B,0x800,0x4E000)/\\EFI\\sles\\shim.efi'
            },
            {
                'BootString': 'Slot 1 Port 1 : HP FlexFabric 10Gb 2-port 534M Adapter - CNA - HP FlexFabric 10Gb 2-port 534M Adapter - NIC (PXE IPv4) ',
                'CorrelatableID': 'PciRoot(0x0)/Pci(0x3,0x0)/Pci(0x0,0x0)',
                'StructuredBootString': 'NIC.Slot.1.1.IPv4',
                'UEFIDevicePath': 'PciRoot(0x0)/Pci(0x3,0x0)/Pci(0x0,0x0)/MAC(2C44FD8D2758,0x0)/IPv4(0.0.0.0)'
            },
            {
                'BootString': 'Slot 1 Port 2 : HP FlexFabric 10Gb 2-port 534M Adapter - CNA - HP FlexFabric 10Gb 2-port 534M Adapter - NIC (PXE IPv4) ',
                'CorrelatableID': 'PciRoot(0x0)/Pci(0x3,0x0)/Pci(0x0,0x1)',
                'StructuredBootString': 'NIC.Slot.1.2.IPv4',
                'UEFIDevicePath': 'PciRoot(0x0)/Pci(0x3,0x0)/Pci(0x0,0x1)/MAC(2C44FD8D275C,0x0)/IPv4(0.0.0.0)'
            },
            {
                'BootString': 'Slot 1 Port 1 : HP FlexFabric 10Gb 2-port 534M Adapter - CNA - HP FlexFabric 10Gb 2-port 534M Adapter - NIC (PXE IPv6) ',
                'CorrelatableID': 'PciRoot(0x0)/Pci(0x3,0x0)/Pci(0x0,0x0)',
                'StructuredBootString': 'NIC.Slot.1.1.IPv6',
                'UEFIDevicePath': 'PciRoot(0x0)/Pci(0x3,0x0)/Pci(0x0,0x0)/MAC(2C44FD8D2758,0x0)/IPv6(0000:0000:0000:0000:0000:0000:0000:0000)'
            },
            {
                'BootString': 'Slot 1 Port 2 : HP FlexFabric 10Gb 2-port 534M Adapter - CNA - HP FlexFabric 10Gb 2-port 534M Adapter - NIC (PXE IPv6) ',
                'CorrelatableID': 'PciRoot(0x0)/Pci(0x3,0x0)/Pci(0x0,0x1)',
                'StructuredBootString': 'NIC.Slot.1.2.IPv6',
                'UEFIDevicePath': 'PciRoot(0x0)/Pci(0x3,0x0)/Pci(0x0,0x1)/MAC(2C44FD8D275C,0x0)/IPv6(0000:0000:0000:0000:0000:0000:0000:0000)'
            },
            {
                'BootString': 'Embedded FlexibleLOM 1 Port 1 : HP FlexFabric 10Gb 2-port 536FLB Adapter - CNA - HP FlexFabric 10Gb 2-port 536FLB Adapter - NIC (PXE IPv4) ',
                'CorrelatableID': 'PciRoot(0x0)/Pci(0x2,0x0)/Pci(0x0,0x0)',
                'StructuredBootString': 'NIC.FlexLOM.1.1.IPv4',
                'UEFIDevicePath': 'PciRoot(0x0)/Pci(0x2,0x0)/Pci(0x0,0x0)/MAC(6CC21737C500,0x0)/IPv4(0.0.0.0)'
            },
            {
                'BootString': 'Embedded FlexibleLOM 1 Port 2 : HP FlexFabric 10Gb 2-port 536FLB Adapter - CNA - HP FlexFabric 10Gb 2-port 536FLB Adapter - NIC (PXE IPv4) ',
                'CorrelatableID': 'PciRoot(0x0)/Pci(0x2,0x0)/Pci(0x0,0x1)',
                'StructuredBootString': 'NIC.FlexLOM.1.2.IPv4',
                'UEFIDevicePath': 'PciRoot(0x0)/Pci(0x2,0x0)/Pci(0x0,0x1)/MAC(6CC21737C508,0x0)/IPv4(0.0.0.0)'
            },
            {
                'BootString': 'Embedded FlexibleLOM 1 Port 1 : HP FlexFabric 10Gb 2-port 536FLB Adapter - CNA - HP FlexFabric 10Gb 2-port 536FLB Adapter - NIC (PXE IPv6) ',
                'CorrelatableID': 'PciRoot(0x0)/Pci(0x2,0x0)/Pci(0x0,0x0)',
                'StructuredBootString': 'NIC.FlexLOM.1.1.IPv6',
                'UEFIDevicePath': 'PciRoot(0x0)/Pci(0x2,0x0)/Pci(0x0,0x0)/MAC(6CC21737C500,0x0)/IPv6(0000:0000:0000:0000:0000:0000:0000:0000)'
            },
            {
                'BootString': 'Embedded FlexibleLOM 1 Port 2 : HP FlexFabric 10Gb 2-port 536FLB Adapter - CNA - HP FlexFabric 10Gb 2-port 536FLB Adapter - NIC (PXE IPv6) ',
                'CorrelatableID': 'PciRoot(0x0)/Pci(0x2,0x0)/Pci(0x0,0x1)',
                'StructuredBootString': 'NIC.FlexLOM.1.2.IPv6',
                'UEFIDevicePath': 'PciRoot(0x0)/Pci(0x2,0x0)/Pci(0x0,0x1)/MAC(6CC21737C508,0x0)/IPv6(0000:0000:0000:0000:0000:0000:0000:0000)'
            }
        ],
        'Name': 'Boot Order Current Settings',
        'PersistentBootConfigOrder': [
            'HD.SD.1.1',
            'Generic.USB.1.1',
            'HD.Emb.1.2',
            'Unknown.Unknown.1',
            'NIC.Slot.1.1.IPv4',
            'NIC.Slot.1.2.IPv4',
            'NIC.Slot.1.1.IPv6',
            'NIC.Slot.1.2.IPv6',
            'NIC.FlexLOM.1.1.IPv4',
            'NIC.FlexLOM.1.2.IPv4',
            'NIC.FlexLOM.1.1.IPv6',
            'NIC.FlexLOM.1.2.IPv6'
        ],
    }
}

ts0_ris_after_create_gen10 = {
    "server": PROFILE2_SH,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/bios/boot",
    "validate": {
        "BootSources": [
            {
                'BootOptionNumber': '000C',
                'BootString': 'Internal SD Card 1 : Generic USB2.0-CRW',
                'CorrelatableID': 'PciRoot(0x0)/Pci(0x14,0x0)/USB(0x7,0x0)',
                'StructuredBootString': 'HD.SD.1.2',
                'UEFIDevicePath': 'PciRoot(0x0)/Pci(0x14,0x0)/USB(0x7,0x0)'
            },
            {
                'BootOptionNumber': '000F',
                'BootString': 'Windows Boot Manager',
                'CorrelatableID': 'PciRoot(0x2)/Pci(0x2,0x0)/Pci(0x0,0x0)',
                'StructuredBootString': 'HD.EmbRAID.1.3',
                'UEFIDevicePath': 'PciRoot(0x2)/Pci(0x2,0x0)/Pci(0x0,0x0)/Scsi(0x0,0x0)/HD(2,GPT,FA85E14D-71FA-4811-BDDB-490F05BFDDED,0x96800,0x31800)/\\EFI\\Microsoft\\Boot\\bootmgfw.efi'
            },
            {
                'BootOptionNumber': '000B',
                'BootString': 'Embedded RAID 1 : HPE P254br - 136.69 GiB, RAID 1 Logical Drive(Target:0, Lun:0)',
                'CorrelatableID': 'PciRoot(0x2)/Pci(0x2,0x0)/Pci(0x0,0x0)',
                'StructuredBootString': 'HD.EmbRAID.1.2',
                'UEFIDevicePath': 'PciRoot(0x2)/Pci(0x2,0x0)/Pci(0x0,0x0)/Scsi(0x0,0x0)'
            },
            {
                'BootOptionNumber': '000A',
                'BootString': 'Generic USB Boot',
                'CorrelatableID': 'UsbClass(0xFFFF,0xFFFF,0xFF,0xFF,0xFF)',
                'StructuredBootString': 'Generic.USB.1.1',
                'UEFIDevicePath': 'UsbClass(0xFFFF,0xFFFF,0xFF,0xFF,0xFF)'
            },
            {
                'BootOptionNumber': '000D',
                'BootString': 'Embedded FlexibleLOM 1 Port 1 : HP FlexFabric 10Gb 2-port 536FLB Adapter - CNA - HP FlexFabric 10Gb 2-port 536FLB Adapter - NIC (HTTP(S) IPv4)',
                'CorrelatableID': 'PciRoot(0x2)/Pci(0x0,0x0)/Pci(0x0,0x0)',
                'StructuredBootString': 'NIC.FlexLOM.1.1.Httpv4',
                'UEFIDevicePath': 'PciRoot(0x2)/Pci(0x0,0x0)/Pci(0x0,0x0)/MAC(5CB901C761F0,0x0)/IPv4(0.0.0.0)/Uri()'
            },
            {
                'BootOptionNumber': '0010',
                'BootString': 'Embedded FlexibleLOM 1 Port 1 : HP FlexFabric 10Gb 2-port 536FLB Adapter - CNA - HP FlexFabric 10Gb 2-port 536FLB Adapter - NIC (PXE IPv4)',
                'CorrelatableID': 'PciRoot(0x2)/Pci(0x0,0x0)/Pci(0x0,0x0)',
                'StructuredBootString': 'NIC.FlexLOM.1.1.IPv4',
                'UEFIDevicePath': 'PciRoot(0x2)/Pci(0x0,0x0)/Pci(0x0,0x0)/MAC(5CB901C761F0,0x0)/IPv4(0.0.0.0)'
            },
            {
                'BootOptionNumber': '0012',
                'BootString': 'Embedded FlexibleLOM 1 Port 2 : HP FlexFabric 10Gb 2-port 536FLB Adapter - CNA - HP FlexFabric 10Gb 2-port 536FLB Adapter - NIC (HTTP(S) IPv4)',
                'CorrelatableID': 'PciRoot(0x2)/Pci(0x0,0x0)/Pci(0x0,0x1)',
                'StructuredBootString': 'NIC.FlexLOM.1.2.Httpv4',
                'UEFIDevicePath': 'PciRoot(0x2)/Pci(0x0,0x0)/Pci(0x0,0x1)/MAC(5CB901C761F8,0x0)/IPv4(0.0.0.0)/Uri()'
            },
            {
                'BootOptionNumber': '0014',
                'BootString': 'Embedded FlexibleLOM 1 Port 2 : HP FlexFabric 10Gb 2-port 536FLB Adapter - CNA - HP FlexFabric 10Gb 2-port 536FLB Adapter - NIC (PXE IPv4)',
                'CorrelatableID': 'PciRoot(0x2)/Pci(0x0,0x0)/Pci(0x0,0x1)',
                'StructuredBootString': 'NIC.FlexLOM.1.2.IPv4',
                'UEFIDevicePath': 'PciRoot(0x2)/Pci(0x0,0x0)/Pci(0x0,0x1)/MAC(5CB901C761F8,0x0)/IPv4(0.0.0.0)'
            },
            {
                'BootOptionNumber': '000E',
                'BootString': 'Embedded FlexibleLOM 1 Port 1 : HP FlexFabric 10Gb 2-port 536FLB Adapter - CNA - HP FlexFabric 10Gb 2-port 536FLB Adapter - NIC (HTTP(S) IPv6)',
                'CorrelatableID': 'PciRoot(0x2)/Pci(0x0,0x0)/Pci(0x0,0x0)',
                'StructuredBootString': 'NIC.FlexLOM.1.1.Httpv6',
                'UEFIDevicePath': 'PciRoot(0x2)/Pci(0x0,0x0)/Pci(0x0,0x0)/MAC(5CB901C761F0,0x0)/IPv6(0000:0000:0000:0000:0000:0000:0000:0000)/Uri()'
            },
            {
                'BootOptionNumber': '0011',
                'BootString': 'Embedded FlexibleLOM 1 Port 1 : HP FlexFabric 10Gb 2-port 536FLB Adapter - CNA - HP FlexFabric 10Gb 2-port 536FLB Adapter - NIC (PXE IPv6)',
                'CorrelatableID': 'PciRoot(0x2)/Pci(0x0,0x0)/Pci(0x0,0x0)',
                'StructuredBootString': 'NIC.FlexLOM.1.1.IPv6',
                'UEFIDevicePath': 'PciRoot(0x2)/Pci(0x0,0x0)/Pci(0x0,0x0)/MAC(5CB901C761F0,0x0)/IPv6(0000:0000:0000:0000:0000:0000:0000:0000)'
            },
            {
                'BootOptionNumber': '0013',
                'BootString': 'Embedded FlexibleLOM 1 Port 2 : HP FlexFabric 10Gb 2-port 536FLB Adapter - CNA - HP FlexFabric 10Gb 2-port 536FLB Adapter - NIC (HTTP(S) IPv6)',
                'CorrelatableID': 'PciRoot(0x2)/Pci(0x0,0x0)/Pci(0x0,0x1)',
                'StructuredBootString': 'NIC.FlexLOM.1.2.Httpv6',
                'UEFIDevicePath': 'PciRoot(0x2)/Pci(0x0,0x0)/Pci(0x0,0x1)/MAC(5CB901C761F8,0x0)/IPv6(0000:0000:0000:0000:0000:0000:0000:0000)/Uri()'
            },
            {
                'BootOptionNumber': '0015',
                'BootString': 'Embedded FlexibleLOM 1 Port 2 : HP FlexFabric 10Gb 2-port 536FLB Adapter - CNA - HP FlexFabric 10Gb 2-port 536FLB Adapter - NIC (PXE IPv6)',
                'CorrelatableID': 'PciRoot(0x2)/Pci(0x0,0x0)/Pci(0x0,0x1)',
                'StructuredBootString': 'NIC.FlexLOM.1.2.IPv6',
                'UEFIDevicePath': 'PciRoot(0x2)/Pci(0x0,0x0)/Pci(0x0,0x1)/MAC(5CB901C761F8,0x0)/IPv6(0000:0000:0000:0000:0000:0000:0000:0000)'
            }

        ],
        'Name': 'Boot Order Current Settings',
        'PersistentBootConfigOrder': [
            'HD.SD.1.2',
            'HD.EmbRAID.1.3',
            'HD.EmbRAID.1.2',
            'Generic.USB.1.1',
            'NIC.FlexLOM.1.1.Httpv4',
            'NIC.FlexLOM.1.1.IPv4',
            'NIC.FlexLOM.1.2.Httpv4',
            'NIC.FlexLOM.1.2.IPv4',
            'NIC.FlexLOM.1.1.Httpv6',
            'NIC.FlexLOM.1.1.IPv6',
            'NIC.FlexLOM.1.2.Httpv6',
            'NIC.FlexLOM.1.2.IPv6'
        ]
    }
}

ts1_ris_after_edit1_pending_gen9 = {
    "server": PROFILE1_SH,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/bios/boot/settings",
    "validate": {
        'Name': 'Boot Order Pending Settings',
        "PersistentBootConfigOrder": [
            'HD.Emb.1.2',
            'HD.SD.1.1',
            'Generic.USB.1.1',
            'Unknown.Unknown.1',
            'NIC.Slot.1.1.IPv4',
            'NIC.Slot.1.2.IPv4',
            'NIC.Slot.1.1.IPv6',
            'NIC.Slot.1.2.IPv6',
            'NIC.FlexLOM.1.1.IPv4',
            'NIC.FlexLOM.1.2.IPv4',
            'NIC.FlexLOM.1.1.IPv6',
            'NIC.FlexLOM.1.2.IPv6'
        ]
    }
}

ts1_ris_after_edit1_pending_gen10 = {
    "server": PROFILE2_SH,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/bios/boot/settings",
    "validate": {
        'Name': 'Boot Order Pending Settings',
        "PersistentBootConfigOrder": [
            'HD.EmbRAID.1.3',
            'HD.EmbRAID.1.2',
            'HD.SD.1.2',
            'Generic.USB.1.1',
            'NIC.FlexLOM.1.1.Httpv4',
            'NIC.FlexLOM.1.1.IPv4',
            'NIC.FlexLOM.1.2.Httpv4',
            'NIC.FlexLOM.1.2.IPv4',
            'NIC.FlexLOM.1.1.Httpv6',
            'NIC.FlexLOM.1.1.IPv6',
            'NIC.FlexLOM.1.2.Httpv6',
            'NIC.FlexLOM.1.2.IPv6'
        ]
    }
}

ts1_ris_after_edit1_gen9 = {
    "server": PROFILE1_SH,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/bios/boot",
    "validate": {
        'BootSources': [
            {
                'BootString': 'Embedded RAID 1 : Smart Array P244br Controller - 136.70 GiB, RAID 1 Logical Drive(Target:0, Lun:0)',
                'CorrelatableID': 'PciRoot(0x0)/Pci(0x2,0x2)/Pci(0x0,0x0)',
                'StructuredBootString': 'HD.Emb.1.2',
                'UEFIDevicePath': 'PciRoot(0x0)/Pci(0x2,0x2)/Pci(0x0,0x0)/Scsi(0x0,0x0)'
            },
            {
                'BootString': 'Internal SD Card 1 : Generic Ultra Fast Media Reader',
                'CorrelatableID': 'PciRoot(0x0)/Pci(0x1D,0x0)/USB(0x0,0x0)/USB(0x2,0x0)/USB(0x0,0x0)',
                'StructuredBootString': 'HD.SD.1.1',
                'UEFIDevicePath': 'PciRoot(0x0)/Pci(0x1D,0x0)/USB(0x0,0x0)/USB(0x2,0x0)/USB(0x0,0x0)'
            },
            {
                'BootString': 'Generic USB Boot',
                'CorrelatableID': 'UsbClass(0xFFFF,0xFFFF,0xFF,0xFF,0xFF)',
                'StructuredBootString': 'Generic.USB.1.1',
                'UEFIDevicePath': 'UsbClass(0xFFFF,0xFFFF,0xFF,0xFF,0xFF)'
            },
            {
                'BootString': 'sles-secureboot',
                'CorrelatableID': 'HD(1,GPT,25BFB49C-8C2D-4FCE-BDFC-D9D01BA7531B,0x800,0x4E000)/\\EFI\\sles\\shim.efi',
                'StructuredBootString': 'Unknown.Unknown.1',
                'UEFIDevicePath': 'HD(1,GPT,25BFB49C-8C2D-4FCE-BDFC-D9D01BA7531B,0x800,0x4E000)/\\EFI\\sles\\shim.efi'
            },
            {
                'BootString': 'Slot 1 Port 1 : HP FlexFabric 10Gb 2-port 534M Adapter - CNA - HP FlexFabric 10Gb 2-port 534M Adapter - NIC (PXE IPv4) ',
                'CorrelatableID': 'PciRoot(0x0)/Pci(0x3,0x0)/Pci(0x0,0x0)',
                'StructuredBootString': 'NIC.Slot.1.1.IPv4',
                'UEFIDevicePath': 'PciRoot(0x0)/Pci(0x3,0x0)/Pci(0x0,0x0)/MAC(2C44FD8D2758,0x0)/IPv4(0.0.0.0)'
            },
            {
                'BootString': 'Slot 1 Port 2 : HP FlexFabric 10Gb 2-port 534M Adapter - CNA - HP FlexFabric 10Gb 2-port 534M Adapter - NIC (PXE IPv4) ',
                'CorrelatableID': 'PciRoot(0x0)/Pci(0x3,0x0)/Pci(0x0,0x1)',
                'StructuredBootString': 'NIC.Slot.1.2.IPv4',
                'UEFIDevicePath': 'PciRoot(0x0)/Pci(0x3,0x0)/Pci(0x0,0x1)/MAC(2C44FD8D275C,0x0)/IPv4(0.0.0.0)'
            },
            {
                'BootString': 'Slot 1 Port 1 : HP FlexFabric 10Gb 2-port 534M Adapter - CNA - HP FlexFabric 10Gb 2-port 534M Adapter - NIC (PXE IPv6) ',
                'CorrelatableID': 'PciRoot(0x0)/Pci(0x3,0x0)/Pci(0x0,0x0)',
                'StructuredBootString': 'NIC.Slot.1.1.IPv6',
                'UEFIDevicePath': 'PciRoot(0x0)/Pci(0x3,0x0)/Pci(0x0,0x0)/MAC(2C44FD8D2758,0x0)/IPv6(0000:0000:0000:0000:0000:0000:0000:0000)'
            },
            {
                'BootString': 'Slot 1 Port 2 : HP FlexFabric 10Gb 2-port 534M Adapter - CNA - HP FlexFabric 10Gb 2-port 534M Adapter - NIC (PXE IPv6) ',
                'CorrelatableID': 'PciRoot(0x0)/Pci(0x3,0x0)/Pci(0x0,0x1)',
                'StructuredBootString': 'NIC.Slot.1.2.IPv6',
                'UEFIDevicePath': 'PciRoot(0x0)/Pci(0x3,0x0)/Pci(0x0,0x1)/MAC(2C44FD8D275C,0x0)/IPv6(0000:0000:0000:0000:0000:0000:0000:0000)'
            },
            {
                'BootString': 'Embedded FlexibleLOM 1 Port 1 : HP FlexFabric 10Gb 2-port 536FLB Adapter - CNA - HP FlexFabric 10Gb 2-port 536FLB Adapter - NIC (PXE IPv4) ',
                'CorrelatableID': 'PciRoot(0x0)/Pci(0x2,0x0)/Pci(0x0,0x0)',
                'StructuredBootString': 'NIC.FlexLOM.1.1.IPv4',
                'UEFIDevicePath': 'PciRoot(0x0)/Pci(0x2,0x0)/Pci(0x0,0x0)/MAC(6CC21737C500,0x0)/IPv4(0.0.0.0)'
            },
            {
                'BootString': 'Embedded FlexibleLOM 1 Port 2 : HP FlexFabric 10Gb 2-port 536FLB Adapter - CNA - HP FlexFabric 10Gb 2-port 536FLB Adapter - NIC (PXE IPv4) ',
                'CorrelatableID': 'PciRoot(0x0)/Pci(0x2,0x0)/Pci(0x0,0x1)',
                'StructuredBootString': 'NIC.FlexLOM.1.2.IPv4',
                'UEFIDevicePath': 'PciRoot(0x0)/Pci(0x2,0x0)/Pci(0x0,0x1)/MAC(6CC21737C508,0x0)/IPv4(0.0.0.0)'
            },
            {
                'BootString': 'Embedded FlexibleLOM 1 Port 1 : HP FlexFabric 10Gb 2-port 536FLB Adapter - CNA - HP FlexFabric 10Gb 2-port 536FLB Adapter - NIC (PXE IPv6) ',
                'CorrelatableID': 'PciRoot(0x0)/Pci(0x2,0x0)/Pci(0x0,0x0)',
                'StructuredBootString': 'NIC.FlexLOM.1.1.IPv6',
                'UEFIDevicePath': 'PciRoot(0x0)/Pci(0x2,0x0)/Pci(0x0,0x0)/MAC(6CC21737C500,0x0)/IPv6(0000:0000:0000:0000:0000:0000:0000:0000)'
            },
            {
                'BootString': 'Embedded FlexibleLOM 1 Port 2 : HP FlexFabric 10Gb 2-port 536FLB Adapter - CNA - HP FlexFabric 10Gb 2-port 536FLB Adapter - NIC (PXE IPv6) ',
                'CorrelatableID': 'PciRoot(0x0)/Pci(0x2,0x0)/Pci(0x0,0x1)',
                'StructuredBootString': 'NIC.FlexLOM.1.2.IPv6',
                'UEFIDevicePath': 'PciRoot(0x0)/Pci(0x2,0x0)/Pci(0x0,0x1)/MAC(6CC21737C508,0x0)/IPv6(0000:0000:0000:0000:0000:0000:0000:0000)'
            }
        ],
        'Name': 'Boot Order Current Settings',
        "PersistentBootConfigOrder": [
            'HD.Emb.1.2',
            'HD.SD.1.1',
            'Generic.USB.1.1',
            'Unknown.Unknown.1',
            'NIC.Slot.1.1.IPv4',
            'NIC.Slot.1.2.IPv4',
            'NIC.Slot.1.1.IPv6',
            'NIC.Slot.1.2.IPv6',
            'NIC.FlexLOM.1.1.IPv4',
            'NIC.FlexLOM.1.2.IPv4',
            'NIC.FlexLOM.1.1.IPv6',
            'NIC.FlexLOM.1.2.IPv6'
        ]
    }
}

ts1_ris_after_edit1_gen10 = {
    "server": PROFILE2_SH,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/bios/boot",
    "validate": {
        'BootSources': [
            {
                'BootOptionNumber': '000F',
                'BootString': 'Windows Boot Manager',
                'CorrelatableID': 'PciRoot(0x2)/Pci(0x2,0x0)/Pci(0x0,0x0)',
                'StructuredBootString': 'HD.EmbRAID.1.3',
                'UEFIDevicePath': 'PciRoot(0x2)/Pci(0x2,0x0)/Pci(0x0,0x0)/Scsi(0x0,0x0)/HD(2,GPT,FA85E14D-71FA-4811-BDDB-490F05BFDDED,0x96800,0x31800)/\\EFI\\Microsoft\\Boot\\bootmgfw.efi'
            },
            {
                'BootOptionNumber': '000B',
                'BootString': 'Embedded RAID 1 : HPE P254br - 136.69 GiB, RAID 1 Logical Drive(Target:0, Lun:0)',
                'CorrelatableID': 'PciRoot(0x2)/Pci(0x2,0x0)/Pci(0x0,0x0)',
                'StructuredBootString': 'HD.EmbRAID.1.2',
                'UEFIDevicePath': 'PciRoot(0x2)/Pci(0x2,0x0)/Pci(0x0,0x0)/Scsi(0x0,0x0)'
            },
            {
                'BootOptionNumber': '000C',
                'BootString': 'Internal SD Card 1 : Generic USB2.0-CRW',
                'CorrelatableID': 'PciRoot(0x0)/Pci(0x14,0x0)/USB(0x7,0x0)',
                'StructuredBootString': 'HD.SD.1.2',
                'UEFIDevicePath': 'PciRoot(0x0)/Pci(0x14,0x0)/USB(0x7,0x0)'
            },
            {
                'BootOptionNumber': '000A',
                'BootString': 'Generic USB Boot',
                'CorrelatableID': 'UsbClass(0xFFFF,0xFFFF,0xFF,0xFF,0xFF)',
                'StructuredBootString': 'Generic.USB.1.1',
                'UEFIDevicePath': 'UsbClass(0xFFFF,0xFFFF,0xFF,0xFF,0xFF)'
            },
            {
                'BootOptionNumber': '000D',
                'BootString': 'Embedded FlexibleLOM 1 Port 1 : HP FlexFabric 10Gb 2-port 536FLB Adapter - CNA - HP FlexFabric 10Gb 2-port 536FLB Adapter - NIC (HTTP(S) IPv4)',
                'CorrelatableID': 'PciRoot(0x2)/Pci(0x0,0x0)/Pci(0x0,0x0)',
                'StructuredBootString': 'NIC.FlexLOM.1.1.Httpv4',
                'UEFIDevicePath': 'PciRoot(0x2)/Pci(0x0,0x0)/Pci(0x0,0x0)/MAC(5CB901C761F0,0x0)/IPv4(0.0.0.0)/Uri()'
            },
            {
                'BootOptionNumber': '0010',
                'BootString': 'Embedded FlexibleLOM 1 Port 1 : HP FlexFabric 10Gb 2-port 536FLB Adapter - CNA - HP FlexFabric 10Gb 2-port 536FLB Adapter - NIC (PXE IPv4)',
                'CorrelatableID': 'PciRoot(0x2)/Pci(0x0,0x0)/Pci(0x0,0x0)',
                'StructuredBootString': 'NIC.FlexLOM.1.1.IPv4',
                'UEFIDevicePath': 'PciRoot(0x2)/Pci(0x0,0x0)/Pci(0x0,0x0)/MAC(5CB901C761F0,0x0)/IPv4(0.0.0.0)'
            },
            {
                'BootOptionNumber': '0012',
                'BootString': 'Embedded FlexibleLOM 1 Port 2 : HP FlexFabric 10Gb 2-port 536FLB Adapter - CNA - HP FlexFabric 10Gb 2-port 536FLB Adapter - NIC (HTTP(S) IPv4)',
                'CorrelatableID': 'PciRoot(0x2)/Pci(0x0,0x0)/Pci(0x0,0x1)',
                'StructuredBootString': 'NIC.FlexLOM.1.2.Httpv4',
                'UEFIDevicePath': 'PciRoot(0x2)/Pci(0x0,0x0)/Pci(0x0,0x1)/MAC(5CB901C761F8,0x0)/IPv4(0.0.0.0)/Uri()'
            },
            {
                'BootOptionNumber': '0014',
                'BootString': 'Embedded FlexibleLOM 1 Port 2 : HP FlexFabric 10Gb 2-port 536FLB Adapter - CNA - HP FlexFabric 10Gb 2-port 536FLB Adapter - NIC (PXE IPv4)',
                'CorrelatableID': 'PciRoot(0x2)/Pci(0x0,0x0)/Pci(0x0,0x1)',
                'StructuredBootString': 'NIC.FlexLOM.1.2.IPv4',
                'UEFIDevicePath': 'PciRoot(0x2)/Pci(0x0,0x0)/Pci(0x0,0x1)/MAC(5CB901C761F8,0x0)/IPv4(0.0.0.0)'
            },
            {
                'BootOptionNumber': '000E',
                'BootString': 'Embedded FlexibleLOM 1 Port 1 : HP FlexFabric 10Gb 2-port 536FLB Adapter - CNA - HP FlexFabric 10Gb 2-port 536FLB Adapter - NIC (HTTP(S) IPv6)',
                'CorrelatableID': 'PciRoot(0x2)/Pci(0x0,0x0)/Pci(0x0,0x0)',
                'StructuredBootString': 'NIC.FlexLOM.1.1.Httpv6',
                'UEFIDevicePath': 'PciRoot(0x2)/Pci(0x0,0x0)/Pci(0x0,0x0)/MAC(5CB901C761F0,0x0)/IPv6(0000:0000:0000:0000:0000:0000:0000:0000)/Uri()'
            },
            {
                'BootOptionNumber': '0011',
                'BootString': 'Embedded FlexibleLOM 1 Port 1 : HP FlexFabric 10Gb 2-port 536FLB Adapter - CNA - HP FlexFabric 10Gb 2-port 536FLB Adapter - NIC (PXE IPv6)',
                'CorrelatableID': 'PciRoot(0x2)/Pci(0x0,0x0)/Pci(0x0,0x0)',
                'StructuredBootString': 'NIC.FlexLOM.1.1.IPv6',
                'UEFIDevicePath': 'PciRoot(0x2)/Pci(0x0,0x0)/Pci(0x0,0x0)/MAC(5CB901C761F0,0x0)/IPv6(0000:0000:0000:0000:0000:0000:0000:0000)'
            },
            {
                'BootOptionNumber': '0013',
                'BootString': 'Embedded FlexibleLOM 1 Port 2 : HP FlexFabric 10Gb 2-port 536FLB Adapter - CNA - HP FlexFabric 10Gb 2-port 536FLB Adapter - NIC (HTTP(S) IPv6)',
                'CorrelatableID': 'PciRoot(0x2)/Pci(0x0,0x0)/Pci(0x0,0x1)',
                'StructuredBootString': 'NIC.FlexLOM.1.2.Httpv6',
                'UEFIDevicePath': 'PciRoot(0x2)/Pci(0x0,0x0)/Pci(0x0,0x1)/MAC(5CB901C761F8,0x0)/IPv6(0000:0000:0000:0000:0000:0000:0000:0000)/Uri()'
            },
            {
                'BootOptionNumber': '0015',
                'BootString': 'Embedded FlexibleLOM 1 Port 2 : HP FlexFabric 10Gb 2-port 536FLB Adapter - CNA - HP FlexFabric 10Gb 2-port 536FLB Adapter - NIC (PXE IPv6)',
                'CorrelatableID': 'PciRoot(0x2)/Pci(0x0,0x0)/Pci(0x0,0x1)',
                'StructuredBootString': 'NIC.FlexLOM.1.2.IPv6',
                'UEFIDevicePath': 'PciRoot(0x2)/Pci(0x0,0x0)/Pci(0x0,0x1)/MAC(5CB901C761F8,0x0)/IPv6(0000:0000:0000:0000:0000:0000:0000:0000)'
            }
        ],
        'Name': 'Boot Order Current Settings',
        "PersistentBootConfigOrder": [
            'HD.EmbRAID.1.3',
            'HD.EmbRAID.1.2',
            'HD.SD.1.2',
            'Generic.USB.1.1',
            'NIC.FlexLOM.1.1.Httpv4',
            'NIC.FlexLOM.1.1.IPv4',
            'NIC.FlexLOM.1.2.Httpv4',
            'NIC.FlexLOM.1.2.IPv4',
            'NIC.FlexLOM.1.1.Httpv6',
            'NIC.FlexLOM.1.1.IPv6',
            'NIC.FlexLOM.1.2.Httpv6',
            'NIC.FlexLOM.1.2.IPv6'
        ]
    }
}

ts0_ris_after_move_gen10 = {
    "server": PROFILE2_SH,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/bios/boot",
    "validate": {
        "BootSources": [
            {
                'BootOptionNumber': '000C',
                'BootString': 'Internal SD Card 1 : Generic USB2.0-CRW',
                'CorrelatableID': 'PciRoot(0x0)/Pci(0x14,0x0)/USB(0x7,0x0)',
                'StructuredBootString': 'HD.SD.1.2',
                'UEFIDevicePath': 'PciRoot(0x0)/Pci(0x14,0x0)/USB(0x7,0x0)'
            },
            {
                'BootOptionNumber': '000F',
                'BootString': 'Windows Boot Manager',
                'CorrelatableID': 'PciRoot(0x2)/Pci(0x2,0x0)/Pci(0x0,0x0)',
                'StructuredBootString': 'HD.EmbRAID.1.3',
                'UEFIDevicePath': 'PciRoot(0x2)/Pci(0x2,0x0)/Pci(0x0,0x0)/Scsi(0x0,0x0)/HD(2,GPT,FA85E14D-71FA-4811-BDDB-490F05BFDDED,0x96800,0x31800)/\\EFI\\Microsoft\\Boot\\bootmgfw.efi'
            },
            {
                'BootOptionNumber': '000B',
                'BootString': 'Embedded RAID 1 : HPE P254br - 136.69 GiB, RAID 1 Logical Drive(Target:0, Lun:0)',
                'CorrelatableID': 'PciRoot(0x2)/Pci(0x2,0x0)/Pci(0x0,0x0)',
                'StructuredBootString': 'HD.EmbRAID.1.2',
                'UEFIDevicePath': 'PciRoot(0x2)/Pci(0x2,0x0)/Pci(0x0,0x0)/Scsi(0x0,0x0)'
            },
            {
                'BootOptionNumber': '000A',
                'BootString': 'Generic USB Boot',
                'CorrelatableID': 'UsbClass(0xFFFF,0xFFFF,0xFF,0xFF,0xFF)',
                'StructuredBootString': 'Generic.USB.1.1',
                'UEFIDevicePath': 'UsbClass(0xFFFF,0xFFFF,0xFF,0xFF,0xFF)'
            },
            {
                'BootOptionNumber': '000D',
                'BootString': 'Embedded FlexibleLOM 1 Port 1 : HP FlexFabric 10Gb 2-port 536FLB Adapter - CNA - HP FlexFabric 10Gb 2-port 536FLB Adapter - NIC (HTTP(S) IPv4)',
                'CorrelatableID': 'PciRoot(0x2)/Pci(0x0,0x0)/Pci(0x0,0x0)',
                'StructuredBootString': 'NIC.FlexLOM.1.1.Httpv4',
                'UEFIDevicePath': 'PciRoot(0x2)/Pci(0x0,0x0)/Pci(0x0,0x0)/MAC(5CB901C761F0,0x0)/IPv4(0.0.0.0)/Uri()'
            },
            {
                'BootOptionNumber': '0010',
                'BootString': 'Embedded FlexibleLOM 1 Port 1 : HP FlexFabric 10Gb 2-port 536FLB Adapter - CNA - HP FlexFabric 10Gb 2-port 536FLB Adapter - NIC (PXE IPv4)',
                'CorrelatableID': 'PciRoot(0x2)/Pci(0x0,0x0)/Pci(0x0,0x0)',
                'StructuredBootString': 'NIC.FlexLOM.1.1.IPv4',
                'UEFIDevicePath': 'PciRoot(0x2)/Pci(0x0,0x0)/Pci(0x0,0x0)/MAC(5CB901C761F0,0x0)/IPv4(0.0.0.0)'
            },
            {
                'BootOptionNumber': '0012',
                'BootString': 'Embedded FlexibleLOM 1 Port 2 : HP FlexFabric 10Gb 2-port 536FLB Adapter - CNA - HP FlexFabric 10Gb 2-port 536FLB Adapter - NIC (HTTP(S) IPv4)',
                'CorrelatableID': 'PciRoot(0x2)/Pci(0x0,0x0)/Pci(0x0,0x1)',
                'StructuredBootString': 'NIC.FlexLOM.1.2.Httpv4',
                'UEFIDevicePath': 'PciRoot(0x2)/Pci(0x0,0x0)/Pci(0x0,0x1)/MAC(5CB901C761F8,0x0)/IPv4(0.0.0.0)/Uri()'
            },
            {
                'BootOptionNumber': '0014',
                'BootString': 'Embedded FlexibleLOM 1 Port 2 : HP FlexFabric 10Gb 2-port 536FLB Adapter - CNA - HP FlexFabric 10Gb 2-port 536FLB Adapter - NIC (PXE IPv4)',
                'CorrelatableID': 'PciRoot(0x2)/Pci(0x0,0x0)/Pci(0x0,0x1)',
                'StructuredBootString': 'NIC.FlexLOM.1.2.IPv4',
                'UEFIDevicePath': 'PciRoot(0x2)/Pci(0x0,0x0)/Pci(0x0,0x1)/MAC(5CB901C761F8,0x0)/IPv4(0.0.0.0)'
            },
            {
                'BootOptionNumber': '000E',
                'BootString': 'Embedded FlexibleLOM 1 Port 1 : HP FlexFabric 10Gb 2-port 536FLB Adapter - CNA - HP FlexFabric 10Gb 2-port 536FLB Adapter - NIC (HTTP(S) IPv6)',
                'CorrelatableID': 'PciRoot(0x2)/Pci(0x0,0x0)/Pci(0x0,0x0)',
                'StructuredBootString': 'NIC.FlexLOM.1.1.Httpv6',
                'UEFIDevicePath': 'PciRoot(0x2)/Pci(0x0,0x0)/Pci(0x0,0x0)/MAC(5CB901C761F0,0x0)/IPv6(0000:0000:0000:0000:0000:0000:0000:0000)/Uri()'
            },
            {
                'BootOptionNumber': '0011',
                'BootString': 'Embedded FlexibleLOM 1 Port 1 : HP FlexFabric 10Gb 2-port 536FLB Adapter - CNA - HP FlexFabric 10Gb 2-port 536FLB Adapter - NIC (PXE IPv6)',
                'CorrelatableID': 'PciRoot(0x2)/Pci(0x0,0x0)/Pci(0x0,0x0)',
                'StructuredBootString': 'NIC.FlexLOM.1.1.IPv6',
                'UEFIDevicePath': 'PciRoot(0x2)/Pci(0x0,0x0)/Pci(0x0,0x0)/MAC(5CB901C761F0,0x0)/IPv6(0000:0000:0000:0000:0000:0000:0000:0000)'
            },
            {
                'BootOptionNumber': '0013',
                'BootString': 'Embedded FlexibleLOM 1 Port 2 : HP FlexFabric 10Gb 2-port 536FLB Adapter - CNA - HP FlexFabric 10Gb 2-port 536FLB Adapter - NIC (HTTP(S) IPv6)',
                'CorrelatableID': 'PciRoot(0x2)/Pci(0x0,0x0)/Pci(0x0,0x1)',
                'StructuredBootString': 'NIC.FlexLOM.1.2.Httpv6',
                'UEFIDevicePath': 'PciRoot(0x2)/Pci(0x0,0x0)/Pci(0x0,0x1)/MAC(5CB901C761F8,0x0)/IPv6(0000:0000:0000:0000:0000:0000:0000:0000)/Uri()'
            },
            {
                'BootOptionNumber': '0015',
                'BootString': 'Embedded FlexibleLOM 1 Port 2 : HP FlexFabric 10Gb 2-port 536FLB Adapter - CNA - HP FlexFabric 10Gb 2-port 536FLB Adapter - NIC (PXE IPv6)',
                'CorrelatableID': 'PciRoot(0x2)/Pci(0x0,0x0)/Pci(0x0,0x1)',
                'StructuredBootString': 'NIC.FlexLOM.1.2.IPv6',
                'UEFIDevicePath': 'PciRoot(0x2)/Pci(0x0,0x0)/Pci(0x0,0x1)/MAC(5CB901C761F8,0x0)/IPv6(0000:0000:0000:0000:0000:0000:0000:0000)'
            }
        ],
        'Name': 'Boot Order Current Settings',
        'PersistentBootConfigOrder': [
            "HD.SD.1.2",
            "HD.EmbRAID.1.3",
            "HD.EmbRAID.1.2",
            "Generic.USB.1.1",
            "NIC.FlexLOM.1.1.Httpv4",
            "NIC.FlexLOM.1.1.IPv4",
            "NIC.FlexLOM.1.2.Httpv4",
            "NIC.FlexLOM.1.2.IPv4",
            "NIC.FlexLOM.1.1.Httpv6",
            "NIC.FlexLOM.1.1.IPv6",
            "NIC.FlexLOM.1.2.Httpv6",
            "NIC.FlexLOM.1.2.IPv6"
        ]
    }
}

# COMPLIANCE DATA

profile1_compliant = {
    "name": PROFILE1_NAME,
    "compliance-preview": {
        "type": "ServerProfileCompliancePreviewV1",
        "automaticUpdates": [],
        "manualUpdates": []}
}

profile2_compliant = {
    "name": PROFILE2_NAME,
    "compliance-preview": {
        "type": "ServerProfileCompliancePreviewV1",
        "automaticUpdates": [],
        "manualUpdates": []}
}

profile1_sp_noncompliant = {
    "name": PROFILE1_NAME,
    "compliance-preview": {
        "type": "ServerProfileCompliancePreviewV1",
        "automaticUpdates": [
            "Change boot order to [SD]."
        ],
        "manualUpdates": []}
}

profile2_sp_noncompliant = {
    "name": PROFILE2_NAME,
    "compliance-preview": {
        "type": "ServerProfileCompliancePreviewV1",
        "automaticUpdates": [
            "Change boot order to [SD]."
        ],
        "manualUpdates": []}
}

profile1_spt_noncompliant = {
    "name": PROFILE1_NAME,
    "compliance-preview": {
        "type": "ServerProfileCompliancePreviewV1",
        "automaticUpdates": [
            "Change boot order to [HardDisk]."
        ],
        "manualUpdates": []}
}

profile2_spt_noncompliant = {
    "name": PROFILE2_NAME,
    "compliance-preview": {
        "type": "ServerProfileCompliancePreviewV1",
        "automaticUpdates": [
            "Change boot order to [HardDisk]."
        ],
        "manualUpdates": []}
}

ts0_create_profiles = [
    create_profile_gen9.copy(),
    create_profile_gen10.copy(),
]

ts0_ris_after_create_pending = [
    ts0_ris_after_create_pending_gen9.copy(),
    ts0_ris_after_create_pending_gen10.copy(),
]

ts0_ris_after_create = [
    ts0_ris_after_create_gen9.copy(),
    ts0_ris_after_create_gen10.copy(),
]

ts1_edit_profiles1 = [
    edit_profile_gen9.copy(),
    edit_profile_gen10.copy(),
]

ts1_ris_after_edit1_pending = [
    ts1_ris_after_edit1_pending_gen9.copy(),
    ts1_ris_after_edit1_pending_gen10.copy(),
]

ts1_ris_after_edit1 = [
    ts1_ris_after_edit1_gen9.copy(),
    ts1_ris_after_edit1_gen10.copy(),
]

ts1_edit_profiles2 = [
    edit2_profile_gen9.copy(),
    edit2_profile_gen10.copy(),
]

ts2_delete_profiles_before_move = [
    create_profile_gen10.copy(),
]

ts2_move_profiles = [
    move_profile_to_different_sht.copy(),
]

ts2_ris_after_move = [
    ts0_ris_after_move_gen10.copy(),
]

ts2_clean_up = [
    edit2_profile_gen9.copy(),
    edit2_profile_gen10.copy(),
]

ts3_create_templates = [
    create_template_gen9.copy(),
    create_template_gen9_2.copy(),
    create_template_gen10.copy(),
    create_template_gen10_2.copy(),
]

ts4_edit_templates = [
    edit_template_gen9.copy(),
    edit_template_gen9_2.copy(),
    edit_template_gen10.copy(),
    edit_template_gen10_2.copy(),
]

ts5_create_templates = [
    create_template_gen9.copy(),
    create_template_gen10.copy(),
]

ts5_create_sp_from_spt = [
    create_sp_from_spt_gen9.copy(),
    create_sp_from_spt_gen10.copy(),
]

sp_compliance = [
    profile1_compliant.copy(),
    profile2_compliant.copy(),
]

ts6_create_sp_from_spt = [
    create_noncompliant_sp_from_spt_gen9.copy(),
    create_noncompliant_sp_from_spt_gen10.copy(),
]

ts6_non_compliance = [
    profile1_sp_noncompliant.copy(),
    profile2_sp_noncompliant.copy(),
]

ts7_edit_templates = [
    edit_template_gen9.copy(),
    edit_template_gen10.copy(),
]

ts7_non_compliance = [
    profile1_spt_noncompliant.copy(),
    profile2_spt_noncompliant.copy(),
]

#
##
# Added by Ron Soto  Negative Test Cases for OVS27399
##
#

# OVTC36891
OVTC36891_Neg_LegBIOS_SD_Primary_Gen9 = {
    "type": "ServerProfileV9",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareUri': 'SH:' + PROFILE1_SH,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": ['SD'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS",
    },
    "connectionSettings": {
        "connections": []
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    }
}

OVTC36891_Neg_LegBIOS_SD_Primary_Gen10 = {
    "type": "ServerProfileV9",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareUri': 'SH:' + PROFILE2_SH,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE2_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": ['SD'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS",
    },
    "connectionSettings": {
        "connections": []
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    }
}

OVTC36891_Neg_Add_LegBIOS_SD_Primary = [
    {'keyword': 'Add Server Profile',
     'argument': OVTC36891_Neg_LegBIOS_SD_Primary_Gen9.copy(),
     'taskState': 'Error',
     'timeout': '30',
     'errorMessage': 'SDBOOT_Invalid_settings'},
    {'keyword': 'Add Server Profile',
     'argument': OVTC36891_Neg_LegBIOS_SD_Primary_Gen10.copy(),
     'taskState': 'Error',
     'timeout': '30',
     'errorMessage': 'SDBOOT_Invalid_settings'}
]

# OVTC36893
OVS27399_Add_LegBIOS_For_Neg_Edit = [
    {"type": "ServerProfileV9",
     "serialNumberType": "Physical",
     "macType": "Physical",
     "wwnType": "Physical",
     "serverHardwareUri": 'SH:' + PROFILE1_SH,
     "enclosureGroupUri": "EG:" + EG_NAME,
     "name": PROFILE1_NAME,
     "affinity": "Bay",
     "bios": {
         "manageBios": False
     },
     "boot": {
         "order": ['HardDisk'],
         "manageBoot": True
     },
     "bootMode": {
         "manageMode": True,
         "mode": "BIOS",
     },
     "connectionSettings": {
         "connections": []
     },
     "sanStorage": {
         'manageSanStorage': False,
         'volumeAttachments': [],
     },
     "localStorage": {
         "sasLogicalJBODs": [],
         "controllers": []
     }},
    {"type": "ServerProfileV9",
     "serialNumberType": "Physical",
     "macType": "Physical",
     "wwnType": "Physical",
     "serverHardwareUri": 'SH:' + PROFILE2_SH,
     "enclosureGroupUri": "EG:" + EG_NAME,
     "name": PROFILE2_NAME,
     "affinity": "Bay",
     "bios": {
         "manageBios": False
     },
     "boot": {
         "order": ['HardDisk'],
         "manageBoot": True
     },
     "bootMode": {
         "manageMode": True,
         "mode": "BIOS",
     },
     "connectionSettings": {
         "connections": []
     },
     "sanStorage": {
         'manageSanStorage': False,
         'volumeAttachments': [],
     },
     "localStorage": {
         "sasLogicalJBODs": [],
         "controllers": []
     }},
]

OVTC36893_Neg_Edit_LegBIOS_SD_Primary = [
    {'keyword': 'Edit Server Profile',
     'argument': OVTC36891_Neg_LegBIOS_SD_Primary_Gen9.copy(),
     'taskState': 'Error',
     'timeout': '30',
     'errorMessage': 'SDBOOT_Invalid_settings'},
    {'keyword': 'Edit Server Profile',
     'argument': OVTC36891_Neg_LegBIOS_SD_Primary_Gen10.copy(),
     'taskState': 'Error',
     'timeout': '30',
     'errorMessage': 'SDBOOT_Invalid_settings'}
]

OVTC36894_Neg_Edit_SDBoot_To_Invalid = [
    {'keyword': 'Edit Server Profile',
     'argument': copy.deepcopy(create_profile_gen9),
     'taskState': 'Error',
     'timeout': '30',
     'errorMessage': 'Invalid_Boot_Value'},
    {'keyword': 'Edit Server Profile',
     'argument': copy.deepcopy(create_profile_gen10),
     'taskState': 'Error',
     'timeout': '30',
     'errorMessage': 'Invalid_Boot_Value'}
]

# set boot order to invalid value for UEFI.  Uses Valid DTO from
# create_profile_gen(9|10) to create profiles for edit to this invalid
# setting.
for profile in OVTC36894_Neg_Edit_SDBoot_To_Invalid:
    profile['argument']['boot']['order'] = ['CD']

# Neg tests for HW that doesn't support SD Boot
Gen8_For_Neg = [
    {"type": "ServerProfileV9",
     "serverHardwareUri": "SH:" + PROFILE1_GEN8_SH,
     "enclosureGroupUri": "EG:" + EG_NAME,
     "serialNumberType": "Virtual",
     "iscsiInitiatorNameType": "AutoGenerated",
     "macType": "Virtual",
     "wwnType": "Virtual",
     "name": "Gen8_Profile",
     "description": "",
     "affinity": "Bay",
     "connectionSettings": {"connections": []},
     "boot": {"manageBoot": True,
              "order": ["CD",
                        "Floppy",
                        "USB",
                        "HardDisk",
                        "PXE"]},
     "bootMode": None,
     "firmware": {"manageFirmware": False,
                  "firmwareBaselineUri": "",
                  "forceInstallFirmware": False,
                  "firmwareInstallType": None,
                  "firmwareScheduleDateTime": "",
                  "firmwareActivationType": "Immediate"},
     "bios": {"manageBios": False,
              "overriddenSettings": []},
     "hideUnusedFlexNics": True,
     "iscsiInitiatorName": "",
     "osDeploymentSettings": None,
     "localStorage": {"sasLogicalJBODs": [],
                      "controllers": []},
     "sanStorage": None,
     "initialScopeUris": []
     }
]

Neg_SD_Primary = {
    "type": "ServerProfileV9",
    "serverHardwareUri": "SH:" + PROFILE1_GEN8_SH,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": "Gen8_Profile",
    "description": "",
    "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": True,
             "order": ["SD",
                       "Floppy",
                       "USB",
                       "HardDisk",
                       "PXE"]},
    "bootMode": None,
    "firmware": {"manageFirmware": False,
                 "firmwareBaselineUri": "",
                 "forceInstallFirmware": False,
                 "firmwareInstallType": None,
                 "firmwareScheduleDateTime": "",
                 "firmwareActivationType": "Immediate"},
    "bios": {"manageBios": False,
             "overriddenSettings": []},
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {"sasLogicalJBODs": [],
                     "controllers": []},
    "sanStorage": None,
    "initialScopeUris": []
}

Neg_Add_SD_Primary = [
    {'keyword': 'Add Server Profile',
     'argument': Neg_SD_Primary.copy(),
     'taskState': 'Error',
     'timeout': '2',
     'errorMessage': 'SDBOOT_Invalid_settings'}]

Neg_Edit_SD_Primary = [
    {'keyword': 'Edit Server Profile',
     'argument': Neg_SD_Primary.copy(),
     'taskState': 'Error',
     'timeout': '2',
     'errorMessage': 'SDBOOT_Invalid_settings'}]

Neg_move_Gen9SD_to_Gen8 = [
    {'keyword': 'Edit Server Profile',
     'argument': ts0_create_profiles[0].copy(),
     'taskState': 'Error',
     'timeout': '2',
     'errorMessage': 'SDBOOT_Invalid_settings'}]
# set hardware to Gen8 server
for profile in Neg_move_Gen9SD_to_Gen8:
    profile['argument']['serverHardwareUri'] = "SH:" + PROFILE1_GEN8_SH

DL_Neg = {
    "type": "ServerProfileV9",
    "serverHardwareUri": "SH:" + PROFILE1_DL_SH,
    "iscsiInitiatorNameType": "AutoGenerated",
    "name": "Gen8_Profile",
    "description": "",
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": True,
             "order": ["SD",
                       "USB",
                       "HardDisk",
                       "PXE"]},
    "bootMode": {"manageMode": True,
                 "mode": "BIOS",
                 "secureBoot": "Unmanaged"},
    "firmware": {"manageFirmware": False,
                 "firmwareBaselineUri": "",
                 "forceInstallFirmware": False,
                 "firmwareInstallType": None,
                 "firmwareScheduleDateTime": "",
                 "firmwareActivationType": "Immediate"},
    "bios": {"manageBios": False,
             "overriddenSettings": []},
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {"sasLogicalJBODs": [],
                     "controllers": []},
    "sanStorage": None,
    "initialScopeUris": []
}

DL_Neg_Create_SP = [
    {'keyword': 'Add Server Profile',
     'argument': DL_Neg.copy(),
     'taskState': 'Error',
     'timeout': '2',
     'errorMessage': 'SDBOOT_Invalid_settings'}]


DL_For_Neg = [
    {"type": "ServerProfileV9",
     "serverHardwareUri": "SH:" + PROFILE1_DL_SH,
     "iscsiInitiatorNameType": "AutoGenerated",
     "name": "Gen8_Profile",
     "description": "",
     "connectionSettings": {"connections": []},
     "boot": {"manageBoot": True,
              "order": ["CD",
                        "USB",
                        "HardDisk",
                        "PXE"]},
     "bootMode": {"manageMode": True,
                  "mode": "BIOS",
                  "secureBoot": "Unmanaged"},
     "firmware": {"manageFirmware": False,
                  "firmwareBaselineUri": "",
                  "forceInstallFirmware": False,
                  "firmwareInstallType": None,
                  "firmwareScheduleDateTime": "",
                  "firmwareActivationType": "Immediate"},
     "bios": {"manageBios": False,
              "overriddenSettings": []},
     "hideUnusedFlexNics": True,
     "iscsiInitiatorName": "",
     "osDeploymentSettings": None,
     "localStorage": {"sasLogicalJBODs": [],
                      "controllers": []},
     "sanStorage": None,
     "initialScopeUris": []
     }
]

DL_Neg_Edit_SP = [
    {'keyword': 'Edit Server Profile',
     'argument': DL_Neg.copy(),
     'taskState': 'Error',
     'timeout': '2',
     'errorMessage': 'SDBOOT_Invalid_settings'}]

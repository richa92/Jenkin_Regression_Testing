import copy

admin_credentials = {
    'userName': 'Administrator',
    'password': 'wpsthpvse1'
}

ilo_credentials = {
    'username': 'Administrator',
    'password': 'hpvse123'
}

# EG
EG_NAME = 'EG1'

# Enclosures
ENC2 = 'CN754404R6'

# Server Hardware
ENC2SHBAY4 = '%s, bay 1' % ENC2
ENC2SHBAY8 = '%s, bay 8' % ENC2

# Server Hardware Types
SERVER_HARDWARE_TYPE1 = 'SY 480 Gen9:3:HP Synergy 3820C 10/20Gb CNA'
SERVER_HARDWARE_TYPE2 = 'SY 480 Gen10:3:Synergy 3820C 10/20Gb CNA'

# Profiles
PROFILE1_NAME = 'SD_Boot_Gen9'
PROFILE1_SH = ENC2SHBAY4
PROFILE1_SHT = SERVER_HARDWARE_TYPE1
PROFILE2_NAME = 'SD_Boot_Gen10'
PROFILE2_SH = ENC2SHBAY8
PROFILE2_SHT = SERVER_HARDWARE_TYPE2
PROFILE3_NAME = 'SD_Boot_Gen9_2'
PROFILE3_SHT = SERVER_HARDWARE_TYPE1
PROFILE4_NAME = 'SD_Boot_Gen10_2'
PROFILE4_SHT = SERVER_HARDWARE_TYPE2

# PROFILE DATA

# Create profile with SD Boot on Gen 9
create_profile_gen9 = {
    "type": "ServerProfileV10",
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
    "type": "ServerProfileV10",
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
    "type": "ServerProfileV10",
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
    "type": "ServerProfileV10",
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
    "type": "ServerProfileV10",
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
    "type": "ServerProfileV10",
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
    "type": "ServerProfileV10",
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
    "type": "ServerProfileTemplateV6",
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
    "type": "ServerProfileTemplateV6",
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
    "type": "ServerProfileTemplateV6",
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
    "type": "ServerProfileTemplateV6",
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
    "type": "ServerProfileTemplateV6",
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
    "type": "ServerProfileTemplateV6",
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
    "type": "ServerProfileTemplateV6",
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
    "type": "ServerProfileTemplateV6",
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
    "type": "ServerProfileV10",
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
    "type": "ServerProfileV10",
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
    "type": "ServerProfileV10",
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
    "type": "ServerProfileV10",
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

ts0_ris_after_create_gen9 = {
    "server": PROFILE1_SH,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/bios/boot",
    "validate": {
        'BootSources': [
            {'BootString': 'Internal SD Card 1 : Generic Ultra Fast Media Reader',
             'CorrelatableID': 'PciRoot(0x0)/Pci(0x1D,0x0)/USB(0x0,0x0)/USB(0x2,0x0)/USB(0x0,0x0)',
             'StructuredBootString': 'HD.SD.1.1',
             'UEFIDevicePath': 'PciRoot(0x0)/Pci(0x1D,0x0)/USB(0x0,0x0)/USB(0x2,0x0)/USB(0x0,0x0)'},
            {'BootString': 'Embedded RAID 1 : Smart Array P240nr Controller - 136.70 GiB, RAID 0 Logical Drive(Target:0, Lun:0)',
             'CorrelatableID': 'PciRoot(0x0)/Pci(0x1,0x0)/Pci(0x0,0x0)',
             'StructuredBootString': 'HD.Emb.1.2',
             'UEFIDevicePath': 'PciRoot(0x0)/Pci(0x1,0x0)/Pci(0x0,0x0)/Scsi(0x0,0x0)'},
            {'BootString': 'Generic USB Boot',
             'CorrelatableID': 'UsbClass(0xFFFF,0xFFFF,0xFF,0xFF,0xFF)',
             'StructuredBootString': 'Generic.USB.1.1',
             'UEFIDevicePath': 'UsbClass(0xFFFF,0xFFFF,0xFF,0xFF,0xFF)'},
            {'BootString': 'Slot 3 Port 1 : HPE Synergy 3820C 10/20Gb Converged Network Adapter - CNA - HPE Synergy 3820C 10/20Gb Converged Network Adapter - NIC (PXE IPv4) ',
             'CorrelatableID': 'PciRoot(0x0)/Pci(0x3,0x2)/Pci(0x0,0x0)',
             'StructuredBootString': 'NIC.Slot.3.1.IPv4',
             'UEFIDevicePath': 'PciRoot(0x0)/Pci(0x3,0x2)/Pci(0x0,0x0)/MAC(9457A5088E30,0x0)/IPv4(0.0.0.0)'},
            {'BootString': 'Slot 3 Port 1 : HPE Synergy 3820C 10/20Gb Converged Network Adapter - CNA - HPE Synergy 3820C 10/20Gb Converged Network Adapter - NIC (PXE IPv6) ',
             'CorrelatableID': 'PciRoot(0x0)/Pci(0x3,0x2)/Pci(0x0,0x0)',
             'StructuredBootString': 'NIC.Slot.3.1.IPv6',
             'UEFIDevicePath': 'PciRoot(0x0)/Pci(0x3,0x2)/Pci(0x0,0x0)/MAC(9457A5088E30,0x0)/IPv6(0000:0000:0000:0000:0000:0000:0000:0000)'}
        ],
        'DefaultBootOrder': [
            'Floppy',
            'Cd',
            'Usb',
            'EmbeddedStorage',
            'PcieSlotStorage',
            'EmbeddedFlexLOM',
            'PcieSlotNic',
            'UefiShell'
        ],
        'Description': 'This is the Server Boot Order Current Settings',
        'Name': 'Boot Order Current Settings',
        'PersistentBootConfigOrder': [
            'HD.SD.1.1',
            'HD.Emb.1.2',
            'Generic.USB.1.1',
            'NIC.Slot.3.1.IPv4',
            'NIC.Slot.3.1.IPv6'],
    }
}

ts0_ris_after_create_gen10 = {
    "server": PROFILE2_SH,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/bios/boot",
    "validate": {
        'BootSources': [
            {'BootOptionNumber': '000B',
             'BootString': 'Internal SD Card 1 : Generic USB3.0-CRW',
             'CorrelatableID': 'PciRoot(0x0)/Pci(0x14,0x0)/USB(0x13,0x0)',
             'StructuredBootString': 'HD.SD.1.2',
             'UEFIDevicePath': 'PciRoot(0x0)/Pci(0x14,0x0)/USB(0x13,0x0)'},
            {'BootOptionNumber': '000C',
             'BootString': 'Embedded RAID 1 : HPE Smart Array P204i-c SR Gen10 - Size:74.5 GiB Port:1I Bay:1 Box:1',
             'CorrelatableID': 'PciRoot(0x1)/Pci(0x2,0x0)/Pci(0x0,0x0)',
             'StructuredBootString': 'HD.EmbRAID.2.1',
             'UEFIDevicePath': 'PciRoot(0x1)/Pci(0x2,0x0)/Pci(0x0,0x0)/Scsi(0x0,0x4000)'},
            {'BootOptionNumber': '000D',
             'BootString': 'Embedded RAID 1 : HPE Smart Array P204i-c SR Gen10 - 74.4 GiB, RAID0 Logical Drive 1(Target:0, Lun:0)',
             'CorrelatableID': 'PciRoot(0x1)/Pci(0x2,0x0)/Pci(0x0,0x0)',
             'StructuredBootString': 'HD.EmbRAID.2.2',
             'UEFIDevicePath': 'PciRoot(0x1)/Pci(0x2,0x0)/Pci(0x0,0x0)/Scsi(0x0,0x0)'},
            {'BootOptionNumber': '000A',
             'BootString': 'Generic USB Boot',
             'CorrelatableID': 'UsbClass(0xFFFF,0xFFFF,0xFF,0xFF,0xFF)',
             'StructuredBootString': 'Generic.USB.1.1',
             'UEFIDevicePath': 'UsbClass(0xFFFF,0xFFFF,0xFF,0xFF,0xFF)'},
            {'BootOptionNumber': '000E',
             'BootString': 'Slot 3 Port 1 : HPE Synergy 3820C 10/20Gb Converged Network Adapter - CNA - HPE Synergy 3820C 10/20Gb Converged Network Adapter - NIC (HTTP(S) IPv4)',
             'CorrelatableID': 'PciRoot(0x2)/Pci(0x2,0x0)/Pci(0x0,0x0)',
             'StructuredBootString': 'NIC.Slot.3.1.Httpv4',
             'UEFIDevicePath': 'PciRoot(0x2)/Pci(0x2,0x0)/Pci(0x0,0x0)/MAC(9CDC719D54D0,0x0)/IPv4(0.0.0.0)/Uri()'},
            {'BootOptionNumber': '0010',
             'BootString': 'Slot 3 Port 1 : HPE Synergy 3820C 10/20Gb Converged Network Adapter - CNA - HPE Synergy 3820C 10/20Gb Converged Network Adapter - NIC (PXE IPv4)',
             'CorrelatableID': 'PciRoot(0x2)/Pci(0x2,0x0)/Pci(0x0,0x0)',
             'StructuredBootString': 'NIC.Slot.3.1.IPv4',
             'UEFIDevicePath': 'PciRoot(0x2)/Pci(0x2,0x0)/Pci(0x0,0x0)/MAC(9CDC719D54D0,0x0)/IPv4(0.0.0.0)'},
            {'BootOptionNumber': '000F',
             'BootString': 'Slot 3 Port 1 : HPE Synergy 3820C 10/20Gb Converged Network Adapter - CNA - HPE Synergy 3820C 10/20Gb Converged Network Adapter - NIC (HTTP(S) IPv6)',
             'CorrelatableID': 'PciRoot(0x2)/Pci(0x2,0x0)/Pci(0x0,0x0)',
             'StructuredBootString': 'NIC.Slot.3.1.Httpv6',
             'UEFIDevicePath': 'PciRoot(0x2)/Pci(0x2,0x0)/Pci(0x0,0x0)/MAC(9CDC719D54D0,0x0)/IPv6(0000:0000:0000:0000:0000:0000:0000:0000)/Uri()'},
            {'BootOptionNumber': '0011',
             'BootString': 'Slot 3 Port 1 : HPE Synergy 3820C 10/20Gb Converged Network Adapter - CNA - HPE Synergy 3820C 10/20Gb Converged Network Adapter - NIC (PXE IPv6)',
             'CorrelatableID': 'PciRoot(0x2)/Pci(0x2,0x0)/Pci(0x0,0x0)',
             'StructuredBootString': 'NIC.Slot.3.1.IPv6',
             'UEFIDevicePath': 'PciRoot(0x2)/Pci(0x2,0x0)/Pci(0x0,0x0)/MAC(9CDC719D54D0,0x0)/IPv6(0000:0000:0000:0000:0000:0000:0000:0000)'}
        ],
        'DefaultBootOrder': [
            'Cd',
            'Usb',
            'EmbeddedStorage',
            'PcieSlotStorage',
            'EmbeddedFlexLOM',
            'PcieSlotNic',
            'UefiShell'
        ],
        'Name': 'Boot Order Current Settings',
        'PersistentBootConfigOrder': [
            'HD.SD.1.2',
            'HD.EmbRAID.2.1',
            'HD.EmbRAID.2.2',
            'Generic.USB.1.1',
            'NIC.Slot.3.1.Httpv4',
            'NIC.Slot.3.1.IPv4',
            'NIC.Slot.3.1.Httpv6',
            'NIC.Slot.3.1.IPv6'
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
            {'BootString': 'Embedded RAID 1 : Smart Array P240nr Controller - 136.70 GiB, RAID 0 Logical Drive(Target:0, Lun:0)',
             'CorrelatableID': 'PciRoot(0x0)/Pci(0x1,0x0)/Pci(0x0,0x0)',
             'StructuredBootString': 'HD.Emb.1.2',
             'UEFIDevicePath': 'PciRoot(0x0)/Pci(0x1,0x0)/Pci(0x0,0x0)/Scsi(0x0,0x0)'},
            {'BootString': 'Internal SD Card 1 : Generic Ultra Fast Media Reader',
             'CorrelatableID': 'PciRoot(0x0)/Pci(0x1D,0x0)/USB(0x0,0x0)/USB(0x2,0x0)/USB(0x0,0x0)',
             'StructuredBootString': 'HD.SD.1.1',
             'UEFIDevicePath': 'PciRoot(0x0)/Pci(0x1D,0x0)/USB(0x0,0x0)/USB(0x2,0x0)/USB(0x0,0x0)'},
            {'BootString': 'Generic USB Boot',
             'CorrelatableID': 'UsbClass(0xFFFF,0xFFFF,0xFF,0xFF,0xFF)',
             'StructuredBootString': 'Generic.USB.1.1',
             'UEFIDevicePath': 'UsbClass(0xFFFF,0xFFFF,0xFF,0xFF,0xFF)'},
            {'BootString': 'Slot 3 Port 1 : HPE Synergy 3820C 10/20Gb Converged Network Adapter - CNA - HPE Synergy 3820C 10/20Gb Converged Network Adapter - NIC (PXE IPv4) ',
             'CorrelatableID': 'PciRoot(0x0)/Pci(0x3,0x2)/Pci(0x0,0x0)',
             'StructuredBootString': 'NIC.Slot.3.1.IPv4',
             'UEFIDevicePath': 'PciRoot(0x0)/Pci(0x3,0x2)/Pci(0x0,0x0)/MAC(9457A5088E30,0x0)/IPv4(0.0.0.0)'},
            {'BootString': 'Slot 3 Port 1 : HPE Synergy 3820C 10/20Gb Converged Network Adapter - CNA - HPE Synergy 3820C 10/20Gb Converged Network Adapter - NIC (PXE IPv6) ',
             'CorrelatableID': 'PciRoot(0x0)/Pci(0x3,0x2)/Pci(0x0,0x0)',
             'StructuredBootString': 'NIC.Slot.3.1.IPv6',
             'UEFIDevicePath': 'PciRoot(0x0)/Pci(0x3,0x2)/Pci(0x0,0x0)/MAC(9457A5088E30,0x0)/IPv6(0000:0000:0000:0000:0000:0000:0000:0000)'}
        ],
        'DefaultBootOrder': [
            'Floppy',
            'Cd',
            'Usb',
            'EmbeddedStorage',
            'PcieSlotStorage',
            'EmbeddedFlexLOM',
            'PcieSlotNic',
            'UefiShell'
        ],
        'Description': 'This is the Server Boot Order Current Settings',
        'Name': 'Boot Order Current Settings',
        'PersistentBootConfigOrder': ['HD.Emb.1.2', 'HD.SD.1.1', 'Generic.USB.1.1', 'NIC.Slot.3.1.IPv4', 'NIC.Slot.3.1.IPv6'],
    }
}

ts1_ris_after_edit1_gen10 = {
    "server": PROFILE2_SH,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/bios/boot",
    "validate": {
        'BootSources': [
            {'BootOptionNumber': '000C',
             'BootString': 'Embedded RAID 1 : HPE Smart Array P204i-c SR Gen10 - Size:74.5 GiB Port:1I Bay:1 Box:1',
             'CorrelatableID': 'PciRoot(0x1)/Pci(0x2,0x0)/Pci(0x0,0x0)',
             'StructuredBootString': 'HD.EmbRAID.2.1',
             'UEFIDevicePath': 'PciRoot(0x1)/Pci(0x2,0x0)/Pci(0x0,0x0)/Scsi(0x0,0x4000)'},
            {'BootOptionNumber': '000D',
             'BootString': 'Embedded RAID 1 : HPE Smart Array P204i-c SR Gen10 - 74.4 GiB, RAID0 Logical Drive 1(Target:0, Lun:0)',
             'CorrelatableID': 'PciRoot(0x1)/Pci(0x2,0x0)/Pci(0x0,0x0)',
             'StructuredBootString': 'HD.EmbRAID.2.2',
             'UEFIDevicePath': 'PciRoot(0x1)/Pci(0x2,0x0)/Pci(0x0,0x0)/Scsi(0x0,0x0)'},
            {'BootOptionNumber': '000B',
             'BootString': 'Internal SD Card 1 : Generic USB3.0-CRW',
             'CorrelatableID': 'PciRoot(0x0)/Pci(0x14,0x0)/USB(0x13,0x0)',
             'StructuredBootString': 'HD.SD.1.2',
             'UEFIDevicePath': 'PciRoot(0x0)/Pci(0x14,0x0)/USB(0x13,0x0)'},
            {'BootOptionNumber': '000A',
             'BootString': 'Generic USB Boot',
             'CorrelatableID': 'UsbClass(0xFFFF,0xFFFF,0xFF,0xFF,0xFF)',
             'StructuredBootString': 'Generic.USB.1.1',
             'UEFIDevicePath': 'UsbClass(0xFFFF,0xFFFF,0xFF,0xFF,0xFF)'},
            {'BootOptionNumber': '000E',
             'BootString': 'Slot 3 Port 1 : HPE Synergy 3820C 10/20Gb Converged Network Adapter - CNA - HPE Synergy 3820C 10/20Gb Converged Network Adapter - NIC (HTTP(S) IPv4)',
             'CorrelatableID': 'PciRoot(0x2)/Pci(0x2,0x0)/Pci(0x0,0x0)',
             'StructuredBootString': 'NIC.Slot.3.1.Httpv4',
             'UEFIDevicePath': 'PciRoot(0x2)/Pci(0x2,0x0)/Pci(0x0,0x0)/MAC(9CDC719D54D0,0x0)/IPv4(0.0.0.0)/Uri()'},
            {'BootOptionNumber': '0010',
             'BootString': 'Slot 3 Port 1 : HPE Synergy 3820C 10/20Gb Converged Network Adapter - CNA - HPE Synergy 3820C 10/20Gb Converged Network Adapter - NIC (PXE IPv4)',
             'CorrelatableID': 'PciRoot(0x2)/Pci(0x2,0x0)/Pci(0x0,0x0)',
             'StructuredBootString': 'NIC.Slot.3.1.IPv4',
             'UEFIDevicePath': 'PciRoot(0x2)/Pci(0x2,0x0)/Pci(0x0,0x0)/MAC(9CDC719D54D0,0x0)/IPv4(0.0.0.0)'},
            {'BootOptionNumber': '000F',
             'BootString': 'Slot 3 Port 1 : HPE Synergy 3820C 10/20Gb Converged Network Adapter - CNA - HPE Synergy 3820C 10/20Gb Converged Network Adapter - NIC (HTTP(S) IPv6)',
             'CorrelatableID': 'PciRoot(0x2)/Pci(0x2,0x0)/Pci(0x0,0x0)',
             'StructuredBootString': 'NIC.Slot.3.1.Httpv6',
             'UEFIDevicePath': 'PciRoot(0x2)/Pci(0x2,0x0)/Pci(0x0,0x0)/MAC(9CDC719D54D0,0x0)/IPv6(0000:0000:0000:0000:0000:0000:0000:0000)/Uri()'},
            {'BootOptionNumber': '0011',
             'BootString': 'Slot 3 Port 1 : HPE Synergy 3820C 10/20Gb Converged Network Adapter - CNA - HPE Synergy 3820C 10/20Gb Converged Network Adapter - NIC (PXE IPv6)',
             'CorrelatableID': 'PciRoot(0x2)/Pci(0x2,0x0)/Pci(0x0,0x0)',
             'StructuredBootString': 'NIC.Slot.3.1.IPv6',
             'UEFIDevicePath': 'PciRoot(0x2)/Pci(0x2,0x0)/Pci(0x0,0x0)/MAC(9CDC719D54D0,0x0)/IPv6(0000:0000:0000:0000:0000:0000:0000:0000)'}
        ],
        'DefaultBootOrder': [
            'Cd',
            'Usb',
            'EmbeddedStorage',
            'PcieSlotStorage',
            'EmbeddedFlexLOM',
            'PcieSlotNic',
            'UefiShell'
        ],
        'Id': 'boot',
        'Name': 'Boot Order Current Settings',
        'PersistentBootConfigOrder': [
            'HD.EmbRAID.2.1',
            'HD.EmbRAID.2.2',
            'HD.SD.1.2',
            'Generic.USB.1.1',
            'NIC.Slot.3.1.Httpv4',
            'NIC.Slot.3.1.IPv4',
            'NIC.Slot.3.1.Httpv6',
            'NIC.Slot.3.1.IPv6'
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

ts0_ris_after_create = [
    ts0_ris_after_create_gen9.copy(),
    ts0_ris_after_create_gen10.copy(),
]

ts1_edit_profiles1 = [
    edit_profile_gen9.copy(),
    edit_profile_gen10.copy(),
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
    ts0_ris_after_create_gen10.copy(),
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
    "type": "ServerProfileV10",
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
    "type": "ServerProfileV10",
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
     'errorMessage': 'SDBOOT_Invalid_settings'
     }
]

# OVTC36893
OVS27399_Add_LegBIOS_For_Neg_Edit = [
    {"type": "ServerProfileV10",
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
    {"type": "ServerProfileV10",
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
     }
     },
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

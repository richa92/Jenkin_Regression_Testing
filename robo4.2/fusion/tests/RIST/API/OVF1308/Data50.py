from dto import *
from env_variables import *

# Potash interconnects
ENC1ICBAY3 = '%s, interconnect 3' % ENC1
ENC2ICBAY6 = '%s, interconnect 6' % ENC2

# Natasha SAS interconnects
ENC1SASICBAY1 = '%s, interconnect 1' % ENC1
ENC1SASICBAY4 = '%s, interconnect 4' % ENC1

# Drive Enclosures (Bigbird)
ENC1DEBAY1 = '%s, bay 1' % ENC1

# Server Hardware
ENC1SHBAY3 = '%s, bay 3' % ENC1
ENC1SHBAY5 = '%s, bay 5' % ENC1
ENC1SHBAY7 = '%s, bay 7' % ENC1
ENC2SHBAY1 = '%s, bay 1' % ENC2
ENC2SHBAY2 = '%s, bay 2' % ENC2
ENC2SHBAY3 = '%s, bay 3' % ENC2
ENC2SHBAY5 = '%s, bay 5' % ENC2
ENC2SHBAY7 = '%s, bay 7' % ENC2
ENC2SHBAY8 = '%s, bay 8' % ENC2
ENC3SHBAY1 = '%s, bay 1' % ENC3
ENC3SHBAY5 = '%s, bay 5' % ENC3

# PROFILE1 SETTINGS
PROFILE1_NAME = 'ENC2SHBAY7_Profile1_PXE_Boot_Options_Test'
PROFILE1_SHT = 'SY 480 Gen10:3:Synergy 3820C 10/20Gb CNA'
PROFILE1_SH = "SH:" + ENC2SHBAY7

# PROFILE2 SETTINGS
PROFILE2_NAME = 'ENC2SHBAY8_Profile2_PXE_Boot_Options_Test'
PROFILE2_SHT = 'SY 480 Gen10:3:Synergy 3820C 10/20Gb CNA'
PROFILE2_SH = "SH:" + ENC2SHBAY8

# 2 Connections IPv4 Only
two_connections_ipv4 = {
    "type": SERVER_PROFILE_TYPE,
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareUri': PROFILE1_SH,
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
        "pxeBootPolicy": "IPv4"
    },
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "PXE-boot-primary",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "PXE",
                },
            }, {
                "id": 2,
                "name": "iSCSI-boot-secondary",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Secondary",
                    "ethernetBootType": "PXE",
                },
            }
        ]
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

# one connection IPv6 Only
one_connection_ipv6 = {
    "type": SERVER_PROFILE_TYPE,
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareUri': PROFILE2_SH,
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
        "mode": "UEFI",
        "pxeBootPolicy": "IPv6"
    },
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "PXE-boot-primary",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "PXE",
                },
            }, ]
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

# one connection IPv6 Only edit to two connections auto
one_connection_ipv6_edit1 = {
    "type": SERVER_PROFILE_TYPE,
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareUri': PROFILE2_SH,
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
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "PXE-boot-primary",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "PXE",
                },
            }, {
                "id": 2,
                "name": "iSCSI-boot-secondary",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Secondary",
                    "ethernetBootType": "PXE",
                },
            }
        ]
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

# 2 Connections IPv4 Only edit to one connection IPv6
two_connections_ipv4_edit1 = {
    "type": SERVER_PROFILE_TYPE,
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareUri': PROFILE1_SH,
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
        "pxeBootPolicy": "IPv6"
    },
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "PXE-boot-primary",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "PXE",
                },
            }, ]
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

# edit to one connection IPv4
one_connection_ipv6_edit2 = {
    "type": SERVER_PROFILE_TYPE,
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareUri': PROFILE2_SH,
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
        "mode": "UEFI",
        "pxeBootPolicy": "IPv4"
    },
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "PXE-boot-primary",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "PXE",
                },
            }, ]
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

# edit to two connections Auto
two_connections_ipv4_edit2 = {
    "type": SERVER_PROFILE_TYPE,
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareUri': PROFILE1_SH,
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
        "connections": [
            {
                "id": 1,
                "name": "PXE-boot-primary",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "PXE",
                },
            }, {
                "id": 2,
                "name": "iSCSI-boot-secondary",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Secondary",
                    "ethernetBootType": "PXE",
                },
            }
        ]
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

# Templates
ipv4_template = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
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
        "mode": "UEFIOptimized",
        "pxeBootPolicy": "IPv4"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {
                "id": 1,
                "name": "PXE-boot-primary",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "PXE",
                },
            }, ],
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

ipv6_template = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
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
        "pxeBootPolicy": "IPv6"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {
                "id": 1,
                "name": "PXE-boot-primary",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "PXE",
                },
            }, {
                "id": 2,
                "name": "iSCSI-boot-secondary",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Secondary",
                    "ethernetBootType": "PXE",
                },
            }, ],
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

auto_template = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "PXE_Boot_Auto_Template",
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
        "connections": [
            {
                "id": 1,
                "name": "PXE-boot-primary",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "PXE",
                },
            }, {
                "id": 2,
                "name": "iSCSI-boot-secondary",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Secondary",
                    "ethernetBootType": "PXE",
                },
            }, ],
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

ipv4_template_edit1 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
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
        "mode": "UEFIOptimized",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {
                "id": 1,
                "name": "PXE-boot-primary",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "PXE",
                },
            }, {
                "id": 2,
                "name": "iSCSI-boot-secondary",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Secondary",
                    "ethernetBootType": "PXE",
                },
            }, ],
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

ipv6_template_edit1 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
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
        "pxeBootPolicy": "IPv4"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {
                "id": 1,
                "name": "PXE-boot-primary",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "PXE",
                },
            }, ],
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

auto_template_edit1 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "PXE_Boot_Auto_Template",
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
        "pxeBootPolicy": "IPv6"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {
                "id": 1,
                "name": "PXE-boot-primary",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "PXE",
                },
            }, {
                "id": 2,
                "name": "iSCSI-boot-secondary",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Secondary",
                    "ethernetBootType": "PXE",
                },
            }, ],
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

ipv4_template_edit2 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
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
        "mode": "UEFIOptimized",
        "pxeBootPolicy": "IPv6"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {
                "id": 1,
                "name": "PXE-boot-primary",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "PXE",
                },
            }, {
                "id": 2,
                "name": "iSCSI-boot-secondary",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Secondary",
                    "ethernetBootType": "PXE",
                },
            }, ],
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

ipv6_template_edit2 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
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
        "connections": [
            {
                "id": 1,
                "name": "PXE-boot-primary",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "PXE",
                },
            }, ],
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

auto_template_edit2 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "PXE_Boot_Auto_Template",
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
        "pxeBootPolicy": "IPv4"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {
                "id": 1,
                "name": "PXE-boot-primary",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "PXE",
                },
            }, {
                "id": 2,
                "name": "iSCSI-boot-secondary",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Secondary",
                    "ethernetBootType": "PXE",
                },
            }, ],
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

# Create profiles from Templates
profile1_from_spt = {
    "type": SERVER_PROFILE_TYPE,
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareUri': PROFILE1_SH,
    'serverProfileTemplateUri': 'SPT:' + PROFILE1_NAME,
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
        "mode": "UEFIOptimized",
        "pxeBootPolicy": "IPv6"
    },
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "PXE-boot-primary",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "PXE",
                },
            }, {
                "id": 2,
                "name": "iSCSI-boot-secondary",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Secondary",
                    "ethernetBootType": "PXE",
                },
            }, ]
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

profile2_from_spt = {
    "type": SERVER_PROFILE_TYPE,
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareUri': PROFILE2_SH,
    'serverProfileTemplateUri': 'SPT:' + PROFILE2_NAME,
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
        "connections": [
            {
                "id": 1,
                "name": "PXE-boot-primary",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "PXE",
                },
            }, ]
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

# Compliance Test
non_compliant_profile1_from_spt_profile_edit = {
    "type": SERVER_PROFILE_TYPE,
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareUri': PROFILE1_SH,
    'serverProfileTemplateUri': 'SPT:' + PROFILE1_NAME,
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
        "mode": "UEFIOptimized",
        "pxeBootPolicy": "IPv4"
    },
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "PXE-boot-primary",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "PXE",
                },
            }, ]
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

non_compliant_profile2_from_spt_profile_edit = {
    "type": SERVER_PROFILE_TYPE,
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareUri': PROFILE2_SH,
    'serverProfileTemplateUri': 'SPT:' + PROFILE2_NAME,
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
        "pxeBootPolicy": "IPv6"
    },
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "PXE-boot-primary",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "PXE",
                },
            }, {
                "id": 2,
                "name": "iSCSI-boot-secondary",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Secondary",
                    "ethernetBootType": "PXE",
                },
            }, ]
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

non_compliant_profile1_from_spt_template_edit = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
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
        "mode": "UEFIOptimized",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {
                "id": 1,
                "name": "PXE-boot-primary",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "PXE",
                },
            }, ],
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

non_compliant_profile2_from_spt_template_edit = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
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
        "pxeBootPolicy": "IPv4"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {
                "id": 1,
                "name": "PXE-boot-primary",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "PXE",
                },
            }, ],
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

# RIS Data
ris_pxe_profile1_ipv4 = {
    "server": ENC2SHBAY7,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/bios/settings/",
    "validate": {
        "Attributes": {
            "PrebootNetworkEnvPolicy": "IPv4",
        }
    }
}

ris_pxe_profile1_ipv6 = {
    "server": ENC2SHBAY7,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/bios/settings/",
    "validate": {
        "Attributes": {
            "PrebootNetworkEnvPolicy": "IPv6",
        }
    }
}

ris_pxe_profile1_auto = {
    "server": ENC2SHBAY7,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/bios/settings/",
    "validate": {
        "Attributes": {
            "PrebootNetworkEnvPolicy": "Auto",
        }
    }
}

ris_pxe_profile2_ipv4 = {
    "server": ENC2SHBAY8,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/bios/settings/",
    "validate": {
        "Attributes": {
            "PrebootNetworkEnvPolicy": "IPv4",
        }
    }
}

ris_pxe_profile2_ipv6 = {
    "server": ENC2SHBAY8,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/bios/settings/",
    "validate": {
        "Attributes": {
            "PrebootNetworkEnvPolicy": "IPv6",
        }
    }
}

ris_pxe_profile2_auto = {
    "server": ENC2SHBAY8,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/bios/settings/",
    "validate": {
        "Attributes": {
            "PrebootNetworkEnvPolicy": "Auto",
        }
    }
}

# Compliance data

sp_compliant_profile1 = {
    "name": PROFILE1_NAME,
    "compliance-preview": {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "automaticUpdates": [],
        "manualUpdates": []
    }
}

sp_compliant_profile2 = {
    "name": PROFILE2_NAME,
    "compliance-preview": {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "automaticUpdates": [],
        "manualUpdates": []
    }
}

sp_non_compliant1_profile1 = {
    "name": PROFILE1_NAME,
    "compliance-preview": {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "automaticUpdates": [
            'Change PXE boot policy to IPv6.',
            'REGEX:Create a connection to network {\\"name\\":\\"net300\\", \\"uri\\":\\".*\\"} with id \\d on \
            port Mezzanine \\(Mezz\\) \\d:\\d-\\w.',
            'REGEX:Change boot for connection \\d on port Mezzanine \\(Mezz\\) \\d:\\d-\\w to PXE secondary.',
        ],
        "manualUpdates": []
    }
}

sp_non_compliant1_profile2 = {
    "name": PROFILE2_NAME,
    "compliance-preview": {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "automaticUpdates": [
            'Change PXE boot policy to Auto.',
        ],
        "manualUpdates": []
    }
}

sp_non_compliant2_profile1 = {
    "name": PROFILE1_NAME,
    "compliance-preview": {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "automaticUpdates": [
            'Change PXE boot policy to Auto.',
        ],
        "manualUpdates": []
    }
}

sp_non_compliant2_profile2 = {
    "name": PROFILE2_NAME,
    "compliance-preview": {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "automaticUpdates": [
            "Change PXE boot policy to IPv4."
        ],
        "manualUpdates": []
    }
}

# Negative Profile Data
create_profile_for_neg_edit_tests = {
    "type": SERVER_PROFILE_TYPE,
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative Edit Profile Test",
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
        "connections": [
            {
                "id": 1,
                "name": "PXE-boot-primary",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "PXE",
                },
            }, {
                "id": 2,
                "name": "iSCSI-boot-secondary",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Secondary",
                    "ethernetBootType": "PXE",
                },
            }
        ]
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

neg_ipv4thenipv6_profile = {
    "type": SERVER_PROFILE_TYPE,
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative Profile Test - Gen10 with PXE policy: IPv4 Then TPv6",
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
        "pxeBootPolicy": "IPv4ThenIPv6"
    },
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "PXE-boot-primary",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "PXE",
                },
            }, {
                "id": 2,
                "name": "iSCSI-boot-secondary",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Secondary",
                    "ethernetBootType": "PXE",
                },
            }
        ]
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

neg_ipv6thenipv4_profile = {
    "type": SERVER_PROFILE_TYPE,
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative Profile Test - Gen10 with PXE policy: IPv6 Then TPv4",
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
        "pxeBootPolicy": "IPv6ThenIPv4"
    },
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "PXE-boot-primary",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "PXE",
                },
            }, {
                "id": 2,
                "name": "iSCSI-boot-secondary",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Secondary",
                    "ethernetBootType": "PXE",
                },
            }
        ]
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

neg_multiple_primary_profile = {
    "type": SERVER_PROFILE_TYPE,
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative Profile Test - Multiple PXE Primary Connections",
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
        "pxeBootPolicy": "IPv4"
    },
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "PXE-boot-primary1",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "PXE",
                },
            }, {
                "id": 2,
                "name": "iSCSI-boot-primary2",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "PXE",
                },
            }
        ]
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

neg_multiple_secondary_profile = {
    "type": SERVER_PROFILE_TYPE,
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative Profile Test - Multiple PXE Secondary Connections",
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
        "pxeBootPolicy": "IPv4"
    },
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "PXE-boot-secondary1",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Secondary",
                    "ethernetBootType": "PXE",
                },
            },
            {
                "id": 2,
                "name": "iSCSI-boot-secondary2",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Secondary",
                    "ethernetBootType": "PXE",
                },
            }
        ],
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

neg_only_secondary_profile = {
    "type": SERVER_PROFILE_TYPE,
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative Profile Test - Only PXE Secondary Connection",
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
        "pxeBootPolicy": "IPv4"
    },
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "PXE-boot-secondary1",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Secondary",
                    "ethernetBootType": "PXE",
                },
            },
        ],
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

neg_ipv4thenipv6_edit_profile = {
    "type": SERVER_PROFILE_TYPE,
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative Edit Profile Test",
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
        "pxeBootPolicy": "IPv4ThenIPv6"
    },
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "PXE-boot-primary",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "PXE",
                },
            }, {
                "id": 2,
                "name": "iSCSI-boot-secondary",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Secondary",
                    "ethernetBootType": "PXE",
                },
            }
        ]
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

neg_ipv6thenipv4_edit_profile = {
    "type": SERVER_PROFILE_TYPE,
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative Edit Profile Test",
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
        "pxeBootPolicy": "IPv6ThenIPv4"
    },
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "PXE-boot-primary",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "PXE",
                },
            }, {
                "id": 2,
                "name": "iSCSI-boot-secondary",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Secondary",
                    "ethernetBootType": "PXE",
                },
            }
        ]
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

# Negative Template Data
create_template_for_neg_edit_tests = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative Edit Template Test",
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
        "connections": [
            {
                "id": 1,
                "name": "PXE-boot-primary",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "PXE",
                },
            }, {
                "id": 2,
                "name": "iSCSI-boot-secondary",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Secondary",
                    "ethernetBootType": "PXE",
                },
            }
        ],
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

neg_ipv4thenipv6_template = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative Template Test - Gen10 with PXE policy: IPv4 Then TPv6",
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
        "pxeBootPolicy": "IPv4ThenIPv6"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {
                "id": 1,
                "name": "PXE-boot-primary",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "PXE",
                },
            }, {
                "id": 2,
                "name": "iSCSI-boot-secondary",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Secondary",
                    "ethernetBootType": "PXE",
                },
            }
        ],
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

neg_ipv6thenipv4_template = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative Template Test - Gen10 with PXE policy: IPv6 Then TPv4",
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
        "pxeBootPolicy": "IPv6ThenIPv4"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {
                "id": 1,
                "name": "PXE-boot-primary",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "PXE",
                },
            }, {
                "id": 2,
                "name": "iSCSI-boot-secondary",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Secondary",
                    "ethernetBootType": "PXE",
                },
            }
        ],
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

neg_multiple_primary_template = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative Template Test - Multiple PXE Primary Connections",
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
        "pxeBootPolicy": "IPv4"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {
                "id": 1,
                "name": "PXE-boot-primary1",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "PXE",
                },
            }, {
                "id": 2,
                "name": "iSCSI-boot-primary2",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "PXE",
                },
            }
        ],
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

neg_multiple_secondary_template = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative Template Test - Multiple PXE Secondary Connections",
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
        "pxeBootPolicy": "IPv4"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {
                "id": 1,
                "name": "PXE-boot-secondary1",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Secondary",
                    "ethernetBootType": "PXE",
                },
            }, {
                "id": 2,
                "name": "iSCSI-boot-secondary2",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Secondary",
                    "ethernetBootType": "PXE",
                },
            }
        ],
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

neg_only_secondary_template = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative Template Test - Only PXE Secondary Connection",
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
        "pxeBootPolicy": "IPv4"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {
                "id": 1,
                "name": "PXE-boot-secondary1",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Secondary",
                    "ethernetBootType": "PXE",
                },
            }, ],
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

neg_ipv4thenipv6_edit_template = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative Edit Template Test",
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
        "pxeBootPolicy": "IPv4ThenIPv6"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {
                "id": 1,
                "name": "PXE-boot-primary",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "PXE",
                },
            }, {
                "id": 2,
                "name": "iSCSI-boot-secondary",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Secondary",
                    "ethernetBootType": "PXE",
                },
            }
        ],
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

neg_ipv6thenipv4_edit_template = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative Edit Template Test",
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
        "pxeBootPolicy": "IPv6ThenIPv4"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {
                "id": 1,
                "name": "PXE-boot-primary",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "PXE",
                },
            }, {
                "id": 2,
                "name": "iSCSI-boot-secondary",
                "functionType": "Ethernet",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Secondary",
                    "ethernetBootType": "PXE",
                },
            }
        ],
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

ts0_create_profiles = [
    create_profile_for_neg_edit_tests.copy(),
]

negative_profile_tasks = [
    {
        'keyword': 'Add Server Profile',
        'argument': neg_ipv4thenipv6_profile.copy(),
        'taskState': 'Error',
        'errorMessage': 'PXE_BOOT_POLICY_ERROR_IPV4_THEN_IPV6'
    },
    {
        'keyword': 'Add Server Profile',
        'argument': neg_ipv6thenipv4_profile.copy(),
        'taskState': 'Error',
        'errorMessage': 'PXE_BOOT_POLICY_ERROR_IPV6_THEN_IPV4'
    },
    {
        'keyword': 'Add Server Profile',
        'argument': neg_multiple_primary_profile.copy(),
        'taskState': 'Error',
        'errorMessage': 'Multiple_primary_boot'
    },
    {
        'keyword': 'Add Server Profile',
        'argument': neg_multiple_secondary_profile.copy(),
        'taskState': 'Error',
        'errorMessage': 'Multiple_secondary_boot'
    },
    {
        'keyword': 'Add Server Profile',
        'argument': neg_only_secondary_profile.copy(),
        'taskState': 'Error',
        'errorMessage': 'Invalid_secondary_boot_connection'
    },
    {
        'keyword': 'Edit Server Profile',
        'argument': neg_ipv4thenipv6_edit_profile.copy(),
        'taskState': 'Error',
        'errorMessage': 'PXE_BOOT_POLICY_ERROR_IPV4_THEN_IPV6'
    },
    {
        'keyword': 'Edit Server Profile',
        'argument': neg_ipv6thenipv4_edit_profile.copy(),
        'taskState': 'Error',
        'errorMessage': 'PXE_BOOT_POLICY_ERROR_IPV6_THEN_IPV4'
    },
]

ts1_create_profiles = [
    two_connections_ipv4.copy(),
    one_connection_ipv6.copy()
]

ts1_edit_profiles1 = [
    two_connections_ipv4_edit1.copy(),
    one_connection_ipv6_edit1.copy()
]

ts1_edit_profiles2 = [
    two_connections_ipv4_edit2.copy(),
    one_connection_ipv6_edit2.copy()
]

ts1_ris_after_create = [
    ris_pxe_profile1_ipv4.copy(),
    ris_pxe_profile2_ipv6.copy(),
]

ts1_ris_after_edit1 = [
    ris_pxe_profile1_ipv6.copy(),
    ris_pxe_profile2_auto.copy(),
]

ts1_ris_after_edit2 = [
    ris_pxe_profile1_auto.copy(),
    ris_pxe_profile2_ipv4.copy(),
]

ts2_create_profiles_template = [
    auto_template.copy(),
    ipv4_template.copy(),
    ipv6_template.copy(),
]

ts2_edit_profiles1_template = [
    auto_template_edit1.copy(),
    ipv4_template_edit1.copy(),
    ipv6_template_edit1.copy(),
]

ts2_edit_profiles2_template = [
    auto_template_edit2.copy(),
    ipv4_template_edit2.copy(),
    ipv6_template_edit2.copy(),
]

ts3_create_profile_templates = [
    create_template_for_neg_edit_tests.copy(),
]

negative_template_tasks = [
    {
        'keyword': 'Add Server Profile Template',
        'argument': neg_ipv4thenipv6_template.copy(),
        'taskState': 'Error',
        'errorMessage': 'PXE_BOOT_POLICY_ERROR_IPV4_THEN_IPV6'
    },
    {
        'keyword': 'Add Server Profile Template',
        'argument': neg_ipv6thenipv4_template.copy(),
        'taskState': 'Error',
        'errorMessage': 'PXE_BOOT_POLICY_ERROR_IPV6_THEN_IPV4'
    },
    {
        'keyword': 'Add Server Profile Template',
        'argument': neg_multiple_primary_template.copy(),
        'taskState': 'Error',
        'errorMessage': 'Multiple_primary_boot'
    },
    {
        'keyword': 'Add Server Profile Template',
        'argument': neg_multiple_secondary_template.copy(),
        'taskState': 'Error',
        'errorMessage': 'Multiple_secondary_boot'
    },
    {
        'keyword': 'Add Server Profile Template',
        'argument': neg_only_secondary_template.copy(),
        'taskState': 'Error',
        'errorMessage': 'Invalid_secondary_boot_connection'
    },
    {
        'keyword': 'Edit Server Profile Template',
        'argument': neg_ipv4thenipv6_edit_template.copy(),
        'taskState': 'Error',
        'errorMessage': 'PXE_BOOT_POLICY_ERROR_IPV4_THEN_IPV6'
    },
    {
        'keyword': 'Edit Server Profile Template',
        'argument': neg_ipv6thenipv4_edit_template.copy(),
        'taskState': 'Error',
        'errorMessage': 'PXE_BOOT_POLICY_ERROR_IPV6_THEN_IPV4'
    },
]

ts4_create_sp_from_spt = [
    profile1_from_spt.copy(),
    profile2_from_spt.copy(),
]

ts4_ris_after_create_from_spt = [
    ris_pxe_profile1_ipv6.copy(),
    ris_pxe_profile2_auto.copy(),
]

ts5_edit_sp_non_compliant = [
    non_compliant_profile1_from_spt_profile_edit.copy(),
    non_compliant_profile2_from_spt_profile_edit.copy(),
]

ts5_edit_spt_non_compliant = [
    non_compliant_profile1_from_spt_template_edit.copy(),
    non_compliant_profile2_from_spt_template_edit.copy(),
]

ts4_sp_compliance = [
    sp_compliant_profile1.copy(),
    sp_compliant_profile2.copy(),
]

ts5_sp_non_compliant1 = [
    sp_non_compliant1_profile1.copy(),
    sp_non_compliant1_profile2.copy(),
]

ts5_sp_non_compliant2 = [
    sp_non_compliant2_profile1.copy(),
    sp_non_compliant2_profile2.copy(),
]

# Credentials
admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
ilo_credentials = {'username': 'Administrator', 'password': 'hpvse123'}
cliq_credentials = {
    'mgmt_ip': '16.71.149.173',
    'username': 'admin',
    'password': 'admin'}

# Resource types for X-API-Version=600
INTERCONNECT_TYPE = 'InterconnectV4'
SERVER_PROFILE_TYPE = 'ServerProfileV10'

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
ENC2SHBAY7 = '%s, bay 7' % ENC2    # SY480 Gen10
ENC2SHBAY8 = '%s, bay 8' % ENC2    # SY480 Gen10
ENC3SHBAY1 = '%s, bay 1' % ENC3    # SY480 Gen9
ENC3SHBAY5 = '%s, bay 5' % ENC3    # SY680 Gen9
# LIG, EG and LE
LIG_NAME = 'LIG1'
SASLIG_NAME = 'SASLIG1'
EG_NAME = 'EG1'
LE_NAME = 'LE1'

interconnects_expected = [
    {"type": INTERCONNECT_TYPE, "name": ENC1ICBAY3,
     "productName": "Virtual Connect SE 40Gb F8 Module for Synergy",
     },
    {"type": INTERCONNECT_TYPE, "name": ENC1ICBAY6,
     "productName": "Synergy 20Gb Interconnect Link Module",
     },
    {"type": INTERCONNECT_TYPE, "name": ENC2ICBAY3,
     "productName": "Synergy 20Gb Interconnect Link Module",
     },
    {"type": INTERCONNECT_TYPE, "name": ENC2ICBAY6,
     "productName": "Virtual Connect SE 40Gb F8 Module for Synergy",
     },
    {"type": INTERCONNECT_TYPE, "name": ENC3ICBAY3,
     "productName": "Synergy 20Gb Interconnect Link Module",
     },
    {"type": INTERCONNECT_TYPE, "name": ENC3ICBAY6,
     "productName": "Synergy 20Gb Interconnect Link Module",
     },

]

interconnects_linked_ports_expected = [
    {
        "name": ENC1 + ", interconnect 3",
        "linked_ports": ['d3', 'd5', 'd6', 'd7', 'd8', 'd13', 'd17', 'd19', 'd20', 'd25', 'd29', 'Q1:1', 'Q2:1', 'Q3:1', 'Q4:1', 'Q7', 'Q8', 'l1', 'l2', 'l3', 'l4']

    },
    {
        "name": ENC1 + ", interconnect 6",
        "linked_ports": ['d3', 'd5', 'd6', 'd7', 'd8', 'l1', 'l2']
    },
    {
        "name": ENC2 + ", interconnect 3",
        "linked_ports": ['d1', 'd5', 'd7', 'd8', 'l1', 'l2']
    },
    {
        "name": ENC2 + ", interconnect 6",
        "linked_ports": ['d1', 'd5', 'd7', 'd8', 'd15', 'd17', 'd18', 'd19', 'd20', 'd25', 'd29', 'Q1:1', 'Q2:1', 'Q3:1', 'Q4:1', 'Q7', 'Q8', 'l1', 'l2', 'l3', 'l4']
    },
    {
        "name": ENC3 + ", interconnect 3",
        "linked_ports": ['d1', 'd5', 'l1', 'l2']
    },
    {
        "name": ENC3 + ", interconnect 6",
        "linked_ports": ['d1', 'd5', 'l1', 'l2']
    },
]

# iSCSI
INITIATOR_GATEWAY = "192.168.0.1"
INITIATOR_SUBNET_MASK = "255.255.192.0"
FIRST_BOOT_TARGET_IP = "192.168.21.71"
CHAP_SECRET = "wpsthpvse123"
MCHAP_SECRET = "hpvse123wpst"

NAME_PREFIX = 'Synergy-Ring1-F791-'
PROFILE_NAME_PREFIX = NAME_PREFIX
# Negative profiles
TS0_PROFILE1_NAME = PROFILE_NAME_PREFIX + 'negative-profile1'
TS0_PROFILE2_NAME = PROFILE_NAME_PREFIX + 'negative-profile2'
TS0_PROFILE3_NAME = PROFILE_NAME_PREFIX + 'negative-profile3'
TS0_PROFILE4_NAME = PROFILE_NAME_PREFIX + 'negative-profile4'
TS0_PROFILE5_NAME = PROFILE_NAME_PREFIX + 'negative-profile5'
TS0_PROFILE6_NAME = PROFILE_NAME_PREFIX + 'negative-profile6'
TS0_PROFILE7_NAME = PROFILE_NAME_PREFIX + 'negative-profile7'
TS0_PROFILE8_NAME = PROFILE_NAME_PREFIX + 'negative-profile8'
TS0_PROFILE9_NAME = PROFILE_NAME_PREFIX + 'negative-profile9'
TS0_PROFILE10_NAME = PROFILE_NAME_PREFIX + 'negative-profile9'
TS0_PROFILE11_NAME = PROFILE_NAME_PREFIX + 'negative-profile11'
TS0_PROFILE12_NAME = PROFILE_NAME_PREFIX + 'negative-profile12'
TS0_PROFILE_SERVER = ENC1SHBAY7
TS0_PROFILE_EG = EG_NAME
TS0_PROFILE_ENC = ENC1

# PROFILE1: ENC1 bay7, Blackbird
PROFILE1_NAME = PROFILE_NAME_PREFIX + "tbird14-bay7-profile"
PROFILE1_SERVER = ENC1SHBAY7
PROFILE1_EG = EG_NAME
PROFILE1_ENC = ENC1
PROFILE1_BOOT_TARGET_NAME = 'iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:6981:tbird14-bay7-win2016-bootvol'
PROFILE1_INITIATOR_NAME = "iqn.2015-02.com.hpe:oneview-tbird14-bay7"
PROFILE1_INITIATOR_IP_1 = "192.168.22.158"
PROFILE1_INITIATOR_IP_2 = "192.168.22.159"
PROFILE1_ISCSI_BOOT_ATTEMPT_1 = "iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:6981:tbird14-bay7-win2016-bootvol_attempt_1"
PROFILE1_ISCSI_BOOT_ATTEMPT_2 = "iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:6981:tbird14-bay7-win2016-bootvol_attempt_2"
PROFILE1_CHAP_NAME = 'tbird14-bay7'

# PROFILE2: ENC2 bay5, Redbird
PROFILE2_NAME = PROFILE_NAME_PREFIX + "tbird17-bay5-profile"
PROFILE2_SERVER = ENC2SHBAY5
PROFILE2_EG = EG_NAME
PROFILE2_ENC = ENC2
PROFILE2_BOOT_TARGET_NAME = "iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:6997:tbird17-bay5-bootvol"
PROFILE2_INITIATOR_NAME = "iqn.2015-02.com.hpe:oneview-tbird17-bay5"
PROFILE2_INITIATOR_IP_1 = "192.168.22.167"
PROFILE2_INITIATOR_IP_2 = "192.168.22.168"
PROFILE2_ISCSI_BOOT_ATTEMPT_1 = "iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:6997:tbird17-bay5-bootvol_attempt_1"
PROFILE2_ISCSI_BOOT_ATTEMPT_2 = "iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:6997:tbird17-bay5-bootvol_attempt_2"
PROFILE2_CHAP_NAME = 'tbird17-bay5'
PROFILE2_MCHAP_NAME = 'tbird17-bay5'

# PROFILE3: PROFILE2 moved to ENC2 bay1
PROFILE3_NAME = PROFILE_NAME_PREFIX + "tbird17-bay1-profile"
PROFILE3_SERVER = ENC2SHBAY1
PROFILE3_EG = EG_NAME
PROFILE3_ENC = ENC2
PROFILE3_BOOT_TARGET_NAME = "iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1247:tbird17-bay1-bootvol"
PROFILE3_INITIATOR_NAME = "iqn.2015-02.com.hpe:oneview-tbird17-bay1"
PROFILE3_INITIATOR_IP_1 = "192.168.22.134"
PROFILE3_INITIATOR_IP_2 = "192.168.22.137"
PROFILE3_ISCSI_BOOT_ATTEMPT_1 = "iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1247:tbird17-bay1-bootvol_attempt_1"
PROFILE3_ISCSI_BOOT_ATTEMPT_2 = "iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1247:tbird17-bay1-bootvol_attempt_2"

# PROFILE4: PROFILE1 moved to ENC1 bay8, Gen10
PROFILE4_NAME = PROFILE_NAME_PREFIX + "tbird14-bay8-profile"
PROFILE4_SERVER = ENC1SHBAY8
PROFILE4_EG = EG_NAME
PROFILE4_ENC = ENC1
PROFILE4_BOOT_TARGET_NAME = 'iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:13007:tbird14-bay8-win2016-bootvol'
PROFILE4_INITIATOR_NAME = "iqn.2015-02.com.hpe:oneview-tbird14-bay8"
PROFILE4_INITIATOR_IP_1 = "192.168.22.51"
PROFILE4_INITIATOR_IP_2 = "192.168.22.56"
PROFILE4_ISCSI_BOOT_ATTEMPT_1 = "iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:13007:tbird14-bay8-win2016-bootvol_attempt_1"
PROFILE4_ISCSI_BOOT_ATTEMPT_2 = "iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:13007:tbird14-bay8-win2016-bootvol_attempt_2"

# Negative tests
# Invalid profile initiator name
negative_profile1 = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + TS0_PROFILE_SERVER, 'enclosureUri': 'ENC:' + TS0_PROFILE_ENC,
                     "enclosureGroupUri": "EG:" + TS0_PROFILE_EG, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                     "macType": "Physical", "wwnType": "Physical", "name": TS0_PROFILE1_NAME, "description": "", "affinity": "Bay",
                     "connectionSettings": {"connections": [
                         {"id": 1, "name": "iSCSI-boot", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                          "ipv4": {
                              "ipAddressSource": "UserDefined",
                              "ipAddress": PROFILE1_INITIATOR_IP_1,
                              "subnetMask": INITIATOR_SUBNET_MASK,
                              "gateway": INITIATOR_GATEWAY
                          },
                          "boot": {
                              "priority": "Primary", "ethernetBootType": "iSCSI",
                              "iscsi": {"initiatorNameSource": "ProfileInitiatorName",
                                        "bootTargetName": PROFILE1_BOOT_TARGET_NAME,
                                        "bootTargetLun": "0", "firstBootTargetIp": FIRST_BOOT_TARGET_IP, "firstBootTargetPort": "3260",
                                        "secondBootTargetIp": "", "secondBootTargetPort": "",
                                        "chapLevel": "None", "chapName": "", "chapSecret": None, "mutualChapName": "", "mutualChapSecret": None}},
                          "requestedVFs": "Auto"}
                     ]},
                     "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                     "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                     "bios": {"manageBios": False, "overriddenSettings": []},
                     "hideUnusedFlexNics": True, "iscsiInitiatorName": "NAME",
                     "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                     }

# Invalid boot initiator name
negative_profile2 = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + TS0_PROFILE_SERVER, 'enclosureUri': 'ENC:' + TS0_PROFILE_ENC,
                     "enclosureGroupUri": "EG:" + TS0_PROFILE_EG, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                     "macType": "Physical", "wwnType": "Physical", "name": TS0_PROFILE2_NAME, "description": "", "affinity": "Bay",
                     "connectionSettings": {"connections": [
                         {"id": 1, "name": "iSCSI-boot", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                          "ipv4": {
                              "ipAddressSource": "UserDefined",
                              "ipAddress": PROFILE1_INITIATOR_IP_1,
                              "subnetMask": INITIATOR_SUBNET_MASK,
                              "gateway": INITIATOR_GATEWAY
                          },
                          "boot": {
                              "priority": "Primary", "ethernetBootType": "iSCSI",
                              "iscsi": {"initiatorNameSource": "UserDefined",
                                        "initiatorName": "NAME",
                                        "bootTargetName": PROFILE1_BOOT_TARGET_NAME,
                                        "bootTargetLun": "0", "firstBootTargetIp": FIRST_BOOT_TARGET_IP, "firstBootTargetPort": "3260",
                                        "secondBootTargetIp": "", "secondBootTargetPort": "",
                                        "chapLevel": "None", "chapName": "", "chapSecret": None, "mutualChapName": "", "mutualChapSecret": None}},
                          "requestedVFs": "Auto"}
                     ]},
                     "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                     "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                     "bios": {"manageBios": False, "overriddenSettings": []},
                     "hideUnusedFlexNics": True, "iscsiInitiatorName": PROFILE1_INITIATOR_NAME,
                     "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                     }

# Invalid virtual function, only first flexNic is supported for software iSCSI
negative_profile3 = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + TS0_PROFILE_SERVER, 'enclosureUri': 'ENC:' + TS0_PROFILE_ENC,
                     "enclosureGroupUri": "EG:" + TS0_PROFILE_EG, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                     "macType": "Physical", "wwnType": "Physical", "name": TS0_PROFILE3_NAME, "description": "", "affinity": "Bay",
                     "connectionSettings": {"connections": [
                         {"id": 1, "name": "iSCSI-boot", "functionType": "Ethernet", "portId": "Mezz 3:2-b", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                          "ipv4": {
                              "ipAddressSource": "UserDefined",
                              "ipAddress": PROFILE1_INITIATOR_IP_1,
                              "subnetMask": INITIATOR_SUBNET_MASK,
                              "gateway": INITIATOR_GATEWAY
                          },
                          "boot": {
                              "priority": "Primary", "ethernetBootType": "iSCSI",
                              "iscsi": {"initiatorNameSource": "ProfileInitiatorName",
                                        "initiatorName": "",
                                        "bootTargetName": PROFILE1_BOOT_TARGET_NAME,
                                        "bootTargetLun": "0", "firstBootTargetIp": FIRST_BOOT_TARGET_IP, "firstBootTargetPort": "3260",
                                        "secondBootTargetIp": "", "secondBootTargetPort": "",
                                        "chapLevel": "None", "chapName": "", "chapSecret": None, "mutualChapName": "", "mutualChapSecret": None}},
                          "requestedVFs": "Auto"}
                     ]},
                     "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                     "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                     "bios": {"manageBios": False, "overriddenSettings": []},
                     "hideUnusedFlexNics": True, "iscsiInitiatorName": PROFILE1_INITIATOR_NAME,
                     "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                     }

# Invalid boot mode
negative_profile4 = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + TS0_PROFILE_SERVER, 'enclosureUri': 'ENC:' + TS0_PROFILE_ENC,
                     "enclosureGroupUri": "EG:" + TS0_PROFILE_EG, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                     "macType": "Physical", "wwnType": "Physical", "name": TS0_PROFILE4_NAME, "description": "", "affinity": "Bay",
                     "connectionSettings": {"connections": [
                         {"id": 1, "name": "iSCSI-boot", "functionType": "Ethernet", "portId": "Mezz 3:1-a", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                          "ipv4": {
                              "ipAddressSource": "UserDefined",
                              "ipAddress": PROFILE1_INITIATOR_IP_1,
                              "subnetMask": INITIATOR_SUBNET_MASK,
                              "gateway": INITIATOR_GATEWAY
                          },
                          "boot": {
                              "priority": "Primary", "ethernetBootType": "iSCSI",
                              "iscsi": {"initiatorNameSource": "ProfileInitiatorName",
                                        "initiatorName": "",
                                        "bootTargetName": PROFILE1_BOOT_TARGET_NAME,
                                        "bootTargetLun": "0", "firstBootTargetIp": FIRST_BOOT_TARGET_IP, "firstBootTargetPort": "3260",
                                        "secondBootTargetIp": "", "secondBootTargetPort": "",
                                        "chapLevel": "None", "chapName": "", "chapSecret": None, "mutualChapName": "", "mutualChapSecret": None}},
                          "requestedVFs": "Auto"}
                     ]},
                     "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]}, "bootMode": {"manageMode": True, "mode": "BIOS"},
                     "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                     "bios": {"manageBios": False, "overriddenSettings": []},
                     "hideUnusedFlexNics": True, "iscsiInitiatorName": PROFILE1_INITIATOR_NAME,
                     "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                     }

# Define secondary boot without primary boot
negative_profile5 = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + TS0_PROFILE_SERVER, 'enclosureUri': 'ENC:' + TS0_PROFILE_ENC,
                     "enclosureGroupUri": "EG:" + TS0_PROFILE_EG, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                     "macType": "Physical", "wwnType": "Physical", "name": TS0_PROFILE5_NAME, "description": "", "affinity": "Bay",
                     "connectionSettings": {"connections": [
                         {"id": 1, "name": "iSCSI-boot", "functionType": "Ethernet", "portId": "Mezz 3:2-a", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                          "ipv4": {
                              "ipAddressSource": "UserDefined",
                              "ipAddress": PROFILE1_INITIATOR_IP_1,
                              "subnetMask": INITIATOR_SUBNET_MASK,
                              "gateway": INITIATOR_GATEWAY
                          },
                          "boot": {
                              "priority": "Secondary", "ethernetBootType": "iSCSI",
                              "iscsi": {"initiatorNameSource": "ProfileInitiatorName",
                                        "initiatorName": "",
                                        "bootTargetName": PROFILE1_BOOT_TARGET_NAME,
                                        "bootTargetLun": "0", "firstBootTargetIp": FIRST_BOOT_TARGET_IP, "firstBootTargetPort": "3260",
                                        "secondBootTargetIp": "", "secondBootTargetPort": "", "chapLevel": "None", "chapName": "", "chapSecret": None, "mutualChapName": "", "mutualChapSecret": None}},
                          "requestedVFs": "Auto"}
                     ]},
                     "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                     "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                     "bios": {"manageBios": False, "overriddenSettings": []},
                     "hideUnusedFlexNics": True, "iscsiInitiatorName": PROFILE1_INITIATOR_NAME,
                     "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                     }

# Multiple Primary boot connections
negative_profile6 = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + TS0_PROFILE_SERVER, 'enclosureUri': 'ENC:' + TS0_PROFILE_ENC,
                     "enclosureGroupUri": "EG:" + TS0_PROFILE_EG, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                     "macType": "Physical", "wwnType": "Physical", "name": TS0_PROFILE6_NAME, "description": "", "affinity": "Bay",
                     "connectionSettings": {"connections": [
                         {"id": 1, "name": "iSCSI-boot-1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                          "networkUri": 'ETH:network-untagged',
                          "ipv4": {
                              "ipAddressSource": "UserDefined",
                              "ipAddress": PROFILE1_INITIATOR_IP_1,
                              "subnetMask": INITIATOR_SUBNET_MASK,
                              "gateway": INITIATOR_GATEWAY
                          },
                          "boot": {
                              "priority": "Primary", "ethernetBootType": "iSCSI",
                              "iscsi": {"initiatorNameSource": "ProfileInitiatorName",
                                        "initiatorName": "",
                                        "bootTargetName": PROFILE1_BOOT_TARGET_NAME,
                                        "bootTargetLun": "0", "firstBootTargetIp": FIRST_BOOT_TARGET_IP, "firstBootTargetPort": "3260",
                                        "secondBootTargetIp": "", "secondBootTargetPort": "", "chapLevel": "None",
                                        "chapName": "", "chapSecret": None, "mutualChapName": "", "mutualChapSecret": None}},
                          "requestedVFs": "Auto"},
                         {"id": 2, "name": "iSCSI-boot-2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                             "networkUri": 'ETH:network-untagged',
                          "ipv4": {
                              "ipAddressSource": "UserDefined",
                              "ipAddress": PROFILE1_INITIATOR_IP_2,
                              "subnetMask": INITIATOR_SUBNET_MASK,
                              "gateway": INITIATOR_GATEWAY
                          },
                             "boot": {
                                 "priority": "Primary", "ethernetBootType": "iSCSI",
                                 "iscsi": {"initiatorNameSource": "ProfileInitiatorName",
                                           "firstBootTargetIp": FIRST_BOOT_TARGET_IP, "firstBootTargetPort": "3260", "secondBootTargetIp": "",
                                           "secondBootTargetPort": "", "chapLevel": "None", "initiatorName": "",
                                           "bootTargetName": PROFILE1_BOOT_TARGET_NAME,
                                           "bootTargetLun": "0", "chapName": "",
                                           "chapSecret": None, "mutualChapName": "", "mutualChapSecret": None}},
                             "requestedVFs": "Auto"}
                     ]},
                     "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                     "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                     "bios": {"manageBios": False, "overriddenSettings": []},
                     "hideUnusedFlexNics": True, "iscsiInitiatorName": PROFILE1_INITIATOR_NAME,
                     "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                     }

# Multiple Secondary boot connections
negative_profile7 = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + TS0_PROFILE_SERVER, 'enclosureUri': 'ENC:' + TS0_PROFILE_ENC,
                     "enclosureGroupUri": "EG:" + TS0_PROFILE_EG, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                     "macType": "Physical", "wwnType": "Physical", "name": TS0_PROFILE7_NAME, "description": "", "affinity": "Bay",
                     "connectionSettings": {"connections": [
                         {"id": 1, "name": "iSCSI-boot-1", "functionType": "Ethernet", "portId": "Mezz 3:2-a", "requestedMbps": "2500",
                          "networkUri": 'ETH:network-untagged',
                          "ipv4": {
                              "ipAddressSource": "UserDefined",
                              "ipAddress": PROFILE1_INITIATOR_IP_1,
                              "subnetMask": INITIATOR_SUBNET_MASK,
                              "gateway": INITIATOR_GATEWAY
                          },
                          "boot": {
                              "priority": "Secondary", "ethernetBootType": "iSCSI",
                              "iscsi": {"initiatorNameSource": "ProfileInitiatorName",
                                        "initiatorName": "",
                                        "bootTargetName": PROFILE1_BOOT_TARGET_NAME,
                                        "bootTargetLun": "0", "firstBootTargetIp": FIRST_BOOT_TARGET_IP, "firstBootTargetPort": "3260",
                                        "secondBootTargetIp": "", "secondBootTargetPort": "", "chapLevel": "None", "chapName": "", "chapSecret": None, "mutualChapName": "", "mutualChapSecret": None}},
                          "requestedVFs": "Auto"},
                         {"id": 2, "name": "iSCSI-boot-2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                          "networkUri": 'ETH:network-untagged',
                          "ipv4": {
                              "ipAddressSource": "UserDefined",
                              "ipAddress": PROFILE1_INITIATOR_IP_2,
                              "subnetMask": INITIATOR_SUBNET_MASK,
                              "gateway": INITIATOR_GATEWAY
                          },
                          "boot": {
                              "priority": "Secondary", "ethernetBootType": "iSCSI",
                              "iscsi": {"initiatorNameSource": "ProfileInitiatorName",
                                        "firstBootTargetIp": FIRST_BOOT_TARGET_IP, "firstBootTargetPort": "3260", "secondBootTargetIp": "",
                                        "secondBootTargetPort": "", "chapLevel": "None", "initiatorName": "",
                                        "bootTargetName": PROFILE1_BOOT_TARGET_NAME,
                                        "bootTargetLun": "0", "chapName": "",
                                        "chapSecret": None, "mutualChapName": "", "mutualChapSecret": None}},
                          "requestedVFs": "Auto"}
                     ]},
                     "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                     "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                     "bios": {"manageBios": False, "overriddenSettings": []},
                     "hideUnusedFlexNics": True, "iscsiInitiatorName": PROFILE1_INITIATOR_NAME,
                     "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                     }

# US50625 Connection initiator name uniqueness
negative_profile8 = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + TS0_PROFILE_SERVER, 'enclosureUri': 'ENC:' + TS0_PROFILE_ENC,
                     "enclosureGroupUri": "EG:" + TS0_PROFILE_EG, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                     "macType": "Physical", "wwnType": "Physical", "name": TS0_PROFILE8_NAME, "description": "", "affinity": "Bay",
                     "connectionSettings": {"connections": [
                         {"id": 1, "name": "iSCSI-boot-1", "functionType": "Ethernet", "portId": "Mezz 3:1-a", "requestedMbps": "2500",
                          "networkUri": 'ETH:network-untagged',
                          "ipv4": {
                              "ipAddressSource": "UserDefined",
                              "ipAddress": PROFILE1_INITIATOR_IP_1,
                              "subnetMask": INITIATOR_SUBNET_MASK,
                              "gateway": INITIATOR_GATEWAY
                          },
                          "boot": {
                              "priority": "Primary", "ethernetBootType": "iSCSI",
                              "iscsi": {"initiatorNameSource": "UserDefined", "initiatorName": "boot1",
                                        "bootTargetName": PROFILE1_BOOT_TARGET_NAME,
                                        "bootTargetLun": "0", "firstBootTargetIp": FIRST_BOOT_TARGET_IP, "firstBootTargetPort": "3260",
                                        "secondBootTargetIp": "", "secondBootTargetPort": "", "chapLevel": "None",
                                        "chapName": "", "chapSecret": None, "mutualChapName": "", "mutualChapSecret": None}},
                          "requestedVFs": "Auto"},
                         {"id": 2, "name": "iSCSI-boot-2", "functionType": "Ethernet", "portId": "Mezz 3:2-a", "requestedMbps": "2500",
                             "networkUri": 'ETH:network-untagged',
                          "ipv4": {
                              "ipAddressSource": "UserDefined",
                              "ipAddress": PROFILE1_INITIATOR_IP_2,
                              "subnetMask": INITIATOR_SUBNET_MASK,
                              "gateway": INITIATOR_GATEWAY
                          },
                             "boot": {
                                 "priority": "Secondary", "ethernetBootType": "iSCSI",
                                 "iscsi": {"initiatorNameSource": "UserDefined", "initiatorName": "boot2",
                                           "firstBootTargetIp": FIRST_BOOT_TARGET_IP, "firstBootTargetPort": "3260", "secondBootTargetIp": "",
                                           "secondBootTargetPort": "", "chapLevel": "None",
                                           "bootTargetName": PROFILE1_BOOT_TARGET_NAME,
                                           "bootTargetLun": "0", "chapName": "",
                                           "chapSecret": None, "mutualChapName": "", "mutualChapSecret": None}},
                             "requestedVFs": "Auto"}
                     ]},
                     "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                     "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                     "bios": {"manageBios": False, "overriddenSettings": []},
                     "hideUnusedFlexNics": True, "iscsiInitiatorName": PROFILE1_INITIATOR_NAME,
                     "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                     }

# US50625 PXE validation
negative_profile9 = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + TS0_PROFILE_SERVER, 'enclosureUri': 'ENC:' + TS0_PROFILE_ENC,
                     "enclosureGroupUri": "EG:" + TS0_PROFILE_EG, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                     "macType": "Physical", "wwnType": "Physical", "name": TS0_PROFILE9_NAME, "description": "", "affinity": "Bay",
                     "connectionSettings": {"connections": [
                         {"id": 1, "name": "pxe-boot", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                          "networkUri": 'ETH:network-untagged',
                          "boot": {"priority": "Primary"},
                          "mac": None, "wwpn": "", "wwnn": "", "requestedVFs": "Auto"},
                         {"id": 2, "name": "iSCSI-boot", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                             "networkUri": 'ETH:network-untagged',
                             "ipv4": {
                                 "ipAddressSource": "UserDefined",
                                 "ipAddress": PROFILE1_INITIATOR_IP_1,
                                 "subnetMask": INITIATOR_SUBNET_MASK,
                                 "gateway": INITIATOR_GATEWAY
                             },
                             "boot": {"priority": "Primary", "ethernetBootType": "iSCSI",
                                      "iscsi": {"initiatorNameSource": "ProfileInitiatorName",
                                                "firstBootTargetIp": FIRST_BOOT_TARGET_IP, "firstBootTargetPort": "3260",
                                                "secondBootTargetIp": "", "secondBootTargetPort": "", "chapLevel": "None", "initiatorName": "",
                                                "bootTargetName": PROFILE1_BOOT_TARGET_NAME, "bootTargetLun": "0", "chapName": "", "chapSecret": None, "mutualChapName": "", "mutualChapSecret": None}},
                             "mac": None, "wwpn": "", "wwnn": "", "requestedVFs": "Auto"}
                     ]},
                     "boot": {"manageBoot": True, "order": ["PXE"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                     "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                     "bios": {"manageBios": False, "overriddenSettings": []},
                     "hideUnusedFlexNics": True, "iscsiInitiatorName": PROFILE1_INITIATOR_NAME,
                     "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                     }

# Network set in iSCSI boot connection
negative_profile10 = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + TS0_PROFILE_SERVER, 'enclosureUri': 'ENC:' + TS0_PROFILE_ENC,
                      "enclosureGroupUri": "EG:" + TS0_PROFILE_EG, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                      "macType": "Physical", "wwnType": "Physical", "name": TS0_PROFILE10_NAME, "description": "", "affinity": "Bay",
                      "connectionSettings": {"connections": [
                          {"id": 1, "name": "iSCSI-boot-primary", "functionType": "Ethernet", "portId": "Mezz 3:1-a", "requestedMbps": "2500",
                           "networkUri": 'NS:NS1',
                           "ipv4": {
                               "ipAddressSource": "UserDefined",
                               "ipAddress": PROFILE1_INITIATOR_IP_1,
                               "subnetMask": INITIATOR_SUBNET_MASK,
                               "gateway": INITIATOR_GATEWAY
                           },
                           "boot": {
                               "priority": "Primary", "ethernetBootType": "iSCSI",
                               "iscsi": {"initiatorNameSource": "ProfileInitiatorName",
                                         "bootTargetName": PROFILE1_BOOT_TARGET_NAME,
                                         "bootTargetLun": "0", "firstBootTargetIp": FIRST_BOOT_TARGET_IP, "firstBootTargetPort": "3260",
                                         "secondBootTargetIp": "", "secondBootTargetPort": "", "chapLevel": "None", "chapName": "", "chapSecret": None, "mutualChapName": "", "mutualChapSecret": None
                                         }}, "requestedVFs": "Auto"},
                      ]},
                      "boot": {"manageBoot": True, "order": ["PXE"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                      "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                      "bios": {"manageBios": False, "overriddenSettings": []},
                      "hideUnusedFlexNics": True, "iscsiInitiatorName": PROFILE1_INITIATOR_NAME,
                      "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                      }

# Invalid bootVlanId in untagged network
negative_profile11 = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + TS0_PROFILE_SERVER, 'enclosureUri': 'ENC:' + TS0_PROFILE_ENC,
                      "enclosureGroupUri": "EG:" + TS0_PROFILE_EG, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                      "macType": "Physical", "wwnType": "Physical", "name": TS0_PROFILE11_NAME, "description": "", "affinity": "Bay",
                      "connectionSettings": {"connections": [
                          {"id": 1, "name": "iSCSI-boot-primary", "functionType": "Ethernet", "portId": "Mezz 3:2-a", "requestedMbps": "2500",
                           "networkUri": 'ETH:network-untagged',
                           "ipv4": {
                               "ipAddressSource": "UserDefined",
                               "ipAddress": PROFILE1_INITIATOR_IP_1,
                               "subnetMask": INITIATOR_SUBNET_MASK,
                               "gateway": INITIATOR_GATEWAY
                           },
                           "boot": {
                               "priority": "Primary", "ethernetBootType": "iSCSI", "bootVlanId": "1",
                               "iscsi": {"initiatorNameSource": "ProfileInitiatorName",
                                         "bootTargetName": PROFILE1_BOOT_TARGET_NAME,
                                         "bootTargetLun": "0", "firstBootTargetIp": FIRST_BOOT_TARGET_IP, "firstBootTargetPort": "3260",
                                         "secondBootTargetIp": "", "secondBootTargetPort": "", "chapLevel": "Chap",
                                         "chapName": "tbird9-bay1", "chapSecret": CHAP_SECRET, "mutualChapName": "", "mutualChapSecret": None
                                         }},
                           "requestedVFs": "Auto"}
                      ]},
                      "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                      "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                      "bios": {"manageBios": False, "overriddenSettings": []},
                      "hideUnusedFlexNics": True, "iscsiInitiatorName": PROFILE1_INITIATOR_NAME,
                      "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                      }

# Invalid bootVlanId for tunnel network
negative_profile12 = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + TS0_PROFILE_SERVER, 'enclosureUri': 'ENC:' + TS0_PROFILE_ENC,
                      "enclosureGroupUri": "EG:" + TS0_PROFILE_EG, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                      "macType": "Physical", "wwnType": "Physical", "name": TS0_PROFILE12_NAME, "description": "", "affinity": "Bay",
                      "connectionSettings": {"connections": [
                          {"id": 1, "name": "iSCSI-boot-primary", "functionType": "Ethernet", "portId": "Mezz 3:2-a", "requestedMbps": "2500", "networkUri": 'ETH:network-tunnel',
                           "ipv4": {
                               "ipAddressSource": "UserDefined",
                               "ipAddress": PROFILE1_INITIATOR_IP_1,
                               "subnetMask": INITIATOR_SUBNET_MASK,
                               "gateway": INITIATOR_GATEWAY
                           },
                           "boot": {
                               "priority": "Primary", "ethernetBootType": "iSCSI", "bootVlanId": "1",
                               "iscsi": {"initiatorNameSource": "ProfileInitiatorName",
                                         "bootTargetName": PROFILE1_BOOT_TARGET_NAME,
                                         "bootTargetLun": "0", "firstBootTargetIp": FIRST_BOOT_TARGET_IP, "firstBootTargetPort": "3260",
                                         "secondBootTargetIp": "", "secondBootTargetPort": "", "chapLevel": "Chap",
                                         "chapName": "tbird9-bay1", "chapSecret": CHAP_SECRET, "mutualChapName": "", "mutualChapSecret": None
                                         }},
                           "requestedVFs": "Auto"}
                      ]},
                      "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                      "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                      "bios": {"manageBios": False, "overriddenSettings": []},
                      "hideUnusedFlexNics": True, "iscsiInitiatorName": PROFILE1_INITIATOR_NAME,
                      "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                      }

negative_profile_tasks = [
    {
        'keyword': 'Add Server Profile',
        'argument': negative_profile1.copy(),
        'taskState': 'Error',
        'timeout': '10',
        'interval': '1',
        'errorMessage': 'Invalid_profile_initiator_name'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_profile2.copy(),
        'taskState': 'Error',
        'timeout': '10',
        'interval': '1',
        'errorMessage': 'Invalid_boot_initiator_name'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_profile3.copy(),
        'taskState': 'Error',
        'timeout': '10',
        'interval': '1',
        'errorMessage': 'Invalid_flexNIC'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_profile4.copy(),
        'taskState': 'Error',
        'timeout': '10',
        'interval': '1',
        'errorMessage': 'Invalid_iSCSI_and_BIOS_boot_mode'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_profile5.copy(),
        'taskState': 'Error',
        'timeout': '10',
        'interval': '1',
        'errorMessage': 'Invalid_secondary_boot_connection'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_profile6.copy(),
        'taskState': 'Error',
        'timeout': '10',
        'interval': '1',
        'errorMessage': 'Multiple_primary_boot'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_profile7.copy(),
        'taskState': 'Error',
        'timeout': '10',
        'interval': '1',
        'errorMessage': 'Multiple_secondary_boot'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_profile8.copy(),
        'taskState': 'Error',
        'timeout': '10',
        'interval': '1',
        'errorMessage': 'Connection_initiator_name_non_unique'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_profile9.copy(),
        'taskState': 'Error',
        'timeout': '10',
        'interval': '1',
        'errorMessage': 'No_iSCSI_boot_for_PXE_boot_order'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_profile10.copy(),
        'taskState': 'Error',
        'timeout': '2',
        'interval': '1',
        'errorMessage': 'Profile_network_set_ethernet'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_profile11.copy(),
        'taskState': 'Error',
        'timeout': '10',
        'interval': '1',
        'errorMessage': 'Invaid_initiator_vlan_id_for_tagged_untagged_network'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_profile12.copy(),
        'taskState': 'Error',
        'timeout': '10',
        'interval': '1',
        'errorMessage': 'Software_iSCSI_Invaid_initiator_vlan_id_for_tunnel_network'},

]

# Positive tests
profile1_bios = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + PROFILE1_SERVER, 'enclosureUri': 'ENC:' + PROFILE1_ENC,
                 "enclosureGroupUri": "EG:" + PROFILE1_EG, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                 "macType": "Physical", "wwnType": "Physical", "name": PROFILE1_NAME, "description": "", "affinity": "Bay",
                 "connectionSettings": {"connections": []},
                 "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]}, "bootMode": {"manageMode": True, "mode": "BIOS"},
                 "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                 "bios": {"manageBios": False, "overriddenSettings": []},
                 "hideUnusedFlexNics": True, "iscsiInitiatorName": PROFILE1_INITIATOR_NAME,
                 "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                 }

# Connection initiator name uses profile defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on Mezz3:2a to tunnel network
# Primary PXE boot connection on Mezz3:1a
profile1_pxe_iscsi = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + PROFILE1_SERVER, 'enclosureUri': 'ENC:' + PROFILE1_ENC,
                      "enclosureGroupUri": "EG:" + PROFILE1_EG, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                      "macType": "Physical", "wwnType": "Physical", "name": PROFILE1_NAME, "description": "", "affinity": "Bay",
                      "connectionSettings": {"connections": [
                          {"id": 1, "name": "pxe-boot", "functionType": "Ethernet", "portId": "Mezz 3:1-a", "requestedMbps": "2500",
                           "networkUri": 'ETH:net300',
                           "boot": {"priority": "Primary"}, "requestedVFs": "Auto"},
                          {"id": 2, "name": "iscsi-boot", "functionType": "Ethernet", "portId": "Mezz 3:2-a", "requestedMbps": "2500",
                              "networkUri": 'ETH:network-tunnel',
                              "ipv4": {
                                  "ipAddressSource": "UserDefined",
                                  "ipAddress": PROFILE1_INITIATOR_IP_1,
                                  "subnetMask": INITIATOR_SUBNET_MASK,
                                  "gateway": INITIATOR_GATEWAY
                              },
                              "boot": {
                                  "priority": "Primary", "ethernetBootType": "iSCSI",
                                  "iscsi": {"initiatorNameSource": "ProfileInitiatorName",
                                            "bootTargetName": PROFILE1_BOOT_TARGET_NAME,
                                            "bootTargetLun": "0", "firstBootTargetIp": FIRST_BOOT_TARGET_IP, "firstBootTargetPort": "3260",
                                            "secondBootTargetIp": "", "secondBootTargetPort": "", "chapLevel": "Chap",
                                            "chapName": PROFILE1_CHAP_NAME, "chapSecret": CHAP_SECRET, "mutualChapName": "", "mutualChapSecret": None
                                            }},
                              "requestedVFs": "Auto"}
                      ]},
                      "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                      "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                      "bios": {"manageBios": False, "overriddenSettings": []},
                      "hideUnusedFlexNics": True, "iscsiInitiatorName": PROFILE1_INITIATOR_NAME,
                      "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                      }

# Profile1: ENC1 bay 1, Blackbird
# Static with gateway unset. OV will set gateway to 0.0.0.0 in RIS
# Connection initiator name uses profile defined
# Profile initiator name is user defined
# Primary unboot connection on Mezz3:2a to tunnel network
profile1_one_unbootable_connection = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + PROFILE1_SERVER, 'enclosureUri': 'ENC:' + PROFILE1_ENC,
                                      "enclosureGroupUri": "EG:" + PROFILE1_EG, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                      "macType": "Physical", "wwnType": "Physical", "name": PROFILE1_NAME, "description": "", "affinity": "Bay",
                                      "connectionSettings": {"connections": [
                                          {"id": 1, "name": "", "functionType": "Ethernet", "portId": "Mezz 3:2-a", "requestedMbps": "2500",
                                           "networkUri": 'ETH:network-tunnel', "boot": {"priority": "NotBootable"}, "requestedVFs": "Auto"}
                                      ]},
                                      "boot": {"manageBoot": True, "order": ["PXE"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                      "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                      "bios": {"manageBios": False, "overriddenSettings": []},
                                      "hideUnusedFlexNics": True, "iscsiInitiatorName": PROFILE1_INITIATOR_NAME,
                                      "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                      }

# Profile1: ENC1 bay 1, Blackbird
# Static with gateway unset. OV will set gateway to 0.0.0.0 in RIS
# Connection initiator name uses profile defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on Mezz3:2a to tunnel network
# CHAP
profile1_one_connection_ip1 = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + PROFILE1_SERVER, 'enclosureUri': 'ENC:' + PROFILE1_ENC,
                               "enclosureGroupUri": "EG:" + PROFILE1_EG, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                               "macType": "Physical", "wwnType": "Physical", "name": PROFILE1_NAME, "description": "", "affinity": "Bay",
                               "connectionSettings": {"connections": [
                                   {"id": 1, "name": "iSCSI-boot-primary", "functionType": "Ethernet", "portId": "Mezz 3:2-a", "requestedMbps": "2500", "networkUri": 'ETH:network-tunnel',
                                    "ipv4": {
                                        "ipAddressSource": "UserDefined",
                                        "ipAddress": PROFILE1_INITIATOR_IP_1,
                                        "subnetMask": INITIATOR_SUBNET_MASK,
                                        "gateway": INITIATOR_GATEWAY
                                    },
                                    "boot": {
                                        "priority": "Primary", "ethernetBootType": "iSCSI",
                                        "iscsi": {"initiatorNameSource": "ProfileInitiatorName",
                                                  "bootTargetName": PROFILE1_BOOT_TARGET_NAME,
                                                  "bootTargetLun": "0", "firstBootTargetIp": FIRST_BOOT_TARGET_IP, "firstBootTargetPort": "3260",
                                                  "secondBootTargetIp": "", "secondBootTargetPort": "", "chapLevel": "Chap",
                                                  "chapName": PROFILE1_CHAP_NAME, "chapSecret": CHAP_SECRET, "mutualChapName": "", "mutualChapSecret": None
                                                  }},
                                       "requestedVFs": "Auto"}
                               ]},
                               "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                               "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                               "bios": {"manageBios": False, "overriddenSettings": []},
                               "hideUnusedFlexNics": True, "iscsiInitiatorName": PROFILE1_INITIATOR_NAME,
                               "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                               }


# Profile1: ENC1 bay 1, Blackbird
# Static with gateway unset. OV will set gateway to 0.0.0.0 in RIS
# Connection initiator name uses profile defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on Mezz3:2a to tunnel network, initiator IP updated
# CHAP
profile1_one_connection_ip2 = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + PROFILE1_SERVER, 'enclosureUri': 'ENC:' + PROFILE1_ENC,
                               "enclosureGroupUri": "EG:" + PROFILE1_EG, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                               "macType": "Physical", "wwnType": "Physical", "name": PROFILE1_NAME, "description": "", "affinity": "Bay",
                               "connectionSettings": {"connections": [
                                   {"id": 1, "name": "iSCSI-boot-primary", "functionType": "Ethernet", "portId": "Mezz 3:2-a", "requestedMbps": "2500", "networkUri": 'ETH:network-tunnel',
                                    "ipv4": {
                                        "ipAddressSource": "UserDefined",
                                        "ipAddress": PROFILE1_INITIATOR_IP_2,
                                        "subnetMask": INITIATOR_SUBNET_MASK,
                                        "gateway": INITIATOR_GATEWAY
                                    },
                                    "boot": {
                                        "priority": "Primary", "ethernetBootType": "iSCSI",
                                        "iscsi": {"initiatorNameSource": "ProfileInitiatorName",
                                                  "bootTargetName": PROFILE1_BOOT_TARGET_NAME,
                                                  "bootTargetLun": "0", "firstBootTargetIp": FIRST_BOOT_TARGET_IP, "firstBootTargetPort": "3260",
                                                  "secondBootTargetIp": "", "secondBootTargetPort": "", "chapLevel": "Chap",
                                                  "chapName": PROFILE1_CHAP_NAME, "chapSecret": CHAP_SECRET, "mutualChapName": "", "mutualChapSecret": None
                                                  }},
                                       "requestedVFs": "Auto"}
                               ]},
                               "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                               "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                               "bios": {"manageBios": False, "overriddenSettings": []},
                               "hideUnusedFlexNics": True, "iscsiInitiatorName": PROFILE1_INITIATOR_NAME,
                               "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                               }

# Profile1: ENC1 bay 1, blackbird
# static with gateway unset. OV will set gateway to 0.0.0.0
# Connection initiator name uses profile defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on Mezz3:2a to untagged network and secondary on Mezz3:1a to tunnel network
# CHAP
profile1_two_connections = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + PROFILE1_SERVER, 'enclosureUri': 'ENC:' + PROFILE1_ENC,
                            "enclosureGroupUri": "EG:" + PROFILE1_EG, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                            "macType": "Physical", "wwnType": "Physical", "name": PROFILE1_NAME, "description": "", "affinity": "Bay",
                            "connectionSettings": {"connections": [
                                {"id": 1, "name": "iSCSI-boot-primary", "functionType": "Ethernet", "portId": "Mezz 3:2-a", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                                 "ipv4": {
                                     "ipAddressSource": "UserDefined",
                                     "ipAddress": PROFILE1_INITIATOR_IP_2,
                                     "subnetMask": INITIATOR_SUBNET_MASK,
                                     "gateway": INITIATOR_GATEWAY
                                 },
                                 "boot": {
                                     "priority": "Primary", "ethernetBootType": "iSCSI",
                                     "iscsi": {"initiatorNameSource": "ProfileInitiatorName",
                                               "bootTargetName": PROFILE1_BOOT_TARGET_NAME,
                                               "bootTargetLun": "0", "firstBootTargetIp": FIRST_BOOT_TARGET_IP, "firstBootTargetPort": "3260",
                                               "secondBootTargetIp": "", "secondBootTargetPort": "", "chapLevel": "Chap",
                                               "chapName": PROFILE1_CHAP_NAME, "chapSecret": CHAP_SECRET, "mutualChapName": "", "mutualChapSecret": None
                                               }},
                                    "requestedVFs": "Auto"},
                                {"id": 2, "name": "iSCSI-boot-secondary", "functionType": "Ethernet", "portId": "Mezz 3:1-a", "requestedMbps": "2500", "networkUri": 'ETH:network-tunnel',
                                 "ipv4": {
                                     "ipAddressSource": "UserDefined",
                                     "ipAddress": PROFILE1_INITIATOR_IP_1,
                                     "subnetMask": INITIATOR_SUBNET_MASK,
                                     "gateway": INITIATOR_GATEWAY
                                 },
                                 "boot": {
                                     "priority": "Secondary", "ethernetBootType": "iSCSI",
                                     "iscsi": {"initiatorNameSource": "ProfileInitiatorName",
                                               "bootTargetName": PROFILE1_BOOT_TARGET_NAME,
                                               "bootTargetLun": "0", "firstBootTargetIp": FIRST_BOOT_TARGET_IP, "firstBootTargetPort": "3260",
                                               "secondBootTargetIp": "", "secondBootTargetPort": "", "chapLevel": "Chap",
                                               "chapName": PROFILE1_CHAP_NAME, "chapSecret": CHAP_SECRET, "mutualChapName": "", "mutualChapSecret": None
                                               }},
                                    "requestedVFs": "Auto"}
                            ]},
                            "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                            "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                            "bios": {"manageBios": False, "overriddenSettings": []},
                            "hideUnusedFlexNics": True, "iscsiInitiatorName": PROFILE1_INITIATOR_NAME,
                            "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                            }

profile2_uefi = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + PROFILE2_SERVER, 'enclosureUri': 'ENC:' + PROFILE2_ENC,
                 "enclosureGroupUri": "EG:" + PROFILE2_EG, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                 "macType": "Physical", "wwnType": "Physical", "name": PROFILE2_NAME, "description": "", "affinity": "Bay",
                 "connectionSettings": {"connections": []},
                 "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                 "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                 "bios": {"manageBios": False, "overriddenSettings": []},
                 "hideUnusedFlexNics": True, "iscsiInitiatorName": PROFILE2_INITIATOR_NAME,
                 "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                 }

# Profile2: ENC2 bay5, Redbird
# static with gateway set to 192.168.0.1
# Connection initiator name is user defined
# Profile initiator name is user-defined
# Primary iSCSI boot connection on 3:1a and secondary on  3:2a
# Primary PXE boot on on  Mezz 3:2a
profile2_pxe_iscsi = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + PROFILE2_SERVER, 'enclosureUri': 'ENC:' + PROFILE2_ENC,
                      "enclosureGroupUri": "EG:" + PROFILE2_EG, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                      "macType": "Physical", "wwnType": "Physical", "name": PROFILE2_NAME, "description": "", "affinity": "Bay",
                      "connectionSettings": {"connections": [
                          {"id": 1, "name": "iSCSI-boot", "functionType": "Ethernet", "portId": "Mezz 3:1-a", "requestedMbps": "2500",
                           "networkUri": 'ETH:network-tunnel',
                           "ipv4": {
                               "ipAddressSource": "UserDefined",
                               "ipAddress": PROFILE2_INITIATOR_IP_1,
                               "subnetMask": INITIATOR_SUBNET_MASK,
                               "gateway": INITIATOR_GATEWAY
                           },
                           "boot": {
                               "priority": "Primary", "ethernetBootType": "iSCSI",
                               "iscsi": {"initiatorNameSource": "UserDefined",
                                         "initiatorName": PROFILE2_INITIATOR_NAME,
                                         "bootTargetName": PROFILE2_BOOT_TARGET_NAME,
                                         "bootTargetLun": "0", "firstBootTargetIp": FIRST_BOOT_TARGET_IP, "firstBootTargetPort": "3260",
                                         "secondBootTargetIp": "", "secondBootTargetPort": "", "chapLevel": "MutualChap",
                                         "chapName": PROFILE2_CHAP_NAME, "chapSecret": CHAP_SECRET,
                                         "mutualChapName": PROFILE2_MCHAP_NAME, "mutualChapSecret": MCHAP_SECRET
                                         }},
                              "requestedVFs": "Auto"},
                          {"id": 2, "name": "pxe-boot", "functionType": "Ethernet", "portId": "Mezz 3:2-a", "requestedMbps": "2500",
                              "networkUri": 'ETH:net300', "boot": {"priority": "Primary"}, "requestedVFs": "Auto"}
                      ]},
                      "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                      "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                      "bios": {"manageBios": False, "overriddenSettings": []},
                      "hideUnusedFlexNics": True, "iscsiInitiatorName": PROFILE2_INITIATOR_NAME,
                      "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                      }

# Profile2: ENC2 bay5, Redbird
# static with gateway set to 192.168.0.1
# Connection initiator name is user defined
# Profile initiator name is user-defined
# Primary iSCSI boot connection on 3:1a and secondary on  3:2a to untagged network
# MCHAP
profile2_two_connections = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + PROFILE2_SERVER, 'enclosureUri': 'ENC:' + PROFILE2_ENC,
                            "enclosureGroupUri": "EG:" + PROFILE2_EG, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                            "macType": "Physical", "wwnType": "Physical", "name": PROFILE2_NAME, "description": "", "affinity": "Bay",
                            "connectionSettings": {"connections": [
                                {"id": 1, "name": "iSCSI-boot-primary", "functionType": "Ethernet", "portId": "Mezz 3:1-a", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                                 "ipv4": {
                                     "ipAddressSource": "UserDefined",
                                     "ipAddress": PROFILE2_INITIATOR_IP_1,
                                     "subnetMask": INITIATOR_SUBNET_MASK,
                                     "gateway": INITIATOR_GATEWAY
                                 },
                                 "boot": {
                                     "priority": "Primary", "ethernetBootType": "iSCSI",
                                     "iscsi": {"initiatorNameSource": "UserDefined",
                                               "initiatorName": PROFILE2_INITIATOR_NAME,
                                               "bootTargetName": PROFILE2_BOOT_TARGET_NAME,
                                               "bootTargetLun": "0", "firstBootTargetIp": FIRST_BOOT_TARGET_IP, "firstBootTargetPort": "3260",
                                               "secondBootTargetIp": "", "secondBootTargetPort": "", "chapLevel": "MutualChap",
                                               "chapName": PROFILE2_CHAP_NAME, "chapSecret": CHAP_SECRET,
                                               "mutualChapName": PROFILE2_MCHAP_NAME, "mutualChapSecret": MCHAP_SECRET
                                               }},
                                    "requestedVFs": "Auto"},
                                {"id": 2, "name": "iSCSI-boot-seondary", "functionType": "Ethernet", "portId": "Mezz 3:2-a", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                                 "ipv4": {
                                     "ipAddressSource": "UserDefined",
                                     "ipAddress": PROFILE2_INITIATOR_IP_2,
                                     "subnetMask": INITIATOR_SUBNET_MASK,
                                     "gateway": INITIATOR_GATEWAY
                                 },
                                 "boot": {
                                     "priority": "Secondary", "ethernetBootType": "iSCSI",
                                     "iscsi": {"initiatorNameSource": "UserDefined",
                                               "initiatorName": PROFILE2_INITIATOR_NAME,
                                               "bootTargetName": PROFILE2_BOOT_TARGET_NAME,
                                               "bootTargetLun": "0", "firstBootTargetIp": FIRST_BOOT_TARGET_IP, "firstBootTargetPort": "3260",
                                               "secondBootTargetIp": "", "secondBootTargetPort": "", "chapLevel": "MutualChap",
                                               "chapName": PROFILE2_CHAP_NAME, "chapSecret": CHAP_SECRET,
                                               "mutualChapName": PROFILE2_MCHAP_NAME, "mutualChapSecret": MCHAP_SECRET
                                               }},
                                    "requestedVFs": "Auto"}
                            ]},
                            "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                            "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                            "bios": {"manageBios": False, "overriddenSettings": []},
                            "hideUnusedFlexNics": True, "iscsiInitiatorName": PROFILE2_INITIATOR_NAME,
                            "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                            }

# Profile2: ENC2 bay5, Redbird
# static with gateway set to 192.168.0.1
# Connection initiator name is user defined
# Profile initiator name is user-defined
# Primary boot connection on 3:1a on untagged network
# MCHAP
profile2_one_connection_ip1 = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + PROFILE2_SERVER, 'enclosureUri': 'ENC:' + PROFILE2_ENC,
                               "enclosureGroupUri": "EG:" + PROFILE2_EG, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                               "macType": "Physical", "wwnType": "Physical", "name": PROFILE2_NAME, "description": "", "affinity": "Bay",
                               "connectionSettings": {"connections": [
                                   {"id": 1, "name": "iSCSI-boot-primary", "functionType": "Ethernet", "portId": "Mezz 3:1-a", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                                    "ipv4": {
                                        "ipAddressSource": "UserDefined",
                                        "ipAddress": PROFILE2_INITIATOR_IP_1,
                                        "subnetMask": INITIATOR_SUBNET_MASK,
                                        "gateway": INITIATOR_GATEWAY
                                    },
                                    "boot": {
                                        "priority": "Primary", "ethernetBootType": "iSCSI",
                                        "iscsi": {"initiatorNameSource": "UserDefined",
                                                  "initiatorName": PROFILE2_INITIATOR_NAME,
                                                  "bootTargetName": PROFILE2_BOOT_TARGET_NAME,
                                                  "bootTargetLun": "0", "firstBootTargetIp": FIRST_BOOT_TARGET_IP, "firstBootTargetPort": "3260",
                                                  "secondBootTargetIp": "", "secondBootTargetPort": "", "chapLevel": "MutualChap",
                                                  "chapName": PROFILE2_CHAP_NAME, "chapSecret": CHAP_SECRET,
                                                  "mutualChapName": PROFILE2_MCHAP_NAME, "mutualChapSecret": MCHAP_SECRET
                                                  }},
                                       "requestedVFs": "Auto"}
                               ]},
                               "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                               "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                               "bios": {"manageBios": False, "overriddenSettings": []},
                               "hideUnusedFlexNics": True, "iscsiInitiatorName": PROFILE2_INITIATOR_NAME,
                               "localStorage": {"sasLogicalJBODs": [], "controllers": []},
                               }

# Profile2: ENC2 bay5, Redbird
# Profile initiator name is user-defined
# Primary unbootable connection on 3:1a and secondary connection on 3:2a
# to untagged network=
profile2_two_unbootable_connections = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + PROFILE2_SERVER, 'enclosureUri': 'ENC:' + PROFILE2_ENC,
                                       "enclosureGroupUri": "EG:" + PROFILE2_EG, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                       "macType": "Physical", "wwnType": "Physical", "name": PROFILE2_NAME, "description": "", "affinity": "Bay",
                                       "connectionSettings": {"connections": [
                                           {"id": 1, "name": "", "functionType": "Ethernet", "portId": "Mezz 3:1-a", "requestedMbps": "2500",
                                            "networkUri": 'ETH:network-untagged', "boot": {"priority": "NotBootable"}, "requestedVFs": "Auto"},
                                           {"id": 2, "name": "", "functionType": "Ethernet", "portId": "Mezz 3:2-a", "requestedMbps": "2500",
                                            "networkUri": 'ETH:network-untagged', "boot": {"priority": "NotBootable"}, "requestedVFs": "Auto"}
                                       ]},
                                       "boot": {"manageBoot": True, "order": ["PXE"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                       "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                       "bios": {"manageBios": False, "overriddenSettings": []},
                                       "hideUnusedFlexNics": True, "iscsiInitiatorName": PROFILE2_INITIATOR_NAME,
                                       "localStorage": {"sasLogicalJBODs": [], "controllers": []},
                                       }


# Profile2: ENC2 bay5, Redbird
# static with gateway set to 192.168.0.1
# Connection initiator name is user defined
# Profile initiator name is user-defined
# Primary boot connection on 3:1a to tunnel network
# MCHAP
profile2_one_connection_ip2 = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + PROFILE2_SERVER, 'enclosureUri': 'ENC:' + PROFILE2_ENC,
                               "enclosureGroupUri": "EG:" + PROFILE2_EG, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                               "macType": "Physical", "wwnType": "Physical", "name": PROFILE2_NAME, "description": "", "affinity": "Bay",
                               "connectionSettings": {"connections": [
                                   {"id": 1, "name": "iSCSI-boot-primary", "functionType": "Ethernet", "portId": "Mezz 3:1-a", "requestedMbps": "2500", "networkUri": 'ETH:network-tunnel',
                                    "ipv4": {
                                        "ipAddressSource": "UserDefined",
                                        "ipAddress": PROFILE2_INITIATOR_IP_2,
                                        "subnetMask": INITIATOR_SUBNET_MASK,
                                        "gateway": INITIATOR_GATEWAY
                                    },
                                    "boot": {
                                        "priority": "Primary", "ethernetBootType": "iSCSI",
                                        "iscsi": {"initiatorNameSource": "UserDefined",
                                                  "initiatorName": PROFILE2_INITIATOR_NAME,
                                                  "bootTargetName": PROFILE2_BOOT_TARGET_NAME,
                                                  "bootTargetLun": "0", "firstBootTargetIp": FIRST_BOOT_TARGET_IP, "firstBootTargetPort": "3260",
                                                  "secondBootTargetIp": "", "secondBootTargetPort": "", "chapLevel": "MutualChap",
                                                  "chapName": PROFILE2_CHAP_NAME, "chapSecret": CHAP_SECRET,
                                                  "mutualChapName": PROFILE2_MCHAP_NAME, "mutualChapSecret": MCHAP_SECRET
                                                  }},
                                       "requestedVFs": "Auto"}
                               ]},
                               "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                               "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                               "bios": {"manageBios": False, "overriddenSettings": []},
                               "hideUnusedFlexNics": True, "iscsiInitiatorName": PROFILE2_INITIATOR_NAME,
                               "localStorage": {"sasLogicalJBODs": [], "controllers": []},
                               }

profile3_uefi = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + PROFILE3_SERVER, 'enclosureUri': 'ENC:' + PROFILE3_ENC,
                 "enclosureGroupUri": "EG:" + PROFILE3_EG, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                 "macType": "Physical", "wwnType": "Physical", "name": PROFILE3_NAME, "description": "", "affinity": "Bay",
                 "connectionSettings": {"connections": []},
                 "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                 "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                 "bios": {"manageBios": False, "overriddenSettings": []},
                 "hideUnusedFlexNics": True, "iscsiInitiatorName": PROFILE3_INITIATOR_NAME,
                 "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                 }

# Profile3: profile2 moved to ENC2 bay1
# static with gateway set to 192.168.0.1
# Connection initiator name uses profile initiator name.
# Profile initiator name is user defined
# Primary boot connection on Mezz3:1a to tunnel network and secondary on Mezz3:2a to untagged network
# NO CHAP
profile3_two_connections = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + PROFILE3_SERVER, 'enclosureUri': 'ENC:' + PROFILE3_ENC,
                            "enclosureGroupUri": "EG:" + PROFILE3_EG, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                            "macType": "Physical", "wwnType": "Physical", "name": PROFILE2_NAME, "description": "", "affinity": "Bay",
                            "connectionSettings": {"connections": [
                                {"id": 1, "name": "iSCSI-boot-primary", "functionType": "Ethernet", "portId": "Mezz 3:1-a", "requestedMbps": "2500", "networkUri": 'ETH:network-tunnel',
                                 "ipv4": {
                                     "ipAddressSource": "UserDefined",
                                     "ipAddress": PROFILE3_INITIATOR_IP_1,
                                     "subnetMask": INITIATOR_SUBNET_MASK,
                                     "gateway": INITIATOR_GATEWAY
                                 },
                                 "boot": {
                                     "priority": "Primary", "ethernetBootType": "iSCSI",
                                     "iscsi": {"initiatorNameSource": "ProfileInitiatorName",
                                               "bootTargetName": PROFILE3_BOOT_TARGET_NAME,
                                               "bootTargetLun": "0", "firstBootTargetIp": FIRST_BOOT_TARGET_IP, "firstBootTargetPort": "3260",
                                               "secondBootTargetIp": "", "secondBootTargetPort": "", "chapLevel": "None", "chapName": "",
                                               "chapSecret": None, "mutualChapName": "", "mutualChapSecret": None
                                               }},
                                    "requestedVFs": "Auto"},
                                {"id": 2, "name": "iSCSI-boot-secondary", "functionType": "Ethernet", "portId": "Mezz 3:2-a", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                                 "ipv4": {
                                     "ipAddressSource": "UserDefined",
                                     "ipAddress": PROFILE3_INITIATOR_IP_2,
                                     "subnetMask": INITIATOR_SUBNET_MASK,
                                     "gateway": INITIATOR_GATEWAY
                                 },
                                 "boot": {
                                     "priority": "Secondary", "ethernetBootType": "iSCSI",
                                     "iscsi": {"initiatorNameSource": "ProfileInitiatorName",
                                               "bootTargetName": PROFILE3_BOOT_TARGET_NAME,
                                               "bootTargetLun": "0", "firstBootTargetIp": FIRST_BOOT_TARGET_IP, "firstBootTargetPort": "3260",
                                               "secondBootTargetIp": "", "secondBootTargetPort": "", "chapLevel": "None", "chapName": "",
                                               "chapSecret": None, "mutualChapName": "", "mutualChapSecret": None
                                               }},
                                    "requestedVFs": "Auto"}
                            ]},
                            "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                            "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                            "bios": {"manageBios": False, "overriddenSettings": []},
                            "hideUnusedFlexNics": True, "iscsiInitiatorName": PROFILE3_INITIATOR_NAME,
                            "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                            }

profile4_uefi = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + PROFILE4_SERVER, 'enclosureUri': 'ENC:' + PROFILE4_ENC,
                 "enclosureGroupUri": "EG:" + PROFILE4_EG, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                 "macType": "Physical", "wwnType": "Physical", "name": PROFILE4_NAME, "description": "", "affinity": "Bay",
                 "connectionSettings": {"connections": []},
                 "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                 "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                 "bios": {"manageBios": False, "overriddenSettings": []},
                 "hideUnusedFlexNics": True, "iscsiInitiatorName": PROFILE4_INITIATOR_NAME,
                 "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                 }

# Profile4: profile1 moved to ENC1 bay8
# static with gateway set to 192.168.0.1
# Connection initiator name uses profile initiator name.
# Profile initiator name is user defined
# Primary boot connection on Mezz3:1a to tunnel network and secondary on Mezz3:2a to untagged network
# NO CHAP
profile4_two_connections = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + PROFILE4_SERVER, 'enclosureUri': 'ENC:' + PROFILE4_ENC,
                            "enclosureGroupUri": "EG:" + PROFILE4_EG, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                            "macType": "Physical", "wwnType": "Physical", "name": PROFILE1_NAME, "description": "", "affinity": "Bay",
                            "connectionSettings": {"connections": [
                                {"id": 1, "name": "iSCSI-boot-primary", "functionType": "Ethernet", "portId": "Mezz 3:1-a", "requestedMbps": "2500", "networkUri": 'ETH:network-tunnel',
                                 "ipv4": {
                                     "ipAddressSource": "UserDefined",
                                     "ipAddress": PROFILE4_INITIATOR_IP_1,
                                     "subnetMask": INITIATOR_SUBNET_MASK,
                                     "gateway": INITIATOR_GATEWAY
                                 },
                                 "boot": {
                                     "priority": "Primary", "ethernetBootType": "iSCSI",
                                     "iscsi": {"initiatorNameSource": "ProfileInitiatorName",
                                               "bootTargetName": PROFILE4_BOOT_TARGET_NAME,
                                               "bootTargetLun": "0", "firstBootTargetIp": FIRST_BOOT_TARGET_IP, "firstBootTargetPort": "3260",
                                               "secondBootTargetIp": "", "secondBootTargetPort": "", "chapLevel": "None", "chapName": "",
                                               "chapSecret": None, "mutualChapName": "", "mutualChapSecret": None
                                               }},
                                    "requestedVFs": "Auto"},
                                {"id": 2, "name": "iSCSI-boot-secondary", "functionType": "Ethernet", "portId": "Mezz 3:2-a", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                                 "ipv4": {
                                     "ipAddressSource": "UserDefined",
                                     "ipAddress": PROFILE4_INITIATOR_IP_2,
                                     "subnetMask": INITIATOR_SUBNET_MASK,
                                     "gateway": INITIATOR_GATEWAY
                                 },
                                 "boot": {
                                     "priority": "Secondary", "ethernetBootType": "iSCSI",
                                     "iscsi": {"initiatorNameSource": "ProfileInitiatorName",
                                               "bootTargetName": PROFILE4_BOOT_TARGET_NAME,
                                               "bootTargetLun": "0", "firstBootTargetIp": FIRST_BOOT_TARGET_IP, "firstBootTargetPort": "3260",
                                               "secondBootTargetIp": "", "secondBootTargetPort": "", "chapLevel": "None", "chapName": "",
                                               "chapSecret": None, "mutualChapName": "", "mutualChapSecret": None
                                               }},
                                    "requestedVFs": "Auto"}
                            ]},
                            "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                            "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                            "bios": {"manageBios": False, "overriddenSettings": []},
                            "hideUnusedFlexNics": True, "iscsiInitiatorName": PROFILE4_INITIATOR_NAME,
                            "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                            }

# RIS Nodes

# Profile1, ENC1 bay7
ris_node_profile1_no_iscsi = {
    "server": PROFILE1_SERVER,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/bios/iSCSI",
    "validate": {
        "Name": "iSCSI Software Initiator Current Settings",
        "iSCSIBootSources":
        [
            {
                "iSCSIBootEnable": "Disabled",
            },
            {
                "iSCSIBootEnable": "Disabled",
            },
            {
                "iSCSIBootEnable": "Disabled",
            },
            {
                "iSCSIBootEnable": "Disabled",
            },
        ],
    }
}

# Profile1: ENC1 bay7, one iSCSI boot connection to initiator IP1
ris_node_profile1_one_connection_ip1 = {
    "server": PROFILE1_SERVER,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/bios/iSCSI",
    "validate": {
        "Name": "iSCSI Software Initiator Current Settings",
        "iSCSIBootSources":
        [
            {
                "StructuredBootString": "NIC.Slot.3.2.iSCSI",
                "iSCSIAuthenticationMethod": "Chap",
                "iSCSIBootAttemptInstance": 1,
                "iSCSIBootAttemptName": PROFILE1_ISCSI_BOOT_ATTEMPT_1,
                "iSCSIBootEnable": "Enabled",
                "iSCSIBootLUN": "0",
                "iSCSIChapSecret": None,
                "iSCSIChapType": "OneWay",
                "iSCSIChapUsername": None,
                "iSCSIConnectRetry": 3,
                "iSCSIConnectTimeoutMS": 20000,
                "iSCSIInitiatorGateway": INITIATOR_GATEWAY,
                "iSCSIInitiatorInfoViaDHCP": False,
                "iSCSIInitiatorIpAddress": PROFILE1_INITIATOR_IP_1,
                "iSCSIInitiatorNetmask": INITIATOR_SUBNET_MASK,
                "iSCSIIpAddressType": "IPv4",
                "iSCSINicSource": "Slot3NicBoot2",
                "iSCSIReverseChapSecret": None,
                "iSCSIReverseChapUsername": None,
                "iSCSITargetInfoViaDHCP": False,
                "iSCSITargetIpAddress": FIRST_BOOT_TARGET_IP,
                "iSCSITargetName": PROFILE1_BOOT_TARGET_NAME,
                "iSCSITargetTcpPort": 3260
            },
            {
                "StructuredBootString": None,
                "UEFIDevicePath": None,
                "iSCSIAuthenticationMethod": "None",
                "iSCSIBootAttemptInstance": 0,
                "iSCSIBootAttemptName": "",
                "iSCSIBootEnable": "Disabled",
                "iSCSIBootLUN": "0",
                "iSCSIChapSecret": None,
                "iSCSIChapType": "OneWay",
                "iSCSIChapUsername": None,
                "iSCSIConnectRetry": 3,
                "iSCSIConnectTimeoutMS": 20000,
                "iSCSIInitiatorGateway": "0.0.0.0",
                "iSCSIInitiatorInfoViaDHCP": True,
                "iSCSIInitiatorIpAddress": "0.0.0.0",
                "iSCSIInitiatorNetmask": "0.0.0.0",
                "iSCSIIpAddressType": "IPv4",
                "iSCSINicSource": None,
                "iSCSIReverseChapSecret": None,
                "iSCSIReverseChapUsername": None,
                "iSCSITargetInfoViaDHCP": True,
                "iSCSITargetIpAddress": "0.0.0.0",
                "iSCSITargetName": None,
                "iSCSITargetTcpPort": 3260
            },
            {
                "StructuredBootString": None,
                "UEFIDevicePath": None,
                "iSCSIAuthenticationMethod": "None",
                "iSCSIBootAttemptInstance": 0,
                "iSCSIBootAttemptName": "",
                "iSCSIBootEnable": "Disabled",
                "iSCSIBootLUN": "0",
                "iSCSIChapSecret": None,
                "iSCSIChapType": "OneWay",
                "iSCSIChapUsername": None,
                "iSCSIConnectRetry": 3,
                "iSCSIConnectTimeoutMS": 20000,
                "iSCSIInitiatorGateway": "0.0.0.0",
                "iSCSIInitiatorInfoViaDHCP": True,
                "iSCSIInitiatorIpAddress": "0.0.0.0",
                "iSCSIInitiatorNetmask": "0.0.0.0",
                "iSCSIIpAddressType": "IPv4",
                "iSCSINicSource": None,
                "iSCSIReverseChapSecret": None,
                "iSCSIReverseChapUsername": None,
                "iSCSITargetInfoViaDHCP": True,
                "iSCSITargetIpAddress": "0.0.0.0",
                "iSCSITargetName": None,
                "iSCSITargetTcpPort": 3260
            },
            {
                "StructuredBootString": None,
                "UEFIDevicePath": None,
                "iSCSIAuthenticationMethod": "None",
                "iSCSIBootAttemptInstance": 0,
                "iSCSIBootAttemptName": "",
                "iSCSIBootEnable": "Disabled",
                "iSCSIBootLUN": "0",
                "iSCSIChapSecret": None,
                "iSCSIChapType": "OneWay",
                "iSCSIChapUsername": None,
                "iSCSIConnectRetry": 3,
                "iSCSIConnectTimeoutMS": 20000,
                "iSCSIInitiatorGateway": "0.0.0.0",
                "iSCSIInitiatorInfoViaDHCP": True,
                "iSCSIInitiatorIpAddress": "0.0.0.0",
                "iSCSIInitiatorNetmask": "0.0.0.0",
                "iSCSIIpAddressType": "IPv4",
                "iSCSINicSource": None,
                "iSCSIReverseChapSecret": None,
                "iSCSIReverseChapUsername": None,
                "iSCSITargetInfoViaDHCP": True,
                "iSCSITargetIpAddress": "0.0.0.0",
                "iSCSITargetName": None,
                "iSCSITargetTcpPort": 3260
            }
        ],
        "iSCSIInitiatorName": PROFILE1_INITIATOR_NAME,
    }
}

# Profile1: ENC1 bay7, one iSCSI boot connection to initiator IP2
ris_node_profile1_one_connection_ip2 = {
    "server": PROFILE1_SERVER,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/bios/iSCSI",
    "validate": {
        "Name": "iSCSI Software Initiator Current Settings",
        "iSCSIBootSources":
        [
            {
                "StructuredBootString": "NIC.Slot.3.2.iSCSI",
                "iSCSIAuthenticationMethod": "Chap",
                "iSCSIBootAttemptInstance": 1,
                "iSCSIBootAttemptName": PROFILE1_ISCSI_BOOT_ATTEMPT_1,
                "iSCSIBootEnable": "Enabled",
                "iSCSIBootLUN": "0",
                "iSCSIChapSecret": None,
                "iSCSIChapType": "OneWay",
                "iSCSIChapUsername": None,
                "iSCSIConnectRetry": 3,
                "iSCSIConnectTimeoutMS": 20000,
                "iSCSIInitiatorGateway": INITIATOR_GATEWAY,
                "iSCSIInitiatorInfoViaDHCP": False,
                "iSCSIInitiatorIpAddress": PROFILE1_INITIATOR_IP_2,
                "iSCSIInitiatorNetmask": INITIATOR_SUBNET_MASK,
                "iSCSIIpAddressType": "IPv4",
                "iSCSINicSource": "Slot3NicBoot2",
                "iSCSIReverseChapSecret": None,
                "iSCSIReverseChapUsername": None,
                "iSCSITargetInfoViaDHCP": False,
                "iSCSITargetIpAddress": FIRST_BOOT_TARGET_IP,
                "iSCSITargetName": PROFILE1_BOOT_TARGET_NAME,
                "iSCSITargetTcpPort": 3260
            },
            {
                "StructuredBootString": None,
                "UEFIDevicePath": None,
                "iSCSIAuthenticationMethod": "None",
                "iSCSIBootAttemptInstance": 0,
                "iSCSIBootAttemptName": "",
                "iSCSIBootEnable": "Disabled",
                "iSCSIBootLUN": "0",
                "iSCSIChapSecret": None,
                "iSCSIChapType": "OneWay",
                "iSCSIChapUsername": None,
                "iSCSIConnectRetry": 3,
                "iSCSIConnectTimeoutMS": 20000,
                "iSCSIInitiatorGateway": "0.0.0.0",
                "iSCSIInitiatorInfoViaDHCP": True,
                "iSCSIInitiatorIpAddress": "0.0.0.0",
                "iSCSIInitiatorNetmask": "0.0.0.0",
                "iSCSIIpAddressType": "IPv4",
                "iSCSINicSource": None,
                "iSCSIReverseChapSecret": None,
                "iSCSIReverseChapUsername": None,
                "iSCSITargetInfoViaDHCP": True,
                "iSCSITargetIpAddress": "0.0.0.0",
                "iSCSITargetName": None,
                "iSCSITargetTcpPort": 3260
            },
            {
                "StructuredBootString": None,
                "UEFIDevicePath": None,
                "iSCSIAuthenticationMethod": "None",
                "iSCSIBootAttemptInstance": 0,
                "iSCSIBootAttemptName": "",
                "iSCSIBootEnable": "Disabled",
                "iSCSIBootLUN": "0",
                "iSCSIChapSecret": None,
                "iSCSIChapType": "OneWay",
                "iSCSIChapUsername": None,
                "iSCSIConnectRetry": 3,
                "iSCSIConnectTimeoutMS": 20000,
                "iSCSIInitiatorGateway": "0.0.0.0",
                "iSCSIInitiatorInfoViaDHCP": True,
                "iSCSIInitiatorIpAddress": "0.0.0.0",
                "iSCSIInitiatorNetmask": "0.0.0.0",
                "iSCSIIpAddressType": "IPv4",
                "iSCSINicSource": None,
                "iSCSIReverseChapSecret": None,
                "iSCSIReverseChapUsername": None,
                "iSCSITargetInfoViaDHCP": True,
                "iSCSITargetIpAddress": "0.0.0.0",
                "iSCSITargetName": None,
                "iSCSITargetTcpPort": 3260
            },
            {
                "StructuredBootString": None,
                "UEFIDevicePath": None,
                "iSCSIAuthenticationMethod": "None",
                "iSCSIBootAttemptInstance": 0,
                "iSCSIBootAttemptName": "",
                "iSCSIBootEnable": "Disabled",
                "iSCSIBootLUN": "0",
                "iSCSIChapSecret": None,
                "iSCSIChapType": "OneWay",
                "iSCSIChapUsername": None,
                "iSCSIConnectRetry": 3,
                "iSCSIConnectTimeoutMS": 20000,
                "iSCSIInitiatorGateway": "0.0.0.0",
                "iSCSIInitiatorInfoViaDHCP": True,
                "iSCSIInitiatorIpAddress": "0.0.0.0",
                "iSCSIInitiatorNetmask": "0.0.0.0",
                "iSCSIIpAddressType": "IPv4",
                "iSCSINicSource": None,
                "iSCSIReverseChapSecret": None,
                "iSCSIReverseChapUsername": None,
                "iSCSITargetInfoViaDHCP": True,
                "iSCSITargetIpAddress": "0.0.0.0",
                "iSCSITargetName": None,
                "iSCSITargetTcpPort": 3260
            }
        ],
        "iSCSIInitiatorName": PROFILE1_INITIATOR_NAME,
    }
}

# Profile1: ENC1 bay7, two iSCSI boot connections
ris_node_profile1_two_connections = {
    "server": PROFILE1_SERVER,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/bios/iSCSI",
    "validate": {
        "Name": "iSCSI Software Initiator Current Settings",
        "iSCSIBootSources":
        [
            {
                "StructuredBootString": "NIC.Slot.3.2.iSCSI",
                "iSCSIAuthenticationMethod": "Chap",
                "iSCSIBootAttemptInstance": 1,
                "iSCSIBootAttemptName": PROFILE1_ISCSI_BOOT_ATTEMPT_1,
                "iSCSIBootEnable": "Enabled",
                "iSCSIBootLUN": "0",
                "iSCSIChapSecret": None,
                "iSCSIChapType": "OneWay",
                "iSCSIChapUsername": None,
                "iSCSIConnectRetry": 3,
                "iSCSIConnectTimeoutMS": 20000,
                "iSCSIInitiatorGateway": INITIATOR_GATEWAY,
                "iSCSIInitiatorInfoViaDHCP": False,
                "iSCSIInitiatorIpAddress": PROFILE1_INITIATOR_IP_2,
                "iSCSIInitiatorNetmask": INITIATOR_SUBNET_MASK,
                "iSCSIIpAddressType": "IPv4",
                "iSCSINicSource": "Slot3NicBoot2",
                "iSCSIReverseChapSecret": None,
                "iSCSIReverseChapUsername": None,
                "iSCSITargetInfoViaDHCP": False,
                "iSCSITargetIpAddress": FIRST_BOOT_TARGET_IP,
                "iSCSITargetName": PROFILE1_BOOT_TARGET_NAME,
                "iSCSITargetTcpPort": 3260
            },
            {
                "StructuredBootString": "NIC.Slot.3.1.iSCSI",
                "iSCSIAuthenticationMethod": "Chap",
                "iSCSIBootAttemptInstance": 2,
                "iSCSIBootAttemptName": PROFILE1_ISCSI_BOOT_ATTEMPT_2,
                "iSCSIBootEnable": "Enabled",
                "iSCSIBootLUN": "0",
                "iSCSIChapSecret": None,
                "iSCSIChapType": "OneWay",
                "iSCSIChapUsername": None,
                "iSCSIConnectRetry": 3,
                "iSCSIConnectTimeoutMS": 20000,
                "iSCSIInitiatorGateway": INITIATOR_GATEWAY,
                "iSCSIInitiatorInfoViaDHCP": False,
                "iSCSIInitiatorIpAddress": PROFILE1_INITIATOR_IP_1,
                "iSCSIInitiatorNetmask": INITIATOR_SUBNET_MASK,
                "iSCSIIpAddressType": "IPv4",
                "iSCSINicSource": "Slot3NicBoot1",
                "iSCSIReverseChapSecret": None,
                "iSCSIReverseChapUsername": None,
                "iSCSITargetInfoViaDHCP": False,
                "iSCSITargetIpAddress": FIRST_BOOT_TARGET_IP,
                "iSCSITargetName": PROFILE1_BOOT_TARGET_NAME,
                "iSCSITargetTcpPort": 3260
            },
            {
                "StructuredBootString": None,
                "UEFIDevicePath": None,
                "iSCSIAuthenticationMethod": "None",
                "iSCSIBootAttemptInstance": 0,
                "iSCSIBootAttemptName": "",
                "iSCSIBootEnable": "Disabled",
                "iSCSIBootLUN": "0",
                "iSCSIChapSecret": None,
                "iSCSIChapType": "OneWay",
                "iSCSIChapUsername": None,
                "iSCSIConnectRetry": 3,
                "iSCSIConnectTimeoutMS": 20000,
                "iSCSIInitiatorGateway": "0.0.0.0",
                "iSCSIInitiatorInfoViaDHCP": True,
                "iSCSIInitiatorIpAddress": "0.0.0.0",
                "iSCSIInitiatorNetmask": "0.0.0.0",
                "iSCSIIpAddressType": "IPv4",
                "iSCSINicSource": None,
                "iSCSIReverseChapSecret": None,
                "iSCSIReverseChapUsername": None,
                "iSCSITargetInfoViaDHCP": True,
                "iSCSITargetIpAddress": "0.0.0.0",
                "iSCSITargetName": None,
                "iSCSITargetTcpPort": 3260
            },
            {
                "StructuredBootString": None,
                "UEFIDevicePath": None,
                "iSCSIAuthenticationMethod": "None",
                "iSCSIBootAttemptInstance": 0,
                "iSCSIBootAttemptName": "",
                "iSCSIBootEnable": "Disabled",
                "iSCSIBootLUN": "0",
                "iSCSIChapSecret": None,
                "iSCSIChapType": "OneWay",
                "iSCSIChapUsername": None,
                "iSCSIConnectRetry": 3,
                "iSCSIConnectTimeoutMS": 20000,
                "iSCSIInitiatorGateway": "0.0.0.0",
                "iSCSIInitiatorInfoViaDHCP": True,
                "iSCSIInitiatorIpAddress": "0.0.0.0",
                "iSCSIInitiatorNetmask": "0.0.0.0",
                "iSCSIIpAddressType": "IPv4",
                "iSCSINicSource": None,
                "iSCSIReverseChapSecret": None,
                "iSCSIReverseChapUsername": None,
                "iSCSITargetInfoViaDHCP": True,
                "iSCSITargetIpAddress": "0.0.0.0",
                "iSCSITargetName": None,
                "iSCSITargetTcpPort": 3260
            }
        ],
        "iSCSIInitiatorName": PROFILE1_INITIATOR_NAME,
    }
}

# Profile2: ENC2 bay5
ris_node_profile2_no_iscsi = {
    "server": PROFILE2_SERVER,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/bios/iSCSI",
    "validate": {
        "Name": "iSCSI Software Initiator Current Settings",
        "iSCSIBootSources":
        [
            {
                "iSCSIBootEnable": "Disabled",
            },
            {
                "iSCSIBootEnable": "Disabled",
            },
            {
                "iSCSIBootEnable": "Disabled",
            },
            {
                "iSCSIBootEnable": "Disabled",
            },
        ],
    }
}

# Profile2: ENC2 bay5, two iSCSI boot connections
ris_node_profile2_two_connections = {
    "server": PROFILE2_SERVER,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/bios/iSCSI",
    "validate": {
        "Name": "iSCSI Software Initiator Current Settings",
        "iSCSIBootSources":
        [
            {
                "StructuredBootString": "NIC.Slot.3.1.iSCSI",
                "iSCSIAuthenticationMethod": "Chap",
                "iSCSIBootAttemptInstance": 1,
                "iSCSIBootAttemptName": PROFILE2_ISCSI_BOOT_ATTEMPT_1,
                "iSCSIBootEnable": "Enabled",
                "iSCSIBootLUN": "0",
                "iSCSIChapSecret": None,
                "iSCSIChapType": "Mutual",
                "iSCSIChapUsername": None,
                "iSCSIConnectRetry": 3,
                "iSCSIConnectTimeoutMS": 20000,
                "iSCSIInitiatorGateway": INITIATOR_GATEWAY,
                "iSCSIInitiatorInfoViaDHCP": False,
                "iSCSIInitiatorIpAddress": PROFILE2_INITIATOR_IP_1,
                "iSCSIInitiatorNetmask": INITIATOR_SUBNET_MASK,
                "iSCSIIpAddressType": "IPv4",
                "iSCSINicSource": "Slot3NicBoot1",
                "iSCSIReverseChapSecret": None,
                "iSCSIReverseChapUsername": None,
                "iSCSITargetInfoViaDHCP": False,
                "iSCSITargetIpAddress": FIRST_BOOT_TARGET_IP,
                "iSCSITargetName": PROFILE2_BOOT_TARGET_NAME,
                "iSCSITargetTcpPort": 3260
            },
            {
                "StructuredBootString": "NIC.Slot.3.2.iSCSI",
                "iSCSIAuthenticationMethod": "Chap",
                "iSCSIBootAttemptInstance": 2,
                "iSCSIBootAttemptName": PROFILE2_ISCSI_BOOT_ATTEMPT_2,
                "iSCSIBootEnable": "Enabled",
                "iSCSIBootLUN": "0",
                "iSCSIChapSecret": None,
                "iSCSIChapType": "Mutual",
                "iSCSIChapUsername": None,
                "iSCSIConnectRetry": 3,
                "iSCSIConnectTimeoutMS": 20000,
                "iSCSIInitiatorGateway": INITIATOR_GATEWAY,
                "iSCSIInitiatorInfoViaDHCP": False,
                "iSCSIInitiatorIpAddress": PROFILE2_INITIATOR_IP_2,
                "iSCSIInitiatorNetmask": INITIATOR_SUBNET_MASK,
                "iSCSIIpAddressType": "IPv4",
                "iSCSINicSource": "Slot3NicBoot2",
                "iSCSIReverseChapSecret": None,
                "iSCSIReverseChapUsername": None,
                "iSCSITargetInfoViaDHCP": False,
                "iSCSITargetIpAddress": FIRST_BOOT_TARGET_IP,
                "iSCSITargetName": PROFILE2_BOOT_TARGET_NAME,
                "iSCSITargetTcpPort": 3260
            },
            {
                "StructuredBootString": None,
                "UEFIDevicePath": None,
                "iSCSIAuthenticationMethod": "None",
                "iSCSIBootAttemptInstance": 0,
                "iSCSIBootAttemptName": "",
                "iSCSIBootEnable": "Disabled",
                "iSCSIBootLUN": "0",
                "iSCSIChapSecret": None,
                "iSCSIChapType": "OneWay",
                "iSCSIChapUsername": None,
                "iSCSIConnectRetry": 3,
                "iSCSIConnectTimeoutMS": 20000,
                "iSCSIInitiatorGateway": "0.0.0.0",
                "iSCSIInitiatorInfoViaDHCP": True,
                "iSCSIInitiatorIpAddress": "0.0.0.0",
                "iSCSIInitiatorNetmask": "0.0.0.0",
                "iSCSIIpAddressType": "IPv4",
                "iSCSINicSource": None,
                "iSCSIReverseChapSecret": None,
                "iSCSIReverseChapUsername": None,
                "iSCSITargetInfoViaDHCP": True,
                "iSCSITargetIpAddress": "0.0.0.0",
                "iSCSITargetName": None,
                "iSCSITargetTcpPort": 3260
            },
            {
                "StructuredBootString": None,
                "UEFIDevicePath": None,
                "iSCSIAuthenticationMethod": "None",
                "iSCSIBootAttemptInstance": 0,
                "iSCSIBootAttemptName": "",
                "iSCSIBootEnable": "Disabled",
                "iSCSIBootLUN": "0",
                "iSCSIChapSecret": None,
                "iSCSIChapType": "OneWay",
                "iSCSIChapUsername": None,
                "iSCSIConnectRetry": 3,
                "iSCSIConnectTimeoutMS": 20000,
                "iSCSIInitiatorGateway": "0.0.0.0",
                "iSCSIInitiatorInfoViaDHCP": True,
                "iSCSIInitiatorIpAddress": "0.0.0.0",
                "iSCSIInitiatorNetmask": "0.0.0.0",
                "iSCSIIpAddressType": "IPv4",
                "iSCSINicSource": None,
                "iSCSIReverseChapSecret": None,
                "iSCSIReverseChapUsername": None,
                "iSCSITargetInfoViaDHCP": True,
                "iSCSITargetIpAddress": "0.0.0.0",
                "iSCSITargetName": None,
                "iSCSITargetTcpPort": 3260
            }
        ],
        "iSCSIInitiatorName": PROFILE2_INITIATOR_NAME,
    }
}

# Profile2: ENC2 bay5, one iSCSI boot connection to initiator IP1
ris_node_profile2_one_connection_ip1 = {
    "server": PROFILE2_SERVER,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/bios/iSCSI",
    "validate": {
        "Name": "iSCSI Software Initiator Current Settings",
        "iSCSIBootSources":
        [
            {
                "StructuredBootString": "NIC.Slot.3.1.iSCSI",
                "iSCSIAuthenticationMethod": "Chap",
                "iSCSIBootAttemptInstance": 1,
                "iSCSIBootAttemptName": PROFILE2_ISCSI_BOOT_ATTEMPT_1,
                "iSCSIBootEnable": "Enabled",
                "iSCSIBootLUN": "0",
                "iSCSIChapSecret": None,
                "iSCSIChapType": "Mutual",
                "iSCSIChapUsername": None,
                "iSCSIConnectRetry": 3,
                "iSCSIConnectTimeoutMS": 20000,
                "iSCSIInitiatorGateway": INITIATOR_GATEWAY,
                "iSCSIInitiatorInfoViaDHCP": False,
                "iSCSIInitiatorIpAddress": PROFILE2_INITIATOR_IP_1,
                "iSCSIInitiatorNetmask": INITIATOR_SUBNET_MASK,
                "iSCSIIpAddressType": "IPv4",
                "iSCSINicSource": "Slot3NicBoot1",
                "iSCSIReverseChapSecret": None,
                "iSCSIReverseChapUsername": None,
                "iSCSITargetInfoViaDHCP": False,
                "iSCSITargetIpAddress": FIRST_BOOT_TARGET_IP,
                "iSCSITargetName": PROFILE2_BOOT_TARGET_NAME,
                "iSCSITargetTcpPort": 3260
            },
            {
                "StructuredBootString": None,
                "UEFIDevicePath": None,
                "iSCSIAuthenticationMethod": "None",
                "iSCSIBootAttemptInstance": 0,
                "iSCSIBootAttemptName": "",
                "iSCSIBootEnable": "Disabled",
                "iSCSIBootLUN": "0",
                "iSCSIChapSecret": None,
                "iSCSIChapType": "OneWay",
                "iSCSIChapUsername": None,
                "iSCSIConnectRetry": 3,
                "iSCSIConnectTimeoutMS": 20000,
                "iSCSIInitiatorGateway": "0.0.0.0",
                "iSCSIInitiatorInfoViaDHCP": True,
                "iSCSIInitiatorIpAddress": "0.0.0.0",
                "iSCSIInitiatorNetmask": "0.0.0.0",
                "iSCSIIpAddressType": "IPv4",
                "iSCSINicSource": None,
                "iSCSIReverseChapSecret": None,
                "iSCSIReverseChapUsername": None,
                "iSCSITargetInfoViaDHCP": True,
                "iSCSITargetIpAddress": "0.0.0.0",
                "iSCSITargetName": None,
                "iSCSITargetTcpPort": 3260
            },
            {
                "StructuredBootString": None,
                "UEFIDevicePath": None,
                "iSCSIAuthenticationMethod": "None",
                "iSCSIBootAttemptInstance": 0,
                "iSCSIBootAttemptName": "",
                "iSCSIBootEnable": "Disabled",
                "iSCSIBootLUN": "0",
                "iSCSIChapSecret": None,
                "iSCSIChapType": "OneWay",
                "iSCSIChapUsername": None,
                "iSCSIConnectRetry": 3,
                "iSCSIConnectTimeoutMS": 20000,
                "iSCSIInitiatorGateway": "0.0.0.0",
                "iSCSIInitiatorInfoViaDHCP": True,
                "iSCSIInitiatorIpAddress": "0.0.0.0",
                "iSCSIInitiatorNetmask": "0.0.0.0",
                "iSCSIIpAddressType": "IPv4",
                "iSCSINicSource": None,
                "iSCSIReverseChapSecret": None,
                "iSCSIReverseChapUsername": None,
                "iSCSITargetInfoViaDHCP": True,
                "iSCSITargetIpAddress": "0.0.0.0",
                "iSCSITargetName": None,
                "iSCSITargetTcpPort": 3260
            },
            {
                "StructuredBootString": None,
                "UEFIDevicePath": None,
                "iSCSIAuthenticationMethod": "None",
                "iSCSIBootAttemptInstance": 0,
                "iSCSIBootAttemptName": "",
                "iSCSIBootEnable": "Disabled",
                "iSCSIBootLUN": "0",
                "iSCSIChapSecret": None,
                "iSCSIChapType": "OneWay",
                "iSCSIChapUsername": None,
                "iSCSIConnectRetry": 3,
                "iSCSIConnectTimeoutMS": 20000,
                "iSCSIInitiatorGateway": "0.0.0.0",
                "iSCSIInitiatorInfoViaDHCP": True,
                "iSCSIInitiatorIpAddress": "0.0.0.0",
                "iSCSIInitiatorNetmask": "0.0.0.0",
                "iSCSIIpAddressType": "IPv4",
                "iSCSINicSource": None,
                "iSCSIReverseChapSecret": None,
                "iSCSIReverseChapUsername": None,
                "iSCSITargetInfoViaDHCP": True,
                "iSCSITargetIpAddress": "0.0.0.0",
                "iSCSITargetName": None,
                "iSCSITargetTcpPort": 3260
            }
        ],
        "iSCSIInitiatorName": PROFILE2_INITIATOR_NAME,
    }
}

# Profile2: ENC2 bay5, one iSCSI boot connection to initiator IP2
ris_node_profile2_one_connection_ip2 = {
    "server": PROFILE2_SERVER,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/bios/iSCSI",
    "validate": {
        "Name": "iSCSI Software Initiator Current Settings",
        "iSCSIBootSources":
        [
            {
                "StructuredBootString": "NIC.Slot.3.1.iSCSI",
                "iSCSIAuthenticationMethod": "Chap",
                "iSCSIBootAttemptInstance": 1,
                "iSCSIBootAttemptName": PROFILE2_ISCSI_BOOT_ATTEMPT_1,
                "iSCSIBootEnable": "Enabled",
                "iSCSIBootLUN": "0",
                "iSCSIChapSecret": None,
                "iSCSIChapType": "Mutual",
                "iSCSIChapUsername": None,
                "iSCSIConnectRetry": 3,
                "iSCSIConnectTimeoutMS": 20000,
                "iSCSIInitiatorGateway": INITIATOR_GATEWAY,
                "iSCSIInitiatorInfoViaDHCP": False,
                "iSCSIInitiatorIpAddress": PROFILE2_INITIATOR_IP_2,
                "iSCSIInitiatorNetmask": INITIATOR_SUBNET_MASK,
                "iSCSIIpAddressType": "IPv4",
                "iSCSINicSource": "Slot3NicBoot1",
                "iSCSIReverseChapSecret": None,
                "iSCSIReverseChapUsername": None,
                "iSCSITargetInfoViaDHCP": False,
                "iSCSITargetIpAddress": FIRST_BOOT_TARGET_IP,
                "iSCSITargetName": PROFILE2_BOOT_TARGET_NAME,
                "iSCSITargetTcpPort": 3260
            },
            {
                "StructuredBootString": None,
                "UEFIDevicePath": None,
                "iSCSIAuthenticationMethod": "None",
                "iSCSIBootAttemptInstance": 0,
                "iSCSIBootAttemptName": "",
                "iSCSIBootEnable": "Disabled",
                "iSCSIBootLUN": "0",
                "iSCSIChapSecret": None,
                "iSCSIChapType": "OneWay",
                "iSCSIChapUsername": None,
                "iSCSIConnectRetry": 3,
                "iSCSIConnectTimeoutMS": 20000,
                "iSCSIInitiatorGateway": "0.0.0.0",
                "iSCSIInitiatorInfoViaDHCP": True,
                "iSCSIInitiatorIpAddress": "0.0.0.0",
                "iSCSIInitiatorNetmask": "0.0.0.0",
                "iSCSIIpAddressType": "IPv4",
                "iSCSINicSource": None,
                "iSCSIReverseChapSecret": None,
                "iSCSIReverseChapUsername": None,
                "iSCSITargetInfoViaDHCP": True,
                "iSCSITargetIpAddress": "0.0.0.0",
                "iSCSITargetName": None,
                "iSCSITargetTcpPort": 3260
            },
            {
                "StructuredBootString": None,
                "UEFIDevicePath": None,
                "iSCSIAuthenticationMethod": "None",
                "iSCSIBootAttemptInstance": 0,
                "iSCSIBootAttemptName": "",
                "iSCSIBootEnable": "Disabled",
                "iSCSIBootLUN": "0",
                "iSCSIChapSecret": None,
                "iSCSIChapType": "OneWay",
                "iSCSIChapUsername": None,
                "iSCSIConnectRetry": 3,
                "iSCSIConnectTimeoutMS": 20000,
                "iSCSIInitiatorGateway": "0.0.0.0",
                "iSCSIInitiatorInfoViaDHCP": True,
                "iSCSIInitiatorIpAddress": "0.0.0.0",
                "iSCSIInitiatorNetmask": "0.0.0.0",
                "iSCSIIpAddressType": "IPv4",
                "iSCSINicSource": None,
                "iSCSIReverseChapSecret": None,
                "iSCSIReverseChapUsername": None,
                "iSCSITargetInfoViaDHCP": True,
                "iSCSITargetIpAddress": "0.0.0.0",
                "iSCSITargetName": None,
                "iSCSITargetTcpPort": 3260
            },
            {
                "StructuredBootString": None,
                "UEFIDevicePath": None,
                "iSCSIAuthenticationMethod": "None",
                "iSCSIBootAttemptInstance": 0,
                "iSCSIBootAttemptName": "",
                "iSCSIBootEnable": "Disabled",
                "iSCSIBootLUN": "0",
                "iSCSIChapSecret": None,
                "iSCSIChapType": "OneWay",
                "iSCSIChapUsername": None,
                "iSCSIConnectRetry": 3,
                "iSCSIConnectTimeoutMS": 20000,
                "iSCSIInitiatorGateway": "0.0.0.0",
                "iSCSIInitiatorInfoViaDHCP": True,
                "iSCSIInitiatorIpAddress": "0.0.0.0",
                "iSCSIInitiatorNetmask": "0.0.0.0",
                "iSCSIIpAddressType": "IPv4",
                "iSCSINicSource": None,
                "iSCSIReverseChapSecret": None,
                "iSCSIReverseChapUsername": None,
                "iSCSITargetInfoViaDHCP": True,
                "iSCSITargetIpAddress": "0.0.0.0",
                "iSCSITargetName": None,
                "iSCSITargetTcpPort": 3260
            }
        ],
        "iSCSIInitiatorName": PROFILE2_INITIATOR_NAME,
    }
}

# Profile3: no iSCSI configured on ENC2 bay1
ris_node_profile3_no_iscsi = {
    "server": PROFILE3_SERVER,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/bios/iSCSI",
    "validate": {
        "Name": "iSCSI Software Initiator Current Settings",
        "iSCSIBootSources":
        [
            {
                "iSCSIBootEnable": "Disabled",
            },
            {
                "iSCSIBootEnable": "Disabled",
            },
            {
                "iSCSIBootEnable": "Disabled",
            },
            {
                "iSCSIBootEnable": "Disabled",
            },
        ],
    }
}

# Profile3: profile2 moved from ENC2 bay5 to ENC2 bay1, two iSCSI boot
# connections
ris_node_profile3_two_connections = {
    "server": PROFILE3_SERVER,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/bios/iSCSI",
    "validate": {
        "Name": "iSCSI Software Initiator Current Settings",
        "iSCSIBootSources":
        [
            {
                "StructuredBootString": "NIC.Slot.3.1.iSCSI",
                "iSCSIAuthenticationMethod": "None",
                "iSCSIBootAttemptInstance": 1,
                "iSCSIBootAttemptName": PROFILE3_ISCSI_BOOT_ATTEMPT_1,
                "iSCSIBootEnable": "Enabled",
                "iSCSIBootLUN": "0",
                "iSCSIChapSecret": None,
                "iSCSIChapType": "OneWay",
                "iSCSIChapUsername": None,
                "iSCSIConnectRetry": 3,
                "iSCSIConnectTimeoutMS": 20000,
                "iSCSIInitiatorGateway": INITIATOR_GATEWAY,
                "iSCSIInitiatorInfoViaDHCP": False,
                "iSCSIInitiatorIpAddress": PROFILE3_INITIATOR_IP_1,
                "iSCSIInitiatorNetmask": INITIATOR_SUBNET_MASK,
                "iSCSIIpAddressType": "IPv4",
                "iSCSINicSource": "Slot3NicBoot1",
                "iSCSIReverseChapSecret": None,
                "iSCSIReverseChapUsername": None,
                "iSCSITargetInfoViaDHCP": False,
                "iSCSITargetIpAddress": FIRST_BOOT_TARGET_IP,
                "iSCSITargetName": PROFILE3_BOOT_TARGET_NAME,
                "iSCSITargetTcpPort": 3260
            },
            {
                "StructuredBootString": "NIC.Slot.3.2.iSCSI",
                "iSCSIAuthenticationMethod": "None",
                "iSCSIBootAttemptInstance": 2,
                "iSCSIBootAttemptName": PROFILE3_ISCSI_BOOT_ATTEMPT_2,
                "iSCSIBootEnable": "Enabled",
                "iSCSIBootLUN": "0",
                "iSCSIChapSecret": None,
                "iSCSIChapType": "OneWay",
                "iSCSIChapUsername": None,
                "iSCSIConnectRetry": 3,
                "iSCSIConnectTimeoutMS": 20000,
                "iSCSIInitiatorGateway": INITIATOR_GATEWAY,
                "iSCSIInitiatorInfoViaDHCP": False,
                "iSCSIInitiatorIpAddress": PROFILE3_INITIATOR_IP_2,
                "iSCSIInitiatorNetmask": INITIATOR_SUBNET_MASK,
                "iSCSIIpAddressType": "IPv4",
                "iSCSINicSource": "Slot3NicBoot2",
                "iSCSIReverseChapSecret": None,
                "iSCSIReverseChapUsername": None,
                "iSCSITargetInfoViaDHCP": False,
                "iSCSITargetIpAddress": FIRST_BOOT_TARGET_IP,
                "iSCSITargetName": PROFILE3_BOOT_TARGET_NAME,
                "iSCSITargetTcpPort": 3260
            },
            {
                "StructuredBootString": None,
                "UEFIDevicePath": None,
                "iSCSIAuthenticationMethod": "None",
                "iSCSIBootAttemptInstance": 0,
                "iSCSIBootAttemptName": "",
                "iSCSIBootEnable": "Disabled",
                "iSCSIBootLUN": "0",
                "iSCSIChapSecret": None,
                "iSCSIChapType": "OneWay",
                "iSCSIChapUsername": None,
                "iSCSIConnectRetry": 3,
                "iSCSIConnectTimeoutMS": 20000,
                "iSCSIInitiatorGateway": "0.0.0.0",
                "iSCSIInitiatorInfoViaDHCP": True,
                "iSCSIInitiatorIpAddress": "0.0.0.0",
                "iSCSIInitiatorNetmask": "0.0.0.0",
                "iSCSIIpAddressType": "IPv4",
                "iSCSINicSource": None,
                "iSCSIReverseChapSecret": None,
                "iSCSIReverseChapUsername": None,
                "iSCSITargetInfoViaDHCP": True,
                "iSCSITargetIpAddress": "0.0.0.0",
                "iSCSITargetName": None,
                "iSCSITargetTcpPort": 3260
            },
            {
                "StructuredBootString": None,
                "UEFIDevicePath": None,
                "iSCSIAuthenticationMethod": "None",
                "iSCSIBootAttemptInstance": 0,
                "iSCSIBootAttemptName": "",
                "iSCSIBootEnable": "Disabled",
                "iSCSIBootLUN": "0",
                "iSCSIChapSecret": None,
                "iSCSIChapType": "OneWay",
                "iSCSIChapUsername": None,
                "iSCSIConnectRetry": 3,
                "iSCSIConnectTimeoutMS": 20000,
                "iSCSIInitiatorGateway": "0.0.0.0",
                "iSCSIInitiatorInfoViaDHCP": True,
                "iSCSIInitiatorIpAddress": "0.0.0.0",
                "iSCSIInitiatorNetmask": "0.0.0.0",
                "iSCSIIpAddressType": "IPv4",
                "iSCSINicSource": None,
                "iSCSIReverseChapSecret": None,
                "iSCSIReverseChapUsername": None,
                "iSCSITargetInfoViaDHCP": True,
                "iSCSITargetIpAddress": "0.0.0.0",
                "iSCSITargetName": None,
                "iSCSITargetTcpPort": 3260
            }
        ],
        "iSCSIInitiatorName": PROFILE3_INITIATOR_NAME,
    }
}

# Profile4: no iSCSI configured on ENC1 bay8
ris_node_profile4_no_iscsi = {
    "server": PROFILE4_SERVER,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/bios/iSCSI",
    "validate": {
        "Name": "iSCSI Software Initiator Current Settings",
        "iSCSISources":
        [
            {
                "iSCSIConnection": "Disabled",
            },
            {
                "iSCSIConnection": "Disabled",
            },
            {
                "iSCSIConnection": "Disabled",
            },
            {
                "iSCSIConnection": "Disabled",
            },
        ],
    }
}

# Profile4: profile1 moved to ENC1 bay8, two iSCSI boot
# connections
ris_node_profile4_two_connections = {
    "server": PROFILE4_SERVER,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/bios/iSCSI",
    "validate": {
        "Name": "iSCSI Software Initiator Current Settings",
        "iSCSISources":
        [
            {
                "StructuredBootString": "NIC.Slot.3.1.iSCSI",
                "iSCSIAuthenticationMethod": "None",
                "iSCSIAttemptInstance": 1,
                "iSCSIAttemptName": PROFILE4_ISCSI_BOOT_ATTEMPT_1,
                "iSCSILUN": "0",
                "iSCSIChapSecret": "",
                "iSCSIChapType": "OneWay",
                "iSCSIChapUsername": "",
                "iSCSIConnectRetry": 3,
                "iSCSIConnectTimeoutMS": 20000,
                "iSCSIConnection": "Enabled",
                "iSCSIInitiatorGateway": INITIATOR_GATEWAY,
                "iSCSIInitiatorInfoViaDHCP": False,
                "iSCSIInitiatorIpAddress": PROFILE4_INITIATOR_IP_1,
                "iSCSIInitiatorNetmask": INITIATOR_SUBNET_MASK,
                "iSCSIIpAddressType": "IPv4",
                "iSCSINicSource": "Slot3NicBoot1",
                "iSCSIReverseChapSecret": "",
                "iSCSIReverseChapUsername": "",
                "iSCSITargetInfoViaDHCP": False,
                "iSCSITargetIpAddress": FIRST_BOOT_TARGET_IP,
                "iSCSITargetName": PROFILE4_BOOT_TARGET_NAME,
                "iSCSITargetTcpPort": 3260
            },
            {
                "StructuredBootString": "NIC.Slot.3.2.iSCSI",
                "iSCSIAuthenticationMethod": "None",
                "iSCSIAttemptInstance": 2,
                "iSCSIAttemptName": PROFILE4_ISCSI_BOOT_ATTEMPT_2,
                "iSCSILUN": "0",
                "iSCSIChapSecret": "",
                "iSCSIChapType": "OneWay",
                "iSCSIChapUsername": "",
                "iSCSIConnectRetry": 3,
                "iSCSIConnectTimeoutMS": 20000,
                "iSCSIConnection": "Enabled",
                "iSCSIInitiatorGateway": INITIATOR_GATEWAY,
                "iSCSIInitiatorInfoViaDHCP": False,
                "iSCSIInitiatorIpAddress": PROFILE4_INITIATOR_IP_2,
                "iSCSIInitiatorNetmask": INITIATOR_SUBNET_MASK,
                "iSCSIIpAddressType": "IPv4",
                "iSCSINicSource": "Slot3NicBoot2",
                "iSCSIReverseChapSecret": "",
                "iSCSIReverseChapUsername": "",
                "iSCSITargetInfoViaDHCP": False,
                "iSCSITargetIpAddress": FIRST_BOOT_TARGET_IP,
                "iSCSITargetName": PROFILE4_BOOT_TARGET_NAME,
                "iSCSITargetTcpPort": 3260
            },
            {
                "StructuredBootString": None,
                "UEFIDevicePath": None,
                "iSCSIAuthenticationMethod": "None",
                "iSCSIAttemptInstance": 0,
                "iSCSIAttemptName": "",
                "iSCSILUN": "0",
                "iSCSIChapSecret": "",
                "iSCSIChapType": "OneWay",
                "iSCSIChapUsername": "",
                "iSCSIConnectRetry": 3,
                "iSCSIConnectTimeoutMS": 20000,
                "iSCSIConnection": "Disabled",
                "iSCSIInitiatorGateway": "0.0.0.0",
                "iSCSIInitiatorInfoViaDHCP": True,
                "iSCSIInitiatorIpAddress": "0.0.0.0",
                "iSCSIInitiatorNetmask": "0.0.0.0",
                "iSCSIIpAddressType": "IPv4",
                "iSCSINicSource": None,
                "iSCSIReverseChapSecret": "",
                "iSCSIReverseChapUsername": "",
                "iSCSITargetInfoViaDHCP": True,
                "iSCSITargetIpAddress": "0.0.0.0",
                "iSCSITargetName": "",
                "iSCSITargetTcpPort": 3260
            },
            {
                "StructuredBootString": None,
                "UEFIDevicePath": None,
                "iSCSIAuthenticationMethod": "None",
                "iSCSIAttemptInstance": 0,
                "iSCSIAttemptName": "",
                "iSCSILUN": "0",
                "iSCSIChapSecret": "",
                "iSCSIChapType": "OneWay",
                "iSCSIChapUsername": "",
                "iSCSIConnectRetry": 3,
                "iSCSIConnectTimeoutMS": 20000,
                "iSCSIConnection": "Disabled",
                "iSCSIInitiatorGateway": "0.0.0.0",
                "iSCSIInitiatorInfoViaDHCP": True,
                "iSCSIInitiatorIpAddress": "0.0.0.0",
                "iSCSIInitiatorNetmask": "0.0.0.0",
                "iSCSIIpAddressType": "IPv4",
                "iSCSINicSource": None,
                "iSCSIReverseChapSecret": "",
                "iSCSIReverseChapUsername": "",
                "iSCSITargetInfoViaDHCP": True,
                "iSCSITargetIpAddress": "0.0.0.0",
                "iSCSITargetName": "",
                "iSCSITargetTcpPort": 3260
            }
        ],
        "iSCSIInitiatorName": PROFILE4_INITIATOR_NAME,
    }
}

ts1_create_profiles = [profile1_pxe_iscsi.copy(),
                       profile2_pxe_iscsi.copy()]

ts1_edit_profiles_1 = [profile1_two_connections.copy(),
                       profile2_two_connections.copy()]

ts1_edit_profiles_2 = [profile1_pxe_iscsi.copy(),
                       profile2_pxe_iscsi.copy()]

ts1_delete_profiles = [profile1_pxe_iscsi.copy(),
                       profile2_pxe_iscsi.copy()]

ts1_all_profiles = [profile1_pxe_iscsi.copy(),
                    profile2_pxe_iscsi.copy()]

ts2_create_profiles = [profile1_one_unbootable_connection.copy(),
                       profile2_two_connections.copy()]

ts2_edit_profiles_1 = [profile1_one_connection_ip1.copy(),
                       profile2_one_connection_ip1.copy()]

ts2_edit_profiles_2 = [profile1_one_connection_ip2.copy(),
                       profile2_two_unbootable_connections.copy()]

ts2_edit_profiles_3 = [profile1_two_connections.copy(),
                       profile2_one_connection_ip2.copy()]

ts2_move_profiles = [profile3_two_connections.copy(),
                     profile4_two_connections.copy()]

ts2_delete_profiles = [profile3_two_connections.copy(),
                       profile4_two_connections.copy()]

ts2_all_profiles = [profile1_two_connections.copy(),
                    profile2_two_connections.copy(),
                    profile3_two_connections.copy(),
                    profile4_two_connections.copy()]

ts1_ris_nodes_after_create = [ris_node_profile1_one_connection_ip1.copy(),
                              ris_node_profile2_one_connection_ip1.copy(), ]

ts1_ris_nodes_after_edit_1 = [ris_node_profile1_two_connections.copy(),
                              ris_node_profile2_two_connections.copy(), ]

ts1_ris_nodes_after_edit_2 = [ris_node_profile1_one_connection_ip1.copy(),
                              ris_node_profile2_one_connection_ip1.copy(), ]

ts1_ris_nodes_after_delete = [ris_node_profile1_no_iscsi.copy(),
                              ris_node_profile2_no_iscsi.copy(), ]

ts2_ris_nodes_after_create = [ris_node_profile1_no_iscsi.copy(),
                              ris_node_profile2_two_connections.copy(), ]

ts2_ris_nodes_after_edit_1 = [ris_node_profile1_one_connection_ip1.copy(),
                              ris_node_profile2_one_connection_ip1.copy(), ]

ts2_ris_nodes_after_edit_2 = [ris_node_profile1_one_connection_ip2.copy(),
                              ris_node_profile2_no_iscsi.copy(), ]

ts2_ris_nodes_after_edit_3 = [ris_node_profile1_two_connections.copy(),
                              ris_node_profile2_one_connection_ip2.copy(), ]

ts2_ris_nodes_after_move = [ris_node_profile3_two_connections.copy(),
                            ris_node_profile4_two_connections.copy()]

ts2_ris_nodes_after_delete = [ris_node_profile1_no_iscsi.copy(),
                              ris_node_profile2_no_iscsi.copy(),
                              ris_node_profile3_no_iscsi.copy(),
                              ris_node_profile4_no_iscsi.copy()]

ris_nodes_iscsi_settings_create = [
    {"server": PROFILE1_SERVER,
     "username": ilo_credentials['username'],
     "password":ilo_credentials['password'],
     "path":"/redfish/v1/Systems/1/bios/iSCSI/settings"
     },
    {"server": PROFILE2_SERVER,
     "username": ilo_credentials['username'],
     "password":ilo_credentials['password'],
     "path":"/redfish/v1/Systems/1/bios/iSCSI/settings"
     },
]

ris_nodes_iscsi_settings_move = [
    {"server": PROFILE3_SERVER,
     "username": ilo_credentials['username'],
     "password": ilo_credentials['password'],
     "path": "/redfish/v1/Systems/1/bios/iSCSI/settings",
     },
    {"server": PROFILE4_SERVER,
     "username": ilo_credentials['username'],
     "password": ilo_credentials['password'],
     "path": "/redfish/v1/Systems/1/bios/iSCSI/settings",
     },
]

suite_setup_profiles = [
    profile1_bios.copy(),
    profile2_uefi.copy(),
    profile3_uefi.copy(),
    profile4_uefi.copy(),
]

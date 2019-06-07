# pylint: disable=E0401,E0602
from dto import *

# Credentials
admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
oa_credentials = {'username': 'Administrator', 'password': 'hpvse14'}
ilo_credentials = {'username': 'Administrator', 'password': 'hpvse1-ilo'}
cliq_credentials = {
    'mgmt_ip': '16.71.149.173',
    'username': 'admin',
    'password': 'admin',
    'port': 16022}


# Enclosures, Interconnects, Server Hardware, LIG, and EG
# Enclosures
ENC1 = 'wpst22'
ENC1_OA1 = "16.125.77.71"
ENC2 = 'wpst23'
ENC2_OA1 = "16.125.77.80"
ENC3 = 'wpst26'
ENC3_OA1 = "16.125.79.45"
# Interconnects
ENC1ICBAY1 = '%s, interconnect 1' % ENC1
ENC1ICBAY2 = '%s, interconnect 2' % ENC1
ENC1ICBAY3 = '%s, interconnect 3' % ENC1
ENC1ICBAY4 = '%s, interconnect 4' % ENC1
ENC1ICBAY5 = '%s, interconnect 5' % ENC1
ENC1ICBAY6 = '%s, interconnect 6' % ENC1
ENC2ICBAY1 = '%s, interconnect 1' % ENC2
ENC2ICBAY2 = '%s, interconnect 2' % ENC2
ENC2ICBAY3 = '%s, interconnect 3' % ENC2
ENC2ICBAY4 = '%s, interconnect 4' % ENC2
ENC2ICBAY5 = '%s, interconnect 5' % ENC2
ENC2ICBAY6 = '%s, interconnect 6' % ENC2
ENC3ICBAY1 = '%s, interconnect 1' % ENC3
ENC3ICBAY2 = '%s, interconnect 2' % ENC3
ENC3ICBAY3 = '%s, interconnect 3' % ENC3
ENC3ICBAY4 = '%s, interconnect 4' % ENC3
ENC3ICBAY5 = '%s, interconnect 5' % ENC3
ENC3ICBAY6 = '%s, interconnect 6' % ENC3
# Server Hardware
ENC1SHBAY1 = '%s, bay 1' % ENC1    # BL465c Gen8
ENC1SHBAY2 = '%s, bay 2' % ENC1    # BL465c Gen8
ENC1SHBAY3 = '%s, bay 3' % ENC1    # BL465c Gen8
ENC1SHBAY4 = '%s, bay 4' % ENC1    # BL420c Gen8
ENC1SHBAY5 = '%s, bay 5' % ENC1    # BL460c Gen9
ENC1SHBAY6 = '%s, bay 6' % ENC1    # BL460c G6
ENC1SHBAY8 = '%s, bay 7' % ENC1    # BL495c G5
ENC1SHBAY14 = '%s, bay 14' % ENC1  # BL460c Gen10
ENC1SHBAY16 = '%s, bay 16' % ENC1  # BL460c Gen10
ENC2SHBAY1 = '%s, bay 1' % ENC2    # BL465c Gen8
ENC2SHBAY2 = '%s, bay 2' % ENC2    # BL465c Gen8
ENC2SHBAY3 = '%s, bay 3' % ENC2    # BL465c Gen8
ENC2SHBAY4 = '%s, bay 4' % ENC2    # BL420c Gen8
ENC2SHBAY5 = '%s, bay 5' % ENC2    # BL460c Gen9
ENC2SHBAY6 = '%s, bay 6' % ENC2    # BL460c G6
ENC2SHBAY7 = '%s, bay 7' % ENC2    # BL2x220c G5
ENC2SHBAY10 = '%s, bay 10' % ENC2  # BL460c Gen10
ENC2SHBAY16 = '%s, bay 16' % ENC2  # BL460c Gen10
ENC3SHBAY1 = '%s, bay 1' % ENC3    # BL465c Gen8
ENC3SHBAY2 = '%s, bay 2' % ENC3    # BL465c Gen8
ENC3SHBAY3 = '%s, bay 3' % ENC3    # BL465c Gen8
ENC3SHBAY4 = '%s, bay 4' % ENC3    # BL420c Gen8
ENC3SHBAY5 = '%s, bay 5' % ENC3    # BL460c Gen9
ENC3SHBAY7 = '%s, bay 7' % ENC3    # BL660c Gen9
ENC3SHBAY8 = '%s, bay 8' % ENC3    # BL660c Gen8
ENC3SHBAY9 = '%s, bay 9' % ENC3    # BL460c G7
ENC3SHBAY10 = '%s, bay 10' % ENC3  # BL465c G7
# LIGs and EGs
LIG1_NAME = 'LIG22'
EG1_NAME = 'EG22'
LIG2_NAME = 'LIG23'
EG2_NAME = 'EG23'
LIG3_NAME = 'LIG26'
EG3_NAME = 'EG26'

enclosures_expected = [
    {"type": ENCLOSURE_TYPE, "name": "wpst22", "state": "Configured", },
    {"type": ENCLOSURE_TYPE, "name": "wpst23", "state": "Configured", },
    {"type": ENCLOSURE_TYPE, "name": "wpst23", "state": "Configured", },
]

interconnects_expected = [
    {"type": INTERCONNECT_TYPE,
     "name": ENC1ICBAY1,
     "productName": "HP VC FlexFabric 10Gb/24-Port Module",
     },
    {"type": INTERCONNECT_TYPE,
     "name": ENC1ICBAY2,
     "productName": "HP VC FlexFabric 10Gb/24-Port Module",
     },
    {"type": INTERCONNECT_TYPE,
     "name": ENC1ICBAY3,
     "productName": "HP VC FlexFabric 10Gb/24-Port Module",
     },
    {"type": INTERCONNECT_TYPE,
     "name": ENC1ICBAY4,
     "productName": "HP VC FlexFabric 10Gb/24-Port Module",
     },
    {"type": INTERCONNECT_TYPE,
     "name": ENC1ICBAY5,
     "productName": "HP VC 8Gb 20-Port FC Module",
     },
    {"type": INTERCONNECT_TYPE,
     "name": ENC1ICBAY6,
     "productName": "HP VC 8Gb 20-Port FC Module",
     },
    {"type": INTERCONNECT_TYPE,
     "name": ENC2ICBAY1,
     "productName": "HP VC FlexFabric-20/40 F8 Module",
     },
    {"type": INTERCONNECT_TYPE,
     "name": ENC2ICBAY2,
     "productName": "HP VC FlexFabric-20/40 F8 Module",
     },
    {"type": INTERCONNECT_TYPE,
     "name": ENC2ICBAY3,
     "productName": "HP VC FlexFabric 10Gb/24-Port Module",
     },
    {"type": INTERCONNECT_TYPE,
     "name": ENC2ICBAY4,
     "productName": "HP VC FlexFabric 10Gb/24-Port Module",
     },
    {"type": INTERCONNECT_TYPE,
     "name": ENC2ICBAY5,
     "productName": "HP VC 8Gb 20-Port FC Module",
     },
    {"type": INTERCONNECT_TYPE,
     "name": ENC2ICBAY6,
     "productName": "HP VC 8Gb 20-Port FC Module",
     },
    {"type": INTERCONNECT_TYPE,
     "name": ENC3ICBAY1,
     "productName": "HP VC FlexFabric 10Gb/24-Port Module",
     },
    {"type": INTERCONNECT_TYPE,
     "name": ENC3ICBAY2,
     "productName": "HP VC FlexFabric 10Gb/24-Port Module",
     },
    {"type": INTERCONNECT_TYPE,
     "name": ENC3ICBAY3,
     "productName": "HP VC FlexFabric 10Gb/24-Port Module",
     },
    {"type": INTERCONNECT_TYPE,
     "name": ENC3ICBAY4,
     "productName": "HP VC FlexFabric 10Gb/24-Port Module",
     },
    {"type": INTERCONNECT_TYPE,
     "name": ENC3ICBAY5,
     "productName": "HP VC 8Gb 24-Port FC Module",
     },
    {"type": INTERCONNECT_TYPE,
     "name": ENC3ICBAY6,
     "productName": "HP VC 8Gb 24-Port FC Module",
     },
]

# iSCSI
INITIATOR_GATEWAY = "192.168.0.1"
INITIATOR_SUBNET_MASK = "255.255.192.0"
FIRST_BOOT_TARGET_IP = "192.168.21.71"
CHAP_SECRET = "wpsthpvse123"
MCHAP_SECRET = "hpvse123wpst"

# Negative profiles
NTS0_PROFILE1_NAME = 'negative-profile1'
NTS0_PROFILE1_SERVER = ENC1SHBAY1
NTS0_PROFILE1_EG = EG1_NAME
NTS0_PROFILE2_NAME = 'negative-profile2'
NTS0_PROFILE2_SERVER = ENC1SHBAY5
NTS0_PROFILE2_EG = EG1_NAME
NTS0_PROFILE3_NAME = 'negative-profile3'
NTS0_PROFILE3_SERVER = ENC1SHBAY1
NTS0_PROFILE3_EG = EG1_NAME
NTS0_PROFILE4_NAME = 'negative-profile4'
NTS0_PROFILE4_SERVER = ENC1SHBAY5
NTS0_PROFILE4_EG = EG1_NAME
NTS0_PROFILE5_NAME = 'negative-profile5'
NTS0_PROFILE5_SERVER = ENC3SHBAY7
NTS0_PROFILE5_EG = EG3_NAME
NTS0_PROFILE6_NAME = 'negative-profile6'
NTS0_PROFILE6_SERVER = ENC3SHBAY7
NTS0_PROFILE6_EG = EG3_NAME
NTS0_PROFILE7_NAME = 'negative-profile7'
NTS0_PROFILE7_SERVER = ENC1SHBAY1
NTS0_PROFILE7_EG = EG1_NAME
NTS0_PROFILE8_NAME = 'negative-profile8'
NTS0_PROFILE8_SERVER = ENC1SHBAY5
NTS0_PROFILE8_EG = EG1_NAME
NTS0_PROFILE9_NAME = 'negative-profile9'
NTS0_PROFILE9_SERVER = ENC1SHBAY5
NTS0_PROFILE9_EG = EG1_NAME
NTS0_PROFILE10_NAME = 'negative-profile10'
NTS0_PROFILE10_SERVER = ENC3SHBAY7
NTS0_PROFILE10_EG = EG3_NAME

# PROFILE1: profile on ENC1 bay1, BL465c Gen8
PROFILE1_NAME = "wpst22-bay1-profile"
PROFILE1_BOOT_TARGET_NAME = 'iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:6927:wpst22-bay1-win2016-bootvol'
PROFILE1_INITIATOR_NAME = "iqn.2015-02.com.hpe:oneview-wpst22-bay1"
PROFILE1_INITIATOR_IP_1 = "192.168.22.140"
PROFILE1_INITIATOR_IP_2 = "192.168.22.141"
PROFILE1_CHAP_NAME = 'wpst22-bay1'
PROFILE1_MCHAP_NAME = 'wpst22-bay1'
PROFILE1_SERVER = ENC1SHBAY1
PROFILE1_EG = EG1_NAME
PROFILE1_ENC = ENC1
PROFILE1_ENC_OA = ENC1_OA1

# PROFILE2: profile on ENC1 bay5, BL460c Gen9
PROFILE2_NAME = "wpst22-bay5-profile"
PROFILE2_BOOT_TARGET_NAME = "iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:6930:wpst22-bay5-win2016-bootvol"
PROFILE2_INITIATOR_NAME = "iqn.2015-02.com.hpe:oneview-wpst22-bay5"
PROFILE2_INITIATOR_IP_1 = "192.168.22.142"
PROFILE2_INITIATOR_IP_2 = "192.168.22.143"
PROFILE2_CHAP_NAME = 'wpst22-bay5'
PROFILE2_SERVER = ENC1SHBAY5
PROFILE2_EG = EG1_NAME
PROFILE2_ENC = ENC1
PROFILE2_ENC_OA = ENC1_OA1

# PROFILE3: profile on ENC3 bay7, BL660c Gen9
PROFILE3_NAME = "wpst26-bay7-profile"
PROFILE3_BOOT_TARGET_NAME = "iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1309:wpst26-bay7-bootvol"
PROFILE3_INITIATOR_NAME = "iqn.2015-02.com.hpe:oneview-wpst26-bay7"
PROFILE3_INITIATOR_IP_1 = "192.168.22.144"
PROFILE3_INITIATOR_IP_2 = "192.168.22.145"
PROFILE3_CHAP_NAME = 'wpst26-bay7'
PROFILE3_MCHAP_NAME = 'wpst26-bay7'
PROFILE3_SERVER = ENC3SHBAY7
PROFILE3_EG = EG3_NAME
PROFILE3_ENC = ENC3
PROFILE3_ENC_OA = ENC3_OA1

# PROFILE4: profile on ENC3 bay8, BL660c Gen8
PROFILE4_NAME = "wpst26-bay8-profile"
PROFILE4_BOOT_TARGET_NAME = "iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1312:wpst26-bay8-bootvol"
PROFILE4_INITIATOR_NAME = "iqn.2015-02.com.hpe:oneview-wpst26-bay8"
PROFILE4_INITIATOR_IP_1 = "192.168.22.146"
PROFILE4_INITIATOR_IP_2 = "192.168.22.147"
PROFILE4_CHAP_NAME = 'wpst26-bay8'
PROFILE4_SERVER = ENC3SHBAY8
PROFILE4_EG = EG3_NAME
PROFILE4_ENC = ENC3
PROFILE4_ENC_OA = ENC3_OA1

# PROFILE5: profile2 moved from ENC1 bay5 to ENC2 bay1
PROFILE5_BOOT_TARGET_NAME = "iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1315:wpst23-bay1-bootvol"
PROFILE5_INITIATOR_NAME = "iqn.2015-02.com.hpe:oneview-wpst23-bay1"
PROFILE5_INITIATOR_IP_1 = "192.168.22.148"
PROFILE5_INITIATOR_IP_2 = "192.168.22.149"
PROFILE5_SERVER = ENC2SHBAY1
PROFILE5_EG = EG2_NAME
PROFILE5_ENC = ENC2
PROFILE5_ENC_OA = ENC2_OA1

# PROFILE6: profile3 moved from ENC3 bay7 to ENC3 bay3
PROFILE6_BOOT_TARGET_NAME = "iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1321:wpst26-bay3-bootvol"
PROFILE6_INITIATOR_NAME = "iqn.2015-02.com.hpe:oneview-wpst26-bay3"
PROFILE6_INITIATOR_IP_1 = "192.168.22.150"
PROFILE6_INITIATOR_IP_2 = "192.168.22.151"
PROFILE6_CHAP_NAME = 'wpst26-bay3'
PROFILE6_SERVER = ENC3SHBAY3
PROFILE6_EG = EG3_NAME
PROFILE6_ENC = ENC3
PROFILE6_ENC_OA = ENC3_OA1

# PROFILE7: profile4 moved from ENC3 bay8 to ENC2 bay5
PROFILE7_BOOT_TARGET_NAME = "iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1324:wpst23-bay5-bootvol"
PROFILE7_INITIATOR_NAME = "iqn.2015-02.com.hpe:oneview-wpst23-bay5"
PROFILE7_INITIATOR_IP_1 = "192.168.22.152"
PROFILE7_INITIATOR_IP_2 = "192.168.22.153"
PROFILE7_SERVER = ENC2SHBAY5
PROFILE7_EG = EG2_NAME
PROFILE7_ENC = ENC2
PROFILE7_ENC_OA = ENC2_OA1

# PROFILE8: profile on ENC1 bay14, BL460c Gen10
PROFILE8_NAME = "wpst22-bay14-profile"
PROFILE8_BOOT_TARGET_NAME = 'iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:6927:wpst22-bay1-win2016-bootvol'
PROFILE8_INITIATOR_NAME = "iqn.2015-02.com.hpe:oneview-wpst22-bay14"
PROFILE8_INITIATOR_IP_1 = "192.168.22.140"
PROFILE8_INITIATOR_IP_2 = "192.168.22.141"
PROFILE8_CHAP_NAME = 'wpst22-bay1'
PROFILE8_MCHAP_NAME = 'wpst22-bay1'
PROFILE8_SERVER = ENC1SHBAY14
PROFILE8_EG = EG1_NAME
PROFILE8_ENC = ENC1
PROFILE8_ENC_OA = ENC1_OA1

# PROFILE9: profile on ENC1 bay16, BL460c Gen10
PROFILE9_NAME = "wpst22-bay16-profile"
PROFILE9_BOOT_TARGET_NAME = "iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:6930:wpst22-bay5-win2016-bootvol"
PROFILE9_INITIATOR_NAME = "iqn.2015-02.com.hpe:oneview-wpst22-bay16"
PROFILE9_INITIATOR_IP_1 = "192.168.22.142"
PROFILE9_INITIATOR_IP_2 = "192.168.22.143"
PROFILE9_CHAP_NAME = 'wpst22-bay5'
PROFILE9_SERVER = ENC1SHBAY16
PROFILE9_EG = EG1_NAME
PROFILE9_ENC = ENC1
PROFILE9_ENC_OA = ENC1_OA1

# Negative Testset
# Invalid profile initiator name
negative_profile1 = {"type": SERVER_PROFILE_TYPE,
                     "serverHardwareUri": 'SH:' + NTS0_PROFILE1_SERVER,
                     "enclosureGroupUri": 'EG:' + NTS0_PROFILE1_EG,
                     "serialNumberType": "Physical",
                     "iscsiInitiatorNameType": "UserDefined",
                     "macType": "Physical",
                     "wwnType": "Physical",
                     "name": NTS0_PROFILE1_NAME,
                     "description": "",
                     "affinity": "Bay",
                     "connectionSettings": {"connections": [
                         {"id": 1,
                          "name": "",
                          "functionType": "iSCSI",
                          "portId": "Flb 1:2-b",
                          "requestedMbps": "2500",
                          "networkUri": 'ETH:network-untagged',
                          "boot": {"priority": "NotBootable"}, }]},
                     "boot": {"manageBoot": True,
                              "order": ["HardDisk", "CD", "Floppy", "USB", "PXE"]},
                     "bootMode": None,
                     "firmware": {"manageFirmware": False},
                     "bios": {"manageBios": False, "overriddenSettings": []},
                     "hideUnusedFlexNics": True,
                     "iscsiInitiatorName": 'NAME',
                     "localStorage": {"sasLogicalJBODs": [],
                                      "controllers": []},
                     "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                     }

# Invalid boot initiator name
negative_profile2 = {"type": SERVER_PROFILE_TYPE,
                     "serverHardwareUri": 'SH:' + NTS0_PROFILE2_SERVER,
                     "enclosureGroupUri": 'EG:' + NTS0_PROFILE2_EG,
                     "serialNumberType": "Physical",
                     "iscsiInitiatorNameType": "UserDefined",
                     "macType": "Physical",
                     "wwnType": "Physical",
                     "name": NTS0_PROFILE2_NAME,
                     "description": "",
                     "affinity": "Bay",
                     "connectionSettings": {"connections": [
                         {"id": 1,
                          "name": "iSCSI-boot-primary",
                          "functionType": "iSCSI",
                          "portId": "Mezz 1:2-b",
                          "requestedMbps": "2500",
                          "networkUri": 'ETH:network-untagged',
                          "ipv4": {"ipAddressSource": "UserDefined",
                                   "subnetMask": INITIATOR_SUBNET_MASK,
                                   "gateway": INITIATOR_GATEWAY,
                                   "ipAddress": PROFILE2_INITIATOR_IP_1
                                   },
                          "boot": {"priority": "Primary",
                                   "bootVlanId": "",
                                   "bootVolumeSource": "UserDefined",
                                   "iscsi": {
                                       "initiatorNameSource": "UserDefined",
                                       "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                                       "firstBootTargetPort": "3260",
                                       "secondBootTargetIp": "",
                                       "secondBootTargetPort": "",
                                       "chapLevel": "None",
                                       "initiatorName": 'NAME',
                                       "bootTargetName": PROFILE2_BOOT_TARGET_NAME,
                                       "bootTargetLun": "0",
                                       "chapName": "",
                                       "chapSecret": None,
                                       "mutualChapSecret": None},
                                   },
                          },
                     ]},
                     "boot": {"manageBoot": True,
                              "order": ["HardDisk",
                                        "CD",
                                        "USB",
                                        "PXE"]},
                     "bootMode": {"manageMode": True,
                                  "mode": "BIOS"},
                     "firmware": {"manageFirmware": False},
                     "bios": {"manageBios": False,
                              "overriddenSettings": []},
                     "hideUnusedFlexNics": True,
                     "iscsiInitiatorName": PROFILE2_INITIATOR_NAME,
                     "localStorage": {"sasLogicalJBODs": [],
                                      "controllers": []},
                     "sanStorage": {'manageSanStorage': False,
                                    'volumeAttachments': []}}

# Invalid virtual function
negative_profile3 = {"type": SERVER_PROFILE_TYPE,
                     "serverHardwareUri": 'SH:' + NTS0_PROFILE3_SERVER,
                     "enclosureGroupUri": 'EG:' + NTS0_PROFILE3_EG,
                     "serialNumberType": "Physical",
                     "iscsiInitiatorNameType": "UserDefined",
                     "macType": "Physical",
                     "wwnType": "Physical",
                     "name": NTS0_PROFILE3_NAME,
                     "description": "",
                     "affinity": "Bay",
                     "connectionSettings": {"connections": [
                         {"id": 1,
                          "name": "",
                          "functionType": "iSCSI",
                          "portId": "Flb 1:2-a",
                          "requestedMbps": "2500",
                          "networkUri": 'ETH:network-untagged',
                          "boot": {"priority": "NotBootable"},
                          }
                     ]},
                     "boot": {"manageBoot": True,
                              "order": ["HardDisk",
                                        "CD",
                                        "Floppy",
                                        "USB",
                                        "PXE"]},
                     "bootMode": None,
                     "firmware": {"manageFirmware": False},
                     "bios": {"manageBios": False,
                              "overriddenSettings": []},
                     "hideUnusedFlexNics": True,
                     "iscsiInitiatorName": PROFILE1_INITIATOR_NAME,
                     "localStorage": {"sasLogicalJBODs": [],
                                      "controllers": []},
                     "sanStorage": {'manageSanStorage': False,
                                    'volumeAttachments': []}}

# Define secondary boot without primary boot
negative_profile4 = {"type": SERVER_PROFILE_TYPE,
                     "serverHardwareUri": 'SH:' + NTS0_PROFILE4_SERVER,
                     "enclosureGroupUri": 'EG:' + NTS0_PROFILE4_EG,
                     "serialNumberType": "Physical",
                     "iscsiInitiatorNameType": "UserDefined",
                     "macType": "Physical",
                     "wwnType": "Physical",
                     "name": NTS0_PROFILE4_NAME,
                     "description": "",
                     "affinity": "Bay",
                     "connectionSettings": {"connections": [
                         {"id": 1,
                          "name": "iSCSI-boot-primary",
                          "functionType": "iSCSI",
                          "portId": "Mezz 1:2-b",
                          "requestedMbps": "2500",
                          "networkUri": 'ETH:network-untagged',
                          "ipv4": {"ipAddressSource": "UserDefined",
                                   "subnetMask": INITIATOR_SUBNET_MASK,
                                   "gateway": INITIATOR_GATEWAY,
                                   "ipAddress": PROFILE2_INITIATOR_IP_1
                                   },
                          "boot": {"priority": "Secondary",
                                   "bootVlanId": "",
                                   "bootVolumeSource": "UserDefined",
                                   "iscsi": {
                                       "initiatorNameSource": "UserDefined",
                                       "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                                       "firstBootTargetPort": "3260",
                                       "secondBootTargetIp": "",
                                       "secondBootTargetPort": "",
                                       "chapLevel": "None",
                                       "initiatorName": PROFILE2_INITIATOR_NAME,
                                       "bootTargetName": PROFILE2_BOOT_TARGET_NAME,
                                       "bootTargetLun": "0",
                                       "chapName": "",
                                       "chapSecret": None,
                                       "mutualChapName": "",
                                       "mutualChapSecret": None},
                                   },
                          },
                     ]},
                     "boot": {"manageBoot": True,
                              "order": ["HardDisk", "CD", "USB", "PXE"]},
                     "bootMode": {"manageMode": True, "mode": "BIOS"},
                     "firmware": {"manageFirmware": False},
                     "bios": {"manageBios": False,
                              "overriddenSettings": []},
                     "hideUnusedFlexNics": True,
                     "iscsiInitiatorName": PROFILE2_INITIATOR_NAME,
                     "localStorage": {"sasLogicalJBODs": [],
                                      "controllers": []},
                     "sanStorage": {'manageSanStorage': False,
                                    'volumeAttachments': []}
                     }

# Multiple Primary boot connections
negative_profile5 = {"type": SERVER_PROFILE_TYPE,
                     "serverHardwareUri": 'SH:' + NTS0_PROFILE5_SERVER,
                     "enclosureGroupUri": 'EG:' + NTS0_PROFILE5_EG,
                     "serialNumberType": "Physical",
                     "iscsiInitiatorNameType": "UserDefined",
                     "macType": "Physical",
                     "wwnType": "Physical",
                     "name": NTS0_PROFILE5_NAME,
                     "description": "",
                     "affinity": "Bay",
                     "connectionSettings": {"connections": [
                         {"id": 1,
                          "name": "iSCSI-boot-primary",
                          "functionType": "iSCSI",
                          "portId": "Flb 2:2-b",
                          "requestedMbps": "2500",
                          "networkUri": 'ETH:network-untagged',
                          "ipv4": {"ipAddressSource": "UserDefined",
                                   "subnetMask": INITIATOR_SUBNET_MASK,
                                   "gateway": INITIATOR_GATEWAY,
                                   "ipAddress": PROFILE3_INITIATOR_IP_1
                                   },
                          "boot": {"priority": "Primary",
                                   "bootVlanId": "",
                                   "bootVolumeSource": "UserDefined",
                                   "iscsi": {
                                       "initiatorNameSource": "ProfileInitiatorName",
                                       "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                                       "firstBootTargetPort": "3260",
                                       "secondBootTargetIp": "",
                                       "secondBootTargetPort": "",
                                       "chapLevel": "None",
                                       "bootTargetName": PROFILE3_BOOT_TARGET_NAME,
                                       "bootTargetLun": "0",
                                       "chapName": "",
                                       "chapSecret": None,
                                       "mutualChapName": "",
                                       "mutualChapSecret": None},
                                   },
                          },
                         {"id": 2,
                          "name": "iSCSI-boot-secondary",
                          "functionType": "iSCSI",
                          "portId": "Flb 2:1-b",
                          "requestedMbps": "2500",
                          "networkUri": 'ETH:network-untagged',
                          "ipv4": {"ipAddressSource": "UserDefined",
                                   "subnetMask": INITIATOR_SUBNET_MASK,
                                   "gateway": INITIATOR_GATEWAY,
                                   "ipAddress": PROFILE3_INITIATOR_IP_2
                                   },
                          "boot": {"priority": "Primary",
                                   "bootVlanId": "",
                                   "bootVolumeSource": "UserDefined",
                                   "iscsi": {
                                       "initiatorNameSource": "ProfileInitiatorName",
                                       "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                                       "firstBootTargetPort": "3260",
                                       "secondBootTargetIp": "",
                                       "secondBootTargetPort": "",
                                       "chapLevel": "None",
                                       "bootTargetName": PROFILE3_BOOT_TARGET_NAME,
                                       "bootTargetLun": "0",
                                       "chapName": "",
                                       "chapSecret": None,
                                       "mutualChapName": "",
                                       "mutualChapSecret": None},
                                   },
                          },
                     ]},
                     "boot": {"manageBoot": True, "order": ["HardDisk"]},
                     "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                     "firmware": {"manageFirmware": False},
                     "bios": {"manageBios": False, "overriddenSettings": []},
                     "hideUnusedFlexNics": True,
                     "iscsiInitiatorName": PROFILE3_INITIATOR_NAME,
                     "localStorage": {"sasLogicalJBODs": [], "controllers": []},
                     "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                     }

# Multiple Secondary boot connections
negative_profile6 = {"type": SERVER_PROFILE_TYPE,
                     "serverHardwareUri": 'SH:' + NTS0_PROFILE6_SERVER,
                     "enclosureGroupUri": 'EG:' + NTS0_PROFILE6_EG,
                     "serialNumberType": "Physical",
                     "iscsiInitiatorNameType": "UserDefined",
                     "macType": "Physical", "wwnType": "Physical",
                     "name": NTS0_PROFILE6_NAME,
                     "description": "",
                     "affinity": "Bay",
                     "connectionSettings": {"connections": [
                         {"id": 1,
                          "name": "iSCSI-boot-primary",
                          "functionType": "iSCSI",
                          "portId": "Flb 2:2-b",
                          "requestedMbps": "2500",
                          "networkUri": 'ETH:network-untagged',
                          "ipv4": {"ipAddressSource": "UserDefined",
                                   "subnetMask": INITIATOR_SUBNET_MASK,
                                   "gateway": INITIATOR_GATEWAY,
                                   "ipAddress": PROFILE3_INITIATOR_IP_1
                                   },
                          "boot": {"priority": "Secondary",
                                   "bootVlanId": "",
                                   "bootVolumeSource": "UserDefined",
                                   "iscsi": {
                                       "initiatorNameSource": "ProfileInitiatorName",
                                       "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                                       "firstBootTargetPort": "3260",
                                       "secondBootTargetIp": "",
                                       "secondBootTargetPort": "",
                                       "chapLevel": "None",
                                       "bootTargetName": PROFILE3_BOOT_TARGET_NAME,
                                       "bootTargetLun": "0",
                                       "chapName": "",
                                       "chapSecret": None,
                                       "mutualChapName": "",
                                       "mutualChapSecret": None}, },
                          },
                         {"id": 2,
                          "name": "iSCSI-boot-secondary",
                          "functionType": "iSCSI",
                          "portId": "Flb 2:1-b",
                          "requestedMbps": "2500",
                          "networkUri": 'ETH:network-untagged',
                          "ipv4": {"ipAddressSource": "UserDefined",
                                   "subnetMask": INITIATOR_SUBNET_MASK,
                                   "gateway": INITIATOR_GATEWAY,
                                   "ipAddress": PROFILE3_INITIATOR_IP_2
                                   },
                          "boot": {"priority": "Secondary",
                                   "bootVlanId": "",
                                   "bootVolumeSource": "UserDefined",
                                   "iscsi": {
                                       "initiatorNameSource": "ProfileInitiatorName",
                                       "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                                       "firstBootTargetPort": "3260",
                                       "secondBootTargetIp": "",
                                       "secondBootTargetPort": "",
                                       "chapLevel": "None",
                                       "bootTargetName": PROFILE3_BOOT_TARGET_NAME,
                                       "bootTargetLun": "0",
                                       "chapName": "",
                                       "chapSecret": None,
                                       "mutualChapName": "",
                                       "mutualChapSecret": None}, },
                          },
                     ]},
                     "boot": {"manageBoot": True, "order": ["HardDisk"]},
                     "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                     "firmware": {"manageFirmware": False},
                     "bios": {"manageBios": False, "overriddenSettings": []},
                     "hideUnusedFlexNics": True,
                     "iscsiInitiatorName": PROFILE3_INITIATOR_NAME,
                     "localStorage": {"sasLogicalJBODs": [], "controllers": []},
                     "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                     }

# Network set in iSCSI boot connection
negative_profile7 = {"type": SERVER_PROFILE_TYPE,
                     "serverHardwareUri": 'SH:' + NTS0_PROFILE7_SERVER,
                     "enclosureGroupUri": 'EG:' + NTS0_PROFILE7_EG,
                     "serialNumberType": "Physical",
                     "iscsiInitiatorNameType": "UserDefined",
                     "macType": "Physical",
                     "wwnType": "Physical",
                     "name": NTS0_PROFILE7_NAME,
                     "description": "",
                     "affinity": "Bay",
                     "connectionSettings": {"connections": [
                         {"id": 1,
                          "name": "",
                          "functionType": "iSCSI",
                          "portId": "Flb 1:2-b",
                          "requestedMbps": "2500",
                          "networkUri": 'NS:NS1',
                          "boot": {"priority": "NotBootable"}, }]},
                     "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "Floppy", "USB", "PXE"]},
                     "bootMode": None,
                     "firmware": {"manageFirmware": False},
                     "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                     "iscsiInitiatorName": PROFILE1_INITIATOR_NAME,
                     "localStorage": {"sasLogicalJBODs": [], "controllers": []},
                     "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}}

# Invalid initiatorVlanIdinitiatorVlanIdinitiatorVlanId for untagged network
negative_profile8 = {"type": SERVER_PROFILE_TYPE,
                     "serverHardwareUri": 'SH:' + NTS0_PROFILE8_SERVER,
                     "enclosureGroupUri": 'EG:' + NTS0_PROFILE8_EG,
                     "serialNumberType": "Physical",
                     "iscsiInitiatorNameType": "UserDefined",
                     "macType": "Physical",
                     "wwnType": "Physical",
                     "name": NTS0_PROFILE8_NAME,
                     "description": "",
                     "affinity": "Bay",
                     "connectionSettings": {"connections": [
                         {"id": 1,
                          "name": "iSCSI-boot-primary",
                          "functionType": "iSCSI",
                          "portId": "Mezz 1:2-b",
                          "requestedMbps": "2500",
                          "networkUri": 'ETH:network-untagged',
                          "ipv4": {"ipAddressSource": "UserDefined",
                                   "subnetMask": INITIATOR_SUBNET_MASK,
                                   "gateway": INITIATOR_GATEWAY,
                                   "ipAddress": PROFILE2_INITIATOR_IP_1
                                   },
                          "boot": {"priority": "Primary",
                                   "bootVlanId": "1",
                                   "bootVolumeSource": "UserDefined",
                                   "iscsi": {
                                       "initiatorNameSource": "UserDefined",
                                       "initiatorName": PROFILE2_INITIATOR_NAME,
                                       "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                                       "firstBootTargetPort": "3260",
                                       "secondBootTargetIp": "",
                                       "secondBootTargetPort": "",
                                       "bootTargetName": PROFILE2_BOOT_TARGET_NAME,
                                       "bootTargetLun": "0",
                                       "chapLevel": "Chap",
                                       "chapName": PROFILE2_CHAP_NAME,
                                       "chapSecret": CHAP_SECRET,
                                       "mutualChapName": "",
                                       "mutualChapSecret": None},
                                   }
                          },
                     ]},
                     "boot": {"manageBoot": True,
                              "order": ["HardDisk", "CD", "USB", "PXE"]},
                     "bootMode": {"manageMode": True, "mode": "BIOS"},
                     "firmware": {"manageFirmware": False},
                     "bios": {"manageBios": False, "overriddenSettings": []},
                     "hideUnusedFlexNics": True,
                     "iscsiInitiatorName": PROFILE2_INITIATOR_NAME,
                     "localStorage": {"sasLogicalJBODs": [], "controllers": []},
                     "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                     }

# Invalid initiatorVlanId for tunnel network
negative_profile9 = {"type": SERVER_PROFILE_TYPE,
                     "serverHardwareUri": 'SH:' + NTS0_PROFILE9_SERVER,
                     "enclosureGroupUri": 'EG:' + NTS0_PROFILE9_EG,
                     "serialNumberType": "Physical",
                     "iscsiInitiatorNameType": "UserDefined",
                     "macType": "Physical",
                     "wwnType": "Physical",
                     "name": NTS0_PROFILE9_NAME,
                     "description": "",
                     "affinity": "Bay",
                     "connectionSettings": {"connections": [
                         {"id": 1,
                          "name": "iSCSI-boot-primary",
                          "functionType": "iSCSI",
                          "portId": "Mezz 1:2-b",
                          "requestedMbps": "2500",
                          "networkUri": 'ETH:network-tunnel',
                          "ipv4": {"ipAddressSource": "UserDefined",
                                   "subnetMask": INITIATOR_SUBNET_MASK,
                                   "gateway": INITIATOR_GATEWAY,
                                   "ipAddress": PROFILE2_INITIATOR_IP_1
                                   },
                          "boot": {"priority": "Primary",
                                   "bootVlanId": "8000",
                                   "bootVolumeSource": "UserDefined",
                                   "iscsi": {
                                       "initiatorNameSource": "UserDefined",
                                       "initiatorName": PROFILE2_INITIATOR_NAME,
                                       "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                                       "firstBootTargetPort": "3260",
                                       "secondBootTargetIp": "",
                                       "secondBootTargetPort": "",
                                       "bootTargetName": PROFILE2_BOOT_TARGET_NAME,
                                       "bootTargetLun": "0",
                                       "chapLevel": "Chap",
                                       "chapName": PROFILE2_CHAP_NAME,
                                       "chapSecret": CHAP_SECRET,
                                       "mutualChapName": "",
                                       "mutualChapSecret": None},
                                   }
                          },
                     ]},
                     "boot": {"manageBoot": True,
                              "order": ["HardDisk", "CD", "USB", "PXE"]},
                     "bootMode": {"manageMode": True, "mode": "BIOS"},
                     "firmware": {"manageFirmware": False},
                     "bios": {"manageBios": False, "overriddenSettings": []},
                     "hideUnusedFlexNics": True,
                     "iscsiInitiatorName": PROFILE2_INITIATOR_NAME,
                     "localStorage": {"sasLogicalJBODs": [], "controllers": []},
                     "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}}

# initiator IP not unique
negative_profile10 = {"type": SERVER_PROFILE_TYPE,
                      "serverHardwareUri": 'SH:' + NTS0_PROFILE10_SERVER,
                      "enclosureGroupUri": 'EG:' + NTS0_PROFILE10_EG,
                      "serialNumberType": "Physical",
                      "iscsiInitiatorNameType": "UserDefined",
                      "macType": "Physical", "wwnType": "Physical",
                      "name": NTS0_PROFILE10_NAME,
                      "description": "",
                      "affinity": "Bay",
                      "connectionSettings": {"connections": [
                          {"id": 1,
                           "name": "iSCSI-boot-primary",
                           "functionType": "iSCSI",
                           "portId": "Flb 2:2-b",
                           "requestedMbps": "2500",
                           "networkUri": 'ETH:network-untagged',
                           "ipv4": {"ipAddressSource": "UserDefined",
                                    "subnetMask": INITIATOR_SUBNET_MASK,
                                    "gateway": INITIATOR_GATEWAY,
                                    "ipAddress": PROFILE3_INITIATOR_IP_1
                                    },
                           "boot": {"priority": "Primary",
                                    "bootVlanId": "",
                                    "bootVolumeSource": "UserDefined",
                                    "iscsi": {
                                        "initiatorNameSource": "ProfileInitiatorName",
                                        "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                                        "firstBootTargetPort": "3260",
                                        "secondBootTargetIp": "",
                                        "secondBootTargetPort": "",
                                        "chapLevel": "None",
                                        "bootTargetName": PROFILE3_BOOT_TARGET_NAME,
                                        "bootTargetLun": "0",
                                        "chapName": "",
                                        "chapSecret": None,
                                        "mutualChapName": "",
                                        "mutualChapSecret": None},
                                    }
                           },
                          {"id": 2,
                           "name": "iSCSI-boot-secondary",
                           "functionType": "iSCSI",
                           "portId": "Flb 2:1-b",
                           "requestedMbps": "2500",
                           "networkUri": 'ETH:network-untagged',
                           "ipv4": {"ipAddressSource": "UserDefined",
                                     "subnetMask": INITIATOR_SUBNET_MASK,
                                     "gateway": INITIATOR_GATEWAY,
                                     "ipAddress": PROFILE3_INITIATOR_IP_1
                                    },
                           "boot": {"priority": "Secondary",
                                    "bootVlanId": "",
                                    "bootVolumeSource": "UserDefined",
                                    "iscsi": {
                                        "initiatorNameSource": "ProfileInitiatorName",
                                        "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                                        "firstBootTargetPort": "3260",
                                        "secondBootTargetIp": "",
                                        "secondBootTargetPort": "",
                                        "chapLevel": "None",
                                        "bootTargetName": PROFILE3_BOOT_TARGET_NAME,
                                        "bootTargetLun": "0",
                                        "chapName": "",
                                        "chapSecret": None,
                                        "mutualChapName": "",
                                        "mutualChapSecret": None},
                                    }
                           },
                      ]},
                      "boot": {"manageBoot": True, "order": ["HardDisk"]},
                      "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                      "firmware": {"manageFirmware": False},
                      "bios": {"manageBios": False, "overriddenSettings": []},
                      "hideUnusedFlexNics": True,
                      "iscsiInitiatorName": PROFILE3_INITIATOR_NAME,
                      "localStorage": {"sasLogicalJBODs": [], "controllers": []},
                      "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}}

negative_profile_tasks = [
    {
        'keyword': 'Add Server Profile',
        'argument': negative_profile1.copy(),
        'taskState': 'Error',
        'errorMessage': 'Invalid_profile_initiator_name'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_profile2.copy(),
        'taskState': 'Error',
        'errorMessage': 'Invalid_boot_initiator_name'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_profile3.copy(),
        'taskState': 'Error',
        'errorMessage': 'Invalid_flexNIC_for_iSCSI_function'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_profile4.copy(),
        'taskState': 'Error',
        'errorMessage': 'Invalid_secondary_boot_connection'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_profile5.copy(),
        'taskState': 'Error',
        'errorMessage': 'Multiple_primary_boot'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_profile6.copy(),
        'taskState': 'Error',
        'errorMessage': 'Multiple_secondary_boot'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_profile7.copy(),
        'taskState': 'Error',
        'errorMessage': 'Profile_network_set_iSCSI'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_profile8.copy(),
        'taskState': 'Error',
        'errorMessage': 'Invaid_initiator_vlan_id_for_tagged_untagged_network'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_profile9.copy(),
        'taskState': 'Error',
        'errorMessage': 'Hardware_iSCSI_Invaid_initiator_vlan_id_for_tunnel_network'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_profile10.copy(),
        'taskState': 'Error',
        'errorMessage': 'IscsiDuplicateInitiatorIpAddress'},

]

# Positive tesNTS

# Profile1: ENC1 bay 1, BL465c Gen8
# Profile initiator name is user defined
# Primary connection on LOM1:2b, unbootable
profile1_one_unbootable_connection = {"type": SERVER_PROFILE_TYPE,
                                      "serverHardwareUri": 'SH:' + PROFILE1_SERVER,
                                      "enclosureGroupUri": 'EG:' + PROFILE1_EG,
                                      "serialNumberType": "Physical",
                                      "iscsiInitiatorNameType": "UserDefined",
                                      "macType": "Physical",
                                      "wwnType": "Physical",
                                      "name": PROFILE1_NAME,
                                      "description": "",
                                      "affinity": "Bay",
                                      "connectionSettings": {"connections": [
                                          {"id": 1,
                                           "name": "",
                                           "functionType": "iSCSI",
                                           "portId": "Flb 1:2-b",
                                           "requestedMbps": "2500",
                                           "networkUri": 'ETH:network-tunnel',
                                           "boot": {"priority": "NotBootable"}, }]},
                                      "boot": {"manageBoot": True,
                                               "order": ["HardDisk", "CD", "Floppy", "USB", "PXE"]},
                                      "bootMode": None,
                                      "firmware": {"manageFirmware": False},
                                      "bios": {"manageBios": False,
                                               "overriddenSettings": []},
                                      "hideUnusedFlexNics": True,
                                      "iscsiInitiatorName": PROFILE1_INITIATOR_NAME,
                                      "localStorage": {"sasLogicalJBODs": [], "controllers": []},
                                      "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}}

# Profile1: ENC1 bay 1, BL465c Gen8
# Connection initiator name is user defined
# Profile initiator name is user-defined
# primary on LOM1:2b
# MCHAP, tunnel network
profile1_one_bootable_connection = {"type": SERVER_PROFILE_TYPE,
                                    "serverHardwareUri": 'SH:' + PROFILE1_SERVER,
                                    "enclosureGroupUri": 'EG:' + PROFILE1_EG,
                                    "serialNumberType": "Physical",
                                    "iscsiInitiatorNameType": "UserDefined",
                                    "macType": "Physical",
                                    "wwnType": "Physical",
                                    "name": PROFILE1_NAME,
                                    "description": "",
                                    "affinity": "Bay",
                                    "connectionSettings": {"connections": [
                                        {"id": 1,
                                         "name": "iSCSI-boot-primary",
                                         "functionType": "iSCSI",
                                         "portId": "Flb 1:2-b",
                                         "requestedMbps": "2500",
                                         "networkUri": 'ETH:network-tunnel',
                                         "ipv4": {
                                             "ipAddressSource": "UserDefined",
                                             "subnetMask": INITIATOR_SUBNET_MASK,
                                             "gateway": INITIATOR_GATEWAY,
                                             "ipAddress": PROFILE1_INITIATOR_IP_1
                                         },
                                         "boot": {
                                             "priority": "Primary",
                                             "bootVlanId": "",
                                             "bootVolumeSource": "UserDefined",
                                             "iscsi": {
                                                 "initiatorNameSource": "UserDefined",
                                                 "initiatorName": PROFILE1_INITIATOR_NAME,
                                                 "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                                                 "firstBootTargetPort": "3260",
                                                 "secondBootTargetIp": "",
                                                 "secondBootTargetPort": "",
                                                 "bootTargetName": PROFILE1_BOOT_TARGET_NAME,
                                                 "bootTargetLun": "0",
                                                 "chapLevel": "MutualChap",
                                                 "chapName": PROFILE1_CHAP_NAME,
                                                 "chapSecret": CHAP_SECRET,
                                                 "mutualChapName": PROFILE1_MCHAP_NAME,
                                                 "mutualChapSecret": MCHAP_SECRET},
                                         }
                                         },
                                    ]},
                                    "boot": {"manageBoot": True,
                                             "order": ["HardDisk", "CD", "Floppy", "USB", "PXE"]},
                                    "bootMode": None,
                                    "firmware": {"manageFirmware": False},
                                    "bios": {"manageBios": False, "overriddenSettings": []},
                                    "hideUnusedFlexNics": True,
                                    "iscsiInitiatorName": PROFILE1_INITIATOR_NAME,
                                    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
                                    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                    }


# Profile2: ENC1 bay5, BL460c Gen9, Legacy BIOS boot mode
# Connection initiator name is user defined
# Profile initiator name is user-defined
# primary on FLB1:1b
# CHAP, tunnel network
profile2_one_bootable_connection = {"type": SERVER_PROFILE_TYPE,
                                    "serverHardwareUri": 'SH:' + PROFILE2_SERVER,
                                    "enclosureGroupUri": 'EG:' + PROFILE2_EG,
                                    "serialNumberType": "Physical",
                                    "iscsiInitiatorNameType": "UserDefined",
                                    "macType": "Physical",
                                    "wwnType": "Physical",
                                    "name": PROFILE2_NAME,
                                    "description": "",
                                    "affinity": "Bay",
                                    "connectionSettings": {"connections": [
                                        {"id": 1,
                                         "name": "iSCSI-boot-primary",
                                         "functionType": "iSCSI",
                                         "portId": "Flb 1:1-b",
                                         "requestedMbps": "2500",
                                         "networkUri": 'ETH:network-tunnel',
                                         "ipv4": {
                                             "ipAddressSource": "UserDefined",
                                             "subnetMask": INITIATOR_SUBNET_MASK,
                                             "gateway": INITIATOR_GATEWAY,
                                             "ipAddress": PROFILE2_INITIATOR_IP_1
                                         },
                                         "boot": {
                                             "priority": "Primary",
                                             "bootVlanId": "",
                                             "bootVolumeSource": "UserDefined",
                                             "iscsi": {
                                                 "initiatorNameSource": "UserDefined",
                                                 "initiatorName": PROFILE2_INITIATOR_NAME,
                                                 "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                                                 "firstBootTargetPort": "3260",
                                                 "secondBootTargetIp": "",
                                                 "secondBootTargetPort": "",
                                                 "bootTargetName": PROFILE2_BOOT_TARGET_NAME,
                                                 "bootTargetLun": "0", "chapLevel": "Chap",
                                                 "chapName": PROFILE2_CHAP_NAME,
                                                 "chapSecret": CHAP_SECRET,
                                                 "mutualChapName": "",
                                                 "mutualChapSecret": None},
                                         }
                                         },
                                    ]},
                                    "boot": {"manageBoot": True,
                                             "order": ["HardDisk", "CD", "USB", "PXE"]},
                                    "bootMode": {"manageMode": True, "mode": "BIOS"},
                                    "firmware": {"manageFirmware": False},
                                    "bios": {"manageBios": False, "overriddenSettings": []},
                                    "hideUnusedFlexNics": True,
                                    "iscsiInitiatorName": PROFILE2_INITIATOR_NAME,
                                    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
                                    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                    }

# Profile2: ENC1 bay5, BL460c Gen9, Legacy BIOS boot mode
# Connection initiator name is user defined
# Profile initiator name is user-defined
# primary onFLB1:1b, secondary on FLB1:2b
# CHAP, tunnel network
profile2_two_bootable_connections = {"type": SERVER_PROFILE_TYPE,
                                     "serverHardwareUri": 'SH:' + PROFILE2_SERVER,
                                     "enclosureGroupUri": 'EG:' + PROFILE2_EG,
                                     "serialNumberType": "Physical",
                                     "iscsiInitiatorNameType": "UserDefined",
                                     "macType": "Physical",
                                     "wwnType": "Physical",
                                     "name": PROFILE2_NAME,
                                     "description": "",
                                     "affinity": "Bay",
                                     "connectionSettings": {"connections": [
                                         {"id": 1,
                                          "name": "iSCSI-boot-primary",
                                          "functionType": "iSCSI",
                                          "portId": "Flb 1:1-b",
                                          "requestedMbps": "2500",
                                          "networkUri": 'ETH:network-tunnel',
                                          "ipv4": {
                                              "ipAddressSource": "UserDefined",
                                              "subnetMask": INITIATOR_SUBNET_MASK,
                                              "gateway": INITIATOR_GATEWAY,
                                              "ipAddress": PROFILE2_INITIATOR_IP_1
                                          },
                                          "boot": {
                                              "priority": "Primary",
                                              "bootVlanId": "",
                                              "bootVolumeSource": "UserDefined",
                                              "iscsi": {
                                                  "initiatorNameSource": "UserDefined",
                                                  "initiatorName": PROFILE2_INITIATOR_NAME,
                                                  "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                                                  "firstBootTargetPort": "3260",
                                                  "secondBootTargetIp": "",
                                                  "secondBootTargetPort": "",
                                                  "bootTargetName": PROFILE2_BOOT_TARGET_NAME,
                                                  "bootTargetLun": "0",
                                                  "chapLevel": "Chap",
                                                  "chapName": PROFILE2_CHAP_NAME,
                                                  "chapSecret": CHAP_SECRET,
                                                  "mutualChapName": "",
                                                  "mutualChapSecret": None},
                                          }
                                          },
                                         {"id": 2,
                                          "name": "iSCSI-boot-secondary",
                                          "functionType": "iSCSI",
                                          "portId": "Flb 1:2-b",
                                          "requestedMbps": "2500",
                                          "networkUri": 'ETH:network-tunnel',
                                          "ipv4": {
                                              "ipAddressSource": "UserDefined",
                                              "subnetMask": INITIATOR_SUBNET_MASK,
                                              "gateway": INITIATOR_GATEWAY,
                                              "ipAddress": PROFILE2_INITIATOR_IP_2
                                          },
                                          "boot": {
                                              "priority": "Secondary",
                                              "bootVlanId": "",
                                              "bootVolumeSource": "UserDefined",
                                              "iscsi": {
                                                  "initiatorNameSource": "UserDefined",
                                                  "initiatorName": PROFILE2_INITIATOR_NAME,
                                                  "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                                                  "firstBootTargetPort": "3260",
                                                  "secondBootTargetIp": "",
                                                  "secondBootTargetPort": "",
                                                  "bootTargetName": PROFILE2_BOOT_TARGET_NAME,
                                                  "bootTargetLun": "0",
                                                  "chapLevel": "Chap",
                                                  "chapName": PROFILE2_CHAP_NAME,
                                                  "chapSecret": CHAP_SECRET,
                                                  "mutualChapName": "",
                                                  "mutualChapSecret": None},
                                          }
                                          },
                                     ]},
                                     "boot": {"manageBoot": True,
                                              "order": ["HardDisk", "CD", "USB", "PXE"]},
                                     "bootMode": {"manageMode": True, "mode": "BIOS"},
                                     "firmware": {"manageFirmware": False},
                                     "bios": {"manageBios": False, "overriddenSettings": []},
                                     "hideUnusedFlexNics": True,
                                     "iscsiInitiatorName": PROFILE2_INITIATOR_NAME,
                                     "localStorage": {"sasLogicalJBODs": [], "controllers": []},
                                     "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                     }

# Profile3: ENC3 bay7, BL660c Gen9, UEFI mode,
# Connection initiator name uses profile defined
# Profile initiator name is user defined
# primary on LOM2:2b
# MCHAP, untagged network
profile3_one_bootable_connection = {"type": SERVER_PROFILE_TYPE,
                                    "serverHardwareUri": 'SH:' + PROFILE3_SERVER,
                                    "enclosureGroupUri": 'EG:' + PROFILE3_EG,
                                    "serialNumberType": "Physical",
                                    "iscsiInitiatorNameType": "UserDefined",
                                    "macType": "Physical",
                                    "wwnType": "Physical",
                                    "name": PROFILE3_NAME,
                                    "description": "",
                                    "affinity": "Bay",
                                    "connectionSettings": {"connections": [
                                        {"id": 1,
                                         "name": "iSCSI-boot-primary",
                                         "functionType": "iSCSI",
                                         "portId": "Flb 2:2-b",
                                         "requestedMbps": "2500",
                                         "networkUri": 'ETH:network-untagged',
                                         "ipv4": {
                                             "ipAddressSource": "UserDefined",
                                             "subnetMask": INITIATOR_SUBNET_MASK,
                                             "gateway": INITIATOR_GATEWAY,
                                             "ipAddress": PROFILE3_INITIATOR_IP_1
                                         },
                                         "boot": {
                                             "priority": "Primary",
                                             "bootVlanId": "",
                                             "bootVolumeSource": "UserDefined",
                                             "iscsi": {
                                                 "initiatorNameSource": "ProfileInitiatorName",
                                                 "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                                                 "firstBootTargetPort": "3260",
                                                 "secondBootTargetIp": "",
                                                 "secondBootTargetPort": "",
                                                 "bootTargetName": PROFILE3_BOOT_TARGET_NAME,
                                                 "bootTargetLun": "0",
                                                 "chapLevel": "MutualChap",
                                                 "chapName": PROFILE3_CHAP_NAME,
                                                 "chapSecret": CHAP_SECRET,
                                                 "mutualChapName": PROFILE3_MCHAP_NAME,
                                                 "mutualChapSecret": MCHAP_SECRET},
                                         }
                                         },
                                    ]},
                                    "boot": {"manageBoot": True, "order": ["HardDisk"]},
                                    "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                    "firmware": {"manageFirmware": False},
                                    "bios": {"manageBios": False, "overriddenSettings": []},
                                    "hideUnusedFlexNics": True,
                                    "iscsiInitiatorName": PROFILE3_INITIATOR_NAME,
                                    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
                                    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                    }

# Profile3: ENC3 bay7, BL660c Gen9, UEFI mode
# Connection initiator name uses profile defined
# Profile initiator name is user defined
# primary on LOM2:2b and secondary on LOM2:1b
# MCHAP, untagged network
profile3_two_bootable_connections = {"type": SERVER_PROFILE_TYPE,
                                     "serverHardwareUri": 'SH:' + PROFILE3_SERVER,
                                     "enclosureGroupUri": 'EG:' + PROFILE3_EG,
                                     "serialNumberType": "Physical",
                                     "iscsiInitiatorNameType": "UserDefined",
                                     "macType": "Physical",
                                     "wwnType": "Physical",
                                     "name": PROFILE3_NAME,
                                     "description": "",
                                     "affinity": "Bay",
                                     "connectionSettings": {"connections": [
                                         {"id": 1,
                                          "name": "iSCSI-boot-primary",
                                          "functionType": "iSCSI",
                                          "portId": "Flb 2:2-b",
                                          "requestedMbps": "2500",
                                          "networkUri": 'ETH:network-untagged',
                                          "ipv4": {
                                              "ipAddressSource": "UserDefined",
                                              "subnetMask": INITIATOR_SUBNET_MASK,
                                              "gateway": INITIATOR_GATEWAY,
                                              "ipAddress": PROFILE3_INITIATOR_IP_1
                                          },
                                          "boot": {
                                              "priority": "Primary",
                                              "bootVlanId": "",
                                              "bootVolumeSource": "UserDefined",
                                              "iscsi": {
                                                  "initiatorNameSource": "ProfileInitiatorName",
                                                  "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                                                  "firstBootTargetPort": "3260",
                                                  "secondBootTargetIp": "",
                                                  "secondBootTargetPort": "",
                                                  "bootTargetName": PROFILE3_BOOT_TARGET_NAME,
                                                  "bootTargetLun": "0",
                                                  "chapLevel": "MutualChap",
                                                  "chapName": PROFILE3_CHAP_NAME,
                                                  "chapSecret": CHAP_SECRET,
                                                  "mutualChapName": PROFILE3_MCHAP_NAME,
                                                  "mutualChapSecret": MCHAP_SECRET},
                                          }
                                          },
                                         {"id": 2,
                                          "name": "iSCSI-boot-secondary",
                                          "functionType": "iSCSI",
                                          "portId": "Flb 2:1-b",
                                          "requestedMbps": "2500",
                                          "networkUri": 'ETH:network-untagged',
                                          "ipv4": {
                                              "ipAddressSource": "UserDefined",
                                              "subnetMask": INITIATOR_SUBNET_MASK,
                                              "gateway": INITIATOR_GATEWAY,
                                              "ipAddress": PROFILE3_INITIATOR_IP_2
                                          },
                                          "boot": {
                                              "priority": "Secondary",
                                              "bootVlanId": "",
                                              "bootVolumeSource": "UserDefined",
                                              "iscsi": {
                                                  "initiatorNameSource": "ProfileInitiatorName",
                                                  "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                                                  "firstBootTargetPort": "3260",
                                                  "secondBootTargetIp": "",
                                                  "secondBootTargetPort": "",
                                                  "bootTargetName": PROFILE3_BOOT_TARGET_NAME,
                                                  "bootTargetLun": "0",
                                                  "chapLevel": "MutualChap",
                                                  "chapName": PROFILE3_CHAP_NAME,
                                                  "chapSecret": CHAP_SECRET,
                                                  "mutualChapName": PROFILE3_MCHAP_NAME,
                                                  "mutualChapSecret": MCHAP_SECRET},
                                          }
                                          },
                                     ]},
                                     "boot": {"manageBoot": True, "order": ["HardDisk"]},
                                     "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                     "firmware": {"manageFirmware": False},
                                     "bios": {"manageBios": False, "overriddenSettings": []},
                                     "hideUnusedFlexNics": True,
                                     "iscsiInitiatorName": PROFILE3_INITIATOR_NAME,
                                     "localStorage": {"sasLogicalJBODs": [], "controllers": []},
                                     "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                     }

# Profile4: ENC3 bay 8, BL660c Gen8
# Connection initiator name user defined
# Profile initiator name is user defined
# Primary on LOM1:2b
# CHAP,untagged network
profile4_one_bootable_connection_lom = {"type": SERVER_PROFILE_TYPE,
                                        "serverHardwareUri": 'SH:' + PROFILE4_SERVER,
                                        "enclosureGroupUri": 'EG:' + PROFILE4_EG,
                                        "serialNumberType": "Physical",
                                        "iscsiInitiatorNameType": "UserDefined",
                                        "macType": "Physical",
                                        "wwnType": "Physical",
                                        "name": PROFILE4_NAME,
                                        "description": "",
                                        "affinity": "Bay",
                                        "connectionSettings": {"connections": [
                                            {"id": 1,
                                             "name": "iSCSI-boot-primary",
                                             "functionType": "iSCSI",
                                             "portId": "Flb 1:2-b",
                                             "requestedMbps": "2500",
                                             "networkUri": 'ETH:network-untagged',
                                             "ipv4": {
                                                 "ipAddressSource": "UserDefined",
                                                 "subnetMask": INITIATOR_SUBNET_MASK,
                                                 "gateway": INITIATOR_GATEWAY,
                                                 "ipAddress": PROFILE4_INITIATOR_IP_1
                                             },
                                             "boot": {
                                                 "priority": "Primary",
                                                 "bootVlanId": "",
                                                 "bootVolumeSource": "UserDefined",
                                                 "iscsi": {
                                                     "initiatorNameSource": "UserDefined",
                                                     "initiatorName": PROFILE4_INITIATOR_NAME,
                                                     "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                                                     "firstBootTargetPort": "3260",
                                                     "secondBootTargetIp": "",
                                                     "secondBootTargetPort": "",
                                                     "bootTargetName": PROFILE4_BOOT_TARGET_NAME,
                                                     "bootTargetLun": "0",
                                                     "chapLevel": "Chap",
                                                     "chapName": PROFILE4_CHAP_NAME,
                                                     "chapSecret": CHAP_SECRET,
                                                     "mutualChapName": "",
                                                     "mutualChapSecret": None},
                                             }
                                             },
                                        ]},
                                        "boot": {"manageBoot": True,
                                                 "order": ["HardDisk", "CD", "Floppy", "USB", "PXE"]},
                                        "bootMode": None,
                                        "firmware": {"manageFirmware": False},
                                        "bios": {"manageBios": False, "overriddenSettings": []},
                                        "hideUnusedFlexNics": True,
                                        "iscsiInitiatorName": PROFILE4_INITIATOR_NAME,
                                        "localStorage": {"sasLogicalJBODs": [], "controllers": []},
                                        "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                        }

# Profile4, ENC3 bay 8, BL660c Gen8
# Connection initiator name user defined
# Profile initiator name is user defined
# Primary on Mezz1:1b
# CHAP, untagged network
profile4_one_bootable_connection_mezz = {"type": SERVER_PROFILE_TYPE,
                                         "serverHardwareUri": 'SH:' + PROFILE4_SERVER,
                                         "enclosureGroupUri": 'EG:' + PROFILE4_EG,
                                         "serialNumberType": "Physical",
                                         "iscsiInitiatorNameType": "UserDefined",
                                         "macType": "Physical",
                                         "wwnType": "Physical",
                                         "name": PROFILE4_NAME,
                                         "description": "",
                                         "affinity": "Bay",
                                         "connectionSettings": {"connections": [
                                             {"id": 1,
                                              "name": "iSCSI-boot-primary",
                                              "functionType": "iSCSI",
                                              "portId": "Mezz 1:1-b",
                                              "requestedMbps": "2500",
                                              "networkUri": 'ETH:network-untagged',
                                              "ipv4": {
                                                  "ipAddressSource": "UserDefined",
                                                  "subnetMask": INITIATOR_SUBNET_MASK,
                                                  "gateway": INITIATOR_GATEWAY,
                                                  "ipAddress": PROFILE4_INITIATOR_IP_1
                                              },
                                              "boot": {
                                                  "priority": "Primary",
                                                  "bootVlanId": "",
                                                  "bootVolumeSource": "UserDefined",
                                                  "iscsi": {
                                                      "initiatorNameSource": "UserDefined",
                                                      "initiatorName": PROFILE4_INITIATOR_NAME,
                                                      "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                                                      "firstBootTargetPort": "3260",
                                                      "secondBootTargetIp": "",
                                                      "secondBootTargetPort": "",
                                                      "bootTargetName": PROFILE4_BOOT_TARGET_NAME,
                                                      "bootTargetLun": "0",
                                                      "chapLevel": "Chap",
                                                      "chapName": PROFILE4_CHAP_NAME,
                                                      "chapSecret": CHAP_SECRET,
                                                      "mutualChapName": "",
                                                      "mutualChapSecret": None},
                                              }
                                              },
                                         ]},
                                         "boot": {"manageBoot": True,
                                                  "order": ["HardDisk", "CD", "Floppy", "USB", "PXE"]},
                                         "bootMode": None,
                                         "firmware": {"manageFirmware": False},
                                         "bios": {"manageBios": False, "overriddenSettings": []},
                                         "hideUnusedFlexNics": True,
                                         "iscsiInitiatorName": PROFILE4_INITIATOR_NAME,
                                         "localStorage": {"sasLogicalJBODs": [], "controllers": []},
                                         "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                         }

# Profile5: profile2 moved from ENC1 bay5 to ENC2 bay1
# Connection initiator name uses profile initiator name.
# Profile initiator name is user-defined
# primary on LOM1:1b
# No CHAP, tunnel network
profile5 = {"type": SERVER_PROFILE_TYPE,
            "serverHardwareUri": 'SH:' + PROFILE5_SERVER,
            "enclosureGroupUri": 'EG:' + PROFILE5_EG,
            "serialNumberType": "Physical",
            "iscsiInitiatorNameType": "UserDefined",
            "macType": "Physical",
            "wwnType": "Physical",
            "name": PROFILE2_NAME,
            "description": "",
            "affinity": "Bay",
            "connectionSettings": {"connections": [
                {"id": 1, "name": "iSCSI-boot-primary",
                 "functionType": "iSCSI",
                 "portId": "Flb 1:1-b",
                 "requestedMbps": "2500",
                 "networkUri": 'ETH:network-tunnel',
                 "ipv4": {
                     "ipAddressSource": "UserDefined",
                     "subnetMask": INITIATOR_SUBNET_MASK,
                     "gateway": INITIATOR_GATEWAY,
                     "ipAddress": PROFILE5_INITIATOR_IP_1
                 },
                 "boot": {
                     "priority": "Primary",
                     "bootVlanId": "",
                     "bootVolumeSource": "UserDefined",
                     "iscsi": {
                         "initiatorNameSource": "ProfileInitiatorName",
                         "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                         "firstBootTargetPort": "3260",
                         "secondBootTargetIp": "",
                         "secondBootTargetPort": "",
                         "chapLevel": "None",
                         "bootTargetName": PROFILE5_BOOT_TARGET_NAME,
                         "bootTargetLun": "0",
                         "chapName": "",
                         "chapSecret": None,
                         "mutualChapName": "",
                         "mutualChapSecret": None},
                 }
                 },
            ]},
            "boot": {"manageBoot": True,
                     "order": ["HardDisk", "CD", "Floppy", "USB", "PXE"]},
            "bootMode": None,
            "firmware": {"manageFirmware": False},
            "bios": {"manageBios": False, "overriddenSettings": []},
            "hideUnusedFlexNics": True,
            "iscsiInitiatorName": PROFILE5_INITIATOR_NAME,
            "localStorage": {"sasLogicalJBODs": [], "controllers": []},
            "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
            }

# Profile6: profile3 on ENC3 bay7 moved to ENC3 bay3
# Connection initiator name uses defined
# Profile initiator name is user-defined
# primary on Mezz1:1b, secondary on Mezz1:2b
# CHAP, untagged network
profile6 = {"type": SERVER_PROFILE_TYPE,
            "serverHardwareUri": 'SH:' + PROFILE6_SERVER,
            "enclosureGroupUri": 'EG:' + PROFILE6_EG,
            "serialNumberType": "Physical",
            "iscsiInitiatorNameType": "UserDefined",
            "macType": "Physical",
            "wwnType": "Physical",
            "name": PROFILE3_NAME,
            "description": "",
            "affinity": "Bay",
            "connectionSettings": {"connections": [
                {"id": 1,
                 "name": "iSCSI-boot-primary",
                 "functionType": "iSCSI",
                 "portId": "Mezz 1:1-b",
                 "requestedMbps": "2500",
                 "networkUri": 'ETH:network-untagged',
                 "ipv4": {
                     "ipAddressSource": "UserDefined",
                     "subnetMask": INITIATOR_SUBNET_MASK,
                     "gateway": INITIATOR_GATEWAY,
                     "ipAddress": PROFILE6_INITIATOR_IP_1
                 },
                 "boot": {
                     "priority": "Primary",
                     "bootVlanId": "",
                     "bootVolumeSource": "UserDefined",
                     "iscsi": {
                         "initiatorNameSource": "UserDefined",
                         "initiatorName": PROFILE6_INITIATOR_NAME,
                         "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                         "firstBootTargetPort": "3260",
                         "secondBootTargetIp": "",
                         "secondBootTargetPort": "",
                         "bootTargetName": PROFILE6_BOOT_TARGET_NAME,
                         "bootTargetLun": "0",
                         "chapLevel": "Chap",
                         "chapName": PROFILE6_CHAP_NAME,
                         "chapSecret": CHAP_SECRET,
                         "mutualChapName": "",
                         "mutualChapSecret": None},
                 }
                 },
                {"id": 2,
                 "name": "iSCSI-boot-secondary",
                 "functionType": "iSCSI",
                 "portId": "Mezz 1:2-b",
                 "requestedMbps": "2500",
                 "networkUri": 'ETH:network-untagged',
                 "ipv4": {
                     "ipAddressSource": "UserDefined",
                     "subnetMask": INITIATOR_SUBNET_MASK,
                     "gateway": INITIATOR_GATEWAY,
                     "ipAddress": PROFILE6_INITIATOR_IP_2
                 },
                 "boot": {
                     "priority": "Secondary",
                     "bootVlanId": "",
                     "bootVolumeSource": "UserDefined",
                     "iscsi": {
                         "initiatorNameSource": "ProfileInitiatorName",
                         "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                         "firstBootTargetPort": "3260",
                         "secondBootTargetIp": "",
                         "secondBootTargetPort": "",
                         "bootTargetName": PROFILE6_BOOT_TARGET_NAME,
                         "bootTargetLun": "0",
                         "chapLevel": "Chap",
                         "chapName": PROFILE6_CHAP_NAME,
                         "chapSecret": CHAP_SECRET,
                         "mutualChapName": "",
                         "mutualChapSecret": None},
                 }
                 }
            ]},
            "boot": {"manageBoot": True,
                     "order": ["HardDisk", "CD", "Floppy", "USB", "PXE"]},
            "bootMode": None,
            "firmware": {"manageFirmware": False},
            "bios": {"manageBios": False, "overriddenSettings": []},
            "hideUnusedFlexNics": True,
            "iscsiInitiatorName": PROFILE6_INITIATOR_NAME,
            "localStorage": {"sasLogicalJBODs": [], "controllers": []},
            "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
            }

# Profile7: profile4 moved from ENC3 bay8 moved to ENC2 bay5
# Connection initiator name uses defined
# Profile initiator name is user-defined
# primary on Mezz1:1b, secondary on Mezz1:2b
# No CHAP, untagged network
profile7 = {"type": SERVER_PROFILE_TYPE,
            "serverHardwareUri": 'SH:' + PROFILE7_SERVER,
            "enclosureGroupUri": 'EG:' + PROFILE7_EG,
            "serialNumberType": "Physical",
            "iscsiInitiatorNameType": "UserDefined",
            "macType": "Physical",
            "wwnType": "Physical",
            "name": PROFILE4_NAME,
            "description": "",
            "affinity": "Bay",
            "connectionSettings": {"connections": [
                {"id": 1,
                 "name": "iSCSI-boot-primary",
                 "functionType": "iSCSI",
                 "portId": "Mezz 1:1-b",
                 "requestedMbps": "2500",
                 "networkUri": 'ETH:network-untagged',
                 "ipv4": {
                     "ipAddressSource": "UserDefined",
                     "subnetMask": INITIATOR_SUBNET_MASK,
                     "gateway": INITIATOR_GATEWAY,
                     "ipAddress": PROFILE7_INITIATOR_IP_1
                 },
                 "boot": {
                     "priority": "Primary",
                     "bootVlanId": "",
                     "bootVolumeSource": "UserDefined",
                     "iscsi": {
                         "initiatorNameSource": "ProfileInitiatorName",
                         "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                         "firstBootTargetPort": "3260",
                         "secondBootTargetIp": "",
                         "secondBootTargetPort": "",
                         "chapLevel": "None",
                         "bootTargetName": PROFILE7_BOOT_TARGET_NAME,
                         "bootTargetLun": "0",
                         "chapName": "",
                         "chapSecret": None,
                         "mutualChapName": "",
                         "mutualChapSecret": None},
                 }
                 },
                {"id": 2,
                 "name": "iSCSI-boot-secondary",
                 "functionType": "iSCSI",
                 "portId": "Mezz 1:2-b",
                 "requestedMbps": "2500",
                 "networkUri": 'ETH:network-untagged',
                 "ipv4": {
                     "ipAddressSource": "UserDefined",
                     "subnetMask": INITIATOR_SUBNET_MASK,
                     "gateway": INITIATOR_GATEWAY,
                     "ipAddress": PROFILE7_INITIATOR_IP_2
                 },
                 "boot": {
                     "priority": "Secondary",
                     "bootVlanId": "",
                     "bootVolumeSource": "UserDefined",
                     "iscsi": {
                         "initiatorNameSource": "ProfileInitiatorName",
                         "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                         "firstBootTargetPort": "3260",
                         "secondBootTargetIp": "",
                         "secondBootTargetPort": "",
                         "chapLevel": "None",
                         "bootTargetName": PROFILE7_BOOT_TARGET_NAME,
                         "bootTargetLun": "0",
                         "chapName": "",
                         "chapSecret": None,
                         "mutualChapName": "",
                         "mutualChapSecret": None},
                 }
                 }
            ]},
            "boot": {"manageBoot": True, "order": ["HardDisk"]},
            "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
            "firmware": {"manageFirmware": False},
            "bios": {"manageBios": False, "overriddenSettings": []},
            "hideUnusedFlexNics": True,
            "iscsiInitiatorName": PROFILE7_INITIATOR_NAME,
            "localStorage": {"sasLogicalJBODs": [], "controllers": []},
            "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
            }

# Profile8: ENC1 bay14, BL460c Gen10, Legacy BIOS boot mode
# Connection initiator name is user defined
# Profile initiator name is user-defined
# primary on FLB1:2b
# CHAP, tunnel network
profile8_one_bootable_connection = {"type": SERVER_PROFILE_TYPE,
                                    "serverHardwareUri": 'SH:' + PROFILE8_SERVER,
                                    "enclosureGroupUri": 'EG:' + PROFILE8_EG,
                                    "serialNumberType": "Physical",
                                    "iscsiInitiatorNameType": "UserDefined",
                                    "macType": "Physical",
                                    "wwnType": "Physical",
                                    "name": PROFILE8_NAME,
                                    "description": "",
                                    "affinity": "Bay",
                                    "connectionSettings": {"connections": [
                                        {"id": 1,
                                         "name": "iSCSI-boot-primary",
                                         "functionType": "iSCSI",
                                         "portId": "Flb 1:2-b",
                                         "requestedMbps": "2500",
                                         "networkUri": 'ETH:network-tunnel',
                                         "ipv4": {
                                             "ipAddressSource": "UserDefined",
                                             "subnetMask": INITIATOR_SUBNET_MASK,
                                             "gateway": INITIATOR_GATEWAY,
                                             "ipAddress": PROFILE8_INITIATOR_IP_1
                                         },
                                         "boot": {
                                             "priority": "Primary",
                                             "bootVlanId": "",
                                             "bootVolumeSource": "UserDefined",
                                             "iscsi": {
                                                 "initiatorNameSource": "UserDefined",
                                                 "initiatorName": PROFILE8_INITIATOR_NAME,
                                                 "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                                                 "firstBootTargetPort": "3260",
                                                 "secondBootTargetIp": "",
                                                 "secondBootTargetPort": "",
                                                 "bootTargetName": PROFILE8_BOOT_TARGET_NAME,
                                                 "bootTargetLun": "0",
                                                 "chapLevel": "MutualChap",
                                                 "chapName": PROFILE8_CHAP_NAME,
                                                 "chapSecret": CHAP_SECRET,
                                                 "mutualChapName": PROFILE8_MCHAP_NAME,
                                                 "mutualChapSecret": MCHAP_SECRET},
                                         }
                                         },
                                    ]},
                                    "boot": {"manageBoot": True,
                                             "order": ["HardDisk", "CD", "USB", "PXE"]},
                                    "bootMode": {"manageMode": True, "mode": "BIOS"},
                                    "firmware": {"manageFirmware": False},
                                    "bios": {"manageBios": False, "overriddenSettings": []},
                                    "hideUnusedFlexNics": True,
                                    "iscsiInitiatorName": PROFILE8_INITIATOR_NAME,
                                    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
                                    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                    }
# Profile9: ENC1 bay16, BL460c Gen10, Legacy BIOS boot mode
# Connection initiator name is user defined
# Profile initiator name is user-defined
# primary onFLB1:1b, secondary on FLB1:2b
# CHAP, tunnel network
profile9_two_bootable_connections = {"type": SERVER_PROFILE_TYPE,
                                     "serverHardwareUri": 'SH:' + PROFILE9_SERVER,
                                     "enclosureGroupUri": 'EG:' + PROFILE9_EG,
                                     "serialNumberType": "Physical",
                                     "iscsiInitiatorNameType": "UserDefined",
                                     "macType": "Physical",
                                     "wwnType": "Physical",
                                     "name": PROFILE9_NAME,
                                     "description": "",
                                     "affinity": "Bay",
                                     "connectionSettings": {"connections": [
                                         {"id": 1,
                                          "name": "iSCSI-boot-primary",
                                          "functionType": "iSCSI",
                                          "portId": "Flb 1:1-b",
                                          "requestedMbps": "2500",
                                          "networkUri": 'ETH:network-tunnel',
                                          "ipv4": {
                                              "ipAddressSource": "UserDefined",
                                              "subnetMask": INITIATOR_SUBNET_MASK,
                                              "gateway": INITIATOR_GATEWAY,
                                              "ipAddress": PROFILE9_INITIATOR_IP_1
                                          },
                                          "boot": {
                                              "priority": "Primary",
                                              "bootVlanId": "",
                                              "bootVolumeSource": "UserDefined",
                                              "iscsi": {
                                                  "initiatorNameSource": "UserDefined",
                                                  "initiatorName": PROFILE9_INITIATOR_NAME,
                                                  "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                                                  "firstBootTargetPort": "3260",
                                                  "secondBootTargetIp": "",
                                                  "secondBootTargetPort": "",
                                                  "bootTargetName": PROFILE9_BOOT_TARGET_NAME,
                                                  "bootTargetLun": "0",
                                                  "chapLevel": "Chap",
                                                  "chapName": PROFILE9_CHAP_NAME,
                                                  "chapSecret": CHAP_SECRET,
                                                  "mutualChapName": "",
                                                  "mutualChapSecret": None},
                                          }
                                          },
                                         {"id": 2,
                                          "name": "iSCSI-boot-secondary",
                                          "functionType": "iSCSI",
                                          "portId": "Flb 1:2-b",
                                          "requestedMbps": "2500",
                                          "networkUri": 'ETH:network-tunnel',
                                          "ipv4": {
                                              "ipAddressSource": "UserDefined",
                                              "subnetMask": INITIATOR_SUBNET_MASK,
                                              "gateway": INITIATOR_GATEWAY,
                                              "ipAddress": PROFILE9_INITIATOR_IP_2
                                          },
                                          "boot": {
                                              "priority": "Secondary",
                                              "bootVlanId": "",
                                              "bootVolumeSource": "UserDefined",
                                              "iscsi": {
                                                  "initiatorNameSource": "UserDefined",
                                                  "initiatorName": PROFILE9_INITIATOR_NAME,
                                                  "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                                                  "firstBootTargetPort": "3260",
                                                  "secondBootTargetIp": "",
                                                  "secondBootTargetPort": "",
                                                  "bootTargetName": PROFILE9_BOOT_TARGET_NAME,
                                                  "bootTargetLun": "0",
                                                  "chapLevel": "Chap",
                                                  "chapName": PROFILE9_CHAP_NAME,
                                                  "chapSecret": CHAP_SECRET,
                                                  "mutualChapName": "",
                                                  "mutualChapSecret": None},
                                          }
                                          },
                                     ]},
                                     "boot": {"manageBoot": True,
                                              "order": ["HardDisk", "CD", "USB", "PXE"]},
                                     "bootMode": {"manageMode": True, "mode": "BIOS"},
                                     "firmware": {"manageFirmware": False},
                                     "bios": {"manageBios": False, "overriddenSettings": []},
                                     "hideUnusedFlexNics": True,
                                     "iscsiInitiatorName": PROFILE9_INITIATOR_NAME,
                                     "localStorage": {"sasLogicalJBODs": [], "controllers": []},
                                     "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                     }
# Profile9: ENC1 bay16, BL460c Gen10, Legacy BIOS boot mode
# Connection initiator name is user defined
# Profile initiator name is user-defined
# primary on FLB1:1b
# CHAP, tunnel network
profile9_one_bootable_connection = {"type": SERVER_PROFILE_TYPE,
                                    "serverHardwareUri": 'SH:' + PROFILE9_SERVER,
                                    "enclosureGroupUri": 'EG:' + PROFILE9_EG,
                                    "serialNumberType": "Physical",
                                    "iscsiInitiatorNameType": "UserDefined",
                                    "macType": "Physical",
                                    "wwnType": "Physical",
                                    "name": PROFILE9_NAME,
                                    "description": "",
                                    "affinity": "Bay",
                                    "connectionSettings": {"connections": [
                                        {"id": 1,
                                         "name": "iSCSI-boot-primary",
                                         "functionType": "iSCSI",
                                         "portId": "Flb 1:1-b",
                                         "requestedMbps": "2500",
                                         "networkUri": 'ETH:network-tunnel',
                                         "ipv4": {
                                             "ipAddressSource": "UserDefined",
                                             "subnetMask": INITIATOR_SUBNET_MASK,
                                             "gateway": INITIATOR_GATEWAY,
                                             "ipAddress": PROFILE9_INITIATOR_IP_1
                                         },
                                         "boot": {
                                             "priority": "Primary",
                                             "bootVlanId": "",
                                             "bootVolumeSource": "UserDefined",
                                             "iscsi": {
                                                 "initiatorNameSource": "UserDefined",
                                                 "initiatorName": PROFILE9_INITIATOR_NAME,
                                                 "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                                                 "firstBootTargetPort": "3260",
                                                 "secondBootTargetIp": "",
                                                 "secondBootTargetPort": "",
                                                 "bootTargetName": PROFILE9_BOOT_TARGET_NAME,
                                                 "bootTargetLun": "0", "chapLevel": "Chap",
                                                 "chapName": PROFILE9_CHAP_NAME,
                                                 "chapSecret": CHAP_SECRET,
                                                 "mutualChapName": "",
                                                 "mutualChapSecret": None},
                                         }
                                         },
                                    ]},
                                    "boot": {"manageBoot": True,
                                             "order": ["HardDisk", "CD", "USB", "PXE"]},
                                    "bootMode": {"manageMode": True, "mode": "BIOS"},
                                    "firmware": {"manageFirmware": False},
                                    "bios": {"manageBios": False, "overriddenSettings": []},
                                    "hideUnusedFlexNics": True,
                                    "iscsiInitiatorName": PROFILE9_INITIATOR_NAME,
                                    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
                                    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                    }

create_profiles = [profile1_one_unbootable_connection.copy(),
                   profile2_two_bootable_connections.copy(),
                   profile3_one_bootable_connection.copy(),
                   profile4_one_bootable_connection_lom.copy(), ]

create_profiles_bootable = [
    profile2_two_bootable_connections.copy(),
    profile3_one_bootable_connection.copy(),
    profile4_one_bootable_connection_lom.copy(), ]

edit_profiles = [profile1_one_bootable_connection.copy(),
                 profile2_one_bootable_connection.copy(),
                 profile3_two_bootable_connections.copy(),
                 profile4_one_bootable_connection_mezz.copy(), ]

move_profiles = [profile5.copy(),
                 profile6.copy(),
                 profile7.copy(),
                 ]

gen9_move_profiles = [profile3_two_bootable_connections.copy(), ]

delete_profiles = [profile1_one_bootable_connection.copy(),
                   profile5.copy(),
                   profile6.copy(),
                   profile7.copy(),
                   ]

gen9_delete_profiles = [profile7.copy(), ]

create_gen10_profiles = [profile8_one_bootable_connection.copy(),
                         profile9_two_bootable_connections.copy(), ]

edit_gen10_profiles = [profile9_one_bootable_connection.copy(), ]

delete_gen10_profiles = [profile8_one_bootable_connection.copy(),
                         profile9_one_bootable_connection.copy(), ]

all_profiles = [profile1_one_bootable_connection.copy(),
                profile2_one_bootable_connection.copy(),
                profile3_one_bootable_connection.copy(),
                profile4_one_bootable_connection_mezz.copy(),
                profile5.copy(),
                profile6.copy(),
                profile7.copy(),
                ]


# RIS nodes

# Profile3: ENC3 bay7
ris_node_profile3 = {
    "server": PROFILE3_SERVER,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/rest/v1/Systems/1/bios/boot",
    "string": "NIC.FlexLOM.\\d.\\d.iSCSI"
}

# Profile7: ENC2 bay5, BL460c Gen9, UEFI mode
ris_node_profile7 = {
    "server": PROFILE7_SERVER,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/rest/v1/Systems/1/bios/boot",
    "string": "NIC.Slot.\\d.\\d.iSCSI"
}

ris_nodes_after_create = [ris_node_profile3.copy(), ]

ris_nodes_after_edit = [ris_node_profile3.copy(), ]

ris_nodes_after_move = [ris_node_profile7.copy()]

ris_nodes_after_delete = [ris_node_profile3.copy(),
                          ris_node_profile7.copy()]

# Blade CLPs

# profile1: ENC1 bay1
clp_profile1_no_profile = {
    "oa": PROFILE1_ENC_OA,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "1",
    "validate":
    """
--------------------------------------
HP FlexFabric 10Gb 2-port 554FLB Adapter
Mezz=9 (FLB=1) DevID=40h (off=0300h)
--------------------------------------
  FIP: 0 (off=031Ch)
     PID01: "set netport1 default"
     PID02: "exit"
  FIP: 1 (off=033Ch)
     PID01: "set netport2 default"
     PID02: "exit"
"""
}

# profile1: ENC1 bay1
clp_profile1_one_unbootable_connection = {
    "oa": PROFILE1_ENC_OA,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "1",
    "validate":
    """
--------------------------------------
HP FlexFabric 10Gb 2-port 554FLB Adapter
Mezz=9 (FLB=1) DevID=40h (off=0300h)
--------------------------------------
  FIP: 0 (off=031Ch)
     PID01: "set netport1 default"
     PID32: "set netport1 OEMHP_CVNI=2001"
     PID33: "set netport1 OEMHP_FlowControl=function"
     PID34: "set netport1 OEMHP_LF0="E;1;FC15B425C3C8;1000;0;0;disabled;disabled""
     PID35: "set netport1 OEMHP_LF1="I;1;FC15B425C3C9;1001;0;0;disabled;disabled""
     PID36: "set netport1 OEMHP_LF2="D;;;;;;;disabled""
     PID37: "set netport1 OEMHP_LF3="D;;;;;;;disabled""
     PID02: "exit"
  FIP: 1 (off=046Bh)
     PID01: "set netport2 default"
     PID32: "set netport2 OEMHP_CVNI=2001"
     PID33: "set netport2 OEMHP_FlowControl=function"
     PID34: "set netport2 OEMHP_LF0="E;1;FC15B425C3CC;1000;0;0;disabled;disabled""
     PID35: "set netport2 OEMHP_LF1="I;1;FC15B425C3CD;1001;2500;10000;disabled;enabled""
     PID36: "set netport2 OEMHP_LF2="D;;;;;;;disabled""
     PID37: "set netport2 OEMHP_LF3="D;;;;;;;disabled""
     PID02: "exit"
"""
}

# profile1: ENC1 bay1
clp_profile1_one_bootable_connection = {
    "oa": PROFILE1_ENC_OA,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "1",
    "validate":
    """
--------------------------------------
HP FlexFabric 10Gb 2-port 554FLB Adapter
Mezz=9 (FLB=1) DevID=40h (off=0300h)
--------------------------------------
  FIP: 0 (off=031Ch)
     PID01: "set netport1 default"
     PID32: "set netport1 OEMHP_CVNI=2001"
     PID33: "set netport1 OEMHP_FlowControl=function"
     PID34: "set netport1 OEMHP_LF0="E;1;FC15B425C3C8;1000;0;0;disabled;disabled""
     PID35: "set netport1 OEMHP_LF1="I;1;FC15B425C3C9;1001;0;0;disabled;disabled""
     PID36: "set netport1 OEMHP_LF2="D;;;;;;;disabled""
     PID37: "set netport1 OEMHP_LF3="D;;;;;;;disabled""
     PID02: "exit"
  FIP: 1 (off=046Bh)
     PID01: "set netport2 default"
     PID32: "set netport2 OEMHP_CVNI=2001"
     PID33: "set netport2 OEMHP_FlowControl=function"
     PID34: "set netport2 OEMHP_LF0="E;1;FC15B425C3CC;1000;0;0;disabled;disabled""
     PID35: "set netport2 OEMHP_LF1="I;1;FC15B425C3CD;1001;2500;10000;enabled;enabled""
     PID36: "set netport2 OEMHP_IPVersion=IPv4"
     PID37: "set netport2 OEMHP_InitiatorIP=192.168.22.140"
     PID38: "set netport2 OEMHP_InitiatorNetmask=255.255.192.0"
     PID39: "set netport2 OEMHP_InitiatorRoute=192.168.0.1"
     PID40: "set netport2 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst22-bay1"
     PID41: "set netport2 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:6927:wpst22-bay1-win2016-bootvol"
     PID42: "set netport2 OEMHP_targetIP=192.168.21.71"
     PID43: "set netport2 OEMHP_targetPort=3260"
     PID44: "set netport2 OEMHP_LUN=0"
     PID45: "set netport2 OEMHP_authenticationMethod=MutualCHAP"
     PID46: "set netport2 OEMHP_username="wpst22-bay1""
     PID47: "set netport2 OEMHP_secret=777073746870767365313233"
     PID48: "set netport2 OEMHP_MutualUsername="wpst22-bay1""
     PID49: "set netport2 OEMHP_mutualSecret=687076736531323377707374"
     PID50: "set netport2 OEMHP_LF2="D;;;;;;;disabled""
     PID51: "set netport2 OEMHP_LF3="D;;;;;;;disabled""
     PID02: "exit"
"""
}

# Profile2: ENC1 bay5
clp_profile2_no_profile = {
    "oa": PROFILE2_ENC_OA,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "5",
    "validate":
    """
--------------------------------------
HP FlexFabric 10Gb 2-port 534M Adapter
Mezz=1 DevID=4Eh (off=0300h)
--------------------------------------
  FIP: 0 (off=031Ch)
     PID01: "set netport1 default"
     PID02: "exit"
  FIP: 1 (off=033Ch)
     PID01: "set netport1 default"
     PID02: "exit"
--------------------------------------
HP LPe1605 16Gb FC HBA for BladeSystem c-Class
Mezz=2 DevID=4Ch (off=0200h)
--------------------------------------
  FIP: 0 (off=021Ch)
     PID01: "set netport0 default"
     PID02: "set netport0 OEMHP_hss=3413"
     PID03: "set netport1 default"
     PID04: "set netport1 OEMHP_hss=3413"
     PID05: "exit"
--------------------------------------
HP FlexFabric 10Gb 2-port 536FLB Adapter
Mezz=9 (FLB=1) DevID=40h (off=0300h)
--------------------------------------
  FIP: 0 (off=031Ch)
     PID01: "set netport1 default"
     PID02: "exit"
  FIP: 1 (off=033Ch)
     PID01: "set netport1 default"
     PID02: "exit"
"""
}

# Profile2: ENC1 bay5
clp_profile2_one_bootable_connection = {
    "oa": PROFILE2_ENC_OA,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "5",
    "validate":
    """
--------------------------------------
HP FlexFabric 10Gb 2-port 534M Adapter
Mezz=1 DevID=4Eh (off=0300h)
--------------------------------------
  FIP: 0 (off=031Ch)
     PID01: "set netport1 default"
     PID02: "exit"
  FIP: 1 (off=033Ch)
     PID01: "set netport1 default"
     PID02: "exit"
--------------------------------------
HP LPe1605 16Gb FC HBA for BladeSystem c-Class
Mezz=2 DevID=4Ch (off=0200h)
--------------------------------------
  FIP: 0 (off=021Ch)
     PID01: "set netport0 default"
     PID02: "set netport0 OEMHP_hss=3413"
     PID03: "set netport1 default"
     PID04: "set netport1 OEMHP_hss=3413"
     PID05: "exit"
--------------------------------------
HP FlexFabric 10Gb 2-port 536FLB Adapter
Mezz=9 (FLB=1) DevID=40h (off=0300h)
--------------------------------------
  FIP: 0 (off=031Ch)
     PID01: "set netport1 default"
     PID32: "set netport1 OEMHP_CVNI=2001"
     PID33: "set netport1 OEMHP_FlowControl=function"
     PID34: "set netport1 OEMHP_LF0="E;1;6CC21737C500;1000;0;0;disabled;disabled""
     PID35: "set netport1 OEMHP_LF1="I;1;6CC21737C501;0;2500;10000;enabled;enabled""
     PID36: "set netport1 OEMHP_IPVersion=IPv4"
     PID37: "set netport1 OEMHP_InitiatorIP=192.168.22.142"
     PID38: "set netport1 OEMHP_InitiatorNetmask=255.255.192.0"
     PID39: "set netport1 OEMHP_InitiatorRoute=192.168.0.1"
     PID40: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst22-bay5"
     PID41: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:6930:wpst22-bay5-win2016-bootvol"
     PID42: "set netport1 OEMHP_targetIP=192.168.21.71"
     PID43: "set netport1 OEMHP_targetPort=3260"
     PID44: "set netport1 OEMHP_LUN=0"
     PID45: "set netport1 OEMHP_authenticationMethod=CHAP"
     PID46: "set netport1 OEMHP_username="wpst22-bay5""
     PID47: "set netport1 OEMHP_secret=777073746870767365313233"
     PID48: "set netport1 OEMHP_LF2="D;;;;;;;disabled""
     PID49: "set netport1 OEMHP_LF3="D;;;;;;;disabled""
     PID02: "exit"
  FIP: 1 (off=06DBh)
     PID01: "set netport1 default"
     PID32: "set netport1 OEMHP_CVNI=2001"
     PID33: "set netport1 OEMHP_FlowControl=function"
     PID34: "set netport1 OEMHP_LF0="E;1;6CC21737C508;1000;0;0;disabled;disabled""
     PID35: "set netport1 OEMHP_LF1="I;1;6CC21737C509;1001;0;0;disabled;disabled""
     PID36: "set netport1 OEMHP_LF2="D;;;;;;;disabled""
     PID37: "set netport1 OEMHP_LF3="D;;;;;;;disabled""
     PID02: "exit"
"""
}

# Profile2: ENC1 bay5
clp_profile2_two_bootable_connections = {
    "oa": PROFILE2_ENC_OA,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "5",
    "validate":
    """
--------------------------------------
HP FlexFabric 10Gb 2-port 534M Adapter
Mezz=1 DevID=4Eh (off=0300h)
--------------------------------------
  FIP: 0 (off=031Ch)
     PID01: "set netport1 default"
     PID02: "exit"
  FIP: 1 (off=033Ch)
     PID01: "set netport1 default"
     PID02: "exit"
--------------------------------------
HP LPe1605 16Gb FC HBA for BladeSystem c-Class
Mezz=2 DevID=4Ch (off=0200h)
--------------------------------------
  FIP: 0 (off=021Ch)
     PID01: "set netport0 default"
     PID02: "set netport0 OEMHP_hss=3413"
     PID03: "set netport1 default"
     PID04: "set netport1 OEMHP_hss=3413"
     PID05: "exit"
--------------------------------------
HP FlexFabric 10Gb 2-port 536FLB Adapter
Mezz=9 (FLB=1) DevID=40h (off=0300h)
--------------------------------------
  FIP: 0 (off=031Ch)
     PID01: "set netport1 default"
     PID32: "set netport1 OEMHP_CVNI=2001"
     PID33: "set netport1 OEMHP_FlowControl=function"
     PID34: "set netport1 OEMHP_LF0="E;1;6CC21737C500;1000;0;0;disabled;disabled""
     PID35: "set netport1 OEMHP_LF1="I;1;6CC21737C501;1001;2500;10000;enabled;enabled""
     PID36: "set netport1 OEMHP_IPVersion=IPv4"
     PID37: "set netport1 OEMHP_InitiatorIP=192.168.22.142"
     PID38: "set netport1 OEMHP_InitiatorNetmask=255.255.192.0"
     PID39: "set netport1 OEMHP_InitiatorRoute=192.168.0.1"
     PID40: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst22-bay5"
     PID41: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:6930:wpst22-bay5-win2016-bootvol"
     PID42: "set netport1 OEMHP_targetIP=192.168.21.71"
     PID43: "set netport1 OEMHP_targetPort=3260"
     PID44: "set netport1 OEMHP_LUN=0"
     PID45: "set netport1 OEMHP_authenticationMethod=CHAP"
     PID46: "set netport1 OEMHP_username="wpst22-bay5""
     PID47: "set netport1 OEMHP_secret=777073746870767365313233"
     PID48: "set netport1 OEMHP_LF2="D;;;;;;;disabled""
     PID49: "set netport1 OEMHP_LF3="D;;;;;;;disabled""
     PID02: "exit"
  FIP: 1 (off=06DEh)
     PID01: "set netport1 default"
     PID32: "set netport1 OEMHP_CVNI=2001"
     PID33: "set netport1 OEMHP_FlowControl=function"
     PID34: "set netport1 OEMHP_LF0="E;1;6CC21737C508;1000;0;0;disabled;disabled""
     PID35: "set netport1 OEMHP_LF1="I;1;6CC21737C509;1001;2500;10000;enabled;enabled""
     PID36: "set netport1 OEMHP_IPVersion=IPv4"
     PID37: "set netport1 OEMHP_InitiatorIP=192.168.22.143"
     PID38: "set netport1 OEMHP_InitiatorNetmask=255.255.192.0"
     PID39: "set netport1 OEMHP_InitiatorRoute=192.168.0.1"
     PID40: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst22-bay5"
     PID41: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:6930:wpst22-bay5-win2016-bootvol"
     PID42: "set netport1 OEMHP_targetIP=192.168.21.71"
     PID43: "set netport1 OEMHP_targetPort=3260"
     PID44: "set netport1 OEMHP_LUN=0"
     PID45: "set netport1 OEMHP_authenticationMethod=CHAP"
     PID46: "set netport1 OEMHP_username="wpst22-bay5""
     PID47: "set netport1 OEMHP_secret=777073746870767365313233"
     PID48: "set netport1 OEMHP_LF2="D;;;;;;;disabled""
     PID49: "set netport1 OEMHP_LF3="D;;;;;;;disabled""
     PID02: "exit"
"""
}

# Profile 3: ENC3 bay 7
clp_profile3_no_profile = {
    "oa": PROFILE3_ENC_OA,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "7",
    "validate":
    """
--------------------------------------
HP FlexFabric 10Gb 2-port 536FLB Adapter
Mezz=9 (FLB=1) DevID=40h (off=0300h)
--------------------------------------
  FIP: 0 (off=031Ch)
     PID01: "set netport1 default"
     PID02: "exit"
  FIP: 1 (off=033Ch)
     PID01: "set netport1 default"
     PID02: "exit"
--------------------------------------
HP FlexFabric 10Gb 2-port 536FLB Adapter
Mezz=A (FLB=2) DevID=41h (off=0300h)
--------------------------------------
  FIP: 0 (off=031Ch)
     PID01: "set netport1 default"
     PID02: "exit"
  FIP: 1 (off=033Ch)
     PID01: "set netport1 default"
     PID02: "exit"
"""
}

# Profile3: ENC3 bay7
clp_profile3_one_bootable_connection = {
    "oa": PROFILE3_ENC_OA,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "7",
    "validate":
    """
--------------------------------------
HP FlexFabric 10Gb 2-port 536FLB Adapter
Mezz=9 (FLB=1) DevID=40h (off=0300h)
--------------------------------------
  FIP: 0 (off=031Ch)
     PID01: "set netport1 default"
     PID02: "exit"
  FIP: 1 (off=033Ch)
     PID01: "set netport1 default"
     PID02: "exit"
--------------------------------------
HP FlexFabric 10Gb 2-port 536FLB Adapter
Mezz=A (FLB=2) DevID=41h (off=0300h)
--------------------------------------
  FIP: 0 (off=031Ch)
     PID01: "set netport1 default"
     PID32: "set netport1 OEMHP_CVNI=2001"
     PID33: "set netport1 OEMHP_FlowControl=function"
     PID34: "set netport1 OEMHP_LF0="E;1;6CC2173718D0;1000;0;0;disabled;disabled""
     PID35: "set netport1 OEMHP_LF1="I;1;6CC2173718D1;1001;0;0;disabled;disabled""
     PID36: "set netport1 OEMHP_LF2="D;;;;;;;disabled""
     PID37: "set netport1 OEMHP_LF3="D;;;;;;;disabled""
     PID02: "exit"
  FIP: 1 (off=046Bh)
     PID01: "set netport1 default"
     PID32: "set netport1 OEMHP_CVNI=2001"
     PID33: "set netport1 OEMHP_FlowControl=function"
     PID34: "set netport1 OEMHP_LF0="E;1;6CC2173718D8;1000;0;0;disabled;disabled""
     PID35: "set netport1 OEMHP_LF1="I;1;6CC2173718D9;1001;2500;10000;enabled;enabled""
     PID36: "set netport1 OEMHP_IPVersion=IPv4"
     PID37: "set netport1 OEMHP_InitiatorIP=192.168.22.144"
     PID38: "set netport1 OEMHP_InitiatorNetmask=255.255.192.0"
     PID39: "set netport1 OEMHP_InitiatorRoute=192.168.0.1"
     PID40: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst26-bay7"
     PID41: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1309:wpst26-bay7-bootvol"
     PID42: "set netport1 OEMHP_targetIP=192.168.21.71"
     PID43: "set netport1 OEMHP_targetPort=3260"
     PID44: "set netport1 OEMHP_LUN=0"
     PID45: "set netport1 OEMHP_authenticationMethod=MutualCHAP"
     PID46: "set netport1 OEMHP_username="wpst26-bay7""
     PID47: "set netport1 OEMHP_secret=777073746870767365313233"
     PID48: "set netport1 OEMHP_MutualUsername="wpst26-bay7""
     PID49: "set netport1 OEMHP_mutualSecret=687076736531323377707374"
     PID50: "set netport1 OEMHP_LF2="D;;;;;;;disabled""
     PID51: "set netport1 OEMHP_LF3="D;;;;;;;disabled""
     PID02: "exit"
"""
}

# Profile 3: ENC3 bay7
clp_profile3_two_bootable_connections = {
    "oa": PROFILE3_ENC_OA,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "7",
    "validate":
    """
--------------------------------------
HP FlexFabric 10Gb 2-port 536FLB Adapter
Mezz=9 (FLB=1) DevID=40h (off=0300h)
--------------------------------------
  FIP: 0 (off=031Ch)
     PID01: "set netport1 default"
     PID02: "exit"
  FIP: 1 (off=033Ch)
     PID01: "set netport1 default"
     PID02: "exit"
--------------------------------------
HP FlexFabric 10Gb 2-port 536FLB Adapter
Mezz=A (FLB=2) DevID=41h (off=0300h)
--------------------------------------
  FIP: 0 (off=031Ch)
     PID01: "set netport1 default"
     PID32: "set netport1 OEMHP_CVNI=2001"
     PID33: "set netport1 OEMHP_FlowControl=function"
     PID34: "set netport1 OEMHP_LF0="E;1;6CC2173718D0;1000;0;0;disabled;disabled""
     PID35: "set netport1 OEMHP_LF1="I;1;6CC2173718D1;1001;2500;10000;enabled;enabled""
     PID36: "set netport1 OEMHP_IPVersion=IPv4"
     PID37: "set netport1 OEMHP_InitiatorIP=192.168.22.145"
     PID38: "set netport1 OEMHP_InitiatorNetmask=255.255.192.0"
     PID39: "set netport1 OEMHP_InitiatorRoute=192.168.0.1"
     PID40: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst26-bay7"
     PID41: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1309:wpst26-bay7-bootvol"
     PID42: "set netport1 OEMHP_targetIP=192.168.21.71"
     PID43: "set netport1 OEMHP_targetPort=3260"
     PID44: "set netport1 OEMHP_LUN=0"
     PID45: "set netport1 OEMHP_authenticationMethod=MutualCHAP"
     PID46: "set netport1 OEMHP_username="wpst26-bay7""
     PID47: "set netport1 OEMHP_secret=777073746870767365313233"
     PID48: "set netport1 OEMHP_MutualUsername="wpst26-bay7""
     PID49: "set netport1 OEMHP_mutualSecret=687076736531323377707374"
     PID50: "set netport1 OEMHP_LF2="D;;;;;;;disabled""
     PID51: "set netport1 OEMHP_LF3="D;;;;;;;disabled""
     PID02: "exit"
  FIP: 1 (off=0749h)
     PID01: "set netport1 default"
     PID32: "set netport1 OEMHP_CVNI=2001"
     PID33: "set netport1 OEMHP_FlowControl=function"
     PID34: "set netport1 OEMHP_LF0="E;1;6CC2173718D8;1000;0;0;disabled;disabled""
     PID35: "set netport1 OEMHP_LF1="I;1;6CC2173718D9;0;2500;10000;enabled;enabled""
     PID36: "set netport1 OEMHP_IPVersion=IPv4"
     PID37: "set netport1 OEMHP_InitiatorIP=192.168.22.144"
     PID38: "set netport1 OEMHP_InitiatorNetmask=255.255.192.0"
     PID39: "set netport1 OEMHP_InitiatorRoute=192.168.0.1"
     PID40: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst26-bay7"
     PID41: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1309:wpst26-bay7-bootvol"
     PID42: "set netport1 OEMHP_targetIP=192.168.21.71"
     PID43: "set netport1 OEMHP_targetPort=3260"
     PID44: "set netport1 OEMHP_LUN=0"
     PID45: "set netport1 OEMHP_authenticationMethod=MutualCHAP"
     PID46: "set netport1 OEMHP_username="wpst26-bay7""
     PID47: "set netport1 OEMHP_secret=777073746870767365313233"
     PID48: "set netport1 OEMHP_MutualUsername="wpst26-bay7""
     PID49: "set netport1 OEMHP_mutualSecret=687076736531323377707374"
     PID50: "set netport1 OEMHP_LF2="D;;;;;;;disabled""
     PID51: "set netport1 OEMHP_LF3="D;;;;;;;disabled""
     PID02: "exit"
"""
}

# Profile4: ENC3 bay8
clp_profile4_no_profile = {
    "oa": PROFILE4_ENC_OA,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "8",
    "validate":
    """
--------------------------------------
HP FlexFabric 10Gb 2-port 554M Adapter
Mezz=1 DevID=4Eh (off=0300h)
--------------------------------------
  FIP: 0 (off=031Ch)
     PID01: "set netport1 default"
     PID02: "exit"
  FIP: 1 (off=033Ch)
     PID01: "set netport2 default"
     PID02: "exit"
Blade 8 mezz 2: NOT FOUND
Blade 8 mezz 3: NOT FOUND
--------------------------------------
HP FlexFabric 10Gb 2-port 554FLB Adapter
Mezz=9 (FLB=1) DevID=40h (off=0300h)
--------------------------------------
  FIP: 0 (off=031Ch)
     PID01: "set netport1 default"
     PID02: "exit"
  FIP: 1 (off=033Ch)
     PID01: "set netport2 default"
     PID02: "exit"
--------------------------------------
HP FlexFabric 10Gb 2-port 554FLB Adapter
Mezz=A (FLB=2) DevID=41h (off=0300h)
--------------------------------------
  FIP: 0 (off=031Ch)
     PID01: "set netport1 default"
     PID02: "exit"
  FIP: 1 (off=033Ch)
     PID01: "set netport2 default"
     PID02: "exit"
"""
}

# Profile4: ENC3 bay8
clp_profile4_one_bootable_connection_lom = {
    "oa": PROFILE4_ENC_OA,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "8",
    "validate":
    """
--------------------------------------
HP FlexFabric 10Gb 2-port 554M Adapter
Mezz=1 DevID=4Eh (off=0300h)
--------------------------------------
  FIP: 0 (off=031Ch)
     PID01: "set netport1 default"
     PID02: "exit"
  FIP: 1 (off=033Ch)
     PID01: "set netport2 default"
     PID02: "exit"
Blade 8 mezz 2: NOT FOUND
Blade 8 mezz 3: NOT FOUND
--------------------------------------
HP FlexFabric 10Gb 2-port 554FLB Adapter
Mezz=9 (FLB=1) DevID=40h (off=0300h)
--------------------------------------
  FIP: 0 (off=031Ch)
     PID01: "set netport1 default"
     PID32: "set netport1 OEMHP_CVNI=2001"
     PID33: "set netport1 OEMHP_FlowControl=function"
     PID34: "set netport1 OEMHP_LF0="E;1;B4B52F5AAA20;1000;0;0;disabled;disabled""
     PID35: "set netport1 OEMHP_LF1="I;1;B4B52F5AAA21;1001;0;0;disabled;disabled""
     PID36: "set netport1 OEMHP_LF2="D;;;;;;;disabled""
     PID37: "set netport1 OEMHP_LF3="D;;;;;;;disabled""
     PID02: "exit"
  FIP: 1 (off=046Bh)
     PID01: "set netport2 default"
     PID32: "set netport2 OEMHP_CVNI=2001"
     PID33: "set netport2 OEMHP_FlowControl=function"
     PID34: "set netport2 OEMHP_LF0="E;1;B4B52F5AAA24;1000;0;0;disabled;disabled""
     PID35: "set netport2 OEMHP_LF1="I;1;B4B52F5AAA25;1001;2500;10000;enabled;enabled""
     PID36: "set netport2 OEMHP_IPVersion=IPv4"
     PID37: "set netport2 OEMHP_InitiatorIP=192.168.22.146"
     PID38: "set netport2 OEMHP_InitiatorNetmask=255.255.192.0"
     PID39: "set netport2 OEMHP_InitiatorRoute=192.168.0.1"
     PID40: "set netport2 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst26-bay8"
     PID41: "set netport2 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1312:wpst26-bay8-bootvol"
     PID42: "set netport2 OEMHP_targetIP=192.168.21.71"
     PID43: "set netport2 OEMHP_targetPort=3260"
     PID44: "set netport2 OEMHP_LUN=0"
     PID45: "set netport2 OEMHP_authenticationMethod=CHAP"
     PID46: "set netport2 OEMHP_username="wpst26-bay8""
     PID47: "set netport2 OEMHP_secret=777073746870767365313233"
     PID48: "set netport2 OEMHP_LF2="D;;;;;;;disabled""
     PID49: "set netport2 OEMHP_LF3="D;;;;;;;disabled""
     PID02: "exit"
--------------------------------------
HP FlexFabric 10Gb 2-port 554FLB Adapter
Mezz=A (FLB=2) DevID=41h (off=0300h)
--------------------------------------
  FIP: 0 (off=031Ch)
     PID01: "set netport1 default"
     PID02: "exit"
  FIP: 1 (off=033Ch)
     PID01: "set netport2 default"
     PID02: "exit"
"""
}

# Profile4: ENC3 bay8
clp_profile4_one_bootable_connection_mezz = {
    "oa": PROFILE4_ENC_OA,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "8",
    "validate":
    """
--------------------------------------
HP FlexFabric 10Gb 2-port 554M Adapter
Mezz=1 DevID=4Eh (off=0300h)
--------------------------------------
  FIP: 0 (off=031Ch)
     PID01: "set netport1 default"
     PID32: "set netport1 OEMHP_CVNI=2001"
     PID33: "set netport1 OEMHP_FlowControl=function"
     PID34: "set netport1 OEMHP_LF0="E;1;A0B3CC1C2660;1000;0;0;disabled;disabled""
     PID35: "set netport1 OEMHP_LF1="I;1;A0B3CC1C2661;1001;2500;10000;enabled;enabled""
     PID36: "set netport1 OEMHP_IPVersion=IPv4"
     PID37: "set netport1 OEMHP_InitiatorIP=192.168.22.146"
     PID38: "set netport1 OEMHP_InitiatorNetmask=255.255.192.0"
     PID39: "set netport1 OEMHP_InitiatorRoute=192.168.0.1"
     PID40: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst26-bay8"
     PID41: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1312:wpst26-bay8-bootvol"
     PID42: "set netport1 OEMHP_targetIP=192.168.21.71"
     PID43: "set netport1 OEMHP_targetPort=3260"
     PID44: "set netport1 OEMHP_LUN=0"
     PID45: "set netport1 OEMHP_authenticationMethod=CHAP"
     PID46: "set netport1 OEMHP_username="wpst26-bay8""
     PID47: "set netport1 OEMHP_secret=777073746870767365313233"
     PID48: "set netport1 OEMHP_LF2="D;;;;;;;disabled""
     PID49: "set netport1 OEMHP_LF3="D;;;;;;;disabled""
     PID02: "exit"
  FIP: 1 (off=06D6h)
     PID01: "set netport2 default"
     PID32: "set netport2 OEMHP_CVNI=2001"
     PID33: "set netport2 OEMHP_FlowControl=function"
     PID34: "set netport2 OEMHP_LF0="E;1;A0B3CC1C2664;1000;0;0;disabled;disabled""
     PID35: "set netport2 OEMHP_LF1="I;1;A0B3CC1C2665;1001;0;0;disabled;disabled""
     PID36: "set netport2 OEMHP_LF2="D;;;;;;;disabled""
     PID37: "set netport2 OEMHP_LF3="D;;;;;;;disabled""
     PID02: "exit"
Blade 8 mezz 2: NOT FOUND
Blade 8 mezz 3: NOT FOUND
--------------------------------------
HP FlexFabric 10Gb 2-port 554FLB Adapter
Mezz=9 (FLB=1) DevID=40h (off=0300h)
--------------------------------------
  FIP: 0 (off=031Ch)
     PID01: "set netport1 default"
     PID02: "exit"
  FIP: 1 (off=033Ch)
     PID01: "set netport2 default"
     PID02: "exit"
--------------------------------------
HP FlexFabric 10Gb 2-port 554FLB Adapter
Mezz=A (FLB=2) DevID=41h (off=0300h)
--------------------------------------
  FIP: 0 (off=031Ch)
     PID01: "set netport1 default"
     PID02: "exit"
  FIP: 1 (off=033Ch)
     PID01: "set netport2 default"
     PID02: "exit"
"""
}

# Profile5: ENC2 bay1
clp_profile5_no_profile = {
    "oa": PROFILE5_ENC_OA,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "1",
    "validate":
    """
--------------------------------------
HP FlexFabric 10Gb 2-port 554FLB Adapter
Mezz=9 (FLB=1) DevID=40h (off=0300h)
--------------------------------------
  FIP: 0 (off=031Ch)
     PID01: "set netport1 default"
     PID02: "exit"
  FIP: 1 (off=033Ch)
     PID01: "set netport2 default"
     PID02: "exit"
"""}

# Profile5: ENC2 bay1
clp_profile5_one_bootable_connection = {
    "oa": PROFILE5_ENC_OA,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "1",
    "validate":
    """
--------------------------------------
HP FlexFabric 10Gb 2-port 554FLB Adapter
Mezz=9 (FLB=1) DevID=40h (off=0300h)
--------------------------------------
  FIP: 0 (off=031Ch)
     PID01: "set netport1 default"
     PID32: "set netport1 OEMHP_CVNI=2001"
     PID33: "set netport1 OEMHP_FlowControl=function"
     PID34: "set netport1 OEMHP_LF0="E;1;D89D6773C010;1000;0;0;disabled;disabled""
     PID35: "set netport1 OEMHP_LF1="I;1;D89D6773C011;1001;2500;10000;enabled;enabled""
     PID36: "set netport1 OEMHP_IPVersion=IPv4"
     PID37: "set netport1 OEMHP_InitiatorIP=192.168.22.148"
     PID38: "set netport1 OEMHP_InitiatorNetmask=255.255.192.0"
     PID39: "set netport1 OEMHP_InitiatorRoute=192.168.0.1"
     PID40: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst23-bay1"
     PID41: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1315:wpst23-bay1-bootvol"
     PID42: "set netport1 OEMHP_targetIP=192.168.21.71"
     PID43: "set netport1 OEMHP_targetPort=3260"
     PID44: "set netport1 OEMHP_LUN=0"
     PID45: "set netport1 OEMHP_authenticationMethod=None"
     PID46: "set netport1 OEMHP_LF2="D;;;;;;;disabled""
     PID47: "set netport1 OEMHP_LF3="D;;;;;;;disabled""
     PID02: "exit"
  FIP: 1 (off=0675h)
     PID01: "set netport2 default"
     PID32: "set netport2 OEMHP_CVNI=2001"
     PID33: "set netport2 OEMHP_FlowControl=function"
     PID34: "set netport2 OEMHP_LF0="E;1;D89D6773C014;1000;0;0;disabled;disabled""
     PID35: "set netport2 OEMHP_LF1="I;1;D89D6773C015;1001;0;0;disabled;disabled""
     PID36: "set netport2 OEMHP_LF2="D;;;;;;;disabled""
     PID37: "set netport2 OEMHP_LF3="D;;;;;;;disabled""
     PID02: "exit"
"""
}

# Profile6: ENC3 bay3
clp_profile6_no_profile = {
    "oa": PROFILE6_ENC_OA,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "3",
    "validate":
    """
--------------------------------------
HP FlexFabric 10Gb 2-port 554M Adapter
Mezz=1 DevID=4Eh (off=0300h)
--------------------------------------
  FIP: 0 (off=031Ch)
     PID01: "set netport1 default"
     PID02: "exit"
  FIP: 1 (off=033Ch)
     PID01: "set netport2 default"
     PID02: "exit"
--------------------------------------
HP LPe1205A 8Gb FC HBA for BladeSystem c-Class
Mezz=2 DevID=4Ch (off=0200h)
--------------------------------------
  FIP: 0 (off=021Ch)
     PID01: "set netport0 default"
     PID02: "set netport0 OEMHP_hss=1416"
     PID03: "set netport1 default"
     PID04: "set netport1 OEMHP_hss=1411"
     PID05: "exit"
--------------------------------------
HP FlexFabric 10Gb 2-port 554FLB Adapter
Mezz=9 (FLB=1) DevID=40h (off=0300h)
--------------------------------------
  FIP: 0 (off=031Ch)
     PID01: "set netport1 default"
     PID02: "exit"
  FIP: 1 (off=033Ch)
     PID01: "set netport2 default"
     PID02: "exit"
"""
}

# Profile6: ENC3 bay3
clp_profile6_two_bootable_connections = {
    "oa": PROFILE6_ENC_OA,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "3",
    "validate":
    """
--------------------------------------
HP FlexFabric 10Gb 2-port 554M Adapter
Mezz=1 DevID=4Eh (off=0300h)
--------------------------------------
  FIP: 0 (off=031Ch)
     PID01: "set netport1 default"
     PID32: "set netport1 OEMHP_CVNI=2001"
     PID33: "set netport1 OEMHP_FlowControl=function"
     PID34: "set netport1 OEMHP_LF0="E;1;A0B3CC1C5060;1000;0;0;disabled;disabled""
     PID35: "set netport1 OEMHP_LF1="I;1;A0B3CC1C5061;1001;2500;10000;enabled;enabled""
     PID36: "set netport1 OEMHP_IPVersion=IPv4"
     PID37: "set netport1 OEMHP_InitiatorIP=192.168.22.150"
     PID38: "set netport1 OEMHP_InitiatorNetmask=255.255.192.0"
     PID39: "set netport1 OEMHP_InitiatorRoute=192.168.0.1"
     PID40: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst26-bay3"
     PID41: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1321:wpst26-bay3-bootvol"
     PID42: "set netport1 OEMHP_targetIP=192.168.21.71"
     PID43: "set netport1 OEMHP_targetPort=3260"
     PID44: "set netport1 OEMHP_LUN=0"
     PID45: "set netport1 OEMHP_authenticationMethod=CHAP"
     PID46: "set netport1 OEMHP_username="wpst26-bay3""
     PID47: "set netport1 OEMHP_secret=777073746870767365313233"
     PID48: "set netport1 OEMHP_LF2="D;;;;;;;disabled""
     PID49: "set netport1 OEMHP_LF3="D;;;;;;;disabled""
     PID02: "exit"
  FIP: 1 (off=06D6h)
     PID01: "set netport2 default"
     PID32: "set netport2 OEMHP_CVNI=2001"
     PID33: "set netport2 OEMHP_FlowControl=function"
     PID34: "set netport2 OEMHP_LF0="E;1;A0B3CC1C5064;1000;0;0;disabled;disabled""
     PID35: "set netport2 OEMHP_LF1="I;1;A0B3CC1C5065;1001;2500;10000;enabled;enabled""
     PID36: "set netport2 OEMHP_IPVersion=IPv4"
     PID37: "set netport2 OEMHP_InitiatorIP=192.168.22.151"
     PID38: "set netport2 OEMHP_InitiatorNetmask=255.255.192.0"
     PID39: "set netport2 OEMHP_InitiatorRoute=192.168.0.1"
     PID40: "set netport2 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst26-bay3"
     PID41: "set netport2 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1321:wpst26-bay3-bootvol"
     PID42: "set netport2 OEMHP_targetIP=192.168.21.71"
     PID43: "set netport2 OEMHP_targetPort=3260"
     PID44: "set netport2 OEMHP_LUN=0"
     PID45: "set netport2 OEMHP_authenticationMethod=CHAP"
     PID46: "set netport2 OEMHP_username="wpst26-bay3""
     PID47: "set netport2 OEMHP_secret=777073746870767365313233"
     PID48: "set netport2 OEMHP_LF2="D;;;;;;;disabled""
     PID49: "set netport2 OEMHP_LF3="D;;;;;;;disabled""
     PID02: "exit"
--------------------------------------
HP LPe1205A 8Gb FC HBA for BladeSystem c-Class
Mezz=2 DevID=4Ch (off=0200h)
--------------------------------------
  FIP: 0 (off=021Ch)
     PID01: "set netport0 default"
     PID02: "set netport0 OEMHP_hss=1416"
     PID03: "set netport1 default"
     PID04: "set netport1 OEMHP_hss=1411"
     PID05: "exit"
--------------------------------------
HP FlexFabric 10Gb 2-port 554FLB Adapter
Mezz=9 (FLB=1) DevID=40h (off=0300h)
--------------------------------------
  FIP: 0 (off=031Ch)
     PID01: "set netport1 default"
     PID02: "exit"
  FIP: 1 (off=033Ch)
     PID01: "set netport2 default"
     PID02: "exit"
"""
}

# Profile7: ENC2 bay5
clp_profile7_no_profile = {
    "oa": PROFILE7_ENC_OA,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "5",
    "validate":
    """
--------------------------------------
HP FlexFabric 10Gb 2-port 534M Adapter
Mezz=1 DevID=4Eh (off=0300h)
--------------------------------------
  FIP: 0 (off=031Ch)
     PID01: "set netport1 default"
     PID02: "exit"
  FIP: 1 (off=033Ch)
     PID01: "set netport1 default"
     PID02: "exit"
--------------------------------------
HP LPe1605 16Gb FC HBA for BladeSystem c-Class
Mezz=2 DevID=4Ch (off=0200h)
--------------------------------------
  FIP: 0 (off=021Ch)
     PID01: "set netport0 default"
     PID02: "set netport0 OEMHP_hss=3413"
     PID03: "set netport1 default"
     PID04: "set netport1 OEMHP_hss=3413"
     PID05: "exit"
--------------------------------------
HP FlexFabric 20Gb 2-port 650FLB Adapter
Mezz=9 (FLB=1) DevID=40h (off=0300h)
--------------------------------------
  FIP: 0 (off=031Ch)
     PID01: "set netport1 default"
     PID02: "exit"
  FIP: 1 (off=033Ch)
     PID01: "set netport2 default"
     PID02: "exit"
"""
}

# Profile7: ENC2 bay5
clp_profile7_two_bootable_connections = {
    "oa": PROFILE7_ENC_OA,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "5",
    "validate":
    """
--------------------------------------
HP FlexFabric 10Gb 2-port 534M Adapter
Mezz=1 DevID=4Eh (off=0300h)
--------------------------------------
  FIP: 0 (off=031Ch)
     PID01: "set netport1 default"
     PID32: "set netport1 OEMHP_CVNI=2001"
     PID33: "set netport1 OEMHP_FlowControl=function"
     PID34: "set netport1 OEMHP_LF0="E;1;2C44FD8D2650;1000;0;0;disabled;disabled""
     PID35: "set netport1 OEMHP_LF1="I;1;2C44FD8D2651;1001;2500;10000;enabled;enabled""
     PID36: "set netport1 OEMHP_IPVersion=IPv4"
     PID37: "set netport1 OEMHP_InitiatorIP=192.168.22.152"
     PID38: "set netport1 OEMHP_InitiatorNetmask=255.255.192.0"
     PID39: "set netport1 OEMHP_InitiatorRoute=192.168.0.1"
     PID40: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst23-bay5"
     PID41: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1324:wpst23-bay5-bootvol"
     PID42: "set netport1 OEMHP_targetIP=192.168.21.71"
     PID43: "set netport1 OEMHP_targetPort=3260"
     PID44: "set netport1 OEMHP_LUN=0"
     PID45: "set netport1 OEMHP_authenticationMethod=None"
     PID46: "set netport1 OEMHP_LF2="D;;;;;;;disabled""
     PID47: "set netport1 OEMHP_LF3="D;;;;;;;disabled""
     PID02: "exit"
  FIP: 1 (off=0675h)
     PID01: "set netport1 default"
     PID32: "set netport1 OEMHP_CVNI=2001"
     PID33: "set netport1 OEMHP_FlowControl=function"
     PID34: "set netport1 OEMHP_LF0="E;1;2C44FD8D2654;1000;0;0;disabled;disabled""
     PID35: "set netport1 OEMHP_LF1="I;1;2C44FD8D2655;1001;2500;10000;enabled;enabled""
     PID36: "set netport1 OEMHP_IPVersion=IPv4"
     PID37: "set netport1 OEMHP_InitiatorIP=192.168.22.153"
     PID38: "set netport1 OEMHP_InitiatorNetmask=255.255.192.0"
     PID39: "set netport1 OEMHP_InitiatorRoute=192.168.0.1"
     PID40: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst23-bay5"
     PID41: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1324:wpst23-bay5-bootvol"
     PID42: "set netport1 OEMHP_targetIP=192.168.21.71"
     PID43: "set netport1 OEMHP_targetPort=3260"
     PID44: "set netport1 OEMHP_LUN=0"
     PID45: "set netport1 OEMHP_authenticationMethod=None"
     PID46: "set netport1 OEMHP_LF2="D;;;;;;;disabled""
     PID47: "set netport1 OEMHP_LF3="D;;;;;;;disabled""
     PID02: "exit"
--------------------------------------
HP LPe1605 16Gb FC HBA for BladeSystem c-Class
Mezz=2 DevID=4Ch (off=0200h)
--------------------------------------
  FIP: 0 (off=021Ch)
     PID01: "set netport0 default"
     PID02: "set netport0 OEMHP_hss=3413"
     PID03: "set netport1 default"
     PID04: "set netport1 OEMHP_hss=3413"
     PID05: "exit"
--------------------------------------
HP FlexFabric 20Gb 2-port 650FLB Adapter
Mezz=9 (FLB=1) DevID=40h (off=0300h)
--------------------------------------
  FIP: 0 (off=031Ch)
     PID01: "set netport1 default"
     PID02: "exit"
  FIP: 1 (off=033Ch)
     PID01: "set netport2 default"
     PID02: "exit"
"""
}
# profile8: ENC1 bay14
clp_profile8_one_unbootable_connection = {
    "oa": PROFILE8_ENC_OA,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "14",
    "validate":
    """
--------------------------------------
HP FlexFabric 10Gb 2-port 536FLB Adapter
Mezz=9 (FLB=1) DevID=40h (off=0300h)
--------------------------------------
  FIP: 0 (off=031Ch)
     PID01: "set netport1 default"
     PID32: "set netport1 OEMHP_CVNI=2001"
     PID33: "set netport1 OEMHP_FlowControl=function"
     PID34: "set netport1 OEMHP_LF0="E;1;FC15B425C3C8;1000;0;0;disabled;disabled""
     PID35: "set netport1 OEMHP_LF1="I;1;FC15B425C3C9;1001;0;0;disabled;disabled""
     PID36: "set netport1 OEMHP_LF2="D;;;;;;;disabled""
     PID37: "set netport1 OEMHP_LF3="D;;;;;;;disabled""
     PID02: "exit"
  FIP: 1 (off=046Bh)
     PID01: "set netport2 default"
     PID32: "set netport2 OEMHP_CVNI=2001"
     PID33: "set netport2 OEMHP_FlowControl=function"
     PID34: "set netport2 OEMHP_LF0="E;1;FC15B425C3CC;1000;0;0;disabled;disabled""
     PID35: "set netport2 OEMHP_LF1="I;1;FC15B425C3CD;1001;2500;10000;disabled;enabled""
     PID36: "set netport2 OEMHP_LF2="D;;;;;;;disabled""
     PID37: "set netport2 OEMHP_LF3="D;;;;;;;disabled""
     PID02: "exit"
"""
}
# profile8: ENC1 bay14
clp_profile8_one_bootable_connection = {
    "oa": PROFILE8_ENC_OA,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "14",
    "validate":
    """
--------------------------------------
HP FlexFabric 10Gb 2-port 536FLB Adapter
Mezz=9 (FLB=1) DevID=40h (off=0300h)
--------------------------------------
  FIP: 0 (off=031Ch)
     PID01: "set netport1 default"
     PID32: "set netport1 OEMHP_CVNI=2001"
     PID33: "set netport1 OEMHP_FlowControl=function"
     PID34: "set netport1 OEMHP_LF0="E;1;5CB901C761F0;1000;0;0;disabled;disabled""
     PID35: "set netport1 OEMHP_LF1="I;1;5CB901C761F1;1001;0;0;disabled;disabled""
     PID36: "set netport1 OEMHP_LF2="D;;;;;;;disabled""
     PID37: "set netport1 OEMHP_LF3="D;;;;;;;disabled""
     PID02: "exit"
  FIP: 1 (off=046Bh)
     PID01: "set netport1 default"
     PID32: "set netport1 OEMHP_CVNI=2001"
     PID33: "set netport1 OEMHP_FlowControl=function"
     PID34: "set netport1 OEMHP_LF0="E;1;5CB901C761F8;1000;0;0;disabled;disabled""
     PID35: "set netport1 OEMHP_LF1="I;1;5CB901C761F9;1001;2500;10000;enabled;enabled""
     PID36: "set netport1 OEMHP_IPVersion=IPv4"
     PID37: "set netport1 OEMHP_InitiatorIP=192.168.22.140"
     PID38: "set netport1 OEMHP_InitiatorNetmask=255.255.192.0"
     PID39: "set netport1 OEMHP_InitiatorRoute=192.168.0.1"
     PID40: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst22-bay14"
     PID41: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:6927:wpst22-bay1-win2016-bootvol"
     PID42: "set netport1 OEMHP_targetIP=192.168.21.71"
     PID43: "set netport1 OEMHP_targetPort=3260"
     PID44: "set netport1 OEMHP_LUN=0"
     PID45: "set netport1 OEMHP_authenticationMethod=MutualCHAP"
     PID46: "set netport1 OEMHP_username="wpst22-bay1""
     PID47: "set netport1 OEMHP_secret=777073746870767365313233"
     PID48: "set netport1 OEMHP_MutualUsername="wpst22-bay1""
     PID49: "set netport1 OEMHP_mutualSecret=687076736531323377707374"
     PID50: "set netport1 OEMHP_LF2="D;;;;;;;disabled""
     PID51: "set netport1 OEMHP_LF3="D;;;;;;;disabled""
     PID02: "exit"
"""
}


CLP_after_create = [clp_profile1_one_unbootable_connection.copy(),
                    clp_profile2_two_bootable_connections.copy(),
                    clp_profile3_one_bootable_connection.copy(),
                    clp_profile4_one_bootable_connection_lom.copy(),
                    ]
CLP_after_create_gen10 = [clp_profile8_one_bootable_connection.copy(), ]

CLP_after_edit = [clp_profile1_one_bootable_connection.copy(),
                  clp_profile2_one_bootable_connection.copy(),
                  clp_profile3_two_bootable_connections.copy(),
                  clp_profile4_one_bootable_connection_mezz.copy()]

CLP_after_move = [clp_profile5_one_bootable_connection.copy(),
                  clp_profile6_two_bootable_connections.copy(),
                  clp_profile7_two_bootable_connections.copy()]

CLP_after_delete = [clp_profile1_no_profile.copy(),
                    clp_profile5_no_profile.copy(),
                    clp_profile6_no_profile.copy(),
                    clp_profile2_no_profile.copy(),
                    clp_profile3_no_profile.copy(),
                    clp_profile4_no_profile.copy(),
                    clp_profile7_no_profile.copy(),
                    ]

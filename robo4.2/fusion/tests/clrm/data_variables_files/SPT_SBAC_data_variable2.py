"""
SPT  automation data variable file
"""

import copy

fortcollins_setup = {}
fortcollins_setup["Enc2"] = {"ServerHardware": ["pulsarwpst-enc2, bay 2", "pulsarwpst-enc2, bay 4"],
                             "ServerHardwareType": ["BL460c Gen8 1", "BL460c Gen8 1"]}
fortcollins_setup["Enc4"] = {"ServerHardware": ["pulsarwpst-enc4, bay 2", "pulsarwpst-enc4, bay 6"],
                             "ServerHardwareType": ["BL460c Gen8 1", "BL460c Gen8 1"]}
fortcollins_setup["Enc5"] = {"ServerHardware": ["pulsarwpst-enc5, bay 1", "pulsarwpst-enc5, bay 2"],
                             "ServerHardwareType": ["BL460c Gen8 1", "BL460c Gen8 1"]}
fortcollins_setup["Storage"] = {"StoragePool": "orionwpstR0",
                                "VolumeStorageSystem": "pulsarwpst3par1-srv"}
fortcollins_setup["Firmware"] = {"Firmware": "Service Pack for ProLiant",
                                 "Version": "2015.09.0",
                                 "Version2": "2017.03.27.06"}

local_setup = {}
local_setup["Hyderabad"] = {"ServerHardware": ["HYDERABAD, bay 2", "HYDERABAD, bay 3", "HYDERABAD, bay 7"],
                            "ServerHardwareType": ["BL460c Gen8 1", "BL460c Gen9 1"]}
local_setup["Storage"] = {"StoragePool": "QA_test_R5",
                          "VolumeStorageSystem": "test"}
local_setup["Firmware"] = {"Firmware": "Service Pack for ProLiant",
                           "Version": "Gen8.1",
                           "Version2": "Gen8.1"}

dcs_c7k_setup = {}
dcs_c7k_setup["Enc"] = {"ServerHardware": ["Encl1, bay 3", "Encl1, bay 4", "Encl1, bay 5", "Encl1, bay 6",
                                           "Encl1, bay 7", "Encl1, bay 8", "Encl1, bay 11", "Encl1, bay 12",
                                           "Encl1, bay 13", "Encl1, bay 14", "Encl1, bay 15", "Encl1, bay 16",
                                           "Encl2, bay 3", "Encl2, bay 4", "Encl2, bay 5", "Encl2, bay 6"],
                        "ServerHardwareType": ["BL460c Gen8 1", "BL660c Gen8 1"]}
dcs_c7k_setup["Storage"] = {"StoragePool": "cpg-growth-limit-1TiB",
                            "VolumeStorageSystem": "ThreePAR-1"}
dcs_c7k_setup["Firmware"] = {"Firmware": "Service Pack for ProLiant",
                             "Version": "Gen8.1",
                             "Version2": "Gen8.1"}
svol = {"svol1": "svol1", "svol2": "svol2", "svol3": "svol3", "svol4": "svol4", "svol5": "svol5", "svol6": "svol6"}

network = {"mgmt": "corp",
           "general1": "icsp",
           "general2": "corp1",
           "tunnel": "tunneled_nw",
           "vmotion1": "net1",
           "vmotion2": "network2",
           "untagged": "untagged_nw",
           "ft": "ft_net",
           "ft2": "ft_net2",
           "production": "production",
           "iscsi": "iSCSI",
           "fc1": "san",
           "ns1": "netset1",
           "ns2": "netset2"}

# ===============================================================================
# To enable dynamic payload for  OVF1053 & 3651
# ===============================================================================
Consistency_Check_Hardware = {"Checked": {"SHT": dcs_c7k_setup["Enc"]["ServerHardwareType"],
                                          "SH": dcs_c7k_setup["Enc"]["ServerHardware"][0:3]},
                              "Unchecked": {"SHT": dcs_c7k_setup["Enc"]["ServerHardwareType"],
                                            "SH": dcs_c7k_setup["Enc"]["ServerHardware"][3:6]},
                              "CheckedMinimumChecked": {"SHT": dcs_c7k_setup["Enc"]["ServerHardwareType"],
                                                        "SH": dcs_c7k_setup["Enc"]["ServerHardware"][6:9]},
                              "CheckedMinimumUnchecked": {"SHT": dcs_c7k_setup["Enc"]["ServerHardwareType"],
                                                          "SH": dcs_c7k_setup["Enc"]["ServerHardware"][9:12]},
                              "NoCheck": {"SHT": dcs_c7k_setup["Enc"]["ServerHardwareType"],
                                          "SH": dcs_c7k_setup["Enc"]["ServerHardware"][12:]}}
server_info = {}
server_info["Enc"] = {"ServerHardware": ["SH1", "SH2", "SH3"],
                      "ServerHardwareType": ["SHT1", "SHT2"], "enclgrp": ["enclgrp", "enclgrp1"]}

# ===============================================================================
#  resources and field used in SPT SP test cases
# ===============================================================================
setup = {"dcs": dcs_c7k_setup["Enc"],
         "fortcollins_Enc2": fortcollins_setup["Enc2"],
         "fortcollins_Enc4": fortcollins_setup["Enc4"],
         "fortcollins_Enc5": fortcollins_setup["Enc5"],
         "Hyderabad": local_setup["Hyderabad"],
         "consistency_check_feature": server_info["Enc"]
         }

resourcesForsetup = {
    "dcs": dcs_c7k_setup,
    "fortcollins_Enc2": fortcollins_setup,
    "fortcollins_Enc4": fortcollins_setup,
    "fortcollins_Enc5": fortcollins_setup,
    "Hyderabad": local_setup,
    "consistency_check_feature": dcs_c7k_setup}

# ===============================================================================
# Choose the setup on which regression test suite need to be executed
# setupName can be "dcs"
#                  "fortcollins_Enc2"
#                  "fortcollins_Enc4"
#                  "fortcollins_Enc5",
#                  "consistency_check_feature"
# ===============================================================================
# setupName = "Hyderabad"
# setupName = "dcs"
setupName = "consistency_check_feature"
adminPassword = "admin123"
OtherUserPassword = "vsbqa*help"
enclgrps = ["enclgrp", "enclgrp1"]
ServerProfileTemplate_type = "ServerProfileTemplateV6"
ServerProfile_type = "ServerProfileV10"
Firmware = resourcesForsetup[setupName]["Firmware"]["Firmware"]
FirmwareVersion = resourcesForsetup[setupName]["Firmware"]["Version"]
FirmwareVersion2 = resourcesForsetup[setupName]["Firmware"]["Version2"]
StoragePool1 = "SP:" + resourcesForsetup[setupName]["Storage"]["StoragePool"]
TemplateUri1 = "ROOT:" + resourcesForsetup[setupName]["Storage"]["StoragePool"]
VolumeStorageSystemUri1 = "SSYS:" + resourcesForsetup[setupName]["Storage"]["VolumeStorageSystem"]
ServerHardwareType = ["SHT:" + setup[setupName]["ServerHardwareType"][0], "SHT:" + setup[setupName]["ServerHardwareType"][1]]
ServerHardware = setup[setupName]["ServerHardware"]

Scope1_ServerHardware = ["SH:" + setup[setupName]["ServerHardware"][0], "SH:" + setup[setupName]["ServerHardware"][1]]
Scope3_ServerHardware = ["SH:" + setup[setupName]["ServerHardware"][1], "SH:" + setup[setupName]["ServerHardware"][2]]
Scope1_StoragePool_1 = "SPOOL:" + resourcesForsetup[setupName]["Storage"]["StoragePool"]
Scope3_StoragePool_1 = Scope1_StoragePool_1

# ===============================================================================
# User's scopes and roles
# ===============================================================================
users_with_scope = {
    "User1_NetAdmin": {"Network administrator": [None]},
    "User1": {"Infrastructure administrator": ["Scope1"]},
    "User1_SPArch": {"Server profile architect": ["Scope1"]},
    "User5_SPArch": {"Server profile architect": ["Scope1", "Scope3"]},
    "User6_InfraAdm": {"Infrastructure administrator": ["Scope1", "Scope3"]},
    "User7_SPArch": {"Server profile architect": ["Scope1", "Scope2", "Scope3", "Scope5"]},
    "User7_SPAdm": {"Server profile administrator": ["Scope3"]},
    "User7_ServAdm": {"Server administrator": ["Scope3"]},
    "User8_SPArch": {"Server profile architect": ["Scope1", "Scope2", "Scope3"]},
    "User9_StorAdm": {"Storage administrator": ["Scope2"]},
    "User10_SPAdm": {"Server profile administrator": ["Scope1", "Scope2", "Scope3", "Scope4"]},
    "User11_SPArch": {"Server profile architect": ["Scope1"],
                      "Server administrator": ["Scope4"]},
    "User12_SPArch": {"Server profile architect": ["Scope5"]},
    "User13_SPArch": {"Server profile architect": ["Scope6"]},
    "User14_SPArch": {"Server profile architect": ["Scope5"],
                      "Server administrator": ["Scope6"]}}

# ===============================================================================
#  user_cred  model generates user credential payload
# ===============================================================================


def user_cred():
    """
    user_cred  model generates user credential payload
    """
    user_cred_payload = {}
    user_cred_payload["Administrator"] = {"userName": "Administrator", "password": adminPassword, "authLoginDomain": "LOCAL", "loginMsgAck": None}
    for user in users_with_scope:
        user_cred_payload[user] = {"userName": user, "password": OtherUserPassword, "authLoginDomain": "LOCAL", "loginMsgAck": None}
    return user_cred_payload

# ===============================================================================
# initialScopeForUsers module generates payload for creating  scope and role for users
# ===============================================================================


def initialScopeForUsers():
    """
    initialScopeForUsers module generates payload for creating  scope and role for users
    """
    users_payload = []
    for user in users_with_scope:
        users_payload.append({"type": "UserAndPermissions", "userName": user, "fullName": "", "password": OtherUserPassword, "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True,
                              "permissions": [{"roleName": "Read only", "scopeUri": None}]})
    return users_payload

# ===============================================================================
# updateUserWithScope module generates payload to update user with new scope and role
# ===============================================================================


def updateUserWithScope():
    """
    updateUserWithScope module generates payload to update user with new scope and role
    """
    update_users_payload = []
    for user in users_with_scope:
        user_payload = {"type": "UserAndPermissions", "userName": user, "permissions": []}
        permissions = []
        for role in users_with_scope[user]:
            for scope in users_with_scope[user][role]:
                scope_payload = {"roleName": role, "scopeUri": scope}
                permissions.append(scope_payload)
        user_payload["permissions"] = permissions
        update_users_payload.append(user_payload)
    return update_users_payload


def usersScopeSettings():
    """
    usersScopeSettings module generates payload to update user with new scope and role
    """
    user_scopes = {"Administrator": []}
    for user in users_with_scope:
        scopesUniq = []
        for role in users_with_scope[user]:
            scopes_lst = users_with_scope[user][role]
            for scope in scopes_lst:
                if scope not in scopesUniq:
                    scopesUniq.append(scope)
        user_scopes[user] = scopesUniq
    return user_scopes


user_credentials = user_cred()
users = initialScopeForUsers()
user_scope = usersScopeSettings()
update_users = updateUserWithScope()

scopes = [{"name": "Scope1",
           "description": "",
           "type": "ScopeV3",
           "addedResourceUris": ["ETH:" + network["general1"], "ETH:" + network["mgmt"], "FC:" + network["fc1"], "ETH:" + network["production"], "ETH:" + network["tunnel"],
                                 "ETH:" + network["ft"], Scope1_ServerHardware[0], Scope1_ServerHardware[1], "ETH:" + network["vmotion1"], "NS:" + network["ns1"],
                                 "SVOL:" + svol["svol1"], "SVOL:" + svol["svol2"], "SVOL:" + svol["svol3"], "SVOL:" + svol["svol4"], Scope1_StoragePool_1, "firmware-baselines:" + Firmware],
           "removedResourceUris": []
           },
          {"name": "Scope2",
           "description": "",
           "type": "ScopeV3",
           "addedResourceUris": [],
           "removedResourceUris": []
           },
          {"name": "Scope3",
           "description": "",
           "type": "ScopeV3",
           "addedResourceUris": ["ETH:" + network["general1"], "ETH:" + network["mgmt"], "FC:" + network["fc1"], "ETH:" + network["production"],
                                 "ETH:" + network["untagged"], "ETH:" + network["ft2"], Scope3_ServerHardware[0], Scope3_ServerHardware[1], "ETH:" + network["vmotion1"],
                                 "NS:" + network["ns1"], "NS:" + network["ns2"], "SVOL:" + svol["svol1"], "SVOL:" + svol["svol2"], "SVOL:" + svol["svol5"], "SVOL:" + svol["svol6"],
                                 Scope3_StoragePool_1, "firmware-baselines:" + Firmware],
           "removedResourceUris": []
           },
          {"name": "Scope4",
           "description": "",
           "type": "ScopeV3",
           "addedResourceUris": ["ETH:" + network["general1"], "ETH:" + network["mgmt"], "FC:" + network["fc1"], "ETH:" + network["production"],
                                 "ETH:" + network["untagged"], "ETH:" + network["ft2"], Scope3_ServerHardware[0], Scope3_ServerHardware[1], "ETH:" + network["vmotion1"],
                                 "NS:" + network["ns1"], "NS:" + network["ns2"], "SVOL:" + svol["svol5"], "SVOL:" + svol["svol6"], Scope3_StoragePool_1],
           "removedResourceUris": []
           },
          {"name": "Scope5",
           "description": "",
           "type": "ScopeV3",
           "addedResourceUris": ["ETH:" + network["general1"], "ETH:" + network["mgmt"], "FC:" + network["fc1"], "ETH:" + network["production"],
                                 "ETH:" + network["untagged"], "ETH:" + network["ft2"], Scope3_ServerHardware[0], Scope3_ServerHardware[1], "ETH:" + network["vmotion1"],
                                 "NS:" + network["ns1"], "NS:" + network["ns2"], "SVOL:" + svol["svol1"], "SVOL:" + svol["svol2"], Scope3_StoragePool_1],
           "removedResourceUris": []
           },
          {"name": "Scope6",
           "description": "",
           "type": "ScopeV3",
           "addedResourceUris": ["ETH:" + network["general1"], "ETH:" + network["mgmt"], "FC:" + network["fc1"], "ETH:" + network["untagged"],
                                 "ETH:" + network["ft2"], Scope3_ServerHardware[1], "ETH:" + network["vmotion1"], "SVOL:" + svol["svol5"], "SVOL:" + svol["svol6"],
                                 Scope3_StoragePool_1],
           "removedResourceUris": []
           }
          ]

# ===============================================================================
#  SPT and SP payload Template used in test cases
# ===============================================================================

SPT_payload_without_net = {"name": "ServerProfileTemplate", "type": ServerProfileTemplate_type, "serverProfileDescription": "", "serverHardwareTypeUri": ServerHardwareType[0],
                           "enclosureGroupUri": "EG:" + enclgrps[0], "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "description": "",
                           "affinity": "Bay", "connectionSettings": {"manageConnections": False},
                           "boot": {"manageBoot": True, "order": ["CD", "Floppy", "USB", "HardDisk", "PXE"]},
                           "bootMode": None,
                           "firmware": {"manageFirmware": False, "firmwareBaselineUri": "", "forceInstallFirmware": False, "firmwareInstallType": None},
                           "bios": {"manageBios": False, "overriddenSettings": []},
                           "hideUnusedFlexNics": True, "iscsiInitiatorNameType": "AutoGenerated",
                           "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {"hostOSType": "VMware (ESXi)", "manageSanStorage": False, "volumeAttachments": []}
                           }

SPT_payload_with_net = {"name": "ServerProfileTemplate", "type": ServerProfileTemplate_type, "serverProfileDescription": "", "serverHardwareTypeUri": ServerHardwareType[0],
                        "enclosureGroupUri": "EG:" + enclgrps[0], "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "description": "", "affinity": "Bay",
                        "connectionSettings": {"manageConnections": True,
                                               "connections": [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                                "networkUri": "ETH:" + network["general1"]},
                                                               {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                                "networkUri": "ETH:" + network["mgmt"]},
                                                               {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500",
                                                                "networkUri": "FC:" + network["fc1"]},
                                                               {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                                "networkUri": "ETH:" + network["production"]},
                                                               {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                                "networkUri": "ETH:" + network["production"]}
                                                               ]
                                               },
                        "boot": {"manageBoot": True, "order": ["CD", "Floppy", "USB", "HardDisk", "PXE"]},
                        "bootMode": None,
                        "firmware": {"manageFirmware": False, "firmwareBaselineUri": "", "forceInstallFirmware": False, "firmwareInstallType": None},
                        "bios": {"manageBios": False, "overriddenSettings": []},
                        "hideUnusedFlexNics": True, "iscsiInitiatorNameType": "AutoGenerated",
                        "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {"hostOSType": "VMware (ESXi)", "manageSanStorage": False, "volumeAttachments": []}
                        }
SPT_payload_with_vol = {"name": "ServerProfileTemplate", "type": ServerProfileTemplate_type, "serverProfileDescription": "", "serverHardwareTypeUri": ServerHardwareType[0],
                        "enclosureGroupUri": "EG:" + enclgrps[0], "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "description": "", "affinity": "Bay",
                        "connectionSettings": {"manageConnections": True,
                                               "connections": [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                                "networkUri": "ETH:" + network["general1"]},
                                                               {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                                "networkUri": "ETH:" + network["mgmt"]},
                                                               {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500",
                                                                "networkUri": "FC:" + network["fc1"], "boot": {"priority": "Primary", "bootVolumeSource": "ManagedVolume"}},
                                                               {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                                "networkUri": "ETH:" + network["production"]},
                                                               {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                                "networkUri": "ETH:" + network["production"]}
                                                               ]
                                               },
                        "boot": {"manageBoot": True, "order": ["CD", "Floppy", "USB", "HardDisk", "PXE"]},
                        "bootMode": None,
                        "firmware": {"manageFirmware": False, "firmwareBaselineUri": "", "forceInstallFirmware": False, "firmwareInstallType": None},
                        "bios": {"manageBios": False, "overriddenSettings": []},
                        "hideUnusedFlexNics": True, "iscsiInitiatorNameType": "AutoGenerated",
                        "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {"hostOSType": "VMware (ESXi)", "manageSanStorage": True, "volumeAttachments": []}
                        }
sanStorage_payload = {"hostOSType": "VMware (ESXi)", "manageSanStorage": True,
                      "volumeAttachments": []}

SP_payload = {"name": "ServerProfileTemplate_SP", "serverHardwareUri": ServerHardware[0], "enclosureGroupUri": "EG:" + enclgrps[0], "type": ServerProfile_type,
              "connectionSettings": {
                  "connections": [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:" + network["general1"]},
                                  {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:" + network["mgmt"]},
                                  {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:" + network["fc1"]},
                                  {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:" + network["production"]},
                                  {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:" + network["production"]}
                                  ]},
              "boot": {"manageBoot": True, "order": ["CD", "Floppy", "USB", "HardDisk", "PXE"]},
              "bootMode": None,
              "firmware": {"manageFirmware": False, "firmwareBaselineUri": "", "forceInstallFirmware": False, "firmwareInstallType": None},
              "bios": {"manageBios": False, "overriddenSettings": []},
              "hideUnusedFlexNics": True, "iscsiInitiatorNameType": "AutoGenerated",
              "localStorage": {"sasLogicalJBODs": [], "controllers": []}}

SP_payload_with_vol = {"name": "ServerProfileTemplate_SP", "serverHardwareUri": ServerHardware[0], "enclosureGroupUri": "EG:" + enclgrps[0], "type": ServerProfile_type,
                       "connectionSettings": {
                           "connections": [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:" + network["general1"]},
                                           {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:" + network["mgmt"]},
                                           {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:" + network["fc1"],
                                            "boot": {"priority": "Primary", "bootVolumeSource": "ManagedVolume"}},
                                           {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:" + network["production"]},
                                           {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:" + network["production"]}
                                           ]},
                       "boot": {"manageBoot": True, "order": ["CD", "Floppy", "USB", "HardDisk", "PXE"]},
                       "bootMode": None,
                       "firmware": {"manageFirmware": False, "firmwareBaselineUri": "", "forceInstallFirmware": False, "firmwareInstallType": None},
                       "bios": {"manageBios": False, "overriddenSettings": []},
                       "hideUnusedFlexNics": True, "iscsiInitiatorNameType": "AutoGenerated",
                       "localStorage": {"sasLogicalJBODs": [], "controllers": []},
                       "sanStorage": {"hostOSType": "VMware (ESXi)", "manageSanStorage": True, "volumeAttachments": []}}

SP_Page_Payload = {"name": "SP_Page", "serverHardwareUri": ServerHardware[0], "enclosureGroupUri": "EG:enclgrp", "type": ServerProfile_type,
                   "connectionSettings": {
                       "connections": [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:" + network["general1"]},
                                       {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:" + network["mgmt"]},
                                       {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:" + network["fc1"]},
                                       {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:" + network["production"]},
                                       {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:" + network["production"]}]}}

SP_Page_with_vol = {"name": "SP_Page", "type": ServerProfile_type, "serverHardwareTypeUri": ServerHardwareType[0], "enclosureGroupUri": "EG:enclgrp", "serialNumberType": "Virtual",
                    "macType": "Virtual", "wwnType": "Virtual", "description": "", "affinity": "Bay",
                    "connectionSettings": {"connections": [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                            "networkUri": "ETH:" + network["general1"]},
                                                           {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                            "networkUri": "ETH:" + network["mgmt"]},
                                                           {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500",
                                                            "networkUri": "FC:" + network["fc1"]},
                                                           {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800",
                                                            "networkUri": "ETH:" + network["production"]},
                                                           {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                            "networkUri": "ETH:" + network["production"]}]},
                    "boot": {"manageBoot": True, "order": ["CD", "Floppy", "USB", "HardDisk", "PXE"]},
                    "bootMode": None,
                    "firmware": {"manageFirmware": False, "firmwareBaselineUri": "", "forceInstallFirmware": False, "firmwareInstallType": None},
                    "bios": {"manageBios": False, "overriddenSettings": []},
                    "hideUnusedFlexNics": True, "iscsiInitiatorNameType": "AutoGenerated",
                    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
                    "sanStorage": {"hostOSType": "VMware (ESXi)", "manageSanStorage": True,
                                   "volumeAttachments": []}}

ServerProfileTemplate_1 = [copy.deepcopy(SPT_payload_without_net)]
ServerProfileTemplate_1[0]["name"] = "ServerProfileTemplate_1"

ServerProfileTemplate_2 = [copy.deepcopy(SPT_payload_with_net)]
ServerProfileTemplate_2[0]["name"] = "ServerProfileTemplate_2"
ServerProfileTemplate_2_SP = [copy.deepcopy(SP_payload)]
ServerProfileTemplate_2_SP[0]["name"] = "ServerProfileTemplate_2_SP"
ServerProfileTemplate_2_SP[0]["serverProfileTemplateUri"] = "SPT:" + ServerProfileTemplate_2[0]["name"]

ServerProfileTemplate_3 = [copy.deepcopy(SPT_payload_with_net)]
ServerProfileTemplate_3[0]["name"] = None

ServerProfileTemplate_4 = [copy.deepcopy(SPT_payload_with_net)]
ServerProfileTemplate_4[0]["name"] = "ServerProfileTemplate_4"
del ServerProfileTemplate_4[0]["type"]

ServerProfileTemplate_5 = [copy.deepcopy(SPT_payload_with_net)]
ServerProfileTemplate_5[0]["name"] = "ServerProfileTemplate_5"
del ServerProfileTemplate_5[0]["serverHardwareTypeUri"]

ServerProfileTemplate_7 = [copy.deepcopy(SPT_payload_with_net)]
ServerProfileTemplate_7[0]["name"] = "ServerProfileTemplate_7"

ServerProfileTemplate_8 = [copy.deepcopy(SPT_payload_with_net)]
ServerProfileTemplate_8[0]["name"] = "ServerProfileTemplate_8"
ServerProfileTemplate_8[0]["sanStorage"] = sanStorage_payload

ServerProfileTemplate_9 = [copy.deepcopy(SPT_payload_with_net)]
ServerProfileTemplate_9[0]["name"] = "ServerProfileTemplate_9"
ServerProfileTemplate_9[0]["sanStorage"] = sanStorage_payload
ServerProfileTemplate_9_update = [copy.deepcopy(SPT_payload_with_net)]
ServerProfileTemplate_9_update[0]["name"] = "ServerProfileTemplate_9"
ServerProfileTemplate_9_update[0]["new_name"] = "ServerProfileTemplate_9_new"
ServerProfileTemplate_9_update[0]["sanStorage"] = sanStorage_payload

ServerProfileTemplate_10 = [copy.deepcopy(SPT_payload_with_net)]
ServerProfileTemplate_10[0]["name"] = "ServerProfileTemplate_10"
ServerProfileTemplate_10_update = [copy.deepcopy(SPT_payload_with_net)]
ServerProfileTemplate_10_update[0]["name"] = "ServerProfileTemplate_10"
ServerProfileTemplate_10_update[0]["serverHardwareTypeUri"] = ServerHardwareType[1]

ServerProfileTemplate_11 = [copy.deepcopy(SPT_payload_with_net)]
ServerProfileTemplate_11[0]["name"] = "ServerProfileTemplate_11"
ServerProfileTemplate_11_update = [copy.deepcopy(SPT_payload_with_net)]
ServerProfileTemplate_11_update[0]["name"] = "ServerProfileTemplate_11"
ServerProfileTemplate_11_conn_update = [{"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:" + network["mgmt"]},
                                        {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:" + network["fc1"]},
                                        {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800", "networkUri": "ETH:" + network["production"]},
                                        {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:" + network["production"]},
                                        {"id": 6, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:" + network["vmotion1"]}
                                        ]
ServerProfileTemplate_11_update[0]["connectionSettings"]["connections"] = ServerProfileTemplate_11_conn_update

ServerProfileTemplate_12 = [copy.deepcopy(SPT_payload_with_net)]
ServerProfileTemplate_12[0]["name"] = "ServerProfileTemplate_12"
ServerProfileTemplate_12[0]["sanStorage"]["manageSanStorage"] = True
ServerProfileTemplate_12_update = [copy.deepcopy(SPT_payload_with_net)]
ServerProfileTemplate_12_update[0]["name"] = "ServerProfileTemplate_12"
ServerProfileTemplate_12_update[0]["sanStorage"]["manageSanStorage"] = True
ServerProfileTemplate_12_vol_update = [{"id": 1,
                                        "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                        "bootVolumePriority": "NotBootable",
                                        "lunType": "Auto",
                                        "volumeUri": "v:" + svol["svol3"],
                                        "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]}]
ServerProfileTemplate_12_update[0]["sanStorage"]["volumeAttachments"] = ServerProfileTemplate_12_vol_update

ServerProfileTemplate_13 = [copy.deepcopy(SPT_payload_with_vol)]
ServerProfileTemplate_13[0]["name"] = "ServerProfileTemplate_13"
ServerProfileTemplate_13_priv_vol = [{"id": 1,
                                      "volume": {
                                          "properties": {
                                              "name": "san_vol1",
                                              "size": 10737418240,
                                              "provisioningType": "Thin",
                                              "isShareable": False,
                                              "storagePool": StoragePool1
                                          },
                                          "isPermanent": False,
                                          "templateUri": TemplateUri1
                                      },
                                      "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                      "bootVolumePriority": "Primary",
                                      "lunType": "Auto",
                                      "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]}]
ServerProfileTemplate_13[0]["sanStorage"]["volumeAttachments"] = ServerProfileTemplate_13_priv_vol
ServerProfileTemplate_13_update = [copy.deepcopy(SPT_payload_with_vol)]
ServerProfileTemplate_13_update[0]["name"] = "ServerProfileTemplate_13"
ServerProfileTemplate_13_update_priv_vol = [{"id": 1,
                                             "volume": {
                                                 "properties": {
                                                     "name": "san_vol",
                                                     "new_name": "san_vol_new",
                                                     "size": 10737418240,
                                                     "provisioningType": "Thin",
                                                     "isShareable": False,
                                                     "storagePool": StoragePool1},
                                                 "isPermanent": False,
                                                 "templateUri": TemplateUri1},
                                             "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                             "bootVolumePriority": "Primary",
                                             "lunType": "Auto",
                                             "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]}]

ServerProfileTemplate_14 = [copy.deepcopy(SPT_payload_with_net)]
ServerProfileTemplate_14[0]["name"] = "ServerProfileTemplate_14"
ServerProfileTemplate_14[0]["sanStorage"]["manageSanStorage"] = True
ServerProfileTemplate_14[0]["sanStorage"]["volumeAttachments"] = [{"id": 1,
                                                                   "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                   "bootVolumePriority": "NotBootable",
                                                                   "lunType": "Auto",
                                                                   "volumeUri": "v:" + svol["svol3"],
                                                                   "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]}]
ServerProfileTemplate_14_update = [copy.deepcopy(SPT_payload_with_net)]
ServerProfileTemplate_14_update[0]["name"] = "ServerProfileTemplate_14"
ServerProfileTemplate_14_update[0]["sanStorage"]["manageSanStorage"] = True

ServerProfileTemplate_15 = [copy.deepcopy(SPT_payload_with_net)]
ServerProfileTemplate_15[0]["name"] = "ServerProfileTemplate_15"

ServerProfileTemplate_16 = [copy.deepcopy(SPT_payload_with_net)]
ServerProfileTemplate_16[0]["name"] = "ServerProfileTemplate_16"
ServerProfileTemplate_16[0]["sanStorage"]["manageSanStorage"] = True

ServerProfileTemplate_17 = [copy.deepcopy(SPT_payload_with_net)]
ServerProfileTemplate_17[0]["name"] = "ServerProfileTemplate_17"
ServerProfileTemplate_17[0]["sanStorage"]["manageSanStorage"] = True

ServerProfileTemplate_18 = [copy.deepcopy(SPT_payload_with_net)]
ServerProfileTemplate_18[0]["name"] = "ServerProfileTemplate_18"
ServerProfileTemplate_18[0]["sanStorage"]["manageSanStorage"] = True

ServerProfileTemplate_19 = [copy.deepcopy(SPT_payload_with_net)]
ServerProfileTemplate_19[0]["name"] = "ServerProfileTemplate_19"
ServerProfileTemplate_19[0]["sanStorage"]["manageSanStorage"] = True

ServerProfileTemplate_26 = [copy.deepcopy(SPT_payload_with_net)]
ServerProfileTemplate_26[0]["name"] = "ServerProfileTemplate_26"
ServerProfileTemplate_26_SP = [copy.deepcopy(SP_payload)]
ServerProfileTemplate_26_SP[0]["name"] = "ServerProfileTemplate_26_SP"
ServerProfileTemplate_26_SP[0]["serverProfileTemplateUri"] = "SPT:" + ServerProfileTemplate_26[0]["name"]

ServerProfileTemplate_21 = [copy.deepcopy(SPT_payload_with_net)]
ServerProfileTemplate_21[0]["name"] = "ServerProfileTemplate_21"
ServerProfileTemplate_21_update = [copy.deepcopy(SPT_payload_with_net)]
ServerProfileTemplate_21_update[0]["name"] = "ServerProfileTemplate_21"
ServerProfileTemplate_21_update[0]["enclosureGroupUri"] = "EG:" + enclgrps[1]

SP_Page_1 = [copy.deepcopy(SP_Page_Payload)]
SP_Page_1[0]["name"] = "SP_Page_1"
SPT_SP_Page_1 = [{"name": "SPT_SP_Page_1", "SP": SP_Page_1}]

SP_Page_12 = [copy.deepcopy(SP_Page_Payload)]
SP_Page_12[0]["name"] = "SP_Page_12"
SPT_SP_Page_12 = [{"name": "SPT_SP_Page_12", "SP": SP_Page_12}]

SP_Page_2 = [copy.deepcopy(SP_Page_Payload)]
SP_Page_2[0]["name"] = "SP_Page_2"
SPT_SP_Page_2 = [{"name": "SPT_SP_Page_2", "SP": SP_Page_2}]
SPT_SP_Page_2_update = [copy.deepcopy(SP_Page_Payload)]
SPT_SP_Page_2_update[0]["name"] = "SPT_SP_Page_2"
SPT_SP_Page_2_update[0]["serverHardwareTypeUri"] = ServerHardwareType[1]


SP_Page_3 = [copy.deepcopy(SP_Page_Payload)]
SP_Page_3[0]["name"] = "SP_Page_3"
SPT_SP_Page_3 = [{"name": "SPT_SP_Page_3", "SP": SP_Page_3}]
SPT_SP_Page_3_update = [copy.deepcopy(SPT_payload_with_net)]
SPT_SP_Page_3_update[0]["name"] = "SPT_SP_Page_3"
SPT_SP_Page_3_update[0]["enclosureGroupUri"] = "EG:" + enclgrps[1]

SP_Page_4 = [copy.deepcopy(SP_Page_with_vol)]
SP_Page_4[0]["name"] = "SP_Page_4"
SPT_SP_Page_4 = [{"name": "SPT_SP_Page_4", "SP": SP_Page_4}]
SPT_SP_Page_4_update = [copy.deepcopy(SPT_payload_with_vol)]
SPT_SP_Page_4_update[0]["name"] = "SPT_SP_Page_4"
SPT_SP_Page_4_update[0]["sanStorage"]["volumeAttachments"] = [{"id": 1,
                                                               "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                               "bootVolumePriority": "NotBootable",
                                                               "lunType": "Auto",
                                                               "volumeUri": "v:" + svol["svol3"],
                                                               "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]}]

SP_Page_5 = [copy.deepcopy(SP_Page_Payload)]
SP_Page_5[0]["name"] = "SP_Page_5"
SP_Page_5[0]['serverHardwareTypeUri'] = ServerHardwareType[0]
del SP_Page_5[0]["serverHardwareUri"]
SPT_SP_Page_5 = [{"name": "SPT_SP_Page_5", "SP": SP_Page_5}]
ServerProfileTemplate_5_SP = [copy.deepcopy(SP_Page_Payload)]
ServerProfileTemplate_5_SP[0]["name"] = "ServerProfileTemplate_5_SP"
ServerProfileTemplate_5_SP[0]["serverProfileTemplateUri"] = "SPT:" + SPT_SP_Page_5[0]["name"]

SP_Page_9 = [copy.deepcopy(SP_payload)]
SP_Page_9[0]["name"] = "SP_Page_9"
SPT_SP_Page_9 = [{"name": "SPT_SP_Page_9", "SP": SP_Page_9}]
SPT_SP_Page_9_update = [copy.deepcopy(SPT_payload_with_net)]
SPT_SP_Page_9_update[0]["name"] = "SPT_SP_Page_9"
SPT_SP_Page_9_update[0]["new_name"] = "SPT_SP_Page_9_new"

SP_Page_10 = [copy.deepcopy(SP_payload)]
SP_Page_10[0]["name"] = "SP_Page_10"
SPT_SP_Page_10 = [{"name": "SPT_SP_Page_10", "SP": SP_Page_10}]

SP_Page_11 = [copy.deepcopy(SP_payload)]
SP_Page_11[0]["name"] = "SP_Page_11"
SPT_SP_Page_11 = [{"name": "SPT_SP_Page_11", "SP": SP_Page_11}]

SP_Page_13 = [copy.deepcopy(SP_payload)]
SP_Page_13[0]["name"] = "SP_Page_13"
SPT_SP_Page_13 = [{"name": "SPT_SP_Page_13", "SP": SP_Page_13}]

SP_Page_22 = [copy.deepcopy(SP_payload)]
SP_Page_22[0]["name"] = "SP_Page_22"
SPT_SP_Page_22 = [{"name": "SPT_SP_Page_22", "SP": SP_Page_22}]

SP_Page_8 = [copy.deepcopy(SP_payload)]
SP_Page_8[0]["name"] = "SP_Page_8"
SP_Page_8[0]["sanStorage"] = {"hostOSType": "VMware (ESXi)", "manageSanStorage": True,
                              "volumeAttachments": [{"id": 1,
                                                     "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                     "bootVolumePriority": "NotBootable",
                                                     "lunType": "Auto",
                                                     "volumeUri": "v:" + svol["svol3"],
                                                     "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]}]}
SPT_SP_Page_8 = [{"name": "SPT_SP_Page_8", "SP": SP_Page_8}]

SPT_SP_Page_8_update = [copy.deepcopy(SPT_payload_with_net)]
SPT_SP_Page_8_update[0]["name"] = "SPT_SP_Page_8"
SPT_SP_Page_8_update[0]["sanStorage"]["manageSanStorage"] = True

UI_ServerProfileTemplate_26 = [copy.deepcopy(SPT_payload_with_net)]
UI_ServerProfileTemplate_26[0]["name"] = "UI_ServerProfileTemplate_26"
UI_ServerProfileTemplate_26_update = [copy.deepcopy(SPT_payload_with_net)]
UI_ServerProfileTemplate_26_update[0]["name"] = "UI_ServerProfileTemplate_26"
UI_ServerProfileTemplate_26_update[0]["sanStorage"] = {"hostOSType": "VMware (ESXi)", "manageSanStorage": True,
                                                       "volumeAttachments": [{"id": 1,
                                                                              "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                              "bootVolumePriority": "NotBootable",
                                                                              "lunType": "Auto",
                                                                              "volumeUri": "v:" + svol["svol3"],
                                                                              "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]},
                                                                             {"id": 2,
                                                                              "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                              "bootVolumePriority": "NotBootable",
                                                                              "lunType": "Auto",
                                                                              "volumeUri": "v:" + svol["svol4"],
                                                                              "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]}]}
UI_ServerProfileTemplate_26_SP = [copy.deepcopy(SP_payload)]
UI_ServerProfileTemplate_26_SP[0]["name"] = "UI_ServerProfileTemplate_26_SP"
UI_ServerProfileTemplate_26_SP[0]["serverProfileTemplateUri"] = "SPT:" + UI_ServerProfileTemplate_26[0]["name"]
UI_ServerProfileTemplate_26_SP[0]["sanStorage"] = {"hostOSType": "VMware (ESXi)", "manageSanStorage": True,
                                                   "volumeAttachments": [{"id": 1,
                                                                          "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                          "bootVolumePriority": "NotBootable",
                                                                          "lunType": "Auto",
                                                                          "volumeUri": "v:" + svol["svol3"],
                                                                          "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]},
                                                                         {"id": 2,
                                                                          "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                          "bootVolumePriority": "NotBootable",
                                                                          "lunType": "Auto",
                                                                          "volumeUri": "v:" + svol["svol4"],
                                                                          "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]}]}

UI_ServerProfileTemplate_46 = [copy.deepcopy(SPT_payload_with_net)]
UI_ServerProfileTemplate_46[0]["name"] = "UI_ServerProfileTemplate_46"
UI_ServerProfileTemplate_46[0]["sanStorage"] = {"hostOSType": "VMware (ESXi)", "manageSanStorage": True,
                                                "volumeAttachments": [{"id": 1,
                                                                       "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                       "bootVolumePriority": "NotBootable",
                                                                       "lunType": "Auto",
                                                                       "volumeUri": "v:" + svol["svol3"],
                                                                       "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]}]}

UI_ServerProfileTemplate_11 = [copy.deepcopy(SPT_payload_with_net)]
UI_ServerProfileTemplate_11[0]["name"] = "UI_ServerProfileTemplate_11"

UI_ServerProfileTemplate_22 = [copy.deepcopy(SPT_payload_with_net)]
UI_ServerProfileTemplate_22[0]["name"] = "UI_ServerProfileTemplate_22"
UI_ServerProfileTemplate_22[0]["sanStorage"] = {"hostOSType": "VMware (ESXi)", "manageSanStorage": True,
                                                "volumeAttachments": [{"id": 1,
                                                                       "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                       "bootVolumePriority": "NotBootable",
                                                                       "lunType": "Auto",
                                                                       "volumeUri": "v:" + svol["svol3"],
                                                                       "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]}]}
UI_ServerProfile_22 = [copy.deepcopy(SP_payload)]
UI_ServerProfile_22[0]["name"] = "UI_ServerProfile_22"
UI_ServerProfile_22[0]["sanStorage"] = {"hostOSType": "VMware (ESXi)", "manageSanStorage": True,
                                        "volumeAttachments": [{"id": 1,
                                                               "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                               "bootVolumePriority": "NotBootable",
                                                               "lunType": "Auto",
                                                               "volumeUri": "v:" + svol["svol3"],
                                                               "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]}]}

UI_ServerProfileTemplate_47 = [copy.deepcopy(SPT_payload_with_net)]
UI_ServerProfileTemplate_47[0]["name"] = "UI_ServerProfileTemplate_47"
UI_ServerProfileTemplate_47[0]["sanStorage"] = {"hostOSType": "VMware (ESXi)", "manageSanStorage": True,
                                                "volumeAttachments": [{"id": 1,
                                                                       "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                       "bootVolumePriority": "NotBootable",
                                                                       "lunType": "Auto",
                                                                       "volumeUri": "v:" + svol["svol3"],
                                                                       "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]},
                                                                      {"id": 2,
                                                                       "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                       "bootVolumePriority": "NotBootable",
                                                                       "lunType": "Auto",
                                                                       "volumeUri": "v:" + svol["svol4"],
                                                                       "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]}]}

UI_ServerProfileTemplate_47_SP = [copy.deepcopy(SP_payload)]
UI_ServerProfileTemplate_47_SP[0]["name"] = "UI_ServerProfileTemplate_47_SP"
UI_ServerProfileTemplate_47_SP[0]["serverProfileTemplateUri"] = "SPT:" + UI_ServerProfileTemplate_47[0]["name"]
UI_ServerProfileTemplate_47_SP[0]["sanStorage"] = {"hostOSType": "VMware (ESXi)", "manageSanStorage": True,
                                                   "volumeAttachments": [{"id": 1,
                                                                          "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                          "bootVolumePriority": "NotBootable",
                                                                          "lunType": "Auto",
                                                                          "volumeUri": "v:" + svol["svol3"],
                                                                          "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]},
                                                                         {"id": 2,
                                                                          "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                          "bootVolumePriority": "NotBootable",
                                                                          "lunType": "Auto",
                                                                          "volumeUri": "v:" + svol["svol4"],
                                                                          "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]}]}

UI_ServerProfileTemplate_62 = [copy.deepcopy(SPT_payload_with_net)]
UI_ServerProfileTemplate_62[0]["name"] = "UI_ServerProfileTemplate_62"
UI_ServerProfileTemplate_62_firmware = {"manageFirmware": True, "firmwareBaselineUri": FirmwareVersion, "forceInstallFirmware": False, "firmwareInstallType": "FirmwareOnlyOfflineMode",
                                        "firmwareActivationType": "Immediate"}
UI_ServerProfileTemplate_62_shared_vol = {"hostOSType": "VMware (ESXi)", "manageSanStorage": True,
                                          "volumeAttachments": [{"id": 1,
                                                                 "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                 "bootVolumePriority": "NotBootable",
                                                                 "lunType": "Auto",
                                                                 "volumeUri": "v:" + svol["svol3"],
                                                                 "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]}]}
UI_ServerProfileTemplate_62[0]["firmware"] = UI_ServerProfileTemplate_62_firmware
UI_ServerProfileTemplate_62[0]["sanStorage"] = UI_ServerProfileTemplate_62_shared_vol
UI_ServerProfileTemplate_62_SP = [copy.deepcopy(SP_payload)]
UI_ServerProfileTemplate_62_SP[0]["name"] = "UI_ServerProfileTemplate_62_SP"
UI_ServerProfileTemplate_62_SP[0]["serverProfileTemplateUri"] = "SPT:" + UI_ServerProfileTemplate_62[0]["name"]
UI_ServerProfileTemplate_62_SP[0]["firmware"] = UI_ServerProfileTemplate_62_firmware
UI_ServerProfileTemplate_62_SP[0]["sanStorage"] = UI_ServerProfileTemplate_62_shared_vol
UI_ServerProfileTemplate_62_SP_update = copy.deepcopy(UI_ServerProfileTemplate_62_SP)
UI_ServerProfileTemplate_62_SP_update[0]["serverHardwareUri"] = ServerHardware[1]

ServerProfileTemplate_27_sanStorage = {"hostOSType": "VMware (ESXi)", "manageSanStorage": True,
                                       "volumeAttachments": [{"id": 1,
                                                              "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                              "bootVolumePriority": "NotBootable",
                                                              "lunType": "Auto",
                                                              "volumeUri": "v:" + svol["svol3"],
                                                              "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]}]}
ServerProfileTemplate_27 = [copy.deepcopy(SPT_payload_with_net)]
ServerProfileTemplate_27[0]["name"] = "ServerProfileTemplate_27"
ServerProfileTemplate_27[0]["sanStorage"] = ServerProfileTemplate_27_sanStorage
ServerProfileTemplate_27_SP = [copy.deepcopy(SP_payload)]
ServerProfileTemplate_27_SP[0]["name"] = "ServerProfileTemplate_27_SP"
ServerProfileTemplate_27_SP[0]["serverProfileTemplateUri"] = "SPT:" + ServerProfileTemplate_27[0]["name"]
ServerProfileTemplate_27_SP[0]["sanStorage"] = ServerProfileTemplate_27_sanStorage
ServerProfileTemplate_27_update = copy.deepcopy(ServerProfileTemplate_27)
ServerProfileTemplate_27_update[0]["connectionSettings"]["connections"] = [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                                            "networkUri": "ETH:" + network["general1"]},
                                                                           {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                                            "networkUri": "ETH:" + network["mgmt"]},
                                                                           {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500",
                                                                            "networkUri": "FC:" + network["fc1"]},
                                                                           {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                                            "networkUri": "ETH:" + network["production"]},
                                                                           {"id": 6, "name": "conn_net1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                                            "networkUri": "ETH:" + network["vmotion1"]},
                                                                           {"id": 7, "name": "conn_tunneled_nw", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                                            "networkUri": "ETH:" + network["tunnel"]}
                                                                           ]

au1 = "Create a connection to network {'name':'" + network["tunnel"] + "', 'uri':'/rest/ethernet-networks/b0816739-2a63-49eb-963a-559d41019555'} with id 6 on FlexibleLOM (Flb) 1:1-d."
au2 = "Change network of connection on FlexibleLOM (Flb) 1:2-c to {'name':'" + network["vmotion1"] + "', 'uri':'/rest/ethernet-networks/abad3e25-549c-4d9a-9394-cc528c6cc866'}."
profile_compliance_SP_27 = {
    "name": "",
    "compliance-preview": {
        "type": "ServerProfileCompliancePreviewV1",
        "automaticUpdates": [au1, au2],
        "manualUpdates": []}
}

REST_API_SPT_SP_Page_17 = [copy.deepcopy(SPT_payload_with_net)]
REST_API_SPT_SP_Page_17[0]["name"] = "REST_API_SPT_SP_Page_17_SPT"
REST_API_SPT_SP_Page_17_sanStorage = {"hostOSType": "VMware (ESXi)", "manageSanStorage": True,
                                      "volumeAttachments": [{"id": 1,
                                                             "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                             "bootVolumePriority": "NotBootable",
                                                             "lunType": "Auto",
                                                             "volumeUri": "v:svol3",
                                                             "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]}]}

REST_API_SPT_SP_Page_17[0]["sanStorage"] = REST_API_SPT_SP_Page_17_sanStorage
REST_API_SPT_SP_Page_17_SP = [copy.deepcopy(SP_payload)]
REST_API_SPT_SP_Page_17_SP[0]["name"] = "REST_API_SPT_SP_Page_17_SP"
REST_API_SPT_SP_Page_17_SP[0]["serverProfileTemplateUri"] = "SPT:" + REST_API_SPT_SP_Page_17[0]["name"]
REST_API_SPT_SP_Page_17_SP[0]["sanStorage"] = REST_API_SPT_SP_Page_17_sanStorage
REST_API_SPT_SP_Page_17_update = copy.deepcopy(REST_API_SPT_SP_Page_17)
REST_API_SPT_SP_Page_17_update[0]["connectionSettings"]["connections"] = [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                                           "networkUri": "ETH:" + network["general1"]},
                                                                          {"id": 2, "name": "conn_tunneled_nw", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                                           "networkUri": "ETH:" + network["tunnel"]},
                                                                          {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500",
                                                                           "networkUri": "FC:" + network["fc1"]},
                                                                          {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                                           "networkUri": "ETH:" + network["production"]},
                                                                          {"id": 6, "name": "conn_net1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                                           "networkUri": "ETH:" + network["vmotion1"]},
                                                                          ]
au17_1 = "Create a connection to network {'name':'" + network["tunnel"] + "', 'uri':'/rest/ethernet-networks/b0816739-2a63-49eb-963a-559d41019555'} with id 6 on FlexibleLOM (Flb) 1:1-d."
au17_2 = "Change network of connection on FlexibleLOM (Flb) 1:2-c to {'name':'" + network["vmotion1"] + "', 'uri':'/rest/ethernet-networks/abad3e25-549c-4d9a-9394-cc528c6cc866'}."
profile_compliance_SP_17 = {
    "name": "",
    "compliance-preview": {
        "type": "ServerProfileCompliancePreviewV1",
        "automaticUpdates": [au17_1, au17_2],
        "manualUpdates": []}
}

UI_ServerProfileTemplate_66 = [copy.deepcopy(SPT_payload_with_net)]
UI_ServerProfileTemplate_66[0]["name"] = "UI_ServerProfileTemplate_66"
UI_ServerProfileTemplate_66_firmware = {"manageFirmware": True, "firmwareBaselineUri": FirmwareVersion, "forceInstallFirmware": False, "firmwareInstallType": "FirmwareOnlyOfflineMode",
                                        "firmwareActivationType": "Immediate"}
UI_ServerProfileTemplate_66_sanStorage = {"hostOSType": "VMware (ESXi)", "manageSanStorage": True,
                                          "volumeAttachments": [{"id": 1,
                                                                 "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                 "bootVolumePriority": "NotBootable",
                                                                 "lunType": "Auto",
                                                                 "volumeUri": "v:" + svol["svol3"],
                                                                 "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]}]}
UI_ServerProfileTemplate_66[0]["firmware"] = UI_ServerProfileTemplate_66_firmware
UI_ServerProfileTemplate_66[0]["sanStorage"] = UI_ServerProfileTemplate_66_sanStorage
UI_ServerProfileTemplate_66_SP = [copy.deepcopy(SP_payload)]
UI_ServerProfileTemplate_66_SP[0]["name"] = "UI_ServerProfileTemplate_66_SP"
UI_ServerProfileTemplate_66_SP[0]["serverProfileTemplateUri"] = "SPT:" + UI_ServerProfileTemplate_66[0]['name']
UI_ServerProfileTemplate_66_SP[0]["firmware"] = UI_ServerProfileTemplate_66_firmware
UI_ServerProfileTemplate_66_SP[0]["sanStorage"] = UI_ServerProfileTemplate_66_sanStorage
UI_ServerProfileTemplate_66_update = copy.deepcopy(UI_ServerProfileTemplate_66)
UI_ServerProfileTemplate_66_update_connections = [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:" + network["general1"]},
                                                  {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:" + network["mgmt"]},
                                                  {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:" + network["fc1"],
                                                   "boot": {"priority": "Primary", "bootVolumeSource": "ManagedVolume"}},
                                                  {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:" + network["production"]},
                                                  {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:" + network["production"]}
                                                  ]
UI_ServerProfileTemplate_66_update_vols = [{"id": 1,
                                            "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                            "bootVolumePriority": "NotBootable",
                                            "lunType": "Auto",
                                            "volumeUri": "v:" + svol["svol3"],
                                            "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]},
                                           {"id": 2,
                                            "volume": {
                                                "properties": {
                                                    "name": "priv_vol",
                                                    "size": 11811160064,
                                                    "provisioningType": "Thin",
                                                    "isShareable": False,
                                                    "storagePool": StoragePool1},
                                                "isPermanent": False,
                                                "templateUri": TemplateUri1},
                                            "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                            "bootVolumePriority": "Primary",
                                            "lunType": "Auto",
                                            "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]}]
UI_ServerProfileTemplate_66_update[0]["connectionSettings"]["connections"] = UI_ServerProfileTemplate_66_update_connections
UI_ServerProfileTemplate_66_update[0]["sanStorage"]["volumeAttachments"] = UI_ServerProfileTemplate_66_update_vols
UI_ServerProfileTemplate_66_SP_update = copy.deepcopy(UI_ServerProfileTemplate_66_SP)
UI_ServerProfileTemplate_66_SP_update[0]["connectionSettings"]["connections"] = UI_ServerProfileTemplate_66_update_connections
UI_ServerProfileTemplate_66_SP_update[0]["sanStorage"]["volumeAttachments"] = UI_ServerProfileTemplate_66_update_vols

au66_1 = "Change boot for connection on FlexibleLOM (Flb) 1:1-b to FC primary."
au66_2 = "Change boot source of connection on FlexibleLOM (Flb) 1:1-b to Managed volume."
au66_3 = "Create volume 'priv_vol'."
profile_compliance_SP_66 = {
    "name": "",
    "compliance-preview": {
        "type": "ServerProfileCompliancePreviewV1",
        "automaticUpdates": [au66_1, au66_2, au66_2, au66_3],
        "manualUpdates": []}
}

UI_ServerProfileTemplate_56 = [copy.deepcopy(SPT_payload_with_net)]
UI_ServerProfileTemplate_56[0]["name"] = "UI_ServerProfileTemplate_56"
UI_ServerProfileTemplate_56_sanStorage = {"hostOSType": "VMware (ESXi)", "manageSanStorage": True,
                                          "volumeAttachments": [{"id": 1,
                                                                 "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                 "bootVolumePriority": "NotBootable",
                                                                 "lunType": "Auto",
                                                                 "volumeUri": "v:" + svol["svol3"],
                                                                 "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]}]}
UI_ServerProfileTemplate_56[0]["sanStorage"] = UI_ServerProfileTemplate_56_sanStorage

UI_ServerProfileTemplate_56_SP = [copy.deepcopy(SP_payload)]
UI_ServerProfileTemplate_56_SP[0]["name"] = "UI_ServerProfileTemplate_56_SP"
UI_ServerProfileTemplate_56_SP[0]["serverProfileTemplateUri"] = "SPT:" + UI_ServerProfileTemplate_56[0]["name"]
UI_ServerProfileTemplate_56_SP[0]["firmware"] = {"manageFirmware": True, "firmwareBaselineUri": FirmwareVersion, "forceInstallFirmware": False, "firmwareInstallType": "FirmwareOnlyOfflineMode",
                                                 "firmwareActivationType": "Immediate"}
UI_ServerProfileTemplate_56_SP[0]["sanStorage"] = UI_ServerProfileTemplate_56_sanStorage
UI_ServerProfileTemplate_56_SP_update = copy.deepcopy(UI_ServerProfileTemplate_56_SP)
UI_ServerProfileTemplate_56_SP_update[0]["firmware"] = {"manageFirmware": True, "firmwareBaselineUri": FirmwareVersion, "forceInstallFirmware": False, "firmwareInstallType": "FirmwareOnlyOfflineMode",
                                                        "firmwareActivationType": "Immediate"}

UI_ServerProfileTemplate_25_1 = copy.deepcopy(SPT_payload_with_net)
UI_ServerProfileTemplate_25_1["name"] = "UI_ServerProfileTemplate_25_1"
UI_ServerProfileTemplate_25_2 = copy.deepcopy(SPT_payload_with_net)
UI_ServerProfileTemplate_25_2["name"] = "UI_ServerProfileTemplate_25_2"
UI_ServerProfileTemplate_25_2["serverHardwareTypeUri"] = ServerHardwareType[1]
UI_ServerProfileTemplate_25_2["enclosureGroupUri"] = "EG:" + enclgrps[1]
UI_ServerProfileTemplate_25 = [UI_ServerProfileTemplate_25_1, UI_ServerProfileTemplate_25_2]
UI_ServerProfileTemplate_25_SP = [copy.deepcopy(SP_payload)]
UI_ServerProfileTemplate_25_SP[0]["serverHardwareTypeUri"] = ServerHardwareType[0]
UI_ServerProfileTemplate_25_SP[0]["name"] = "UI_ServerProfileTemplate_25_SP"
del UI_ServerProfileTemplate_25_SP[0]["serverHardwareUri"]
UI_ServerProfileTemplate_25_SP[0]["serverProfileTemplateUri"] = "SPT:" + UI_ServerProfileTemplate_25_1["name"]
UI_ServerProfileTemplate_25_SP[0]["sanStorage"] = {"hostOSType": "VMware (ESXi)", "manageSanStorage": True,
                                                   "volumeAttachments": [{"id": 1,
                                                                          "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                          "bootVolumePriority": "NotBootable",
                                                                          "lunType": "Auto",
                                                                          "volumeUri": "v:" + svol["svol3"],
                                                                          "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]}]}
UI_ServerProfileTemplate_25_SP_update = copy.deepcopy(UI_ServerProfileTemplate_25_SP)
UI_ServerProfileTemplate_25_SP_update[0]["serverHardwareTypeUri"] = ServerHardwareType[1]
UI_ServerProfileTemplate_25_SP_update[0]["enclosureGroupUri"] = "EG:" + enclgrps[1]
UI_ServerProfileTemplate_25_SP_update[0]["serverProfileTemplateUri"] = "SPT:" + UI_ServerProfileTemplate_25_2["name"]
# previous version  of OV supports below  commented compliance  payload
# profile_compliance_SP_25 = {
#    "name": "",
#    "compliance-preview": {
#        "type": "ServerProfileCompliancePreviewV1",
#        "automaticUpdates": None,
#        "manualUpdates": None}
# }
profile_compliance_SP_25 = {
    "name": "",
    "compliance-preview": {
        "type": "ServerProfileCompliancePreviewV1",
        "automaticUpdates": None,
        "manualUpdates": []}
}
UI_ServerProfileTemplate_40 = [copy.deepcopy(SPT_payload_with_vol)]
UI_ServerProfileTemplate_40[0]["name"] = "UI_ServerProfileTemplate_40"
UI_ServerProfileTemplate_40[0]["sanStorage"] = {"hostOSType": "VMware (ESXi)", "manageSanStorage": True,
                                                "volumeAttachments": [{"id": 1,
                                                                       "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                       "bootVolumePriority": "NotBootable",
                                                                       "lunType": "Auto",
                                                                       "volumeUri": "v:" + svol["svol3"],
                                                                       "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]},
                                                                      {"id": 2,
                                                                       "volume": {
                                                                           "properties": {
                                                                               "name": "priv_vol",
                                                                               "size": 11811160064,
                                                                               "provisioningType": "Thin",
                                                                               "isShareable": False,
                                                                               "storagePool": StoragePool1},
                                                                           "isPermanent": False,
                                                                           "templateUri": TemplateUri1},
                                                                       "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                       "bootVolumePriority": "Primary",
                                                                       "lunType": "Auto",
                                                                       "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]
                                                                       }]}

UI_ServerProfileTemplate_40_SP = [copy.deepcopy(SP_payload_with_vol)]
UI_ServerProfileTemplate_40_SP[0]["name"] = "UI_ServerProfileTemplate_40_SP"
UI_ServerProfileTemplate_40_SP[0]["sanStorage"] = UI_ServerProfileTemplate_40[0]["sanStorage"]
UI_ServerProfileTemplate_40_SP[0]["serverProfileTemplateUri"] = "SPT:" + UI_ServerProfileTemplate_40[0]["name"]
UI_ServerProfileTemplate_40_update = copy.deepcopy(UI_ServerProfileTemplate_40)
UI_ServerProfileTemplate_40_update[0]["connectionSettings"]["connections"] = [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                                               "networkUri": "ETH:" + network["general1"]},
                                                                              {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                                               "networkUri": "ETH:" + network["mgmt"]},
                                                                              {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500",
                                                                               "networkUri": "FC:" + network["fc1"]},
                                                                              {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2400",
                                                                               "networkUri": "ETH:" + network["production"]}
                                                                              ]
UI_ServerProfileTemplate_40_update[0]["localStorage"] = {"sasLogicalJBODs": [], "controllers": [{
    "logicalDrives": [{
        "name": "HPSUT-Volume",
        "raidLevel": "RAID1",
        "bootable": False,
        "numPhysicalDrives": 2}],
    "deviceSlot": "Embedded",
    "mode": "RAID",
    "initialize": True}]}

UI_ServerProfileTemplate_40_update[0]["sanStorage"]["volumeAttachments"] = [{"id": 1,
                                                                             "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                             "bootVolumePriority": "NotBootable",
                                                                             "lunType": "Auto",
                                                                             "volumeUri": "v:" + svol["svol3"],
                                                                             "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]}]

au40_1 = "Change boot order to [CD, USB, Floppy, HardDisk, PXE]."
au40_2 = "Delete the connection with id 5 on FlexibleLOM (Flb) 1:2-c.", u"Change boot for connection on FlexibleLOM (Flb) 1:1-b to not bootable."
mu40_1 = "Modify local storage settings to match with the server profile template."
profile_compliance_SP_40 = {
    "name": "",
    "compliance-preview": {
        "type": "ServerProfileCompliancePreviewV1",
        "automaticUpdates": [au40_1, au40_2],
        "manualUpdates": [mu40_1]}
}
UI_ServerProfileTemplate_70_1 = [copy.deepcopy(SPT_payload_with_net)]
UI_ServerProfileTemplate_70_1[0]["name"] = "UI_ServerProfileTemplate_70_1"
UI_ServerProfileTemplate_70_1_sanStorage = {"hostOSType": "VMware (ESXi)", "manageSanStorage": True,
                                            "volumeAttachments": []}
UI_ServerProfileTemplate_70_1[0]["sanStorage"] = UI_ServerProfileTemplate_70_1_sanStorage
UI_ServerProfileTemplate_70_1_SP = [copy.deepcopy(SP_payload)]
UI_ServerProfileTemplate_70_1_SP[0]["name"] = "UI_ServerProfileTemplate_70_1_SP"
UI_ServerProfileTemplate_70_1_SP[0]["sanStorage"] = UI_ServerProfileTemplate_70_1_sanStorage
UI_ServerProfileTemplate_70_1_SP_update = copy.deepcopy(UI_ServerProfileTemplate_70_1_SP)
UI_ServerProfileTemplate_70_1_SP_update[0]["serverProfileTemplateUri"] = "SPT:" + UI_ServerProfileTemplate_70_1[0]["name"]

# Below is for reference. Don"t delete
# with OV version 4.00
# UI_ServerProfileTemplate_70_1_SP_compliance = {"name": "UI_ServerProfileTemplate_70_1_SP", "compliance-preview": {
#     "type": "ServerProfileCompliancePreviewV1",
#     "isOnlineUpdate": None,
#     "manualUpdates": None,
#     "automaticUpdates": None,
# }}

# with OV version 4.10
UI_ServerProfileTemplate_70_1_SP_compliance = {"name": "UI_ServerProfileTemplate_70_1_SP", "compliance-preview": {
    "type": "ServerProfileCompliancePreviewV1",
    "isOnlineUpdate": None,
    "manualUpdates": [],
    "automaticUpdates": [],
}}
UI_ServerProfileTemplate_70_2 = [copy.deepcopy(SPT_payload_with_net)]
UI_ServerProfileTemplate_70_2[0]["name"] = "UI_ServerProfileTemplate_70_2"
UI_ServerProfileTemplate_70_2_connections = [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:" + network["general1"]},
                                             {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:" + network["mgmt"]},
                                             {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:" + network["fc1"]},
                                             {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800", "networkUri": "ETH:" + network["production"]},
                                             ]
UI_ServerProfileTemplate_70_2_sanStorage = {"hostOSType": "VMware (ESXi)", "manageSanStorage": True,
                                            "volumeAttachments": []}
UI_ServerProfileTemplate_70_2[0]["sanStorage"] = UI_ServerProfileTemplate_70_2_sanStorage
UI_ServerProfileTemplate_70_2_SP = [copy.deepcopy(SP_payload)]
UI_ServerProfileTemplate_70_2_SP[0]["name"] = "UI_ServerProfileTemplate_70_2_SP"
UI_ServerProfileTemplate_70_2_SP[0]["sanStorage"] = UI_ServerProfileTemplate_70_2_sanStorage

UI_ServerProfileTemplate_70_2_SP_update = copy.deepcopy(UI_ServerProfileTemplate_70_2_SP)
UI_ServerProfileTemplate_70_2_SP_update[0]["serverProfileTemplateUri"] = "SPT:" + UI_ServerProfileTemplate_70_2[0]["name"]

# Below is for reference. Don"t delete
# with OV version 4.10, 4.00
# UI_ServerProfileTemplate_70_2_SP_compliance = {"name": "UI_ServerProfileTemplate_70_2_SP", "compliance-preview": {
#    "type": "ServerProfileCompliancePreviewV1",
#    "isOnlineUpdate": False,
#    "manualUpdates": [],
#    "automaticUpdates": [],
# }}
# Below payload supports in 4.20
UI_ServerProfileTemplate_70_2_SP_compliance = {"name": "UI_ServerProfileTemplate_70_2_SP", "compliance-preview": {
    "type": "ServerProfileCompliancePreviewV1",
    "isOnlineUpdate": None,
    "manualUpdates": [],
    "automaticUpdates": [],
}}

UI_ServerProfileTemplate_34_1 = [copy.deepcopy(SPT_payload_with_net)]
UI_ServerProfileTemplate_34_1[0]["name"] = "UI_ServerProfileTemplate_34"
UI_ServerProfileTemplate_34_1_connections = [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                             {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                             {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                             {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800", "networkUri": "ETH:production"},
                                             {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}]
UI_ServerProfileTemplate_34_1[0]["connectionSettings"]["connections"] = UI_ServerProfileTemplate_34_1_connections
UI_ServerProfileTemplate_34_1_sanStorage = sanStorage_payload
UI_ServerProfileTemplate_34_1[0]["sanStorage"] = UI_ServerProfileTemplate_34_1_sanStorage
UI_ServerProfileTemplate_34_1_SP = [copy.deepcopy(SP_payload)]
UI_ServerProfileTemplate_34_1_SP[0]["name"] = "UI_ServerProfileTemplate_34_SP"
UI_ServerProfileTemplate_34_1_SP[0]["serverProfileTemplateUri"] = "SPT:" + UI_ServerProfileTemplate_34_1[0]["name"]
UI_ServerProfileTemplate_34_1_SP[0]["connectionSettings"]["connections"] = UI_ServerProfileTemplate_34_1_connections
UI_ServerProfileTemplate_34_1_SP[0]["sanStorage"] = UI_ServerProfileTemplate_34_1_sanStorage
UI_ServerProfileTemplate_34_1_SPT_update = [copy.deepcopy(SPT_payload_with_net)]
UI_ServerProfileTemplate_34_1_SPT_update[0]["name"] = "UI_ServerProfileTemplate_34"
UI_ServerProfileTemplate_34_1_update_sanStorage = [{"id": 1,
                                                    "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                    "bootVolumePriority": "NotBootable",
                                                    "lunType": "Auto",
                                                    "volumeUri": "v:" + svol["svol1"],
                                                    "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]}
                                                   ]
UI_ServerProfileTemplate_34_1_SPT_update[0]["sanStorage"]["volumeAttachments"] = UI_ServerProfileTemplate_34_1_update_sanStorage
UI_ServerProfileTemplate_34_SP_compliance = {"name": "UI_ServerProfileTemplate_34_SP", "compliance-preview": {
    "type": "ServerProfileCompliancePreviewV1",
    "isOnlineUpdate": True,
    "manualUpdates": [],
    "automaticUpdates": ["REGEX:Change requested bandwidth of connection .*",
                         "REGEX:Create an attachment to volume \{\"name\":\".*\", \"uri\":\"\/rest\/storage-volumes\/.*\"}\.",
                         ]
}}
UI_ServerProfileTemplate_34_1_SP_update = copy.deepcopy(UI_ServerProfileTemplate_34_1_SP)
UI_ServerProfileTemplate_34_1_SP_update[0]["sanStorage"]["volumeAttachments"] = UI_ServerProfileTemplate_34_1_update_sanStorage

UI_ServerProfileTemplate_45 = [copy.deepcopy(SPT_payload_with_net)]
UI_ServerProfileTemplate_45[0]["name"] = "UI_ServerProfileTemplate_45"
UI_ServerProfileTemplate_45[0]["connectionSettings"]["connections"] = [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                                        "networkUri": "ETH:" + network["general1"]},
                                                                       {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                                        "networkUri": "ETH:" + network["mgmt"]},
                                                                       {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500",
                                                                        "networkUri": "FC:" + network["fc1"]},
                                                                       {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800",
                                                                        "networkUri": "ETH:" + network["production"]},
                                                                       {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                                        "networkUri": "ETH:" + network["production"]}
                                                                       ]
UI_ServerProfileTemplate_45[0]["sanStorage"] = sanStorage_payload
UI_ServerProfileTemplate_45_SP1 = copy.deepcopy(SP_payload)
UI_ServerProfileTemplate_45_SP1["name"] = "UI_ServerProfileTemplate_45_SP1"
UI_ServerProfileTemplate_45_SP1['serverHardwareUri'] = ServerHardware[0]
UI_ServerProfileTemplate_45_SP1["connectionSettings"]["connections"] = UI_ServerProfileTemplate_45[0]["connectionSettings"]["connections"]
UI_ServerProfileTemplate_45_SP1["serverProfileTemplateUri"] = "SPT:" + UI_ServerProfileTemplate_45[0]["name"]
UI_ServerProfileTemplate_45_SP1["sanStorage"] = sanStorage_payload
UI_ServerProfileTemplate_45_SP2 = copy.deepcopy(SP_payload)
UI_ServerProfileTemplate_45_SP2["name"] = "UI_ServerProfileTemplate_45_SP2"
UI_ServerProfileTemplate_45_SP2['serverHardwareUri'] = ServerHardware[1]
UI_ServerProfileTemplate_45_SP2["connectionSettings"]["connections"] = UI_ServerProfileTemplate_45[0]["connectionSettings"]["connections"]
UI_ServerProfileTemplate_45_SP2["serverProfileTemplateUri"] = "SPT:" + UI_ServerProfileTemplate_45[0]["name"]
UI_ServerProfileTemplate_45_SP2["sanStorage"] = sanStorage_payload
UI_ServerProfileTemplate_45_SP = [UI_ServerProfileTemplate_45_SP1, UI_ServerProfileTemplate_45_SP2]
UI_ServerProfileTemplate_45_SPT_update = copy.deepcopy(UI_ServerProfileTemplate_45)
UI_ServerProfileTemplate_45_SPT_update[0]["connectionSettings"]["connections"] = [
    {"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:" + network["general1"]},
    {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:" + network["mgmt"]},
    {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:" + network["fc1"]},
    {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:" + network["production"]},
    {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:" + network["production"]}]
UI_ServerProfileTemplate_45_SP_update = [copy.deepcopy(UI_ServerProfileTemplate_45_SP1)]
UI_ServerProfileTemplate_45_SP_update[0]["connectionSettings"]["connections"] = UI_ServerProfileTemplate_45_SPT_update[0]["connectionSettings"]["connections"]

# Below is for reference. Don"t delete
# with OV version 4.00
# UI_ServerProfileTemplate_45_SP1_compliance = {"name": "UI_ServerProfileTemplate_45_SP1", "compliance-preview": {
#     "type": "ServerProfileCompliancePreviewV1",
#     "isOnlineUpdate": None,
#     "manualUpdates": None,
#     "automaticUpdates": None,
# }}

# with OV version 4.10
UI_ServerProfileTemplate_45_SP1_compliance = {"name": UI_ServerProfileTemplate_45_SP1["name"], "compliance-preview": {
    "type": "ServerProfileCompliancePreviewV1",
    "isOnlineUpdate": None,
    "manualUpdates": [],
    "automaticUpdates": [],
}}

UI_ServerProfileTemplate_45_SP2_compliance = {"name": UI_ServerProfileTemplate_45_SP2["name"], "compliance-preview": {
    "type": "ServerProfileCompliancePreviewV1",
    "isOnlineUpdate": True,
    "manualUpdates": [],
    "automaticUpdates": ["REGEX:Change requested bandwidth of connection .*",
                         ]
}}

UI_ServerProfileTemplate_57 = [copy.deepcopy(SPT_payload_with_net)]
UI_ServerProfileTemplate_57[0]["name"] = "UI_ServerProfileTemplate_57"
UI_ServerProfileTemplate_57_connections = [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:" + network["general1"]},
                                           {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:" + network["mgmt"]},
                                           {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:" + network["fc1"]},
                                           {"id": 4, "name": "conn_netset", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800", "networkUri": "NS:" + network["ns1"]},
                                           {"id": 5, "name": "conn_net", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:" + network["vmotion1"]},
                                           {"id": 6, "name": "tunnel_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:" + network["tunnel"]}
                                           ]
UI_ServerProfileTemplate_57[0]["connectionSettings"]["connections"] = UI_ServerProfileTemplate_57_connections
UI_ServerProfileTemplate_57[0]["sanStorage"] = sanStorage_payload

# Override SPT settings for boot, BIOS settings , Advanced settings : hideUnusedFlexNics : while creating SP from SPT
UI_ServerProfileTemplate_57_SP = [copy.deepcopy(SP_payload)]
UI_ServerProfileTemplate_57_SP[0]["name"] = "UI_ServerProfileTemplate_57_SP"
UI_ServerProfileTemplate_57_SP[0]["hideUnusedFlexNics"] = False
UI_ServerProfileTemplate_57_SP[0]["connectionSettings"]["connections"] = UI_ServerProfileTemplate_57_connections
UI_ServerProfileTemplate_57_SP[0]["serverProfileTemplateUri"] = "SPT:" + UI_ServerProfileTemplate_57[0]["name"]
UI_ServerProfileTemplate_57_SP[0]["bios"] = {"manageBios": True, "overriddenSettings": [{"id": "64", "value": "1"}]}
UI_ServerProfileTemplate_57_SP[0]['boot']['order'] = ['Floppy', 'CD', 'USB', 'HardDisk', 'PXE']
UI_ServerProfileTemplate_57_SP[0]["sanStorage"] = sanStorage_payload

UI_ServerProfileTemplate_57_SP_compliance = {"name": "UI_ServerProfileTemplate_57_SP", "compliance-preview": {
    "type": "ServerProfileCompliancePreviewV1",
    "isOnlineUpdate": False,
    "manualUpdates": [],
    "automaticUpdates": ["REGEX:Change boot order to \[CD, Floppy, USB, HardDisk, PXE\]\.",
                         "REGEX:Change hide unused FlexNICs to Yes\.",
                         ]
}}

UI_ServerProfileTemplate_69 = [copy.deepcopy(SPT_payload_with_net)]
UI_ServerProfileTemplate_69[0]["name"] = "UI_ServerProfileTemplate_69"
UI_ServerProfileTemplate_69_sanStorage = sanStorage_payload
UI_ServerProfileTemplate_69[0]["sanStorage"] = UI_ServerProfileTemplate_69_sanStorage

UI_ServerProfileTemplate_69_SP1 = copy.deepcopy(SP_payload)
UI_ServerProfileTemplate_69_SP1["name"] = "UI_ServerProfileTemplate_69_SP1"
UI_ServerProfileTemplate_69_SP1["serverProfileTemplateUri"] = "SPT:" + UI_ServerProfileTemplate_69[0]["name"]
UI_ServerProfileTemplate_69_SP1["sanStorage"] = UI_ServerProfileTemplate_69_sanStorage
UI_ServerProfileTemplate_69_SP2 = copy.deepcopy(SP_payload)
UI_ServerProfileTemplate_69_SP2["name"] = "UI_ServerProfileTemplate_69_SP2"
UI_ServerProfileTemplate_69_SP2["serverHardwareUri"] = ServerHardware[1]
UI_ServerProfileTemplate_69_SP2["serverProfileTemplateUri"] = "SPT:" + UI_ServerProfileTemplate_69[0]["name"]
UI_ServerProfileTemplate_69_SP2["sanStorage"] = UI_ServerProfileTemplate_69_sanStorage
UI_ServerProfileTemplate_69_SP = [UI_ServerProfileTemplate_69_SP1, UI_ServerProfileTemplate_69_SP2]
UI_ServerProfileTemplate_69_SPT_update = copy.deepcopy(UI_ServerProfileTemplate_69)
UI_ServerProfileTemplate_69_SPT_update[0]["connectionSettings"]["connections"] = [
    {"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:" + network["general1"]},
    {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:" + network["mgmt"]},
    {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:" + network["fc1"]},
    {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:" + network["production"]},
    {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800", "networkUri": "ETH:" + network["production"]},
    {"id": 6, "name": "tunnel_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:" + network["tunnel"]}]

UI_ServerProfileTemplate_69_SP1_compliance = {"name": "UI_ServerProfileTemplate_69_SP1", "compliance-preview": {
    "type": "ServerProfileCompliancePreviewV1",
    "isOnlineUpdate": False,
    "manualUpdates": [],
    "automaticUpdates": ["REGEX:Create a connection to network \{\"name\":\".*\", \"uri\":\"\/rest\/ethernet-networks\/.*\"\} with id .*\.",
                         "REGEX:Change requested bandwidth of connection .*b\/s\.", ]
}}

UI_ServerProfileTemplate_69_SP2_compliance = {"name": "UI_ServerProfileTemplate_69_SP2", "compliance-preview": {
    "type": "ServerProfileCompliancePreviewV1",
    "isOnlineUpdate": False,
    "manualUpdates": [],
    "automaticUpdates": ["REGEX:Create a connection to network \{\"name\":\".*\", \"uri\":\"\/rest\/ethernet-networks\/.*\"\} with id .*\.",
                         "REGEX:Change requested bandwidth of connection .*b\/s\.", ]
}}

UI_ServerProfileTemplate_43 = [copy.deepcopy(SPT_payload_with_net)]
UI_ServerProfileTemplate_43[0]["name"] = "UI_ServerProfileTemplate_43"
UI_ServerProfileTemplate_43_firmware = {"manageFirmware": True, "firmwareBaselineUri": FirmwareVersion, "forceInstallFirmware": False, "firmwareInstallType": "FirmwareOnlyOfflineMode",
                                        "firmwareActivationType": "Immediate"}
UI_ServerProfileTemplate_43_sanStorage = {"hostOSType": "VMware (ESXi)", "manageSanStorage": True,
                                          "volumeAttachments": [{"id": 1,
                                                                 "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                 "bootVolumePriority": "NotBootable",
                                                                 "lunType": "Auto",
                                                                 "volumeUri": "v:" + svol["svol3"],
                                                                 "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]}]}
UI_ServerProfileTemplate_43[0]["firmware"] = UI_ServerProfileTemplate_43_firmware
UI_ServerProfileTemplate_43[0]["sanStorage"] = UI_ServerProfileTemplate_43_sanStorage

UI_ServerProfileTemplate_43_SP = [copy.deepcopy(SP_payload)]
UI_ServerProfileTemplate_43_SP[0]["name"] = "UI_ServerProfileTemplate_43_SP"
UI_ServerProfileTemplate_43_SP[0]["serverProfileTemplateUri"] = "SPT:" + UI_ServerProfileTemplate_43[0]["name"]
UI_ServerProfileTemplate_43_SP[0]["firmware"] = UI_ServerProfileTemplate_43_firmware
UI_ServerProfileTemplate_43_SP[0]["sanStorage"] = UI_ServerProfileTemplate_43_sanStorage

uplink_sets = {"uplink1": {"name": "upl_corp",
                           "ethernetNetworkType": "Untagged",
                           "networkType": "Ethernet",
                           "networkUris": [network["mgmt"]],
                           "nativeNetworkUri": None,
                           "mode": "Auto",
                           "logicalPortConfigInfos": [{"enclosure": "1", "bay": "1", "port": "Q1.2", "speed": "Auto"}]},
               "uplink3": {"name": "upl_san",
                           "networkType": "FibreChannel",
                           "ethernetNetworkType": "NotApplicable",
                           "networkUris": [network["fc1"]],
                           "nativeNetworkUri": None,
                           "mode": "Auto",
                           "lacpTimer": "Long",
                           "logicalPortConfigInfos": [{"enclosure": "1", "bay": "1", "port": "X3", "speed": "Auto"}]}}

ligs = {"name": "lig",
        "type": "logical-interconnect-groupV500",
        "enclosureType": "C7000",
        "interconnectMapTemplate": [{"enclosure": 1, "bay": 1, "type": "HP VC FlexFabric-20/40 F8 Module", "enclosureIndex": 1},
                                    {"enclosure": 1, "bay": 2, "type": "HP VC FlexFabric-20/40 F8 Module", "enclosureIndex": 1}],
        "uplinkSets": [uplink_sets["uplink1"].copy(), uplink_sets["uplink3"].copy()],
        "internalNetworkUris": [network["ft"], network["general2"], network["vmotion1"], network["untagged"], network["tunnel"]]}

update_lig = {"lig": [ligs], "li": [{"name": "Encl1-lig"}, {"name": "Encl2-lig"}], "networks": [network["general1"], network["production"]]}

ethernet_networks_revert = [{"smartLink": "true", "ethernetNetworkType": "Tagged", "name": network["production"], "connectionTemplateUri": None,
                             "privateNetwork": "false", "type": "ethernet-networkV4", "vlanId": "100", "purpose": "General"},
                            {"smartLink": "true", "ethernetNetworkType": "Tagged", "name": network["general1"], "connectionTemplateUri": None,
                             "privateNetwork": "false", "type": "ethernet-networkV4", "vlanId": "70", "purpose": "General"}]

uplink_sets_revert = {"uplink1": {"name": "upl_corp",
                                  "ethernetNetworkType": "Untagged",
                                  "networkType": "Ethernet",
                                  "networkUris": network["mgmt"],
                                  "nativeNetworkUri": None,
                                  "mode": "Auto",
                                  "logicalPortConfigInfos": [{"enclosure": "1", "bay": "1", "port": "Q1.2", "speed": "Auto"}]},
                      "uplink2": {"name": "upl_icsp",
                                  "ethernetNetworkType": "Tagged",
                                  "networkType": "Ethernet",
                                  "networkUris": [network["general1"]],
                                  "nativeNetworkUri": None,
                                  "mode": "Auto",
                                  "logicalPortConfigInfos": [{"bay": "1", "port": "Q1.1", "speed": "Auto"}]},
                      "uplink3": {"name": "upl_san",
                                  "networkType": "FibreChannel",
                                  "ethernetNetworkType": "NotApplicable",
                                  "networkUris": [network["fc1"]],
                                  "nativeNetworkUri": None,
                                  "mode": "Auto",
                                  "lacpTimer": "Long",
                                  "logicalPortConfigInfos": [{"enclosure": "1", "bay": "1", "port": "X3", "speed": "Auto"}]}}

ligs_revert = {"name": "lig",
               "type": "logical-interconnect-groupV500",
               "enclosureType": "C7000",
               "interconnectMapTemplate": [{"enclosure": 1, "bay": 1, "type": "HP VC FlexFabric-20/40 F8 Module", "enclosureIndex": 1},
                                           {"enclosure": 1, "bay": 2, "type": "HP VC FlexFabric-20/40 F8 Module", "enclosureIndex": 1}],
               "uplinkSets": [uplink_sets_revert["uplink1"].copy(), uplink_sets_revert["uplink2"].copy(), uplink_sets_revert["uplink3"].copy()],
               "internalNetworkUris": [network["production"], network["ft"], network["general2"], network["vmotion1"], network["untagged"], network["tunnel"], network["ft2"], network["vmotion2"]]}

revert_scopes_SPT_43 = [{"name": "Scope3",
                         "description": "",
                         "type": "ScopeV3",
                         "addedResourceUris": ["ETH:" + network["general1"], "ETH:" + network["production"]],
                         "removedResourceUris": []},
                        {"name": "Scope1",
                         "description": "",
                         "type": "ScopeV3",
                         "addedResourceUris": ["ETH:" + network["general1"], "ETH:" + network["production"]],
                         "removedResourceUris": []}]

revert_update_lig = {"lig": [ligs_revert], "li": [{"name": "Encl1-lig"}, {"name": "Encl2-lig"}], "scopes": revert_scopes_SPT_43}
update_lig_name = {"name": "lig", "new_name": "lig_updated"}
revert_lig_name = {"name": "lig_updated", "new_name": "lig"}
profile_compliance_SP_43 = {
    "name": "UI_ServerProfileTemplate_43_SP",
    "compliance-preview": {
        "type": "ServerProfileCompliancePreviewV1",
        "automaticUpdates": [],
        "manualUpdates": []}
}

SPT_SBAC_1 = [copy.deepcopy(SPT_payload_without_net)]
SPT_SBAC_1[0]["name"] = "SPT_SBAC_1"
SPT_SBAC_1[0]["initialScopeUris"] = ["Scope:Scope1"]

SPT_SBAC_4_1 = [copy.deepcopy(SPT_payload_with_net)]
SPT_SBAC_4_1[0]["name"] = "SPT_SBAC_4_1"
SPT_SBAC_4_1[0]["initialScopeUris"] = ["Scope:Scope1"]

SPT_SBAC_4_2 = [copy.deepcopy(SPT_payload_with_net)]
SPT_SBAC_4_2[0]["name"] = "SPT_SBAC_4_2"
SPT_SBAC_4_2[0]["initialScopeUris"] = ["Scope:Scope1"]

SPT_SBAC_32 = [copy.deepcopy(SPT_payload_without_net)]
SPT_SBAC_32[0]["name"] = "SPT_SBAC_32"
SPT_SBAC_32[0]["initialScopeUris"] = ["Scope:Scope1", "Scope:Scope3"]

SPT_SBAC_32_UserUpdate1 = [{"type": "UserAndPermissions", "userName": "User5_SPArch", "enabled": True, "replaceRoles": True,
                            "permissions": [{"roleName": "Server profile architect", "scopeUri": "Scope1"}, {"roleName": "Read only", "scopeUri": None}]},
                           {"type": "UserAndPermissions", "userName": "User6_InfraAdm", "enabled": True, "replaceRoles": True,
                            "permissions": [{"roleName": "Infrastructure administrator", "scopeUri": "Scope1"}, {"roleName": "Read only", "scopeUri": None}]}]

SPT_SBAC_32_UserUpdate2 = [{"type": "UserAndPermissions", "userName": "User5_SPArch", "enabled": True, "replaceRoles": True,
                            "permissions": [{"roleName": "Read only", "scopeUri": None}]},
                           {"type": "UserAndPermissions", "userName": "User6_InfraAdm", "enabled": True, "replaceRoles": True,
                            "permissions": [{"roleName": "Read only", "scopeUri": None}]}]

SPT_SBAC_32_UserResetToOldScopes = [{"type": "UserAndPermissions", "userName": "User5_SPArch", "enabled": True, "replaceRoles": True,
                                     "permissions": [{"roleName": "Server profile architect", "scopeUri": "Scope1"},
                                                     {"roleName": "Server profile architect", "scopeUri": "Scope3"},
                                                     {"roleName": "Read only", "scopeUri": None}]},
                                    {"type": "UserAndPermissions", "userName": "User6_InfraAdm", "enabled": True, "replaceRoles": True,
                                     "permissions": [{"roleName": "Infrastructure administrator", "scopeUri": "Scope1"},
                                                     {"roleName": "Infrastructure administrator", "scopeUri": "Scope3"},
                                                     {"roleName": "Read only", "scopeUri": None}]}]

SPT_SBAC_35 = [copy.deepcopy(SPT_payload_without_net)]
SPT_SBAC_35[0]["name"] = "SPT_SBAC_35"
SPT_SBAC_35[0]["initialScopeUris"] = ["Scope:Scope1"]

SPT_SBAC_42 = [copy.deepcopy(SPT_payload_without_net)]
SPT_SBAC_42[0]["name"] = "SPT_SBAC_42"
SPT_SBAC_42[0]["sanStorage"] = {"hostOSType": "VMware (ESXi)", "manageSanStorage": True,
                                "volumeAttachments": []}
SPT_SBAC_42[0]["initialScopeUris"] = ["Scope:Scope1", "Scope:Scope3"]

SPT_SBACC_42_EditScope_1 = [{"name": "Scope3",
                             "description": "",
                             "type": "ScopeV3",
                             "addedResourceUris": [],
                             "removedResourceUris": ["NS:" + network["ns2"]]}]

SPT_SBAC_42_ScopeResetToOldResources = [{"name": "Scope3",
                                         "description": "",
                                         "type": "ScopeV3",
                                         "addedResourceUris": ["NS:" + network["ns2"]],
                                         "removedResourceUris": []}]

SPT_SBAC_42_UserUpdate1 = [{"type": "UserAndPermissions", "userName": "User5_SPArch", "enabled": True, "replaceRoles": True,
                            "permissions": [{"roleName": "Server profile architect", "scopeUri": "Scope1"},
                                            {"roleName": "Read only", "scopeUri": None}]},
                           {"type": "UserAndPermissions", "userName": "User6_InfraAdm", "enabled": True, "replaceRoles": True,
                            "permissions": [{"roleName": "Server profile architect", "scopeUri": "Scope1"},
                                            {"roleName": "Read only", "scopeUri": None}]}]

SPT_SBAC_42_UserResetToOldScopes = [{"type": "UserAndPermissions", "userName": "User5_SPArch", "enabled": True, "replaceRoles": True,
                                     "permissions": [{"roleName": "Server profile architect", "scopeUri": "Scope1"},
                                                     {"roleName": "Server profile architect", "scopeUri": "Scope3"},
                                                     {"roleName": "Read only", "scopeUri": None}]},
                                    {"type": "UserAndPermissions", "userName": "User6_InfraAdm", "enabled": True, "replaceRoles": True,
                                     "permissions": [{"roleName": "Infrastructure administrator", "scopeUri": "Scope1"},
                                                     {"roleName": "Infrastructure administrator", "scopeUri": "Scope3"},
                                                     {"roleName": "Read only", "scopeUri": None}]}]

SPT_SBAC_43 = [copy.deepcopy(SPT_payload_with_vol)]
SPT_SBAC_43[0]["name"] = "SPT_SBAC_43"
SPT_SBAC_43[0]["sanStorage"]["volumeAttachments"] = [{"id": 1,
                                                      "volume": {
                                                          "properties": {
                                                              "name": "san_vol1",
                                                              "size": 10737418240,
                                                              "provisioningType": "Thin",
                                                              "isShareable": False,
                                                              "storagePool": StoragePool1
                                                          },
                                                          "isPermanent": False,
                                                          "templateUri": TemplateUri1
                                                      },
                                                      "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                      "bootVolumePriority": "Primary",
                                                      "lunType": "Auto",
                                                      "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]},
                                                     {"id": 2,
                                                      "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                      "bootVolumePriority": "NotBootable",
                                                      "lunType": "Auto",
                                                      "volumeUri": "v:" + svol["svol3"],
                                                      "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]}]
SPT_SBAC_43[0]["initialScopeUris"] = ["Scope:Scope1"]


SPT_SBAC_43_UserUpdate1 = [{"type": "UserAndPermissions", "userName": "User1_SPArch", "enabled": True, "replaceRoles": True, "permissions": [{"roleName": "Read only", "scopeUri": None}]},
                           {"type": "UserAndPermissions", "userName": "User1", "enabled": True, "replaceRoles": True, "permissions": [{"roleName": "Read only", "scopeUri": None}]}]

SPT_SBAC_43_UserResetToOldScopes = [{"type": "UserAndPermissions", "userName": "User1_SPArch", "enabled": True, "replaceRoles": True,
                                     "permissions": [{"roleName": "Server profile architect", "scopeUri": "Scope1"}, {"roleName": "Read only", "scopeUri": None}]},
                                    {"type": "UserAndPermissions", "userName": "User1", "enabled": True, "replaceRoles": True,
                                     "permissions": [{"roleName": "Infrastructure administrator", "scopeUri": "Scope1"},
                                                     {"roleName": "Read only", "scopeUri": None}]}]

SPT_SBAC_44 = [copy.deepcopy(SPT_payload_with_vol)]
SPT_SBAC_44[0]["name"] = "SPT_SBAC_44"
SPT_SBAC_44[0]["initialScopeUris"] = ["Scope:Scope1", "Scope:Scope3"]
SPT_SBAC_44[0]["sanStorage"]["volumeAttachments"] = [{"id": 1,
                                                      "volume": {
                                                          "properties": {
                                                              "name": "san_vol1",
                                                              "size": 10737418240,
                                                              "provisioningType": "Thin",
                                                              "isShareable": False,
                                                              "storagePool": StoragePool1
                                                          },
                                                          "isPermanent": False,
                                                          "templateUri": TemplateUri1
                                                      },
                                                      "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                      "bootVolumePriority": "Primary",
                                                      "lunType": "Auto",
                                                      "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]},
                                                     {"id": 2,
                                                      "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                      "bootVolumePriority": "NotBootable",
                                                      "lunType": "Auto",
                                                      "volumeUri": "v:" + svol["svol6"],
                                                      "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]}]

SPT_SBAC_44_UserUpdate1 = [{"type": "UserAndPermissions", "userName": "User5_SPArch", "enabled": True, "replaceRoles": True,
                            "permissions": [{"roleName": "Server profile architect", "scopeUri": "Scope1"},
                                            {"roleName": "Read only", "scopeUri": None}]},
                           {"type": "UserAndPermissions", "userName": "User6_InfraAdm", "enabled": True, "replaceRoles": True,
                            "permissions": [{"roleName": "Infrastructure administrator", "scopeUri": "Scope1"},
                                            {"roleName": "Read only", "scopeUri": None}]}]

SPT_SBAC_44_UserUpdate2 = [{"type": "UserAndPermissions", "userName": "User5_SPArch", "enabled": True, "replaceRoles": True,
                            "permissions": [{"roleName": "Read only", "scopeUri": None}]},
                           {"type": "UserAndPermissions", "userName": "User6_InfraAdm", "enabled": True, "replaceRoles": True,
                            "permissions": [{"roleName": "Read only", "scopeUri": None}]}]

SPT_SBAC_44_UserResetToOldScopes = [{"type": "UserAndPermissions", "userName": "User5_SPArch", "enabled": True, "replaceRoles": True,
                                     "permissions": [{"roleName": "Server profile architect", "scopeUri": "Scope1"},
                                                     {"roleName": "Server profile architect", "scopeUri": "Scope3"},
                                                     {"roleName": "Read only", "scopeUri": None}]},
                                    {"type": "UserAndPermissions", "userName": "User6_InfraAdm", "enabled": True, "replaceRoles": True,
                                     "permissions": [{"roleName": "Infrastructure administrator", "scopeUri": "Scope1"},
                                                     {"roleName": "Infrastructure administrator", "scopeUri": "Scope3"},
                                                     {"roleName": "Read only", "scopeUri": None}]}]

ServerProfileTemplate_SBAC_11 = [copy.deepcopy(SPT_payload_with_net)]
ServerProfileTemplate_SBAC_11[0]["name"] = "ServerProfileTemplate_SBAC_11"
ServerProfileTemplate_SBAC_11[0]["initialScopeUris"] = ["Scope:Scope1", "Scope:Scope3"]
ServerProfileTemplate_SBAC_11_SP = [copy.deepcopy(SP_payload)]
ServerProfileTemplate_SBAC_11_SP[0]["name"] = "ServerProfileTemplate_SBAC_11_SP"
ServerProfileTemplate_SBAC_11_SP[0]["serverProfileTemplateUri"] = "SPT:" + ServerProfileTemplate_SBAC_11[0]["name"]
ServerProfileTemplate_SBAC_11_SP[0]["initialScopeUris"] = ["Scope:Scope1", "Scope:Scope3"]

ServerProfileTemplate_SBAC_16 = [copy.deepcopy(SPT_payload_with_net)]
ServerProfileTemplate_SBAC_16[0]["name"] = "ServerProfileTemplate_SBAC_16"
ServerProfileTemplate_SBAC_16[0]["initialScopeUris"] = ["Scope:Scope1", "Scope:Scope2", "Scope:Scope3"]
ServerProfileTemplate_SBAC_16_SP = [copy.deepcopy(SP_payload)]
ServerProfileTemplate_SBAC_16_SP[0]["name"] = "ServerProfileTemplate_SBAC_16_SP"
ServerProfileTemplate_SBAC_16_SP[0]["serverProfileTemplateUri"] = "SPT:" + ServerProfileTemplate_SBAC_16[0]["name"]
ServerProfileTemplate_SBAC_16_SP[0]["initialScopeUris"] = ["Scope:Scope1", "Scope:Scope2", "Scope:Scope3"]

SPT_SBAC_OVD15519 = [copy.deepcopy(SPT_payload_with_net)]
SPT_SBAC_OVD15519[0]["name"] = "SPT_SBAC_OVD15519"
SPT_SBAC_OVD15519[0]["sanStorage"] = sanStorage_payload

SPT_SBACC_OVD15519_EditScope_1 = [{"name": "Scope3",
                                   "description": "",
                                   "type": "ScopeV3",
                                   "addedResourceUris": ["SPT:" + SPT_SBAC_OVD15519[0]["name"]],
                                   "removedResourceUris": []}]

SPT_SBAC_OVD15519_SP1 = [copy.deepcopy(SP_payload)]
SPT_SBAC_OVD15519_SP1[0]["name"] = "SPT_SBAC_OVD15519_SP1"
SPT_SBAC_OVD15519_SP1[0]["serverHardwareUri"] = Scope3_ServerHardware[0]
SPT_SBAC_OVD15519_SP1[0]["serverProfileTemplateUri"] = "SPT:" + SPT_SBAC_OVD15519[0]["name"]
SPT_SBAC_OVD15519_SP1[0]["sanStorage"] = sanStorage_payload
SPT_SBAC_OVD15519_SP1[0]["firmware"] = {"manageFirmware": True, "firmwareBaselineUri": FirmwareVersion, "forceInstallFirmware": False, "firmwareInstallType": None},

SPT_SBAC_OVD15519_SP2 = [copy.deepcopy(SP_payload)]
SPT_SBAC_OVD15519_SP2[0]["name"] = "SPT_SBAC_OVD15519_SP1"
SPT_SBAC_OVD15519_SP2[0]["serverHardwareUri"] = Scope3_ServerHardware[1]
SPT_SBAC_OVD15519_SP2[0]["serverProfileTemplateUri"] = "SPT:" + SPT_SBAC_OVD15519[0]["name"]
SPT_SBAC_OVD15519_SP2[0]["sanStorage"] = sanStorage_payload
SPT_SBAC_OVD15519_SP2_firmware = {"manageFirmware": True, "firmwareBaselineUri": FirmwareVersion, "forceInstallFirmware": False, "firmwareInstallType": None},
SPT_SBAC_OVD15519_SP2[0]["firmware"] = SPT_SBAC_OVD15519_SP2_firmware
SPT_SBAC_13 = [copy.deepcopy(SPT_payload_with_net)]
SPT_SBAC_13[0]["name"] = "SPT_SBAC_13"
SPT_SBAC_13_sanStorage = sanStorage_payload
SPT_SBAC_13[0]["sanStorage"] = SPT_SBAC_13_sanStorage

SPT_SBAC_13_SP = [copy.deepcopy(SP_payload)]
SPT_SBAC_13_SP[0]["name"] = "SPT_SBAC_13_SP"
SPT_SBAC_13_SP[0]["serverHardwareUri"] = Scope3_ServerHardware[0]
SPT_SBAC_13_SP[0]["serverProfileTemplateUri"] = "SPT:" + SPT_SBAC_13[0]["name"]
SPT_SBAC_13_SP[0]["firmware"] = {"manageFirmware": True, "firmwareBaselineUri": FirmwareVersion, "forceInstallFirmware": False, "firmwareInstallType": None}
SPT_SBAC_13_SP[0]["sanStorage"] = SPT_SBAC_13_sanStorage

SPT_SBAC_14 = [copy.deepcopy(SPT_payload_with_net)]
SPT_SBAC_14[0]["name"] = "SPT_SBAC_14"
SPT_SBAC_14[0]["sanStorage"] = sanStorage_payload
SPT_SBAC_14[0]["initialScopeUris"] = ["Scope:Scope3"]
SPT_SBAC_14_SP = [copy.deepcopy(SP_payload)]
SPT_SBAC_14_SP[0]["name"] = "SPT_SBAC_14_SP"
SPT_SBAC_14_SP[0]["serverHardwareUri"] = Scope3_ServerHardware[0]
SPT_SBAC_14_SP[0]["serverProfileTemplateUri"] = "SPT:" + SPT_SBAC_14[0]["name"]
SPT_SBAC_14_SP_firmware = {"manageFirmware": True, "firmwareBaselineUri": FirmwareVersion, "forceInstallFirmware": False, "firmwareInstallType": None}
SPT_SBAC_14_SP_sanStorage = sanStorage_payload
SPT_SBAC_14_SP[0]["firmware"] = SPT_SBAC_14_SP_firmware
SPT_SBAC_14_SP[0]["sanStorage"] = SPT_SBAC_14_SP_sanStorage
SPT_SBAC_14_SP[0]["initialScopeUris"] = ["Scope:Scope3", "Scope:Scope1", "Scope:Scope2"]

SPT_SBAC_15 = [copy.deepcopy(SPT_payload_with_net)]
SPT_SBAC_15[0]["name"] = "SPT_SBAC_15"
SPT_SBAC_15_sanStorage = {"hostOSType": "VMware (ESXi)", "manageSanStorage": True,
                          "volumeAttachments": []}
SPT_SBAC_15[0]["sanStorage"] = SPT_SBAC_15_sanStorage
SPT_SBAC_15[0]["initialScopeUris"] = ["Scope:Scope3"]
SPT_SBAC_15_SP = [copy.deepcopy(SP_payload)]
SPT_SBAC_15_SP[0]["name"] = "SPT_SBAC_15_SP"
SPT_SBAC_15_SP[0]["serverHardwareUri"] = Scope3_ServerHardware[0]
SPT_SBAC_15_SP[0]["serverProfileTemplateUri"] = "SPT:" + SPT_SBAC_15[0]["name"]
SPT_SBAC_15_SP[0]["firmware"] = {"manageFirmware": True, "firmwareBaselineUri": FirmwareVersion, "forceInstallFirmware": False, "firmwareInstallType": None}
SPT_SBAC_15_SP[0]["sanStorage"] = SPT_SBAC_15_sanStorage
SPT_SBAC_15_SP[0]["initialScopeUris"] = ["Scope:Scope3", "Scope:Scope1"]

SPT_SBAC_OVD13618 = [copy.deepcopy(SPT_payload_with_net)]
SPT_SBAC_OVD13618[0]["name"] = "SPT_SBAC_OVD13618"
SPT_SBAC_OVD13618[0]["sanStorage"] = sanStorage_payload
SPT_SBAC_OVD13618[0]["initialScopeUris"] = ["Scope:Scope1", "Scope:Scope2", "Scope:Scope3"]


SPT_SBAC_OVD13618_EditScope_1 = [{"name": "Scope4",
                                  "description": "",
                                  "type": "ScopeV3",
                                  "addedResourceUris": ["SPT:" + SPT_SBAC_OVD13618[0]["name"]],
                                  "removedResourceUris": []}]

SPT_SBAC_OVD13618_SP = [copy.deepcopy(SP_payload)]
SPT_SBAC_OVD13618_SP[0]["name"] = "SPT_SBAC_OVD13618_SP"
SPT_SBAC_OVD13618_SP[0]["serverHardwareUri"] = Scope3_ServerHardware[0]
SPT_SBAC_OVD13618_SP[0]["serverProfileTemplateUri"] = "SPT:" + SPT_SBAC_OVD13618[0]["name"]
SPT_SBAC_OVD13618_SP[0]["initialScopeUris"] = ["Scope:Scope1", "Scope:Scope2", "Scope:Scope3", "Scope:Scope4"]

SPT_SBAC_OVD13618_EditScope_2 = [{"name": "Scope4",
                                  "description": "",
                                  "type": "ScopeV3",
                                  "addedResourceUris": [],
                                  "removedResourceUris": ["SPT:" + SPT_SBAC_OVD13618[0]["name"]]},
                                 {"name": "Scope3",
                                  "description": "",
                                  "type": "ScopeV3",
                                  "addedResourceUris": [],
                                  "removedResourceUris": ["SPT:" + SPT_SBAC_OVD13618[0]["name"]]},
                                 {"name": "Scope2",
                                  "description": "",
                                  "type": "ScopeV3",
                                  "addedResourceUris": [],
                                  "removedResourceUris": ["SPT:" + SPT_SBAC_OVD13618[0]["name"]]},
                                 {"name": "Scope1",
                                  "description": "",
                                  "type": "ScopeV3",
                                  "addedResourceUris": [],
                                  "removedResourceUris": ["SPT:" + SPT_SBAC_OVD13618[0]["name"]]}]

SPT_SBAC_OVD13618_SP_update = copy.deepcopy(SPT_SBAC_OVD13618_SP)
del SPT_SBAC_OVD13618_SP_update[0]["serverProfileTemplateUri"]

SPT_SBAC_10 = [copy.deepcopy(SPT_payload_with_net)]
SPT_SBAC_10[0]["initialScopeUris"] = ["Scope:Scope1", "Scope:Scope4"]
SPT_SBAC_10[0]["sanStorage"] = {"hostOSType": "VMware (ESXi)", "manageSanStorage": True,
                                "volumeAttachments": [{"id": 1,
                                                       "volume": {
                                                           "properties": {
                                                               "name": "v:" + svol["svol1"],
                                                               "size": 11000000000,
                                                               "provisioningType": "Thin",
                                                               "isShareable": False,
                                                               "storagePool": StoragePool1
                                                           },
                                                           "isPermanent": False,
                                                           "templateUri": TemplateUri1
                                                       },
                                                       "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                       "bootVolumePriority": "NotBootable",
                                                       "lunType": "Auto",
                                                       "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]
                                                       },
                                                      {"id": 2,
                                                       "volume": {
                                                           "properties": {
                                                               "name": "v:" + svol["svol2"],
                                                               "size": 11000000000,
                                                               "provisioningType": "Thin",
                                                               "isShareable": False,
                                                               "storagePool": StoragePool1
                                                           },
                                                           "isPermanent": False,
                                                           "templateUri": TemplateUri1
                                                       },
                                                       "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                       "bootVolumePriority": "NotBootable",
                                                       "lunType": "Auto",
                                                       "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]
                                                       },
                                                      {"id": 3,
                                                       "volume": {
                                                           "properties": {
                                                               "name": "v:" + svol["svol5"],
                                                               "size": 11000000000,
                                                               "provisioningType": "Thin",
                                                               "isShareable": False,
                                                               "storagePool": StoragePool1
                                                           },
                                                           "isPermanent": False,
                                                           "templateUri": TemplateUri1
                                                       },
                                                       "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                       "bootVolumePriority": "NotBootable",
                                                       "lunType": "Auto",
                                                       "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]
                                                       },
                                                      {"id": 4,
                                                       "volume": {
                                                           "properties": {
                                                               "name": "v:" + svol["svol6"],
                                                               "size": 11000000000,
                                                               "provisioningType": "Thin",
                                                               "isShareable": False,
                                                               "storagePool": StoragePool1
                                                           },
                                                           "isPermanent": False,
                                                           "templateUri": TemplateUri1
                                                       },
                                                       "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                       "bootVolumePriority": "NotBootable",
                                                       "lunType": "Auto",
                                                       "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]
                                                       }]}
SPT_SBAC_09 = [copy.deepcopy(SPT_payload_with_net)]
SPT_SBAC_09[0]["name"] = "SPT_SBAC_09"
SPT_SBAC_09[0]["sanStorage"] = {"hostOSType": "VMware (ESXi)", "manageSanStorage": True,
                                "volumeAttachments": [{"id": 1,
                                                       "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                       "bootVolumePriority": "NotBootable",
                                                       "lunType": "Auto",
                                                       "volumeUri": "v:" + svol["svol3"],
                                                       "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]
                                                       }]}
SPT_SBAC_09[0]["initialScopeUris"] = ["Scope:Scope5"]

SPT_SBAC_17 = [copy.deepcopy(SPT_payload_with_net)]
SPT_SBAC_17[0]["name"] = "SPT_SBAC_17"
SPT_SBAC_17[0]["initialScopeUris"] = ["Scope:Scope5"]

SPT_SBAC_17_SP = [copy.deepcopy(SP_payload)]
SPT_SBAC_17_SP[0]["name"] = "SPT_SBAC_17_SP"
SPT_SBAC_17_SP[0]["serverProfileTemplateUri"] = "SPT:" + SPT_SBAC_17[0]["name"]

SPT_SBAC_25 = [copy.deepcopy(SPT_payload_with_net)]
SPT_SBAC_25[0]["name"] = "SPT_SBAC_25"
SPT_SBAC_25[0]["connectionSettings"]["connections"] = [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                        "networkUri": "ETH:" + network["general1"]},
                                                       {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                        "networkUri": "ETH:" + network["mgmt"]},
                                                       {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500",
                                                        "networkUri": "FC:" + network["fc1"]}
                                                       ]
SPT_SBAC_25[0]["initialScopeUris"] = ["Scope:Scope6"]
SPT_SBAC_25_update = copy.deepcopy(SPT_SBAC_25)
SPT_SBAC_25_update[0]["connectionSettings"]["connections"] = [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                               "networkUri": "ETH:" + network["general1"]},
                                                              {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                               "networkUri": "ETH:" + network["mgmt"]},
                                                              {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500",
                                                               "networkUri": "FC:" + network["fc1"]},
                                                              {"id": 4, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                               "networkUri": "ETH:" + network["production"]}
                                                              ]

SPT_SBAC_27_update = [copy.deepcopy(SPT_payload_with_net)]
SPT_SBAC_27_update[0]["name"] = "SPT_SBAC_25"
SPT_SBAC_27_update[0]["connectionSettings"]["connections"] = [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                               "networkUri": "ETH:" + network["general1"]},
                                                              {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                               "networkUri": "ETH:" + network["mgmt"]},
                                                              {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500",
                                                               "networkUri": "FC:" + network["fc1"]},
                                                              {"id": 4, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                               "networkUri": "ETH:" + network["production"]},
                                                              {"id": 5, "name": "netset1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                               "networkUri": "NS:" + network["ns1"]},
                                                              {"id": 6, "name": "netset2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "NS:" + network["ns2"]}]
SPT_SBAC_27_update[0]["initialScopeUris"] = ["Scope:Scope6"]

SPT_SBAC_25_update_scope = [{"name": "Scope6",
                             "description": "",
                             "type": "ScopeV3",
                             "addedResourceUris": ["ETH:" + network["production"]],
                             "removedResourceUris": []}]

SPT_SBAC_27_update_scope = [{"name": "Scope6",
                             "description": "",
                             "type": "ScopeV3",
                             "addedResourceUris": ["NS:" + network["ns1"], "NS:" + network["ns2"]],
                             "removedResourceUris": []}]

SPT_SBAC_27_reverse_scope = [{"name": "Scope6",
                              "description": "",
                              "type": "ScopeV3",
                              "addedResourceUris": [],
                              "removedResourceUris": ["ETH:" + network["production"], "NS:" + network["ns1"], "NS:" + network["ns2"]]}]

SPT_SBAC_36 = [copy.deepcopy(SPT_payload_with_net)]
SPT_SBAC_36[0]["name"] = "SPT_SBAC_36"
SPT_SBAC_36[0]["connectionSettings"]["connections"] = [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                        "networkUri": "ETH:" + network["general1"]},
                                                       {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                        "networkUri": "ETH:" + network["mgmt"]},
                                                       {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500",
                                                        "networkUri": "FC:" + network["fc1"]}
                                                       ]
SPT_SBAC_36[0]["initialScopeUris"] = ["Scope:Scope5", "Scope:Scope6"]
SPT_SBAC_36_update = copy.deepcopy(SPT_SBAC_36)
SPT_SBAC_36_update[0]["name"] = "SPT_SBAC_36"
SPT_SBAC_36_update[0]["connectionSettings"]["connections"] = [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                               "networkUri": "ETH:" + network["general1"]},
                                                              {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                               "networkUri": "ETH:" + network["mgmt"]},
                                                              {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500",
                                                               "networkUri": "FC:" + network["fc1"]},
                                                              {"id": 4, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                               "networkUri": "ETH:" + network["production"]}]

SPT_SBAC_36_UserUpdate = [{"type": "UserAndPermissions", "userName": "User14_SPArch", "enabled": True, "replaceRoles": True,
                           "permissions": [{"roleName": "Read only", "scopeUri": None}]}]

SPT_SBAC_36_UserResetToOldScopes = [{"type": "UserAndPermissions", "userName": "User14_SPArch", "enabled": True, "replaceRoles": True,
                                     "permissions": [{"roleName": "Server profile architect", "scopeUri": "Scope5"},
                                                     {"roleName": "Server administrator", "scopeUri": "Scope6"}]}]

SPT_OVF1035_02 = [copy.deepcopy(SPT_payload_without_net)]
SPT_OVF1035_02[0]["name"] = "SPT_OVF1035_02"
SPT_OVF1035_02_SP = [copy.deepcopy(SP_payload)]
SPT_OVF1035_02_SP[0]["name"] = "SPT_OVF1035_02_SP"
SPT_OVF1035_02_SP[0]["serverProfileTemplateUri"] = "SPT:" + SPT_OVF1035_02[0]["name"]

profile_compliance_SPT_OVF1035_02_SP = {"name": SPT_OVF1035_02_SP[0]["name"], "compliance-preview": {
    "type": "ServerProfileCompliancePreviewV1",
    "isOnlineUpdate": None,
    "manualUpdates": [],
    "automaticUpdates": []
}}

# profile_compliance_SPT_OVF1035_02_SP = {
#     "name": "",
#     "compliance-preview": {
#         "type": "ServerProfileCompliancePreviewV1",
#         "isOnlineUpdate": None,"automaticUpdates": None,
#         "manualUpdates": None}
# }

SPT_OVF1035_03_1 = [copy.deepcopy(SPT_payload_with_net)]
SPT_OVF1035_03_1[0]["name"] = "SPT_OVF1035_03_1"
SPT_OVF1035_03_1_update = [copy.deepcopy(SPT_payload_without_net)]
SPT_OVF1035_03_1_update[0]["name"] = "SPT_OVF1035_03_1"

SPT_OVF1035_03_2 = [copy.deepcopy(SPT_payload_with_net)]
SPT_OVF1035_03_2[0]["name"] = "SPT_OVF1035_03_2"

SPT_OVF1035_03_2_SP = [copy.deepcopy(SP_payload)]
SPT_OVF1035_03_2_SP[0]["name"] = "SPT_OVF1035_03_2_SP"
SPT_OVF1035_03_2_SP[0]["serverProfileTemplateUri"] = "SPT:" + SPT_OVF1035_03_2[0]["name"]
SPT_OVF1035_03_2_update = [copy.deepcopy(SPT_payload_without_net)]
SPT_OVF1035_03_2_update[0]["name"] = SPT_OVF1035_03_2[0]["name"]

SPT_OVF1035_04_1 = [copy.deepcopy(SPT_payload_without_net)]
SPT_OVF1035_04_1[0]["name"] = "SPT_OVF1035_04_1"
SPT_OVF1035_04_1_update = [copy.deepcopy(SPT_payload_with_net)]
SPT_OVF1035_04_1_update[0]["name"] = "SPT_OVF1035_04_1"

SPT_OVF1035_04_2 = [copy.deepcopy(SPT_payload_without_net)]
SPT_OVF1035_04_2[0]["name"] = "SPT_OVF1035_04_2"
SPT_OVF1035_04_2_SP = [copy.deepcopy(SP_payload)]
SPT_OVF1035_04_2_SP[0]["name"] = "SPT_OVF1035_04_2_SP"
SPT_OVF1035_04_2_SP[0]["serverProfileTemplateUri"] = "SPT:" + SPT_OVF1035_04_2[0]["name"]

SPT_OVF1035_04_2_update = [copy.deepcopy(SPT_payload_with_net)]
SPT_OVF1035_04_2_update[0]["name"] = "SPT_OVF1035_04_2"

SPT_OVF1035_API_1 = [copy.deepcopy(SPT_payload_with_net)]
SPT_OVF1035_API_1[0]["name"] = "SPT_OVF1035_API_1"
SPT_OVF1035_API_1_connections = [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto",
                                  "requestedMbps": "2500", "networkUri": "ETH:" + network["general1"]},
                                 {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto",
                                  "requestedMbps": "2500", "networkUri": "ETH:" + network["mgmt"]},
                                 {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto",
                                  "requestedMbps": "2500", "networkUri": "FC:" + network["fc1"]},
                                 {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto",
                                  "requestedMbps": "2500", "networkUri": "ETH:" + network["production"]},
                                 {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto",
                                  "requestedMbps": "2800", "networkUri": "ETH:" + network["production"]}]
SPT_OVF1035_API_1[0]["connectionSettings"]["connections"] = SPT_OVF1035_API_1_connections
SPT_OVF1035_API_1_SP = [copy.deepcopy(SP_payload)]
SPT_OVF1035_API_1_SP[0]["name"] = "SPT_OVF1035_API_1_SP"
SPT_OVF1035_API_1_SP[0]["serverProfileTemplateUri"] = "SPT:" + SPT_OVF1035_API_1[0]["name"]


profile_compliance_SPT_OVF1035_API_1_SP_01 = {"name": SPT_OVF1035_API_1_SP[0]["name"], "compliance-preview": {
    "type": "ServerProfileCompliancePreviewV1",
    "isOnlineUpdate": True,
    "manualUpdates": [],
    "automaticUpdates": ["REGEX:Change requested bandwidth of connection .*"]
}}

# profile_compliance_SPT_OVF1035_API_1_SP_01 = {
#     "name": "SPT_OVF1035_API_1_SP",
#     "compliance-preview": {
#         "type": "ServerProfileCompliancePreviewV1",
#         "isOnlineUpdate": True,
#         "automaticUpdates": ["REGEX:Change requested bandwidth of connection on .*"]
#         "manualUpdates": None}
# }
SPT_OVF1035_API_1_update = [copy.deepcopy(SPT_payload_without_net)]
SPT_OVF1035_API_1_update[0]["name"] = "SPT_OVF1035_API_1"


profile_compliance_SPT_OVF1035_API_1_SP_02 = {"name": SPT_OVF1035_API_1_SP[0]["name"], "compliance-preview": {
    "type": "ServerProfileCompliancePreviewV1",
    "isOnlineUpdate": None,
    "manualUpdates": [],
    "automaticUpdates": []
}}

# profile_compliance_SPT_OVF1035_API_1_SP_02 = {
#     "name": "SPT_OVF1035_API_1_SP",
#     "compliance-preview": {
#         "type": "ServerProfileCompliancePreviewV1",
#         "isOnlineUpdate": None,
#         "automaticUpdates": None
#         "manualUpdates": None}
# }

SPT_OVF1035_API_2 = [copy.deepcopy(SPT_payload_without_net)]
SPT_OVF1035_API_2[0]["name"] = "SPT_OVF1035_API_2"
SPT_OVF1035_API_2_SP = [copy.deepcopy(SP_payload)]
SPT_OVF1035_API_2_SP[0]["name"] = "SPT_OVF1035_API_2_SP"
SPT_OVF1035_API_2_SP[0]["serverProfileTemplateUri"] = "SPT:" + SPT_OVF1035_API_2[0]["name"]
SPT_OVF1035_API_2_update = [copy.deepcopy(SPT_payload_with_net)]
SPT_OVF1035_API_2_update[0]["name"] = "SPT_OVF1035_API_2"
SPT_OVF1035_API_2_connections = [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto",
                                  "requestedMbps": "2500", "networkUri": "ETH:" + network["general1"]},
                                 {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto",
                                  "requestedMbps": "2500", "networkUri": "ETH:" + network["mgmt"]},
                                 {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto",
                                  "requestedMbps": "2500", "networkUri": "FC:" + network["fc1"]},
                                 {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto",
                                  "requestedMbps": "2500", "networkUri": "ETH:" + network["production"]},
                                 {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto",
                                  "requestedMbps": "2800", "networkUri": "ETH:" + network["production"]}]
SPT_OVF1035_API_2_update[0]["connectionSettings"]["connections"] = SPT_OVF1035_API_2_connections
profile_compliance_SPT_OVF1035_API_2_SP = {"name": SPT_OVF1035_API_2_SP[0]["name"], "compliance-preview": {
    "type": "ServerProfileCompliancePreviewV1",
    "isOnlineUpdate": True,
    "manualUpdates": [],
    "automaticUpdates": ["REGEX:Change requested bandwidth of connection .*"]
}}
# ===============================================================================
# Local storage is missing
# ===============================================================================
UI_SPT_30 = [copy.deepcopy(SPT_payload_with_vol)]
UI_SPT_30[0]["name"] = "UI_SPT_30"
UI_SPT_30[0]["sanStorage"] = {"hostOSType": "VMware (ESXi)", "complianceControl": "Checked", "manageSanStorage": True,
                              "volumeAttachments": [{"id": 1,
                                                     "volume": {
                                                         "properties": {
                                                             "name": "san_vol1",
                                                             "size": 10737418240,
                                                             "provisioningType": "Thin",
                                                             "isShareable": False,
                                                             "storagePool": StoragePool1
                                                         },
                                                         "isPermanent": False,
                                                         "templateUri": TemplateUri1,
                                                         "associatedTemplateAttachmentId": "SPTVAID:1"
                                                     },
                                                     "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                     "bootVolumePriority": "Primary",
                                                     "lunType": "Auto",
                                                     "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]},
                                                    {"id": 2,
                                                     "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                     "bootVolumePriority": "NotBootable",
                                                     "lunType": "Auto",
                                                     "volumeUri": "v:" + svol["svol1"],
                                                     "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]}]}

UI_SPT_30_SP = [copy.deepcopy(SP_payload_with_vol)]
UI_SPT_30_SP[0]["name"] = "UI_SPT_30_SP"
UI_SPT_30_SP[0]["serverProfileTemplateUri"] = "SPT:" + UI_SPT_30[0]["name"]
UI_SPT_30_SP[0]["sanStorage"]["volumeAttachments"] = [{"id": 1,
                                                       "volume": {
                                                           "properties": {
                                                               "name": "san_vol1",
                                                               "size": 10737418240,
                                                               "provisioningType": "Thin",
                                                               "isShareable": False,
                                                               "storagePool": StoragePool1
                                                           },
                                                           "isPermanent": False,
                                                           "templateUri": TemplateUri1,
                                                           "associatedTemplateAttachmentId": "SPTVAID:1"},
                                                       "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                       "bootVolumePriority": "Primary",
                                                       "lunType": "Auto",
                                                       "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]},
                                                      {"id": 2,
                                                       "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                       "bootVolumePriority": "NotBootable",
                                                       "lunType": "Auto",
                                                       "volumeUri": "v:" + svol["svol1"],
                                                       "associatedTemplateAttachmentId": "SPTVAID:2",
                                                       "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]}]
UI_SPT_30_update_1 = [copy.deepcopy(SPT_payload_with_net)]
UI_SPT_30_update_1[0]["name"] = "UI_SPT_30"
UI_SPT_30_update_1[0]["sanStorage"] = {"hostOSType": "VMware (ESXi)", "complianceControl": "Checked", "manageSanStorage": True,
                                       "volumeAttachments": [{"id": 2,
                                                              "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                              "bootVolumePriority": "NotBootable",
                                                              "lunType": "Auto",
                                                              "volumeUri": "v:" + svol["svol1"],
                                                              "associatedTemplateAttachmentId": "SPTVAID:2",
                                                              "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]}]}
# ===============================================================================
#  Need to update
# ===============================================================================
#                              'localStorage': {'sasLogicalJBODs': [], 'complianceControl': 'Checked',
#                                               'controllers': [{
#                                                   'logicalDrives': [{
#                                                   'name': 'sas_hdd1',
#                                                   'raidLevel': 'RAID1',
#                                                   'bootable': True,
#                                                   'numPhysicalDrives': 2,
#                                                   'driveTechnology': 'SataHdd',
#                                                   'sasLogicalJBODId': None,
#                                                   'accelerator': 'Unmanaged'
#                                                   }],
#                                                   'deviceSlot': 'Embedded',
#                                                   'mode': 'RAID',
#                                                   'initialize': True
#                                                   }]
#                                               },
mu1 = "REGEX:Change boot for connection 3 on port .* to not bootable."
mu2 = "REGEX:Delete volume attachment for {\"name\":\"san_vol1\", \"uri\":\"/rest/storage-volumes/.*"
# mu3 = "Modify local storage settings to match with the server profile template."

UI_SPT_30_SP_compliance_1 = {"name": UI_SPT_30_SP[0]["name"], "compliance-preview": {
    "type": "ServerProfileCompliancePreviewV1",
    "isOnlineUpdate": None,
    "manualUpdates": [mu1, mu2],
    #    "manualUpdates": [mu1, mu2, mu3],
    "automaticUpdates": []
}}

# Valid for 4.10
# UI_SPT_30_SP_compliance_1 = {"name": UI_SPT_30_SP[0]["name"], "compliance-preview": {
#    "type": "ServerProfileCompliancePreviewV1",
#    "isOnlineUpdate": None,
#    "manualUpdates": [mu1],
#    "automaticUpdates": []
# }}
UI_SPT_30_SP_update_1 = [copy.deepcopy(SP_payload)]
UI_SPT_30_SP_update_1[0]["name"] = "UI_SPT_30_SP"
UI_SPT_30_SP_update_1[0]["serverHardwareUri"] = ServerHardware[1]
UI_SPT_30_SP_update_1[0]["serverProfileTemplateUri"] = "SPT:" + UI_SPT_30[0]["name"]
UI_SPT_30_SP_update_1[0]["sanStorage"] = {"hostOSType": "VMware (ESXi)", "manageSanStorage": True,
                                          "volumeAttachments": [{"id": 2,
                                                                 "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                 "bootVolumePriority": "NotBootable",
                                                                 "lunType": "Auto",
                                                                 "volumeUri": "v:" + svol["svol1"],
                                                                 "associatedTemplateAttachmentId": "SPTVAID:2",
                                                                 "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]}]}

UI_SPT_30_SP_compliance_2 = {"name": UI_SPT_30_SP_update_1[0]["name"], "compliance-preview": {
    "type": "ServerProfileCompliancePreviewV1",
    "isOnlineUpdate": None,
    "manualUpdates": [],
    "automaticUpdates": [],
}}
# ===============================================================================
# TODO Not appropriate to test case
# ===============================================================================
UI_SPT_68 = [copy.deepcopy(SPT_payload_with_net)]
UI_SPT_68[0]["name"] = "UI_SPT_68"
UI_SPT_68_connections = [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                         {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                         {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                         {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800", "networkUri": "ETH:production"},
                         {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                         ]
UI_SPT_68[0]["connectionSettings"]["connections"] = UI_SPT_68_connections
UI_SPT_68[0]["sanStorage"] = sanStorage_payload
UI_SPT_68_SP = [copy.deepcopy(SP_payload)]
UI_SPT_68_SP[0]["name"] = "UI_SPT_68_SP"
UI_SPT_68_SP[0]["serverHardwareUri"] = ServerHardware[1]
UI_SPT_68_SP[0]["serverProfileTemplateUri"] = "SPT:" + UI_SPT_68[0]['name']
UI_SPT_68_SP[0]["connectionSettings"]["connections"] = UI_SPT_68_connections
UI_SPT_68_SP[0]["sanStorage"] = sanStorage_payload
UI_SPT_68_update_1 = copy.deepcopy(UI_SPT_68)
UI_SPT_68_update_1[0]["connectionSettings"]["connections"] = [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                               "networkUri": "ETH:" + network["general1"]},
                                                              {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                               "networkUri": "ETH:" + network["mgmt"]},
                                                              {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500",
                                                               "networkUri": "FC:" + network["fc1"]},
                                                              {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                               "networkUri": "ETH:" + network["production"]},
                                                              {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                               "networkUri": "ETH:" + network["production"]},
                                                              {"id": 6, "name": "tunnel_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                               "networkUri": "ETH:" + network["tunnel"]}
                                                              ]

UI_SPT_68_SP_compliance_1 = {"name": UI_SPT_68_SP[0]["name"], "compliance-preview": {
    "type": "ServerProfileCompliancePreviewV1",
    "isOnlineUpdate": False,
    "manualUpdates": [],
    "automaticUpdates": ["REGEX:Create a connection to network \{\"name\":\".*\", \"uri\":\"\/rest\/ethernet-networks\/.*\"\} with id .*\.",
                         "REGEX:Change requested bandwidth of connection .*b\/s\.",
                         ]
}}

UI_SPT_68_SP_update_1 = copy.deepcopy(UI_SPT_68_SP)
UI_SPT_68_SP_update_1[0]['serverProfileTemplateUri'] = ''

UI_SPT_68_SP_compliance_2 = {"name": UI_SPT_68_SP[0]["name"], "compliance-preview": {
    "type": "ServerProfileCompliancePreviewV1",
    "isOnlineUpdate": False,
    "manualUpdates": [],
    "automaticUpdates": []
}}

REST_API_SPT_SP_Page_15_1 = [copy.deepcopy(SPT_payload_with_net)]
REST_API_SPT_SP_Page_15_1[0]["name"] = "REST_API_SPT_SP_Page_16_1"
REST_API_SPT_SP_Page_15_2 = copy.deepcopy(REST_API_SPT_SP_Page_15_1)

REST_API_SPT_SP_Page_16_1 = copy.deepcopy(SPT_payload_with_net)
REST_API_SPT_SP_Page_16_1["name"] = "REST_API_SPT_SP_Page_16_1"
REST_API_SPT_SP_Page_16_2 = copy.deepcopy(SPT_payload_with_net)
REST_API_SPT_SP_Page_16_2["name"] = "REST_API_SPT_SP_Page_16_2"
REST_API_SPT_SP_Page_16 = [REST_API_SPT_SP_Page_16_1, REST_API_SPT_SP_Page_16_2]
REST_API_SPT_SP_Page_16_update = [copy.deepcopy(REST_API_SPT_SP_Page_16_1)]
REST_API_SPT_SP_Page_16_update[0]["new_name"] = "REST_API_SPT_SP_Page_16_2"

OVF1035_09 = [copy.deepcopy(SPT_payload_with_net)]
OVF1035_09[0]["name"] = "OVF1035_09"
OVF1035_09_update = [copy.deepcopy(SPT_payload_without_net)]
OVF1035_09_update[0]["name"] = "OVF1035_09"

REST_API_SPT_SP_Page_14 = [copy.deepcopy(SPT_payload_with_net)]
REST_API_SPT_SP_Page_14[0]["name"] = "REST_API_SPT_SP_Page_14"
REST_API_SPT_SP_Page_14[0]["connectionSettings"]["connections"] = [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                                    "networkUri": "ETH:" + network["general1"]},
                                                                   {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                                    "networkUri": "ETH:" + network["mgmt"]},
                                                                   {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500",
                                                                    "networkUri": "FC:" + network["fc1"]},
                                                                   {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                                    "networkUri": "ETH:" + network["production"]}
                                                                   ]
REST_API_SPT_SP_Page_14[0]["serverHardwareTypeUri"] = "SHT:BL460c Gen8 1 Invalid"

SP_Page_23 = [copy.deepcopy(SP_payload)]
SP_Page_23[0]["name"] = "SP_Page_23"

SPT_SP_Page_23 = [{"name": "SPT_SP_Page_23", "SP": SP_Page_23}]
SPT_SP_Page_23_SP_1 = copy.deepcopy(SP_Page_23)
SPT_SP_Page_23_SP_1[0]["name"] = "SPT_SP_Page_23_SP_1"
SPT_SP_Page_23_SP_1[0]["serverHardwareUri"] = ServerHardware[1]
SPT_SP_Page_23_SP_1[0]["serverProfileTemplateUri"] = "SPT:" + SPT_SP_Page_23[0]["name"]

OVF1035_08 = [copy.deepcopy(SPT_payload_without_net)]
OVF1035_08[0]["name"] = "OVF1035_08"
OVF1035_08_update = copy.deepcopy(OVF1035_08)
OVF1035_08_update[0]["connectionSettings"] = {"manageConnections": True,
                                              "connections": [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                               "networkUri": "ETH:" + network["general1"]},
                                                              {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                               "networkUri": "ETH:" + network["mgmt"]},
                                                              {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500",
                                                               "networkUri": "FC:" + network["fc1"]},
                                                              {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                               "networkUri": "ETH:" + network["production"]}]}

SP_Page_21 = [copy.deepcopy(SP_payload)]
SP_Page_21[0]["name"] = "SP_Page_21"
SP_Page_21[0]["serverHardwareUri"] = ServerHardware[1]
SP_Page_21[0]["sanStorage"] = {"hostOSType": "VMware (ESXi)", "manageSanStorage": True,
                               "volumeAttachments": [{"id": 1,
                                                      "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                      "bootVolumePriority": "NotBootable",
                                                      "lunType": "Auto",
                                                      "volumeUri": "v:" + svol["svol3"],
                                                      "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]}]}

SPT_SP_Page_21 = [{"name": "SPT_SP_Page_21", "SP": SP_Page_21}]
SPT_SP_Page_21_update = [copy.deepcopy(SPT_payload_with_net)]
SPT_SP_Page_21_update[0]["name"] = "SPT_SP_Page_21"
SPT_SP_Page_21_update[0]["firmware"] = {"manageFirmware": True, "firmwareBaselineUri": FirmwareVersion, "forceInstallFirmware": False,
                                        "firmwareInstallType": "FirmwareAndOSDrivers", "firmwareActivationType": "Immediate"}
SPT_SP_Page_21_update[0]["sanStorage"] = SP_Page_21[0]["sanStorage"]

UI_ServerProfileTemplate_67_1 = copy.deepcopy(SPT_payload_with_net)
UI_ServerProfileTemplate_67_1["name"] = "UI_ServerProfileTemplate_67_1"
UI_ServerProfileTemplate_67_1["sanStorage"] = {"hostOSType": "VMware (ESXi)", "manageSanStorage": True,
                                               "volumeAttachments": [{"id": 1,
                                                                      "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                      "bootVolumePriority": "NotBootable",
                                                                      "lunType": "Auto",
                                                                      "volumeUri": "v:" + svol["svol3"],
                                                                      "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]}]}
UI_ServerProfileTemplate_67_2 = copy.deepcopy(UI_ServerProfileTemplate_67_1)
UI_ServerProfileTemplate_67_2["name"] = "UI_ServerProfileTemplate_67_2"
UI_ServerProfileTemplate_67_2["sanStorage"] = copy.deepcopy(UI_ServerProfileTemplate_67_1["sanStorage"])
UI_ServerProfileTemplate_67 = [UI_ServerProfileTemplate_67_1, UI_ServerProfileTemplate_67_2]
UI_ServerProfileTemplate_67_SP = [copy.deepcopy(SP_payload)]
UI_ServerProfileTemplate_67_SP[0]["name"] = "UI_ServerProfileTemplate_67_SP"
UI_ServerProfileTemplate_67_SP[0]["serverHardwareUri"] = ServerHardware[1]
UI_ServerProfileTemplate_67_SP[0]["serverProfileTemplateUri"] = "SPT:" + UI_ServerProfileTemplate_67_1["name"]
UI_ServerProfileTemplate_67_SP[0]["sanStorage"] = copy.deepcopy(UI_ServerProfileTemplate_67_1["sanStorage"])

UI_ServerProfileTemplate_67_SP_update = copy.deepcopy(UI_ServerProfileTemplate_67_SP)
UI_ServerProfileTemplate_67_SP_update[0]["serverProfileTemplateUri"] = "SPT:" + UI_ServerProfileTemplate_67_2["name"]
UI_ServerProfileTemplate_67_SP_update[0]["sanStorage"]["volumeAttachments"] = [{"id": 1,
                                                                                "associatedTemplateAttachmentId": 'SPTVAID:1',
                                                                                "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                                "bootVolumePriority": "NotBootable",
                                                                                "lunType": "Auto",
                                                                                "volumeUri": "v:" + svol["svol3"],
                                                                                "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]}]
profile_compliance_SP_67 = {"name": UI_ServerProfileTemplate_67_SP[0]["name"],
                            "compliance-preview": {"type": "ServerProfileCompliancePreviewV1",
                                                   "isOnlineUpdate": None,
                                                   "manualUpdates": [],
                                                   "automaticUpdates": []
                                                   }}
UI_ServerProfileTemplate_67_update = [copy.deepcopy(UI_ServerProfileTemplate_67_2)]
UI_ServerProfileTemplate_67_update[0]["sanStorage"]["volumeAttachments"] = [{"id": 1,
                                                                             "associatedTemplateAttachmentId": "SPTVAID:1",
                                                                             "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                             "bootVolumePriority": "NotBootable",
                                                                             "lunType": "Auto",
                                                                             "volumeUri": "v:" + svol["svol3"],
                                                                             "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]}]
UI_ServerProfileTemplate_67_update[0]["bios"] = {"manageBios": True, "overriddenSettings": []}
UI_ServerProfileTemplate_67_update[0]["boot"]["order"] = ["USB", "HardDisk", "PXE", "CD", "Floppy"]
profile_compliance_SP_67_updated = {"name": UI_ServerProfileTemplate_67_SP[0]["name"],
                                    "compliance-preview": {"type": "ServerProfileCompliancePreviewV1",
                                                           "isOnlineUpdate": False,
                                                           "manualUpdates": [],
                                                           "automaticUpdates": ["REGEX:Change boot order to .*", "REGEX:Change BIOS settings to managed by profile."]
                                                           }}

REST_API_SPT_SP_Page_18 = [copy.deepcopy(SPT_payload_without_net)]
REST_API_SPT_SP_Page_18[0]["name"] = ""

REST_API_SPT_SP_Page_19 = [copy.deepcopy(SPT_payload_without_net)]
REST_API_SPT_SP_Page_19[0]["name"] = "REST_API_SPT_SP_Page_19"
REST_API_SPT_SP_Page_19[0]["type"] = ""

SPT_SBAC6_1 = [copy.deepcopy(SPT_payload_with_net)]
SPT_SBAC6_1[0]["name"] = "SPT_SBAC6_1"
SPT_SBAC6_1[0]["firmware"] = {"manageFirmware": True, "firmwareBaselineUri": FirmwareVersion, "forceInstallFirmware": False, "firmwareInstallType": "FirmwareOnlyOfflineMode",
                              "firmwareActivationType": "Immediate"}
SPT_SBAC6_1[0]["initialScopeUris"] = ["Scope:Scope1", "Scope:Scope5"]

SPT_SBAC6_2 = [copy.deepcopy(SPT_payload_with_net)]
SPT_SBAC6_2[0]["name"] = "SPT_SBAC6_2"
SPT_SBAC6_2[0]["firmware"] = {"manageFirmware": True, "firmwareBaselineUri": FirmwareVersion, "forceInstallFirmware": False, "firmwareInstallType": "FirmwareOnlyOfflineMode",
                              "firmwareActivationType": "Immediate"}
SPT_SBAC6_2[0]["initialScopeUris"] = ["Scope:Scope5"]

SPT_SBAC71 = [copy.deepcopy(SPT_payload_without_net)]
SPT_SBAC71[0]["name"] = "ServerProfileTemplate_1"
SPT_SBAC71[0]["initialScopeUris"] = ["Scope:Scope1"]

SPT_SBAC72 = [copy.deepcopy(SPT_payload_without_net)]
SPT_SBAC72[0]["name"] = "ServerProfileTemplate_2"
SPT_SBAC72[0]["initialScopeUris"] = ["Scope:Scope1", "Scope:Scope3"]

storage_volumes = [{"storageSystemUri": VolumeStorageSystemUri1, "name": svol["svol3"]}]

UI_ServerProfileTemplate_48 = {
    "name": UI_ServerProfileTemplate_56_SP[0]["name"],
    "compliance-preview": {
        "type": "ServerProfileCompliancePreviewV1",
        "automaticUpdates": [],
        "manualUpdates": []}
}

UI_ServerProfileTemplate_42_SP = [copy.deepcopy(SP_payload)]
UI_ServerProfileTemplate_42_SP[0]["name"] = "UI_ServerProfileTemplate_42_SP"
UI_ServerProfileTemplate_42_SP[0]["connectionSettings"]["connections"] = UI_ServerProfileTemplate_57_connections
UI_ServerProfileTemplate_42_SP[0]["sanStorage"] = sanStorage_payload
UI_ServerProfileTemplate_42_SP[0]["bios"] = {"manageBios": True, "overriddenSettings": [{"id": "64", "value": "1"}]}
UI_ServerProfileTemplate_42_SP[0]["serverProfileTemplateUri"] = "SPT:" + UI_ServerProfileTemplate_57[0]["name"]

UI_ServerProfileTemplate_42_compliance = {
    "name": UI_ServerProfileTemplate_42_SP[0]["name"],
    "compliance-preview": {
        "type": "ServerProfileCompliancePreviewV1",
        "automaticUpdates": [],
        "manualUpdates": []}
}
network_sets_update_add = [{"name": network["ns1"], "add_networkUris": [network["general2"]], "type": "network-setV4"}]
network_sets_update_delete = [{"name": network["ns1"], "delete_networkUris": [network["general2"]], "type": "network-setV4"}]

UI_ServerProfileTemplate_50 = [copy.deepcopy(SPT_payload_with_net)]
UI_ServerProfileTemplate_50[0]["name"] = "UI_ServerProfileTemplate_50"

UI_ServerProfileTemplate_50_update = copy.deepcopy(UI_ServerProfileTemplate_50)
UI_ServerProfileTemplate_50_update[0]["new_name"] = "!@#$%^&"
UI_ServerProfileTemplate_51_SP = [copy.deepcopy(SP_payload)]
UI_ServerProfileTemplate_51_SP[0]["name"] = "UI_ServerProfileTemplate_51_SP"
UI_ServerProfileTemplate_51_SP[0]["bios"] = {"manageBios": True, "overriddenSettings": [{"id": "64", "value": "1"}]}
UI_ServerProfileTemplate_51_SP[0]["serverProfileTemplateUri"] = "SPT:" + UI_ServerProfileTemplate_50[0]["name"]
UI_ServerProfileTemplate_51_SP_update = copy.deepcopy(UI_ServerProfileTemplate_51_SP)
UI_ServerProfileTemplate_51_SP_update[0]["new_name"] = "!@"

UI_ServerProfileTemplate_12 = [copy.deepcopy(SPT_payload_without_net)]
UI_ServerProfileTemplate_12[0]["name"] = "UI_ServerProfileTemplate_12"

SPT_SBAC_8 = [copy.deepcopy(SPT_payload_without_net)]
SPT_SBAC_8[0]["name"] = "SPT_SBAC_8"
SPT_SBAC_8[0]["initialScopeUris"] = {"Scope:Scope2"}

REST_API_SPT_SP_Page_20 = [copy.deepcopy(SPT_payload_without_net)]
REST_API_SPT_SP_Page_20[0]["name"] = "REST_API_SPT_SP_Page_20"

REST_API_SPT_SP_Page_21 = [copy.deepcopy(SPT_payload_without_net)]
REST_API_SPT_SP_Page_21[0]["name"] = "REST_API_SPT_SP_Page_21"

SPT_SP_Page_20 = [copy.deepcopy(SPT_payload_with_net)]
SPT_SP_Page_20[0]["name"] = "SPT_SP_Page_20"
SPT_SP_Page_20_SP = [copy.deepcopy(SP_payload)]
SPT_SP_Page_20_SP[0]["name"] = "SPT_SP_Page_20_SP"
SPT_SP_Page_20_SP[0]["serverHardwareUri"] = ServerHardware[1]
SPT_SP_Page_20_SP[0]["serverProfileTemplateUri"] = "SPT:" + SPT_SP_Page_20[0]["name"]
SPT_SP_Page_20_update = copy.deepcopy(SPT_SP_Page_20)
SPT_SP_Page_20_update[0]["serverHardwareTypeUri"] = ServerHardwareType[1]

UI_ServerProfileTemplate_34 = [copy.deepcopy(SPT_payload_with_vol)]
UI_ServerProfileTemplate_34[0]["name"] = "UI_ServerProfileTemplate_34"
UI_ServerProfileTemplate_34[0]["sanStorage"]["volumeAttachments"] = [{"id": 1,
                                                                      "volume": {
                                                                          "properties": {
                                                                              "name": "san_vol1",
                                                                              "size": 10737418240,
                                                                              "provisioningType": "Thin",
                                                                              "isShareable": False,
                                                                              "storagePool": StoragePool1
                                                                          },
                                                                          "isPermanent": False,
                                                                          "templateUri": TemplateUri1
                                                                      },
                                                                      "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                      "bootVolumePriority": "Primary",
                                                                      "lunType": "Auto",
                                                                      "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}],
                                                                      "associatedTemplateAttachmentId": "1"},
                                                                     {"id": 2,
                                                                      "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                      "bootVolumePriority": "NotBootable",
                                                                      "lunType": "Auto",
                                                                      "volumeUri": "v:" + svol["svol1"],
                                                                      "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}],
                                                                      "associatedTemplateAttachmentId": "2"}]

UI_ServerProfileTemplate_34_SP = [copy.deepcopy(SP_payload_with_vol)]
UI_ServerProfileTemplate_34_SP[0]["name"] = "UI_ServerProfileTemplate_34_SP"
UI_ServerProfileTemplate_34_SP[0]["serverHardwareUri"] = ServerHardware[1]
UI_ServerProfileTemplate_34_SP[0]["serverProfileTemplateUri"] = "SPT:" + UI_ServerProfileTemplate_34[0]["name"]
UI_ServerProfileTemplate_34_SP[0]["sanStorage"]["volumeAttachments"] = [{"id": 1,
                                                                         "volume": {
                                                                             "properties": {
                                                                                 "name": "san_vol1",
                                                                                 "size": 10737418240,
                                                                                 "provisioningType": "Thin",
                                                                                 "isShareable": False,
                                                                                 "storagePool": StoragePool1
                                                                             },
                                                                             "isPermanent": False,
                                                                             "templateUri": TemplateUri1
                                                                         },
                                                                         "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                         "bootVolumePriority": "Primary",
                                                                         "lunType": "Auto",
                                                                         "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}],
                                                                         "associatedTemplateAttachmentId": "1"},
                                                                        {"id": 2,
                                                                         "associatedTemplateAttachmentId": "2",
                                                                         "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                         "bootVolumePriority": "NotBootable",
                                                                         "lunType": "Auto",
                                                                         "volumeUri": "v:" + svol["svol1"],
                                                                         "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]}]

UI_ServerProfileTemplate_34_update = copy.deepcopy(UI_ServerProfileTemplate_34)
UI_ServerProfileTemplate_34_update_connections = [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet",
                                                   "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                  {"id": 2, "name": "corp_conn", "functionType": "Ethernet",
                                                   "portId": "Auto", "requestedMbps": "2800", "networkUri": 'ETH:corp'},
                                                  {"id": 3, "name": "san_conn", "functionType": "FibreChannel",
                                                   "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san",
                                                   "boot": {"priority": "Primary", "bootVolumeSource": "ManagedVolume"}},
                                                  {"id": 4, "name": "conn_prod1", "functionType": "Ethernet",
                                                   "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                  {"id": 5, "name": "conn_prod2", "functionType": "Ethernet",
                                                   "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}]
UI_ServerProfileTemplate_34_update[0]["connectionSettings"]["connections"] = UI_ServerProfileTemplate_34_update_connections
UI_ServerProfileTemplate_34_update[0]["sanStorage"]["volumeAttachments"] = [{"id": 1,
                                                                             "volume": {
                                                                                 "properties": {
                                                                                     "name": "san_vol1_rename",
                                                                                     "size": 10737418340,
                                                                                     "provisioningType": "Thin",
                                                                                     "isShareable": False,
                                                                                     "storagePool": StoragePool1},
                                                                                 "isPermanent": False,
                                                                                 "templateUri": TemplateUri1},
                                                                             "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                             "bootVolumePriority": "Primary",
                                                                             "lunType": "Auto",
                                                                             "associatedTemplateAttachmentId": "1",
                                                                             "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]},
                                                                            {"id": 2,
                                                                             "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                             "bootVolumePriority": "NotBootable",
                                                                             "lunType": "Auto",
                                                                             "volumeUri": "v:" + svol["svol1"],
                                                                             "associatedTemplateAttachmentId": "2",
                                                                             "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]}]

au34_1 = "REGEX:Change requested bandwidth of connection .*"
mu34_1 = "REGEX:Attachment id 1 for volume .*must be at least the capacity of the volume as defined in the server profile template.\
 The capacity of the volume can be corrected on the volumes page.  Alternatively, the volume's defined capacity can be corrected on the server profile template and volume template .*."
profile_compliance_SP_34_1 = {"name": UI_ServerProfileTemplate_34_SP[0]["name"],
                              "compliance-preview": {"type": "ServerProfileCompliancePreviewV1",
                                                     "isOnlineUpdate": True,
                                                     "manualUpdates": [mu34_1],
                                                     "automaticUpdates": [au34_1]
                                                     }}

profile_compliance_SP_34_2 = {"name": UI_ServerProfileTemplate_34_SP[0]["name"],
                              "compliance-preview": {"type": "ServerProfileCompliancePreviewV1",
                                                     "isOnlineUpdate": None,
                                                     "manualUpdates": [],
                                                     "automaticUpdates": []
                                                     }}
UI_ServerProfileTemplate_25_new = copy.deepcopy(SPT_payload_with_net)
UI_ServerProfileTemplate_25_new["name"] = "UI_ServerProfileTemplate_25"
UI_ServerProfileTemplate_25_different_encgrp = copy.deepcopy(SPT_payload_with_net)
UI_ServerProfileTemplate_25_different_encgrp["name"] = "UI_ServerProfileTemplate_25_different_encgrp"
UI_ServerProfileTemplate_25_different_encgrp["enclosureGroupUri"] = "EG:" + enclgrps[1]
UI_ServerProfileTemplate_OVTC32293_25 = [UI_ServerProfileTemplate_25_new, UI_ServerProfileTemplate_25_different_encgrp]
UI_ServerProfileTemplate_OVTC32293_25_SP = [copy.deepcopy(SP_payload)]
UI_ServerProfileTemplate_OVTC32293_25_SP[0]["serverHardwareUri"] = ServerHardware[1]
UI_ServerProfileTemplate_OVTC32293_25_SP[0]["serverProfileTemplateUri"] = "SPT:" + UI_ServerProfileTemplate_25_new["name"]
UI_ServerProfileTemplate_OVTC32293_25_SP_update = copy.deepcopy(UI_ServerProfileTemplate_OVTC32293_25_SP)
UI_ServerProfileTemplate_OVTC32293_25_SP_update[0]["serverProfileTemplateUri"] = "SPT:" + UI_ServerProfileTemplate_25_different_encgrp["name"]

mu25_1 = "REGEX:Change enclosure group to *."
profile_compliance_SP_25_1 = {"name": UI_ServerProfileTemplate_OVTC32293_25_SP[0]["name"],
                              "compliance-preview": {"type": "ServerProfileCompliancePreviewV1",
                                                     "isOnlineUpdate": None,
                                                     "manualUpdates": [mu25_1],
                                                     "automaticUpdates": []
                                                     }}

profile_compliance_SP_25_2 = {"name": UI_ServerProfileTemplate_OVTC32293_25_SP[0]["name"],
                              "compliance-preview": {"type": "ServerProfileCompliancePreviewV1",
                                                     "isOnlineUpdate": None,
                                                     "manualUpdates": [],
                                                     "automaticUpdates": []}}
SPT_SBAC_28_EditScope = [{"name": "Scope1",
                          "description": "",
                          "type": "ScopeV3",
                          "addedResourceUris": [],
                          "removedResourceUris": ["ETH:" + network["production"]]}]

UI_ServerProfileTemplate_71_SP = [copy.deepcopy(SP_payload_with_vol)]
UI_ServerProfileTemplate_71_SP[0]["name"] = "UI_SPT_68_SP"
UI_ServerProfileTemplate_71_SP[0]["serverProfileTemplateUri"] = "SPT:" + UI_SPT_68[0]["name"]

ServerProfileTemplate_20 = [copy.deepcopy(SPT_payload_without_net)]
ServerProfileTemplate_20[0]["name"] = "ServerProfileTemplate_20_spt"
ServerProfileTemplate_20_SPT = [copy.deepcopy(SPT_payload_with_net)]
ServerProfileTemplate_20_SPT[0]["name"] = "ServerProfileTemplate_20_spt"

UI_ServerProfileTemplate_52_1 = copy.deepcopy(SPT_payload_with_net)
UI_ServerProfileTemplate_52_1["name"] = "UI_ServerProfileTemplate_52_SPT"
UI_ServerProfileTemplate_52_2 = copy.deepcopy(SPT_payload_with_net)
UI_ServerProfileTemplate_52_2["name"] = "UI_ServerProfileTemplate_52_SPT1"
UI_ServerProfileTemplate_52_2["serverHardwareTypeUri"] = ServerHardwareType[1]
UI_ServerProfileTemplate_52_SPT = [UI_ServerProfileTemplate_52_1, UI_ServerProfileTemplate_52_2]

UI_ServerProfileTemplate_49 = [copy.deepcopy(SPT_payload_with_net)]
UI_ServerProfileTemplate_49[0]["name"] = "UI_ServerProfileTemplate_49_@$"
UI_ServerProfileTemplate_49_SP = [copy.deepcopy(SP_payload)]
UI_ServerProfileTemplate_49_SP[0]["name"] = "UI_ServerProfileTemplate_49_SP_@$"
UI_ServerProfileTemplate_49_SP[0]["serverProfileTemplateUri"] = "SPT:" + UI_ServerProfileTemplate_49[0]["name"]
UI_ServerProfileTemplate_49_SP[0]["connectionSettings"]["connections"] = [
    {"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:" + network["general1"]},
    {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:" + network["mgmt"]},
    {"id": 3, "name": "ft_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:" + network["ft"]},
    {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:" + network["production"]},
    {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:" + network["production"]}]
UI_ServerProfileTemplate_55 = [copy.deepcopy(SPT_payload_with_net)]
UI_ServerProfileTemplate_55[0]["name"] = "UI_ServerProfileTemplate_55"
UI_ServerProfileTemplate_55[0]["firmware"] = {"manageFirmware": False, "firmwareBaselineUri": "", "forceInstallFirmware": False, "firmwareInstallType": "FirmwareOnlyOfflineMode",
                                              "firmwareActivationType": "Immediate"}
UI_ServerProfileTemplate_55[0]["sanStorage"] = {"hostOSType": "VMware (ESXi)", "manageSanStorage": True,
                                                "volumeAttachments": [{"id": 1,
                                                                       "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                       "bootVolumePriority": "NotBootable",
                                                                       "lunType": "Auto",
                                                                       "volumeUri": "v:" + svol["svol3"],
                                                                       "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]}]}

UI_ServerProfileTemplate_55_SP = [copy.deepcopy(SP_payload)]
UI_ServerProfileTemplate_55_SP[0]["name"] = "UI_ServerProfileTemplate_55_SP"
UI_ServerProfileTemplate_55_SP[0]["serverHardwareUri"] = ServerHardware[1]
UI_ServerProfileTemplate_55_SP[0]["serverProfileTemplateUri"] = "SPT:" + UI_ServerProfileTemplate_55[0]["name"]
UI_ServerProfileTemplate_55_SP[0]["firmware"] = {"manageFirmware": True, "firmwareBaselineUri": FirmwareVersion, "forceInstallFirmware": False, "firmwareInstallType": "FirmwareOnlyOfflineMode",
                                                 "firmwareActivationType": "Immediate"}
UI_ServerProfileTemplate_55_SP[0]["sanStorage"] = {"hostOSType": "VMware (ESXi)", "manageSanStorage": True,
                                                   "volumeAttachments": [{"id": 1,
                                                                          "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                          "bootVolumePriority": "NotBootable",
                                                                          "lunType": "Auto",
                                                                          "volumeUri": "v:" + svol["svol3"],
                                                                          "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]},
                                                                         {"id": 2,
                                                                          "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                          "bootVolumePriority": "NotBootable",
                                                                          "lunType": "Auto",
                                                                          "volumeUri": "v:" + svol["svol4"],
                                                                          "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]}]}

UI_ServerProfileTemplate_57_1 = [copy.deepcopy(SPT_payload_with_net)]
UI_ServerProfileTemplate_57_1[0]["name"] = "UI_ServerProfileTemplate_57"
UI_ServerProfileTemplate_57_1[0]["firmware"] = {"manageFirmware": False, "firmwareBaselineUri": "", "forceInstallFirmware": False, "firmwareInstallType": "FirmwareOnlyOfflineMode",
                                                "firmwareActivationType": "Immediate"}
UI_ServerProfileTemplate_57_1[0]["sanStorage"] = {"hostOSType": "VMware (ESXi)", "manageSanStorage": True,
                                                  "volumeAttachments": [{"id": 1,
                                                                         "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                         "bootVolumePriority": "NotBootable",
                                                                         "lunType": "Auto",
                                                                         "volumeUri": "v:" + svol["svol3"],
                                                                         "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]},
                                                                        {"id": 2,
                                                                         "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                         "bootVolumePriority": "NotBootable",
                                                                         "lunType": "Auto",
                                                                         "volumeUri": "v:" + svol["svol4"],
                                                                         "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]}]}

UI_ServerProfileTemplate_57_SP_1 = [copy.deepcopy(SP_payload)]
UI_ServerProfileTemplate_57_SP_1[0]["name"] = "UI_ServerProfileTemplate_57_SP"
UI_ServerProfileTemplate_57_SP_1[0]["serverHardwareUri"] = ServerHardware[1]
UI_ServerProfileTemplate_57_SP_1[0]["serverProfileTemplateUri"] = "SPT:" + UI_ServerProfileTemplate_57_1[0]["name"]
UI_ServerProfileTemplate_57_SP_1[0]["firmware"] = {"manageFirmware": True, "firmwareBaselineUri": FirmwareVersion, "forceInstallFirmware": False, "firmwareInstallType": "FirmwareOnlyOfflineMode",
                                                   "firmwareActivationType": "Immediate"}
UI_ServerProfileTemplate_57_SP_1[0]["sanStorage"] = {"hostOSType": "VMware (ESXi)", "manageSanStorage": True,
                                                     "volumeAttachments": [{"id": 1,
                                                                            "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                            "bootVolumePriority": "NotBootable",
                                                                            "lunType": "Auto",
                                                                            "volumeUri": "v:" + svol["svol3"],
                                                                            "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]},
                                                                           {"id": 2,
                                                                            "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                            "bootVolumePriority": "NotBootable",
                                                                            "lunType": "Auto",
                                                                            "volumeUri": "v:" + svol["svol4"],
                                                                            "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]}]}

UI_ServerProfileTemplate_29 = [copy.deepcopy(SPT_payload_with_net)]
UI_ServerProfileTemplate_29[0]["name"] = "UI_ServerProfileTemplate_29"
UI_ServerProfileTemplate_29[0]["boot"]["manageBoot"] = False
UI_ServerProfileTemplate_29[0]["bios"]["manageBios"] = False
UI_ServerProfileTemplate_29_SP = [copy.deepcopy(SP_payload)]
UI_ServerProfileTemplate_29_SP[0]["name"] = "UI_ServerProfileTemplate_29_SP"
UI_ServerProfileTemplate_29_SP[0]["serverProfileTemplateUri"] = "SPT:" + UI_ServerProfileTemplate_29[0]["name"]
UI_ServerProfileTemplate_29_SP[0]["boot"]["manageBoot"] = False
UI_ServerProfile_SP_Power_On = ServerHardware[0]
UI_ServerProfileTemplate_29_update = copy.deepcopy(UI_ServerProfileTemplate_29)
UI_ServerProfileTemplate_29_update[0]["boot"] = {'manageBoot': True, 'order': ['HardDisk', 'USB', 'CD', 'PXE', 'Floppy']}
UI_ServerProfileTemplate_29_update[0]["bios"]["manageBios"] = True
profile_compliance_UI_ServerProfile_SP = {"name": "UI_ServerProfileTemplate_29_SP",
                                          "compliance-preview": {
                                              "type": "ServerProfileCompliancePreviewV1",
                                              "automaticUpdates": ["REGEX:Change boot order to .*", "REGEX:Change BIOS settings to managed by profile."],
                                              "manualUpdates": []
                                          }
                                          }
profile_compliance_UI_ServerProfile_SP1 = {"name": "UI_ServerProfileTemplate_29_SP",
                                           "compliance-preview": {
                                               "type": "ServerProfileCompliancePreviewV1",
                                               "automaticUpdates": [],
                                               "manualUpdates": []}
                                           }
UI_ServerProfile_SP_Power_Off = ServerHardware[0]
UI_ServerProfileTemplate_29_sp_SPT = copy.deepcopy(UI_ServerProfileTemplate_29_SP)
UI_ServerProfileTemplate_29_sp_SPT[0]["boot"] = {'manageBoot': True, 'order': ['HardDisk', 'USB', 'CD', 'PXE', 'Floppy']}
UI_ServerProfileTemplate_29_sp_SPT[0]["bios"]["manageBios"] = True
UI_ServerProfileTemplate_32 = [copy.deepcopy(SPT_payload_with_net)]
UI_SPT_32_connections = [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                          "networkUri": "ETH:" + network["general1"]},
                         {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                          "networkUri": "ETH:" + network["mgmt"]},
                         {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500",
                          "networkUri": "FC:" + network["fc1"]}
                         ]
UI_ServerProfileTemplate_32[0]["name"] = "UI_ServerProfileTemplate_32"
UI_ServerProfileTemplate_32[0]["connectionSettings"]["connections"] = UI_SPT_32_connections
UI_ServerProfileTemplate_32_SP1 = copy.deepcopy(SP_payload)
UI_ServerProfileTemplate_32_SP1["name"] = "UI_ServerProfileTemplate_32_SP1"
UI_ServerProfileTemplate_32_SP1["serverProfileTemplateUri"] = "SPT:" + UI_ServerProfileTemplate_32[0]["name"]
UI_ServerProfileTemplate_32_SP1["connectionSettings"]["connections"] = UI_SPT_32_connections
UI_ServerProfileTemplate_32_SP2 = copy.deepcopy(SP_payload)
UI_ServerProfileTemplate_32_SP2["name"] = "UI_ServerProfileTemplate_32_SP2"
UI_ServerProfileTemplate_32_SP2["serverHardwareUri"] = ServerHardware[1]
UI_ServerProfileTemplate_32_SP2["serverProfileTemplateUri"] = "SPT:" + UI_ServerProfileTemplate_32[0]["name"]
UI_ServerProfileTemplate_32_SP2["connectionSettings"]["connections"] = UI_SPT_32_connections
UI_ServerProfileTemplate_32_SP = [UI_ServerProfileTemplate_32_SP1, UI_ServerProfileTemplate_32_SP2]
UI_ServerProfileTemplate_32_SP1_Update = copy.deepcopy(UI_ServerProfileTemplate_32)
UI_SPT_32_connections_1 = [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                            "networkUri": "ETH:" + network["general1"]},
                           {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                            "networkUri": "ETH:" + network["mgmt"]},
                           {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500",
                            "networkUri": "FC:" + network["fc1"]},
                           {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                            "networkUri": "ETH:" + network["production"]}]
UI_ServerProfileTemplate_32_SP1_Update[0]["connectionSettings"]["connections"] = UI_SPT_32_connections_1
SPT_32_firmware = {"manageFirmware": True, "firmwareBaselineUri": FirmwareVersion, "forceInstallFirmware": False,
                   "firmwareInstallType": "FirmwareOnlyOfflineMode", "firmwareActivationType": "Immediate"}
UI_ServerProfileTemplate_32_SP1_Update[0]["firmware"] = SPT_32_firmware
UI_ServerProfileTemplate_32_SP1_Update[0]["bios"]["manageBios"] = True
UI_ServerProfileTemplate_32_SP1_Update[0]["boot"]["order"] = ['CD', 'Floppy', 'HardDisk', 'USB', 'PXE']
profile_compliance_UI_ServerProfileTemplate_32_SP = {"name": UI_ServerProfileTemplate_32_SP1["name"],
                                                     "compliance-preview": {
                                                         "type": "ServerProfileCompliancePreviewV1",
                                                         "automaticUpdates": ["REGEX:Create a connection to network .*",
                                                                              "REGEX:Change firmware baseline to .*",
                                                                              "REGEX:Change firmware installation method to Firmware only.",
                                                                              "REGEX:Change firmware activation type to Immediately.",
                                                                              "REGEX:Change boot order to .*",
                                                                              "REGEX:Change BIOS settings to managed by profile."],
                                                         "manualUpdates": []}
                                                     }
profile_compliance_UI_ServerProfileTemplate_32_SP1 = {"name": UI_ServerProfileTemplate_32_SP2["name"],
                                                      "compliance-preview": {
                                                          "type": "ServerProfileCompliancePreviewV1",
                                                          "automaticUpdates": ["REGEX:Create a connection to network .*", "REGEX:Change firmware baseline to .*", "REGEX:Change firmware installation method to Firmware only.", "REGEX:Change firmware activation type to Immediately.", "REGEX:Change boot order to .*", "REGEX:Change BIOS settings to managed by profile."],
                                                          "manualUpdates": []}
                                                      }

ServerProfileTemplate_12_SPT = [copy.deepcopy(SPT_payload_with_net)]
ServerProfileTemplate_12_SPT[0]["name"] = "ServerProfileTemplate_12_SPT"
ServerProfileTemplate_12_SP = [copy.deepcopy(SP_payload)]
ServerProfileTemplate_12_SP[0]["name"] = 'ServerProfileTemplate_12_SP'
ServerProfileTemplate_12_SP[0]["serverProfileTemplateUri"] = "SPT:" + ServerProfileTemplate_12_SPT[0]["name"]

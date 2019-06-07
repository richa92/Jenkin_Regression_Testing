

def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist

"""
#   gotDev team
def make_range_list(vrange):
    rlist = []
    for x in xrange(vrange['start'], (vrange['end'] + 1)):
        rlist.append(vrange['prefix'] + str(x) + vrange['suffix'])
    return rlist

def rlist(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist
"""

# spp = "SPPGen10Snap1_2016_1220_70"


spp = "bp-2017-05-02-00"

localfile1 = """C:\\133_Machine\\Firmware_bundle\\New_Snap1FF_Bundles\\Customised_Spp_For_Snap1FF_file\\bp-2017-05-02-00.iso"""
# localfile1= """C:\\Supportfiles\\C7K_sppfiles\\upgarde_one\\SPPGen10Snap1.2016_1220.70.iso"""
# localfile2= """C:\\Supportfiles\\C7K_sppfiles\\Downgrade_one\\bp-2016-06-24-00.iso"""
localfile2 = """C:\\133_Machine\\Firmware_bundle\\SPP2016100.2016_1015.191.iso"""

lig1_ethernetsettings = {'type': 'EthernetInterconnectSettingsV3', 'enableRichTLV': True, 'interconnectType': 'Ethernet'}

li_set1 = {"type": "EthernetInterconnectSettingsV201", "enableRichTLV": True, "enableTaggedLldp": True}
li_set2 = {"type": "EthernetInterconnectSettingsV201", "enableRichTLV": False, "enableTaggedLldp": True}
li_set3 = {"type": "EthernetInterconnectSettingsV201", "enableRichTLV": True, "enableTaggedLldp": False}
li_set4 = {"type": "EthernetInterconnectSettingsV201", "enableRichTLV": False, "enableTaggedLldp": False}
Abb = "SGH420HHYA, interconnect 3"
ICM_Alert1 = "Staging started for the interconnect " + Abb + " with firmware version 3.01 v7.2.1_38 from baseline"

#  Support dump

create_support_dump = [{"encrypt": True, "errorCode": "CI", "userName": "administrator", "password": "wpsthpvse1"}, {"encrypt": True, "errorCode": "CI", "userName": "backup", "password": "password"}, {"encrypt": True, "errorCode": "CI", "userName": "server", "password": "password"}]

# ${ICM_Alert2}                    Staging success for the interconnect SGH420HHYA, interconnect 3 with firmware version 3.01 v7.2.1_38 from baseline

# ${ICM_Alert3}                    Activation success for the interconnect SGH420HHYA, interconnect 3 with firmware version 3.01 v7.2.1_38 from baseline
# ${ICM_Alert4}                       Activation started for the interconnect SGH420HHYA, interconnect 3 with firmware version 3.01 v7.2.1_38 from baseline


apic_admin_credentials = {"aaaUser": {
    "attributes": {
        "name": "admin", "pwd": "password"}}}

apic_ip = ['10.10.0.203', '10.10.5.16']

li_spp_downgrade = {'command': 'UPDATE', 'sppUri': '/rest/firmware-drivers/{}'.format(spp), 'force': True}

li_spp_upgrade = {'command': 'UPDATE', 'sppUri': '/rest/firmware-drivers/bp-2016-06-24-00', 'force': 'true'}
li_spp_upgrade1 = {'command': 'STAGE', 'ethernetActivationDelay': '5', 'ethernetActivationType': 'OddEven', 'fcActivationDelay': '5', 'fcActivationType': 'Serial', 'force': 'true', 'sppUri': '/rest/firmware-drivers/{}'.format(spp)}
li_spp_upgrade2 = {'command': 'Stage', 'sppUri': '/rest/firmware-drivers/bp-2016-06-24-00', 'force': 'true'}
li_spp_upgrade3 = {'command': 'ACTIVATE', 'sppUri': '/rest/firmware-drivers/bp-2016-06-24-00', 'force': 'true'}
li_spp_upgrade4 = {'command': 'Update', 'sppUri': '/rest/firmware-drivers/bp-2016-06-24-00', 'force': 'true'}
li_spp_upgrade5 = {'command': 'ACTIVATE', 'ethernetActivationDelay': '5', 'ethernetActivationType': 'OddEven', 'fcActivationDelay': '5', 'fcActivationType': 'Serial', 'force': 'true', 'sppUri': '/rest/firmware-drivers/{}'.format(spp)}
li_spp_upgrade6 = {"command": "UPDATE", "ethernetActivationDelay": "5", "ethernetActivationType": "Parallel", "fcActivationDelay": "5", "fcActivationType": "Parallel", "force": "true", "sppUri": "/rest/firmware-drivers/bp-2016-06-24-00"}
li_spp_upgrade6yf = {'command': 'UPDATE', 'ethernetActivationDelay': '0', 'ethernetActivationType': 'Parallel', 'fcActivationDelay': '0', 'fcActivationType': 'Parallel', 'force': 'false', 'sppUri': '/rest/firmware-drivers/{}'.format(spp)}
li_spp_upgrade7 = {'command': 'UPDATE', 'ethernetActivationDelay': '0', 'ethernetActivationType': 'Parallel', 'fcActivationDelay': '0', 'fcActivationType': 'Parallel', 'force': 'true', 'sppUri': '/rest/firmware-drivers/bp-2016-06-24-00'}
li_spp_upgrade_bug = {'command': 'UPDATE', 'ethernetActivationDelay': '5', 'ethernetActivationType': 'Parallel', 'fcActivationDelay': '5', 'fcActivationType': 'Parallel', 'force': True, 'sppUri': '/rest/firmware-drivers/{}'.format(spp)}
li_spp_upgrade6_same = {'command': 'UPDATE', 'ethernetActivationDelay': '5', 'ethernetActivationType': 'Parallel', 'fcActivationDelay': '5', 'fcActivationType': 'Parallel', 'force': 'false', 'sppUri': '/rest/firmware-drivers/bp-2016-06-24-00'}
li_spp_upgrade1_al = {'command': 'STAGE', 'ethernetActivationDelay': '5', 'ethernetActivationType': 'OddEven', 'fcActivationDelay': '5', 'fcActivationType': 'Serial', 'force': 'true', 'sppUri': '/rest/firmware-drivers/bp-2016-06-24-00'}
li_spp_upgrade1_ala = {'command': 'ACTIVATE', 'ethernetActivationDelay': '5', 'ethernetActivationType': 'OddEven', 'fcActivationDelay': '5', 'fcActivationType': 'Serial', 'force': 'true', 'sppUri': '/rest/firmware-drivers/bp-2016-06-24-00'}

li_spp_upgrade_Ranjan_bug = {'command': 'UPDATE', 'ethernetActivationDelay': '5', 'ethernetActivationType': 'Parallel', 'fcActivationDelay': '5', 'fcActivationType': 'Parallel', 'force': True, 'sppUri': '/rest/firmware-drivers/bp-2016-06-24-00'}

li_spp_upgrade1_test = {'command': 'STAGE', 'ethernetActivationDelay': '5', 'ethernetActivationType': 'OddEven', 'fcActivationDelay': '5', 'fcActivationType': 'Serial', 'force': 'true', 'sppUri': '/rest/firmware-drivers/bp-2016-06-24-00'}
li_spp_upgrade5_test = {'command': 'ACTIVATE', 'ethernetActivationDelay': '5', 'ethernetActivationType': 'OddEven', 'fcActivationDelay': '5', 'fcActivationType': 'Serial', 'force': 'true', 'sppUri': '/rest/firmware-drivers/bp-2016-06-24-00'}

li_spp_upgrade6yf_test = {'command': 'UPDATE', 'ethernetActivationDelay': '0', 'ethernetActivationType': 'Parallel', 'fcActivationDelay': '0', 'fcActivationType': 'Parallel', 'force': 'true', 'sppUri': '/rest/firmware-drivers/{}'.format(spp)}

New_li_spp_upgrade_li_tst = {"sppUri": "/rest/firmware-drivers/{}".format(spp), "command": "UPDATE", "force": "true", "ethernetActivationType": "OddEven", "ethernetActivationDelay": "5", "fcActivationType": "OddEven", "fcActivationDelay": "5"}

New_li_spp_upgrade_li_tst_h = {"sppUri": "/rest/firmware-drivers/{}".format(spp), "command": "UPDATE", "force": "true", "ethernetActivationType": "OddEven", "ethernetActivationDelay": "5", "fcActivationType": "OddEven", "fcActivationDelay": "5"}

New_li_spp_downgrade_li_tst = {"sppUri": "/rest/firmware-drivers/bp-2016-06-24-00", "command": "UPDATE", "force": "true", "ethernetActivationType": "OddEven", "ethernetActivationDelay": "5", "fcActivationType": "OddEven", "fcActivationDelay": "5"}

Demo_New_li_spp_upgrade_li_tst_h = {"sppUri": "/rest/firmware-drivers/{}".format(spp), "command": "UPDATE", "force": "true", "ethernetActivationType": "Parallel", "ethernetActivationDelay": "5", "fcActivationType": "Parallel", "fcActivationDelay": "5"}

Demo_New_li_spp_Downgrade_LI_li_tst_h = {"sppUri": "/rest/firmware-drivers/bp-2016-06-24-00", "command": "UPDATE", "force": "false", "ethernetActivationType": "Parallel", "ethernetActivationDelay": "5", "fcActivationType": "Parallel", "fcActivationDelay": "5"}

demo_New_li_spp_downgrade_li_tst_l = {"sppUri": "/rest/firmware-drivers/bp-2016-06-24-00", "command": "UPDATE", "force": "true", "ethernetActivationType": "Parallel", "ethernetActivationDelay": "5", "fcActivationType": "Parallel", "fcActivationDelay": "5"}

Demo_li_spp_upgrade5_test_l = {'command': 'ACTIVATE', 'ethernetActivationDelay': '5', 'ethernetActivationType': 'Parallel', 'fcActivationDelay': '5', 'fcActivationType': 'Parallel', 'force': 'true', 'sppUri': '/rest/firmware-drivers/bp-2016-06-24-00'}

Demo_li_spp_upgrade1_test_stg_l = {'command': 'STAGE', 'ethernetActivationDelay': '5', 'ethernetActivationType': 'OddEven', 'fcActivationDelay': '5', 'fcActivationType': 'Serial', 'force': 'true', 'sppUri': '/rest/firmware-drivers/{}'.format(spp)}
Demo_li_spp_upgrade1_test_stg_2 = {'command': 'STAGE', 'ethernetActivationDelay': '5', 'ethernetActivationType': 'OddEven', 'fcActivationDelay': '5', 'fcActivationType': 'Serial', 'force': 'true', 'sppUri': '/rest/firmware-drivers/{}'.format(spp)}

Demo_li_spp_upgrade5_active_add_nw_remove_higher = {'command': 'ACTIVATE', 'ethernetActivationDelay': '5', 'ethernetActivationType': 'Serial', 'fcActivationDelay': '5', 'fcActivationType': 'Serial', 'force': 'true', 'sppUri': '/rest/firmware-drivers/{}'.format(spp)}

li_spp_upgrade_Ranjan_bug_new_format = {"sppUri": "/rest/firmware-drivers/{}".format(spp), "command": "UPDATE", "force": True, "ethernetActivationType": "Parallel", "ethernetActivationDelay": "5", "fcActivationType": "Parallel", "fcActivationDelay": "5"}

Demo_New_li_spp_upgrade_li_tst_delay_empty = {"sppUri": "/rest/firmware-drivers/{}".format(spp), "command": "UPDATE", "force": "true", "ethernetActivationType": "Parallel", "ethernetActivationDelay": None, "fcActivationType": "Parallel", "fcActivationDelay": None}

# Multi_lis_tests

Demo_li_Stagingon_oneLi = {'command': 'STAGE', 'ethernetActivationDelay': '5', 'ethernetActivationType': 'OddEven', 'fcActivationDelay': '5', 'fcActivationType': 'Serial', 'force': 'true', 'sppUri': '/rest/firmware-drivers/bp-2016-06-24-00'}

Demo_li_Stagingon_allLi = {'command': 'STAGE', 'ethernetActivationDelay': '5', 'ethernetActivationType': 'OddEven', 'fcActivationDelay': '5', 'fcActivationType': 'Serial', 'force': 'true', 'sppUri': '/rest/firmware-drivers/{}'.format(spp)}

Demo_li_activate_on_one_higher_one = {'command': 'ACTIVATE', 'ethernetActivationDelay': '5', 'ethernetActivationType': 'Parallel', 'fcActivationDelay': '5', 'fcActivationType': 'Parallel', 'force': 'true', 'sppUri': '/rest/firmware-drivers/{}'.format(spp)}

Demo_li_activate_on_one_higher_two = {'command': 'ACTIVATE', 'ethernetActivationDelay': '5', 'ethernetActivationType': 'Parallel', 'fcActivationDelay': '5', 'fcActivationType': 'Parallel', 'force': 'true', 'sppUri': '/rest/firmware-drivers/{}'.format(spp)}


Demo_upgrade_li_1_multi_lis_tests1_higher = {"sppUri": "/rest/firmware-drivers/{}".format(spp), "command": "UPDATE", "force": "true", "ethernetActivationType": "Parallel", "ethernetActivationDelay": "5", "fcActivationType": "Parallel", "fcActivationDelay": "5"}
Demo_upgrade_li_2_multi_lis_tests2_higher = {"sppUri": "/rest/firmware-drivers/{}".format(spp), "command": "UPDATE", "force": "true", "ethernetActivationType": "Parallel", "ethernetActivationDelay": "5", "fcActivationType": "Parallel", "fcActivationDelay": "5"}

Demo_upgrade_li_1_multi_lis_stage_lower = {"sppUri": "/rest/firmware-drivers/bp-2016-06-24-00", "command": "UPDATE", "force": "true", "ethernetActivationType": "Parallel", "ethernetActivationDelay": "5", "fcActivationType": "Parallel", "fcActivationDelay": "5"}

Demo_upgrade_li_1_multi_lis_tests1_lower_bb1 = {"sppUri": "/rest/firmware-drivers/bp-2016-06-24-00", "command": "UPDATE", "force": "true", "ethernetActivationType": "Parallel", "ethernetActivationDelay": "5", "fcActivationType": "Parallel", "fcActivationDelay": "5"}
# Tests
Demo_li_spp_upgrade1_test_stg_higher = {'command': 'STAGE', 'ethernetActivationDelay': '5', 'ethernetActivationType': 'OddEven', 'fcActivationDelay': '5', 'fcActivationType': 'Serial', 'force': 'true', 'sppUri': '/rest/firmware-drivers/{}'.format(spp)}

Demo_li_spp_upgrade1_test_stg_serial_higher = {'command': 'STAGE', 'ethernetActivationDelay': '5', 'ethernetActivationType': 'Serial', 'fcActivationDelay': '5', 'fcActivationType': 'Serial', 'force': 'true', 'sppUri': '/rest/firmware-drivers/{}'.format(spp)}

Demo_li_spp_DOWNGRADELIgrade1_test_stg_serial_higher = {'command': 'STAGE', 'ethernetActivationDelay': '5', 'ethernetActivationType': 'Serial', 'fcActivationDelay': '5', 'fcActivationType': 'Serial', 'force': 'true', 'sppUri': '/rest/firmware-drivers/bp-2016-06-24-00'}

Demo_li_spp_upgrade1_test_stg_oddeven_higher = {'command': 'STAGE', 'ethernetActivationDelay': '5', 'ethernetActivationType': 'OddEven', 'fcActivationDelay': '5', 'fcActivationType': 'OddEven', 'force': 'true', 'sppUri': '/rest/firmware-drivers/{}'.format(spp)}

Demo_li_spp_dwngrd1_test_stg_oddeven_higher = {'command': 'STAGE', 'ethernetActivationDelay': '5', 'ethernetActivationType': 'OddEven', 'fcActivationDelay': '5', 'fcActivationType': 'OddEven', 'force': 'true', 'sppUri': '/rest/firmware-drivers/bp-2016-06-24-00'}

Demo_li_spp_upgrade5_test_higher = {'command': 'ACTIVATE', 'ethernetActivationDelay': '5', 'ethernetActivationType': 'Parallel', 'fcActivationDelay': '5', 'fcActivationType': 'Parallel', 'force': 'true', 'sppUri': '/rest/firmware-drivers/{}'.format(spp)}

Viren_Demo_li_spp_upgrade5_test_higher = {'command': 'ACTIVATE', 'ethernetActivationDelay': '5', 'ethernetActivationType': 'Parallel', 'fcActivationDelay': '5', 'fcActivationType': 'Parallel', 'force': 'true', 'sppUri': '/rest/firmware-drivers/{}'.format(spp)}

Demo_li_spp_upgrade5_test_serial_higher = {'command': 'ACTIVATE', 'ethernetActivationDelay': '5', 'ethernetActivationType': 'Serial', 'fcActivationDelay': '5', 'fcActivationType': 'Serial', 'force': 'true', 'sppUri': '/rest/firmware-drivers/{}'.format(spp)}

Demo_li_spp_upgrade5_test_oddeven_active_higher = {'command': 'ACTIVATE', 'ethernetActivationDelay': '5', 'ethernetActivationType': 'Serial', 'fcActivationDelay': '5', 'fcActivationType': 'Serial', 'force': 'true', 'sppUri': '/rest/firmware-drivers/{}'.format(spp)}

Demo_li_spp_downgrade_test_oddeven_active_higher = {'command': 'ACTIVATE', 'ethernetActivationDelay': '5', 'ethernetActivationType': 'OddEven', 'fcActivationDelay': '5', 'fcActivationType': 'OddEven', 'force': 'true', 'sppUri': '/rest/firmware-drivers/bp-2016-06-24-00'}


# Demo_li_spp_upgrade1_test_stg_lower = {'command':'STAGE','ethernetActivationDelay':'5','ethernetActivationType':'OddEven','fcActivationDelay':'5','fcActivationType':'Serial','force': 'true','sppUri':'/rest/firmware-drivers/bp-2016-06-24-00'}

Demo_li_spp_upgrade1_test_stg_lower = {'command': 'STAGE', 'ethernetActivationDelay': '5', 'ethernetActivationType': 'OddEven', 'fcActivationDelay': '5', 'fcActivationType': 'Serial', 'force': 'true', 'sppUri': '/rest/firmware-drivers/SPP2016100_2016_1015_191'}

Demo_li_spp_UPGRADEgrade1_test_stg_lower = {'command': 'STAGE', 'ethernetActivationDelay': '5', 'ethernetActivationType': 'OddEven', 'fcActivationDelay': '5', 'fcActivationType': 'Serial', 'force': 'true', 'sppUri': '/rest/firmware-drivers/{}'.format(spp)}

Demo_li_spp_upgrade5_test_act_lower = {'command': 'ACTIVATE', 'ethernetActivationDelay': '5', 'ethernetActivationType': 'OddEven', 'fcActivationDelay': '5', 'fcActivationType': 'OddEven', 'force': 'true', 'sppUri': '/rest/firmware-drivers/SPP2016100_2016_1015_191'}

# Demo_li_spp_upgrade5_test_act_lower= {'command':'ACTIVATE','ethernetActivationDelay':'5','ethernetActivationType':'OddEven','fcActivationDelay':'5','fcActivationType':'OddEven','force': 'true','sppUri':'/rest/firmware-drivers/bp-2016-06-24-00'}

Demo_li_spp_upgrade5_Serial_act_lower = {'command': 'ACTIVATE', 'ethernetActivationDelay': '5', 'ethernetActivationType': 'Serial', 'fcActivationDelay': '5', 'fcActivationType': 'Serial', 'force': 'true', 'sppUri': '/rest/firmware-drivers/SPP2016100_2016_1015_191'}


Demo_li_spp_LIUPGRADEgrade5_test_act_lower = {'command': 'ACTIVATE', 'ethernetActivationDelay': '5', 'ethernetActivationType': 'Parallel', 'fcActivationDelay': '5', 'fcActivationType': 'Parallel', 'force': 'true', 'sppUri': '/rest/firmware-drivers/{}'.format(spp)}

# demo_New_li_spp_downgrade_li_tst_lower_l = {"sppUri":"/rest/firmware-drivers/bp-2016-06-24-00","command":"UPDATE","force":"true","ethernetActivationType":"Parallel","ethernetActivationDelay":"5","fcActivationType":"Parallel","fcActivationDelay":"5"}

demo_New_li_spp_downgrade_li_tst_lower_l = {"sppUri": "/rest/firmware-drivers/SPP2016100_2016_1015_191", "command": "UPDATE", "force": "true", "ethernetActivationType": "Parallel", "ethernetActivationDelay": "5", "fcActivationType": "Parallel", "fcActivationDelay": "5"}


Demo_New_li_spp_upgrade_serial_li_tst_higher = {"sppUri": "/rest/firmware-drivers/{}".format(spp), "command": "UPDATE", "force": "true", "ethernetActivationType": "Serial", "ethernetActivationDelay": "5", "fcActivationType": "Serial", "fcActivationDelay": "5"}

demo_New_li_spp_downgrade_Serial_li_tst_lower_l = {"sppUri": "/rest/firmware-drivers/bp-2016-06-24-00", "command": "UPDATE", "force": "true", "ethernetActivationType": "Serial", "ethernetActivationDelay": "5", "fcActivationType": "Serial", "fcActivationDelay": "5"}


demo_New_li_spp_downgrade_li_serial_lower_l = {"sppUri": "/rest/firmware-drivers/bp-2016-06-24-00", "command": "UPDATE", "force": "true", "ethernetActivationType": "Serial", "ethernetActivationDelay": "5", "fcActivationType": "Serial", "fcActivationDelay": "5"}

Demo_New_li_spp_upgrade_Oddevenb_li_tst_higher = {"sppUri": "/rest/firmware-drivers/{}".format(spp), "command": "UPDATE", "force": "true", "ethernetActivationType": "OddEven", "ethernetActivationDelay": "5", "fcActivationType": "OddEven", "fcActivationDelay": "5"}
Demo_New_li_spp_upgrade_Oddevenb_li_same_ver_higher = {"sppUri": "/rest/firmware-drivers/{}".format(spp), "command": "UPDATE", "force": "true", "ethernetActivationType": "OddEven", "ethernetActivationDelay": "5", "fcActivationType": "OddEven", "fcActivationDelay": "5"}

Demo_New_li_spp_upgrade_Oddevenb_li_no_flag_higher = {"sppUri": "/rest/firmware-drivers/{}".format(spp), "command": "UPDATE", "force": "false", "ethernetActivationType": "OddEven", "ethernetActivationDelay": "5", "fcActivationType": "OddEven", "fcActivationDelay": "5"}

le_spp1 = {'forceInstallFirmware': 'true', 'firmwareBaselineUri': '/rest/firmware-drivers/SPPgen9snap6_2015_1027_19',
           'firmwareUpdateOn': 'SharedInfrastructureAndServerProfiles',
           'logicalInterconnectUpdateMode': 'Parallel',
           'validateIfLIFirmwareUpdateIsNonDisruptive': 'false',
           'updateFirmwareOnUnmanagedInterconnect': 'true'}
Tr = 'true'

le_sppnew = {'op': 'replace', 'path': '/firmware', 'value': {'firmwareBaselineUri': '/rest/firmware-drivers/SPPgen9snap6_2015_1027_19', 'forceInstallFirmware': 'true', 'firmwareUpdateOn': 'SharedInfrastructureOnly'}}
le_spp_pp = {"op": "replace", "path": "/firmware", "value": {"firmwareBaselineUri": "/rest/firmware-drivers/bp-2016-06-24-00", "forceInstallFirmware": "true", "firmwareUpdateOn": "SharedInfrastructureOnly"}}

le_spp_pp_OA_onlyf = {"op": "replace", "path": "/firmware", "value": {"firmwareBaselineUri": "/rest/firmware-drivers/bp-2016-06-24-00", "forceInstallFirmware": "false", "firmwareUpdateOn": "EnclosureOnly"}}
le_spp_pp_OA_onlyf1 = {"op": "replace", "path": "/firmware", "value": {"firmwareBaselineUri": "/rest/firmware-drivers/bp-2016-06-24-00", "forceInstallFirmware": "true", "firmwareUpdateOn": "EnclosureOnly"}}
hple_spp_pp_OA_onlyf1 = {"forceInstallFirmware": True, "firmwareBaselineUri": "/rest/firmware-drivers/{}".format(spp),
                         "firmwareUpdateOn": "EnclosureOnly",
                         "logicalInterconnectUpdateMode": "Parallel",
                         "validateIfLIFirmwareUpdateIsNonDisruptive": False, }

hple_spp_pp_OA_onlyf1_BB = {"forceInstallFirmware": True, "firmwareBaselineUri": "/rest/firmware-drivers/{}".format(spp),
                            "firmwareUpdateOn": "EnclosureOnly",
                            "logicalInterconnectUpdateMode": "Parallel",
                            "validateIfLIFirmwareUpdateIsNonDisruptive": False, }

hple_spp_pp_OA_onlyf = {"forceInstallFirmware": False, "firmwareBaselineUri": "/rest/firmware-drivers/bp-2016-06-24-00",
                        "firmwareUpdateOn": "EnclosureOnly",
                        "logicalInterconnectUpdateMode": "Parallel",
                        "validateIfLIFirmwareUpdateIsNonDisruptive": False, }

le_spp_pp_sh_inf_only = {"op": "replace", "path": "/firmware", "value": {"firmwareBaselineUri": "/rest/firmware-drivers/bp-2016-06-24-00", "forceInstallFirmware": "true", "firmwareUpdateOn": "SharedInfrastructureOnly"}}
le_spp_pp_sh_inf_onlyf = {"op": "replace", "path": "/firmware", "value": {"firmwareBaselineUri": "/rest/firmware-drivers/bp-2016-06-24-00", "forceInstallFirmware": "false", "firmwareUpdateOn": "SharedInfrastructureOnly"}}

hple_spp_pp_sh_inf_onlyf = {"forceInstallFirmware": False, "firmwareBaselineUri": "/rest/firmware-drivers/bp-2016-06-24-00",
                            "firmwareUpdateOn": "SharedInfrastructureOnly",
                            "logicalInterconnectUpdateMode": "Parallel",
                            "validateIfLIFirmwareUpdateIsNonDisruptive": False, }

le_spp_pp_sh_inf_prf_only = {"op": "replace", "path": "/firmware", "value": {"firmwareBaselineUri": "/rest/firmware-drivers/bp-2016-06-24-00", "forceInstallFirmware": "true", "firmwareUpdateOn": "SharedInfrastructureAndServerProfiles"}}

hple_spp_pp_sh_inf_prf_only = {"forceInstallFirmware": True, "firmwareBaselineUri": "/rest/firmware-drivers/{}".format(spp),
                               "firmwareUpdateOn": "SharedInfrastructureAndServerProfiles",
                               "logicalInterconnectUpdateMode": "Parallel",
                               "validateIfLIFirmwareUpdateIsNonDisruptive": False, }

le_spp_pp_sh_inf_prf_onlyf = {"op": "replace", "path": "/firmware", "value": {"firmwareBaselineUri": "/rest/firmware-drivers/bp-2016-06-24-00", "forceInstallFirmware": "false", "firmwareUpdateOn": "SharedInfrastructureAndServerProfiles"}}
hple_spp_pp_sh_inf_prf_onlyf = {"forceInstallFirmware": False, "firmwareBaselineUri": "/rest/firmware-drivers/bp-2016-06-24-00",
                                "firmwareUpdateOn": "SharedInfrastructureAndServerProfiles",
                                "logicalInterconnectUpdateMode": "Parallel",
                                "validateIfLIFirmwareUpdateIsNonDisruptive": False, }
new_le_spp_pp_sh_inf_only = {"op": "replace", "path": "/firmware", "value": {"firmwareBaselineUri": "/rest/firmware-drivers/bp-2016-06-24-00", "forceInstallFirmware": True, "firmwareUpdateOn": "SharedInfrastructureOnly"}}
new_le_spp_pp_sh_inf_only_bug = {"op": "replace", "path": "/firmware", "value": {"firmwareBaselineUri": "/rest/firmware-drivers/bp-2016-06-24-00", "forceInstallFirmware": 'true', "firmwareUpdateOn": "SharedInfrastructureOnly"}}

hple_spp_bb_upgrade_lw_with_flag_OA = {"forceInstallFirmware": True, "firmwareBaselineUri": "/rest/firmware-drivers/{}".format(spp),
                                       "firmwareUpdateOn": "EnclosureOnly",
                                       "logicalInterconnectUpdateMode": "Parallel",
                                       "validateIfLIFirmwareUpdateIsNonDisruptive": False, }

hple_spp_bb_upgrade_lw_with_flag_sh_prifile = {"forceInstallFirmware": True, "firmwareBaselineUri": "/rest/firmware-drivers/{}".format(spp),
                                               "firmwareUpdateOn": "SharedInfrastructureAndServerProfiles",
                                               "logicalInterconnectUpdateMode": "Parallel",
                                               "validateIfLIFirmwareUpdateIsNonDisruptive": False, }


hple_spp_bb = {"forceInstallFirmware": True, "firmwareBaselineUri": "/rest/firmware-drivers/{}".format(spp),
               "firmwareUpdateOn": "SharedInfrastructureOnly",
               "logicalInterconnectUpdateMode": "Parallel",
               "validateIfLIFirmwareUpdateIsNonDisruptive": False, }

hple_spp_bb_upgrade_lw_no_flag = {"forceInstallFirmware": False, "firmwareBaselineUri": "/rest/firmware-drivers/{}".format(spp),
                                  "firmwareUpdateOn": "SharedInfrastructureOnly",
                                  "logicalInterconnectUpdateMode": "Parallel",
                                  "validateIfLIFirmwareUpdateIsNonDisruptive": False, }

hple_spp_bb_upgrade_lw_with_flag = {"forceInstallFirmware": True, "firmwareBaselineUri": "/rest/firmware-drivers/{}".format(spp),
                                    "firmwareUpdateOn": "SharedInfrastructureOnly",
                                    "logicalInterconnectUpdateMode": "Parallel",
                                    "validateIfLIFirmwareUpdateIsNonDisruptive": False, }

hple_spp_bb_upgrade_lw_with_flag_h = {"forceInstallFirmware": True, "firmwareBaselineUri": "/rest/firmware-drivers/{}".format(spp),
                                      "firmwareUpdateOn": "SharedInfrastructureOnly",
                                      "logicalInterconnectUpdateMode": "Parallel",
                                      "validateIfLIFirmwareUpdateIsNonDisruptive": False, }

hple_spp_bb_upgrade_lw_with_flag_h_snap6 = {"forceInstallFirmware": True, "firmwareBaselineUri": "/rest/firmware-drivers/SPPgen9snap6_2015_1027_19",
                                            "firmwareUpdateOn": "SharedInfrastructureOnly",
                                            "logicalInterconnectUpdateMode": "Parallel",
                                            "validateIfLIFirmwareUpdateIsNonDisruptive": False, }

hple_spp_bb_nw = {"forceInstallFirmware": True, "firmwareBaselineUri": "/rest/firmware-drivers/bp-2016-06-24-00",
                  "firmwareUpdateOn": "SharedInfrastructureOnly",
                  "logicalInterconnectUpdateMode": "Parallel",
                  "validateIfLIFirmwareUpdateIsNonDisruptive": False, }

hple_spp_bb_nw_lw = {"forceInstallFirmware": True, "firmwareBaselineUri": "/rest/firmware-drivers/bp-2016-06-24-00",
                     "firmwareUpdateOn": "SharedInfrastructureOnly",
                     "logicalInterconnectUpdateMode": "Parallel",
                     "validateIfLIFirmwareUpdateIsNonDisruptive": False, }
# Test LE flow

hple_spp_bb_upgrade_lower_with_No_flag_OA = {"forceInstallFirmware": True, "firmwareBaselineUri": "/rest/firmware-drivers/bp-2016-06-24-00",
                                             "firmwareUpdateOn": "EnclosureOnly",
                                             "logicalInterconnectUpdateMode": "Parallel",
                                             "validateIfLIFirmwareUpdateIsNonDisruptive": False, }

hple_spp_bb_upgrade__with_No_flag_OAonly = {"forceInstallFirmware": False, "firmwareBaselineUri": "/rest/firmware-drivers/{}".format(spp),
                                            "firmwareUpdateOn": "EnclosureOnly",
                                            "logicalInterconnectUpdateMode": "Parallel",
                                            "validateIfLIFirmwareUpdateIsNonDisruptive": False, }

hple_spp_bb_upgrade_higher_with_no_flag_sh_prifile = {"forceInstallFirmware": True, "firmwareBaselineUri": "/rest/firmware-drivers/{}".format(spp),
                                                      "firmwareUpdateOn": "SharedInfrastructureAndServerProfiles",
                                                      "logicalInterconnectUpdateMode": "Parallel",
                                                      "validateIfLIFirmwareUpdateIsNonDisruptive": False, }

hple_spp_bb_upgrade_shareinfraonly_without_flag_upgrade_h = {"forceInstallFirmware": False, "firmwareBaselineUri": "/rest/firmware-drivers/{}".format(spp),
                                                             "firmwareUpdateOn": "SharedInfrastructureOnly",
                                                             "logicalInterconnectUpdateMode": "Parallel",
                                                             "validateIfLIFirmwareUpdateIsNonDisruptive": False, }

hple_spp_bb_downgrade_shareinfraonly_without_flag_dwngrade_h = {"forceInstallFirmware": True, "firmwareBaselineUri": "/rest/firmware-drivers/bp-2016-06-24-00",
                                                                "firmwareUpdateOn": "SharedInfrastructureOnly",
                                                                "logicalInterconnectUpdateMode": "Parallel",
                                                                "validateIfLIFirmwareUpdateIsNonDisruptive": False, }

hple_spp_bb_upgrade_sh_infra_with_flag_higher = {"forceInstallFirmware": True, "firmwareBaselineUri": "/rest/firmware-drivers/{}".format(spp),
                                                 "firmwareUpdateOn": "SharedInfrastructureOnly",
                                                 "logicalInterconnectUpdateMode": "Parallel",
                                                 "validateIfLIFirmwareUpdateIsNonDisruptive": False, }

LE_UPGRADE_SH_INFRA_WITH_OUT_FLAG = {"forceInstallFirmware": False, "firmwareBaselineUri": "/rest/firmware-drivers/{}".format(spp),
                                     "firmwareUpdateOn": "SharedInfrastructureOnly",
                                     "logicalInterconnectUpdateMode": "Parallel",
                                     "validateIfLIFirmwareUpdateIsNonDisruptive": False, }

hple_spp_bb_downgrade_sh_infra_with_flag_higher = {"forceInstallFirmware": True, "firmwareBaselineUri": "/rest/firmware-drivers/bp-2016-06-24-00",
                                                   "firmwareUpdateOn": "SharedInfrastructureOnly",
                                                   "logicalInterconnectUpdateMode": "Parallel",
                                                   "validateIfLIFirmwareUpdateIsNonDisruptive": False, }

# LE_DOWNGRADE_SH_INFRA_WITH_FLAG = {"forceInstallFirmware": True,"firmwareBaselineUri":"/rest/firmware-drivers/bp-2016-06-24-00",
# "firmwareUpdateOn":"SharedInfrastructureOnly",
# "logicalInterconnectUpdateMode":"Parallel",
# "validateIfLIFirmwareUpdateIsNonDisruptive": False,}

LE_DOWNGRADE_SH_INFRA_WITH_FLAG = {"forceInstallFirmware": True, "firmwareBaselineUri": "/rest/firmware-drivers/SPP2016100_2016_1015_191",
                                   "firmwareUpdateOn": "SharedInfrastructureOnly",
                                   "logicalInterconnectUpdateMode": "Parallel",
                                   "validateIfLIFirmwareUpdateIsNonDisruptive": False, }


hple_spp_bb_upgrade_sh_infra_with_flag_not_set_spp_higher = {"forceInstallFirmware": True, "firmwareBaselineUri": "",
                                                             "firmwareUpdateOn": "SharedInfrastructureOnly",
                                                             "logicalInterconnectUpdateMode": "Parallel",
                                                             "validateIfLIFirmwareUpdateIsNonDisruptive": False, }

hple_spp_bb_upgrade_higher_with_flag_sh_prifile = {"forceInstallFirmware": True, "firmwareBaselineUri": "/rest/firmware-drivers/{}".format(spp),
                                                   "firmwareUpdateOn": "SharedInfrastructureAndServerProfiles",
                                                   "logicalInterconnectUpdateMode": "Parallel",
                                                   "validateIfLIFirmwareUpdateIsNonDisruptive": False, }

LE_UPGRADE_SH_INFRA_PROFILE_WITH_OUT_FLAG = {"forceInstallFirmware": False, "firmwareBaselineUri": "/rest/firmware-drivers/{}".format(spp),
                                             "firmwareUpdateOn": "SharedInfrastructureAndServerProfiles",
                                             "logicalInterconnectUpdateMode": "Parallel",
                                             "validateIfLIFirmwareUpdateIsNonDisruptive": False, }


hple_spp_bb_downgrade_higher_with_flag_sh_prifile = {"forceInstallFirmware": True, "firmwareBaselineUri": "/rest/firmware-drivers/bp-2016-06-24-00",
                                                     "firmwareUpdateOn": "SharedInfrastructureAndServerProfiles",
                                                     "logicalInterconnectUpdateMode": "Parallel",
                                                     "validateIfLIFirmwareUpdateIsNonDisruptive": False, }

hple_spp_bb_dwngrde_higher_with_flag_sh_prifile = {"forceInstallFirmware": True, "firmwareBaselineUri": "/rest/firmware-drivers/bp-2016-06-24-00",
                                                   "firmwareUpdateOn": "SharedInfrastructureAndServerProfiles",
                                                   "logicalInterconnectUpdateMode": "Parallel",
                                                   "validateIfLIFirmwareUpdateIsNonDisruptive": False, }

# LE_DOWNGRADE_SH_INFRA_PROFIL_WITH_FLAG ={"forceInstallFirmware": True,"firmwareBaselineUri":"/rest/firmware-drivers/bp-2016-06-24-00",
#        "firmwareUpdateOn":"SharedInfrastructureAndServerProfiles",
#       "logicalInterconnectUpdateMode":"Parallel",
#      "validateIfLIFirmwareUpdateIsNonDisruptive": False,}

LE_DOWNGRADE_SH_INFRA_PROFIL_WITH_FLAG = {"forceInstallFirmware": True, "firmwareBaselineUri": "/rest/firmware-drivers/SPP2016100_2016_1015_191",
                                          "firmwareUpdateOn": "SharedInfrastructureAndServerProfiles",
                                          "logicalInterconnectUpdateMode": "Parallel",
                                          "validateIfLIFirmwareUpdateIsNonDisruptive": False, }

# Negtive LI

li_spp_upgrade6_same_version = {"command": "UPDATE", "ethernetActivationDelay": "5", "ethernetActivationType": "Parallel", "fcActivationDelay": "5", "fcActivationType": "Parallel", "force": "false", "sppUri": "/rest/firmware-drivers/bp-2016-06-24-00"}

li_spp_upgrade6_downgrade_version = {"command": "UPDATE", "ethernetActivationDelay": "5", "ethernetActivationType": "Parallel", "fcActivationDelay": "5", "fcActivationType": "Parallel", "force": "false", "sppUri": "/rest/firmware-drivers/bp-2016-06-24-00"}

New_li_spp_upgrade_li_tst_same_h = {"sppUri": "/rest/firmware-drivers/{}".format(spp), "command": "UPDATE", "force": "false", "ethernetActivationType": "OddEven", "ethernetActivationDelay": "5", "fcActivationType": "OddEven", "fcActivationDelay": "5"}

New_li_spp_upgrade_li_tst_same_L = {"sppUri": "/rest/firmware-drivers/bp-2016-06-24-00", "command": "UPDATE", "force": "false", "ethernetActivationType": "OddEven", "ethernetActivationDelay": "5", "fcActivationType": "OddEven", "fcActivationDelay": "5"}

New_li_spp_upgrade_li_tst_same_hh = {"sppUri": "/rest/firmware-drivers/{}".format(spp), "command": "UPDATE", "force": "false", "ethernetActivationType": "OddEven", "ethernetActivationDelay": "5", "fcActivationType": "OddEven", "fcActivationDelay": "5"}

LI_NEGATIVE_upgrade_SAMEVERSION_WITH_OUT_FLAG = {"sppUri": "/rest/firmware-drivers/{}".format(spp), "command": "UPDATE", "force": "false", "ethernetActivationType": "OddEven", "ethernetActivationDelay": "5", "fcActivationType": "OddEven", "fcActivationDelay": "5"}


# lLI_NEGATIVE_DOWNGRADE_WITHOUT_FLAG= {"command":"UPDATE","ethernetActivationDelay":"5","ethernetActivationType":"Parallel","fcActivationDelay":"5","fcActivationType":"Parallel","force": "false","sppUri":"/rest/firmware-drivers/bp-2016-06-24-00"}

lLI_NEGATIVE_DOWNGRADE_WITHOUT_FLAG = {"command": "UPDATE", "ethernetActivationDelay": "5", "ethernetActivationType": "Parallel", "fcActivationDelay": "5", "fcActivationType": "Parallel", "force": "false", "sppUri": "/rest/firmware-drivers/SPP2016100_2016_1015_191"}

# Negtive LE

hple_spp_bb_nw_same = {"forceInstallFirmware": False, "firmwareBaselineUri": "/rest/firmware-drivers/bp-2016-06-24-00",
                       "firmwareUpdateOn": "SharedInfrastructureOnly",
                       "logicalInterconnectUpdateMode": "Parallel",
                       "validateIfLIFirmwareUpdateIsNonDisruptive": False, }
hple_spp_bb_nw_same_h = {"forceInstallFirmware": False, "firmwareBaselineUri": "/rest/firmware-drivers/{}".format(spp),
                         "firmwareUpdateOn": "SharedInfrastructureOnly",
                         "logicalInterconnectUpdateMode": "Parallel",
                         "validateIfLIFirmwareUpdateIsNonDisruptive": False, }

hple_spp_bb_upgrade_no_flag = {"forceInstallFirmware": False, "firmwareBaselineUri": "/rest/firmware-drivers/bp-2016-06-24-00",
                               "firmwareUpdateOn": "SharedInfrastructureOnly",
                               "logicalInterconnectUpdateMode": "Parallel",
                               "validateIfLIFirmwareUpdateIsNonDisruptive": False, }

hple_spp_pp_OA_onlyf_s_oa = {"forceInstallFirmware": False, "firmwareBaselineUri": "/rest/firmware-drivers/bp-2016-06-24-00",
                             "firmwareUpdateOn": "EnclosureOnly",
                             "logicalInterconnectUpdateMode": "Parallel",
                             "validateIfLIFirmwareUpdateIsNonDisruptive": False, }

hple_spp_pp_OA_onlyf_s_oa_h = {"forceInstallFirmware": False, "firmwareBaselineUri": "/rest/firmware-drivers/{}".format(spp),
                               "firmwareUpdateOn": "EnclosureOnly",
                               "logicalInterconnectUpdateMode": "Parallel",
                               "validateIfLIFirmwareUpdateIsNonDisruptive": False, }

hple_spp_pp_OA_onlyf_s_oa_Neg_lower = {"forceInstallFirmware": False, "firmwareBaselineUri": "/rest/firmware-drivers/bp-2016-06-24-00",
                                       "firmwareUpdateOn": "EnclosureOnly",
                                       "logicalInterconnectUpdateMode": "Parallel",
                                       "validateIfLIFirmwareUpdateIsNonDisruptive": False, }

hple_spp_pp_OA_onlyf_s_oa_Neg_higher = {"forceInstallFirmware": False, "firmwareBaselineUri": "/rest/firmware-drivers/{}".format(spp),
                                        "firmwareUpdateOn": "EnclosureOnly",
                                        "logicalInterconnectUpdateMode": "Parallel",
                                        "validateIfLIFirmwareUpdateIsNonDisruptive": False, }

OA_CREDENTIAL_DATA = {"oaIpAddress": "192.168.144.132", "oaUsername": "Administrator", "oaPassword": "Admin"}
admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}
network_admin = {'userName': 'network', 'password': 'networkadmin'}
storage_admin = {'userName': 'storage', 'password': 'storageadmin'}
backup_admin = {'userName': 'backup', 'password': 'backupadmin'}
server_admin = {'userName': 'server', 'password': 'serveradmin'}
read_only = {'userName': 'readonly', 'password': 'readonly'}


"""
admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}
network_admin = {'userName': 'network', 'password': 'networkadmin'}
storage_admin = {'userName': 'storage', 'password': 'storageadmin'}
backup_admin = {'userName': 'backup', 'password': 'backupadmin'}
server_admin = {'userName': 'server', 'password': 'serveradmin'}
read_only = {'userName': 'readonly', 'password': 'readonly'}
"""
vcenter = {'server': '15.199.230.130', 'user': 'rbriggs', 'password': 'hpvse1'}

users = [{'userName': 'server', 'password': 'serveradmin', 'fullName': 'Sarah', 'roles': ['Server administrator'], 'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'network', 'password': 'networkadmin', 'fullName': 'Nat', 'roles': ['Network administrator'], 'emailAddress': 'nat@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'backup', 'password': 'backupadmin', 'fullName': 'Backup', 'roles': ['Backup administrator'], 'emailAddress': 'backup@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'readonly', 'password': 'readonly', 'fullName': 'Rheid', 'roles': ['Read only'], 'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'storage', 'password': 'storageadmin', 'fullName': 'Rheid', 'roles': ['Storage administrator'], 'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'}
         ]

licenses = [{'key': 'YCDE D9MA H9P9 8HUZ U7B5 HWW5 Y9JL KMPL MHND 7AJ9 DXAU 2CSM GHTG L762 LFH6 F4R4 KJVT D5KM EFVW DT5J 83HJ 8VC6 AK2P 3EW2 L9YE HUNJ TZZ7 MB5X 82Z5 WHEF GE4C LUE3 BKT8 WXDG NK6Y C4GA HZL4 XBE7 3VJ6 2MSU 4ZU9 9WGG CZU7 WE4X YN44 CH55 KZLG 2F4N A8RJ UKEG 3F9V JQY5 "423207356 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR H3TCJHCGAYAY"'},
            {'key': 'QC3C A9MA H9PQ GHVZ U7B5 HWW5 Y9JL KMPL 2HVF 4FZ9 DXAU 2CSM GHTG L762 7JX5 V5FU KJVT D5KM EFVW DV5J 43LL PSS6 AK2P 3EW2 T9YE XUNJ TZZ7 MB5X 82Z5 WHEF GE4C LUE3 BKT8 WXDG NK6Y C4GA HZL4 XBE7 3VJ6 2MSU 4ZU9 9WGG CZU7 WE4X YN44 CH55 KZLG 2F4N A8RJ UKEG 3F9V JQY5 "423207566 HPOV-NFR2 HP_OneView_w/o_iLO_48_Seat_NFR 6H72JHCGY5AU"'}
            ]

ranges = [{'name': 'FCOE-MAC', 'type': 'Range', 'category': 'id-range-VMAC', 'rangeCategory': 'CUSTOM', 'startAddress': 'AA:AA:AA:00:00:00', 'endAddress': 'AA:AA:AA:00:00:80', 'enabled': True},
          {'name': 'FCOE-WWN', 'type': 'Range', 'category': 'id-range-VWWN', 'rangeCategory': 'CUSTOM', 'startAddress': '2A:AA:AA:AA:AA:AA:AA:AA', 'endAddress': '2A:AA:AA:AA:AA:AA:AB:29', 'enabled': True},
          {'name': 'FCOE-SN', 'type': 'Range', 'category': 'id-range-VSN', 'rangeCategory': 'CUSTOM', 'startAddress': 'VCUAAAAAAA', 'endAddress': 'VCUAAAAADT', 'enabled': True}]

ethernet_networks_p1 = [{'name': 'ETH_NW1',
                         'type': 'ethernet-networkV3',
                         'vlanId': 1,
                         'purpose': 'General',
                         'smartLink': True,
                         'privateNetwork': False,
                         'connectionTemplateUri': None,
                         'ethernetNetworkType': 'Tagged'}
                        ]
eth_nw1_p = [{"vlanId": "1", "ethernetNetworkType": "Tagged", "subnetUri": None, "purpose": "General", "name": "ETH_NW1", "smartLink": "true", "privateNetwork": "false", "connectionTemplateUri": None, "type": "ethernet-networkV4"}, ]
eth_s_bb = [{"vlanId": "100", "ethernetNetworkType": "Tagged", "subnetUri": None, "purpose": "General", "name": "ETH_NW2", "smartLink": 'true', "privateNetwork": 'false', "connectionTemplateUri": None, "type": "ethernet-networkV4"}, ]

fc_networks_p = [{'type': 'fc-networkV4', 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
                  'name': 'FC_NW1', 'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'}]

ethernet_networks_TBird = [{'name': 'eth-100', 'type': 'ethernet-networkV300', 'vlanId': 100, 'purpose': 'General', 'smartLink': True,
                            'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tagged'}]

fcoe_networksp = [{
    "name": "FCOE_NW100",
    "type": "fcoe-networkV4",
    "vlanId": "100"
}, ]

fcoe_net_bb_s = [{'name': 'fcoe_103', 'type': 'fcoe-networkV300', 'vlanId': '103'},
                 {'name': 'fcoe_104', 'type': 'fcoe-networkV300', 'vlanId': '104'}, ]

ethernet_networks1 = [{'name': 'eth-100',
                       'type': 'ethernet-networkV3',
                       'vlanId': 100,
                       'purpose': 'General',
                       'smartLink': True,
                       'privateNetwork': False,
                       'connectionTemplateUri': None,
                       'ethernetNetworkType': 'Tunnel'},
                      {'name': 'eth-101',
                       'type': 'ethernet-networkV3',
                       'vlanId': 101,
                       'purpose': 'General',
                       'smartLink': True,
                       'privateNetwork': False,
                       'connectionTemplateUri': None,
                       'ethernetNetworkType': 'Tunnel'},
                      ]
ethernet_networks = [{'name': 'eth-100',
                      'type': 'ethernet-networkV3',
                      'vlanId': 100,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'},
                     {'name': 'eth-101',
                      'type': 'ethernet-networkV3',
                      'vlanId': 101,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'},
                     {'name': 'eth-102',
                      'type': 'ethernet-networkV3',
                      'vlanId': 102,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'},
                     {'name': 'network-a',
                      'type': 'ethernet-networkV3',
                      'vlanId': 200,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'},
                     {'name': 'network-b',
                      'type': 'ethernet-networkV3',
                      'vlanId': 201,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'},
                     {'name': 'network-c',
                      'type': 'ethernet-networkV3',
                      'vlanId': 202,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'},
                     {'name': 'network-d',
                      'type': 'ethernet-networkV3',
                      'vlanId': 203,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'},
                     {'name': 'network-e',
                      'type': 'ethernet-networkV3',
                      'vlanId': 204,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'},

                     ]

network_sets = [{'name': 'netset1', 'type': 'network-set', 'networkUris': ['network-a'], 'nativeNetworkUri': None}]

fcoe_networks_p = {'name': 'FCOE_ETH', 'vlanId': '101', 'connectionTemplateUri': 'null', 'managedSanUri': 'null', 'type': 'fcoe-networkV300'}

fcoe_networks = {'fcoe-1': {'name': 'fcoe-1', 'type': 'fcoe-network', 'vlanId': 1},
                 'fcoe-100': {'name': 'fcoe-100', 'type': 'fcoe-network', 'vlanId': 100},
                 'fcoe-2000': {'name': 'fcoe-2000', 'type': 'fcoe-network', 'vlanId': 2000},
                 'fcoe-100b': {'name': 'fcoe-100b', 'type': 'fcoe-network', 'vlanId': 100},
                 'fcnetwork-a': {'name': 'fcnetwork-a', 'type': 'fcoe-network', 'vlanId': 209},
                 'network-a': {'name': 'network-a', 'type': 'fcoe-network', 'vlanId': 210},
                 'network-b': {'name': 'network-b', 'type': 'fcoe-network', 'vlanId': 211},
                 'no-vlanId': {'name': 'no-vlanId', 'type': 'fcoe-network'},
                 'fcoe-4095': {'name': 'fcoe-4095', 'type': 'fcoe-network', 'vlanId': 4095}}

fcoe_ranges = {'fcoe-range32a': {'prefix': 'fcoe-', 'suffix': 'a', 'start': 1001, 'end': 1032},
               'fcoe-range32b': {'prefix': 'fcoe-', 'suffix': 'b', 'start': 1001, 'end': 1032},
               'fcoe-range32c': {'prefix': 'fcoe-', 'suffix': 'c', 'start': 1001, 'end': 1032},
               'fcoe-range32d': {'prefix': 'fcoe-', 'suffix': 'd', 'start': 1001, 'end': 1032},
               'fcoe-range33': {'prefix': 'fcoe-', 'suffix': '', 'start': 1001, 'end': 1033},
               'fcoe-range30a': {'prefix': 'fcoe-', 'suffix': 'a', 'start': 1001, 'end': 1030},
               'fcoe-range128': {'prefix': 'fcoe-', 'suffix': '', 'start': 1001, 'end': 1128},
               'fcoe-range-delete-20': {'prefix': 'fcoe-', 'suffix': '', 'start': 1109, 'end': 1128}
               }

fc_networks = [{'type': 'fc-networkV2',
                'linkStabilityTime': 30,
                'autoLoginRedistribution': True,
                'name': 'fcnetwork-a',
                'connectionTemplateUri': None,
                'managedSanUri': None,
                'fabricType': 'FabricAttach'}]
enc_group = {'name': 'EG_B1',
             'configurationScript': None,
             'interconnectBayMappings':
             [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:LIG_B1'},
              {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:LIG_B1'},
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG_B1'},
              {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:LIG_B1'},
              {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG_B1'},
              {'interconnectBay': 7, 'logicalInterconnectGroupUri': 'LIG:LIG_B1'},
              {'interconnectBay': 8, 'logicalInterconnectGroupUri': 'LIG:LIG_B1'}],
             'ipRangeUris': [], 'enclosureCount': 1}

enc_group_tbird_SE_dhcp = [{'name': 'EGLldp',
                            'interconnectBayMappings': [{'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG'},
                                                        {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG'}],
                            'ipAddressingMode': 'DHCP',
                            'ipRangeUris': [], 'enclosureCount':1,
                            'powerMode':'RedundantPowerFeed', 'ambientTemperatureMode':'Standard'
                            }]

enc_group_permnc = {'name': 'EG_B1',
                    'type': 'EnclosureGroupV400',
                    'enclosureTypeUri': '/rest/enclosure-types/c7000',
                    'stackingMode': 'Enclosure',
                    'interconnectBayMappingCount': 8,
                    'configurationScript': None,
                    'interconnectBayMappings':
                    [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:LIG_B1'},
                     {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:LIG_B1'},
                     {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG_B1'},
                     {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:LIG_B1'},
                     {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                     {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG_B1'},
                     {'interconnectBay': 7, 'logicalInterconnectGroupUri': 'LIG:LIG_B1'},
                     {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}]}

enc_group_02 = {'name': 'EGLldp',
                'type': 'EnclosureGroupV200',
                'enclosureTypeUri': '/rest/enclosure-types/c7000',
                'stackingMode': 'Enclosure',
                'interconnectBayMappingCount': 8,
                'configurationScript': None,
                'interconnectBayMappings':
                [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                 {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                 {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
                 {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                 {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
                 {'interconnectBay': 6, 'logicalInterconnectGroupUri': None},
                 {'interconnectBay': 7, 'logicalInterconnectGroupUri': None},
                 {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}]}

#         <enclosure name="WPST-PAY113-EN1" licensingintent="OneViewNoiLO" oa1hostname="15.199.230.74" oa1hostname_ipv6="" oa1username="Administrator" oa1password="hpvse1" oa2hostname="" oa2hostname_ipv6="" oa2username="" oa2password="" group="FCoE-1" serialnumber="2S1351P8NP" force="false"></enclosure>
encDCS = [{'hostname': '172.18.1.11', 'username': 'dcs', 'password': 'dcs', 'enclosureGroupUri': 'EG:EGLldp', 'force': False, 'licensingIntent': 'OneViewNoiLO'}]
encREAL1 = [{'hostname': '192.168.144.132', 'username': 'Administrator', 'password': 'Admin', 'enclosureGroupUri': 'EG:EG_B1', 'force': False, 'licensingIntent': 'OneViewNoiLO'}]
encREAL = [{'hostname': '192.168.144.132', 'username': 'Administrator', 'password': 'Admin', 'enclosureGroupUri': 'EG:EG_B1', 'force': True, 'licensingIntent': 'OneViewNoiLO', 'firmwareBaselineUri': '/rest/firmware-drivers/bp-2016-06-24-00', 'forceInstallFirmware': 'true'}]
encREALBB = [{'hostname': '192.168.144.132', 'username': 'Administrator', 'password': 'Admin', 'enclosureGroupUri': 'EG:EG_B1', 'force': True, 'licensingIntent': 'OneViewNoiLO'}]
encREAL_duringenc = [{'hostname': '192.168.144.132', 'username': 'Administrator', 'password': 'Admin', 'enclosureGroupUri': 'EG:EG_B1', 'force': True, 'licensingIntent': 'OneViewNoiLO', 'firmwareBaselineUri': '/rest/firmware-drivers/bp-2016-06-24-00', 'forceInstallFirmware': True}]
encReal_new_duringenc = {"username": "Administrator", "password": "Admin", "enclosureGroupUri": 'EG:EG_B1', "firmwareBaselineUri": "/rest/firmware-drivers/bp-2016-06-24-00", "updateFirmwareOn": "EnclosureOnly", "force": "false", "forceInstallFirmware": "true", "licensingIntent": "OneViewNoiLO", "hostname": "192.168.144.132"}

encReal_new_duringenc_no_flag = {"username": "Administrator", "password": "Admin", "enclosureGroupUri": 'EG:EG_B1', "firmwareBaselineUri": "/rest/firmware-drivers/{}".format(spp), "updateFirmwareOn": "EnclosureOnly", "force": "false", "forceInstallFirmware": "false", "licensingIntent": "OneViewNoiLO", "hostname": "192.168.144.132"}
# enc_new_REAL_during_enc = [{'username':'Administrator','password':'Admin','enclosureGroupUri':'EG:EG_B1','firmwareBaselineUri':'/rest/firmware-drivers/{}'.format(spp),'updateFirmwareOn':'EnclosureOnly','force':'true','forceInstallFirmware':'true','licensingIntent':'OneViewNoiLO','hostname':'192.168.144.132'}]
enc_new_REAL_during_enc = [{"username": "Administrator", "password": "Admin", "enclosureGroupUri": 'EG:EG_B1', "firmwareBaselineUri": "/rest/firmware-drivers/{}".format(spp), "updateFirmwareOn": "EnclosureOnly", "force": "false", "forceInstallFirmware": "true", "licensingIntent": "OneViewNoiLO", "hostname": "192.168.144.132"}]
enc_new_REAL_during_enc_downgrade = [{"username": "Administrator", "password": "Admin", "enclosureGroupUri": 'EG:EG_B1', "firmwareBaselineUri": "/rest/firmware-drivers/bp-2016-06-24-00", "updateFirmwareOn": "EnclosureOnly", "force": "true", "forceInstallFirmware": "true", "licensingIntent": "OneViewNoiLO", "hostname": "192.168.144.132"}]

enc_new_REAL_during_enc_upgrade = [{"username": "Administrator", "password": "Admin", "enclosureGroupUri": 'EG:EG_B1', "firmwareBaselineUri": "/rest/SPPGen10Snap1_2016_1220_70", "updateFirmwareOn": "EnclosureOnly", "force": "true", "forceInstallFirmware": "true", "licensingIntent": "OneViewNoiLO", "hostname": "192.168.144.132"}]

enc_new_REAL_during_enc_Upgrade_rpm_BB = [{"username": "Administrator", "password": "Admin", "enclosureGroupUri": 'EG:EG_B1', "firmwareBaselineUri": "/rest/firmware-drivers/{}".format(spp), "updateFirmwareOn": "EnclosureOnly", "force": "true", "forceInstallFirmware": "true", "licensingIntent": "OneViewNoiLO", "hostname": "192.168.144.132"}]

encs = encREALBB
encsbb_flag = encREAL_duringenc
encsbb_no_flag = encReal_new_duringenc_no_flag
encsbb_new_parm = enc_new_REAL_during_enc
ENC1 = 'SGH420HHYA'
LE = 'SGH420HHYA'
LIG1 = 'LIG1'
LIG2 = 'LIG_B2'

encs_f1212_new_downgrade = enc_new_REAL_during_enc_downgrade
encs_f1212_new_upgrade = enc_new_REAL_during_enc_Upgrade_rpm_BB

appliance = {'type': 'ApplianceNetworkConfiguration',
             'applianceNetworks':
             [{'device': 'eth0',
               'macAddress': None,
               'interfaceName': '15.199.x.x',
               'activeNode': '1',
               'unconfigure': False,
               'ipv4Type': 'STATIC',
               'ipv4Subnet': '255.255.240.0',
               'ipv4Gateway': '15.199.224.1',
               'ipv4NameServers': ['16.110.135.51', '16.110.135.52'],
               'app1Ipv4Addr': '15.199.229.190',
               'ipv6Type': 'UNCONFIGURE',
               'hostname': 'f100.usa.hp.com',
               'confOneNode': True,
               'domainName': 'usa.hp.com',
               'aliasDisabled': True,
               }],
             }

timeandlocale = {'type': 'TimeAndLocale', 'dateTime': None, 'timezone': 'UTC', 'ntpServers': ['ntp.hpecorp.net'], 'locale': 'en_US.UTF-8'}


uplink_sets = {'us1': {'name': 'us1',
                       'ethernetNetworkType': 'Tunnel',
                       'networkType': 'Ethernet',
                       'networkUris': ['eth-100'],
                       'primaryPort': None,
                       'nativeNetworkUri': None,
                       'mode': 'Auto',
                       'logicalPortConfigInfos': [{'bay': '1', 'port': 'X1', 'speed': 'Auto'},
                                                  {'bay': '1', 'port': 'X1', 'speed': 'Auto'},
                                                  ]},
               'us2': {'name': 'us2',
                       'ethernetNetworkType': 'Tunnel',
                       'networkType': 'Ethernet',
                       'networkUris': ['eth-101'],
                       'primaryPort': None,
                       'nativeNetworkUri': None,
                       'mode': 'Auto',
                       'logicalPortConfigInfos': [{'bay': '2', 'port': 'X1', 'speed': 'Auto'},
                                                  {'bay': '2', 'port': 'X2', 'speed': 'Auto'},
                                                  ]},
               'BLIG_UP1': {'name': 'BLIG_UP1',
                            'mode': 'Auto',
                            'networkType': 'FibreChannel',
                            'ethernetNetworkType': None,
                            'lacpTimer': 'Short',
                            'networkUris': ['FC_NW1'],
                            'primaryPort': None,
                            'nativeNetworkUri': None,

                            'logicalPortConfigInfos': [{'bay': '3', 'port': 'X1', 'speed': 'Auto'}]},

               'BLIG_UP2': {'name': 'BLIG_UP2',
                            'mode': 'Auto',
                            'networkType': 'FibreChannel',
                            'ethernetNetworkType': None,
                            'lacpTimer': 'Short',
                            'networkUris': ['FC_NW2'],
                            'primaryPort': None,
                            'nativeNetworkUri': None,

                            'logicalPortConfigInfos': [{'bay': '4', 'port': 'X1', 'speed': 'Auto'}]},


               'LIGUPS1': {'name': 'BLIG_UP1',
                           'mode': 'Auto',
                           'networkType': 'FibreChannel',
                           'ethernetNetworkType': 'null',
                           'lacpTimer': 'Short',
                           'networkUris': ['FC_NW1'],
                           'primaryPort': None,
                           'nativeNetworkUri': None,

                           'logicalPortConfigInfos': [{'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 17}, {'type': 'Enclosure', 'relativeValue': 1}]}}]
                           },


               'LIGUPS2': {'name': 'BLIG_UP2',
                           'mode': 'Auto',
                           'networkType': 'FibreChannel',
                           'ethernetNetworkType': 'null',
                           'lacpTimer': 'Short',
                           'networkUris': ['FC_NW2'],
                           'primaryPort': None,
                           'nativeNetworkUri': None,

                           'logicalPortConfigInfos': [{'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 4}, {'type': 'Port', 'relativeValue': 17}, {'type': 'Enclosure', 'relativeValue': 1}]}}]
                           },


               'us3': {'name': 'us3',
                       'ethernetNetworkType': 'Tagged',
                       'networkType': 'Ethernet',
                       'networkUris': make_range_list(**fcoe_ranges['fcoe-range32c']),
                       'primaryPort': None,
                       'nativeNetworkUri': None,
                       'mode': 'Auto',
                       'logicalPortConfigInfos': [{'bay': '5', 'port': 'X1', 'speed': 'Auto'},
                                                  {'bay': '5', 'port': 'X2', 'speed': 'Auto'},
                                                  {'bay': '5', 'port': 'X3', 'speed': 'Auto'},
                                                  {'bay': '5', 'port': 'X4', 'speed': 'Auto'},
                                                  {'bay': '5', 'port': 'X5', 'speed': 'Auto'},
                                                  {'bay': '5', 'port': 'X6', 'speed': 'Auto'},
                                                  {'bay': '5', 'port': 'X7', 'speed': 'Auto'},
                                                  {'bay': '5', 'port': 'X8', 'speed': 'Auto'}]},
               'us33': {'name': 'us-33-exceeds-32',
                        'ethernetNetworkType': 'Tagged',
                        'networkType': 'Ethernet',
                        'networkUris': make_range_list(**fcoe_ranges['fcoe-range33']),
                        'primaryPort': None,
                        'nativeNetworkUri': None,
                        'mode': 'Auto',
                        'logicalPortConfigInfos': [{'bay': '4', 'port': 'X1', 'speed': 'Auto'},
                                                   {'bay': '4', 'port': 'X2', 'speed': 'Auto'},
                                                   {'bay': '4', 'port': 'X3', 'speed': 'Auto'},
                                                   {'bay': '4', 'port': 'X4', 'speed': 'Auto'}]},
               'us1-b': {'name': 'us1-b-removed X10, 30 networks',
                         'ethernetNetworkType': 'Tagged',
                         'networkType': 'Ethernet',
                         'networkUris': make_range_list(**fcoe_ranges['fcoe-range30a']),
                         'primaryPort': None,
                         'nativeNetworkUri': None,
                         'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '1', 'port': 'X1', 'speed': 'Auto'},
                                                    {'bay': '1', 'port': 'X2', 'speed': 'Auto'},
                                                    {'bay': '1', 'port': 'X3', 'speed': 'Auto'},
                                                    {'bay': '1', 'port': 'X4', 'speed': 'Auto'},
                                                    {'bay': '1', 'port': 'X5', 'speed': 'Auto'},
                                                    {'bay': '1', 'port': 'X6', 'speed': 'Auto'},
                                                    {'bay': '1', 'port': 'X7', 'speed': 'Auto'},
                                                    {'bay': '1', 'port': 'X8', 'speed': 'Auto'},
                                                    {'bay': '1', 'port': 'X9', 'speed': 'Auto'}]},

               'us1-c': {'name': 'us-3-exceeds-32max',
                         'ethernetNetworkType': 'Tagged',
                         'networkType': 'Ethernet',
                         'networkUris': ['fcoe-1001', 'fcoe-1002', 'fcoe-1003'],
                         'primaryPort': None,
                         'nativeNetworkUri': None,
                         'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '1', 'port': 'X10', 'speed': 'Auto'}]},
               'us1-d': {'name': 'us1',
                         'ethernetNetworkType': 'Tagged',
                         'networkType': 'Ethernet',
                         'networkUris': make_range_list(**fcoe_ranges['fcoe-range32a']),
                         'primaryPort': None,
                         'nativeNetworkUri': None,
                         'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '1', 'port': 'X1', 'speed': 'Auto'},
                                                    {'bay': '1', 'port': 'X2', 'speed': 'Auto'},
                                                    {'bay': '1', 'port': 'X3', 'speed': 'Auto'},
                                                    {'bay': '1', 'port': 'X4', 'speed': 'Auto'}]},
               'us1-eth': {'name': 'us1-eth',
                           'ethernetNetworkType': 'Tagged',
                           'networkType': 'Ethernet',
                           'networkUris': ['network-d'],
                           'primaryPort': None,
                           'nativeNetworkUri': None,
                           'mode': 'Auto',
                           'logicalPortConfigInfos': [{'bay': '1', 'port': 'X5', 'speed': 'Auto'},
                                                      {'bay': '1', 'port': 'X6', 'speed': 'Auto'}]},
               'us2-d': {'name': 'us2',
                         'ethernetNetworkType': 'Tagged',
                         'networkType': 'Ethernet',
                         'networkUris': make_range_list(**fcoe_ranges['fcoe-range32b']),
                         'primaryPort': None,
                         'nativeNetworkUri': None,
                         'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '3', 'port': 'X1', 'speed': 'Auto'},
                                                    {'bay': '3', 'port': 'X2', 'speed': 'Auto'}]},
               'us2-fc': {'name': 'us2-fc',
                          'ethernetNetworkType': 'Tagged',
                          'networkType': 'FibreChannel',
                          'networkUris': ['fcnetwork-a'],
                          'primaryPort': None,
                          'nativeNetworkUri': None,
                          'mode': 'Auto',
                          'logicalPortConfigInfos': [{'bay': '3', 'port': 'X3', 'speed': 'Auto'},
                                                     {'bay': '3', 'port': 'X4', 'speed': 'Auto'}]},
               'us2-fc2': {'name': 'us2-fc2',
                           'ethernetNetworkType': 'Tagged',
                           'networkType': 'FibreChannel',
                           'networkUris': ['fcnetwork-b'],
                           'primaryPort': None,
                           'nativeNetworkUri': None,
                           'mode': 'Auto',
                           'logicalPortConfigInfos': [{'bay': '4', 'port': 'X1', 'speed': 'Auto'},
                                                      {'bay': '4', 'port': 'X2', 'speed': 'Auto'}]},

               'us3-d': {'name': 'us3',
                         'ethernetNetworkType': 'Tagged',
                         'networkType': 'Ethernet',
                         'networkUris': make_range_list(**fcoe_ranges['fcoe-range32c']),
                         'primaryPort': None,
                         'nativeNetworkUri': None,
                         'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '5', 'port': 'X1', 'speed': 'Auto'},
                                                    {'bay': '5', 'port': 'X2', 'speed': 'Auto'},
                                                    {'bay': '5', 'port': 'X3', 'speed': 'Auto'},
                                                    {'bay': '5', 'port': 'X4', 'speed': 'Auto'}]},
               'us3-eth': {'name': 'us3-eth',
                           'ethernetNetworkType': 'Tagged',
                           'networkType': 'Ethernet',
                           'networkUris': ['network-e'],
                           'primaryPort': None,
                           'nativeNetworkUri': None,
                           'mode': 'Auto',
                           'logicalPortConfigInfos': [{'bay': '5', 'port': 'X5', 'speed': 'Auto'},
                                                      {'bay': '5', 'port': 'X6', 'speed': 'Auto'},
                                                      {'bay': '5', 'port': 'X7', 'speed': 'Auto'},
                                                      {'bay': '5', 'port': 'X8', 'speed': 'Auto'}]},
               'us3-2ics': {'name': 'us2-ics',
                            'ethernetNetworkType': 'Tagged',
                            'networkType': 'Ethernet',
                            'networkUris': ['fcoe-100'],
                            'primaryPort': None,
                            'nativeNetworkUri': None,
                            'mode': 'Auto',
                            'logicalPortConfigInfos': [{'bay': '5', 'port': 'X5', 'speed': 'Auto'},
                                                       {'bay': '6', 'port': 'X5', 'speed': 'Auto'}]},
               'unsupported-ics': {'name': 'unsupported-ics',
                                   'ethernetNetworkType': 'Tagged',
                                   'networkType': 'Ethernet',
                                   'networkUris': ['fcoe-100'],
                                   'primaryPort': None,
                                   'nativeNetworkUri': None,
                                   'mode': 'Auto',
                                   'logicalPortConfigInfos': [{'bay': '1', 'port': 'X1', 'speed': 'Auto'}]},
               'unsupported-ics2': {'name': 'unsupported-ics2',
                                    'ethernetNetworkType': 'Tagged',
                                    'networkType': 'Ethernet',
                                    'networkUris': ['fcoe-100'],
                                    'primaryPort': None,
                                    'nativeNetworkUri': None,
                                    'mode': 'Auto',
                                    'logicalPortConfigInfos': [{'bay': '1', 'port': '1', 'speed': 'Auto'}]},
               'duplicate-vlan': {'name': 'duplicate-vlan',
                                  'ethernetNetworkType': 'Tagged',
                                  'networkType': 'Ethernet',
                                  'networkUris': ['eth-100', 'fcoe-100'],
                                  'primaryPort': None,
                                  'nativeNetworkUri': None,
                                  'mode': 'Auto',
                                  'logicalPortConfigInfos': [{'bay': '1', 'port': 'X1', 'speed': 'Auto'}]},
               'BFS': {'name': 'BFS',
                       'ethernetNetworkType': 'Tagged',
                       'networkType': 'Ethernet',
                       'networkUris': ['eth-102', 'fcoe-1002'],
                       'primaryPort': None,
                       'nativeNetworkUri': None,
                       'mode': 'Auto',
                       'logicalPortConfigInfos': [{'bay': '1', 'port': 'X1', 'speed': 'Auto'},
                                                  {'bay': '1', 'port': 'X2', 'speed': 'Auto'}]},
               'BFS-fcoe': {'name': 'BFS-fcoe',
                            'ethernetNetworkType': 'Tagged',
                            'networkType': 'Ethernet',
                            'networkUris': ['fcoe-1002'],
                            'primaryPort': None,
                            'nativeNetworkUri': None,
                            'mode': 'Auto',
                            'logicalPortConfigInfos': [{'bay': '1', 'port': 'X2', 'speed': 'Auto'}]},
               }


ligs_encp = [{'name': 'LIGP1',
              'type': 'logical-interconnect-groupV300',
              'enclosureType': 'C7000',
              'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC Flex-10/10D Module'},
                                          {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC Flex-10/10D Module'},
                                          ],
              'uplinkSets': [{'name': 'ETH-FCOE',
                              'ethernetNetworkType': 'Tagged',
                              'networkType': 'Ethernet',
                              'networkUris': ['ETH_NW1'],
                              'nativeNetworkUri': None,
                              'mode': 'Auto',
                              'logicalPortConfigInfos': [{'bay': '1', 'port': 'X1', 'speed': 'Auto'},
                                                         {'bay': '2', 'port': 'X1', 'speed': 'Auto'}]}
                             ],
              'stackingMode': 'Enclosure',
              'ethernetSettings': None,
              'state': 'Active',
              'telemetryConfiguration': None,
              'snmpConfiguration': None}
             ]


"""

uplink_sets_dev = {'IC-a': {'name': 'IC',
                        'ethernetNetworkType': 'Untagged',
                        'networkType': 'Ethernet',
                        'networkUris': ['IC'],
                        'nativeNetworkUri': None,
                        'mode': 'Auto',
                        'logicalPortConfigInfos': [{'bay': '3', 'port': 'X6', 'speed': 'Auto'}]},
               'IC-b': {'name': 'IC',
                        'ethernetNetworkType': 'Untagged',
                        'networkType': 'Ethernet',
                        'networkUris': ['IC'],
                        'nativeNetworkUri': None,
                        'mode': 'Auto',
                        'logicalPortConfigInfos': [{'bay': '2', 'port': 'X6', 'speed': 'Auto'}]},
               'FAB-A-FA': {'name': 'FAB-A-FA',
                            'ethernetNetworkType': 'NotApplicable',
                            'networkType': 'FibreChannel',
                            'networkUris': ['SAN-3-A-FA-3-1'],
                            'nativeNetworkUri': None,
                            'mode': 'Auto',
                            'logicalPortConfigInfos': [{'bay': '3', 'port': 'X1', 'speed': 'Auto'}]},

                'LIGUPS1': {'name': 'BLIG_UP1',
                     'mode':'Auto',
                     'networkType':'FibreChannel',
                     'ethernetNetworkType': 'null',
                     'lacpTimer':'Short',
                     'networkUris': ['FC_NW1'],
                     'primaryPort': None,
                      'nativeNetworkUri': None',

                      'logicalPortConfigInfos': [{'desiredSpeed':'Auto','logicalLocation':{'locationEntries':[{'type':'Bay','relativeValue':3},{'type':'Port','relativeValue':17},{'type':'Enclosure','relativeValue':1}]}}]},


        'LIGUPS2': {'name': 'BLIG_UP2',
                     'mode':'Auto',
                     'networkType':'FibreChannel',
                     'ethernetNetworkType': 'null',
                     'lacpTimer':'Short',
                     'networkUris': ['FC_NW2'],
                     'primaryPort': None,
                      'nativeNetworkUri': None',

                      'logicalPortConfigInfos': [{'desiredSpeed':'Auto','logicalLocation':{'locationEntries':[{'type':'Bay','relativeValue':4},{'type':'Port','relativeValue':17},{'type':'Enclosure','relativeValue':1}]}}]},

               'FAB-B-FA': {'name': 'FAB-B-FA',
                            'ethernetNetworkType': 'NotApplicable',
                            'networkType': 'FibreChannel',
                            'networkUris': ['SAN-4-B-FA-4-1'],
                            'nativeNetworkUri': None,
                            'mode': 'Auto',
                            'logicalPortConfigInfos': [{'bay': '4', 'port': 'X1', 'speed': 'Auto'}]},
           'FAB-A2-FA': {'name': 'FAB-A2-FA',
                            'ethernetNetworkType': 'NotApplicable',
                            'networkType': 'FibreChannel',
                            'networkUris': ['SAN-3-A-FA-3-1-2-3-4'],
                            'nativeNetworkUri': None,
                            'mode': 'Auto',
                            'logicalPortConfigInfos': [{'bay': '3', 'port': '1', 'speed': 'Auto'},
                                                       {'bay': '3', 'port': '2', 'speed': 'Auto'},
                                                       {'bay': '3', 'port': '3', 'speed': 'Auto'},
                                                       {'bay': '3', 'port': '4', 'speed': 'Auto'}]},
               'FAB-B2-FA': {'name': 'FAB-B2-FA',
                            'ethernetNetworkType': 'NotApplicable',
                            'networkType': 'FibreChannel',
                            'networkUris': ['SAN-4-B-FA-4-1-2-3-4'],
                            'nativeNetworkUri': None,
                            'mode': 'Auto',
                            'logicalPortConfigInfos': [{'bay': '4', 'port': '1', 'speed': 'Auto'},
                                                       {'bay': '4', 'port': '2', 'speed': 'Auto'},
                                                       {'bay': '4', 'port': '3', 'speed': 'Auto'},
                                                       {'bay': '4', 'port': '4', 'speed': 'Auto'}]},
               'FAB-C-FA': {'name': 'FAB-C-FA',
                         'ethernetNetworkType': 'NotApplicable',
                         'networkType': 'FibreChannel',
                         'networkUris': ['SAN-FA-5-5'],
                         'nativeNetworkUri': None,
                         'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '5', 'port': 'X5', 'speed': 'Auto'}]},
               'FAB-D-FA': {'name': 'FAB-D-FA',
                         'ethernetNetworkType': 'NotApplicable',
                         'networkType': 'FibreChannel',
                         'networkUris': ['SAN-FA-6-5'],
                         'nativeNetworkUri': None,
                         'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '6', 'port': 'X5', 'speed': 'Auto'}]},
               'Tunnel1': {'name': 'Tunnel1',
                           'ethernetNetworkType': 'Tunnel',
                           'networkType': 'Ethernet',
                           'networkUris': ['Tunnel1'],
                           'nativeNetworkUri': None,
                           'mode': 'Auto',
                           'logicalPortConfigInfos': [{'bay': '1', 'port': 'X7', 'speed': 'Auto'}]},
               'Tunnel2': {'name': 'Tunnel2',
                           'ethernetNetworkType': 'Tunnel',
                           'networkType': 'Ethernet',
                           'networkUris': ['Tunnel2'],
                           'nativeNetworkUri': None,
                           'mode': 'Auto',
                           'logicalPortConfigInfos': [{'bay': '2', 'port': 'X7', 'speed': 'Auto'}]},
               'BigPipe1-a': {'name': 'BigPipe1',
                              'ethernetNetworkType': 'Tagged',
                              'networkType': 'Ethernet',
                              'networkUris': make_range_list({'start': 2, 'end': 317, 'prefix': 'net_', 'suffix': '-O'}) + make_range_list({'start': 700, 'end': 710, 'prefix': 'net_', 'suffix': '-O'}) + make_range_list({'start': 3990, 'end': 4000, 'prefix': 'net_', 'suffix': '-O'}) + make_range_list({'start': 637, 'end': 668, 'prefix': 'FCOE-A-', 'suffix': '-O'}),
                              'nativeNetworkUri': None,
                              'mode': 'Auto',
                              'logicalPortConfigInfos': [{'bay': '1', 'port': 'X1', 'speed': 'Auto'},
                                                         {'bay': '1', 'port': 'X2', 'speed': 'Auto'}]},
               'BigPipe2-a': {'name': 'BigPipe2',
                              'ethernetNetworkType': 'Tagged',
                              'networkType': 'Ethernet',
                  'networkUris': make_range_list({'start': 2, 'end': 317, 'prefix': 'net_', 'suffix': '-E'}) + make_range_list({'start': 700, 'end': 710, 'prefix': 'net_', 'suffix': '-E'}) + make_range_list({'start': 3990, 'end': 4000, 'prefix': 'net_', 'suffix': '-E'}) + make_range_list({'start': 637, 'end': 668, 'prefix': 'FCOE-B-', 'suffix': '-E'}),
                              'nativeNetworkUri': None,
                              'mode': 'Auto',
                              'logicalPortConfigInfos':  [{'bay': '2', 'port': 'X1', 'speed': 'Auto'},
                                                          {'bay': '2', 'port': 'X2', 'speed': 'Auto'}]},
               'BigPipe1-b': {'name': 'BigPipe1',
                              'ethernetNetworkType': 'Tagged',
                              'networkType': 'Ethernet',
                              'networkUris': make_range_list({'start': 2, 'end': 317, 'prefix': 'net_', 'suffix': '-O'}) + make_range_list({'start': 700, 'end': 710, 'prefix': 'net_', 'suffix': '-O'}) + make_range_list({'start': 3990, 'end': 4000, 'prefix': 'net_', 'suffix': '-O'}) + make_range_list({'start': 637, 'end': 668, 'prefix': 'FCOE-A-', 'suffix': '-O'}),
                              'nativeNetworkUri': None,
                              'mode': 'Auto',
                              'logicalPortConfigInfos': [{'bay': '1', 'port': 'X5', 'speed': 'Auto'},
                                                         {'bay': '1', 'port': 'X6', 'speed': 'Auto'}]},
               'BigPipe2-b': {'name': 'BigPipe2',
                              'ethernetNetworkType': 'Tagged',
                              'networkType': 'Ethernet',
                  'networkUris': make_range_list({'start': 2, 'end': 317, 'prefix': 'net_', 'suffix': '-E'}) + make_range_list({'start': 700, 'end': 710, 'prefix': 'net_', 'suffix': '-E'}) + make_range_list({'start': 3990, 'end': 4000, 'prefix': 'net_', 'suffix': '-E'}) + make_range_list({'start': 637, 'end': 668, 'prefix': 'FCOE-B-', 'suffix': '-E'}),
                              'nativeNetworkUri': None,
                              'mode': 'Auto',
                              'logicalPortConfigInfos': [{'bay': '2', 'port': 'X5', 'speed': 'Auto'},
                                                         {'bay': '2', 'port': 'X6', 'speed': 'Auto'}]},
               'BigPipe1-c': {'name': 'BigPipe1',
                              'ethernetNetworkType': 'Tagged',
                              'networkType': 'Ethernet',
                              'networkUris': make_range_list({'start': 2, 'end': 317, 'prefix': 'net_', 'suffix': '-O'}) + make_range_list({'start': 700, 'end': 710, 'prefix': 'net_', 'suffix': '-O'}) + make_range_list({'start': 3990, 'end': 4000, 'prefix': 'net_', 'suffix': '-O'}) + make_range_list({'start': 637, 'end': 668, 'prefix': 'FCOE-A-', 'suffix': '-O'}),
                              'nativeNetworkUri': None,
                              'mode': 'Auto',
                              'logicalPortConfigInfos': [{'bay': '1', 'port': 'X2', 'speed': 'Auto'},
                                                         {'bay': '1', 'port': 'X3', 'speed': 'Auto'}]},
               'BigPipe2-c': {'name': 'BigPipe2',
                              'ethernetNetworkType': 'Tagged',
                              'networkType': 'Ethernet',
                  'networkUris': make_range_list({'start': 2, 'end': 317, 'prefix': 'net_', 'suffix': '-E'}) + make_range_list({'start': 700, 'end': 710, 'prefix': 'net_', 'suffix': '-E'}) + make_range_list({'start': 3990, 'end': 4000, 'prefix': 'net_', 'suffix': '-E'}) + make_range_list({'start': 637, 'end': 668, 'prefix': 'FCOE-B-', 'suffix': '-E'}),
                              'nativeNetworkUri': None,
                              'mode': 'Auto',
                              'logicalPortConfigInfos': [{'bay': '2', 'port': 'X2', 'speed': 'Auto'},
                                                         {'bay': '2', 'port': 'X3', 'speed': 'Auto'}]},
                }
"""

icmap_02 = [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC FlexFabric-20/40 F8 Module'},

            ]
icmap_old = [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
             {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
             {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC 16Gb 24-Port FC Module'},
             {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC 16Gb 24-Port FC Module'},
             {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
             {'enclosure': 1, 'enclosureIndex': 1, 'bay': 7, 'type': 'HP VC 8Gb 24-Port FC Module'},

             ]
icmap = [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
         {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
         {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC 16Gb 24-Port FC Module'},
         {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC 16Gb 24-Port FC Module'},
         {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
         {'enclosure': 1, 'enclosureIndex': 1, 'bay': 7, 'type': 'HP VC 8Gb 24-Port FC Module'},

         ]

BB_icmap = [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC 16Gb 24-Port FC Module'},
            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC 16Gb 24-Port FC Module'},
            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 7, 'type': 'HP VC 8Gb 24-Port FC Module'},
            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 8, 'type': 'HP VC 8Gb 24-Port FC Module'},

            ]
icmapbb = [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
           {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC 16Gb 24-Port FC Module'},
           {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
           {'enclosure': 1, 'enclosureIndex': 1, 'bay': 7, 'type': 'HP VC 8Gb 24-Port FC Module'},

           ]

icmap2 = [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC Flex-10 Enet Module'},
          {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC Flex-10 Enet Module'}]

icmap3 = [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC 8Gb 20-Port FC Module'}]

icmap4 = [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC Flex-10/10D Module'},
          {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC Flex-10/10D Module'},
          {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC Flex-10 Enet Module'},
          {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC Flex-10 Enet Module'},
          {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
          {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
          ]

# I inly taken put it here

li_uplink_sets = {'us1': {'name': 'Uses-FC',
                          'ethernetNetworkType': 'NotApplicable',
                          'networkType': 'FibreChannel',
                          'networkUris': [],
                          'fcNetworkUris': ['FC_NW1'],
                          'fcoeNetworkUris': [],
                          'lacpTimer': 'Short',
                          'logicalInterconnectUri': None,
                          'primaryPortLocation': None,
                          'manualLoginRedistributionState': 'NotSupported',
                          'connectionMode': 'Auto',
                          'nativeNetworkUri': None,
                          'portConfigInfos': [{'bay': '3', 'port': '1', 'desiredSpeed': 'Auto', 'enclosure': ENC1},
                                              {'bay': '4', 'port': '1', 'desiredSpeed': 'Auto', 'enclosure': ENC1}]},
                  'us2': {'name': 'ETH-FCOE2',
                          'ethernetNetworkType': 'Tagged',
                          'networkType': 'Ethernet',
                          'networkUris': ['net_104'],
                          'fcNetworkUris': [],
                          'fcoeNetworkUris': ['FCOE_NW1'],
                          'lacpTimer': 'Short',
                          'logicalInterconnectUri': None,
                          'primaryPortLocation': None,
                          'manualLoginRedistributionState': 'NotSupported',
                          'connectionMode': 'Auto',
                          'nativeNetworkUri': None,
                          'portConfigInfos': [{'bay': '6', 'port': 'X1', 'desiredSpeed': 'Auto', 'enclosure': ENC1}]},
                  'us3': {'name': 'Uses_ETH',
                          'ethernetNetworkType': 'Tagged',
                          'networkType': 'Ethernet',
                          'networkUris': ['ETH_NW1'],
                          'fcNetworkUris': [],
                          'fcoeNetworkUris': [],
                          'lacpTimer': 'Short',
                          'logicalInterconnectUri': None,
                          'primaryPortLocation': None,
                          'manualLoginRedistributionState': 'NotSupported',
                          'connectionMode': 'Auto',
                          'nativeNetworkUri': None,
                          'portConfigInfos': [{'bay': '3', 'port': 'X1', 'desiredSpeed': 'Auto', 'enclosure': ENC1},
                                              {'bay': '4', 'port': 'X2', 'desiredSpeed': 'Auto', 'enclosure': ENC1}]},
                  }


ligs = {'lig1':
        {'name': 'LIG_B1',
         'type': 'logical-interconnect-groupV300',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': BB_icmap,
         'uplinkSets': [uplink_sets['LIGUPS1'].copy(), uplink_sets['LIGUPS2'].copy()],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None},

        'P_new_lig1':
        {'name': 'LIG_B1',
         'type': 'logical-interconnect-groupV300',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'}
                                     ],
         'uplinkSets': [{'name': 'ETH-US',
                         'ethernetNetworkType': 'Tagged',
                         'networkType': 'Ethernet',
                         'networkUris': ['ETH_NW1'],
                         'nativeNetworkUri': None,
                         'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '1', 'port': 'X1', 'speed': 'Auto'},

                                                    {'bay': '2', 'port': 'X1', 'speed': 'Auto'}]},
                        {'name': 'FC-FA',
                            'ethernetNetworkType': 'NotApplicable',
                            'networkType': 'FibreChannel',
                            'networkUris': ['FC_NW1'],
                            'nativeNetworkUri': None,
                            'mode': 'Auto',
                            'logicalPortConfigInfos': [{'bay': '6', 'port': 'X1', 'speed': 'Auto'}]},

                        {'name': 'FCOE',
                         'ethernetNetworkType': 'Tagged',
                         'networkType': 'Ethernet',
                         'networkUris': ['FCOE_NW100'],
                         'primaryPort': None,
                         'nativeNetworkUri': None,
                         'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '6', 'port': 'X2', 'speed': 'Auto'}]}
                        ],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None},

        'P_new_4eth':
        {'name': 'LIG_B1',
         'type': 'logical-interconnect-groupV300',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                     ],
         'uplinkSets': [{'name': 'ETHUP1',
                         'ethernetNetworkType': 'Tagged',
                         'networkType': 'Ethernet',
                         'networkUris': ['ETH_NW1'],
                         'nativeNetworkUri': None,
                         'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '1', 'port': 'X1', 'speed': 'Auto'},
                                                    {'bay': '2', 'port': 'X1', 'speed': 'Auto'}]},


                        ],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None},

        'P_new_lig2':
        {'name': 'LIG_B1',
         'type': 'logical-interconnect-groupV300',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                     ],
         'uplinkSets': [{'name': 'ETH-One',
                         'ethernetNetworkType': 'Tagged',
                         'networkType': 'Ethernet',
                         'networkUris': ['ETH_NW1'],
                         'nativeNetworkUri': None,
                         'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '1', 'port': 'X1', 'speed': 'Auto'},
                                                    {'bay': '2', 'port': 'X1', 'speed': 'Auto'}]},

                        {'name': 'ETH-FCOE2',
                         'ethernetNetworkType': 'Tagged',
                         'networkType': 'Ethernet',
                         'networkUris': ['FCOE_NW100'],
                         'mode': 'Auto',
                         'nativeNetworkUri': None,
                         'logicalPortConfigInfos': [{'bay': '1', 'port': 'X3', 'speed': 'Auto'},
                                                    {'bay': '2', 'port': 'X3', 'speed': 'Auto'}]}],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None},

        'Perf_new_lig4icm':
        {'name': 'LIG_B1',
         'type': 'logical-interconnect-groupV300',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                     ],
         'uplinkSets': [{'name': 'ETH-UP1',
                         'ethernetNetworkType': 'Tagged',
                         'networkType': 'Ethernet',
                         'networkUris': ['ETH_NW1'],
                         'nativeNetworkUri': None,
                         'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '1', 'port': 'X1', 'speed': 'Auto'},
                                                    {'bay': '2', 'port': 'X1', 'speed': 'Auto'}]},

                        {'name': 'ETH-Up2',
                         'ethernetNetworkType': 'Tagged',
                         'networkType': 'Ethernet',
                         'networkUris': ['FCOE_NW100'],
                         'mode': 'Auto',
                         'nativeNetworkUri': None,
                         'logicalPortConfigInfos': [{'bay': '1', 'port': 'X3', 'speed': 'Auto'},
                                                    {'bay': '2', 'port': 'X3', 'speed': 'Auto'}]}],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None},

        'new_lig1':
        {'name': 'LIG_B1',
         'type': 'logical-interconnect-groupV4',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': BB_icmap,
         'uplinkSets': [{'name': 'FC-FA1',
                         'ethernetNetworkType': 'NotApplicable',
                         'networkType': 'FibreChannel',
                         'networkUris': ['FC_NW1'],
                         'nativeNetworkUri': None,
                         'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '3', 'port': '2', 'speed': 'Auto'}]},
                        {'name': 'ETH_FA1',
                         'ethernetNetworkType': 'Tagged',
                         'networkType': 'Ethernet',
                         'networkUris': ['ETH_NW1'],
                         'primaryPort': None,
                         'nativeNetworkUri': None,
                         'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '1', 'port': 'X2', 'speed': 'Auto'}]},
                        {'name': 'ETH_FA2',
                         'ethernetNetworkType': 'Tagged',
                         'networkType': 'Ethernet',
                         'networkUris': ['ETH_NW2'],
                         'primaryPort': None,
                         'nativeNetworkUri': None,
                         'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '2', 'port': 'X2', 'speed': 'Auto'}]},
                        {'name': 'FC-FA2',
                            'ethernetNetworkType': 'NotApplicable',
                            'networkType': 'FibreChannel',
                            'networkUris': ['FC_NW2'],
                            'nativeNetworkUri': None,
                            'mode': 'Auto',
                            'logicalPortConfigInfos': [{'bay': '4', 'port': '2', 'speed': 'Auto'}]}
                        ],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None},


        'ligTT':
        {'name': 'LIG1',
         'type': 'logical-interconnect-groupV300',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': icmap,
         'uplinkSets': [uplink_sets['us1'].copy(), uplink_sets['us2'].copy()],
         'stackingMode': 'Enclosure',
         'ethernetSettings': {'type': 'EthernetInterconnectSettingsV201', 'enableRichTLV': True, 'enableTaggedLldp': True, 'interconnectType': 'Ethernet'},
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None},

        'ligFT':
        {'name': 'LIG1',
         'type': 'logical-interconnect-groupV3',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': icmap,
         'uplinkSets': [uplink_sets['us1'].copy(), uplink_sets['us2'].copy()],
         'stackingMode': 'Enclosure',
         'ethernetSettings': {'type': 'EthernetInterconnectSettingsV201', 'enableRichTLV': False, 'enableTaggedLldp': True, 'interconnectType': 'Ethernet'},
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None},

        'ligTF':
        {'name': 'LIG1',
         'type': 'logical-interconnect-groupV3',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': icmap,
         'uplinkSets': [uplink_sets['us1'].copy(), uplink_sets['us2'].copy()],
         'stackingMode': 'Enclosure',
         'ethernetSettings': {'type': 'EthernetInterconnectSettingsV201', 'enableRichTLV': True, 'enableTaggedLldp': False, 'interconnectType': 'Ethernet'},
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None},

        'ligFF':
        {'name': 'LIG1',
         'type': 'logical-interconnect-groupV3',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': icmap,
         'uplinkSets': [uplink_sets['us1'].copy(), uplink_sets['us2'].copy()],
         'stackingMode': 'Enclosure',
         'ethernetSettings': {'type': 'EthernetInterconnectSettingsV201', 'enableRichTLV': False, 'enableTaggedLldp': False, 'interconnectType': 'Ethernet'},
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None}


        }


#  Got from H V Harish

lig_c7k_enc = {"type": "logical-interconnect-groupV300",
               "ethernetSettings": {"type": "EthernetInterconnectSettingsV201", "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
               "description": None,
               "name": "LIG_B1",
               "interconnectMapTemplate":
               {"interconnectMapEntryTemplates": [
                   {"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 1}, {"type": "Enclosure", "relativeValue": 1}]}, "logicalDownlinkUri": None, "permittedInterconnectTypeUri": "HP VC FlexFabric 10Gb/24-Port Module", "enclosureIndex": 1},
                   {"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 2}, {"type": "Enclosure", "relativeValue": 2}]}, "logicalDownlinkUri": None, "permittedInterconnectTypeUri": "HP VC FlexFabric 10Gb/24-Port Module", "enclosureIndex": 2},
                   {"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 3}, {"type": "Enclosure", "relativeValue": 1}]}, "logicalDownlinkUri": None, "permittedInterconnectTypeUri": "HP VC 16Gb 24-Port FC Module", "enclosureIndex": 1},
                   {"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 4}, {"type": "Enclosure", "relativeValue": 2}]}, "logicalDownlinkUri": None, "permittedInterconnectTypeUri": "HP VC 16Gb 24-Port FC Module", "enclosureIndex": 2},
                   {"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 6}, {"type": "Enclosure", "relativeValue": 2}]}, "logicalDownlinkUri": None, "permittedInterconnectTypeUri": "HP VC FlexFabric 10Gb/24-Port Module", "enclosureIndex": 2},
                   {"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 7}, {"type": "Enclosure", "relativeValue": 1}]}, "logicalDownlinkUri": None, "permittedInterconnectTypeUri": "HP VC 16Gb 24-Port FC Module", "enclosureIndex": 1}]},
               "enclosureType": "C7000",
               "enclosureIndexes": [1, 2],
               "internalNetworkUris": [],
               "snmpConfiguration": {"type": "snmp-configuration", "readCommunity": "public", "systemContact": "", "trapDestinations": None, "snmpAccess": None, "enabled": True, "description": None, "name": None, "state": None, "category": "snmp-configuration"},
               "qosConfiguration": {"activeQosConfig": {"type": "QosConfiguration", "configType": "Passthrough", "uplinkClassificationType": None, "downlinkClassificationType": None, "qosTrafficClassifiers": None, "description": None, "status": None, "name": None, "state": None, "created": None, "eTag": None, "modified": None, "category": "qos-aggregated-configuration", "uri": None}, "inactiveFCoEQosConfig": None, "inactiveNonFCoEQosConfig": None, "type": "qos-aggregated-configuration", "name": None, "state": None, "status": None, "eTag": None, "modified": None, "created": None, "category": "qos-aggregated-configuration", "uri": None},
               "uplinkSets": [
                   {"networkUris": ["SAN-1-A"], "mode":"Auto", "lacpTimer":"Short", "primaryPort":None,
                    "logicalPortConfigInfos":[{"desiredSpeed": "Auto", "logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 3}, {"type": "Port", "relativeValue": 17}, {"type": "Enclosure", "relativeValue": 1}]}}],
                    "networkType": "FibreChannel", "ethernetNetworkType": None, "name": "SAN-1-A"},
                   {"networkUris": ["SAN-1-AB"], "mode":"Auto", "lacpTimer":"Short", "primaryPort":None,
                    "logicalPortConfigInfos":[{"desiredSpeed": "Auto", "logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 4}, {"type": "Port", "relativeValue": 17}, {"type": "Enclosure", "relativeValue": 1}]}}],
                    "networkType": "FibreChannel", "ethernetNetworkType": None, "name": "SAN-1-AB"}
               ]
               }


telemetry = {'enableTelemetry': True, 'sampleInterval': 400, 'sampleCount': 20}

trapDestinations = [{'trapSeverities': ['Major'],
                     'enetTrapCategories': ['Other'],
                     'fcTrapCategories': ['Other'],
                     'vcmTrapCategories': ['Legacy'],
                     'trapFormat': 'SNMPv1',
                     'trapDestination': '192.168.99.99',
                     'communityString': 'public'}]

snmp = {'snmpAccess': ['192.168.1.0/24'],
        'trapDestinations': trapDestinations}

enet = {'enableFastMacCacheFailover': False}

fc_networks_NW1 = [{'type': 'fc-networkV4', 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
                    'name': 'FC_NW1', 'managedSanUri': None, 'fabricType': 'FabricAttach', 'connectionTemplateUri': None}]


fc_networks_NW1_Original = [{'type': 'fc-networkV4', 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
                             'name': 'FC_NW1', 'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'}]

fc_network = [{'type': 'fc-networkV4',
               'linkStabilityTime': 30,
               'fabricType': 'FabricAttach',
               'autoLoginRedistribution': True,
               'name': 'fc1',
               'state': 'Active'}]

fc_networks_NW2 = [{'type': 'fc-networkV4', 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
                    'name': 'FC_NW2', 'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'}]
"""
profile1 = {'type': 'ServerProfileV5', 'serverHardwareUri': 'WPST-PABA58-EN1, bay 1',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:WPST-PABA58-EN1', 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'WPST-PABA58-EN1_Bay1-BFS', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
                    'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:eth-102', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Flb 1:1-b', 'requestedMbps': '2500', 'networkUri': 'FCOE:fcoe-1002', 'boot': {'priority': 'Primary', 'targets': [{'arrayWwpn': '21110002AC003655', 'lun': '0'}]}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    ]}

profile2 = {'type': 'ServerProfileV5', 'serverHardwareUri': 'WPST-PABA58-EN1, bay 2',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:WPST-PABA58-EN1', 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'WPST-PABA58-EN1_Bay2', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
                    'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:eth-102', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                   ]}

server_profiles = [profile1.copy(), profile2.copy()]

"""
server_profiles = [{'type': 'ServerProfileV5', 'serverHardwareUri': 'SGH420HHYA, bay 8',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:SGH420HHYA', 'enclosureGroupUri': 'EG:EG_B1', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'SP_PERMC1', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': False},
                    'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezzanine 1:1', 'requestedMbps': '2500', 'networkUri': 'ETH:FC_NW1', 'mac': None, 'wwpn': '', 'wwnn': ''},

                                    ]},
                   {'type': 'ServerProfileV5', 'serverHardwareUri': 'SGH420HHYA, bay 3',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:SGH420HHYA', 'enclosureGroupUri': 'EG:EG_B1', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'SP_PERMC2', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': False},
                    'connections': [{'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:FC_NW2', 'mac': None, 'wwpn': '', 'wwnn': ''},

                                    ]},
                   ]

server_profiles1 = [{'type': 'ServerProfileV5', 'serverHardwareUri': 'SGH411DFYA, bay 3',
                     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:SGH411DFYA', 'enclosureGroupUri': 'EG:EGLldp', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                     'name': 'Sp_APIC', 'description': '', 'affinity': 'Bay',
                     'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
                     'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:APIC1', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                     {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-b', 'requestedMbps': '2500', 'networkUri': 'ETH:APIC2', 'boot': {'priority': 'Primary', 'targets': [{'arrayWwpn': '21110002AC003655', 'lun': '0'}]}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                     ]},

                    ]

server_profiles_pp = [
    {'type': 'ServerProfileV6', 'serverHardwareUri': ENC1 + ', bay 8',
     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_B1',
     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
     'name': 'Profile_permc', 'description': '', 'affinity': 'Bay',
     'boot': {'manageBoot': False, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
     'connections': [
         {'id': 1, 'name': '1', 'functionType': 'FibreChannel', 'portId': 'Auto',
          'requestedMbps': 'Auto', 'networkUri': 'FC:FC_NW1',
          'mac': None, 'wwpn': '', 'wwnn': ''},
         {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Auto',
          'requestedMbps': 'Auto', 'networkUri': 'FC:FC_NW2',
          'mac': None, 'wwpn': '', 'wwnn': ''},
     ]},

]


mytests_server_profiles_2FCOE = [
    {'type': 'ServerProfileV6', 'serverHardwareUri': ENC1 + ', bay 8',
     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_B1',
     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
     'name': '2ETH_2FCOE', 'description': '', 'affinity': 'Bay',
     'boot': {'manageBoot': 'true', 'order': ['HardDisk']},
     'bootMode':{'manageMode': 'true', 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
     'connections': [

         {'id': 1, 'name': '1', 'functionType': 'FibreChannel', 'portId': 'Auto',
          'requestedMbps': int(2500), 'networkUri': 'FCOE:FCOE_NW100',
          'boot': {'priority': 'Secondary', 'bootVolumeSource': 'UserDefined', 'targets': [{'arrayWwpn': '21220002AC009290', 'lun': '1'}]},
          'mac': None, 'wwpn': '', 'wwnn': ''},


         {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Auto',
          'requestedMbps': int(2500), 'networkUri': 'FCOE:FCOE_NW200',
          'boot': {'priority': 'Secondary', 'bootVolumeSource': 'UserDefined', 'targets': [{'arrayWwpn': '21220002AC009290', 'lun': '0'}]},
          'mac': None, 'wwpn': '', 'wwnn': ''},
     ]},

]

server_profiles_2eth_2fcoe = [
    {'type': 'ServerProfileV6', 'serverHardwareUri': ENC1 + ', bay 3',
     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_B1',
     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
     'name': 'Profile_permc', 'description': '', 'affinity': 'Bay',
     'boot': {'manageBoot': False, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
     'bootMode':{'manageMode': 'true', 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
     'connections': [
         {'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Auto',
          'requestedMbps': int(2500), 'networkUri': 'ETH:ETH_NW1',
          'mac': None, 'wwpn': '', 'wwnn': ''},
         {'id': 2, 'name': int(2500), 'functionType': 'Ethernet', 'portId': 'Auto',
          'requestedMbps': '2', 'networkUri': 'ETH:ETH_NW2',
          'mac': None, 'wwpn': '', 'wwnn': ''},
         {'id': 3, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Auto',
          'requestedMbps': int(2), 'networkUri': 'FCOE:FCOE_NW100',
          'mac': None, 'wwpn': '', 'wwnn': ''},
         {'id': 4, 'name': '4', 'functionType': 'FibreChannel', 'portId': 'Flb 1:1-b',
          'requestedMbps': int(2), 'networkUri': 'FCOE:FCOE_NW101',
          'mac': None, 'wwpn': '', 'wwnn': ''},
     ]},

]


server_profiles_1eth_1fcoe = [
    {'type': 'ServerProfileV6', 'serverHardwareUri': ENC1 + ', bay 9',
     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_B1',
     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
     'name': '4Eth', 'description': '', 'affinity': 'Bay',
     'boot': {'manageBoot': False, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
     'connections': [
         {'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Auto',
          'requestedMbps': int(2500), 'networkUri': 'ETH:ETH_NW1',
          'mac': None, 'wwpn': '', 'wwnn': ''},

         {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Auto',
          'requestedMbps': int(2500), 'networkUri': 'FCOE:FCOE_NW100',
          'mac': None, 'wwpn': '', 'wwnn': ''},

     ]},

]

server_profiles_4ethonly = [
    {'type': 'ServerProfileV6', 'serverHardwareUri': ENC1 + ', bay 8',
     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_B1',
     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
     'name': '4Eth', 'description': '', 'affinity': 'Bay',
     'boot': {'manageBoot': False, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
     'bootMode':{'manageMode': 'true', 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
     'connections': [
         {'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a',
          'requestedMbps': int(2500), 'networkUri': 'ETH:ETH_NW1',
          'mac': None, 'wwpn': '', 'wwnn': ''},

         {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a',
          'requestedMbps': int(2500), 'networkUri': 'ETH:ETH_NW1',
          'mac': None, 'wwpn': '', 'wwnn': ''},
         {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-c',
          'requestedMbps': int(2500), 'networkUri': 'ETH:ETH_NW2',
          'mac': None, 'wwpn': '', 'wwnn': ''},
         {'id': 4, 'name': '4', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-c',
          'requestedMbps': int(2500), 'networkUri': 'ETH:ETH_NW2',
          'mac': None, 'wwpn': '', 'wwnn': ''},

     ]},

]


server_profiles_nwset4ethonly = [
    {'type': 'ServerProfileV6', 'serverHardwareUri': ENC1 + ', bay 8',
     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_B1',
     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
     'name': '4Eth', 'description': '', 'affinity': 'Bay',
     'boot': {'manageBoot': False, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
     'connections': [
         {'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a',
          'requestedMbps': int(2500), 'networkUri': 'ETH:NW_set1',
          'mac': None, 'wwpn': '', 'wwnn': ''},

         {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a',
          'requestedMbps': int(2500), 'networkUri': 'ETH:NW_set2',
          'mac': None, 'wwpn': '', 'wwnn': ''},

     ]},

]


New_server_profiles_4ETH = [
    {'type': 'ServerProfileV6', 'serverHardwareUri': ENC1 + ', bay 8',
     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_B1',
     'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
     'name': '4Eth', 'description': '', 'affinity': 'Bay',
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
     'connections': [
         {'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a',
          'requestedMbps': int(2500), 'networkUri': 'ETH:ETH_NW1',
          'mac': None, 'wwpn': '', 'wwnn': ''},

         {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a',
          'requestedMbps': int(2500), 'networkUri': 'ETH:ETH_NW1',
          'mac': None, 'wwpn': '', 'wwnn': ''},
         {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-c',
          'requestedMbps': int(2500), 'networkUri': 'ETH:ETH_NW2',
          'mac': None, 'wwpn': '', 'wwnn': ''},
         {'id': 4, 'name': '4', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-c',
          'requestedMbps': int(2500), 'networkUri': 'ETH:ETH_NW2',
          'mac': None, 'wwpn': '', 'wwnn': ''},

     ]},

]

server_profiles_4eth_fwupdate = [
    {'type': 'ServerProfileV6', 'serverHardwareUri': ENC1 + ', bay 8',
     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_B1',
     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
     'name': '4Eth_fw update', 'description': '', 'affinity': 'Bay',
     'boot': {'manageBoot': False, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
     'bootMode':{'manageMode': 'true', 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
     'firmware': {'manageFirmware': 'true', 'firmwareBaselineUri': '/rest/firmware-drivers/SPPgen9snap6_2016_0517_107', 'forceInstallFirmware': 'true', 'firmwareInstallType': 'FirmwareOnlyOfflineMode'},
     'connections': [
         {'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a',
          'requestedMbps': int(2500), 'networkUri': 'ETH:ETH_NW1',
          'mac': None, 'wwpn': '', 'wwnn': ''},

         {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a',
          'requestedMbps': int(2500), 'networkUri': 'ETH:ETH_NW1',
          'mac': None, 'wwpn': '', 'wwnn': ''},
         {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-c',
          'requestedMbps': int(2500), 'networkUri': 'ETH:ETH_NW2',
          'mac': None, 'wwpn': '', 'wwnn': ''},
         {'id': 4, 'name': '4', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-c',
          'requestedMbps': int(2500), 'networkUri': 'ETH:ETH_NW2',
          'mac': None, 'wwpn': '', 'wwnn': ''},

     ]},

]

server_profiles_2ethonly = [
    {'type': 'ServerProfileV6', 'serverHardwareUri': ENC1 + ', bay 16',
     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_B1',
     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
     'name': '2Eth', 'description': '', 'affinity': 'Bay',
     'boot': {'manageBoot': False, 'order': ['HardDisk']},
     'bootMode':{'manageMode': 'true', 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
     'connections': [
         {'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a',
          'requestedMbps': int(2500), 'networkUri': 'ETH:ETH_NW2',
          'mac': None, 'wwpn': '', 'wwnn': ''},

         {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a',
          'requestedMbps': int(2500), 'networkUri': 'ETH:ETH_NW2',
          'mac': None, 'wwpn': '', 'wwnn': ''},


     ]},

]


server_profiles_2FConly = [
    {'type': 'ServerProfileV6', 'serverHardwareUri': ENC1 + ', bay 8',
     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_B1',
     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
     'name': '2FC', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': False, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
                    'bootMode':{'manageMode': 'true', 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                    'connections': [
                        {'id': 1, 'name': '1', 'functionType': 'FibreChannel', 'portId': 'Auto',
                         'requestedMbps': 'Auto', 'networkUri': 'FC:FC_NW1',
                         'mac': None, 'wwpn': '', 'wwnn': ''},
                        {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Auto',
                         'requestedMbps': 'Auto', 'networkUri': 'FC:FC_NW2',
                         'mac': None, 'wwpn': '', 'wwnn': ''},
                    ]},

]


server_profiles_2ETH2FCOEonly = [
    {'type': 'ServerProfileV6', 'serverHardwareUri': ENC1 + ', bay 8',
     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_B1',
     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
     'name': '2ETH_2FCOE', 'description': '', 'affinity': 'Bay',
     'boot': {'manageBoot': False, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
     'bootMode':{'manageMode': 'true', 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
     'connections': [
         {'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Auto',
          'requestedMbps': int(2500), 'networkUri': 'ETH:ETH_NW3',
          'mac': None, 'wwpn': '', 'wwnn': ''},
         {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Auto',
          'requestedMbps': int(2500), 'networkUri': 'ETH:ETH_NW3',
          'mac': None, 'wwpn': '', 'wwnn': ''},

         {'id': 3, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Auto',
          'requestedMbps': int(2500), 'networkUri': 'FCOE:FCOE_NW100',
          'mac': None, 'wwpn': '', 'wwnn': ''},
         {'id': 4, 'name': '4', 'functionType': 'FibreChannel', 'portId': 'Auto',
          'requestedMbps': int(2500), 'networkUri': 'FCOE:FCOE_NW200',
          'mac': None, 'wwpn': '', 'wwnn': ''},
     ]},

]

server_profiles_2ETH2FCOEonlyBFS = [
    {'type': 'ServerProfileV6', 'serverHardwareUri': ENC1 + ', bay 8',
     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_B1',
     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
     'name': '2ETH_2FCOE', 'description': '', 'affinity': 'Bay',
     'boot': {'manageBoot': False, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
     'bootMode':{'manageMode': 'true', 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
     'sanStorage': {'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': 'true', 'volumeAttachments': [{'id': 1, 'volumeUri': None, 'isBootVolume': 'false', 'lunType': 'Auto', 'lun': None, 'storagePaths': [], 'volumeName':'Vol_name_bb', 'volumeDescription':'create_vm', 'volumeStoragePoolUri':'/rest/storage-pools/00262AF9-E05F-46FE-A732-CCABC5A77A79', 'volumeStorageSystemUri':'/rest/storage-systems/1637520', 'volumeProvisionType':'Full', 'volumeProvisionedCapacityBytes':'27917287424', 'volumeShareable':'false', 'permanent':'true'}]},
     'connections': [
         {'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Auto',
          'requestedMbps': int(2500), 'networkUri': 'ETH:ETH_NW2',
          'mac': None, 'wwpn': '', 'wwnn': ''},
         {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Auto',
          'requestedMbps': int(2500), 'networkUri': 'ETH:ETH_NW2',
          'mac': None, 'wwpn': '', 'wwnn': ''},

         {'id': 3, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Auto',
          'requestedMbps': int(2500), 'networkUri': 'FCOE:FCOE_NW100',
          'mac': None, 'wwpn': '', 'wwnn': ''},
         {'id': 4, 'name': '4', 'functionType': 'FibreChannel', 'portId': 'Auto',
          'requestedMbps': int(2500), 'networkUri': 'FCOE:FCOE_NW200',
          'mac': None, 'wwpn': '', 'wwnn': ''},
     ]},

]

server_profiles_2ETH2FCOEonlyBFSN = [
    {'type': 'ServerProfileV6', 'serverHardwareUri': ENC1 + ', bay 8',
     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_B1',
     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
     'name': '2ETH_2FCOE', 'description': '', 'affinity': 'Bay',
     'boot': {'manageBoot': False, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
     'bootMode':{'manageMode': 'true', 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
     'sanStorage': {'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': 'true', 'volumeAttachments': [{'id': 1, 'volumeUri': '/rest/storage-volumes/E97102D3-D027-43E2-B382-86D884AC48B2', 'isBootVolume': 'false', 'lunType': 'Auto', 'lun': None, 'storagePaths': [{'isEnabled': 'true', 'connectionId': 1, 'storageTargetType': 'Auto', 'storageTargets': []}, {'isEnabled': 'true', 'connectionId': 2, 'storageTargetType': 'Auto', 'storageTargets': []}]}]},
     'connections': [
         {'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Auto',
          'requestedMbps': int(2500), 'networkUri': 'ETH:ETH_NW2',
          'mac': None, 'wwpn': '', 'wwnn': ''},
         {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Auto',
          'requestedMbps': int(2500), 'networkUri': 'ETH:ETH_NW2',
          'mac': None, 'wwpn': '', 'wwnn': ''},

         {'id': 3, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Auto',
          'requestedMbps': int(2500), 'networkUri': 'FCOE:FCOE_NW100',
          'mac': None, 'wwpn': '', 'wwnn': ''},
         {'id': 4, 'name': '4', 'functionType': 'FibreChannel', 'portId': 'Auto',
          'requestedMbps': int(2500), 'networkUri': 'FCOE:FCOE_NW200',
          'mac': None, 'wwpn': '', 'wwnn': ''},
     ]},

]


server_profiles_2FConlyBFS = [
    {'type': 'ServerProfileV6', 'serverHardwareUri': ENC1 + ', bay 8',
     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_B1',
     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
     'name': '2FC', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': False, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
                    'bootMode':{'manageMode': 'true', 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                    'sanStorage': {'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': 'true', 'volumeAttachments': [{'id': 1, 'volumeUri': None, 'isBootVolume': 'false', 'lunType': 'Auto', 'lun': None, 'storagePaths': [], 'volumeName':'Vol_name_bb', 'volumeDescription':'create_vm', 'volumeStoragePoolUri':'/rest/storage-pools/00262AF9-E05F-46FE-A732-CCABC5A77A79', 'volumeStorageSystemUri':'/rest/storage-systems/1637520', 'volumeProvisionType':'Full', 'volumeProvisionedCapacityBytes':'27917287424', 'volumeShareable':'false', 'permanent':'true'}]},
                    'connections': [
                        {'id': 1, 'name': '1', 'functionType': 'FibreChannel', 'portId': 'Auto',
                         'requestedMbps': 'Auto', 'networkUri': 'FC:FC_NW1',
                         'mac': None, 'wwpn': '', 'wwnn': ''},
                        {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Auto',
                         'requestedMbps': 'Auto', 'networkUri': 'FC:FC_NW2',
                         'mac': None, 'wwpn': '', 'wwnn': ''},
                    ]},

]

server_profiles_2FConlyBFSN = [
    {'type': 'ServerProfileV6', 'serverHardwareUri': ENC1 + ', bay 8',
     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_B1',
     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
     'name': '2FC', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': False, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
                    'bootMode':{'manageMode': 'true', 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                    'sanStorage': {'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': 'true', 'volumeAttachments': [{'id': 1, 'volumeUri': '/rest/storage-volumes/E97102D3-D027-43E2-B382-86D884AC48B2', 'isBootVolume': 'false', 'lunType': 'Auto', 'lun': None, 'storagePaths': [{'isEnabled': 'true', 'connectionId': 1, 'storageTargetType': 'Auto', 'storageTargets': []}, {'isEnabled': 'true', 'connectionId': 2, 'storageTargetType': 'Auto', 'storageTargets': []}]}]},
                    'connections': [
                        {'id': 1, 'name': '1', 'functionType': 'FibreChannel', 'portId': 'Auto',
                         'requestedMbps': 'Auto', 'networkUri': 'FC:FC_NW1',
                         'mac': None, 'wwpn': '', 'wwnn': ''},
                        {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Auto',
                         'requestedMbps': 'Auto', 'networkUri': 'FC:FC_NW2',
                         'mac': None, 'wwpn': '', 'wwnn': ''},
                    ]},

]


server_profiles_2ethonly_BFS = [
    {'type': 'ServerProfileV6', 'serverHardwareUri': ENC1 + ', bay 8',
     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_B1',
     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
     'name': '2Eth', 'description': '', 'affinity': 'Bay',
     'boot': {'manageBoot': False, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
     'bootMode':{'manageMode': 'true', 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
     'sanStorage': {'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': 'true', 'volumeAttachments': [{'id': 1, 'volumeUri': None, 'isBootVolume': 'false', 'lunType': 'Auto', 'lun': None, 'storagePaths': [], 'volumeName':'Vol_name_bb', 'volumeDescription':'create_vm', 'volumeStoragePoolUri':'/rest/storage-pools/00262AF9-E05F-46FE-A732-CCABC5A77A79', 'volumeStorageSystemUri':'/rest/storage-systems/1637520', 'volumeProvisionType':'Full', 'volumeProvisionedCapacityBytes':'27917287424', 'volumeShareable':'false', 'permanent':'true'}]},
     'connections': [
         {'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a',
          'requestedMbps': int(2500), 'networkUri': 'ETH:ETH_NW2',
          'mac': None, 'wwpn': '', 'wwnn': ''},

         {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a',
          'requestedMbps': int(2500), 'networkUri': 'ETH:ETH_NW2',
          'mac': None, 'wwpn': '', 'wwnn': ''},


     ]},

]

server_profiles_2ethonly_BFSN = [
    {'type': 'ServerProfileV6', 'serverHardwareUri': ENC1 + ', bay 8',
     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_B1',
     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
     'name': '2Eth', 'description': '', 'affinity': 'Bay',
     'boot': {'manageBoot': False, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
     'bootMode':{'manageMode': 'true', 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
     'sanStorage': {'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': 'true', 'volumeAttachments': [{'id': 1, 'volumeUri': '/rest/storage-volumes/E97102D3-D027-43E2-B382-86D884AC48B2', 'isBootVolume': 'false', 'lunType': 'Auto', 'lun': None, 'storagePaths': [{'isEnabled': 'true', 'connectionId': 1, 'storageTargetType': 'Auto', 'storageTargets': []}, {'isEnabled': 'true', 'connectionId': 2, 'storageTargetType': 'Auto', 'storageTargets': []}]}]},
     'connections': [
         {'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a',
          'requestedMbps': int(2500), 'networkUri': 'ETH:ETH_NW2',
          'mac': None, 'wwpn': '', 'wwnn': ''},

         {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a',
          'requestedMbps': int(2500), 'networkUri': 'ETH:ETH_NW2',
          'mac': None, 'wwpn': '', 'wwnn': ''},


     ]},

]

bot_new_server_profiles_2FConlyBFS = [
    {'type': 'ServerProfileV6', 'serverHardwareUri': ENC1 + ', bay 8',
     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_B1',
     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
     'name': '2FC', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': 'true', 'order': ['HardDisk', 'CD', 'Floppy', 'USB', 'PXE']},
                    'bootMode':{'manageMode': 'true', 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                    'sanStorage': {'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': 'true', 'volumeAttachments': [{'id': 1, 'volumeUri': None, 'isBootVolume': 'false', 'lunType': 'Auto', 'lun': None, 'storagePaths': [], 'volumeName':'Vol_name_bb', 'volumeDescription':'create_vm', 'volumeStoragePoolUri':'/rest/storage-pools/00262AF9-E05F-46FE-A732-CCABC5A77A79', 'volumeStorageSystemUri':'/rest/storage-systems/1637520', 'volumeProvisionType':'Full', 'volumeProvisionedCapacityBytes':'27917287424', 'volumeShareable':'false', 'permanent':'true'}]},
                    'connections': [
                        {'id': 1, 'name': '1', 'functionType': 'FibreChannel', 'portId': 'Auto',
                         'requestedMbps': 'Auto', 'networkUri': 'FC:FC_NW1',
                         'boot': {'priority': 'Primary', 'bootVolumeSource': 'UserDefined', 'targets': [{'arrayWwpn': '21120002AC009290', 'lun': '1'}]},
                         'mac': None, 'wwpn': '', 'wwnn': ''},
                        {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Auto',
                         'requestedMbps': 'Auto', 'networkUri': 'FC:FC_NW2',
                         'boot': {'priority': 'Secondary', 'bootVolumeSource': 'UserDefined', 'targets': [{'arrayWwpn': '21110002AC009290', 'lun': '1'}]},
                         'mac': None, 'wwpn': '', 'wwnn': ''},
                    ]},

]


storagepath_server_profiles_2FConlyBFS = [
    {'type': 'ServerProfileV6', 'serverHardwareUri': ENC1 + ', bay 8',
     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_B1',
     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
     'name': '2FC', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': 'true', 'order': ['HardDisk']},
                    'bootMode':{'manageMode': 'true', 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                    'sanStorage': {'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': 'true', 'volumeAttachments': [{'id': 1, 'volumeUri': '/rest/storage-volumes/E97102D3-D027-43E2-B382-86D884AC48B2', 'isBootVolume': 'false', 'lunType': 'Auto', 'lun': None, 'storagePaths': [{'isEnabled': 'true', 'connectionId': 1, 'storageTargetType': 'Auto', 'storageTargets': []}, {'isEnabled': 'true', 'connectionId': 2, 'storageTargetType': 'Auto', 'storageTargets': []}]}]},
                    'connections': [
                        {'id': 1, 'name': '1', 'functionType': 'FibreChannel', 'portId': 'Auto',
                         'requestedMbps': 'Auto', 'networkUri': 'FC:FC_NW1',
                         'boot': {'priority': 'Primary', 'bootVolumeSource': 'UserDefined', 'targets': [{'arrayWwpn': '500143803682FD68', 'lun': '1'}]},
                         'mac': None, 'wwpn': '', 'wwnn': ''},
                        {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Auto',
                         'requestedMbps': 'Auto', 'networkUri': 'FC:FC_NW2',
                         'boot': {'priority': 'Secondary', 'bootVolumeSource': 'UserDefined', 'targets': [{'arrayWwpn': '500143803682FD68', 'lun': '1'}]},
                         'mac': None, 'wwpn': '', 'wwnn': ''},
                    ]},

]

Nstoragepath_server_profiles_2FCBFS_3parwwn = [
    {'type': 'ServerProfileV6', 'serverHardwareUri': ENC1 + ', bay 16',
     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_B1',
     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
     'name': '2FC_BFS', 'description': '', 'affinity': 'Bay',
     'boot': {'manageBoot': 'true', 'order': ['HardDisk']},
     'bootMode':{'manageMode': 'true', 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
     'connections': [
         {'id': 1, 'name': '1', 'functionType': 'FibreChannel', 'portId': 'Auto',
          'requestedMbps': 'Auto', 'networkUri': 'FC:FC_NW1',
          'boot': {'priority': 'Primary', 'bootVolumeSource': 'UserDefined', 'targets': [{'arrayWwpn': '21120002AC009290', 'lun': '1'}]},
          'mac': None, 'wwpn': '', 'wwnn': ''},
         {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Auto',
          'requestedMbps': 'Auto', 'networkUri': 'FC:FC_NW2',
          'boot': {'priority': 'Secondary', 'bootVolumeSource': 'UserDefined', 'targets': [{'arrayWwpn': '21120002AC009290', 'lun': '1'}]},
          'mac': None, 'wwpn': '', 'wwnn': ''},
     ]},

]

server_profiles_2FC_Data = [
    {'type': 'ServerProfileV6', 'serverHardwareUri': ENC1 + ', bay 16',
     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_B1',
     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
     'name': '2FC', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': False, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
                    'bootMode':{'manageMode': 'true', 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                    'connections': [
                        {'id': 1, 'name': '1', 'functionType': 'FibreChannel', 'portId': 'Auto',
                         'requestedMbps': 'Auto', 'networkUri': 'FC:FC_NW1',
                         'mac': None, 'wwpn': '', 'wwnn': ''},
                        {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Auto',
                         'requestedMbps': 'Auto', 'networkUri': 'FC:FC_NW2',
                         'mac': None, 'wwpn': '', 'wwnn': ''},
                    ]},

]

server_profiles_2FC_Data_SP = [
    {'type': 'ServerProfileV6', 'serverHardwareUri': ENC1 + ', bay 7',
     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_B1',
     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
     'name': 'server_profile_bay2', 'description': '', 'affinity': 'Bay',
     'boot': {'manageBoot': False, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
     'bootMode':{'manageMode': 'true', 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
     'connections': [
         {'id': 1, 'name': '1', 'functionType': 'FibreChannel', 'portId': 'Auto',
          'requestedMbps': 'Auto', 'networkUri': 'FC:FC_NW1',
          'mac': None, 'wwpn': '', 'wwnn': ''},
         {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Auto',
          'requestedMbps': 'Auto', 'networkUri': 'FC:FC_NW2',
          'mac': None, 'wwpn': '', 'wwnn': ''},
     ]},

]

NN_server_profiles_2FC_2ETH_Data = [
    {'type': 'ServerProfileV6', 'serverHardwareUri': ENC1 + ', bay 8',
     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_B1',
     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
     'name': '2FC_2ETH_DATA', 'description': '', 'affinity': 'Bay',
     'boot': {'manageBoot': False, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
     'bootMode':{'manageMode': 'true', 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
     'connections': [
         {'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Auto',
          'requestedMbps': int(2500), 'networkUri': 'ETH:ETH_NW2',
          'mac': None, 'wwpn': '', 'wwnn': ''},
         {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Auto',
          'requestedMbps': int(2500), 'networkUri': 'ETH:ETH_NW2',
          'mac': None, 'wwpn': '', 'wwnn': ''},
         {'id': 3, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Auto',
          'requestedMbps': 'Auto', 'networkUri': 'FC:FC_NW1',
          'mac': None, 'wwpn': '', 'wwnn': ''},
         {'id': 4, 'name': '4', 'functionType': 'FibreChannel', 'portId': 'Auto',
          'requestedMbps': 'Auto', 'networkUri': 'FC:FC_NW2',
          'mac': None, 'wwpn': '', 'wwnn': ''},
     ]},

]


NN_server_profiles_2FC_2ETH_BFS = [
    {'type': 'ServerProfileV6', 'serverHardwareUri': ENC1 + ', bay 8',
     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_B1',
     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
     'name': '2FC_2ETH_BFS', 'description': '', 'affinity': 'Bay',
     'boot': {'manageBoot': 'true', 'order': ['HardDisk']},
     'bootMode':{'manageMode': 'true', 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
     'connections': [
         {'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Auto',
          'requestedMbps': int(2500), 'networkUri': 'ETH:ETH_NW2',
          'mac': None, 'wwpn': '', 'wwnn': ''},
         {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Auto',
          'requestedMbps': int(2500), 'networkUri': 'ETH:ETH_NW2',
          'mac': None, 'wwpn': '', 'wwnn': ''},
         {'id': 3, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Auto',
          'requestedMbps': 'Auto', 'networkUri': 'FC:FC_NW1',
          'boot': {'priority': 'Primary', 'bootVolumeSource': 'UserDefined', 'targets': [{'arrayWwpn': '21120002AC009290', 'lun': '0'}]},
          'mac': None, 'wwpn': '', 'wwnn': ''},
         {'id': 4, 'name': '4', 'functionType': 'FibreChannel', 'portId': 'Auto',
          'requestedMbps': 'Auto', 'networkUri': 'FC:FC_NW2',
          'boot': {'priority': 'Secondary', 'bootVolumeSource': 'UserDefined', 'targets': [{'arrayWwpn': '21120002AC009290', 'lun': '0'}]},
          'mac': None, 'wwpn': '', 'wwnn': ''},
     ]},

]


New_server_profiles_2ETH_2FCOE_BFS = [
    {'type': 'ServerProfileV6', 'serverHardwareUri': ENC1 + ', bay 8',
     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_B1',
     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
     'name': '2ETH_2FCOE_BFS', 'description': '', 'affinity': 'Bay',
     'boot': {'manageBoot': 'true', 'order': ['HardDisk']},
     'bootMode':{'manageMode': 'true', 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
     'connections': [
         {'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Auto',
          'requestedMbps': int(2500), 'networkUri': 'ETH:ETH_NW2',
          'mac': None, 'wwpn': '', 'wwnn': ''},
         {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Auto',
          'requestedMbps': int(2500), 'networkUri': 'ETH:ETH_NW2',
          'mac': None, 'wwpn': '', 'wwnn': ''},
         {'id': 3, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Auto',
          'requestedMbps': int(2500), 'networkUri': 'FCOE:FCOE_NW100',
          'boot': {'priority': 'Secondary', 'bootVolumeSource': 'UserDefined', 'targets': [{'arrayWwpn': '21210002AC009290', 'lun': '0'}]},
          'mac': None, 'wwpn': '', 'wwnn': ''},
         {'id': 4, 'name': '4', 'functionType': 'FibreChannel', 'portId': 'Auto',
          'requestedMbps': int(2500), 'networkUri': 'FCOE:FCOE_NW200',
          'boot': {'priority': 'Primary', 'bootVolumeSource': 'UserDefined', 'targets': [{'arrayWwpn': '21210002AC009290', 'lun': '0'}]},
          'mac': None, 'wwpn': '', 'wwnn': ''},
     ]},

]

New_server_profiles_2ETH_2FCOE_Data = [
    {'type': 'ServerProfileV6', 'serverHardwareUri': ENC1 + ', bay 7',
     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_B1',
     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
     'name': '2ETH_2FCOE_DATA', 'description': '', 'affinity': 'Bay',
     'boot': {'manageBoot': 'false', 'order': ['HardDisk']},
     'bootMode':{'manageMode': 'true', 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
     'connections': [
         {'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Auto',
          'requestedMbps': int(2500), 'networkUri': 'ETH:ETH_NW2',
          'mac': None, 'wwpn': '', 'wwnn': ''},
         {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Auto',
          'requestedMbps': int(2500), 'networkUri': 'ETH:ETH_NW2',
          'mac': None, 'wwpn': '', 'wwnn': ''},
         {'id': 3, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Auto',
          'requestedMbps': int(2500), 'networkUri': 'FCOE:FCOE_NW100',
          'mac': None, 'wwpn': '', 'wwnn': ''},
         {'id': 4, 'name': '4', 'functionType': 'FibreChannel', 'portId': 'Auto',
          'requestedMbps': int(2500), 'networkUri': 'FCOE:FCOE_NW200',
          'mac': None, 'wwpn': '', 'wwnn': ''},
     ]},

]

New_server_profiles_2FCOE_DATA = [
    {'type': 'ServerProfileV6', 'serverHardwareUri': ENC1 + ', bay 8',
     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_B1',
     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
     'name': '2ETH_2FCOE', 'description': '', 'affinity': 'Bay',
     'boot': {'manageBoot': False, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
     'bootMode':{'manageMode': 'true', 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
     'connections': [

         {'id': 1, 'name': '1', 'functionType': 'FibreChannel', 'portId': 'Auto',
          'requestedMbps': int(2500), 'networkUri': 'FCOE:FCOE_NW100',
          'mac': None, 'wwpn': '', 'wwnn': ''},
         {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Auto',
          'requestedMbps': int(2500), 'networkUri': 'FCOE:FCOE_NW200',
          'mac': None, 'wwpn': '', 'wwnn': ''},
     ]},

]

# ======================================================================
Nstoragepath_serverprofiles_2FConlyBFS_mezwwwn = [
    {'type': 'ServerProfileV6', 'serverHardwareUri': ENC1 + ', bay 8',
     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_B1',
     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
     'name': '2FC_BFS', 'description': '', 'affinity': 'Bay',
     'boot': {'manageBoot': 'true', 'order': ['HardDisk']},
     'bootMode':{'manageMode': 'true', 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
     'connections': [
         {'id': 1, 'name': '1', 'functionType': 'FibreChannel', 'portId': 'Auto',
          'requestedMbps': 'Auto', 'networkUri': 'FC:FC_NW1',
          'boot': {'priority': 'Primary', 'bootVolumeSource': 'UserDefined', 'targets': [{'arrayWwpn': '500143803682FD68', 'lun': '1'}]},
          'mac': None, 'wwpn': '', 'wwnn': ''},
         {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Auto',
          'requestedMbps': 'Auto', 'networkUri': 'FC:FC_NW2',
          'boot': {'priority': 'Secondary', 'bootVolumeSource': 'UserDefined', 'targets': [{'arrayWwpn': '500143803682FD6A', 'lun': '1'}]},
          'mac': None, 'wwpn': '', 'wwnn': ''},
     ]},

]
server_profiles_bb = [
    {'type': 'ServerProfileV6', 'serverHardwareUri': ENC1 + ', bay 8',
     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_B1',
     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
     'name': 'Profile5', 'description': '', 'affinity': 'Bay',
     'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
     'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-a',
                      'requestedMbps': '2500', 'networkUri': 'ETH:net_102',
                      'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                     {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1-b',
                      'requestedMbps': '2500', 'networkUri': 'FCOE:fcoe_103',
                      'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                     {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-a',
                      'requestedMbps': '2500', 'networkUri': 'ETH:net_101',
                      'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}]},
    {'type': 'ServerProfileV6', 'serverHardwareUri': ENC1 + ', bay 3',
     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG',
     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
     'name': 'Profile6', 'description': '', 'affinity': 'Bay',
     'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
     'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-a',
                      'requestedMbps': '2500', 'networkUri': 'ETH:net_102',
                      'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                     {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1-b',
                      'requestedMbps': '2500', 'networkUri': 'FCOE:fcoe_103',
                      'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                     {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-a',
                      'requestedMbps': '2500', 'networkUri': 'ETH:net_101',
                      'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}]},
]

fc_network_crt = {"name": "BBHUUY21", "connectionTemplateUri": "null", "linkStabilityTime": "30", "autoLoginRedistribution": "true", "fabricType": "FabricAttach", "managedSanUri": "null", "type": "fc-networkV300"}


New_server_profiles_1FCOE_Manage_volume_BFS = [
    {'type': 'ServerProfileV6', 'serverHardwareUri': ENC1 + ', bay 16',
     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_B1',
     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
     'name': '2ETH_2FCOE_BFS', 'description': '', 'affinity': 'Bay',
     'boot': {'manageBoot': 'true', 'order': ['HardDisk']},
     'bootMode':{'manageMode': 'true', 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
     'connections': [
         {'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Auto',
          'requestedMbps': int(2500), 'networkUri': 'ETH:ETH_NW2',
          'mac': None, 'wwpn': '', 'wwnn': ''},
         {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Auto',
          'requestedMbps': int(2500), 'networkUri': 'ETH:ETH_NW2',
          'mac': None, 'wwpn': '', 'wwnn': ''},
         {'id': 3, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Auto',
          'requestedMbps': int(2500), 'networkUri': 'FCOE:FCOE_NW100',
          'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'},
          'mac': None, 'wwpn': '', 'wwnn': ''},
         {'id': 4, 'name': '4', 'functionType': 'FibreChannel', 'portId': 'Auto',
          'requestedMbps': int(2500), 'networkUri': 'FCOE:FCOE_NW200',
          'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'},
          'mac': None, 'wwpn': '', 'wwnn': ''},
     ]},

]

New_server_profiles_2ETH_2FCOE_BFS_SANBB = [
    {'type': 'ServerProfileV6', 'serverHardwareUri': ENC1 + ', bay 16',
     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_B1',
     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
     'name': '2ETH_2FCOE_BFS', 'description': '', 'affinity': 'Bay',
     'boot': {'manageBoot': 'true', 'order': ['HardDisk']},
     'bootMode':{'manageMode': 'true', 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
     'sanStorage': {'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': 'true', 'volumeAttachments': [{'id': 1, 'volumeUri': '/rest/storage-volumes/090E8A94-C507-4B4D-B83A-550D506E7622', 'isBootVolume': 'false', 'lunType': 'Manual', 'lun': 0, 'storagePaths': [{'isEnabled': 'true', 'connectionId': 3, 'storageTargetType': 'Auto', 'storageTargets': []}]}]},
     'connections': [
         {'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Auto',
          'requestedMbps': int(2500), 'networkUri': 'ETH:ETH_NW2',
          'mac': None, 'wwpn': '', 'wwnn': ''},
         {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Auto',
          'requestedMbps': int(2500), 'networkUri': 'ETH:ETH_NW2',
          'mac': None, 'wwpn': '', 'wwnn': ''},
         {'id': 3, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Auto',
          'requestedMbps': int(2500), 'networkUri': 'FCOE:FCOE_NW200',
          'boot': {'priority': 'Primary', 'bootVolumeSource': 'UserDefined', 'targets': [{'arrayWwpn': '21210002AC009290', 'lun': '1'}]},
          'mac': None, 'wwpn': '', 'wwnn': ''},
         {'id': 4, 'name': '4', 'functionType': 'FibreChannel', 'portId': 'Auto',
          'requestedMbps': int(2500), 'networkUri': 'FCOE:FCOE_NW100',
          'boot': {'priority': 'Secondary', 'bootVolumeSource': 'UserDefined', 'targets': [{'arrayWwpn': '21210002AC009290', 'lun': '1'}]},
          'mac': None, 'wwpn': '', 'wwnn': ''},

     ]},

]
New_server_profiles_2ETH_2FCOE_BFS_No_SAN = [
    {'type': 'ServerProfileV6', 'serverHardwareUri': ENC1 + ', bay 7',
     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_B1',
     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
     'name': '2ETH_2FCOE_BFS', 'description': '', 'affinity': 'Bay',
     'boot': {'manageBoot': 'true', 'order': ['HardDisk']},
     'bootMode':{'manageMode': 'true', 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
     'connections': [
         {'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Auto',
          'requestedMbps': int(2500), 'networkUri': 'ETH:ETH_NW2',
          'mac': None, 'wwpn': '', 'wwnn': ''},
         {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Auto',
          'requestedMbps': int(2500), 'networkUri': 'ETH:ETH_NW2',
          'mac': None, 'wwpn': '', 'wwnn': ''},
         {'id': 3, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Auto',
          'requestedMbps': int(2500), 'networkUri': 'FCOE:FCOE_NW200',
          'boot': {'priority': 'Primary', 'bootVolumeSource': 'UserDefined', 'targets': [{'arrayWwpn': '21210002AC009290', 'lun': '0'}]},
          'mac': None, 'wwpn': '', 'wwnn': ''},
         {'id': 4, 'name': '4', 'functionType': 'FibreChannel', 'portId': 'Auto',
          'requestedMbps': int(2500), 'networkUri': 'FCOE:FCOE_NW100',
          'boot': {'priority': 'Secondary', 'bootVolumeSource': 'UserDefined', 'targets': [{'arrayWwpn': '21210002AC009290', 'lun': '0'}]},
          'mac': None, 'wwpn': '', 'wwnn': ''},

     ]},

]

New_server_profiles_2ETH_2FCOE_BFS_SANBB_PB99 = [
    {'type': 'ServerProfileV6', 'serverHardwareUri': ENC1 + ', bay 16',
     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_B1',
     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
     'name': '2ETH_2FCOE_BFS', 'description': '', 'affinity': 'Bay',
     'boot': {'manageBoot': 'true', 'order': ['HardDisk']},
     'bootMode':{'manageMode': 'true', 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
     'sanStorage': {'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': 'true', 'volumeAttachments': [{'id': 1, 'volumeUri': '/rest/storage-volumes/9947A0D1-24E2-425A-913D-14829FEB5D80', 'isBootVolume': 'false', 'lunType': 'Manual', 'lun': 1, 'storagePaths': [{'isEnabled': 'true', 'connectionId': 3, 'storageTargetType': 'Auto', 'storageTargets': []}]}]},
     'connections': [
         {'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Auto',
          'requestedMbps': int(2500), 'networkUri': 'ETH:ETH_NW2',
          'mac': None, 'wwpn': '', 'wwnn': ''},
         {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Auto',
          'requestedMbps': int(2500), 'networkUri': 'ETH:ETH_NW2',
          'mac': None, 'wwpn': '', 'wwnn': ''},
         {'id': 3, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Auto',
          'requestedMbps': int(2500), 'networkUri': 'FCOE:FCOE_NW200',
          'boot': {'priority': 'Primary', 'bootVolumeSource': 'UserDefined', 'targets': [{'arrayWwpn': '21210002AC009290', 'lun': '1'}]},
          'mac': None, 'wwpn': '', 'wwnn': ''},
         {'id': 4, 'name': '4', 'functionType': 'FibreChannel', 'portId': 'Auto',
          'requestedMbps': int(2500), 'networkUri': 'FCOE:FCOE_NW100',
          'boot': {'priority': 'Secondary', 'bootVolumeSource': 'UserDefined', 'targets': [{'arrayWwpn': '21210002AC009290', 'lun': '1'}]},
          'mac': None, 'wwpn': '', 'wwnn': ''},

     ]},

]
server_profiles_2FC_2ETH_BFS_Automation_SP = [
    {'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 12',
     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_B1',
     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
     'name': 'server_profile_bay2', 'description': '', 'affinity': 'Bay',
     'boot': {'manageBoot': 'true', 'order': ['HardDisk']},
     'bootMode':{'manageMode': 'true', 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
     'connections': [
         {'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Auto',
          'requestedMbps': int(2500), 'networkUri': 'ETH:ETH_NW1',
          'mac': None, 'wwpn': '', 'wwnn': ''},
         {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Auto',
          'requestedMbps': int(2500), 'networkUri': 'ETH:ETH_NW2',
          'mac': None, 'wwpn': '', 'wwnn': ''},
         {'id': 3, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Auto',
          'requestedMbps': 'Auto', 'networkUri': 'FC:FC_NW1',
          'boot': {'priority': 'Primary', 'bootVolumeSource': 'UserDefined', 'targets': [{'arrayWwpn': '20110002AC009290', 'lun': '0'}]},
          'mac': None, 'wwpn': '', 'wwnn': ''},
         {'id': 4, 'name': '4', 'functionType': 'FibreChannel', 'portId': 'Auto',
          'requestedMbps': 'Auto', 'networkUri': 'FC:FC_NW2',
          'boot': {'priority': 'Secondary', 'bootVolumeSource': 'UserDefined', 'targets': [{'arrayWwpn': '20110002AC009290', 'lun': '0'}]},
          'mac': None, 'wwpn': '', 'wwnn': ''},
     ]},

]

ExpectedErrorLiMsg1 = 'Unable to update firmware on the logical interconnect. Downgrading firmware without selecting the Force Installation option is not supported.'
ExpectedErrorLiMsg3 = """Retry update firmware operation with 'Force Installation' option selected."""
HH_VV = '?view=flat-tree&start=0&count=100&_'
TAKS_VAR = '/rest/tasks/'
E_value = 'No update required. Selected firmware is already installed in the logical interconnect'

LI_UPGRADE_UPDATE_PARALLELDEMO_RPM = {"command": "UPDATE", "ethernetActivationDelay": "5", "ethernetActivationType": "Parallel", "fcActivationDelay": "5", "fcActivationType": "Parallel", "force": "false", "sppUri": "/rest/firmware-drivers/{}".format(spp)}

LI_DOWNGRADE_UPDATE_PARALLELDEMO_NEGATIVE_RPM = {"command": "UPDATE", "ethernetActivationDelay": "5", "ethernetActivationType": "Parallel", "fcActivationDelay": "5", "fcActivationType": "Parallel", "force": "false", "sppUri": "/rest/firmware-drivers/CUST-SPP-RPMONLY-DOWNGRADE-191"}

"""
uplink_sets = {'IC-a': {'name': 'IC',
                        'ethernetNetworkType': 'Untagged',
                        'networkType': 'Ethernet',
                        'networkUris': ['IC'],
                        'nativeNetworkUri': None,
                        'mode': 'Auto',
                        'logicalPortConfigInfos': [{'bay': '3', 'port': 'X6', 'speed': 'Auto'}]},
               'IC-b': {'name': 'IC',
                        'ethernetNetworkType': 'Untagged',
                        'networkType': 'Ethernet',
                        'networkUris': ['IC'],
                        'nativeNetworkUri': None,
                        'mode': 'Auto',
                        'logicalPortConfigInfos': [{'bay': '2', 'port': 'X6', 'speed': 'Auto'}]},
               'FAB-A-FA': {'name': 'FAB-A-FA',
                            'ethernetNetworkType': 'NotApplicable',
                            'networkType': 'FibreChannel',
                            'networkUris': ['SAN-3-A-FA-3-1'],
                            'nativeNetworkUri': None,
                            'mode': 'Auto',
                            'logicalPortConfigInfos': [{'bay': '3', 'port': 'X1', 'speed': 'Auto'}]},
               'FAB-B-FA': {'name': 'FAB-B-FA',
                            'ethernetNetworkType': 'NotApplicable',
                            'networkType': 'FibreChannel',
                            'networkUris': ['SAN-4-B-FA-4-1'],
                            'nativeNetworkUri': None,
                            'mode': 'Auto',
                            'logicalPortConfigInfos': [{'bay': '4', 'port': 'X1', 'speed': 'Auto'}]},
           'FAB-A2-FA': {'name': 'FAB-A2-FA',
                            'ethernetNetworkType': 'NotApplicable',
                            'networkType': 'FibreChannel',
                            'networkUris': ['SAN-3-A-FA-3-1-2-3-4'],
                            'nativeNetworkUri': None,
                            'mode': 'Auto',
                            'logicalPortConfigInfos': [{'bay': '3', 'port': '1', 'speed': 'Auto'},
                                                       {'bay': '3', 'port': '2', 'speed': 'Auto'},
                                                       {'bay': '3', 'port': '3', 'speed': 'Auto'},
                                                       {'bay': '3', 'port': '4', 'speed': 'Auto'}]},
               'FAB-B2-FA': {'name': 'FAB-B2-FA',
                            'ethernetNetworkType': 'NotApplicable',
                            'networkType': 'FibreChannel',
                            'networkUris': ['SAN-4-B-FA-4-1-2-3-4'],
                            'nativeNetworkUri': None,
                            'mode': 'Auto',
                            'logicalPortConfigInfos': [{'bay': '4', 'port': '1', 'speed': 'Auto'},
                                                       {'bay': '4', 'port': '2', 'speed': 'Auto'},
                                                       {'bay': '4', 'port': '3', 'speed': 'Auto'},
                                                       {'bay': '4', 'port': '4', 'speed': 'Auto'}]},
               'FAB-C-FA': {'name': 'FAB-C-FA',
                         'ethernetNetworkType': 'NotApplicable',
                         'networkType': 'FibreChannel',
                         'networkUris': ['SAN-FA-5-5'],
                         'nativeNetworkUri': None,
                         'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '5', 'port': 'X5', 'speed': 'Auto'}]},
               'FAB-D-FA': {'name': 'FAB-D-FA',
                         'ethernetNetworkType': 'NotApplicable',
                         'networkType': 'FibreChannel',
                         'networkUris': ['SAN-FA-6-5'],
                         'nativeNetworkUri': None,
                         'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '6', 'port': 'X5', 'speed': 'Auto'}]},
               'Tunnel1': {'name': 'Tunnel1',
                           'ethernetNetworkType': 'Tunnel',
                           'networkType': 'Ethernet',
                           'networkUris': ['Tunnel1'],
                           'nativeNetworkUri': None,
                           'mode': 'Auto',
                           'logicalPortConfigInfos': [{'bay': '1', 'port': 'X7', 'speed': 'Auto'}]},
               'Tunnel2': {'name': 'Tunnel2',
                           'ethernetNetworkType': 'Tunnel',
                           'networkType': 'Ethernet',
                           'networkUris': ['Tunnel2'],
                           'nativeNetworkUri': None,
                           'mode': 'Auto',
                           'logicalPortConfigInfos': [{'bay': '2', 'port': 'X7', 'speed': 'Auto'}]},
               'BigPipe1-a': {'name': 'BigPipe1',
                              'ethernetNetworkType': 'Tagged',
                              'networkType': 'Ethernet',
                              'networkUris': make_range_list({'start': 2, 'end': 317, 'prefix': 'net_', 'suffix': '-O'}) + make_range_list({'start': 700, 'end': 710, 'prefix': 'net_', 'suffix': '-O'}) + make_range_list({'start': 3990, 'end': 4000, 'prefix': 'net_', 'suffix': '-O'}) + make_range_list({'start': 637, 'end': 668, 'prefix': 'FCOE-A-', 'suffix': '-O'}),
                              'nativeNetworkUri': None,
                              'mode': 'Auto',
                              'logicalPortConfigInfos': [{'bay': '1', 'port': 'X1', 'speed': 'Auto'},
                                                         {'bay': '1', 'port': 'X2', 'speed': 'Auto'}]},
               'BigPipe2-a': {'name': 'BigPipe2',
                              'ethernetNetworkType': 'Tagged',
                              'networkType': 'Ethernet',
                  'networkUris': make_range_list({'start': 2, 'end': 317, 'prefix': 'net_', 'suffix': '-E'}) + make_range_list({'start': 700, 'end': 710, 'prefix': 'net_', 'suffix': '-E'}) + make_range_list({'start': 3990, 'end': 4000, 'prefix': 'net_', 'suffix': '-E'}) + make_range_list({'start': 637, 'end': 668, 'prefix': 'FCOE-B-', 'suffix': '-E'}),
                              'nativeNetworkUri': None,
                              'mode': 'Auto',
                              'logicalPortConfigInfos':  [{'bay': '2', 'port': 'X1', 'speed': 'Auto'},
                                                          {'bay': '2', 'port': 'X2', 'speed': 'Auto'}]},
               'BigPipe1-b': {'name': 'BigPipe1',
                              'ethernetNetworkType': 'Tagged',
                              'networkType': 'Ethernet',
                              'networkUris': make_range_list({'start': 2, 'end': 317, 'prefix': 'net_', 'suffix': '-O'}) + make_range_list({'start': 700, 'end': 710, 'prefix': 'net_', 'suffix': '-O'}) + make_range_list({'start': 3990, 'end': 4000, 'prefix': 'net_', 'suffix': '-O'}) + make_range_list({'start': 637, 'end': 668, 'prefix': 'FCOE-A-', 'suffix': '-O'}),
                              'nativeNetworkUri': None,
                              'mode': 'Auto',
                              'logicalPortConfigInfos': [{'bay': '1', 'port': 'X5', 'speed': 'Auto'},
                                                         {'bay': '1', 'port': 'X6', 'speed': 'Auto'}]},
               'BigPipe2-b': {'name': 'BigPipe2',
                              'ethernetNetworkType': 'Tagged',
                              'networkType': 'Ethernet',
                  'networkUris': make_range_list({'start': 2, 'end': 317, 'prefix': 'net_', 'suffix': '-E'}) + make_range_list({'start': 700, 'end': 710, 'prefix': 'net_', 'suffix': '-E'}) + make_range_list({'start': 3990, 'end': 4000, 'prefix': 'net_', 'suffix': '-E'}) + make_range_list({'start': 637, 'end': 668, 'prefix': 'FCOE-B-', 'suffix': '-E'}),
                              'nativeNetworkUri': None,
                              'mode': 'Auto',
                              'logicalPortConfigInfos': [{'bay': '2', 'port': 'X5', 'speed': 'Auto'},
                                                         {'bay': '2', 'port': 'X6', 'speed': 'Auto'}]},
               'BigPipe1-c': {'name': 'BigPipe1',
                              'ethernetNetworkType': 'Tagged',
                              'networkType': 'Ethernet',
                              'networkUris': make_range_list({'start': 2, 'end': 317, 'prefix': 'net_', 'suffix': '-O'}) + make_range_list({'start': 700, 'end': 710, 'prefix': 'net_', 'suffix': '-O'}) + make_range_list({'start': 3990, 'end': 4000, 'prefix': 'net_', 'suffix': '-O'}) + make_range_list({'start': 637, 'end': 668, 'prefix': 'FCOE-A-', 'suffix': '-O'}),
                              'nativeNetworkUri': None,
                              'mode': 'Auto',
                              'logicalPortConfigInfos': [{'bay': '1', 'port': 'X2', 'speed': 'Auto'},
                                                         {'bay': '1', 'port': 'X3', 'speed': 'Auto'}]},
               'BigPipe2-c': {'name': 'BigPipe2',
                              'ethernetNetworkType': 'Tagged',
                              'networkType': 'Ethernet',
                  'networkUris': make_range_list({'start': 2, 'end': 317, 'prefix': 'net_', 'suffix': '-E'}) + make_range_list({'start': 700, 'end': 710, 'prefix': 'net_', 'suffix': '-E'}) + make_range_list({'start': 3990, 'end': 4000, 'prefix': 'net_', 'suffix': '-E'}) + make_range_list({'start': 637, 'end': 668, 'prefix': 'FCOE-B-', 'suffix': '-E'}),
                              'nativeNetworkUri': None,
                              'mode': 'Auto',
                              'logicalPortConfigInfos': [{'bay': '2', 'port': 'X2', 'speed': 'Auto'},
                                                         {'bay': '2', 'port': 'X3', 'speed': 'Auto'}]},
                }

ligs = [{'name': '12-FF-FF-LIG',
         'type': 'logical-interconnect-groupV300',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                     ],
         'uplinkSets': [uplink_sets['IC-a'],
                        uplink_sets['FAB-A-FA'],
                        uplink_sets['FAB-B-FA'],
                        uplink_sets['Tunnel1'],
                        uplink_sets['Tunnel2'],
                        uplink_sets['BigPipe1-a'],
                        uplink_sets['BigPipe2-a']],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None},
        {'name': '13-FFF8-FFF8-LIG',
         'type': 'logical-interconnect-groupV300',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': [{'bay': 1, 'type': 'HP VC FlexFabric-20/40 F8 Module','enclosure': 1, 'enclosureIndex': 1},
                                     {'bay': 2, 'type': 'HP VC FlexFabric-20/40 F8 Module','enclosure': 1, 'enclosureIndex': 1},
                                     {'bay': 3, 'type': 'HP VC FlexFabric-20/40 F8 Module','enclosure': 1, 'enclosureIndex': 1},
                                     {'bay': 4, 'type': 'HP VC FlexFabric-20/40 F8 Module','enclosure': 1, 'enclosureIndex': 1},
                                     ],
         'uplinkSets': [uplink_sets['IC-a'],
                        uplink_sets['FAB-A-FA'],
                        uplink_sets['FAB-B-FA'],
                        uplink_sets['Tunnel1'],
                        uplink_sets['Tunnel2'],
                        uplink_sets['BigPipe1-b'],
                        uplink_sets['BigPipe2-b']],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None},
        {'name': '14-F10D-8FC20-8FC24-LIG',
         'type': 'logical-interconnect-groupV300',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC Flex-10/10D Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC Flex-10/10D Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC 8Gb 20-Port FC Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC 8Gb 20-Port FC Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC 8Gb 24-Port FC Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC 8Gb 24-Port FC Module'},
                     ],
         'uplinkSets': [uplink_sets['IC-b'],
                uplink_sets['FAB-A2-FA'],
                        uplink_sets['FAB-B2-FA'],
                        uplink_sets['FAB-C-FA'],
                        uplink_sets['FAB-D-FA'],
                        uplink_sets['Tunnel1'],
                        uplink_sets['Tunnel2'],
                        uplink_sets['BigPipe1-c'],
                        uplink_sets['BigPipe2-c']],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None},
        ]

"""

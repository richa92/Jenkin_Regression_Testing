#!/usr/bin/env python

#############################################################################
# potash_1gbsupport.py
# Script for 1GBSUPPORT and Auto-Split Features
# Functionality Testing in Potash
#############################################################################
import string
import functions_potash
import UserInput
import sys
import time
global spaces
spaces = "\n______________________________________________________________________________\n"


#############################################################################
# autosplit_status_with_le_test
#############################################################################

def autosplit_status_with_le_test(session, output_file, total_cmds_executed, total_cmds_passed, total_cmds_failed):
    cmd_output = functions_potash.execute_cmd(session, "set cli pagination off")
    output_file.write(cmd_output)
    print cmd_output

    cmd_output = functions_potash.execute_cmd(session, "show auto-split-status")
    output_file.write(cmd_output)

    if ("Enabled" not in cmd_output):
        total_cmds_passed = total_cmds_passed + 1
        result = "\n" + " show auto-split-status with LE TEST" + "=Passed\n" + "\nPASSED\n"
    else:
        total_cmds_failed = total_cmds_failed + 1
        result = "\n" + " show auto-split-status with LE TEST" + "=Failed=" + "Failed in Output Validation\n" + "\nFAILED\n"
    output_file.write(result)

    return(total_cmds_passed, total_cmds_failed)


#############################################################################
# show_transceiver_info_interface_status_test
# Execute show transceiver info and show interface status CLI commands
# and verify 1GB transceiver functionality
#############################################################################

def show_transceiver_info_show_interface_status_test(session, output_file, total_cmds_executed, total_cmds_passed, total_cmds_failed):

    cmd1 = "show transceiver-info ten-gigabitEthernet " + UserInput.ONEGBSUPPORT_UPLINK1
    show_trans_info_uplink1_output = functions_potash.execute_cmd(session, cmd1)
    output_file.write(show_trans_info_uplink1_output)

    cmd2 = "show transceiver-info ten-gigabitEthernet " + UserInput.ONEGBSUPPORT_UPLINK2
    show_trans_info_uplink2_output = functions_potash.execute_cmd(session, cmd2)
    output_file.write(show_trans_info_uplink2_output)

    cmd3 = "show int status"
    cmd_output3 = functions_potash.execute_cmd(session, cmd3)
    output_file.write(cmd_output3)
    split_word_uplink1 = "Ten-GigabitEthernet" + UserInput.ONEGBSUPPORT_UPLINK1
    show_interface_status_uplink1 = cmd_output3.split(split_word_uplink1)[1].split('Auto-MDIX on')[0]

    split_word_uplink2 = "Ten-GigabitEthernet" + UserInput.ONEGBSUPPORT_UPLINK2
    show_interface_status_uplink2 = cmd_output3.split(split_word_uplink2)[1].split('Auto-MDIX on')[0]

    if (("1Gb" in show_trans_info_uplink1_output) and
            ("1Gb" in show_trans_info_uplink2_output) and
            ("connected        Full     1 Gbps      Auto" in show_interface_status_uplink1) and
            ("connected        Full     1 Gbps      Auto" in show_interface_status_uplink2)):
        total_cmds_passed = total_cmds_passed + 1
        result = "\n" + " show_transceiver_info_show_interface_status_test" + "=Passed\n" + "\nPASSED\n"
    else:
        total_cmds_failed = total_cmds_failed + 1
        result = "\n" + " show_transceiver_info_show_interface_status_test" + "=Failed=" + "Failed in Output Validation\n" + "\nFAILED\n"
    output_file.write(result)

    return(total_cmds_passed, total_cmds_failed)


#############################################################################
# Test 1GB transceiver functionality with no negotiation
#############################################################################

def no_negotiation_test(session, output_file, total_cmds_executed, total_cmds_passed, total_cmds_failed):

    cmd_output = functions_potash.execute_cmd(session, "configure terminal")
    output_file.write(cmd_output)
    print cmd_output

    cmd = "no breakout interface ten-GigabitEthernet " + UserInput.ONEGBSUPPORT_UPLINK2
    cmd_output = functions_potash.execute_cmd(session, cmd)
    output_file.write(cmd_output)
    print cmd_output

    cmd = "interface fortyGigE " + UserInput.ONEGBSUPPORT_UPLINK2.split(':')[0]
    cmd_output = functions_potash.execute_cmd(session, cmd)
    output_file.write(cmd_output)
    print cmd_output

    cmd = "no negotiation"
    cmd_output = functions_potash.execute_cmd(session, cmd)
    output_file.write(cmd_output)
    print cmd_output

    cmd_output = functions_potash.execute_cmd(session, "end")
    output_file.write(cmd_output)
    print cmd_output

    cmd3 = "show int status"
    cmd_output3 = functions_potash.execute_cmd(session, cmd3)
    output_file.write(cmd_output3)
    split_word_uplink2 = "FortyGigE" + UserInput.ONEGBSUPPORT_UPLINK2.split(':')[0]
    show_interface_status_40Guplink2 = cmd_output3.split(split_word_uplink2)[1].split('Auto-MDIX on')[0]

    cmd_output = functions_potash.execute_cmd(session, "configure terminal")
    output_file.write(cmd_output)
    print cmd_output

    cmd = "breakout interface fortyGigE " + UserInput.ONEGBSUPPORT_UPLINK2.split(':')[0]
    cmd_output = functions_potash.execute_cmd(session, cmd)
    output_file.write(cmd_output)
    print cmd_output

    cmd_output = functions_potash.execute_cmd(session, "end")
    output_file.write(cmd_output)
    print cmd_output

    cmd3 = "show int status"
    cmd_output3 = functions_potash.execute_cmd(session, cmd3)
    output_file.write(cmd_output3)
    split_word_uplink2 = "Ten-GigabitEthernet" + UserInput.ONEGBSUPPORT_UPLINK2
    show_interface_status_10Guplink2 = cmd_output3.split(split_word_uplink2)[1].split('Auto-MDIX on')[0]

    if (("not connected    Full     -           No-Negotiation" in show_interface_status_40Guplink2) and
            ("connected        Full     1 Gbps      Auto" in show_interface_status_10Guplink2)):
        total_cmds_passed = total_cmds_passed + 1
        result = "\n" + " show_transceiver_info_test" + "=Passed\n" + "\nPASSED\n"
    else:
        total_cmds_failed = total_cmds_failed + 1
        result = "\n" + " show_transceiver_info_test" + "=Failed=" + "Failed in Output Validation\n" + "\nFAILED\n"
    output_file.write(result)

    return(total_cmds_passed, total_cmds_failed)


#############################################################################
# Test 1GB transceiver functionality with Negotiation
#############################################################################

def negotiation_test(session, output_file, total_cmds_executed, total_cmds_passed, total_cmds_failed):

    cmd_output = functions_potash.execute_cmd(session, "configure terminal")
    output_file.write(cmd_output)
    print cmd_output

    cmd = "interface ten-GigabitEthernet " + UserInput.ONEGBSUPPORT_UPLINK2
    cmd_output = functions_potash.execute_cmd(session, cmd)
    output_file.write(cmd_output)
    print cmd_output

    cmd = "no negotiation"
    cmd_output = functions_potash.execute_cmd(session, cmd)
    output_file.write(cmd_output)
    print cmd_output

    cmd = "end"
    cmd_output = functions_potash.execute_cmd(session, cmd)
    output_file.write(cmd_output)
    print cmd_output

    time.sleep(5)

    cmd = "show interface status"
    cmd_output = functions_potash.execute_cmd(session, cmd)
    output_file.write(cmd_output)
    print cmd_output
    split_word_uplink2 = "Ten-GigabitEthernet" + UserInput.ONEGBSUPPORT_UPLINK2
    show_interface_status_uplink2_nonegotiation = cmd_output.split(split_word_uplink2)[1].split('Auto-MDIX on')[0]

    cmd_output = functions_potash.execute_cmd(session, "configure terminal")
    output_file.write(cmd_output)
    print cmd_output

    cmd = "interface ten-GigabitEthernet " + UserInput.ONEGBSUPPORT_UPLINK2
    cmd_output = functions_potash.execute_cmd(session, cmd)

    cmd_output = functions_potash.execute_cmd(session, "configure terminal")
    output_file.write(cmd_output)
    print cmd_output

    cmd = "interface ten-GigabitEthernet " + UserInput.ONEGBSUPPORT_UPLINK2
    cmd_output = functions_potash.execute_cmd(session, cmd)
    output_file.write(cmd_output)
    print cmd_output

    cmd = "negotiation"
    cmd_output = functions_potash.execute_cmd(session, cmd)
    output_file.write(cmd_output)
    print cmd_output

    cmd = "end"
    cmd_output = functions_potash.execute_cmd(session, cmd)
    output_file.write(cmd_output)
    print cmd_output

    time.sleep(5)

    cmd = "show interface status"
    cmd_output = functions_potash.execute_cmd(session, cmd)
    output_file.write(cmd_output)
    print cmd_output
    split_word_uplink2 = "Ten-GigabitEthernet" + UserInput.ONEGBSUPPORT_UPLINK2
    show_interface_status_uplink2_negotiation = cmd_output.split(split_word_uplink2)[1].split('Auto-MDIX on')[0]

    cmd_output = functions_potash.execute_cmd(session, "configure terminal")
    output_file.write(cmd_output)
    print cmd_output

    cmd = "interface ten-GigabitEthernet " + UserInput.ONEGBSUPPORT_UPLINK2
    cmd_output = functions_potash.execute_cmd(session, cmd)
    output_file.write(cmd_output)
    print cmd_output

    cmd = "no negotiation"
    cmd_output = functions_potash.execute_cmd(session, cmd)
    output_file.write(cmd_output)
    print cmd_output

    cmd = "speed auto"
    cmd_output = functions_potash.execute_cmd(session, cmd)
    output_file.write(cmd_output)
    print cmd_output

    cmd = "end"
    cmd_output = functions_potash.execute_cmd(session, cmd)
    output_file.write(cmd_output)
    print cmd_output

    time.sleep(5)

    cmd = "show interface status"
    cmd_output = functions_potash.execute_cmd(session, cmd)
    output_file.write(cmd_output)
    print cmd_output
    split_word_uplink2 = "Ten-GigabitEthernet" + UserInput.ONEGBSUPPORT_UPLINK2
    show_interface_status_uplink2_noneg_speedauto = cmd_output.split(split_word_uplink2)[1].split('Auto-MDIX on')[0]

    if (("not connected    Full     -           No-Negotiation" in show_interface_status_uplink2_nonegotiation) and
            ("connected        Full     1 Gbps      Auto" in show_interface_status_uplink2_negotiation) and
            ("connected        Full     1 Gbps      Auto" in show_interface_status_uplink2_noneg_speedauto)):
        total_cmds_passed = total_cmds_passed + 1
        result = "\n" + " show_transceiver_info_test" + "=Passed\n" + "\nPASSED\n"
    else:
        total_cmds_failed = total_cmds_failed + 1
        result = "\n" + " show_transceiver_info_test" + "=Failed=" + "Failed in Output Validation\n" + "\nFAILED\n"
    output_file.write(result)

    return(total_cmds_passed, total_cmds_failed)


#############################################################################
# execute_tests
# - Main routine from where all the tests gets executed
#############################################################################
def execute_tests():
    ExecutionOutput = "../AUTOMATION_RESULTS/" + "ExecutionOutput_1GBSUPPORT.txt"
    output_file = open(ExecutionOutput, "w")
    session = functions_potash.ssh_connect(UserInput.POTASHIP, UserInput.USERNAME, UserInput.PASSWORD)

    total_cmds_executed = 0
    total_cmds_passed = 0
    total_cmds_failed = 0

    output_file.write(spaces + "1GBSUPPORT FUNCTIONAL TESTS" + spaces)

    cmd_output = functions_potash.execute_cmd(session, "show firmware version")
    output_file.write(cmd_output)

    output_file.write(spaces + "\n")
    total_cmds_passed, total_cmds_failed = autosplit_status_with_le_test(session, output_file, total_cmds_executed, total_cmds_passed, total_cmds_failed)
    output_file.write(spaces + "\n")

    total_cmds_passed, total_cmds_failed = show_transceiver_info_show_interface_status_test(session, output_file, total_cmds_executed, total_cmds_passed, total_cmds_failed)
    output_file.write(spaces + "\n")

    total_cmds_passed, total_cmds_failed = no_negotiation_test(session, output_file, total_cmds_executed, total_cmds_passed, total_cmds_failed)
    output_file.write(spaces + "\n")

    total_cmds_passed, total_cmds_failed = negotiation_test(session, output_file, total_cmds_executed, total_cmds_passed, total_cmds_failed)
    output_file.write(spaces + "\n")

    functions_potash.final_output(output_file, ExecutionOutput, total_cmds_executed, total_cmds_passed, total_cmds_failed)

script_name = sys.argv[0]
if ("potash_1gbsupport" in script_name):
    execute_tests()

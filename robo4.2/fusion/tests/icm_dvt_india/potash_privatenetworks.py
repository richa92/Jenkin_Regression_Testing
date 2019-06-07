#!/usr/bin/env python

#############################################################################
# potash_privatenetworks.py
# Script for PRIVATENETWORKS Feature Functionality Testing in Potash
#############################################################################
import string
import functions_potash
import UserInput
import sys


#############################################################################
# privatenetworks_vlan_test
# Enable or Disable Private Networks in specified VLAN and verify
# action - should be 'Enable' or 'Disable' in below.
#############################################################################
def privatenetworks_vlan_test(session, output_file, total_cmds_executed, total_cmds_passed, total_cmds_failed, action):
    cmd_output = functions_potash.execute_cmd(session, "configure terminal")
    output_file.write(cmd_output)
    print cmd_output

    cmd_output = functions_potash.execute_cmd(session, "private-network feature enable")
    output_file.write(cmd_output)
    print cmd_output

    cmd = "vlan " + UserInput.PRIVATENETWORKS_VLAN
    cmd_output = functions_potash.execute_cmd(session, cmd)
    output_file.write(cmd_output)
    print cmd_output

    cmd = "private-network " + action
    cmd_output = functions_potash.execute_cmd(session, cmd)
    output_file.write(cmd_output)
    print cmd_output

    cmd_output = functions_potash.execute_cmd(session, "end")
    output_file.write(cmd_output)
    print cmd_output

    cmd = "show vlan id " + UserInput.PRIVATENETWORKS_VLAN
    cmd_output = functions_potash.execute_cmd(session, cmd)
    output_file.write(cmd_output)
    search_word = "Private Network Status   : " + action

    if (search_word in cmd_output):
        total_cmds_passed = total_cmds_passed + 1
        result = "\n" + action + " Private Networks in VLAN and verify" + "=Passed\n" + "\nPASSED\n"
    else:
        total_cmds_failed = total_cmds_failed + 1
        result = "\n" + action + " Private Networks in VLAN and verify" + "=Failed=" + "Failed in Output Validation\n" + "\nFAILED\n"
    output_file.write(result)
    return(total_cmds_passed, total_cmds_failed)

#############################################################################
# newly_created_vlan_privatenetworks_test
# Verify Private Network feature is disabled for newly created VLAN
#############################################################################


def newly_created_vlan_privatenetworks_test(session, output_file, total_cmds_executed, total_cmds_passed, total_cmds_failed):
    cmd_output = functions_potash.execute_cmd(session, "configure terminal")
    output_file.write(cmd_output)
    print cmd_output

    cmd = "no vlan " + UserInput.PRIVATENETWORKS_NEWVLAN
    cmd_output = functions_potash.execute_cmd(session, cmd)
    output_file.write(cmd_output)

    cmd = "vlan " + UserInput.PRIVATENETWORKS_NEWVLAN
    cmd_output = functions_potash.execute_cmd(session, cmd)
    output_file.write(cmd_output)

    cmd_output = functions_potash.execute_cmd(session, "vlan active")
    output_file.write(cmd_output)

    cmd_output = functions_potash.execute_cmd(session, "end")
    output_file.write(cmd_output)

    cmd = "show vlan id " + UserInput.PRIVATENETWORKS_NEWVLAN
    cmd_output = functions_potash.execute_cmd(session, cmd)
    output_file.write(cmd_output)

    search_word = "Private Network Status   : Disabled"
    if (search_word in cmd_output):
        total_cmds_passed = total_cmds_passed + 1
        result = "\n" + "Private Networks feature should be disabled for newly created VLAN" + "=Passed\n" + "\nPASSED\n"
    else:
        total_cmds_failed = total_cmds_failed + 1
        result = "\n" + "Private Networks feature should be disabled for newly created VLAN" + "=Failed=" + "Failed in Output Validation\n" + "\nFAILED\n"
    output_file.write(result)
    return(total_cmds_passed, total_cmds_failed)

#############################################################################
# reset_privatenetworks_feature
# When Private Network Feature is completely disabled for the ICM,
# Verify Private Network feature should be disabled in all VLANS
#############################################################################


def reset_privatenetworks_feature(session, output_file, total_cmds_executed, total_cmds_passed, total_cmds_failed):
    cmd_output = functions_potash.execute_cmd(session, "configure terminal")
    output_file.write(cmd_output)

    cmd_output = functions_potash.execute_cmd(session, "private-network feature disable")
    output_file.write(cmd_output)

    cmd_output = functions_potash.execute_cmd(session, "end")
    output_file.write(cmd_output)

    cmd = "show vlan id " + UserInput.PRIVATENETWORKS_VLAN
    cmd_output = functions_potash.execute_cmd(session, cmd)
    output_file.write(cmd_output)

    search_word = "Private Network Status   : Disabled"
    if (search_word in cmd_output):
        total_cmds_passed = total_cmds_passed + 1
        result = "\n" + "Disable Private Network Feature completely" + "=Passed\n" + "\nPASSED\n"
    else:
        total_cmds_failed = total_cmds_failed + 1
        result = "\n" + "Disable Private Network Feature completely" + "=Failed=" + "Failed in Output Validation\n" + "\nFAILED\n"
    output_file.write(result)
    return(total_cmds_passed, total_cmds_failed)

#############################################################################
# execute_tests
# - main routine from where all tests gets invoked.
#############################################################################


def execute_tests():

    total_cmds_executed = 0
    total_cmds_passed = 0
    total_cmds_failed = 0
    line_decoration = "\n______________________________________________________________________________\n"

    ExecutionOutput = "../AUTOMATION_RESULTS/" + "ExecutionOutput_PRIVATENETWORKS.txt"
    output_file = open(ExecutionOutput, "w")
    session = functions_potash.ssh_connect(UserInput.POTASHIP, UserInput.USERNAME, UserInput.PASSWORD)

    output_file.write(line_decoration + "PRIVATENETWORKS FUNCTIONAL TESTS" + line_decoration)

    cmd_output = functions_potash.execute_cmd(session, "show firmware version")
    output_file.write(cmd_output)

    output_file.write(line_decoration + "\n")
    total_cmds_passed, total_cmds_failed = privatenetworks_vlan_test(session, output_file, total_cmds_executed, total_cmds_passed, total_cmds_failed, 'Enable')
    output_file.write(line_decoration + "\n")

    total_cmds_passed, total_cmds_failed = privatenetworks_vlan_test(session, output_file, total_cmds_executed, total_cmds_passed, total_cmds_failed, 'Disable')
    output_file.write(line_decoration + "\n")

    total_cmds_passed, total_cmds_failed = newly_created_vlan_privatenetworks_test(session, output_file, total_cmds_executed, total_cmds_passed, total_cmds_failed)
    output_file.write(line_decoration + "\n")

    total_cmds_passed, total_cmds_failed = reset_privatenetworks_feature(session, output_file, total_cmds_executed, total_cmds_passed, total_cmds_failed)
    output_file.write(line_decoration + "\n")

    functions_potash.final_output(output_file, ExecutionOutput, total_cmds_executed, total_cmds_passed, total_cmds_failed)

script_name = sys.argv[0]
if ("potash_privatenetworks" in script_name):
    execute_tests()

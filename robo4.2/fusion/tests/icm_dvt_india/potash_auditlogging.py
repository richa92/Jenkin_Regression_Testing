#!/usr/bin/env python


#############################################################################
# potash_auditlogging.py
# Script for AUDITLOGGING Feature Functionality Testing in Potash
#############################################################################
import string
import functions_potash
import UserInput
import sys

global spaces
spaces = "\n______________________________________________________________________________\n"


#############################################################################
# auditlogging_reset_test
# Execute 'audit-logging reset' cmd from Potash config prompt and
# verify the functionality
#############################################################################

def auditlogging_reset_test(session, output_file, total_cmds_executed, total_cmds_passed, total_cmds_failed):
    cmd_output = functions_potash.execute_cmd(session, "configure terminal")
    output_file.write(cmd_output)
    print cmd_output

    cmd_output = functions_potash.execute_cmd(session, "audit-logging enable")
    output_file.write(cmd_output)
    print cmd_output

    cmd_output = functions_potash.execute_cmd(session, "audit-logging reset")
    output_file.write(cmd_output)
    print cmd_output

    cmd_output = functions_potash.execute_cmd(session, "end")
    output_file.write(cmd_output)
    print cmd_output

    cmd_output = functions_potash.execute_cmd(session, "show audit")
    output_file.write(cmd_output)
    print cmd_output

    if ("INFO: Audit: AUDIT LOG file clear SUCCESS" in cmd_output):
        total_cmds_passed = total_cmds_passed + 1
        result = "\n" + " AUDITLOGGING RESET TEST" + "=Passed\n" + "\nPASSED\n"
    else:
        total_cmds_failed = total_cmds_failed + 1
        result = "\n" + " AUDITLOGGING RESET TEST" + "=Failed=" + "Failed in Output Validation\n" + "\nFAILED\n"
    output_file.write(result)

    return_value = functions_potash.execute_exit_cmd(session, "exit")
    output_file.write(return_value)

    return(total_cmds_passed, total_cmds_failed)


#############################################################################
# auditlogging_enable_test
# Execute 'audit-logging enable' from Potash CLI Config prompt
# and verify the functionality
#############################################################################
def auditlogging_enable_test(session, output_file, total_cmds_executed, total_cmds_passed, total_cmds_failed):
    cmd_output = functions_potash.execute_cmd(session, "configure terminal")
    output_file.write(cmd_output)
    print cmd_output

    cmd_output = functions_potash.execute_cmd(session, "audit-logging enable")
    output_file.write(cmd_output)
    print cmd_output

    cmd_output = functions_potash.execute_cmd(session, "end")
    output_file.write(cmd_output)
    print cmd_output

    cmd_output = functions_potash.execute_cmd(session, "show audit")
    output_file.write(cmd_output)
    print cmd_output

    if (("INFO: Audit:OneView Logging out ...! SUCCESS SSH" in cmd_output) and
        ("INFO: Audit:OneView Logging in ...! SUCCESS SSH" in cmd_output) and
            ("INFO: Audit: AUDIT LOG file clear SUCCESS" in cmd_output)):
        total_cmds_passed = total_cmds_passed + 1
        result = "\n" + " AUDITLOGGING ENABLE TEST" + "=Passed\n" + "\nPASSED\n"
    else:
        total_cmds_failed = total_cmds_failed + 1
        result = "\n" + " AUDITLOGGING ENABLE TEST" + "=Failed=" + "Failed in Output Validation\n" + "\nFAILED\n"
    output_file.write(result)

    return(total_cmds_passed, total_cmds_failed)


#############################################################################
# auditlogging_disable_test
# Execute 'audit-logging disable' from Potash CLI config prompt
# and verify the functionality
#############################################################################
def auditlogging_disable_test(session, output_file, total_cmds_executed, total_cmds_passed, total_cmds_failed):
    cmd_output = functions_potash.execute_cmd(session, "configure terminal")
    output_file.write(cmd_output)
    print cmd_output

    cmd_output = functions_potash.execute_cmd(session, "audit-logging reset")
    output_file.write(cmd_output)
    print cmd_output

    cmd_output = functions_potash.execute_cmd(session, "audit-logging disable")
    output_file.write(cmd_output)
    print cmd_output

    cmd_output = functions_potash.execute_cmd(session, "end")
    output_file.write(cmd_output)
    print cmd_output

    cmd_output = functions_potash.execute_cmd(session, "show audit")
    output_file.write(cmd_output)
    print cmd_output

    return_value = functions_potash.execute_exit_cmd(session, "exit")
    output_file.write(return_value)

    session = functions_potash.ssh_connect(UserInput.POTASHIP, UserInput.USERNAME, UserInput.PASSWORD)

    cmd_output = functions_potash.execute_cmd(session, "show audit")
    output_file.write(cmd_output)
    print cmd_output

    if (("INFO: Audit:OneView Logging out ...! SUCCESS SSH" not in cmd_output) and
            ("INFO: Audit:OneView Logging in ...! SUCCESS SSH" not in cmd_output)):
        total_cmds_passed = total_cmds_passed + 1
        result = "\n" + " AUDITLOGGING DISABLE TEST" + "=Passed\n" + "\nPASSED\n"
    else:
        total_cmds_failed = total_cmds_failed + 1
        result = "\n" + " AUDITLOGGING DISABLE TEST" + "=Failed=" + "Failed in Output Validation\n" + "\nFAILED\n"
    output_file.write(result)

    return(total_cmds_passed, total_cmds_failed, session)


#############################################################################
# execute_tests
# - Main routine from where all the tests gets executed
#############################################################################
def execute_tests():
    ExecutionOutput = "../AUTOMATION_RESULTS/" + "ExecutionOutput_AUDITLOGGING.txt"
    output_file = open(ExecutionOutput, "w")
    session = functions_potash.ssh_connect(UserInput.POTASHIP, UserInput.USERNAME, UserInput.PASSWORD)

    total_cmds_executed = 0
    total_cmds_passed = 0
    total_cmds_failed = 0

    output_file.write(spaces + "AUDITLOGGING FUNCTIONAL TESTS" + spaces)

    cmd_output = functions_potash.execute_cmd(session, "show firmware version")
    output_file.write(cmd_output)

    output_file.write(spaces + "\n")
    total_cmds_passed, total_cmds_failed = auditlogging_reset_test(session, output_file, total_cmds_executed, total_cmds_passed, total_cmds_failed)
    output_file.write(spaces + "\n")

    session = functions_potash.ssh_connect(UserInput.POTASHIP, UserInput.USERNAME, UserInput.PASSWORD)
    total_cmds_passed, total_cmds_failed = auditlogging_enable_test(session, output_file, total_cmds_executed, total_cmds_passed, total_cmds_failed)
    output_file.write(spaces + "\n")

    total_cmds_passed, total_cmds_failed, session = auditlogging_disable_test(session, output_file, total_cmds_executed, total_cmds_passed, total_cmds_failed)
    output_file.write(spaces + "\n")

    functions_potash.final_output(output_file, ExecutionOutput, total_cmds_executed, total_cmds_passed, total_cmds_failed)

script_name = sys.argv[0]
if ("potash_auditlogging" in script_name):
    execute_tests()

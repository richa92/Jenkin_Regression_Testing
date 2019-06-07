#!/usr/bin/env python
###########################################################################
# functions_potash.py
# The common functions to be used for functionality testing in Potash
###########################################################################
import sys
import os
import string
import pexpect
import re
import UserInput


##########################################################################
# This function executes a Potash CLI command
# and returns output of command
# session - this is the session thats returned from ssh_connect.
# cmd     - Potash CLI command to be executed in the session.
##########################################################################
def execute_cmd(session, cmd):
    session.expect("#", 3)
    session.sendline(cmd)
    session.send("\x0D")
    session.expect([UserInput.cliPrompt, '\)# ', 'e--'])
    cmd_output = session.before + session.after
    print cmd + "\n" + cmd_output
    return cmd_output


##########################################################################
# This function executes exit CLI command in Potash and closes the session
##########################################################################
def execute_exit_cmd(session, cmd):
    session.expect("#", 3)
    session.sendline(cmd)
    session.send("\x0D")
    return cmd


##########################################################################
# This function is used to login to Potash module
# A new session is returned that should be used for executing
# and CLI command in that session.
##########################################################################
def ssh_connect(host, user, password):
    time_out = None
    ssh_cmd = "ssh -o StrictHostKeyChecking=no " + user + "@" + host
    child = pexpect.spawn(ssh_cmd)
    child.timeout = time_out
    index = child.expect(['yes/no', 'password:'])
    if index == 0:
        child.sendline('yes')
        child.expect('password:')
    child.sendline(password)
    return child


######################################################################################
# The final execution results are written to the ExecutionOutput_Feature.txt file.
# output_file - File Pointer to the output file.
######################################################################################
def final_output(output_file, executionOutputFile, total_cmds_executed, total_cmds_passed, total_cmds_failed):
    space = "\n==============================================================================\n"
    final_output = "\n\n" + space + "Automation Test Results:" + space
    output_file.write(final_output)

    tests_executed = "Total Tests/Commands Executed: " + str(total_cmds_passed + total_cmds_failed)
    tests_passed = "\nTotal Tests/Commands Passed  : " + str(total_cmds_passed)
    test_failed = "\nTotal Tests/Commands Failed  : " + str(total_cmds_failed)
    test_results = tests_executed + tests_passed + test_failed + space
    output_file.write(test_results)

    output_file.close()
    cmd = "sed -i 's/\r//g' " + executionOutputFile
    os.system(cmd)

#!/usr/bin/env python


#############################################################################
# potash_snmpv3enhancements.py
# Script for SNMPV3ENHANCEMENTS Feature Functionality Testing in Potash
#############################################################################
import string
import functions_potash
import UserInput
import sys
global spaces
spaces = "\n______________________________________________________________________________\n"


#############################################################################
# snmp_targetparams_engineid_v3auth_test
# Set SNMPV3 Target Params Table with Engineid, V3AUTH and
# verify the same
#############################################################################

def snmp_targetparams_engineid_v3auth_test(session, output_file, total_cmds_executed, total_cmds_passed, total_cmds_failed):

    cmd_output = functions_potash.execute_cmd(session, "set cli pagination off")
    output_file.write(cmd_output)
    print cmd_output

    cmd_output = functions_potash.execute_cmd(session, "show snmp engineid")
    output_file.write(cmd_output)

    engineid = cmd_output.split('EngineId:')[1].split('OneView#')[0]
    engineid = engineid.rstrip()

    cmd_output = functions_potash.execute_cmd(session, "configure terminal")
    output_file.write(cmd_output)
    print cmd_output

    cmd_output = functions_potash.execute_cmd(session, "enable snmpagent")
    output_file.write(cmd_output)
    print cmd_output

    cmd_output = functions_potash.execute_cmd(session, "snmp user user1")
    output_file.write(cmd_output)
    print cmd_output

    set_targetparams = "snmp targetparams Targetparam1 user user1 EngineID " + engineid + " security-model v3 auth message-processing v3"

    cmd_output = functions_potash.execute_cmd(session, set_targetparams)
    output_file.write(cmd_output)
    print cmd_output

    cmd_output = functions_potash.execute_cmd(session, "end")
    output_file.write(cmd_output)
    print cmd_output

    cmd_output = functions_potash.execute_cmd(session, "show snmp targetparam")
    output_file.write(cmd_output)
    print cmd_output
    targetparam_table = cmd_output.split('Targetparam1')[1].split('--------------------------')[0]

    if (("Message Processing Model : v3" in targetparam_table) and
            ("Security Model           : v3" in targetparam_table) and
            ("Security Name            : user1" in targetparam_table) and
            ("Security Level           : Authentication, No Privacy" in targetparam_table) and
            (engineid in targetparam_table)):
        total_cmds_passed = total_cmds_passed + 1
        result = "\n" + " SNMP TARGETPARAMS ENGINEID V3AUTH TEST" + "=Passed\n" + "\nPASSED\n"
    else:
        total_cmds_failed = total_cmds_failed + 1
        result = "\n" + " SNMP TARGETPARAMS ENGINEID V3AUTH TEST" + "=Failed=" + "Failed in Output Validation\n" + "\nFAILED\n"
    output_file.write(result)

    return(total_cmds_passed, total_cmds_failed)

#############################################################################
# snmp_targetparams_engineid_v3noauth_test
# Set SNMPV3 Target Params Table with Engineid, V3NOAUTH and
# verify the same
#############################################################################


def snmp_targetparams_engineid_v3noauth_test(session, output_file, total_cmds_executed, total_cmds_passed, total_cmds_failed):
    cmd_output = functions_potash.execute_cmd(session, "show snmp engineid")
    output_file.write(cmd_output)

    engineid = cmd_output.split('EngineId:')[1].split('OneView#')[0]
    engineid = engineid.rstrip()

    cmd_output = functions_potash.execute_cmd(session, "configure terminal")
    output_file.write(cmd_output)
    print cmd_output

    cmd_output = functions_potash.execute_cmd(session, "enable snmpagent")
    output_file.write(cmd_output)
    print cmd_output

    cmd_output = functions_potash.execute_cmd(session, "snmp user user1")
    output_file.write(cmd_output)
    print cmd_output

    set_targetparams = "snmp targetparams Targetparam1 user user1 EngineID " + engineid + " security-model v3 noauth message-processing v3"

    cmd_output = functions_potash.execute_cmd(session, set_targetparams)
    output_file.write(cmd_output)
    print cmd_output

    cmd_output = functions_potash.execute_cmd(session, "end")
    output_file.write(cmd_output)
    print cmd_output

    cmd_output = functions_potash.execute_cmd(session, "show snmp targetparam")
    output_file.write(cmd_output)
    print cmd_output
    targetparam_table = cmd_output.split('Targetparam1')[1].split('--------------------------')[0]

    if (("Message Processing Model : v3" in targetparam_table) and
            ("Security Model           : v3" in targetparam_table) and
            ("Security Name            : user1" in targetparam_table) and
            ("Security Level           : No Authentication, No Privacy" in targetparam_table) and
            (engineid in targetparam_table)):
        total_cmds_passed = total_cmds_passed + 1
        result = "\n" + " SNMP TARGETPARAMS ENGINEID V3AUTH TEST" + "=Passed\n" + "\nPASSED\n"
    else:
        total_cmds_failed = total_cmds_failed + 1
        result = "\n" + " SNMP TARGETPARAMS ENGINEID V3AUTH TEST" + "=Failed=" + "Failed in Output Validation\n" + "\nFAILED\n"
    output_file.write(result)

    return(total_cmds_passed, total_cmds_failed)


#############################################################################
# snmp_targetparams_engineid_v3priv_test
# Set SNMPV3 Target Params Table with Engineid, V3PRIV and
# verify the same
#############################################################################

def snmp_targetparams_engineid_v3priv_test(session, output_file, total_cmds_executed, total_cmds_passed, total_cmds_failed):
    cmd_output = functions_potash.execute_cmd(session, "show snmp engineid")
    output_file.write(cmd_output)

    engineid = cmd_output.split('EngineId:')[1].split('OneView#')[0]
    engineid = engineid.rstrip()

    cmd_output = functions_potash.execute_cmd(session, "configure terminal")
    output_file.write(cmd_output)
    print cmd_output

    cmd_output = functions_potash.execute_cmd(session, "enable snmpagent")
    output_file.write(cmd_output)
    print cmd_output

    cmd_output = functions_potash.execute_cmd(session, "snmp user user1")
    output_file.write(cmd_output)
    print cmd_output

    set_targetparams = "snmp targetparams Targetparam1 user user1 EngineID " + engineid + " security-model v3 priv message-processing v3"
    cmd_output = functions_potash.execute_cmd(session, set_targetparams)
    output_file.write(cmd_output)
    print cmd_output

    cmd_output = functions_potash.execute_cmd(session, "end")
    output_file.write(cmd_output)
    print cmd_output

    cmd_output = functions_potash.execute_cmd(session, "show snmp targetparam")
    output_file.write(cmd_output)
    print cmd_output
    targetparam_table = cmd_output.split('Targetparam1')[1].split('--------------------------')[0]

    if (("Message Processing Model : v3" in targetparam_table) and
            ("Security Model           : v3" in targetparam_table) and
            ("Security Name            : user1" in targetparam_table) and
            ("Security Level           : Authentication, Privacy" in targetparam_table) and
            (engineid in targetparam_table)):

        total_cmds_passed = total_cmds_passed + 1
        result = "\n" + " SNMP TARGETPARAMS ENGINEID V3AUTH TEST" + "=Passed\n" + "\nPASSED\n"
    else:
        total_cmds_failed = total_cmds_failed + 1
        result = "\n" + " SNMP TARGETPARAMS ENGINEID V3AUTH TEST" + "=Failed=" + "Failed in Output Validation\n" + "\nFAILED\n"
    output_file.write(result)

    return(total_cmds_passed, total_cmds_failed)


#############################################################################
# snmp_notify_notification_type_inform_test
# Test snmp notify with notification type set as INFORM and verify the same
#############################################################################

def snmp_notify_notification_type_inform_test(session, output_file, total_cmds_executed, total_cmds_passed, total_cmds_failed):
    cmd_output = functions_potash.execute_cmd(session, "configure terminal")
    output_file.write(cmd_output)
    print cmd_output

    cmd_output = functions_potash.execute_cmd(session, "enable snmpagent")
    output_file.write(cmd_output)
    print cmd_output

    cmd_output = functions_potash.execute_cmd(session, "snmp user user2")
    output_file.write(cmd_output)
    print cmd_output

    cmd_output = functions_potash.execute_cmd(session, "snmp community index com3 name hpname3 security user2")
    output_file.write(cmd_output)
    print cmd_output

    cmd_output = functions_potash.execute_cmd(session, "snmp group group2 user user2 security-model v3")
    output_file.write(cmd_output)
    print cmd_output

    cmd_output = functions_potash.execute_cmd(session, "snmp targetaddr Targetaddres1 param hp1 12.0.0.100 taglist tag1")
    output_file.write(cmd_output)
    print cmd_output

    cmd_output = functions_potash.execute_cmd(session, "snmp notify notify1 tag tag1 type inform nonvolatile")
    output_file.write(cmd_output)
    print cmd_output

    cmd_output = functions_potash.execute_cmd(session, "end")
    output_file.write(cmd_output)
    print cmd_output

    cmd_output = functions_potash.execute_cmd(session, "show snmp notif")
    output_file.write(cmd_output)
    print cmd_output
    snmp_notif = cmd_output.split('notify1')[1].split('---------------------------')[0]

    if (("Notify Tag   : tag1" in snmp_notif) and
            ("Notify Type  : inform" in snmp_notif) and
            ("Storage Type : Nonvolatile" in snmp_notif)):

        total_cmds_passed = total_cmds_passed + 1
        result = "\n" + " SNMP TARGETPARAMS ENGINEID V3AUTH TEST" + "=Passed\n" + "\nPASSED\n"
    else:
        total_cmds_failed = total_cmds_failed + 1
        result = "\n" + " SNMP TARGETPARAMS ENGINEID V3AUTH TEST" + "=Failed=" + "Failed in Output Validation\n" + "\nFAILED\n"
    output_file.write(result)

    return(total_cmds_passed, total_cmds_failed)


#############################################################################
# execute_tests
# - Main routine from where all the tests gets executed
#############################################################################
def execute_tests():
    ExecutionOutput = "../AUTOMATION_RESULTS/" + "ExecutionOutput_SNMPV3ENHANCEMENTS.txt"
    output_file = open(ExecutionOutput, "w")
    session = functions_potash.ssh_connect(UserInput.POTASHIP, UserInput.USERNAME, UserInput.PASSWORD)

    total_cmds_executed = 0
    total_cmds_passed = 0
    total_cmds_failed = 0

    output_file.write(spaces + "SNMPV3ENHANCEMENTS FUNCTIONAL TESTS" + spaces)

    cmd_output = functions_potash.execute_cmd(session, "show firmware version")
    output_file.write(cmd_output)

    output_file.write(spaces + "\n")
    total_cmds_passed, total_cmds_failed = snmp_targetparams_engineid_v3auth_test(session, output_file, total_cmds_executed, total_cmds_passed, total_cmds_failed)
    output_file.write(spaces + "\n")

    total_cmds_passed, total_cmds_failed = snmp_targetparams_engineid_v3noauth_test(session, output_file, total_cmds_executed, total_cmds_passed, total_cmds_failed)
    output_file.write(spaces + "\n")

    total_cmds_passed, total_cmds_failed = snmp_targetparams_engineid_v3priv_test(session, output_file, total_cmds_executed, total_cmds_passed, total_cmds_failed)
    output_file.write(spaces + "\n")

    total_cmds_passed, total_cmds_failed = snmp_notify_notification_type_inform_test(session, output_file, total_cmds_executed, total_cmds_passed, total_cmds_failed)
    output_file.write(spaces + "\n")

    functions_potash.final_output(output_file, ExecutionOutput, total_cmds_executed, total_cmds_passed, total_cmds_failed)

script_name = sys.argv[0]
if ("potash_snmpv3enhancements" in script_name):
    execute_tests()

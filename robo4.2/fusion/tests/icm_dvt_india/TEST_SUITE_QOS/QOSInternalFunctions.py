#!/usr/bin/env python

###########################################################################
# QOSInternalFunctions.py
# All the Internal functions required for QOS feature are defined here
###########################################################################
import sys
import string
import paramiko
import time


def ssh_connect_paramiko(host, user, password):
    print (host + user + password)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=user, password=password, port=22)
    time.sleep(5)
    return ssh


def execute_cmd(ssh, cmd):
    channel = ssh.invoke_shell()
    time.sleep(5)
    channel.send("set cli pagination off\n")
    time.sleep(2)
    channel.send(cmd)
    time.sleep(4)
    cmd_output = channel.recv(8000)
    print cmd_output
    return cmd_output


def QOS_CLI_Verification(ssh, qosconfig, interface):

    fail_flag = "0"
    classes = [0, 1, 2, 3, 4, 5, 6, 7]

    show_ets_global_output = execute_cmd(ssh, "show ets global info\n")

    if (("ETS Admin Configuration Mode  : QOS" not in show_ets_global_output) or
            ("ETS Oper Configuration Mode   : QOS" not in show_ets_global_output)):
        print "CLI Verification Failed :  show ets global info did not produce expected output"
        fail_flag = "1"

    for qosConfiguration_key, qosConfiguration_value in qosconfig.iteritems():
        print qosConfiguration_key
        print qosConfiguration_value

        for activeQosConfig_key, activeQosConfig_value in qosConfiguration_value.iteritems():
            if ("activeQosConfig" in activeQosConfig_key):
                print "Retrieved activeQosConfig value "

                for qosTrafficClassifiers_key, qosTrafficClassifiers_value in activeQosConfig_value.iteritems():
                    if ("qosTrafficClassifiers" in qosTrafficClassifiers_key):
                        print ("Retrieved qosTrafficClassifiers value")

                        for index in classes:
                            for key, value in qosTrafficClassifiers_value[index].iteritems():
                                if ("qosTrafficClass" in key):
                                    print ("Retrieved qosTrafficClass")
                                    qosTrafficClass_value = value

                                    for bandwidthShare_key, bandwidthShare_value in qosTrafficClass_value.iteritems():
                                        if ("bandwidthShare" in bandwidthShare_key):
                                            print (bandwidthShare_value)
                                            if index == 0:
                                                class0 = bandwidthShare_value
                                            if (index == 1):
                                                class1 = bandwidthShare_value
                                            if (index == 2):
                                                class2 = bandwidthShare_value
                                            if (index == 3):
                                                class3 = bandwidthShare_value
                                            if (index == 4):
                                                class4 = bandwidthShare_value
                                            if (index == 5):
                                                class5 = bandwidthShare_value
                                            if (index == 6):
                                                class6 = bandwidthShare_value
                                            if (index == 7):
                                                class7 = bandwidthShare_value

    print ("Bandwidth for 7 classes : " + class0 + class1 + class2 + class3 + class4 + class5 + class6 + class7)

    show_priority_grouping_cmd = "show interface " + interface + " priority-grouping detail\n"
    show_priority_grouping_output = execute_cmd(ssh, show_priority_grouping_cmd)

    ets_local_port_info = show_priority_grouping_output.split('ETS Local Port Info')[1].split('Willing Status           :Disabled')[0]
    split_ets_local = ets_local_port_info.split('\n')

    print "\n ETS Locat Port Info : "
    print ets_local_port_info
    print ("\n split_ets_local Values " + split_ets_local[4] + split_ets_local[5] + split_ets_local[6] + split_ets_local[7])
    print (split_ets_local[8] + split_ets_local[9] + split_ets_local[10] + split_ets_local[11])

    if ((class0 in split_ets_local[4]) and
            (class1 in split_ets_local[5]) and
            (class2 in split_ets_local[6]) and
            (class3 in split_ets_local[7]) and
            (class4 in split_ets_local[8]) and
            (class5 in split_ets_local[9]) and
            (class6 in split_ets_local[10]) and
            (class7 in split_ets_local[11])):
        print "CLI Verification - Expected output retrieved from ETS Local Port Info cmd "
    else:
        print "CLI Verification Failed - Did not receive expected output from ETS Local Port Info cmd"
        fail_flag = "1"

    ets_admin_port_info = show_priority_grouping_output.split('ETS Admin Port Info')[1].split('Willing Status           :Disabled')[0]
    split_ets_admin = ets_admin_port_info.split('\n')

    print "\n split_ets_admin : "
    print split_ets_admin
    print ("\n split_ets_admin Values " + split_ets_admin[4] + split_ets_admin[5] + split_ets_admin[6] + split_ets_admin[7])
    print (split_ets_admin[8] + split_ets_admin[9] + split_ets_admin[10] + split_ets_admin[11])

    if ((class0 in split_ets_admin[4]) and
            (class1 in split_ets_admin[5]) and
            (class2 in split_ets_admin[6]) and
            (class3 in split_ets_admin[7]) and
            (class4 in split_ets_admin[8]) and
            (class5 in split_ets_admin[9]) and
            (class6 in split_ets_admin[10]) and
            (class7 in split_ets_admin[11])):
        print "CLI Verification - Expected output retrieved from ETS Admin Port Info cmd "
    else:
        print "CLI Verification Failed - Did not receive expected output from ETS Admin Port Info cmd"
        fail_flag = "1"

    return fail_flag

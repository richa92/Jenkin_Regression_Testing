#!/usr/local/bin/python
import warnings
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    import paramiko
import logging
import sys
import tempfile
import os
import re
import time
import string
import threading
from os import write
libLogger = "api-logger"
from robot.libraries.BuiltIn import BuiltIn


def validate_total_samples(port_no, output, total_samples):
    list_val = [output['portStatistics'][i] for i in range(len(output['portStatistics'])) if output['portStatistics'][i]['portName'] == port_no]
    keys_list = ['receiveKilobytesPerSec', 'transmitKilobytesPerSec', 'receivePacketsPerSec', 'transmitPacketsPerSec']
    return_output = {}
    s = []
    for i in keys_list:
        attr_values = list_val[0]['advancedStatistics'][i].split(':')
        print attr_values
        if len(attr_values) != int(total_samples):
            return False, " Failed to verify the number of samples, it is not matching with the expected number of samples"
        else:
            return_output[i] = list_val[0]['advancedStatistics'][i].split(':')
    return True, return_output


def validate_total_samples_lower_version(port_no, output, total_samples):
    list_val = [output['portStatistics'][i] for i in range(len(output['portStatistics'])) if output['portStatistics'][i]['portName'] == port_no]
    keys_list = ['receiveKilobytesPerSec', 'transmitKilobytesPerSec', 'receivePacketsPerSec', 'transmitPacketsPerSec']
    return_output = {}
    s = []
    attr_values = list_val[0]['advancedStatistics']
    print attr_values
    if attr_values is not None:
        return False, " Statistics data available for lower version"
    else:
        return_output = list_val[0]['advancedStatistics']
    return True, return_output


def vaildate_port_statistics(port_no, output, total_samples):
    list_val = [output['portStatistics'][i] for i in range(len(output['portStatistics'])) if output['portStatistics'][i]['portName'] == port_no]
    keys_list = ['receiveKilobytesPerSec', 'transmitKilobytesPerSec', 'receivePacketsPerSec', 'transmitPacketsPerSec']
    return_output = {}

    for i in keys_list:
        s = []
        attr_values = list_val[0]['advancedStatistics'][i].split(':')
        print attr_values
        for x in attr_values:
            if int(x) == 0:
                s.append(int(x))
                print s
                print len(s)
        if len(attr_values) == len(s) and len(attr_values) == int(total_samples):
            return_output[i] = list_val[0]['advancedStatistics'][i].split(':')
        else:
            return False, " Failed to verify the number of samples, it is not matching with the expected number of samples"
    return True, return_output


def vaildate_port_statistics_after_passing_traffic(port_no, output, total_samples, expected_samples):
    list_val = [output['portStatistics'][i] for i in range(len(output['portStatistics'])) if output['portStatistics'][i]['portName'] == port_no]
    keys_list = ['receiveKilobytesPerSec', 'transmitKilobytesPerSec', 'receivePacketsPerSec', 'transmitPacketsPerSec']
    return_output = {}

    for i in keys_list:
        s = []
        attr_values = list_val[0]['advancedStatistics'][i].split(':')
        print attr_values
        for x in attr_values:
            if int(x) != 0:
                s.append(int(x))
                print len(s)
        if len(attr_values) == len(s) and len(attr_values) == int(total_samples):
            return False, " Failed to verify the number of samples, it is not matching with the expected number of samples"
        else:
            return_output[i] = list_val[0]['advancedStatistics'][i].split(':')
    return True, return_output


def start_traffic(ip, username, password, wcmd):
    io_thread = threading.Thread(target=execute_windows_commands, args=(ip, username, password, wcmd))
    io_thread.start()


def execute_windows_commands(ip, username, passwd, wcmd):
    '''
    Execute any windows commands
    '''
    try:
        build_cmd = "psexec \\\\" + ip + " -u " + username + " -p " + passwd + " " + wcmd
        output = os.system(build_cmd)
        return output
    except Exception as e:
        return e

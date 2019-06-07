
'''
This module contains the code to get the IP's of the
ethernet networks. Using the IP's it can login to the
server and execute the diskspd commands to start the traffic.
Diskspd results or ouput will be redirected to the log file

'''

import paramiko
import os
import time
import re
import threading
import Queue


def execute_diskspd(ip, username, passwd, diskspd_cmd):
    '''
    Execute the diskSPD tool Command
    '''
    try:
        single_cmd = "psexec \\\\" + ip + " -u " + username + " -p " + passwd + " " +\
            diskspd_cmd
        output = os.system(single_cmd)
        return (output)
    except Exception as e:
        return (e)


def validate_windows_lun_count(ip, username, passwd, diskspd_cmd):
    output = execute_diskspd(ip,
                             username, passwd, diskspd_cmd)
    with open("C:\\WINDOWSLUN.txt") as f:
        lines = f.readlines()
        print lines
        count = 0
        for i in lines:
            if "3PARdata" in i:
                count = count + 1
                print count
        return count

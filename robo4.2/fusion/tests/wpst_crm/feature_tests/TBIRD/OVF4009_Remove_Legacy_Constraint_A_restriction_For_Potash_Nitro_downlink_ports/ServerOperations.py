'''
This module contains the code to get the IP's of the
ethernet networks. Using the IP's it can login to the
server and execute the diskspd commands to start the traffic.
Diskspd results or ouput will be redirected to the log file

'''


import os
import paramiko
import re


def execute_windows_commands(ip, username, passwd, wcmd):
    '''
    Execute the diskSPD tool Command
    '''
    try:
        single_cmd = "C:\\PSTools\\PSTools\\PSExec \\\\" + ip + " -u " + username + " -p " + passwd + " " + \
                     wcmd
        print single_cmd
        output = os.system(single_cmd)
        return (output)
    except Exception as e:
        return (e)

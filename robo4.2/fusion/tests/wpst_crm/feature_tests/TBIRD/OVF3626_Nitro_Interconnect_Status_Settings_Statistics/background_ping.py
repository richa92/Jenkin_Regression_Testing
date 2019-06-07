import time
import re
import os
import threading


def execute_windows_commands(ip, username, passwd, wcmd):
    '''
    Execute any windows commands using psexec
    '''
    try:
        build_cmd = "psexec \\\\" + ip + " -u " + username + " -p " + passwd + " " + wcmd
        output = os.system(build_cmd)
        return output
    except Exception as e:
        return e


def execute_traffic(ip, username, passwd, wcmd):
    io_thread = threading.Thread(target=execute_windows_commands, args=(ip, username, passwd, wcmd))
    io_thread.start()
